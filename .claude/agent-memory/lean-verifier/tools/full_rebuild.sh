#!/bin/bash
# Full QOU library rebuild from source, topological order, error-only failure detection.
cd /home/user/qou/content/quantum-observable-universe/lean
export LEAN_PATH=$(ls -d $PWD/.lake/build/lib/lean /home/user/qou/.lake/packages/*/.lake/build/lib/lean | tr '\n' ':')
LOG=/tmp/qou-rebuild.log; : > $LOG; ERR=/tmp/qou-rebuild-errors.txt; : > $ERR
n=0; ok=0; fail=0; t0=$(date +%s); total=$(grep -c . /tmp/full_topo.txt)
while read -r m; do
  n=$((n+1)); p=${m//./\/}; o=.lake/build/lib/lean/$p.olean; mkdir -p "$(dirname $o)"
  out=$(lean -o "$o" -i "${o%.olean}.ilean" "$p.lean" 2>&1 | grep -v "^note:")
  e=$(echo "$out" | grep -c "error")
  if [ "$e" -gt 0 ]; then fail=$((fail+1)); echo "FAIL $m ($e errors) [$n/$total]" >> $LOG; { echo "### $m"; echo "$out" | grep -A3 "error" | head -12; } >> $ERR
  else ok=$((ok+1)); [ $((n % 100)) -eq 0 ] && echo "progress $n/$total ok=$ok fail=$fail elapsed=$(( $(date +%s)-t0 ))s" >> $LOG; fi
done < /tmp/full_topo.txt
echo "DONE library: $n modules ok=$ok fail=$fail elapsed=$(( $(date +%s)-t0 ))s" >> $LOG
