Let $\beta$ be a braid with $c$ crossings, $L = \hat{\beta}$
its closure, and
$\kappa_c^{\mathrm{comp}}(L, q) \in H^2(\mathcal{R}, \mathbb{G}_m)$
be the Skein resolution obstruction
([Skein resolution obstruction](#def:skein-resolution-obstruction)).
The Kummer exact sequence
([Kummer specialisation](#prop:ns-kummer-specialisation))

$$
  1 \to \mu_n \to \mathbb{G}_m
  \xrightarrow{(\cdot)^n} \mathbb{G}_m \to 1
$$

specialises the obstruction at each $\mathbb{G}_m$-torsion
level $n$:

$$
  \kappa_c^{\mathrm{comp}}(L, q)
  \;\mapsto\;
  \kappa_c^{\mathrm{comp}}(L, q) \bmod n
  \;\in\;
  H^2(\mathcal{R}, \mathbb{G}_m) / n\,H^2(\mathcal{R}, \mathbb{G}_m).
$$

**Proposition.**
*Let $\beta$ encode a computation with $c$ crossings, and let
$\deg P_L = c^2 - 1$ be the maximal degree of the Skein
polynomial
([quantum universality](#conj:quantum-computational-universality),
part 4).  At the root of unity $q_k = e^{2\pi i/(k+2)}$ with
$n = k + 2$:*

1. *(Topological component.)*
   *$\kappa_c^{\mathrm{comp}} \bmod n = 0$ iff $n > c^2 - 1$ —
   iff the Hecke algebra quotient $H_n(q_k)/\mathrm{Rad}$ has
   dimension exceeding the Skein polynomial degree, so that no
   information is lost in the cyclotomic reduction.*

2. *(Analytic component.)*
   *Even when the topological component vanishes ($n > c^2 - 1$),
   the analytic component $\delta_c^{\mathrm{comp}}$ measures
   the irreducible weight of the resolution tree — the fraction
   of $3^c$ paths that carry non-cancelling Skein weight.  For
   NP-complete braids, this component is non-vanishing:*

   $$
     \delta_c^{\mathrm{comp}}(L, q_k) \;\neq\; 0
     \qquad\text{(NP-complete $\beta$, any $k$).}
   $$

3. *(Complementary subgroups.)*
   *The topological and analytic components live in complementary
   summands of $H^2(\mathcal{R}, \mathbb{G}_m)$, paralleling the
   NS obstruction
   ([NS obstruction tower](#prop:ns-obstruction-tower)): the
   topological component is a discrete invariant (Skein degree mod
   $n$), while the analytic component is a continuous invariant
   (residual weight in $(0, \infty)$).  They cannot cancel.*

**Parallel with the NS Kummer specialisation.**

The structure mirrors the NS case exactly:

| NS obstruction | Computational obstruction |
|----------------|--------------------------|
| $\kappa_0 = e(\xi)$, $\mathrm{tr} = \chi(A) = -6$ | $\kappa_c^{\mathrm{comp, top}}$, $\mathrm{tr} = \deg P_L = c^2 - 1$ |
| $\kappa_0 \bmod n = 0$ iff $n \mid 6$ | $\kappa_c^{\mathrm{comp, top}} \bmod n = 0$ iff $n > c^2 - 1$ |
| Vanishes for $n \in \{1,2,3,6\}$ | Vanishes for $n > c^2 - 1$ |
| Persists for $n \geq 7$ (infinitely many) | Persists for $n \leq c^2 - 1$ (finitely many, but growing with $c$) |
| $\delta_n$: jet divergence at collision | $\delta_c^{\mathrm{comp}}$: irreducible tree weight |
| Complementary in $H^2(\mathcal{S}, \mathbb{G}_m)$ | Complementary in $H^2(\mathcal{R}, \mathbb{G}_m)$ |

**The Kummer tower and the quadratic level.**

At root of unity $q_k$, the Hecke algebra $H_n(q_k)$ has
radical $\mathrm{Rad} \neq 0$, and the quotient
$H_n(q_k)/\mathrm{Rad}$ has dimension bounded by $(k+2)^n$.
The Skein polynomial, reduced modulo the cyclotomic ideal
$(q^{k+2} - 1)$, has degree $\leq k + 1$.

Part (1) of the
[quantum universality](#conj:quantum-computational-universality)
conjecture says: the level $k$ must satisfy $k + 2 \leq c^2 - 1$
for the polynomial to retain all information.  This is the
Kummer divisibility condition: the obstruction at level $n$ is

$$
  \kappa_c^{\mathrm{comp}} \bmod n
  \;=\;
  \begin{cases}
    0 & \text{if } n > c^2 - 1, \\
    \neq 0 & \text{if } n \leq c^2 - 1 \text{ and }
      n \nmid (c^2 - 1).
  \end{cases}
$$

For NP-complete braids with $c = \Omega(N)$, the obstruction
persists through all Kummer levels $n \leq c^2 - 1 =
\Omega(N^2)$ — quadratically many levels.  This is the
**computational perpetual obstruction**: the topological
component grows quadratically with the computation size, and no
finite Kummer level suffices to kill it.

**The $q \to 1$ limit.**

As $q \to 1$ (the classical limit), $\kappa \to \infty$ and
$n = 2\kappa \to \infty$.  But for any fixed computation with
$c$ crossings, $n = 2\kappa > c^2 - 1$ once $\kappa$ is
large enough, and the topological component vanishes.

However — and this is the crux — the **analytic component**
$\delta_c^{\mathrm{comp}}$ does **not** vanish at $q = 1$.
At $q = 1$, the Skein variable $s = q^{1/2} - q^{-1/2} = 0$,
and every smoothing contributes zero weight.  The resolution
tree degenerates: only the $L_+$ and $L_-$ branches survive
(with weights $q$ and $-q^{-1}$, both equal to $\pm 1$ at
$q = 1$).  The tree reduces to $2^c$ paths with weights
$\pm 1$ — a **classical Boolean computation**.

The classical Boolean sum $\sum_\gamma (\pm 1)$ is the analytic
component $\delta_c^{\mathrm{comp}}(L, 1)$.  For
NP-complete problems, this sum is irreducible: the $2^c$
Boolean paths carry non-cancelling contributions, and no
polynomial sample determines the total.  The analytic
obstruction persists at $q = 1$.

**Summary.**  The computational Kummer specialisation follows
the NS pattern: the topological component is controlled by the
Skein degree ($c^2 - 1$) via Kummer divisibility, and the
analytic component is controlled by the irreducible weight of
the resolution tree.  Both are nonzero for NP-complete braids,
they live in complementary subgroups, and the total obstruction
$\kappa_c^{\mathrm{comp}} \neq 0$ at every Kummer level — the
**computational perpetual obstruction**.
