#!/usr/bin/env bash
# L6a4 obstruction class 2, end to end, under caps sized to THIS container.
#
# Three prior attempts produced no verdict and none failed on the mathematics:
# each died when the filesystem filled.  The caps below are sized from measurement
# (15 GB RAM / 13 free, 4 cores, 5.0 GB disk free), and they are deliberately
# ASYMMETRIC, because the two resources fail differently:
#
#   ulimit -v 10 GB  -- generous.  Memory exhaustion is survivable: the kernel
#                       kills the process and the session continues.
#   ulimit -f  1 GB  -- tight, and the one that matters.  Disk exhaustion is NOT
#                       survivable from inside the session: the harness cannot
#                       write a child's stdout, so every command fails including
#                       the rm that would fix it.  A runaway .res cannot be
#                       allowed to eat the 5.0 GB of headroom the container has.
#
# BUDGET.  The driver's own measured note: class 1 settles mod p in 373 s, over Q
# in 713 s, and classes 2/3/4 ALL exceeded 900 s mod p.  So 900 is known-insufficient
# and the default 1200 is barely above it; 3000 s gives class 2 real room.
#
# SOUNDNESS.  This driver re-imposes the non-zero condition only on the SURVIVING
# variables, so by its own docstring it does not restore it by construction --
# "Never report a solution from this driver that has not round-tripped."  A dimension
# and degree from here are therefore PROVISIONAL until ptolemy_exact_character.py
# lifts a point and evaluates snappy's ORIGINAL equations.
ulimit -v 10485760
ulimit -f 2097152
cd "$(dirname "$0")"
echo "caps: -v $(ulimit -v) KB  -f $(ulimit -f) blocks | disk $(df -h / | awk 'NR==2{print $4}') | start $(date -u +%FT%TZ)"
timeout 3300 python3 -u ptolemy_class_sweep.py L6a4 2 25 3000 3
echo "exit=$? end=$(date -u +%FT%TZ) disk=$(df -h / | awk 'NR==2{print $4}')"
