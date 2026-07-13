<!-- FILE_START: archimedean-condition-intro.md -->
The Descartes elliptic curve $\mathcal{E}_q$ names a structure. The Descartes condition selects its Euler characteristic. We explain the descent of the spectral data to a zero-dimensional locus. We state the condition $\chi(A) = -6$ on the algebraic substrate. The derivation chain illustrates how three colors, Reeb flow, and Calabi–Yau compatibility force this single value. We record concrete instances and the one-dimensional descent. We then compute the resulting genus.

The lepton spectrum follows directly. We identify the lepton families with Reeb-orientation strata on Bring's curve and their chirality assignments with trefoil subgroups. 

The remaining blocks assemble the knot-particle generator set. The combinatorial structural fact holds: only finitely many torus knots embed in Bring's surface. We build the genus filtration that identifies the generator set. The formal coordinates and $d_q^2$ obstruction supply the interpretive bridge to the substrate side.

We close the section by proving generation completeness: the embeddable torus knots generate the chapter's particle spectrum exactly. This result underpins the next section, where we isolate the simplest particle: the unit defect at $z = 1$.
<!-- FILE_END: archimedean-condition-intro.md -->

<!-- FILE_START: descent-to-zero.md -->
By the :refterm[descent]{#descent} theorem ([Descartes universe](#thm:descartes)), we may restrict our study to dimension-zero manifolds equipped with bundles $P$ and $\mathcal{S}$. At a point $p\in M_0$, the substrate parameter $q(p)= 1 + \lvert\langle L_\varTheta, F_A^{+}\rangle\rvert(p)$ ([substrate parameter](#def:substrate-parameter)) assigns a specific quantum constant $q\in[1,\infty)$ determined by $P$ and $\mathcal{S}$. Here $\mathcal{S}$ represents the totality of fermionic matter packed into the fibre at $p$. The trivial bundle $\mathcal{S}=\mathcal{S}_0$ corresponds to empty space, where every point's location is exactly known. A non-trivial bundle $\mathcal{S}$ fills spacetime with fermions, entering the regime of the quantum Bring's surface whose underlying geometry is non-commutative ([Section](#sec:quantum-brings)).
<!-- FILE_END: descent-to-zero.md -->

<!-- FILE_START: archimedean-condition.md -->
A quantum observable universe $(\mathbf{C}, A, \tau)$ over $R$ ([quantum observable universe](#def:quantum-observable-universe), [QU-to-QOU lifting](#thm:qu-to-qou)) satisfies the **Descartes condition** if the categorical Euler characteristic takes the value

$$
  \chi(A) =  \mathrm{tr}(\mathrm{id}_A) =  -6  \in  R.
$$

This requires $6 \in R^{\times}$ (i.e. $\mathrm{char}(R) \nmid 6$). The class $[A] \in K_0(\mathbf{C})$ has rank $-6$. By [QU-to-QOU lifting](#thm:qu-to-qou)(3--4), this forces $\kappa_n \neq 0$ for all $n$ and produces $6$ branch points in the geometric :refterm[descent]{#descent} (with total ramification $R_{\mathrm{tot}} = 2d + 6$). We call a quantum observable universe satisfying this condition a *Descartes universe*.
<!-- FILE_END: archimedean-condition.md -->

<!-- FILE_START: chi-minus-six-chain.md -->
The value $\chi(A) = -6$ is derived, not assumed. We present the complete chain.

**Step 1: Start with the QOU triple.** We have $(\mathbf{C}, A, \tau)$ with gauge group $G = \mathrm{SU}(2)$. The object $A$ is the fundamental representation, and $\tau$ is the fibre functor.

**Step 2: The fibre functor produces a rank-2 bundle.** The fibre functor $\tau$ maps $A$ to a rank-2 vector bundle $V$ over a compact Riemann surface $M_0$. Since $G = \mathrm{SU}(2)$, the determinant $\det(V)$ is trivial. Thus $\deg(V) = 0$.

**Step 3: Apply Riemann--Roch.** For a rank-$r$ bundle of degree $d$ over a genus-$g$ surface:

$$
  \chi(V) = d + r(1 - g) = 0 + 2(1 - g) = 2 - 2g
$$

**Step 4: Yekutieli obstructions require $g \geq 1$.** The Yekutieli lifting obstructions require $\kappa_n \neq 0$ at every level of the brane tower. The obstruction classes lie in $H^2(M_0, B)$. For these to be non-trivial, we need $H^2(M_0, \mathbb{C}^*) \neq 0$, which requires $g \geq 1$.

**Step 5: The Frobenius--Hopf structure fixes 6 branch points.** The Frobenius--Hopf structure forces the algebra to have exactly 6 branch points in its geometric :refterm[descent]{#descent} (from the $S_3 \subset S_5$ orbits on the 6 Weierstrass points of Bring's surface). This fixes $|\chi(A)| = 6$.

**Step 6: The sign is negative.** The bundle has more obstructions than sections. Specifically, $\chi(V) = -6$ means $h^0(V) - h^1(V) = -6$, so $h^1(V) \geq 6$ (obstructions dominate).

**Step 7: Therefore $g = 4$.** From $\chi(V) = 2 - 2g = -6$, we obtain $g = 4$. The unique maximally symmetric genus-4 curve is Bring's surface $\Sigma_4$, with automorphism group $S_5$ of order 120.

**Step 8 (motivic-Galois reading).** *Steps 4 and 5 lift to a single algebraic statement at the level of the [motivic substrate](#def:motivic-substrate). The condition $\chi(A) = -6$ controls the value of the substrate's motivic $L$-function at the boundary of analytic continuation. The Yekutieli non-vanishing $\kappa_n \neq 0$ at every level becomes the non-vanishing of the Frobenius character at every finite place $p \nmid 6$. This is the content of [motivic perpetual obstruction](#conj:motivic-perpetual-obstruction) applied with $\chi(A) = -6$ ([Kummer tower](#rem:kummer-tower) §motivic-Galois). The "$g \geq 1$" condition (Step 4) is the cyclotomic-place criterion $H^1_{\mathrm{Gal}}(\mathrm{Gal}(\bar{\mathbb{Q}}_p/\mathbb{Q}_p), \mu_n(1)) \neq 0$, realised at every $p$. The Riemann–Roch derivation is the archimedean shadow ($v = \infty$ realization) of this stronger adelic statement.*
<!-- FILE_END: chi-minus-six-chain.md -->

<!-- FILE_START: archimedean-calabi-yau.md -->
The constraint $\chi(\mathcal{S}) = -6$ specialises to each archimedean example:

- *Calabi--Yau* ([Calabi--Yau](#ex:calabi-yau)): constrains the alternating sum of Betti numbers. Only manifolds admitting a principal $\mathrm{SU}(2)$-bundle with this Euler characteristic realise the Descartes universe.
- *ALE links* ([ALE space](#ex:ale)): selects finite subgroups $\Gamma \subset \mathrm{SU}(2)$ via arithmetic constraints on the McKay quiver.
- *Affine space* $M = \mathbb{C}^2$: forces non-trivial bundle topology. The $q$-harmonic zero-modes of $\Delta_q$ reproduce the CMB thermal spectrum in the $q \to 1$ regime.
<!-- FILE_END: archimedean-calabi-yau.md -->

<!-- FILE_START: descent-one-dim.md -->
By the :refterm[descent]{#descent} theorem ([jet prolongation](#prop:jet-prolongation)), a two-complex-dimensional Descartes universe $(\mathbf{C}, \varTheta, G, \mathcal{S})$ with $M = \mathbb{C}^2$ descends to a one-complex-dimensional variety $M_0$. The stability of the Euler characteristic under :refterm[descent]{#descent} and lifting ([Euler characteristic stability](#prop:euler-char-stability)) ensures that the descended universe retains $\chi(\mathcal{S}) = -6$. We may therefore study the Descartes universe using one-complex-dimensional varieties. The :refterm[descent]{#descent} may continue to dimension zero ([:refterm[descent]{#descent} reduction to zero](#rem:descent-reduction-zero)), where fibre data at a single point captures the entire quantum observable universe.
<!-- FILE_END: descent-one-dim.md -->

<!-- FILE_START: genus-maximal-descent.md -->
Let $(\mathbf{C}, A, \tau)$ be a quantum observable universe satisfying the Descartes condition $\chi(A) = -6$ ([Descartes condition](#def:archimedean-condition)). If the geometric :refterm[descent]{#descent} produces a compact one-complex-dimensional base $M_0$, then $M_0$ is a Riemann surface of genus $g = 4$.

More precisely: the categorical Euler characteristic $\mathrm{tr}(\mathrm{id}_A) = -6$ determines the topological type of the base curve. Under the fibre functor $\tau$ of any archimedean realisation, Riemann--Roch on $M_0$ forces $2(1 - g) = -6$, hence $g = 4$. This is the maximal genus consistent with the Hurwitz bound $|\mathrm{Aut}(\Sigma)| \leq 84(g - 1) = 252$.
<!-- FILE_END: genus-maximal-descent.md -->
