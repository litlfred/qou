**Proposition (Min-Frobenius-norm collapse for $T_\beta$).**
*Let $H = H_n(R, q)$ be the Iwahori–Hecke algebra over a field $R$,
equipped with the Jones–Markov trace $\tau_M : H \to R$ uniquely
determined by the [Wenzl–Jones uniqueness theorem](#prop:markov-trace-frobenius-selection).
Equip $H$ with the **Frobenius inner product**
$\langle X, Y \rangle_\tau := \tau_M(X \cdot Y)$.
The element of minimum Frobenius norm satisfying the linear
constraint $\tau_M(T_\beta) = S$ for given $S \in R$ is*

$$
\boxed{\; T_\beta = S \cdot 1_H \;}
$$

*with $\| T_\beta \|^2_\tau = S^2$.*

## Proof — Lagrangian / completing-the-square argument

Let $X \in H$ satisfy the constraint $\tau_M(X) = S$.  Write the
decomposition $X = (X - S \cdot 1) + S \cdot 1$ and expand the
Frobenius norm-squared:

$$
\| X \|^2_\tau = \tau_M(X \cdot X)
              = \tau_M\big((X - S \cdot 1)(X - S \cdot 1)\big)
                + 2 S \, \tau_M(X) - S^2 \, \tau_M(1).
$$

(This is the algebraic identity $X X = (X - S)(X - S) + 2 S X - S^2$
inside any commutative ring, lifted to $H$ via the linearity of
$\tau_M$.  See [`completing_the_square_substrate`](markov-trace-frobenius-selection.lean#L139)
for the substrate-model statement.)

Substituting the Markov normalisation $\tau_M(1) = 1$ and the
constraint $\tau_M(X) = S$:

$$
\| X \|^2_\tau = \| X - S \cdot 1 \|^2_\tau + 2 S^2 - S^2
             = \| X - S \cdot 1 \|^2_\tau + S^2.
$$

The Jones–Markov trace $\tau_M$ is **positive-semi-definite on
squares** (a standard property of the unique normalised trace on
the symmetric semisimple Iwahori–Hecke algebra at generic $q$),
so $\| X - S \cdot 1 \|^2_\tau \ge 0$.  Therefore

$$
\| X \|^2_\tau \;\ge\; S^2,
$$

with equality iff $\| X - S \cdot 1 \|^2_\tau = 0$.  By the
[non-degeneracy](#prop:markov-trace-frobenius-selection) of
$\tau_M$ (Wenzl 1988, Jones 1987), the only $Y \in H$ with
$\tau_M(Y \cdot Y) = 0$ is $Y = 0$; hence $X - S \cdot 1 = 0$, i.e.
$X = S \cdot 1$.

Therefore the minimum-Frobenius-norm primal-feasible element is
$T_\beta = S \cdot 1$, with $\| T_\beta \|^2_\tau = S^2$. $\quad\blacksquare$

## Corollary — observable c_k invariance

The $\mathfrak{Q}_\beta$ production rule extracts the c_k Taylor coefficients from
$\tau_M(T_\beta)(q)$.  Under either norm choice — Euclidean L2 on
coordinate-vector space $R^6$ (the SHAPE $\times$ S decomposition)
or the canonical Markov–Frobenius norm above — the SDP **constraint**
$\tau_M(T_\beta) = S = \mathfrak{Q}_\beta / E_0$ is satisfied identically.
Therefore $\tau_M(T_\beta)(q) \equiv S(q)$ in both cases, and the
c_k are **L2/Markov-invariant**:

$$
c_k^{\,L2} = c_k^{\,Markov} = c_k\!\!\left(S(q)\right)
\quad\text{for all } k.
$$

The L2 picture and the Markov picture differ in which $T_\beta \in
H_n(R, q)$ is the *canonical* primal-feasible operator (the SDP
**objective** picks different points in the constraint level set),
but they agree on every **observable** because observables are
extracted from the constraint, not from the operator's coordinate
expansion.  The cross-anchor c_3 swing recorded in the
[canonical-framing audit](https://github.com/litlfred/qou/blob/main/docs/audits/2026-05-31-qbeta-ck-truncation-order-canonical-framing.md)
is therefore a property of $S(q) = \mathfrak{Q}_\beta(q) / E_0(q)$ itself —
upstream of the SDP norm choice.

## Categorical reading

Under the Markov–Frobenius norm $T_\beta = S \cdot 1_H$ is a
**scalar multiple of the identity**.  All q-dependence of the
canonical primal-feasible operator flows through the single
q-rational scalar $S(q)$; there is no multi-channel SHAPE
distributed across the NF basis $\{\gamma, \sigma_0, \sigma_1,
L_+, L_-, e_-\}$.  The six-channel spread observed
under the Euclidean coordinate norm is a **basis-dependence**
of the inner product on $R^6$, not categorical structure of
$T_\beta$.

This is the natural categorical answer to "what is $T_\beta$ as
an operator?": the Markov–Frobenius minimum-norm primal-feasible
solution is the **least-Hecke-Frobenius-norm** operator hitting
the target trace, which is the canonical choice from the
Wenzl–Jones standpoint.

## Lean formalisation

The substrate-model proof (where $A = R$ and $\tau = \mathrm{id}$,
reducing the algebra to its ground field) is sorry-free at
[`t_beta_markov_min_frobenius_collapse_substrate`](markov-trace-frobenius-selection.lean).
The full $H_n(R, q)$ proof — requiring the Mathlib `Algebra R A`
typeclass infrastructure plus the positive-semi-definiteness of
$\tau_M$ on squares as a class hypothesis — is queued for a
follow-up Lean PR.  The substrate-model proof captures the
essential algebraic content (the completing-the-square identity);
the general lift is mechanical typeclass scaffolding.

## References

- [`docs/audits/2026-06-03-qbeta-markov-trace-shape-collapse.md`](https://github.com/litlfred/qou/blob/claude/qbeta-markov-trace-2026-06-03/docs/audits/2026-06-03-qbeta-markov-trace-shape-collapse.md)
  — structural finding + numerical verification at $q_0$.
- [`docs/coordination/1ppq-qbeta.md`](https://github.com/litlfred/qou/blob/claude/qbeta-markov-trace-2026-06-03/docs/coordination/1ppq-qbeta.md)
  — 1ppQ master ledger.
- Jones 1987 — Hecke algebra Markov trace existence + uniqueness.
- Wenzl 1988 — non-degeneracy of the Markov trace.
