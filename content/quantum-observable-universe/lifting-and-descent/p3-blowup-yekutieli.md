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

**Location of a counter-example: the cohomological address.**
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
