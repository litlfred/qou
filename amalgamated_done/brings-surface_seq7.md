<!-- FILE_START: spectral-gauge-intro.md -->
With the smooth Bring surface and its cyclotomic reduction established, we construct the gauge data. We define the quaternionic spectral resolvents, tying the resolvent basis $\{\omega_k\}$ to the quaternionic structure on the spectral bundle. We state the algebraic identities these resolvents satisfy and specify the $\mathrm{Sp}(1)$ action that organises their evolution.

We construct the Seiberg–Witten data on this basis. We parametrise the Seiberg–Witten differential by lepton generation. We compute the lepton mass integrals. We then provide the abelianisation required to evaluate those integrals via the nonabelian multiplicative integral on exceptional divisors and the Cartan reduction.

The closing blocks bridge to the subsequent section. We fix the color sectorisation in resolvent variables via coordinates $\mathfrak{r}, \mathfrak{g}, \mathfrak{b}$. We extract the categorical braid action and the knot eigenbasis from the spectral data. We define the Descartes elliptic curve $\mathcal{E}_q$ over the spectral plane, which the Descartes condition pins down via $\chi = -6$.
<!-- FILE_END: spectral-gauge-intro.md -->

<!-- FILE_START: quaternionic-spectral-resolvents.md -->
Let $\mathcal{S}$ denote Bring's surface ([Bring's surface](#def:brings-surface)). Let $q\in\mathbb{C}$ with $0<\lvert q\rvert\le 1$, and set $r=-\ln\lvert q\rvert$ so that $\lvert q\rvert=e^{-r}$. Write $\mathbf{i},\mathbf{j},\mathbf{k}$ for the standard basis of $\mathrm{Im}\mathbb{H}$. Using the Lusztig $q$-exponential and $q$-logarithm,

```tex
\begin{equation}\label{eq:q-exp}
  \exp_q(x)= \sum_{n=0}^{\infty}\frac{x^n}{[n]_q!},
  \qquad
  \ln_q(1+x)= \sum_{n=1}^{\infty}(-1)^{n+1}\frac{x^n}{[n]_q},
\end{equation}
```

we define the **quaternionic spectral resolvents** $\omega_k\colon\mathcal{S}\to J^\infty E$ by

```tex
\begin{align}
  \omega_0 &= 
    \Bigl(\tfrac{1}{\sqrt{5}}\!\sum_{j=0}^{4}x_j\Bigr)
    \ln_q(1+r)
    &&\text{(uncertainty),}
    \label{eq:omega-0}\\[4pt]
  \omega_1 &= 
    \frac{\mathbf{i}}{\ln_q(1+r)}
    \Bigl(\tfrac{1}{\sqrt{5}}\!\sum_{j=0}^{4}\zeta^{j}x_j+i\Bigr)
    &&\text{(space-like),}
    \label{eq:omega-1}\\[4pt]
  \omega_2 &= 
    \mathbf{j}
    \Bigl(\tfrac{1}{\sqrt{5}}\!\sum_{j=0}^{4}\zeta^{2j}x_j+i\Bigr)
    \bigl(\exp_q(r)-1\bigr)
    &&\text{(time-like),}
    \label{eq:omega-2}\\[4pt]
  \omega_3 &= 
    \mathbf{k}
    \Bigl(\tfrac{1}{\sqrt{5}}\!\sum_{j=0}^{4}\zeta^{3j}x_j+i\Bigr)
    \bigl(\exp_q(r)-1\bigr)
    &&\text{(time-like).}
    \label{eq:omega-3}
\end{align}
```

By the first power sum, $\omega_0=0$ in the balanced state. The remaining coordinates embed $\mathcal{S}$ into the infinite jet shell $J^\infty E$ ([jet shell](#rem:jet-shell)).
<!-- FILE_END: quaternionic-spectral-resolvents.md -->

<!-- FILE_START: omega-constraints.md -->
In the spectral resolvent basis ([quaternionic spectral resolvents](#def:quaternionic-spectral-resolvents)), Bring's surface equations enforce three constraints:

- *Barycentric:* $\omega_0=0$.
- *Quadric ($\mathbb{H}$ condition):* $\omega_1\bar{\omega}_1+\omega_2\bar{\omega}_3=0$. This preserves the horizontal self-duality $F_A|_H={*_H}F_A|_H$ ([self-dual curvature](#ex:self-dual-curvature)) and enforces a Minkowski-like balance between space-like and time-like modes.
- *Cubic (phase locking):* a quintic resonance locks the expansion of $\ln_q$ to $\exp_q$. This preserves the $C_5$ symmetry and the Descartes condition $\chi=-6$.
<!-- FILE_END: omega-constraints.md -->

<!-- FILE_START: spectral-dynamics.md -->
The growth profiles of the quaternionic spectral resolvents separate the space-like and time-like sectors of Bring's surface:

- *$\omega_1$ (space-like):* the factor $1/\ln_q(1+r)$ diverges as $r\to 0$. Thus $\omega_1$ achieves infinite density at the base stratum $M_0$, characterising the primordial vortex. This mode anchors the $U(1)$ longitudinal backbone of the $\mathrm{SU}(2)$ bundle.
- *$\omega_2,\omega_3$ (time-like):* the factor $\exp_q(r)-1$ vanishes at $r=0$ and grows rapidly for small $r$, driven by the $q$-deformed Reeb flow ([$q$-Reeb flow](#ex:q-reeb-flow)). These ladder modes expand at the big bang before tapering as the geometric viscosity ([$q$-harmonic physical interpretation](#rem:q-harmonic-physical)) takes hold.

We embed the radial parameter into $\mathrm{Sp}(1)$ via the unit quaternion to realise the rotation as a function of $r$:

```tex
\begin{equation}\label{eq:sp1-quaternion}
  \mathbf{q}(r)
  = 
  \cos_q\!\varTheta(r)+\mathbf{u}\sin_q\!\varTheta(r),
  \qquad
  \varTheta(r)=\tfrac{\pi}{2}e^{-r}.
\end{equation}
```

Here $\cos_q$ and $\sin_q$ are the $q$-deformed trigonometric functions built from $\exp_q$:

$$
  \cos_q(x)=\frac{\exp_q(ix)+\exp_q(-ix)}{2},
  \qquad
  \sin_q(x)=\frac{\exp_q(ix)-\exp_q(-ix)}{2i}.
$$

The element $\mathbf{u}\in\mathrm{Im}\mathbb{H}$ is a fixed unit imaginary quaternion. The conjugation $\boldsymbol{\omega}'=\mathbf{q}(r)\boldsymbol{\omega}\mathbf{q}(r)^{*}$ supplies maximum twist ($\varTheta=\pi/2$) in the deep-quantum regime $r\to 0$ and a classical freeze ($\varTheta\to 0$) as $r\to\infty$.
<!-- FILE_END: spectral-dynamics.md -->

<!-- FILE_START: mi-sw-abelianisation.md -->
Let $\mathcal{S}_c \cong \mathbb{P}^1(\mathbb{C})$ be the exceptional divisor at a branch point $z_c$ ([Bring's surface smoothness](#rem:brings-smoothness)), and let $(\nabla_A q, L \wedge F^+)$ be the connection--curvature pair of the ([mass identity](#def:mass-identity)). For each vertical degree $n \geq 0$ in the Reeb decomposition, the restriction of the nonabelian multiplicative integral to $\mathcal{S}_c$ abelianises to the $n$-th prolonged Seiberg--Witten period:

```tex
\begin{equation}\label{eq:mi-sw-abelianisation}
  \bigl\lVert
  \mathrm{MI}\!\!\int_{\mathcal{S}_c}
  \bigl(\nabla_A q, L \wedge F^+\bigr)
  \bigr\rVert_{J^n}
  = 
  \bigl\lvert a_D^{(n)}\bigr\rvert
  = 
  \biggl\lvert\oint_{\mathcal{S}_c}\lambda_{\mathrm{SW}}^{(n)}\biggr\rvert,
\end{equation}
```

where $\lVert\cdot\rVert_{J^n}$ denotes the Killing-form norm projected onto the $n$-th jet component, and $\lambda_{\mathrm{SW}}^{(n)}$ is the $n$-th prolonged Seiberg--Witten differential.

**Archimedean specialisation (§7c).** This block sits on the archimedean side of the substrate wall. It invokes real- or complex-analytic constructs—real-valued physical observables, real-analytic bounds, transcendental constants, or numerical evaluation at the substrate parameter $q_0$. The generic categorical/$q$-deformation identities it relies upon remain valid over an abstract coefficient ring; only their archimedean realisation is specialised here.
<!-- FILE_END: mi-sw-abelianisation.md -->

<!-- FILE_START: mi-sw-abelianisation-cartan.md -->
**Lemma (Cartan reduction recovers the Seiberg--Witten differential).**
Let $\mathcal{S}_c \cong \mathbb{P}^1(\mathbb{C})$ be the exceptional divisor at a branch point $z_c$ ([Bring's surface smoothness](#rem:brings-smoothness)). Let $\nabla_A$ be the $\mathrm{SU}(2)$-connection of the mass identity restricted to $\mathcal{S}_c$. Then:

1. The principal $\mathrm{SU}(2)$-bundle trivialises over $\mathcal{S}_c$ (because $\pi_1(\mathrm{SU}(2)) = 0$ classifies every $\mathrm{SU}(2)$-bundle over $S^2$). Thus $\nabla_A$ reduces to an $\mathfrak{su}(2)$-valued $1$-form $A|_{\mathcal{S}_c}$.
2. Under the weight-space decomposition ([weight space decomposition](#rem:weight-space-decomposition)), the restriction splits as

   $$
     A\big|_{\mathcal{S}_c}
       = A^0 \otimes H
       + A^+ \otimes E_+
       + A^- \otimes E_-,
   $$

   with $H, E_\pm$ the standard generators of $\mathfrak{su}(2)$ and $A^0$ a $\mathrm{U}(1)$-valued $1$-form.
3. The Cartan component provides the Seiberg--Witten differential:

   $$
     A^0 = X\, dz = \lambda_{\mathrm{SW}}.
   $$

   Here $X$ is the color coordinate cut out as the Higgs-field eigenvalue on the single sheet to which the spectral curve ([color bundles](#rem:color-bundles)) restricts over $\mathcal{S}_c$.
<!-- FILE_END: mi-sw-abelianisation-cartan.md -->

<!-- FILE_START: sw-period-residue-sum.md -->
Let $\mathcal{S}_c \cong \mathbb{P}^1(\mathbb{C})$ be the exceptional divisor at a branch point $z_c$ ([Bring's surface smoothness](#rem:brings-smoothness)). Let $\lambda_{\mathrm{SW}}^{(n)}$ be the $n$-th prolonged Seiberg--Witten differential of the [MI--SW abelianisation](#prop:mi-sw-abelianisation). Because $\lambda_{\mathrm{SW}}^{(n)}$ is a meromorphic $1$-form on the compact Riemann surface $\mathcal{S}_c$, possessing poles only at the branch points, its period equals the sum of its residues:

$$
\oint_{\mathcal{S}_c}\lambda_{\mathrm{SW}}^{(n)}
\;=\;
2\pi i \sum_{p\,\in\,\mathcal{S}_c}\operatorname{Res}_p\,\lambda_{\mathrm{SW}}^{(n)}.
$$

In particular, the prolonged Seiberg--Witten period $a_D^{(n)} = \oint_{\mathcal{S}_c}\lambda_{\mathrm{SW}}^{(n)}$ functions as an **algebraic residue sum**. We evaluate it by collecting the local residues at the branch-point poles; no contour integration is required.

**Residue support and body order.** The branch-point poles support the residues. The vertical (jet) degree $n$ governs the number of contributing poles. The $n$-th prolongation lifts the connection to the $n$-jet bundle $J^n E$, so the weight data of rank $n$ indexes the residue family at level $n$. The residue sum therefore carries the **body-order grading**. The period at vertical degree $n$ yields the $n$-body contribution. Each residue constitutes a per-block quantum-dimensional weight on the Wedderburn decomposition restricted to that level.
<!-- FILE_END: sw-period-residue-sum.md -->

<!-- FILE_START: jet-sw-tau-decomposition.md -->
**Proposition (jet decomposition of the Archimedean functor).**

Let $\tau$ be the Archimedean realisation functor (step 9 of the canonical chain). Applied to the surface-ordered multiplicative integral of the mass-identity connection--curvature pair over the exceptional divisor $\mathcal{S}_c$, it decomposes as the sum over vertical (jet) degrees of the prolonged Seiberg--Witten periods:

$$
\tau\!\left(\mathrm{MI}\!\!\int_{\mathcal{S}_c}\bigl(\nabla_A q,\,L\wedge F^+\bigr)\right)
\;=\;
\sum_{n\geq 0} a_D^{(n)}
\;=\;
\sum_{n\geq 0}\oint_{\mathcal{S}_c}\lambda_{\mathrm{SW}}^{(n)}.
$$

The $n=0$ term is the electron period $a_D^{(e)}$. Each higher term is the $n$-th prolonged period of [`prop:mi-sw-abelianisation`](#prop:mi-sw-abelianisation), which [`prop:sw-period-residue-sum`](#prop:sw-period-residue-sum) identifies as an algebraic residue sum. Consequently, the Seiberg--Witten differential **is the jet-graded decomposition of the Archimedean functor**. The functor $\tau$ observes the entire prolongation tower simultaneously, and the vertical (jet/body) order $n$ indexes its graded pieces. This provides the structural counterpart, on the realisation side, of the "observe last" principle. The jet tower travels intact through the filtration, and $\tau$ collapses it to the graded sum only at observation.
<!-- FILE_END: jet-sw-tau-decomposition.md -->

<!-- FILE_START: color-sector-coords.md -->
With notation as in [exceptional divisor](#def:exceptional-divisor), fix the substrate parameter $q$ ([substrate parameter](#def:substrate-parameter)) and set $\phi \in [0,\pi]$, $\psi \in [0, 2\pi/3]$. We define the **red**, **green**, and **blue** sector embeddings by

```tex
\begin{align*}
  \mathfrak{r}(\phi,\psi)
  &=  O + R\bigl(\sin\phi \bigl(\cos(\psi + q\phi) T_1
         + \sin(\psi + q\phi) T_2\bigr) - \cos\phi N\bigr),\\
  \mathfrak{g}(\phi,\psi)
  &=  \mathfrak{r}\!\bigl(\phi,\psi + \tfrac{2\pi}{3}\bigr),\\
  \mathfrak{b}(\phi,\psi)
  &=  \mathfrak{r}\!\bigl(\phi,\psi + \tfrac{4\pi}{3}\bigr).
\end{align*}
```

The *color twist* $q\phi$ rotates each sector by $q$ full turns as the latitude $\phi$ runs from the south pole ($0$) to the north pole ($\pi$). This encodes the chirality of the substrate parameter.

The three sectors tile the exceptional divisor precisely:

$$
  \mathcal{S}_p =  \mathfrak{r}(p) \cup \mathfrak{g}(p) \cup \mathfrak{b}(p).
$$

Adjacent sectors share only their boundary meridians (at $\psi = 0$ and $\psi = 2\pi/3$ in each sector's local coordinate). The union covers $\mathcal{S}_p$ without overlap. The three sectors correspond to the three copies of $S_3 \subset S_5$ in [chirality and trefoil](#rem:chirality-trefoil): $\mathfrak{r}$ constitutes the first, $\mathfrak{g}$ the second, and $\mathfrak{b}$ the third.
<!-- FILE_END: color-sector-coords.md -->

<!-- FILE_START: descartes-braid-structure.md -->
Let $(\mathbf{C}, A, \tau)$ be a Descartes universe ([Descartes condition](#def:archimedean-condition)). Then:

1. The braiding of $\mathbf{C} = \mathrm{Rep}(\mathrm{SU}_q(2))$ induces a faithful representation $\rho_3\colon B_3 \to \mathrm{Aut}_{\mathbf{C}}(V^{\otimes 3})$ on the fundamental representation $V$ ([braid action on tensor products](#prop:braid-action-tensor)).
2. The image of $\rho_3$ in $\mathrm{SU}(2)$ (via the fibre functor $\tau$) is the binary dihedral group $\mathrm{Dic}_3$ of order $12$ ([SU(2) generators](#def:su2-generators)).
3. The composite $B_3 \xrightarrow{\rho_3} \mathrm{Dic}_3 \twoheadrightarrow S_3$ recovers the three copies of $S_3$ inside $S_5 = \mathrm{Aut}(\Sigma_4)$ ([chirality and trefoil](#rem:chirality-trefoil)), mapping one to each colour sector.
4. This structure holds over any base ring $R$ with $30 \in R^{\times}$. It applies directly to the $\mathfrak{p}$-adic realisation ([$p$-adic realisation](#ex:p-adic-realisation)), where knot complements and skein relations remain unavailable.
<!-- FILE_END: descartes-braid-structure.md -->

<!-- FILE_START: descartes-knot-eigenbasis.md -->
Let $(\mathbf{C}, A, \tau)$ be a Descartes universe ([Descartes condition](#def:archimedean-condition)) with $\mathbf{C} = \mathrm{Rep}(\mathrm{SU}_q(2))$ and $V$ the fundamental representation. The knot-type eigenbasis is complete:

1. **(Iwahori--Hecke algebra instantiation.)** The Descartes condition forces $\chi(A) = -6$. This sets the genus $g = 4$ and gauge group $\mathrm{SU}_q(2)$ to rank $2$. The $R$-matrix of $\mathcal{U}_q(\mathfrak{su}(2))$ ([$R$-matrix braiding](#rem:r-matrix-braiding)) supplies a braiding $c_{V,V}$ on $\mathbf{C}$ with eigenvalues $q$ and $-q^{-1}$. The quotient by the quadratic relation $(c_{V,V} - q)(c_{V,V} + q^{-1}) = 0$ yields the Iwahori--Hecke algebra $H_n(q)$ acting on $V^{\otimes n}$.
2. **(Schur--Weyl decomposition.)** The Descartes condition demands $q$ not be a root of unity (via $6 \in R^{\times}$ and non-degeneracy of the Frobenius form). Consequently, $H_n(q)$ is semisimple (Jimbo's theorem). The $q$-Schur--Weyl decomposition ([knot eigenbasis completeness](#prop:knot-eigenbasis-complete)(1)) applies: every $V^{\otimes n}$ decomposes into irreducible summands labelled by two-part partitions $\lambda \vdash n$.
3. **(Braid representation.)** The faithful representation $\rho_3 \colon B_3 \to \mathrm{Aut}_{\mathbf{C}}(V^{\otimes 3})$ ([braid-group structure](#cor:descartes-braid-structure)(1)) extends to $\rho_n \colon B_n \to \mathrm{Aut}_{\mathbf{C}}(V^{\otimes n})$ for all $n$ via [braid action on tensor products](#prop:braid-action-tensor). The Markov trace on the Iwahori--Hecke algebra tower detects every irreducible summand.
4. **(Completeness.)** By the combining theorem ([knot eigenbasis completeness](#prop:knot-eigenbasis-complete)), the three inputs—Schur--Weyl decomposition, Alexander surjectivity, and Markov trace detection—yield a complete knot-type eigenbasis for the algebraic direct limit $V_{\mathrm{phys}} = \varinjlim V^{\otimes n}$. A finite categorical trace over knot-labelled summands replaces the Feynman path integral.
<!-- FILE_END: descartes-knot-eigenbasis.md -->

<!-- FILE_START: descartes-elliptic-curve.md -->
**Proposition.**
Let $(\mathbf{C}, A, \tau)$ be the Descartes universe with $\chi(A) = -6$ and substrate parameter $q$. Set $s = \sqrt{q}$. The color elliptic fiber ([color elliptic](#prop:color-elliptic)) of Bring's surface at spacetime ratio $z = s - s^{-1}$ is the elliptic curve

$$
  \mathcal{E}_q  : 
  y^2 =  x^3
  +  \frac{2s^4 + s^3 - 2s^2 - s + 2}{3s^2}x
  +  \frac{5(s^2 + s - 1)(4s^4 - s^3 - 4s^2 + s + 4)}{27s^3}
$$

with Weierstrass coefficients expressible directly in $q$:

$$
  p(q) = 
  \frac{2(q^2 - q + 1)}{3q}
  +  \frac{q - 1}{3\sqrt{q}},
$$

$$
  r(q) = 
  \frac{20(q - 1)^3}{27q^{3/2}}
  +  \frac{5(q - 1)^2}{9q}
  +  \frac{5(\sqrt{q} - 1/\sqrt{q})}{9}
  +  \frac{20}{27}.
$$
<!-- FILE_END: descartes-elliptic-curve.md -->

<!-- FILE_START: descartes-elliptic-invariants.md -->
**Remark (interpretation).**

**Invariants.**

| Quantity | Formula | Value at the substrate parameter $q$ |
|----------|---------|---------------------|
| Discriminant | $\Delta(q)$ | $-18.95$ |
| $j$-invariant | $j(q) = 256(2z^2 + z + 2)^3 / \Delta$ | $129.9$ |
| Real components | $1$ (since $\Delta < 0$) | |
| 2-torsion | one real point at $x_T = -p(q)/3 - \cdots$ | $x_T = -0.684$ |

**Classical limit.**
At $q = 1$ (equivalently $s = 1$, $z = 0$), the curve degenerates to

$$
  E_1  :  y^2 = x^3 + \tfrac{2}{3}x + \tfrac{20}{27},
  \qquad \Delta = -16, \quad j = 128.
$$

Clearing denominators ($X = 3x$, $Y = 3\sqrt{3}y$) yields the integral model $Y^2 = X^3 + 18X + 60$ with $\Delta = -2^4 \cdot 3^5 \cdot 31$. The factor $31$ reflects the arithmetic of the quintic resolvent underlying Bring's surface.
<!-- FILE_END: descartes-elliptic-invariants.md -->

<!-- FILE_START: golden-ratio-degeneration-brings.md -->
**Remark (interpretation).**

**Golden ratio degeneration.**
The second Weierstrass coefficient $r(q)$ contains the factor $(s^2 + s - 1)$ in its numerator. This vanishes at $s = (\sqrt{5} - 1)/2 = 1/\varphi$, the reciprocal of the golden ratio $\varphi = (1 + \sqrt{5})/2$. At this value $q = 1/\varphi^2 = (3 - \sqrt{5})/2 \approx 0.382$, the curve $\mathcal{E}_q$ acquires a cusp. The elliptic fiber degenerates and the color fibration becomes singular.
<!-- FILE_END: golden-ratio-degeneration-brings.md -->

<!-- FILE_START: descartes-elliptic-curve-interpretation.md -->
**Remark (interpretation).**

This identifies the **sub-classical regime** $q < 1$. Here, the substrate parameter reverses its role; the quantum deformation acts in the opposite direction. The golden ratio threshold $q = 1/\varphi^2$ marks the boundary beyond which the Descartes universe cannot support stable color structure.

**$q$-Dependence of the stability structure.**
As $q$ varies from $1$ to $\infty$:

| Regime | $q$ | $j(\mathcal{E}_q)$ | Physics |
|--------|-----|----------|---------|
| Classical | $q = 1$ | $128$ | No crossing asymmetry; $E_1$ is smooth |
| Sub-golden | $q < 1/\varphi^2$ | undefined | $\mathcal{E}_q$ singular; no stable color fibers |
| Golden threshold | $q = 1/\varphi^2$ | $\to \infty$ | Cusp; color degeneration |
| Physical | the substrate $q$ | $129.9$ | Our universe; $\mathcal{E}_q$ smooth with $\Delta < 0$ |
| Deep quantum | $q \to \infty$ | $\to 0$ | $j \to 0$; curve approaches CM curve |
<!-- FILE_END: descartes-elliptic-curve-interpretation.md -->
