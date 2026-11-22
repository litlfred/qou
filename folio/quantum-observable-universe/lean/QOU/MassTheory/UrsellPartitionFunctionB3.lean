import QOU.MassTheory.MayerThreeBodySign
import Mathlib.Tactic

/-!
# The corpus `b₃` is minus the third Ursell function of a lattice gas — and the sign is Mayer's

Bean `qou-rwhv` asked for the partition function `Ξ` whose cluster (Mayer) expansion has the
corpus's connected three-body cumulant as its third Ursell coefficient. This file records the
answer at the level a generic commutative ring can state it, and the one ordered-field fact that
settles the sign. Audit: `docs/audits/2026-09-12-ursell-partition-function-for-b3.md`; probe:
`computations/probes/ursell_partition_function_for_b3_probe.py`.

## The objects

* **The canonical partition function of a cluster** `S` is the product of its bond factors,
  `Z_S = ∏_{e ⊆ S} f_e`. In the framework `f_e = μ_e ∈ (0,1)` is the trace of the interface
  letter, and `Z_S = tr_M(W_atom(S)) / tr_M(W_free(S))` by connected-sum multiplicativity of the
  Markov trace (`QOU.MathlibExt.MonotoneWordFactorizes.tr_stabWord_eq_prod_tr`; re-measured on the
  live alternating-core word in the probe, to `1e-40`).
* **The Ursell functions** `φᵀ_S` are defined by the cluster property
  `Z_S = Σ_{π ∈ Π(S)} ∏_{B ∈ π} φᵀ_B` (Jansen–Kolesnikov, `library/s10955-022-02992-6/`, p. 5),
  equivalently as the sum over connected spanning graphs of `∏ g_e` with the Mayer variable
  `g_e = f_e − 1`. `cluster3` / `phi4_eq_connected_sum` are those two descriptions agreeing.
* **The grand-canonical partition function** of the same cluster is
  `Ξ_S(z) = Σ_{T ⊆ S} z^T Z_T` — a hard-core lattice gas on the nucleon sites, activity `z_i`
  per site, pair weight `μ_e`. Its multilinear log is `ln Ξ_S = Σ_T z^T φᵀ_T` (the exponential
  formula; verified symbolically in the probe, `∂³ ln Ξ / ∂z₁∂z₂∂z₃ |₀ = φᵀ₃`). That `Ξ` is the
  partition function the bean asked for: polymers = nucleons, weight `g = μ − 1`, compatibility
  = hard core on sites, ensemble = grand canonical over the sub-clusters of a fixed nucleus.
* **The corpus's multiplicative assembly** is `W(S) = 1 − Z_S` (`MayerThreeBodySign`), and its
  cumulants are Boolean-lattice (inclusion–exclusion) inversions of `W`
  (`QOU.Mass.PairwiseCumulantVanishing.b3`, `b4`).

## What is proved

1. `b3corpus_eq_neg_phi3` — `b₃^corpus = −φᵀ₃`, exactly, as a ring identity (the 400/400 of the
   2026-08-30 probe, in closed form).
2. `boolean3_eq_phi3` / `b4corpus_eq` — *why* it holds at `n = 3` and *why* it fails at `n = 4`:
   the Boolean inversion of a bond-multiplicative `Z` is the sum over spanning edge sets with **no
   isolated vertex**, the Ursell function is the sum over **connected** ones, and the smallest
   isolated-vertex-free disconnected graph is two disjoint edges on four vertices. So
   `b₄^corpus = −φᵀ₄ − (g₁₂g₃₄ + g₁₃g₂₄ + g₁₄g₂₃)`, and the defect is nonzero (`matching_defect`).
3. `phi3_pos` / `b3corpus_neg` — on `f ∈ (0,1)` the third Ursell function is **strictly
   positive**, so `b₃^corpus < 0` for **every** bond triple, non-uniform included. There is no
   threshold: `MayerThreeBodySign.lt_of_b3_pos`'s `fpn > 2/3` was the bound obtained by leaving
   `P₃ ≥ 0` free; once `P₃` is the bond product it can never be met
   (`b3corpus_uniform_closed_form`: `b₃ = −(1−f)²(f+2)`).
4. `restored_eq_neg_activity` — the 2026-08-30 "restore the alternation" prescription
   `b_n = (−1)^{n−1} φᵀ_n` is the coefficient of `−ln(Ξ/Ξ_free)` at **negative activity**
   `z ↦ −z`. The corpus's uniform `b_n = −φᵀ_n` is that coefficient at positive activity, i.e.
   the Mayer expansion's own sign. Nothing in the classical theory supplies `+φᵀ₃` for a gas of
   pair factors below `1`.

## What this says about the 2026-08-30 reading

`docs/audits/2026-08-30-ursell-alternating-sign-and-the-b3-obstruction.md` §3 concluded that
`MayerThreeBodySign`'s negative `b₃` is "a missing `(−1)^{n−1}`, not a physical obstruction".
Items 3–4 reverse that: the alternation of `φᵀ_n` is *already* what makes the corpus `b₃`
negative, and restoring it a second time names no ensemble. Within the Mayer vocabulary a
positive connected three-body coefficient at positive activity needs a bond factor **above** `1`
(an attractive Mayer channel, `g > 0`), which no letter of the production word has — scope (a)
for that last clause, measured in the probe. The magnitude `2.2511` MeV recorded there is
`+φᵀ₃` at the deuteron-pinned scale and inherits the negative-activity reading: it is not a
postdiction of a derived quantity.

## Base ring (§7c)

Everything through item 2 and item 4 is a polynomial identity over a generic `CommRing R`. Item
3 needs an ordering and is stated over `[Field K] [LinearOrder K] [IsStrictOrderedRing K]`,
mirroring `MayerThreeBodySign`, which it imports so that `b3corpus_uniform_eq_mayerSign` can tie
the two definitions of `b₃` together on the nose.

-- Ref: [jansen2022cluster] https://doi.org/10.1007/s10955-022-02992-6 — Ursell functions by
   the cluster property, alternating sign on non-negative potentials (§3.1).
-- Ref: [leitner2026] docs/audits/2026-08-08-binding-functional-attack-vectors-and-li2q-guard.md
   §10a — `μ = e^{−B/α}`, the Boltzmann identification the Mayer variable rests on.
-/

namespace QOU.MassTheory.UrsellPartitionFunctionB3

section Generic

variable {R : Type*} [CommRing R]

/-! ## Ursell functions, `n ≤ 3` -/

/-- The Mayer variable of a bond factor: `g = f − 1`. -/
def mayer (f : R) : R := f - 1

/-- The second Ursell function: the single edge. -/
def phi2 (g : R) : R := g

/-- The third Ursell function: the four connected spanning graphs on three labelled vertices —
the triangle and the three paths. -/
def phi3 (g12 g13 g23 : R) : R := g12 * g13 * g23 + g12 * g13 + g12 * g23 + g13 * g23

/-- The canonical partition function of a three-cluster with bond factors `f_e`: the product of
the bond factors, which is the trace ratio `tr_M(atom)/tr_M(free)` by bond multiplicativity. -/
def Z3 (f12 f13 f23 : R) : R := f12 * f13 * f23

/-- **The cluster property at `n = 3`.** `Z_S = Σ_{π ∈ Π(S)} ∏_{B ∈ π} φᵀ_B` over the five set
partitions of a three-set (`{123}`, three of type `2+1`, and `1+1+1`), with `φᵀ_{i} = 1`. This is
the defining relation of the Ursell functions, and it is what makes `φᵀ_T` the coefficient of
`z^T` in `ln Ξ` (exponential formula). -/
theorem cluster3 (f12 f13 f23 : R) :
    Z3 f12 f13 f23
      = 1 + phi2 (mayer f12) + phi2 (mayer f13) + phi2 (mayer f23)
        + phi3 (mayer f12) (mayer f13) (mayer f23) := by
  unfold Z3 phi2 phi3 mayer; ring

/-! ## The corpus assembly and its Boolean cumulants -/

/-- The multiplicative assembly of `MayerThreeBodySign`: `W(S) = 1 − Z_S`. -/
def W (Z : R) : R := 1 - Z

/-- The corpus's connected three-body cumulant on a triangle of bond factors: the Boolean
(inclusion–exclusion) inversion `W(123) − W(12) − W(13) − W(23)`, singletons carrying `W = 0`.
This is `QOU.Mass.PairwiseCumulantVanishing.b3` evaluated on the multiplicative binding. -/
def b3corpus (f12 f13 f23 : R) : R :=
  W (Z3 f12 f13 f23) - W f12 - W f13 - W f23

/-- **The identity.** The corpus's three-body cumulant is exactly minus the third Ursell function
of the Mayer variables — for every triple, uniform or not. -/
theorem b3corpus_eq_neg_phi3 (f12 f13 f23 : R) :
    b3corpus f12 f13 f23 = -phi3 (mayer f12) (mayer f13) (mayer f23) := by
  unfold b3corpus W Z3 phi3 mayer; ring

/-- **Why it holds at `n = 3`.** The Boolean inversion of the bond-multiplicative `Z` itself,
`Z(123) − Z(12) − Z(13) − Z(23) + Z(1) + Z(2) + Z(3) − Z(∅)` with `Z = 1` on sets carrying no
bond, is the sum over spanning edge sets with no isolated vertex. On three vertices every such
edge set is connected, so it *is* `φᵀ₃`. -/
theorem boolean3_eq_phi3 (f12 f13 f23 : R) :
    Z3 f12 f13 f23 - f12 - f13 - f23 + 1 + 1 + 1 - 1
      = phi3 (mayer f12) (mayer f13) (mayer f23) := by
  unfold Z3 phi3 mayer; ring

/-- On uniform bonds `b₃ = 3f − 2 − f³ = −(1 − f)²(f + 2)`: the `2/3` threshold of
`MayerThreeBodySign` is never reached once `P₃` is the bond product. -/
theorem b3corpus_uniform_closed_form (f : R) :
    b3corpus f f f = -((1 - f) ^ 2 * (f + 2)) := by
  unfold b3corpus W Z3; ring

/-! ## `n = 4`: where the identity breaks, and by exactly what -/

/-- Canonical partition function of a four-cluster: the product of its six bond factors. -/
def Z4 (f12 f13 f14 f23 f24 f34 : R) : R := f12 * f13 * f14 * f23 * f24 * f34

/-- The fourth Ursell function **defined by the cluster property**
`Z_S = Σ_{π ∈ Π(S)} ∏_{B ∈ π} φᵀ_B` over the fifteen set partitions of a four-set: one of type
`4`, four of type `3+1`, three of type `2+2`, six of type `2+1+1`, one of type `1+1+1+1`. -/
def phi4 (g12 g13 g14 g23 g24 g34 : R) : R :=
  Z4 (g12 + 1) (g13 + 1) (g14 + 1) (g23 + 1) (g24 + 1) (g34 + 1)
    - (phi3 g12 g13 g23 + phi3 g12 g14 g24 + phi3 g13 g14 g34 + phi3 g23 g24 g34)
    - (g12 * g34 + g13 * g24 + g14 * g23)
    - (g12 + g13 + g14 + g23 + g24 + g34)
    - 1

/-- The cluster-property definition agrees with the connected-graph sum: the thirty-eight
connected spanning subgraphs of `K₄` (sixteen trees, fifteen with four edges, six with five,
and `K₄` itself). -/
theorem phi4_eq_connected_sum (g12 g13 g14 g23 g24 g34 : R) :
    phi4 g12 g13 g14 g23 g24 g34
      = g12*g13*g14 + g12*g14*g23 + g13*g14*g23 + g12*g13*g14*g23 + g12*g13*g24
        + g13*g14*g24 + g12*g13*g14*g24 + g12*g23*g24 + g13*g23*g24 + g12*g13*g23*g24
        + g14*g23*g24 + g12*g14*g23*g24 + g13*g14*g23*g24 + g12*g13*g14*g23*g24
        + g12*g13*g34 + g12*g14*g34 + g12*g13*g14*g34 + g12*g23*g34 + g13*g23*g34
        + g12*g13*g23*g34 + g14*g23*g34 + g12*g14*g23*g34 + g13*g14*g23*g34
        + g12*g13*g14*g23*g34 + g12*g24*g34 + g13*g24*g34 + g12*g13*g24*g34
        + g14*g24*g34 + g12*g14*g24*g34 + g13*g14*g24*g34 + g12*g13*g14*g24*g34
        + g12*g23*g24*g34 + g13*g23*g24*g34 + g12*g13*g23*g24*g34 + g14*g23*g24*g34
        + g12*g14*g23*g24*g34 + g13*g14*g23*g24*g34 + g12*g13*g14*g23*g24*g34 := by
  unfold phi4 Z4 phi3; ring

/-- The corpus's four-body cumulant, in the form `QOU.Mass.PairwiseCumulantVanishing.b4` uses:
`W(1234) − Σ_{pairs} W − Σ_{triples} b₃(T)`, on the multiplicative binding. -/
def b4corpus (f12 f13 f14 f23 f24 f34 : R) : R :=
  W (Z4 f12 f13 f14 f23 f24 f34)
    - (W f12 + W f13 + W f14 + W f23 + W f24 + W f34)
    - (b3corpus f12 f13 f23 + b3corpus f12 f14 f24 + b3corpus f13 f14 f34
        + b3corpus f23 f24 f34)

/-- **Where the identity breaks.** The corpus's `b₄` is minus the fourth Ursell function **minus
the three perfect matchings** — the isolated-vertex-free spanning graphs on four vertices that
are not connected. This is the closed form of the 2026-08-30 probe's "matches neither `+φᵀ₄` nor
`−φᵀ₄`, 200/200". -/
theorem b4corpus_eq (f12 f13 f14 f23 f24 f34 : R) :
    b4corpus f12 f13 f14 f23 f24 f34
      = -phi4 (mayer f12) (mayer f13) (mayer f14) (mayer f23) (mayer f24) (mayer f34)
        - (mayer f12 * mayer f34 + mayer f13 * mayer f24 + mayer f14 * mayer f23) := by
  unfold b4corpus b3corpus W phi4 Z4 Z3 phi3 mayer; ring

/-- The matching defect is not zero: at uniform `f = 1/2` it is `3/4`. -/
theorem matching_defect :
    mayer (1 / 2 : ℚ) * mayer (1 / 2) + mayer (1 / 2) * mayer (1 / 2)
        + mayer (1 / 2) * mayer (1 / 2) = 3 / 4 := by
  unfold mayer; norm_num

/-! ## The Mayer coefficients of the binding, and the negative-activity reading -/

/-- The multilinear log of `Ξ_S(z) = Σ_{T ⊆ S} z^T Z_T` on a three-cluster:
`U = Σ_T z^T φᵀ_T` (the exponential formula; verified symbolically in the probe). -/
def U (z1 z2 z3 g12 g13 g23 : R) : R :=
  z1 + z2 + z3 + z1 * z2 * g12 + z1 * z3 * g13 + z2 * z3 * g23
    + z1 * z2 * z3 * phi3 g12 g13 g23

/-- The Mayer expansion of the log-derived binding `B = −α ln(Ξ/Ξ_free)` (in units of `α`):
`−(U − Σ_i z_i)`, the free reference `Ξ_free = ∏(1 + z_i)` removed. -/
def mayerBinding (z1 z2 z3 g12 g13 g23 : R) : R :=
  -(U z1 z2 z3 g12 g13 g23 - (z1 + z2 + z3))

/-- **Uniform minus.** The Mayer coefficients of the binding are `−φᵀ_T` at every order: the
pair coefficient `−g = 1 − f` (positive on `(0,1)`) and the triple coefficient `−φᵀ₃`. The corpus's
`b₂ = −φᵀ₂`, `b₃ = −φᵀ₃` is this expansion, not a sign error in it. -/
theorem mayerBinding_eq (z1 z2 z3 g12 g13 g23 : R) :
    mayerBinding z1 z2 z3 g12 g13 g23
      = z1 * z2 * (-g12) + z1 * z3 * (-g13) + z2 * z3 * (-g23)
        + z1 * z2 * z3 * (-phi3 g12 g13 g23) := by
  unfold mayerBinding U; ring

/-- The 2026-08-30 "restored alternation" `b_T = (−1)^{|T|−1} φᵀ_T`: pair coefficients `−g`,
triple coefficient `+φᵀ₃`. -/
def restored (z1 z2 z3 g12 g13 g23 : R) : R :=
  z1 * z2 * (-g12) + z1 * z3 * (-g13) + z2 * z3 * (-g23) + z1 * z2 * z3 * phi3 g12 g13 g23

/-- **The restored alternation is the Mayer binding at negative activity.** Flipping the sign of
the third coefficient alone is exactly `z ↦ −z` in `−ln(Ξ/Ξ_free)`; no ensemble at positive
activity produces it. -/
theorem restored_eq_neg_activity (z1 z2 z3 g12 g13 g23 : R) :
    restored z1 z2 z3 g12 g13 g23 = mayerBinding (-z1) (-z2) (-z3) g12 g13 g23 := by
  unfold restored mayerBinding U; ring

end Generic

section Ordered

variable {K : Type*} [Field K] [LinearOrder K] [IsStrictOrderedRing K]

/-- **The Ursell alternation at `n = 3`, strict.** For bond factors in `(0,1)` the third Ursell
function is strictly positive: `φᵀ₃ = (1−f₁₂)(1−f₁₃) f₂₃ + (1−f₂₃)((1−f₁₂) + (1−f₁₃))`, a sum of a
strictly positive and a non-negative term. -/
theorem phi3_pos {f12 f13 f23 : K} (h12 : 0 < f12 ∧ f12 < 1) (h13 : 0 < f13 ∧ f13 < 1)
    (h23 : 0 < f23 ∧ f23 < 1) :
    0 < phi3 (mayer f12) (mayer f13) (mayer f23) := by
  have e : phi3 (mayer f12) (mayer f13) (mayer f23)
      = (1 - f12) * (1 - f13) * f23 + (1 - f23) * ((1 - f12) + (1 - f13)) := by
    unfold phi3 mayer; ring
  rw [e]
  have h1 : 0 < (1 - f12) * (1 - f13) * f23 :=
    mul_pos (mul_pos (by linarith) (by linarith)) h23.1
  have h2 : 0 ≤ (1 - f23) * ((1 - f12) + (1 - f13)) :=
    mul_nonneg (by linarith) (by linarith)
  linarith

/-- **No threshold.** The corpus's three-body cumulant is strictly negative for every bond triple
in `(0,1)`, uniform or not, whatever the like-pair typing. -/
theorem b3corpus_neg {f12 f13 f23 : K} (h12 : 0 < f12 ∧ f12 < 1) (h13 : 0 < f13 ∧ f13 < 1)
    (h23 : 0 < f23 ∧ f23 < 1) :
    b3corpus f12 f13 f23 < 0 := by
  rw [b3corpus_eq_neg_phi3]
  have := phi3_pos h12 h13 h23
  linarith

omit [LinearOrder K] [IsStrictOrderedRing K] in
/-- On uniform bonds this file's `b₃` is `MayerThreeBodySign.b3` with `P₃ = f³` — the same object,
so `lt_of_b3_pos` and `b3corpus_neg` are about one quantity. -/
theorem b3corpus_uniform_eq_mayerSign (f : K) :
    b3corpus f f f = MayerThreeBodySign.b3 f (f ^ 3) := by
  unfold b3corpus W Z3 MayerThreeBodySign.b3 MayerThreeBodySign.b2; ring

/-- The pair coefficient of the Mayer binding is positive on `(0,1)`: `−φᵀ₂ = 1 − f > 0`. With
`phi3_pos` this is the alternation `(−1)^{n−1} φᵀ_n > 0` at `n = 2, 3`, and it is the sign
pattern the corpus already carries — `b₂ > 0`, `b₃ < 0`. -/
theorem neg_phi2_pos {f : K} (h : 0 < f ∧ f < 1) : 0 < -phi2 (mayer f) := by
  unfold phi2 mayer; linarith

end Ordered

end QOU.MassTheory.UrsellPartitionFunctionB3
