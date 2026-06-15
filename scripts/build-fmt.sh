#!/usr/bin/env bash
#
# build-fmt.sh — precompile the shared LaTeX preamble into <name>.fmt so
# pdflatex can skip re-parsing the heavy preamble (pgf / tikz / tikz-cd /
# hyperref + the unicode shims) on every compile unit and every latexmk pass.
# Pair with `bun run pipeline/build.ts ... --use-format <name>` (or
# generate-main-tex --use-format <name>), which emits a `%&<name>` first line
# instead of inlining the preamble.
#
# CACHE MODEL (mirrors the *.qa.json / *.witness.json sidecar staleness model):
# the format is keyed on sha256(preamble.tex). The hash is written next to the
# format as <name>.fmt.sha, so "is the format stale?" is a one-line string
# compare — exactly the sidecar pattern. The format is rebuilt ONLY when the
# preamble hash drifts (or with --force).
#
# Usage:
#   scripts/build-fmt.sh [--preamble PATH] [--name NAME] [--out-dir DIR] [--force]
# Defaults:
#   --preamble latex/preamble.tex   --name qou   --out-dir .
#
# ENGINE: requires pdflatex + mylatexformat (TeX Live). The dump invocation
# itself is NOT exercisable in the dev sandbox (no TeX engine) — only the
# cache/idempotency logic is. For testing, override the engine via the
# FMT_ENGINE env var; it is invoked as:  $FMT_ENGINE <name> <driver.tex> <out-dir>
# and is expected to produce <out-dir>/<name>.fmt.
#
set -euo pipefail

PREAMBLE="latex/preamble.tex"
NAME="qou"
OUTDIR="."
FORCE=0

while [ $# -gt 0 ]; do
  case "$1" in
    --preamble) PREAMBLE="$2"; shift 2;;
    --name)     NAME="$2";     shift 2;;
    --out-dir)  OUTDIR="$2";   shift 2;;
    --force)    FORCE=1;       shift;;
    -h|--help)
      grep '^#' "$0" | sed 's/^# \{0,1\}//'; exit 0;;
    *) echo "build-fmt: unknown arg: $1" >&2; exit 2;;
  esac
done

[ -f "$PREAMBLE" ] || { echo "build-fmt: preamble not found: $PREAMBLE" >&2; exit 1; }
mkdir -p "$OUTDIR"

FMT="$OUTDIR/$NAME.fmt"
SHAFILE="$OUTDIR/$NAME.fmt.sha"
if command -v sha256sum >/dev/null 2>&1; then
  SHA="$(sha256sum "$PREAMBLE" | cut -d' ' -f1)"
elif command -v shasum >/dev/null 2>&1; then
  SHA="$(shasum -a 256 "$PREAMBLE" | cut -d' ' -f1)"   # macOS / BSD
else
  echo "build-fmt: need sha256sum or shasum" >&2; exit 1
fi

# Cache hit: format present and its recorded preamble hash still matches.
if [ "$FORCE" -eq 0 ] && [ -f "$FMT" ] && [ -f "$SHAFILE" ] \
   && [ "$(cat "$SHAFILE" 2>/dev/null)" = "$SHA" ]; then
  echo "build-fmt: $FMT up-to-date (preamble sha ${SHA:0:12}) — skip"
  exit 0
fi

echo "build-fmt: building $FMT from $PREAMBLE (sha ${SHA:0:12})"

# mylatexformat stops dumping at \begin{document} or \endofdump. preamble.tex
# has neither, so feed it then \endofdump via a tiny driver (absolute paths so
# the working directory is irrelevant). If a package is not dump-safe, move
# ONLY that package after \endofdump in the driver — see
# docs/workplans/2026-06-14-latex-build-caching-strategy.md §3.
# Portable temp driver (BSD/macOS lack `mktemp --suffix` and may lack realpath).
DRIVER_DIR="$(mktemp -d "${TMPDIR:-/tmp}/latex-fmt.XXXXXX")"
DRIVER="$DRIVER_DIR/driver.tex"
trap 'rm -rf "$DRIVER_DIR"' EXIT
PREAMBLE_ABS="$(cd "$(dirname "$PREAMBLE")" && pwd)/$(basename "$PREAMBLE")"
printf '\\input{%s}\n\\endofdump\n' "$PREAMBLE_ABS" > "$DRIVER"

if [ -n "${FMT_ENGINE:-}" ]; then
  # Test / override hook (no real TeX engine in the dev sandbox).
  "$FMT_ENGINE" "$NAME" "$DRIVER" "$OUTDIR"
else
  ( cd "$OUTDIR" && pdflatex -ini -interaction=nonstopmode -halt-on-error \
      -jobname="$NAME" "&pdflatex" mylatexformat.ltx "$DRIVER" )
fi

[ -f "$FMT" ] || {
  echo "build-fmt: ERROR — $FMT not produced (format build failed)." >&2
  echo "  If a package is not dump-safe, move it after \\endofdump (doc §3)." >&2
  exit 1
}

# Record the preamble hash only after a verified successful build.
echo "$SHA" > "$SHAFILE"
echo "build-fmt: wrote $FMT (+ $NAME.fmt.sha)"
