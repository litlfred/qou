#!/usr/bin/env bash
# check-sidecars.sh — PRE-COMMIT preflight: map changed files → the QA sidecars /
# criteria that apply to them, so agents check the RELEVANT sidecars instead of
# relying on the reactive post-commit qa-sweep (which does not cover everything).
#
# Motivation (2026-06-25): a gratuitous `(q : ℝ)` / `SL₂(ℝ)` landed on a purely
# algebraic statement in a STANDALONE library Lean file. The §7c rule is documented
# and doubly-tooled (`q-usage-*`, `wall-side-correct`/`checkWallSide`), but both
# checkers run per content-block `<block>.qa.json` — a library file with no `.md`/`.ts`
# sibling has no sidecar and escapes the sweep. This script closes that gap: it tells
# you, for exactly the files you touched, which sidecar criteria apply and runs the
# §7c base-ring check on un-sidecar'd library Lean by hand.
#
# Usage:
#   scripts/check-sidecars.sh [file ...]     # explicit files
#   scripts/check-sidecars.sh                # default: staged + unstaged vs HEAD
#
# Exit code: 0 always (advisory). Look for ⚠ lines — they need agent action.

set -uo pipefail
ROOT=$(git rev-parse --show-toplevel 2>/dev/null) || { echo "not a git repo"; exit 0; }
cd "$ROOT"

# Collect target files.
if [ "$#" -gt 0 ]; then
  files=("$@")
else
  mapfile -t files < <( { git diff --name-only HEAD 2>/dev/null; git diff --cached --name-only 2>/dev/null; } | sort -u )
fi
mapfile -t files < <(printf '%s\n' "${files[@]:-}" | sort -u | grep -v '^$' || true)
[ "${#files[@]}" -eq 0 ] && { echo "check-sidecars: no changed files."; exit 0; }

# Code-level archimedean markers (the §7c wall). Prose in /- -/ docstrings is ignored
# by stripping comment lines first; we scan the CODE body only.
ARCH='(\(q : ℝ\)|: ℝ\b|\(ℝ\)|Real\.(sqrt|rpow|log|exp|cos|sin|pi)|\blinarith\b|\bpositivity\b|\bnlinarith\b|\bnorm_num\b|LinearOrderedField|0 < q\b|\bCODATA\b|MeV)'

action=0
echo "check-sidecars: ${#files[@]} changed file(s)"
echo

for f in "${files[@]}"; do
  [ -f "$f" ] || continue
  case "$f" in
    content/*/lean/*.lean|content/*lean*/*.lean)
      base="${f%.lean}"
      if [ -f "$base.md" ] || [ -f "$base.ts" ]; then
        # Content-block Lean — has (or should have) a .qa.json sidecar.
        qa="$base.qa.json"
        echo "▸ $f  [content-block Lean]"
        if [ -f "$qa" ]; then
          crits=$(grep -oE '"(q-usage-[a-z0-9-]+|wall-side-correct|[a-z-]+-statement-integrity|da-[a-z0-9-]+|one-voice-[a-z0-9-]+)"' "$qa" 2>/dev/null | tr -d '"' | sort -u | paste -sd', ' -)
          echo "    sidecar: $qa"
          echo "    criteria: ${crits:-<none cached>}"
        else
          echo "    ⚠ NO sidecar yet"; action=1
        fi
        echo "    → refresh: bun run content/pipeline/qa-sweep.ts $base"
      else
        # STANDALONE library Lean — NOT covered by any per-block checker (no .qa.json
        # sidecar; sidecars live on content blocks in chapter dirs). §7c by hand. Two
        # violation classes are flagged; pure-ℝ in an archimedean-domain path is fine.
        # Strip /- … -/ doc blocks and -- comments so prose ℝ doesn't false-positive.
        body=$(sed '\#/-#,\#-/#d' "$f" | sed 's|--.*||')
        GEN='(\{R : Type|\[CommRing|\[Field |\[GroupWithZero|\(R := )'
        # Path-domain heuristic. Calibrated for PER-COMMIT use (your 1–5 changed files):
        # a triage hint, not a verdict. On a WHOLE-TREE sweep it OVER-FIRES — catch-all
        # dirs (BraidKnot/ especially) hold legitimately-archimedean files
        # (QRogersPentagonArchimedean, QBeta*, PerNucleusMassDerivation, dilog…), and
        # large files (e.g. Mathlib/HeckeAlgebra.lean) deliberately pair a generic core
        # with an ℝ realization. Confirm per-file before acting; see
        # docs/audits/2026-06-25-lean-library-tree-7c-coverage-gap.md.
        ALG='/(BraidKnot|BraidsAndKnots|Braiding|HeckeAlgebra|AlgebraicSubstrate|Hecke|MathlibExt|Mathlib|Machinery)/'
        printf '%s\n' "$body" | grep -qE "$ARCH" && has_arch=1 || has_arch=0
        printf '%s\n' "$body" | grep -qE "$GEN"  && has_gen=1  || has_gen=0
        if [ "$has_arch" = 1 ] && [ "$has_gen" = 1 ]; then
          echo "▸ $f  [⚠ §7c MIXED generic+archimedean → wall violation: split into two files per §7c]"
          printf '%s\n' "$body" | grep -nE "$ARCH" | head -6 | sed 's/^/         arch: /'
          action=1
        elif [ "$has_arch" = 1 ] && printf '%s' "$f" | grep -qE "$ALG"; then
          echo "▸ $f  [⚠ §7c ℝ in ALGEBRAIC-domain path → likely gratuitous; default to generic {R}]"
          printf '%s\n' "$body" | grep -nE "$ARCH" | head -6 | sed 's/^/         arch: /'
          action=1
        elif [ "$has_arch" = 1 ]; then
          echo "▸ $f  [library Lean — archimedean-domain path; ℝ OK (no sidecar — verify domain is genuinely archimedean)]"
        else
          echo "▸ $f  [library Lean — no archimedean markers, generic OK]"
        fi
      fi
      ;;
    content/*.md|content/*.ts)
      base="${f%.*}"
      qa="$base.qa.json"
      echo "▸ $f  [content block]"
      if [ -f "$qa" ]; then
        crits=$(grep -oE '"(q-usage-[a-z0-9-]+|wall-side-correct|one-voice-[a-z0-9-]+|da-[a-z0-9-]+|[a-z-]+-integrity|remark-[a-z-]+)"' "$qa" 2>/dev/null | tr -d '"' | sort -u | paste -sd', ' -)
        echo "    sidecar criteria: ${crits:-<none cached>}"
      else
        echo "    (no sidecar yet)"
      fi
      echo "    → bun run content/pipeline/qa-sweep.ts $base   (refresh stale criteria)"
      ;;
    computations/*.py)
      echo "▸ $f  [compute producer]"
      echo "    → LP/SDP? run python computations/lp_dual_witness_validator.py ; re-run producer to refresh *.witness.json"
      ;;
    computations/*.witness.json|*/*.witness.json)
      echo "▸ $f  [witness]"
      echo "    → check scriptCommitSha/scriptHash drift; LP/SDP duals via lp_dual_witness_validator.py"
      ;;
    *) : ;;  # no known sidecar axis
  esac
done

echo
if [ "$action" -eq 1 ]; then
  echo "⚠ check-sidecars: action needed above. Resolve §7c markers / refresh sidecars BEFORE commit."
else
  echo "check-sidecars: no un-sidecar'd §7c flags. Still run qa-sweep on any content blocks listed."
fi
exit 0
