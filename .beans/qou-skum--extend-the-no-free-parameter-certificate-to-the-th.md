---
# qou-skum
title: Extend the no-free-parameter certificate to the theta channel
status: completed
type: task
priority: high
created_at: 2026-08-07T15:16:34Z
updated_at: 2026-08-07T20:45:29Z
---

The T5 no-free-parameter certificate (`computations/no_free_parameter_certificate.py`,
bean qou-s16e, epic qou-8lxd) makes "every number is traceable to a calibration,
a derived constant, or combinatorics" MECHANICAL rather than agent-policed. Its
own scope note is explicit: **"Scope of the certificate is the mass path only —
other observables are not yet covered."**

The theta/Q_beta channel is exactly such an uncovered observable, and it is
known to contain a free parameter.

PR #4513 proves in Lean (`QOU/QBeta/AfreeThetaConstraint.lean`, sorry-free) that
the channel `S_K = A_omega * kappa * (ln^2 q0 - theta_K^2)` has two anchor
equations in three unknowns, so `A_omega` is a genuine free parameter — one
degree of freedom that nothing internal pins beyond a one-sided `A >= 2.05`.
`ratio_attained` gives an explicit witness `A = (y*S1 - S2)/(kappa*L*(y-1))`
realising ANY ratio `y > 1`, so the underdetermination is proved, not sampled.

`A_omega = 3` is a hardcoded literal in `qbeta_t4_stokes3_crux_probe.py`,
imported from GGM rather than derived. Every theta value in the corpus is
inverted through it and is therefore A_omega-conditioned.

TASK: extend the certificate's import-closure walk beyond the canonical mass
facade to the theta/Q_beta path, so `A_omega = 3` gets classified. Expected
outcome is `UNTRACEABLE` (a bare literal in arithmetic with no calibration tag,
no witness read, no structural identification) — which is the CORRECT answer,
and would turn the circularity into a standing CI-visible fact rather than a
note someone has to remember.

WHY THIS IS THE HIGHEST-LEVERAGE ITEM ON THE ARC: the arc has produced three
consecutive structural negatives (rdmr refuted; ratio-shaped offl candidates
proved unfalsifiable; A_omega = 3 shown to rest only on the literature value).
None of it is enforceable today. The certificate is the mechanism that makes it
enforceable, and it already exists — it just does not reach this channel.

Caveat to carry: the certificate is a high-recall STATIC detector, not a proof
(its own epistemic-scope section). A clean run is evidence, never a theorem.

Cross-refs: PR #4513; docs/scope/2026-08-01-t4-anchor-circularity.md;
docs/scope/2026-08-01-theta-independent-routes.md; beans qou-qnnq, qou-offl,
qou-i3yg, qou-s16e.


---

## 2026-08-07 DONE — and the extension found a detector bug worth more than the extension

Certificate now covers the theta channel. It flags all four literals:
`q0 = 1.11020`, `A_omega = 3`, `S_muon`, `S_proton`. Mass-path entry points
stay at 0 untraceable; self-test passes (14 synthetic cases).

**BUG FOUND — bare numeric assignments were invisible.** The classifier's own
comment said a literal counts as arithmetic if it is "operand of a BinOp, OR a
bare module-level constant assignment", but NO code path implemented the second
case. Consequence:

    S_muon = +0.00968298   -> UnaryOp -> CAUGHT
    q0     =  1.11020      -> bare Constant -> INVISIBLE

Identical values, opposite verdicts, purely on a redundant leading sign — and
the bare form is the commonest way to type a magic number. Demonstrated with a
minimal AST test, then fixed.

Closing it took untraceable from 2 to 72. Nearly all of the new hits were
`experimental_constants.py`, a tagged CODATA/PDG/SnapPy reference module with
per-entry uncertainties — the same "calibration by construction" category as the
already-whitelisted `codata_*` modules; it had simply never been added, because
every entry in it is a plain `NAME = <literal>` and so was invisible. Added.
Back to 4, all in the theta channel.

**SECOND GAP — `A_omega = 3` was waved through as `structural`** because
3 is in STRUCTURAL_INTS. That whitelist is for rep dimensions, group orders,
exponents and indices; a physical channel coefficient is none of those. Added an
`ADJUDICATED_FREE` mechanism (keyed by assigned name, each entry stating why)
that overrides the small-int whitelist. A_omega is now correctly UNTRACEABLE,
citing the Lean proof that it is a genuine free parameter.

NET EFFECT: the circularity is now CI-visible. `--strict` would fail on the
theta channel until A_omega is either derived or explicitly tagged.

Note `q0 = 1.11020` is untraceable AND wrong — canonical is ~1.1099786. That
belongs with the other hardcoded-literal issues in qou-i3yg.
