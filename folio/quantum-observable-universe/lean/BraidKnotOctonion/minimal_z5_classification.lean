import Mathlib.Tactic

/-!
# QOU.HyperellipticQuintic.minimal_z5_classification

Canonical Lean declaration for content block at
[`quantum-observable-universe/braids-and-knots/hyperelliptic-z5-classification.ts`](quantum-observable-universe/braids-and-knots/hyperelliptic-z5-classification.ts).

The `lean.ref` URI `qou:QOU.HyperellipticQuintic.minimal_z5_classification`
resolves to `minimal_z5_classification` below.

The classification theorem has two layers:

* the **geometric** input — that the minimal genus of a hyperelliptic
  Riemann surface carrying a faithful `ℤ₅` automorphism commuting with
  the hyperelliptic involution is `g = 2` (the `bar φ`-orbit / Möbius-
  normalisation argument in the manuscript).  This is the single open
  categorical/geometric fact, carried here as a hypothesis `hg : g = 2`;
* the **arithmetic** consequence — that the branch divisor then has
  `|Branch(π)| = 2g + 2 = 6` by Riemann–Hurwitz.  This is a genuine
  computation and is *derived* (`by`/`omega`), not projected from an
  opaque context field.

This is pattern A of the vacuity-fix playbook: isolate the lone open
geometric input (`g = 2`) as a hypothesis and mechanically derive the
remaining numerical claims.  The previous encoding posited the whole
conjunction as a single class field and projected it — a vacuous
self-assuming projection — and is removed.
-/

namespace QOU.HyperellipticQuintic

/-- Riemann–Hurwitz branch count for a hyperelliptic (degree-`2`)
cover: `|Branch(π)| = 2g + 2`. -/
def branchCount (g : ℕ) : ℕ := 2 * g + 2

/-- **Minimal `ℤ₅`-hyperelliptic classification** (Riemann–Hurwitz
numerics) — [manuscript theorem].

Let `X` be a smooth projective Riemann surface of minimal genus that is
hyperelliptic (degree-`2` cover `π : X → ℙ¹` with involution `ι`) and
admits a faithful `ℤ₅` automorphism `φ` commuting with `ι`.  The
manuscript shows by the `bar φ`-orbit / Möbius-normalisation argument
that the minimal such genus is `g = 2`; this is the lone open geometric
input, carried as the hypothesis `hg : g = 2`.

Given `g = 2`, the branch-divisor cardinality is **derived**:
`|Branch(π)| = 2g + 2 = 6`.  (The full classification — `X ≅ 𝒳₅ :
y² = x⁵ − 1` — concerns the curve isomorphism and is tracked
separately.) -/
-- Ref: [leitner2026] quantum-observable-universe/braids-and-knots/hyperelliptic-z5-classification.ts
theorem minimal_z5_classification {g branch_count : ℕ}
    (hg : g = 2) (hbranch : branch_count = branchCount g) :
    g = 2 ∧ branch_count = 2 * g + 2 ∧ branch_count = 6 := by
  refine ⟨hg, ?_, ?_⟩
  · rw [hbranch, branchCount]
  · rw [hbranch, branchCount, hg]

end QOU.HyperellipticQuintic
