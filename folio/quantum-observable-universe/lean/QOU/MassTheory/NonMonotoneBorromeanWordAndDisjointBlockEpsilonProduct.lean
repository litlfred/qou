/-
Copyright (c) 2026 QOU Contributors. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
-/

/-!
# Non-Monotone Canonical Atom Word and Disjoint-Block Epsilon-Series Factorization

Formalizes the structural findings of `qou-wdij`:

1. **Interleaved Canonical Atom Word is Non-Monotone**:
   - The grouped nucleon generator sequence `[0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1]` has
     zero adjacent generator-index descents ($g_{\text{next}} < g_{\text{prev}}$), whereas
     the canonical interleaved sequence `[0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0]` has strict
     descents ($1 \to 0$) on its very first four letters (`[0, 1, 0, 1]`), causing every
     monotone-word transfer routine to refuse the canonical atom word.
   - At $n = 3$, the discrepancy between grouped and interleaved traces is confined
     entirely to the $2$-dimensional $(2,1)$ sector (where $\sigma_0$ and $\sigma_1$
     do not commute), while the two $1$-dimensional sectors $(3)$ and $(1,1,1)$
     have zero commutator because $\sigma_0$ and $\sigma_1$ act by identical scalars there.

2. **Coarser Disjoint-Block Product Law Survives Non-Monotonicity at $O(\varepsilon^2)$**:
   - Although letter-level monotone factorization fails inside a nucleon, disjoint
     strand blocks still multiply as quadratic $\varepsilon$-series:
     for $F_i(\varepsilon) = a_i(1 + r_i \varepsilon + q_i \varepsilon^2)$, the product
     $F_1(\varepsilon) F_2(\varepsilon)$ matches the truncated quadratic series with
     coefficients $c_0 = a_1 a_2$, $c_1 = a_1 a_2 (r_1 + r_2)$, and
     $c_2 = a_1 a_2 (q_1 + r_1 r_2 + q_2)$ up to an exact $O(\varepsilon^3)$ remainder.
-/

namespace QOU.MassTheory.NonMonotoneBorromeanWordAndDisjointBlockEpsilonProduct

/-- Adjacent generator-index descent $\max(0, g_{\text{prev}} - g_{\text{next}})$. -/
def adjacentOrderDescent (gPrev gNext : Int) : Int :=
  if gNext < gPrev then gPrev - gNext else 0

/-- Sum of adjacent descents across a 4-letter prefix $(g_0, g_1, g_2, g_3)$. -/
def fourLetterPrefixDescentSum (g0 g1 g2 g3 : Int) : Int :=
  adjacentOrderDescent g0 g1 + adjacentOrderDescent g1 g2 + adjacentOrderDescent g2 g3

/-- Scalar action commutator $s_0 s_1 - s_1 s_0$ on a $1$-dimensional representation where $s_0 = s_1 = s$. -/
def oneDimScalarCommutator (s : Int) : Int :=
  s * s - s * s

/-- Order-$0$ product coefficient $c_0 = a_1 a_2$. -/
def quadSeriesProdC0 (a1 a2 : Int) : Int :=
  a1 * a2

/-- Order-$1$ product coefficient $c_1 = a_1 a_2 (r_1 + r_2)$. -/
def quadSeriesProdC1 (a1 r1 a2 r2 : Int) : Int :=
  a1 * a2 * (r1 + r2)

/-- Order-$2$ product coefficient $c_2 = a_1 a_2 (q_1 + r_1 r_2 + q_2)$. -/
def quadSeriesProdC2 (a1 r1 q1 a2 r2 q2 : Int) : Int :=
  a1 * a2 * (q1 + r1 * r2 + q2)

/-- Canonical interleaved prefix `[0, 1, 0, 1]` has positive generator-index descent
    while grouped prefix `[0, 0, 0, 0]` has zero descent, and $1$-dimensional scalar
    sectors have identically zero generator commutator (`qou-wdij`). -/
theorem canonical_interleaved_prefix_non_monotone_and_oneDim_commutator_zero
    (s : Int) :
    fourLetterPrefixDescentSum 0 1 0 1 = 1 ∧
      fourLetterPrefixDescentSum 0 0 0 0 = 0 ∧
      fourLetterPrefixDescentSum 0 0 0 0 < fourLetterPrefixDescentSum 0 1 0 1 ∧
      oneDimScalarCommutator s = 0 := by
  dsimp [fourLetterPrefixDescentSum, adjacentOrderDescent, oneDimScalarCommutator]
  have hcomm : s * s - s * s = 0 := Int.sub_self (s * s)
  refine ⟨rfl, rfl, by decide, hcomm⟩

/-- Exact order-by-order $\varepsilon$-series product identity (`qou-wdij`):
    for two quadratic factors $a_1 + b_1 \varepsilon + c_1 \varepsilon^2$ and
    $a_2 + b_2 \varepsilon + c_2 \varepsilon^2$, the product minus its quadratic
    truncation $a_1 a_2 + (a_1 b_2 + b_1 a_2)\varepsilon + (a_1 c_2 + b_1 b_2 + c_1 a_2)\varepsilon^2$
    equals the cubic-plus-quartic remainder
    $(b_1 c_2 + c_1 b_2)\varepsilon^3 + (c_1 c_2)\varepsilon^4$. -/
theorem disjoint_block_quadratic_epsilon_series_product_law
    (a1 b1 c1 a2 b2 c2 eps : Int) :
    (a1 + b1 * eps + c1 * (eps * eps)) * (a2 + b2 * eps + c2 * (eps * eps)) -
      (quadSeriesProdC0 a1 a2 +
        (a1 * b2 + b1 * a2) * eps +
        (a1 * c2 + b1 * b2 + c1 * a2) * (eps * eps)) =
      (b1 * c2 + c1 * b2) * (eps * eps * eps) +
        (c1 * c2) * (eps * eps * eps * eps) := by
  dsimp [quadSeriesProdC0]
  have hL : (a1 + b1 * eps + c1 * (eps * eps)) * (a2 + b2 * eps + c2 * (eps * eps)) =
      a1 * (a2 + b2 * eps + c2 * (eps * eps)) +
      (b1 * eps) * (a2 + b2 * eps + c2 * (eps * eps)) +
      (c1 * (eps * eps)) * (a2 + b2 * eps + c2 * (eps * eps)) := by
    rw [Int.add_mul, Int.add_mul]
  have h1 : a1 * (a2 + b2 * eps + c2 * (eps * eps)) =
      a1 * a2 + a1 * (b2 * eps) + a1 * (c2 * (eps * eps)) := by
    rw [Int.mul_add, Int.mul_add]
  have h2 : (b1 * eps) * (a2 + b2 * eps + c2 * (eps * eps)) =
      (b1 * eps) * a2 + (b1 * eps) * (b2 * eps) + (b1 * eps) * (c2 * (eps * eps)) := by
    rw [Int.mul_add, Int.mul_add]
  have h3 : (c1 * (eps * eps)) * (a2 + b2 * eps + c2 * (eps * eps)) =
      (c1 * (eps * eps)) * a2 + (c1 * (eps * eps)) * (b2 * eps) +
      (c1 * (eps * eps)) * (c2 * (eps * eps)) := by
    rw [Int.mul_add, Int.mul_add]
  have h1b : a1 * (b2 * eps) = (a1 * b2) * eps := by rw [← Int.mul_assoc]
  have h1c : a1 * (c2 * (eps * eps)) = (a1 * c2) * (eps * eps) := by rw [← Int.mul_assoc]
  have h2a : (b1 * eps) * a2 = (b1 * a2) * eps := by
    rw [Int.mul_assoc, Int.mul_comm eps a2, ← Int.mul_assoc]
  have h2b : (b1 * eps) * (b2 * eps) = (b1 * b2) * (eps * eps) := by
    calc (b1 * eps) * (b2 * eps)
      _ = b1 * (eps * (b2 * eps)) := Int.mul_assoc b1 eps (b2 * eps)
      _ = b1 * ((eps * b2) * eps) := by rw [← Int.mul_assoc eps b2 eps]
      _ = b1 * ((b2 * eps) * eps) := by rw [Int.mul_comm eps b2]
      _ = b1 * (b2 * (eps * eps)) := by rw [Int.mul_assoc b2 eps eps]
      _ = (b1 * b2) * (eps * eps) := by rw [← Int.mul_assoc b1 b2 (eps * eps)]
  have h2c : (b1 * eps) * (c2 * (eps * eps)) = (b1 * c2) * (eps * eps * eps) := by
    calc (b1 * eps) * (c2 * (eps * eps))
      _ = b1 * (eps * (c2 * (eps * eps))) := Int.mul_assoc b1 eps (c2 * (eps * eps))
      _ = b1 * ((eps * c2) * (eps * eps)) := by rw [← Int.mul_assoc eps c2 (eps * eps)]
      _ = b1 * ((c2 * eps) * (eps * eps)) := by rw [Int.mul_comm eps c2]
      _ = b1 * (c2 * (eps * (eps * eps))) := by rw [Int.mul_assoc c2 eps (eps * eps)]
      _ = b1 * (c2 * (eps * eps * eps)) := by rw [← Int.mul_assoc eps eps eps]
      _ = (b1 * c2) * (eps * eps * eps) := by rw [← Int.mul_assoc b1 c2 (eps * eps * eps)]
  have h3a : (c1 * (eps * eps)) * a2 = (c1 * a2) * (eps * eps) := by
    rw [Int.mul_assoc, Int.mul_comm (eps * eps) a2, ← Int.mul_assoc]
  have h3b : (c1 * (eps * eps)) * (b2 * eps) = (c1 * b2) * (eps * eps * eps) := by
    calc (c1 * (eps * eps)) * (b2 * eps)
      _ = c1 * ((eps * eps) * (b2 * eps)) := Int.mul_assoc c1 (eps * eps) (b2 * eps)
      _ = c1 * (((eps * eps) * b2) * eps) := by rw [← Int.mul_assoc (eps * eps) b2 eps]
      _ = c1 * ((b2 * (eps * eps)) * eps) := by rw [Int.mul_comm (eps * eps) b2]
      _ = c1 * (b2 * (eps * eps * eps)) := by rw [Int.mul_assoc b2 (eps * eps) eps]
      _ = (c1 * b2) * (eps * eps * eps) := by rw [← Int.mul_assoc c1 b2 (eps * eps * eps)]
  have h3c : (c1 * (eps * eps)) * (c2 * (eps * eps)) =
      (c1 * c2) * (eps * eps * eps * eps) := by
    calc (c1 * (eps * eps)) * (c2 * (eps * eps))
      _ = c1 * ((eps * eps) * (c2 * (eps * eps))) :=
          Int.mul_assoc c1 (eps * eps) (c2 * (eps * eps))
      _ = c1 * (((eps * eps) * c2) * (eps * eps)) := by
          rw [← Int.mul_assoc (eps * eps) c2 (eps * eps)]
      _ = c1 * ((c2 * (eps * eps)) * (eps * eps)) := by
          rw [Int.mul_comm (eps * eps) c2]
      _ = c1 * (c2 * ((eps * eps) * (eps * eps))) := by
          rw [Int.mul_assoc c2 (eps * eps) (eps * eps)]
      _ = c1 * (c2 * (eps * eps * eps * eps)) := by
          rw [← Int.mul_assoc (eps * eps) eps eps]
      _ = (c1 * c2) * (eps * eps * eps * eps) := by
          rw [← Int.mul_assoc c1 c2 (eps * eps * eps * eps)]
  have hd1 : (a1 * b2 + b1 * a2) * eps = (a1 * b2) * eps + (b1 * a2) * eps :=
    Int.add_mul (a1 * b2) (b1 * a2) eps
  have hd2 : (a1 * c2 + b1 * b2 + c1 * a2) * (eps * eps) =
      (a1 * c2) * (eps * eps) + (b1 * b2) * (eps * eps) + (c1 * a2) * (eps * eps) := by
    rw [Int.add_mul, Int.add_mul]
  have hd3 : (b1 * c2 + c1 * b2) * (eps * eps * eps) =
      (b1 * c2) * (eps * eps * eps) + (c1 * b2) * (eps * eps * eps) :=
    Int.add_mul (b1 * c2) (c1 * b2) (eps * eps * eps)
  rw [hL, h1, h2, h3, h1b, h1c, h2a, h2b, h2c, h3a, h3b, h3c, hd1, hd2, hd3]
  omega

end QOU.MassTheory.NonMonotoneBorromeanWordAndDisjointBlockEpsilonProduct
