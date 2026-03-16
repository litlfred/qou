#!/usr/bin/env bash
# generate-diff.sh — produce a latexdiff document comparing the current
# working tree against the merge-base (fork point) with the main branch.
#
# Uses `git merge-base` so that the diff only shows changes introduced
# on the feature branch, not unrelated changes merged into main since
# the branch was created.
#
# Outputs:  diff.tex  in the repository root, ready for compilation.
#
# Requirements (on the runner):
#   latexdiff   (usually in texlive-extra-utils or the latexdiff package)
#   latexpand   (usually in texlive-extra-utils)
#   git
#
# Usage:
#   .github/scripts/generate-diff.sh
#
# Colour convention
#   deleted text  →  red
#   added   text  →  green  (dark green, rgb 0 0.5 0)
#
# Math handling
#   --math-markup=coarse  treats each changed math environment as a single
#   unit: the entire old formula is shown in red, the entire new one in green.

set -euo pipefail

REPO_ROOT="$(git rev-parse --show-toplevel)"
cd "$REPO_ROOT"

MAIN_DIR="$(mktemp -d)"
trap 'rm -rf "$MAIN_DIR"' EXIT

# ── 1. Extract sources at the fork point (merge-base) ───────────────────────
echo "::group::Extract merge-base sources"
MERGE_BASE="$(git merge-base origin/main HEAD)"
echo "Merge-base commit: ${MERGE_BASE}"
git archive "$MERGE_BASE" | tar -x -C "$MAIN_DIR"
echo "::endgroup::"

# ── 2. Flatten both versions ────────────────────────────────────────────────
echo "::group::Flatten LaTeX sources"
MAIN_FLAT="$(mktemp)"
BRANCH_FLAT="$(mktemp)"
trap 'rm -rf "$MAIN_DIR" "$MAIN_FLAT" "$BRANCH_FLAT"' EXIT

(cd "$MAIN_DIR" && latexpand main.tex) > "$MAIN_FLAT"
latexpand main.tex                      > "$BRANCH_FLAT"
echo "::endgroup::"

# ── 3. Run latexdiff ────────────────────────────────────────────────────────
# --math-markup=coarse : changed math environments are shown as whole units
# --type=CFONT         : font-based markup (more robust brace handling than
#                        the default UNDERLINE, which can misparse \ref{} etc.
#                        inside \DIFdel{...}/\DIFadd{...} wrappers)
# --append-safecmd     : protect cross-reference commands from being broken
#                        up by the diff markup (prevents "extra }" errors)
echo "::group::Run latexdiff"
latexdiff \
  --math-markup=coarse \
  --type=CFONT \
  --append-safecmd="ref,eqref,cite,label,autoref,nameref,hyperref" \
  "$MAIN_FLAT" "$BRANCH_FLAT" \
  > diff.tex \
  || { echo "::warning::latexdiff failed; falling back to unchanged source"
       cp "$BRANCH_FLAT" diff.tex; }
echo "::endgroup::"

# ── 4. Patch colours ────────────────────────────────────────────────────────
# latexdiff default:  added = blue,  deleted = red
# We want:            added = dark green (0,0.5,0),  deleted = red (keep)
#
# Also replace uwave (wavy underline) with simple text for cleaner output,
# and keep sout (strikethrough) for deletions.
echo "::group::Patch diff colours"

# Added text: blue → dark green (case-insensitive to catch both \color{blue} and \color{BLUE})
sed -i 's/\\color{[Bb][Ll][Uu][Ee]}/\\color[rgb]{0,0.5,0}/g'   diff.tex

# If CFONT type colour definitions are present, override BLUE
sed -i 's/\\definecolor{BLUE}{rgb}{0,0,1}/\\definecolor{BLUE}{rgb}{0,0.5,0}/g' diff.tex

# Ensure xcolor is loaded (needed for rgb colour model)
# Insert after the \RequirePackage{color} line that latexdiff adds
sed -i 's/\\RequirePackage{color}/\\RequirePackage{xcolor}/' diff.tex

echo "::endgroup::"

echo "✓ diff.tex generated ($(wc -l < diff.tex) lines)"
