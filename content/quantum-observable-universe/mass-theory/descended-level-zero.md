The jet-tower decomposition
([jet-tower remark](#rem\:mass-endomorphism-jet-tower))
asserts that the descended (holonomy) contribution to the mass
appears **once only**, at jet level $0$, and that levels
$n \ge 1$ carry only singleton and quadratic transient
contributions. This proposition provides the derivation: the
descended projector stabilises under composition, so iterated
:refterm[descent]{#descent} collapses to the base-level holonomy regardless of the
jet level at which it is read off.

**Proposition.** Let $\hat\tau_n$ be the :refterm[descent]{#descent} involution at
level $n$ ([:refterm[descent]{#descent} involution](#def\:descent-involution)) and
$\mathcal{A}^{\mathrm{desc}}_{n+1} = \mathrm{im}\,\hat\tau_n$
the descended subalgebra. For every jet level $n \ge 0$, the
descended component of the mass integrand $\alpha^{(n+1)}$
equals the base-level descended contribution:

$$
  \bigl\lVert
    \mathrm{tr}\!\bigl(\hat\tau_n(\alpha^{(n+1)})\bigr)
  \bigr\rVert
  \;=\;
  \mathfrak{m}(\varrho_0)
  \;=\;
  \Bigl\lvert \textstyle\prod_i \hat V_i^{(0)} \Bigr\rvert,
$$

independent of $n$. Consequently the descended term enters
the tower sum **at level $0$ only**; levels $n \ge 1$
contribute only through transient modes
$\mathcal{A}^{\mathrm{trans}}_{n+1} = \ker\hat\tau_n$.

## Why summing it per level is a double count

If the tower sum were written as

$$
  \mathfrak{m}(\varrho)
  \;\stackrel{?}{=}\;
  \sum_{n=0}^{N}
    \Bigl(
      \bigl\lvert\textstyle\prod_i \hat V_i^{(n)}\bigr\rvert
      + \sum_i \Phi_q(|\hat V_i^{(n)}|)
      + z^2 \sum_{(i,j)} \Phi_q(|\hat V_i^{(n)}\hat V_j^{(n)}|)
    \Bigr),
$$

every level would carry a separate descended product. By
Step 4 each such product equals $\mathfrak{m}(\varrho_0)$ (up
to the $\hbar_q^{2n}$ brane-tower weight), and the tower sum
would overcount the base-level holonomy by

$$
  \sum_{n=1}^{N} \hbar_q^{2n} \cdot \mathfrak{m}(\varrho_0)
  \;=\;
  \mathfrak{m}(\varrho_0) \cdot
  \frac{\hbar_q^{2}(1 - \hbar_q^{2N})}{1 - \hbar_q^{2}}.
$$

At $q_0 \approx 1.11$ and $N = 3$, this overcount is
$\approx 0.00991 \cdot \mathfrak{m}(\varrho_0)$ — a **1%
contamination** of every binding-energy prediction, much larger
than the target ppm precision. The $\hbar_q^{2n}$ weights damp
but do not eliminate the double count; only explicit restriction
to level $0$ for the descended term eliminates it.

## Correct formula

Combining Step 4 with the transient decomposition of
([topological mass proof](#prf\:topological-mass)) and the
quadratic closure of
([jet-tower remark](#rem\:mass-endomorphism-jet-tower)):

$$
  \mathfrak{m}(\varrho)
  \;=\;
  \underbrace{\Bigl\lvert \textstyle\prod_i \hat V_i^{(0)} \Bigr\rvert}_{\text{desc, level 0 only}}
  \;+\;
  \sum_{n=0}^{N} \hbar_q^{2n}
    \Bigl(
      \sum_i \Phi_q(|\hat V_i^{(n)}|)
      + z^2 \sum_{(i,j) \in \mathcal{P}_n}
        \Phi_q(|\hat V_i^{(n)} \hat V_j^{(n)}|)
    \Bigr).
$$

The descended factor is pulled out of the level sum. Only
the transient contributions (singletons and pairs) retain
the per-level $\hbar_q^{2n}$ weights, and they vanish
geometrically by the jet-tower tail bound
([jet-tower convergence](#prop\:jet-tower-convergence)).

## Engineering consequence

This proposition is the derivational justification for the
HIGH-#1 fix in the infrastructure audit
(`docs/infrastructure-audit-.md`):

> Strip the desc term from `tower_mass_level` calls inside the
> level loop; compute desc once at level 0 and treat levels 1+
> as singleton + pair only.

The fix is not a numerical trick or heuristic: it is the
correct implementation of Step 4 above. The code's prior
behaviour of re-adding the descended product at every jet
level violated the idempotence of $\hat\tau_n$ and overcounted
the level-$0$ holonomy by the geometric series displayed above.

## Relation to the Nakayama triviality

At the base level, the Nakayama automorphism
$\Psi = S^2 = \mathrm{id}$ in $H_n(R, q)$
([categorical mass as Markov trace](#prop\:categorical-mass-markov)),
The single-level mass is $\mathrm{tr}_M(\rho(\beta))$
(signed at the categorical level; positive observable at $q_0$
by Wenzl positivity for canonical $T_w$).
The base-level descended term $\prod_i \hat V_i^{(0)}$ is
exactly this Markov trace by the factorization theorem
([Markov trace factorization](#thm\:markov-trace-factorization)).
The descended contribution is therefore the **Nakayama-trivial
holonomy at the base**, and its $n$-independence in Step 4 is
the jet-tower expression of Nakayama triviality: every :refterm[descent]{#descent}
step undoes a jet prolongation without introducing new Nakayama
twist.
