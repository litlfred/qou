import subprocess
import sys

print("Running split_amalgamated.py to restore Milnor rewrites...")
try:
    subprocess.check_call(['python3', 'scripts/split_amalgamated.py'])
except Exception as e:
    print(f"Error running split_amalgamated: {e}")
    sys.exit(1)

try:
    output = subprocess.check_output(['git', 'status', '--porcelain', 'content/quantum-observable-universe'], text=True)
except Exception as e:
    print(f"Error getting git status: {e}")
    sys.exit(1)

files = []
for line in output.splitlines():
    filepath = line[3:].strip()
    if filepath.endswith('.md') or filepath.endswith('.ts') or filepath.endswith('.qa.json'):
        files.append(filepath)

if not files:
    print("No modified files to commit.")
    sys.exit(0)

batch_size = 20
print(f"Found {len(files)} files to commit. Committing in batches of {batch_size}...")

for i in range(0, len(files), batch_size):
    batch = files[i:i+batch_size]
    print(f"Committing batch {i//batch_size + 1} ({len(batch)} files)...")
    subprocess.check_call(['git', 'add'] + batch)
    first_file = batch[0].split('/')[-1]
    commit_msg = f"chore(milnor): drain batch (H1-H8) starting with {first_file}"
    subprocess.check_call(['git', 'commit', '-m', commit_msg])

print("Finished manual batch commits.")
