/-
# The bond/charge arc's assertions, proved

Owner, 2026-08-30: *"lean prove all your assertions"*.

Across this arc a number of claims were established by **measurement** — random
sampling, or evaluation on a finite list of nuclei. Those that are algebraic
identities are proved here, so that they hold for every input rather than for
the ones that were tried. Section 6 lists what is left, and why each is a
measurement rather than a theorem.

Every statement is over a generic `CommRing` (AGENTS.md §7c) except the two
positivity results in §2, which need an ordered field and say so.

Companion probes:
`ursell_alternation_sign_identity`, `pair_layer_isospin_parity`,
`mirror_charge_asymmetry_scaling`, `level3_em_channel_parity`,
`level3_bond_charge_rule`.

Beans `qou-rwhv`, `qou-1pig`, `qou-vudb`, `qou-dhsn`, `qou-nial`.
-/
import Mathlib.Algebra.Ring.Defs
import Mathlib.Algebra.Order.Field.Defs
import Mathlib.Tactic.Ring
import Mathlib.Tactic.LinearCombination
import Mathlib.Tactic.Linarith

namespace QOU.MassTheory.BondArcTheorems

variable {R : Type*} [CommRing R]

/-! ## 1. The Ursell identity at `n = 3`

`ursell_alternation_sign_identity` checked `b₃ = -φᵀ₃` on 400 random non-uniform
triples in exact rational arithmetic. It is an identity, so it holds for all. -/

/-- The corpus's multiplicative assembly on a pair: `W = 1 - f`. -/
def W2 (f : R) : R := 1 - f

/-- The corpus's connected 3-body cumulant,
`b₃ = W(3) - [W(12) + W(13) + W(23)]` with `W(S) = 1 - ∏ f`. -/
def corpusB3 (f₁₂ f₁₃ f₂₃ : R) : R :=
  (1 - f₁₂ * f₁₃ * f₂₃) - (W2 f₁₂ + W2 f₁₃ + W2 f₂₃)

/-- The second Ursell function, `φᵀ₂ = g` — the single connected graph on two
vertices is the edge. -/
def ursell2 (g : R) : R := g

/-- The third Ursell function, `φᵀ₃ = Σ_{G connected on 3} ∏_{E(G)} g`: the three
two-edge paths and the triangle (Jansen–Kolesnikov p. 5). -/
def ursell3 (g₁₂ g₁₃ g₂₃ : R) : R :=
  g₁₂ * g₁₃ + g₁₂ * g₂₃ + g₁₃ * g₂₃ + g₁₂ * g₁₃ * g₂₃

/-- **`W(2) = -φᵀ₂`** under the Boltzmann identification `g = f - 1`. -/
theorem W2_eq_neg_ursell2 (f : R) : W2 f = -ursell2 (f - 1) := by
  unfold W2 ursell2; ring

/-- **`b₃ = -φᵀ₃`, exactly, for every triple.** This is the identity the probe
sampled; it is now proved rather than tested. -/
theorem corpusB3_eq_neg_ursell3 (f₁₂ f₁₃ f₂₃ : R) :
    corpusB3 f₁₂ f₁₃ f₂₃ = -ursell3 (f₁₂ - 1) (f₁₃ - 1) (f₂₃ - 1) := by
  unfold corpusB3 W2 ursell3; ring

/-- The closed form the identity reduces to: `b₃ = f₁₂ + f₁₃ + f₂₃ - 2 - f₁₂f₁₃f₂₃`. -/
theorem corpusB3_closed (f₁₂ f₁₃ f₂₃ : R) :
    corpusB3 f₁₂ f₁₃ f₂₃ = f₁₂ + f₁₃ + f₂₃ - 2 - f₁₂ * f₁₃ * f₂₃ := by
  unfold corpusB3 W2; ring

/-! ## 2. The alternation, at the two orders that matter

The classical statement is `(-1)^{n-1} φᵀ_n ≥ 0` for a non-negative pair
potential, i.e. Mayer variable `g ∈ (-1, 0)`. The probe verified it by sampling
at `n = 2, 3, 4, 5`; the two orders the arc actually uses are proved here.
These need an order, so they are stated over a `LinearOrderedField`. -/

variable {K : Type*} [Field K] [LinearOrder K] [IsStrictOrderedRing K]

omit [IsStrictOrderedRing K] in
/-- **`φᵀ₂ ≤ 0`.** This is what settles the OCR'd exponent: the reading
`(-1)^n φᵀ_n ≥ 0` would demand `φᵀ₂ ≥ 0` and fails immediately. -/
theorem ursell2_nonpos {g : K} (hg : g ≤ 0) : ursell2 g ≤ 0 := hg

/-- **`φᵀ₃ > 0`** for `g ∈ (-1, 0)` — the opposite sign, and the sign nature has.
The proof is the regrouping `g₁₂g₁₃ + g₁₂g₁₃g₂₃ = g₁₂g₁₃(1 + g₂₃)`, in which
every factor is positive: two negatives multiply to a positive, and `1 + g > 0`
is exactly `g > -1`.

Note the hypotheses: all three variables must be **negative**, but only **one**
of them needs `> -1`. The repulsive class gives `-1 < g < 0` on all three, so the
theorem applies; it is stated at the weaker hypothesis because that is what the
proof uses, and a Lean file should not carry hypotheses it does not need. -/
theorem ursell3_pos {a b c : K} (ha' : a < 0) (hb' : b < 0)
    (hc : -1 < c) (hc' : c < 0) : 0 < ursell3 a b c := by
  have hab : 0 < a * b := mul_pos_of_neg_of_neg ha' hb'
  have hac : 0 < a * c := mul_pos_of_neg_of_neg ha' hc'
  have hbc : 0 < b * c := mul_pos_of_neg_of_neg hb' hc'
  have h1c : 0 < 1 + c := by linarith
  have key : ursell3 a b c = a * b * (1 + c) + a * c + b * c := by
    unfold ursell3; ring
  rw [key]
  have : 0 < a * b * (1 + c) := mul_pos hab h1c
  linarith

/-- **The `(-1)^n` reading fails at `n = 2`** whenever `g < 0`, which is the
whole repulsive class. Stated as the negation, since that is the use. -/
theorem ocr_exponent_fails_at_two {g : K} (hg : g < 0) : ¬ (0 ≤ ursell2 g) := by
  unfold ursell2; linarith

/-! ## 3. The pair layer

`pair_layer_isospin_parity` evaluated these at the substrate `q₀`. They are
identities in `z` and `h`, so they hold at every `q`. -/

/-- `f_pp = z` — the positive crossing. -/
def fPP (z : R) : R := z
/-- `f_nn = z - h` — the negative crossing, under `σ⁻¹ = σ - h`. -/
def fNN (z h : R) : R := z - h
/-- `f_pn` under `strict_averaged` is `z - h/2`; stated **quadrupled** as
`4z - 2h` so that nothing below needs division and the base ring stays a bare
`CommRing`. -/
def fPNstrictQuad (z h : R) : R := 4 * z - 2 * h
/-- `f_pn` under `bring_color_weighted` is `z - h(1/2 - δ/4)`; quadrupled,
`4z - 2h + hδ`. -/
def fPNbringQuad (z h δ : R) : R := 4 * z - 2 * h + h * δ

/-- **`f_pp - f_nn = h`** — the isovector term IS the skein relation
`σ - σ⁻¹ = q - q⁻¹`. No free coefficient, and no `δ`: this is the same value
under every `pn_convention`, because neither `fPP` nor `fNN` mentions `δ`. -/
theorem fPP_sub_fNN (z h : R) : fPP z - fNN z h = h := by
  unfold fPP fNN; ring

/-- The charge-**even** part of the like-pair channel, doubled: `f_pp + f_nn =
2z - h`. Together with `fPP_sub_fNN` this is the full parity decomposition —
even `= z - h/2`, odd `= h/2`. -/
theorem like_pair_even_doubled (z h : R) : fPP z + fNN z h = 2 * z - h := by
  unfold fPP fNN; ring

/-- **`strict_averaged` puts `f_pn` exactly on the like-pair midpoint**, so its
`T = 0` / `T = 1` splitting is identically zero. -/
theorem strict_T01_zero (z h : R) :
    fPNstrictQuad z h - 2 * (fPP z + fNN z h) = 0 := by
  unfold fPNstrictQuad fPP fNN; ring

/-- **`bring_color_weighted`'s `T = 0` / `T = 1` splitting is exactly `hδ/4`**,
stated quadrupled as `hδ`. -/
theorem bring_T01_quad (z h δ : R) :
    fPNbringQuad z h δ - 2 * (fPP z + fNN z h) = h * δ := by
  unfold fPNbringQuad fPP fNN; ring

/-- **The isovector term is `2/δ` times the isoscalar one**, in the quadrupled
normalisation: `4·(f_pp - f_nn) = (4/δ)·(T01 splitting)`, i.e. the ratio is a
fact about `δ` alone and carries no other structure. Stated division-free as the
cross-multiplied identity. -/
theorem isovector_over_isoscalar (z h δ : R) :
    δ * (fPP z - fNN z h) = fPNbringQuad z h δ - 2 * (fPP z + fNN z h) := by
  unfold fPP fNN fPNbringQuad; ring

/- **`bring_color_weighted` does not touch the like pairs.** There is deliberately
no theorem here: `fPP` and `fNN` do not take `δ` as an argument at all, so the
claim is true by the *shape* of the definitions and any Lean statement of it
would be vacuous. `fPP_sub_fNN` is the substantive content — the like-pair
difference is `h`, with no `δ` anywhere in it, under every `pn_convention`. -/

/-! ## 4. The mirror difference for an additive assembly

`mirror_charge_asymmetry_scaling`'s load-bearing step: under the §10a log form
the binding is additive over bonds, so a mirror pair's difference collapses to
one constant times a bond-count difference. -/

/-- An additive binding: `n_pp` pp bonds, `n_nn` nn bonds, `n_pn` pn bonds, each
contributing its own energy. -/
def additiveBinding (nPP nNN nPN bPP bNN bPN : R) : R :=
  nPP * bPP + nNN * bNN + nPN * bPN

/-- **The mirror difference is `(n_pp - n_nn)(b_pp - b_nn)`.** Under `p ↔ n` the
pp and nn counts trade and the pn count is fixed, so everything else cancels —
including the pn term entirely. -/
theorem mirror_difference (nPP nNN nPN bPP bNN bPN : R) :
    additiveBinding nPP nNN nPN bPP bNN bPN
      - additiveBinding nNN nPP nPN bPP bNN bPN
      = (nPP - nNN) * (bPP - bNN) := by
  unfold additiveBinding; ring

/-- **The chain assembly's bond-count difference is `Z - N`** — no factor of `A`,
which is the `A⁰` scaling the probe measured. A chain on `p^Z n^N` has `Z-1` pp
bonds and `N-1` nn bonds. -/
theorem chain_count_difference (Z N : R) : (Z - 1) - (N - 1) = Z - N := by ring

/-- **The complete graph's bond-count difference is `(Z-N)(A-1)/2`**, stated
doubled: `Z(Z-1) - N(N-1) = (Z-N)(Z+N-1)`. Linear in `A`, which is the `A¹`
scaling the probe measured. -/
theorem complete_count_difference_doubled (Z N : R) :
    Z * (Z - 1) - N * (N - 1) = (Z - N) * (Z + N - 1) := by ring

/-! ## 5. The crossing counts

`level3_em_channel_parity` measured `n₊ + n₋ = 10A - 2` and `n₊ - n₋ = 4Z` on 12
nuclei and scoped the claim **(a)** for that reason. The word is built as a
**chain**: for each nucleon its intra-nucleon letters, then one inter-nucleon
letter per adjacent pair. Reading the per-nucleon and per-interface counts off
that construction gives closed forms, and the probe verifies they reproduce the
implementation exactly on 14 nuclei to `A = 100`. With the model fixed, the two
statistics are **theorems**. -/

/-- Positive crossings: `6` per proton, `5` per neutron, plus one per pp
interface, of which a chain on `p^Z n^N` has `Z - 1`. -/
def nPlus (Z N : R) : R := 6 * Z + 5 * N + (Z - 1)

/-- Negative crossings: `3` per proton, `4` per neutron, plus one per nn
interface, of which there are `N - 1`. -/
def nMinus (Z N : R) : R := 3 * Z + 4 * N + (N - 1)

/-- Averaged (non-braid) letters: `2` per nucleon, plus the single pn interface —
a chain on `p^Z n^N` has exactly one p→n transition. -/
def nAvg (Z N : R) : R := 2 * (Z + N) + 1

/-- `n₊ = 7Z + 5N - 1`. -/
theorem nPlus_closed (Z N : R) : nPlus Z N = 7 * Z + 5 * N - 1 := by
  unfold nPlus; ring

/-- `n₋ = 3Z + 5N - 1`. -/
theorem nMinus_closed (Z N : R) : nMinus Z N = 3 * Z + 5 * N - 1 := by
  unfold nMinus; ring

/-- **`n₊ + n₋ = 10A - 2`** — the Coulomb-channel multiplicity, depending on `A`
alone. Proved, not sampled. -/
theorem count_sum (Z N : R) : nPlus Z N + nMinus Z N = 10 * (Z + N) - 2 := by
  unfold nPlus nMinus; ring

/-- **`n₊ - n₋ = 4Z`** — the writhe, the strong-channel multiplicity, carrying
all of the charge dependence. -/
theorem count_writhe (Z N : R) : nPlus Z N - nMinus Z N = 4 * Z := by
  unfold nPlus nMinus; ring

/-- **`n_avg = 2A + 1`**, as `atom_braid_word_3A`'s own docstring states. -/
theorem count_avg (Z N : R) : nAvg Z N = 2 * (Z + N) + 1 := by
  unfold nAvg; ring

/-- **The Coulomb channel is mirror-invariant.** Its multiplicity `n₊ + n₋`
depends only on `A = Z + N`, so it takes the same value on `(Z, N)` and `(N, Z)`
— hence contributes exactly zero to every mirror splitting, for every nucleus
rather than for the five that were checked. -/
theorem coulomb_channel_mirror_invariant (Z N : R) :
    nPlus Z N + nMinus Z N = nPlus N Z + nMinus N Z := by
  unfold nPlus nMinus; ring

/-- **The strong channel is not**: it differs by `4(Z - N)`. The charge
dependence is present, in the wrong channel. -/
theorem strong_channel_mirror_difference (Z N : R) :
    (nPlus Z N - nMinus Z N) - (nPlus N Z - nMinus N Z) = 4 * (Z - N) := by
  unfold nPlus nMinus; ring

/-- Both counts are **affine** in `(Z, N)`: their second differences in `Z`
vanish. This is what `CrossingCountAffine` needs, now from the construction
rather than from a fitted formula. -/
theorem counts_affine (N : R) : ∀ Z : R,
    (nPlus (Z + 2) N - 2 * nPlus (Z + 1) N + nPlus Z N = 0)
      ∧ (nMinus (Z + 2) N - 2 * nMinus (Z + 1) N + nMinus Z N = 0) := by
  intro Z
  constructor <;> simp only [nPlus, nMinus] <;> ring

/-! ## 6. What is NOT proved here, and why

* **The observed exponents** (`0.874` for AME2020, `0.780` for the Coulomb
  reference) and the magic-shell comparison are measurements against data.
  They are not theorems and nothing here makes them so.
* **`b₃ = -φᵀ₃` does not extend to `n = 4`.** Establishing that needs `φᵀ₄`,
  a sum over the 38 connected graphs on four vertices; the probe settles it by
  exhibiting 200 counterexamples and it is left there.
* **`isovector / isoscalar > 1000`** depends on the numeric value of `δ` at the
  substrate `q₀`; §3 proves the two quantities are `h/2` and `hδ/4`, so the
  ratio is `2/δ`, but that it exceeds `1000` is a fact about `δ`.
* **The per-nucleon counts `(6,3,2)` and `(5,4,2)` in §5** are read off the
  implementation, not derived from the quark content. §5's theorems are exact
  **given** them, and the probe verifies the model reproduces
  `atom_braid_word_3A` on 14 nuclei to `A = 100`. That is what upgrades
  `qou-dhsn`'s statistics from sampled to proved *for this construction* — not
  a proof that the construction is the right one.
-/

end QOU.MassTheory.BondArcTheorems
