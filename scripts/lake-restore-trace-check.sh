#!/usr/bin/env bash
# Measure whether a Lake tree's oleans carry their own `.trace` siblings, and
# set (or clear) the `.lake/RESTORED-NO-TRACES` marker accordingly.
#
# WHY THIS EXISTS (bean qou-r13s)
# --------------------------------
# Lake decides a module is up to date from its `.trace` sibling, not from the
# `.olean`. An olean with no trace is "out of date", so `lake build` rebuilds
# it -- and rebuilding EVICTS the untraced olean. Measured 2026-08-15 on a
# restored tree: `lake build QOU UGB Fred2005` took root mathlib oleans from
# 6990 to 334 in ten minutes with zero paper-library progress, silently.
#
# The restore recipe's response was to `touch .lake/RESTORED-NO-TRACES`
# UNCONDITIONALLY and tell every agent never to `lake build`. That hard-codes a
# property of the cache archive into the consumer, and the archive has since
# changed: `lake-cache/qou-v4-24-0` was reseeded 2026-08-31 with 100.0% paired
# trace coverage (6170/6172 oleans), so the marker now asserts something false
# in the blocking direction.
#
# A measurement cannot go stale the way that assertion did. Run this after a
# restore instead of touching the marker blind.
#
# COUNT PAIRED TRACES, NOT TRACES
# --------------------------------
# `total .trace files * 100 / oleans` is NOT a coverage: a Lake tree carries
# many traces that belong to no olean (`.c.o.export.trace`, `cache.trace`,
# `.tar.gz.trace`, `lake.trace`, `package-lock.json.trace`). Measured on a
# partially built qou tree: 13 oleans, 25 traces -- a naive ratio reports 192%.
# Two spellings are both valid pairings:
#     build/lib/lean/Cache/IO.olean  ->  build/lib/lean/Cache/IO.trace
#     .lake/lakefile.olean           ->  .lake/lakefile.olean.trace
#
# WHAT A HIGH COVERAGE DOES AND DOES NOT ESTABLISH
# ------------------------------------------------
# Present traces are NECESSARY for Lake to accept a restored olean. They are not
# demonstrated here to be SUFFICIENT: a trace records input hashes, so Lake can
# still rebuild if the source tree it hashes differs from the one that produced
# them. This script reports the necessary condition and says so; it does not
# claim `lake build` is safe. Establishing that costs a real build, which risks
# the cache it would be testing.
#
# USAGE
#     scripts/lake-restore-trace-check.sh [root]     # measure + set/clear marker
#     scripts/lake-restore-trace-check.sh --report [root]   # measure only
#     scripts/lake-restore-trace-check.sh --selftest
#
# EXIT: 0 = coverage >= threshold (traces present); 1 = below (marker set).
set -uo pipefail

THRESHOLD="${TRACE_COVERAGE_MIN:-90}"
MODE=measure
case "${1:-}" in
  --selftest) MODE=selftest; shift ;;
  --report)   MODE=report;   shift ;;
esac
ROOT="${1:-$(git rev-parse --show-toplevel 2>/dev/null || echo .)}"

# paired_coverage <root> -> prints "<oleans> <paired> <pct>"
paired_coverage() {
  local root="$1"
  find "$root/.lake" \( -name '*.olean' -o -name '*.trace' \) -type f 2>/dev/null \
  | awk '
      /\.trace$/ { seen[$0]=1; next }
      /\.olean$/ { ol[++n]=$0 }
      END {
        for (i=1;i<=n;i++) {
          o=ol[i]; b=o; sub(/\.olean$/,"",b)
          if ((b ".trace") in seen || (o ".trace") in seen) p++
        }
        printf "%d %d %.1f\n", n, p, (n ? p*100.0/n : 0)
      }'
}

if [ "$MODE" = selftest ]; then
  echo "SELFTEST — does the marker follow the MEASUREMENT, both directions?"
  tmp=$(mktemp -d); trap 'rm -rf "$tmp"' EXIT INT TERM
  mk() { # mk <dir> <n_olean> <n_traced>
    mkdir -p "$1/.lake/build/lib/lean"
    for i in $(seq 1 "$2"); do
      : > "$1/.lake/build/lib/lean/M$i.olean"
      [ "$i" -le "$3" ] && : > "$1/.lake/build/lib/lean/M$i.trace"
    done
    # a trace belonging to no olean — must NOT count toward coverage
    : > "$1/.lake/build/lib/lean/lake.trace"
  }
  ok=1
  mk "$tmp/traced" 10 10
  mk "$tmp/bare"   10 0
  c_traced=$(paired_coverage "$tmp/traced" | cut -d' ' -f3)
  c_bare=$(paired_coverage "$tmp/bare"     | cut -d' ' -f3)
  echo "  fully traced tree -> ${c_traced}%  (expect 100.0)"
  echo "  untraced tree     -> ${c_bare}%  (expect 0.0)"
  [ "$c_traced" = "100.0" ] || ok=0
  [ "$c_bare"   = "0.0"   ] || ok=0

  # The non-olean trace must not inflate the count: a naive
  # total-traces/oleans ratio would report 110% on the traced tree.
  naive=$(find "$tmp/traced/.lake" -name '*.trace' | wc -l | tr -d ' ')
  echo "  non-olean trace ignored -> paired 10, naive total ${naive} (naive would read 110%)"
  [ "$naive" = "11" ] || ok=0

  # And the marker must follow the measurement in BOTH directions.
  : > "$tmp/traced/.lake/RESTORED-NO-TRACES"     # stale marker on a traced tree
  "$0" "$tmp/traced" >/dev/null 2>&1
  [ -f "$tmp/traced/.lake/RESTORED-NO-TRACES" ] && { echo "  FAIL: stale marker not cleared on a traced tree"; ok=0; } \
    || echo "  stale marker on traced tree -> CLEARED"
  "$0" "$tmp/bare" >/dev/null 2>&1
  [ -f "$tmp/bare/.lake/RESTORED-NO-TRACES" ] && echo "  untraced tree -> marker SET" \
    || { echo "  FAIL: marker not set on an untraced tree"; ok=0; }

  echo
  [ "$ok" = 1 ] && { echo "  PASS"; exit 0; }
  echo "  FAIL — do not trust this check."; exit 1
fi

echo "lake-restore-trace-check:"
out=$(paired_coverage "$ROOT")
n=$(echo "$out" | cut -d' ' -f1); p=$(echo "$out" | cut -d' ' -f2); pct=$(echo "$out" | cut -d' ' -f3)
echo "  root:   $ROOT"
echo "  oleans: $n     traced: $p  (${pct}%)   threshold: ${THRESHOLD}%"

if [ "$n" -eq 0 ]; then
  echo "  no oleans found — nothing to judge (is this a built/restored tree?)" >&2
  exit 1
fi

low=$(awk -v a="$pct" -v b="$THRESHOLD" 'BEGIN{print (a<b)?1:0}')
if [ "$MODE" = report ]; then
  [ "$low" = 1 ] && exit 1 || exit 0
fi

if [ "$low" = 1 ]; then
  : > "$ROOT/.lake/RESTORED-NO-TRACES"
  echo "  -> marker SET. Lake would rebuild and EVICT these oleans."
  echo "     Verify with lean-direct; do NOT 'lake build' at the root."
  exit 1
fi
rm -f "$ROOT/.lake/RESTORED-NO-TRACES"
echo "  -> marker CLEARED. Traces are present, which is what Lake reads."
echo "     NOTE: necessary, not proven sufficient — a trace records input hashes,"
echo "     so Lake may still rebuild if the source tree differs. Prefer lean-direct."
exit 0
