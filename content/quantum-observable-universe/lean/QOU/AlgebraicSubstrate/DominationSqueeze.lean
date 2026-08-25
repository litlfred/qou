import Mathlib.Order.WithBot
import Mathlib.Algebra.Order.Group.Defs
import Mathlib.Data.Real.Basic

/-!
# QOU.AlgebraicSubstrate.DominationSqueeze — the squeeze as an algebraic object

**The move.** Every surreal bound in `appendix-surreals` — RH, BSD, q-Collatz,
P-vs-NP, q-NS blowup — runs one shared step: put a *cost* and a *budget* at
different `ordω` grades and read off `cost > budget`. That step is stated in an
**ordered field** (`ℝ(ε) ⊂ No`), which is exactly why
[`QOU.Archimedean.SurrealGradingPrune`](../Archimedean/SurrealGradingPrune.lean)
can prove it blind to anything happening inside `ℝ`.

This file replaces it with its algebraic content. The step is **not** an order
fact. It is the strict-triangle equality of a valuation:

> if `val a < val b` then `val (a + b) = val a` — a strictly dominant term
> survives, and the sub-dominant one cannot cancel it.

Everything the squeeze is used for follows from that, and it needs **no ordered
field, no `ℝ`, no surreals, no transfer principle** — only an abelian group with
a filtration. So the argument moves to the *substrate* side of the archimedean
wall, where the framework's GB / jet filtration already lives.

## What this buys

| Ordered-field form | Algebraic form |
|---|---|
| `ordω(A) > ordω(B) ⟹ A > B` | `val A < val B ⟹ val (A + B) = val A` |
| needs an ordered field | needs an abelian group + filtration |
| lives past the substrate wall | lives on the substrate side |
| **blind on `ℝ`** (`SurrealGradingPrune`) | informative on any graded object |
| `lem:surreal-squeeze`'s Lean is a tautology | `add_ne_zero_of_val_lt` is a theorem |

**Sign convention.** `val` is a *valuation*: **smaller means more dominant**
(order of vanishing), with `val 0 = ⊤`. The corpus's `ordω` runs the other way
(`ordω(ε⁻¹) = 1 > −3 = ordω(ε³)`), so `ordω = −val`. A squeeze written
`ordω(cost) > ordω(budget)` reads here as `val cost < val budget`.

## Where it instantiates

* `jetDomination` below — the jet / GB filtration on coefficient sequences,
  i.e. order of vanishing at `q = 1`. This is the grading
  `QOU.Archimedean.TowerHeightAttack §3` requires and the bare
  `VolumeTowerDecomposition` (a plain `HasSum`) does not supply.
* Any `ℕ`-filtered ring, via `val x = sup {n | x ∈ Fⁿ}`.
* The Ohtsuki tower `𝔙_b = 𝔙₀ + Σ κₙ (2πb²)ⁿ` — `val` = leading `ℏ`-order.

## Scope

This makes the *inference step* of the surreal bounds rigorous and reusable. It
establishes **none of their premises** — the Reeb-period budget accounting, the
non-compressibility conjecture, the `std`-of-the-skein assumption are untouched,
and no millennium bound becomes a proof of anything because of this file.
-/

namespace QOU.AlgebraicSubstrate

variable {A : Type*} [AddCommGroup A] {Γ : Type*} [LinearOrder Γ]

/-- **Domination structure** — a filtration / valuation on an abelian group,
carrying exactly the data the squeeze arguments use and nothing else.

`val a` is the grade / filtration depth / order of vanishing of `a`, with `⊤`
for `0`. The only axiom is the ultrametric bound; strict domination is
**derived** (`val_add_eq_of_lt`), not assumed. -/
structure Domination (A : Type*) [AddCommGroup A] (Γ : Type*) [LinearOrder Γ] where
  /-- Grade / filtration depth. Smaller = more dominant. -/
  val : A → WithTop Γ
  /-- Zero is infinitely deep. -/
  val_zero : val 0 = ⊤
  /-- Negation preserves depth. -/
  val_neg : ∀ a, val (-a) = val a
  /-- Ultrametric bound: a sum is at least as deep as its shallowest summand. -/
  le_val_add : ∀ a b, min (val a) (val b) ≤ val (a + b)

namespace Domination

variable (D : Domination A Γ)

/-- **Strict domination (the core).** A strictly dominant term determines the
grade of the sum — the ultrametric strict-triangle *equality*.

This is the algebraic content of `lem:surreal-squeeze`. Note what is absent: no
order on `A`, no field, no archimedean structure. -/
theorem val_add_eq_of_lt {a b : A} (h : D.val a < D.val b) :
    D.val (a + b) = D.val a := by
  refine le_antisymm ?_ (by simpa [min_eq_left h.le] using D.le_val_add a b)
  by_contra hlt
  push_neg at hlt
  have hback : min (D.val (a + b)) (D.val (-b)) ≤ D.val ((a + b) + -b) := D.le_val_add _ _
  rw [D.val_neg b, show (a + b) + -b = a by simp] at hback
  exact absurd hback (not_le.mpr (lt_min hlt h))

/-- **The squeeze, algebraically: a dominant term cannot be cancelled.**

`val cost < val budget ⟹ cost + budget ≠ 0`. This is what every surreal bound
in the appendix actually needs — *"the budget cannot absorb the cost"* — and
here it is a theorem about a filtered abelian group, not an inequality in an
ordered field. -/
theorem add_ne_zero_of_val_lt {a b : A} (h : D.val a < D.val b) : a + b ≠ 0 := by
  intro hab
  have h1 : D.val (a + b) = D.val a := D.val_add_eq_of_lt h
  rw [hab, D.val_zero] at h1
  rw [← h1] at h
  exact absurd h (by simp)

/-- Sub-dominant corrections cannot make two elements equal. -/
theorem ne_of_val_lt {a b : A} (h : D.val a < D.val b) : a ≠ b := by
  rintro rfl
  exact lt_irrefl _ h

/-- Two terms strictly below a common bound stay strictly below it when added.
Stated against an arbitrary grade `g`, which is what the tower arguments need
(the bound is a grade, not always the value of some element). -/
theorem lt_val_add' {g : WithTop Γ} {b c : A} (hb : g < D.val b) (hc : g < D.val c) :
    g < D.val (b + c) :=
  lt_of_lt_of_le (lt_min hb hc) (D.le_val_add b c)

/-- Two strictly deeper terms stay strictly deeper when added. -/
theorem lt_val_add {a b c : A} (hb : D.val a < D.val b) (hc : D.val a < D.val c) :
    D.val a < D.val (b + c) :=
  D.lt_val_add' hb hc

/-- A finite collection of terms strictly deeper than the **grade** `γ` sums to
something strictly deeper than `γ`.

Stated against a grade rather than an element: that makes the empty-list case
free (`val 0 = ⊤ > γ`) and is the form the tower arguments need. -/
theorem lt_val_sum_grade {γ : Γ} (s : List A)
    (h : ∀ b ∈ s, (γ : WithTop Γ) < D.val b) : (γ : WithTop Γ) < D.val s.sum := by
  induction s with
  | nil => simp [D.val_zero]
  | cons c t ih =>
      rw [List.sum_cons]
      exact D.lt_val_add' (h c (List.mem_cons_self ..))
        (ih fun b hb => h b (List.mem_cons_of_mem _ hb))

/-- A finite collection of strictly deeper terms sums to something strictly
deeper. (`ha` rules out `a = 0`, for which the empty sum is a counterexample.) -/
theorem lt_val_sum {a : A} (ha : D.val a < ⊤) (s : List A)
    (h : ∀ b ∈ s, D.val a < D.val b) : D.val a < D.val s.sum := by
  induction s with
  | nil => simpa [D.val_zero] using ha
  | cons c t ih =>
      rw [List.sum_cons]
      exact D.lt_val_add (h c (List.mem_cons_self ..))
        (ih fun b hb => h b (List.mem_cons_of_mem _ hb))

/-- **Iterated domination — the tower form.** A leading level survives the whole
tail, provided every tail term is strictly deeper. This is the shape the tower
arguments need: one dominant level against infinitely many corrections
(here, any finite truncation of them). -/
theorem val_add_sum_eq {a : A} (ha : D.val a < ⊤) (s : List A)
    (h : ∀ b ∈ s, D.val a < D.val b) : D.val (a + s.sum) = D.val a :=
  D.val_add_eq_of_lt (D.lt_val_sum ha s h)

/-- **The tower does not collapse.** A dominant leading term plus strictly
deeper corrections is non-zero — the algebraic form of "the obstruction
survives to this level". -/
theorem add_sum_ne_zero {a : A} (ha : D.val a < ⊤) (s : List A)
    (h : ∀ b ∈ s, D.val a < D.val b) : a + s.sum ≠ 0 :=
  D.add_ne_zero_of_val_lt (D.lt_val_sum ha s h)

end Domination

/-! ## §2  The jet / GB filtration as a `Domination`

Order of vanishing of a coefficient sequence at `q = 1` — the grading
`TowerHeightAttack §3` needs and `VolumeTowerDecomposition` lacks. -/

open Classical

/-- Order of vanishing: least index with a non-zero coefficient, `⊤` for the
zero sequence. -/
noncomputable def jetVal (f : ℕ → ℝ) : WithTop ℕ :=
  if h : ∃ n, f n ≠ 0 then ((Nat.find h : ℕ) : WithTop ℕ) else ⊤

theorem jetVal_eq_top_iff {f : ℕ → ℝ} : jetVal f = ⊤ ↔ ∀ n, f n = 0 := by
  rw [jetVal]
  split_ifs with h
  · exact ⟨fun htop => absurd htop (by simp),
           fun hall => absurd (Nat.find_spec h) (by simp [hall])⟩
  · push_neg at h; simp [h]

theorem eq_zero_of_lt_jetVal {f : ℕ → ℝ} {n : ℕ} (h : (n : WithTop ℕ) < jetVal f) :
    f n = 0 := by
  by_contra hn
  have hex : ∃ m, f m ≠ 0 := ⟨n, hn⟩
  rw [jetVal, dif_pos hex] at h
  exact absurd hn (Nat.find_min hex (WithTop.coe_lt_coe.mp h))

theorem ne_zero_of_jetVal_eq {f : ℕ → ℝ} {m : ℕ} (h : jetVal f = (m : WithTop ℕ)) :
    f m ≠ 0 := by
  rw [jetVal] at h
  split_ifs at h with hex
  · have hm : Nat.find hex = m := by exact_mod_cast h
    exact hm ▸ Nat.find_spec hex
  · exact absurd h (by simp)

theorem jetVal_congr {f g : ℕ → ℝ} (h : ∀ n, f n ≠ 0 ↔ g n ≠ 0) :
    jetVal f = jetVal g := by
  unfold jetVal
  split_ifs with h1 h2 h2
  · have : Nat.find h1 = Nat.find h2 :=
      le_antisymm (Nat.find_le ((h _).mpr (Nat.find_spec h2)))
                  (Nat.find_le ((h _).mp (Nat.find_spec h1)))
    rw [this]
  · exact absurd (h1.imp fun n hn => (h n).mp hn) h2
  · exact absurd (h2.imp fun n hn => (h n).mpr hn) h1
  · rfl

/-- **The jet filtration is a domination structure.** Concrete witness that
`Domination` is non-vacuous, on exactly the grading the tower argument needs. -/
noncomputable def jetDomination : Domination (ℕ → ℝ) ℕ where
  val := jetVal
  val_zero := jetVal_eq_top_iff.mpr fun _ => rfl
  val_neg a := jetVal_congr fun n => by simp
  le_val_add a b := by
    by_contra hlt
    push_neg at hlt
    have hne : jetVal (a + b) ≠ ⊤ := fun htop => by
      rw [htop] at hlt; exact absurd hlt (by simp)
    obtain ⟨m, hm⟩ := WithTop.ne_top_iff_exists.mp hne
    have hm' : jetVal (a + b) = (m : WithTop ℕ) := by exact_mod_cast hm.symm
    rw [hm'] at hlt
    have h2 := lt_min_iff.mp hlt
    exact ne_zero_of_jetVal_eq hm'
      (by simp [eq_zero_of_lt_jetVal h2.1, eq_zero_of_lt_jetVal h2.2])

/-! ## §3  Bridge back to the ordered-field form

The algebraic core *implies* the ordered-field squeeze whenever the domination
is order-compatible, so nothing is lost by working algebraically. And
`SurrealGradingPrune` says the converse direction is where the information was
never there: on `ℝ` the grading is constant, so the ordered-field form has no
premise to fire on. Together: **use the algebraic form; the ordered-field form
is the special case that happens to be blind.** -/

/-- Order-compatibility: a strictly dominant term is strictly larger. This is
the *extra* hypothesis the ordered-field reading needs, and the one that has no
content on `ℝ`. -/
structure OrderedDomination (A : Type*) [AddCommGroup A] [LinearOrder A]
    (Γ : Type*) [LinearOrder Γ] extends Domination A Γ where
  /-- Strictly dominant (smaller `val`) and positive ⟹ strictly larger. -/
  lt_of_val_lt : ∀ {a b : A}, 0 < a → 0 < b → val a < val b → b < a

/-- **The ordered-field squeeze, recovered.** `ordω(cost) > ordω(budget)` —
i.e. `val cost < val budget` — gives `budget < cost`, which is exactly what
`rem:collatz-surreal-bound`, `rem:p-vs-np-surreal-bound` and
`rem:ns-surreal-bound` invoke. Nothing is lost by taking the algebraic core as
primitive. -/
theorem OrderedDomination.squeeze {A : Type*} [AddCommGroup A] [LinearOrder A]
    (D : OrderedDomination A Γ) {cost budget : A}
    (hc : 0 < cost) (hb : 0 < budget) (h : D.val cost < D.val budget) :
    budget < cost :=
  D.lt_of_val_lt hc hb h

end QOU.AlgebraicSubstrate
