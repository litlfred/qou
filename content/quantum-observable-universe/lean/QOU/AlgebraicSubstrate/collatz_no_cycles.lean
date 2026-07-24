import Mathlib.Data.Real.Basic
import Mathlib.Tactic.Ring

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
-- Ref: [manuscript] quantum-observable-universe/appendix-surreals/collatz-no-cycles.ts
theorem collatz_no_cycles [ctx : CollatzNoCyclesContext] :
    ctx.q_int_3 - ctx.q * ctx.q_int_2 = 1 ∧
    ∀ P : ℝ, ctx.is_periodic P → P = 1 :=
  by
    have h_coprime : ctx.q_int_3 - ctx.q * ctx.q_int_2 = 1 := by
      rw [ctx.q_int_2_def, ctx.q_int_3_def]
      ring
    exact ⟨h_coprime, ctx.no_cycles_of_coprime h_coprime⟩

end QOU.AlgebraicSubstrate
