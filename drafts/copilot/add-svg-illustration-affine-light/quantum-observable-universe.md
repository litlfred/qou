---
abstract: |
  This paper presents a mathematical framework for the Quantum Observable Universe (QOU). We introduce the notion of quantum torsion in this setting, study its lifting to higher categorical structures, and examine the resulting interpretational and experimental consequences. Speculative extensions are discussed in the final chapter.
author:
- Frederick Carl Leitner[^1]
bibliography:
- references.bib
date: 2026-03-14
title: Quantum Observable Universe
---

<div class="center">

  
This work is licensed under a [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/).  
You are free to share and adapt this material for any purpose,  
provided appropriate credit is given, a link to the license is provided,  
and any changes made are indicated.

</div>

# Quantum Observable Universe

<div id="def:c-quantum-universe" class="definition">

**Definition 1.1** ($\mathbb{C}$ Quantum Universe). *A *$\mathbb{C}$ quantum universe* is a triple $(M, G, E)$ where:*

1.  *$M$ is a CR manifold;*

2.  *$G = \mathrm{SU}(2)$;*

3.  *$E \to M$ is a principal $G$-bundle (called the *bulk*) with fibres $\mathbb{CP}$ and $\mathrm{SO}(3)$ holonomy.*

</div>

<div id="def:c-quantum-observable-universe" class="definition">

**Definition 1.2** ($\mathbb{C}$ Quantum Observable Universe). *A *$\mathbb{C}$ quantum observable universe* is a $\mathbb{C}$ quantum universe $(M, G, E)$ (Definition <a href="#def:c-quantum-universe" data-reference-type="ref" data-reference="def:c-quantum-universe">1.1</a>) that satisfies the following compactly supported cohomology conditions: $$H^0_c(M, \mathrm{Ad}(E)) = 0
  \qquad\text{and}\qquad
  H^0_c(M, E) = 0.$$*

</div>

<div id="rem:jet-bundle" class="remark">

**Remark 1.3** (Jet-bundle formulation). *The conditions in Definition <a href="#def:c-quantum-observable-universe" data-reference-type="ref" data-reference="def:c-quantum-observable-universe">1.2</a> admit a natural reformulation in terms of the first jet bundle $J^1 E$. The vanishing $H^0_c(M, E) = 0$ ensures that no non-trivial compactly supported section of $E$ exists, while $H^0_c(M, \mathrm{Ad}(E)) = 0$ eliminates compactly supported infinitesimal gauge symmetries. Together, these conditions mean that the space of sections of $J^1 E$ with compact support injects into the space of connections, preventing any local degeneracy of the gauge field.*

</div>

<div id="lem:unique-connection" class="lemma">

**Lemma 1.4** (Uniqueness of the connection). *Let $(M, G, E)$ be a $\mathbb{C}$ quantum observable universe. Then the vanishing conditions $$H^0_c(M, \mathrm{Ad}(E)) = 0
  \qquad\text{and}\qquad
  H^0_c(M, E) = 0$$ imply that the connection $A$ on $E$ is unique up to gauge equivalence.*

</div>

<div class="proof">

*Proof.* ◻

</div>

<div id="prop:self-dual-curvature" class="proposition">

**Proposition 1.5** (Self-duality of the curvature). *Let $(M, G, E)$ be a $\mathbb{C}$ quantum observable universe with connection $A$. Then the curvature $F_A$ is self-dual, i.e. $$F_A = {*}\, F_A.$$*

</div>

<div class="proof">

*Proof.* ◻

</div>

<div id="ex:calabi-yau" class="example">

**Example 1.6** (Calabi–Yau manifolds). *Let $M$ be a Calabi–Yau manifold. The Ricci-flat Kähler metric on $M$ endows it with a natural CR structure, and the trivial $\mathrm{SU}(2)$-bundle $E = M \times \mathrm{SU}(2)$ yields a $\mathbb{C}$ quantum observable universe when the compactly supported cohomology conditions of Definition <a href="#def:c-quantum-observable-universe" data-reference-type="ref" data-reference="def:c-quantum-observable-universe">1.2</a> are satisfied.*

</div>

<div id="ex:ale" class="example">

**Example 1.7** (ALE spaces). *Let $M$ be an asymptotically locally Euclidean (ALE) space. ALE spaces arise as minimal resolutions of quotient singularities $\mathbb{C}^2 / \Gamma$ for finite subgroups $\Gamma \subset \mathrm{SU}(2)$. Equipped with a hyper-Kähler metric and the corresponding principal $\mathrm{SU}(2)$-bundle, $M$ provides a $\mathbb{C}$ quantum observable universe satisfying self-dual curvature (Proposition <a href="#prop:self-dual-curvature" data-reference-type="ref" data-reference="prop:self-dual-curvature">1.5</a>).*

</div>

<div id="ex:affine" class="example">

**Example 1.8** ($n$-dimensional affine space). *Let $M = \mathbb{C}^n$ with the standard CR structure inherited from its embedding in $\mathbb{C}^n$. The trivial principal $\mathrm{SU}(2)$-bundle $E = \mathbb{C}^n \times \mathrm{SU}(2)$ admits a flat instanton connection satisfying the self-duality condition (Proposition <a href="#prop:self-dual-curvature" data-reference-type="ref" data-reference="prop:self-dual-curvature">1.5</a>). When the compactly supported cohomology conditions of Definition <a href="#def:c-quantum-observable-universe" data-reference-type="ref" data-reference="def:c-quantum-observable-universe">1.2</a> hold, $(\mathbb{C}^n, G, E)$ is a $\mathbb{C}$ quantum observable universe. For $n = 2$, this recovers the two-dimensional affine example $M = \mathbb{C}^2$.*

</div>

<div id="def:substrate-parameter" class="definition">

**Definition 1.9** (Substrate parameter). *Let $(M, G, E)$ be a $\mathbb{C}$ quantum observable universe with connection $A$. Write $F_A = dA + A \wedge A$ for the curvature and let $F_A^+$ denote its self-dual part. Let $L \in \Gamma(T^*M \otimes \overline{T^*M})$ be the *Levi form*, a Hermitian form on the tangent bundle of $M$. The *substrate parameter* is the function $q \colon M \to \mathbb{R}$ defined by $$q(p) \;=\; \exp\!\bigl(-\lVert L \wedge F_A^+ \rVert(p)\bigr),
  \qquad p \in M.$$*

</div>

<div id="def:quantum-gauge-group" class="definition">

**Definition 1.10** (Quantum Gauge Group). *Let $(M, G, E)$ be a $\mathbb{C}$ quantum observable universe with substrate parameter $q$ (Definition <a href="#def:substrate-parameter" data-reference-type="ref" data-reference="def:substrate-parameter">1.9</a>). The *quantum gauge group* is the quantum group $\mathrm{SU}_q(2)$ obtained by deforming the structure group $G = \mathrm{SU}(2)$ at the parameter $q$.*

</div>

<div id="def:quantum-planck-constant" class="definition">

**Definition 1.11** (Quantum Planck Constant). *Let $(M, G, E)$ be a $\mathbb{C}$ quantum observable universe with substrate parameter $q$ (Definition <a href="#def:substrate-parameter" data-reference-type="ref" data-reference="def:substrate-parameter">1.9</a>). The *quantum Planck constant* is the function $\hbar_q \colon M \to \mathbb{R}$ defined by $$\hbar_q(p) \;=\; 1 - q(p), \qquad p \in M.$$ As $q(p) \to 1$ (classicality), $\hbar_q(p) \to 0$ and quantum effects vanish; as $q(p) \to 0$ (deep-quantum regime), $\hbar_q(p) \to 1$.*

</div>

<div id="rem:j1e-local-states" class="remark">

**Remark 1.12** ($J^1E$ as the space of local states). *The jet bundle $J^1 E$ serves as the space of local states of the $\mathbb{C}$ quantum observable universe. The classical gauge dynamics, encoded by the *instanton connection* $A$ (Lemma <a href="#lem:unique-connection" data-reference-type="ref" data-reference="lem:unique-connection">1.4</a>), are weighted by the substrate parameter $q$ (Definition <a href="#def:substrate-parameter" data-reference-type="ref" data-reference="def:substrate-parameter">1.9</a>) to define the quantum field algebra $\mathrm{SU}_q(2)$ (Definition <a href="#def:quantum-gauge-group" data-reference-type="ref" data-reference="def:quantum-gauge-group">1.10</a>).*

</div>

<div id="def:q-harmonic-form" class="definition">

**Definition 1.13** ($q$-Harmonic form (Particle)). *Let $(M, G, E)$ be a $\mathbb{C}$ quantum observable universe with substrate parameter $q$ (Definition <a href="#def:substrate-parameter" data-reference-type="ref" data-reference="def:substrate-parameter">1.9</a>). Let $d_q$ denote the $q$-deformed exterior derivative on the CR manifold $M$. A *particle* is a section $\alpha \in \Gamma(M,\, \Lambda^k T^*M \otimes J^1 E)$ that is $q$-harmonic, i.e. lies in the kernel of the $q$-Laplacian: $$\Delta_q \alpha
  \;=\; (d_q\,\delta_q + \delta_q\,d_q)\,\alpha
  \;=\; 0,$$ where $\delta_q$ is the formal adjoint of $d_q$. The condition $\Delta_q\alpha = 0$ ensures that the form sits in a ground state of the $q$-viscosity.*

</div>

<div id="def:reeb-decomposition" class="definition">

**Definition 1.14** (Reeb decomposition). *Let $M$ be a CR manifold equipped with a contact form $\theta$ and let $\xi$ denote the associated *Reeb vector field*, characterised by $\iota_\xi\,d\theta = 0$ and $\theta(\xi) = 1$. Every differential form $\alpha$ on $M$ decomposes as $$\alpha \;=\; \alpha_H + \alpha_V,
  \qquad\text{where}\qquad
  \iota_\xi\,\alpha_V \neq 0,$$ with $\alpha_H$ the *horizontal component* (annihilated by $\iota_\xi$) and $\alpha_V$ the *vertical component* (having a non-trivial contraction with $\xi$).*

</div>

<div id="def:q-reeb-vector-field" class="definition">

**Definition 1.15** ($q$-Deformed Reeb vector field). *Let $(M, G, E)$ be a $\mathbb{C}$ quantum observable universe with substrate parameter $q$ (Definition <a href="#def:substrate-parameter" data-reference-type="ref" data-reference="def:substrate-parameter">1.9</a>) and Reeb vector field $\xi$ (Definition <a href="#def:reeb-decomposition" data-reference-type="ref" data-reference="def:reeb-decomposition">1.14</a>). The *$q$-deformed Reeb vector field* is the vector field $\xi_q$ on $M$ defined by its action on smooth functions $f \in C^\infty(M)$: $$\xi_q(f) \;=\; q\,\xi(f) + (1 - q)\,[\xi, X_f]_q,$$ where $X_f$ is the horizontal lift of $\mathrm{grad}\,f$ to $H$ and $[\,\cdot\,,\cdot\,]_q$ denotes the $q$-deformed Lie bracket on $\mathfrak{X}(M)$. When $q = 1$, one recovers the classical Reeb field $\xi_1 = \xi$.*

</div>

<div id="def:q-reeb-flow" class="definition">

**Definition 1.16** ($q$-Deformed Reeb flow). *Let $\xi_q$ be the $q$-deformed Reeb vector field (Definition <a href="#def:q-reeb-vector-field" data-reference-type="ref" data-reference="def:q-reeb-vector-field">1.15</a>). The *$q$-deformed Reeb flow* is the one-parameter family of diffeomorphisms $\phi_t^q \colon M \to M$, $t \in \mathbb{R}$, generated by $\xi_q$: $$\frac{d}{dt}\,\phi_t^q \;=\; \xi_q \circ \phi_t^q,
  \qquad \phi_0^q = \mathrm{id}_M.$$*

</div>

<div id="def:q-torsion-leaf" class="definition">

**Definition 1.17** ($q$-Torsion leaf). *Let $H = \ker\theta \subset TM$ be the horizontal distribution on the CR manifold $M$. A *$q$-torsion leaf* is a maximal integral submanifold $L \hookrightarrow M$ of $H$ that is invariant under the $q$-deformed Reeb flow (Definition <a href="#def:q-reeb-flow" data-reference-type="ref" data-reference="def:q-reeb-flow">1.16</a>): $$T_p L \;\subset\; H_p
  \quad\text{for all } p \in L,
  \qquad\text{and}\qquad
  \phi_t^q(L) = L
  \quad\text{for all } t \in \mathbb{R}.$$*

</div>

<div id="rem:q-torsion-leaf-minimum" class="remark">

**Remark 1.18** ($q$-Torsion leaves as energy minima). *Let $A_q$ denote the $q$-deformed connection on $E$ and define the $q$-curvature $$\Omega_q \;=\; dA_q + \tfrac{1}{2}\,[A_q,\, A_q]_q.$$ A $q$-torsion leaf $L$ (Definition <a href="#def:q-torsion-leaf" data-reference-type="ref" data-reference="def:q-torsion-leaf">1.17</a>) is a local minimum of $\lVert\Omega_q\rVert$ restricted to the horizontal distribution: the invariance of $L$ under $\phi_t^q$ forces the first variation of $\lVert\Omega_q|_L\rVert$ to vanish, so $L$ sits in a $q$-curvature well. Physically, a $q$-torsion leaf represents a region of the CR manifold where the gauge curvature is minimised and the $q$-deformed dynamics are in equilibrium.*

</div>

<div id="def:fermion" class="definition">

**Definition 1.19** (Fermion). *A *fermion* is a $q$-harmonic form (Definition <a href="#def:q-harmonic-form" data-reference-type="ref" data-reference="def:q-harmonic-form">1.13</a>) that has a non-trivial vertical component in the Reeb decomposition (Definition <a href="#def:reeb-decomposition" data-reference-type="ref" data-reference="def:reeb-decomposition">1.14</a>): $$\Delta_q\,\alpha = 0
  \qquad\text{and}\qquad
  \iota_\xi\,\alpha_V \neq 0.$$*

</div>

<div id="def:boson" class="definition">

**Definition 1.20** (Boson). *A *boson* is a $q$-harmonic form (Definition <a href="#def:q-harmonic-form" data-reference-type="ref" data-reference="def:q-harmonic-form">1.13</a>) that is purely horizontal in the Reeb decomposition (Definition <a href="#def:reeb-decomposition" data-reference-type="ref" data-reference="def:reeb-decomposition">1.14</a>): $$\Delta_q\,\alpha = 0
  \qquad\text{and}\qquad
  \alpha = \alpha_H
  \quad(\text{equivalently, } \iota_\xi\,\alpha = 0
        \text{ by Definition~\ref{def:reeb-decomposition}}).$$*

</div>

<div id="rem:reeb-physical" class="remark">

**Remark 1.21** (Physical interpretation of the Reeb decomposition). *The Reeb vector field $\xi$ singles out the direction of internal spin on the CR manifold. Forms that “see” this direction (fermions) carry half-integer spin; forms confined to the horizontal distribution (bosons) do not couple to the Reeb flow and carry integer spin. The decomposition $\alpha = \alpha_H + \alpha_V$ is therefore the geometric origin of the spin–statistics distinction in this framework.*

</div>

<div id="rem:q-harmonic-physical" class="remark">

**Remark 1.22** (Physical interpretation of $q$-harmonicity). *The $q$-Laplacian $\Delta_q$ encodes the $q$-deformed viscosity of the CR geometry. A $q$-harmonic form is a zero-mode of this operator and thus represents a stable excitation — a particle — of the quantum observable universe. The deformation parameter $q$ interpolates between the classical regime ($q \to 1$, where $\Delta_q$ reduces to the Hodge Laplacian) and the deep-quantum regime ($q \to 0$), so the notion of “particle” is itself $q$-dependent.*

</div>

<div id="rem:gr-substrate-geometry" class="remark">

**Remark 1.23** (General Relativity as the “Substrate Geometry”). *In this model the metric is effectively replaced by the Levi form $L$ and its coupling to the gauge curvature $F_A$. Gravity is expressed through the Variational Bicomplex as the back-reaction of the gauge fields on the CR manifold $M$.*

*The Einstein–Hilbert action is recovered by examining the variation of the action $S_q$ with respect to the Levi form $L$: $$\frac{\delta S_q}{\delta L}
  \;\implies\;
  G_{\mu\nu} \;\sim\; T_{\mu\nu}^{(q)},$$ where $T_{\mu\nu}^{(q)}$ is a *quantum-weighted* stress-energy tensor. Because $q(p) = \exp\!\bigl(-\lVert L \wedge F^+\rVert\bigr)$, the geometry of the brane $M$ is forced to curve to accommodate the tension of the $\mathrm{SU}(2)$ instantons.*

</div>

<div id="rem:schrodinger-jet-coaction" class="remark">

**Remark 1.24** (The Schrödinger Equation as “Jet Co-action”). *The Schrödinger equation describes the evolution of a state in the fibre $\mathbb{CP}$. In the jet-bundle framework this is expressed as the condition of parallel transport along the connection $A$.*

*For a section $\psi \in \Gamma(E)$, the Schrödinger dynamics are found in the kernel of the $q$-deformed covariant derivative on $J^1 E$: $$i\,\hbar_q(p)\, D_A \psi \;=\; \hat{H}_q\, \psi,$$ where $\hat{H}_q$ is the $q$-deformed Hamiltonian operator and:*

- *$\hbar_q(p) = 1 - q(p)$: the quantum Planck constant (Definition <a href="#def:quantum-planck-constant" data-reference-type="ref" data-reference="def:quantum-planck-constant">1.11</a>) is a local field;*

- *$D_A = d + A$: the connection $A$ (the instanton) acts as the potential.*

*As $q(p) \to 1$ (classicality), the uncertainty vanishes and the wave-like nature of the section freezes into a classical trajectory.*

</div>

<div id="rem:main-commutative-diagram" class="remark">

**Remark 1.25** (Main Commutative Diagram). *The relationship between these two seemingly disparate equations is captured by the main commutative diagram of the $\mathbb{C}$-quantum universe, where $\mathbf{E}$ denotes the Euler–Lagrange operator. The link is the substrate parameter $q(p)$: $$\begin{CD}
J^1E @>{\text{Variational Derivative } \mathbf{E}}>>
  \text{General Relativity (Geometry)} \\
@V{\text{Jet Co-action}}VV
  @VV{\text{Coupling via } q(p)}V \\
\Gamma(E) @>{\text{Parallel Transport}}>>
  \text{Schr\"odinger Eq.\ (Quantum States)}
\end{CD}$$*

</div>

# Lifting of Quantum Torsion

<div id="prop:jet-prolongation" class="proposition">

**Proposition 2.1** (Jet Prolongation). *Let $(M, G, E)$ be a $\mathbb{C}$ quantum observable universe (Definition <a href="#def:c-quantum-observable-universe" data-reference-type="ref" data-reference="def:c-quantum-observable-universe">1.2</a>) with connection $A$ and metric $g$ on $E$. Write $\widetilde{M} = E$ for the total space of $E$, viewed as a manifold, and define $E'$ as the bundle of orthonormal frames of the first jet bundle $J^1 E$. Then $A$ and $g$ uniquely determine a connection $A'$ on $E'$ such that $(\widetilde{M}, G, E')$ is a $\mathbb{C}$ quantum observable universe.*

</div>

<div class="proof">

*Proof.* ◻

</div>

<div id="def:recursive-brane-tower" class="definition">

**Definition 2.2** (Recursive Brane Tower). *Let $(M, G, E)$ be a $\mathbb{C}$ quantum observable universe (Definition <a href="#def:c-quantum-observable-universe" data-reference-type="ref" data-reference="def:c-quantum-observable-universe">1.2</a>). Set $M_0 = M$ and $E_1 = E$. *Inductively*, define $E_{n+1}$ as the jet prolongation (Proposition <a href="#prop:jet-prolongation" data-reference-type="ref" data-reference="prop:jet-prolongation">2.1</a>) of $E_n$.*

*The *brane relation* is the following recursive structure:*

1.  *Each total space $E_n$ is treated as the base manifold $M_{n+1}$ for the next level; $E_n$ is the *brane* of $E_{n+1}$.*

2.  *At each level, $A_n \in \mathcal{A}(E_{n-1})$ is the $n$-th level instanton connection satisfying the Hermitian Yang–Mills equations on $E_n$.*

</div>

<div id="ex:brane-tower-levels" class="example">

**Example 2.3** (First two levels). *Starting from a $\mathbb{C}$ quantum observable universe $(M, G, E_1)$, the first jet prolongation yields $E_2$ with base manifold $M_1 = E_1$. The connection $A_1$ on $E_1$ satisfies the Hermitian Yang–Mills equations, and $A_2$ on $E_2$ is uniquely determined by Proposition <a href="#prop:jet-prolongation" data-reference-type="ref" data-reference="prop:jet-prolongation">2.1</a>.*

</div>

<div id="def:quantum-characteristic-classes" class="definition">

**Definition 2.4** (Quantum Characteristic Classes). *Let $\{E_n\}_{n \geq 1}$ be the recursive brane tower (Definition <a href="#def:recursive-brane-tower" data-reference-type="ref" data-reference="def:recursive-brane-tower">2.2</a>). The *quantum characteristic classes* are the cohomology classes $$\kappa_n \;\in\; H^*\!\bigl(E_{n+1},\, \mathbb{Z}\bigr)$$ that label the monodromy fixed points of the holonomy representation as one transitions from $E_n$ to $E_{n+1}$.*

</div>

<div id="rem:betti-numbers-brane" class="remark">

**Remark 2.5** (Betti numbers of the brane tower). *Let $b_k(E_n) = \dim H^k(E_n, \mathbb{R})$ denote the $k$-th Betti number of $E_n$. Since $E_{n+1}$ is the bundle of orthonormal frames of $J^1 E_n$, the Betti numbers of $E_{n+1}$ are determined by those of $E_n$ via the Leray–Serre spectral sequence applied to the fibration $E_{n+1} \to E_n$. In particular, the quantum characteristic classes (Definition <a href="#def:quantum-characteristic-classes" data-reference-type="ref" data-reference="def:quantum-characteristic-classes">2.4</a>) obstruct the collapse of this spectral sequence and control the growth of $b_k(E_{n+1})$ in terms of $b_k(E_n)$.*

</div>

<div id="rem:q-harmonic-basis-brane" class="remark">

**Remark 2.6** ($q$-Harmonic basis of the brane tower). *For each level $n$, the $q$-harmonic $1$-forms $\alpha_{n,i}$ belong to the space $\mathcal{H}^1(E_n,\, \mathrm{ad}\, E_n)$ of harmonic $1$-forms on $E_n$ with values in the adjoint bundle $\mathrm{ad}\, E_n$. These are characterised by the self-duality condition relative to the instanton connection $A_n$ (Definition <a href="#def:recursive-brane-tower" data-reference-type="ref" data-reference="def:recursive-brane-tower">2.2</a>): $$\alpha_{n,i} \in \mathcal{H}^1
  \iff
  d_{A_n}\,\alpha = 0
  \quad\text{and}\quad
  d_{A_n}^*\,\alpha = 0,$$ where the Hodge-star operator is induced by the Hermitian metric that the Levi form $L$ (Definition <a href="#def:substrate-parameter" data-reference-type="ref" data-reference="def:substrate-parameter">1.9</a>) defines on the horizontal distribution. The index $i$ runs over $1 \leq i \leq b_1(E_n)$ (Remark <a href="#rem:betti-numbers-brane" data-reference-type="ref" data-reference="rem:betti-numbers-brane">2.5</a>).*

*At the base level $n = 0$, with Euler characteristic $\chi(M) = 3$, there are three primary basis vectors $\{\,\phi_1,\, \phi_2,\, \phi_3\,\}$. At level $n = 1$ the basis lifts: the new basis includes the original modes together with their $J^1$ prolongations (Proposition <a href="#prop:jet-prolongation" data-reference-type="ref" data-reference="prop:jet-prolongation">2.1</a>), which are the first-order resolutions of the base flows.*

</div>

<div id="rem:weight-space-decomposition" class="remark">

**Remark 2.7** (Weight-space decomposition of the harmonic basis). *The adjoint bundle $\mathrm{ad}\, E_n$ has fibre $\mathfrak{su}(2)$. Via the weight-space decomposition of $\mathrm{SU}(2)$, the harmonic basis of $\mathcal{H}^1(E_n,\, \mathrm{ad}\, E_n)$ splits into two families.*

**Longitudinal modes.* These forms constitute the $\mathrm{U}(1)$ backbone of the decomposition. They take values in the Cartan subalgebra of $\mathfrak{su}(2)$ and have the geometric form $\omega^0 \otimes H$, where $H$ is the diagonal generator. They represent steady-state laminar flows aligned with the $\mathrm{U}(1)$ subgroup. If the bundle splits at a monodromy fixed point, these are the only modes that survive; they correspond to the magnetic flux of the stable vortices.*

**Ladder modes.* These are the raising and lowering vortices of the decomposition. They take values in the off-diagonal generators $E_\pm$ of $\mathfrak{su}(2)$ and have the geometric form $\omega^\pm \otimes E_\pm$. They describe the entangling flows that twist the $\mathbb{CP}^1$ fibre as one moves along the brane. These modes are responsible for the non-commutativity in the $\mathrm{SU}_q(2)$ algebra (Definition <a href="#def:direct-limit-algebra" data-reference-type="ref" data-reference="def:direct-limit-algebra">2.10</a>).*

*In the $1$-jet bundle $J^1 E_n$ (Remark <a href="#rem:j1e-local-states" data-reference-type="ref" data-reference="rem:j1e-local-states">1.12</a>), each basis element $\alpha$ is a pair consisting of a *value* (the direction of the $\mathrm{SU}(2)$ flow in the fibre) and a *momentum* (the gradient of that flow relative to the complex structure of the brane).*

</div>

<div id="rem:algebraic-filter" class="remark">

**Remark 2.8** (The algebraic filter). *Let $\alpha$ be a harmonic $1$-form in the basis of Remark <a href="#rem:q-harmonic-basis-brane" data-reference-type="ref" data-reference="rem:q-harmonic-basis-brane">2.6</a>. Its *signature* is determined by its commutator with the curvature $F_A$ (Definition <a href="#def:substrate-parameter" data-reference-type="ref" data-reference="def:substrate-parameter">1.9</a>).*

**Fermionic type (matter).* $[F_A,\, \alpha] \neq 0$. These forms are entangled with the curvature: they see the $\mathrm{SO}(3)$ holonomy and the $-6$ index fixed points. Their geodesics are trapped or spiralling around the three fundamental vortex filaments.*

**Bosonic type (radiation).* $[F_A,\, \alpha] = 0$. These forms commute with the curvature. They are the longitudinal modes (Remark <a href="#rem:weight-space-decomposition" data-reference-type="ref" data-reference="rem:weight-space-decomposition">2.7</a>) that flow through the bulk without being deflected by the monodromy fixed points. Their geodesics are straight relative to the gauge-fluid flow.*

</div>

<div id="rem:distributional-connection" class="remark">

**Remark 2.9** (Distributional connection at the limit). *At the limit $n \to \infty$ one no longer looks at a single connection $A$, but at a *distributional connection* represented by the series $$A_\infty
  \;=\;
  \sum_{n=0}^{\infty}\;\sum_{i=1}^{b_1(E_n)}
  c_{n,i}\,\alpha_{n,i}\,,$$ where $c_{n,i} \in \mathbb{C}$ and $\{\alpha_{n,i}\}$ is the $q$-harmonic basis of Remark <a href="#rem:q-harmonic-basis-brane" data-reference-type="ref" data-reference="rem:q-harmonic-basis-brane">2.6</a>. This turns the gauge field into a harmonic expansion across the infinite jet space $J^\infty E$ (Remark <a href="#rem:jet-shell" data-reference-type="ref" data-reference="rem:jet-shell">2.11</a>).*

</div>

<div id="def:direct-limit-algebra" class="definition">

**Definition 2.10** ($\mathbb{C}$ Quantum Observable Universe as Direct Limit). *Let $\{E_n\}_{n \geq 1}$ be the recursive brane tower (Definition <a href="#def:recursive-brane-tower" data-reference-type="ref" data-reference="def:recursive-brane-tower">2.2</a>) with substrate parameters $q_n$ (Definition <a href="#def:substrate-parameter" data-reference-type="ref" data-reference="def:substrate-parameter">1.9</a>) at each level. The *$\mathbb{C}$ quantum observable universe* is the direct limit algebra $$\mathcal{A}_\infty
  \;=\;
  \varinjlim\,
  \Gamma\!\bigl(J^1 E_n,\, \mathrm{SU}_{q_n}(2)\bigr).$$*

</div>

<div id="rem:jet-shell" class="remark">

**Remark 2.11** (Jet Shell of the universe). *In the limit $n \to \infty$, the infinite jet bundle $J^\infty E = \varprojlim\, J^k E$ becomes the *jet shell* of the universe. All finite-level brane data are encoded in this pro-finite structure, and the algebra $\mathcal{A}_\infty$ (Definition <a href="#def:direct-limit-algebra" data-reference-type="ref" data-reference="def:direct-limit-algebra">2.10</a>) acts naturally on sections of the jet shell.*

</div>

<div id="prop:vacuum-state" class="proposition">

**Proposition 2.12** (Existence and Uniqueness of the Vacuum State). *Let $\mathcal{A}_\infty$ be the direct limit algebra (Definition <a href="#def:direct-limit-algebra" data-reference-type="ref" data-reference="def:direct-limit-algebra">2.10</a>) equipped with the global $\mathrm{SU}(2)$ action and the recursive $q$-deformations. Then there exists a unique state $\omega \colon \mathcal{A}_\infty \to \mathbb{C}$ that is $\mathrm{SU}(2)$-invariant: $$\omega(g \cdot a) = \omega(a)
  \quad\text{for all } g \in \mathrm{SU}(2),\;
  a \in \mathcal{A}_\infty.$$*

</div>

<div class="proof">

*Proof.* ◻

</div>

<div id="rem:mass-geometric-drag" class="remark">

**Remark 2.13** (Mass as geometric drag). *In this recursive $\mathrm{SU}(2)$ tower (Definition <a href="#def:recursive-brane-tower" data-reference-type="ref" data-reference="def:recursive-brane-tower">2.2</a>), mass is not an intrinsic property of a point-particle but rather a measure of the *geometric drag* (or “viscosity”) encountered by a stable vortex as it propagates through the $1$-jet bundle $J^1 E_n$. When $q \neq 1$ the field is non-commutative: moving the vortex requires a continuous rearrangement of the $\mathrm{SU}_q(2)$ algebra (Definition <a href="#def:direct-limit-algebra" data-reference-type="ref" data-reference="def:direct-limit-algebra">2.10</a>) across the fibres.*

</div>

<div id="prop:euler-char-stability" class="proposition">

**Proposition 2.14** (Stability of the Euler characteristic). *Let $(M, G, E)$ be a $\mathbb{C}$ quantum observable universe and let $\{E_n\}_{n \geq 1}$ be the recursive brane tower (Definition <a href="#def:recursive-brane-tower" data-reference-type="ref" data-reference="def:recursive-brane-tower">2.2</a>). Then the Euler characteristic $\chi(E)$ is stable under descent and lifting: for each level $n$, $$\chi(E_{n+1}) \;=\; \chi(E_n).$$ In particular, if the base level satisfies $\chi(E_1) = c$, then $\chi(E_n) = c$ for all $n \geq 1$.*

</div>

<div class="proof">

*Proof.* ◻

</div>

<div id="def:mass-identity" class="definition">

**Definition 2.15** (Mass Identity). *Let $(M, G, E)$ be a $\mathbb{C}$ quantum observable universe with substrate parameter $q$ (Definition <a href="#def:substrate-parameter" data-reference-type="ref" data-reference="def:substrate-parameter">1.9</a>), connection $A$, Levi form $L$, and self-dual curvature $F^+$. Let $\gamma$ be a closed cycle encircling the vortex filament. The *inertial mass* $m$ of a stable vortex is $$m \;\propto\; \oint_\gamma \lVert \nabla_A\, q \rVert
               \cdot \lVert L \wedge F^+ \rVert\,.$$*

</div>

### Descent

<div id="def:descent-dim-1" class="definition">

**Definition 2.16** (Descent to Dimension $1$). *Let $\{E_n\}_{n \geq 1}$ be the recursive brane tower (Definition <a href="#def:recursive-brane-tower" data-reference-type="ref" data-reference="def:recursive-brane-tower">2.2</a>). The *descent* is the reverse traversal of the tower: starting from level $n$ one passes to level $n-1$ by restricting the connection $A_n$ and the bundle $E_n$ to the base manifold $M_{n-1}$. The descent terminates when the base manifold $M_k$ reaches $\dim M_k = 1$, at which point $M_k$ is diffeomorphic to $S^1$ or $\mathbb{R}$.*

</div>

<div id="rem:descent-reduction" class="remark">

**Remark 2.17** (Reduction at dimension $1$). *When $\dim M_k = 1$ the geometric data of the $\mathbb{C}$ quantum observable universe collapse as follows.*

1.  **Connection.* The $\mathrm{SU}(2)$ connection $A_k$ restricts to a single dimension; its holonomy reduces to a $\mathrm{U}(1)$ phase around $S^1$.*

2.  **Bundle.* The principal $\mathrm{SU}(2)$ bundle $E$ descends to a bundle over the $1$-dimensional base whose fibre dynamics are locked into a single periodic flow.*

3.  **Reeb direction.* The inverse of the Reeb vector field (Definition <a href="#def:q-reeb-vector-field" data-reference-type="ref" data-reference="def:q-reeb-vector-field">1.15</a>) becomes the only direction of motion; the horizontal distribution is trivial and no bosonic modes (Remark <a href="#rem:algebraic-filter" data-reference-type="ref" data-reference="rem:algebraic-filter">2.8</a>) survive.*

</div>

<div id="rem:descent-physical" class="remark">

**Remark 2.18** (Physical implications of a $1$-dimensional base). *At dimension $1$ the physical content simplifies drastically.*

1.  **Primordial vortex.* The vortex filaments of the mass identity (Definition <a href="#def:mass-identity" data-reference-type="ref" data-reference="def:mass-identity">2.15</a>) are no longer embedded in a larger space; the entire manifold *is* the filament.*

2.  **Mass as pure drag.* The mass identity reduces to an integral over the whole of $M_k$: $$m \;\propto\; \oint_{M_k} \lVert \nabla_A\, q \rVert
                           \cdot \lVert L \wedge F^+ \rVert\,,$$ so that mass represents the fundamental geometric resistance of the $1$-dimensional flow against the $\mathrm{SU}(2)$ rotation.*

3.  **Lepton generations.* Since the number of lepton generations is bounded by the Euler characteristic and vertical degree (Remark <a href="#rem:betti-numbers-brane" data-reference-type="ref" data-reference="rem:betti-numbers-brane">2.5</a>), a $1$-dimensional base supports only the most fundamental fermionic state; there is no room for higher-degree vertical harmonic forms.*

</div>

<div id="rem:descent-fixed-point" class="remark">

**Remark 2.19** (Fixed-point mechanism: ascent and descent). *Each step down the brane tower removes a space-like dimension through the $\mathrm{SU}(2)$ rotation and its associated fixed-point set.*

1.  **Ascent (generation).* Moving from $M_k$ ($\dim = 1$) to $M_{k+1}$ ($\dim = 3$) lifts the connection $A$ to higher categorical structures via the jet prolongation (Proposition <a href="#prop:jet-prolongation" data-reference-type="ref" data-reference="prop:jet-prolongation">2.1</a>).*

2.  **Descent (filtering).* Moving back down acts as an algebraic filter (Remark <a href="#rem:algebraic-filter" data-reference-type="ref" data-reference="rem:algebraic-filter">2.8</a>). The ladder modes (Remark <a href="#rem:weight-space-decomposition" data-reference-type="ref" data-reference="rem:weight-space-decomposition">2.7</a>) are stripped away until only the longitudinal modes—the $\mathrm{U}(1)$ backbone—remain at the $1$-dimensional limit.*

</div>

# The Descartes Universe

<div id="def:descartes-condition" class="definition">

**Definition 3.1** (Descartes condition). *A $\mathbb{C}$ quantum observable universe $(M, G, E)$ (Definition <a href="#def:c-quantum-observable-universe" data-reference-type="ref" data-reference="def:c-quantum-observable-universe">1.2</a>) satisfies the *Descartes condition* if the Euler characteristic of the bulk bundle is $$\chi(E) \;=\; -6.$$ A $\mathbb{C}$ quantum observable universe satisfying the Descartes condition is called a *Descartes universe*.*

<div class="center">

**“Je pense, donc je suis.”  
— René Descartes**

</div>

</div>

<div id="rem:descartes-calabi-yau" class="remark">

**Remark 3.2** (The Descartes condition on Calabi–Yau manifolds). *Let $(M, G, E)$ be a Calabi–Yau quantum observable universe (Example <a href="#ex:calabi-yau" data-reference-type="ref" data-reference="ex:calabi-yau">1.6</a>). The Descartes condition $\chi(E) = -6$ constrains the Hodge numbers of the Calabi–Yau manifold $M$: the alternating sum of Betti numbers of the bulk bundle $E$ must equal $-6$. In particular, only Calabi–Yau manifolds whose topology admits a principal $\mathrm{SU}(2)$-bundle with this Euler characteristic can realise the Descartes universe.*

</div>

<div id="rem:descartes-ale" class="remark">

**Remark 3.3** (The Descartes condition on ALE spaces). *For an ALE quantum observable universe (Example <a href="#ex:ale" data-reference-type="ref" data-reference="ex:ale">1.7</a>), the Descartes condition $\chi(E) = -6$ selects specific finite subgroups $\Gamma \subset \mathrm{SU}(2)$ in the quotient singularity $\mathbb{C}^2 / \Gamma$. The Euler characteristic of the resolved space and its principal bundle are tied to the order and representation theory of $\Gamma$, so the Descartes condition imposes arithmetic constraints on the McKay quiver of $\Gamma$.*

</div>

<div id="rem:descartes-affine" class="remark">

**Remark 3.4** (The Descartes condition on affine space). *For the affine quantum observable universe $M = \mathbb{C}^n$ (Example <a href="#ex:affine" data-reference-type="ref" data-reference="ex:affine">1.8</a>), the Descartes condition $\chi(E) = -6$ forces the principal $\mathrm{SU}(2)$-bundle $E$ to carry non-trivial topology despite the contractibility of the base. In the two-dimensional case $M = \mathbb{C}^2$, the $q$-harmonic forms on this bundle (Definition <a href="#def:q-harmonic-form" data-reference-type="ref" data-reference="def:q-harmonic-form">1.13</a>) determine the spectrum of stable excitations. In the regime $q(p) \to 1$ (near-classicality), the zero-modes of $\Delta_q$ reproduce the thermal fluctuation spectrum of the Cosmic Microwave Background: the Hodge numbers of $E$ govern the multiplicity of angular modes, and the negative Euler characteristic forces a non-trivial distribution of these modes across the CR manifold $M$.*

</div>

<div id="rem:descent-one-dim" class="remark">

**Remark 3.5** (Descent to one complex dimension). *By the descent theorem (Proposition <a href="#prop:jet-prolongation" data-reference-type="ref" data-reference="prop:jet-prolongation">2.1</a>), a two-complex-dimensional Descartes universe $(M, G, E)$ with $M = \mathbb{C}^2$ descends to a one-complex-dimensional variety $M_0$. The stability of the Euler characteristic under descent and lifting (Proposition <a href="#prop:euler-char-stability" data-reference-type="ref" data-reference="prop:euler-char-stability">2.14</a>) ensures that the descended universe retains $\chi(E) = -6$. We may therefore study the Descartes universe entirely in the setting of one-complex-dimensional varieties.*

</div>

<div id="prop:genus-maximal-descent" class="proposition">

**Proposition 3.6** (Genus of the maximal descent). *Let $(M, G, E)$ be a Descartes universe that descends to a compact one-complex-dimensional variety $M_0$. Then $M_0$ is a Riemann surface of genus $g = 4$.*

</div>

<div class="proof">

*Proof.* For a compact Riemann surface of genus $g$, the Euler characteristic is $\chi = 2 - 2g$. The Descartes condition requires $\chi(E) = -6$. On the maximal descent $M_0$, the stability of the Euler characteristic (Proposition <a href="#prop:euler-char-stability" data-reference-type="ref" data-reference="prop:euler-char-stability">2.14</a>) gives $\chi(M_0) = -6$, whence $2 - 2g = -6$ and $g = 4$. ◻

</div>

<div id="rem:descartes-leptons" class="remark">

**Remark 3.7** (Electrons, muons and the Reeb decomposition). *The Reeb decomposition (Definition <a href="#def:reeb-decomposition" data-reference-type="ref" data-reference="def:reeb-decomposition">1.14</a>) applied to a Descartes universe yields two classes of fermionic excitations (Definition <a href="#def:fermion" data-reference-type="ref" data-reference="def:fermion">1.19</a>). The degree of the vertical component $\alpha_V$ distinguishes them: forms with $\deg\alpha_V = 1$ correspond to electrons, while forms with $\deg\alpha_V = 2$ correspond to muons. More generally, each additional unit of vertical degree is identified with a successive lepton generation. The constraint $\chi(E) = -6$ bounds the number of such generations, since the Hodge decomposition of $E$ admits only finitely many independent vertical harmonic forms.*

</div>

<div id="rem:descartes-chirality" class="remark">

**Remark 3.8** (Chirality as Reeb orientation). *The Reeb vector field $\xi$ on the CR manifold $M$ carries a natural orientation: the sign of the contact form $\theta(\xi) = 1$ singles out a preferred direction along the vertical distribution. Left-handed and right-handed chiralities correspond to the two orientations of $\xi$ relative to the complex structure of $M$. For fermions (Definition <a href="#def:fermion" data-reference-type="ref" data-reference="def:fermion">1.19</a>), the vertical component $\alpha_V$ transforms with a definite sign under reversal of $\xi$, so chirality is encoded in the $\pm$-eigenspaces of the Reeb involution $\xi \mapsto -\xi$. Bosons (Definition <a href="#def:boson" data-reference-type="ref" data-reference="def:boson">1.20</a>), being purely horizontal, are chirality-blind — consistent with the observed parity invariance of the electromagnetic and strong interactions.*

</div>

<div id="rem:light-cone-affine" class="remark">

**Remark 3.9** (Light cone of an affine chart). *Consider an open subset $U \subset M_0$ representing a portion of the descended universe from the big bang to heat death. An *affine chart* on $U$ is a local coordinate patch in which the metric on the base manifold $M_0$ defines a causal structure. The *light cone* of the affine chart is the boundary of the causal future in $U$: it is determined by the metric on $M_0$ and has the property that no singularity of the ambient space is visible from within the chart. In this way, the affine chart provides a non-singular window onto a portion of the Descartes universe.*

</div>

<figure id="fig:affine-light-cone">

<figcaption>Affine light cone on the brane (<span class="math inline"><em>χ</em>(<em>E</em>) =  − 6</span>), depicted as a surface of revolution with exponential profile. The brane carries a twisted rectangular grid illustrating the torsion of the bundle <span class="math inline"><em>E</em></span>; the grid lines twist progressively along the surface, aligning with the brane boundary. The cone vertex at the big bang (<span class="math inline"><em>q</em><sub><em>p</em></sub> → 0</span>, <span class="math inline">ℏ<sub><em>q</em></sub> → 1</span>, <span class="math inline">∥<em>L</em> ∧ <em>F</em><sup>+</sup>∥ → ∞</span>) opens into an expanding wedge—a narrow strip at the observer (Milky Way)—that grows faster than linearly and wraps around the back of the brane towards the heat death (<span class="math inline"><em>q</em><sub><em>p</em></sub> → 1</span>, <span class="math inline">ℏ<sub><em>q</em></sub> → 0</span>, <span class="math inline">∥<em>L</em> ∧ <em>F</em><sup>+</sup>∥ → 0</span>), where it nearly closes to the full circle. The upward tilt at the heat-death end reflects the intrinsic curvature; time is encoded in the brane geometry, not as an external axis. See Remark <a href="#rem:light-cone-affine" data-reference-type="ref" data-reference="rem:light-cone-affine">3.9</a>. </figcaption>
</figure>

<figure id="fig:reeb-viscosity">
<embed src="figures/reeb-viscosity.pdf" style="width:85.0%" />
<figcaption><span class="math inline"><em>E</em></span> operating on <span class="math inline">ℂ<sup>1</sup></span> QOU: Reeb dimension as brane thickness (<span class="math inline"><em>χ</em>(<em>E</em>) =  − 6</span>). The Reeb vector field <span class="math inline"><em>ξ</em><sub><em>q</em></sub></span> (Definition <a href="#def:q-reeb-vector-field" data-reference-type="ref" data-reference="def:q-reeb-vector-field">1.15</a>) gives the brane an intrinsic “thickness” representing the <span class="math inline"><em>q</em></span>-deformed viscosity of the gauge fluid on which the bundle <span class="math inline"><em>E</em></span> operates. At the big bang (<span class="math inline"><em>q</em><sub><em>p</em></sub> → 0</span>, <span class="math inline">ℏ<sub><em>q</em></sub> → 1</span>) the brane is thin: the gauge fluid is energetic and <span class="math inline"><em>E</em></span> swirls it up freely. Towards the heat death (<span class="math inline"><em>q</em><sub><em>p</em></sub> → 1</span>, <span class="math inline">ℏ<sub><em>q</em></sub> → 0</span>) the brane thickens: the fluid becomes viscous (mud-like), energy capacity drops, and the <span class="math inline"><em>q</em></span>-deformed Reeb flow (Definition <a href="#def:q-reeb-flow" data-reference-type="ref" data-reference="def:q-reeb-flow">1.16</a>) stiffens to the classical Reeb field <span class="math inline"><em>ξ</em></span>. The brown gradient illustrates this increasing viscosity. The displayed region is a single affine chart (<span class="math inline"><em>z</em><sub>1</sub> ≠ 0</span>) on Bring’s curve <span class="math inline"><em>Σ</em><sub>4</sub></span> (Remark <a href="#rem:brings-curve" data-reference-type="ref" data-reference="rem:brings-curve">3.12</a>), projected stereographically to <span class="math inline">ℝ<sup>3</sup></span>. </figcaption>
</figure>

<div id="rem:figure-summary" class="remark">

**Remark 3.10** (Summary of Figures <a href="#fig:affine-light-cone" data-reference-type="ref" data-reference="fig:affine-light-cone">3.1</a> and <a href="#fig:reeb-viscosity" data-reference-type="ref" data-reference="fig:reeb-viscosity">3.2</a>). *Together, the two figures capture the geometric anatomy of the Descartes universe ($\chi(E) = -6$). Figure <a href="#fig:affine-light-cone" data-reference-type="ref" data-reference="fig:affine-light-cone">3.1</a> shows the *affine light cone*: the causal wedge on the brane that an observer can access, starting as a point at the big bang and opening towards the heat death. The twisted grid on the surface records the torsion of the bundle $E$; the grid lines align with the brane boundary and twist progressively, reflecting the $E$-bundle curvature. Time is encoded intrinsically in the exponential profile of the brane rather than as an external axis. Figure <a href="#fig:reeb-viscosity" data-reference-type="ref" data-reference="fig:reeb-viscosity">3.2</a> exposes the transverse direction: the *Reeb dimension* $\xi_q$ gives the brane a physical thickness proportional to the $q$-deformed viscosity of the gauge fluid. Thin (big bang) means high energy capacity and free swirling of $E$; thick (heat death) means viscous, mud-like rigidity with vanishing energy capacity. The substrate parameter $q$ interpolates smoothly between these extremes, so neither the big-bang nor heat-death singularity is realised — the torsion twists faster than the integrals can diverge.*

*Both figures depict a single tiny neighbourhood of Bring’s curve $\Sigma_4$ (Remark <a href="#rem:brings-curve" data-reference-type="ref" data-reference="rem:brings-curve">3.12</a>). Good projections for visualising such a neighbourhood include:*

1.  **Affine chart* ($z_i \neq 0$): picking one of the five homogeneous coordinates $z_1, \ldots, z_5$ as non-zero reduces the three Bring equations to a codimension-$3$ locus in $\mathbb{C}^4$; a small ball in this affine patch gives the displayed region.*

2.  **Stereographic projection* ($\mathbb{P}^4 \to \mathbb{R}^4
          \to \mathbb{R}^3$): project from a point at infinity onto the tangent hyperplane to obtain a real $3$-dimensional image.*

3.  **Period-matrix slice*: the Jacobian $J(\Sigma_4)$ is a principally polarised abelian variety of dimension $4$; a $2$-dimensional slice through the period lattice gives a flat conformal chart.*

*The boundary of the displayed neighbourhood is the intersection of a small geodesic ball $B_\varepsilon(p) \subset \Sigma_4$ with the affine chart $\{z_1 \neq 0\}$; the ball radius $\varepsilon$ is chosen so that the curvature of $\Sigma_4$ is nearly constant inside $B_\varepsilon(p)$.*

</div>

<div id="rem:chirality-trefoil" class="remark">

**Remark 3.11** (Chirality and trefoil subgroups). *The chirality of the observable universe — manifest in the three colour charges of quantum chromodynamics — is encoded in the symmetry group of the descended surface $M_0$. Proposition <a href="#prop:genus-maximal-descent" data-reference-type="ref" data-reference="prop:genus-maximal-descent">3.6</a> identifies $M_0$ as a genus-$4$ Riemann surface. We require a genus-$4$ surface whose automorphism group contains three subgroups isomorphic to $S_3$ — quotients of the trefoil knot group $\pi_1(S^3 \setminus K) \cong \langle x, y \mid x^2 = y^3 \rangle$ — corresponding to the three colour charges (red, green, blue). These $S_3$ subgroups generate a subgroup of the monodromy group, and the remaining generators of the full automorphism group act by conjugation, permuting the three $S_3$ subgroups among themselves.*

</div>

<div id="rem:brings-curve" class="remark">

**Remark 3.12** (Bring’s curve). *Bring’s curve is the unique Riemann surface of genus $4$ with the maximal automorphism group $S_5$ (order $120$) for its genus. It is defined by the intersection of three symmetric hypersurfaces in $\mathbb{P}^4$: $$\sum_{i=1}^{5} z_i = 0,
  \qquad
  \sum_{i=1}^{5} z_i^2 = 0,
  \qquad
  \sum_{i=1}^{5} z_i^3 = 0.$$ The symmetric group $S_5$ acts by permuting the five homogeneous coordinates, and this action realises the monodromy structure described in Remark <a href="#rem:chirality-trefoil" data-reference-type="ref" data-reference="rem:chirality-trefoil">3.11</a>: the group $S_5$ contains three copies of $S_3$ (quotients of the trefoil knot group) corresponding to the three colour charges, and elements outside these subgroups act by conjugation, permuting the three copies among themselves.*

</div>

<div id="thm:descartes" class="theorem">

**Theorem 3.13** (Descartes theorem). *Let $\mathcal{C}_{-6}$ denote the category of $\mathbb{C}$ quantum observable universes satisfying the Descartes condition $\chi(E) = -6$, with morphisms given by QOU maps that preserve the Euler characteristic. Then Bring’s curve $\Sigma_4$ (Remark <a href="#rem:brings-curve" data-reference-type="ref" data-reference="rem:brings-curve">3.12</a>) is a terminal object in $\mathcal{C}_{-6}$: for every Descartes universe $(M, G, E)$ in $\mathcal{C}_{-6}$, there exists a unique morphism $(M, G, E) \to (\Sigma_4, G, E_{\Sigma_4})$ in $\mathcal{C}_{-6}$.*

</div>

<div class="proof">

*Proof.* ◻

</div>

<div id="rem:universality-general" class="remark">

**Remark 3.14** (Universality for a given Euler characteristic). *The Descartes theorem (Theorem <a href="#thm:descartes" data-reference-type="ref" data-reference="thm:descartes">3.13</a>) is expected to be a special case of a more general result: for any admissible Euler characteristic $\chi$, the category $\mathcal{C}_{\chi}$ of $\mathbb{C}$ quantum observable universes with $\chi(E) = \chi$ should admit a terminal object determined by the unique maximally symmetric Riemann surface of the corresponding genus. The Descartes case $\chi = -6$ (genus $4$) is distinguished by Bring’s curve, but analogous universal objects are expected at other values of $\chi$.*

</div>

# Path Integrals and Braiding

In the QOU framework, traditional path integrals are replaced by finite sums over the discrete fibre structure. Since the base space $B$ and each fibre are finite, the continuum measure $\mathcal{D}\phi$ collapses to a combinatorial sum, eliminating the need for renormalisation of divergent integrals.

The braid group acts naturally on the fibre degrees of freedom. What we observe as particle interactions corresponds to the action of braid operators exchanging strands in the fibre bundle. The algebraic content of these interactions is therefore encoded in braid-group representations rather than in Feynman vertices.

The exchange operations carry a $q$-deformation parameter inherited from the quantum group structure of the fibres. Concretely, the $R$-matrix of $\mathcal{U}_q(\mathfrak{su}(2))$ furnishes a $q$-deformed braid operator whose eigenvalues govern the phase acquired under particle exchange.

Under this correspondence, specific knot types map to particle identities. The trefoil knot, being the simplest non-trivial torus knot, is identified with the quark; the muon arises as a lift of the trefoil to a higher fibre level. The unknot, carrying trivial braiding, corresponds to the neutrino.

# Interpretations

# Experimental Evidence

The QOU framework (Chapter <a href="#chap:qou" data-reference-type="ref" data-reference="chap:qou">1</a>) makes predictions that differ from the standard $\Lambda$CDM cosmology and the Standard Model of particle physics. This chapter catalogues observable signatures, organised by scale, and maps each to existing data sets, planned observations, and potential new experiments.

## Large-Scale Observations

### CMB Anisotropy and $q$-Torsion Imprint

<div id="rem:cmb-q-torsion" class="remark">

**Remark 6.1** (CMB non-uniformity from $q$-torsion). *In the Descartes universe (Example <a href="#ex:descartes" data-reference-type="ref" data-reference="ex:descartes">[ex:descartes]</a>), the negative Euler characteristic $\chi(E) = -6$ forces a non-trivial distribution of angular modes across the CR manifold (Remark <a href="#rem:descartes-cmb" data-reference-type="ref" data-reference="rem:descartes-cmb">[rem:descartes-cmb]</a>). The $q$-torsion leaves (Definition <a href="#def:q-torsion-leaf" data-reference-type="ref" data-reference="def:q-torsion-leaf">1.17</a>; here “leaves” is the geometric plural of *leaf*) imprint a characteristic pattern on the CMB that deviates from the statistically isotropic Gaussian field predicted by $\Lambda$CDM. Specifically, the $q$-deformed Reeb flow (Definition <a href="#def:q-reeb-flow" data-reference-type="ref" data-reference="def:q-reeb-flow">1.16</a>) introduces *torsion* into the temperature and polarisation multipoles, producing preferred spiral directions in the $B$-mode spectrum.*

</div>

##### Existing data sets.

- *Planck* 2018 full-sky temperature and polarisation maps (PR3/PR4).

- *WMAP* nine-year data release.

- ACT (Atacama Cosmology Telescope) and SPT (South Pole Telescope) high-$\ell$ power spectra.

##### Planned observations.

- *LiteBIRD* (JAXA, launch $\sim$<!-- -->2032): full-sky $B$-mode polarisation survey sensitive to large-angular-scale torsion signatures.

- *CMB-S4*: ground-based next-generation CMB survey with improved sensitivity to polarisation anomalies.

- *Simons Observatory*: intermediate-scale polarimetry bridging current and CMB-S4 sensitivities.

##### Potential new experiments.

- A dedicated search for spiral (chiral) patterns in existing CMB $B$-mode data, testing for the preferred handedness predicted by the Reeb orientation (Remark <a href="#rem:descartes-chirality" data-reference-type="ref" data-reference="rem:descartes-chirality">3.8</a>).

- Cross-correlation of CMB anomalies (e.g. the Cold Spot, hemispherical asymmetry) with the angular structure of $q$-torsion leaves.

### Gravitational Signatures and Emergent Geometry

<div id="rem:gravity-emergent" class="remark">

**Remark 6.2** (Gravity as emergent substrate geometry). *In the QOU framework, general relativity emerges as the substrate geometry of the CR manifold (Remark <a href="#rem:gr-substrate-geometry" data-reference-type="ref" data-reference="rem:gr-substrate-geometry">1.23</a>). The quantum-weighted stress-energy tensor $T_{\mu\nu}^{(q)}$ introduces $q$-dependent corrections to the Einstein field equations. This is consistent with recent work treating gravity as arising from an information-theoretic context .*

</div>

##### Existing data sets.

- LIGO/Virgo/KAGRA gravitational wave catalogues (GWTC-1 through GWTC-3).

- Pulsar Timing Array data sets (NANOGrav 15-year, EPTA, PPTA, IPTA).

- Solar System ephemeris tests of general relativity (Cassini, MESSENGER).

##### Planned observations.

- *LISA* (ESA, launch $\sim$<!-- -->2035): space-based gravitational wave detector sensitive to low-frequency waveform corrections from the $q$-deformed field equations.

- *Einstein Telescope*: next-generation ground-based detector with sensitivity to post-merger ringdown deviations.

##### Potential new experiments.

- Precision tests of the equivalence principle at quantum scales, probing whether the substrate parameter $q$ (Definition <a href="#def:substrate-parameter" data-reference-type="ref" data-reference="def:substrate-parameter">1.9</a>) introduces composition-dependent deviations.

- Tabletop gravity experiments at sub-millimetre scales to search for $q$-dependent modifications to the Newtonian potential.

### Large-Scale Structure and Topological Defects

<div id="rem:topological-defects" class="remark">

**Remark 6.3** (Topological signatures in large-scale structure). *The $\mathrm{SO}(3)$ holonomy of the bulk bundle (Definition <a href="#def:c-quantum-universe" data-reference-type="ref" data-reference="def:c-quantum-universe">1.1</a>) and the monodromy fixed points of the quantum characteristic classes (Definition <a href="#def:quantum-characteristic-classes" data-reference-type="ref" data-reference="def:quantum-characteristic-classes">2.4</a>) may leave topological imprints on the large-scale distribution of matter — for instance, preferred filamentary alignments or voids correlated with the brane tower structure (Definition <a href="#def:recursive-brane-tower" data-reference-type="ref" data-reference="def:recursive-brane-tower">2.2</a>).*

</div>

##### Existing data sets.

- SDSS (Sloan Digital Sky Survey) galaxy catalogues and BAO measurements.

- DES (Dark Energy Survey) weak-lensing maps.

- *eROSITA* X-ray sky survey cluster catalogues.

##### Planned observations.

- *Euclid* (ESA): wide-field survey of galaxy shapes and redshifts for weak-lensing tomography.

- *Vera C. Rubin Observatory* (LSST): deep optical survey enabling statistical tests of filament chirality.

- *Roman Space Telescope* (NASA): high-redshift galaxy survey.

##### Potential new experiments.

- Statistical analysis of cosmic-web filament handedness as a probe of global $q$-torsion.

- Void-shape analysis to detect signatures of monodromy fixed points in the brane tower.

## Small-Scale Observations

### Mass Equation Predictions

<div id="rem:mass-ratio-predictions" class="remark">

**Remark 6.4** (Theoretical mass ratios from the mass identity). *The mass identity (Definition <a href="#def:mass-identity" data-reference-type="ref" data-reference="def:mass-identity">2.15</a>) expresses inertial mass as a line integral of $\lVert\nabla_A q\rVert \cdot \lVert L \wedge F^+\rVert$ around a vortex filament. For the Descartes universe with $\chi(E) = -6$, the topological data of the bundle constrain the allowed vortex configurations and hence the mass spectrum. The electron–muon mass ratio, for instance, is governed by the ratio of vertical degrees in the Reeb decomposition (Remark <a href="#rem:descartes-leptons" data-reference-type="ref" data-reference="rem:descartes-leptons">3.7</a>). Evaluating the mass identity at successive levels of the brane tower (Definition <a href="#def:recursive-brane-tower" data-reference-type="ref" data-reference="def:recursive-brane-tower">2.2</a>) may yield theoretical predictions for lepton and hadron mass ratios.*

</div>

##### Existing data sets.

- CODATA recommended values of fundamental constants (electron, muon, tau masses; fine-structure constant).

- Particle Data Group (PDG) Review of Particle Physics.

- Precision atomic spectroscopy measurements (hydrogen, muonium, positronium).

##### Planned observations.

- Muon $g-2$ experiment at Fermilab (E989): precision measurement of the anomalous magnetic moment.

- COMET and Mu2e experiments: searches for charged lepton flavour violation that would constrain inter-generation mixing in the Reeb decomposition.

##### Potential new experiments.

- High-precision comparisons of the electron–muon and muon–tau mass ratios against values computed from the mass identity with specific $q$ and $\chi(E)$.

- Lattice calculations of QOU vortex masses to compare with QCD lattice results.

### Quantum Hall Effect of Photons

<div id="rem:photonic-hall" class="remark">

**Remark 6.5** (Photonic quantum Hall effect and $q$-deformed braiding). *Recent experiments have demonstrated a quantized Hall drift in photonic Chern insulators . In the QOU framework, bosons are purely horizontal $q$-harmonic forms (Definition <a href="#def:boson" data-reference-type="ref" data-reference="def:boson">1.20</a>), and the Hall conductance arises from the Chern number of the bulk bundle restricted to the horizontal distribution. The $q$-deformation modifies the quantisation condition, predicting fractional corrections of order $1 - q$ to the Hall conductance.*

</div>

##### Existing data sets.

- Frequency-encoded photonic Chern insulator measurements of Chénier et al. .

- Many-body interference data in kagome lattices .

- Chiral phonon experiments in rare-earth halides .

##### Planned observations.

- Extension of photonic Chern insulator experiments to tunable $q$-regimes via lattice-geometry variation.

- Fractional quantum Hall experiments in synthetic photonic systems with controllable topology.

##### Potential new experiments.

- Measurement of Hall conductance in photonic lattices at varying effective $q$ parameters, seeking the $1 - q$ correction predicted by the quantum Planck constant (Definition <a href="#def:quantum-planck-constant" data-reference-type="ref" data-reference="def:quantum-planck-constant">1.11</a>).

- Cold-atom realisations of $\mathrm{SU}(2)$ gauge fields in optical lattices, testing the $q$-deformed braiding statistics of Chapter <a href="#chap:path-integrals-braiding" data-reference-type="ref" data-reference="chap:path-integrals-braiding">4</a>.

### Lepton Anomalies and Reeb-Decomposition Tests

<div id="rem:lepton-discrepancies" class="remark">

**Remark 6.6** (Electron–muon discrepancies). *The QOU framework predicts that lepton generations are distinguished by the vertical degree of the Reeb decomposition (Remark <a href="#rem:descartes-leptons" data-reference-type="ref" data-reference="rem:descartes-leptons">3.7</a>). Discrepancies between electron and muon interactions — such as the anomalous magnetic moment tensions and lepton flavour universality violations observed at the $B$-factories — may reflect the distinct Reeb-vertical structure of each generation rather than new heavy-particle loops.*

</div>

##### Existing data sets.

- Muon $g-2$ results from BNL E821 and Fermilab E989.

- LHCb $R_K$ and $R_{K^*}$ measurements of lepton flavour universality.

- Belle II early data on $B$-meson decays.

##### Planned observations.

- Full Belle II data set ($\sim$<!-- -->50 ab$^{-1}$ integrated luminosity): precision tests of lepton universality in $\tau$ decays.

- HL-LHC (High-Luminosity LHC): extended reach for rare lepton flavour violating processes.

##### Potential new experiments.

- Precision measurements of the proton charge radius via muonic vs. electronic hydrogen to probe generation-dependent coupling to the substrate parameter.

- Electron–muon scattering experiments (e.g. MUonE at CERN) to directly test the $q$-dependent corrections to the electromagnetic vertex.

### Informational and Entropic Gravity Tests

<div id="rem:entropic-gravity" class="remark">

**Remark 6.7** (Entropic forces and the substrate parameter). *The substrate parameter $q$ (Definition <a href="#def:substrate-parameter" data-reference-type="ref" data-reference="def:substrate-parameter">1.9</a>) encodes the coupling between the Levi form and the gauge curvature. In the near-classical regime $q \to 1$, gravity emerges as a geometric back-reaction (Remark <a href="#rem:gr-substrate-geometry" data-reference-type="ref" data-reference="rem:gr-substrate-geometry">1.23</a>). Recent work on the quantum mechanics of entropic forces  provides a complementary perspective: the entropic interpretation may correspond to the thermodynamic limit of the $q$-deformed partition function on the brane tower.*

</div>

##### Existing data sets.

- Cavendish-type torsion balance experiments (e.g. Eöt-Wash group).

- Casimir force measurements at micrometre scales.

- Neutron interferometry (gravity resonance spectroscopy).

##### Planned observations.

- MICROSCOPE follow-up missions: improved equivalence principle tests in space.

- Atom interferometry experiments (MAGIS, AION, ZAIGA) probing gravitational decoherence.

##### Potential new experiments.

- Entanglement-assisted gravity experiments testing whether gravitational interactions preserve quantum coherence as predicted by the $q$-deformed field equations.

- High-precision measurements of Casimir forces in geometries designed to isolate contributions from $q$-deformed vacuum fluctuations.

### Crystal Lattice Resonance and Substrate Telescopes

<div id="rem:crystal-resonance" class="remark">

**Remark 6.8** (Quantum resonance in crystal lattices). *A periodic crystal lattice provides a macroscopic, coherent probe of the substrate parameter $q$ (Definition <a href="#def:substrate-parameter" data-reference-type="ref" data-reference="def:substrate-parameter">1.9</a>). The discrete translational symmetry of the lattice selects a set of reciprocal vectors that couple to the horizontal distribution of the CR manifold $M$. Where the lattice spacing is commensurate with the characteristic scale of a $q$-torsion leaf (Definition <a href="#def:q-torsion-leaf" data-reference-type="ref" data-reference="def:q-torsion-leaf">1.17</a>), a resonance condition is satisfied: the $q$-harmonic forms (Definition <a href="#def:q-harmonic-form" data-reference-type="ref" data-reference="def:q-harmonic-form">1.13</a>) on the brane constructively interfere with the phonon modes of the crystal, amplifying vacuum fluctuations at specific frequencies. The resonance frequency $\nu_{\mathrm{res}}$ is predicted to depend on the local value of $q$ and the lattice geometry.*

</div>

<div id="rem:substrate-telescope" class="remark">

**Remark 6.9** (Substrate Telescopes). *The directional dependence of $q$-torsion suggests a new class of detector: the *Substrate Telescope*. A large, high-purity single crystal is slowly rotated while the variation of vacuum noise power or phonon resonance efficiency is recorded as a function of orientation. Because the $q$-torsion leaves carry a preferred direction inherited from the $q$-deformed Reeb flow (Definition <a href="#def:q-reeb-flow" data-reference-type="ref" data-reference="def:q-reeb-flow">1.16</a>), the noise spectrum should exhibit a modulation correlated with the crystal’s orientation relative to the bulk bundle. This is conceptually analogous to a Weber-bar gravitational wave detector, but targets the anisotropy of the substrate parameter rather than metric strain.*

</div>

##### Existing data sets.

- Many-body interference measurements in kagome crystals , which probe coherent lattice-scale quantum effects.

- Chiral phonon spectroscopy in rare-earth halide crystals , demonstrating orientation-dependent effective magnetic fields from lattice vibrations.

- High-$Q$ quartz bulk acoustic wave (BAW) oscillator noise measurements, which record excess phase noise beyond thermal limits.

- Precision Casimir-effect experiments using crystalline surfaces (e.g. silicon and gold single crystals).

- Resonant-mass gravitational wave detector data (e.g. AURIGA, NAUTILUS bar detectors), which recorded orientation-dependent noise floors in cryogenic crystalline bars.

##### Planned observations.

- Next-generation phononic crystal experiments with tunable lattice constants, enabling a systematic scan of the resonance condition across different effective $q$ regimes.

- Extension of kagome and pyrochlore quantum-interference experiments to larger single crystals with controlled rotational staging.

- Cryogenic SQUID-based noise spectroscopy on rotating high-purity sapphire or silicon crystals.

##### Potential new experiments.

- A dedicated Substrate Telescope prototype: a cryogenically cooled, slowly rotating single crystal (e.g. ultra-pure silicon or quartz) instrumented with SQUID magnetometers and phonon sensors, searching for orientation-dependent modulation of the vacuum noise floor.

- Comparative resonance measurements across crystals with different lattice symmetries (cubic, hexagonal, trigonal) to map the dependence of $\nu_{\mathrm{res}}$ on lattice geometry and thereby constrain the local value of $q$.

- Re-analysis of archival resonant-bar detector data (AURIGA, NAUTILUS, EXPLORER) for residual orientation-dependent signals consistent with $q$-torsion anisotropy rather than gravitational wave backgrounds.

# Speculations

[^1]: World Health Organization
