The formal grouplike $\exp_q \in G(\mathcal{H}_q)$
([$q$-exponential](#def:q-exponential)) admits convergent
power-series realisations over the $p$-adic fields $\mathbb{Q}_p$ and
$\mathbb{C}_p$, recovering the archimedean Taylor series
([Taylor series of $\exp_q$](#prop:q-exponential-taylor)) as an
ultrametric series once the divisibility obstruction over
$\mathbb{F}_p$ ([finite-field
obstruction](#rem:q-exp-finite-field-obstruction)) is controlled by
requiring $q$ sufficiently close to $1$ in the $p$-adic metric.

**Setup.**  Let $v_p \colon \mathbb{C}_p^\times \to \mathbb{Q}$ be the
$p$-adic valuation normalised by $v_p(p) = 1$, and write
$|x|_p = p^{-v_p(x)}$.  A formal series
$\sum a_n x^n \in \mathbb{Q}_p[\![x]\!]$ converges at $x \in \mathbb{C}_p$
iff $v_p(a_n x^n) \to \infty$, i.e. iff
$v_p(a_n)/n + v_p(x) \to \infty$.

**Jackson factorial valuation.**  Assume $q \in 1 + p\mathbb{Z}_p$, so
$v_p(q - 1) = e \ge 1$.  Then $q$ has multiplicative order $p^k$ in
$(\mathbb{Z}/p^{k+e}\mathbb{Z})^\times$ for every $k \ge 0$, and

$$
  v_p\bigl([n]_q\bigr)
  \;=\;
  v_p\!\left(\frac{q^n - 1}{q - 1}\right)
  \;=\;
  v_p(n)
  \qquad
  \text{for } q \in 1 + p\mathbb{Z}_p, \; p \ne 2.
$$

(At $p = 2$ the identity $v_2([n]_q) = v_2(n) + O(1)$ holds with a
small correction.)  Consequently the Jackson factorial satisfies

$$
  v_p\bigl([n]_q!\bigr)
  \;=\;
  \sum_{k=1}^{n} v_p([k]_q)
  \;=\;
  v_p(n!)
  \;=\;
  \frac{n - s_p(n)}{p - 1},
$$

where $s_p(n)$ is the sum of base-$p$ digits of $n$ (Legendre's
formula).  The $q$-deformation therefore does **not** change the
$p$-adic growth of denominators relative to the classical exponential:
$v_p([n]_q!) = v_p(n!)$.

**Convergence on $\mathbb{Q}_p$.**  For $q \in 1 + p\mathbb{Z}_p$ and
$x \in \mathbb{Q}_p$ with $v_p(x) \ge 1$ (i.e. $x \in p\mathbb{Z}_p$),
the Taylor series

$$
  \exp_q(x) \;=\; \sum_{n \ge 0} \frac{x^n}{[n]_q!}
$$

converges in $\mathbb{Q}_p$ because
$v_p(x^n/[n]_q!) \ge n - (n - s_p(n))/(p-1) \to \infty$.  The limit is a
grouplike of $\mathcal{H}_q \otimes \mathbb{Q}_p$ and agrees, under the reduction
$\mathbb{Z}_p \twoheadrightarrow \mathbb{F}_p$, with the truncated
exponential $\exp_q^{(p)}$ of the finite-field remark.  Equivalently,
the $p$-adic $\exp_q$ is the **Witt-vector lift** of the
$\mathbb{F}_p$-truncated polynomial: the unique continuous grouplike on
$p\mathbb{Z}_p$ whose reduction mod $p$ is $\exp_q^{(p)}$ modulo
$x^p = 0$.

**Convergence on $\mathbb{C}_p$.**  Over $\mathbb{C}_p$ (the completion
of $\overline{\mathbb{Q}_p}$), the radius of convergence widens to
include fractional valuations but remains strictly smaller than the
naive archimedean disc.  The series converges for all $x \in \mathbb{C}_p$
with

$$
  v_p(x) \;>\; \frac{1}{p - 1},
$$

matching the classical $p$-adic exponential's radius
$|x|_p < p^{-1/(p-1)}$.  Since $v_p([n]_q!) = v_p(n!)$, the radius is
**identical** to the classical $\exp$ radius — the $q$-deformation
does not shrink the disc.  At the boundary $v_p(x) = 1/(p-1)$ the
series diverges (same as classical $\exp$), and the grouplike $\exp_q$
does not extend continuously beyond this disc.

**$q$-deformation of the Dwork/Artin--Hasse exponentials.**  Just as
the classical Artin--Hasse exponential
$E_p(x) = \exp\bigl(\sum_{k \ge 0} x^{p^k}/p^k\bigr)$ extends the $p$-adic
$\exp$ to $x \in \mathbb{Z}_p$ by absorbing denominators through
Frobenius, a $q$-analogue

$$
  E_p^q(x)
  \;=\;
  \exp_q\!\left(\sum_{k \ge 0} \frac{x^{p^k}}{[p^k]_q}\right)
$$

converges on the unit disc $v_p(x) \ge 0$ provided $v_p(q - 1) \ge 1$.
This is the categorical avatar of the Artin--Hasse construction and
plays the role, in the $q$-deformed story, of the Frobenius-stable
formal group law underlying Dwork's theory of exponential sums.  See
the Witt-vector lift remark
([Witt vector lift](#rem:witt-lift-qou)) for the functorial formulation.

**Comparison table.**

| Base ring | Does $\exp_q$ exist as a grouplike? | Series convergence |
|-----------|------------------------------------|--------------------|
| $\mathbb{Z}[q, q^{-1}]$ | Yes (formal) | Formal power series only |
| $\mathbb{C}$ (or char-$0$) | Yes | Entire function of $x$ |
| $\mathbb{F}_p$ ($q \in \mathbb{F}_p^\times$) | Yes (formal symbol) | Fails; replaced by $\exp_q^{(p)}$ mod $x^p$ |
| $\mathbb{Q}_p$ ($q \in 1 + p\mathbb{Z}_p$) | Yes | Converges on $p\mathbb{Z}_p$ (Witt lift) |
| $\mathbb{C}_p$ ($q \in 1 + p\mathbb{Z}_p$) | Yes | Converges on $v_p(x) > 1/(p-1)$ |
| $\mathbb{C}_p$, $v_p(q-1) = 0$ | Yes (formal) | No convergence (order of $q$ in residue field) |

**Moral.**  The grouplike $\exp_q$ is *always* present as a formal
Hopf-algebraic object; what varies between base rings is the domain of
*evaluation*.  The $p$-adic side gives a convergent realisation whenever
$q$ is $p$-adically close to $1$ — matching the heuristic that the
substrate parameter "deforms" the classical exponential without
changing its $p$-adic growth profile.
