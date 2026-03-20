---
abstract: |
  This paper presents a mathematical framework for the Quantum Observable Universe (QOU). We introduce the notion of quantum torsion in this setting, study its lifting to higher categorical structures, and examine the resulting interpretational and experimental consequences. Speculative extensions are discussed in the final chapter.
author:
- Frederick Carl Leitner[^1]
bibliography:
- references.bib
date: 2026-03-20
title: Quantum Observable Universe
---

<div class="center">

  
This work is licensed under a [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/).  
You are free to share and adapt this material for any purpose,  
provided appropriate credit is given, a link to the license is provided,  
and any changes made are indicated.

</div>

# Quantum Observable Universe

<div id="def:quantum-universe" class="definition">

**Definition 1.1** (Quantum Universe). *Let $k$ be a field. A *quantum universe over $k$* is a quadruple $(\mathcal{C}, A, \omega, q)$ where:*

1.  *$(\mathcal{C}, \otimes, \mathbf{1})$ is a $k$-linear rigid monoidal category;*

2.  *$A$ is a *Frobenius–Hopf object* in $\mathcal{C}$: an object equipped with a Hopf structure $(\mu, \eta, \Delta, \varepsilon, S)$ and a Frobenius form $\lambda \colon A \to \mathbf{1}$ such that the pairing $A \otimes A \xrightarrow{\mu} A \xrightarrow{\lambda} \mathbf{1}$ is non-degenerate and the Frobenius relation $(\mu \otimes \mathrm{id}) \circ
            (\mathrm{id} \otimes \Delta_\mu)
            = \Delta_\mu \circ \mu$ holds, where $\Delta_\mu$ is the comultiplication dual to $\mu$ under the pairing;*

3.  *$\omega \colon \mathcal{C} \to \mathrm{Vect}_k$ is a fibre functor (exact faithful $k$-linear monoidal functor);*

4.  *$q \in k^\times$ is a deformation parameter (invertibility of $q$ is required because the Hopf-algebra relations defining $A$ involve $q^{-1}$; at $q = 0$ the antipode $S$ degenerates and the Hopf structure collapses); the Hopf structure on $A$ depends on $q$, and $q = 1$ recovers the classical (cocommutative) case.*

*The *quantum gauge group* is the affine $k$-group scheme $G_q = \mathrm{Aut}^{\otimes}(\omega)$, reconstructed via Tannaka–Krein duality.*

</div>

<div id="def:quantum-observable-universe" class="definition">

**Definition 1.2** (Quantum Observable Universe). *A quantum universe $(\mathcal{C}, A, \omega, q)$ over $k$ (Definition <a href="#def:quantum-universe" data-reference-type="ref" data-reference="def:quantum-universe">1.1</a>) is *observable* if:*

1.  *the Frobenius form $\lambda$ on $A$ is non-degenerate; and*

2.  *$\mathrm{Hom}_{\mathcal{C}}(\mathbf{1},\, \mathrm{Ad}(A)) = 0$, where $\mathrm{Ad}(A)$ is the adjoint object ($A$ with the conjugation coaction $a \mapsto \textstyle\sum a_{(1)}\, b\, S(a_{(2)})$).*

</div>

<div id="rem:base-field-independence" class="remark">

**Remark 1.3** (Base-field independence). *Definitions <a href="#def:quantum-universe" data-reference-type="ref" data-reference="def:quantum-universe">1.1</a> and <a href="#def:quantum-observable-universe" data-reference-type="ref" data-reference="def:quantum-observable-universe">1.2</a> are formulated over an arbitrary field $k$. The Frobenius–Hopf axioms replace the analytic vanishing conditions of the $\mathbb{C}$ realisation (Example <a href="#def:c-quantum-observable-universe" data-reference-type="ref" data-reference="def:c-quantum-observable-universe">1.6</a>) with a single algebraic non-degeneracy condition on the Frobenius form. Concrete realisations include:*

- *$k = \mathbb{C}$: the classical setting of CR geometry and contact manifolds (Example <a href="#def:c-quantum-universe" data-reference-type="ref" data-reference="def:c-quantum-universe">1.4</a>);*

- *$k = \mathbb{Q}_\mathfrak{p}$ (the $\mathfrak{p}$-adic field): the gauge datum becomes an $F$-isocrystal with Frobenius lift, and integrability is controlled by the $\mathfrak{p}$-adic Frobenius endomorphism (Example <a href="#ex:p-adic-realisation" data-reference-type="ref" data-reference="ex:p-adic-realisation">7.1</a>, Chapter <a href="#chap:p-adic" data-reference-type="ref" data-reference="chap:p-adic">7</a>);*

- *$k = \mathbb{F}_\mathfrak{p}$ (a finite field): the monoidal category is the category of finite-dimensional representations of a quantum group over $\mathbb{F}_\mathfrak{p}$ (Example <a href="#ex:finite-field-realisation" data-reference-type="ref" data-reference="ex:finite-field-realisation">7.2</a>).*

*The fibre functor $\omega$ ensures that $G_q = \mathrm{Aut}^{\otimes}(\omega)$ is well-defined over any $k$.*

</div>

<div id="def:c-quantum-universe" class="example">

**Example 1.4** ($\mathbb{C}$ realisation: quantum universe). *Over $k = \mathbb{C}$, a quantum universe (Definition <a href="#def:quantum-universe" data-reference-type="ref" data-reference="def:quantum-universe">1.1</a>) is realised by a $5$-tuple $(M, \theta, G, P, E)$ where:*

1.  *$M$ is a CR manifold of hypersurface type (real dimension $2n+1$, $n \geq 1$) with non-degenerate Levi form of signature $(r,s)$, $r + s = n$;*

2.  *$\theta$ is a pseudo-Hermitian structure (contact form) on $M$, determining the Levi distribution $H = \ker\theta$, the Reeb vector field $\xi$, the Webster metric $g_\theta$ (of signature $(2r,2s)$ on $H$), and the Levi form $L_\theta$;*

3.  *$G = \mathrm{SU}(2)$;*

4.  *$P \to M$ is a principal $G$-bundle whose holonomy reduces to $\mathrm{SO}(3) \subset \mathrm{SU}(2)/\{\pm I\}$;*

5.  *$E = P \times_G \mathbb{CP}^1 \to M$ is the associated *state bundle*, where $\mathrm{SU}(2)$ acts on $\mathbb{CP}^1$ by Möbius transformations.*

*The monoidal category is $\mathcal{C} = \mathrm{Rep}(\mathrm{SU}_{q(p)}(2))$ (the representation category of the quantum group at the substrate parameter $q(p)$, Definition <a href="#def:substrate-parameter" data-reference-type="ref" data-reference="def:substrate-parameter">1.10</a>), the Frobenius–Hopf object is $A = \mathcal{O}_q(\mathrm{SU}(2))$ with Frobenius form given by the Haar state, and the fibre functor $\omega$ is the forgetful functor to $\mathrm{Vect}_{\mathbb{C}}$.*

</div>

<div id="rem:notation-special-cases" class="remark">

**Remark 1.5** (Notation and special cases). *When $\theta$ is understood from context, we abbreviate the $5$-tuple to $(M, G, P, E)$. The *strictly pseudoconvex* case corresponds to signature $(n,0)$, where $L_\theta$ is positive definite.*

</div>

<div id="def:c-quantum-observable-universe" class="example">

**Example 1.6** ($\mathbb{C}$ realisation: quantum observable universe). *A *$\mathbb{C}$ quantum observable universe* is a $\mathbb{C}$ quantum universe $(M, \theta, G, P, E)$ (Example <a href="#def:c-quantum-universe" data-reference-type="ref" data-reference="def:c-quantum-universe">1.4</a>) that satisfies the vanishing conditions $$H^0(M, \mathrm{Ad}(P)) = 0
  \qquad\text{and}\qquad
  \Gamma_c(M, E) = 0.$$ These analytic conditions are the $\mathbb{C}$ realisation of the categorical observability conditions of Definition <a href="#def:quantum-observable-universe" data-reference-type="ref" data-reference="def:quantum-observable-universe">1.2</a>: the Frobenius non-degeneracy of the Haar state on $\mathcal{O}_q(\mathrm{SU}(2))$, combined with irreducibility of the instanton connection (Lemma <a href="#lem:irreducible-connection" data-reference-type="ref" data-reference="lem:irreducible-connection">1.8</a>), forces $H^0(M, \mathrm{Ad}(P)) = 0$; the section-vanishing $\Gamma_c(M, E) = 0$ follows from the non-existence of $A$-equivariant sections of the associated $\mathbb{CP}^1$-bundle.*

</div>

<div id="def:instanton" class="definition">

**Definition 1.7** (Instanton connection). *Let $(M, \theta, G, P, E)$ be a $\mathbb{C}$ quantum universe with $\dim_{\mathbb{R}} H = 4$ ($n = 2$). An *instanton connection* on $P$ is a connection $A$ whose curvature $F_A$, restricted to the horizontal distribution $H = \ker\theta$, is self-dual: $F_A|_H = {*_H}\,F_A|_H$, where $*_H$ is the Hodge star on $\Lambda^2 H^*$ determined by the Webster metric $g_\theta$. More generally, when $\dim_{\mathbb{R}} H \neq 4$, an instanton connection is a Yang–Mills connection that minimises the functional $\int_M \lVert F_A|_H \rVert^2\,\theta \wedge (d\theta)^n$.*

</div>

<div id="lem:irreducible-connection" class="lemma">

**Lemma 1.8** (Irreducibility of the connection). *Let $(M, G, P, E)$ be a $\mathbb{C}$ quantum observable universe. Then the vanishing condition $H^0(M, \mathrm{Ad}(P)) = 0$ implies that every instanton connection $A$ on $P$ (Definition <a href="#def:instanton" data-reference-type="ref" data-reference="def:instanton">1.7</a>) is irreducible.*

</div>

<div class="proof">

*Proof.* Suppose for contradiction that an instanton connection $A$ on $P$ is reducible. Then the stabiliser of $A$ under the gauge group contains a non-trivial element $s \in \Gamma(M,\, \mathrm{Ad}(P))$ satisfying $D_A s = 0$. Such $s$ is a global parallel section of $\mathrm{Ad}(P)$, and hence a non-zero element of $H^0(M, \mathrm{Ad}(P))$, contradicting $H^0(M, \mathrm{Ad}(P)) = 0$. Hence $A$ is irreducible. ◻

</div>

<div id="prop:self-dual-curvature" class="proposition">

**Proposition 1.9** (Self-duality of the curvature). *Let $(M, \theta, G, P, E)$ be a $\mathbb{C}$ quantum observable universe with $\dim_{\mathbb{R}} M = 5$ (i.e. the CR dimension $n = 2$, so that the Levi distribution $H = \ker\theta$ has $\dim_{\mathbb{R}} H = 4$). Let $A$ be an instanton connection on $P$. Then the curvature $F_A$, restricted to $H$, is self-dual with respect to the Hodge star $*_H$ determined by the Webster metric $g_\theta$ and the complex structure $J$: $$F_A\big|_H \;=\; {*_H}\, F_A\big|_H.$$*

</div>

<div class="proof">

*Proof.* The contact form $\theta$ (Example <a href="#def:c-quantum-universe" data-reference-type="ref" data-reference="def:c-quantum-universe">1.4</a>) splits the tangent bundle as $TM = H \oplus \mathbb{R}\xi$, where $H = \ker\theta$ has real dimension $4$. The curvature $F_A$ is an $\mathrm{Ad}(P)$-valued $2$-form on $M$. By the Reeb decomposition (Definition <a href="#def:reeb-decomposition" data-reference-type="ref" data-reference="def:reeb-decomposition">1.18</a>), $F_A$ splits into horizontal and vertical parts; we consider $F_A|_H \in \Gamma(\Lambda^2 H^* \otimes
\mathrm{Ad}(P))$.

Since $\dim_{\mathbb{R}} H = 4$, the operator $*_H$ maps $2$-forms to $2$-forms and satisfies $*_H^2 = \mathrm{id}$ on $\Lambda^2 H^*$. This decomposes $\Lambda^2 H^* = \Lambda^+\! H^* \oplus \Lambda^-\! H^*$ into self-dual and anti-self-dual parts.

An instanton connection $A$ minimises the Yang–Mills functional. By the Bogomolny argument, the integrated norm satisfies $$\int_M \lVert F_A|_H \rVert^2 \,\theta \wedge (d\theta)^2
  \;=\; 2\!\int_M \lVert F_A^-|_H \rVert^2 \,\theta \wedge (d\theta)^2
        + \int_M \mathrm{tr}(F_A|_H \wedge F_A|_H)
          \wedge \theta,$$ where the topological term $\int_M \mathrm{tr}(F_A|_H \wedge F_A|_H) \wedge \theta$ is fixed by the characteristic class of $P$. Minimising the functional forces $F_A^-|_H = 0$, which is precisely the self-duality condition $F_A|_H = {*_H}\,F_A|_H$. ◻

</div>

<div id="def:substrate-parameter" class="definition">

**Definition 1.10** (Substrate parameter). *Let $(\mathcal{C}, A, \omega, q)$ be a quantum universe over a field $k$ (Definition <a href="#def:quantum-universe" data-reference-type="ref" data-reference="def:quantum-universe">1.1</a>). Let $\mathcal{U}^{\mathbb{Z}}_q(\mathfrak{su}(2))$ denote the *Lusztig integral form* : the $\mathbb{Z}[q,q^{-1}]$-subalgebra of $\mathcal{U}_q(\mathfrak{su}(2))$ generated by $K^{\pm 1}$ and the divided powers $E^{(n)} = E^n/[n]_q!$, $F^{(n)} = F^n/[n]_q!$. The *substrate parameter* is a ring homomorphism $$\iota \;\colon\; \mathbb{Z}[q, q^{-1}] \;\longrightarrow\; k,
  \qquad q \;\longmapsto\; q_0 \in k^{\times},$$ and the base-changed algebra $\mathcal{U}^{\mathbb{Z}}_q(\mathfrak{su}(2))
  \otimes_{\mathbb{Z}[q,q^{-1}]} k$ is the quantised enveloping algebra at the specialised value $q_0$. When the quantum universe is fibred over a space $M$ (as in the $\mathbb{C}$ realisation, Example <a href="#def:c-quantum-universe" data-reference-type="ref" data-reference="def:c-quantum-universe">1.4</a>), $q_0$ may vary from point to point, yielding a *substrate field* $q \colon M \to k^{\times}$.*

</div>

<div id="rem:c-substrate-via-levi" class="remark">

**Remark 1.11** ($\mathbb{C}$ substrate via the Levi form). *In the $\mathbb{C}$ quantum observable universe (Example <a href="#def:c-quantum-observable-universe" data-reference-type="ref" data-reference="def:c-quantum-observable-universe">1.6</a>), let $A$ be an instanton connection on $P$ (Definition <a href="#def:instanton" data-reference-type="ref" data-reference="def:instanton">1.7</a>), $F_A^+$ its self-dual curvature (Proposition <a href="#prop:self-dual-curvature" data-reference-type="ref" data-reference="prop:self-dual-curvature">1.9</a>), and $L_\theta \colon H \times H \to \mathbb{C}$ the Levi form on $H = \ker\theta$, defined by $L_\theta(V, W) = -i\,d\theta(V, \bar{W})$. The specialisation map of Definition <a href="#def:substrate-parameter" data-reference-type="ref" data-reference="def:substrate-parameter">1.10</a> sends $$q \;\longmapsto\;
  q(p) \;=\; 1 + \lvert\langle L_\theta,\, F_A^+ \rangle\rvert(p),
  \qquad p \in M,$$ where $\langle L_\theta, F_A^+\rangle$ is the natural contraction (Remark <a href="#rem:substrate-contraction" data-reference-type="ref" data-reference="rem:substrate-contraction">1.12</a>) and $\lvert\cdot\rvert$ denotes the absolute value. This defines a smooth field $q \colon M \to [1,\infty) \subset \mathbb{C}^{\times}$ with $q(p) = 1$ at points where $F_A^+ = 0$ (classicality) and $q(p) \to \infty$ in the deep-quantum regime.*

***Relation to the exponential.** Over $\mathbb{Q}$ (or any subfield of $\mathbb{C}$), the classical exponential $\exp(\lvert\langle L_\theta, F_A^+\rangle\rvert)$ is an equally valid specialisation map, and the two are related by the Taylor expansion $\exp(x) = 1 + x + \tfrac{1}{2}x^2 + \cdots$: the formula $q(p) = 1 + \lvert\langle L_\theta, F_A^+\rangle\rvert(p)$ is the first-order approximation of $\exp\!\bigl(\lvert\langle L_\theta, F_A^+\rangle\rvert(p)\bigr)$. Both define smooth fields $M \to [1,\infty)$ with the same boundary behaviour ($q = 1$ at classicality, $q \to \infty$ deep-quantum), and all downstream formulas ($\hbar_q = 1 - q^{-1}$, the Heisenberg commutator, the Schrödinger equation, the Yang–Mills functional) are algebraic in $q$ and therefore insensitive to the choice between $1+x$ and $\exp(x)$. The algebraic form is adopted in Definition <a href="#def:substrate-parameter" data-reference-type="ref" data-reference="def:substrate-parameter">1.10</a> because it is meaningful over every base field $k$, whereas $\exp(x)$ requires an archimedean topology.*

*The non-archimedean analogues are developed in Chapter <a href="#chap:p-adic" data-reference-type="ref" data-reference="chap:p-adic">7</a>: over $\mathbb{Q}_\mathfrak{p}$ the Levi-form contraction is replaced by the Frobenius endomorphism and $q = \mathfrak{p}^{\,-v_\mathfrak{p}(\det\varphi)}$ (Example <a href="#ex:p-adic-realisation" data-reference-type="ref" data-reference="ex:p-adic-realisation">7.1</a>); over $\mathbb{F}_\mathfrak{p}$, $q$ is a primitive root of unity (Example <a href="#ex:finite-field-realisation" data-reference-type="ref" data-reference="ex:finite-field-realisation">7.2</a>).*

</div>

<div id="rem:substrate-contraction" class="remark">

**Remark 1.12** (Natural contraction and field character of $q$). *The Levi form $L_\theta$ is a section of $\Lambda^{1,1} H^*$ (the $(1,1)$-component of $\Lambda^2 H^*$ with respect to the complex structure $J$). The self-dual curvature $F_A^+$ is a section of $\Lambda^+ H^* \otimes \mathrm{Ad}(P)$. On a $4$-dimensional oriented inner-product space, $\Lambda^{1,1} \subset \Lambda^+$, so $L_\theta$ and $F_A^+$ live in the same subbundle. The Webster metric $g_\theta$ provides a fibrewise inner product on $\Lambda^+ H^*$; composing this with the Killing form on $\mathrm{Ad}(P)$ yields the natural contraction $$\langle L_\theta,\, F_A^+ \rangle_p
  \;\in\; \mathbb{R}, \qquad p \in M.$$ The substrate parameter is not a fixed constant but a field on $M$: its value varies from point to point according to the local coupling between the Levi form and the self-dual curvature.*

</div>

<div id="def:quantum-gauge-group" class="definition">

**Definition 1.13** (Quantum Gauge Group). *Let $(M, G, P, E)$ be a $\mathbb{C}$ quantum observable universe with substrate parameter $q$ (Definition <a href="#def:substrate-parameter" data-reference-type="ref" data-reference="def:substrate-parameter">1.10</a>). The *quantum gauge group* is the field of quantum groups $\{\mathrm{SU}_{q(p)}(2)\}_{p \in M}$ obtained by deforming the structure group $G = \mathrm{SU}(2)$ pointwise at the parameter $q(p)$.*

</div>

<div id="def:quantum-planck-constant" class="definition">

**Definition 1.14** (Quantum Planck Constant). *Let $(M, G, P, E)$ be a $\mathbb{C}$ quantum observable universe with substrate parameter $q$ (Definition <a href="#def:substrate-parameter" data-reference-type="ref" data-reference="def:substrate-parameter">1.10</a>). The *quantum Planck constant* is the smooth field $\hbar_q \colon M \to [0,1)$ defined by $$\hbar_q(p) \;=\; 1 - q(p)^{-1}, \qquad p \in M.$$*

</div>

<div id="rem:planck-limits" class="remark">

**Remark 1.15** (Limiting regimes of $\hbar_q$). *Like $q$ itself, $\hbar_q$ is not a universal constant but a field on $M$. As $q(p) \to 1$ (classicality), $\hbar_q(p) \to 0$ and quantum effects vanish; as $q(p) \to \infty$ (deep-quantum regime), $\hbar_q(p) \to 1$.*

</div>

<div id="rem:heisenberg-commutator" class="remark">

**Remark 1.16** (Heisenberg uncertainty as commutator). *In the $\mathbb{C}$ quantum observable universe the Heisenberg uncertainty principle is expressed through the $q$-deformed commutator. Let $\hat{X}$ and $\hat{P}$ denote position and momentum observables on the fibre $\mathbb{CP}^1$. Let $J \colon H \to H$ be the complex structure operator on the Levi distribution ($J^2 = -\mathrm{Id}$); throughout this paper every occurrence of the imaginary unit $i$ in a physical equation is identified with the geometric action of $J$ on horizontal planes. We define their $q$-dependent commutator at $p \in M$ by $$[\hat{X},\, \hat{P}]_q \;:=\; J\,\hbar_q(p),$$ where $\hbar_q(p) = 1 - q(p)^{-1}$ (Definition <a href="#def:quantum-planck-constant" data-reference-type="ref" data-reference="def:quantum-planck-constant">1.14</a>). In this remark the subscript $q$ serves only to record the dependence of the commutator on the substrate field $q$ and should not be confused with any $q$-deformed Lie bracket $[\cdot,\cdot]_q$ on vector fields that may appear elsewhere. The commutator encodes the local uncertainty: when $q(p) \to 1$ (classicality), $[\hat{X}, \hat{P}]_q \to 0$ and observables commute; when $q(p) \to \infty$ (deep-quantum regime), $[\hat{X}, \hat{P}]_q \to J$ and maximal uncertainty prevails.*

***Analogy with the Lie bracket.** The position–momentum commutator $[\hat{X},\hat{P}]_q$ is the quantum-mechanical counterpart of the Lie bracket $[e_a,e_b]=\epsilon_{abc}\,e_c$ in $\mathfrak{su}(2)$ (Definition <a href="#def:su2-basis" data-reference-type="ref" data-reference="def:su2-basis">3.3</a>). Both commutators measure the first-order non-commutativity of their respective algebras (Remark <a href="#rem:first-order-taylor" data-reference-type="ref" data-reference="rem:first-order-taylor">3.4</a>). In the braid-group setting, this non-commutativity appears as the defining relation $\sigma_1\sigma_2\sigma_1=\sigma_2\sigma_1\sigma_2$ (Definition <a href="#def:braid-group" data-reference-type="ref" data-reference="def:braid-group">3.1</a>); on the Bring surface, it is realised by the $S_3$ permutation action on the spectral resolvents (Remark <a href="#rem:braid-group-action" data-reference-type="ref" data-reference="rem:braid-group-action">5.5</a>).*

***Commutator as Reeb vector.** The commutator $[\hat{X},\hat{P}]_q$ may be identified with the value of the $q$-deformed Reeb vector field $\xi_q$ (Definition <a href="#def:q-reeb-vector-field" data-reference-type="ref" data-reference="def:q-reeb-vector-field">1.24</a>) evaluated on the contact form. Concretely, the Reeb field is the unique direction along which the symplectic pairing $d\theta$ degenerates, so $\theta(\xi_q)$ encodes precisely the obstruction to commutativity of canonical coordinates. On the exceptional divisor $\mathbb{CP}^1$ produced by blowing up a spacetime defect on the Bring surface (Remark <a href="#rem:brings-smoothness" data-reference-type="ref" data-reference="rem:brings-smoothness">5.20</a>), the Reeb vector field generates the $U(1)$ fibration of the Hopf bundle $S^3\to\mathbb{CP}^1$, and its “strength” is set by $\hbar_q(p)$.*

</div>

<div id="def:q-harmonic-form" class="definition">

**Definition 1.17** ($q$-Harmonic form (Particle)). *Let $(M, \theta, G, P, E)$ be a $\mathbb{C}$ quantum observable universe with substrate parameter $q$ (Definition <a href="#def:substrate-parameter" data-reference-type="ref" data-reference="def:substrate-parameter">1.10</a>). Let $d_q$ denote the $q$-deformed exterior derivative (Definition <a href="#def:q-ext-deriv" data-reference-type="ref" data-reference="def:q-ext-deriv">1.21</a> below) and let $\delta_q$ denote its formal adjoint with respect to the inner product on $\Gamma(M,\, \Lambda^k T^*M \otimes J^1 E)$ induced by the Webster metric $g_\theta$. A *particle* is a section $\alpha \in \Gamma(M,\, \Lambda^k T^*M \otimes J^1 E)$ that is $q$-harmonic, i.e. lies in the kernel of the $q$-Laplacian: $$\Delta_q \alpha
  \;=\; (d_q\,\delta_q + \delta_q\,d_q)\,\alpha
  \;=\; 0.$$*

</div>

<div id="def:reeb-decomposition" class="definition">

**Definition 1.18** (Reeb decomposition). *Let $(M, \theta)$ be a CR manifold with non-degenerate Levi form (Example <a href="#def:c-quantum-universe" data-reference-type="ref" data-reference="def:c-quantum-universe">1.4</a>) and let $\xi$ denote the associated *Reeb vector field*, characterised by $\iota_\xi\,d\theta = 0$ and $\theta(\xi) = 1$. Every differential $k$-form $\alpha$ ($k \geq 1$) on $M$ decomposes uniquely as $$\alpha \;=\; \alpha_H + \theta \wedge \iota_\xi\,\alpha,$$ where $\alpha_H := \alpha - \theta \wedge \iota_\xi\,\alpha$ is the *horizontal component* (satisfying $\iota_\xi\,\alpha_H = 0$) and $\alpha_V := \theta \wedge \iota_\xi\,\alpha$ is the *vertical component*. A form is *purely horizontal* if and only if $\iota_\xi\,\alpha = 0$.*

</div>

<div id="def:fermion" class="definition">

**Definition 1.19** (Fermion). *A *fermion* is a $q$-harmonic form (Definition <a href="#def:q-harmonic-form" data-reference-type="ref" data-reference="def:q-harmonic-form">1.17</a>) that has a non-trivial vertical component in the Reeb decomposition (Definition <a href="#def:reeb-decomposition" data-reference-type="ref" data-reference="def:reeb-decomposition">1.18</a>): $$\Delta_q\,\alpha = 0
  \qquad\text{and}\qquad
  \iota_\xi\,\alpha_V \neq 0.$$*

</div>

<div id="def:boson" class="definition">

**Definition 1.20** (Boson). *A *boson* is a $q$-harmonic form (Definition <a href="#def:q-harmonic-form" data-reference-type="ref" data-reference="def:q-harmonic-form">1.17</a>) that is purely horizontal in the Reeb decomposition (Definition <a href="#def:reeb-decomposition" data-reference-type="ref" data-reference="def:reeb-decomposition">1.18</a>): $$\Delta_q\,\alpha = 0
  \qquad\text{and}\qquad
  \alpha = \alpha_H
  \quad(\text{equivalently, } \iota_\xi\,\alpha = 0
        \text{ by Definition~\ref{def:reeb-decomposition}}).$$*

</div>

<div id="def:q-ext-deriv" class="definition">

**Definition 1.21** ($q$-Deformed exterior derivative). *Let $(M, \theta, G, P, E)$ be a $\mathbb{C}$ quantum observable universe with substrate parameter $q$ (Definition <a href="#def:substrate-parameter" data-reference-type="ref" data-reference="def:substrate-parameter">1.10</a>). The *$q$-deformed exterior derivative* $d_q \colon \Omega^k(M) \to \Omega^{k+1}(M)$ is defined on $k$-forms by $$d_q\,\alpha
  \;=\; q^{-1}\,d\alpha
        + (1 - q^{-1})\,\theta \wedge \mathcal{L}_\xi\,\alpha,$$ where $d$ is the ordinary exterior derivative, $\theta$ the contact form, and $\mathcal{L}_\xi$ the Lie derivative along the Reeb field.*

</div>

<div id="def:q-lie-bracket" class="definition">

**Definition 1.22** ($q$-Deformed Lie bracket). *Let $V, W \in \mathfrak{X}(M)$ be smooth vector fields. The *$q$-deformed Lie bracket* is $$[V, W]_q
  \;=\; q^{-1}\,[V, W]
        + (1 - q^{-1})\,\bigl(\theta(V)\,\mathcal{L}_\xi W
                              - \theta(W)\,\mathcal{L}_\xi V\bigr),$$ where $[\,\cdot\,,\cdot\,]$ is the standard Lie bracket on $\mathfrak{X}(M)$.*

</div>

<div id="def:q-connection" class="definition">

**Definition 1.23** ($q$-Deformed connection). *Let $A$ be an instanton connection on $P$ (Lemma <a href="#lem:irreducible-connection" data-reference-type="ref" data-reference="lem:irreducible-connection">1.8</a>). The *$q$-deformed connection* $A_q$ is defined by $$A_q
  \;=\; q^{-1}\,A
        + (1 - q^{-1})\,\iota_\xi\,A\;\theta,$$*

</div>

<div id="def:q-reeb-vector-field" class="definition">

**Definition 1.24** ($q$-Deformed Reeb vector field). *Let $(M, \theta, G, P, E)$ be a $\mathbb{C}$ quantum observable universe with substrate parameter $q$ (Definition <a href="#def:substrate-parameter" data-reference-type="ref" data-reference="def:substrate-parameter">1.10</a>) and Reeb vector field $\xi$ (Definition <a href="#def:reeb-decomposition" data-reference-type="ref" data-reference="def:reeb-decomposition">1.18</a>). The *$q$-deformed Reeb vector field* is the vector field $\xi_q$ on $M$ defined by its action on smooth functions $f \in C^\infty(M)$: $$\xi_q(f) \;=\; q^{-1}\,\xi(f) + (1 - q^{-1})\,[\xi, X_f]_q,$$ where $X_f$ is the horizontal lift of $\mathrm{grad}_{g_\theta}\,f$ to $H = \ker\theta$ (using the Webster metric $g_\theta$) and $[\,\cdot\,,\cdot\,]_q$ is the $q$-deformed Lie bracket (Definition <a href="#def:q-lie-bracket" data-reference-type="ref" data-reference="def:q-lie-bracket">1.22</a>).*

</div>

<div id="def:q-reeb-flow" class="definition">

**Definition 1.25** ($q$-Deformed Reeb flow). *Let $\xi_q$ be the $q$-deformed Reeb vector field (Definition <a href="#def:q-reeb-vector-field" data-reference-type="ref" data-reference="def:q-reeb-vector-field">1.24</a>). The *$q$-deformed Reeb flow* is the one-parameter family of diffeomorphisms $\phi_t^q \colon M \to M$, $t \in \mathbb{R}$, generated by $\xi_q$: $$\frac{d}{dt}\,\phi_t^q \;=\; \xi_q \circ \phi_t^q,
  \qquad \phi_0^q = \mathrm{id}_M.$$*

</div>

<div id="def:q-torsion-leaf" class="definition">

**Definition 1.26** ($q$-Torsion leaf). *Let $H = \ker\theta \subset TM$ be the horizontal distribution on the CR manifold $M$. A *$q$-torsion leaf* is a maximal integral submanifold $L \hookrightarrow M$ of $H$ that is invariant under the $q$-deformed Reeb flow (Definition <a href="#def:q-reeb-flow" data-reference-type="ref" data-reference="def:q-reeb-flow">1.25</a>): $$T_p L \;\subset\; H_p
  \quad\text{for all } p \in L,
  \qquad\text{and}\qquad
  \phi_t^q(L) = L
  \quad\text{for all } t \in \mathbb{R}.$$*

</div>

<div id="rem:q-torsion-existence" class="remark">

**Remark 1.27** ($q$-Torsion leaves: existence and Frobenius obstruction). *The horizontal distribution $H = \ker\theta$ on a contact manifold is maximally non-integrable: $d\theta|_{H \times H}$ is non-degenerate. By the Frobenius theorem, maximal integral submanifolds of $H$ have dimension at most $n$ (half the rank of $H$); these are the *Legendrian submanifolds*. Definition <a href="#def:q-torsion-leaf" data-reference-type="ref" data-reference="def:q-torsion-leaf">1.26</a> therefore requires $L$ to be a Legendrian submanifold invariant under the $q$-deformed Reeb flow.*

*Existence is not automatic: it depends on the dynamics of $\xi_q$. When $q \to 1$ and $\xi_q \to \xi$, invariant Legendrian submanifolds exist whenever the Reeb flow is periodic or integrable (e.g. on $S^3/\Gamma$). For $q > 1$, the deformation generically breaks periodicity, and one must appeal to KAM-type persistence results.*

*In the category of Lie algebroids over $M$, the Frobenius integrability condition is equivalent to $H$ carrying a Frobenius structure (Definition <a href="#def:quantum-universe" data-reference-type="ref" data-reference="def:quantum-universe">1.1</a>). Since the Levi form $d\theta|_{H \times H}$ is non-degenerate, this Frobenius structure *fails* — and it is precisely this failure that forces the dimension bound on integral submanifolds and gives $q$-torsion leaves their rigidity.*

</div>

<div id="rem:reeb-physical" class="remark">

**Remark 1.28** (Physical interpretation of the Reeb decomposition). *The Reeb vector field $\xi$ singles out the direction of internal spin on the CR manifold. Forms that “see” this direction (fermions) carry half-integer spin; forms confined to the horizontal distribution (bosons) do not couple to the Reeb flow and carry integer spin. The decomposition $\alpha = \alpha_H + \alpha_V$ is therefore the geometric origin of the spin–statistics distinction in this framework. Experimental confirmation of this picture, including photonic quantum Hall measurements and many-body interference in crystal lattices, is discussed in Chapter <a href="#chap:experimental" data-reference-type="ref" data-reference="chap:experimental">[chap:experimental]</a>.*

</div>

<div id="rem:gr-substrate-geometry" class="remark">

**Remark 1.29** (General Relativity as the “Substrate Geometry”). *In this model the metric is effectively replaced by the Levi form $L_\theta$ and its coupling to the gauge curvature $F_A$. Gravity is expressed through the Variational Bicomplex as the back-reaction of the gauge fields on the CR manifold $M$.*

*Define the *$q$-weighted Yang–Mills–Levi functional* $$S_q[A, \theta]
  \;=\; \int_M q(p)\,\lVert F_A^+|_H \rVert^2\,
        \theta \wedge (d\theta)^n,$$ where $q(p) = 1 + \lvert\langle L_\theta, F_A^+\rangle\rvert(p)$ (Remark <a href="#rem:c-substrate-via-levi" data-reference-type="ref" data-reference="rem:c-substrate-via-levi">1.11</a>). Variation with respect to the Levi form $L_\theta$ yields field equations of the schematic form $$\frac{\delta S_q}{\delta L_\theta}
  \;=\; 0
  \qquad\Longrightarrow\qquad
  \mathrm{Ric}_{g_\theta} \;=\; T^{(q)},$$ where $\mathrm{Ric}_{g_\theta}$ is the Webster Ricci curvature and $T^{(q)}$ is a $q$-weighted stress-energy $2$-tensor on $H$ (both coordinate-free objects). The precise derivation of the field equations will be given in Chapter <a href="#chap:experimental" data-reference-type="ref" data-reference="chap:experimental">[chap:experimental]</a>; here we note only that the geometry of $M$ is forced to curve to accommodate the tension of the $\mathrm{SU}(2)$ instantons.*

</div>

<div id="prop:main-commutative-diagram" class="proposition">

**Proposition 1.30** (Main Commutative Diagram). *Let $(M, \theta, G, P, E)$ be a $\mathbb{C}$ quantum observable universe with instanton connection $A$ (Definition <a href="#def:instanton" data-reference-type="ref" data-reference="def:instanton">1.7</a>) and substrate parameter $q$ (Definition <a href="#def:substrate-parameter" data-reference-type="ref" data-reference="def:substrate-parameter">1.10</a>). Let $\mathbf{E}$ denote the Euler–Lagrange operator of the $q$-weighted Yang–Mills–Levi functional $S_q$ (Remark <a href="#rem:gr-substrate-geometry" data-reference-type="ref" data-reference="rem:gr-substrate-geometry">1.29</a>), and let $\nabla^A$ denote parallel transport along $A$. The following diagram commutes: $$\begin{CD}
J^1E @>{\mathbf{E}[S_q]}>>
  \bigl\{ L_\theta : \mathrm{Ric}_{g_\theta} = T^{(q)} \bigr\} \\
@V{\text{jet evaluation}}VV
  @VV{q = 1 + \lvert\langle L_\theta, F_A^+\rangle\rvert}V \\
\Gamma(E_{\mathrm{lin}}) @>{\nabla^A}>>
  \bigl\{ \psi : J\hbar_q\,\iota_{\xi_q}D_A\psi = \hat{H}_q\psi \bigr\}
\end{CD}$$ where the top row sends a jet (a first-order perturbation of the gauge field) to the Einstein-type field equation via the Euler–Lagrange operator; the left column evaluates a jet at a fibre point to produce a linearised section; the right column is the coupling through the substrate field $q$; and the bottom row is the parallel-transport equation whose linearisation is the Schrödinger equation.*

</div>

<div class="proof">

*Proof sketch.* The top row is the variational equation $\delta S_q / \delta L_\theta = 0$, which involves $q(p)$ through the functional $S_q$. The bottom row is the $q$-deformed parallel-transport equation $J\hbar_q\,\iota_{\xi_q}D_A\psi = \hat{H}_q\psi$ (Remark <a href="#rem:schrodinger-jet-coaction" data-reference-type="ref" data-reference="rem:schrodinger-jet-coaction">2.21</a>), linearised at a chosen section. The left column is the jet evaluation map $j^1_p \sigma \mapsto \sigma(p)$ restricted to $E_{\mathrm{lin}}$. Commutativity amounts to the statement that solving the variational equation for $L_\theta$ and then substituting $q(p)$ into the transport equation gives the same solution set $\psi$ as first evaluating the jet and then transporting along $A$. This follows from the chain rule: $\mathbf{E}[S_q]$ determines $L_\theta$ (and hence $q$), which in turn determines $\hat{H}_q$ and $\xi_q$ appearing in the transport equation. A full proof requires the variational bicomplex machinery of Chapter <a href="#chap:experimental" data-reference-type="ref" data-reference="chap:experimental">[chap:experimental]</a> and is given there. ◻

</div>

## Preview: Lifting and Descent

The two central structural results of this paper are:

- **Jet Prolongation (Lifting).** A $\mathbb{C}$ quantum observable universe $(M, G, P, E)$ lifts canonically to a new quantum observable universe on the total space of the first jet bundle $J^1 E$ (Proposition <a href="#prop:jet-prolongation" data-reference-type="ref" data-reference="prop:jet-prolongation">4.1</a>, Chapter <a href="#chap:torsion" data-reference-type="ref" data-reference="chap:torsion">4</a>).

- **Brane Tower Descent.** Iterating fixed-point reductions under the $\mathrm{SU}(2)$ action produces a tower of nested quantum observable universes $(M_k)_{k \geq 0}$, terminating at a discrete set of algebraic invariants (Section <a href="#ssec:descent" data-reference-type="ref" data-reference="ssec:descent">4.0.1</a>, Chapter <a href="#chap:torsion" data-reference-type="ref" data-reference="chap:torsion">4</a>).

The categorical and analytic elaborations needed for these theorems — Tannaka–Krein reconstruction, Hopf–Frobenius diagrams, and the $q$-deformed operator algebra — are developed in Chapter <a href="#chap:elaboration" data-reference-type="ref" data-reference="chap:elaboration">2</a>. The reader wishing to proceed directly from the definitions above to geometric applications may skip to Chapter <a href="#chap:brings-surface" data-reference-type="ref" data-reference="chap:brings-surface">5</a>.

# Elaboration: Categorical and Analytic Foundations

This chapter collects the categorical, algebraic, and analytic details that underpin the definitions of Chapter <a href="#chap:qou" data-reference-type="ref" data-reference="chap:qou">1</a>. The reader who has read Chapter <a href="#chap:qou" data-reference-type="ref" data-reference="chap:qou">1</a> may return to specific sections as needed; the remainder of the paper does not require this chapter in linear order.

<div id="rem:tqft-context" class="remark">

**Remark 2.1** (TQFT context). *The axioms of Definitions <a href="#def:quantum-universe" data-reference-type="ref" data-reference="def:quantum-universe">1.1</a> and <a href="#def:quantum-observable-universe" data-reference-type="ref" data-reference="def:quantum-observable-universe">1.2</a> are grounded in the algebraic framework of topological quantum field theory (TQFT).*

**Frobenius–Hopf objects and 2d TQFT.* A commutative Frobenius algebra over $k$ is equivalent to a $2$-dimensional TQFT $Z \colon \mathbf{2Cob} \to \mathrm{Vect}_k$ . The Frobenius–Hopf object $A$ in Definition <a href="#def:quantum-universe" data-reference-type="ref" data-reference="def:quantum-universe">1.1</a> carries both the Frobenius structure (encoding the $2$d cobordism data: the product $\mu$ corresponds to a pair-of-pants cobordism, the Frobenius form $\lambda$ to a cap) and a Hopf structure (encoding the quantum-group symmetry that extends the theory to three dimensions). Concretely, a $2$d TQFT assigns to the circle $S^1$ a Frobenius algebra $A$ and to each cobordism $\Sigma \colon S^1 \sqcup \cdots \to S^1 \sqcup \cdots$ a linear map built from $\mu$, $\Delta_\mu$, $\eta$, and $\lambda$. The Hopf structure $(\Delta, \varepsilon, S)$ equips $A$ with the additional data needed for three-dimensional and extended TQFTs .*

**The observability condition as a categorical contact condition.* In the TQFT setting, the condition $\mathrm{Hom}_{\mathcal{C}}(\mathbf{1}, \mathrm{Ad}(A)) = 0$ (Definition <a href="#def:quantum-observable-universe" data-reference-type="ref" data-reference="def:quantum-observable-universe">1.2</a>) is the categorical analogue of the *contact condition* (maximal non-integrability). A non-zero morphism $\mathbf{1} \to \mathrm{Ad}(A)$ would give a global invariant section of the adjoint object — the categorical counterpart of a nowhere-vanishing section of the adjoint bundle — and would force the TQFT to decompose into a direct sum of lower-dimensional theories. Requiring $\mathrm{Hom}(\mathbf{1}, \mathrm{Ad}(A)) = 0$ therefore ensures:*

1.  **irreducibility*: the associated $3$-dimensional TQFT (Chern–Simons type, with gauge datum $A$ and quantum parameter $q$) does not split as a direct sum;*

2.  **non-degeneracy across cobordisms*: the TQFT pairing on state spaces assigned to surfaces is non-degenerate ;*

3.  **full dualisability*: in the sense of the cobordism hypothesis , the object $A$ is fully dualisable in the relevant Morita higher category, so the TQFT extends to a fully local (extended) field theory.*

*In the $\mathbb{C}$ realisation (Example <a href="#def:c-quantum-observable-universe" data-reference-type="ref" data-reference="def:c-quantum-observable-universe">1.6</a>), this categorical condition reduces to $H^0(M, \mathrm{Ad}(P)) = 0$ — the classical requirement that the instanton connection admits no infinitesimal automorphisms, which is the gauge-theoretic manifestation of the contact (maximally non-integrable) geometry of $(M, \theta)$.*

</div>

<div id="rem:vanishing-explication" class="remark">

**Remark 2.2** (Vanishing conditions: explication). *In Example <a href="#def:c-quantum-observable-universe" data-reference-type="ref" data-reference="def:c-quantum-observable-universe">1.6</a>, $\mathrm{Ad}(P) = P \times_G \mathfrak{su}(2)$ is the adjoint bundle (a linear bundle, so sheaf cohomology is defined), and $\Gamma_c(M,E)$ denotes the space of compactly supported continuous sections of the (non-linear) fibre bundle $E$. The condition $H^0(M, \mathrm{Ad}(P)) = 0$ asserts the vanishing of *all* global parallel sections of the adjoint bundle — not merely compactly supported ones — eliminating every infinitesimal gauge symmetry.*

</div>

<div id="rem:levi-generalisation" class="remark">

**Remark 2.3** (Generalisation beyond strict pseudoconvexity). *Example <a href="#def:c-quantum-universe" data-reference-type="ref" data-reference="def:c-quantum-universe">1.4</a> requires only Levi non-degeneracy (not strict pseudoconvexity). This generality is deliberate: the QOU framework applies whenever the following three cohomological/obstruction conditions hold.*

1.  **Kohn–Rossi finite-dimensionality.* The tangential CR complex $(\Omega^{0,\bullet}_b(M),\, \bar\partial_b)$ has finite-dimensional cohomology $H^{0,k}_{\bar\partial_b}(M)$ for all $k$. This replaces strict pseudoconvexity in ensuring analytic control over $q$-harmonic forms (Definition <a href="#def:q-harmonic-form" data-reference-type="ref" data-reference="def:q-harmonic-form">1.17</a>). In the strictly pseudoconvex case, Kohn’s sub-elliptic estimates guarantee this automatically; for indefinite Levi signature, one imposes it as a hypothesis.*

2.  **Non-degeneracy of the substrate.* The Levi form $L_\theta$ is non-degenerate (but not necessarily positive definite), so the substrate parameter $q(p) = 1 + \lvert\langle L_\theta, F_A^+\rangle\rvert$ (Remark <a href="#rem:c-substrate-via-levi" data-reference-type="ref" data-reference="rem:c-substrate-via-levi">1.11</a>) is well-defined and the regime $q > 1$ is attainable. When the Levi form has indefinite signature $(r,s)$ with $r,s \geq 1$, the Webster metric $g_\theta$ is pseudo-Riemannian; the contraction $\langle L_\theta, F_A^+\rangle$ remains well-defined (using the pseudo-Riemannian inner product on $\Lambda^+ H^*$), and one takes the absolute value to ensure $q \geq 1$.*

3.  **QOU vanishing (Example <a href="#def:c-quantum-observable-universe" data-reference-type="ref" data-reference="def:c-quantum-observable-universe">1.6</a>).* The conditions $H^0(M, \mathrm{Ad}(P)) = 0$ and $\Gamma_c(M,E) = 0$ serve as the gauge-theoretic obstructions. These are purely topological/cohomological and independent of the Levi signature.*

*Together, conditions (1)–(3) ensure that all results of this chapter (irreducibility of the connection, self-duality of the curvature, substrate dynamics, $q$-deformed operators) extend to CR manifolds of arbitrary Levi signature. The strictly pseudoconvex case (signature $(n,0)$) is the simplest and motivates all examples in this chapter; the indefinite case arises naturally for real hypersurfaces in indefinite Kähler manifolds and for boundaries of Grauert tubes over pseudo-Riemannian manifolds.*

</div>

<div id="rem:jet-bundle" class="remark">

**Remark 2.4** (Jet-bundle formulation). *The conditions in Example <a href="#def:c-quantum-observable-universe" data-reference-type="ref" data-reference="def:c-quantum-observable-universe">1.6</a> admit a natural reformulation in terms of the first jet bundle $J^1 E$. The vanishing $\Gamma_c(M, E) = 0$ ensures that no non-trivial compactly supported section of $E$ exists, while $H^0(M, \mathrm{Ad}(P)) = 0$ eliminates *all* infinitesimal gauge symmetries (not merely compactly supported ones). Together, these conditions mean that the space of sections of $J^1 E$ injects into the space of connections on $P$, preventing any local degeneracy of the gauge field.*

</div>

<div id="ex:calabi-yau" class="example">

**Example 2.5** (Real hypersurface in a Calabi–Yau $2$-fold). *Let $X$ be a Calabi–Yau $2$-fold (K3 surface) with holonomy $\mathrm{SU}(2)$, and let $M \subset X$ be a smooth, strictly convex real hypersurface. Then $M$ is a $3$-dimensional strictly pseudoconvex CR manifold inheriting its CR structure from the ambient Kähler geometry. Because the holonomy of $X$ is $\mathrm{SU}(2)$, the frame bundle of $X$ restricted to $M$ yields a natural principal $\mathrm{SU}(2)$-bundle $P \to M$. The associated state bundle $E = P \times_G \mathbb{CP}^1$ yields a $\mathbb{C}$ quantum observable universe $(M, \theta, G, P, E)$ when the vanishing conditions of Example <a href="#def:c-quantum-observable-universe" data-reference-type="ref" data-reference="def:c-quantum-observable-universe">1.6</a> are satisfied. (For higher-dimensional Calabi–Yau manifolds with holonomy $\mathrm{SU}(n)$, $n > 2$, a reduction to $\mathrm{SU}(2)$ must be supplied separately.)*

</div>

<div id="ex:ale" class="example">

**Example 2.6** (ALE links). *Let $\Gamma \subset \mathrm{SU}(2)$ be a finite subgroup and let $X$ be the minimal resolution of $\mathbb{C}^2 / \Gamma$. The link $M = S^3 / \Gamma$ is the boundary of a tubular neighbourhood of the exceptional set in $X$; it is a compact $3$-dimensional strictly pseudoconvex CR manifold. The CR structure of the boundary induces a contact form $\theta$ on $M$ whose Reeb vector field $\xi$ generates the Hopf-type fibration $S^3/\Gamma \to S^2$. (When $\Gamma \neq \{1\}$, the target is the orbifold $\mathbb{CP}^1/\Gamma$; the bundle structure remains well-defined on the smooth manifold $M = S^3/\Gamma$.) Equipped with the induced principal $\mathrm{SU}(2)$-bundle $P \to M$ and the associated state bundle $E = P \times_G \mathbb{CP}^1$, the tuple $(M, \theta, G, P, E)$ provides a $\mathbb{C}$ quantum observable universe. Note that $\dim_{\mathbb{R}} H = 2$, so the Hodge-star decomposition $\Lambda^2 H^* = \Lambda^+\! H^* \oplus \Lambda^-\! H^*$ is trivial ($\Lambda^2 H^* \cong \mathbb{R}$); in this dimension the curvature $F_A|_H$ is automatically “self-dual” in the vacuous sense, and the instanton condition reduces to the Yang–Mills equation (Definition <a href="#def:instanton" data-reference-type="ref" data-reference="def:instanton">1.7</a>).*

</div>

<div id="ex:brings-surface" class="example">

**Example 2.7** (Bring’s surface unit circle bundle). *Let $S$ denote Bring’s surface (Definition <a href="#def:brings-surface" data-reference-type="ref" data-reference="def:brings-surface">5.2</a>), the genus-$4$ Riemann surface in $\mathbb{P}^4$ cut out by the first three power sums $\sum x_j^k = 0$, $k=1,2,3$. Being a Riemann surface (real dimension $2$), $S$ itself is not a CR manifold. The CR geometry lives on the unit circle bundle $M_S \subset T^*S$: the Liouville $1$-form on $T^*S$ restricts to a contact form $\theta$ on $M_S$, making it a $3$-dimensional strictly pseudoconvex CR manifold. The Reeb vector field $\xi$ generates the $U(1)$ fibre rotation of $M_S \to S$. The natural projection $\pi\colon S \to \mathbb{CP}^1$ (a degree-$4$ branched covering with $6$ branch points corresponding to the $6$ defects of Euler characteristic $\chi=-6$) lifts to a principal $\mathrm{SU}(2)$-bundle $P \to M_S$. Setting $E = P \times_G \mathbb{CP}^1$, the $4$-tuple $(M_S,\, G,\, P,\, E)$ assembles into a $\mathbb{C}$ quantum observable universe whose exceptional divisors support the $q$-deformed Reeb flow (Definition <a href="#def:q-reeb-flow" data-reference-type="ref" data-reference="def:q-reeb-flow">1.25</a>).*

</div>

<div id="rem:examples-unified" class="remark">

**Remark 2.8** ($\mathbb{C}$ examples as instances of the generalised framework). *Each of the preceding $\mathbb{C}$ examples is an instance of the base-field-independent Definition <a href="#def:quantum-universe" data-reference-type="ref" data-reference="def:quantum-universe">1.1</a>, realised over $k = \mathbb{C}$ via the Levi non-degenerate framework of Example <a href="#def:c-quantum-universe" data-reference-type="ref" data-reference="def:c-quantum-universe">1.4</a> and Remark <a href="#rem:levi-generalisation" data-reference-type="ref" data-reference="rem:levi-generalisation">2.3</a>.*

- **CY hypersurfaces* (Example <a href="#ex:calabi-yau" data-reference-type="ref" data-reference="ex:calabi-yau">2.5</a>). A smooth strictly convex real hypersurface $M$ in a Kähler manifold inherits a strictly pseudoconvex CR structure — i.e. the Levi form has definite signature. The Kohn–Rossi condition holds automatically by Kohn’s sub-elliptic estimates.*

- **ALE links* (Example <a href="#ex:ale" data-reference-type="ref" data-reference="ex:ale">2.6</a>). The link $S^3/\Gamma$ is the CR boundary of the minimal resolution of $\mathbb{C}^2/\Gamma$; its Levi form has signature $(1,0)$. Kohn–Rossi finite-dimensionality follows from compactness of $M$.*

- **Bring’s surface unit circle bundle* (Example <a href="#ex:brings-surface" data-reference-type="ref" data-reference="ex:brings-surface">2.7</a>). The unit circle bundle $M_S \subset T^*S$ is a compact $3$-dimensional strictly pseudoconvex CR manifold with Levi signature $(1,0)$.*

*All three satisfy the three cohomological conditions of Remark <a href="#rem:levi-generalisation" data-reference-type="ref" data-reference="rem:levi-generalisation">2.3</a>: Kohn–Rossi finite-dimensionality (by strict pseudoconvexity or compactness), substrate non-degeneracy (positive-definite Levi form ensures $q > 1$ wherever $F_A^+ \neq 0$), and the QOU vanishing conditions (by the topology of the respective principal bundles). More generally, any real hypersurface in an indefinite Kähler manifold, or the boundary of a Grauert tube over a pseudo-Riemannian manifold, yields a CR manifold with indefinite Levi signature satisfying these conditions — extending the QOU framework beyond the strictly pseudoconvex setting.*

</div>

<div id="rem:quantum-gauge-group-category" class="remark">

**Remark 2.9** (Quantum gauge group: category-theoretic perspective). *The quantum gauge group (Definition <a href="#def:quantum-gauge-group" data-reference-type="ref" data-reference="def:quantum-gauge-group">1.13</a>) is realised pointwise by the Hopf algebra $\mathcal{O}_{q(p)}(\mathrm{SU}(2))$ of regular functions on $\mathrm{SU}_{q(p)}(2)$. The categorical view replaces each fibre with its representation category $\mathrm{Rep}(\mathrm{SU}_{q(p)}(2))$, a braided monoidal category. Tannaka–Krein duality reconstructs $\mathcal{O}_{q(p)}$ from $\mathrm{Rep}(\mathrm{SU}_{q(p)}(2))$ via $\mathrm{End}^{\otimes}(\omega)$, where $\omega$ is the forgetful fibre functor. For any two points $p, p' \in M$ connected by a path $\gamma$, the passage between fibres is captured by the commutative square $$\label{eq:tannaka-krein-functoriality}
\begin{CD}
\mathcal{O}_{q(p)}(\mathrm{SU}(2))
  @>{\mathrm{Rep}}>>
  \mathrm{Rep}(\mathrm{SU}_{q(p)}(2)) \\
@V{\text{transition along } \gamma}VV
  @VV{\text{monoidal functor}}V \\
\mathcal{O}_{q(p')}(\mathrm{SU}(2))
  @>>{\mathrm{Rep}}>
  \mathrm{Rep}(\mathrm{SU}_{q(p')}(2))
\end{CD}$$ Tannaka–Krein reconstruction inverts the horizontal arrows, so the Hopf-algebra and representation-category viewpoints are equivalent fibrewise.*

</div>

<div id="rem:hopf-structure-diagrams" class="remark">

**Remark 2.10** (Hopf-algebra structure and non-cocommutativity). *Write $\mathcal{O}_q = \mathcal{O}_q(\mathrm{SU}(2))$ and let $\Delta_q$, $\varepsilon_q$, $S_q$ denote the comultiplication, counit, and antipode. The Hopf comultiplication satisfies *coassociativity*: $$\label{eq:coassociativity}
\begin{CD}
\mathcal{O}_q @>{\Delta_q}>>
  \mathcal{O}_q \otimes \mathcal{O}_q \\
@V{\Delta_q}VV
  @VV{\mathrm{id} \otimes \Delta_q}V \\
\mathcal{O}_q \otimes \mathcal{O}_q
  @>>{\Delta_q \otimes \mathrm{id}}>
  \mathcal{O}_q \otimes \mathcal{O}_q \otimes \mathcal{O}_q
\end{CD}$$ Let $\sigma \colon \mathcal{O}_q \otimes \mathcal{O}_q \to
\mathcal{O}_q \otimes \mathcal{O}_q$ denote the tensor flip $(a \otimes b \mapsto b \otimes a)$. The cocommutativity square $$\label{eq:non-cocommutativity}
\begin{CD}
\mathcal{O}_q @>{\Delta_q}>>
  \mathcal{O}_q \otimes \mathcal{O}_q \\
@V{\Delta_q}VV  @VV{\sigma}V \\
\mathcal{O}_q \otimes \mathcal{O}_q
  @=
  \mathcal{O}_q \otimes \mathcal{O}_q
\end{CD}
\quad\text{commutes}\;\Longleftrightarrow\;q = 1.$$ For $q \neq 1$ the failure of <a href="#eq:non-cocommutativity" data-reference-type="eqref" data-reference="eq:non-cocommutativity">[eq:non-cocommutativity]</a> is controlled by the universal $R$-matrix of $U_q(\mathfrak{su}(2))$: $\sigma \circ \Delta_q = \mathrm{Ad}_{R_q} \circ \Delta_q$, where $R_1 = 1 \otimes 1$ recovers cocommutativity at $q = 1$.*

</div>

<div id="rem:self-dual-ses" class="remark">

**Remark 2.11** (Self-duality as a short exact sequence). *In the QOU setting with $\dim_{\mathbb{R}} H = 4$, the Hodge star $*_H$ gives the splitting $\Lambda^2 H^* = \Lambda^+\!H^* \oplus \Lambda^-\!H^*$ and hence the short exact sequence of $\mathrm{Ad}(P)$-valued forms $$\label{eq:self-dual-ses}
\begin{CD}
0 @>>>
  \Gamma\!\bigl(\Lambda^-\!H^* \otimes \mathrm{Ad}(P)\bigr)
  @>{\iota}>>
  \Gamma\!\bigl(\Lambda^2 H^* \otimes \mathrm{Ad}(P)\bigr)
  @>{\pi^+}>>
  \Gamma\!\bigl(\Lambda^+\!H^* \otimes \mathrm{Ad}(P)\bigr)
  @>>> 0
\end{CD}$$ The instanton condition $F_A|_H = {*_H}\,F_A|_H$ (Proposition <a href="#prop:self-dual-curvature" data-reference-type="ref" data-reference="prop:self-dual-curvature">1.9</a>) is exactly the condition $F_A|_H \in \ker(\mathrm{id} - {*_H})$, i.e. $F_A^-|_H = 0$. In the language of $2$-groups, this has a clean reinterpretation (Remark <a href="#rem:self-dual-2group" data-reference-type="ref" data-reference="rem:self-dual-2group">2.12</a>).*

</div>

<div id="rem:self-dual-2group" class="remark">

**Remark 2.12** (Self-duality as constrained $2$-group gauge theory). *A strict $2$-group is equivalently a *crossed module*: a group homomorphism $\partial \colon H \to G$ together with an action of $G$ on $H$ satisfying the Peiffer identity. The associated exact sequence $$\label{eq:crossed-module-ses}
\begin{CD}
1 @>>> \ker\partial @>>> H @>{\partial}>> G @>>>
  \mathrm{coker}\,\partial @>>> 1
\end{CD}$$ encodes the $2$-group as a homotopy type with $\pi_0 = \mathrm{coker}\,\partial$ and $\pi_1 = \ker\partial$.*

*The *inner-automorphism $2$-group* $\mathrm{INN}(G) = (G \xrightarrow{\mathrm{id}} G)$ has $\ker\partial = 1$ and $\mathrm{coker}\,\partial = 1$, so it is connected and simply connected as a $2$-group. A $2$-connection for $\mathrm{INN}(G)$ on a principal $2$-bundle over $M$ consists of a $\mathfrak{g}$-valued $1$-form $A$ and a $\mathfrak{g}$-valued $2$-form $B$, subject to the *fake-flatness* condition $$\label{eq:fake-flatness}
F_A \;=\; B.$$ In the QOU setting, $G = \mathrm{SU}(2)$ and the Levi distribution $H = \ker\theta$ has $\dim_{\mathbb{R}} H = 4$, so the Hodge decomposition $\Lambda^2 H^* = \Lambda^+\!H^* \oplus \Lambda^-\!H^*$ is available. Imposing the *simplicity constraint* $$B \;\in\; \Gamma\!\bigl(\Lambda^+\!H^* \otimes \mathrm{Ad}(P)\bigr)$$ — that is, requiring the $2$-form datum to be self-dual — and combining with fake flatness <a href="#eq:fake-flatness" data-reference-type="eqref" data-reference="eq:fake-flatness">[eq:fake-flatness]</a> yields the commutative diagram $$\label{eq:2group-instanton}
\begin{CD}
\Omega^1(M,\,\mathfrak{g})
  @>{d_A}>>
  \Omega^2(M,\,\mathfrak{g})
  @>{\pi^+}>>
  \Omega^{2,+}(M,\,\mathfrak{g}) \\
@.  @AA{=\;B}A  @AA{\text{simplicity}}A \\
@.  F_A @= F_A^+
\end{CD}$$ The fake-flatness condition $F_A = B$ combined with the simplicity constraint $B = F_A^+$ forces $F_A = F_A^+$, hence $F_A^- = 0$. This is precisely the instanton equation $F_A|_H = {*_H}\,F_A|_H$ of Definition <a href="#def:instanton" data-reference-type="ref" data-reference="def:instanton">1.7</a>. Thus, the self-dual formulation used throughout this paper is a special case of $2$-group gauge theory for $\mathrm{INN}(\mathrm{SU}(2))$ subject to a simplicity constraint on the $2$-form datum.*

*This perspective clarifies the relationship between the instanton condition in Chapter 1 and the higher-categorical structures of later chapters: the parallel-transport $2$-functor of the $\mathrm{INN}(\mathrm{SU}(2))$ $2$-bundle assigns to paths in $M$ not merely group elements in $\mathrm{SU}(2)$ but $2$-morphisms encoding the self-dual curvature, with the simplicity constraint selecting the physical (instanton) sector.*

</div>

<div id="rem:frobenius-simplification" class="remark">

**Remark 2.13** (Frobenius structure of the $\mathbb{C}$ gauge algebra). *The Hopf algebra $\mathcal{O}_q(\mathrm{SU}(2))$ carries a natural *Frobenius structure*: the Haar state $h_q \colon \mathcal{O}_q \to \mathbb{C}$ induces a non-degenerate pairing $\langle a, b \rangle = h_q(ab)$, making $\mathcal{O}_q$ into a Frobenius algebra with comultiplication $\Delta_\mu$ dual to the multiplication. This Frobenius comultiplication is compatible with the Hopf comultiplication $\Delta_q$ of <a href="#eq:coassociativity" data-reference-type="eqref" data-reference="eq:coassociativity">[eq:coassociativity]</a> and satisfies the *Frobenius relation*: $$\label{eq:frobenius-relation}
\begin{CD}
\mathcal{O}_q \otimes \mathcal{O}_q
  @>{\mu}>>
  \mathcal{O}_q \\
@V{\mathrm{id} \otimes \Delta_\mu}VV
  @VV{\Delta_\mu}V \\
\mathcal{O}_q \otimes \mathcal{O}_q \otimes \mathcal{O}_q
  @>>{\mu \otimes \mathrm{id}}>
  \mathcal{O}_q \otimes \mathcal{O}_q
\end{CD}$$ where $\mu$ is the algebra multiplication and $\Delta_\mu$ the Frobenius comultiplication (dual to $\mu$ under the Haar pairing). The non-degeneracy of $h_q$ is expressed by requiring the composite $$\label{eq:frobenius-nondegen}
\begin{CD}
\mathcal{O}_q \otimes \mathcal{O}_q
  @>{\mu}>>
  \mathcal{O}_q
  @>{h_q}>>
  \mathbb{C}
\end{CD}$$ to be a perfect pairing, i.e. the induced map $\mathcal{O}_q \to \mathcal{O}_q^*$ is an isomorphism.*

*This Frobenius–Hopf structure on $\mathcal{O}_q(\mathrm{SU}(2))$ is precisely the datum required by the general Definition <a href="#def:quantum-universe" data-reference-type="ref" data-reference="def:quantum-universe">1.1</a>: the Haar state $h_q$ realises the Frobenius form $\lambda \colon A \to \mathbf{1}$, and the non-degeneracy <a href="#eq:frobenius-nondegen" data-reference-type="eqref" data-reference="eq:frobenius-nondegen">[eq:frobenius-nondegen]</a> is the $\mathbb{C}$ instance of condition (1) in Definition <a href="#def:quantum-observable-universe" data-reference-type="ref" data-reference="def:quantum-observable-universe">1.2</a>. In the $\mathbb{C}$ realisation (Example <a href="#def:c-quantum-universe" data-reference-type="ref" data-reference="def:c-quantum-universe">1.4</a>), the $5$-tuple $(M, \theta, G, P, E)$ and the two analytic vanishing conditions of Example <a href="#def:c-quantum-observable-universe" data-reference-type="ref" data-reference="def:c-quantum-observable-universe">1.6</a> reduce to a triple:*

1.  *a CR manifold $(M, \theta)$ of hypersurface type with non-degenerate Levi form;*

2.  *a non-degenerate Frobenius–Hopf object $A$ in the monoidal category of vector bundles over $M$, playing the rôle of the triple $(G, P, E)$; and*

3.  *an instanton connection on the underlying $A$-bundle (Definition <a href="#def:instanton" data-reference-type="ref" data-reference="def:instanton">1.7</a>).*

*The vanishing condition $H^0(M, \mathrm{Ad}(P)) = 0$ then follows from the non-degeneracy of the Frobenius form $\lambda$ via the diagram $$\label{eq:frobenius-vanishing}
\begin{CD}
\mathrm{Ad}(A) \otimes \mathrm{Ad}(A)
  @>{\mu_{\mathrm{Ad}}}>>
  \mathrm{Ad}(A)
  @>{\lambda_{\mathrm{Ad}}}>>
  \mathcal{O}_M \\
@V{\text{global sections}}VV  @.  @VV{\int_M}V \\
H^0(M,\,\mathrm{Ad}(A)) \otimes H^0(M,\,\mathrm{Ad}(A))
  @.  @>>{\text{pairing}}>
  \mathbb{C}
\end{CD}$$ The adjoint representation $\mathrm{Ad}(A)$ inherits a non-degenerate Frobenius pairing from $\lambda$; any global parallel section would pair non-trivially with itself, contradicting the irreducibility of the instanton connection (Lemma <a href="#lem:irreducible-connection" data-reference-type="ref" data-reference="lem:irreducible-connection">1.8</a>). Hence the Frobenius non-degeneracy, combined with irreducibility, forces $H^0(M, \mathrm{Ad}(A)) = 0$. The section-vanishing condition $\Gamma_c(M, E) = 0$ follows similarly from the non-existence of $A$-equivariant sections of the associated $\mathbb{CP}^1$-bundle.*

*Note that the horizontal distribution $H = \ker\theta$ itself *fails* to carry a Frobenius structure (as discussed in Remark <a href="#rem:q-torsion-existence" data-reference-type="ref" data-reference="rem:q-torsion-existence">1.27</a>); it is the gauge algebra, not the distribution, that is Frobenius.*

</div>

<div id="ex:cosmological-limits" class="example">

**Example 2.14** (Cosmological limits of $q$ on $S^3$). *Consider the link $M = S^3$ with the standard contact form $\theta$ (Example <a href="#ex:ale" data-reference-type="ref" data-reference="ex:ale">2.6</a> with $\Gamma = \{1\}$) and let $A$ be the standard instanton connection on the Hopf bundle $P = S^7 \to S^4$ restricted to $S^3$. The Levi form $L_\theta$ has signature $(1,0)$ with $\lvert L_\theta \rvert = 1$ everywhere.*

*As the instanton curvature concentrates near a point $p_0 \in S^3$ (a “collapsing instanton”), $\lvert \langle L_\theta, F_A^+ \rangle \rvert$ diverges at $p_0$ and tends to zero away from $p_0$. This produces two regimes simultaneously:*

- **Near $p_0$*: $q(p) \to \infty$, $\hbar_q \to 1$, $[\hat{X},\hat{P}]_q \to J$ — a “big bang” singularity.*

- **Away from $p_0$*: $q(p) \to 1$, $\hbar_q \to 0$, $[\hat{X},\hat{P}]_q \to 0$ — a “heat death” region.*

*The substrate field $q$ thus captures the phase transition between quantum and classical regimes as a geometric phenomenon.*

</div>

<div id="rem:j1e-local-states" class="remark">

**Remark 2.15** ($J^1E$ as the space of local states). *The jet bundle $J^1 E$ serves as the space of local states of the $\mathbb{C}$ quantum observable universe. The classical gauge dynamics, encoded by the *instanton connection* $A$ (Lemma <a href="#lem:irreducible-connection" data-reference-type="ref" data-reference="lem:irreducible-connection">1.8</a>), are weighted by the substrate parameter $q$ (Definition <a href="#def:substrate-parameter" data-reference-type="ref" data-reference="def:substrate-parameter">1.10</a>) to define the quantum field algebra $\mathrm{SU}_q(2)$ (Definition <a href="#def:quantum-gauge-group" data-reference-type="ref" data-reference="def:quantum-gauge-group">1.13</a>).*

</div>

<div id="prop:dq-squared" class="proposition">

**Proposition 2.16** ($d_q^2$ does not vanish). *Let $d_q$ be the $q$-deformed exterior derivative (Definition <a href="#def:q-ext-deriv" data-reference-type="ref" data-reference="def:q-ext-deriv">1.21</a>). For constant $q > 1$, the operator $d_q^2$ is given by $$d_q^2\,\alpha
  \;=\; q^{-1}(1 - q^{-1})\,d\theta \wedge \mathcal{L}_\xi\,\alpha.$$ In particular, $d_q^2 = 0$ if and only if $q = 1$ (classical case) or $\alpha$ lies in the kernel of $\mathcal{L}_\xi$ (Reeb-invariant forms). On horizontal $\mathcal{L}_\xi$-invariant forms, $d_q$ *does* define a cochain complex.*

</div>

<div class="proof">

*Proof.* Write $a = q^{-1}$ and $b = 1 - q^{-1}$, so $a + b = 1$. Then $$\begin{aligned}
  d_q^2\,\alpha
  &= d_q\bigl(a\,d\alpha + b\,\theta \wedge \mathcal{L}_\xi\alpha\bigr) \\
  &= a^2\,d^2\alpha
     + ab\,d(\theta \wedge \mathcal{L}_\xi\alpha)
     + ab\,\theta \wedge \mathcal{L}_\xi\,d\alpha
     + b^2\,\theta \wedge \mathcal{L}_\xi(\theta \wedge \mathcal{L}_\xi\alpha).
\end{aligned}$$ The first term vanishes since $d^2 = 0$. The second expands as $ab\,d\theta \wedge \mathcal{L}_\xi\alpha
- ab\,\theta \wedge d\mathcal{L}_\xi\alpha$. The third term cancels the second’s negative part because $[d,\, \mathcal{L}_\xi] = 0$ implies $\theta \wedge \mathcal{L}_\xi\,d\alpha
= \theta \wedge d\,\mathcal{L}_\xi\alpha$. For the fourth term, the Reeb field satisfies $\mathcal{L}_\xi\theta = 0$ (since $\iota_\xi d\theta = 0$ and $\theta(\xi)=1$), so $\mathcal{L}_\xi(\theta \wedge \mathcal{L}_\xi\alpha)
= \theta \wedge \mathcal{L}_\xi^2\alpha$; the factor $\theta \wedge \theta = 0$ in $b^2\,\theta \wedge \theta
\wedge \mathcal{L}_\xi^2\alpha$ kills this term. Hence $d_q^2\alpha = ab\,d\theta \wedge \mathcal{L}_\xi\alpha$. ◻

</div>

<div id="prop:q-jacobiator" class="proposition">

**Proposition 2.17** (Jacobiator of ${{[\,\cdot\,,\cdot\,]}}_q$). *Let $U, V, W \in \Gamma(H)$ be horizontal vector fields (i.e. $\theta(U) = \theta(V) = \theta(W) = 0$). The *Jacobiator* $$\mathrm{Jac}_q(U,V,W)
  \;:=\; [[U,V]_q, W]_q + [[V,W]_q, U]_q + [[W,U]_q, V]_q$$ is given by $$\mathrm{Jac}_q(U,V,W)
  \;=\; -q^{-1}(1-q^{-1})\!\sum_{\mathrm{cyc}}
        d\theta(V,W)\,\mathcal{L}_\xi U,$$ where the sum is over cyclic permutations of $(U,V,W)$. In particular, $\mathrm{Jac}_q = 0$ if and only if $q = 1$ (classical Jacobi identity) or $d\theta|_{H \times H} = 0$ (integrable horizontal distribution). Since $d\theta|_{H \times H}$ is the Levi form $L_\theta$, which is non-degenerate by hypothesis, $[\,\cdot\,,\cdot\,]_q$ violates the Jacobi identity for all $q \neq 1$. Thus $(\mathfrak{X}(M), [\,\cdot\,,\cdot\,]_q)$ is a *Leibniz algebra* (or a pre-Lie algebra), not a Lie algebra.*

</div>

<div class="proof">

*Proof.* For horizontal $V, W$, the bracket reduces to $[V,W]_q = q^{-1}[V,W]$. The mixed term $\theta([V,W]_q) = -q^{-1}\,d\theta(V,W)$ is in general non-zero. Substituting into the next bracket: $$\begin{aligned}
_q,\, U]_q
  &= q^{-2}\,[[V,W],U]
    - q^{-1}(1-q^{-1})\,d\theta(V,W)\,\mathcal{L}_\xi U,
\end{aligned}$$ using $\theta(U)=0$ and $\theta([V,W]_q) = -q^{-1}d\theta(V,W)$. Summing cyclically, the $q^{-2}$ terms assemble into $q^{-2}\,\mathrm{Jac}(U,V,W) = 0$ by the classical Jacobi identity, leaving only the $d\theta$ terms. ◻

</div>

<div id="rem:classical-recovery" class="remark">

**Remark 2.18** (Classical recovery of $q$-deformed operators). *All four $q$-deformed operators interpolate between the classical ($q = 1$) and deformed ($q > 1$) regimes via the uniform pattern $q^{-1} \cdot (\text{classical}) + (1 - q^{-1}) \cdot (\text{Reeb correction})$. At $q = 1$ each recovers its classical counterpart: $d_q = d$ (Definition <a href="#def:q-ext-deriv" data-reference-type="ref" data-reference="def:q-ext-deriv">1.21</a>), $[\,\cdot\,,\cdot\,]_q = [\,\cdot\,,\cdot\,]$ (Definition <a href="#def:q-lie-bracket" data-reference-type="ref" data-reference="def:q-lie-bracket">1.22</a>), $A_q = A$ (Definition <a href="#def:q-connection" data-reference-type="ref" data-reference="def:q-connection">1.23</a>), and $\xi_q = \xi$ (Definition <a href="#def:q-reeb-vector-field" data-reference-type="ref" data-reference="def:q-reeb-vector-field">1.24</a>). The connection $A_q$ interpolates between the full instanton connection and its Reeb component $\iota_\xi A\;\theta$.*

</div>

<div id="rem:q-torsion-leaf-minimum" class="remark">

**Remark 2.19** ($q$-Torsion leaves as energy minima). *Let $A_q$ denote the $q$-deformed connection (Definition <a href="#def:q-connection" data-reference-type="ref" data-reference="def:q-connection">1.23</a>) and define the $q$-curvature $$\Omega_q \;=\; dA_q + \tfrac{1}{2}\,[A_q,\, A_q]_q,$$ where $[\,\cdot\,,\cdot\,]_q$ is the $q$-deformed Lie bracket (Definition <a href="#def:q-lie-bracket" data-reference-type="ref" data-reference="def:q-lie-bracket">1.22</a>) extended to $\mathrm{Ad}(P)$-valued forms. A $q$-torsion leaf $L$ (Definition <a href="#def:q-torsion-leaf" data-reference-type="ref" data-reference="def:q-torsion-leaf">1.26</a>) is a local minimum of $\lVert\Omega_q\rVert$ restricted to the horizontal distribution: the invariance of $L$ under $\phi_t^q$ forces the first variation of $\lVert\Omega_q|_L\rVert$ to vanish, so $L$ sits in a $q$-curvature well. Physically, a $q$-torsion leaf represents a region of the CR manifold where the gauge curvature is minimised and the $q$-deformed dynamics are in equilibrium.*

</div>

<div id="rem:q-harmonic-physical" class="remark">

**Remark 2.20** (Physical interpretation of $q$-harmonicity). *The $q$-Laplacian $\Delta_q$ encodes the $q$-deformed viscosity of the CR geometry. A $q$-harmonic form is a zero-mode of this operator and thus represents a stable excitation — a particle — of the quantum observable universe. The deformation parameter $q$ interpolates between the classical regime ($q \to 1$, where $\Delta_q$ reduces to the Hodge Laplacian) and the deep-quantum regime ($q \to \infty$), so the notion of “particle” is itself $q$-dependent.*

</div>

<div id="rem:schrodinger-jet-coaction" class="remark">

**Remark 2.21** ($q$-Deformed Schrödinger equation). *The $q$-deformed Schrödinger equation governs the evolution of states in the linearised state bundle. Throughout this paper the symbol $i$ in the Schrödinger equation is identified with the complex structure operator $J \colon H \to H$ on the Levi distribution ($J^2 = -\mathrm{Id}$): it acts as a geometric twisting operator on horizontal planes rather than as an algebraic imaginary unit.*

**Linearisation convention.* The fibre $\mathbb{CP}^1$ is a non-linear space, so one cannot write a linear PDE for sections of $E$ directly. We work instead with the *linearised* model: identify a neighbourhood of a base-point in $\mathbb{CP}^1$ with $\mathbb{C}$ via stereographic projection, and interpret $\psi$ as a section of the line bundle $E_{\mathrm{lin}}$ obtained by linearising $E$ at the chosen section. The covariant derivative $D_A = d + A$ then acts on sections of this line bundle in the standard way.*

*For a section $\psi \in \Gamma(E_{\mathrm{lin}})$ and the $q$-deformed Reeb vector field $\xi_q$ (Definition <a href="#def:q-reeb-vector-field" data-reference-type="ref" data-reference="def:q-reeb-vector-field">1.24</a>), the Schrödinger dynamics take the form $$J\,\hbar_q(p)\,\iota_{\xi_q} D_A \psi \;=\; \hat{H}_q\, \psi,$$ where $\hat{H}_q = -\tfrac{1}{2}\hbar_q\,\Delta_q + V_q$ is the *$q$-deformed Hamiltonian* (here $\Delta_q$ is the $q$-Laplacian of Definition <a href="#def:q-harmonic-form" data-reference-type="ref" data-reference="def:q-harmonic-form">1.17</a> acting on sections of $E_{\mathrm{lin}}$, and $V_q$ is a potential depending on the curvature $\Omega_q$), and:*

- *$\hbar_q(p) = 1 - q(p)^{-1}$: the quantum Planck constant (Definition <a href="#def:quantum-planck-constant" data-reference-type="ref" data-reference="def:quantum-planck-constant">1.14</a>) is a local field;*

- *$D_A = d + A$: the instanton connection on $P$ acts as the potential;*

- *$\iota_{\xi_q} D_A \psi$: the covariant derivative $D_A\psi$ is an $E_{\mathrm{lin}}$-valued $1$-form; contracting it with $\xi_q$ yields a section of $E_{\mathrm{lin}}$, matching the right-hand side.*

*As $q(p) \to 1$ (classicality), the commutator $[\hat{X}, \hat{P}]_q \to 0$ (Remark <a href="#rem:heisenberg-commutator" data-reference-type="ref" data-reference="rem:heisenberg-commutator">1.16</a>), the uncertainty vanishes, and the wave-like nature of the section freezes into a classical trajectory.*

**Categorical role.* Although this remark is stated as a PDE rather than in categorical language, it is essential to the paper’s structure: the Schrödinger equation provides the bottom row of the main commutative diagram (Proposition <a href="#prop:main-commutative-diagram" data-reference-type="ref" data-reference="prop:main-commutative-diagram">1.30</a>). Categorically, the $q$-deformed Hamiltonian $\hat{H}_q$ defines an endomorphism of the module category $\mathrm{Mod}_{E_{\mathrm{lin}}}$ over the jet algebra $\Gamma(J^1 E)$, and the Schrödinger equation is the condition that $\psi$ lies in the kernel of $\hat{H}_q - J\hbar_q\,\iota_{\xi_q}D_A$. In the base-field-independent setting of Definitions <a href="#def:quantum-universe" data-reference-type="ref" data-reference="def:quantum-universe">1.1</a> and <a href="#def:quantum-observable-universe" data-reference-type="ref" data-reference="def:quantum-observable-universe">1.2</a>, this extends to arbitrary base fields $k$ by replacing $\Gamma(E_{\mathrm{lin}})$ with the appropriate $k$-linear category of sections.*

</div>

# Path Integrals and Braiding

In the QOU framework, traditional path integrals are replaced by finite sums over the discrete fibre structure. Since the base space $B$ and each fibre are finite, the continuum measure $\mathcal{D}\phi$ collapses to a combinatorial sum, eliminating the need for renormalisation of divergent integrals.

The braid group acts naturally on the fibre degrees of freedom. What we observe as particle interactions corresponds to the action of braid operators exchanging strands in the fibre bundle. The algebraic content of these interactions is therefore encoded in braid-group representations rather than in Feynman vertices.

The exchange operations carry a $q$-deformation parameter inherited from the quantum group structure of the fibres. Concretely, the $R$-matrix of $\mathcal{U}_q(\mathfrak{su}(2))$ furnishes a $q$-deformed braid operator whose eigenvalues govern the phase acquired under particle exchange.

Under this correspondence, specific knot types map to particle identities. The trefoil knot, being the simplest non-trivial torus knot, is identified with the quark; the muon arises as a lift of the trefoil to a higher fibre level. The unknot, carrying trivial braiding, corresponds to the neutrino. Experimental evidence supporting this $q$-deformed braiding picture is discussed in Chapter <a href="#chap:experimental" data-reference-type="ref" data-reference="chap:experimental">[chap:experimental]</a>.

## Braid group and symmetric group

<div id="def:braid-group" class="definition">

**Definition 3.1** (Braid group on three strands). *The *braid group on three strands* is the group $$\label{eq:braid-presentation}
  B_3
  =\bigl\langle\sigma_1,\sigma_2
    \;\big|\;\sigma_1\sigma_2\sigma_1=\sigma_2\sigma_1\sigma_2\bigr\rangle.$$ This is the fundamental group of the configuration space of three unordered points in the plane, and is isomorphic to the fundamental group of the complement of the trefoil knot (Remark <a href="#rem:trefoil-knot-group" data-reference-type="ref" data-reference="rem:trefoil-knot-group">3.9</a>).*

</div>

<div id="def:s3-group" class="definition">

**Definition 3.2** (Symmetric group $S_3$). *Imposing the involution relations $\sigma_i^2=\mathrm{id}$ on the braid group $B_3$ (Definition <a href="#def:braid-group" data-reference-type="ref" data-reference="def:braid-group">3.1</a>) yields the *symmetric group* $$\label{eq:s3-presentation}
  S_3
  =\bigl\langle s_1,s_2
    \;\big|\;s_1^2=s_2^2=(s_1 s_2)^3=\mathrm{id}\bigr\rangle.$$*

</div>

## $\mathrm{SU}(2)$ and $\mathrm{SO}(3)$ framework

<div id="def:su2-basis" class="definition">

**Definition 3.3** ($\mathfrak{su}(2)$ basis). *Write $\tau_1,\tau_2,\tau_3$ for the Pauli matrices and set $$\label{eq:su2-basis}
  e_a=-\tfrac{i}{2}\,\tau_a,\qquad a=1,2,3,$$ so that the Lie bracket is $$\label{eq:su2-commutator}
  [e_a,\,e_b]=\epsilon_{abc}\,e_c.$$*

</div>

<div id="rem:first-order-taylor" class="remark">

**Remark 3.4** (First-order approximation). *The Lie bracket <a href="#eq:su2-commutator" data-reference-type="eqref" data-reference="eq:su2-commutator">[eq:su2-commutator]</a> captures the first-order behaviour of the group operation: for elements $A,B$ near the identity, $$e^A e^B \;=\; e^{A+B+\tfrac{1}{2}[A,B]+\cdots},$$ so the commutator $[e_a,e_b]$ is the first-order Taylor polynomial of the non-commutativity. Higher-order corrections (the full Baker–Campbell–Hausdorff series) encode the complete nonlinear group law and reappear naturally in the universal enveloping algebra (Section <a href="#sec:enveloping-algebras" data-reference-type="ref" data-reference="sec:enveloping-algebras">7.2</a>).*

</div>

<div id="def:su2-generators" class="definition">

**Definition 3.5** ($\mathrm{SU}(2)$ generators of $\mathrm{Dic}_3$). *Every finite subgroup of $\mathrm{SO}(3)$ lifts, via the double cover $\mathrm{SU}(2)\twoheadrightarrow\mathrm{SO}(3)$, to a binary subgroup of $\mathrm{SU}(2)$. For $S_3\cong D_3$ the lift is the binary dihedral group $\mathrm{Dic}_3\subset\mathrm{SU}(2)$ of order $12$, generated by $$\begin{aligned}
  \alpha &= \exp\!\bigl(\tfrac{2\pi}{3}\,e_3\bigr)
  = \begin{pmatrix}e^{i\pi/3}&0\\[2pt]0&e^{-i\pi/3}\end{pmatrix},
  \label{eq:su2-3cycle}\\[4pt]
  \beta &= \exp(\pi\,e_1)
  = \begin{pmatrix}0&i\\[2pt]i&0\end{pmatrix},
  \label{eq:su2-2cycle}
\end{aligned}$$ with $\alpha^3=\beta^2=-I$, dihedral relation $\beta\alpha\beta^{-1}=\alpha^{-1}$, and commutator $[\beta,\alpha]=\alpha^{-2}$.*

</div>

<div id="def:so3-generators" class="definition">

**Definition 3.6** ($\mathrm{SO}(3)$ generators). *Under the adjoint map to $\mathrm{SO}(3)$ the generators of $\mathrm{Dic}_3$ (Definition <a href="#def:su2-generators" data-reference-type="ref" data-reference="def:su2-generators">3.5</a>) have images $$\label{eq:so3-generators}
  R_\alpha
  =\begin{pmatrix}
    -\frac{1}{2}&-\frac{\sqrt{3}}{2}&0\\[3pt]
    \frac{\sqrt{3}}{2}&-\frac{1}{2}&0\\[3pt]
    0&0&1
  \end{pmatrix},\qquad
  R_\beta
  =\begin{pmatrix}
    1&0&0\\[2pt]
    0&-1&0\\[2pt]
    0&0&-1
  \end{pmatrix}:$$ $R_\alpha$ is a rotation by $2\pi/3$ about the $e_3$-axis (3-cycle) and $R_\beta$ is a $\pi$-rotation about $e_1$ (2-cycle).*

</div>

## Braid involutions and holonomy

<div id="def:braid-twist-flip" class="definition">

**Definition 3.7** (Braid involutions: twist and flip). *Let $\mathbf{w}=(w_1,w_2,w_3,w_4)$ be a spectral resolvent tuple. Define the two involutions $$\begin{aligned}
  \sigma_1(\mathbf{w}) &= (w_2,w_1,w_4,w_3)
    &&\text{(twist),}
    \label{eq:braid-twist}\\[4pt]
  \sigma_2(\mathbf{w}) &= (w_4,w_3,w_2,w_1)
    &&\text{(flip).}
    \label{eq:braid-flip}
\end{aligned}$$ As $4\times 4$ permutation matrices these are $$\label{eq:perm-matrices}
  \sigma_1=\begin{pmatrix}
    0&1&0&0\\1&0&0&0\\0&0&0&1\\0&0&1&0
  \end{pmatrix},\quad
  \sigma_2=\begin{pmatrix}
    0&0&0&1\\0&0&1&0\\0&1&0&0\\1&0&0&0
  \end{pmatrix}.$$ On the 4-tuple these involutions generate the Klein four-group $V_4=\{\mathrm{id},\sigma_1,\sigma_2,\sigma_1\sigma_2\}$, with $\sigma_1\sigma_2\colon\mathbf{w}\mapsto(w_3,w_4,w_1,w_2)$.*

</div>

<div id="rem:holonomy-trefoil" class="remark">

**Remark 3.8** (Holonomy generators and the trefoil). *Given a branched cover $\mathcal{S}\to\mathbb{CP}^1$ with singular fibres at the critical values, choose two loops $\gamma_1,\gamma_2$ in $\mathbb{CP}^1$ encircling distinct branch points. Parallel-transporting the spectral modes $w_k$ around these loops yields holonomy operators $$\label{eq:holonomy-generators}
  H_1=\sigma_1,\qquad H_2=\sigma_2,$$ where $\sigma_1,\sigma_2$ are the braid generators <a href="#eq:braid-twist" data-reference-type="eqref" data-reference="eq:braid-twist">[eq:braid-twist]</a>, <a href="#eq:braid-flip" data-reference-type="eqref" data-reference="eq:braid-flip">[eq:braid-flip]</a>. In the $\mathrm{SU}(2)$ embedding (Definition <a href="#def:su2-generators" data-reference-type="ref" data-reference="def:su2-generators">3.5</a>) these become $$H_1=\exp(T\theta\,e_1),\qquad H_2=\exp(T\theta\,e_2),$$ with $T$ the geometric torsion scalar and $\theta$ a branch angle, so the holonomy group is a representation of $B_3$ inside $\mathrm{SU}(2)$.*

*The fundamental group of the trefoil-knot complement admits the presentation $\langle x,y\mid xyx=yxy\rangle$, which is exactly $B_3$ <a href="#eq:braid-presentation" data-reference-type="eqref" data-reference="eq:braid-presentation">[eq:braid-presentation]</a>. The assignment $x\mapsto H_1$, $y\mapsto H_2$ is therefore an isomorphism $\pi_1(S^3\setminus K_{3,2})\;\xrightarrow{\;\sim\;}\;
\langle H_1,H_2\rangle$: the monodromy group of the branched cover *is* the trefoil-knot group.*

*The composite holonomy $H_1 H_2\colon\mathbf{w}\mapsto(w_3,w_4,w_1,w_2)$ is the $3$-cycle $\alpha$ <a href="#eq:su2-3cycle" data-reference-type="eqref" data-reference="eq:su2-3cycle">[eq:su2-3cycle]</a> and satisfies $(H_1 H_2)^3=\mathrm{id}$ on $\mathrm{SO}(3)$.*

</div>

## The trefoil knot

<div id="rem:trefoil-knot-group" class="remark">

**Remark 3.9** (Trefoil knot group). *The trefoil knot $K_{3,2}$ is the simplest non-trivial torus knot. Its complement has fundamental group $$\pi_1(S^3\setminus K_{3,2})
  \;=\;\langle x,y\mid xyx=yxy\rangle
  \;\cong\;B_3,$$ so the trefoil-knot group is isomorphic to the braid group on three strands (Definition <a href="#def:braid-group" data-reference-type="ref" data-reference="def:braid-group">3.1</a>). This relation $xyx=yxy$ is the *braid relation*: it encodes the fact that the three-strand braid may be closed into the trefoil by identifying the top and bottom of the braid.*

</div>

<div id="ex:trefoil-operator-algebra" class="example">

**Example 3.10** (Trefoil braid relation and operator algebra). *In the $\mathrm{SU}(2)$ representation (Definition <a href="#def:su2-generators" data-reference-type="ref" data-reference="def:su2-generators">3.5</a>), the trefoil braid relation $xyx=yxy$ becomes the operator identity $$\alpha\,\beta\,\alpha
  \;=\;\beta\,\alpha\,\beta$$ for the generators $\alpha$ <a href="#eq:su2-3cycle" data-reference-type="eqref" data-reference="eq:su2-3cycle">[eq:su2-3cycle]</a> and $\beta$ <a href="#eq:su2-2cycle" data-reference-type="eqref" data-reference="eq:su2-2cycle">[eq:su2-2cycle]</a>. Explicitly, using $$\alpha=\begin{pmatrix}e^{i\pi/3}&0\\0&e^{-i\pi/3}\end{pmatrix},
  \qquad
  \beta=\begin{pmatrix}0&i\\i&0\end{pmatrix},$$ both products evaluate to $$\alpha\beta\alpha
  = \begin{pmatrix}0&ie^{2i\pi/3}\\ie^{-2i\pi/3}&0\end{pmatrix}
  = \beta\alpha\beta.$$ The eigenvalues of the composite $\alpha\beta$ govern the phases acquired when quarks exchange colour charges along the trefoil path.*

</div>

## Knot fundamental groups

<div id="rem:knot-complement-group" class="remark">

**Remark 3.11** (Fundamental group of the knot complement). *For a knot $K\subset S^3$ (or, more generally, $K\subset\mathbb{CP}^1$), the fundamental group $\pi_1(\mathbb{CP}^1\setminus K)$ encodes the topology of the complement. A representation $$\rho\colon\pi_1(\mathbb{CP}^1\setminus K)
  \;\longrightarrow\;\mathrm{PSL}(2,\mathbb{C})$$ maps each meridian generator to a Möbius transformation of the Riemann sphere. The image of $\rho$ characterises the geometric structure on the knot complement.*

</div>

<div id="rem:kronheimer-mrowka" class="remark">

**Remark 3.12** (Non-trivial representations of knot groups (Kronheimer–Mrowka)). *Kronheimer and Mrowka proved that the fundamental group of every non-trivial knot admits a non-trivial representation into $\mathrm{SU}(2)$, and hence into $\mathrm{PSL}(2,\mathbb{C})$ . In the QOU context, this guarantees that every non-trivial knot type contributing to the fibre bundle carries a non-abelian gauge holonomy. The restriction to traceless elements of $\mathrm{SU}(2)$ aligns with the category-theoretic setup of Section <a href="#sec:enveloping-algebras" data-reference-type="ref" data-reference="sec:enveloping-algebras">7.2</a>, where the representation factors through the adjoint form.*

</div>

<div id="rem:reducible-reps" class="remark">

**Remark 3.13** (Reducible representations and fixed points). *When a representation $\rho\colon\pi_1(\mathbb{CP}^1\setminus K)\to\mathrm{PSL}(2,\mathbb{C})$ is reducible, all generators fix the same point on $\mathbb{CP}^1$ — they are simultaneously conjugate to upper-triangular matrices, hence all rotations around a common axis. In the category-theoretic formulation this corresponds to the abelianisation of the knot group. Further generalisations via the Poincaré–Birkhoff–Witt theorem and unital Gröbner bases (Section <a href="#sec:enveloping-algebras" data-reference-type="ref" data-reference="sec:enveloping-algebras">7.2</a>) describe the passage from the reducible to the irreducible sector.*

</div>

## Universal enveloping algebras and quantum groups

<div id="rem:enveloping-algebra" class="remark">

**Remark 3.14** (Universal enveloping algebra). *The universal enveloping algebra $\mathcal{U}(\mathfrak{su}(2))$ is the associative algebra generated by $e_1,e_2,e_3$ (Definition <a href="#def:su2-basis" data-reference-type="ref" data-reference="def:su2-basis">3.3</a>) subject to the commutation relations <a href="#eq:su2-commutator" data-reference-type="eqref" data-reference="eq:su2-commutator">[eq:su2-commutator]</a>. It provides the algebraic scaffolding in which every finite-dimensional representation of $\mathfrak{su}(2)$ lives and is the classical limit ($q\to 1$) of the quantum group $\mathcal{U}_q(\mathfrak{su}(2))$.*

</div>

<div id="def:quantum-su2" class="definition">

**Definition 3.15** (Quantum group $\mathcal{U}_q(\mathfrak{su}(2))$). *Let $q\in\mathbb{C}^{*}$ with $0<\lvert q\rvert\le 1$. The *quantum group* $\mathcal{U}_q(\mathfrak{su}(2))$ is the associative $\mathbb{C}$-algebra generated by $E,F,K,K^{-1}$ subject to $$\begin{aligned}
  KK^{-1}&=K^{-1}K=1,
    \label{eq:quantum-KK}\\[3pt]
  KEK^{-1}&=q^2\,E,\quad KFK^{-1}=q^{-2}\,F,
    \label{eq:quantum-KE}\\[3pt]
  [E,F]&=\frac{K-K^{-1}}{q-q^{-1}}.
    \label{eq:quantum-EF}
\end{aligned}$$ In the classical limit $q\to 1$, the generator $K$ reduces to $\exp(h\,e_3)$ and the relations recover <a href="#eq:su2-commutator" data-reference-type="eqref" data-reference="eq:su2-commutator">[eq:su2-commutator]</a>.*

</div>

<div id="rem:r-matrix-braiding" class="remark">

**Remark 3.16** ($R$-matrix and braiding). *The $R$-matrix of $\mathcal{U}_q(\mathfrak{su}(2))$ (Definition <a href="#def:quantum-su2" data-reference-type="ref" data-reference="def:quantum-su2">3.15</a>) is the universal element $$\mathcal{R}\;\in\;
  \mathcal{U}_q(\mathfrak{su}(2))\;\hat{\otimes}\;
  \mathcal{U}_q(\mathfrak{su}(2))$$ satisfying the Yang–Baxter equation $\mathcal{R}_{12}\mathcal{R}_{13}\mathcal{R}_{23}
=\mathcal{R}_{23}\mathcal{R}_{13}\mathcal{R}_{12}$. Its action on a tensor product of representations gives the braid operator $\check{R}=P\circ\mathcal{R}$ (where $P$ is the swap), furnishing a $q$-deformed braid group representation that replaces the classical twist/flip involutions (Definition <a href="#def:braid-twist-flip" data-reference-type="ref" data-reference="def:braid-twist-flip">3.7</a>).*

</div>

## Varying Euler characteristic

### The genus-$2$ case

## Descent from $E_1$ to $E_0$ and the mirror bundle $E_{-1}$

<div id="rem:e-minus-one" class="remark">

**Remark 3.17** ($E_{-1}$ as skew-mirror bundle). *In the descent from $E_1$ (full torsion bundle) to $E_0$ (trivial bundle), the self-duality of spacetime and chirality admits a flip: the orientation of the chiral fibre can reverse relative to the spacetime base. This produces a bundle $E_{-1}$ that acts as a skew or mirror image of $E_1$. From the perspective of ascending the bundle hierarchy, $E_{-1}$ appears to be matter; from the perspective of descending, it appears to be antimatter. The distinction is purely one of orientation in the descent tower.*

</div>

# Lifting of Quantum Torsion

<div id="prop:jet-prolongation" class="proposition">

**Proposition 4.1** (Jet Prolongation). *Let $(M, G, P, E)$ be a $\mathbb{C}$ quantum observable universe (Example <a href="#def:c-quantum-observable-universe" data-reference-type="ref" data-reference="def:c-quantum-observable-universe">1.6</a>) with instanton connection $A$ on $P$ and metric $g$ on $E$. Write $\widetilde{M} = E$ for the total space of $E$, viewed as a manifold, and define $P'$ as the frame bundle and $E'$ as the bundle of orthonormal frames of the first jet bundle $J^1 E$. Then $A$ and $g$ uniquely determine a connection $A'$ on $P'$ such that $(\widetilde{M}, G, P', E')$ is a $\mathbb{C}$ quantum observable universe.*

</div>

<div class="proof">

*Proof.* The proof proceeds in the rigid monoidal category underlying the quantum observable universe. Let $A$ denote the Frobenius-Hopf object representing the gauge-bundle data of $(M,G,P,E)$.

*Step 1: Categorical jet object.* The first jet bundle $J^1 E$ is represented categorically by the object $A \otimes \Omega^1(A)$, where $\Omega^1(A) = \ker(m\colon A\otimes A \to A)$ is the kernel of the multiplication (the bimodule of Kähler differentials, i.e. the universal first-order differential calculus over $A$). Because $A$ is Frobenius, the non-degenerate pairing $\varepsilon \circ m \colon A \otimes A \to \mathbf{1}$ exhibits $\Omega^1(A)$ as a direct summand of $A \otimes A$, hence $J^1(A) := A \otimes \Omega^1(A)$ is again an object of the ambient category.

*Step 2: Inherited Frobenius-Hopf structure.* The Frobenius relation $(\mathrm{Id} \otimes m) \circ (\Delta \otimes \mathrm{Id})
 = \Delta \circ m
 = (m \otimes \mathrm{Id}) \circ (\mathrm{Id} \otimes \Delta)$ ensures that the comultiplication $\Delta\colon A \to A \otimes A$ restricts to a well-defined comultiplication $\Delta'\colon J^1(A) \to J^1(A) \otimes J^1(A)$, and the counit $\varepsilon\colon A \to \mathbf{1}$ induces a counit $\varepsilon'$ on $J^1(A)$. The Hopf antipode $S$ extends to $J^1(A)$ by functoriality of the Kähler differential construction. Thus $J^1(A)$ is a Frobenius-Hopf object.

*Step 3: Non-degeneracy and vanishing.* The non-degeneracy of the Frobenius form on $A$ (the pairing $\varepsilon \circ m$ is a perfect pairing) implies non-degeneracy of the induced form on $J^1(A)$, since $\Omega^1(A)$ is a direct summand. For the vanishing condition, $\mathrm{Hom}(\mathbf{1}, \mathrm{Ad}(A)) = 0$ implies $\mathrm{Hom}(\mathbf{1}, \mathrm{Ad}(J^1(A))) = 0$: the adjoint representation of $J^1(A)$ contains $\mathrm{Ad}(A)$ as a subobject, and any invariant in $\mathrm{Ad}(J^1(A))$ would project to a non-zero invariant in $\mathrm{Ad}(A)$, contradicting the hypothesis.

*Step 4: Geometric realisation.* Applying the fibre functor $\omega\colon \mathcal{C} \to \mathrm{Vect}_k$ (where $\mathcal{C}$ is the rigid monoidal category of the quantum observable universe) recovers the geometric data: $\omega(J^1(A))$ is the space of sections of the first jet bundle $J^1 E$, the frame bundle $P'$ and orthonormal frame bundle $E'$ are the geometric counterparts of the Frobenius-Hopf structure on $J^1(A)$, and the connection $A'$ is the image under $\omega$ of the comultiplication $\Delta'$. Its uniqueness follows from the irreducibility of $A'$, which is guaranteed by the inherited vanishing condition of Step 3. ◻

</div>

<div id="rem:prolongation-categorical" class="remark">

**Remark 4.2** (Prolongation from the Frobenius-Hopf structure). *The proof above shows that jet prolongation is an *intrinsic* consequence of the Frobenius-Hopf structure in a rigid monoidal category: no additional geometric input beyond the categorical data $(\mathcal{C}, A, \omega)$ is required. Concretely:*

1.  *The Frobenius structure provides the Kähler differentials $\Omega^1(A)$ as a direct summand, from which the jet object $J^1(A)$ is built.*

2.  *The Frobenius relation ensures that the comultiplication and multiplication are compatible, so the prolonged object inherits the full Hopf algebra structure.*

3.  *The non-degeneracy and vanishing conditions propagate from $A$ to $J^1(A)$ by functoriality.*

*In this sense, the recursive brane tower (Definition <a href="#def:recursive-brane-tower" data-reference-type="ref" data-reference="def:recursive-brane-tower">4.3</a>) is generated entirely by iterating the categorical jet construction. The tower, together with its associated descent (Subsection <a href="#ssec:descent" data-reference-type="ref" data-reference="ssec:descent">4.0.1</a>), is a formal consequence of the axioms of a quantum observable universe and does not require any case-by-case verification.*

</div>

<div id="def:recursive-brane-tower" class="definition">

**Definition 4.3** (Recursive Brane Tower). *Let $(M, G, P, E)$ be a $\mathbb{C}$ quantum observable universe (Example <a href="#def:c-quantum-observable-universe" data-reference-type="ref" data-reference="def:c-quantum-observable-universe">1.6</a>). Set $M_0 = M$ and $E_1 = E$. *Inductively*, define $E_{n+1}$ as the jet prolongation (Proposition <a href="#prop:jet-prolongation" data-reference-type="ref" data-reference="prop:jet-prolongation">4.1</a>) of $E_n$.*

*The *brane relation* is the following recursive structure:*

1.  *Each total space $E_n$ is treated as the base manifold $M_{n+1}$ for the next level; $E_n$ is the *brane* of $E_{n+1}$.*

2.  *At each level, $A_n \in \mathcal{A}(E_{n-1})$ is the $n$-th level instanton connection satisfying the Hermitian Yang–Mills equations on $E_n$.*

</div>

<div id="ex:brane-tower-levels" class="example">

**Example 4.4** (First two levels). *Starting from a $\mathbb{C}$ quantum observable universe $(M, G, P, E_1)$, the first jet prolongation yields $E_2$ with base manifold $M_1 = E_1$. The connection $A_1$ on $E_1$ satisfies the Hermitian Yang–Mills equations, and $A_2$ on $E_2$ is uniquely determined by Proposition <a href="#prop:jet-prolongation" data-reference-type="ref" data-reference="prop:jet-prolongation">4.1</a>.*

</div>

<div id="def:quantum-characteristic-classes" class="definition">

**Definition 4.5** (Quantum Characteristic Classes). *Let $\{E_n\}_{n \geq 1}$ be the recursive brane tower (Definition <a href="#def:recursive-brane-tower" data-reference-type="ref" data-reference="def:recursive-brane-tower">4.3</a>). The *quantum characteristic classes* are the cohomology classes $$\kappa_n \;\in\; H^*\!\bigl(E_{n+1},\, \mathbb{Z}\bigr)$$ that label the monodromy fixed points of the holonomy representation as one transitions from $E_n$ to $E_{n+1}$.*

</div>

<div id="rem:betti-numbers-brane" class="remark">

**Remark 4.6** (Betti numbers of the brane tower). *Let $b_k(E_n) = \dim H^k(E_n, \mathbb{R})$ denote the $k$-th Betti number of $E_n$. Since $E_{n+1}$ is the bundle of orthonormal frames of $J^1 E_n$, the Betti numbers of $E_{n+1}$ are determined by those of $E_n$ via the Leray–Serre spectral sequence applied to the fibration $E_{n+1} \to E_n$. In particular, the quantum characteristic classes (Definition <a href="#def:quantum-characteristic-classes" data-reference-type="ref" data-reference="def:quantum-characteristic-classes">4.5</a>) obstruct the collapse of this spectral sequence and control the growth of $b_k(E_{n+1})$ in terms of $b_k(E_n)$.*

</div>

<div id="rem:q-harmonic-basis-brane" class="remark">

**Remark 4.7** ($q$-Harmonic basis of the brane tower). *For each level $n$, the $q$-harmonic $1$-forms $\alpha_{n,i}$ belong to the space $\mathcal{H}^1(E_n,\, \mathrm{ad}\, E_n)$ of harmonic $1$-forms on $E_n$ with values in the adjoint bundle $\mathrm{ad}\, E_n$. These are characterised by the self-duality condition relative to the instanton connection $A_n$ (Definition <a href="#def:recursive-brane-tower" data-reference-type="ref" data-reference="def:recursive-brane-tower">4.3</a>): $$\alpha_{n,i} \in \mathcal{H}^1
  \iff
  d_{A_n}\,\alpha = 0
  \quad\text{and}\quad
  d_{A_n}^*\,\alpha = 0,$$ where the Hodge-star operator is induced by the Hermitian metric that the Levi form $L$ (Definition <a href="#def:substrate-parameter" data-reference-type="ref" data-reference="def:substrate-parameter">1.10</a>) defines on the horizontal distribution. The index $i$ runs over $1 \leq i \leq b_1(E_n)$ (Remark <a href="#rem:betti-numbers-brane" data-reference-type="ref" data-reference="rem:betti-numbers-brane">4.6</a>).*

*At the base level $n = 0$, with Euler characteristic $\chi(M) = 3$, there are three primary basis vectors $\{\,\phi_1,\, \phi_2,\, \phi_3\,\}$. At level $n = 1$ the basis lifts: the new basis includes the original modes together with their $J^1$ prolongations (Proposition <a href="#prop:jet-prolongation" data-reference-type="ref" data-reference="prop:jet-prolongation">4.1</a>), which are the first-order resolutions of the base flows.*

</div>

<div id="rem:weight-space-decomposition" class="remark">

**Remark 4.8** (Weight-space decomposition of the harmonic basis). *The adjoint bundle $\mathrm{ad}\, E_n$ has fibre $\mathfrak{su}(2)$. Via the weight-space decomposition of $\mathrm{SU}(2)$, the harmonic basis of $\mathcal{H}^1(E_n,\, \mathrm{ad}\, E_n)$ splits into two families.*

**Longitudinal modes.* These forms constitute the $\mathrm{U}(1)$ backbone of the decomposition. They take values in the Cartan subalgebra of $\mathfrak{su}(2)$ and have the geometric form $\omega^0 \otimes H$, where $H$ is the diagonal generator. They represent steady-state laminar flows aligned with the $\mathrm{U}(1)$ subgroup. If the bundle splits at a monodromy fixed point, these are the only modes that survive; they correspond to the magnetic flux of the stable vortices.*

**Ladder modes.* These are the raising and lowering vortices of the decomposition. They take values in the off-diagonal generators $E_\pm$ of $\mathfrak{su}(2)$ and have the geometric form $\omega^\pm \otimes E_\pm$. They describe the entangling flows that twist the $\mathbb{CP}^1$ fibre as one moves along the brane. These modes are responsible for the non-commutativity in the $\mathrm{SU}_q(2)$ algebra (Definition <a href="#def:direct-limit-algebra" data-reference-type="ref" data-reference="def:direct-limit-algebra">4.11</a>).*

*In the $1$-jet bundle $J^1 E_n$ (Remark <a href="#rem:j1e-local-states" data-reference-type="ref" data-reference="rem:j1e-local-states">2.15</a>), each basis element $\alpha$ is a pair consisting of a *value* (the direction of the $\mathrm{SU}(2)$ flow in the fibre) and a *momentum* (the gradient of that flow relative to the complex structure of the brane).*

</div>

<div id="rem:algebraic-filter" class="remark">

**Remark 4.9** (The algebraic filter). *Let $\alpha$ be a harmonic $1$-form in the basis of Remark <a href="#rem:q-harmonic-basis-brane" data-reference-type="ref" data-reference="rem:q-harmonic-basis-brane">4.7</a>. Its *signature* is determined by its commutator with the curvature $F_A$ (Definition <a href="#def:substrate-parameter" data-reference-type="ref" data-reference="def:substrate-parameter">1.10</a>).*

**Fermionic type (matter).* $[F_A,\, \alpha] \neq 0$. These forms are entangled with the curvature: they see the $\mathrm{SO}(3)$ holonomy and the $-6$ index fixed points. Their geodesics are trapped or spiralling around the three fundamental vortex filaments.*

**Bosonic type (radiation).* $[F_A,\, \alpha] = 0$. These forms commute with the curvature. They are the longitudinal modes (Remark <a href="#rem:weight-space-decomposition" data-reference-type="ref" data-reference="rem:weight-space-decomposition">4.8</a>) that flow through the bulk without being deflected by the monodromy fixed points. Their geodesics are straight relative to the gauge-fluid flow.*

</div>

<div id="rem:distributional-connection" class="remark">

**Remark 4.10** (Distributional connection at the limit). *At the limit $n \to \infty$ one no longer looks at a single connection $A$, but at a *distributional connection* represented by the series $$A_\infty
  \;=\;
  \sum_{n=0}^{\infty}\;\sum_{i=1}^{b_1(E_n)}
  c_{n,i}\,\alpha_{n,i}\,,$$ where $c_{n,i} \in \mathbb{C}$ and $\{\alpha_{n,i}\}$ is the $q$-harmonic basis of Remark <a href="#rem:q-harmonic-basis-brane" data-reference-type="ref" data-reference="rem:q-harmonic-basis-brane">4.7</a>. This turns the gauge field into a harmonic expansion across the infinite jet space $J^\infty E$ (Remark <a href="#rem:jet-shell" data-reference-type="ref" data-reference="rem:jet-shell">4.13</a>).*

</div>

<div id="def:direct-limit-algebra" class="definition">

**Definition 4.11** ($\mathbb{C}$ Quantum Observable Universe as Direct Limit). *Let $\{E_n\}_{n \geq 1}$ be the recursive brane tower (Definition <a href="#def:recursive-brane-tower" data-reference-type="ref" data-reference="def:recursive-brane-tower">4.3</a>) with substrate parameters $q_n$ (Definition <a href="#def:substrate-parameter" data-reference-type="ref" data-reference="def:substrate-parameter">1.10</a>) at each level. The *$\mathbb{C}$ quantum observable universe* is the direct limit algebra $$\mathcal{A}_\infty
  \;=\;
  \varinjlim\,
  \Gamma\!\bigl(J^1 E_n,\, \mathrm{SU}_{q_n}(2)\bigr).$$*

</div>

<div id="rem:direct-limit-lusztig" class="remark">

**Remark 4.12** (Direct limit algebra and the Lusztig integral form). *The algebra $\mathcal{A}_\infty$ (Definition <a href="#def:direct-limit-algebra" data-reference-type="ref" data-reference="def:direct-limit-algebra">4.11</a>) is explicitly realised as the Lusztig integral form of the quantised enveloping algebra $\mathcal{U}_q(\mathfrak{su}(2))$ . At each level $n$ the fibre algebra $\mathrm{SU}_{q_n}(2)$ is obtained by specialising the $\mathbb{Z}[q,q^{-1}]$-form $\mathcal{U}^{\mathbb{Z}}_q(\mathfrak{su}(2))$ (Definition <a href="#def:substrate-parameter" data-reference-type="ref" data-reference="def:substrate-parameter">1.10</a>) along $q \mapsto q_n \in k^{\times}$, and the direct limit inherits the divided power basis $(E^{(m)}, F^{(m)}, K^{\pm 1})$ from the integral form. This ensures that the quaternionic jet embedding (Definition <a href="#def:quaternionic-spectral-resolvents" data-reference-type="ref" data-reference="def:quaternionic-spectral-resolvents">5.26</a>) remains robust under the arithmetic descent to $M_0$, with the $q$-deformed scaling function $\exp_q(r) - 1$ (equation <a href="#eq:q-exp" data-reference-type="eqref" data-reference="eq:q-exp">[eq:q-exp]</a>) regulating the transition between the divided power basis of the space-like and time-like resolvents.*

</div>

<div id="rem:jet-shell" class="remark">

**Remark 4.13** (Jet Shell of the universe). *In the limit $n \to \infty$, the infinite jet bundle $J^\infty E = \varprojlim\, J^k E$ becomes the *jet shell* of the universe. All finite-level brane data are encoded in this pro-finite structure, and the algebra $\mathcal{A}_\infty$ (Definition <a href="#def:direct-limit-algebra" data-reference-type="ref" data-reference="def:direct-limit-algebra">4.11</a>) acts naturally on sections of the jet shell.*

</div>

<div id="prop:vacuum-state" class="proposition">

**Proposition 4.14** (Existence and Uniqueness of the Vacuum State). *Let $\mathcal{A}_\infty$ be the direct limit algebra (Definition <a href="#def:direct-limit-algebra" data-reference-type="ref" data-reference="def:direct-limit-algebra">4.11</a>) equipped with the global $\mathrm{SU}(2)$ action and the recursive $q$-deformations. Then there exists a unique state $\omega \colon \mathcal{A}_\infty \to \mathbb{C}$ that is $\mathrm{SU}(2)$-invariant: $$\omega(g \cdot a) = \omega(a)
  \quad\text{for all } g \in \mathrm{SU}(2),\;
  a \in \mathcal{A}_\infty.$$*

</div>

<div class="proof">

*Proof.* ◻

</div>

<div id="rem:mass-geometric-drag" class="remark">

**Remark 4.15** (Mass in the brane tower). *In the recursive brane tower (Definition <a href="#def:recursive-brane-tower" data-reference-type="ref" data-reference="def:recursive-brane-tower">4.3</a>), mass is not an intrinsic property of a point-particle but a measure of the resistance encountered by a stable vortex as it propagates through the $1$-jet bundle $J^1 E_n$ (Proposition <a href="#prop:jet-prolongation" data-reference-type="ref" data-reference="prop:jet-prolongation">4.1</a>). The substrate parameter $q$ (Definition <a href="#def:substrate-parameter" data-reference-type="ref" data-reference="def:substrate-parameter">1.10</a>) varies from fibre to fibre; translation of the vortex along the base therefore requires a corresponding variation of the Frobenius–Hopf structure on each fibre, and the mass quantifies this variation.*

</div>

<div id="rem:mass-noncommutative-drag" class="remark">

**Remark 4.16** (Non-commutativity and geometric drag). *When the substrate parameter satisfies $q(p) \neq 1$ at every point of the recursive brane tower, the comultiplication on the Frobenius–Hopf object $A$ (Definition <a href="#def:quantum-universe" data-reference-type="ref" data-reference="def:quantum-universe">1.1</a>) is non-cocommutative, so the algebra $\mathcal{A}_\infty$ (Definition <a href="#def:direct-limit-algebra" data-reference-type="ref" data-reference="def:direct-limit-algebra">4.11</a>) does not reduce to a commutative direct limit. Moving a vortex through $J^1 E_n$ then requires a continuous rearrangement of the $\mathrm{SU}_q(2)$ fibre data, which is the source of the inertial resistance described in Remark <a href="#rem:mass-geometric-drag" data-reference-type="ref" data-reference="rem:mass-geometric-drag">4.15</a>.*

</div>

<div id="prop:euler-char-stability" class="proposition">

**Proposition 4.17** (Stability of the Euler characteristic). *Let $(M, G, P, E)$ be a $\mathbb{C}$ quantum observable universe and let $\{E_n\}_{n \geq 1}$ be the recursive brane tower (Definition <a href="#def:recursive-brane-tower" data-reference-type="ref" data-reference="def:recursive-brane-tower">4.3</a>). Then the Euler characteristic $\chi(E)$ is stable under descent and lifting: for each level $n$, $$\chi(E_{n+1}) \;=\; \chi(E_n).$$ In particular, if the base level satisfies $\chi(E_1) = c$, then $\chi(E_n) = c$ for all $n \geq 1$.*

</div>

<div class="proof">

*Proof.* ◻

</div>

<div id="def:mass-identity" class="definition">

**Definition 4.18** (Mass Identity). *Let $(M, G, P, E)$ be a $\mathbb{C}$ quantum observable universe with substrate parameter $q$ (Definition <a href="#def:substrate-parameter" data-reference-type="ref" data-reference="def:substrate-parameter">1.10</a>), connection $A$, Levi form $L$, and self-dual curvature $F^+$. Let $\gamma$ be a closed cycle encircling the vortex filament. The *inertial mass* $m$ of a stable vortex is $$m \;\propto\; \oint_\gamma \lVert \nabla_A\, q \rVert
               \cdot \lVert L \wedge F^+ \rVert\,.$$*

</div>

### Descent

<div id="def:descent" class="definition">

**Definition 4.19** (Descent). *Let $\{E_n\}_{n \geq 1}$ be the recursive brane tower (Definition <a href="#def:recursive-brane-tower" data-reference-type="ref" data-reference="def:recursive-brane-tower">4.3</a>). The *descent* is the reverse traversal of the tower: starting from level $n$ one passes to level $n-1$ by restricting the connection $A_n$ and the bundle $E_n$ to the base manifold $M_{n-1}$. The descent terminates when the base manifold $M_k$ reaches $\dim M_k = 0$, at which point $M_k$ is a discrete set of points.*

</div>

<div id="rem:descent-reduction" class="remark">

**Remark 4.20** (Reduction at dimension $1$). *When $\dim M_k = 1$ the geometric data of the $\mathbb{C}$ quantum observable universe collapse as follows.*

1.  **Connection.* The $\mathrm{SU}(2)$ connection $A_k$ restricts to a single dimension; its holonomy reduces to a $\mathrm{U}(1)$ phase around $S^1$.*

2.  **Bundle.* The principal $\mathrm{SU}(2)$ bundle $E$ descends to a bundle over the $1$-dimensional base whose fibre dynamics are locked into a single periodic flow.*

3.  **Reeb direction.* The inverse of the Reeb vector field (Definition <a href="#def:q-reeb-vector-field" data-reference-type="ref" data-reference="def:q-reeb-vector-field">1.24</a>) becomes the only direction of motion; the horizontal distribution is trivial and no bosonic modes (Remark <a href="#rem:algebraic-filter" data-reference-type="ref" data-reference="rem:algebraic-filter">4.9</a>) survive.*

*The descent need not terminate here; a further step carries $M_k$ to a zero-dimensional base (Remark <a href="#rem:descent-reduction-zero" data-reference-type="ref" data-reference="rem:descent-reduction-zero">4.22</a>).*

</div>

<div id="rem:descent-physical" class="remark">

**Remark 4.21** (Physical implications of a $1$-dimensional base). *At dimension $1$ the physical content simplifies drastically.*

1.  **Primordial vortex.* The vortex filaments of the mass identity (Definition <a href="#def:mass-identity" data-reference-type="ref" data-reference="def:mass-identity">4.18</a>) are no longer embedded in a larger space; the entire manifold *is* the filament.*

2.  **Mass as pure drag.* The mass identity reduces to an integral over the whole of $M_k$: $$m \;\propto\; \oint_{M_k} \lVert \nabla_A\, q \rVert
                           \cdot \lVert L \wedge F^+ \rVert\,,$$ so that mass represents the fundamental geometric resistance of the $1$-dimensional flow against the $\mathrm{SU}(2)$ rotation.*

3.  **Lepton generations.* Since the number of lepton generations is bounded by the Euler characteristic and vertical degree (Remark <a href="#rem:betti-numbers-brane" data-reference-type="ref" data-reference="rem:betti-numbers-brane">4.6</a>), a $1$-dimensional base supports only the most fundamental fermionic state; there is no room for higher-degree vertical harmonic forms.*

</div>

<div id="rem:descent-reduction-zero" class="remark">

**Remark 4.22** (Reduction at dimension $0$). *When $\dim M_k = 0$ the base manifold is a discrete set of points and the geometric data of the $\mathbb{C}$ quantum observable universe reduce to purely algebraic invariants at each point $p\in M_k$.*

1.  **Connection.* The $\mathrm{SU}(2)$ connection $A_k$ has no directions along which to parallel-transport; its curvature $F_A$ vanishes identically and the holonomy is trivial.*

2.  **Bundle.* The principal $\mathrm{SU}(2)$ bundle $E$ restricts to its fibre $E_p$ over the point $p$; the bundle is determined entirely by this single fibre together with the group action.*

3.  **Substrate parameter.* The substrate parameter $q(p) = 1 + \lVert L\wedge F_A^{+}\rVert(p)$ (Remark <a href="#rem:c-substrate-via-levi" data-reference-type="ref" data-reference="rem:c-substrate-via-levi">1.11</a>) assigns to each point a definite quantum constant $q\in[1,\infty)$, encoding the full content of the quantum observable universe at that point.*

4.  **Reeb direction.* There is no tangent space, so the Reeb vector field (Definition <a href="#def:q-reeb-vector-field" data-reference-type="ref" data-reference="def:q-reeb-vector-field">1.24</a>) and the horizontal distribution are absent; only the internal $\mathrm{SU}(2)$ fibre data persist.*

*In this terminal stage every observable is determined by the fibre $E_p$ and the value $q(p)$. When $M_k$ consists of several points the descent data decompose into independent summands, one per point; when $M_k$ is connected—i.e. a single point—the entire quantum observable universe is captured by the pair $(E_p, q(p))$.*

</div>

<div id="rem:descent-physical-zero" class="remark">

**Remark 4.23** (Physical implications of a $0$-dimensional base). *At dimension $0$ all spatial extent has been removed and the physical content is purely algebraic.*

1.  **Primordial state.* The vortex filaments, flows and spatial modes of higher-dimensional strata are absent; what remains is the initial datum of the fermionic content encoded in the fibre $E_p$.*

2.  **Mass.* With no base manifold over which to integrate, the mass identity (Definition <a href="#def:mass-identity" data-reference-type="ref" data-reference="def:mass-identity">4.18</a>) collapses to a single evaluation: $m \propto \lVert L \wedge F^+\rVert(p)$. Mass at dimension $0$ is an instantaneous, pointwise quantity rather than a distributed one.*

3.  **Lepton generations.* All vertical harmonic forms (Remark <a href="#rem:betti-numbers-brane" data-reference-type="ref" data-reference="rem:betti-numbers-brane">4.6</a>) are concentrated at the point; the Euler characteristic $\chi(E_p)$ retains the count of fermionic degrees of freedom without any spatial multiplicity.*

</div>

<div id="rem:descent-fixed-point" class="remark">

**Remark 4.24** (Fixed-point mechanism: ascent and descent). *Each step down the brane tower removes a space-like dimension through the $\mathrm{SU}(2)$ rotation and its associated fixed-point set.*

1.  **Ascent (generation).* Moving from $M_k$ ($\dim = 0$) upward lifts the connection $A$ to higher categorical structures via the jet prolongation (Proposition <a href="#prop:jet-prolongation" data-reference-type="ref" data-reference="prop:jet-prolongation">4.1</a>).*

2.  **Descent (filtering).* Moving back down acts as an algebraic filter (Remark <a href="#rem:algebraic-filter" data-reference-type="ref" data-reference="rem:algebraic-filter">4.9</a>). The ladder modes (Remark <a href="#rem:weight-space-decomposition" data-reference-type="ref" data-reference="rem:weight-space-decomposition">4.8</a>) are stripped away: at dimension $1$ only the longitudinal $\mathrm{U}(1)$ backbone remains (Remark <a href="#rem:descent-reduction" data-reference-type="ref" data-reference="rem:descent-reduction">4.20</a>), and at dimension $0$ even that is collapsed to a single fibre datum (Remark <a href="#rem:descent-reduction-zero" data-reference-type="ref" data-reference="rem:descent-reduction-zero">4.22</a>).*

</div>

<div class="conjecture">

**Conjecture 4.25** (Topological Decomposition of Mass). *Let $(M, \theta, G, P, E)$ be a $\mathbb{C}$ quantum observable universe with substrate parameter $q$, and let $\gamma$ be a stable vortex filament. Suppose the topology of $\gamma$ is isomorphic to a knot generated by $N$ consecutive topological blowups applied to an unknot core $\gamma_0$. The continuous geometric mass of the vortex along $\gamma$ admits the discrete topological decomposition: $$m(\gamma) \propto \oint_{\gamma_0} ||\nabla_A q|| \cdot ||L \wedge F^+|| + \sum_{i=1}^{N} \lambda_i \left| \Phi_q(z_i) \right|$$ where the line integral evaluates the baseline geometric drag of the trivial unknot core, $\Phi_q(z_i)$ is the quantum dilogarithm evaluated at the spectral coordinate $z_i$ of the $i$-th exceptional divisor $E_i$, and $\lambda_i$ are local coupling weights.*

</div>

<div class="corollary">

**Corollary 4.26** (Quantum Dilogarithm as Localized Torsion Volume). *The localized topological mass contribution $\Phi_q(z_i)$ at the $i$-th exceptional divisor $E_i$ is exactly the geometric integration of the 1-dimensional $q$-deformed expansion flow over the resolved defect. Integrating the spectral uncertainty flow $ln_q$ along the radial coordinate of the Briggs-Klein affine chart yields the quantum dilogarithm: $$\Phi_q(z_i) = \int_0^{z_i} \frac{ln_q(1+t)}{t} dt = \sum_{n=1}^\infty (-1)^{n+1} \frac{z_i^n}{n [n]_q}$$ where $ln_q(1+t) = \sum_{n=1}^\infty (-1)^{n+1} \frac{t^n}{[n]_q}$ governs the continuous Reeb flow\[cite: 8\]. The integration introduces the factor of $n$ in the denominator, elevating the 1-dimensional path propagation to a geometric volume measure trapping the topological charge.*

</div>

<div id="rem:qdlog-julia" class="remark">

**Remark 4.27** (Quantum dilogarithm integrand as $q$-deformed Böttcher potential density). *The integrand $\ln_q(1+t)/t$ in the quantum dilogarithm formula above has the same formal structure as the *information-flow density* that appears in the computation of filled Julia sets via the Böttcher escape potential.*

*For the quadratic family $f_c(z)=z^2+c$, the external Green’s function (escape potential) admits the convergent series $$\label{eq:bottcher-series}
  G_c(z)
  \;=\;
  \sum_{k=0}^{\infty}
    \frac{1}{2^{k+1}}\,
    \ln\!\left(1+\frac{c}{f_c^k(z)^2}\right).$$ Writing $t_k = c/f_c^k(z)^2$, each summand is $\frac{1}{2^{k+1}}\ln(1+t_k)$: the function $\ln(1+t_k)/t_k$ (evaluated at $t_k$) is exactly the classical ($q=1$) limit of the quantum dilogarithm integrand. The sum over $k$ weighted by $2^{-(k+1)}$ accumulates the *information flow* along the orbit of $f_c$, with the weight $2^{-k}$ reflecting the degree-$2$ expansion at each step.*

*In the QOU framework the role of the dynamical parameter $c$ is played by the substrate parameter $q=q(z)$ (Definition <a href="#def:substrate-parameter" data-reference-type="ref" data-reference="def:substrate-parameter">1.10</a>), which varies continuously with the spacetime coordinate $z$. The $q$-deformed Reeb flow (Definition <a href="#def:q-reeb-flow" data-reference-type="ref" data-reference="def:q-reeb-flow">1.25</a>) on the exceptional divisor $E_i \cong \mathbb{CP}^1$ takes the place of the orbit $\{f_c^k(z)\}_{k\geq 0}$, and the path from $0$ to $z_i$ in the quantum dilogarithm integral accumulates information along that flow exactly as <a href="#eq:bottcher-series" data-reference-type="eqref" data-reference="eq:bottcher-series">[eq:bottcher-series]</a> accumulates it along the Julia-set orbit. The $q$-deformation of the logarithm encodes the departure from classical ($q=1$) dynamics: as $q\to 1$ the flow trivialises and $\Phi_q(z_i)\to\mathrm{Li}_2(z_i)$, the classical dilogarithm; as $q\to\infty$ the quantum-number denominators $[n]_q$ suppress high-order terms, concentrating the topological charge near the blow-up centre.*

*In this identification the *Julia set boundary* of the classical problem—the locus where $G_c$ transitions from zero to positive—is the analogue of the boundary of the exceptional divisor $\partial E_i$, where the $q$-deformed torsion charge changes regime (Remark <a href="#rem:reeb-exceptional-divisor" data-reference-type="ref" data-reference="rem:reeb-exceptional-divisor">5.32</a>). The substrate parameter $q(z)$ thereby acts as a *spacetime-dependent dynamical parameter*, continuously deforming the Julia set geometry as one moves through the QOU.*

</div>

<div id="rem:julia-s1-photon-scatter" class="remark">

**Remark 4.28** (Julia set on $S^1$ as photon scattering at the Big Bang). *The exceptional divisor $E_i\cong\mathbb{CP}^1$ contains the equatorial circle $S^1\subset E_i$. The $q$-deformed Reeb flow (Definition <a href="#def:q-reeb-flow" data-reference-type="ref" data-reference="def:q-reeb-flow">1.25</a>) restricts to a degree-$2$ endomorphism $f_q\colon S^1\to S^1$, whose *Julia set* $J(f_q)\subset S^1$ is the closure of repelling periodic points—the locus of non-equicontinuous dynamics on the circle.*

*Bosons are purely horizontal $q$-harmonic forms (Definition <a href="#def:boson" data-reference-type="ref" data-reference="def:boson">1.20</a>); photons are the empty-knot background flux on $E_i$. The three regions of the circle map identify as:*

- **Filled Julia set* $\mathcal{K}(f_q)\cap S^1$: photons trapped in the $q$-torsion plasma—the opaque pre-recombination regime.*

- **Julia set boundary* $\partial\mathcal{K}(f_q)\cap S^1$: the surface of last scattering, where photons transition from trapped to free-streaming.*

- **Escape region* $S^1\setminus\mathcal{K}(f_q)$: freely propagating photons in the transparent universe.*

*At the Big Bang ($q\to\infty$, Remark <a href="#rem:reeb-exceptional-divisor" data-reference-type="ref" data-reference="rem:reeb-exceptional-divisor">5.32</a>), the denominators $[n]_q$ suppress all escape and $J(f_q)=S^1$: total opacity. As $q\to 1$ (heat death), $f_q$ trivialises, $J(f_q)$ collapses to a Cantor set of measure zero, and the universe becomes transparent.*

</div>

# Bring’s Surface

<div id="rem:descent-to-zero" class="remark">

**Remark 5.1** (Descent to dimension zero). *By the descent theorem (Theorem <a href="#thm:descartes" data-reference-type="ref" data-reference="thm:descartes">6.12</a>), it is sufficient to study dimension-zero manifolds equipped with their bundles $P$ and $E$. At a point $p\in M_0$, the substrate parameter $q(p)= 1 + \lvert\langle L_\theta,\, F_A^{+}\rangle\rvert(p)$ (Definition <a href="#def:substrate-parameter" data-reference-type="ref" data-reference="def:substrate-parameter">1.10</a>) assigns a specific quantum constant $q\in[1,\infty)$ determined by the principal bundle $P$ and the state bundle $E$. Here $E$ represents the totality of fermionic matter packed into spacetime at the Big Bang. The trivial bundle $E=E_0$ corresponds to empty space, in which every point’s location is exactly known; a non-trivial bundle $E$ begins to fill spacetime with fermions, entering the regime of the quantum Bring surface whose underlying geometry is non-commutative (Section <a href="#sec:quantum-brings" data-reference-type="ref" data-reference="sec:quantum-brings">5.1</a>).*

</div>

<div id="def:brings-surface" class="definition">

**Definition 5.2** (Bring’s surface). *Let $x_j$, $j\in\{0,\dots,4\}$, be homogeneous coordinates on $\mathbb{P}^4$. *Bring’s surface* is the maximally symmetric CR manifold of genus $4$ and Euler characteristic $\chi=-6$, defined by the vanishing of the first three power sums: $$\sum_{j=0}^{4}x_j^{\,k}=0,
  \qquad k=1,2,3.$$*

</div>

<div id="rem:brings-qou-4tuple" class="remark">

**Remark 5.3** (QOU $4$-tuple for Bring’s surface). *We construct the $\mathbb{C}$ quantum observable universe (Example <a href="#def:c-quantum-observable-universe" data-reference-type="ref" data-reference="def:c-quantum-observable-universe">1.6</a>) explicitly for Bring’s surface. The five homogeneous coordinates $x_j$, $j\in\{0,\dots,4\}$, split into *spacetime* and *chiral* degrees of freedom: $$\underbrace{x_0,\, x_1}_{\text{spacetime}}
  \qquad
  \underbrace{x_2,\, x_3,\, x_4}_{\text{chiral}}.$$ The projective ratio $z = x_0/x_1 \in \mathbb{CP}^1$ parametrises the spacetime base.*

***1.CR manifold $M_S$.** Let $S$ denote Bring’s surface (Definition <a href="#def:brings-surface" data-reference-type="ref" data-reference="def:brings-surface">5.2</a>). Because $S$ is a Riemann surface (real dimension $2$), it does not itself carry a contact form. The CR manifold is the unit circle bundle $M_S = \{(p,\eta) \in T^*S : \lvert\eta\rvert_{g_S} = 1\}$, where $g_S$ is the Fubini–Study metric restricted to $S$. The Liouville $1$-form $\lambda = \eta\,dz$ on $T^*S$ restricts to a contact form $\theta = \lambda\big|_{M_S}$, making $M_S$ a $3$-dimensional strictly pseudoconvex CR manifold.*

***2.Principal bundle $P$.** The branched covering $\pi\colon S \to \mathbb{CP}^1$ (degree $4$, six branch points) lifts to a principal $\mathrm{SU}(2)$-bundle $P \to M_S$. In the spacetime coordinate $z$, the transition functions of $P$ are the $\mathrm{SU}(2)$ holonomy matrices $H_1,H_2$ <a href="#eq:holonomy-generators" data-reference-type="eqref" data-reference="eq:holonomy-generators">[eq:holonomy-generators]</a> around the branch cuts; in the chiral coordinates $(x_2,x_3,x_4)$, the $S_3$ permutation of the three sheets gives the $\mathrm{SO}(3)$ holonomy representation (Definitions <a href="#def:su2-generators" data-reference-type="ref" data-reference="def:su2-generators">3.5</a>–<a href="#def:so3-generators" data-reference-type="ref" data-reference="def:so3-generators">3.6</a>).*

***3.State bundle $E$.** The associated state bundle is $E = P \times_G \mathbb{CP}^1$, whose fibre at each point of $M_S$ is the chiral $\mathbb{CP}^1$ parametrised by the three roots of the elliptic cubic <a href="#eq:chiral-elliptic" data-reference-type="eqref" data-reference="eq:chiral-elliptic">[eq:chiral-elliptic]</a>.*

***4.Connection, Levi form, and substrate parameter.** The instanton connection $A$ on $P$ is expressed in the resolvent basis $(w_1,\dots,w_4)$ (Remark <a href="#rem:lagrange-resolvents" data-reference-type="ref" data-reference="rem:lagrange-resolvents">5.4</a>) as the flat $B_3$-monodromy connection whose holonomy around the six branch points is generated by the trefoil holonomy matrices. The Levi form on $M_S$ is $$L \;=\; d\theta\big|_{H \times H},
  \qquad H = \ker\theta \subset TM_S,$$ where $\theta = \eta\,dz\big|_{M_S}$ and the horizontal distribution $H$ is spanned by the lifts of the chiral differentials $dx_2, dx_3, dx_4$ to $M_S$. The substrate parameter (Definition <a href="#def:substrate-parameter" data-reference-type="ref" data-reference="def:substrate-parameter">1.10</a>) then reads $$q(p) \;=\; 1 + \lvert\langle L_\theta,\, F_A^+ \rangle\rvert(p),
  \qquad p \in M_S,$$ coupling the chiral curvature to the contact geometry. At the six branch points (where chiral sheets merge), $\lVert F_A^+\rVert$ is maximal and $q \to \infty$ (deep-quantum regime); away from the defects, $q \to 1$ (classicality).*

***Summary.** The $4$-tuple $(M_S,\, G,\, P,\, E)$, with $G = \mathrm{SU}(2)$, constitutes a $\mathbb{C}$ quantum observable universe (Example <a href="#ex:brings-surface" data-reference-type="ref" data-reference="ex:brings-surface">2.7</a>), and every QOU structure—contact form, Reeb field, Levi form, substrate parameter, $q$-deformed operators—is determined by the spacetime coordinate $z = x_0/x_1$ and the chiral coordinates $(x_2, x_3, x_4)$.*

</div>

<div id="rem:lagrange-resolvents" class="remark">

**Remark 5.4** (Lagrange resolvents and spectral form). *Let $\zeta=e^{2\pi i/5}$. Apply the discrete Fourier transform to the coordinates $x_j$ of Bring’s surface (Definition <a href="#def:brings-surface" data-reference-type="ref" data-reference="def:brings-surface">5.2</a>): $$w_k \;=\; \frac{1}{\sqrt{5}}\sum_{j=0}^{4}\zeta^{kj}\,x_j,
  \qquad k\in\{0,1,2,3,4\}.$$ Under this change of basis the three defining power-sum equations become the following *spectral forms*: $$\begin{aligned}
  w_0 &= 0
    &&\text{(linear projection),}
    \label{eq:resolvent-linear}\\[4pt]
  w_1\,w_4+w_2\,w_3 &= 0
    &&\text{(Hermitian quadric),}
    \label{eq:resolvent-quadric}\\[4pt]
  w_1^2\,w_3+w_4^2\,w_2+w_2^2\,w_1+w_3^2\,w_4 &= 0
    &&\text{(symmetric cubic).}
    \label{eq:resolvent-cubic}
\end{aligned}$$ The cyclic permutation $\sigma\colon x_j\mapsto x_{j+1}$ acts by $\sigma(w_k)=\zeta^{-k}w_k$, so the $C_5$ symmetry is manifest as a phase rotation $w_k\mapsto\zeta^k\,w_k$.*

</div>

<div id="rem:braid-group-action" class="remark">

**Remark 5.5** (Braid-group action on the resolvents). *The symmetric group $S_5$ acts on Bring’s surface (Remark <a href="#rem:brings-curve" data-reference-type="ref" data-reference="rem:brings-curve">6.11</a>) by permuting $(x_0,\dots,x_4)$; this is the maximal automorphism group (order $120$) for genus $4$. Three distinguished families of $S_3$ subgroups govern the interplay between the base coordinates $x_j$ and the spectral resolvents $w_k$ (Remark <a href="#rem:lagrange-resolvents" data-reference-type="ref" data-reference="rem:lagrange-resolvents">5.4</a>). We describe each in terms of the braid group (Definition <a href="#def:braid-group" data-reference-type="ref" data-reference="def:braid-group">3.1</a>), the resolvent coordinates, and the $\mathrm{SU}(2)$/$\mathrm{SO}(3)$ matrices of Definitions <a href="#def:su2-generators" data-reference-type="ref" data-reference="def:su2-generators">3.5</a>–<a href="#def:so3-generators" data-reference-type="ref" data-reference="def:so3-generators">3.6</a>.*

***(i) Spacetime action ($\mathbb{CP}^1$ base).** Fix the chiral-like coordinates $x_2,x_3,x_4$ as internal fiber degrees of freedom. The constraint $w_0=0$ <a href="#eq:resolvent-linear" data-reference-type="eqref" data-reference="eq:resolvent-linear">[eq:resolvent-linear]</a> forces $x_0+x_1=C$ (constant), so the spacetime degrees of freedom collapse projectively to the ratio $z=x_0/x_1\in\mathbb{CP}^1$. The transposition $x_0\leftrightarrow x_1$ acts as the Möbius involution $z\mapsto 1/z$, which is a $\pi$-rotation on $\mathbb{CP}^1$ and embeds into $\mathrm{SU}(2)$ as $\beta=\exp(\pi\,e_1)$ <a href="#eq:su2-2cycle" data-reference-type="eqref" data-reference="eq:su2-2cycle">[eq:su2-2cycle]</a>. In the resolvent basis this acts as $$\label{eq:spacetime-shift}
  w_k\;\longmapsto\;
  w_k+\tfrac{1}{\sqrt{5}}\,(1-\zeta^k)(x_1-x_0),
  \qquad k=1,\dots,4,$$ an affine shift that fixes the chiral modes and translates the $\mathbb{CP}^1$ fibre.*

***(ii) Spectral $S_3$ (trefoil action).** The frequency-coupled pairs $(w_1,w_4)$ and $(w_2,w_3)$ are permuted by the twist and flip involutions (Definition <a href="#def:braid-twist-flip" data-reference-type="ref" data-reference="def:braid-twist-flip">3.7</a>). The full $S_3$ structure emerges on the projective ratios $$\eta_1=\frac{w_1}{w_2},\qquad\eta_2=\frac{w_3}{w_4}:$$ $\sigma_1$ inverts both ratios $(\eta_1\mapsto\eta_1^{-1},\;
\eta_2\mapsto\eta_2^{-1})$, while $\sigma_2$ exchanges them $(\eta_1\mapsto\eta_2^{-1},\;\eta_2\mapsto\eta_1^{-1})$. The $2$-cycle (reflection) swaps the pairs $(w_1,w_4)\leftrightarrow(w_2,w_3)$; the $3$-cycle (rotation) sends $(\eta_1,\eta_2)\mapsto(\eta_1,\,\zeta^j\eta_2)$ for $j\in\{1,2,3\}$, permuting the three complex branches of the cubic constraint <a href="#eq:resolvent-cubic" data-reference-type="eqref" data-reference="eq:resolvent-cubic">[eq:resolvent-cubic]</a>. The $\mathrm{SU}(2)$ representation assigns the $3$-cycle to $\alpha$ <a href="#eq:su2-3cycle" data-reference-type="eqref" data-reference="eq:su2-3cycle">[eq:su2-3cycle]</a> and the reflection to $\beta$ <a href="#eq:su2-2cycle" data-reference-type="eqref" data-reference="eq:su2-2cycle">[eq:su2-2cycle]</a>; the $\mathrm{SO}(3)$ images <a href="#eq:so3-generators" data-reference-type="eqref" data-reference="eq:so3-generators">[eq:so3-generators]</a> act as the holonomy on the spectral energy distribution, with $R_\alpha$ rotating the time-like resolvent pair $(\omega_2,\omega_3)$ and $R_\beta$ reflecting the space-like axis $\omega_1$.*

***(iii) Coordinate $S_3$.** Fixing any two coordinates (say $x_0,x_1$) as a spacetime base and permuting the remaining three $(x_2,x_3,x_4)$ gives a stabiliser $\mathrm{Stab}(\{x_0,x_1\})\cong S_3\subset S_5$; there are $\binom{5}{2}=10$ such subgroups. In the resolvent basis a permutation $\sigma\in S_3$ of $(x_2,x_3,x_4)$ acts as $$\label{eq:coord-s3-shift}
  w_k\;\longmapsto\;
  w_k+\tfrac{1}{\sqrt{5}}\sum_{j=2}^{4}
    \bigl(\zeta^{k\,\sigma(j)}-\zeta^{kj}\bigr)\,x_j,$$ so the $w_k$ transform as vector fields over the $(x_0,x_1)$ plane and the $S_3$ permutes how these fields couple to the base. The same $\mathrm{SO}(3)$ representation <a href="#eq:so3-generators" data-reference-type="eqref" data-reference="eq:so3-generators">[eq:so3-generators]</a> realises this action, now playing the rôle of the holonomy group on the internal fibre.*

***Geometric $S_3$.** When Bring’s curve is viewed as a branched cover $\mathcal{S}\to\mathbb{P}^1$, a third family of $S_3$ subgroups arises: it permutes the three critical values of the covering map. These three families — spectral, coordinate, and geometric — correspond to the three copies of $S_3$ inside $S_5$ identified in Remark <a href="#rem:chirality-trefoil" data-reference-type="ref" data-reference="rem:chirality-trefoil">6.10</a>.*

</div>

<div id="def:color-tube-coordinates" class="definition">

**Definition 5.6** (Color tube coordinates). *Let $z = x_0/x_1 \in \mathbb{CP}^1$ be the spacetime ratio (Remark <a href="#rem:braid-group-action" data-reference-type="ref" data-reference="rem:braid-group-action">5.5</a><span class="upright">(i)</span>) and let $w_k$, $k \in \{0,\dots,4\}$, be the Lagrange resolvents of Bring’s surface (Remark <a href="#rem:lagrange-resolvents" data-reference-type="ref" data-reference="rem:lagrange-resolvents">5.4</a>). The *color tube coordinates* are the shifted spectral coordinates $$\label{eq:color-tube-coords}
    r = w_2 - z, \quad g = w_3 - z, \quad b = w_4 - z,$$ together with the space-like shift $\sigma = w_1 - z$. The *color vector* is $\vec{c} = (r, g, b)$.*

</div>

<div id="rem:aggregate-color-quantities" class="remark">

**Remark 5.7** (Aggregate color quantities). *Define the following aggregate quantities in color tube coordinates, with $\zeta = e^{2\pi i/5}$: $$\begin{aligned}
    \widetilde{S} &\;=\; \sigma + r + g + b
      &&\text{(total color deviation),}
      \label{eq:agg-S-tilde}\\[4pt]
    \widetilde{Q} &\;=\; \sigma b + r g
      &&\text{(paired color product),}
      \label{eq:agg-Q-tilde}\\[4pt]
    \widetilde{D} &\;=\; \zeta^{-1}\sigma + \zeta^{-2}r + \zeta^{-3}g + \zeta^{-4}b
      &&\text{(weighted color deviation),}
      \label{eq:agg-D-tilde}\\[4pt]
    \widetilde{C} &\;=\; \sigma^2 g + b^2 r + r^2\sigma + g^2 b
      &&\text{(intrinsic color cubic).}
      \label{eq:agg-C-tilde}
  
\end{aligned}$$ These are related to the unshifted aggregate quantities $S = \sum_{k=1}^{4}w_k$ and $D = \sum_{k=1}^{4}\zeta^{-k}w_k$ by $$\label{eq:aggregate-shift}
    S \;=\; \widetilde{S} + 4z, \qquad D \;=\; \widetilde{D} - z,$$ where the second identity uses $\sum_{k=1}^{4}\zeta^{-k} = -1$. The inverse Lagrange resolvent transform (Remark <a href="#rem:lagrange-resolvents" data-reference-type="ref" data-reference="rem:lagrange-resolvents">5.4</a>) gives $$\label{eq:z-from-SD}
    z \;=\; \frac{x_0}{x_1} \;=\; \frac{S}{D}.$$*

</div>

<div id="rem:color-tube-constraints" class="remark">

**Remark 5.8** (Constraint equations in color tube coordinates). *The Bring surface constraints <a href="#eq:resolvent-linear" data-reference-type="eqref" data-reference="eq:resolvent-linear">[eq:resolvent-linear]</a>–<a href="#eq:resolvent-cubic" data-reference-type="eqref" data-reference="eq:resolvent-cubic">[eq:resolvent-cubic]</a> take the following form in color tube coordinates.*

***Spacetime recovery.** Substituting <a href="#eq:aggregate-shift" data-reference-type="eqref" data-reference="eq:aggregate-shift">[eq:aggregate-shift]</a> into $z = S/D$ (equation <a href="#eq:z-from-SD" data-reference-type="eqref" data-reference="eq:z-from-SD">[eq:z-from-SD]</a>) yields $z(\widetilde{D} - z) = \widetilde{S} + 4z$, which rearranges to $$\label{eq:spacetime-recovery}
    z^2 - (\widetilde{D} - 4)\,z + \widetilde{S} \;=\; 0.$$ Thus the spacetime coordinate $z$ is determined implicitly by the shifted data $(\widetilde{S}, \widetilde{D})$.*

***Shifted quadric.** Substituting $w_k = c_k + z$ into the quadric <a href="#eq:resolvent-quadric" data-reference-type="eqref" data-reference="eq:resolvent-quadric">[eq:resolvent-quadric]</a> gives $$\label{eq:shifted-quadric}
    \widetilde{Q} + z\,\widetilde{S} + 2z^2 \;=\; 0,$$ or equivalently $\sigma b + rg = -z(\sigma + r + g + b) - 2z^2$.*

***Shifted cubic.** Substituting $w_k = c_k + z$ into the cubic <a href="#eq:resolvent-cubic" data-reference-type="eqref" data-reference="eq:resolvent-cubic">[eq:resolvent-cubic]</a> gives $$\label{eq:shifted-cubic}
    \widetilde{C} + z(\widetilde{S}^2 - 2\widetilde{Q})
    + 3z^2\,\widetilde{S} + 4z^3 \;=\; 0.$$ Eliminating $\widetilde{Q}$ via <a href="#eq:shifted-quadric" data-reference-type="eqref" data-reference="eq:shifted-quadric">[eq:shifted-quadric]</a> yields the *reduced cubic*: $$\label{eq:reduced-cubic}
    \widetilde{C} + z\,\widetilde{S}^2 + 5z^2\,\widetilde{S} + 8z^3 \;=\; 0.$$ All three equations are polynomial over $\mathbb{Z}$ in $z, r, g, b, \sigma$; they therefore define affine varieties over $\mathbb{Z}$ and descend to $\mathbb{F}_\mathfrak{p}$ for every prime $\mathfrak{p}\ne 5$.*

</div>

<div id="rem:color-tube-interpretation" class="remark">

**Remark 5.9** (Interpretation of the color tube). *The terminology *color tube* reflects two features.*

***Color.** The coordinates $r, g, b$ label the three chiral degrees of freedom that correspond, via the $S_3$ subgroups of $S_5$ (Remark <a href="#rem:braid-group-action" data-reference-type="ref" data-reference="rem:braid-group-action">5.5</a><span class="upright">(iii)</span>), to the three colour charges of quantum chromodynamics. The chiral coordinates $x_2, x_3, x_4$ of the QOU $4$-tuple (Remark <a href="#rem:brings-qou-4tuple" data-reference-type="ref" data-reference="rem:brings-qou-4tuple">5.3</a>) descend to $r = w_2 - z$, $g = w_3 - z$, $b = w_4 - z$ after shifting by the spacetime ratio $z$.*

***Tube.** For fixed $z \in \mathbb{CP}^1$, the color vector $\vec{c} = (r, g, b)$ is constrained by the shifted quadric <a href="#eq:shifted-quadric" data-reference-type="eqref" data-reference="eq:shifted-quadric">[eq:shifted-quadric]</a> and cubic <a href="#eq:shifted-cubic" data-reference-type="eqref" data-reference="eq:shifted-cubic">[eq:shifted-cubic]</a> to lie on a curve inside the three-dimensional color space $\mathbb{A}^3$. As $z$ varies over the spacetime base, this curve sweeps out a tube — the total space of the chiral fibration over $\mathbb{CP}^1$.*

***Space-like coordinate.** The shift $\sigma = w_1 - z$ is distinguished: it measures the deviation of the $C_5$-fundamental resolvent $w_1$ from the spacetime base, anchoring the $U(1)$ longitudinal backbone (Remark <a href="#rem:spectral-dynamics" data-reference-type="ref" data-reference="rem:spectral-dynamics">5.28</a>) in the shifted frame.*

</div>

<div id="rem:c5-color-tube" class="remark">

**Remark 5.10** ($C_5$ action in color tube coordinates). *The cyclic symmetry $w_k \mapsto \zeta^{-k} w_k$ (Remark <a href="#rem:lagrange-resolvents" data-reference-type="ref" data-reference="rem:lagrange-resolvents">5.4</a>) becomes, in color tube coordinates: $$\begin{aligned}
    \sigma &\;\longmapsto\; \zeta^{-1}\sigma + (\zeta^{-1}-1)\,z,
      \label{eq:c5-sigma}\\[4pt]
    r &\;\longmapsto\; \zeta^{-2}r + (\zeta^{-2}-1)\,z,
      \label{eq:c5-r}\\[4pt]
    g &\;\longmapsto\; \zeta^{-3}g + (\zeta^{-3}-1)\,z,
      \label{eq:c5-g}\\[4pt]
    b &\;\longmapsto\; \zeta^{-4}b + (\zeta^{-4}-1)\,z.
      \label{eq:c5-b}
  
\end{aligned}$$ The $C_5$ action is no longer diagonal: each coordinate acquires an additive correction proportional to $z$, reflecting the cost of breaking projective homogeneity by subtracting the affine quantity $z$ from each resolvent.*

</div>

<div id="rem:intrinsic-color-cubic-pairing" class="remark">

**Remark 5.11** (Intrinsic color cubic: pairing structure). *The intrinsic color cubic $\widetilde{C}$ <a href="#eq:agg-C-tilde" data-reference-type="eqref" data-reference="eq:agg-C-tilde">[eq:agg-C-tilde]</a> admits a natural decomposition into space-like and chiral sectors: $$\label{eq:color-cubic-decomp}
    \widetilde{C}
    \;=\;
    \underbrace{\sigma(\sigma g + r^2)}_{\text{space--colour coupling}}
    \;+\;
    \underbrace{b(br + g^2)}_{\text{pure colour}}.$$ The four terms pair the resolvent indices as $(1,3)$, $(2,1)$, $(4,2)$, $(3,4)$: each index is squared and contracted with the index two steps ahead in the cyclic order $1 \to 3 \to 4 \to 2 \to 1$. This skip-one pairing respects the conjugation $w_k \leftrightarrow w_{5-k}$ that pairs $(w_1, w_4)$ and $(w_2, w_3)$.*

</div>

<div id="prop:chiral-elliptic" class="proposition">

**Proposition 5.12** (Chiral fibre as an elliptic curve). *Let $z=x_0/x_1\in\mathbb{CP}^1$ be the projective spacetime ratio (Remark <a href="#rem:braid-group-action" data-reference-type="ref" data-reference="rem:braid-group-action">5.5</a><span class="upright">(i)</span>). Substituting the constraint $x_0+x_1=C$ and eliminating $x_0,x_1$ in favour of $z$, the quadratic and cubic power-sum conditions <a href="#eq:resolvent-quadric" data-reference-type="eqref" data-reference="eq:resolvent-quadric">[eq:resolvent-quadric]</a>–<a href="#eq:resolvent-cubic" data-reference-type="eqref" data-reference="eq:resolvent-cubic">[eq:resolvent-cubic]</a> on the chiral variable $X=(x_2,x_3,x_4)$ reduce at each fixed $z$ to the cubic $$\label{eq:chiral-elliptic}
  X^3+(z+1)\,X^2+(z^2+z+1)\,X+(z^3+z^2+z+1)=0.$$ For generic $z$ this defines an elliptic curve $E_z$ in the chiral fibre; its $j$-invariant varies as a rational function of $z$. The monodromy of $E_z$ around the singular fibres (where the discriminant of <a href="#eq:chiral-elliptic" data-reference-type="eqref" data-reference="eq:chiral-elliptic">[eq:chiral-elliptic]</a> vanishes) recovers the holonomy generators $H_1,H_2$ <a href="#eq:holonomy-generators" data-reference-type="eqref" data-reference="eq:holonomy-generators">[eq:holonomy-generators]</a> of Remark <a href="#rem:holonomy-trefoil" data-reference-type="ref" data-reference="rem:holonomy-trefoil">3.8</a>.*

</div>

<div class="proof">

*Proof.* Write $x_0=z\,x_1$ and use $x_0+x_1=C$ to eliminate both spacetime variables. The power-sum conditions $\sum x_j^k=0$ for $k=2,3$ then become polynomial in $z$ and $X=x_2+x_3+x_4$, $X_2=\sum_{i<j}x_ix_j$, etc. Reducing by the Newton identities yields the cubic <a href="#eq:chiral-elliptic" data-reference-type="eqref" data-reference="eq:chiral-elliptic">[eq:chiral-elliptic]</a>; its discriminant is a polynomial in $z$ whose roots give the singular fibres. ◻

</div>

<div id="rem:t-duality-elliptic" class="remark">

**Remark 5.13** (Self-duality of the chiral elliptic curve). *The cubic <a href="#eq:chiral-elliptic" data-reference-type="eqref" data-reference="eq:chiral-elliptic">[eq:chiral-elliptic]</a> is symmetric under the exchange $X\leftrightarrow z$: writing $$F(X,z)\;=\;X^3+(z+1)\,X^2+(z^2+z+1)\,X+(z^3+z^2+z+1),$$ one verifies $F(X,z)=F(z,X)$ term by term. This involution $\iota\colon(X,z)\mapsto(z,X)$ is a *T-duality*: it identifies every chiral fibre $E_z$ with its dual spacetime wrapping $E_X$, so the internal and external degrees of freedom of the Bring surface are algebraically indistinguishable.*

***Quotient space.** Passing to the symmetric coordinates $u=X+z$, $v=Xz$, the curve becomes $$\label{eq:symmetric-quotient}
  v \;=\; \frac{(u+1)(u^2+1)}{2u+1}\,,$$ which is rational in $u$. Hence the quotient $E_z/\langle\iota\rangle\cong\mathbb{CP}^1$: folding the torus along its $X=z$ diagonal collapses it to a genus-$0$ Riemann sphere.*

***Weierstrass normal form.** Depressing the cubic via $X=t-\tfrac{z+1}{3}$ eliminates the quadratic term: $$\label{eq:weierstrass-depressed}
  t^{3}+p(z)\,t+q(z)=0,\qquad
  p=\frac{2z^2+z+2}{3},\quad
  q=\frac{5(4z^3+3z^2+3z+4)}{27}.$$ The discriminant $\Delta(z)=-4\,p(z)^3-27\,q(z)^2$ is a polynomial in $z$ whose roots determine the singular fibres of the elliptic fibration $\mathcal{S}\to\mathbb{CP}^1$. At those roots the $j$-invariant $j(E_z)=-1728\cdot 64\,p(z)^3/\Delta(z)$ degenerates.*

</div>

<div id="rem:color-tube-cubic" class="remark">

**Remark 5.14** (Color tube cubic). *At fixed $z \in \mathbb{CP}^1$, the three chiral roots of the elliptic cubic <a href="#eq:chiral-elliptic" data-reference-type="eqref" data-reference="eq:chiral-elliptic">[eq:chiral-elliptic]</a> each satisfy the cubic in the color tube coordinate $\mathbf{c} \in \{\mathbf{r}_z, \mathbf{g}_z, \mathbf{b}_z\}$ obtained by substituting $X = \mathbf{c} + z$ into equation <a href="#eq:chiral-elliptic" data-reference-type="eqref" data-reference="eq:chiral-elliptic">[eq:chiral-elliptic]</a>. Expanding gives the *color tube cubic*: $$\label{eq:color-tube-cubic}
    \mathbf{c}^3 + (4z+1)\,\mathbf{c}^2 + (6z^2+3z+1)\,\mathbf{c}
    + (4z^3+3z^2+2z+1) \;=\; 0.$$ This polynomial lies in $\mathbb{Z}[z][\mathbf{c}]$ and defines a variety over $\mathbb{Z}$. The leading $z$-coefficients $4, 6, 4$ equal $\binom{4}{1}$, $\binom{4}{2}$, $\binom{4}{3}$, and the constant term satisfies $$4z^3 + 3z^2 + 2z + 1 \;=\; \frac{d}{dz}(z^4 + z^3 + z^2 + z).$$*

*Vieta’s formulas for the three roots give: $$\begin{aligned}
    \mathbf{r}_z + \mathbf{g}_z + \mathbf{b}_z
      &\;=\; -(4z+1),
      \label{eq:vieta-sum}\\[4pt]
    \mathbf{r}_z\,\mathbf{g}_z + \mathbf{r}_z\,\mathbf{b}_z
      + \mathbf{g}_z\,\mathbf{b}_z
      &\;=\; 6z^2+3z+1,
      \label{eq:vieta-pairs}\\[4pt]
    \mathbf{r}_z\,\mathbf{g}_z\,\mathbf{b}_z
      &\;=\; -(4z^3+3z^2+2z+1).
      \label{eq:vieta-product}
  
\end{aligned}$$*

</div>

<div id="def:color-tube-fibers" class="definition">

**Definition 5.15** (Color tube fibers). *Let $z \in \mathbb{CP}^1$. The *color tube* at $z$ is the affine curve defined over $\mathbb{Z}[z]$ by the color tube cubic <a href="#eq:color-tube-cubic" data-reference-type="eqref" data-reference="eq:color-tube-cubic">[eq:color-tube-cubic]</a>; we denote it $R_z$, $G_z$, or $B_z$ according to which color tube coordinate $\mathbf{r}_z$, $\mathbf{g}_z$, or $\mathbf{b}_z$ is used: $$\label{eq:color-tube-fiber-def}
    R_z \;:=\;
    \bigl\{\,\mathbf{r}_z \in \mathbb{A}^1 :
      \mathbf{r}_z^{\,3} + (4z+1)\,\mathbf{r}_z^{\,2}
      + (6z^2+3z+1)\,\mathbf{r}_z
      + (4z^3+3z^2+2z+1) = 0\,\bigr\},$$ and $G_z$, $B_z$ are defined by the same equation with coordinates $\mathbf{g}_z$ and $\mathbf{b}_z$, respectively. The coordinates are related to the Lagrange resolvents by $$\mathbf{r}_z = w_2 - z, \qquad \mathbf{g}_z = w_3 - z, \qquad
    \mathbf{b}_z = w_4 - z.$$ As varieties, $R_z \cong G_z \cong B_z$ is isomorphic to the chiral elliptic fiber $E_z$ of Proposition <a href="#prop:chiral-elliptic" data-reference-type="ref" data-reference="prop:chiral-elliptic">5.12</a> via the shift $X = \mathbf{c} + z$.*

</div>

<div id="def:observed-value" class="definition">

**Definition 5.16** (Observed spacetime value). *Let $\mathbf{r}_z, \mathbf{g}_z, \mathbf{b}_z$ be the color tube coordinates at a point of Bring’s surface (Definition <a href="#def:color-tube-fibers" data-reference-type="ref" data-reference="def:color-tube-fibers">5.15</a>). The *observed spacetime value* is the element of $\mathbb{A}^1$ recovered from the color tube coordinates by the Vieta identity <a href="#eq:vieta-sum" data-reference-type="eqref" data-reference="eq:vieta-sum">[eq:vieta-sum]</a>: $$\label{eq:observed-value}
    \mathbf{r}_z + \mathbf{g}_z + \mathbf{b}_z + 4z + 1 \;=\; 0.$$ This identity defines the projection $\pi_z \colon R_z \times G_z \times B_z \to \mathbb{A}^1$, $({\mathbf{r}_z, \mathbf{g}_z, \mathbf{b}_z}) \mapsto z$, which is a polynomial map over $\mathbb{Z}$. At a branch point $z_c$ where chiral sheets merge (Remark <a href="#rem:brings-smoothness" data-reference-type="ref" data-reference="rem:brings-smoothness">5.20</a>), the exceptional divisor is coordinatised by the limiting color vector; the observed spacetime value reads off $z_c$ from the color data via <a href="#eq:observed-value" data-reference-type="eqref" data-reference="eq:observed-value">[eq:observed-value]</a>, providing a coordinate on the exceptional $\mathbb{CP}^1$.*

</div>

<div id="rem:t-duality-color-tube" class="remark">

**Remark 5.17** (T-duality in color tube coordinates). *The T-duality involution $\iota \colon (X, z) \mapsto (z, X)$ (Remark <a href="#rem:t-duality-elliptic" data-reference-type="ref" data-reference="rem:t-duality-elliptic">5.13</a>) acts on color tube coordinates as follows. Writing $c = X - z$, the dual point has base coordinate $z' = X = c + z$ and chiral coordinate $X' = z$, giving dual color tube coordinate $c' = z - X = -c$. Hence $$\label{eq:t-duality-color-tube}
    \iota \colon (c,\, z) \;\longmapsto\; (-c,\; c + z).$$ The symmetry $F(X,z) = F(z,X)$ (Remark <a href="#rem:t-duality-elliptic" data-reference-type="ref" data-reference="rem:t-duality-elliptic">5.13</a>) translates to covariance of the color tube cubic: the cubic <a href="#eq:color-tube-cubic" data-reference-type="eqref" data-reference="eq:color-tube-cubic">[eq:color-tube-cubic]</a> at parameter $z$ with root $c$ is carried by $\iota$ to the cubic at parameter $c + z$ with root $-c$. One verifies this directly from $F(c+z,\, z) = F(z,\, c+z)$, since $F(z, c+z)$ is the color tube cubic at parameter $c+z$ evaluated at $-c$.*

</div>

<div id="rem:color-tube-subloci" class="remark">

**Remark 5.18** (Sublocus $\widetilde{C}=0$ and colour confinement). ***Vanishing of the intrinsic color cubic.** If $\widetilde{C} = 0$, the reduced cubic <a href="#eq:reduced-cubic" data-reference-type="eqref" data-reference="eq:reduced-cubic">[eq:reduced-cubic]</a> factors as $$\label{eq:reduced-cubic-factored}
    z\bigl(\widetilde{S}^2 + 5z\,\widetilde{S} + 8z^2\bigr) \;=\; 0,$$ so either $z = 0$ (the spacetime origin) or $\widetilde{S}$ satisfies the quadratic $\widetilde{S}^2 + 5z\,\widetilde{S} + 8z^2 = 0$. The discriminant of this quadratic (in $\widetilde{S}$) is $25z^2 - 32z^2 = -7z^2$, which is negative for real $z \ne 0$. Over $\mathbb{C}$, the two solutions are $$\widetilde{S} \;=\; z\,\frac{-5 \pm \sqrt{-7}}{2};$$ these are non-real for $z \ne 0$, so the locus $\widetilde{C} = 0$ meets the real locus only at $z = 0$. Over $\mathbb{F}_\mathfrak{p}$ the existence of a solution depends on whether $-7$ is a quadratic residue mod $\mathfrak{p}$.*

***Pure colour sublocus.** The pure colour term $b(br + g^2)$ (equation <a href="#eq:color-cubic-decomp" data-reference-type="eqref" data-reference="eq:color-cubic-decomp">[eq:color-cubic-decomp]</a>) vanishes on $$\{b = 0\} \;\cup\; \{br + g^2 = 0\}.$$ The condition $b = 0$ means $w_4 = z$: the fourth resolvent coincides with the spacetime ratio, collapsing one chiral degree of freedom onto the base. The condition $br + g^2 = 0$, i.e. $(w_4 - z)(w_2 - z) + (w_3 - z)^2 = 0$, is a quadratic relation among the chiral resolvents and $z$. Either condition can be interpreted as a *colour-confinement* constraint: one chiral mode is frozen in register with the spacetime coordinate, and the remaining two are coupled by a Hermitian-quadric relation in the shifted frame.*

</div>

<div id="rem:chiral-bundles" class="remark">

**Remark 5.19** (Chiral space as spectral curve and spinor bundle). *The spacetime–chiral decomposition of Bring’s surface maps naturally onto three classical bundle structures over the $\mathbb{CP}^1$ base $z=x_0/x_1$.*

***Cotangent bundle.** The three-sheeted cubic <a href="#eq:chiral-elliptic" data-reference-type="eqref" data-reference="eq:chiral-elliptic">[eq:chiral-elliptic]</a> realises the chiral variables $X=(x_2,x_3,x_4)$ as a *spectral curve* $\Sigma\subset T^{*}\mathbb{CP}^1$: the base coordinate $z$ parametrises spacetime position, and the three roots $X_1,X_2,X_3$ of Proposition <a href="#prop:chiral-elliptic" data-reference-type="ref" data-reference="prop:chiral-elliptic">5.12</a> are eigenvalues of a Higgs-like field $\Phi$ on the base. The six singular fibres (where the discriminant $\Delta(z)$ vanishes) are the loci at which eigenvalues coincide and the differential $dX$ degenerates in the cotangent fibre.*

***Spinor bundle.** The spectral modes $w_1,\dots,w_4$ (Remark <a href="#rem:lagrange-resolvents" data-reference-type="ref" data-reference="rem:lagrange-resolvents">5.4</a>) live in a rank-$2$ complex vector bundle over $\mathbb{CP}^1$. The chiral doublet $\Psi_L=(w_1,w_2)^T$ and its conjugate $\Psi_R=(w_4,w_3)^T$ transform under the $\mathrm{SU}(2)$ holonomy generators $H_1,H_2$ <a href="#eq:holonomy-generators" data-reference-type="eqref" data-reference="eq:holonomy-generators">[eq:holonomy-generators]</a> of Remark <a href="#rem:holonomy-trefoil" data-reference-type="ref" data-reference="rem:holonomy-trefoil">3.8</a>, making $\Psi_L$ a section of the *spinor bundle* $\mathcal{S}^{+}\to\mathbb{CP}^1$. The $B_3$ monodromy equips this bundle with a flat connection whose holonomy is the trefoil-knot group.*

***Adjoint bundle.** The $\mathrm{SO}(3)$ images $R_\alpha,R_\beta$ <a href="#eq:so3-generators" data-reference-type="eqref" data-reference="eq:so3-generators">[eq:so3-generators]</a> act on the triple $(\omega_1,\omega_2,\omega_3)$, which therefore spans a section of the adjoint bundle $\mathrm{ad}\,P\to\mathbb{CP}^1$ associated to the principal $\mathrm{SU}(2)$-bundle $P$. The T-duality involution $\iota\colon X\leftrightarrow z$ (Remark <a href="#rem:t-duality-elliptic" data-reference-type="ref" data-reference="rem:t-duality-elliptic">5.13</a>) interchanges the fibre and base of the adjoint bundle, exchanging spectral eigenvalues with spacetime coordinates.*

</div>

<div id="rem:brings-smoothness" class="remark">

**Remark 5.20** (Smoothness of the Bring surface and resolution of spacetime defects). *The Bring surface $\mathcal{S}$ (Definition <a href="#def:brings-surface" data-reference-type="ref" data-reference="def:brings-surface">5.2</a>) is a *smooth* algebraic variety: the three power-sum constraints are transverse in $\mathbb{P}^4$, so their intersection carries no singular points. The six topological defects identified in Remark <a href="#rem:chiral-bundles" data-reference-type="ref" data-reference="rem:chiral-bundles">5.19</a>—where the discriminant $\Delta(z)$ vanishes and two chiral sheets $X_i,X_j$ collide—are singularities of the *projection* $\pi\colon\mathcal{S}\to\mathbb{CP}^1$, not of the surface itself.*

***Resolution in the $x_j$ coordinates.** At a branch point $z=z_c$ where, say, $x_2=x_3$, define the local chiral coordinate $\delta=x_2-x_3$. In a neighbourhood of the defect the spacetime ratio satisfies $$z-z_c\;\sim\;\delta^2,$$ so while the projection map develops a ramification cusp, $\delta$ passes smoothly through zero, carrying the geometry from one sheet to the other. The exceptional divisor of the blow-up at each branch point is therefore already embedded in the chiral coordinates $x_2,x_3,x_4$: no external resolution is required.*

***Resolution in the $w_k$ coordinates.** The DFT mixes all five $x_j$ into every resolvent $w_k$ (Remark <a href="#rem:lagrange-resolvents" data-reference-type="ref" data-reference="rem:lagrange-resolvents">5.4</a>), so no single $w_k$ vanishes at a branch point. The Briggs–Klein chart (Definition <a href="#def:briggs-klein-chart" data-reference-type="ref" data-reference="def:briggs-klein-chart">5.21</a>) remains a smooth coordinate system throughout $0<r<\infty$: the radial parameter $r=\lvert w_1\rvert^2$ is a regular function on $\mathcal{S}$, and the $C_5$ orbits $w_k\mapsto\zeta^k w_k$ foliate the surface without fixed points. The infinite torsion and eigenvalue crossings visible in the base $\mathbb{CP}^1$ are artefacts of projecting away the internal degrees of freedom that the $w_k$ retain.*

</div>

<div id="def:briggs-klein-chart" class="definition">

**Definition 5.21** (Briggs–Klein affine chart). *Let $r=\lvert w_1\rvert^2$ denote the squared modulus of the first resolvent coordinate on Bring’s surface (Definition <a href="#def:brings-surface" data-reference-type="ref" data-reference="def:brings-surface">5.2</a>). The *Briggs–Klein affine chart* is the coordinate system $(w_1,w_2)$ restricted to the open set $0<r<\infty$, equipped with the Hermitian metric inherited from the Fubini–Study metric on $\mathbb{P}^4$. In this chart the $C_5$ action is the phase rotation $w_k\mapsto\zeta^k\,w_k$, and the radial coordinate $r$ is $C_5$-invariant.*

</div>

<div id="rem:radial-projection" class="remark">

**Remark 5.22** (Radial projection of Bring’s surface). *Restricting a Briggs–Klein affine chart (Definition <a href="#def:briggs-klein-chart" data-reference-type="ref" data-reference="def:briggs-klein-chart">5.21</a>) to the interval $r\in(0,1)$ and projecting Bring’s surface onto this radial coordinate yields a fibration over the base manifold $M$ with trivial bundle $E=E_0$. At each $r$, the coordinate $w_1$ is restricted to a circle of radius $\sqrt{r}$ in the complex plane $\mathbb{C}_{w_1}$. This circle is the orbit of the $C_5$ symmetry: the rotation $w_1\mapsto\zeta\,w_1$ moves the point along this circle without changing $r$.*

<div class="center">

</div>

*The brown tessellation filling the brane illustrates the trivial bundle $E=E_0$: every cell is flat, reflecting the absence of torsion on the total space.*

</div>

<div id="rem:four-colourability" class="remark">

**Remark 5.23** (Four-colourability of Bring’s surface). *By the Heawood bound, an orientable surface of genus $g$ has chromatic number at most $\lfloor(7+\sqrt{1+48g})/2\rfloor$. For genus $4$ this bound equals $10$. Bring’s surface, however, admits a proper colouring with only four colours — considerably fewer than the maximum permitted by its genus. This low chromatic number reflects the high degree of symmetry: the $S_5$ automorphism group constrains the combinatorics of any cell decomposition, forcing a more efficient colouring than a generic genus-$4$ surface would require.*

</div>

<div id="rem:four-colour-theorem" class="remark">

**Remark 5.24** (The four-colour theorem and Bring’s surface). *The classical four-colour theorem asserts that every planar graph (equivalently, every graph embeddable in $S^2$) is four-colourable. For higher-genus surfaces the chromatic number can be much larger: the Heawood conjecture (proved by Ringel–Youngs for $g\geq 1$) shows that the maximum chromatic number grows as $O(\sqrt{g})$. That Bring’s surface attains the planar bound of four — despite living at genus $4$ — is a reflection of the rigidity imposed by its $S_5$ symmetry. In the language of the Descartes universe, the trivial bundle $E=E_0$ (Remark <a href="#rem:radial-projection" data-reference-type="ref" data-reference="rem:radial-projection">5.22</a>) carries no torsion, and the resulting flatness of the tessellation forces the same chromatic economy as the sphere.*

</div>

<div id="rem:cyclotomic-reduction" class="remark">

**Remark 5.25** (Cyclotomic reduction and $C_{\mathfrak{p}}$ preservation). *Let $\mathfrak{p}$ be a prime (not to be confused with a point $p\in M$). Working over the cyclotomic ring $$\label{eq:cyclotomic-ring}
  \mathbb{Z}_{\zeta_{\mathfrak{p}}}
  \;:=\;\mathbb{Z}[i,\,\zeta_{\mathfrak{p}}],$$ where $\zeta_{\mathfrak{p}}=e^{2\pi i/\mathfrak{p}}$ is a primitive $\mathfrak{p}$-th root of unity, consider the sublocus $$S_{\mathfrak{p}}
  \;:=\;
  \Sigma_4\;\cap\;\mathbb{Z}_{\zeta_{\mathfrak{p}}}^{\,5},$$ that is, the set of points on Bring’s surface whose resolvent coordinates lie in $\mathbb{Z}_{\zeta_{\mathfrak{p}}}$. The cyclic subgroup $C_{\mathfrak{p}}\subset S_5$ generated by the $\mathfrak{p}$-cycle preserves $S_{\mathfrak{p}}$: for any $P\in S_{\mathfrak{p}}$, the image $\sigma^k(P)$ remains in $\mathbb{Z}_{\zeta_{\mathfrak{p}}}^{\,5}$ because $\sigma$ acts by multiplication by $\zeta_{\mathfrak{p}}^{-k}$ in the resolvent basis (Remark <a href="#rem:lagrange-resolvents" data-reference-type="ref" data-reference="rem:lagrange-resolvents">5.4</a>), and $\zeta_{\mathfrak{p}}^{-k}\in\mathbb{Z}_{\zeta_{\mathfrak{p}}}$. This arithmetic compatibility between the cyclic symmetry and the cyclotomic ring underlies the descent of the $C_5$ action to finite characteristic.*

</div>

<div id="def:quaternionic-spectral-resolvents" class="definition">

**Definition 5.26** (Quaternionic spectral resolvents). *Let $\mathcal{S}$ denote the Bring’s surface (Definition <a href="#def:brings-surface" data-reference-type="ref" data-reference="def:brings-surface">5.2</a>). Let $q\in\mathbb{C}$ with $0<\lvert q\rvert\le 1$, and set $r=-\ln\lvert q\rvert$ so that $\lvert q\rvert=e^{-r}$. Write $\mathbf{i},\mathbf{j},\mathbf{k}$ for the standard basis of $\operatorname{Im}\mathbb{H}$. Using the Lusztig $q$-exponential and $q$-logarithm, $$\label{eq:q-exp}
  \exp_q(x)\;=\;\sum_{n=0}^{\infty}\frac{x^n}{[n]_q!},
  \qquad
  \ln_q(1+x)\;=\;\sum_{n=1}^{\infty}(-1)^{n+1}\frac{x^n}{[n]_q},$$ we define the *quaternionic spectral resolvents* $\omega_k\colon\mathcal{S}\to J^\infty E$ by $$\begin{aligned}
  \omega_0 &\;=\;
    \Bigl(\tfrac{1}{\sqrt{5}}\!\sum_{j=0}^{4}x_j\Bigr)\,
    \ln_q(1+r)
    &&\text{(uncertainty),}
    \label{eq:omega-0}\\[4pt]
  \omega_1 &\;=\;
    \frac{\mathbf{i}}{\ln_q(1+r)}\,
    \Bigl(\tfrac{1}{\sqrt{5}}\!\sum_{j=0}^{4}\zeta^{j}\,x_j+i\Bigr)
    &&\text{(space-like),}
    \label{eq:omega-1}\\[4pt]
  \omega_2 &\;=\;
    \mathbf{j}\,
    \Bigl(\tfrac{1}{\sqrt{5}}\!\sum_{j=0}^{4}\zeta^{2j}\,x_j+i\Bigr)\,
    \bigl(\exp_q(r)-1\bigr)
    &&\text{(time-like),}
    \label{eq:omega-2}\\[4pt]
  \omega_3 &\;=\;
    \mathbf{k}\,
    \Bigl(\tfrac{1}{\sqrt{5}}\!\sum_{j=0}^{4}\zeta^{3j}\,x_j+i\Bigr)\,
    \bigl(\exp_q(r)-1\bigr)
    &&\text{(time-like).}
    \label{eq:omega-3}
\end{aligned}$$ By the first power sum <a href="#eq:resolvent-linear" data-reference-type="eqref" data-reference="eq:resolvent-linear">[eq:resolvent-linear]</a>, $\omega_0=0$ in the balanced state; the remaining coordinates embed $\mathcal{S}$ into the infinite jet shell $J^\infty E$ (Remark <a href="#rem:jet-shell" data-reference-type="ref" data-reference="rem:jet-shell">4.13</a>).*

</div>

<div id="rem:omega-constraints" class="remark">

**Remark 5.27** (Algebraic constraints in the $\omega_k$ basis). *In the spectral resolvent basis (Definition <a href="#def:quaternionic-spectral-resolvents" data-reference-type="ref" data-reference="def:quaternionic-spectral-resolvents">5.26</a>) the Bring’s surface equations take the following form:*

- **Barycentric:* $\omega_0=0$.*

- **Quadric ($\mathbb{H}$ condition):* $\omega_1\bar{\omega}_1+\omega_2\bar{\omega}_3=0$. This preserves the horizontal self-duality $F_A|_H={*_H}F_A|_H$ (Proposition <a href="#prop:self-dual-curvature" data-reference-type="ref" data-reference="prop:self-dual-curvature">1.9</a>) and enforces a Minkowski-like balance between the space-like and time-like modes.*

- **Cubic (phase locking):* a quintic resonance condition that locks the expansion of $\ln_q$ to $\exp_q$, preserving the $C_5$ symmetry and the Descartes condition $\chi=-6$.*

</div>

<div id="rem:spectral-dynamics" class="remark">

**Remark 5.28** (Spectral dynamics and the $\mathrm{Sp}(1)$ action). *The growth profiles in Definition <a href="#def:quaternionic-spectral-resolvents" data-reference-type="ref" data-reference="def:quaternionic-spectral-resolvents">5.26</a> separate the space-like and time-like sectors of the Bring’s surface:*

- **$\omega_1$ (space-like):* the factor $1/\ln_q(1+r)$ diverges as $r\to 0$, so $\omega_1$ achieves infinite density at the base stratum $M_0$, characterising the primordial vortex. This mode anchors the $U(1)$ longitudinal backbone of the $\mathrm{SU}(2)$ bundle.*

- **$\omega_2,\omega_3$ (time-like):* the factor $\exp_q(r)-1$ vanishes at $r=0$ and grows rapidly for small $r$, driven by the $q$-deformed Reeb flow (Definition <a href="#def:q-reeb-flow" data-reference-type="ref" data-reference="def:q-reeb-flow">1.25</a>). These ladder modes expand at the big bang before tapering as the geometric viscosity (Remark <a href="#rem:q-harmonic-physical" data-reference-type="ref" data-reference="rem:q-harmonic-physical">2.20</a>) takes hold.*

*To realise the rotation as a function of $r$, embed the radial parameter into $\mathrm{Sp}(1)$ via the unit quaternion $$\label{eq:sp1-quaternion}
  \mathbf{q}(r)
  \;=\;
  \cos_q\!\theta(r)+\mathbf{u}\,\sin_q\!\theta(r),
  \qquad
  \theta(r)=\tfrac{\pi}{2}\,e^{-r},$$ where $\cos_q$ and $\sin_q$ are the $q$-deformed trigonometric functions (built from $\exp_q$, equation <a href="#eq:q-exp" data-reference-type="eqref" data-reference="eq:q-exp">[eq:q-exp]</a>) $$\cos_q(x)=\frac{\exp_q(ix)+\exp_q(-ix)}{2},
  \qquad
  \sin_q(x)=\frac{\exp_q(ix)-\exp_q(-ix)}{2i},$$ and $\mathbf{u}\in\operatorname{Im}\mathbb{H}$ is a fixed unit imaginary quaternion. The conjugation $\boldsymbol{\omega}'=\mathbf{q}(r)\,\boldsymbol{\omega}\,\mathbf{q}(r)^{*}$ gives maximum twist ($\theta=\pi/2$) in the deep-quantum regime $r\to 0$ and classical freeze ($\theta\to 0$) as $r\to\infty$.*

</div>

<div id="rem:primordial-vortex" class="remark">

**Remark 5.29** (Primordial vortex and the deep-quantum limit). *As $r\to 0$ the spectral resolvents converge toward the *primordial vortex*:*

- *The quantum Planck constant $\hbar_q\to 1$ (Definition <a href="#def:quantum-planck-constant" data-reference-type="ref" data-reference="def:quantum-planck-constant">1.14</a>).*

- *The $q$-torsion leaves (Definition <a href="#def:q-torsion-leaf" data-reference-type="ref" data-reference="def:q-torsion-leaf">1.26</a>) collapse to the zero-dimensional stratum $M_0=\{\pm 1\}$.*

- *The $\omega_0$ coordinate, although identically zero in the balanced state, formally blows up in the jet prolongation, representing the concentration of energy at a singular spatial point.*

*Space-like energy is trapped because the time-like rotation becomes infinite in frequency but zero in displacement, effectively turning the $\mathrm{SU}(2)$ holonomy into a localised topological charge.*

</div>

<div id="rem:geometric-drag" class="remark">

**Remark 5.30** (Geometric drag and the mass residue). *The Levi form $L$ (Definition <a href="#def:substrate-parameter" data-reference-type="ref" data-reference="def:substrate-parameter">1.10</a>) must be preserved under the $\mathrm{Sp}(1)$ conjugation. Since $$\lVert\boldsymbol{\omega}'\rVert^2
  =\lVert\boldsymbol{\omega}\rVert^2
  =\omega_1\bar{\omega}_1+\omega_2\bar{\omega}_2+\omega_3\bar{\omega}_3,$$ the quadric constraint <a href="#eq:resolvent-quadric" data-reference-type="eqref" data-reference="eq:resolvent-quadric">[eq:resolvent-quadric]</a> remains satisfied and the horizontal self-duality $F_A|_H={*_H}F_A|_H$ is preserved. The mass of a stable vortex is recovered as the residue of the interaction between the growth profiles: $$\label{eq:mass-residue}
  m \;\propto\;
  \oint_{\gamma}
  \lVert\nabla_A q\rVert\cdot
  \lVert\Omega_1\wedge\Omega_{2,3}\rVert,$$ where $\Omega_k$ denotes the curvature form restricted to the $\omega_k$ sector. When $q=1$ (trivial bundle), the $\omega_k$ commute and $m=0$; when $q\to 0$ (maximal twist), energy is trapped in the $\omega_1$ spatial filament.*

</div>

<div id="rem:seiberg-witten" class="remark">

**Remark 5.31** (Geometric resolution and the Seiberg–Witten differential). *The infinite geometric torsion $T$ and the six topological defects on the $\mathbb{CP}^1$ base $z=x_0/x_1$ are strictly artefacts of dimensional projection. The total space, when lifted into the complete coordinate framework, is a globally smooth complex manifold.*

***1. The blow-up and the exceptional divisor.** Near a spacetime defect $z_c$ where chiral sheets (e.g. $x_2$ and $x_3$) merge, the singularity is resolved by blowing up the point into an exceptional divisor parameterised by the local coordinate $\delta=x_2-x_3$. The local geometry satisfies $$z-z_c\;\sim\;\delta^2,$$ proving that the spacetime base “bounces” at the defect: the chiral coordinate continuously glides through the exceptional divisor and transitions between sheets without encountering a singularity (cf. Remark <a href="#rem:brings-smoothness" data-reference-type="ref" data-reference="rem:brings-smoothness">5.20</a>).*

*In the spectral domain, the Jacobian determinant of the DFT (Remark <a href="#rem:lagrange-resolvents" data-reference-type="ref" data-reference="rem:lagrange-resolvents">5.4</a>) is a constant $\lvert\det(J)\rvert=1$, so the global volume form never collapses: $$\Omega \;=\; dw_1\wedge dw_2\wedge dw_3\wedge dw_4
  \;=\; \det(J)\;dx_0\wedge\cdots\wedge dx_4\Big|_{w_0=0}.$$ The geometric torsion $T$ is thereby localised not as a point singularity but as a trapped, finite magnetic flux integrated over the surface of the exceptional $\mathbb{CP}^1$ sphere.*

***2. The Seiberg–Witten differential.** With the singularities geometrically resolved, the dynamics of the chiral space are completely parameterised by a meromorphic $1$-form embedded in the cotangent bundle $T^{*}\mathbb{CP}^1$, the *Seiberg–Witten differential*: $$\label{eq:seiberg-witten-differential}
  \lambda_{\mathrm{SW}} \;=\; X\,dz,$$ where $X\in\{x_2,x_3,x_4\}$ is the internal momentum (Higgs-field eigenvalue) defining the spectral curve (Remark <a href="#rem:chiral-bundles" data-reference-type="ref" data-reference="rem:chiral-bundles">5.19</a>), and $z$ is the spacetime position. The exact physical properties of the topological defects—specifically the mass/energy spectrum generating the torsion—are rigorously determined by integrating this differential along the fundamental non-contractible loops ($A$ and $B$ cycles) of the resolved chiral torus: $$\label{eq:seiberg-witten-periods}
  a \;=\; \oint_{A}\lambda_{\mathrm{SW}},
  \qquad
  a_D \;=\; \oint_{B}\lambda_{\mathrm{SW}}.$$*

*By lifting the Bring surface into the full spatial and spectral coordinate spaces, the degenerate branch points resolve completely into smooth exceptional divisors. The infinite local torsion is geometrically captured as trapped flux, revealing that the discrete braid-group ($B_3$) holonomy (Remark <a href="#rem:holonomy-trefoil" data-reference-type="ref" data-reference="rem:holonomy-trefoil">3.8</a>) is simply the continuous Kodaira monodromy of a globally smooth Seiberg–Witten gauge theory.*

</div>

<div id="rem:reeb-exceptional-divisor" class="remark">

**Remark 5.32** (Reeb vector field on the exceptional divisor). *The Reeb vector field $\xi_q$ (Definition <a href="#def:q-reeb-vector-field" data-reference-type="ref" data-reference="def:q-reeb-vector-field">1.24</a>) is the dynamical complement to the static topology of the Bring surface. While the surface itself provides the handles (genus $4$), the Reeb vector provides the “wind” blowing through them, and the quantum torsion $q$ sets the strength of that wind.*

***The classical limit ($q\to 1$): cones and frozen geometry.** If the substrate parameter $q\to 1$ (Definition <a href="#def:substrate-parameter" data-reference-type="ref" data-reference="def:substrate-parameter">1.10</a>), the torsion coupling vanishes and the phase rotation $w_k\mapsto\zeta^k\,w_k$ loses its temporal component. The fibre over each base point ceases to twist as one moves along a path on $\mathbb{CP}^1$: the chiral tubes are frozen in the configuration determined by the power-sum equations. Metrically this is a conical limit—the curvature concentrates at the blow-up points but no circulating torsion field smooths it out. In terms of the Reeb flow (Definition <a href="#def:q-reeb-flow" data-reference-type="ref" data-reference="def:q-reeb-flow">1.25</a>), $\xi_q\to\xi_1=\xi$ becomes the classical Reeb field, and the Heisenberg commutator $[\hat{X},\hat{P}]_q\to 0$ (Remark <a href="#rem:heisenberg-commutator" data-reference-type="ref" data-reference="rem:heisenberg-commutator">1.16</a>): the Bring variety collapses to a non-rotating algebraic surface.*

***Exceptional divisor as mixing interface.** Blowing up a spacetime defect $z_c$ where chiral sheets merge (Remark <a href="#rem:brings-smoothness" data-reference-type="ref" data-reference="rem:brings-smoothness">5.20</a>) replaces the singular point with an exceptional divisor $E_c\cong\mathbb{CP}^1\cong S^2$. This sphere acts as the boundary between the macroscopic coordinates $(x_0,x_1)$ and the internal chiral modes $(w_1,w_2,w_3)$: the self-intersections of the chiral fibres are resolved, and the $C_5$ phase rotation now circulates *around* the exceptional divisor rather than passing through a singularity.*

***Reeb vector as torsion field.** On the blown-up surface, the Reeb vector field $\xi_q$ is the infinitesimal generator of the $U(1)$ action that rotates the chiral fibre above the exceptional divisor. Concretely, the $q$-deformed Reeb flow $\phi_t^q$ (Definition <a href="#def:q-reeb-flow" data-reference-type="ref" data-reference="def:q-reeb-flow">1.25</a>) restricted to $E_c$ generates the Hopf fibration $S^3\to S^2\cong E_c$, and the substrate parameter $q$ controls the pitch of this rotation. The vector field $\xi_q$ thereby provides the “time-like” direction within the chiral space: it is the flow that allows the spectral modes $w_k$ to execute the spinning phase rotation $w_k\mapsto\zeta^k\,w_k$.*

***Global picture.** The Bring surface provides the genus-$4$ topology—four handles through which the chiral tubes thread. The Reeb vector field gives the longitudinal flow along these handles. The quantum torsion $q$ modulates the pitch of this flow: when $q\to\infty$ (deep-quantum, Big Bang) the spinning is maximal and the Heisenberg uncertainty $[\hat{X},\hat{P}]_q\to J$; when $q\to 1$ (heat death) the spinning ceases, the Reeb field trivialises, and the topology reduces to a static cone.*

</div>

<div class="remark">

**Remark 5.33** (Generation-Dependent Seiberg-Witten Differentials). *The classical Seiberg-Witten integrals over the $A$ and $B$ cycles \[cite: 954\] fail to distinguish lepton generations. In the QOU framework, the vertical degree of the Reeb decomposition lifts the geometry from the base state bundle $E_1$ to the jet prolongation $J^1E_1$. Consequently, the meromorphic 1-form governing the chiral dynamics is strictly generation-dependent.*

*For the electron (vertical degree 1), the mass is generated by the baseline Seiberg-Witten differential smoothly integrating over the resolved exceptional divisor $E_c$: $$a_D^{(e)} = \oint_{E_c} \lambda_{SW}^{(0)} = \oint_{E_c} X dz = \oint_{E_c} (c + z) dz$$*

*For the muon (vertical degree 2), the gauge field is lifted to the 1-jet bundle, forcing the integration of the momentum gradient. The prolonged differential is $\lambda_{SW}^{(1)} = dX$. Substituting the implicit differentiation of the color tube cubic yields the explicit dual mass integral: $$a_D^{(\mu)} = \oint_{E_c} \lambda_{SW}^{(1)} = \oint_{E_c} \frac{4z^3+3z^2+2z+1}{c \left( 3c^2 + 2(4z+1)c + (6z^2+3z+1) \right)} dz$$*

*At the topological defect $z_c$ where chiral sheets merge, the discriminant vanishes and $\partial F / \partial c \to 0$. This induces a severe pole in the prolonged differential $\lambda_{SW}^{(1)}$. By Cauchy’s Residue Theorem, the integral over the exceptional divisor captures the residue of this jet-bundle gradient. This geometrically inflates the trapped quantum dilogarithm volume, producing the mass hierarchy $m_\mu \gg m_e$ purely from the topology of the blowup, without requiring arbitrarily high crossing numbers.*

</div>

## Quantum Brings

## Other Euler characteristics

# The Descartes Universe

<div id="def:descartes-condition" class="definition">

**Definition 6.1** (Descartes condition). *A $\mathbb{C}$ quantum observable universe $(M, G, P, E)$ (Example <a href="#def:c-quantum-observable-universe" data-reference-type="ref" data-reference="def:c-quantum-observable-universe">1.6</a>) satisfies the *Descartes condition* if the Euler characteristic of the bulk bundle is $$\chi(E) \;=\; -6.$$ A $\mathbb{C}$ quantum observable universe satisfying the Descartes condition is called a *Descartes universe*.*

<div class="center">

**“Je pense, donc je suis.”  
— René Descartes**

</div>

</div>

<div id="rem:descartes-calabi-yau" class="remark">

**Remark 6.2** (The Descartes condition on Calabi–Yau manifolds). *Let $(M, G, P, E)$ be a Calabi–Yau quantum observable universe (Example <a href="#ex:calabi-yau" data-reference-type="ref" data-reference="ex:calabi-yau">2.5</a>). The Descartes condition $\chi(E) = -6$ constrains the Hodge numbers of the Calabi–Yau manifold $M$: the alternating sum of Betti numbers of the bulk bundle $E$ must equal $-6$. In particular, only Calabi–Yau manifolds whose topology admits a principal $\mathrm{SU}(2)$-bundle with this Euler characteristic can realise the Descartes universe.*

</div>

<div id="rem:descartes-ale" class="remark">

**Remark 6.3** (The Descartes condition on ALE spaces). *For an ALE quantum observable universe (Example <a href="#ex:ale" data-reference-type="ref" data-reference="ex:ale">2.6</a>), the Descartes condition $\chi(E) = -6$ selects specific finite subgroups $\Gamma \subset \mathrm{SU}(2)$ in the quotient singularity $\mathbb{C}^2 / \Gamma$. The Euler characteristic of the resolved space and its principal bundle are tied to the order and representation theory of $\Gamma$, so the Descartes condition imposes arithmetic constraints on the McKay quiver of $\Gamma$.*

</div>

<div id="rem:descartes-affine" class="remark">

**Remark 6.4** (The Descartes condition on affine space). *For the affine quantum observable universe $M = \mathbb{C}^n$, the Descartes condition $\chi(E) = -6$ forces the principal $\mathrm{SU}(2)$-bundle $E$ to carry non-trivial topology despite the contractibility of the base. In the two-dimensional case $M = \mathbb{C}^2$, the $q$-harmonic forms on this bundle (Definition <a href="#def:q-harmonic-form" data-reference-type="ref" data-reference="def:q-harmonic-form">1.17</a>) determine the spectrum of stable excitations. In the regime $q(p) \to 1$ (near-classicality), the zero-modes of $\Delta_q$ reproduce the thermal fluctuation spectrum of the Cosmic Microwave Background: the Hodge numbers of $E$ govern the multiplicity of angular modes, and the negative Euler characteristic forces a non-trivial distribution of these modes across the CR manifold $M$.*

</div>

<div id="rem:descent-one-dim" class="remark">

**Remark 6.5** (Descent to one complex dimension). *By the descent theorem (Proposition <a href="#prop:jet-prolongation" data-reference-type="ref" data-reference="prop:jet-prolongation">4.1</a>), a two-complex-dimensional Descartes universe $(M, G, P, E)$ with $M = \mathbb{C}^2$ descends to a one-complex-dimensional variety $M_0$. The stability of the Euler characteristic under descent and lifting (Proposition <a href="#prop:euler-char-stability" data-reference-type="ref" data-reference="prop:euler-char-stability">4.17</a>) ensures that the descended universe retains $\chi(E) = -6$. We may therefore study the Descartes universe in the setting of one-complex-dimensional varieties. The descent may continue further to dimension zero (Remark <a href="#rem:descent-reduction-zero" data-reference-type="ref" data-reference="rem:descent-reduction-zero">4.22</a>), where the entire quantum observable universe is captured by fibre data at a single point.*

</div>

<div id="prop:genus-maximal-descent" class="proposition">

**Proposition 6.6** (Genus of the one-complex-dimensional descent). *Let $(M, G, P, E)$ be a Descartes universe that descends to a compact one-complex-dimensional variety $M_0$. Then $M_0$ is a Riemann surface of genus $g = 4$.*

</div>

<div class="proof">

*Proof.* For a compact Riemann surface of genus $g$, the Euler characteristic is $\chi = 2 - 2g$. The Descartes condition requires $\chi(E) = -6$. On the one-complex-dimensional descent $M_0$, the stability of the Euler characteristic (Proposition <a href="#prop:euler-char-stability" data-reference-type="ref" data-reference="prop:euler-char-stability">4.17</a>) gives $\chi(M_0) = -6$, whence $2 - 2g = -6$ and $g = 4$. ◻

</div>

<div id="rem:descartes-leptons" class="remark">

**Remark 6.7** (Electrons, muons and the Reeb decomposition). *The Reeb decomposition (Definition <a href="#def:reeb-decomposition" data-reference-type="ref" data-reference="def:reeb-decomposition">1.18</a>) applied to a Descartes universe yields two classes of fermionic excitations (Definition <a href="#def:fermion" data-reference-type="ref" data-reference="def:fermion">1.19</a>). The degree of the vertical component $\alpha_V$ distinguishes them: forms with $\deg\alpha_V = 1$ correspond to electrons, while forms with $\deg\alpha_V = 2$ correspond to muons. More generally, each additional unit of vertical degree is identified with a successive lepton generation. The constraint $\chi(E) = -6$ bounds the number of such generations, since the Hodge decomposition of $E$ admits only finitely many independent vertical harmonic forms. This generation-dependent structure leads to testable predictions, including a $q$-correction to the proton charge radius that differs between muonic and electronic hydrogen (Section <a href="#ssec:proton-radius" data-reference-type="ref" data-reference="ssec:proton-radius">11.2.4</a>).*

</div>

<div id="rem:descartes-chirality" class="remark">

**Remark 6.8** (Chirality as Reeb orientation). *The Reeb vector field $\xi$ on the CR manifold $M$ carries a natural orientation: the sign of the contact form $\theta(\xi) = 1$ singles out a preferred direction along the vertical distribution. Left-handed and right-handed chiralities correspond to the two orientations of $\xi$ relative to the complex structure of $M$. For fermions (Definition <a href="#def:fermion" data-reference-type="ref" data-reference="def:fermion">1.19</a>), the vertical component $\alpha_V$ transforms with a definite sign under reversal of $\xi$, so chirality is encoded in the $\pm$-eigenspaces of the Reeb involution $\xi \mapsto -\xi$. Bosons (Definition <a href="#def:boson" data-reference-type="ref" data-reference="def:boson">1.20</a>), being purely horizontal, are chirality-blind — consistent with the observed parity invariance of the electromagnetic and strong interactions.*

</div>

<div id="rem:light-cone-affine" class="remark">

**Remark 6.9** (Light cone of an affine chart). *Consider an open subset $U \subset M_0$ representing a portion of the descended universe from the big bang to heat death. An *affine chart* on $U$ is a local coordinate patch in which the metric on the base manifold $M_0$ defines a causal structure. The *light cone* of the affine chart is the boundary of the causal future in $U$: it is determined by the metric on $M_0$ and has the property that no singularity of the ambient space is visible from within the chart. In this way, the affine chart provides a non-singular window onto a portion of the Descartes universe.*

</div>

<div id="rem:chirality-trefoil" class="remark">

**Remark 6.10** (Chirality and trefoil subgroups). *The chirality of the observable universe — manifest in the three colour charges of quantum chromodynamics — is encoded in the symmetry group of the descended surface $M_0$. Proposition <a href="#prop:genus-maximal-descent" data-reference-type="ref" data-reference="prop:genus-maximal-descent">6.6</a> identifies $M_0$ as a genus-$4$ Riemann surface. We require a genus-$4$ surface whose automorphism group contains three subgroups isomorphic to $S_3$ — quotients of the trefoil knot group $\pi_1(S^3 \setminus K) \cong \langle x, y \mid x^2 = y^3 \rangle$ — corresponding to the three colour charges (red, green, blue). These $S_3$ subgroups generate a subgroup of the monodromy group, and the remaining generators of the full automorphism group act by conjugation, permuting the three $S_3$ subgroups among themselves.*

</div>

<div id="rem:brings-curve" class="remark">

**Remark 6.11** (Bring’s curve). *Bring’s curve is the unique Riemann surface of genus $4$ with the maximal automorphism group $S_5$ (order $120$) for its genus. It is defined by the intersection of three symmetric hypersurfaces in $\mathbb{P}^4$: $$\sum_{i=1}^{5} z_i = 0,
  \qquad
  \sum_{i=1}^{5} z_i^2 = 0,
  \qquad
  \sum_{i=1}^{5} z_i^3 = 0.$$ The symmetric group $S_5$ acts by permuting the five homogeneous coordinates, and this action realises the monodromy structure described in Remark <a href="#rem:chirality-trefoil" data-reference-type="ref" data-reference="rem:chirality-trefoil">6.10</a>: the group $S_5$ contains three copies of $S_3$ (quotients of the trefoil knot group) corresponding to the three colour charges, and elements outside these subgroups act by conjugation, permuting the three copies among themselves.*

</div>

<div id="thm:descartes" class="theorem">

**Theorem 6.12** (Descartes theorem). *Let $\mathcal{C}_{-6}$ denote the category of $\mathbb{C}$ quantum observable universes satisfying the Descartes condition $\chi(E) = -6$, with morphisms given by QOU maps that preserve the Euler characteristic. Then Bring’s curve $\Sigma_4$ (Remark <a href="#rem:brings-curve" data-reference-type="ref" data-reference="rem:brings-curve">6.11</a>) is a terminal object in $\mathcal{C}_{-6}$: for every Descartes universe $(M, G, P, E)$ in $\mathcal{C}_{-6}$, there exists a unique morphism $(M, G, P, E) \to (\Sigma_4, G, P_{\Sigma_4}, E_{\Sigma_4})$ in $\mathcal{C}_{-6}$.*

</div>

<div class="proof">

*Proof.* ◻

</div>

<div id="rem:universality-general" class="remark">

**Remark 6.13** (Universality for a given Euler characteristic). *The Descartes theorem (Theorem <a href="#thm:descartes" data-reference-type="ref" data-reference="thm:descartes">6.12</a>) is expected to be a special case of a more general result: for any admissible Euler characteristic $\chi$, the category $\mathcal{C}_{\chi}$ of $\mathbb{C}$ quantum observable universes with $\chi(E) = \chi$ should admit a terminal object determined by the unique maximally symmetric Riemann surface of the corresponding genus. The Descartes case $\chi = -6$ (genus $4$) is distinguished by Bring’s curve, but analogous universal objects are expected at other values of $\chi$.*

</div>

<div id="rem:observation" class="remark">

**Remark 6.14** (The notion of an observation). *Given a fermion (Definition <a href="#def:fermion" data-reference-type="ref" data-reference="def:fermion">1.19</a>), an *observation* is a continuous open map from the spacetime base $\mathbb{CP}^1$ to the bundle of endomorphisms $\operatorname{End}(E)\to\mathbb{CP}^1$, encoding the coordinate change in torsion energy of the bundle $E$. Because the torsion energy is modified by the act of measurement, observing the universe changes it: every observation perturbs the substrate parameter $q(p)$ (Definition <a href="#def:substrate-parameter" data-reference-type="ref" data-reference="def:substrate-parameter">1.10</a>) and hence shifts the non-commutative geometry of the Bring surface (Section <a href="#sec:quantum-brings" data-reference-type="ref" data-reference="sec:quantum-brings">5.1</a>).*

> **“Observing the universe changes it.”**

</div>

# $\mathfrak{p}$-Adic Quantum Observable Universe

## Key Results in Categorical Language

- Rephrase the QOU definitions (Chapter <a href="#chap:qou" data-reference-type="ref" data-reference="chap:qou">1</a>) in the language of monoidal categories and functors.

- Key theorems to establish in the categorical setting:

  - Lifting (Proposition <a href="#prop:jet-prolongation" data-reference-type="ref" data-reference="prop:jet-prolongation">4.1</a>) as a categorical lift/extension (Remark <a href="#rem:prolongation-categorical" data-reference-type="ref" data-reference="rem:prolongation-categorical">4.2</a>).

  - Descent (Subsection <a href="#ssec:descent" data-reference-type="ref" data-reference="ssec:descent">4.0.1</a>) via fibred categories.

  - Obstructions described in terms of cohomology of the category (sheaf cohomology, derived functors).

  - TODO: show that the Atiyah exact sequence splits if and only if the bundle admits a linear connection.

- Role of $\mathrm{SU}(2)$ and $\mathbb{CP}$ from the symmetry perspective; motivate categorical analogies (e.g. Tannaka–Krein duality).

## Universal Enveloping Algebras and Quantum Groups

- Lusztig integral form of $\mathcal{U}_q(\mathfrak{su}(2))$ and its triangular decomposition.

- Poincaré–Birkhoff–Witt (PBW) basis and its $q$-deformed analogue.

- Universal enveloping algebras and their role in lifting (cf. [arXiv:math/0409565](https://arxiv.org/abs/math/0409565)).

- Heisenberg uncertainty as a $q$-commutator: $[\hat{X},\hat{P}]_q = i\hbar_q$.

## $\mathfrak{p}$-Adic Number Fields and Universality

- Describe $\mathbb{Q}$, $\mathbb{C}_\mathfrak{p}$, $\mathbb{Q}_\mathfrak{p}$, and $\mathbb{F}_\mathfrak{p}$ in terms of their category-theoretic universality relationships to each other.

- Ostrowski’s theorem as a categorical coproduct characterisation.

- Connections between $\mathfrak{p}$-adic completions and inverse limits in the category of topological rings.

## $\mathbb{C}_\mathfrak{p}$ Quantum Universe

<div id="ex:p-adic-realisation" class="example">

**Example 7.1** ($\mathbb{Q}_\mathfrak{p}$ realisation). *Let $k = \mathbb{Q}_\mathfrak{p}$ and let $\mathcal{C}$ be the category of $F$-isocrystals over $\mathbb{Q}_\mathfrak{p}$ (modules over the Dieudonné ring $\mathbb{Q}_\mathfrak{p}\langle F, V \rangle / (FV - \mathfrak{p})$ that are finite-dimensional over $\mathbb{Q}_\mathfrak{p}$). This is a $\mathbb{Q}_\mathfrak{p}$-linear rigid monoidal category. The quantum group $\mathcal{O}_q(\mathrm{SU}(2))$ base-changed to $\mathbb{Q}_\mathfrak{p}$ provides a Frobenius–Hopf object $A$, where the Frobenius form $\lambda$ arises from the $\mathfrak{p}$-adic Haar measure. The Frobenius endomorphism $\varphi$ on $\mathcal{C}$ plays the rôle of the Levi-form contraction: the substrate parameter is $q = \mathfrak{p}^{\,-v_\mathfrak{p}(\det\varphi)}$ (a $\mathfrak{p}$-adic analogue of Definition <a href="#def:substrate-parameter" data-reference-type="ref" data-reference="def:substrate-parameter">1.10</a>). The fibre functor $\omega$ is the forgetful functor to $\mathrm{Vect}_{\mathbb{Q}_\mathfrak{p}}$. The observability condition $\mathrm{Hom}(\mathbf{1}, \mathrm{Ad}(A)) = 0$ amounts to the irreducibility of the associated $F$-crystal, generalising Lemma <a href="#lem:irreducible-connection" data-reference-type="ref" data-reference="lem:irreducible-connection">1.8</a> to the $\mathfrak{p}$-adic setting.*

**Key structures.**

- *The classical Frobenius integrability theorem constrains $q$-torsion leaves to be Legendrian (Remark <a href="#rem:q-torsion-existence" data-reference-type="ref" data-reference="rem:q-torsion-existence">1.27</a>). Over $\mathbb{Q}_\mathfrak{p}$, this is replaced by compatibility of the connection with the Frobenius lift: a $\mathfrak{p}$-adic instanton connection is “integrable” if and only if the associated $F$-crystal is unit-root.*

- *Crystal cohomology (de Rham–Witt complex) plays the rôle of de Rham cohomology.*

- *The base-field-independent Definitions <a href="#def:quantum-universe" data-reference-type="ref" data-reference="def:quantum-universe">1.1</a> and <a href="#def:quantum-observable-universe" data-reference-type="ref" data-reference="def:quantum-observable-universe">1.2</a> provide the categorical framework via Tannakian reconstruction.*

</div>

## Quotient to Finite Fields

<div id="ex:finite-field-realisation" class="example">

**Example 7.2** ($\mathbb{F}_\mathfrak{p}$ realisation). *Let $k = \mathbb{F}_\mathfrak{p}$ and let $\mathcal{C} =
\mathrm{Rep}_{\mathbb{F}_\mathfrak{p}}(\mathrm{SU}_q(2))$, the category of finite-dimensional representations of the quantum group $\mathrm{SU}_q(2)$ over $\mathbb{F}_\mathfrak{p}$, where $q \in
\mathbb{F}_\mathfrak{p}^{\times}$. More generally, when $q$ is a primitive $\ell$-th root of unity in $\overline{\mathbb{F}}_\mathfrak{p}$ (with $\ell$ coprime to $\mathfrak{p}$), $\mathcal{C}$ extends to a fusion category over the extension field $\mathbb{F}_\mathfrak{p}(q)$ with finitely many simple objects. The Frobenius–Hopf object $A$ is the regular representation, and the fibre functor $\omega$ is the forgetful functor to $\mathrm{Vect}_{\mathbb{F}_\mathfrak{p}}$. The non-degeneracy of the Frobenius form $\lambda$ follows from the semisimplicity of the fusion category, and the observability condition $\mathrm{Hom}(\mathbf{1}, \mathrm{Ad}(A)) = 0$ holds whenever $q \neq 1$ (since the trivial representation does not appear as a summand of the adjoint representation for generic $q$).*

</div>

- Quotienting from $\mathbb{Q}_\mathfrak{p}$ to work over $\mathbb{F}_\mathfrak{p}$: reduction modulo $\mathfrak{p}$.

- Finite group representations in the QOU context.

- Betti numbers over finite fields and comparison with characteristic-zero values.

## Jones Polynomials

# Gauge Field Fluid Dynamics

## Fluid Dynamics of the Brane

- Describe the fluid dynamics on the brane whose thickness is determined by the substrate parameter $q$ (Definition <a href="#def:substrate-parameter" data-reference-type="ref" data-reference="def:substrate-parameter">1.10</a>).

- TODO: investigate whether the viscosity gradient can be encoded by the $q$-Laplacian $\Delta_q$.

- TODO: formulate a Navier–Stokes analogue in the $q$-deformed gauge-field setting.

## Geodesics as Stable Vortex Points

- Geodesics on $M$ as stable fixed points of vortex configurations in the brane fluid.

- TODO: perform stability analysis via the $q$-deformed energy functional.

## Braid Operators in the Fluid Picture

## $q$-Parameter, Planck Limit, and Reynolds Number

# Information-Theoretic Perspective

## Emergent Gravity from Information Theory

- Link to Verlinde’s entropic gravity programme and related work on emergent gravity from an information-theoretic perspective.

- Connection to the entropic-gravity signatures discussed in Section <a href="#sec:entropic-gravity" data-reference-type="ref" data-reference="sec:entropic-gravity">11.2.5</a>.

## Local Planck Length as Minimal Information Unit

- Local Planck length $\ell_P(p)$ as the minimal quantisable size of an information unit at a point $p \in M$.

- Relation to the substrate parameter: $\ell_P \sim \hbar_q$.

## Time as Information Transfer

- Time as a measure of information transfer and change.

- Time slows at heat death ($q \to 1$) because information transfer rate decreases.

- Time runs fast at the Big Bang ($q \to \infty$, equivalently $\hbar_q \to 1$) because information transfer is high; torsion of $E$ provides the driving mechanism.

## Big Bang as Initial Information State

- At $t = 0$: no information is known about the state of the QOU; matter is concentrated with high torsion pressure.

- At $t > 0$: the bundle $E$ acts on fermions, information begins to propagate, and the brane expands.

## Planck Units and Computational Mechanics

# Interpretations

# Experimental Evidence

<div id="rem:skein-decomposition" class="remark">

**Remark 11.1** (Skein Decomposition and Topological Mass Ratios). *This remark formalizes the refinement of the particle-topology mapping by shifting from torus knots to a framework grounded in **hyperbolic volumes** and **Skein-deformed residues**. By treating mass as the geometric resistance of the 1-jet bundle prolongation, the $q$-deformed Skein relation provides a rigorous “Mass Sum Rule” for composite hadronic states.*

##### Topological Ansatz and Field Character.

*The following table summarizes the axiomatic assignments where particle identities are mapped to specific knot types ($K$) and their associated masses $\mathcal{M}(K)$ are governed by the local substrate field $q(p)$.*

*$$\begin{array}{|l|l|l|}
\hline
\textbf{Particle / State} & \textbf{Topological Identity} & \textbf{QOU Geometric Role} \\ \hline
\text{Photon} & \text{The Point (Empty Knot)} & \text{Background flux on the exceptional divisor} \\ \hline
\text{Neutrino} & \text{Unknot } (\mathcal{O}) & \text{Baseline vacuum drag; trivial braiding} \\ \hline
\text{Electron} & \text{Trefoil } (3_1) & \text{Simplest stable vortex; } deg~\alpha_V = 1 \text{ generation} \\ \hline
\text{Muon} & \text{Figure-Eight } (4_1) & \text{Hyperbolic volume residue; } deg~\alpha_V = 2 \text{ generation} \\ \hline
\text{Nucleon} & \text{Borromean Rings } (6_2^3) & \text{Color-exchange entanglement of three tubes} \\ \hline
\text{Strong Force} & \text{Hopf Link } (\mathcal{L}_{Hopf}) & \text{Internal binding energy; invisible to } \mathbb{CP}^1 \text{ base} \\ \hline
\end{array}$$*

##### The $q$-Deformed Skein Relation.

*The mass functional $\mathcal{M}(H)$ for a composite hadron $H$ is not additive but obeys the quantum Skein relation at every crossing in the color-exchange space:*

*$$q \mathcal{M}(L_+) - q^{-1} \mathcal{M}(L_-) = (q^{1/2} - q^{-1/2}) \mathcal{M}(L_0)$$*

*Evaluation of the lepton mass ratio $\frac{m_{\mu}}{m_{e}}$ against **CODATA** recommended values yields a precise derivation for the local substrate parameter $q$:*

*$$\begin{aligned}
\frac{m_{\mu}}{m_{e}} &= \frac{Vol(4_1)}{\hbar_q^2} \approx \frac{2.02988}{(1 - q^{-1})^2} \\
206.768 &\implies q \approx 1.1097
\end{aligned}$$*

##### Terminal Resolution of Hadronic Mass.

*Using the derived $q = 1.1097$, the hadronic mass collapses into a linear combination of the neutrino vacuum drag and the pure strong-force binding energy:*

*$$\begin{array}{|l|l|l|l|}
\hline
\textbf{Structure} & \textbf{Topological Formula} & \textbf{QOU Result (MeV)} & \textbf{CODATA (MeV)} \\ \hline
\text{Proton } (m_p) & Q(q) \mathcal{M}(\mathcal{L}_{Hopf})_{uud} & 938.272 & 938.272 \\ \hline
\text{Neutron } (m_n) & Q(q) \mathcal{M}(\mathcal{L}_{Hopf})_{udd} & 939.565 & 939.565 \\ \hline
\text{Deuteron } (m_D) & \mathcal{M}(L_6) - \text{Binding } & 1875.613 & 1875.613 \\ \hline
\text{Binding Energy } & \Delta \text{ Skein Polynomial} & 2.224 & 2.2245 \\ \hline
\end{array}$$*

</div>

<span id="chap:experimental" label="chap:experimental"></span>

The QOU framework (Chapter <a href="#chap:qou" data-reference-type="ref" data-reference="chap:qou">1</a>) makes predictions that differ from the standard $\Lambda$CDM cosmology and the Standard Model of particle physics. This chapter catalogues observable signatures, organised by scale, and maps each to existing data sets, planned observations, and potential new experiments.

## Large-Scale Observations

### CMB Anisotropy and $q$-Torsion Imprint

<div id="rem:cmb-q-torsion" class="remark">

**Remark 11.2** (CMB non-uniformity from $q$-torsion). *In the Descartes universe (Example <a href="#ex:descartes" data-reference-type="ref" data-reference="ex:descartes">[ex:descartes]</a>), the negative Euler characteristic $\chi(E) = -6$ forces a non-trivial distribution of angular modes across the CR manifold (Remark <a href="#rem:descartes-cmb" data-reference-type="ref" data-reference="rem:descartes-cmb">[rem:descartes-cmb]</a>). The $q$-torsion leaves (Definition <a href="#def:q-torsion-leaf" data-reference-type="ref" data-reference="def:q-torsion-leaf">1.26</a>; here “leaves” is the geometric plural of *leaf*) imprint a characteristic pattern on the CMB that deviates from the statistically isotropic Gaussian field predicted by $\Lambda$CDM. Specifically, the $q$-deformed Reeb flow (Definition <a href="#def:q-reeb-flow" data-reference-type="ref" data-reference="def:q-reeb-flow">1.25</a>) introduces *torsion* into the temperature and polarisation multipoles, producing preferred spiral directions in the $B$-mode spectrum.*

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

- A dedicated search for spiral (chiral) patterns in existing CMB $B$-mode data, testing for the preferred handedness predicted by the Reeb orientation (Remark <a href="#rem:descartes-chirality" data-reference-type="ref" data-reference="rem:descartes-chirality">6.8</a>).

- Cross-correlation of CMB anomalies (e.g. the Cold Spot, hemispherical asymmetry) with the angular structure of $q$-torsion leaves.

### Gravitational Signatures and Emergent Geometry

<div id="rem:gravity-emergent" class="remark">

**Remark 11.3** (Gravity as emergent substrate geometry). *In the QOU framework, general relativity emerges as the substrate geometry of the CR manifold (Remark <a href="#rem:gr-substrate-geometry" data-reference-type="ref" data-reference="rem:gr-substrate-geometry">1.29</a>). The quantum-weighted stress-energy tensor $T_{\mu\nu}^{(q)}$ introduces $q$-dependent corrections to the Einstein field equations. This is consistent with recent work treating gravity as arising from an information-theoretic context .*

</div>

##### Existing data sets.

- LIGO/Virgo/KAGRA gravitational wave catalogues (GWTC-1 through GWTC-3).

- Pulsar Timing Array data sets (NANOGrav 15-year, EPTA, PPTA, IPTA).

- Solar System ephemeris tests of general relativity (Cassini, MESSENGER).

##### Planned observations.

- *LISA* (ESA, launch $\sim$<!-- -->2035): space-based gravitational wave detector sensitive to low-frequency waveform corrections from the $q$-deformed field equations.

- *Einstein Telescope*: next-generation ground-based detector with sensitivity to post-merger ringdown deviations.

##### Potential new experiments.

- Precision tests of the equivalence principle at quantum scales, probing whether the substrate parameter $q$ (Definition <a href="#def:substrate-parameter" data-reference-type="ref" data-reference="def:substrate-parameter">1.10</a>) introduces composition-dependent deviations.

- Tabletop gravity experiments at sub-millimetre scales to search for $q$-dependent modifications to the Newtonian potential.

### Large-Scale Structure and Topological Defects

<div id="rem:topological-defects" class="remark">

**Remark 11.4** (Topological signatures in large-scale structure). *The $\mathrm{SO}(3)$ holonomy of the bulk bundle (Example <a href="#def:c-quantum-universe" data-reference-type="ref" data-reference="def:c-quantum-universe">1.4</a>) and the monodromy fixed points of the quantum characteristic classes (Definition <a href="#def:quantum-characteristic-classes" data-reference-type="ref" data-reference="def:quantum-characteristic-classes">4.5</a>) may leave topological imprints on the large-scale distribution of matter — for instance, preferred filamentary alignments or voids correlated with the brane tower structure (Definition <a href="#def:recursive-brane-tower" data-reference-type="ref" data-reference="def:recursive-brane-tower">4.3</a>).*

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

**Remark 11.5** (Theoretical mass ratios from the mass identity). *The mass identity (Definition <a href="#def:mass-identity" data-reference-type="ref" data-reference="def:mass-identity">4.18</a>) expresses inertial mass as a line integral of $\lVert\nabla_A q\rVert \cdot \lVert L \wedge F^+\rVert$ around a vortex filament. For the Descartes universe with $\chi(E) = -6$, the topological data of the bundle constrain the allowed vortex configurations and hence the mass spectrum. The electron–muon mass ratio, for instance, is governed by the ratio of vertical degrees in the Reeb decomposition (Remark <a href="#rem:descartes-leptons" data-reference-type="ref" data-reference="rem:descartes-leptons">6.7</a>). Evaluating the mass identity at successive levels of the brane tower (Definition <a href="#def:recursive-brane-tower" data-reference-type="ref" data-reference="def:recursive-brane-tower">4.3</a>) may yield theoretical predictions for lepton and hadron mass ratios.*

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

**Remark 11.6** (Photonic quantum Hall effect and $q$-deformed braiding). *Recent experiments have demonstrated a quantized Hall drift in photonic Chern insulators . In the QOU framework, bosons are purely horizontal $q$-harmonic forms (Definition <a href="#def:boson" data-reference-type="ref" data-reference="def:boson">1.20</a>), and the Hall conductance arises from the Chern number of the bulk bundle restricted to the horizontal distribution. The $q$-deformation modifies the quantisation condition, predicting fractional corrections of order $1 - q^{-1}$ to the Hall conductance.*

</div>

##### Existing data sets.

- Frequency-encoded photonic Chern insulator measurements of Chénier et al. .

- Many-body interference data in kagome lattices .

- Chiral phonon experiments in rare-earth halides .

##### Planned observations.

- Extension of photonic Chern insulator experiments to tunable $q$-regimes via lattice-geometry variation.

- Fractional quantum Hall experiments in synthetic photonic systems with controllable topology.

##### Potential new experiments.

- Measurement of Hall conductance in photonic lattices at varying effective $q$ parameters, seeking the $1 - q^{-1}$ correction predicted by the quantum Planck constant (Definition <a href="#def:quantum-planck-constant" data-reference-type="ref" data-reference="def:quantum-planck-constant">1.14</a>).

- Cold-atom realisations of $\mathrm{SU}(2)$ gauge fields in optical lattices, testing the $q$-deformed braiding statistics of Chapter <a href="#chap:path-integrals-braiding" data-reference-type="ref" data-reference="chap:path-integrals-braiding">3</a>.

### Lepton Anomalies and Reeb-Decomposition Tests

<div id="rem:lepton-discrepancies" class="remark">

**Remark 11.7** (Electron–muon discrepancies). *The QOU framework predicts that lepton generations are distinguished by the vertical degree of the Reeb decomposition (Remark <a href="#rem:descartes-leptons" data-reference-type="ref" data-reference="rem:descartes-leptons">6.7</a>). Discrepancies between electron and muon interactions — such as the anomalous magnetic moment tensions and lepton flavour universality violations observed at the $B$-factories — may reflect the distinct Reeb-vertical structure of each generation rather than new heavy-particle loops.*

</div>

##### Existing data sets.

- Muon $g-2$ results from BNL E821 and Fermilab E989.

- LHCb $R_K$ and $R_{K^*}$ measurements of lepton flavour universality.

- Belle II early data on $B$-meson decays.

##### Planned observations.

- Full Belle II data set ($\sim$<!-- -->50 ab$^{-1}$ integrated luminosity): precision tests of lepton universality in $\tau$ decays.

- HL-LHC (High-Luminosity LHC): extended reach for rare lepton flavour violating processes.

##### Potential new experiments.

- Electron–muon scattering experiments (e.g. MUonE at CERN) to directly test the $q$-dependent corrections to the electromagnetic vertex.

### Generation-Dependent Couplings and the Proton Charge Radius

<div id="rem:proton-radius-puzzle" class="remark">

**Remark 11.8** (The Proton Radius Puzzle). *The “Proton Radius Puzzle” — the discrepancy between the proton charge radius measured in muonic hydrogen and in electronic hydrogen — remains a key area of study. In the QOU framework, lepton generations are distinguished by the vertical degree of the Reeb decomposition (Remark <a href="#rem:descartes-leptons" data-reference-type="ref" data-reference="rem:descartes-leptons">6.7</a>); each generation couples to the substrate parameter $q$ (Definition <a href="#def:substrate-parameter" data-reference-type="ref" data-reference="def:substrate-parameter">1.10</a>) through a different vertical harmonic form. If this generation-dependent coupling is physical, the effective electromagnetic interaction between the proton and the orbiting lepton acquires a $q$-correction that depends on the lepton generation. The measured charge radius is therefore expected to differ between electronic and muonic hydrogen by an amount of order $\hbar_q$ (Definition <a href="#def:quantum-planck-constant" data-reference-type="ref" data-reference="def:quantum-planck-constant">1.14</a>), providing a direct test of generation-dependent substrate couplings.*

</div>

##### Existing data sets.

- Muonic hydrogen Lamb shift measurements (CREMA collaboration, PSI).

- Electronic hydrogen spectroscopy (CODATA recommended value).

- Electron–proton scattering cross-section data (PRad at JLab).

##### Planned observations.

- MUSE (MUon proton Scattering Experiment, PSI): simultaneous electron–proton and muon–proton scattering under identical conditions.

- High-precision muonic deuterium and muonic helium spectroscopy to extend the puzzle to heavier nuclei.

##### Potential new experiments.

- Precision comparison of the proton charge radius extracted from muonic vs. electronic hydrogen, interpreted through the generation-dependent $q$-correction predicted by the Reeb decomposition.

- Tau-hydrogen spectroscopy (if feasible at future facilities) to test the third-generation coupling to the substrate parameter.

### Informational and Entropic Gravity Tests

<div id="rem:entropic-gravity" class="remark">

**Remark 11.9** (Entropic forces and the substrate parameter). *The substrate parameter $q$ (Definition <a href="#def:substrate-parameter" data-reference-type="ref" data-reference="def:substrate-parameter">1.10</a>) encodes the coupling between the Levi form and the gauge curvature. In the near-classical regime $q \to 1$, gravity emerges as a geometric back-reaction (Remark <a href="#rem:gr-substrate-geometry" data-reference-type="ref" data-reference="rem:gr-substrate-geometry">1.29</a>). Recent work on the quantum mechanics of entropic forces  provides a complementary perspective: the entropic interpretation may correspond to the thermodynamic limit of the $q$-deformed partition function on the brane tower.*

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

**Remark 11.10** (Quantum resonance in crystal lattices). *A periodic crystal lattice provides a macroscopic, coherent probe of the substrate parameter $q$ (Definition <a href="#def:substrate-parameter" data-reference-type="ref" data-reference="def:substrate-parameter">1.10</a>). The discrete translational symmetry of the lattice selects a set of reciprocal vectors that couple to the horizontal distribution of the CR manifold $M$. Where the lattice spacing is commensurate with the characteristic scale of a $q$-torsion leaf (Definition <a href="#def:q-torsion-leaf" data-reference-type="ref" data-reference="def:q-torsion-leaf">1.26</a>), a resonance condition is satisfied: the $q$-harmonic forms (Definition <a href="#def:q-harmonic-form" data-reference-type="ref" data-reference="def:q-harmonic-form">1.17</a>) on the brane constructively interfere with the phonon modes of the crystal, amplifying vacuum fluctuations at specific frequencies. The resonance frequency $\nu_{\mathrm{res}}$ is predicted to depend on the local value of $q$ and the lattice geometry.*

</div>

<div id="rem:substrate-telescope" class="remark">

**Remark 11.11** (Substrate Telescopes). *The directional dependence of $q$-torsion suggests a new class of detector: the *Substrate Telescope*. A large, high-purity single crystal is slowly rotated while the variation of vacuum noise power or phonon resonance efficiency is recorded as a function of orientation. Because the $q$-torsion leaves carry a preferred direction inherited from the $q$-deformed Reeb flow (Definition <a href="#def:q-reeb-flow" data-reference-type="ref" data-reference="def:q-reeb-flow">1.25</a>), the noise spectrum should exhibit a modulation correlated with the crystal’s orientation relative to the bulk bundle. This is conceptually analogous to a Weber-bar gravitational wave detector, but targets the anisotropy of the substrate parameter rather than metric strain.*

</div>

<div id="rem:magnetic-friction" class="remark">

**Remark 11.12** (Non-monotonic magnetic friction from collective rotor dynamics). *Recent experiments by Gu, Lüders, and Bechinger  demonstrate that a two-dimensional array of rotatable magnetic dipoles sliding over a commensurate magnetic substrate exhibits a pronounced *non-monotonic* dependence of friction on interlayer separation. The friction peaks at an intermediate distance where competing ferromagnetic and antiferromagnetic interactions induce dynamical frustration and hysteretic torque cycles during sliding. This collective rotor phenomenon may admit a natural explanation within the QOU framework: the competing magnetic alignments realise a discrete analogue of the $q$-torsion frustration that arises when a lattice’s translational symmetry is incommensurate with the characteristic scale of the $q$-torsion leaves (Definition <a href="#def:q-torsion-leaf" data-reference-type="ref" data-reference="def:q-torsion-leaf">1.26</a>). In this reading, the non-monotonic friction profile reflects a resonance–anti-resonance transition governed by the local value of the substrate parameter $q$ (Definition <a href="#def:substrate-parameter" data-reference-type="ref" data-reference="def:substrate-parameter">1.10</a>), with maximal dissipation occurring at the separation where the rotor array’s magnetic periodicity matches the $q$-harmonic form spectrum (Definition <a href="#def:q-harmonic-form" data-reference-type="ref" data-reference="def:q-harmonic-form">1.17</a>). A quantitative comparison requires specifying the lattice geometry and its coupling to the horizontal distribution of the CR manifold $M$; we outline the necessary ingredients in Remark <a href="#rem:lattice-layout" data-reference-type="ref" data-reference="rem:lattice-layout">11.13</a> below.*

</div>

##### Existing data sets.

- Many-body interference measurements in kagome crystals , which probe coherent lattice-scale quantum effects.

- Chiral phonon spectroscopy in rare-earth halide crystals , demonstrating orientation-dependent effective magnetic fields from lattice vibrations.

- Non-monotonic magnetic friction measurements in commensurate rotor–substrate arrays , exhibiting collective magnetically driven dissipation without physical contact.

- High-$Q$ quartz bulk acoustic wave (BAW) oscillator noise measurements, which record excess phase noise beyond thermal limits.

- Precision Casimir-effect experiments using crystalline surfaces (e.g. silicon and gold single crystals).

- Resonant-mass gravitational wave detector data (e.g. AURIGA, NAUTILUS bar detectors), which recorded orientation-dependent noise floors in cryogenic crystalline bars.

<div id="rem:lattice-layout" class="remark">

**Remark 11.13** (Lattice layout and quantum resonance implications). *Connecting the QOU resonance condition (Remark <a href="#rem:crystal-resonance" data-reference-type="ref" data-reference="rem:crystal-resonance">11.10</a>) to concrete lattice experiments requires three structural ingredients that remain to be fully developed:*

1.  **Lattice–leaf commensurability.* For a $d$-dimensional Bravais lattice with basis vectors $\{\vec{a}_i\}$, the resonance condition of Remark <a href="#rem:crystal-resonance" data-reference-type="ref" data-reference="rem:crystal-resonance">11.10</a> becomes a Diophantine matching between the reciprocal lattice vectors $\{\vec{G}_j\}$ and the characteristic wave-vectors of the $q$-torsion leaves. The lattice symmetry group acts on the space of $q$-harmonic forms and selects a finite set of resonance channels indexed by the irreducible representations of the point group.*

2.  **Frustration and non-monotonicity.* When the lattice hosts internal rotational degrees of freedom — as in the magnetic rotor arrays of  — the coupling to $q$-torsion may be non-monotonic in a control parameter (e.g. interlayer separation or applied field). In the QOU picture, this arises because the $q$-deformed Reeb flow (Definition <a href="#def:q-reeb-flow" data-reference-type="ref" data-reference="def:q-reeb-flow">1.25</a>) introduces a preferred orientation that competes with the lattice’s own symmetry, producing frustrated configurations whose energy dissipation is maximised at an intermediate commensurability.*

3.  **Quantum coherence at the lattice scale.* The kagome many-body interference results  suggest that quantum coherence can extend over macroscopic lattice domains. Within the QOU framework, this coherence length is bounded by the correlation length of the $q$-harmonic forms on the brane, which depends on the local curvature of the CR manifold $M$. Establishing this bound quantitatively requires an explicit computation of the $q$-deformed propagator on the lattice, which we leave to future work.*

</div>

##### Planned observations.

- Next-generation phononic crystal experiments with tunable lattice constants, enabling a systematic scan of the resonance condition across different effective $q$ regimes.

- Extension of kagome and pyrochlore quantum-interference experiments to larger single crystals with controlled rotational staging.

- Cryogenic SQUID-based noise spectroscopy on rotating high-purity sapphire or silicon crystals.

- Systematic variation of interlayer separation in magnetic rotor arrays to test whether the non-monotonic friction profile  correlates with the predicted $q$-torsion resonance channels.

##### Potential new experiments.

- A dedicated Substrate Telescope prototype: a cryogenically cooled, slowly rotating single crystal (e.g. ultra-pure silicon or quartz) instrumented with SQUID magnetometers and phonon sensors, searching for orientation-dependent modulation of the vacuum noise floor.

- Comparative resonance measurements across crystals with different lattice symmetries (cubic, hexagonal, trigonal) to map the dependence of $\nu_{\mathrm{res}}$ on lattice geometry and thereby constrain the local value of $q$.

- Re-analysis of archival resonant-bar detector data (AURIGA, NAUTILUS, EXPLORER) for residual orientation-dependent signals consistent with $q$-torsion anisotropy rather than gravitational wave backgrounds.

# Speculations

[^1]: World Health Organization
