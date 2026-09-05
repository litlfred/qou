---
# qou-48dw
title: Cross-check PhysRevD.108.106023.pdf at computations/probes/aomega_bps_sector_nondegeneracy.py
status: completed
type: task
priority: normal
created_at: 2026-08-08T23:36:42Z
updated_at: 2026-09-05T08:47:54Z
---

Cross-check the probe's 5-node figure-eight count against the published explicit 5x5 quiver matrix, and record in the witness that the count is now confirmed rather than inferred from det(4_1).

**From the source**
- sec. III A, the explicit matrix C^{4_1}, with the size formula in sec. III ("(4mp+1) x (4mp+1)") — The figure-eight knot, as the double-twist knot with both twist parameters equal to one, has an explicit 5x5 quiver matrix under the knots-quivers correspondence.
  Use here: Independently confirms the 5-node open-BPS count that conj:stokes-dt-bps-bridge's sector non-degeneracy argument infers from det(4_1) = 5, turning an inference into a checked value.

Source: `library/physrevd108106023/PhysRevD.108.106023.pdf` — no `references.ts` entry yet
Relevance: **core** — agent assessment, not yet adjudicated.

Raised by `local/paper-relevance-triage`; the ledger row is in `content/bib-qa-verifications.json`.

STALE LINE 2026-08-21 (bean qou-kqbk, PR #5384). The body above says 'no `references.ts` entry yet'. There is one:

  library/physrevd108106023/  ->  [singh-physrevd108106023]
  Knot-quiver correspondence for double twist knots

The library registration backlog is drained to zero. NOT closing this bean — the entry existing is necessary for the task in the title and not sufficient. Use [singh-physrevd108106023] as the citation key when you do it.


## DONE — confirmed, and the RULE behind it is confirmed too (2026-09-05)

The bean asked to cross-check `aomega_bps_sector_nondegeneracy.py`'s 5-node 4₁
count against the published 5×5, and record in the witness that the count is
confirmed rather than inferred from `det(4₁)`. Both halves done.

**The count is read, not inferred.** Singh et al. (`physrevd108106023`,
PRD 108 106023, `sections/sec-005-1-u2-r2.md`) print the 4₁ quiver form as a
motivic sum over `d₁+…+d₅ = r` with an explicit 5×5 symmetric `C_41`. Five
indices, five rows, and `det(4₁) = 5`.

**The OCR transcription is NOT taken on trust**, which is the part that makes it
evidence. The ingested text is column-mangled — `C_41`'s rows arrive as
`-1 -20 11`. So the transcription is cross-validated against the *quadratic form
in the exponent of the motivic series* printed in the same passage, a
separately-typeset object: **all 15 independent entries agree.** One mismatch
would have failed the probe rather than produced a number.

**The sharper question the bean did not ask.** Confirming 5 at one knot does not
test the RULE `#nodes = det` the probe reasons through — if it were true at 4₁
and false elsewhere the probe would be right for the wrong reason. Measured at
four knots: `3_1`→3 (KRSS), `4_1`→5, `6_1`→9, `8_1`→13, node counts read off the
printed matrix widths against exact determinants. All four agree, and all equal
the family formula `1 + 4pm`.

**The verdict is UNCHANGED and the direction matters.** The probe concludes the
open-HOMFLY / Gukov–Stošić bridge FAILS the A_ω gate because `5 ∉ {3,4}`.
Confirming the 5 is real makes that negative **stronger**. Recorded explicitly in
the witness (`effect_on_verdict`) because "count confirmed" is exactly the
headline a later reader could mistake for the bridge being repaired.

## Rider — a float64 in the target probe, and a MEASURED detector blind spot

`aomega_bps_sector_nondegeneracy.py` computed its determinants as
`det_from_alexander((-1) - 1 + (1 / (-1)))`. `1 / (-1)` is **float64** — banned
outright by AGENTS.md §"PROBES ARE NOT EXEMPT". Harmless at these magnitudes,
but a probe's conclusion is an argument nothing re-derives. Fixed to `Fraction`.

**No gate could see it, and that is measured rather than assumed.** All six
source-scanning gates (`mpf_float_source_audit`, `mpf_context_dps_audit`,
`module_const_precision_audit`, `numpy_mpmath_dtype_leak_audit`,
`f64_into_mpmath_audit`, `mpf_mixed_arithmetic_audit`) are silent on the pre-fix
file, and the witness-scanning ratchets never see it because the emitted values
are **integers** that serialise cleanly.

**With a positive control**, because "silent" and "crashed" look identical: a
planted `mpmath.mpf(0.1)` in the same temp copy was reported at line 141 by
`mpf_float_source_audit`, while lines 40 and 42 went unreported. The gate
scanned that exact file and did not see the float division.

New taxonomy row for `docs/audits/2026-08-15-detector-blindness-taxonomy.md`:
**a float64 computation whose result is integral — invisible to every
witness-scanning ratchet because it serialises as an int, and invisible to every
source gate because the spelling is bare `int / int` rather than any flagged
form.**

Probe: `d1b_published_41_quiver_confirms_node_count_probe.py`, 7/7, all four
pre-recorded predictions confirmed.
