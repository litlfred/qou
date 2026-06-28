**Conjecture (Klein icosahedral–quintic bridge, sharpened).** *There is a
faithful icosahedral $A_5$-action on the categorical base $\mathbb{P}(V)$ — the
projective space of the $2$-dimensional braiding object $V$, whose archimedean
realisation is $\tau(\mathbb{P}(V)) \cong \mathbb{P}^1(\mathbb{C})$ — realising
Klein's icosahedral solution of the Bring–Jerrard quintic, with orbifold
quotient $\mathbb{P}(V)/A_5 \cong S^2(2,3,5)$, the base of the Seifert fibration
$S^3/2I \to S^2(2,3,5)$ of the Poincaré homology sphere. Its order-$2$ and
order-$3$ generators are at the icosahedral angle and are therefore **distinct**
from the trefoil $S_3$ generators carried by the exceptional divisor.*

## Established skeleton (classical)

1. **The Bring curve is the Bring–Jerrard root variety.** The defining
   equations $\sum_j x_j = \sum_j x_j^2 = \sum_j x_j^3 = 0$
   ([Bring's curve](#rem:brings-curve)) are the vanishing of the first three
   power sums of the five roots — the configuration of quintics in
   **Bring–Jerrard normal form** $z^5 + az + b$ \cite{bring1786}.
2. **The $(2,3,5)$ triangle rotation group is the icosahedral $A_5$.** The
   triangle is spherical, $\tfrac12 + \tfrac13 + \tfrac15 = \tfrac{31}{30} > 1$,
   so its orientation-preserving group is finite of order $60$, namely $A_5$,
   acting on $\mathbb{P}(V)$ with exceptional orbits $\{12, 20, 30\}$.
3. **Klein's solution.** The one-parameter Bring–Jerrard quintic is solved by
   the icosahedral equation \cite{klein1888}, with the five roots on the five
   inscribed tetrahedra ($5 = [A_5 : A_4]$).

## Proof attempt — the naive assembly is refuted (scope-limited)

The natural first route is to *reuse* the corpus's existing force operations as
the $(2,3,5)$ generators. This route is **refuted**, decisively, from the
corpus's own data. The canonical generators ([SU(2) generators](#def:su2-generators))
are

$$
  \alpha = \exp\!\bigl(\tfrac{2\pi}{3}e_3\bigr) \ (\text{order } 3,\ \text{colour/trefoil}),
  \qquad
  \beta = \exp(\pi e_1) \ (\text{order } 2,\ \text{EM involution } z \mapsto 1/z),
$$

with the **established dihedral relation** $\beta\alpha\beta^{-1} = \alpha^{-1}$.
Since $\beta^2 = 1$ in $\mathrm{SO}(3)$ (so $\beta^{-1} = \beta$), this gives
$\beta\alpha\beta = \alpha^{-1}$, whence

$$
  (\beta\alpha)^2 = (\beta\alpha\beta)\,\alpha = \alpha^{-1}\alpha = 1.
$$

So $\beta\alpha$ has order $2$ (equivalently $\mathrm{tr}\,R_\beta R_\alpha = -1$,
a $\pi$-rotation): $\langle \alpha, \beta\rangle$ satisfies the **$(2,3,2)$
dihedral** relation and is the trefoil $S_3 \cong D_3$ — **not** the icosahedral
$(2,3,5)$ group, which would require $(\beta\alpha)$ of order $5$
($\mathrm{tr} = 2\cos 72^\circ$ or $2\cos 144^\circ$, never $-1$). The order-$5$
$\zeta_5$ pentad sits on a *third* axis and is not in any triangle relation with
$\alpha, \beta$.

This is a **scope-limited negative (a)**: it refutes the *as-is* assembly of the
existing trefoil generators, not the existence of an icosahedral realisation.
Its content is exactly the corpus's own structural split
([fivefold symmetry](#rem:fivefold-symmetry)): the $3$-fold (colour, periodic,
lattice-compatible) and the $5$-fold (weak, aperiodic, parity-violating) are
**distinct irreducible components** — they do not assemble into one icosahedral
group through the trefoil's perpendicular $e_1, e_3$ axes.

## Construction — the surviving group-theoretic core is discharged

Klein's icosahedral generators on $\mathbb{P}(V)$ (coordinate $w$,
$\varepsilon = e^{2\pi i/5}$ \cite{klein1888}) supply the icosahedral-angle pair
the trefoil could not — and the order-$5$ element is *exactly the corpus
$\zeta_5$ pentad*:

$$
  S : w \mapsto \varepsilon\, w \quad (\text{the } \zeta_5 \text{ pentad, order } 5,\ \text{fixing } 0/\infty),
  \qquad
  T = \tfrac{1}{\sqrt5}\begin{pmatrix} \varepsilon-\varepsilon^4 & \varepsilon^2-\varepsilon^3 \\ \varepsilon^2-\varepsilon^3 & -(\varepsilon-\varepsilon^4)\end{pmatrix}
  \ (\text{icosahedral } 2\text{-fold}).
$$

Setting $c_2 = T$ (order $2$) and $c_3 = TS$ (order $3$) gives
$c_2 c_3 = T\,TS = S$ — the $\zeta_5$ pentad, of order **exactly $5$**, with
$S^5 = T^2 = (ST)^3 = 1$, so $\langle S, T\rangle \cong A_5$ (order $60$). Thus
order-$2$/order-$3$ generators at the icosahedral angle, *distinct* from the
trefoil's perpendicular pair, **exist** and assemble the $\zeta_5$ pentad into
the icosahedral $A_5$. Verified parameter-free in
[`scripts/keystone_klein_icosahedral_construction.py`](https://github.com/litlfred/qou/blob/main/scripts/keystone_klein_icosahedral_construction.py);
the abstract realizability of the $(2,3,5)$ relation is Lean-proved sorry-free
(`icosahedral_235_realizable`: explicit even permutations $(1\,2)(3\,4)$,
$(0\,2\,4)$ with product the $5$-cycle), the positive complement to the
$(2,3,2)$ refutation.

The six branch points $\{\zeta_5^k, \infty\}$ are not $A_5$-invariant (no
icosahedral orbit has size $6$; minimum $12$): they are the $C_5$-pentagon
skeleton — the equatorial $S$-orbit — not the full icosahedral set.

## Keystone-base orbifold identification (established)

The orbifold quotient is classical icosahedral geometry, and it is the keystone
base. The three exceptional $A_5$-orbits on $\mathbb{P}(V)$ — vertices ($12$),
faces ($20$), edges ($30$) — have cyclic stabilisers of orders
$60/\{12,20,30\} = \{5,3,2\}$, the **cone-point orders** of the quotient. Hence

$$
  \mathbb{P}(V)/A_5 \;=\; S^2(2,3,5),
  \qquad
  \chi_{\mathrm{orb}} = 2 - \!\sum_{m\in\{2,3,5\}}\!\bigl(1-\tfrac1m\bigr)
   = \tfrac{1}{30}
   = \frac{\chi(\mathbb{P}^1)}{|A_5|} = \frac{2}{60},
$$

the matching Euler characteristics confirming the underlying surface is the
genus-$0$ sphere \cite{klein1888}. This spherical orbifold $S^2(2,3,5)$ is
exactly the base of the Seifert fibration $S^3/2I \to S^2(2,3,5)$ of the
**Poincaré homology sphere** — $2I \subset \mathrm{SU}(2)=S^3$ being the binary
cover of $A_5 \subset \mathrm{SO}(3)$, so the induced fibration descends to
$\mathbb{P}^1/A_5$. The cone-structure facts are Lean-proved sorry-free
(`cone_orders`, `orbifold_euler_char`, `orbifold_euler_char_eq_cover`,
`orbifold_spherical`).

## The sole residual open content — canonicity on the categorical base

With the group-theoretic core *constructed* and the orbifold target
*identified*, the only remaining conjectural claim is the **canonicity** of the
icosahedral action on the categorical base $\mathbb{P}(V)$: that the icosahedral
$A_5$ is intrinsic to the braiding object $V$, not merely imposed. The corpus
furnishes the order-$5$ $\zeta_5$ pentad ($c_2c_3$) and the order-$3$ trefoil
canonically; what is not yet established is a *canonical* icosahedral $2$-fold —
Klein's $T$, at the icosahedral angle, distinct from the dihedral EM involution
$\beta$ the corpus carries. Pinning $T$ to a braiding-intrinsic operation on
$\mathbb{P}(V)$ would promote the whole bridge to a theorem.

**Scope (unchanged).** Even fully established, this bridge sits on the geometric
/ $V_\lambda$ (icosahedral-selector) side of the Schur–Weyl duality: it
identifies and motivates the keystone $S^3/2I$ arena, but does **not** produce
the Hecke-side measure $W_\lambda$, its Schur–Weyl dual. The keystone
$W_\lambda$ closure remains the separate open problem.

## Scope

This bridge lives on the geometric / $V_\lambda$ (icosahedral-selector) side of
the Schur–Weyl duality. It **motivates** the keystone's $S^3/2I$ arena; it does
**not** by itself produce the Hecke-side measure $W_\lambda$, its Schur–Weyl
dual. Promotion to a theorem requires constructing the icosahedral-angle
generators on $\mathbb{P}(V)$ (Klein's resolvent) and identifying
$\mathbb{P}(V)/A_5$ with the keystone base — both open; the trefoil-generator
route is closed by the refutation above.
