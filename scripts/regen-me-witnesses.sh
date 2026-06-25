#!/usr/bin/env bash
# regen-me-witnesses.sh — guarded one-shot regen of the ct80 m_e-stale witnesses.
#
# Bean ct80 (PR #2747) fixed the truncated electron mass in
#   computations/substrate/experimental_constants.py
#     M_E_MEV  0.51099895000  ->  0.51099895069   (full CODATA-2022)
# so every *.witness.json produced by a script that reads m_e FROM THAT MODULE
# is now stale and must be regenerated, and the value fix + the regen must land
# together. (Sibling producers that read m_e from codata_constants were fixed by
# bean me3r / #2725 and are NOT in this set.)
#
# This is a thin wrapper around the orchestrator that does the real work:
#   computations/regen_me_witnesses_batch.py
# The orchestrator enumerates the producer set deterministically (direct,
# non-deprecated, witness-emitting importers of experimental_constants) and
# GUARDS the run: it refuses to write anything unless the environment is
# full-precision (pyhecke_native importable AND OUTPUT_DPS/COMPUTE_DPS >= 50).
# That guard exists because a previous ct80 pass regenerated in a sandbox
# WITHOUT pyhecke_native, silently regressed 50-dps mpf values to f64, and had
# to revert all of them — an L1 precision regression.
#
# Usage:
#   scripts/regen-me-witnesses.sh                 # DRY RUN (default): list only
#   scripts/regen-me-witnesses.sh --dry-run       # explicit dry run
#   scripts/regen-me-witnesses.sh --run           # FULL-ENV regen (guard-gated)
#   scripts/regen-me-witnesses.sh --run --limit 5 # first 5 producers
#   scripts/regen-me-witnesses.sh --run --no-commit
#
# Any extra args are forwarded verbatim to the orchestrator. In --run mode the
# orchestrator's stdout is also teed to /tmp/regen-me.log (long-compute
# logging discipline). DRY RUN writes nothing and is safe in any environment.
set -euo pipefail

# Repo root = parent of this script's dir (scripts/ lives at the repo root).
HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO="$(cd "${HERE}/.." && pwd)"
RUNNER="${REPO}/computations/regen_me_witnesses_batch.py"

if [[ ! -f "${RUNNER}" ]]; then
  echo "error: orchestrator not found at ${RUNNER}" >&2
  exit 1
fi

# Detect whether this invocation is a real run (--run present) so we can tee.
is_run=0
for a in "$@"; do
  if [[ "$a" == "--run" ]]; then is_run=1; fi
done

cd "${REPO}"
if [[ "${is_run}" -eq 1 ]]; then
  # Full-env regen — unbuffered + teed per the long-compute logging discipline.
  python3 -u "${RUNNER}" "$@" 2>&1 | tee /tmp/regen-me.log
else
  # Dry run (default). Nothing is executed or written.
  python3 -u "${RUNNER}" "$@"
fi
