import Mathlib.Tactic

/-!
# Intensive vs Extensive Binding Channels and Closure Component Arity (`qou-6xvw`, `qou-8ms1`)

This module formalizes two structural classifications in the nuclear binding sector:

1. **Intensive vs Extensive Additive Binding Channels (`qou-6xvw`)**:
   An intensive channel satisfies scale invariance $I(2A) = I(A)$, whereas an
   extensive additive channel satisfies $E(x + y) = E(x) + E(y)$ so that
   $E(2A) = 2 E(A)$ and $E(3A) = 3 E(A)$. If $I(A) = E(A) > 0$ at an anchor mass
   number $A$, then at $2A$ the extensive channel exceeds the intensive channel by
   $E(2A) - I(2A) = E(A) > 0$, and no channel with $C(A) \neq 0$ can be both
   scale-invariant and additive at $A$.

2. **Closure Component Arity vs Single-Knot Census Assignments (`qou-8ms1`)**:
   Since $\sigma_g$ and $\sigma_g^{-1}$ induce the same permutation transposition,
   the closure component count of the canonical $A$-nucleon word with $m_{\mathrm{odd}}$
   odd-multiplicity bonds is $c_{\mathrm{atom}}(A, m_{\mathrm{odd}}) = 2A - m_{\mathrm{odd}}$.
   At unit bond multiplicity ($m_{\mathrm{odd}} = A - 1$), $c_{\mathrm{atom}}(A, A - 1) = A + 1$.
   Consequently $c_{\mathrm{atom}}(2, 1) = 3 \neq 1$ (excluding single-component knots
   such as $6_2$ at $A = 2$) and $c_{\mathrm{atom}}(3, 2) = 4 \notin \{1, 3\}$
   (excluding $8_{11}$ and $L6a4$ at $A = 3$).
-/

namespace QOU.MassTheory.IntensiveVsExtensiveBindingAndClosureArity

/-- An additive channel $E(x + y) = E(x) + E(y)$ satisfies $E(2A) = 2 E(A)$ and
$E(3A) = 3 E(A)$ for every $A$. -/
theorem additive_channel_double_and_triple (E : ℝ → ℝ)
    (h_add : ∀ x y : ℝ, E (x + y) = E x + E y) (A : ℝ) :
    E (2 * A) = 2 * E A ∧ E (3 * A) = 3 * E A := by
  have h2_arg : 2 * A = A + A := by ring
  have h2 : E (2 * A) = 2 * E A := by
    rw [h2_arg, h_add A A]
    ring
  have h3_arg : 3 * A = 2 * A + A := by ring
  have h3 : E (3 * A) = 3 * E A := by
    rw [h3_arg, h_add (2 * A) A, h2]
    ring
  exact ⟨h2, h3⟩

/-- If an intensive channel $I(2A) = I(A)$ and an extensive channel $E(2A) = 2 E(A)$
agree at anchor $A$ with $E(A) > 0$, their discrepancy at $2A$ is $E(A) > 0$. -/
theorem intensive_extensive_discrepancy_at_double (I E : ℝ → ℝ) (A : ℝ)
    (h_int : I (2 * A) = I A) (h_ext : E (2 * A) = 2 * E A)
    (h_anchor : I A = E A) (h_pos : 0 < E A) :
    E (2 * A) - I (2 * A) = E A ∧ 0 < E (2 * A) - I (2 * A) := by
  have h_diff : E (2 * A) - I (2 * A) = E A := by
    rw [h_ext, h_int, h_anchor]
    ring
  have h_diff_pos : 0 < E (2 * A) - I (2 * A) := by
    rw [h_diff]
    exact h_pos
  exact ⟨h_diff, h_diff_pos⟩

/-- No channel $C : \mathbb{R} \to \mathbb{R}$ with $C(A) \neq 0$ can simultaneously
satisfy scale-invariance $C(2A) = C(A)$ and extensivity $C(2A) = 2 C(A)$. -/
theorem no_nonzero_channel_both_intensive_and_extensive (C : ℝ → ℝ) (A : ℝ)
    (h_nz : C A ≠ 0) :
    ¬ (C (2 * A) = C A ∧ C (2 * A) = 2 * C A) := by
  rintro ⟨h_int, h_ext⟩
  have h_eq : C A = 2 * C A := by
    rw [← h_int, h_ext]
  have h_zero : C A = 0 := by
    linarith
  exact h_nz h_zero

/-- Free $A$-nucleon braid closure component count $c_{\mathrm{free}}(A) = 2A$. -/
def freeClosureComponents (A : ℤ) : ℤ :=
  2 * A

/-- Bonded $A$-nucleon braid closure component count $c_{\mathrm{atom}}(A, m_{\mathrm{odd}})
= 2A - m_{\mathrm{odd}}$ after $m_{\mathrm{odd}}$ odd-multiplicity inter-nucleon bonds. -/
def atomClosureComponents (A m_odd : ℤ) : ℤ :=
  freeClosureComponents A - m_odd

/-- On a connected chain of $A - 1$ odd-multiplicity bonds, the closure component
count is $c_{\mathrm{atom}}(A, A - 1) = A + 1$. -/
theorem unit_bond_chain_components (A : ℤ) :
    atomClosureComponents A (A - 1) = A + 1 := by
  unfold atomClosureComponents freeClosureComponents
  have h_alg : 2 * A - (A - 1) = A + 1 := by
    ring
  exact h_alg

/-- At $A = 2$ ($m_{\mathrm{odd}} = 1$) and $A = 3$ ($m_{\mathrm{odd}} = 2$), the derived
closure component counts are $3$ and $4$ respectively, excluding $1$-component knots
and $3$-component links at $A = 3$. -/
theorem deuteron_and_triton_closure_arity_obstruction :
    atomClosureComponents 2 1 = 3 ∧
      atomClosureComponents 2 1 ≠ 1 ∧
      atomClosureComponents 3 2 = 4 ∧
      atomClosureComponents 3 2 ≠ 1 ∧
      atomClosureComponents 3 2 ≠ 3 := by
  have h2 : atomClosureComponents 2 1 = 3 := by
    have h := unit_bond_chain_components 2
    exact h
  have h3 : atomClosureComponents 3 2 = 4 := by
    have h := unit_bond_chain_components 3
    exact h
  refine ⟨h2, ?_, h3, ?_, ?_⟩
  · rw [h2]; decide
  · rw [h3]; decide
  · rw [h3]; decide

end QOU.MassTheory.IntensiveVsExtensiveBindingAndClosureArity
