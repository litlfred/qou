<!-- FILE_START: brings-surface-qou-intro.md -->
The preamble establishes that three colors, a Reeb flow, and a $\chi = -6$ ledger force a unique surface. We now define that surface. We begin with Bring's surface (the $S_5$-symmetric quartic-and-quadric in $\mathbb{P}^4$), followed by its geometric realisations and physics interpretations. The central claim is the proposition that Bring's surface is a quantum observable universe. It constructs a QOU 4-tuple and computes the required invariants via the categorical Euler characteristic of $\mathcal{O}_q(\mathrm{SU}(2))$ and the Riemann–Hurwitz count for the canonical map $\Sigma_4 \to \mathbb{P}(V)$.

We conclude by explicitly packaging the QOU 4-tuple $(\mathbf{C}, \varTheta, G, \mathcal{S})$ for downstream use. We then describe the braid-group action on the resolvents. The resolvent variables transform under $B_5$; the $S_5$-invariant combinations selected by that action furnish the color tube coordinates.
<!-- FILE_END: brings-surface-qou-intro.md -->

<!-- FILE_START: brings-surface-def.md -->
Let $R$ be a commutative ring with $30 \in R^{\times}$ (i.e. $\mathrm{char}(R) \nmid 30$). Let $x_j$, $j\in\{0,\dots,4\}$, be homogeneous coordinates on $\mathbb{P}^4_R$. **Bring's surface** is the algebraic variety

$$
  \Sigma_4 =  \mathrm{Proj}\!\left(
    R[x_0,\dots,x_4]\Big/\bigl(\textstyle\sum x_j,
    \textstyle\sum x_j^2, \textstyle\sum x_j^3\bigr)
  \right),
$$

defined by the vanishing of the first three power sums. Over any algebraically closed field $K \supseteq R$, $\Sigma_4$ is a smooth projective curve of genus $4$. Its automorphism group is $\mathrm{Aut}(\Sigma_4) \cong S_5$. It has order $120$, the maximum possible for genus $4$, though below the Hurwitz bound $84(g-1) = 252$. Its Euler characteristic is $\chi(\Sigma_4) = 2 - 2g = -6$.
<!-- FILE_END: brings-surface-def.md -->

<!-- FILE_START: brings-surface-example.md -->
Bring's surface $\Sigma_4$ is the projective curve in $\mathbb{CP}^4$ defined by three equations:

$$
  x_1 + x_2 + x_3 + x_4 + x_5 = 0
$$

$$
  x_1^2 + x_2^2 + x_3^2 + x_4^2 + x_5^2 = 0
$$

$$
  x_1^3 + x_2^3 + x_3^3 + x_4^3 + x_5^3 = 0
$$

This is a smooth curve of genus 4, yielding $\chi = 2 - 2g = 2 - 8 = -6$. Its automorphism group is $S_5$, acting by permutations of the five coordinates.

**Genus 4.** The Euler characteristic $\chi(A) = -6$ is forced by the Yekutieli lifting obstructions. Riemann–Roch for the rank-2 bundle $V$ over the base curve gives $\chi(V) = \deg(V) + \mathrm{rank}(V)(1-g) = 0 + 2(1-g)$. Setting $\chi(V) = -6$ yields $g = 4$.

**Minimality of Bring's surface.** Among all genus-4 curves, Bring's surface is the **terminal object**. It has the largest automorphism group ($S_5$ has order 120), and any other genus-4 QOU maps to it. This establishes the Descartes theorem.

**Concrete coordinates.** Pick the affine patch $x_5 = 1$. Then $x_4 = -(x_1+x_2+x_3+1)$ and the remaining two equations define a curve in $\mathbb{C}^3$. At $(x_1,x_2,x_3,x_4,x_5) = (1, \zeta, \zeta^2, \zeta^3, \zeta^4)$ where $\zeta = e^{2\pi i/5}$, all three power sums vanish.
<!-- FILE_END: brings-surface-example.md -->

<!-- FILE_START: brings-realisations.md -->
Over an archimedean field $K$ (e.g. $\mathbb{Q}$, $\mathbb{R}$, or $\mathbb{C}$), Bring's surface is a compact Riemann surface of genus $4$. The unit circle bundle $M_S$ in $T^*\Sigma_4$ is a CR manifold of hypersurface type (real dimension $3$). It provides the archimedean realisation of the quantum observable universe ([$\mathbb{C}$-quantum universe](#ex:c-quantum-universe)).
<!-- FILE_END: brings-realisations.md -->

<!-- FILE_START: brings-physics-interpretations.md -->
Physics interpretations—lepton generations, chirality, colour—are further realisations of the $S_5$-symmetric structure of Bring's surface. See [Descartes leptons](#rem:archimedean-leptons) in [Chapter 6](#chap:brings-surface).
<!-- FILE_END: brings-physics-interpretations.md -->

<!-- FILE_START: brings-is-qou.md -->
Bring's surface $\Sigma_4$ ([Bring's surface](#def:brings-surface)) determines a quantum observable universe over $R$ (with $30 \in R^{\times}$):

1. *Quantum universe.*  Set $\mathbf{C} = \mathrm{Rep}(\mathrm{SU}_{q}(2))$ over $R$, $A = \mathcal{O}_q(\mathrm{SU}(2))$ with Frobenius form given by the Haar state, and $\tau$ the forgetful functor to $R$-$\mathrm{Mod}$. The differential calculus $\Omega^1(A)$ is the Woronowicz $3$-dimensional calculus.
2. *Observability.* $\mathrm{Hom}(\mathbf{1}, \mathrm{Ad}(A)) = 0$ by the quantum Schur lemma. $\mathrm{SU}_q(2)$ has no non-trivial invariants in the adjoint representation.
3. *Yekutieli lifting.*  The brane tower satisfies the Quantum lifting condition ([Yekutieli lifting](#prop:yekutieli-lifting)). The obstruction classes $\kappa_n \neq 0$ persist at every level by [motivic perpetual obstruction](#conj:motivic-perpetual-obstruction) applied with $\chi(A) = -6$.
4. *Euler characteristic.*  By [QU-to-QOU lifting](#thm:qu-to-qou), $\chi(A) = \mathrm{tr}(\mathrm{id}_A) = 2 - 2g = -6$.
5. *Geometric :refterm[descent]{#descent}* (for $n = 1$, $\dim M_S = 3$):

   $$
     M_S \xrightarrow{ \mathrm{Reeb}} \Sigma_4
     \xrightarrow{\pi} \mathbb{P}(V)
     \xrightarrow{ \mathrm{branch}} \{6 \text{points}\}.
   $$

   The degree-$4$ covering $\pi$ has $6$ branch points with total ramification $R_{\mathrm{tot}} = 14$ (Riemann–Hurwitz). The ramification profile is determined by the $S_5$-symmetry.
<!-- FILE_END: brings-is-qou.md -->

<!-- FILE_START: brings-euler-characteristic.md -->
*The categorical Euler characteristic $\chi(A) = \mathrm{tr}(\mathrm{id}_A)$ for $A = \mathcal{O}_q(\mathrm{SU}(2))$ on Bring's surface $\Sigma_4$ equals*

$$
  \chi(A) = \chi(\Sigma_4) = 2 - 2g(\Sigma_4) = -6.
$$

*This value is recovered as the quantum dimension specialised at the Descartes substrate parameter $q_0$.*
<!-- FILE_END: brings-euler-characteristic.md -->

<!-- FILE_START: brings-riemann-hurwitz.md -->
*The Reeb quotient $M_S \to \Sigma_4$ collapses $\mathrm{U}(1)$-orbits to the weight-$0$ subalgebra $A_0 = A^{\mathrm{U}(1)}$. The canonical covering $\pi \colon \Sigma_4 \to \mathbb{P}(V)$ has degree $4$ with total ramification*

$$
  R_{\mathrm{tot}}
  = 2g(\Sigma_4) - 2 - 4(2g(\mathbb{P}^1) - 2)
  = 14.
$$

*This ramification is distributed by $S_5$-symmetry over exactly $6$ branch points.*
<!-- FILE_END: brings-riemann-hurwitz.md -->

<!-- FILE_START: brings-qou-4tuple.md -->
We construct the archimedean quantum observable universe ([$\mathbb{C}$-quantum observable universe](#ex:c-quantum-observable-universe)) explicitly for Bring's surface. The five homogeneous coordinates $x_j$, $j\in\{0,\dots,4\}$, split into *spacetime* and *color* degrees of freedom:

$$
  \underbrace{x_0, x_1}_{\text{spacetime}}
  \qquad
  \underbrace{x_2, x_3, x_4}_{\text{color}}.
$$

The projective ratio $z = x_0/x_1 \in \mathbb{P}^1(\mathbb{C})$ parametrises the spacetime base.

**1. CR manifold $M_S$.**
Let $S$ denote Bring's surface ([Bring's surface](#def:brings-surface)). Because $S$ is a Riemann surface (real dimension $2$), it does not itself carry a contact form. The CR manifold is the unit circle bundle $M_S = \{(p,\eta) \in T^*S : \lvert\eta\rvert_{g_S} = 1\}$, where $g_S$ is the Fubini–Study metric restricted to $S$. The Liouville $1$-form $\lambda = \eta\,dz$ on $T^*S$ restricts to a contact form $\varTheta = \lambda\big|_{M_S}$, making $M_S$ a $3$-dimensional strictly pseudoconvex CR manifold.

**2. Principal bundle $P$.**
The branched covering $\pi\colon S \to \mathbb{P}^1(\mathbb{C})$ (degree $4$, six branch points) lifts to a principal $\mathrm{SU}(2)$-bundle $P \to M_S$. In the spacetime coordinate $z$, the transition functions of $P$ are the $\mathrm{SU}(2)$ holonomy matrices $H_1,H_2$ around the branch cuts. In the color coordinates $(x_2,x_3,x_4)$, the $S_3$ permutation of the three sheets yields the $\mathrm{SO}(3)$ holonomy representation ([SU(2) generators](#def:su2-generators)–[SO(3) generators](#def:so3-generators)).

**3. State bundle $\mathcal{S}$.**
The associated state bundle is $\mathcal{S} = P \times_G \mathbb{P}^1(\mathbb{C})$. Its fibre at each point of $M_S$ is the color $\mathbb{P}^1(\mathbb{C})$ parametrised by the three roots of the elliptic cubic.

**4. Connection, Levi form, and substrate parameter.**
The instanton connection $A$ on $P$ is expressed in the resolvent basis $(w_1,\dots,w_4)$ ([Lagrange resolvents](#rem:lagrange-resolvents)) as the flat $B_3$-monodromy connection. Its holonomy around the six branch points is generated by the trefoil holonomy matrices. The Levi form on $M_S$ is

$$
  L =  d\varTheta\big|_{H \times H},
  \qquad H = \ker\varTheta \subset TM_S,
$$

where $\varTheta = \eta\,dz\big|_{M_S}$ and the horizontal distribution $H$ is spanned by the lifts of the color differentials $dx_2, dx_3, dx_4$ to $M_S$. The substrate parameter ([substrate parameter](#def:substrate-parameter)) is

$$
  q(p) =  1 + \lvert\langle L_\varTheta, F_A^+ \rangle\rvert(p),
  \qquad p \in M_S.
$$

It couples the color curvature to the contact geometry. At the six branch points (where color sheets merge), $\lVert F_A^+\rVert$ is maximal and $q \to \infty$ (deep-quantum regime). Away from the defects, $q \to 1$ (classicality).

**Summary.**
The $4$-tuple $(\mathbf{C}, \varTheta, G, \mathcal{S})$, with $G = \mathrm{SU}(2)$, constitutes a Descartes universe ($\chi(\mathcal{S}) = -6$) ([Bring's surface](#ex:brings-surface)). Every QOU structure—contact form, Reeb field, Levi form, substrate parameter, $q$-deformed operators—is determined by the spacetime coordinate $z = x_0/x_1$ and the color coordinates $(x_2, x_3, x_4)$.
<!-- FILE_END: brings-qou-4tuple.md -->

<!-- FILE_START: brings-qou-axiom-map.md -->
We record how each axiom of a quantum observable universe ([quantum observable universe](#def:quantum-observable-universe)) is realised on Bring's surface.

**(i) Non-degeneracy.**
The Frobenius form $\int_A = h_q$ is the Haar state on $A = \mathcal{O}_q(\mathrm{SU}(2))$. Faithfulness of $h_q$ for compact quantum groups supplies the isomorphism $A \xrightarrow{ \sim } A^{\vee}$. The antipode $S$ and $h_q$ define the dagger $f^{\dagger} = h_q \circ \mu(S(f) \otimes -)$. This dagger is positive-definite ([positive definite dagger](#prop:positive-definite-dagger)) because the Haar state satisfies $h_q(a^* a) > 0$ for $a \neq 0$.

**(ii) Observability.**
The adjoint representation decomposes as $\mathrm{Ad}(A) \cong V_1 \oplus V_2 \oplus \cdots$ with no spin-$0$ summand. Thus $\mathrm{Hom}(\mathbf{1}, \mathrm{Ad}(A)) = 0$ by the quantum Schur lemma. Geometrically, Bring's surface has no global holomorphic vector field (it has genus $g = 4 > 1$).

**(iii) Categorical volume constraint.**
The fundamental object $V$ of $\mathbf{C} = \mathrm{Rep}(\mathrm{SU}_q(2))$ has categorical dimension $2$. In the archimedean realisation, $V$ is the rank-$2$ defining representation carried by the state bundle fibre $\mathcal{S}_p \cong \mathbb{C}^2$ ([Bring's QOU 4-tuple](#rem:brings-qou-4tuple), item 3). The non-degenerate epimorphism $\epsilon \colon \Lambda^2 V \to \mathbf{1}$ is instantiated by the Levi form $L_\varTheta = -id\varTheta|_{H \times H}$ ([archimedean realisations](#rem:archimedean-realisations)). Because $L_\varTheta$ is alternating and non-degenerate on the rank-$4$ real distribution $H = \ker\varTheta$, it furnishes the symplectic pairing that makes $V$ self-dual. This forces $\det(g_V) = 1$, selecting $\mathrm{SU}(2)$ over $\mathrm{GL}(2)$. In the spectral coordinates ([Lagrange resolvents](#rem:lagrange-resolvents)), this constraint manifests as the Hermitian quadric $w_1 w_4 + w_2 w_3 = 0$, which is the $\mathrm{SL}(2)$ Plucker relation for $\Lambda^2 V$. The top-degree extension to the full color fibre is the spectral volume constraint. See Seiberg–Witten for the explicit symplectic form and its relation to $\epsilon$.
<!-- FILE_END: brings-qou-axiom-map.md -->

<!-- FILE_START: braid-group-action.md -->
The symmetric group $S_5$ acts on Bring's surface ([Bring's curve](#rem:brings-curve)) by permuting $(x_0,\dots,x_4)$. This provides the maximal automorphism group (order $120$) for genus $4$. Three distinguished families of $S_3$ subgroups govern the interplay between the base coordinates $x_j$ and the spectral resolvents $w_k$ ([Lagrange resolvents](#rem:lagrange-resolvents)). We describe each using the braid group ([braid group](#def:braid-group)), the resolvent coordinates, and the $\mathrm{SU}(2)$/$\mathrm{SO}(3)$ matrices of [SU(2) generators](#def:su2-generators)–[SO(3) generators](#def:so3-generators).

**(i) Spacetime action ($\mathbb{P}^1(\mathbb{C})$ base).**
Fix the color coordinates $x_2,x_3,x_4$ as internal fiber degrees of freedom. The constraint $w_0=0$ forces $x_0+x_1=C$ (constant). The spacetime degrees of freedom collapse projectively to the ratio $z=x_0/x_1\in\mathbb{P}^1(\mathbb{C})$. The transposition $x_0\leftrightarrow x_1$ acts as the Mobius involution $z\mapsto 1/z$. This constitutes a $\pi$-rotation on $\mathbb{P}^1(\mathbb{C})$ and embeds into $\mathrm{SU}(2)$ as $\beta=\exp(\pi e_1)$. In the resolvent basis it acts as

```tex
\begin{equation}\label{eq:spacetime-shift}
  w_k \longmapsto 
  w_k+\tfrac{1}{\sqrt{5}}(1-\zeta^k)(x_1-x_0),
  \qquad k=1,\dots,4.
\end{equation}
```

This affine shift fixes the color modes and translates the $\mathbb{P}^1(\mathbb{C})$ fibre.

**(ii) Spectral $S_3$ (trefoil action).**
The frequency-coupled pairs $(w_1,w_4)$ and $(w_2,w_3)$ are permuted by the twist and flip involutions ([braid twist-flip](#def:braid-twist-flip)). The full $S_3$ structure emerges on the projective ratios

$$
  \eta_1=\frac{w_1}{w_2},\qquad\eta_2=\frac{w_3}{w_4}.
$$

$\sigma_1$ inverts both ratios $(\eta_1\mapsto\eta_1^{-1}, \eta_2\mapsto\eta_2^{-1})$, while $\sigma_2$ exchanges them $(\eta_1\mapsto\eta_2^{-1},\eta_2\mapsto\eta_1^{-1})$. The $2$-cycle (reflection) swaps the pairs $(w_1,w_4)\leftrightarrow(w_2,w_3)$. The $3$-cycle (rotation) sends $(\eta_1,\eta_2)\mapsto(\eta_1,\zeta^j\eta_2)$ for $j\in\{1,2,3\}$, permuting the three complex branches of the cubic constraint. The $\mathrm{SU}(2)$ representation assigns the $3$-cycle to $\alpha$ and the reflection to $\beta$. The $\mathrm{SO}(3)$ images act as the holonomy on the spectral energy distribution. $R_\alpha$ rotates the time-like resolvent pair $(\omega_2,\omega_3)$ and $R_\beta$ reflects the space-like axis $\omega_1$.

**(iii) Coordinate $S_3$.**
Fixing any two coordinates (say $x_0,x_1$) as a spacetime base and permuting the remaining three $(x_2,x_3,x_4)$ yields a stabiliser $\mathrm{Stab}(\{x_0,x_1\})\cong S_3\subset S_5$. There are $\binom{5}{2}=10$ such subgroups. In the resolvent basis a permutation $\sigma\in S_3$ of $(x_2,x_3,x_4)$ acts as

```tex
\begin{equation}\label{eq:coord-s3-shift}
  w_k \longmapsto 
  w_k+\tfrac{1}{\sqrt{5}}\sum_{j=2}^{4}
    \bigl(\zeta^{k\sigma(j)}-\zeta^{kj}\bigr)x_j.
\end{equation}
```

The $w_k$ transform as vector fields over the $(x_0,x_1)$ plane. The $S_3$ permutes how these fields couple to the base. The same $\mathrm{SO}(3)$ representation realises this action, now supplying the holonomy group on the internal fibre.

**Geometric $S_3$.**
When Bring's curve is viewed as a branched cover $\mathcal{S}\to\mathbb{P}^1$, a third family of $S_3$ subgroups arises. It permutes the three critical values of the covering map. These three families—spectral, coordinate, and geometric—correspond to the three copies of $S_3$ inside $S_5$ identified in [chirality and trefoil](#rem:chirality-trefoil).
<!-- FILE_END: braid-group-action.md -->

