import subprocess
import sys
import os

def compile_production_site():
    print("=" * 60)
    print("   pyMachDM: Compiling Production Static Website Files   ")
    print("=" * 60)
    
    venv_mkdocs = os.path.join(".venv", "Scripts", "mkdocs") if os.name == "nt" else os.path.join(".venv", "bin", "mkdocs")
    cmd = [venv_mkdocs, "build"] if os.path.exists(venv_mkdocs) else ["mkdocs", "build"]
    
    try:
        subprocess.run(cmd, check=True)
        print("\n[SUCCESS] Compilation complete! Production ready inside /site folder.")
    except Exception as e:
        print(f"\n[ERROR] Build pipeline encountered a problem: {e}")
        sys.exit(1)

if __name__ == "__main__":
    compile_production_site()