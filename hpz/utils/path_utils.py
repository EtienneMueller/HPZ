import os
import subprocess

def check_and_download_path(file_path):
    if file_path.startswith("/projects/proj-5160_scott_lab-1128.4.503/"):
        
        out_file = os.path.join(os.getcwd(), "data")
        if not os.path.exists(out_file):
            os.makedirs(out_file)
        
        subprocess.run(
            "unimelb-mf-download "
            "--overwrite "
            "--csum-check "
            "--nb-workers 4 "
            "--mf.config /home/etiennem/.Arcitecta/mflux2.cfg "
            f"--out {out_file} {file_path}",
            shell=True,
            check=True
        )
        
        return out_file + "/" + os.path.basename(file_path.rstrip('/'))
    
    else:
        return file_path
