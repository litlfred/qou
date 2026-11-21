import QOU.MassTheory.TransverseSurfaceCurvature

/-!
# QOU.MassTheory.TransversePairingClusterDecomposition

**The transverse non-abelian-Stokes pairing is an exactly *quadratic* cluster
functional: it has NO irreducible three-body content at fixed curvature data.**

Companion to
[`TransverseSurfaceCurvature`](TransverseSurfaceCurvature.lean) (the ordered
pairing `listPairing` and the trace-annihilation theorem) and
[`GermRootVectorGaugeFixing`](GermRootVectorGaugeFixing.lean) (the
single-generator scope-(b) vanishing). Bean `qou-prjo`.

## Why this file exists

The bean's open gate is the **super-pairwise extensive** many-body binding term.
Two readings of the transverse surface curvature are already excluded:

* the **diagonal / Betti-count** reading is exactly linear in link count
  (`seifertBettiOne_link_additive`) hence pairwise-capped;
* the **scalar-trace** readout vanishes identically (`listPairing_trace_zero`).

That leaves the **off-diagonal cross-handle pairing**, whose super-pairwise
status was untested. This file settles the *algebraic* half of the question,
and it settles it **negatively at fixed curvature data**:

> `listPairing` is bilinear in the transported curvatures, so under **any**
> partition of the surface bands into ordered blocks it decomposes **exactly**
> into one-block and two-block terms — `listPairing_append`. Consequently the
> three-block Möbius (cluster) residual **vanishes identically**
> (`moebius3_eq_zero`), as does the four-block one (`moebius4_eq_zero`).

So a nonzero measured three-body residual can have **exactly one** source: the
per-block transported-curvature *lists themselves* differ between
sub-configurations. Under the pinned Yekutieli ordering the transport to a band
is the ordered product of **everything earlier in the word**, so deleting a
nucleon changes the transport of every later one — the lists are
context-dependent and the residual is generically nonzero. This file makes that
the *only* available mechanism, which is what turns a numerical measurement of
the residual into a statement about transport rather than about curvature.

## What is proved (sorry-free)

| Layer | Declarations |
|---|---|
| Bilinearity | `curvComm_add_left`, `curvComm_add_right`, `rowPairing_eq_curvComm_sum`, `rowPairing_append` |
| Exact block decomposition | `listPairing_append` (the one-block + one-block + **cross** identity), `listPairing_append_eq_add_iff` |
| Additivity criteria | `crossPairing_eq_zero_of_commute`, `listPairing_append_add_of_collinear` (the `GermRootVectorGaugeFixing` mechanism, restated in cluster language) |
| **No irreducible ≥3-body content** | `moebius3_eq_zero`, `moebius4_eq_zero` |

## What is NOT proved — read before citing

* This does **not** show the transverse pairing is additive over links *in
  practice*. It shows the residual is zero **when the block curvature lists are
  held fixed**. The measured residual on real multi-generator words is nonzero
  (probe
  `computations/probes/nastokes_multigen_cluster_additivity_probe.py`), and by
  the theorems here that nonzero value is *entirely* attributable to
  context-dependence of the Yekutieli transport.
* Nothing here derives a **magnitude**. `sorry-free ≠ derived`: no binding
  energy, no `Δ_λ`, no AME comparison appears in this file, and nothing is
  wired.
* `listPairing` uses the surface-**ordered** (Yekutieli) convention. A
  homological reading weighted by a Seifert intersection form `J` is a
  different bilinear form; `listPairing_append` is the ordered case. The
  quadratic-hence-no-3-body argument applies verbatim to any bilinear form
  whose block restriction is the corresponding sub-block, but that
  generalisation is not formalised here.

**Base ring (§7c).** Generic non-commutative `Ring R` throughout; the collinear
corollary adds a generic `CommRing K` acting by `Algebra K R`. No `ℝ`, no
ordering, no `Real.*`, no archimedean evaluation.

## References
- Ref: [yekutieli2015] https://doi.org/10.1142/9537 — non-abelian multiplicative
  integration and Stokes' theorem on surfaces.
- Ref: [leitner2026] `docs/audits/2026-08-09-nastokes-multigenerator-cluster-additivity.md`
-/

namespace QOU.MassTheory.TransversePairingCluster

open QOU.MassTheory.TransverseSurfaceCurvature

variable {R : Type*} [Ring R]

/-! ## 1. Bilinearity of the curvature bracket -/

theorem curvComm_add_left (a b c : R) :
    curvComm (a + b) c = curvComm a c + curvComm b c := by
  simp only [curvComm, add_mul, mul_add]
  abel

theorem curvComm_add_right (a b c : R) :
    curvComm a (b + c) = curvComm a b + curvComm a c := by
  simp only [curvComm, add_mul, mul_add]
  abel

/-- **A row of the ordered pairing is a single bracket against the row sum.**
    `rowPairing c l = ⟦Σ l, c⟧` — the cost of a row is one commutator, not
    `|l|` of them, and the row depends on `l` only through its sum. -/
theorem rowPairing_eq_curvComm_sum (c : R) (l : List R) :
    rowPairing c l = curvComm l.sum c := by
  induction l with
  | nil => simp [rowPairing, curvComm]
  | cons y ys ih => rw [rowPairing, ih, List.sum_cons, curvComm_add_left]

theorem rowPairing_append (c : R) (l₁ l₂ : List R) :
    rowPairing c (l₁ ++ l₂) = rowPairing c l₁ + rowPairing c l₂ := by
  simp only [rowPairing_eq_curvComm_sum, List.sum_append, curvComm_add_left]

/-! ## 2. The exact block decomposition -/

/-- **THE CLUSTER DECOMPOSITION.**

    Splitting the surface bands into an earlier block `l₁` and a later block
    `l₂`, the ordered transverse pairing is

      `Ω(l₁ ++ l₂) = Ω(l₁) + Ω(l₂) + ⟦Σ l₂, Σ l₁⟧`.

    The interaction between the two blocks is **one** commutator of the two
    block sums — the two-body cluster term. There is no residue beyond it: the
    pairing is bilinear, so a block decomposition terminates at second order. -/
theorem listPairing_append (l₁ l₂ : List R) :
    listPairing (l₁ ++ l₂)
      = listPairing l₁ + listPairing l₂ + curvComm l₂.sum l₁.sum := by
  induction l₁ with
  | nil => simp [listPairing, curvComm]
  | cons c t ih =>
    rw [List.cons_append, listPairing, listPairing, rowPairing_append, ih,
      rowPairing_eq_curvComm_sum c l₂, List.sum_cons, curvComm_add_right]
    abel

/-- **Additivity criterion.** The pairing is additive across a block split
    exactly when the two block sums commute. -/
theorem listPairing_append_eq_add_iff (l₁ l₂ : List R) :
    listPairing (l₁ ++ l₂) = listPairing l₁ + listPairing l₂
      ↔ curvComm l₂.sum l₁.sum = 0 := by
  rw [listPairing_append]
  constructor
  · intro h; exact add_eq_left.mp h
  · intro h; rw [h, add_zero]

theorem crossPairing_eq_zero_of_commute (l₁ l₂ : List R)
    (h : l₂.sum * l₁.sum = l₁.sum * l₂.sum) : curvComm l₂.sum l₁.sum = 0 := by
  rw [curvComm, h, sub_self]

/-- **The `GermRootVectorGaugeFixing` mechanism in cluster language.** If both
    block sums are scalar multiples of one common element — the situation forced
    on a single-generator word, where every transported curvature is a scalar
    multiple of the root vector `F_q` — the cross term vanishes and the pairing
    *is* additive across the split. Multi-generator words break the hypothesis,
    which is exactly where the cross term can survive. -/
theorem listPairing_append_add_of_collinear {K : Type*} [CommRing K] [Algebra K R]
    (l₁ l₂ : List R) (F : R) (a b : K)
    (h₁ : l₁.sum = a • F) (h₂ : l₂.sum = b • F) :
    listPairing (l₁ ++ l₂) = listPairing l₁ + listPairing l₂ := by
  rw [listPairing_append_eq_add_iff, h₁, h₂, curvComm]
  rw [smul_mul_assoc, mul_smul_comm, smul_smul, smul_mul_assoc, mul_smul_comm,
    smul_smul, mul_comm b a, sub_self]

/-! ## 3. No irreducible three- or four-body content at fixed curvature data -/

/-- **THE MÖBIUS THEOREM (three blocks).**

    For *fixed* block curvature lists `l₁, l₂, l₃`, the three-body cluster
    (Möbius) residual of the ordered transverse pairing

      `Ω(123) − Ω(12) − Ω(13) − Ω(23) + Ω(1) + Ω(2) + Ω(3)`

    is **identically zero**. The pairing is bilinear, so every block
    decomposition stops at two-block terms and the alternating sum cancels them
    exactly.

    **Reading.** The transverse surface-curvature pairing carries *no*
    irreducible three-body content of its own. Any nonzero three-body residual
    measured on actual braid words is therefore not a property of the curvature
    at all: it can only come from the block lists *changing* between
    sub-configurations, i.e. from context-dependence of the parallel transport
    (under the Yekutieli ordering, the transport to a band is the ordered
    product of everything earlier in the word). -/
theorem moebius3_eq_zero (l₁ l₂ l₃ : List R) :
    listPairing (l₁ ++ l₂ ++ l₃)
        - listPairing (l₁ ++ l₂) - listPairing (l₁ ++ l₃) - listPairing (l₂ ++ l₃)
        + listPairing l₁ + listPairing l₂ + listPairing l₃ = 0 := by
  simp only [listPairing_append, List.sum_append, curvComm_add_right]
  abel

/-- **The four-block Möbius residual also vanishes identically**, for the same
    reason: a bilinear functional has no irreducible `k`-body content for
    `k ≥ 3`. Stated explicitly (rather than by induction over `Finset`s) so the
    cancellation is directly checkable. -/
theorem moebius4_eq_zero (l₁ l₂ l₃ l₄ : List R) :
    listPairing (l₁ ++ l₂ ++ l₃ ++ l₄)
        - listPairing (l₁ ++ l₂ ++ l₃) - listPairing (l₁ ++ l₂ ++ l₄)
        - listPairing (l₁ ++ l₃ ++ l₄) - listPairing (l₂ ++ l₃ ++ l₄)
        + listPairing (l₁ ++ l₂) + listPairing (l₁ ++ l₃) + listPairing (l₁ ++ l₄)
        + listPairing (l₂ ++ l₃) + listPairing (l₂ ++ l₄) + listPairing (l₃ ++ l₄)
        - listPairing l₁ - listPairing l₂ - listPairing l₃ - listPairing l₄ = 0 := by
  simp only [listPairing_append, List.sum_append, curvComm_add_right]
  abel

/-- **The three-body residual is exactly a transport defect.** If the block
    lists change from `lᵢ` to `lᵢ'` when the third block is present, the
    three-body residual equals the difference of the two Möbius sums — and the
    fixed-list one is zero by `moebius3_eq_zero`. This is the precise sense in
    which a measured nonzero residual measures *context-dependence of the
    transport*, not a three-body property of the curvature. -/
theorem moebius3_eq_sub_of_context (l₁ l₂ l₃ l₁' l₂' l₃' : List R) :
    listPairing (l₁' ++ l₂' ++ l₃')
        - listPairing (l₁ ++ l₂) - listPairing (l₁ ++ l₃) - listPairing (l₂ ++ l₃)
        + listPairing l₁ + listPairing l₂ + listPairing l₃
      = listPairing (l₁' ++ l₂' ++ l₃') - listPairing (l₁ ++ l₂ ++ l₃) := by
  have h := moebius3_eq_zero l₁ l₂ l₃
  linear_combination (norm := abel) h

end QOU.MassTheory.TransversePairingCluster
