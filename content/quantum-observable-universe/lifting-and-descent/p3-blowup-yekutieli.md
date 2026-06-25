> **Summary.** Finite-time NS blowup is identified with a finite obstruction level $n^*$ in the brane tower at which a velocity field ceases to lift (the Yekutieli lifting obstruction).
> A counter-example is encoded by the cohomological address $(v_0, T^*, \Sigma, n^*, \kappa_{n^*})$, with the singular set $\Sigma$ controlled by local cohomology at the unit defect $z=1$.

The [regularity breakdown](#conj\:regularity-breakdown) at $q = 1$
is a **cohomological obstruction** in the
[Yekutieli lifting](#prop\:yekutieli-lifting) framework.

## Yekutieli tower and regularity

The [recursive brane tower](#def\:recursive-brane-tower)
$\{A_n\}_{n \geq 0}$ with jet prolongations
$A_n \hookrightarrow A_{n+1}$ produces a sequence of central
extensions of gerbes

$$
  1 \to \mathcal{B}
  \to \mathfrak{G}_{n+1}
  \to \mathfrak{G}_n
  \to 1,
$$

each carrying an obstruction class
$\kappa_n \in H^2(\mathcal{S}, \mathcal{B})$
([quantum characteristic classes](#def\:quantum-characteristic-classes)).
A velocity field $v$ on the state bundle $\mathcal{S}$ is
**smooth** (infinitely differentiable) if and only if it lifts
through the entire tower — i.e. $v$ admits a compatible
representative at every level $A_n$:

$$
  v \text{ smooth}
  \quad\Longleftrightarrow\quad
  \kappa_n(v) = 0  \forall n \geq 0.
$$

## Regularity as lifting

**Regularity as lifting.**
The [q-NS solution](#thm\:q-ns-wellposedness) $v_q(t)$ is smooth
for $q > 1$ because the exponential damping of high modes ensures
$v_q$ has exponentially decaying Fourier coefficients, which
guarantees all Yekutieli obstruction classes vanish:

$$
  |\hat{v}_k(t)| \leq |\hat{v}_k(0)|e^{-\nu_q[k]_q^2 t}
  \quad\Longrightarrow\quad
  \kappa_n(v_q(t)) = 0  \foralln.
$$

The decay rate $\nu_q [k]_q^2 \sim \varepsilonq^{2k}$ exceeds
any polynomial, so $v_q$ lifts through the tower to all levels.

## Blowup as cohomological obstruction

**Blowup as obstruction.**
At $q = 1$, the spectral decay becomes polynomial:
$|\hat{v}_k(t)| \sim k^{-s}$ for some Sobolev exponent $s$.
The obstruction class $\kappa_n(v_1(t))$ at level $n$ is
controlled by the $n$-th jet of $v$, which involves derivatives
of order $n$.  If $v \in H^s$ with $s$ finite, then for
$n > s$ the $n$-th jet is undefined and the lifting fails:

$$
  \kappa_n(v_1(t)) \neq 0
  \quad\text{for}\quad
  n > s(t),
$$

where $s(t)$ is the Sobolev regularity at time $t$.

**Finite-time blowup means finite obstruction level.**
If a NS solution loses regularity at time $T^*$, its Sobolev
exponent $s(t) \to s^*$ as $t \to T^{*-}$ for some finite
$s^* \geq 0$.  The **obstruction level** is

$$
  n^* = \lfloor s^* \rfloor + 1.
$$

This is the level in the brane tower where the velocity field
ceases to lift.  The blowup is localised at this level:

* **Below $n^*$**: the velocity is smooth and lifts perfectly.
* **At $n^*$**: the obstruction class $\kappa_{n^*}$ is nonzero
  — the twisted 2-cocycle condition
  ([:refterm[descent]{#descent} condition](#prop\:descent-condition)) fails.
* **Above $n^*$**: the solution does not exist in those gerbes.

## Cohomological address of a counter-example

**Where a counter-example lives: the cohomological address.**
A counter-example to NS regularity is a quintuple

$$
  (v_0, T^*, \Sigma, n^*, \kappa_{n^*})
$$

consisting of:

1. **Initial data** $v_0 \in C^\infty(\mathbb{R}^3)$,
   divergence-free, finite energy.
2. **Blowup time** $T^* < \infty$.
3. **Singular set** $\Sigma \subset \mathbb{R}^3$ — the spatial
   locus where regularity fails.
4. **Obstruction level** $n^* \in \mathbb{N}$ — the brane tower
   level where lifting fails.
5. **Obstruction class** $\kappa_{n^*} \in H^2(\Sigma, \mathcal{B})$
   — the nonzero cohomology class that prevents lifting.

The Hausdorff dimension $d_H(\Sigma)$ and the obstruction level
$n^*$ are related by Sobolev embedding:

| $d_H(\Sigma)$ | Blowup geometry | $n^*$    | Singular $H^s$ |
| ------------- | --------------- | -------- | -------------- |
| $0$           | Point           | $\geq 3$ | $s^* < 3/2$    |
| $1$           | Filament        | $\geq 2$ | $s^* < 2$      |
| $2$           | Sheet           | $\geq 1$ | $s^* < 5/2$    |

## Local cohomology and topological selection

**The local cohomology connection.**
The [local cohomology group](#def\:local-cohomology-group)
$H^1_{\mathfrak{m}_1}(A)$ at the unit defect $z = 1$ measures
precisely the obstruction to extending sections across the
singularity.  At $q = 1$, the defect locus $\{z = 1\}$ is the
entire base manifold (the substrate parameter is identically
$1$), so:

$$
  H^1_{\mathfrak{m}_1}(A)\big|_{q=1}
  = 
  R^1\Gamma_{\mathfrak{m}_1}(A)
   \neq  0.
$$

This nonvanishing is the algebraic origin of the blowup: the
$\mathfrak{m}_1$-torsion functor has nontrivial derived functor
precisely at the point $q = 1$ where regularity fails.

For $q > 1$, the defect locus $\{z = q^{-1}\} \neq \{z = 1\}$
is separated from the unit, and $H^1_{\mathfrak{m}_1}(A) = 0$
— no obstruction, hence regularity.

**The :refterm[descent]{#descent} condition and vortex reconnection.**
The [twisted 2-cocycle condition](#prop\:descent-condition)

$$
  d(g_{ijk}^{(n)}) = a_{ij}^{(n)} \cdot g_{ijk}^{(n)}
  \cdot (a_{jk}^{(n)})^{-1}
$$

fails at the singular set $\Sigma$ because the transition
functions $g_{ij}^{(n)}$ develop discontinuities there.  In the
fluid picture, these discontinuities correspond to
[vortex reconnection](#rem\:vortex-reconnection) events where the
divisor topology changes.  The obstruction class $\kappa_{n^*}$
measures the total topological change at $\Sigma$: it is the
net "reconnection charge" — the signed count of reconnection
events weighted by their fusion-rule multiplicities.

**Constraint from Berry phase.**
The obstruction class must be consistent with the
$\mathrm{SU}_q(2)$ representation theory.  Specifically,
$\kappa_{n^*}$ must lie in the image of the character map

$$
  \chi \colon
  \mathrm{Rep}(\mathrm{SU}_q(2))
   \to 
  H^2(\Sigma, \mathcal{B}),
$$

which restricts the possible values of $\kappa_{n^*}$ to a
discrete lattice.  This is a **topological selection rule** on
the blowup: not all vorticity concentrations are allowed, only
those whose cohomological charge is compatible with the
categorical structure.
