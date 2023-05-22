import os
import subprocess
import os
os.chdir('modules')

ruta_scripts = r"D:\Trabajo\Codigos\Videos Automaticos\modules"

# Ejecutamos los scripts
scripts = ["writetext.py", "removeletters.py", "loquendo.py", "changeloquendo.py", "uplodadanddownload.py", "audacityauto.py", "replyup.py", "srtauto.py", "movetrash.py"]

for script in scripts:
    answer = input(f"\nDo you want to run {script}? (y/n/cancel):\n")
    if answer.lower() == "y":
        script_path = os.path.join(ruta_scripts, script)
        result = subprocess.run(["python", script_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if result.returncode == 0:
            print(f"{script} completed successfully\n")
        else:
            print(f"{script} failed with error code:\n", result.returncode)
    elif answer.lower() == "cancel":
        print(f"Execution cancelled by user, stopping at {script}\n")
        break
    else:
        print(f"{script} skipped\n")
