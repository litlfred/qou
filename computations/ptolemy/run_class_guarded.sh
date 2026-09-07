#!/usr/bin/env bash
# Run one class with a DISK GUARD.  This container is a ~38G quota with mathlib (4G)
# and .git (7.3G) resident; it reached 44K free twice today, the state where the
# harness cannot write its own output and every command fails.  An unguarded solve
# that spills to disk takes the whole session down, so watch free space and kill the
# solve -- not the container -- if it drops below the floor.
set -uo pipefail
NAME="${1:-L6a4}"; K="${2:-2}"; CAP="${3:-25}"; BUDGET="${4:-4800}"
WALL="${5:-5400}"; FLOOR_MB="${6:-700}"; LOG="/tmp/sweep_${NAME}_c${K}.log"
FLOOR_KB=$((FLOOR_MB*1024))
cd /home/user/qou/computations/ptolemy
nohup timeout "$WALL" python3 -u ptolemy_class_sweep.py "$NAME" "$K" "$CAP" "$BUDGET" > "$LOG" 2>&1 &
RUN=$!
echo "started pid $RUN on $NAME c$K; floor ${FLOOR_MB} MB; log $LOG"
while kill -0 "$RUN" 2>/dev/null; do
  FREE=$(df -k / | awk 'NR==2 {print $4}')
  if [ "$FREE" -lt "$FLOOR_KB" ]; then
    echo "DISK GUARD FIRED: ${FREE}K free < ${FLOOR_KB}K -- killing the solve"
    pkill -P "$RUN" 2>/dev/null; kill "$RUN" 2>/dev/null
    for p in $(pgrep -x msolve); do kill "$p" 2>/dev/null; done
    echo "GUARD_KILL" >> "$LOG"
    break
  fi
  sleep 20
done
echo "watcher done; free now $(df -h / | awk 'NR==2 {print $4}')"
