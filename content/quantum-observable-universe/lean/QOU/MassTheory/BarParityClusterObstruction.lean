import Mathlib.Algebra.Ring.Hom.Defs
import Mathlib.Tactic

/-!
# QOU.MassTheory.BarParityClusterObstruction — why raw-trace cumulants miss the bar-even scale

Formalizes the sharpest structural finding of the k(A) additive-cluster negative
(2026-07-18, bean `qou-7uxa`, PR #3875,
`docs/coordination/2026-07-18-ka-additive-cluster-negative-structural-findings.md`):
the raw per-knot trace `tr_M(K)` at `q₀` is **bar-odd**, so any Mayer/Ursell
cluster cumulant built from raw traces carries the wrong bar-parity for the
bar-even absolute mass scale — and the fix the negative identified is to
symmetrize the generators to bar-even first.

The bar involution is abstracted as an arbitrary ring endomorphism `bar : R →+* R`
(with `Function.Involutive bar` where needed), so the results are agnostic to
whether the physical involution is `q ↦ q⁻¹` or the channel-swap `q ↦ −q⁻¹`
(α_EM #3936). `BarEven t := bar t = t`, `BarOdd t := bar t = -t`.

Proved sorry-free over a generic `CommRing`:

* `sym_barEven` — the symmetrization `t + bar t` is always bar-even;
* `barEven_mul` — a product of bar-even elements is bar-even (clusters built from
  symmetrized traces stay bar-even);
* `barOdd_mul_barOdd` — a product of **two** bar-odd elements is bar-even (parity
  `(−1)² = 1`): the pairwise `b₂` channel is bar-even *by count*;
* `cumulant_barParity_mixed` — a connected cumulant `κ = j − p` with `j` bar-odd
  (the joint 2-trace) and `p` bar-even (product of two 1-traces) satisfies
  `bar κ = −j − p`: it is bar-parity **mixed**, not bar-even;
* `cumulant_not_barEven` — such a `κ` is bar-even only in the degenerate case
  `2·j = 0` (the I-par obstruction the negative reported: the raw cumulant is not
  bar-even because the joint-trace part `j` is bar-odd and nonzero);
* `cumulant_barEven_of_symmetrized` — with the generators bar-even-symmetrized
  (`j`, `p` both bar-even) the cumulant **is** bar-even: the productive lead.
-/

namespace QOU.MassTheory.BarParityClusterObstruction

variable {R : Type*} [CommRing R] (bar : R →+* R)

/-- `t` is fixed by the bar involution. -/
def BarEven (t : R) : Prop := bar t = t

/-- `t` is negated by the bar involution. -/
def BarOdd (t : R) : Prop := bar t = -t

/-- **Symmetrization is bar-even.** `t + bar t` is fixed by an involutive `bar`. -/
theorem sym_barEven (hb : Function.Involutive bar) (t : R) :
    BarEven bar (t + bar t) := by
  show bar (t + bar t) = t + bar t
  rw [map_add, hb t]
  ring

/-- A product of two bar-even elements is bar-even. -/
theorem barEven_mul {u v : R} (hu : BarEven bar u) (hv : BarEven bar v) :
    BarEven bar (u * v) := by
  show bar (u * v) = u * v
  rw [map_mul, hu, hv]

/-- A product of two bar-odd elements is **bar-even** (parity `(−1)² = 1`) — the
pairwise `b₂` channel is bar-even by count. -/
theorem barOdd_mul_barOdd {u v : R} (hu : BarOdd bar u) (hv : BarOdd bar v) :
    BarEven bar (u * v) := by
  show bar (u * v) = u * v
  rw [map_mul, hu, hv]
  ring

/-- **Mixed bar-parity of the connected cumulant.** With `j` bar-odd (the joint
2-trace) and `p` bar-even (the product of two 1-traces), the cumulant `κ = j − p`
has `bar κ = −j − p`: neither `κ` (bar-even) nor `−κ` (bar-odd) in general. -/
theorem cumulant_barParity_mixed {j p : R} (hj : BarOdd bar j) (hp : BarEven bar p) :
    bar (j - p) = -j - p := by
  rw [map_sub, hj, hp]

/-- **The I-par obstruction.** A raw-trace cumulant `κ = j − p` (`j` bar-odd joint
trace, `p` bar-even product) is bar-even only if `2·j = 0` — i.e. never, when the
bar-odd joint-trace part is nonzero (and `R` is `2`-torsion-free). This is the
bar-parity FAIL the additive-cluster negative reported. -/
theorem cumulant_not_barEven {j p : R} (hj : BarOdd bar j) (hp : BarEven bar p)
    (hbe : BarEven bar (j - p)) : (2 : R) * j = 0 := by
  have h1 : bar (j - p) = j - p := hbe
  have h2 : bar (j - p) = -j - p := cumulant_barParity_mixed bar hj hp
  have h3 : j - p = -j - p := by rw [← h1, h2]
  linear_combination h3

/-- **The fix (productive lead).** If the generators are bar-even-symmetrized so
that both the joint trace `j` and the product `p` are bar-even, the cumulant
`κ = j − p` **is** bar-even — the bar-even channel the absolute scale requires. -/
theorem cumulant_barEven_of_symmetrized {j p : R} (hj : BarEven bar j)
    (hp : BarEven bar p) : BarEven bar (j - p) := by
  show bar (j - p) = j - p
  rw [map_sub, hj, hp]

end QOU.MassTheory.BarParityClusterObstruction
