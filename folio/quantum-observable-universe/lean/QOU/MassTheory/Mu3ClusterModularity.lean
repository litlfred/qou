/-
# The μ₃ sign door is exactly the (sub/super)-modularity of the joint block-trace

Companion to `QOU.MassTheory.Mu4RhoFCluster` (#4354), which proved the **pairwise
product** ρ_F cluster route cannot supply the positive residual moment
`μ₃ = +0.4708` (`mu3_ne_pairwise_3body_cluster`; the multiplicative
`c(1 − ∏ fᵢ)`, `fᵢ ∈ [0,1]`, has non-positive beyond-pairwise 3-body content, and
`markovZD_lt_one_iff` forecloses the only escape `fᵢ > 1` at `q₀ ≈ 1.110`, where
`z = q³/(q²+1) < 1`).  The standing OPEN door
that wall leaves is a **genuine non-multiplicative 3-body operator** — the connected
(Ursell) part of the *joint* block-trace, which does not factor into pairwise
factors.

This file makes the open door **precise and checkable**.  The framework's connected
3-body cluster (`computations/three_body_joint_trace_a3.py`, H₉ joint trace, 0 fit)
is

    c₃ = joint − pair_sum = E₀·(g_a + g_b − g_∅ − g_ab),

where `g(S) = Σ_λ y_λ |χ_λ(w_S)|` is the block-trace of the braid word carrying the
interface subset `S ⊆ {a, b}`.  The bracket is exactly **minus the second mixed
finite difference** of the set function `g` on the interface Boolean lattice:

    Δ²g := g_ab − g_a − g_b + g_∅,        c₃ = −E₀·Δ²g.

Hence (for `E₀ > 0`)

    sign(c₃) = −sign(Δ²g),   and   c₃ > 0  ⟺  Δ²g < 0  ⟺  g strictly **submodular**.

So the positive residual moment `μ₃ > 0` is reachable **iff** the joint block-trace
is strictly submodular (co-present bonds reduce the trace by *less* than the sum of
their independent reductions — diminishing returns / the joint saturating *above*
the pair-sum).

**Two facts pin the door (this file, sorry-free):**

* `cluster_eq_neg_second_diff` — the identity `c₃ = −E₀·Δ²g` (ring).
* `mu3_pos_iff_submodular` / `mu3_requires_submodular` — `μ₃ = c₃ > 0` (with
  `E₀ > 0`) forces `Δ²g < 0`: the open question is *exactly* submodularity.
* `multiplicative_second_diff` + `multiplicative_supermodular` +
  `multiplicative_cluster_nonpos` — a **product-decrease** block-trace
  (`g_S = g_∅·∏_{i∈S} rᵢ`, `rᵢ ∈ [0,1]`) has `Δ²g = g_∅·(1−r_a)(1−r_b) ≥ 0`
  (**supermodular**), so its cluster is `≤ 0`.  This **re-derives the #4354 wall in
  the modularity language** and unifies it: the multiplicative route is on the
  *supermodular* (wrong) side, and `μ₃ > 0` demands the *submodular* side that no
  product model reaches.

**Scope discipline.**  This is a scope-(b) *structural bridge* — it converts the
open "3-body sign" question into the sharply-stated "sign of Δ²g" question and
re-derives the multiplicative wall — it does **not** by itself prove the joint
block-trace's sign is forced.  The FKG epic (`qou-x631`,
`wlambda-covariance-epic-phase4b-fkg-comonotone`) found `f^λ` is *not* universally
log-supermodular (fails at `k = 8`), so there is **no** universal
sign-definiteness theorem for these character functionals; supermodularity of the
*measured* joint trace (probe below) is a scope-(a) property of the specific
operator, not a forced invariant.  The companion probe
`computations/deltalambda/mu3_cluster_modularity_probe.py` measures `Δ²g` from the
cached joint-trace witness (0 fit) and finds it **positive** (supermodular) for
both A=3 isotopes — so the specific H₉ joint-trace operator also lands on the wrong
sign side.

**Anti-fit.**  `μ₃ > 0` enters only as a hypothesis; no AME quantity is fitted, no
normalization is wired.  The `Δ²g` measurement is q₀-only, 0 fit.

**Measurement provenance (corrected 2026-08-02).**  This file adds **no probe** — the
`Δ²g` values quoted above are not measured here.  They are corroborated on `main` by
`computations/deltalambda/ursell_slot_alignment_probe.py`, which reproduces the `c₃`
baseline (−1.769 T, −1.405 ³He) exactly, and are consumed by
`computations/deltalambda/triangle_bond_submodularity_probe.py` (GAP-3), which tests
the non-adjacent (1–3) bond flagged here as the untested derived lever.

**Slot correction (from the merged GAP-7 work).**  The `μₖ` moments are indexed by
*particle* count while `Δᵐg` is indexed by *bond* count, so the triangle's correct
assembly is `μ₃-slot = ∑Δ²g + Δ³g` (`QOU.MassTheory.UrsellSlotAlignment.triangle_moment_decomp`).
That correction roughly **doubles the magnitude but preserves the sign**, so the
obstruction proved below survives it and the μ₃ gap widens; the equivalence
`c₃ > 0 ⟺ Δ²g < 0` proved here is unaffected, since it is an identity in the
two-bond variables, not a claim about which slot the residual occupies.
-/
import Mathlib.Tactic

/-
VERIFICATION STATUS: `lean`-direct exit 0, sorry-free (see PR).  Self-contained
(`import Mathlib.Tactic` only); all proofs are `ring`/`nlinarith`/`mul_nonneg`.
-/

namespace QOU.MassTheory.Mu3ClusterModularity

/-! ### The second mixed difference and the cluster identity -/

/-- The **second mixed finite difference** of a set-function `g` on the interface
Boolean lattice `{∅, a, b, ab}`, represented by its four values
`(g_∅, g_a, g_b, g_ab)`:  `Δ²g = g_ab − g_a − g_b + g_∅`.  `Δ²g > 0` is
**supermodularity** (co-present bonds reinforce), `Δ²g < 0` is **submodularity**
(diminishing returns). -/
def secondDiff (g₀ gₐ g_b gₐᵦ : ℝ) : ℝ := gₐᵦ - gₐ - g_b + g₀

/-- The connected 3-body cluster of the joint block-trace,
`c₃ = joint − pair_sum = E₀·(g_a + g_b − g_∅ − g_ab)` (the framework's
`three_body_joint_trace_a3` object). -/
def cluster3 (E₀ g₀ gₐ g_b gₐᵦ : ℝ) : ℝ := E₀ * (gₐ + g_b - g₀ - gₐᵦ)

/-- **The cluster is minus `E₀` times the second mixed difference.**
`c₃ = −E₀·Δ²g`.  This is the whole content: the connected 3-body cluster sign is
the (opposite of the) modularity sign of the joint block-trace. -/
theorem cluster_eq_neg_second_diff (E₀ g₀ gₐ g_b gₐᵦ : ℝ) :
    cluster3 E₀ g₀ gₐ g_b gₐᵦ = -E₀ * secondDiff g₀ gₐ g_b gₐᵦ := by
  unfold cluster3 secondDiff; ring

/-! ### The μ₃ door: `μ₃ > 0` ⟺ the joint block-trace is strictly submodular -/

/-- **The door, as an iff.**  With `E₀ > 0`, the connected cluster is positive
**iff** the second mixed difference is negative — i.e. iff the joint block-trace
is strictly **submodular**. -/
theorem cluster_pos_iff_submodular {E₀ g₀ gₐ g_b gₐᵦ : ℝ} (hE : 0 < E₀) :
    0 < cluster3 E₀ g₀ gₐ g_b gₐᵦ ↔ secondDiff g₀ gₐ g_b gₐᵦ < 0 := by
  rw [cluster_eq_neg_second_diff]
  constructor
  · intro h
    nlinarith [h]
  · intro h
    have : 0 < E₀ * (-(secondDiff g₀ gₐ g_b gₐᵦ)) :=
      mul_pos hE (by linarith)
    nlinarith [this]

/-- **`μ₃ > 0` forces submodularity.**  If the positive residual moment `μ₃`
equals the connected cluster `c₃` (with `E₀ > 0`), then the joint block-trace is
strictly submodular (`Δ²g < 0`).  This is the exact reframing of the standing open
sign question: μ₃ is reachable by the joint-trace cluster **only** in the
submodular regime. -/
theorem mu3_requires_submodular {μ₃ E₀ g₀ gₐ g_b gₐᵦ : ℝ} (hμ : 0 < μ₃)
    (hE : 0 < E₀) (heq : μ₃ = cluster3 E₀ g₀ gₐ g_b gₐᵦ) :
    secondDiff g₀ gₐ g_b gₐᵦ < 0 := by
  rw [(cluster_pos_iff_submodular hE).symm]; rwa [← heq]

/-! ### Multiplicative (product-decrease) block-trace ⇒ supermodular ⇒ `c₃ ≤ 0`

Re-derivation of the #4354 wall in the modularity language.  A block-trace that
factors as a product of independent per-interface **decrease** factors
`rᵢ ∈ [0,1]` (`g_a = g₀·r_a`, `g_b = g₀·r_b`, `g_ab = g₀·r_a·r_b`) is supermodular,
so its connected cluster is non-positive — the multiplicative route is on the
*wrong* side of the door. -/

/-- For a product-decrease block-trace, `Δ²g = g₀·(1 − r_a)·(1 − r_b)`. -/
theorem multiplicative_second_diff (g₀ rₐ r_b : ℝ) :
    secondDiff g₀ (g₀ * rₐ) (g₀ * r_b) (g₀ * rₐ * r_b)
      = g₀ * (1 - rₐ) * (1 - r_b) := by
  unfold secondDiff; ring

/-- **Multiplicative ⇒ supermodular.**  With `g₀ > 0` and decrease factors
`r_a, r_b ∈ [0,1]`, the product-decrease block-trace has `Δ²g ≥ 0`. -/
theorem multiplicative_supermodular {g₀ rₐ r_b : ℝ} (hg : 0 < g₀)
    (ha₀ : 0 ≤ rₐ) (ha₁ : rₐ ≤ 1) (hb₀ : 0 ≤ r_b) (hb₁ : r_b ≤ 1) :
    0 ≤ secondDiff g₀ (g₀ * rₐ) (g₀ * r_b) (g₀ * rₐ * r_b) := by
  rw [multiplicative_second_diff]
  have h1 : (0:ℝ) ≤ 1 - rₐ := by linarith
  have h2 : (0:ℝ) ≤ 1 - r_b := by linarith
  exact mul_nonneg (mul_nonneg (le_of_lt hg) h1) h2

/-- **Multiplicative ⇒ non-positive cluster.**  The product-decrease block-trace's
connected 3-body cluster is `≤ 0` (for `E₀ ≥ 0`): it lands on the supermodular /
`c₃ ≤ 0` side, so it can never equal `μ₃ > 0`.  Modularity-language re-derivation
of `QOU.MassTheory.mu3_ne_pairwise_3body_cluster`. -/
theorem multiplicative_cluster_nonpos {E₀ g₀ rₐ r_b : ℝ} (hE : 0 ≤ E₀)
    (hg : 0 < g₀) (ha₀ : 0 ≤ rₐ) (ha₁ : rₐ ≤ 1) (hb₀ : 0 ≤ r_b) (hb₁ : r_b ≤ 1) :
    cluster3 E₀ g₀ (g₀ * rₐ) (g₀ * r_b) (g₀ * rₐ * r_b) ≤ 0 := by
  rw [cluster_eq_neg_second_diff]
  have hsm := multiplicative_supermodular hg ha₀ ha₁ hb₀ hb₁
  nlinarith [mul_nonneg hE hsm]

/-- **(WALL, modularity form.)**  `μ₃ > 0` cannot equal any multiplicative
product-decrease cluster.  Companion to `mu3_ne_pairwise_3body_cluster`; the two
prove the same exclusion from the two viewpoints (product content ≤ 0 vs.
supermodular Δ²g ≥ 0). -/
theorem mu3_ne_multiplicative_cluster {μ₃ E₀ g₀ rₐ r_b : ℝ} (hμ : 0 < μ₃)
    (hE : 0 ≤ E₀) (hg : 0 < g₀) (ha₀ : 0 ≤ rₐ) (ha₁ : rₐ ≤ 1)
    (hb₀ : 0 ≤ r_b) (hb₁ : r_b ≤ 1) :
    μ₃ ≠ cluster3 E₀ g₀ (g₀ * rₐ) (g₀ * r_b) (g₀ * rₐ * r_b) := by
  have hcl := multiplicative_cluster_nonpos hE hg ha₀ ha₁ hb₀ hb₁
  intro hEq; rw [hEq] at hμ; linarith

end QOU.MassTheory.Mu3ClusterModularity
