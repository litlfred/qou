#!/usr/bin/env bash
# qa-writer — one of qou's QA writers, as qou.json `qa.writers` declares them.
#
#   bash "${INSTANCE:-.}/scripts/qa-writer.sh" <rendering|lean|compute|accuracy>
#
# The integrated QA page (cat-harness-tools scripts/qa-page.ts) draws one
# section per QA axis from the records a layer publishes to its qa-reports
# branch. qou.json declares which writer answers for which axis; this script is
# what each declared `run` calls, so the same command works in both places it
# runs:
#
#   - the platform's layer-qa-publish.yml (called by .github/workflows/
#     compute-qa.yml): cwd is the INDEX checkout, qou is mounted at ./qou,
#     INSTANCE=qou and QA_HOME=qou/test/results are exported;
#   - scripts/qa-publish-local.sh (run by publish-main-local.sh, because
#     Actions is dispatch-only here): cwd is qou's root, the platform is
#     ./folio-assistant, INSTANCE is unset and QA_HOME=test/results.
#
# QA_HOME is resolved against the caller's cwd BEFORE this script moves to
# qou's root. A writer exits 0 when it WROTE its record, whatever the record
# says: a red verdict is a result to publish, and only "could not write" fails
# (layer-qa-publish.yml fails the job on a failing writer, so a partial record
# is never published).
set -euo pipefail
WHO=${1:?usage: qa-writer.sh <rendering|lean|compute|accuracy>}
CALLER=$(pwd)
HERE=$(cd "$(dirname "$0")/.." && pwd)
QA_HOME=${QA_HOME:-test/results}
case "$QA_HOME" in /*) HOME_ABS=$QA_HOME ;; *) HOME_ABS=$CALLER/$QA_HOME ;; esac
# The platform: qou's own ./folio-assistant when it has one (an agent's
# checkout), else the index checkout the caller runs in (the workflow).
if [ -d "$HERE/folio-assistant/cat-harness-tools" ]; then PLAT=$HERE/folio-assistant; else PLAT=$CALLER; fi
mkdir -p "$HOME_ABS"
cd "$HERE"

pydeps() {
  python3 -c "import mpmath, numpy, scipy, pytest" >/dev/null 2>&1 \
    || python3 -m pip install --quiet mpmath numpy scipy pytest
}

case "$WHO" in
  rendering)
    # The platform's writer (folio-assistant-sci, ported from
    # scripts/lib/paper-render-qa.py). build/paper is build-paper-pdf.sh's
    # output; with none, every check reads n/a rather than clean.
    W=$PLAT/folio-assistant-sci/scripts/paper-render-qa.ts
    if [ ! -f "$W" ]; then
      # Not a failure to compute: this platform predates the writer. No record
      # is written, so the page reads the rendering axis as unknown.
      echo "qa-writer: $W is absent (folio-assistant-sci#217 not in this platform): no rendering record, the axis reads unknown"; exit 0
    fi
    bun run "$W" build/paper --root . --out "$HOME_ABS/rendering/paper.render-qa.json"
    ;;
  lean)
    # Source-level, no Lean build: vacuity, self-assuming projections, uncited
    # axioms. Counted per scanned file in the shared vocabulary: fail (a
    # non-exempt finding), warn (exempt findings only), pass (no finding).
    mkdir -p "$HOME_ABS/lean"
    OUT=$HOME_ABS/lean/lean-vacuity-axiom-audit.json
    bun run folio/pipeline/lean-vacuity-axiom-audit.ts --json "$OUT" --quiet >/dev/null
    python3 - "$OUT" <<'PY'
import json, sys
p = sys.argv[1]
d = json.load(open(p, encoding="utf-8"))
fail = sum(1 for hits in d["flagged"].values() if any(not h.get("exempt") for h in hits))
warn = len(d["flagged"]) - fail
d["counts"] = {"fail": fail, "warn": warn, "pass": d["scanned_files"] - len(d["flagged"])}
json.dump(d, open(p, "w", encoding="utf-8"), indent=2)
print(f"qa-writer lean: {d['counts']} over {d['scanned_files']} file(s)")
PY
    ;;
  compute)
    # Every compute-QA gate (processes/tools/compute-qa.bpmn). A gate whose
    # setup is missing here (the MPFR LP binary, say) is recorded `unknown`,
    # never skipped. Writes test/results/compute-qa/<gate>.json.
    pydeps
    PYTHONPATH=computations:tools/pyhecke/python:tools/qou-substrate/python:computations/substrate \
      python3 scripts/compute-qa.py --every || true
    ;;
  accuracy)
    # The observational accuracy scorecard (ACCURACY.md against its witnesses).
    pydeps
    python3 scripts/generate-accuracy-scorecard.py --check --qa-report || true
    ;;
  *) echo "qa-writer: unknown writer '$WHO'" >&2; exit 2 ;;
esac

# The compute and accuracy writers write into qou's own test/results; carry
# them to QA_HOME when that is somewhere else.
if [ "$WHO" = compute ] || [ "$WHO" = accuracy ]; then
  [ -d test/results/compute-qa ] || { echo "qa-writer: $WHO wrote nothing under test/results/compute-qa" >&2; exit 1; }
  if [ "$(cd test/results && pwd -P)" != "$(cd "$HOME_ABS" && pwd -P)" ]; then
    mkdir -p "$HOME_ABS/compute-qa" && cp test/results/compute-qa/*.json "$HOME_ABS/compute-qa/"
  fi
fi
