import json
import os
import subprocess

def populate_git_packages():
    with open("lake-manifest.json", "r") as f:
        manifest = json.load(f)

    for pkg in manifest.get("packages", []):
        if pkg.get("type") == "git":
            name = pkg["name"]
            url = pkg["url"]
            rev = pkg["rev"]
            pkg_dir = os.path.join(".lake", "packages", name)
            
            if not os.path.exists(pkg_dir):
                os.makedirs(pkg_dir)
            
            print(f"Populating {name} from {url} at {rev} in {pkg_dir}")
            
            # Use subprocess to run git commands
            def run_git(args):
                subprocess.run(["git"] + args, cwd=pkg_dir, check=True)
            
            try:
                # If .git doesn't exist, init it
                if not os.path.exists(os.path.join(pkg_dir, ".git")):
                    run_git(["init"])
                    run_git(["remote", "add", "origin", url])
                
                # Fetch the specific revision
                run_git(["fetch", "--depth", "1", "origin", rev])
                # Checkout the files into the working tree
                run_git(["checkout", "FETCH_HEAD"])
                
            except subprocess.CalledProcessError as e:
                print(f"Failed to populate {name}: {e}")

if __name__ == "__main__":
    populate_git_packages()
