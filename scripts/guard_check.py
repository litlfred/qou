#!/usr/bin/env python3
"""Guard modified content/*.md files before auto-commit.

Three outcomes per file, not two:

  PASS  -> the filename is printed on stdout; the caller commits it.
  BLOCK -> "Reverting <path> (<reason>)" on stdout, and the working-tree edit
           is discarded with `git checkout -- <path>`.
  SKIP  -> a warning on stderr; the file is NEITHER committed NOR reverted.

The third outcome exists because the guard's own machinery can fail.  Both
`git diff` calls used to sit under a bare `except: pass`, so a crash fell
through to `return True` -- a file the guard never managed to evaluate was
reported as having passed it.  Making that error return False instead would be
worse, not safer: BLOCK runs `git checkout -- <path>`, which destroys the
working-tree edit.  An unevaluated file is not a failed file, so it is given
neither verdict; it stays dirty and is retried on the next run.

Diagnostics for SKIP go to stderr on purpose: stdout is a filename list that
scripts/auto_commit_batches.py feeds straight to `git add`.

Exit status stays 0 when files are skipped.  The caller runs this under
subprocess.check_output, which raises on a non-zero exit and would then commit
nothing at all -- one unevaluable file must not block every other file in the
batch.  A skip is therefore reported loudly rather than fatally, and it can
never be mistaken for a pass: the skipped file is absent from stdout and is
left modified in the working tree.
"""

import subprocess
import sys

PASS, BLOCK, SKIP = True, False, None

MAX_LINE_DELTA = 200


def _git(args, filepath):
    """Run a git command; return stdout, or None if the guard could not run it."""
    try:
        return subprocess.check_output(['git'] + args, text=True)
    except Exception as exc:  # not BaseException: let Ctrl-C propagate
        print(f"SKIP {filepath}: guard could not run `git {' '.join(args)}`: "
              f"{exc.__class__.__name__}: {exc}", file=sys.stderr)
        return None


def check_file(filepath):
    if not filepath.endswith('.md'):
        print(f"Reverting {filepath} (not .md)")
        return BLOCK

    # Check >200-line delta
    diff_out = _git(['diff', '--numstat', filepath], filepath)
    if diff_out is None:
        return SKIP
    diff_out = diff_out.strip()
    if diff_out:
        fields = diff_out.split('\t')
        if len(fields) < 2 or not fields[0].isdigit() or not fields[1].isdigit():
            print(f"SKIP {filepath}: unparseable `git diff --numstat` output: "
                  f"{diff_out!r}", file=sys.stderr)
            return SKIP
        added, deleted = int(fields[0]), int(fields[1])
        if added > MAX_LINE_DELTA or deleted > MAX_LINE_DELTA:
            print(f"Reverting {filepath} (>{MAX_LINE_DELTA} line delta)")
            return BLOCK

    # Check diagram/eqn/anchor deletion
    diff_text = _git(['diff', '-U0', filepath], filepath)
    if diff_text is None:
        return SKIP
    for line in diff_text.splitlines():
        if line.startswith('-') and not line.startswith('---'):
            if '$$' in line or '\\begin' in line or '```mermaid' in line or '{#' in line:
                print(f"Reverting {filepath} (math/diagram/anchor deletion)")
                return BLOCK

    return PASS


modified = subprocess.check_output(['git', 'status', '--porcelain'], text=True).splitlines()
to_commit = []
skipped = []
for line in modified:
    if line.startswith(' M ') or line.startswith('M '):
        filepath = line[3:].strip()
        if filepath.startswith('"') and filepath.endswith('"'):
            filepath = filepath[1:-1]

        if filepath.startswith('content/'):
            verdict = check_file(filepath)
            if verdict is PASS:
                to_commit.append(filepath)
            elif verdict is BLOCK:
                subprocess.call(['git', 'checkout', '--', filepath])
            else:  # SKIP -- leave the working tree exactly as it is
                skipped.append(filepath)

# Output the valid files (stdout is a filename list -- keep it clean)
for f in to_commit:
    print(f)

if skipped:
    print(f"\nguard_check: {len(skipped)} file(s) SKIPPED -- the guard could not "
          f"evaluate them. Left uncommitted and unreverted:", file=sys.stderr)
    for f in skipped:
        print(f"  {f}", file=sys.stderr)
