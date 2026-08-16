/-
Copyright (c) 2026 QOU contributors. All rights reserved.
-/
import Mathlib.GroupTheory.Perm.Basic
import Mathlib.Tactic

/-!
# Per-strand twists are per-component framings, and that constrains the multiset

Bean `qou-kebu` (T2b). Companion to
[`TwistSeparationContent.lean`](TwistSeparationContent.lean).

## Why the bean's proposed route cannot work as written

`qou-kebu` proposes deriving the per-strand twist multisets from the ribbon
structure:

> 1. The twist `θ_V = q^{c_V}` acts on each strand by the Casimir
> 2. For `T(2,p) = σ₁^p`, the total twist is `p·θ_V`
> 3. The per-strand multiset is determined by the braid monodromy

Step 1 cannot deliver step 3. The corpus's own probe states the reason:
*"On a simple object of a ribbon category the twist `theta` acts by a **scalar**;
for Hecke / quantum-`sl_N` the exponent is the **content sum** of the
partition"* (`ribbon_twist_charge_quantum_probe.py:13-17`). A scalar attached to
an object is one number. The battery's answers are **non-constant** multisets —
`u = {0,1,1}`, `d = {-1,-1,1}` — and no scalar produces a non-constant
multiset over identical strands. That probe tested `Q = c(λ)/3` directly and it
failed; this is the structural reason it had to.

`θ` is the *weight per unit framing* (`q^{c_V t_i}`), not the framing `t_i`.
Deriving the multiset needs something that fixes the **integers**, and `θ` is
not it.

## What does fix them: the closure map

The mechanism the bean's step 3 gestures at is real, but it is the
**permutation**, not the twist. In a framed link the framing is one integer
**per component**, not per strand. Closing a braid `β ∈ B_n` joins strand `i` to
strand `π(β)(i)`, so the strands in one cycle of `π(β)` become **one component**
— and a framing that is well defined on the link must take the same value on all
of them.

That is `IsComponentFraming` below: `t ∘ π = t`. It is not an extra assumption
about ribbons; it is what "the framing of a framed link" means, transported to
strand indices.

## The falsifiable content

Component-constancy forces the multiset's *shape* to be built from cycle
lengths, which turns each battery answer into a statement about the fermion's
braid word:

* `constant_of_transitive` — if `π` is transitive (a single `n`-cycle, i.e. the
  closure is a **knot**), the framing is constant, so the multiset is `{a,…,a}`.
* `eq_one_of_injective` — if the multiset has all entries **distinct**, then
  `π = 1`: the closure is a totally split `n`-component link.

Applied to the four battery survivors (`strand-twist-y-battery.witness.json`):

| fermion | multiset | forced |
|---|---|---|
| `u` | `{0,1,1}` | `π` is **not** transitive — `u`'s closure is not a knot |
| `d` | `{-1,-1,1}`, `{-1,0,0}` | same |
| `ν` | `{-1,0,1}` | `π = 1` — totally split |
| `ν` | `{0,0,0}` | unconstrained |
| `e` | `{-1,-1,-1}` | unconstrained (constant fits any `π`) |

These are **predictions about the braid words**, checkable the moment those
words exist. They are also the first constraints in this arc that are derived
rather than enumerated: the battery searched 10 000 assignments and reported
which survive; this says which are *possible* given a braid, before any search.

## Scope

Scope-(a) on the route, scope-(b) on the one step that a proved invariant
excludes. Excluded, by the scalar/multiset mismatch above: `θ` alone determining
a non-constant per-strand multiset. **Not** excluded: the twist entering as the
weight `q^{c_V t_i}` (its actual role), the hypercharge programme, or `qou-kebu`
itself — this reformulates its step 3 rather than closing it.

The blocking input is unchanged and is recorded in the battery's own witness:
the corpus carries **no per-chiral-fermion framed braid words** (`htw2`). Until
those exist the table above cannot be evaluated — which is precisely why it is
worth stating now, as the test those words will face.
-/

namespace QOU.StandardModel.ComponentFraming

variable {n : ℕ}

/-- A **component framing**: a per-strand integer that is constant along the
closure, i.e. invariant under the braid's underlying permutation.

Strands `i` and `π i` are joined by the closure, so they lie on one component of
the resulting link; a framing of that link assigns them the same integer. -/
def IsComponentFraming (π : Equiv.Perm (Fin n)) (t : Fin n → ℤ) : Prop :=
  ∀ i, t (π i) = t i

/-- Invariance under `π` propagates to every power of `π`. -/
theorem invariant_pow {π : Equiv.Perm (Fin n)} {t : Fin n → ℤ}
    (h : IsComponentFraming π t) : ∀ (k : ℕ) (i : Fin n), t ((π ^ k) i) = t i := by
  intro k
  induction k with
  | zero => intro i; simp
  | succ m ih =>
      intro i
      have hstep : (π ^ (m + 1)) i = (π ^ m) (π i) := by
        rw [pow_succ, Equiv.Perm.mul_apply]
      rw [hstep, ih (π i), h i]

/-- **A knot closure forces a constant framing.**

If `π` is transitive — every strand reachable from every other, i.e. the closure
has a single component — then a component framing takes one value throughout, so
its multiset is `{a, …, a}`.

Contrapositive, which is the usable form: a **non-constant** multiset proves the
closure is *not* a knot. -/
theorem constant_of_transitive {π : Equiv.Perm (Fin n)} {t : Fin n → ℤ}
    (h : IsComponentFraming π t)
    (htrans : ∀ i j : Fin n, ∃ k : ℕ, (π ^ k) i = j) :
    ∀ i j : Fin n, t i = t j := by
  intro i j
  obtain ⟨k, hk⟩ := htrans i j
  calc t i = t ((π ^ k) i) := (invariant_pow h k i).symm
    _ = t j := by rw [hk]

/-- **All-distinct twists force a totally split closure.**

If the framing is injective — the entries of the multiset are pairwise distinct —
then `π` is the identity, so the closure is an `n`-component split link. -/
theorem eq_one_of_injective {π : Equiv.Perm (Fin n)} {t : Fin n → ℤ}
    (h : IsComponentFraming π t) (hinj : Function.Injective t) :
    π = 1 :=
  Equiv.ext fun i => by simpa using hinj (h i)

/-! ### The two battery answers that carry force

Stated over `Fin 3`, the strand count the battery uses
(`strands_per_fermion: 3`). -/

/-- `u = {0, 1, 1}` is not constant, so `u`'s braid closure is **not a knot**.

Here the framing is exhibited concretely: strand 0 carries twist `0`, strands 1
and 2 carry `1`. -/
theorem u_multiset_forces_nontransitive
    {π : Equiv.Perm (Fin 3)} {t : Fin 3 → ℤ}
    (h : IsComponentFraming π t)
    (h0 : t 0 = 0) (h1 : t 1 = 1) :
    ¬ (∀ i j : Fin 3, ∃ k : ℕ, (π ^ k) i = j) := by
  intro htrans
  have := constant_of_transitive h htrans 0 1
  rw [h0, h1] at this
  exact absurd this (by decide)

/-- `ν = {-1, 0, 1}` has pairwise-distinct entries, so `π = 1`: the closure is a
three-component split link. -/
theorem nu_multiset_forces_trivial_perm
    {π : Equiv.Perm (Fin 3)} {t : Fin 3 → ℤ}
    (h : IsComponentFraming π t) (hinj : Function.Injective t) :
    π = 1 :=
  eq_one_of_injective h hinj

end QOU.StandardModel.ComponentFraming
