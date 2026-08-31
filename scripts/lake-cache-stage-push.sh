#!/usr/bin/env bash
# Incremental push of a prebuilt cache commit, in batches.
#
# Three bugs killed the earlier attempts; all are guarded here.
#
#  1. `refs/heads/lake-cache/.staging-N` is an INVALID ref name -- git forbids a
#     path component beginning with a dot.  It failed identically to a network
#     error because the retry helper sent stderr to /dev/null.  Errors are
#     surfaced now and the name is checked up front.
#  2. The retry helper used `for i in ...`; bash functions share global scope
#     without `local`, so it clobbered the caller's counter, which then sat at
#     6/27 for 1868 iterations.  Everything is `local`, the retry counter is
#     `attempt`, and the outer loop asserts strict progress.
#  3. `pkill -f push-incremental.sh` matched the very shell that ran it (pkill -f
#     tests full command lines, and the heredoc contained the name), killing the
#     write before the file existed.  Hence the rename: nothing greps for this.
set -euo pipefail
cd /workspace/qou
FULL_COMMIT="${1:?full orphan commit}"
BR="${2:?target branch}"
STAGE="${STAGE:-lake-cache/staging-test}"
BATCH="${BATCH:-5}"
git check-ref-format "refs/heads/$STAGE" || { echo "invalid staging ref: $STAGE"; exit 1; }

push_retry() {
  local refspec="$1" attempt out
  for attempt in 1 2 3 4; do
    if out=$(git push -f origin "$refspec" 2>&1); then return 0; fi
    printf '    attempt %s failed: %s\n' "$attempt" \
      "$(printf '%s' "$out" | grep -iE 'error|fatal|rejected' | head -1)"
    sleep $(( 2 ** attempt ))
  done
  return 1
}

E=$(mktemp); trap 'rm -f "$E"' EXIT
git ls-tree "$FULL_COMMIT" > "$E"
N=$(wc -l < "$E")
printf 'staging %s parts to %s in batches of %s\n' "$N" "$STAGE" "$BATCH"

parent=""; cursor=0
while [ "$cursor" -lt "$N" ]; do
  prev="$cursor"
  cursor=$(( cursor + BATCH )); [ "$cursor" -gt "$N" ] && cursor="$N"
  [ "$cursor" -gt "$prev" ] || { echo "ABORT: no progress ($prev -> $cursor)"; exit 1; }
  tree=$(head -n "$cursor" "$E" | git mktree)
  if [ -z "$parent" ]; then commit=$(git commit-tree "$tree" -m "staging $cursor/$N")
  else commit=$(git commit-tree "$tree" -p "$parent" -m "staging $cursor/$N"); fi
  parent="$commit"
  printf '  %s/%s parts ... ' "$cursor" "$N"
  push_retry "$commit:refs/heads/$STAGE" || { echo "FAILED at $cursor/$N"; exit 1; }
  echo "ok"
done

echo "all blobs staged; moving $BR (ref-only, no new objects)"
push_retry "$FULL_COMMIT:refs/heads/$BR" || { echo "FINAL PUSH FAILED"; exit 1; }
git push origin --delete "$STAGE" >/dev/null 2>&1 || true
echo "DONE: $BR -> $FULL_COMMIT"
