---
# qou-8pl2
title: 'PLAUSIBLE-NOT-PROVED: Gell-Mann–Okubo from the crossing-energy splitting'
status: in-progress
pr: 8185
type: task
priority: normal
tags:
    - reorg-2026-10-04
    - 8f-flavour
created_at: 2026-08-06T00:00:00Z
updated_at: 2026-10-10T07:15:50Z
parent: qou-8lxd
---

## UPDATE 2026-08-07 — the question was MIS-POSED; reframed

`QOU/Eightfold/GellMannOkuboIdentity.lean` (sorry-free, generic `[CommRing R]`):

* `gmo_identity` : for the first-order octet ansatz
  `m²(I,Y) = a + b·Y + c·(I(I+1) − Y²/4)`, the combination
  `4m_K² − 3m_η² − m_π²` vanishes **for all a, b, c**.
* `gmo_cannot_discriminate` : two arbitrarily different breaking patterns give
  the SAME value of the combination (zero).
* `gmo_independent_of_breaking_strength` : `b` — the entire hypercharge
  dependence, i.e. the whole content of a breaking mechanism — cancels exactly.

**So GMO has no discriminating power.** If the QOU crossing-energy splitting is
first-order octet it reproduces GMO automatically, and doing so is NOT evidence
for the framework — every first-order octet model does equally well. The
original bean framing ("derive the splitting pattern from the crossing energy")
was asking for something that would prove nothing.

**Both numbers in the old comparison were wrong to compare.** The ~3.3% is the
q-deformation of `dim_q(adjoint)` — a *dimension*, not a mass splitting, and not
a quantity that can appear on either side of GMO. Category error; withdrawn.

## The reframed open question

The only testable content is the **~6% deviation**, which measures the failure
of first-order breaking: second-order terms in the mass operator, plus η–η′
singlet mixing. The framework has derived no second-order term, so it currently
predicts deviation **0**, not 3.3%.

* A derived second-order term giving ≈6% would be a genuine prediction.
* A derived second-order term giving a different value would **falsify** the
  crossing-energy mechanism. That is a real falsification test and it is worth
  running.
* Note η–η′ mixing is entangled with the singlet channel, which at N=2 does not
  exist at all (`RowCapObstruction.lean`) — so this is downstream of `qou-8pl3`.

## Original claim (retained)

The meson mass relation `4 m_K² = 3 m_η² + m_π²` should follow from the
crossing-energy splitting pattern on the `A_2` weight lattice, the kaon
involving a strange-quark braid word of different writhe than the pion.

## Status

**Asserted, never derived.** The chapter previously said the relation "is a
consequence of" the crossing-energy pattern and then, one sentence later, called
the numerical agreement "an open cross-check" — a claim and its own retraction
in the same paragraph. Rewritten (see the `content(eightfold)` honesty pass).

## The one numerical datum

`computations/gmo_meson_crosscheck.py`:
* experimental GMO deviation: `≈ 6%`
* `q`-deformation of the adjoint quantum dimension at `q_0 ≈ 1.11`: `≈ 3.3%`

Same order of magnitude, factor `≈ 2` apart, **no mechanism connecting them**.
This is currently recorded as an unexplained coincidence of scale and must not
be cited as agreement.

## What would settle it

1. Derive the mass operator from the crossing energy
   `E_×(q) = ½(q − q⁻¹)` acting on the octet braid words, and show the GMO
   combination is the eigenvalue relation it induces. Note GMO is conventionally
   an SU(3)-breaking statement about the *linear* mass operator (squared masses
   for mesons); the derivation must reproduce that structure, not just a number.
2. Or show the factor-2 discrepancy is a genuine prediction of the framework
   (i.e. QOU predicts GMO should be violated at ~3.3%, contradicting the ~6%
   observed) — that is a **falsification test**, and running it is more valuable
   than continuing to describe the two numbers as close.

## Blocked on

Both routes are gated on `N = 3` (item 1 of the chapter's open problems) and on
hypercharge `Y` (item 2), since inter-multiplet splittings depend on `Y`. Within
an isospin multiplet the splitting is electromagnetic and comes from the writhe
difference, which IS derived — that sub-case is the honest place to start.

## Progress Update (Round 55 — PR #8185)
- [x] Formalized non-vacuous Lean 4 theorems (`0` `sorry`, `0` vacuity advisories across all 6 static audits) in `folio/quantum-observable-universe/lean/QOU/Eightfold/ColourConjugationGMODeviationAndAsymmetry.lean` and wired into `QOU.lean`.
- [x] Added 50-dps `mpmath` probe `computations/probes/colour_conjugation_gmo_deviation_and_asymmetry_probe.py` and 2-commit stamped witness `computations/probes/colour-conjugation-gmo-deviation-and-asymmetry.witness.json` (`scriptCommitSha: dc490df3193b70802e4608a98cc9402380f4dbcd`, `HEAD: ea791bb906663eb37105b3486abd6e07818699ed`).
- [x] Opened `litlfred/qou#8185` (status kept at `in-progress` per no-unilateral-closure policy).
