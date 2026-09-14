import QOU.MathlibExt.MarkovTraceInterleavedCrossTerm
import Mathlib.Tactic

/-!
# Which non-monotone words carry a cross term — the revisit-class prune

`MonotoneWordTraceFactorizes` proves that an ascending word factorizes. This file asks the
converse question the formalize-first discipline requires before any probe is run: **which
departures from monotonicity produce a cross term, and which are cross-term-free?** A word is
non-monotone when some generator `g m` *recurs* after a higher generator has appeared. The
class is stratified by what lies between the two occurrences, and the answer is sharp:

| revisit pattern (`x ∈ H m`) | cross term | declaration |
|---|---|---|
| `x · gₘ · gₘ₊₁ · gₘ` — one step up and back | **none** (cyclicity alone) | `oneStepRevisit_eq_monotone` |
| `x · gₘ · gₘ₊₂ · gₘ` — skip the neighbour | **none** (far commutation) | `skipRevisit_eq_monotone` |
| `x · gₘ · gₘ₊₁ · gₘ₊₂ · gₘ` — climb two, come back | **none** | `twoStepClimbRevisit_eq_monotone` |
| `x · gₘ · gₘ₊₁ · gₘ · gₘ₊₁` — the **cyclic square** `(gₘ gₘ₊₁)²` | **`z² − h z − 1`** | `cyclicSquare_cross_term` |

So a cross term is **not** produced by a bond re-crossing after its neighbour, nor by any
single revisit that climbs and returns. It is produced exactly when two adjacent generators
*alternate* — `gₘ gₘ₊₁ gₘ gₘ₊₁` — which is the braid `(σₘ σₘ₊₁)²` whose closure on three
strands is the torus knot `T(3,2)` (one component, the three strands cyclically permuted),
against the monotone `gₘ² gₘ₊₁²` whose closure is the Hopf chain (three components). The
`n = 4` word of `MarkovTraceInterleavedCrossTerm` is this three-strand object stabilised once
(`interleaved_eq_stab_cyclicSquare`); the cross term there is `z · (z² − h z − 1)`.

**Correction of an earlier claim (2026-09-04).** `MarkovTraceInterleavedCrossTerm` and the
audit of 2026-09-03 describe `n = 4` as "the smallest instance where the product formula
fails". It is not: the smallest instance is `n = 3`, content `(2, 2)`, the cyclic square
against the Hopf chain, with cross term exactly the convention-D Markov defect `z² − h z − 1`
(no `z` prefactor). `qou-ls86`'s `n = 3` identity concerned content `(2, 1)` only, where the
single interleaved word is a rotation of the monotone one.

## Reading for the nucleus

Three adjacent strands cyclically braided is the algebraic signature of a closed **triple** —
`(σₘ σₘ₊₁)²`, closure `T(3,2)` — against the pairwise chain the production word writes. In the
production atom word the class has two realisations, and only the first is choice-free:

* **A cyclic-triple bond** (any `A ≥ 2`). The bond letter `B` at generator `3k+2` is doubled
  and its two crossings alternate with the last two intra crossings of nucleon `k` at `3k+1`
  (or, mirror-wise, the first two of nucleon `k+1` at `3k+3`): `… L₁L₂L₃ · B · L₄ · B …`. The
  three strands are adjacent, no conjugation is needed, and the cross term against the
  same-content monotone word (a two-crossing Hopf-clasp bond) is exactly
  `b(L₁L₂L₃) · (z² − hz − 1) · tr(prefix) · ∏ tr(suffix runs)` by `cyclicSquare_cross_term`
  plus multilinearity in the affine letters. This is what
  `computations/probes/cyclic_triple_bond_cross_term_probe.py` measures.
* **A cyclic coordination graph** (`A ≥ 3`): three nucleons each bonded to the other two. On
  the linear strand layout the closing bond joins non-adjacent strands and needs a band
  generator (a conjugated crossing passing over or under the middle nucleon), so this
  realisation carries a choice the algebra does not make for it. Not probed here.

What is excluded either way: a bond that merely re-crosses its neighbour, reaches over it and
returns, or is stacked as a clasp `B²` — none of these leaves the monotone trace.

## Base ring (§7c)

Generic `CommRing R`, `Ring A`, through `MarkovTrace` (T1–T3). The Hecke quadratic, the braid
relation and far commutation are hypotheses on the generators where used; each theorem names
exactly the ones it needs.

-- Ref: [leitner2026] folio/quantum-observable-universe/lean/QOU/MathlibExt/MarkovTraceInterleavedCrossTerm.lean
-- Ref: [jones1987] https://doi.org/10.2307/1971403 — the Markov trace on the Hecke tower.
-/

namespace QOU.MathlibExt.RevisitClass

open QOU.MathlibExt.OcneanuTrace

variable {R : Type*} [CommRing R] {A : Type*} [Ring A] [Algebra R A]
variable (T : MarkovTrace R A)

/-! ## Cross-term-free revisits -/

/-- **One-step revisit carries no cross term.** For any prefix `x ∈ H m`,
`tr(x gₘ gₘ₊₁ gₘ) = tr(x gₘ gₘ gₘ₊₁)`: rotate the trailing `gₘ` to the front, peel `gₘ₊₁`,
rotate back. Cyclicity and one Markov move only — no braid relation, no quadratic. This is
`qou-ls86`'s `n = 3` identity with an arbitrary prefix. -/
theorem oneStepRevisit_eq_monotone (m : ℕ) (x : A) (hx : x ∈ T.H m) :
    T.tr (x * T.g m * T.g (m + 1) * T.g m) = T.tr (x * T.g m * T.g m * T.g (m + 1)) := by
  have hmem : T.g m * x * T.g m ∈ T.H (m + 1) :=
    (T.H (m + 1)).mul_mem ((T.H (m + 1)).mul_mem (T.g_mem m)
      (T.H_mono (Nat.le_succ m) hx)) (T.g_mem m)
  have hmem' : x * T.g m * T.g m ∈ T.H (m + 1) :=
    (T.H (m + 1)).mul_mem ((T.H (m + 1)).mul_mem (T.H_mono (Nat.le_succ m) hx)
      (T.g_mem m)) (T.g_mem m)
  rw [T.tr_mul_comm (x * T.g m * T.g (m + 1)) (T.g m), ← mul_assoc, ← mul_assoc,
    T.markov (m + 1) _ hmem, T.markov (m + 1) _ hmem',
    T.tr_mul_comm (T.g m * x) (T.g m), ← mul_assoc, T.tr_mul_comm (T.g m * T.g m) x, mul_assoc]

/-- **Skipping the neighbour carries no cross term.** If `gₘ₊₂` commutes with `gₘ`,
`x gₘ gₘ₊₂ gₘ = x gₘ gₘ gₘ₊₂` outright. -/
theorem skipRevisit_eq_monotone (m : ℕ) (x : A)
    (hcomm : T.g (m + 2) * T.g m = T.g m * T.g (m + 2)) :
    T.tr (x * T.g m * T.g (m + 2) * T.g m) = T.tr (x * T.g m * T.g m * T.g (m + 2)) := by
  rw [mul_assoc (x * T.g m), hcomm, ← mul_assoc]

/-- **Climbing two steps and returning carries no cross term.** `x gₘ gₘ₊₁ gₘ₊₂ gₘ`: move
`gₘ` past `gₘ₊₂` (far commutation), peel `gₘ₊₂` (Markov), then the one-step identity. -/
theorem twoStepClimbRevisit_eq_monotone (m : ℕ) (x : A) (hx : x ∈ T.H m)
    (hcomm : T.g (m + 2) * T.g m = T.g m * T.g (m + 2)) :
    T.tr (x * T.g m * T.g (m + 1) * T.g (m + 2) * T.g m)
      = T.tr (x * T.g m * T.g m * T.g (m + 1) * T.g (m + 2)) := by
  have hx2 : x ∈ T.H (m + 2) := T.H_mono (by omega) hx
  have hg0 : T.g m ∈ T.H (m + 2) := T.H_mono (by omega) (T.g_mem m)
  have hg1 : T.g (m + 1) ∈ T.H (m + 2) := T.g_mem (m + 1)
  have hmem : x * T.g m * T.g (m + 1) * T.g m ∈ T.H (m + 2) :=
    (T.H (m + 2)).mul_mem ((T.H (m + 2)).mul_mem ((T.H (m + 2)).mul_mem hx2 hg0) hg1) hg0
  have hmem' : x * T.g m * T.g m * T.g (m + 1) ∈ T.H (m + 2) :=
    (T.H (m + 2)).mul_mem ((T.H (m + 2)).mul_mem ((T.H (m + 2)).mul_mem hx2 hg0) hg0) hg1
  rw [mul_assoc (x * T.g m * T.g (m + 1)), hcomm, ← mul_assoc, T.markov (m + 2) _ hmem,
    T.markov (m + 2) _ hmem', oneStepRevisit_eq_monotone T m x hx]

/-! ## The cross-term-bearing revisit: the cyclic square -/

/-- The Hopf-chain trace with prefix: `tr(x gₘ² gₘ₊₁²) = (hz+1)² · tr x`. -/
theorem tr_hopfChain (m : ℕ) (h : R) (x : A) (hx : x ∈ T.H m)
    (hq0 : T.g m * T.g m = h • T.g m + 1) (hq1 : T.g (m + 1) * T.g (m + 1) = h • T.g (m + 1) + 1) :
    T.tr (x * T.g m * T.g m * (T.g (m + 1) * T.g (m + 1))) = (h * T.z + 1) ^ 2 * T.tr x := by
  have hxg : x * T.g m * T.g m ∈ T.H (m + 1) :=
    (T.H (m + 1)).mul_mem ((T.H (m + 1)).mul_mem (T.H_mono (Nat.le_succ m) hx)
      (T.g_mem m)) (T.g_mem m)
  have hsq : T.tr (x * T.g m * T.g m) = (h * T.z + 1) * T.tr x := by
    rw [mul_assoc, hq0, mul_add, mul_one, mul_smul_comm, map_add, map_smul, smul_eq_mul,
      T.markov m x hx]
    ring
  rw [hq1, mul_add, mul_one, mul_smul_comm, map_add, map_smul, smul_eq_mul,
    T.markov (m + 1) _ hxg, hsq]
  ring

/-- The cyclic-square trace with prefix: `tr(x gₘ gₘ₊₁ gₘ gₘ₊₁) = (h z (h z + 1) + z²) · tr x`,
via the braid relation and the quadratic. Requires `x` to commute with `gₘ₊₁` (far
commutation of the prefix with the new generator). -/
theorem tr_cyclicSquare (m : ℕ) (h : R) (x : A) (hx : x ∈ T.H m)
    (hq0 : T.g m * T.g m = h • T.g m + 1)
    (hbraid : T.g m * T.g (m + 1) * T.g m = T.g (m + 1) * T.g m * T.g (m + 1))
    (hxc : x * T.g (m + 1) = T.g (m + 1) * x) :
    T.tr (x * T.g m * T.g (m + 1) * T.g m * T.g (m + 1))
      = (h * (T.z * (h * T.z + 1)) + T.z ^ 2) * T.tr x := by
  -- rotate the trailing `gₘ₊₁` to the front and commute it past `x`
  have h1 : T.tr (x * T.g m * T.g (m + 1) * T.g m * T.g (m + 1))
      = T.tr (x * (T.g (m + 1) * T.g m * T.g (m + 1) * T.g m)) := by
    rw [T.tr_mul_comm (x * T.g m * T.g (m + 1) * T.g m) (T.g (m + 1))]
    congr 1
    calc T.g (m + 1) * (x * T.g m * T.g (m + 1) * T.g m)
        = (T.g (m + 1) * x) * (T.g m * T.g (m + 1) * T.g m) := by simp only [mul_assoc]
      _ = (x * T.g (m + 1)) * (T.g m * T.g (m + 1) * T.g m) := by rw [hxc]
      _ = x * (T.g (m + 1) * T.g m * T.g (m + 1) * T.g m) := by simp only [mul_assoc]
  -- braid: `gₘ₊₁ gₘ gₘ₊₁ gₘ = gₘ gₘ₊₁ gₘ gₘ`, then the quadratic on the last `gₘ²`
  have h2 : T.g (m + 1) * T.g m * T.g (m + 1) * T.g m
      = T.g m * T.g (m + 1) * (h • T.g m + 1) := by
    rw [← hbraid, mul_assoc (T.g m * T.g (m + 1)), hq0]
  rw [h1, h2, mul_add, mul_one, mul_smul_comm, mul_add, mul_smul_comm, map_add, map_smul,
    smul_eq_mul]
  -- `tr(x gₘ gₘ₊₁ gₘ) = tr(x gₘ² gₘ₊₁) = z (hz+1) tr x` and `tr(x gₘ gₘ₊₁) = z² tr x`
  have hxg : x * T.g m * T.g m ∈ T.H (m + 1) :=
    (T.H (m + 1)).mul_mem ((T.H (m + 1)).mul_mem (T.H_mono (Nat.le_succ m) hx)
      (T.g_mem m)) (T.g_mem m)
  have hxg1 : x * T.g m ∈ T.H (m + 1) :=
    (T.H (m + 1)).mul_mem (T.H_mono (Nat.le_succ m) hx) (T.g_mem m)
  have hsq : T.tr (x * T.g m * T.g m) = (h * T.z + 1) * T.tr x := by
    rw [mul_assoc, hq0, mul_add, mul_one, mul_smul_comm, map_add, map_smul, smul_eq_mul,
      T.markov m x hx]
    ring
  have hA : T.tr (x * (T.g m * T.g (m + 1) * T.g m)) = T.z * ((h * T.z + 1) * T.tr x) := by
    rw [← mul_assoc, ← mul_assoc, oneStepRevisit_eq_monotone T m x hx,
      T.markov (m + 1) _ hxg, hsq]
  have hB : T.tr (x * (T.g m * T.g (m + 1))) = T.z * (T.z * T.tr x) := by
    rw [← mul_assoc, T.markov (m + 1) _ hxg1, T.markov m x hx]
  rw [hA, hB]
  ring

/-- **THE MINIMAL CROSS TERM — three strands.** With the same content `(2, 2)`, the cyclic
square `(gₘ gₘ₊₁)²` and the Hopf chain `gₘ² gₘ₊₁²` differ by exactly the convention-D Markov
defect: `tr(x (gₘ gₘ₊₁)²) − tr(x gₘ² gₘ₊₁²) = (z² − h z − 1) · tr x`. This is the smallest
instance where the product formula fails — `n = 3`, not `n = 4`. -/
theorem cyclicSquare_cross_term (m : ℕ) (h : R) (x : A) (hx : x ∈ T.H m)
    (hq0 : T.g m * T.g m = h • T.g m + 1) (hq1 : T.g (m + 1) * T.g (m + 1) = h • T.g (m + 1) + 1)
    (hbraid : T.g m * T.g (m + 1) * T.g m = T.g (m + 1) * T.g m * T.g (m + 1))
    (hxc : x * T.g (m + 1) = T.g (m + 1) * x) :
    T.tr (x * T.g m * T.g (m + 1) * T.g m * T.g (m + 1))
        - T.tr (x * T.g m * T.g m * (T.g (m + 1) * T.g (m + 1)))
      = (T.z ^ 2 - h * T.z - 1) * T.tr x := by
  rw [tr_cyclicSquare T m h x hx hq0 hbraid hxc, tr_hopfChain T m h x hx hq0 hq1]
  ring

/-- **The `n = 4` interleaved word is the stabilised cyclic square.** `tr(g₀ g₁ g₀ g₂ g₁) =
z · tr((g₁ g₀)²)`: rotate `g₁` to the front, peel `g₂`. So the `n = 4` cross term
`z (z² − h z − 1)` is the three-strand one times a Markov stabilisation — the object behind
the cross term is the torus knot `T(3,2)` of the cyclically braided triple, not anything
four-strand. -/
theorem interleaved_eq_stab_cyclicSquare :
    T.tr (T.g 0 * T.g 1 * T.g 0 * T.g 2 * T.g 1) = T.z * T.tr (T.g 1 * T.g 0 * T.g 1 * T.g 0) := by
  have h0 : T.g 0 ∈ T.H 2 := T.H_mono (by norm_num) (T.g_mem 0)
  have h1 : T.g 1 ∈ T.H 2 := T.g_mem 1
  have hmem : T.g 1 * T.g 0 * T.g 1 * T.g 0 ∈ T.H 2 :=
    (T.H 2).mul_mem ((T.H 2).mul_mem ((T.H 2).mul_mem h1 h0) h1) h0
  rw [T.tr_mul_comm (T.g 0 * T.g 1 * T.g 0 * T.g 2) (T.g 1)]
  have hassoc : T.g 1 * (T.g 0 * T.g 1 * T.g 0 * T.g 2)
      = T.g 1 * T.g 0 * T.g 1 * T.g 0 * T.g 2 := by
    simp only [mul_assoc]
  rw [hassoc, T.markov 2 _ hmem]

/-! ## Convention D: the three-strand cross term in closed form -/

/-- At convention D the three-strand cross term is `−(q⁴ + q² + 1)/(q² + 1)²` — the Markov
defect itself (`markovDefect_convD`) — and it is **negative** for every real `q > 0`: the
cyclic square's trace is smaller than the Hopf chain's, so a cyclically braided triple carries
extra log-suppression, i.e. extra binding. -/
theorem cyclicSquare_cross_term_neg_convD (q : ℝ) (hq : 0 < q) :
    (q ^ 3 / (q ^ 2 + 1)) ^ 2 - (q - q⁻¹) * (q ^ 3 / (q ^ 2 + 1)) - 1 < 0 := by
  have h2 : q ^ 2 + 1 ≠ 0 := by positivity
  rw [QOU.MathlibExt.InterleavedCrossTerm.markovDefect_convD q h2]
  apply div_neg_of_neg_of_pos
  · have : 0 < q ^ 4 + q ^ 2 + 1 := by positivity
    linarith
  · positivity

/-! ## Dressed letters: the cross term is BLIND to the square's own dressings

Every statement above is about bare generators `gᵢ`.  The production bonds are
**charge-dressed** letters `bᵢ = gᵢ + dᵢ·1` (`QOU.MathlibExt.MarkovBondRule.sigmaPlus`),
so the question a downstream reader actually has is whether the cross term sees the
dressing.  `cyclicSquare_cross_term_dressed` answers it: **it does not** — the dressed
difference is the same `z² − h z − 1`, with `s` and `t` absent from the result.

The mechanism is `dressed_difference_expand`, and each of its four brackets is settled
here:

| bracket | coefficient | value | by |
|---|---|---|---|
| `acac − a²c²` | `1` | `(z² − hz − 1)·tr x` | `cyclicSquare_cross_term` |
| `aca − a²c` | `t` | `0` | `oneStepRevisit_eq_monotone` |
| `cac − ac²` | `s` | `0` | `mirrorRevisit_eq_monotone` |
| `ca − ac` | `s·t` | `0` | `tr_bondCommutator` |

So the three brackets that *could* have carried the dressing are exactly the three the
revisit-class table above already lists as cross-term-free.  The blindness is not a
coincidence of one computation; it is that table, read one degree down.

**Downstream.**  The `n = 4` interleaved word is this square stabilised once
(`interleaved_eq_stab_cyclicSquare`), so its dressed cross term is `(z + d)·(z² − hz − 1)`
with `d` the *stabilising* letter's dressing only: the square's own two dressings drop out,
the stabiliser's survives.  That is the structural reason the interleaved pair is
charge-blind.  Added 2026-09-14, bean `qou-vwu3`. -/

/-- The charge-dressed letter `bᵢ = gᵢ + dᵢ·1`. -/
noncomputable def dressed (m : ℕ) (d : R) : A := T.g m + d • (1 : A)

/-- **The dressed difference decomposes into four brackets.**  A pure ring identity —
scalars are central, so expanding `(a+s)(c+t)(a+s)(c+t) − (a+s)²(c+t)²` leaves the degree-4
bracket plus one bracket per lower degree, with no `s²`, `t²`, `s²t` or `st²` term surviving:
those cancel between the two words because they multiply the *same* monomial in `a, c`. -/
theorem dressed_difference_expand (m : ℕ) (s t : R) :
    dressed T m s * dressed T (m + 1) t * dressed T m s * dressed T (m + 1) t
      - dressed T m s * dressed T m s * (dressed T (m + 1) t * dressed T (m + 1) t)
    = (T.g m * T.g (m + 1) * T.g m * T.g (m + 1)
        - T.g m * T.g m * (T.g (m + 1) * T.g (m + 1)))
      + t • (T.g m * T.g (m + 1) * T.g m - T.g m * T.g m * T.g (m + 1))
      + s • (T.g (m + 1) * T.g m * T.g (m + 1) - T.g m * T.g (m + 1) * T.g (m + 1))
      + (s * t) • (T.g (m + 1) * T.g m - T.g m * T.g (m + 1)) := by
  simp only [dressed, add_mul, mul_add, mul_assoc, smul_mul_assoc, mul_smul_comm,
    one_mul, mul_one]
  module

/-- **The bond commutator is trace-invisible.**  `tr(x gₘ₊₁ gₘ) = tr(x gₘ gₘ₊₁)` whenever the
prefix commutes with `gₘ₊₁`: rotate `gₘ₊₁` to the front, commute it past `x`, rotate back.
Cyclicity only — no Markov move, no braid relation, no quadratic. -/
theorem tr_bondCommutator (m : ℕ) (x : A) (hxc : x * T.g (m + 1) = T.g (m + 1) * x) :
    T.tr (x * (T.g (m + 1) * T.g m)) = T.tr (x * (T.g m * T.g (m + 1))) := by
  have e : x * (T.g (m + 1) * T.g m) = T.g (m + 1) * (x * T.g m) := by
    rw [← mul_assoc, hxc, mul_assoc]
  rw [e, T.tr_mul_comm (T.g (m + 1)) (x * T.g m), mul_assoc]

/-- **The mirror revisit is trace-monotone too.**  `tr(x gₘ₊₁ gₘ gₘ₊₁) = tr(x gₘ gₘ₊₁²)`.
This is `oneStepRevisit_eq_monotone` read through the braid relation: braid the left word
back to `x gₘ gₘ₊₁ gₘ`, apply the one-step identity, then collapse the doubled letter on each
side with its Hecke quadratic.  Both sides equal `h z² · tr x + z · tr x`. -/
theorem mirrorRevisit_eq_monotone (m : ℕ) (h : R) (x : A) (hx : x ∈ T.H m)
    (hq0 : T.g m * T.g m = h • T.g m + 1)
    (hq1 : T.g (m + 1) * T.g (m + 1) = h • T.g (m + 1) + 1)
    (hbraid : T.g m * T.g (m + 1) * T.g m = T.g (m + 1) * T.g m * T.g (m + 1)) :
    T.tr (x * (T.g (m + 1) * T.g m * T.g (m + 1)))
      = T.tr (x * (T.g m * T.g (m + 1) * T.g (m + 1))) := by
  have hx1 : x ∈ T.H (m + 1) := T.H_mono (Nat.le_succ m) hx
  have hxa : x * T.g m ∈ T.H (m + 1) := (T.H (m + 1)).mul_mem hx1 (T.g_mem m)
  have hL1 : T.tr (x * (T.g (m + 1) * T.g m * T.g (m + 1)))
      = T.tr (x * T.g m * T.g m * T.g (m + 1)) := by
    rw [← hbraid]
    have e : x * (T.g m * T.g (m + 1) * T.g m) = x * T.g m * T.g (m + 1) * T.g m := by
      simp only [mul_assoc]
    rw [e, oneStepRevisit_eq_monotone T m x hx]
  have hA : T.tr (x * T.g m * T.g m * T.g (m + 1))
      = h * (T.z * (T.z * T.tr x)) + T.z * T.tr x := by
    have e : x * T.g m * T.g m * T.g (m + 1)
        = h • (x * T.g m * T.g (m + 1)) + x * T.g (m + 1) := by
      rw [mul_assoc x, hq0, mul_add, mul_one, mul_smul_comm, add_mul, smul_mul_assoc]
    rw [e, map_add, map_smul, smul_eq_mul, T.markov (m + 1) _ hxa, T.markov m x hx,
      T.markov (m + 1) x hx1]
  have hB : T.tr (x * (T.g m * T.g (m + 1) * T.g (m + 1)))
      = h * (T.z * (T.z * T.tr x)) + T.z * T.tr x := by
    have e : x * (T.g m * T.g (m + 1) * T.g (m + 1))
        = h • (x * T.g m * T.g (m + 1)) + x * T.g m := by
      rw [mul_assoc (T.g m), hq1, mul_add, mul_one, mul_smul_comm, mul_add, mul_smul_comm,
        ← mul_assoc]
    rw [e, map_add, map_smul, smul_eq_mul, T.markov (m + 1) _ hxa, T.markov m x hx]
  rw [hL1, hA, hB]

/-- **THE CROSS TERM IS BLIND TO THE SQUARE'S OWN DRESSINGS.**  For dressed letters
`b₀ = gₘ + s·1` and `b₁ = gₘ₊₁ + t·1`,

`tr(x b₀b₁b₀b₁) − tr(x b₀² b₁²) = (z² − h z − 1) · tr x`,

*the same value as for bare generators* — `s` and `t` do not appear.  Under the same
hypotheses as `cyclicSquare_cross_term`, which is the `s = t = 0` case.

Consequence for the production word: a cyclically braided triple contributes the identical
cross term whatever charges sit on its two alternating letters, so this class of word cannot
distinguish `pp` from `nn` and cannot be the carrier of a charge-antisymmetric term. -/
theorem cyclicSquare_cross_term_dressed (m : ℕ) (h s t : R) (x : A) (hx : x ∈ T.H m)
    (hq0 : T.g m * T.g m = h • T.g m + 1) (hq1 : T.g (m + 1) * T.g (m + 1) = h • T.g (m + 1) + 1)
    (hbraid : T.g m * T.g (m + 1) * T.g m = T.g (m + 1) * T.g m * T.g (m + 1))
    (hxc : x * T.g (m + 1) = T.g (m + 1) * x) :
    T.tr (x * (dressed T m s * dressed T (m + 1) t * dressed T m s * dressed T (m + 1) t))
        - T.tr (x * (dressed T m s * dressed T m s
            * (dressed T (m + 1) t * dressed T (m + 1) t)))
      = (T.z ^ 2 - h * T.z - 1) * T.tr x := by
  have hD4 : T.tr (x * (T.g m * T.g (m + 1) * T.g m * T.g (m + 1)
      - T.g m * T.g m * (T.g (m + 1) * T.g (m + 1)))) = (T.z ^ 2 - h * T.z - 1) * T.tr x := by
    rw [mul_sub, map_sub]
    have e1 : x * (T.g m * T.g (m + 1) * T.g m * T.g (m + 1))
        = x * T.g m * T.g (m + 1) * T.g m * T.g (m + 1) := by simp only [mul_assoc]
    have e2 : x * (T.g m * T.g m * (T.g (m + 1) * T.g (m + 1)))
        = x * T.g m * T.g m * (T.g (m + 1) * T.g (m + 1)) := by simp only [mul_assoc]
    rw [e1, e2, cyclicSquare_cross_term T m h x hx hq0 hq1 hbraid hxc]
  have hB2 : T.tr (x * (T.g m * T.g (m + 1) * T.g m - T.g m * T.g m * T.g (m + 1))) = 0 := by
    rw [mul_sub, map_sub]
    have e1 : x * (T.g m * T.g (m + 1) * T.g m) = x * T.g m * T.g (m + 1) * T.g m := by
      simp only [mul_assoc]
    have e2 : x * (T.g m * T.g m * T.g (m + 1)) = x * T.g m * T.g m * T.g (m + 1) := by
      simp only [mul_assoc]
    rw [e1, e2, oneStepRevisit_eq_monotone T m x hx, sub_self]
  have hB3 : T.tr (x * (T.g (m + 1) * T.g m * T.g (m + 1)
      - T.g m * T.g (m + 1) * T.g (m + 1))) = 0 := by
    rw [mul_sub, map_sub, mirrorRevisit_eq_monotone T m h x hx hq0 hq1 hbraid, sub_self]
  have hB4 : T.tr (x * (T.g (m + 1) * T.g m - T.g m * T.g (m + 1))) = 0 := by
    rw [mul_sub, map_sub, tr_bondCommutator T m x hxc, sub_self]
  have hsub : T.tr (x * (dressed T m s * dressed T (m + 1) t * dressed T m s
        * dressed T (m + 1) t))
        - T.tr (x * (dressed T m s * dressed T m s
            * (dressed T (m + 1) t * dressed T (m + 1) t)))
      = T.tr (x * (dressed T m s * dressed T (m + 1) t * dressed T m s * dressed T (m + 1) t
          - dressed T m s * dressed T m s
            * (dressed T (m + 1) t * dressed T (m + 1) t))) := by
    rw [mul_sub, map_sub]
  rw [hsub, dressed_difference_expand T m s t]
  simp only [mul_add, mul_smul_comm, map_add, map_smul, smul_eq_mul]
  rw [hD4, hB2, hB3, hB4]
  ring

end QOU.MathlibExt.RevisitClass

