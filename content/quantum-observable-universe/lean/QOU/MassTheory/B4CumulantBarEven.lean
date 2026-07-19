/-
# Bar-evenness of the ⁴He writhe-exchange cumulant determinant

The Δ_λ magnitude front (2026-07-18, Vector 3) asks whether **bar-even
symmetrisation** of the connected `b_A = -ln det(I + m·S)` cumulant
(`b4_slater_antisymmetrizer_exchange_sign.py`, #3924) can isolate a mass
(bar-even) part from a decay (bar-odd) part and thereby tame the ⁴He
magnitude overshoot.

This file records the structural obstruction at `A = 4`.  The ⁴He writhe
exchange matrix `S` (diagonal `1`, off-diagonal `sgn·m` with pp = +1,
nn = -1, pn = +1 on the word `ppnn`) has the **symmetric spectrum**
`{±√5, ±1}`, so its shifted determinant has the closed form

  `det (I + m·S) = (1 - 5 m²)(1 - m²)`   =:  `he4WritheDet m`.

That the `4×4` determinant equals this closed form is verified **exactly**
(45-digit `mp.det` agreement, over the concrete symmetric matrix) in the
companion probe
`computations/deltalambda/deltalambda_bareven_b4_magnitude_probe.py`
(assertion `writhe_det_matches_closed_form`).  This file supplies the
other half: the closed form is a function of `m²` alone, hence **even in
`m`** (`he4WritheDet_bar_even`).

Consequence.  The cumulant `b₄ = -ln (he4WritheDet m)` is invariant under
`m ↦ -m`, which is exactly the bar involution `q ↦ q⁻¹` acting on a
bar-odd magnitude.  So at the dominant `A = 4` wall the bar-even
symmetrisation `½(b₄(q) + b₄(q⁻¹))` returns `b₄` unchanged: there is **no
bar-odd part to remove**, and Vector 3 cannot alter the ⁴He cumulant.

This is a *scope-(b) structural exclusion* of bar-even symmetrisation as a
fix for the `A = 4` overshoot (a proved invariant: evenness of the
determinant in `m`), not a scope-(a) numerical miss.  It complements — does
not re-derive — the 2026-06-25 scope-(b) pruning that ⁴He binding must be
bar-even (`docs/audits/2026-06-25-he4-magic-factor-bar-even-pruning.md`):
there the *observable* is forced bar-even; here the *cumulant carrier* is
shown to be already bar-even, so symmetrisation is a no-op.

Base ring: generic `CommRing R` (§7c) — no ordering, no `Real`; the
statement is a polynomial identity in the formal magnitude `m`.

## The deformed A=4 pole and the failed zero-mode regulator (2026-07-19)

`ReebPnMagnitude.ss_det_zero_at_criticality` proves the *2×2 ss-sector*
determinant vanishes at the deformed criticality `g²(1+b²) = 1`
(`b = [2]_v`, the q-deformed pn-degree).  The section below lifts that to the
**full A=4 writhe determinant** and records the structural reason the standard
zero-mode regularisation cannot rescue the cumulant `b₄ = -ln det`:

* `he4DetViaEig` writes the A=4 determinant through the ss eigenvalue `L`
  (`L² = 1 + b²`; classical `L = √5`), factored so the zero mode `(1 - m·L)`
  is explicit.
* `he4DetViaEig_zero_at_pole`: on the pole `m·L = 1` (the derived magnitude
  `g_reeb` sits here, `b4_deformed_sspole_sector_probe.py`) the whole
  determinant vanishes — `b₄ = -ln 0 = +∞`.  So the single-scalar cumulant is
  **exactly critical** at the physical magnitude, not merely large.
* `he4DetReduced_gt_one_at_pole`: the zero-mode-**reduced** determinant (drop
  the vanishing `(1 - m·L)` factor — the standard collective-coordinate
  prescription) equals `2(1 - m²) > 1` for `m² < ½`.  A determinant `> 1` gives
  `b = -ln det < 0`: the reduced regulator is **anti-binding**.  This is the
  Lean-proved reason the reduced-determinant regulator fails (repulsive), a
  scope-(b) structural negative complementing the scope-(a) numerical battery in
  `b4_deformed_sspole_sector_probe.py`.  The binding magnitude is therefore not
  a `-ln det` free energy; the exact zero mode signals a collective-coordinate
  (moduli-volume) contribution — the geometric `Vol·ρ` object — not the loop
  determinant (cf. `ReebPnMagnitude.ss_det_no_linear_term`).
-/
import Mathlib.Tactic.Ring
import Mathlib.Algebra.Order.Field.Basic
import Mathlib.Tactic.Linarith

namespace QOU.MassTheory

variable {R : Type*} [CommRing R]

/-- Closed form of the ⁴He writhe cumulant determinant `det (I + m·S)`,
`S` the `ppnn` writhe exchange matrix with spectrum `{±√5, ±1}`.  (The
`det = this` equality is verified exactly against `mp.det` in
`deltalambda_bareven_b4_magnitude_probe.py`.) -/
def he4WritheDet (m : R) : R := (1 - 5 * m ^ 2) * (1 - m ^ 2)

/-- The ⁴He writhe cumulant determinant factors as `(1 - √5 m)(1 + √5 m)(1 - m)(1 + m)`,
i.e. it is `(1 - 5 m²)(1 - m²)` — exhibiting the symmetric `{±√5, ±1}`
spectrum as the four roots `m ∈ {±1/√5, ±1}`. -/
theorem he4WritheDet_eq (m : R) :
    he4WritheDet m = 1 - 6 * m ^ 2 + 5 * m ^ 4 := by
  unfold he4WritheDet; ring

/-- **⁴He cumulant is bar-even.**  `he4WritheDet` is a function of `m²`
alone, so it is invariant under `m ↦ -m`.  Hence the connected cumulant
`b₄ = -ln (he4WritheDet m)` is even in the magnitude `m`.  Under the bar
involution `q ↦ q⁻¹` acting on a bar-odd magnitude (`m ↦ -m`) this says
`b₄(q) = b₄(q⁻¹)`: bar-even symmetrisation is a **no-op** at `A = 4`, so it
cannot tame the ⁴He magnitude overshoot (the scope-(b) obstruction to
Vector 3). -/
theorem he4WritheDet_bar_even (m : R) : he4WritheDet (-m) = he4WritheDet m := by
  unfold he4WritheDet; ring

/-! ## Deformed A=4 determinant via the ss eigenvalue, and the failed zero-mode regulator -/

/-- The A=4 writhe determinant written through the **ss-sector eigenvalue** `L`
(`L² = 1 + b²`; classical integer pn-degree `b = 2` gives `L = √5`), with the
zero mode `(1 - m·L)` factored out explicitly:
`det(I + m·S) = (1 - m·L)(1 + m·L)(1 - m²)`.  The `(1 ± m·L)` pair is the
species-**symmetric** (pp-sym, nn-sym) sector; the `(1 - m²)` is the Pauli
intra-pair (`λ = ±1`) sector. -/
def he4DetViaEig (L m : R) : R := (1 - m * L) * (1 + m * L) * (1 - m ^ 2)

/-- `he4DetViaEig` collapses to the closed form `(1 - L²m²)(1 - m²)`; with
`L² = 5` this is `he4WritheDet`. -/
theorem he4DetViaEig_eq (L m : R) :
    he4DetViaEig L m = (1 - L ^ 2 * m ^ 2) * (1 - m ^ 2) := by
  unfold he4DetViaEig; ring

/-- With the classical ss eigenvalue `L² = 5`, `he4DetViaEig` is exactly the
classical ⁴He writhe determinant `(1 - 5m²)(1 - m²)`. -/
theorem he4DetViaEig_classical (L m : R) (hL : L ^ 2 = 5) :
    he4DetViaEig L m = he4WritheDet m := by
  rw [he4DetViaEig_eq, hL]; unfold he4WritheDet; ring

/-- **Exact criticality: the A=4 determinant vanishes on the pole.**  When the
magnitude sits on the ss-sector pole `m·L = 1` (the derived `g_reeb` does, since
`g_reeb² (1 + [2]_v²) = 1`, `b4_deformed_sspole_sector_probe.py`), the full A=4
writhe determinant is **zero** — so the single-scalar cumulant `b₄ = -ln det` is
`+∞`.  The construction is exactly critical at the physical magnitude, not merely
large: the ⁴He overshoot is this pole seen through the classical ceiling. -/
theorem he4DetViaEig_zero_at_pole (L m : R) (h : m * L = 1) :
    he4DetViaEig L m = 0 := by
  unfold he4DetViaEig; rw [h]; ring

/-- The **zero-mode-reduced** determinant — drop the vanishing `(1 - m·L)`
factor (the standard collective-coordinate prescription for a functional
determinant with an exact zero mode). -/
def he4DetReduced (L m : R) : R := (1 + m * L) * (1 - m ^ 2)

/-- On the pole `m·L = 1` the reduced determinant is `2(1 - m²)`. -/
theorem he4DetReduced_at_pole (L m : R) (h : m * L = 1) :
    he4DetReduced L m = 2 * (1 - m ^ 2) := by
  unfold he4DetReduced; rw [h]; ring

end QOU.MassTheory

namespace QOU.MassTheory

variable {F : Type*} [Field F] [LinearOrder F] [IsStrictOrderedRing F]

/-- **The reduced regulator is anti-binding.**  On the pole `m·L = 1`, the
zero-mode-reduced determinant `2(1 - m²)` exceeds `1` whenever `m² < ½` (which
the derived magnitude satisfies: `g_reeb² ≈ 0.1996`).  A determinant `> 1` gives
`b = -ln det < 0` — **repulsive**.  This is the Lean-proved reason the standard
zero-mode / reduced-determinant regularisation cannot rescue the b₄ cumulant: it
flips the sign.  Hence the binding magnitude is not a `-ln det` free energy; the
exact zero mode is a collective coordinate (moduli volume), i.e. the geometric
`Vol·ρ` object, not the loop determinant. -/
theorem he4DetReduced_gt_one_at_pole (L m : F) (h : m * L = 1) (hm : m ^ 2 < 1 / 2) :
    1 < he4DetReduced L m := by
  rw [he4DetReduced_at_pole L m h]
  have e : (2 : F) * (1 - m ^ 2) = 2 - 2 * m ^ 2 := by ring
  rw [e]; linarith

end QOU.MassTheory
