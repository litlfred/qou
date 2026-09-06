---
# qou-cvky
title: 'The 22 at-risk files from #6864 were never run — measure which actually break, fix those'
status: completed
type: task
priority: normal
created_at: 2026-09-06T10:45:45Z
updated_at: 2026-09-06T11:01:35Z
---

## MEASURED AND FIXED — PR #6940

#6864 said the 22 at-risk files were "CANDIDATES, not breakages" and never ran
them. Ran them on main (1352b02c29), 19 files, 90 s budget each:

    14  NON-MONOTONE (genuinely broken by the 2026-09-05 ordering ruling)
     3  ok
     1  timeout at 90 s
     1  unrelated pre-existing error

**This is the FIRST population in this arc where the symptom count held up.**
Every other one over-counted by roughly 10x — 48 dead pointers with zero rot
(`qou-...` dead-pointer sweep), 12 live shadows with one defect, 4 junk points
with one live, "twelve carrier repairs" that were five. I had built a prior that
symptom counts over-count. **Here that prior would have been wrong**, and the
only way to know was to run them. Worth carrying: the prior is about *counting by
symptom without executing*, not about candidate lists as such — when the symptom
IS the failure mode (a hard import-time/call-time raise), the count is honest.

## Two breakage routes

4 files called `chi_all_lambda_reduced_block`; 7 called bare `chi_all_lambda`
from `chi_monotone_transfer`. Both fixed by routing to
`chi_general_word.chi_all_lambda_any` (identical signature + optional `fast`).

`reduced_block_kernel.py` needed a DIFFERENT fix: its own `__main__` self-test
compares `chi_all_lambda` against this module's block accelerator, and BOTH are
monotone-only, so the interleaved word would test the guard rather than the
composition. Pinned to `intra_order="grouped"`. Routing it to the dispatcher
would also be circular (`chi_general_word` imports it).

## My own sweep bug, caught by the re-run

Robust regex for call sites, brittle exact-string match for imports → the two
files whose import carries `# noqa: E402` had calls renamed and imports not
(NameError). Fixed; a call-without-import check now reports 0 mismatches.

## Left honestly red, deliberately

- `audits/word_to_mpfr_template_scale_audit.py` line 63 hardcodes
  `("0.403767...", "1.29667...")` for 3He — PRE-RULING grouped values. Computed
  Borromean: `0.0585962...` / `0.1881786...`. It now REACHES the comparison and
  reports a real change where it previously crashed. Updating the baseline is the
  move AGENTS.md forbids; the canonical value is a `qou-hu1f` question.
- `delta_lambda_shape_probe.py` unpacks 4 from `_constants()` which returns 3.
  NOT mine, NOT the regression: `git log -S "g8"` on `mass_binding_dashboard.py`
  is empty, so it never returned a 4th value, and #6881 changed only the
  `float()` wrappers.

Three witness files regenerated as producer side-effects were REVERTED, not
committed — contended files main regenerates on its own cadence, whose committed
values also predate the ordering ruling.
