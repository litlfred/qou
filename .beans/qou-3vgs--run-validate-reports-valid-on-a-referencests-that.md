---
# qou-3vgs
title: run-validate reports Valid on a references.ts that does not parse
status: todo
type: task
priority: normal
created_at: 2026-08-21T16:55:42Z
updated_at: 2026-08-21T16:56:09Z
---

MEASURED 2026-08-21 by controlled test (found while working qou-ghy5).

I broke references.ts by accident — an unescaped double quote inside a
double-quoted note — and `bun run scripts/run-validate.ts` still printed
'Valid'. So I broke it deliberately to check:

    export const references BROKEN_SYNTAX_TEST: CSLData[] = [

  bun import          -> error: Expected ";" but found "BROKEN_SYNTAX_TEST"
  run-validate.ts     -> Valid - 27 issue(s)

File restored immediately; the corpus is unaffected.

So the bibliography can be syntactically broken — unparseable, every citation
in the paper unresolvable, the .bib un-regenerable — and the content
pipeline's validation reports success. run-validate checks content blocks and
does not import references.ts.

What DOES catch it: importing the module. `bun -e 'await
import("content/schema/references.ts")'` fails immediately, and any script
that reads the entries by executing the module rather than scanning the text
fails with it.

Note the same blind spot in scripts/check-citation-keys.py, added on this
branch: it resolves keys by REGEX over the source, deliberately (it also has
to read comments correctly), so it reports normally on a file that does not
parse. Its docstring now says so.

Cheapest fix: have run-validate import references.ts, or add a one-line
parse gate to check-sidecars.sh, which is already the stated pre-commit
preflight.
