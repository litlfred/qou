import Mathlib.Data.Real.Basic
import Mathlib.Tactic.Ring
import Mathlib.Algebra.Ring.GeomSum

/-!
# QOU.AlgebraicSubstrate.collatz_no_cycles

**Canonical declaration** for content block at
[`quantum-observable-universe/appendix-surreals/collatz-no-cycles.ts`](quantum-observable-universe/appendix-surreals/collatz-no-cycles.ts).

This module states the manuscript claim over a context class so the `lean.ref` URI resolves to a real, compiling declaration in the `qou` Lake package (§3b-conditional). See the declaration docstring below for what the term discharges versus what is carried as a context-class axiom.
-/

namespace QOU.AlgebraicSubstrate


/-- QOU-furnished context for the `collatz_no_cycles` claim: the fields
    below are the Skein data provided by a quantum observable universe
    `(𝐂, A, τ)` — `q` is its substrate parameter and the Skein-Collatz
    `is_periodic` predicate lives on its Skein module. The `_of_coprime`
    field carries the manuscript no-cycle content conditionally. -/
class CollatzNoCyclesContext where
  /-- Substrate parameter `q : ℝ` of the QOU. -/
  q : ℝ
  /-- The q-integer `[2]_q`. -/
  q_int_2 : ℝ
  /-- The q-integer `[3]_q`. -/
  q_int_3 : ℝ
  /-- Definition of the q-integer 2: `[2]_q = q + 1`. -/
  q_int_2_def : q_int_2 = q + 1
  /-- Definition of the q-integer 3: `[3]_q = q^2 + q + 1`. -/
  q_int_3_def : q_int_3 = q * q + q + 1
  /-- The Skein-Collatz map periodic orbits. The fixed-point set
      `Periodic = {P : ∀ k > 0, C_q^k P ≠ P} ∪ {1}`. -/
  is_periodic : ℝ → Prop
  /-- Manuscript no-cycle claim under the coprime Bézout identity. -/
  no_cycles_of_coprime : q_int_3 - q * q_int_2 = 1 → (∀ P : ℝ, is_periodic P → P = 1)

/-- **Manuscript statement** (full body):

**Proposition (balanced-holonomy cycle exclusion, within a QOU).**
Let $(\mathbf{C}, A, \tau)$ be a quantum observable universe with
substrate parameter $q$ and Skein module
$\mathcal{S}(q) \cong \mathbb{Z}[q^{\pm 1}]$.
The Skein-Collatz map $\mathcal{C}_q$ has no periodic orbit of balanced
multiplicative holonomy ($A = 1$) other than the degenerate fixed point;
equivalently $[3]_q^{k_{\mathrm{odd}}} = [2]_q^{k}$ has no solution with
$k_{\mathrm{odd}} \geq 1$, by coprimality of $[2]_q$ and $[3]_q$.

*Proof.* A periodic orbit of length $k$ with $k_{\mathrm{odd}}$
odd steps and $k_{\mathrm{even}}$ even steps satisfies
$\mathcal{C}_q^k(P) = P$. The odd steps multiply by
$[3]_q / [2]_q$ and the even steps multiply by $1/[2]_q$,
so the return condition requires:

$$
  \frac{[3]_q^{k_{\mathrm{odd}}}}{[2]_q^{k_{\mathrm{odd}} + k_{\mathrm{even}}}}
  =  1,
  \qquad\text{i.e.,}\qquad
  [3]_q^{k_{\mathrm{odd}}} =  [2]_q^k
  \quad (k = k_{\mathrm{odd}} + k_{\mathrm{even}}).
$$

But $[2]_q$ and $[3]_q$ are **coprime** in $\mathbb{Z}[q]$.
The Skein divisibility identity gives the proof in one line:

$$
  [3]_q - q[2]_q = 1,
$$

so $\gcd([2]_q, [3]_q) = 1$ by Bézout.  Since $[3]_q$
is a unit modulo $[2]_q$:

$$
  [3]_q^{k_{\mathrm{odd}}}
  \equiv 1^{k_{\mathrm{odd}}}
  \equiv 1
  \pmod{[2]_q},
$$

while $[2]_q^k \equiv 0 \pmod{[2]_q}$ for $k \geq 1$.
These are never equal for $k_{\mathrm{odd}} \geq 1$.
A cycle with $k_{\mathrm{odd}} = 0$ (all even steps) would
be $P \mapsto P / [2]_q^k = P$, forcing $P = 0$.

Therefore the only periodic orbit is $P = 1$
(the unknot).  $\square$

**Classical limit.** At $q = 1$: $\gcd(2, 3) = 1$ and
$3^a \neq 2^b$ for $a, b > 0$ (unique prime factorization).
The $q$-deformation lifts this to polynomial coprimality.

**The full $(a, a+1)$ family.** The identity
$\gcd([a]_q, [b]_q) = [\gcd(a,b)]_q$ shows that all
Collatz-type maps $(a, a+1)$ exclude periodic cycles,
since $\gcd(a, a+1) = 1$ for all $a$.  Cycle exclusion
is a consequence of consecutive integers being coprime
— a fa

[…truncated; see manuscript for remainder…]

    The Lean encoding below states the manuscript claim over a context class and discharges it from the class's fields (§3b-conditional). The declaration type-checks as a complete term; the substantive mathematical content is carried by the context-class axioms, and a full derivation from substrate primitives remains pending. -/
-- Ref: [leitner2026] quantum-observable-universe/appendix-surreals/collatz-no-cycles.ts
theorem collatz_no_cycles [ctx : CollatzNoCyclesContext] :
    ctx.q_int_3 - ctx.q * ctx.q_int_2 = 1 ∧
    ∀ P : ℝ, ctx.is_periodic P → P = 1 :=
  by
    have h_coprime : ctx.q_int_3 - ctx.q * ctx.q_int_2 = 1 := by
      rw [ctx.q_int_2_def, ctx.q_int_3_def]
      ring
    exact ⟨h_coprime, ctx.no_cycles_of_coprime h_coprime⟩

/-- **Balanced-holonomy cycle exclusion (proved, sorry-free).**

    Given a QOU whose Skein `q`-integers satisfy the Skein divisibility
    relation `[3]_q = q·[2]_q + 1` with `[2]_q` a non-unit (as holds for
    `[2]_q = q + 1` in the Skein module `ℤ[q^{±1}]`), the equation
    `[3]_q^{k_odd} = [2]_q^{k}` has **no** solution with `k ≥ 1`.

    A Skein-Collatz periodic orbit of *balanced* multiplicative holonomy
    (`A = [3]_q^{k_odd}/[2]_q^{k} = 1`) would force exactly this equation,
    so this lemma discharges the `A = 1` sub-case of no-cycles by
    coprimality — unconditionally, over a generic commutative ring. It
    does **not** settle the affine (`A ≠ 1`) case, which is part of the
    open `conj:q-collatz`.

    Proof: `[3]_q ≡ 1 (mod [2]_q)` from the divisibility relation, so
    `[2]_q ∣ [3]_q^{k_odd} − 1`; and `[2]_q ∣ [2]_q^{k}` for `k ≥ 1`.
    Equality would give `[2]_q ∣ 1`, i.e. `[2]_q` a unit — contradiction. -/
-- Ref: [collatz1937]
theorem balanced_holonomy_excluded {R : Type*} [CommRing R]
    (two three q : R) (hdiv : three = q * two + 1) (hnu : ¬ IsUnit two)
    {ko k : ℕ} (hk : 1 ≤ k) : three ^ ko ≠ two ^ k := by
  intro h
  have hdvd1 : two ∣ three - 1 := ⟨q, by rw [hdiv]; ring⟩
  have hstep : three - 1 ∣ three ^ ko - 1 := by
    simpa using sub_dvd_pow_sub_pow three 1 ko
  have hdvd_pow : two ∣ three ^ ko - 1 := hdvd1.trans hstep
  have hdvd_two_k : two ∣ two ^ k := dvd_pow_self two (Nat.one_le_iff_ne_zero.mp hk)
  have hdvd_three_pow : two ∣ three ^ ko := h ▸ hdvd_two_k
  have hone : two ∣ (1 : R) := by
    have := dvd_sub hdvd_three_pow hdvd_pow
    simpa using this
  exact hnu (isUnit_of_dvd_one hone)

end QOU.AlgebraicSubstrate
