#!/bin/bash
# Overnight run on Mac: push k as high as possible
# Uses incremental computation (k+1 builds on k)
#
# Usage:
#   cd computations
#   nohup bash run-overnight-mac.sh > overnight.log 2>&1 &
#   tail -f overnight.log

set -e
echo "Starting overnight computation at $(date)"

# Run each level, saving results incrementally
for k in 6 7 8 9 10 11 12 13 14; do
    echo ""
    echo "========== Level k=$k at $(date) =========="
    python3 hecke_characters.py -k $k --max-z 30 -o "hecke-k${k}-overnight.json" 2>&1
    echo "Completed k=$k at $(date)"
done

echo ""
echo "Overnight computation complete at $(date)"
