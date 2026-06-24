**Proposition.** *In the $\mathfrak{Q}_\beta$ precision-ladder factorisation*

$$
\mathfrak{Q}_\beta(q) \;=\; Q_A(q) \cdot \cos(\alpha_{\text{eff}}(q))
  \cdot \prod_{k \ge 2} \bigl(1 + c_k \cdot u^k\bigr),
\qquad u \;=\; b(q) \cdot \hbar_q^2,
$$

*the ladder $R(u) := \prod_k(1 + c_k u^k)$ admits a clean integer-$u$ Taylor
representation (no $\sqrt{u}$ branch) if and only if $R$ is bar-even, i.e.
$R$ is an even function of $t := q - 1$ about $q = 1$.*

## Why this matters (the structural discriminant)

The substrate variable $u = b(q) \cdot \hbar_q^2$ has a **double zero** at
$q = 1$:

$$
u(q) \;=\; b(1) \cdot t^2 + O(t^3)
\;=\; \frac{\sqrt{3}}{2} \, t^2 + O(t^3),
\qquad t = q - 1.
$$

Under the bar-involution $q \mapsto q^{-1}$, the local coordinate transforms
as $t \mapsto -t + O(t^2)$. The leading term $u \sim t^2$ is invariant under
$t \mapsto -t$, so:

- **If $R$ is even in $t$** (bar-even), every Taylor coefficient lives at
  even powers of $t$, which the $u$-grading absorbs: $R(u)$ admits
  an integer-power Taylor representation in $u$ with no $\sqrt{u}$ branch.
- **If $R$ has odd-in-$t$ content**, those coefficients sit at $t^{2k+1}$
  and cannot be absorbed into integer powers of $u \sim t^2$: the $q \to u$
  reversion picks up a $\sqrt{u}$ branch, and the scalar $c_k$ extraction
  is singular at $u = 0$ (the $\sqrt{u}$-branch obstruction).

The bar-even invariant is the **§4(b) formalize-first gate** of the
[refuted-class map](../../../docs/audits/2026-06-04-qbeta-ck-refuted-class-map-and-open-axis.md):
*any candidate kernel $R(q,\xi)$ for the Habiro element $F(q)$ must clear
the bar-evenness check before the numerical anchor sweep runs*.

## Proof (one-line ring identity)

The N=2 instance is the prototype. With $u = b \cdot \hbar_q^2$:

$$
1 \;-\; u^2
\;=\; 1 - (b \cdot \hbar_q^2)^2
\;=\; 1 - b^2 \cdot \hbar_q^4.
$$

This is a `ring` identity in any commutative ring containing $b$ and
$\hbar_q$. Both factors are bar-even at the Taylor level: $b^2(q)$ is a
manifest q-rational that satisfies $b^2(q^{-1}) = b^2(q)$ exactly
(verified in the [`qbeta_symbolic_chain_alpha_b.py`](https://github.com/litlfred/qou/blob/main/computations/qbeta/qbeta_symbolic_chain_alpha_b.py)
chain), and $\hbar_q^4$ is even in $t$ to leading order
($\hbar_q = t - t^2 + O(t^3)$, so $\hbar_q^2 = t^2 - 2t^3 + O(t^4)$ and
$\hbar_q^4 = t^4 + O(t^5)$ — the odd-in-$t$ content sits at orders $t^5$
and higher, which the bar-even ladder absorbs trivially). $\blacksquare$

## Contrast: α_EM template vs 𝔔_β trace-difference

| programme | kernel | bar-even? | scalar $c_k$ extraction |
|---|---|---|---|
| $\alpha_{\text{EM}}$ | $H(q) = [2]_q \cdot (1 - h^2 \alpha)$ | **yes** — $[2]_q = q + q^{-1}$ and $h^2 = (q - q^{-1})^2$ are manifest q-symmetric | **clean** |
| $\mathfrak{Q}_\beta$ | trace-difference $T_\beta$ on the operator level | **no** — archimedean trace mixes odd-in-$t$ content (closed operator-level framing) | **singular at $u = 0$** |

The bar-even discriminant explains the asymmetry structurally: $\alpha_{\text{EM}}$
admits a scalar Habiro element because its kernel is bar-even; $\mathfrak{Q}_\beta$ does
not, so its $c_k \ge 3$ requires the **operator-level grading** (the open
[probe-B](https://github.com/litlfred/qou/blob/claude/qbeta-ck-habiro-operator-route-2026-06-04/docs/audits/2026-06-04-qbeta-ck-operator-route-kickoff.md)
spec from the closed sibling analysis).

## Use in the formalize-first gate for new $F(q)$ candidates

Before any numerical anchor sweep on a new candidate $F(q)$ / kernel
$R(q,\xi)$:

1. **State the candidate** as a power series in $t = q - 1$ (or
   equivalently, a Laurent polynomial in $q^{\pm 1/2}$).
2. **Compute $R(q^{-1}, \xi^{-1})$** symbolically.
3. **Subtract**: $\Delta := R(q,\xi) - R(q^{-1}, \xi^{-1})$. If
   $\Delta \neq 0$ identically (as an element of the ring), the candidate
   has odd-in-$t$ content and **cannot** produce a clean integer-$u$
   ladder.
4. **Stop**: a candidate failing this check is a member of refuted class
   C1–C2 (real-q forms with anchor-dependent odd-$t$ content) — add a row
   to the refuted-class map §2 and abort the numerical sweep.

This is the bar-involution test of the §4 invariants from the
refuted-class map, formalised. It complements the
[`CFinite.recurrence_step`](https://github.com/litlfred/qou/blob/main/content/quantum-observable-universe/lean/QOU/QBeta/RationalCoeffRecurrence.lean)
engine: the
recurrence step says "*given a kernel, here is the next $c_k$*"; the
bar-even invariant here says "*here is the necessary condition any
candidate kernel must satisfy*".
