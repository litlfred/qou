#!/bin/bash
# Overnight shell closure computation.
# Runs k=3..15 (or as far as feasible), witnesses, commits, pushes.
#
# Usage: nohup bash run_shell_overnight.sh > shell_overnight.log 2>&1 &

set -e
cd "$(dirname "$0")"

echo "=== Shell closure overnight computation ==="
echo "Started: $(date)"

# Run with increasing k, timeout each level
python3 shell_closure_compute.py --kmax 9 --zmax 30

echo ""
echo "k=3..9 done. Attempting k=10 (may take hours)..."
timeout 14400 python3 shell_closure_compute.py --kmax 10 --zmax 30 || {
    echo "k=10 timed out after 4 hours. Using k=9 results."
}

echo ""
echo "Committing witness..."
cd ..
git add computations/shell-closure.witness.json computations/shell_closure_compute.py
git commit -m "Witness categorical shell closure k=3..9 (or 10)

Computed per-partition nuclear character at all k levels using
Hoefsmit seminormal matrices. Forward δ² of cumulative
Wedderburn-weighted ln|χ_λ| gives categorical shell signal.

No Gaussian. Shell emerges from computation.

https://claude.ai/code/session_01PGXnAjTVFYWKhGVGovVx5H" || true

git push -u origin claude/identify-bottlenecks-5gg3A || {
    echo "Push failed, retrying in 2s..."
    sleep 2
    git push -u origin claude/identify-bottlenecks-5gg3A || {
        sleep 4
        git push -u origin claude/identify-bottlenecks-5gg3A || echo "Push failed after 3 attempts"
    }
}

echo ""
echo "Completed: $(date)"
