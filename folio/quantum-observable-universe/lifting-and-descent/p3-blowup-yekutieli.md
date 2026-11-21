The [regularity breakdown](#conj:regularity-breakdown) at $q = 1$ is a **cohomological obstruction** in the [Yekutieli lifting](#prop:yekutieli-lifting) framework.

## Brane tower and regularity

The [recursive brane tower](#def:recursive-brane-tower) $\{A_n\}_{n \geq 0}$ with jet prolongations $A_n \hookrightarrow A_{n+1}$ produces a sequence of central extensions of gerbes:
$$
  1 \to \mathcal{B}
  \to \mathfrak{G}_{n+1}
  \to \mathfrak{G}_n
  \to 1.
$$
Each carries an obstruction class $\kappa_n \in H^2(\mathcal{S}, \mathcal{B})$ ([quantum characteristic classes](#def:quantum-characteristic-classes)). A velocity field $v$ on the state bundle $\mathcal{S}$ is **smooth** if and only if it lifts through the entire tower. It admits a compatible representative at every level $A_n$:
$$
  v \text{ smooth}
  \quad\Longleftrightarrow\quad
  \kappa_n(v) = 0  \forall n \geq 0.
$$

## Blowup as cohomological obstruction

**Blowup as obstruction.** At $q = 1$, the spectral decay is polynomial: $|\hat{v}_k(t)| \sim k^{-s}$ for some Sobolev exponent $s$. The obstruction class $\kappa_n(v_1(t))$ at level $n$ depends on the $n$-th jet of $v$, which requires derivatives of order $n$. If $v \in H^s$ with $s$ finite, the $n$-th jet is undefined for $n > s$. The lifting fails:
$$
  \kappa_n(v_1(t)) \neq 0
  \quad\text{for}\quad
  n > s(t),
$$
where $s(t)$ is the Sobolev regularity at time $t$.

**Finite-time blowup means finite obstruction level.** If a NS solution loses regularity at time $T^*$, its Sobolev exponent $s(t) \to s^*$ as $t \to T^{*-}$ for some finite $s^* \geq 0$. The **obstruction level** is:
$$
  n^* = \lfloor s^* \rfloor + 1.
$$
The velocity field ceases to lift at this level. The blowup localises here:
- **Below $n^*$**: the velocity is smooth and lifts perfectly.
- **At $n^*$**: the obstruction class $\kappa_{n^*}$ is nonzero. The twisted 2-cocycle condition ([:refterm[descent]{#descent} condition](#prop:descent-condition)) fails.
- **Above $n^*$**: the velocity field has no lift to those levels of the tower.
