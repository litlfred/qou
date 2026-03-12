---
abstract: |
  This paper presents a mathematical framework for the Quantum Observable Universe (QOU). We introduce the notion of quantum torsion in this setting, study its lifting to higher categorical structures, and examine the resulting interpretational and experimental consequences. Speculative extensions are discussed in the final chapter.
author:
- Frederick Carl Leitner[^1]
bibliography:
- references.bib
date: 2026-03-12
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

<div id="ex:descartes" class="example">

**Example 1.8** (Descartes universe). *Let $M = \mathbb{C}^2$ and assume $\chi(E) = -6$. We call the resulting $\mathbb{C}$ quantum observable universe the *Descartes universe*.*

<div class="center">

**“Je pense, donc je suis.”  
— René Descartes**

</div>

</div>

<div id="rem:descartes-cmb" class="remark">

**Remark 1.9** (Descartes universe and the CMB). *In the Descartes universe (Example <a href="#ex:descartes" data-reference-type="ref" data-reference="ex:descartes">1.8</a>), the Euler characteristic $\chi(E) = -6$ constrains the topology of the bulk bundle $E$. The $q$-harmonic forms on this bundle (Definition <a href="#def:q-harmonic-form" data-reference-type="ref" data-reference="def:q-harmonic-form">1.16</a>) determine the spectrum of stable excitations. In the regime $q(p) \to 1$ (near-classicality), the zero-modes of $\Delta_q$ reproduce the thermal fluctuation spectrum of the Cosmic Microwave Background: the Hodge numbers of $E$ govern the multiplicity of angular modes, and the negative Euler characteristic forces a non-trivial distribution of these modes across the CR manifold $M = \mathbb{C}^2$.*

</div>

<div id="rem:descartes-leptons" class="remark">

**Remark 1.10** (Electrons, muons and the Reeb decomposition). *The Reeb decomposition (Definition <a href="#def:reeb-decomposition" data-reference-type="ref" data-reference="def:reeb-decomposition">1.17</a>) applied to the Descartes universe yields two classes of fermionic excitations (Definition <a href="#def:fermion" data-reference-type="ref" data-reference="def:fermion">1.22</a>). The degree of the vertical component $\alpha_V$ distinguishes them: forms with $\deg\alpha_V = 1$ correspond to electrons, while forms with $\deg\alpha_V = 2$ correspond to muons. More generally, each additional unit of vertical degree is identified with a successive lepton generation. The constraint $\chi(E) = -6$ bounds the number of such generations, since the Hodge decomposition of $E$ admits only finitely many independent vertical harmonic forms.*

</div>

<div id="rem:descartes-chirality" class="remark">

**Remark 1.11** (Chirality as Reeb orientation). *The Reeb vector field $\xi$ on the CR manifold $M$ carries a natural orientation: the sign of the contact form $\theta(\xi) = 1$ singles out a preferred direction along the vertical distribution. Left-handed and right-handed chiralities correspond to the two orientations of $\xi$ relative to the complex structure of $M$. For fermions (Definition <a href="#def:fermion" data-reference-type="ref" data-reference="def:fermion">1.22</a>), the vertical component $\alpha_V$ transforms with a definite sign under reversal of $\xi$, so chirality is encoded in the $\pm$-eigenspaces of the Reeb involution $\xi \mapsto -\xi$. Bosons (Definition <a href="#def:boson" data-reference-type="ref" data-reference="def:boson">1.23</a>), being purely horizontal, are chirality-blind — consistent with the observed parity invariance of the electromagnetic and strong interactions.*

</div>

<div id="def:substrate-parameter" class="definition">

**Definition 1.12** (Substrate parameter). *Let $(M, G, E)$ be a $\mathbb{C}$ quantum observable universe with connection $A$. Write $F_A = dA + A \wedge A$ for the curvature and let $F_A^+$ denote its self-dual part. Let $L \in \Gamma(T^*M \otimes \overline{T^*M})$ be the *Levi form*, a Hermitian form on the tangent bundle of $M$. The *substrate parameter* is the function $q \colon M \to \mathbb{R}$ defined by $$q(p) \;=\; \exp\!\bigl(-\lVert L \wedge F_A^+ \rVert(p)\bigr),
  \qquad p \in M.$$*

</div>

<div id="def:quantum-gauge-group" class="definition">

**Definition 1.13** (Quantum Gauge Group). *Let $(M, G, E)$ be a $\mathbb{C}$ quantum observable universe with substrate parameter $q$ (Definition <a href="#def:substrate-parameter" data-reference-type="ref" data-reference="def:substrate-parameter">1.12</a>). The *quantum gauge group* is the quantum group $\mathrm{SU}_q(2)$ obtained by deforming the structure group $G = \mathrm{SU}(2)$ at the parameter $q$.*

</div>

<div id="def:quantum-planck-constant" class="definition">

**Definition 1.14** (Quantum Planck Constant). *Let $(M, G, E)$ be a $\mathbb{C}$ quantum observable universe with substrate parameter $q$ (Definition <a href="#def:substrate-parameter" data-reference-type="ref" data-reference="def:substrate-parameter">1.12</a>). The *quantum Planck constant* is the function $\hbar_q \colon M \to \mathbb{R}$ defined by $$\hbar_q(p) \;=\; 1 - q(p), \qquad p \in M.$$ As $q(p) \to 1$ (classicality), $\hbar_q(p) \to 0$ and quantum effects vanish; as $q(p) \to 0$ (deep-quantum regime), $\hbar_q(p) \to 1$.*

</div>

<div id="rem:j1e-local-states" class="remark">

**Remark 1.15** ($J^1E$ as the space of local states). *The jet bundle $J^1 E$ serves as the space of local states of the $\mathbb{C}$ quantum observable universe. The classical gauge dynamics, encoded by the *instanton connection* $A$ (Lemma <a href="#lem:unique-connection" data-reference-type="ref" data-reference="lem:unique-connection">1.4</a>), are weighted by the substrate parameter $q$ (Definition <a href="#def:substrate-parameter" data-reference-type="ref" data-reference="def:substrate-parameter">1.12</a>) to define the quantum field algebra $\mathrm{SU}_q(2)$ (Definition <a href="#def:quantum-gauge-group" data-reference-type="ref" data-reference="def:quantum-gauge-group">1.13</a>).*

</div>

<div id="def:q-harmonic-form" class="definition">

**Definition 1.16** ($q$-Harmonic form (Particle)). *Let $(M, G, E)$ be a $\mathbb{C}$ quantum observable universe with substrate parameter $q$ (Definition <a href="#def:substrate-parameter" data-reference-type="ref" data-reference="def:substrate-parameter">1.12</a>). Let $d_q$ denote the $q$-deformed exterior derivative on the CR manifold $M$. A *particle* is a section $\alpha \in \Gamma(M,\, \Lambda^k T^*M \otimes J^1 E)$ that is $q$-harmonic, i.e. lies in the kernel of the $q$-Laplacian: $$\Delta_q \alpha
  \;=\; (d_q\,\delta_q + \delta_q\,d_q)\,\alpha
  \;=\; 0,$$ where $\delta_q$ is the formal adjoint of $d_q$. The condition $\Delta_q\alpha = 0$ ensures that the form sits in a ground state of the $q$-viscosity.*

</div>

<div id="def:reeb-decomposition" class="definition">

**Definition 1.17** (Reeb decomposition). *Let $M$ be a CR manifold equipped with a contact form $\theta$ and let $\xi$ denote the associated *Reeb vector field*, characterised by $\iota_\xi\,d\theta = 0$ and $\theta(\xi) = 1$. Every differential form $\alpha$ on $M$ decomposes as $$\alpha \;=\; \alpha_H + \alpha_V,
  \qquad\text{where}\qquad
  \iota_\xi\,\alpha_V \neq 0,$$ with $\alpha_H$ the *horizontal component* (annihilated by $\iota_\xi$) and $\alpha_V$ the *vertical component* (having a non-trivial contraction with $\xi$).*

</div>

<div id="def:q-reeb-vector-field" class="definition">

**Definition 1.18** ($q$-Deformed Reeb vector field). *Let $(M, G, E)$ be a $\mathbb{C}$ quantum observable universe with substrate parameter $q$ (Definition <a href="#def:substrate-parameter" data-reference-type="ref" data-reference="def:substrate-parameter">1.12</a>) and Reeb vector field $\xi$ (Definition <a href="#def:reeb-decomposition" data-reference-type="ref" data-reference="def:reeb-decomposition">1.17</a>). The *$q$-deformed Reeb vector field* is the vector field $\xi_q$ on $M$ defined by its action on smooth functions $f \in C^\infty(M)$: $$\xi_q(f) \;=\; q\,\xi(f) + (1 - q)\,[\xi, X_f]_q,$$ where $X_f$ is the horizontal lift of $\mathrm{grad}\,f$ to $H$ and $[\,\cdot\,,\cdot\,]_q$ denotes the $q$-deformed Lie bracket on $\mathfrak{X}(M)$. When $q = 1$, one recovers the classical Reeb field $\xi_1 = \xi$.*

</div>

<div id="def:q-reeb-flow" class="definition">

**Definition 1.19** ($q$-Deformed Reeb flow). *Let $\xi_q$ be the $q$-deformed Reeb vector field (Definition <a href="#def:q-reeb-vector-field" data-reference-type="ref" data-reference="def:q-reeb-vector-field">1.18</a>). The *$q$-deformed Reeb flow* is the one-parameter family of diffeomorphisms $\phi_t^q \colon M \to M$, $t \in \mathbb{R}$, generated by $\xi_q$: $$\frac{d}{dt}\,\phi_t^q \;=\; \xi_q \circ \phi_t^q,
  \qquad \phi_0^q = \mathrm{id}_M.$$*

</div>

<div id="def:q-torsion-leaf" class="definition">

**Definition 1.20** ($q$-Torsion leaf). *Let $H = \ker\theta \subset TM$ be the horizontal distribution on the CR manifold $M$. A *$q$-torsion leaf* is a maximal integral submanifold $L \hookrightarrow M$ of $H$ that is invariant under the $q$-deformed Reeb flow (Definition <a href="#def:q-reeb-flow" data-reference-type="ref" data-reference="def:q-reeb-flow">1.19</a>): $$T_p L \;\subset\; H_p
  \quad\text{for all } p \in L,
  \qquad\text{and}\qquad
  \phi_t^q(L) = L
  \quad\text{for all } t \in \mathbb{R}.$$*

</div>

<div id="rem:q-torsion-leaf-minimum" class="remark">

**Remark 1.21** ($q$-Torsion leaves as energy minima). *Let $A_q$ denote the $q$-deformed connection on $E$ and define the $q$-curvature $$\Omega_q \;=\; dA_q + \tfrac{1}{2}\,[A_q,\, A_q]_q.$$ A $q$-torsion leaf $L$ (Definition <a href="#def:q-torsion-leaf" data-reference-type="ref" data-reference="def:q-torsion-leaf">1.20</a>) is a local minimum of $\lVert\Omega_q\rVert$ restricted to the horizontal distribution: the invariance of $L$ under $\phi_t^q$ forces the first variation of $\lVert\Omega_q|_L\rVert$ to vanish, so $L$ sits in a $q$-curvature well. Physically, a $q$-torsion leaf represents a region of the CR manifold where the gauge curvature is minimised and the $q$-deformed dynamics are in equilibrium.*

</div>

<div id="def:fermion" class="definition">

**Definition 1.22** (Fermion). *A *fermion* is a $q$-harmonic form (Definition <a href="#def:q-harmonic-form" data-reference-type="ref" data-reference="def:q-harmonic-form">1.16</a>) that has a non-trivial vertical component in the Reeb decomposition (Definition <a href="#def:reeb-decomposition" data-reference-type="ref" data-reference="def:reeb-decomposition">1.17</a>): $$\Delta_q\,\alpha = 0
  \qquad\text{and}\qquad
  \iota_\xi\,\alpha_V \neq 0.$$*

</div>

<div id="def:boson" class="definition">

**Definition 1.23** (Boson). *A *boson* is a $q$-harmonic form (Definition <a href="#def:q-harmonic-form" data-reference-type="ref" data-reference="def:q-harmonic-form">1.16</a>) that is purely horizontal in the Reeb decomposition (Definition <a href="#def:reeb-decomposition" data-reference-type="ref" data-reference="def:reeb-decomposition">1.17</a>): $$\Delta_q\,\alpha = 0
  \qquad\text{and}\qquad
  \alpha = \alpha_H
  \quad(\text{equivalently, } \iota_\xi\,\alpha = 0
        \text{ by Definition~\ref{def:reeb-decomposition}}).$$*

</div>

<div id="rem:reeb-physical" class="remark">

**Remark 1.24** (Physical interpretation of the Reeb decomposition). *The Reeb vector field $\xi$ singles out the direction of internal spin on the CR manifold. Forms that “see” this direction (fermions) carry half-integer spin; forms confined to the horizontal distribution (bosons) do not couple to the Reeb flow and carry integer spin. The decomposition $\alpha = \alpha_H + \alpha_V$ is therefore the geometric origin of the spin–statistics distinction in this framework.*

</div>

<div id="rem:q-harmonic-physical" class="remark">

**Remark 1.25** (Physical interpretation of $q$-harmonicity). *The $q$-Laplacian $\Delta_q$ encodes the $q$-deformed viscosity of the CR geometry. A $q$-harmonic form is a zero-mode of this operator and thus represents a stable excitation — a particle — of the quantum observable universe. The deformation parameter $q$ interpolates between the classical regime ($q \to 1$, where $\Delta_q$ reduces to the Hodge Laplacian) and the deep-quantum regime ($q \to 0$), so the notion of “particle” is itself $q$-dependent.*

</div>

<div id="rem:gr-substrate-geometry" class="remark">

**Remark 1.26** (General Relativity as the “Substrate Geometry”). *In this model the metric is effectively replaced by the Levi form $L$ and its coupling to the gauge curvature $F_A$. Gravity is expressed through the Variational Bicomplex as the back-reaction of the gauge fields on the CR manifold $M$.*

*The Einstein–Hilbert action is recovered by examining the variation of the action $S_q$ with respect to the Levi form $L$: $$\frac{\delta S_q}{\delta L}
  \;\implies\;
  G_{\mu\nu} \;\sim\; T_{\mu\nu}^{(q)},$$ where $T_{\mu\nu}^{(q)}$ is a *quantum-weighted* stress-energy tensor. Because $q(p) = \exp\!\bigl(-\lVert L \wedge F^+\rVert\bigr)$, the geometry of the brane $M$ is forced to curve to accommodate the tension of the $\mathrm{SU}(2)$ instantons.*

</div>

<div id="rem:schrodinger-jet-coaction" class="remark">

**Remark 1.27** (The Schrödinger Equation as “Jet Co-action”). *The Schrödinger equation describes the evolution of a state in the fibre $\mathbb{CP}$. In the jet-bundle framework this is expressed as the condition of parallel transport along the connection $A$.*

*For a section $\psi \in \Gamma(E)$, the Schrödinger dynamics are found in the kernel of the $q$-deformed covariant derivative on $J^1 E$: $$i\,\hbar_q(p)\, D_A \psi \;=\; \hat{H}_q\, \psi,$$ where $\hat{H}_q$ is the $q$-deformed Hamiltonian operator and:*

- *$\hbar_q(p) = 1 - q(p)$: the quantum Planck constant (Definition <a href="#def:quantum-planck-constant" data-reference-type="ref" data-reference="def:quantum-planck-constant">1.14</a>) is a local field;*

- *$D_A = d + A$: the connection $A$ (the instanton) acts as the potential.*

*As $q(p) \to 1$ (classicality), the uncertainty vanishes and the wave-like nature of the section freezes into a classical trajectory.*

</div>

<div id="rem:main-commutative-diagram" class="remark">

**Remark 1.28** (Main Commutative Diagram). *The relationship between these two seemingly disparate equations is captured by the main commutative diagram of the $\mathbb{C}$-quantum universe, where $\mathbf{E}$ denotes the Euler–Lagrange operator. The link is the substrate parameter $q(p)$: $$\begin{CD}
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
  d_{A_n}^*\,\alpha = 0,$$ where the Hodge-star operator is induced by the Hermitian metric that the Levi form $L$ (Definition <a href="#def:substrate-parameter" data-reference-type="ref" data-reference="def:substrate-parameter">1.12</a>) defines on the horizontal distribution. The index $i$ runs over $1 \leq i \leq b_1(E_n)$ (Remark <a href="#rem:betti-numbers-brane" data-reference-type="ref" data-reference="rem:betti-numbers-brane">2.5</a>).*

*At the base level $n = 0$, with Euler characteristic $\chi(M) = 3$, there are three primary basis vectors $\{\,\phi_1,\, \phi_2,\, \phi_3\,\}$. At level $n = 1$ the basis lifts: the new basis includes the original modes together with their $J^1$ prolongations (Proposition <a href="#prop:jet-prolongation" data-reference-type="ref" data-reference="prop:jet-prolongation">2.1</a>), which are the first-order resolutions of the base flows.*

</div>

<div id="rem:weight-space-decomposition" class="remark">

**Remark 2.7** (Weight-space decomposition of the harmonic basis). *The adjoint bundle $\mathrm{ad}\, E_n$ has fibre $\mathfrak{su}(2)$. Via the weight-space decomposition of $\mathrm{SU}(2)$, the harmonic basis of $\mathcal{H}^1(E_n,\, \mathrm{ad}\, E_n)$ splits into two families.*

**Longitudinal modes.* These forms constitute the $\mathrm{U}(1)$ backbone of the decomposition. They take values in the Cartan subalgebra of $\mathfrak{su}(2)$ and have the geometric form $\omega^0 \otimes H$, where $H$ is the diagonal generator. They represent steady-state laminar flows aligned with the $\mathrm{U}(1)$ subgroup. If the bundle splits at a monodromy fixed point, these are the only modes that survive; they correspond to the magnetic flux of the stable vortices.*

**Ladder modes.* These are the raising and lowering vortices of the decomposition. They take values in the off-diagonal generators $E_\pm$ of $\mathfrak{su}(2)$ and have the geometric form $\omega^\pm \otimes E_\pm$. They describe the entangling flows that twist the $\mathbb{CP}^1$ fibre as one moves along the brane. These modes are responsible for the non-commutativity in the $\mathrm{SU}_q(2)$ algebra (Definition <a href="#def:direct-limit-algebra" data-reference-type="ref" data-reference="def:direct-limit-algebra">2.10</a>).*

*In the $1$-jet bundle $J^1 E_n$ (Remark <a href="#rem:j1e-local-states" data-reference-type="ref" data-reference="rem:j1e-local-states">1.15</a>), each basis element $\alpha$ is a pair consisting of a *value* (the direction of the $\mathrm{SU}(2)$ flow in the fibre) and a *momentum* (the gradient of that flow relative to the complex structure of the brane).*

</div>

<div id="rem:algebraic-filter" class="remark">

**Remark 2.8** (The algebraic filter). *Let $\alpha$ be a harmonic $1$-form in the basis of Remark <a href="#rem:q-harmonic-basis-brane" data-reference-type="ref" data-reference="rem:q-harmonic-basis-brane">2.6</a>. Its *signature* is determined by its commutator with the curvature $F_A$ (Definition <a href="#def:substrate-parameter" data-reference-type="ref" data-reference="def:substrate-parameter">1.12</a>).*

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

**Definition 2.10** ($\mathbb{C}$ Quantum Observable Universe as Direct Limit). *Let $\{E_n\}_{n \geq 1}$ be the recursive brane tower (Definition <a href="#def:recursive-brane-tower" data-reference-type="ref" data-reference="def:recursive-brane-tower">2.2</a>) with substrate parameters $q_n$ (Definition <a href="#def:substrate-parameter" data-reference-type="ref" data-reference="def:substrate-parameter">1.12</a>) at each level. The *$\mathbb{C}$ quantum observable universe* is the direct limit algebra $$\mathcal{A}_\infty
  \;=\;
  \varinjlim\,
  \Gamma\!\bigl(J^1 E_n,\, \mathrm{SU}_{q_n}(2)\bigr).$$*

</div>

<div id="rem:jet-shell" class="remark">

**Remark 2.11** (Jet Shell of the universe). *In the limit $n \to \infty$, the infinite jet bundle $J^\infty E = \varprojlim\, J^k E$ becomes the *jet shell* of the universe. All finite-level brane data are encoded in this pro-finite structure, and the algebra $\mathcal{A}_\infty$ (Definition <a href="#def:direct-limit-algebra" data-reference-type="ref" data-reference="def:direct-limit-algebra">2.10</a>) acts naturally on sections of the jet shell.*

</div>

<div id="rem:vacuum-state" class="remark">

**Remark 2.12** (The Vacuum State). *The *physical vacuum* is a state $\omega \colon \mathcal{A}_\infty \to \mathbb{C}$ on the direct limit algebra (Definition <a href="#def:direct-limit-algebra" data-reference-type="ref" data-reference="def:direct-limit-algebra">2.10</a>) that is invariant under the global $\mathrm{SU}(2)$ action and the recursive $q$-deformations: $$\omega(g \cdot a) = \omega(a)
  \quad\text{for all } g \in \mathrm{SU}(2),\;
  a \in \mathcal{A}_\infty.$$*

</div>

<div id="rem:mass-geometric-drag" class="remark">

**Remark 2.13** (Mass as geometric drag). *In this recursive $\mathrm{SU}(2)$ tower (Definition <a href="#def:recursive-brane-tower" data-reference-type="ref" data-reference="def:recursive-brane-tower">2.2</a>), mass is not an intrinsic property of a point-particle but rather a measure of the *geometric drag* (or “viscosity”) encountered by a stable vortex as it propagates through the $1$-jet bundle $J^1 E_n$. When $q \neq 1$ the field is non-commutative: moving the vortex requires a continuous rearrangement of the $\mathrm{SU}_q(2)$ algebra (Definition <a href="#def:direct-limit-algebra" data-reference-type="ref" data-reference="def:direct-limit-algebra">2.10</a>) across the fibres.*

</div>

<div id="def:mass-identity" class="definition">

**Definition 2.14** (Mass Identity). *Let $(M, G, E)$ be a $\mathbb{C}$ quantum observable universe with substrate parameter $q$ (Definition <a href="#def:substrate-parameter" data-reference-type="ref" data-reference="def:substrate-parameter">1.12</a>), connection $A$, Levi form $L$, and self-dual curvature $F^+$. Let $\gamma$ be a closed cycle encircling the vortex filament. The *inertial mass* $m$ of a stable vortex is $$m \;\propto\; \oint_\gamma \lVert \nabla_A\, q \rVert
               \cdot \lVert L \wedge F^+ \rVert\,.$$*

</div>

# Interpretations

# Experimental Evidence

# Speculations

[^1]: World Health Organization
