import click
import json
import logging
import os
import suite2p


@click.command()
@click.option('-i', '--input', 'fish_abs_path', default="data/AG_cntnap257_spontaneous_20220324_fish11_2Hz_range245_step5_exposure10_power70/", help="Absolute path to the directory with .tif files.")
@click.option('-o', '--output', 'output_directory', default="suite2p_AG_cntnap257_spontaneous_20220324_fish11_2Hz_range245_step5_exposure10_power70/", help="Absolute path to this fish's individual output folder.")
@click.option('-c', '--config', 's2p_config_json', default="ops_1P_whole.json", help="Path to a JSON file containing ops for Suite2P.")
@click.option('--log-level', default='INFO', help='Set the logging level (e.g., DEBUG, INFO, WARNING, ERROR, CRITICAL)')
def main(fish_abs_path, output_directory, s2p_config_json, log_level):
    logging.basicConfig(level=getattr(logging, log_level.upper(), None))
    logging.info(f"Logging level set to {log_level}")
    
    with open(s2p_config_json, 'r') as fp:
        input_ops = json.load(fp)

    ops = suite2p.default_ops()
    ops.update(input_ops)
    logging.debug(ops)

    db = {
        'look_one_level_down': True,
        'data_path': [fish_abs_path],
        'fast_disk': os.path.join(
            os.path.dirname(output_directory),
            f'data/registered_binary/{os.path.basename(fish_abs_path)}'),
        'save_folder': output_directory,
    }
    logging.debug(db)

    logging.info("Running Suite2P...")
    suite2p.run_s2p(ops=ops, db=db)


if __name__ == '__main__':
    main()
