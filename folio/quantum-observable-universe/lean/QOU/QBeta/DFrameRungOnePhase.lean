/-
# (D1): the ladder's rung-1 phase IS the counit-minus-trace gap

The bean `qou-cds1` names its own next step:

> The concrete next step is therefore narrower than 'derive alpha':
> **Lean-prove (D1)**, `2*alpha = net(Delta) - tr_M^z(Delta)`.

It is narrower still than the bean says, and this file is what is actually
missing.

## What already existed (corpus-grep, before writing anything)

`QOU/Interactions/qbeta_counit_vs_trace.lean` has carried the analytic core
since 2026-06-16 — two and a half months before the bean asked for it:

* `epsNP h = h^2/2 - h`         the Frobenius counit of `Delta`  (= `net`)
* `trMNP h z = h^2/2 - h*z`     the Ocneanu trace of `Delta`
* `eps_sub_trMNP : epsNP h - trMNP h z = h*(z-1)`   the exact gap
* `agree_iff` : for `h != 0` the two functionals agree iff `z = 1`

A first draft of this file re-derived all four under new names. That was
duplication and is deleted. Nothing here restates them; this imports them.

## What was genuinely missing

The existing file relates the counit to the trace. It never mentions
`alpha = (z-1)*h/2`, so it never says the gap IS twice the ladder's rung-1
phase — and that connection is the whole content of (D1). It is what upgrades
`alpha` from a bare `def` to a derived object, which is the bean's stated goal.

The two `alpha` definitions on `main` do not close it either:
`EigenphaseCarrierVacuity.eigenphase` is built on `markovZC`, i.e. pinned to
the EXCISED convention C; `BraidImageEigenphaseExclusion.alphaOf` is `ℝ`-valued
and function-valued. Neither is a convention-free statement over a general
field, which is what a claim "identically in q and z" requires.

So this file is one bridge theorem plus its sharpness, and nothing else.

## Characteristic two is a real hypothesis, not boilerplate

`2 * (x/2) = x` fails when `2 = 0`. In characteristic two the left side of
(D1) is identically `0` while the gap `h*(z-1)` need not be, so the identity is
FALSE there and `(2 : K) != 0` is load-bearing. Note the imported lemmas do
NOT need it: in `epsNP - trMNP` the `h^2/2` cancels before any division
matters. The hypothesis enters with `alpha`, which carries an uncancelled `/2`.

## Provenance

* IDENTIFICATION: a sibling's, PR #5337 comment 5421747260 (bean `qou-avt5`) —
  "the ladder's phase IS eps - tr_M". Not mine.
* EXACT DERIVATION incl. the factor of 2 that a loose reading of that sentence
  drops: `computations/qbeta/qbeta_d_frame_rung_one_rederivation_probe.py`
  (PR #5864).
* `Delta`'s NF coordinates `[h^2/2, -h/2, -h/2, 0, 0, 0]` are INPUT, rebuilt
  from typed-crossing words by that probe and already encoded in the imported
  `epsNP` / `trMNP`. Not proved here.

No convention is assumed anywhere: `z` is free, and nothing substitutes
`sqrt q/(q+1)` (C) or `q^3/(q^2+1)` (D). Generic field, `h` free, no ordering,
no `q` — §7c.
-/
import QOU.Interactions.qbeta_counit_vs_trace

namespace QOU.QBeta

open QOU.Interactions.QBetaCounitTrace

variable {K : Type*} [Field K]

/-- The Q_beta ladder's rung-1 phase, `alpha = (z-1)*h/2`.

Stated over a general field with `z` and `h` free — unlike
`EigenphaseCarrierVacuity.eigenphase`, which is pinned to the excised
convention C via `markovZC`, and unlike `BraidImageEigenphaseExclusion.alphaOf`,
which is `ℝ`- and function-valued. A claim holding "identically in q and z"
needs the free form. -/
def rungOnePhase (z h : K) : K := (z - 1) * h / 2

/-- **(D1).** Twice the rung-1 phase is exactly the counit-minus-trace gap on
the neutron−proton difference, identically in both variables.

This is the bridge the corpus was missing: `eps_sub_trMNP` gives the gap as
`h*(z-1)`, and this identifies that gap with `2*alpha`. Together they make
`alpha` derived rather than asserted.

`(2 : K) ≠ 0` is necessary — see the module docstring. -/
theorem rungOnePhase_eq_counit_sub_trace (z h : K) (h2 : (2 : K) ≠ 0) :
    2 * rungOnePhase z h = epsNP h - trMNP h z := by
  rw [eps_sub_trMNP]
  unfold rungOnePhase
  field_simp

/-- **The falsifiable content.** Leave the Ocneanu weight on the sigma-
generators as an unknown `w`; then (D1) holds **iff** `w = z`.

So the rung-1 phase does not merely happen to equal the gap — it PINS the
Markov parameter. This is the precise form of the claim that `z` enters the
five-rung ladder in exactly one place, and it is what stops
`rungOnePhase_eq_counit_sub_trace` from being arithmetic on chosen constants.

`h ≠ 0` is necessary and its sharpness is recorded below. -/
theorem generatorWeight_forced (z h w : K) (h2 : (2 : K) ≠ 0) (hh : h ≠ 0) :
    2 * rungOnePhase z h = epsNP h - trMNP h w ↔ w = z := by
  rw [eps_sub_trMNP, rungOnePhase_eq_counit_sub_trace z h h2, eps_sub_trMNP]
  constructor
  · intro hyp
    -- cancel the nonzero `h`, then the shared `- 1`
    have h1 : z - 1 = w - 1 := mul_left_cancel₀ hh hyp
    exact (sub_left_inj.mp h1).symm
  · rintro rfl; rfl

/-- Sharpness of `h ≠ 0`: at the classical point `h = 0` the weight is
genuinely unpinned — (D1) holds for EVERY `w`.

This is the same degeneracy the corpus records when it warns that a theorem
evaluated only at the classical point `q = 1` is convention-agnostic by
accident of sitting on the coincidence, so it says nothing about which
convention is right.

Note this needs NO `(2 : K) ≠ 0`: at `h = 0` both sides vanish even in
characteristic two, so the lemma is strictly stronger than (D1) is there. -/
theorem generatorWeight_unpinned_at_classical (z w : K) :
    2 * rungOnePhase z (0 : K) = epsNP (0 : K) - trMNP (0 : K) w := by
  rw [eps_sub_trMNP]
  unfold rungOnePhase
  simp

end QOU.QBeta
