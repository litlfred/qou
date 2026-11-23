/-
Copyright (c) 2026 litlfred. All rights reserved.
-/
import QOU.MathlibExt.RSZIsoformalInterface
import QOU.QBeta.A3AntiSelfAdjointLift

/-!
# QOU.QBeta.StokesAmplitudeE — can the Stokes / resurgence route supply the A=3 amplitude `E`? A WALL.

**Scope.**  `QOU.QBeta.A3AntiSelfAdjointLift` (merged #4611) bracketed the A=3 Δ_λ
magnitude lift `r* = μ₃/c₃ ≈ 1.585` to EXACTLY ONE free real degree of freedom: the
anti-self-adjoint off-block amplitude `E`.  Its `amplitude_nonzero` proved any genuine
lift forces `E ≠ 0`; its `amplitude_surjective`/`amplitude_injective` proved `E ↦ factor`
is a bijection, so pinning `E` to hit `r*` **without an independent derivation is a FIT**.
Deriving `E` from the substrate is the open keystone (`qou-jqof`, epic `qou-x631`).

This file asks the assigned question — **can the local Stokes-constant / resurgence /
Écalle-Borel route supply `E`?** — and answers it with a rigorous **WALL**, extending the
retraction PR #4790 (`c1_infinity_isoformalDim_eq_zero`: C1's `∞` is pure isoclinic ⇒ no
local Stokes data) to the amplitude `E` specifically.

**The bridge (MODEL, cited — NOT a fit, NOT a smuggled decomposition).**  The amplitude a
*local* q-Stokes datum can supply is the strictly-off-block part of the q-Stokes matrix.
By RSZ (Astérisque 355, §5.5.2 / Thm 5.5.7) the q-Stokes matrices are **unipotent**
automorphisms inducing the **identity on `gr M₀`**: `St = I + N` with `N` strictly
off-block nilpotent.  `N` carries exactly one coordinate per slope-pairing modulus, and
the number of those moduli is RSZ Thm 3.3.5's isoformal dimension
`d = rszIsoformalDim k r μ = Σ_{i<j} rᵢrⱼ(μⱼ−μᵢ)` (`RSZIsoformalInterface`).  So the
local-Stokes-supplied amplitude is the coordinate sum `∑_{i<d} coeffᵢ·vᵢ`
(`stokesAmplitude`): a linear form with **no constant term** — the zero constant term *is*
the unipotency (identity diagonal), an RSZ import, stated as the model, never claimed as
derived (per §"Defined residual ≠ derived decomposition").  We do NOT assert `E` *is* this;
we assert the honest conditional: **IF `E` is supplied by local Stokes data, THEN it has
this form**, and derive the walls.

**The WALL — two branches, both block the local Stokes route.**

* **Pure-isoclinic branch (scope-(b), proved invariant `rszIsoformalDim_one`).**  When the
  carrier module has a **single** Newton slope (`k = 1` — exactly C1's `∞`, #4790), the
  isoformal dimension is `0` (`rszIsoformalDim_one`), so the local-Stokes amplitude is
  **forced to `0`** (`stokesAmplitude_eq_zero_of_dim_zero`).  Composed with
  `A3AntiSelfAdjointLift.amplitude_nonzero`, a single-slope module's local Stokes data
  **cannot produce the lift** (`pureIsoclinic_local_stokes_cannot_lift`).  The cited
  invariant is the *emptiness of the slope-pairing index set at `k = 1`* — a proved
  dimension bound, licensing scope-(b).

* **Multi-slope branch (scope-(a)).**  A local-Stokes lift therefore **forces** ≥ 2
  distinct slopes (`local_stokes_lift_forces_positive_dim`: `1 ≤ d`).  But when `d ≥ 1` the
  local amplitude is **surjective onto `R`** (`stokesAmplitude_surjective_of_dim_pos`): the
  nonempty isoformal moduli leaves `E` **entirely free** — local Stokes data does **not**
  select its value.  Selecting the point in the moduli is the job of the **global** (`0↔∞`)
  Birkhoff connection matrix — theta-valued, un-started, and NOT local Stokes data (#4790's
  successor W2, `docs/audits/2026-08-01-branch-selection-birkhoff-connection-matrix.md`).

**Net verdict — WALL (scope-(a) with a scope-(b) sub-exclusion).**  The **local**
Stokes-constant / resurgence / Écalle-Borel route provably cannot supply the numeric `E`:
either the carrier is single-slope and local Stokes data gives `E = 0` (no lift,
scope-(b)), or it is multi-slope and local Stokes data leaves `E` free — its value living
in the global Birkhoff matrix, a distinct open object.  This unifies the sibling Stokes
negatives — the naive large-order amplitude gives `2πP ≈ 1` not the GGM `3`
(`2026-08-01-stokes3-largeorder-amplitude-41.md`); the bar-odd ladder resums but is
anchor-blind on the real meridian, its Stokes datum exp-suppressed and fibre-borne
(`2026-08-01-qborel-ecalle-resum-barodd.md`); the ±i phase supplies the Δ_λ *sign* neither
(`2026-08-01-stokes-phase-sign-delta-lambda.md`) — into a single structural statement at the
amplitude level: **the carrier module's LOCAL Stokes moduli is too small to be `E`.**

**Honesty (STRICT).**  Four sorry-free structural theorems (an empty-index vanishing, a
strict-inequality contradiction composing `amplitude_nonzero`, a case split, a
surjectivity witness); no `native_decide`, no trivial-true, no axiom.  The bridge form is a
CITED RSZ model, stated as a conditional, never a derivation of `E`.  The open successor —
`E` from the global Birkhoff matrix — is a §3b dependent conjecture carrier with genuine
content and **NO instance**; discharging it by *choosing* the amplitude to hit `κ` would be
the forbidden fit and is not done.  Nothing fitted, nothing wired; `μ₃/c₃`/AME/`q₀` never
inverted; `q₀`-derivation not routed through.

**Base ring (§7c).**  `stokesAmplitude` and its vanishing: generic `[CommRing R]`.  The
lift/contradiction theorems and the carrier reuse `A3AntiSelfAdjointLift`'s
`[Field R] [LinearOrder R] [IsStrictOrderedRing R]` (the `> 1` ordering + `D⁻¹` Schur
inverse are genuinely archimedean/field).  No `ℝ`, no `Real.*`; the numerics `r* ≈ 1.585`
live only in the Python witness / audit.

## References

- [ramis-sauloy-zhang-2013] https://arxiv.org/abs/0903.0853 (Thm 3.3.5 dimension formula;
  §5.5.2 / Thm 5.5.7 q-Stokes matrices unipotent, identity on `gr M₀`).
- [leitner2026] `QOU.MathlibExt.RSZIsoformalInterface` (`rszIsoformalDim`, `rszIsoformalDim_one`);
  `QOU.QBeta.A3AntiSelfAdjointLift` (`amplitude_nonzero`, `evenFaceCorrection`, `crossTerm`);
  the retraction `docs/audits/2026-08-08-c1-infinity-has-no-stokes-multiplier.md` (PR #4790);
  the global-Birkhoff successor `docs/audits/2026-08-01-branch-selection-birkhoff-connection-matrix.md`;
  the sibling Stokes negatives `docs/audits/2026-08-01-{stokes3-largeorder-amplitude-41,qborel-ecalle-resum-barodd,stokes-phase-sign-delta-lambda}.md`;
  `conj:qdifference-kernel-prolongation-symbol`; bean `qou-jqof`.
-/

noncomputable section

namespace QOU.QBeta.StokesAmplitudeE

open QOU.QBeta.A3AntiSelfAdjointLift
open QOU.MathlibExt.RSZ

/-! ### The local q-Stokes amplitude model (RSZ Thm 5.5.7 unipotency). -/

/-- **The amplitude a LOCAL q-Stokes datum can supply**, as the coordinate sum of the
    strictly-off-block nilpotent part `N` of the unipotent q-Stokes matrix `St = I + N`
    over the `d` slope-pairing moduli (RSZ Thm 3.3.5 supplies `d = rszIsoformalDim`; Thm
    5.5.7 supplies the unipotency ⇒ **no constant term**).

    A linear form with zero constant term: the vanishing at `d = 0` below is the faithful
    RSZ statement that a single-slope module has no strictly-off-block part, NOT a smuggled
    decomposition of `E`. -/
def stokesAmplitude {R : Type*} [CommRing R] (d : ℕ) (coeff v : Fin d → R) : R :=
  ∑ i : Fin d, coeff i * v i

/-! ### Part 1 — pure isoclinic (single slope, `d = 0`): the local amplitude VANISHES. -/

/-- **Zero isoformal moduli ⇒ zero local Stokes amplitude (sorry-free).**  With no
    slope-pairing coordinates (`d = 0`) the coordinate sum is empty, hence `0`.  This is the
    amplitude-level content of RSZ `rszIsoformalDim_one` / #4790's
    `c1_infinity_isoformalDim_eq_zero`: a pure isoclinic module has no local Stokes data to
    BE the amplitude. -/
theorem stokesAmplitude_eq_zero_of_dim_zero {R : Type*} [CommRing R] {d : ℕ}
    (coeff v : Fin d → R) (hd : d = 0) :
    stokesAmplitude d coeff v = 0 := by
  subst hd
  dsimp [stokesAmplitude]
  simp

/-- **C1's `∞` supplies zero local moduli (sorry-free).**  The pure-isoclinic single edge
    `(r, d) = (2, 1)` at C1's `∞` (after the forced ramified pullback, `k = 1`) has
    isoformal dimension `0` (`rszIsoformalDim_one`), so `(rszIsoformalDim 1 r μ).toNat = 0`.
    This is the RSZ input that places C1 in the vanishing branch of Part 2. -/
theorem c1_isoformal_toNat_zero (r μ : Fin 1 → ℤ) :
    (rszIsoformalDim 1 r μ).toNat = 0 := by
  rw [rszIsoformalDim_one]; rfl

/-! ### Part 2 — the scope-(b) sub-exclusion: single-slope local Stokes CANNOT lift. -/

/-- **A single-slope module's local Stokes data cannot produce the A=3 lift (sorry-free).**
    Composing Part 1 with `A3AntiSelfAdjointLift.amplitude_nonzero` (a genuine lift forces
    `E ≠ 0`): if the local-Stokes amplitude is drawn from a zero-dimensional isoformal
    moduli (`d = 0`, pure isoclinic), it equals `0`, so the even-face correction stays at
    the self-adjoint value `≤ 1` — **no lift**.

    **Scope-(b) structural exclusion**, cited invariant = the emptiness of the RSZ
    slope-pairing index set at `k = 1` (`rszIsoformalDim_one`, a proved dimension bound).
    What is excluded is *the local Stokes datum of a single-slope carrier as a source of the
    lift* — not resurgence's role in the magnitude generally, and not the ±i discontinuity's
    existence (proved elsewhere). -/
theorem pureIsoclinic_local_stokes_cannot_lift {R : Type*} [Field R] [LinearOrder R]
    [IsStrictOrderedRing R] {d : ℕ} (A B D Csa : R) (coeff v : Fin d → R) (hd : d = 0)
    (hsa : evenFaceCorrection A (crossTerm B Csa D) ≤ 1) :
    ¬ (1 < evenFaceCorrection A (crossTerm B (Csa + stokesAmplitude d coeff v) D)) := by
  intro hlift
  exact amplitude_nonzero A B D Csa (stokesAmplitude d coeff v) hsa hlift
    (stokesAmplitude_eq_zero_of_dim_zero coeff v hd)

/-! ### Part 3 — the dichotomy: a local-Stokes lift FORCES ≥ 2 distinct slopes. -/

/-- **A local-Stokes lift forces positive isoformal dimension (sorry-free).**  Contrapositive
    of Part 2: if the local-Stokes amplitude produces a genuine lift `> 1`, the moduli
    dimension is `≥ 1`, i.e. the carrier module has ≥ 2 distinct Newton slopes.  A pure
    isoclinic carrier (like C1's `∞`) is thereby excluded as the source of the lift. -/
theorem local_stokes_lift_forces_positive_dim {R : Type*} [Field R] [LinearOrder R]
    [IsStrictOrderedRing R] {d : ℕ} (A B D Csa : R) (coeff v : Fin d → R)
    (hsa : evenFaceCorrection A (crossTerm B Csa D) ≤ 1)
    (hlift : 1 < evenFaceCorrection A (crossTerm B (Csa + stokesAmplitude d coeff v) D)) :
    1 ≤ d := by
  rcases Nat.eq_zero_or_pos d with h0 | hpos
  · exact absurd hlift (pureIsoclinic_local_stokes_cannot_lift A B D Csa coeff v h0 hsa)
  · exact hpos

/-! ### Part 4 — even in the multi-slope branch, local data does NOT pin `E`. -/

/-- **Positive isoformal dimension ⇒ the local amplitude is SURJECTIVE onto `R` (sorry-free).**
    When `d ≥ 1` the coordinate sum reaches every target (fix `coeff ≡ 1`, put the target on
    one coordinate).  So a nonempty local Stokes moduli leaves the amplitude `E` **entirely
    free**: local Stokes data does not select its value.  Mirrors
    `A3AntiSelfAdjointLift.amplitude_surjective` at the moduli level — the value of `E` must
    come from the GLOBAL (`0↔∞`) Birkhoff connection matrix, not from local Stokes data. -/
theorem stokesAmplitude_surjective_of_dim_pos {R : Type*} [CommRing R] {d : ℕ} (hd : 0 < d)
    (t : R) : ∃ v : Fin d → R, stokesAmplitude d (fun _ => 1) v = t := by
  refine ⟨fun i => if i = ⟨0, hd⟩ then t else 0, ?_⟩
  simp only [stokesAmplitude, one_mul]
  rw [Finset.sum_ite_eq' Finset.univ (⟨0, hd⟩ : Fin d) (fun _ => t)]
  simp

/-! ### Part 5 — the OPEN successor: `E` from the GLOBAL Birkhoff matrix (§3b, no instance). -/

/-- **§3b dependent conjecture — the amplitude `E` is supplied by the GLOBAL Birkhoff
    connection matrix, not by local Stokes data.**

    `@conjecture: dependent` (its content depends on the open construction of the global
    `0↔∞` q-monodromy / Birkhoff connection matrix of the carrier module — theta-valued,
    un-started; #4790's successor W2 and
    `docs/audits/2026-08-01-branch-selection-birkhoff-connection-matrix.md`).

    Distinct from `A3AntiSelfAdjointLift.DerivedAmplitudeGivesLift` (which names the DM
    q-cubic prolongation symbol): this carrier records the WALL's positive branch — a
    **multi-slope** carrier whose local Stokes moduli is nonempty (necessary, by
    `local_stokes_lift_forces_positive_dim`), with the amplitude pinned by the **global**
    Birkhoff datum rather than any local Stokes constant.

    **Content-bearing, not self-assuming.**  `multislope` carries the RSZ necessary
    condition (`1 ≤ dim`, an INPUT the geometry must satisfy); `birkhoff_pins` is the forced
    `E ≠ 0` (tied to the lift by `amplitude_nonzero`); `gives_lift` carries the physical
    lift as a hypothesis.  **No instance is supplied**: building the theta-valued Birkhoff
    matrix and reading `E` off it is the open successor; discharging this by *choosing* `E`
    to hit `κ` (`stokesAmplitude_surjective_of_dim_pos` / `amplitude_surjective`) is the
    forbidden fit and is not done. -/
class GlobalBirkhoffSuppliesAmplitude {R : Type*} [Field R] [LinearOrder R]
    [IsStrictOrderedRing R] (A B D Csa E κ : R) : Prop where
  /-- The carrier module has ≥ 2 distinct Newton slopes: its local isoformal moduli is
      nonempty (`1 ≤ dim`).  Necessary for any local Stokes freedom
      (`local_stokes_lift_forces_positive_dim`); it is precisely what C1's pure-isoclinic
      `∞` (`rszIsoformalDim_one = 0`) fails to have. -/
  multislope : ∃ (k : ℕ) (r μ : Fin k → ℤ), 1 ≤ (rszIsoformalDim k r μ).toNat
  /-- The amplitude `E` — pinned by the GLOBAL Birkhoff connection matrix, not any local
      Stokes constant — breaks graded self-adjointness (`E ≠ 0`; forced by the strict lift
      via `amplitude_nonzero`). -/
  birkhoff_pins : E ≠ 0
  /-- and it drives the even-face correction to the physical lift `κ > 1` (unreachable by the
      self-adjoint branching Schur complement, `A3OffBlockDerivation.magnitudeFactor_le_one`). -/
  gives_lift : evenFaceCorrection A (crossTerm B (Csa + E) D) = κ ∧ 1 < κ

/-- Linearity of `stokesAmplitude d coeff` in the coordinate vector `v`:
`stokesAmplitude d coeff (v + w) = stokesAmplitude d coeff v + stokesAmplitude d coeff w`. -/
theorem stokesAmplitude_add_right {R : Type*} [CommRing R] (d : ℕ)
    (coeff v w : Fin d → R) :
    stokesAmplitude d coeff (fun i => v i + w i) =
      stokesAmplitude d coeff v + stokesAmplitude d coeff w := by
  dsimp [stokesAmplitude]
  rw [← Finset.sum_add_distrib]
  refine Finset.sum_congr rfl (fun i _ => ?_)
  ring

end QOU.QBeta.StokesAmplitudeE
