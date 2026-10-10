import QOU.SchurWeyl.MarkovTraceUnique

/-!
# QOU.SchurWeyl.SymmetrisingTraceZeroParam — a Markov trace with `z = 0` is the symmetrising trace

The **symmetrising (regular) trace** on the Iwahori–Hecke algebra is the functional
`τ(T_w) = δ_{w,1}`: it takes the value `1` on the identity and `0` on every other element of the
standard basis.  This file proves that **a Markov trace with parameter `z = 0` is exactly that
functional**, on every `H_n(q)` of the tower.

## The basis used

`Hecke K q qi n` is presented as a quotient of the free algebra, so it carries no built-in `T_w`
basis.  The basis used is the coset family of `HeckeCoset`:

```
cosetFam 0 () = 1,      cosetFam (m+1) (b, j) = ι(cosetFam m b) · r_j,
r_j = σ_m σ_{m−1} ⋯ σ_{m−j+1}   (r_0 = 1),
```

which spans (`HeckeCoset.span_cosetFam_eq_top`) and has `(m+1)! = |S_{m+1}|` elements
(`HeckeCoset.card_cosetIndex`).  Each element is a product of distinguished coset representatives
`r_j`, i.e. the `T_w` for the permutation `w` read off from the factorisation, of length
`cosetLen p = Σ j`.  The identity is the unique index of length `0`.

## The statement

`MarkovTraceFamily.tr_cosetFam_of_zero`: if `T` is a Markov trace with `z = 0`, then

```
T.tr m (cosetFam m p) = if cosetLen p = 0 then 1 else 0.
```

Combined with `HeckeCoset.markovTrace_unique` (a Markov trace is determined by its parameter),
this says: **every `z = 0` Markov trace is the symmetrising trace**, and there is at most one.

## Proof

Induction on `m`, exactly the shape of `markovTrace_unique`.  For `p = (b, j)`:

* `j = 0`: `r_0 = 1`, so `tr(ι(cosetFam b)) = tr(cosetFam b)` by consistency, and
  `cosetLen (b, 0) = cosetLen b`.
* `j ≥ 1`: `r_j = σ_m · ι(t)` (`descProd_eq_last_mul_incl`), so cyclicity and the Markov axiom give
  `tr = z · tr(t · cosetFam b) = 0`; and `cosetLen (b, j) ≥ j ≥ 1`.

## Base ring (§7c)

Generic `[CommRing K]`; nothing archimedean.

LaTeX label: `thm:symmetrising-trace-zero-param`
-/

namespace QOU.SchurWeyl
namespace HeckeCoset

open Hecke HeckeInclusion

variable {K : Type*} [CommRing K] {q qi : K}

/-- The **length** of a coset-family index: the total number of generators in
`cosetFam m p = ι(⋯ι(r_{j₁})⋯) · r_{j_m}`, i.e. `Σ jₖ`. -/
def cosetLen : (m : ℕ) → cosetIndex m → ℕ
  | 0, _ => 0
  | (m + 1), p => cosetLen m p.1 + p.2.val

@[simp] theorem cosetLen_zero (p : cosetIndex 0) : cosetLen 0 p = 0 := rfl

theorem cosetLen_succ (m : ℕ) (p : cosetIndex (m + 1)) :
    cosetLen (m + 1) p = cosetLen m p.1 + p.2.val := rfl

/-- **A Markov trace with `z = 0` is the symmetrising trace.**  On the coset basis it is `1` at the
identity (the unique index of length `0`) and `0` everywhere else. -/
theorem MarkovTraceFamily.tr_cosetFam_of_zero (T : MarkovTraceFamily K q qi 0) :
    ∀ (m : ℕ) (p : cosetIndex m),
      T.tr m (cosetFam (K := K) (q := q) (qi := qi) m p)
        = if cosetLen m p = 0 then 1 else 0
  | 0, _ => by
      show T.tr 0 1 = _
      rw [T.tr_one, cosetLen_zero, if_pos rfl]
  | (m + 1), p => by
      rw [cosetFam_succ, cosetLen_succ]
      rcases Nat.eq_zero_or_pos (p.2 : ℕ) with h0 | hp
      · rw [h0, descProd_zero, mul_one, T.tr_incl, add_zero]
        exact MarkovTraceFamily.tr_cosetFam_of_zero T m p.1
      · obtain ⟨t, ht⟩ := descProd_eq_last_mul_incl (K := K) (q := q) (qi := qi) m
          (p.2 : ℕ) hp (by have := p.2.isLt; omega)
        rw [ht, T.tr_coset, zero_mul, if_neg (by omega)]

/-- The identity index (all `jₖ = 0`). -/
def cosetOne : (m : ℕ) → cosetIndex m
  | 0 => ()
  | (m + 1) => (cosetOne m, 0)

theorem cosetLen_eq_zero_iff : ∀ (m : ℕ) (p : cosetIndex m), cosetLen m p = 0 ↔ p = cosetOne m
  | 0, p => by simp only [cosetLen_zero, true_iff]; rfl
  | (m + 1), (b, j) => by
      show cosetLen m b + j.val = 0 ↔ (b, j) = (cosetOne m, (0 : Fin (m + 2)))
      rw [Prod.mk.injEq, ← cosetLen_eq_zero_iff m b, Fin.ext_iff, Fin.val_zero]
      omega

/-- `cosetFam` at the identity index is `1`. -/
theorem cosetFam_cosetOne : ∀ m : ℕ,
    cosetFam (K := K) (q := q) (qi := qi) m (cosetOne m) = 1
  | 0 => rfl
  | (m + 1) => by
      show heckeIncl K q qi m (cosetFam m (cosetOne m)) * descProd m 0 = 1
      rw [cosetFam_cosetOne m, map_one, descProd_zero, mul_one]

/-- **The symmetrising-trace form**: a `z = 0` Markov trace is `δ` on the coset basis — `1` at the
identity index and `0` at every other one. -/
theorem MarkovTraceFamily.tr_cosetFam_eq_delta (T : MarkovTraceFamily K q qi 0) (m : ℕ)
    (p : cosetIndex m) :
    (p = cosetOne m → T.tr m (cosetFam (K := K) (q := q) (qi := qi) m p) = 1) ∧
      (p ≠ cosetOne m → T.tr m (cosetFam (K := K) (q := q) (qi := qi) m p) = 0) := by
  rw [T.tr_cosetFam_of_zero m p]
  exact ⟨fun h => if_pos ((cosetLen_eq_zero_iff m p).mpr h),
    fun h => if_neg fun h' => h ((cosetLen_eq_zero_iff m p).mp h')⟩

/-- **The Markov parameter is zero iff the trace vanishes on `σ₀`** — so a Markov trace is the
symmetrising trace exactly when `tr₁(σ₀) = 0`.  (Forward direction is `param_eq`; this records it
in the form used to read `z = 0` off a trace.) -/
theorem MarkovTraceFamily.param_eq_zero_iff {z : K} (T : MarkovTraceFamily K q qi z) :
    z = 0 ↔ T.tr 1 (σ K q qi 1 (Fin.last 0)) = 0 := by
  rw [T.param_eq]

end HeckeCoset
end QOU.SchurWeyl
