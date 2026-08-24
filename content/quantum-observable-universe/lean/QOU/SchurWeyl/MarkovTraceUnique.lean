import QOU.SchurWeyl.HeckeCoset

/-!
# QOU.SchurWeyl.MarkovTraceUnique — a Markov trace is determined by its parameter

`MarkovConventionD` and `MarkovNormalisation` prove that `ocneanuWeight` at convention D satisfies
the two defining properties of a Markov trace weight.  That licenses "**a** Markov trace"; the
definite article needs uniqueness, which is what this file proves:

**any two Markov traces on the Hecke tower with the same `z` agree, on every `H_n(q)`.**

## How

`HeckeCoset.span_cosetFam_eq_top` already supplies the spanning family — `cosetFam (m+1) (b, j) =
ι(cosetFam m b) · r_j` with `r_j = σ_m σ_{m-1} ⋯` — so the whole proof is an induction over it:

* `r_0 = 1`, so the element is `ι(w)` and consistency gives `tr_{m+1}(ι w) = tr_m w`.
* `r_j` for `1 ≤ j ≤ m+1` factors as **the top generator times something from the subalgebra**
  (`descProd_eq_last_mul_incl`).  Cyclicity moves that tail across, and the Markov property
  collapses what is left: `tr(ι w · σ_m · ι t) = tr(ι(t·w) · σ_m) = z · tr_m(t·w)`.

Then `Submodule.span_induction` extends off the family.  The `j ≤ m+1` bound matters: the
factorisation is **false** past it — `descProd 0 2 = σ_0 · σ_0`, and `σ_0 ∉ ι(H_0) = K·1` — but
`cosetIndex` only ever supplies `j : Fin (m+2)`, so the family stays inside the range.

## What this does and does not give

It is a real theorem: the induction uses all four axioms, and dropping any one breaks it.  But it
is a statement **about** `MarkovTraceFamily`, and **no instance is built here** — so it does not,
by itself, identify the weighted seminormal trace with anything.  Doing that needs the seminormal
trace packaged as a `MarkovTraceFamily`, which in turn needs two properties not yet proved for it:

* **cyclicity** `tr(xy) = tr(yx)` — should follow blockwise from `Matrix.trace_mul_comm`;
* **consistency** `tr_{n+1}(ι x) = tr_n x` — the corner decomposition again, this time without the
  `σ` factor, closed by `ocneanuWeight_addable_sum`.

Until that packaging exists, read this as "uniqueness holds, and the identification is one step
away", not as "the Ocneanu weight is *the* Markov trace".  Index conventions will need care in
that step: this file's `tr (n+1)` is the trace on `Hecke K q qi (n+1) = H_{n+2}(q)`, while
`markov_conventionD` is indexed by the diagram size.

## Base ring (§7c)

Generic `[CommRing K]` throughout — no ordering, nothing archimedean, and no `ℝ`.

LaTeX label: `thm:markov-trace-unique`
-/

namespace QOU.SchurWeyl
namespace HeckeCoset

open Hecke HeckeInclusion

variable {K : Type*} [CommRing K] {q qi z : K}

/-- For `1 ≤ j ≤ m+1`, the coset representative `r_j` factors as the top generator times
something from the subalgebra. -/
theorem descProd_eq_last_mul_incl (m : ℕ) :
    ∀ j : ℕ, 1 ≤ j → j ≤ m + 1 →
      ∃ t : Hecke K q qi m, descProd (K := K) (q := q) (qi := qi) m j
        = σ K q qi (m + 1) (Fin.last m) * heckeIncl K q qi m t
  | 0, h, _ => absurd h (by omega)
  | 1, _, _ => ⟨1, by
      rw [descProd_succ, descProd_zero, one_mul, map_one, mul_one]
      congr 1⟩
  | (j + 2), _, hle => by
      obtain ⟨t, ht⟩ := descProd_eq_last_mul_incl m (j + 1) (by omega) (by omega)
      have hlt : m - (j + 1) < m := by omega
      refine ⟨t * σ K q qi m ⟨m - (j + 1), hlt⟩, ?_⟩
      rw [descProd_succ, ht, map_mul, heckeIncl_σ, mul_assoc]
      congr 2


/-- **A Markov trace on the Hecke tower**, with parameter `z`. -/
structure MarkovTraceFamily (K : Type*) [CommRing K] (q qi z : K) where
  tr : (n : ℕ) → Hecke K q qi n →ₗ[K] K
  tr_one : ∀ n, tr n 1 = 1
  tr_cyclic : ∀ n (x y : Hecke K q qi n), tr n (x * y) = tr n (y * x)
  tr_incl : ∀ n (x : Hecke K q qi n), tr (n + 1) (heckeIncl K q qi n x) = tr n x
  tr_markov : ∀ n (x : Hecke K q qi n),
    tr (n + 1) (heckeIncl K q qi n x * σ K q qi (n + 1) (Fin.last n)) = z * tr n x

theorem MarkovTraceFamily.tr_coset (U : MarkovTraceFamily K q qi z) (m : ℕ)
    (w t : Hecke K q qi m) :
    U.tr (m + 1) (heckeIncl K q qi m w
        * (σ K q qi (m + 1) (Fin.last m) * heckeIncl K q qi m t))
      = z * U.tr m (t * w) := by
  rw [← mul_assoc, U.tr_cyclic (m + 1) (heckeIncl K q qi m w * σ K q qi (m + 1) (Fin.last m))
    (heckeIncl K q qi m t), ← mul_assoc, ← map_mul, U.tr_markov]

/-- **Uniqueness of the Markov trace.** -/
theorem markovTrace_unique (T S : MarkovTraceFamily K q qi z) :
    ∀ (n : ℕ) (x : Hecke K q qi n), T.tr n x = S.tr n x := by
  intro n
  induction n with
  | zero =>
      intro x
      have hx : x ∈ Submodule.span K
          (Set.range (cosetFam (K := K) (q := q) (qi := qi) 0)) := by
        rw [span_cosetFam_eq_top]; trivial
      induction hx using Submodule.span_induction with
      | mem y hy =>
          obtain ⟨p, rfl⟩ := hy
          show T.tr 0 1 = S.tr 0 1
          rw [T.tr_one, S.tr_one]
      | zero => simp
      | add a b _ _ ha hb => simp [ha, hb]
      | smul c a _ ha => simp [ha]
  | succ m ih =>
      intro x
      have hx : x ∈ Submodule.span K
          (Set.range (cosetFam (K := K) (q := q) (qi := qi) (m + 1))) := by
        rw [span_cosetFam_eq_top]; trivial
      induction hx using Submodule.span_induction with
      | mem y hy =>
          obtain ⟨p, rfl⟩ := hy
          rw [cosetFam_succ]
          rcases Nat.eq_zero_or_pos (p.2 : ℕ) with h0 | hp
          · rw [h0, descProd_zero, mul_one, T.tr_incl, S.tr_incl, ih]
          · obtain ⟨t, ht⟩ := descProd_eq_last_mul_incl (K := K) (q := q) (qi := qi) m
              (p.2 : ℕ) hp (by have := p.2.isLt; omega)
            rw [ht, T.tr_coset, S.tr_coset, ih]
      | zero => simp
      | add a b _ _ ha hb => simp [ha, hb]
      | smul c a _ ha => simp [ha]

end HeckeCoset
end QOU.SchurWeyl
