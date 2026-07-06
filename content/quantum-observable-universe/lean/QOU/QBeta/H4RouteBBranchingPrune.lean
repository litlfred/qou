/-
Copyright (c) 2026 litlfred. All rights reserved.

# H₄ route-B structural prune — the branching exclusion, machine-checked

Bean `8we6` (genuine c₄ rungs → Casoratian W₃ sign test) authorised three routes
to the missing `c₄^even` Q_β rung. **Route B** — keep the validated H₃ transition
element `Δ(net)` unchanged, include it in `H₄(q)`, and read its `λ ⊢ 4` Hoefsmit
block levels as the N=4 rung — was pruned *before any build* by a one-line
structural argument (audit `docs/audits/2026-07-03-8we6-h4-route-b-structural-prune.md`).
This file makes that argument a proved theorem.

**The argument.** For an element of `H₃ ⊂ H₄`, its `λ ⊢ 4` characters are fixed
sums of its `λ ⊢ 3` characters, by the branching rule `S₄ ↓ S₃`
(remove one box):

    χ₍₄₎     = χ₍₃₎
    χ₍₃,₁₎   = χ₍₃₎ + χ₍₂,₁₎
    χ₍₂,₂₎   = χ₍₂,₁₎
    χ₍₂,₁,₁₎ = χ₍₂,₁₎ + χ₍₁,₁,₁₎
    χ₍₁,₁,₁,₁₎ = χ₍₁,₁,₁₎

So the five `λ ⊢ 4` readings are the image of the three `λ ⊢ 3` readings under a
fixed linear map. Two consequences, both proved below:

* `branchToH4_two_relations` — the five `λ ⊢ 4` readings satisfy **two** fixed
  branching relations (`χ₍₃,₁₎ = χ₍₄₎ + χ₍₂,₂₎` and `χ₍₂,₁,₁₎ = χ₍₂,₂₎ + χ₍₁,₁,₁₎`).
  They carry no independent N=4 degree of freedom — the route-B prune, scope-(a)
  with the invariant (branching) cited.
* `branchToH4_injective` — conversely the three `λ ⊢ 3` readings are recoverable
  from the `λ ⊢ 4` readings, so the H₃ data is exactly the independent content.

**Consequence for the build.** A genuine `c₄^even` rung must come from an H₄ object
with **σ₂-support** (route A), not from re-decomposing the unchanged H₃ element.
Route A's object choice is owner-gated framework content, not an agent ansatz.

Base ring: only addition is used — no `0`, associativity, or commutativity — so
this is stated over the weakest structure that types `branchToH4`, `[Add R]`
(CLAUDE.md §7c — weakest honest base). The block readings are formal parameters
with no archimedean structure. Sorry-free.

`-- Ref:` [sagan2001] the branching rule `Sₙ ↓ Sₙ₋₁` (remove one box) is standard
symmetric-group representation theory; the q-analogue (restriction along
`H_{n} ↪ H_{n+1}`) is likewise standard (Goodman–Wenzl, Ram,
`docs/audits/2026-07-03-8we6-h4-route-b-structural-prune.md`).
-/
import Mathlib.Algebra.Group.Basic

namespace QOU.QBeta

variable {R : Type*} [Add R]

/-- The five `λ ⊢ 4` block readings of an element of `H₃ ⊂ H₄`, as functions of its
    three `λ ⊢ 3` readings `(a, b, c) = (χ₍₃₎, χ₍₂,₁₎, χ₍₁,₁,₁₎)`, by the branching
    rule `S₄ ↓ S₃`. Order: `(χ₍₄₎, χ₍₃,₁₎, χ₍₂,₂₎, χ₍₂,₁,₁₎, χ₍₁,₁,₁,₁₎)`. -/
def branchToH4 (a b c : R) : R × R × R × R × R := (a, a + b, b, b + c, c)

/-- **Route-B prune (no independent N=4 rung).** The five `λ ⊢ 4` block readings of
    any element of `H₃ ⊂ H₄` satisfy two fixed branching relations, so they are
    determined by the three `λ ⊢ 3` readings — re-decomposing the unchanged H₃
    element at `λ ⊢ 4` cannot produce a genuine `c₄^even` rung. -/
theorem branchToH4_two_relations (a b c : R) :
    (branchToH4 a b c).2.1 = (branchToH4 a b c).1 + (branchToH4 a b c).2.2.1 ∧
    (branchToH4 a b c).2.2.2.1 = (branchToH4 a b c).2.2.1 + (branchToH4 a b c).2.2.2.2 :=
  ⟨rfl, rfl⟩

/-- **H₃ data is the independent content.** The `λ ⊢ 3` readings are recovered from
    the `λ ⊢ 4` readings (`a = χ₍₄₎`, `b = χ₍₂,₂₎`, `c = χ₍₁,₁,₁,₁₎`), so `branchToH4`
    is injective: it adds no information beyond the three H₃ numbers. -/
theorem branchToH4_injective :
    Function.Injective (fun t : R × R × R => branchToH4 t.1 t.2.1 t.2.2) := by
  rintro ⟨a₁, b₁, c₁⟩ ⟨a₂, b₂, c₂⟩ h
  simp only [branchToH4, Prod.mk.injEq] at h
  obtain ⟨ha, _, hb, _, hc⟩ := h
  simp [ha, hb, hc]

end QOU.QBeta
