This remark collects the base-ring, three-context, Habiro,
archimedean, and physical realisations of the
[$q$-logarithm](#def:q-logarithm).

**Base-ring independence.**  The adjoint pair $(\log_q, \exp_q)$ lives
in the universal setting of Hopf algebras — no convergence is
required.  Over $\mathbb{F}_p$ the $\log_q$ of a grouplike is still
a well-defined primitive, even when the series representation fails
([finite-field obstruction](#rem:q-exp-finite-field-obstruction)).

**Three-context behaviour.**  Mirroring $\exp_q$
([$p$-adic $\exp_q$](#rem:q-exp-p-adic)):

- **$\mathbb{F}_p$.**  The series $\log_q(1 + x) = \sum (-1)^{n-1} x^n / [n]_q$
  has zero denominators whenever $[n]_q$ vanishes in $\mathbb{F}_p$
  (i.e. $n \ge \mathrm{ord}_{\mathbb{F}_p^\times}(q)$).  The truncation
  $\log_q^{(p)}(1+x) = \sum_{n=1}^{p-1} (-1)^{n-1} x^n / [n]_q$ becomes
  primitive modulo $x^p = 0$ and inverts $\exp_q^{(p)}$ on the first
  infinitesimal neighbourhood of $1$.
- **$\mathbb{Q}_p$.**  For $q \in 1 + p\mathbb{Z}_p$ the series
  converges on $1 + p\mathbb{Z}_p$ because $v_p([n]_q) = v_p(n)$ and
  the denominators grow no faster than the classical $p$-adic
  $\log$; the result is a continuous primitive $p\mathbb{Z}_p \to p\mathbb{Z}_p$
  inverting the Witt-vector $\exp_q$.
- **$\mathbb{C}_p$.**  Converges on $v_p(x) > 0$ (the open unit disc
  around $1$, i.e. $|1 + x - 1|_p < 1$), matching the classical $p$-adic
  $\log$ radius.  The logarithm extends by Iwasawa's convention to all
  of $\mathbb{C}_p^\times$ via $\log_q(p) = 0$ if one wants a global
  branch.

**Native algebraic home: the Habiro ring.**  The series
representation $\log_q(1 + x) = \sum_{n \geq 1} (-1)^{n-1} x^n/[n]_q$
has cyclotomic denominators $[n]_q$, so its partial sums are
coherent modulo the Habiro ideal $((q;q)_m)$. Equivalently, the
adjoint pair $(\log_q, \exp_q)$ acts on the formal-power-series
ring $\widehat{\mathbb{Z}[q]}[\![x]\!]$ over the Habiro ring
([Habiro ring](#def:habiro-ring)). Cyclotomic-projection
$\widehat{\mathbb{Z}[q]} \to \mathbb{Z}[q]/\Phi_N(q)$ at the
$N$-th finite place sends $\log_q$ to its level-$N$ truncation,
giving evaluation at any root of unity without invoking
$\mathbb{C}$ or analytic continuation.

**Archimedean realisation.**  Over $\mathbb{C}$ the adjoint pair
$(\log_q, \exp_q)$ is represented by the convergent series

$$
  \log_q(1 + x) \;=\; \sum_{n \ge 1} \frac{(-1)^{n-1}  x^n}{[n]_q}
$$

(a corollary of the Taylor expansion of $\exp_q$; cf.
[Taylor series of $\exp_q$](#prop:q-exponential-taylor)).

**Physical meaning.**  The Reeb-flow holonomy between two substrate
slices $q_1 < q_2$ is a grouplike element; its $q$-logarithm is the
infinitesimal generator of the flow on $\mathrm{Prim}(\mathcal{H}_q)$.  Hence
$\log_q$ measures *cosmological displacement* in Hopf-algebraic
units — the analogue of a "time rapidity" on the substrate side.
