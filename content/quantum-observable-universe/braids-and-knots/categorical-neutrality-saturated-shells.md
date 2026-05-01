## Statement

**Proposition 1 (Categorical Neutrality of Saturated Shells).**
*An $n$-strand algebraic state represents a stable, completed shell if
and only if the full-twist ribbon operator $\theta_n \in Z(H_n(q))$
acts trivially on the dominant irreducible Hecke module $V_\lambda$,
yielding a global topological charge*

$$
  \kappa_\lambda \;:=\; \sum_{x \in \lambda} c(x) \;=\; 0,
$$

*where $c(x) = j - i$ is the discrete Jucys–Murphy content of the
box $x = (i, j) \in \lambda$.*

## Status

This is a **conjecture** (CLAUDE.md §3b axiom-class pattern): it
asserts the *physical* equivalence between "stable, completed shell"
and the algebraic neutrality condition $\kappa_\lambda = 0$. Two
ingredients are standard Hecke folklore and are used as inputs:

- **Eigenvalue of the full twist on $V_\lambda$**: $\theta_n$ is
  central in $H_n(q)$ and acts as the scalar $q^{2 \kappa_\lambda}$
  on $V_\lambda$ \cite{mathas1999, kassel1995}.
- **Content sum vanishing $\Leftrightarrow$ self-conjugate
  partition**: over a fully saturated Jucys–Murphy spectrum (all
  boxes contributing once each), $\sum_{x \in \lambda} c(x) = 0$ iff
  $\lambda = \lambda'$.

The conjectural content is the *first* direction — that saturation
of the brane tower forces global neutrality — which depends on the
locality-free reading of the categorical mass endomorphism
([mass endomorphism conjecture](#conj:mass-endomorphism)) and on the
absence of a screening mechanism in the rigid braided monoidal
category.

## Proof sketch (conjectural)

**Step 1 — Global topological action.**
Operating without any locality hypothesis on $\Phi_n$
([phi-n as global section](#rem:phi-n-global-section)), any
non-trivial action of the ribbon operator $\theta_n$ on a putative
"local" state cannot be screened: it propagates unbounded topological
flux through the rigid braided monoidal category $\mathbf{C}$.
Finite observable mass

$$
  \mathfrak{m}(\varrho) \;=\; \mathrm{tr}_M\!\bigl(\Phi_n(\varrho)\bigr)
$$

therefore requires $\theta_n \cdot \Phi_n = \Phi_n$, i.e. absolute
topological neutrality of the saturated state.

**Step 2 — Jucys–Murphy content evaluation.**
By a standard result of Hecke representation theory
\cite{mathas1999}, the full twist $\theta_n$ is central in $H_n(q)$
and acts on the irreducible $V_\lambda$ by the scalar
$q^{2 \kappa_\lambda}$, where

$$
  \kappa_\lambda \;=\; \sum_{x \in \lambda} c(x),
  \qquad
  c\bigl((i, j)\bigr) \;=\; j - i.
$$

Triviality of $\theta_n$ on $V_\lambda$ at generic $q$ is therefore
equivalent to $\kappa_\lambda = 0$.

**Step 3 — The self-conjugacy constraint.**
For a partition $\lambda \vdash n$ with conjugate $\lambda'$, the
content sum satisfies

$$
  \kappa_{\lambda'} \;=\; -\,\kappa_\lambda.
$$

When the Jucys–Murphy spectrum is fully saturated — every box
contributes its content exactly once and there is no external
weighting — $\kappa_\lambda = 0$ forces $\lambda = \lambda'$.
Stable completed shells therefore correspond to perfectly symmetric,
**self-conjugate** Young diagrams in the Hecke branching lattice.

## What this replaces

This proposition is the algebraic-geometry replacement for the
matrix-evaluation criterion of
[shell-closure-stability](#prop:shell-closure-stability): instead
of measuring shell closure by SDP-monotonicity of $\sigma_F$ along
the dressing chain, it reads it directly off the centre of $H_n(q)$.
The two criteria are predicted to coincide on the noble-gas /
nuclear-magic ladders, but the centre-of-Hecke version generalises
to $n \geq 12$ where Hoefsmit matrix evaluation is intractable
([magic numbers from $q$](#prop:magic-numbers-from-q),
[k=12 barrier bypass](#rem:k12-barrier-bypass)).
