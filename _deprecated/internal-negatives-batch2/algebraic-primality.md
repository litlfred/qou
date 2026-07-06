## Definition

**Definition (algebraic primality).**
*Let $\mathbf{C}$ be the rigid :refterm[braided monoidal category]{#braided-monoidal-category} of the
framework, $A \in \mathbf{C}$ a generating object, and $V_n =
A^{\otimes n}$ the $n$-fold tensor power. Fix substrate $q > 1$
(generic, not a root of unity). For each $n \in \mathbb{N}_{\geq 1}$,
the confinement SDP at $(n, q)$
([prop:confinement-sdp](#prop\:confinement-sdp)) has a canonical
optimal state*

$$
  \psi_n(q) \;\in\; V_n.
$$

*The integer $n$ is **algebraically prime at $q$** (synonymously,
**magic at $q$**) if and only if for every decomposition*

$$
  n \;=\; n_1 + n_2 + \cdots + n_k,
  \qquad k \geq 2,\;\; n_i \geq 1,
$$

*the kernel obstruction*

$$
  \psi_n(q) \;\notin\;
  \overline{\mathrm{span}}\bigl\{
    \psi_{n_1}(q) \otimes \psi_{n_2}(q) \otimes \cdots \otimes \psi_{n_k}(q)
  \bigr\}.
$$

## Three equivalent characterisations (conjecturally)

| Form                      | Statement                                                                                                                         |
| ------------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| **Tensor irreducibility** | $\psi_n(q)$ is not a tensor product of smaller-index canonical states                                                             |
| **SDP rank excess**       | $\rho(n, q) > \sum_i \rho(n_i, q)$ for every decomposition $n = \sum n_i$                                                         |
| **Unfolding distance**    | the braid-equivalence distance from $w_n^*(q)$ to any tensor product $w_{n_1}^* \otimes \cdots \otimes w_{n_k}^*$ is at least $1$ |

The three are conjecturally equivalent in the rigid braided monoidal
category $\mathbf{C}$ at generic $q > 1$.

## Properties

**Recursive but well-founded.** Algebraic primality at $n$ refers to
canonical states $\psi_{n_i}$ for $n_i < n$. The recursion bottoms
out at $n = 1$: there, no decomposition into $k \geq 2$ parts each
$\geq 1$ exists (sum lower-bound). $n = 1$ is therefore *vacuously*
prime — see
[prop:n-equals-1-vacuous-magic](#prop\:n-equals-1-vacuous-magic).

**$q$-fixed and intrinsic.** The definition references only the SDP
machinery and the tensor-product structure of $\mathbf{C}$. No
empirical input. Magic-set membership is a *property of $(n, q)$*
that can in principle be computed once $\mathbf{C}$, $q$, and the
SDP construction are specified.

**Stability under $q$-perturbation.** As $q$ varies in $(1, \infty)$,
the set of algebraically-prime $n$ is *piecewise constant* on open
intervals separated by critical $q^*$ values where some
$\psi_n(q)$ crosses into or out of a tensor-product span. The
existence of finitely many critical $q^*$ in any compact subinterval
follows from the rationality structure of the SDP cost in $q$
(see [qdim-argmax-theory](https://github.com/litlfred/qou/blob/claude/qou-algebraic-refactor-1qVFc/computations/qdim-argmax-theory.md)).

## Connection to existing framework conjectures

* **Homological condensation**:
  [conj:homological-shell-condensation](#conj\:homological-shell-condensation)
  characterises magic via spectral-sequence collapse. Tensor
  irreducibility translates to non-vanishing of certain higher
  $E_r$-page differentials.

## Empirical-match conjecture

The empirical magic ladder claim is the separate conjecture
[conj:algebraic-primality-equals-empirical-at-q0](#conj\:algebraic-primality-equals-empirical-at-q0):
at $q = q_0$, the set of algebraically prime integers equals
$\{1, 2, 8, 20, 28, 50, 82, 126\}$. The "$1$" is vacuous;
$\{2, 8, 20, 28, 50, 82, 126\}$ is the empirical nuclear magic
ladder.

## Why a fresh definition

Three previous candidates (partition statistics, LR self-fusion
self-conjugacy, q-dim argmax) have all been *empirically refuted*
as magic-ladder selectors — see
[magic-ladder pattern investigation](https://github.com/litlfred/qou/blob/claude/qou-algebraic-refactor-1qVFc/computations/magic-ladder-pattern-investigation.md)
and
[q-dim argmax theory](https://github.com/litlfred/qou/blob/claude/qou-algebraic-refactor-1qVFc/computations/qdim-argmax-theory.md).

Algebraic primality is the working candidate that:

1. Is *intrinsic* (no empirical input, no special $q_0$ in the
   definition itself);
2. Handles the previous "$n = 2$ degeneracy" concern *without
   special clauses* — primality reads $\psi_2 \neq \psi_1 \otimes
   \psi_1$, which holds whenever the SDP at $n = 2$ produces a
   non-trivial bound state. Self-conjugacy of the Hecke label is
   not required;
3. Is *recursively well-founded* via the $n = 1$ vacuous base case;
4. Is *empirically falsifiable* — at $q = q_0$, the predicted set
   should equal $\{1, 2, 8, 20, 28, 50, 82, 126\}$.
