#!/bin/bash
# Overnight run: Hecke character mass computation at k=8
# H₈(q) has 22 partitions, max dim = 70
# Expected runtime: ~1-10 min per atom, ~hours total
#
# Usage:
#   cd folio-assistant/computations
#   nohup bash run-k8-overnight.sh > k8-overnight.log 2>&1 &
#   tail -f k8-overnight.log

set -e

echo "Starting k=8 overnight computation at $(date)"
echo "H_8(q): 22 partitions, dim up to 70"
echo ""

# Light atoms first (fast)
python3 hecke_characters.py -k 8 --max-z 10 -o hecke-k8-light.json -v

# Medium atoms
python3 hecke_characters.py -k 8 --max-z 20 -o hecke-k8-medium.json

# Heavy atoms (slower)
python3 hecke_characters.py -k 8 --max-z 30 -o hecke-k8-heavy.json

echo ""
echo "Completed k=8 computation at $(date)"
echo "Results in: hecke-k8-light.json, hecke-k8-medium.json, hecke-k8-heavy.json"
