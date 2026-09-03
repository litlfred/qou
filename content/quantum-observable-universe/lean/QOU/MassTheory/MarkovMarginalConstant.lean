/-
# QOU.MassTheory.MarkovMarginalConstant

Bean `qou-6tcn`.  The invariant behind
`computations/meson/cut_entropy_is_A_independent_probe.py`: a **Markov tower**
has an `n`-independent fixed-width marginal, so any functional of that marginal
— an entanglement entropy across a fixed-width cut included — is constant in
`n`, and therefore cannot equal an extensive quantity.

`prop:markov-trace-frobenius-selection` defines a Markov trace as *"a compatible
family of linear functionals `τ_n : H_n(R,q) → R`"*.  Compatibility is a
**one-step** condition: restricting level `n+1` gives level `n`.  What is proved
here is that the one-step condition forces the **any-depth** conclusion — the
marginal taken from level `n + d` equals `w n` for every `d`.  That is the
content; the hypothesis is not the conclusion restated (cf. AGENTS.md §3b-cond
item 5, the self-assuming-projection rule), and §"Non-vacuity" below exhibits a
family where dropping the hypothesis breaks the conclusion.

Measured instance: for the convention-D Markov weights
`y_{(n-k,k)} = [n-2k+1]_q / [2]_q^n`, the three-strand marginal of the
`n`-strand measure is `A_(3) = [4]_q/[2]_q^3`, `A_(2,1) = [2]_q/[2]_q^3` for
every `n` — i.e. the three-strand measure itself, to better than `1e-50` out to
`n = 24`.  Consequently `E₀ · S_cut = 4.33633 MeV` at every `A`, while `B_AME`
rises `17.6×` from `²H` to `⁷Li`.  That is a **scope-(b)** exclusion: the
invariant is named, definitional, and not fitted.

**Base ring (AGENTS.md §7c).** Everything is stated over a bare `{R : Type u}`
with **no** typeclass — the argument is pure rewriting and needs no ring, order
or archimedean structure.  There is no `ℝ` anywhere.

**Imports: none.**  The file checks against core Lean alone, so `Nat` is
spelled `Nat` rather than `ℕ` (that notation arrives with Mathlib).
`autoImplicit` is switched **off**: with it on and no imports, an unbound `ℕ`
is silently auto-bound as a fresh type variable and every numeral in the file
then fails to elaborate — which is exactly how this file first failed.
-/

set_option autoImplicit false

namespace QOU.MassTheory

universe u v w

variable {R : Type u} {ι : Type v}

/-- The marginal of the level-`(n + d)` weights, restricted down `d` steps to
level `n`.  Stated for a bare `restrict`/`w` pair rather than as a field of a
structure, so that §"Non-vacuity" can instantiate it with a pair that does *not*
satisfy the step condition. -/
def margDown (restrict : Nat → (ι → R) → (ι → R)) (w : Nat → ι → R) :
    Nat → Nat → (ι → R)
  | n, 0 => w n
  | n, d + 1 => restrict n (margDown restrict w (n + 1) d)

/-- **The invariant.**  One-step compatibility forces depth-independence: the
marginal taken from level `n + d` is `w n`, for every depth `d`.

This is the Markov property doing the work.  The hypothesis constrains a single
step; the conclusion is about all of them. -/
theorem margDown_eq_of_step
    {restrict : Nat → (ι → R) → (ι → R)} {w : Nat → ι → R}
    (h : ∀ n, restrict n (w (n + 1)) = w n) :
    ∀ n d, margDown restrict w n d = w n := by
  intro n d
  induction d generalizing n with
  | zero => rfl
  | succ d ih => rw [margDown, ih (n + 1), h n]

/-- **Any functional of the marginal is depth-independent.**  In the application
`F` is the von Neumann entropy of the reduced state on a fixed-width cut; the
proof does not care what it is. -/
theorem marginal_functional_const
    {restrict : Nat → (ι → R) → (ι → R)} {w : Nat → ι → R} {β : Type w}
    (h : ∀ n, restrict n (w (n + 1)) = w n) (F : (ι → R) → β) (n : Nat) :
    ∀ d e, F (margDown restrict w n d) = F (margDown restrict w n e) := by
  intro d e
  rw [margDown_eq_of_step h n d, margDown_eq_of_step h n e]

/-- **A constant cannot match a target that takes two values.**

Stated as a refutation of pointwise agreement rather than as `∃ c, f c ≠ g c`:
the negation is constructive, needing no classical step. -/
theorem not_forall_eq_of_const_of_two_values {α : Type u} {β : Type w}
    (f g : α → β) (hf : ∀ a b, f a = f b) {a b : α} (hg : g a ≠ g b) :
    ¬ ∀ c, f c = g c := fun hc =>
  hg ((hc a).symm.trans ((hf a b).trans (hc b)))

/-- **The exclusion, assembled.**  If the marginal is Markov-compatible and the
target takes two different values, no depth reproduces the target everywhere.

Applied: `F ∘ margDown` is `E₀ · S_cut`, constant in `A`; `g` is `B_AME`, which
differs between `²H` and `⁷Li`. -/
theorem marginal_functional_ne_two_valued
    {restrict : Nat → (ι → R) → (ι → R)} {w : Nat → ι → R} {β : Type w}
    (h : ∀ n, restrict n (w (n + 1)) = w n) (F : (ι → R) → β) (n : Nat)
    (g : Nat → β) {a b : Nat} (hg : g a ≠ g b) :
    ¬ ∀ d, F (margDown restrict w n d) = g d :=
  not_forall_eq_of_const_of_two_values _ g
    (marginal_functional_const h F n) hg

/-! ## Non-vacuity

Two guards, both required by AGENTS.md §3b-tax: the hypothesis must be
satisfiable, and it must be load-bearing. -/

/-- The hypothesis is satisfiable: a constant tower is Markov-compatible. -/
theorem step_satisfiable (c : ι → R) :
    ∀ n, (fun (_ : Nat) (f : ι → R) => f) n ((fun _ => c) (n + 1))
        = (fun _ => c) n :=
  fun _ => rfl

/-- **The hypothesis is load-bearing.**  Drop it and the conclusion fails: with
`restrict` the identity and `w n = fun _ => n`, the depth-1 marginal at level
`0` is `1`, not `w 0 = 0`.  So `margDown_eq_of_step` is not a tautology about
`margDown`, and the step condition is doing real work. -/
theorem margDown_ne_without_step :
    ∃ (restrict : Nat → (Unit → Nat) → (Unit → Nat)) (w : Nat → Unit → Nat),
      margDown restrict w 0 1 ≠ w 0 :=
  ⟨fun _ f => f, fun n _ => n, fun hcontra =>
    Nat.one_ne_zero (congrFun hcontra ())⟩

end QOU.MassTheory
