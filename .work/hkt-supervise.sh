#!/usr/bin/env bash
# Poll-restart the hadron knot table after a container suspend.
#
# scripts/hkt-resume.sh is idempotent: it refuses to start a second producer
# when one is already running (it matches `^python3 computations/
# hadron_knot_table.py` in `ps -eo cmd`), and it gates on the mpfr LP kernel
# before starting at all. So calling it on a timer is safe, and turns "the
# box suspended and the run sat dead until somebody looked" into "the run
# restarts within one poll".
#
# 2026-09-13: the run died at 11:38:02 on a session resume and was noticed 20
# minutes later, by hand. That is the failure this closes. Per-atom
# checkpointing means a reset costs only the atom in flight -- but only if
# something restarts it.
set -uo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
while true; do
  "$ROOT/scripts/hkt-resume.sh" --commit >>"$ROOT/.work/hkt-supervise.log" 2>&1
  sleep 120
done
