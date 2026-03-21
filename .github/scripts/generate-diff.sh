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
# --type=CFONT         : colour + font-size change (no underline/strikethrough)
# --math-markup=coarse : changed math environments are shown as whole units

# --type=CFONT         : font-based markup (more robust brace handling than
#                        the default UNDERLINE, which can misparse \ref{} etc.
#                        inside \DIFdel{...}/\DIFadd{...} wrappers)
# --append-safecmd     : protect cross-reference commands from being broken
#                        up by the diff markup (prevents "extra }" errors)

echo "::group::Run latexdiff"
latexdiff \
  --type=CFONT \
  --math-markup=coarse \
  --append-safecmd="ref,eqref,cite,label,autoref,nameref,hyperref" \
  "$MAIN_FLAT" "$BRANCH_FLAT" \
  > diff.tex \
  || { echo "::warning::latexdiff failed; falling back to unchanged source"
       cp "$BRANCH_FLAT" diff.tex; }
echo "::endgroup::"

# ── 4. Patch colours ────────────────────────────────────────────────────────
# latexdiff CFONT:    added = blue,  deleted = red
# We want:            added = dark green (0,0.5,0),  deleted = red (keep)
#
# Strategy: define a named colour (DIFgreen) using \definecolor with the
# {rgb} model, which works with both the color and xcolor packages.
# Then replace every \color{blue}/\color{BLUE} with \color{DIFgreen}.
echo "::group::Patch diff colours"

# 1. Define DIFgreen just before \begin{document} (robust: works regardless of
#    whether the document loads color, xcolor, or latexdiff injects RequirePackage)
sed -i '/\\begin{document}/i \\\definecolor{DIFgreen}{rgb}{0,0.5,0} %DIF PREAMBLE' diff.tex

# 2. Override the BLUE colour definition that CFONT type emits
sed -i 's/\\definecolor{BLUE}{rgb}{[^}]*}/\\definecolor{BLUE}{rgb}{0,0.5,0}/g' diff.tex

# 3. Replace \color{blue} / \color{BLUE} with \color{DIFgreen}
sed -i 's/\\color{[Bb][Ll][Uu][Ee]}/\\color{DIFgreen}/g' diff.tex

echo "::endgroup::"

# ── 5. Append Lean checks summary ────────────────────────────────────────
# Show sorry count changes and Lean file diffs between main and the branch.
echo "::group::Lean checks summary"

# Count sorry markers in each version
MAIN_SORRY=0
BRANCH_SORRY=0
if [ -d "$MAIN_DIR/lean" ]; then
  MAIN_SORRY=$(grep -r --include='*.lean' -c '\bsorry\b' "$MAIN_DIR/lean/" 2>/dev/null \
    | awk -F: '{s+=$NF} END {print s+0}' || echo 0)
fi
if [ -d lean ]; then
  BRANCH_SORRY=$(grep -r --include='*.lean' -c '\bsorry\b' lean/ 2>/dev/null \
    | awk -F: '{s+=$NF} END {print s+0}' || echo 0)
fi

# Collect changed Lean files
LEAN_CHANGED_FILES=$(git diff --name-only "$MERGE_BASE" HEAD -- 'lean/**/*.lean' 2>/dev/null || true)
LEAN_ADDED_FILES=$(git diff --diff-filter=A --name-only "$MERGE_BASE" HEAD -- 'lean/**/*.lean' 2>/dev/null || true)
LEAN_DELETED_FILES=$(git diff --diff-filter=D --name-only "$MERGE_BASE" HEAD -- 'lean/**/*.lean' 2>/dev/null || true)
LEAN_MODIFIED_FILES=$(git diff --diff-filter=M --name-only "$MERGE_BASE" HEAD -- 'lean/**/*.lean' 2>/dev/null || true)

# Count changed files
N_CHANGED=$(echo "$LEAN_CHANGED_FILES" | grep -c . 2>/dev/null || echo 0)
N_ADDED=$(echo "$LEAN_ADDED_FILES" | grep -c . 2>/dev/null || echo 0)
N_DELETED=$(echo "$LEAN_DELETED_FILES" | grep -c . 2>/dev/null || echo 0)
N_MODIFIED=$(echo "$LEAN_MODIFIED_FILES" | grep -c . 2>/dev/null || echo 0)

# Compute sorry delta
SORRY_DELTA=$((BRANCH_SORRY - MAIN_SORRY))
if [ "$SORRY_DELTA" -gt 0 ]; then
  SORRY_STATUS="\\\\textcolor{red}{+${SORRY_DELTA} sorry markers added}"
elif [ "$SORRY_DELTA" -lt 0 ]; then
  SORRY_STATUS="\\\\textcolor{DIFgreen}{${SORRY_DELTA} sorry markers removed}"
else
  SORRY_STATUS="No change in sorry count"
fi

# Per-file sorry counts (branch only, for changed files)
PERFILE_SORRY=""
if [ -n "$LEAN_CHANGED_FILES" ]; then
  while IFS= read -r lf; do
    [ -z "$lf" ] && continue
    if [ -f "$lf" ]; then
      FC=$(grep -c '\bsorry\b' "$lf" 2>/dev/null || echo 0)
      PERFILE_SORRY="${PERFILE_SORRY}    \\\\texttt{${lf//\_/\\_}} & ${FC} \\\\\\\\\n"
    fi
  done <<< "$LEAN_CHANGED_FILES"
fi

# Generate the Lean diff body (unified diff of Lean files, truncated)
LEAN_DIFF=""
if [ -n "$LEAN_CHANGED_FILES" ]; then
  LEAN_DIFF=$(git diff "$MERGE_BASE" HEAD -- 'lean/**/*.lean' 2>/dev/null | head -200 || true)
fi

# Inject Lean checks appendix before \end{document}
LEAN_SECTION=$(cat <<'LEANSECTION'
\clearpage
\appendix
\section*{Lean Formalization Changes}
\addcontentsline{toc}{section}{Lean Formalization Changes}

\subsection*{Sorry Audit}
\begin{tabular}{lr}
\hline
\textbf{Metric} & \textbf{Count} \\
\hline
LEANSECTION
)

# Build the sorry table rows
LEAN_SECTION="${LEAN_SECTION}
    Main (merge-base) sorry count & ${MAIN_SORRY} \\\\
    Branch sorry count & ${BRANCH_SORRY} \\\\
\\hline
\\end{tabular}

\\medskip
${SORRY_STATUS}
"

# File changes summary
LEAN_SECTION="${LEAN_SECTION}
\\subsection*{Changed Lean Files}
\\begin{tabular}{lr}
\\hline
\\textbf{Category} & \\textbf{Count} \\\\
\\hline
    Added & ${N_ADDED} \\\\
    Modified & ${N_MODIFIED} \\\\
    Deleted & ${N_DELETED} \\\\
\\hline
    Total & ${N_CHANGED} \\\\
\\hline
\\end{tabular}
"

# Per-file sorry table (only if there are changed files with sorry)
if [ -n "$PERFILE_SORRY" ]; then
  LEAN_SECTION="${LEAN_SECTION}
\\subsection*{Sorry Counts in Changed Files}
\\begin{tabular}{lr}
\\hline
\\textbf{File} & \\textbf{sorry count} \\\\
\\hline
$(echo -e "$PERFILE_SORRY")\\hline
\\end{tabular}
"
fi

# File listing
if [ -n "$LEAN_CHANGED_FILES" ]; then
  FILE_LIST=""
  while IFS= read -r lf; do
    [ -z "$lf" ] && continue
    FILE_LIST="${FILE_LIST}  \\item \\texttt{${lf//\_/\\_}}"$'\n'
  done <<< "$LEAN_CHANGED_FILES"
  LEAN_SECTION="${LEAN_SECTION}
\\subsection*{File List}
\\begin{itemize}
${FILE_LIST}\\end{itemize}
"
fi

# Lean diff listing (truncated to keep PDF manageable)
if [ -n "$LEAN_DIFF" ]; then
  # Escape special LaTeX chars in the diff output for verbatim
  LEAN_SECTION="${LEAN_SECTION}
\\subsection*{Lean Diff (truncated)}
{\\small
\\begin{verbatim}
${LEAN_DIFF}
\\end{verbatim}
}
"
fi

# Insert before \end{document}
# Use a temp file to avoid sed issues with multi-line content
LEAN_SECTION_FILE="$(mktemp)"
echo "$LEAN_SECTION" > "$LEAN_SECTION_FILE"

# Use Python for reliable multi-line insertion (sed struggles with this)
python3 -c "
import sys
section = open('$LEAN_SECTION_FILE').read()
with open('diff.tex', 'r') as f:
    content = f.read()
content = content.replace(r'\end{document}', section + r'\end{document}')
with open('diff.tex', 'w') as f:
    f.write(content)
"
rm -f "$LEAN_SECTION_FILE"

echo "  Sorry: main=${MAIN_SORRY} branch=${BRANCH_SORRY} delta=${SORRY_DELTA}"
echo "  Changed Lean files: ${N_CHANGED} (added=${N_ADDED} modified=${N_MODIFIED} deleted=${N_DELETED})"
echo "::endgroup::"

echo "✓ diff.tex generated ($(wc -l < diff.tex) lines)"
