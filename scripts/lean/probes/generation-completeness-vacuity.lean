/-!
# Probe: does `generation_completeness` constrain any knot?

**Result: no.** `isReachable` is true of every `KnotType`, the genus
hypothesis is never used, and the corollary's first conjunct is its own
hypothesis restated.

`content/quantum-observable-universe/brings-surface/generation-completeness.lean`
is two theorems over two definitions:

```lean
def isEmbeddable (K : KnotType) : Prop := K.seifertGenus ≤ genusBound   -- 4
def isReachable  (K : KnotType) : Prop := ∃ r : ℕ, r ≤ K.unknottingNumber

theorem generation_completeness (K : KnotType) (h_embed : isEmbeddable K) :
    isReachable K := ⟨K.unknottingNumber, le_refl _⟩

theorem spectrum_complete (K : KnotType) (h : K.seifertGenus ≤ 4) :
    isEmbeddable K ∧ isReachable K := ⟨h, generation_completeness K h⟩
```

`∃ r : ℕ, r ≤ K.unknottingNumber` is inhabited by `r = 0` for **any** `K`, so
it says nothing about knots, generators, or Skein moves. `KnotType` is two
naturals with no knot in it. The docstring meanwhile claims:

> *"Let K be any knot with Seifert genus g(K) ≤ 4. Then K is reachable from
>  the generator set G by a finite sequence of Skein crossing changes."*

and the corollary claims *"The Descartes particle spectrum is complete over
embeddable knots."*

Lean's own linter already says half of this: compiling the file emits
`warning: unused variable 'h_embed'`.

To run (needs Mathlib oleans; `import Mathlib.Data.Nat.Basic` only, so this is
cheap):

    cp content/quantum-observable-universe/brings-surface/generation-completeness.lean /tmp/p.lean
    sed -n '/^-- ==== PROBE/,$p' scripts/lean/probes/generation-completeness-vacuity.lean >> /tmp/p.lean
    LP=""; for d in .lake/packages/*/.lake/build/lib/lean; do LP="$LP$PWD/$d:"; done
    LEAN_PATH="$LP" lean /tmp/p.lean          # exit 0 = every claim below holds

Verified exit 0 on lean-v4.24.0, 2026-08-30. Bean qou-0avp.
-/

-- ==== PROBE BODY (appended to the source file by the recipe above) ====
namespace QOU.Archimedean

-- `isReachable` holds for EVERY KnotType: the genus hypothesis is not needed.
theorem probe_reachable_is_unconditional (K : KnotType) : isReachable K :=
  ⟨0, Nat.zero_le _⟩

-- Including ones with no relation to any knot.
theorem probe_reachable_junk : isReachable ⟨999, 0⟩ := ⟨0, Nat.zero_le _⟩

-- So the genus bound is inert: it holds with the hypothesis NEGATED.
theorem probe_reachable_even_when_not_embeddable
    (K : KnotType) (_h : ¬ isEmbeddable K) : isReachable K :=
  ⟨0, Nat.zero_le _⟩

-- And `spectrum_complete`'s first conjunct is its own hypothesis restated.
theorem probe_spectrum_first_conjunct_is_the_hypothesis
    (K : KnotType) (h : K.seifertGenus ≤ 4) : isEmbeddable K := h

end QOU.Archimedean
