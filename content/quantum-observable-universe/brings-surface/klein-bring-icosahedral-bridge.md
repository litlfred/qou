**Conjecture (Klein icosahedral–quintic bridge).** *The three force-symmetry
operations carried by the Bring exceptional divisor — the order-$2$
electromagnetic Möbius involution $z \mapsto 1/z$
([braid-group action](#rem:braid-group-action)), the order-$3$ colour/trefoil
$3$-cycle, and the order-$5$ weak $\zeta_5$ rotation
([fivefold symmetry](#rem:fivefold-symmetry)) — are the $(2,3,5)$ generators of
a single faithful icosahedral $A_5$-action on the exceptional divisor
$\mathrm{ED} \cong \mathbb{P}^1(\mathbb{C})$, realising Klein's icosahedral
solution of the Bring–Jerrard quintic, with orbifold quotient
$\mathrm{ED}/A_5 \cong S^2(2,3,5)$ — the base of the Seifert fibration
$S^3/2I \to S^2(2,3,5)$ of the Poincaré homology sphere.*

## Established skeleton (classical)

Three classical facts make the bridge well-posed:

1. **The Bring curve is the Bring–Jerrard root variety.** The defining
   equations of Bring's surface, $\sum_j x_j = \sum_j x_j^2 = \sum_j x_j^3 = 0$
   ([Bring's curve](#rem:brings-curve)), are exactly the vanishing of the first
   three power sums of the five roots $(x_0,\dots,x_4)$ — i.e. the configuration
   space of quintics in **Bring–Jerrard normal form** $z^5 + az + b$, reached
   from the general quintic by Tschirnhaus transformations \cite{bring1786}.
2. **The $(2,3,5)$ triangle rotation group is the icosahedral $A_5$.** The
   triangle is spherical, $\tfrac12 + \tfrac13 + \tfrac15 = \tfrac{31}{30} > 1$,
   so its orientation-preserving group is finite of order $60$, namely $A_5$,
   acting on $\mathbb{P}^1(\mathbb{C})$ with exceptional orbits of sizes
   $\{12, 20, 30\}$ ($12$ vertices, $20$ faces, $30$ edges) and generic orbit
   $60$.
3. **Klein's solution.** The one-parameter Bring–Jerrard quintic is solved by
   the icosahedral equation: the degree-$60$ icosahedral rational function on
   $\mathbb{P}^1(\mathbb{C})$ \cite{klein1888}, with the five roots realised on
   the five inscribed tetrahedra ($5 = [A_5 : A_4]$).

The pentagon sits inside the icosahedron: the $\zeta_5$ rotation $C_5$ is a
vertex stabiliser in $A_5$, and together with the involution $z \mapsto 1/z$ it
generates the dihedral $D_5$ — the normaliser of a Sylow-$5$ in $A_5$. The
hyperelliptic data $y^2 = x^5 - 1$ with branch points $\{\zeta_5^k\} \cup
\{\infty\}$ ([hyperelliptic quintic](#def:hyperelliptic-quintic)) is the
$C_5$-fixed pentagon structure on the ED.

## What is conjectural (the QOU wiring)

The classical pieces above are established; the open content is their
**assembly**:

- In the corpus the three operations act on *different* coordinates — the
  $z \mapsto 1/z$ involution and the $\zeta_5$ rotation on the base ratio
  $z = x_0/x_1$, the colour/trefoil $3$-cycle on the spectral ratios
  $\eta_1, \eta_2$ ([braid-group action](#rem:braid-group-action)). The
  conjecture is that they assemble into **one** faithful $A_5$ on a single
  $\mathbb{P}^1(\mathbb{C})$ satisfying the icosahedral relation
  $(c_2 c_3)^5 = 1$, $c_2^2 = c_3^3 = 1$.
- That this $A_5$-sphere is the Seifert base $S^2(2,3,5)$ of the keystone
  Poincaré sphere $S^3/2I$, so the icosahedral arena of the
  [$W_\lambda$ keystone](https://github.com/litlfred/qou/blob/main/docs/coordination/s5-so3-keystone.md)
  is reached from the Bring ED through Klein's map rather than posited.

The six marked branch points $\{\zeta_5^k, \infty\}$ are **not** $A_5$-invariant
(no icosahedral orbit has size $6$; the minimum is $12$) — consistent with their
being the $C_5$-pentagon sub-structure rather than the full icosahedral data.
The $A_5$ acts on the *unmarked* sphere; the pentagon is its $C_5$-fixed
skeleton.

## Scope

This bridge lives on the geometric / $V_\lambda$ (icosahedral-selector) side of
the Schur–Weyl duality, where the hyperbolic volume and the icosahedral arena
sit. It **motivates** the keystone's $S^3/2I$ arena; it does **not** by itself
produce the Hecke-side measure $W_\lambda$, which is the Schur–Weyl dual (see the
gauge-embedding scope audit). Promotion to a theorem requires (i) the single-sphere
$A_5$ assembly and (ii) the identification of $\mathrm{ED}/A_5$ with the
keystone Seifert base — both currently open.
