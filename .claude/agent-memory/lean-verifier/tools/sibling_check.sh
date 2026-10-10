#!/bin/bash
cd /home/user/qou/folio/quantum-observable-universe/lean
export LEAN_PATH=$(ls -d $PWD/.lake/build/lib/lean /home/user/qou/folio/unital-groebner-bases/lean/.lake/build/lib/lean /home/user/qou/.lake/packages/*/.lake/build/lib/lean | tr "\n" ":")
LOG=/tmp/qou-siblings2.log; : > $LOG; ERR=/tmp/qou-siblings2-errors.txt; : > $ERR
n=0; ok=0; fail=0; t0=$(date +%s); total=$(wc -l < /tmp/siblings.txt)
while read -r f; do
  n=$((n+1)); p="/home/user/qou/folio/quantum-observable-universe/${f#./}"
  out=$(lean "$p" 2>&1 | grep -v "^note:"); e=$(echo "$out" | grep -c "error")
  if [ "$e" -gt 0 ]; then fail=$((fail+1)); echo "FAIL ${f#./} ($e errors) [$n/$total]" >> $LOG; { echo "### ${f#./}"; echo "$out" | grep -A3 "error" | head -12; } >> $ERR
  else ok=$((ok+1)); [ $((n % 100)) -eq 0 ] && echo "progress $n/$total ok=$ok fail=$fail elapsed=$(( $(date +%s)-t0 ))s" >> $LOG; fi
done < /tmp/siblings.txt
echo "DONE siblings: $n files ok=$ok fail=$fail elapsed=$(( $(date +%s)-t0 ))s" >> $LOG
