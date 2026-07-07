import subprocess
import sys

# Read the valid files from guard_check.py output
try:
    output = subprocess.check_output(['python3', 'scripts/guard_check.py'], text=True)
    files = [line.strip() for line in output.splitlines() if line.strip() and not line.startswith('Reverting')]
except Exception as e:
    print(f"Error running guard_check: {e}")
    sys.exit(1)

batch_size = 20
for i in range(0, len(files), batch_size):
    batch = files[i:i+batch_size]
    print(f"Committing batch {i//batch_size + 1} ({len(batch)} files)...")
    
    # Add files
    subprocess.call(['git', 'add'] + batch)
    
    # Commit
    first_file = batch[0].split('/')[-1]
    commit_msg = f"chore(milnor): drain batch (H1-H8) starting with {first_file}"
    subprocess.call(['git', 'commit', '-m', commit_msg])

print("Finished batch commits.")
