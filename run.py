import subprocess
import sys
import os

def launch_local_server():
    print("=" * 60)
    print("   pyMachDM: Launching Academic Website Dev Server Locally   ")
    print("=" * 60)
    
    # Force use of the local virtual environment's executable 
    venv_mkdocs = os.path.join(".venv", "Scripts", "mkdocs") if os.name == "nt" else os.path.join(".venv", "bin", "mkdocs")
    
    # Fallback to standard command if venv is missing
    cmd = [venv_mkdocs, "serve"] if os.path.exists(venv_mkdocs) else ["mkdocs", "serve"]
    
    try:
        subprocess.run(cmd, check=True)
    except KeyboardInterrupt:
        print("\n[INFO] Local dev server safely terminated by user.")
    except Exception as e:
        print(f"\n[ERROR] Failed to run server: {e}")
        sys.exit(1)

if __name__ == "__main__":
    launch_local_server()