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
# WHAT THIS DOES *NOT* COVER, corrected the same day it was written.
#
# It was written for "the run died at 11:38:02 on a session resume and was
# noticed 20 minutes later", and it does NOT close that. A container recycle
# kills this supervisor too -- measured: at 12:25 both the table and this
# script were gone. A supervisor inside the thing being supervised cannot
# outlive it.
#
# The mechanism that actually survives a recycle is the SessionStart hook,
# scripts/session-start-coord-sweep.sh, which now reports the table's state as
# its first line. This still earns its place for the other failure: a run that
# dies while the container lives.
set -uo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
while true; do
  "$ROOT/scripts/hkt-resume.sh" --commit >>"$ROOT/.work/hkt-supervise.log" 2>&1
  sleep 120
done
