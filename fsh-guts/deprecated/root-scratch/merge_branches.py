import subprocess
import sys

branches = [
    "cool-newton-ecd1hr",
    "aj-conjecture-qou-uz5m6x",
    "qbeta-wp-boundary-lean-2026-07-07",
    "qbeta-gs-net-vs-cos-ladder-2026-07-07"
]

successful_branches = []
failed_branches = []

for b in branches:
    print(f"=== Merging {b} ===")
    
    res = subprocess.run(["git", "checkout", "-b", f"local_{b}", f"origin/claude/{b}"])
    if res.returncode != 0:
        subprocess.run(["git", "checkout", f"local_{b}"])
        subprocess.run(["git", "reset", "--hard", f"origin/claude/{b}"])
    
    print(f"Rebasing {b} onto main...")
    res = subprocess.run(["git", "rebase", "main"])
    if res.returncode != 0:
        print(f"Rebase failed for {b}. Skipping.")
        subprocess.run(["git", "rebase", "--abort"])
        failed_branches.append(b)
        continue
        
    print(f"Fast-forwarding main to include {b}...")
    subprocess.run(["git", "checkout", "main"], check=True)
    res = subprocess.run(["git", "merge", "--ff-only", f"local_{b}"])
    if res.returncode != 0:
        print(f"Merge failed for {b}. Skipping.")
        failed_branches.append(b)
        continue
    
    successful_branches.append(b)

print(f"Successfully merged: {successful_branches}")
print(f"Failed to merge: {failed_branches}")
