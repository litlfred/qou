# Author Questions — Meat-Adding Pass Analysis

Compiled while upgrading ~212 placeholder canonicals on PR #806.
Each question has 2-4 concrete options to pick from.

## Q1 — How aggressive should we be with `claim : Prop` vs typed?

Currently every block carries:

```lean
class FooContext where
  -- typed hypothesis fields (q : ℝ, Z : ℕ, Braid : Type, etc.)
  holds : Prop                 -- the residual claim, still abstract

theorem foo [ctx : FooContext] : ctx.holds := by sorry
```

The `holds : Prop` field is a placeholder — it carries no internal
structure. Refining it requires per-block work to express the
manuscript claim in Lean's type system.

**Options for the next pass**:

1. **(A) Leave `holds : Prop` everywhere; do per-block claim
   refinement chapter-by-chapter** (Descartes → BraidKnot →
   ParticleInteractions → …). Highest fidelity, slowest. ~5-30 min
   per block × 164 = 14-82 hrs.

2. **(B) Bulk-convert to `claim : ⟨lhs⟩ = ⟨rhs⟩`** where the .md
   has an explicit equation, else leave `holds : Prop`. Recognises
   `=`, `↔`, `<`, `≤` in the docstring; extracts the LHS/RHS as
   abstract `R` / `Prop` symbols. Fast but the claims are still
   abstract — only the SHAPE (=/↔) is captured.

3. **(C) Build shared typeclass infrastructure** for common themes
   (Hecke / Markov / Wedderburn / Skein-polynomial / Fluid-dynamics).
   Then refactor blocks to use the shared infra. Slowest setup but
   highest reuse — once `MarkovTraceClaim`, `WedderburnDecomposition`,
   `SkeinResolution` typeclasses are defined, the per-block work
   is "name the witness fields".

## Q2 — Should we merge the `noncomputable instance` sorries with
the new context pattern?

The 27 conjecture-class placeholders use:

```lean
class FooConjecture where
  residual : ℝ
  residual_eq_zero : residual = 0

noncomputable instance : FooConjecture := by sorry
```

The new bulk-shape blocks use:

```lean
class FooContext where ...; holds : Prop
theorem foo [ctx] : ctx.holds := by sorry
```

These are different patterns. Should I:

1. **(A) Leave them distinct** — `class … instance` for conjectures,
   `class … theorem` for provable kinds.

2. **(B) Migrate conjecture classes to the new pattern** so all
   `Prop`-valued claims look uniform. The §3b-cond audit may need
   adjustment.

## Q3 — Heuristic field extraction misses for ~50 narrative blocks

The keyword-inference passes added typed fields for blocks whose
.md mentions `q`, `Z`, `N`, `braid`, `partition`, etc. But some
blocks' .md describes the math without using these tokens — e.g.
"the canonical Möbius integration-limit pencil section becomes
stationary". For these, the typed fields are abstract `Type` rather
than meaningful types.

**Are there shared abstractions you'd like me to centralise**
(e.g., a `QOU.Categorical.MöbiusSection` typeclass) that I'd
re-use across multiple blocks? Or per-block hand-crafted is fine?

## Q4 — Which next chapter to deepen?

Given the typed-field pass is done, picking ONE chapter and hand-
crafting all its blocks (Q1 option A) gives the highest fidelity.
Suggested ordering by manuscript-importance × Lean-ease:

1. **`descartes-universe`** (~20 blocks) — many `Polynomial ℤ` /
   `Matrix ℝ` claims I've already typed in.
2. **`appendix-surreals`** — Mathlib's `Surreal` is well-developed;
   could close several sorries via existing `OrderHom` infra.
3. **`particle-interactions`** — heavy on numerical predictions
   (CODATA + tolerance); good for `norm_num` discharges.
4. **`fluid-dynamics`** — heavy on q-NS analysis; requires
   substantial Mathlib `Sobolev` / `L^p` infra.

## Q5 — `axiom` vs `class+instance` for the §3b conjecture witnesses?

CLAUDE.md §3b prescribes `class C where … ; noncomputable instance
: C := by sorry`. But many of the new conjecture-class fields are
specific equations (`residual = 0`); these could equally be
`axiom C_residual_zero : residual = 0`. The `axiom` form is more
honest about "this is an unproven assumption" but the class form
allows downstream conditional dependence.

**Keep class form or migrate to `axiom` per-claim?**

