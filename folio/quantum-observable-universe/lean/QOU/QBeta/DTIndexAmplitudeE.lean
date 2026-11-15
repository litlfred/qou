/-
Copyright (c) 2026 litlfred. All rights reserved.
-/
import Mathlib.Tactic

/-!
# QOU.QBeta.DTIndexAmplitudeE — the DT-invariant / 3d-index / graded-Euler route is BAR-PARITY excluded from supplying the A=3 anti-self-adjoint amplitude `E`

**Scope (read this first).**  `QOU.QBeta.A3AntiSelfAdjointLift` (merged #4611) bracketed the
observed A=3 magnitude lift `r* = μ₃/c₃ ≈ 1.585 > 1` to **exactly one free real degree of
freedom** — the anti-self-adjoint off-block amplitude `E := C + σ B` (deviation of the off-block
`C` from its graded-self-adjoint value `−(σ B)`).  It proved `E ↦ factor` is an affine bijection
(`factor = factor_sa − B·D⁻¹·E/A`, `amplitude_surjective`/`amplitude_injective`), and that any
genuine lift **forces** `E ≠ 0` (`amplitude_nonzero`).  Deriving `E` from the substrate — never
fitting it to `r*` — is the open keystone `qou-jqof` (epic `qou-x631`, convergence bean
`qou-3dya`).

**This file's angle — the DT-invariant / 3d-index / graded-Euler substrate route.**  The corpus
already establishes that the per-partition binding factor is a Behrend-signed Donaldson–Thomas /
3d-index graded Euler characteristic, `Δ_λ = (−1)^{n(λ)}·dim V_λ = DT(𝓑_λ)` (sorry-free, all `n`;
`DeltaLambdaDTIndexGeneralN`), and that the DT/graded-Euler machinery over the Wedderburn blocks
lands integers — the sandwich normalization `Σ_{λ⊢3} Δ_λ = −2` and the count `3` / `{3,4}`
(`StokesDTCountExceedsRecursionOrder`).  The forward question this file attacks:

> Does the DT-invariant / 3d-index graded-Euler DATA supply the numeric amplitude `E` that hits
> `r*` — i.e. is `E` a Behrend-signed DT count / graded Euler characteristic of a
> substrate-forced moduli?

**Verdict — scope-(b) structural exclusion (invariant: bar-parity).**  **NO.**  The DT-index /
3d-index / graded-Euler datum is, by definition, an **integer** (a Behrend-weighted virtual point
count, equivalently an alternating dimension sum `χ = Σ_k (−1)^k dim(G)_k ∈ ℤ`).  Every integer —
indeed every element of the prime field fixed by the bar involution — is **bar-EVEN**
(`σ x = x`, `dtIndex_barEven` via `map_intCast`).  But the anti-self-adjoint amplitude `E` is
**bar-ODD** (`σ E = −E`): this is *derived*, not assumed (`amplitude_barOdd`) — the physical
mass / C1 face carries a **bar-even** Berezinian cross-term `B·D⁻¹·C` (the parity of the ratio
`r* = μ₃/c₃`, both moments bar-even; `BerezinianSelfAdjointCrossTerm`), which forces the off-block
`C` bar-odd (`crossTermBarEven_imp_C_barOdd`), hence `E = C + σ B` bar-odd.  A nonzero element
**cannot** be both bar-even and bar-odd (`barEven_barOdd_eq_zero`, invariant: `char R ≠ 2`).

Therefore (`dtIndex_cannot_supply_amplitude`, sorry-free): the nonzero anti-self-adjoint amplitude
`E` that a genuine lift forces is **NOT** any DT-invariant / 3d-index / graded-Euler value.  The
DT route lives entirely in the **bar-even** (self-adjoint, real π-phase, `≤ 1`) sector; `E` lives
in the **bar-odd** (anti-self-adjoint, `±i` / π/2 resurgent-Stokes-phase) sector.

**What this buys, and its honest limit.**  This is a genuine *proved invariant* (bar-parity), so
it is a scope-(b) exclusion — but a **route-scoped** one: it excludes the DT / graded-Euler
integer count from *being* `E`, not the amplitude `E` from being derivable.  It **hands `E` back
to the bar-odd sector** — the resurgent Stokes / DM q-cubic prolongation symbol
(`conj:qdifference-kernel-prolongation-symbol`), which is the ±i (π/2) resurgent phase, bar-ODD,
the correct parity.  This *converges from a fresh direction* with the Stokes route a sibling
agent is on (bean `qou-jqof`): the DT-index attack does not merely fail — it *proves* the amplitude
cannot be a DT count and points at Stokes as the only remaining home.  It is fully consistent with
`amplitude_surjective` (some real `E` hits `r*`): that witness is a bar-odd geometric scalar, never
a DT integer.

**Why not a fit; why no axiom of the conclusion.**  Nothing here inverts `r*`, `μ₃`, `c₃`, AME,
CODATA, or `q₀`.  There is **no** conjecture class carrying `E`'s value — the file is a pure
*limitative* (impossibility) result, so there is nothing to launder.  The one physical input taken
as a hypothesis is the **bar-EVEN parity of the mass-face cross-term** (an established parity
datum, `BerezinianSelfAdjointCrossTerm` / `OddDecayWeightParity`), which is a *sub-hypothesis about
the observable's parity* — not the conclusion; the theorem DERIVES `E`'s bar-oddness and then the
exclusion from it.

**Base ring (§7c).**  Generic `{R : Type*} [Field R]` throughout (scalar inverses `D⁻¹` genuinely
required — the §7c `[Field R]` inverse carve-out); the char≠2 collapse adds `[CharZero R]` (the
only archimedean-adjacent hypothesis, and the weakest one that gives `(2 : R) ≠ 0`; a
`LinearOrderedField` such as `ℝ` is `CharZero`, so downstream specialisation is free).  No `ℝ`, no
`Real.*`; the numerics `r* ≈ 1.585`, `μ₃`, `c₃`, and the DT integers `−2` / `3` live only in the
Python witness / audit, downstream of the substrate→archimedean wall.

**Relation to the established corpus bar-parity invariant.**  The bar-parity *exclusion
principle* is already accepted corpus infrastructure — `QOU.BraidKnot.BarParityInvariant`
(`barEven_barOdd_forces_zero`, bean `qou-ph2a` / `s5bb`) proves the same "bar-even ∧ bar-odd ⇒ 0"
filter at the **function** level (`f(q⁻¹) = ±f(q)` for `f : K → K`, `q ↦ q⁻¹` concrete).  This file
is the **element / scalar** analog (`σ : R →+* R` acting on scalars — the model in which the A=3
off-blocks `B, C, D, E` live), and its genuinely new step is `dtIndex_barEven`: a DT-index / 3d-index
/ graded-Euler value is an **integer**, hence bar-even, so the DT route falls on the excluded (`≤ 1`,
self-adjoint) side of that established filter and cannot supply the bar-odd amplitude `E`.

## References

- [leitner2026] `QOU.QBeta.A3AntiSelfAdjointLift` (`amplitude_nonzero` — the lift forces `E ≠ 0`;
  `amplitude_surjective`/`amplitude_injective` — `E` is the single free/unique DOF);
  `QOU.QBeta.A3OffBlockDerivation` (`magnitudeFactor_le_one` — the self-adjoint branching is a
  reduction `≤ 1`; `offBlockNum_bar_odd`, `branching_graded_selfadjoint` — the branching parity
  data); `QOU.QBeta.BerezinianSelfAdjointCrossTerm` (self-adjoint ⇒ bar-even cross-term — the
  physical parity of the mass face); `conj:qdifference-kernel-prolongation-symbol` (the bar-ODD
  resurgent Stokes / DM q-cubic datum that WOULD derive `E`); `docs/coordination/option-e.md`
  (ROUTE 2-c); beans `qou-jqof` / `qou-3dya`.
- [wenzl1988] Wenzl, "Hecke algebras of type Aₙ and subfactors", Invent. Math. 92 (1988) 349-383
  (the Markov trace weights on the Wedderburn blocks).
- [donagi-markman1996cubics] https://arxiv.org/abs/alg-geom/9408004 §1 (the cubic condition that
  would pin the off-block amplitude geometrically — bar-odd, not a DT integer).
-/

noncomputable section

namespace QOU.QBeta.DTIndexAmplitudeE

/-! ### Bar-parity predicates.

`σ : R →+* R` is the bar involution `q ↦ q⁻¹` (a ring homomorphism).  An element is **bar-even**
when `σ` fixes it (real π-phase / self-adjoint sector) and **bar-odd** when `σ` negates it
(`±i` / π/2 resurgent-Stokes-phase / anti-self-adjoint sector). -/

/-- Bar-even: fixed by the bar involution.  The self-adjoint / real-π-phase sector; the mass /
    C1 (`cosh`) face and every integer-valued DT-index / graded-Euler characteristic live here. -/
def BarEven {R : Type*} [Ring R] (σ : R →+* R) (x : R) : Prop := σ x = x

/-- Bar-odd: negated by the bar involution.  The anti-self-adjoint / `±i`-π/2-phase sector; the
    GGM decay (`sinh`) face and the resurgent-Stokes amplitude `E` live here. -/
def BarOdd {R : Type*} [Ring R] (σ : R →+* R) (x : R) : Prop := σ x = -x

/-! ### The DT-index / graded-Euler value is BAR-EVEN. -/

/-- **A DT-index / 3d-index / graded-Euler value is bar-even (sorry-free).**  A Behrend-signed DT
    count, a rotated 3d-index, or a graded Euler characteristic `χ = Σ_k (−1)^k dim(G)_k` is an
    **integer**; the bar involution (a ring homomorphism) fixes the image of `ℤ` in `R`
    (`map_intCast`).  So every such value is bar-even — it lives in the self-adjoint / real-π-phase
    sector, the same sector as the `≤ 1` self-adjoint branching factor. -/
theorem dtIndex_barEven {R : Type*} [Ring R] (σ : R →+* R) (d : ℤ) :
    BarEven σ ((d : R)) := by
  show σ ((d : R)) = (d : R)
  exact map_intCast σ d

/-! ### A nonzero element cannot be both bar-even and bar-odd (invariant: char ≠ 2). -/

/-- **Bar-even ∧ bar-odd ⇒ zero (sorry-free; invariant: `char R ≠ 2`).**  If `σ x = x` (bar-even)
    and `σ x = −x` (bar-odd) then `x = −x`, so `2·x = 0`; in a field of characteristic zero
    `(2 : R) ≠ 0`, hence `x = 0`.  The bar-parity sectors intersect only at `0`. -/
theorem barEven_barOdd_eq_zero {R : Type*} [Field R] [CharZero R] (σ : R →+* R) (x : R)
    (he : BarEven σ x) (ho : BarOdd σ x) : x = 0 := by
  have hxx : x = -x := he.symm.trans ho
  have h2 : (2 : R) * x = 0 := by linear_combination hxx
  have h2ne : (2 : R) ≠ 0 := by norm_num
  exact (mul_eq_zero.mp h2).resolve_left h2ne

/-- **A nonzero bar-odd element is not equal to any bar-even element (sorry-free).**  The general
    limitative core: the bar-odd amplitude `E ≠ 0` cannot coincide with any bar-even quantity —
    in particular with any DT-index / graded-Euler value (`dtIndex_barEven`). -/
theorem barOdd_ne_barEven {R : Type*} [Field R] [CharZero R] (σ : R →+* R)
    (E x : R) (hEodd : BarOdd σ E) (hEne : E ≠ 0) (hxeven : BarEven σ x) : E ≠ x := by
  intro h
  subst h
  exact hEne (barEven_barOdd_eq_zero σ E hxeven hEodd)

/-! ### The anti-self-adjoint amplitude `E` is BAR-ODD (derived, not assumed). -/

/-- **A bar-even mass-face cross-term forces the off-block `C` bar-ODD (sorry-free).**  The
    physical mass / C1 face carries a **bar-even** Berezinian cross-term `t = B·D⁻¹·C`
    (`BerezinianSelfAdjointCrossTerm`; the parity of `r* = μ₃/c₃`).  With the branching datum
    `B` bar-odd (`σ B = −B`, `A3OffBlockDerivation.offBlockNum_bar_odd`) and the odd diagonal `D`
    bar-even (`σ D = D`, the bar-conjugate 1-dim blocks give `D = a + σ a`), applying `σ` to `t`
    gives `−B·D⁻¹·σ C = B·D⁻¹·C`; cancelling the nonzero `B·D⁻¹` yields `σ C = −C`.  So the
    off-block that produces a bar-even mass face is itself bar-odd. -/
theorem crossTermBarEven_imp_C_barOdd {R : Type*} [Field R] (σ : R →+* R)
    (B C D : R) (hB : B ≠ 0) (hD : D ≠ 0)
    (hBodd : BarOdd σ B) (hDeven : BarEven σ D)
    (hcross : BarEven σ (B * D⁻¹ * C)) : BarOdd σ C := by
  simp only [BarEven, BarOdd] at *
  rw [map_mul, map_mul, map_inv₀, hBodd, hDeven] at hcross
  -- hcross : -B * D⁻¹ * σ C = B * D⁻¹ * C
  have hBD : B * D⁻¹ ≠ 0 := mul_ne_zero hB (inv_ne_zero hD)
  have h1 : B * D⁻¹ * σ C = B * D⁻¹ * (-C) := by linear_combination -hcross
  exact mul_left_cancel₀ hBD h1

/-- **The anti-self-adjoint amplitude `E = C + σ B` is bar-ODD (sorry-free).**  From `C` bar-odd
    (`crossTermBarEven_imp_C_barOdd`), `B` bar-odd, and `σ` involutive (`σ (σ B) = B`):
    `σ(C + σ B) = σ C + B = −C + B = −(C + σ B)`.  `E` sits in the anti-self-adjoint /
    resurgent-Stokes-phase sector — the OPPOSITE bar-parity from any DT-index value. -/
theorem amplitude_barOdd {R : Type*} [Field R] (σ : R →+* R)
    (B C D : R) (hB : B ≠ 0) (hD : D ≠ 0) (hinv : ∀ x, σ (σ x) = x)
    (hBodd : BarOdd σ B) (hDeven : BarEven σ D)
    (hcross : BarEven σ (B * D⁻¹ * C)) :
    BarOdd σ (C + σ B) := by
  have hCodd : σ C = -C := crossTermBarEven_imp_C_barOdd σ B C D hB hD hBodd hDeven hcross
  have hBodd' : σ B = -B := hBodd
  show σ (C + σ B) = -(C + σ B)
  rw [map_add, hinv B, hCodd, hBodd']
  ring

/-! ### The scope-(b) exclusion: no DT-index value supplies the lift amplitude. -/

/-- **THE SCOPE-(b) STRUCTURAL EXCLUSION (sorry-free; invariant cited: bar-parity + `char ≠ 2`).**
    The nonzero anti-self-adjoint amplitude `E = C + σ B` that a genuine A=3 lift forces
    (`A3AntiSelfAdjointLift.amplitude_nonzero` supplies `hlift : C + σ B ≠ 0`) is **NOT** equal to
    any DT-invariant / 3d-index / graded-Euler value `(d : R)`, `d : ℤ`.

    The DT datum is bar-even (`dtIndex_barEven`); `E` is bar-odd (`amplitude_barOdd`, derived from
    the bar-even mass-face cross-term); a nonzero element cannot be both (`barEven_barOdd_eq_zero`).
    So the DT-invariant / 3d-index / graded-Euler route — which produces integer Behrend counts —
    **cannot** supply the amplitude that hits `r*`.  The amplitude belongs to the bar-ODD
    resurgent-Stokes / DM q-cubic sector (`conj:qdifference-kernel-prolongation-symbol`), not the
    bar-EVEN DT-index sector. -/
theorem dtIndex_cannot_supply_amplitude {R : Type*} [Field R] [CharZero R] (σ : R →+* R)
    (B C D : R) (hB : B ≠ 0) (hD : D ≠ 0) (hinv : ∀ x, σ (σ x) = x)
    (hBodd : BarOdd σ B) (hDeven : BarEven σ D)
    (hcross : BarEven σ (B * D⁻¹ * C))
    (hlift : C + σ B ≠ 0) (d : ℤ) :
    C + σ B ≠ (d : R) :=
  barOdd_ne_barEven σ (C + σ B) (d : R)
    (amplitude_barOdd σ B C D hB hD hinv hBodd hDeven hcross) hlift (dtIndex_barEven σ d)

end QOU.QBeta.DTIndexAmplitudeE
