Stacking the Kummer sequences for all $n$ gives the
**Kummer tower** --- a filtration of $\mathbb{G}_m$ by its
torsion subgroups:

$$
  \mu_1 \subset \mu_2 \subset \mu_3
  \subset \cdots \subset
  \mu_\infty \subset \mathbb{G}_m,
$$

where $\mu_\infty = \bigcup_{n \geq 1} \mu_n$ is the
subgroup of all roots of unity (the $\mathbb{G}_m$-torsion).
This filtration induces a descending filtration on the
obstruction:

$$
  \kappa  \in 
  F^1 H^2 \supset F^2 H^2 \supset F^3 H^2
  \supset \cdots,
  \qquad
  F^n H^2 = nH^2(\mathcal{S}, \mathbb{G}_m).
$$

The class $\kappa$ lies in $F^n$ iff it is $n$-divisible,
i.e., $\kappa \bmod n = 0$.

**The trace and divisibility.**
The [QU-to-QOU theorem](#thm:qu-to-qou) establishes that the
first Yekutieli obstruction is the Euler class of the Reeb
bundle: $\kappa_0 = e(\xi)$, with trace
$\mathrm{tr}(\kappa_0) = \chi(A)$.  The Kummer reduction
at level $n$ is controlled by the divisibility of this
trace:

$$
  \kappa_0 \bmod n = 0
  \quad\Longleftrightarrow\quad
  n  \big|  \chi(A).
$$

The obstruction $\kappa_0$ therefore vanishes at
precisely those Kummer levels $n$ that divide $|\chi(A)|$,
and persists at all others.  For any non-zero Euler
characteristic, this gives a **finite set** of vanishing
levels (the divisors of $|\chi(A)|$) and a
**density-$1$ set** of persisting levels.

**Complementary subgroup structure.**
The obstruction at level $n$ in the brane tower
([QU-to-QOU](#thm:qu-to-qou), item 3) decomposes as

$$
  \kappa_n = \kappa_0 + \delta_n,
$$

where $\delta_n$ is the jet correction at level $n$.  The
key structural fact is that $\kappa_0$ and $\delta_n$ live
in **complementary subgroups** of
$H^2(\mathcal{S}, \mathbb{G}_m)$.  The Euler class $\kappa_0$
is a topological invariant (determined by the contact
structure), while $\delta_n$ is an analytic correction
(determined by the jet data at level $n$).  They cannot
cancel: their sum $\kappa_n$ is nonzero whenever $\kappa_0$
is non-torsion.

This is the **perpetual obstruction** phenomenon: a
non-torsion Euler class $\kappa_0$ produces a non-vanishing
obstruction at every level of the brane tower.  No amount
of jet refinement can remove it.

**Motivic-Galois reading.**
*The Kummer filtration on $H^2(\mathcal{S}, \mathbb{G}_m)$ is the
restriction to the cyclotomic Galois subgroup
$\mathrm{Gal}(\mathbb{Q}(\mu_\infty)/\mathbb{Q})$ of the
**motivic-Galois filtration** on the
[motivic substrate](#def:motivic-substrate). At each finite place
$p \nmid \chi(A)$ of $\mathbb{Q}$
([adelic substrate](#def:adelic-substrate)), the realization
$\rho_p$ projects $\kappa_0$ to a non-trivial Frobenius character in
$H^1_{\mathrm{Gal}}(\mathrm{Gal}(\bar{\mathbb{Q}}_p/\mathbb{Q}_p),\,\mu_n(1))$
through the cyclotomic ideal $\mathbb{Z}[q]/\Phi_n(q)$. Perpetuity
of the obstruction is then the statement that the motivic-Galois
character of the Frobenius–Hopf substrate is non-trivial in
$\mathrm{Hom}(\chi_n, 1)$ for almost every $n$ — a stronger
formulation of "all but finitely many Kummer levels persist" that
is realised at every cyclotomic place rather than only as
torsion-divisibility.*

**Summary.**
For any quantum universe with non-zero Euler characteristic
$\chi(A) \neq 0$:

1. The Yekutieli obstruction $\kappa_0$ is non-trivial.
2. The Kummer tower produces a filtration on the obstruction
   space, indexed by divisibility.
3. The obstruction persists at all Kummer levels
   $n \nmid \chi(A)$ --- a cofinite set.
4. The complementary subgroup structure prevents jet
   corrections from cancelling the topological obstruction.
5. Any property of $\mathbf{C}_q$ that depends on the
   vanishing of $\kappa_0 \bmod n$ for all $n$ must contend
   with this arithmetic obstruction at each level of the tower.
6. **(Motivic-Galois)** Equivalently, the Frobenius character of
   $\kappa_0$ is non-trivial at almost every finite place
   $p \nmid \chi(A)$ — perpetuity is realised place-by-place in
   the realization tower, not only as a torsion-filtration claim.

The full consequences of this filtration for specific
properties of the substrate family will be developed in the
chapters that follow.
