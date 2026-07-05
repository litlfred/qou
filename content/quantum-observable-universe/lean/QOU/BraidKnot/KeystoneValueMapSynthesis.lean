import QOU.BraidKnot.KeystoneSelfDualSpectralNarrowing
import QOU.BraidKnot.KeystonePerronFrobeniusGroundState

/-!
# Keystone value step: the three-leg synthesis — the value-map target is uniquely `d_q`

The value-step reframe narrows the keystone target vector via three structural inputs (see
`docs/audits/2026-07-05-keystone-selfduality-spectral-narrowing.md`):

* **(A) Frobenius pairing** — the quantum-dimension vector `d` is the orthogonal system's vacuum
  overlap and is *self-dual* (`d(λ′) = d(λ)`), so it lies in the `C = +1` sector
  (`KeystoneSelfDualSpectralNarrowing.vacuumRow_conj_invariant`).  Here that self-duality enters as
  the hypothesis `C d = d`.
* **(B) Perron–Frobenius / Ocneanu–Wenzl selection** — a positive, normalised ground eigenvector of
  the fusion operator is uniquely `d` (`PerronFrobeniusGroundState.eq_d_of_normalized`).
* **(C) Self-duality** — on the `C = +1` self-dual sector the modular `S` (`S² = C`) has eigenvalues
  `±1` (`eigenvalue_selfdual_sector_pm_one`).

This file composes the three into a single statement `keystone_value_map_pinned`: a positive eigenvector
of the fusion operator, normalised at one index and simultaneously an `S`-eigenvector, is **equal to
`d_q`** *and* its `S`-eigenvalue is `±1`.  No new hypotheses beyond the three legs; the proof is a pure
composition of the already-proved lemmas, so it is sorry-free.

**Scope.** Keystone value step (s013).  Conditional on the same owner-gated instance as leg (B) (the
physical fusion category whose PF eigenvector is the *Hecke* `d_q`); this file states the *synthesis
implication*, not the physics.

Base ring: an ordered field `[Field R] [LinearOrder R] [IsStrictOrderedRing R]` (leg (B) positivity;
leg (C) needs a field for the eigenvalue argument).
-/

namespace QOU.BraidKnot.Keystone

open Matrix

variable {ι R : Type*} [Fintype ι] [DecidableEq ι] [Field R] [LinearOrder R] [IsStrictOrderedRing R]

/-- **Keystone value-map synthesis (sorry-free): the target is uniquely `d_q`, self-dual, and its
`S`-eigenvalue is `±1`.**

Given
* a self-dual transform `T` (`S² = C`, leg (C)),
* the Perron–Frobenius selection `[PerronFrobeniusGroundState N rho d]` (leg (B)),
* the self-duality of the quantum dimensions `C d = d` (leg (A): `d` lies in the `C = +1` sector),

any positive eigenvector `v` of the fusion operator `N` at the Frobenius eigenvalue that is normalised
to agree with `d` at one index `k` and is simultaneously an `S`-eigenvector with eigenvalue `ζ`
satisfies **`v = d` and `ζ² = 1`**.  So the value-map target is pinned to the quantum-dimension vector,
which sits in the self-dual sector where `S` acts by `±1` — the full narrowing, in one line. -/
theorem keystone_value_map_pinned
    (T : SelfDualSTransform ι R)
    {N : Matrix ι ι R} {rho : R} {d : ι → R} [PerronFrobeniusGroundState N rho d]
    (hCfix : T.C.mulVec d = d)
    (v : ι → R) (hv_pos : ∀ i, 0 < v i) (hv_eig : N.mulVec v = rho • v)
    (k : ι) (hnorm : v k = d k)
    (ζ : R) (hSeig : T.S.mulVec v = ζ • v) :
    v = d ∧ ζ ^ 2 = 1 := by
  have hvd : v = d :=
    PerronFrobeniusGroundState.eq_d_of_normalized v hv_pos hv_eig k hnorm
  refine ⟨hvd, ?_⟩
  have hv_ne : v ≠ 0 := fun h => by simpa [h] using hv_pos k
  have hvCfix : T.C.mulVec v = v := by rw [hvd]; exact hCfix
  exact eigenvalue_selfdual_sector_pm_one T hv_ne hvCfix ζ hSeig

/-- Corollary of leg (B): the value-map target is the *unique* such vector — two positive,
`k`-normalised fusion-ground eigenvectors agree (independent of the self-dual transform). -/
theorem keystone_value_map_unique
    {N : Matrix ι ι R} {rho : R} {d : ι → R} [PerronFrobeniusGroundState N rho d]
    (v w : ι → R) (hv_pos : ∀ i, 0 < v i) (hv_eig : N.mulVec v = rho • v)
    (hw_pos : ∀ i, 0 < w i) (hw_eig : N.mulVec w = rho • w)
    (k : ι) (hvk : v k = d k) (hwk : w k = d k) : v = w :=
  PerronFrobeniusGroundState.ground_state_unique v w hv_pos hv_eig hw_pos hw_eig k hvk hwk

end QOU.BraidKnot.Keystone
