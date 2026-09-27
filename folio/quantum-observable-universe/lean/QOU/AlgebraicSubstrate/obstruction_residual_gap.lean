import Mathlib.Tactic
import QOU.AlgebraicSubstrate.qou_obstruction_reduction

/-!
# Localising the residual gap of `thm:qou-obstruction-reduction` (Tier C, C11)

`collatz_contact_boundary` is §3b-conditional, and its docstring names the
residual as *"the `κ₀ = χ(A)` trace-gap input inherited from
`QouObstructionReductionContext`"*, with *"a full derivation of the remaining
substrate primitives remains pending"*. That is accurate but imprecise: it says a
gap remains without saying how large it is or what would close it.

This file measures it. Two results, both sorry-free:

1. **The gap is exactly one integer equation.** The context carries the gap
   across three fields — `trace_pairing`, `hattori_stallings`,
   `trace_pairing_cast`. `residual_gap_iff` shows that in the presence of
   `trace_pairing_cast` the Hattori–Stallings field is *logically equivalent* to
   the bare equation `κ₀ = χ(A)`. So the trace-pairing apparatus contributes
   nothing: the residual is one equation between two integers, not a body of
   analytic input.

2. **The structural inputs cannot close it.** The context's docstring asserts the
   gap "is NOT derivable from the two structural inputs (`vdb_duality`,
   `drinfeld_rigidity`)". That was prose. `structuralCore_not_force_gap` proves
   it: an explicit assignment satisfies both inputs while `κ₀ ≠ χ(A)`. And
   `structuralCore_hhCohDim_two` shows the same two inputs *do* still force
   conclusion (a), `dim HH² = 1` — so the separation is sharp. Conclusion (a) is
   derived; conclusions (b),(c) are not, and no strengthening of the two
   literature inputs will change that.

## Is the context a self-assuming projection? No — but the margin is thin

AGENTS.md §3b-cond rule 5 forbids a class that carries a block's own *conclusion*
as a field with a "theorem" that merely projects it. Result 1 shows
`obstruction_trace_gap` is close to that shape: strip `trace_pairing` and its
`_cast` and the remaining field says `κ₀ = χ(A)` outright.

It is nevertheless **not** a rule-5 violation, and the distinction is worth
stating because it is the whole justification for the current encoding. The
block's conclusion (c) is `κ₀ ≡ 0 (mod n) ↔ n ∣ χ(A)`. The assumed equation
`κ₀ = χ(A)` is not that conclusion; it is a *named literature input* (the
Hattori–Stallings / Chern-character trace computation) which, composed with the
**definitional** `kappa_vanishes_def`, yields the conclusion. Assuming a cited
theorem and deriving from it is the §3b-cond pattern working as intended.

What a reader should take away is narrower and more useful: the three trace
fields are one hypothesis wearing three names, so anyone auditing the residual
should audit `hattori_stallings` alone, and anyone closing it must supply an
actual Hochschild computation — no rearrangement of the existing fields will do
it.

Base ring: `ℤ` and `ℝ` only where the context already uses them; nothing new is
specialised (§7c).
-/

namespace QOU.AlgebraicSubstrate.ObstructionResidualGap

open QOU.AlgebraicSubstrate

/-! ## 1 — the residual is exactly `κ₀ = χ(A)` -/

/-- **The trace-pairing apparatus is decorative.** Given that the pairing is the
    canonical cast (`trace_pairing_cast`), the Hattori–Stallings hypothesis
    `trace_pairing χ(A) = κ₀` says *precisely* `κ₀ = χ(A)` and nothing more.

    Stated over free data rather than over the class, so that it characterises
    the *shape* of the hypothesis rather than merely re-deriving what an instance
    already grants. -/
theorem residual_gap_iff (tp : ℤ → ℝ) (chi kappa : ℤ)
    (hcast : ∀ z : ℤ, tp z = (z : ℝ)) :
    tp chi = (kappa : ℝ) ↔ kappa = chi := by
  rw [hcast chi]
  constructor
  · intro h
    exact_mod_cast h.symm
  · intro h
    rw [h]

/-- The same for the Chern-character field: given the cast, `φ₁ = trace χ(A)` is
    exactly `φ₁ = (χ(A) : ℝ)`. -/
theorem chern_character_iff (tp : ℤ → ℝ) (chi : ℤ) (phi : ℝ)
    (hcast : ∀ z : ℤ, tp z = (z : ℝ)) :
    phi = tp chi ↔ phi = (chi : ℝ) := by
  rw [hcast chi]

/-- **The residual, at the class.** For any context, the gap discharged by
    `obstruction_trace_gap` is equivalent to the single equation `κ₀ = χ(A)` —
    which the context grants. Recording it in this form makes the audit target
    unambiguous. -/
theorem context_residual_is_kappa_eq_chi [ctx : QouObstructionReductionContext] :
    (ctx.trace_pairing ctx.chi_A = (ctx.kappa0 : ℝ)) ↔ ctx.kappa0 = ctx.chi_A :=
  residual_gap_iff ctx.trace_pairing ctx.chi_A ctx.kappa0 ctx.trace_pairing_cast

/-! ## 2 — the structural inputs do not reach the gap

The two literature inputs constrain only the Hochschild dimensions. Isolating
them from the trace data shows exactly what they can and cannot do. -/

/-- The context's **structural core**: the two literature inputs
    (`vdb_duality`, `drinfeld_rigidity`) together with the raw dimension data and
    the two integers, but *without* any trace field. -/
structure StructuralCore where
  /-- `dim_k HH^i(U_q, Ad)`. -/
  hhCohDim : ℕ → ℕ
  /-- `dim_k HH_i(U_q, Ad)`. -/
  hhHomDim : ℕ → ℕ
  /-- Euler characteristic `χ(A)`. -/
  chi_A : ℤ
  /-- The primitive Kummer obstruction integer `κ₀`. -/
  kappa0 : ℤ
  /-- Van den Bergh / Calabi–Yau duality in dimension 3. -/
  vdb_duality : ∀ i : ℕ, i ≤ 3 → hhCohDim i = hhHomDim (3 - i)
  /-- Drinfeld rigidity. -/
  drinfeld_rigidity : hhHomDim 1 = 1

/-- **Conclusion (a) IS reached by the structural inputs alone**: CY-3 duality
    composed with Drinfeld rigidity gives `dim HH² = 1`, with no trace data. -/
theorem structuralCore_hhCohDim_two (c : StructuralCore) : c.hhCohDim 2 = 1 :=
  (c.vdb_duality 2 (by decide)).trans c.drinfeld_rigidity

/-- An explicit structural core with `χ(A) = 0` but `κ₀ = 1`. Both literature
    inputs hold; the two integers differ. -/
def gapWitness : StructuralCore where
  hhCohDim := fun i => if i = 2 then 1 else 0
  hhHomDim := fun j => if j = 1 then 1 else 0
  chi_A := 0
  kappa0 := 1
  vdb_duality := by decide +kernel
  drinfeld_rigidity := by norm_num

/-- **The structural inputs do NOT force `κ₀ = χ(A)`** — the context docstring's
    claim that the trace gap "is NOT derivable from the two structural inputs",
    now proved rather than asserted. `gapWitness` satisfies Van den Bergh duality
    and Drinfeld rigidity while `κ₀ ≠ χ(A)`.

    Combined with `structuralCore_hhCohDim_two` this separates the block's
    conclusions exactly: (a) follows from the literature inputs; (b) and (c) are
    independent of them and rest solely on the trace computation. -/
theorem structuralCore_not_force_gap :
    ∃ c : StructuralCore, c.kappa0 ≠ c.chi_A :=
  ⟨gapWitness, by decide⟩

/-- **What closing C11 requires, stated as a theorem rather than a hope.** Supply
    the single equation `κ₀ = χ(A)` and every conditional conclusion of
    `thm:qou-obstruction-reduction` follows for a structural core — conclusion
    (a) from the literature inputs, (c) from the equation plus the definitional
    vanishing predicate. Nothing else in the context is load-bearing. -/
theorem core_with_gap_gives_conclusions (c : StructuralCore)
    (hgap : c.kappa0 = c.chi_A) (kv : ℕ → Prop)
    (hdef : ∀ n : ℕ, kv n ↔ (n : ℤ) ∣ c.kappa0) :
    c.hhCohDim 2 = 1 ∧ ∀ n : ℕ, (kv n ↔ (n : ℤ) ∣ c.chi_A) := by
  refine ⟨structuralCore_hhCohDim_two c, fun n => ?_⟩
  rw [hdef n, hgap]

end QOU.AlgebraicSubstrate.ObstructionResidualGap
