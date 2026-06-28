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

## What survives (the sharpened conjecture)

The proof attempt **narrows** the open content. Klein's icosahedral $A_5
\subset \mathrm{PGL}(V)$ on $\mathbb{P}(V)$ exists as classical geometry; the
conjecture is that

- this icosahedral $A_5$ — with order-$2$ and order-$3$ generators at the
  **icosahedral angle** ($\arccos$ of the vertex–face inner product), *distinct*
  from the trefoil's perpendicular pair — is realised on the Bring base
  $\mathbb{P}(V)$ through Klein's resolvent of the Bring–Jerrard quintic, and
- its quotient $\mathbb{P}(V)/A_5 \cong S^2(2,3,5)$ is the keystone Seifert base
  of $S^3/2I$.

The six branch points $\{\zeta_5^k, \infty\}$ are not $A_5$-invariant (no
icosahedral orbit has size $6$; minimum $12$): they are the $C_5$-pentagon
skeleton, the vertex-stabiliser data, not the full icosahedral set.

## Scope

This bridge lives on the geometric / $V_\lambda$ (icosahedral-selector) side of
the Schur–Weyl duality. It **motivates** the keystone's $S^3/2I$ arena; it does
**not** by itself produce the Hecke-side measure $W_\lambda$, its Schur–Weyl
dual. Promotion to a theorem requires constructing the icosahedral-angle
generators on $\mathbb{P}(V)$ (Klein's resolvent) and identifying
$\mathbb{P}(V)/A_5$ with the keystone base — both open; the trefoil-generator
route is closed by the refutation above.
