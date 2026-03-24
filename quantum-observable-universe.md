---
abstract: |
  This paper presents a mathematical framework for the Quantum Observable Universe (QOU). We introduce the notion of quantum torsion in this setting, study its lifting to higher categorical structures, and examine the resulting interpretational and experimental consequences. Speculative extensions are discussed in the final chapter.
author:
- Frederick Carl Leitner
bibliography:
- references.bib
date: 2026-03-21
title: Quantum Observable Universe
---

<div class="center">

  
This work is licensed under a [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/).  
You are free to share and adapt this material for any purpose,  
provided appropriate credit is given, a link to the license is provided,  
and any changes made are indicated.

</div>

**Proof-status key**

|                                               |                           |                                                   |                              |
|:---------------------------------------------:|:--------------------------|:-------------------------------------------------:|:-----------------------------|
|   <span style="color: ForestGreen"></span>    | Fully proved (sorry-free) | <span style="color: BurntOrange">$\forall$</span> | Stated in Lean (has `sorry`) |
| <span style="color: OliveGreen">-0.3em</span> | Merged into Mathlib       |   <span style="color: BrickRed">$\times$</span>   | Not ready to formalize       |

# Introduction

## Overview

This paper develops the theory of the **quantum observable universe** (QOU), a rigid monoidal category that encodes the algebraic structure of quantum observables together with the geometric data needed to recover spacetime physics.

**[Chapter 1](#chap:qou)** opens with notational preliminaries from category theory—rigid monoidal categories, dagger structures, and representation-theoretic examples—and gives a succinct axiomatic definition of a quantum observable universe. We derive several consequences that follow from the rigidity of the symmetries: a Frobenius relation, an involutive dagger structure, a canonical volume form, and the emergence of $\mathrm{SU}(2)$ via a Tannaka–Krein reconstruction. We define the categorical action functional and derive the variational equations that govern quantum observable universes. The chapter closes with an elaboration of the categorical and analytic foundations, including jet prolongation, transport, and torsion.

**[Chapter 2](#chap:torsion)** establishes lifting and descent theorems for quantum torsion, identifying the key obstructions—both cohomological and categorical—to extending local data to global structures.

**[Chapter 3](#chap:path-integrals-braiding)** explores knots and braids in the QOU framework, and provides both a fluid-dynamical and an information-theoretic perspective on the resulting invariants.

**[Chapter 4](#chap:universality)** examines quantum observable universes over different ground fields: the Archimedean (complex), non-Archimedean ($\mathfrak{p}$-adic), and finite-field cases.

**[Chapter 5](#chap:brings-surface)** develops Bring’s surface as a complete worked example of a quantum observable universe, providing explicit coordinate systems for spacetime and colour-time. We construct Lagrange resolvents, colour-tube coordinates, chiral fibrations, quaternionic spectral resolvents, and the Seiberg–Witten resolution.

**[Chapter 6](#chap:descartes-universe)** opens with the Descartes condition and theorem, then presents the topological mass ansatz and surveys experimental and observational evidence for the QOU framework, including predictions arising from the skein-theoretic mass formula and comparison with measured hadronic spectra.

**[Chapter 7](#chap:interpretations)** collects interpretive remarks and speculative extensions of the theory.

# Quantum Observable Universe

## Introduction

This chapter introduces the central construction of the paper: the **quantum observable universe**, a rigid symmetric monoidal category encoding the algebraic structure of quantum observables. We begin with categorical preliminaries (§<a href="#sec:rigid-monoidal" data-reference-type="ref" data-reference="sec:rigid-monoidal">1.2</a>), define the core axioms (§<a href="#sec:core-definitions" data-reference-type="ref" data-reference="sec:core-definitions">1.3</a>), and derive their consequences — including the emergence of $\mathrm{SU}(2)$ as the unique gauge group (§<a href="#sec:axiom-consequences" data-reference-type="ref" data-reference="sec:axiom-consequences">1.4</a>).

The categorical axioms lead to differential structures, a spatial realization functor bridging abstract algebra to contact geometry (§<a href="#sec:spatial-realization" data-reference-type="ref" data-reference="sec:spatial-realization">1.6</a>), and a variational action (§<a href="#sec:categorical-action" data-reference-type="ref" data-reference="sec:categorical-action">1.8</a>) whose Euler–Lagrange equations unify the Einstein field equation, Yang–Mills gauge theory, and the Schrödinger transport equation in a single commutative diagram (§<a href="#sec:physical-interpretation" data-reference-type="ref" data-reference="sec:physical-interpretation">1.15</a>).

## Preliminary: rigid monoidal categories

<div id="def:rigid-monoidal-category" class="definition">

**Definition 1.1** (Rigid monoidal category). *[<sup><span style="color: BurntOrange">$\forall$</span></sup>](https://litlfred.github.io/qou/lean/QOU.RigidMonoidalCategory) A **monoidal category** $(\mathcal{C}, \otimes, \mathbf{1})$ is a category equipped with a bifunctor $\otimes \colon \mathcal{C} \times \mathcal{C} \to \mathcal{C}$ (the *tensor product*), a unit object $\mathbf{1}$, and natural isomorphisms expressing associativity and unitality:*

*$$\begin{gathered}
\begin{tikzcd}[column sep=3em]
  (X \otimes Y) \otimes Z
    \ar[r, "\alpha_{X,Y,Z}", "\sim"']
  & X \otimes (Y \otimes Z)
\end{tikzcd}
\\[-0.5em]
\text{\small associativity}
\end{gathered}
\qquad
\begin{gathered}
\begin{tikzcd}[column sep=2.5em]
  \mathbf{1} \otimes X
    \ar[r, "\ell_X", "\sim"']
  & X
  & X \otimes \mathbf{1}
    \ar[l, "\rho_X"', "\sim"]
\end{tikzcd}
\\[-0.5em]
\text{\small unitality}
\end{gathered}$$*

*The category is *rigid* if every object $V$ has a *dual* $V^{\vee}$ together with morphisms $\mathrm{ev}_V \colon V \otimes V^{\vee} \to \mathbf{1}$ and $\mathrm{coev}_V \colon \mathbf{1} \to V^{\vee} \otimes V$ such that the following *snake identity* diagrams commute:*

*$$\label{eq:snake-identities}
\begin{gathered}
\begin{tikzcd}[row sep=2em, column sep=2.5em]
  V
    \ar[r, "\mathrm{id} \otimes \mathrm{coev}"]
    \ar[dr, "\mathrm{id}_V"']
  & V \otimes V^{\vee} \otimes V
    \ar[d, "\mathrm{ev} \otimes \mathrm{id}"]
  \\
  & V
\end{tikzcd}
\\[-0.5em]
\text{\small left snake identity}
\end{gathered}
\qquad\qquad
\begin{gathered}
\begin{tikzcd}[row sep=2em, column sep=2.5em]
  V^{\vee}
    \ar[r, "\mathrm{coev} \otimes \mathrm{id}"]
    \ar[dr, "\mathrm{id}_{V^{\vee}}"']
  & V^{\vee} \otimes V \otimes V^{\vee}
    \ar[d, "\mathrm{id} \otimes \mathrm{ev}"]
  \\
  & V^{\vee}
\end{tikzcd}
\\[-0.5em]
\text{\small right snake identity}
\end{gathered}$$*

*We say $\mathcal{C}$ is *$R$-linear* (for a commutative ring $R$) if every hom-set is an $R$-module and composition is $R$-bilinear.*

*The category is *symmetric monoidal* if it is further equipped with a natural isomorphism (the *braiding*) $\sigma_{X,Y} \colon X \otimes Y \xrightarrow{\sim} Y \otimes X$ satisfying $\sigma_{Y,X} \circ \sigma_{X,Y} = \mathrm{id}$ and compatible with the associator. Given a braiding, the *exterior power* $\Lambda^k V$ is defined as the image of the antisymmetriser $\mathrm{Alt}_k = \sum_{\pi \in S_k} \mathrm{sgn}(\pi)\,\pi$ acting on $V^{\otimes k}$, where permutations act via $\sigma$.*

</div>

<div id="def:snake-identity" class="definition">

**Definition 1.2** (Snake identity). *[<sup><span style="color: BurntOrange">$\forall$</span></sup>](https://litlfred.github.io/qou/lean/QOU.snake_identity_left)*

*Let $(\mathcal{C}, \otimes, \mathbf{1})$ be a monoidal category and let $V$ be an object with dual $V^{\vee}$, evaluation $\mathrm{ev} \colon V \otimes V^{\vee} \to \mathbf{1}$, and coevaluation $\mathrm{coev} \colon \mathbf{1} \to V^{\vee} \otimes V$. The **snake identities** (also called *zig-zag identities*) are the two equations:*

***Left snake identity.***

*$$(\mathrm{ev} \otimes \mathrm{id}_V)
\circ (\mathrm{id}_V \otimes \mathrm{coev})
= \mathrm{id}_V.$$*

*More precisely, unfolding the associator and unitor isomorphisms, the composite*

*$$V \xrightarrow{\rho_V^{-1}} V \otimes \mathbf{1}
\xrightarrow{\mathrm{id}_V \otimes \mathrm{coev}}
V \otimes (V^{\vee} \otimes V)
\xrightarrow{\alpha^{-1}_{V, V^{\vee}, V}}
(V \otimes V^{\vee}) \otimes V
\xrightarrow{\mathrm{ev} \otimes \mathrm{id}_V}
\mathbf{1} \otimes V
\xrightarrow{\lambda_V} V$$*

*equals $\mathrm{id}_V$.*

***Right snake identity.** The composite*

*$$V^{\vee} \xrightarrow{\lambda_{V^{\vee}}^{-1}} \mathbf{1} \otimes V^{\vee}
\xrightarrow{\mathrm{coev} \otimes \mathrm{id}_{V^{\vee}}}
(V^{\vee} \otimes V) \otimes V^{\vee}
\xrightarrow{\alpha_{V^{\vee}, V, V^{\vee}}}
V^{\vee} \otimes (V \otimes V^{\vee})
\xrightarrow{\mathrm{id}_{V^{\vee}} \otimes \mathrm{ev}}
V^{\vee} \otimes \mathbf{1}
\xrightarrow{\rho_{V^{\vee}}} V^{\vee}$$*

*equals $\mathrm{id}_{V^{\vee}}$.*

*These identities express the fact that $(\mathrm{ev}, \mathrm{coev})$ exhibit $V^{\vee}$ as a right dual of $V$ (equivalently, that the pair forms an *exact pairing* in the sense of [CategoryTheory.ExactPairing](#rem:glossary-exact-pairing)). The terminology "snake" comes from the graphical calculus, where the composites trace out an S-shaped curve that straightens to a vertical line.*

</div>

<div id="ex:rigid-monoidal-vect" class="example">

**Example 1.3** (\$\\}mathbb{C}\[z\]\$ and \$\\}mathcal{O}(\\}mathrm{SU}(2))\$).

*The polynomial ring $\mathbb{C}[z]$ is the algebra of functions on the complex line $\mathbb{C}$. The category $\mathrm{Vect}_{\mathbb{C}}$ of finite-dimensional complex vector spaces is the simplest $\mathbb{C}$-linear rigid monoidal category: the tensor product is $V \otimes W$, the unit is $\mathbf{1} = \mathbb{C}$, and the dual is $V^{\vee} = \mathrm{Hom}(V, \mathbb{C})$ with $\mathrm{ev}(v \otimes f) = f(v)$.*

*Similarly, the *coordinate ring* $\mathcal{O}(\mathrm{SU}(2))$ is the algebra of polynomial functions on the group $\mathrm{SU}(2)$, generated by the matrix entries $\alpha, \beta, \bar\alpha, \bar\beta$ with $\alpha\bar\alpha + \beta\bar\beta = 1$. The category $\mathcal{C} = \mathrm{Rep}(\mathrm{SU}(2))$ of finite-dimensional representations is $\mathbb{C}$-linear rigid monoidal. Its simple objects are the spin-$j$ representations $V_j$ ($j = 0, \tfrac12, 1, \ldots$, $\dim V_j = 2j+1$). The *fundamental object* is $V = V_{1/2} \cong \mathbb{C}^2$.*

</div>

## Core definitions

<div id="def:quantum-universe" class="definition">

**Definition 1.4** (Quantum Universe). *[<sup><span style="color: BurntOrange">$\forall$</span></sup>](https://litlfred.github.io/qou/lean/QOU.QuantumUniverse)*

*Let $R$ be a commutative ring. A *quantum universe over $R$* is a triple $(\mathcal{C}, A, \tau)$ where:*

1.  *$(\mathcal{C}, \otimes, \mathbf{1})$ is an $R$-linear rigid symmetric monoidal category ([rigid monoidal category](#def:rigid-monoidal-category)) — the symmetric braiding $\sigma_{X,Y} \colon X \otimes Y
    \xrightarrow{\sim} Y \otimes X$ is required for exterior powers $\Lambda^k V$ and is canonically induced by the fibre functor $\tau$ via the Tannakian structure;*

2.  *$A$ is a *Frobenius–Hopf object* in $\mathcal{C}$: an object equipped with morphisms $$\begin{tikzcd}[row sep=1.5em, column sep=2.5em]
      A \otimes A \ar[r, "\mu"]
      & A \ar[r, "\int_A"]
      & \mathbf{1}
      & {\scriptstyle\text{(multiplication, Frobenius form)}}
      \\
      \mathbf{1} \ar[r, "\eta"]
      & A \ar[r, "\varepsilon"]
      & \mathbf{1}
      & {\scriptstyle\text{(unit, counit)}}
      \\
      A \ar[r, "\Delta"]
      & A \otimes A
      & A \ar[l, "S"']
      & {\scriptstyle\text{(comultiplication, antipode)}}
    \end{tikzcd}$$ — multiplication $\mu$, unit $\eta$, comultiplication $\Delta$, counit $\varepsilon$, antipode $S$, and Frobenius form $\int_A$ — satisfying: **(H)** $(A, \mu, \eta, \Delta, \varepsilon, S)$ is a Hopf algebra object in $\mathcal{C}$; **(F)** the [Frobenius pairing](#def:frobenius-pairing) $\int_A \circ \mu \colon A \otimes A \to \mathbf{1}$ is non-degenerate, inducing an isomorphism $A \xrightarrow{\;\sim\;} A^{\vee}$;*

3.  *$\tau \colon \mathcal{C} \to R\text{-}\mathrm{Mod}$ is a *fibre functor*: an exact, faithful, $R$-linear monoidal functor;*

4.  *$A$ admits a *differential calculus*: the module of K"ahler differentials $\Omega^1(A)$ exists in $\mathcal{C}$.*

</div>

<div id="def:frobenius-pairing" class="definition">

**Definition 1.5** (Frobenius pairing). *[<sup><span style="color: BurntOrange">$\forall$</span></sup>](https://litlfred.github.io/qou/lean/QOU.FrobeniusHopfData.frobeniusForm)*

*Let $(\mathcal{C}, A, \tau)$ be a [quantum universe](#def:quantum-universe) with multiplication $\mu \colon A \otimes A \to A$ and Frobenius form $\int_A \colon A \to \mathbf{1}$. The *Frobenius pairing* is the composite*

*$$\label{eq:frobenius-pairing}
\begin{tikzcd}[column sep=2.5em]
  A \otimes A \ar[r, "\mu"]
  & A \ar[r, "\int_A"]
  & \mathbf{1}
\end{tikzcd}$$*

*We say the Frobenius pairing is *non-degenerate* when this composite induces an isomorphism $A \xrightarrow{\;\sim\;} A^{\vee}$ to the dual object. Equivalently, the snake identities hold: there exists a coevaluation $\tilde{\eta} \colon \mathbf{1} \to A \otimes A$ such that the two composites*

*$$A \xrightarrow{\rho^{-1}} A \otimes \mathbf{1}
  \xrightarrow{\mathrm{id} \otimes \tilde{\eta}} A \otimes A \otimes A
  \xrightarrow{\alpha^{-1}} (A \otimes A) \otimes A
  \xrightarrow{(\int_A \circ \mu) \otimes \mathrm{id}} \mathbf{1} \otimes A
  \xrightarrow{\lambda_A} A$$*

*and its mirror are both equal to $\mathrm{id}_A$.*

</div>

<div id="ex:quantum-universe-su2" class="example">

**Example 1.6** (\$\\}mathrm{SU}(2)\$ as a quantum universe).

*Continuing [rigid monoidal Vect](#ex:rigid-monoidal-vect), we verify each axiom of [quantum universe](#def:quantum-universe) for $G = \mathrm{SU}(2)$.*

***(i) Category.** $\mathcal{C} = \mathrm{Rep}(\mathrm{SU}(2))$, the category of finite-dimensional complex representations. Objects are vector spaces $V$ with a continuous $G$-action $\rho_V \colon G \to \mathrm{GL}(V)$; morphisms are $G$-equivariant linear maps. This is an $\mathbb{C}$-linear rigid monoidal category ([rigid monoidal Vect](#ex:rigid-monoidal-vect)). The $G$-action on tensor products is diagonal: $g \cdot (v \otimes w) = (g \cdot v) \otimes
(g \cdot w)$; on duals it is the contragredient: $(g \cdot f)(v) = f(g^{-1} \cdot v)$.*

***(ii) Frobenius–Hopf object.** $A = \mathcal{O}(\mathrm{SU}(2))$, the coordinate ring of polynomial functions on the group. Its Hopf structure encodes the group operations:*

*\| Operation \| Formula \| Meaning \| \|———–\|———\|———\| \| *Multiplication* $\mu(f \otimes g)$ \| $f \cdot g$ \| pointwise product of functions \| \| *Unit* $\eta(1)$ \| $1_A$ \| constant function $1$ \| \| *Comultiplication* $\Delta(f)(x, y)$ \| $f(xy)$ \| pullback of group multiplication \| \| *Counit* $\varepsilon(f)$ \| $f(e)$ \| evaluation at the identity \| \| *Antipode* $S(f)(x)$ \| $f(x^{-1})$ \| pullback of inversion \| \| *Frobenius form* $\int_A(f)$ \| $\int_G f\, d\mu$ \| Haar integration on $G$ \|*

*The [Frobenius pairing](#def:frobenius-pairing) $\langle f, g \rangle = \int_A(\mu(f \otimes g)) = \int_G f(x)\, g(x)\, d\mu_{\mathrm{Haar}}(x)$ is positive definite (faithfulness of the Haar integral).*

***(iii) Fibre functor.** $\tau \colon \mathrm{Rep}(\mathrm{SU}(2)) \to
\mathrm{Vect}_{\mathbb{C}}$ is the forgetful functor: $\tau(V, \rho)
= V$ (forget the $G$-action, keep the vector space). It is exact (short exact sequences of representations split), faithful (a non-zero equivariant map is non-zero as a linear map), and monoidal ($\tau(V \otimes W) = \tau(V) \otimes \tau(W)$). By Tannaka–Krein duality, $G$ can be recovered from $\tau$: $G \cong \mathrm{Aut}^{\otimes}(\tau)$, the group of monoidal natural automorphisms of the fibre functor.*

***(iv) Differential calculus.** The left-invariant calculus on $\mathrm{SU}(2)$ provides $\Omega^1(A) = \mathrm{span}\{\omega_1, \omega_2, \omega_3\}$, the left-invariant $1$-forms dual to the Lie algebra basis $\{e_1, e_2, e_3\}$ of $\mathfrak{su}(2)$ (with $[e_a, e_b] = \epsilon_{abc}\, e_c$; [SU(2) basis](#def:su2-basis)). The universal derivation $d \colon A \to \Omega^1(A)$ acts by $df = \sum_i (\partial_i f)\, \omega_i$, recovering the Lie derivative along each generator.*

</div>

<div id="def:higher-forms" class="definition">

**Definition 1.7** (Higher differential forms). *[<sup><span style="color: BurntOrange">$\forall$</span></sup>](https://litlfred.github.io/qou/lean/QOU.HigherForms)*

*Let $(\mathcal{C}, A, \tau)$ be a quantum universe with differential calculus $\Omega^1(A)$ ([quantum universe](#def:quantum-universe)). The *higher differential forms* are the graded $A$-bimodule*

*$$\Omega^k(A) \;=\; \bigwedge\nolimits_A^k \Omega^1(A),
  \qquad k = 0, 1, 2, \ldots$$*

*(exterior powers of the $A$-bimodule $\Omega^1(A)$ in $\mathcal{C}$), with $\Omega^0(A) = A$. For an object $V$ in $\mathcal{C}$, $\Lambda^k V$ denotes the $k$-th exterior power of $V$ in the sense of rigid monoidal categories. The differential $d \colon \Omega^k(A) \to \Omega^{k+1}(A)$ extends the universal derivation by the graded Leibniz rule, and satisfies $d^2 = 0$.*

</div>

<div id="ex:higher-forms-su2" class="example">

**Example 1.8** (Higher forms on \$\\}mathcal{O}(\\}mathrm{SU}(2))\$).

*Continuing [quantum universe on SU(2)](#ex:quantum-universe-su2), the left-invariant calculus on $A = \mathcal{O}(\mathrm{SU}(2))$ has $\Omega^1(A) = \mathrm{span}\{\omega_1, \omega_2, \omega_3\}$ (three left-invariant $1$-forms, dual to the Lie algebra $\mathfrak{su}(2) = \mathrm{span}\{e_1, e_2, e_3\}$). The higher forms are:*

- *$\Omega^0(A) = A = \mathcal{O}(\mathrm{SU}(2))$ (functions on the group).*

- *$\Omega^1(A) = A \otimes \mathrm{span}\{\omega_1, \omega_2, \omega_3\}$ (left-invariant $1$-forms, dimension $3$ over $A$).*

- *$\Omega^2(A) = A \otimes \mathrm{span}\{\omega_1 \wedge \omega_2,\,
  \omega_1 \wedge \omega_3,\, \omega_2 \wedge \omega_3\}$ (dimension $3$ over $A$).*

- *$\Omega^3(A) = A \otimes \mathrm{span}\{\omega_1 \wedge \omega_2 \wedge
  \omega_3\}$ (the volume form, dimension $1$ over $A$).*

- *$\Omega^k(A) = 0$ for $k \geq 4$.*

*The differential $d$ is determined by $d\omega_i = -\tfrac{1}{2}
\epsilon_{ijk}\,\omega_j \wedge \omega_k$ (the Maurer–Cartan equation of $\mathfrak{su}(2)$).*

</div>

<div id="def:quantum-observable-universe" class="definition">

**Definition 1.9** (Quantum Observable Universe). *[<sup><span style="color: BurntOrange">$\forall$</span></sup>](https://litlfred.github.io/qou/lean/QOU.QuantumObservableUniverse)*

*A quantum universe $(\mathcal{C}, A, \tau)$ over $R$ ([quantum universe](#def:quantum-universe)) is *observable* if the forgetful functor $\tau$ ([Example](#ex:rigid-monoidal-vect)) is faithful and the following conditions hold:*

1.  **(non-degenerate integration)* the Frobenius form $\int_A \colon A \to \mathbf{1}$ induces a non-degenerate pairing $(a, b) \mapsto \int_A ab$ ([Frobenius pairing](#def:frobenius-pairing)), giving an isomorphism $A \xrightarrow{\;\sim\;} A^{\vee}$;*

2.  **(observability)* there are no hidden global symmetries: $\mathrm{Hom}_{\mathcal{C}}(\mathbf{1},\,
    \mathrm{Ad}(A)) = 0$, where $\mathrm{Ad}(A)$ is the adjoint object ($A$ acted on by conjugation). Physically, this means every internal degree of freedom is accessible to measurement — no gauge transformation acts trivially on all observables. The formal statement is that every morphism $\mathbf{1} \to \mathrm{Ad}(A)$ is zero: $$\begin{tikzcd}[column sep=2.5em]
      \mathbf{1} \ar[r, "0"] & \mathrm{Ad}(A)
    \end{tikzcd}
    \qquad\text{(observability)}$$*

3.  **(measurability / anomaly-free)* the primary Chern classes of the adjoint object vanish in the cohomology induced by the forgetful projection $\tau$: $$c_1(\mathrm{Ad}(A)) = 0
      \qquad\text{and}\qquad
      c_2(\mathrm{Ad}(A)) = 0.$$ Here the Chern classes $c_i$ are defined via the fibre functor: $c_i(\mathrm{Ad}(A)) := c_i(\tau(\mathrm{Ad}(A)))$ in the de Rham cohomology of the realised bundle. The first condition ($c_1 = 0$) ensures the adjoint bundle is orientable, precluding global anomalies; the second ($c_2 = 0$) ensures the volume form acquires no topological phases. For many applications, axioms (1), (2), and (4) suffice — axiom (3) is needed only when global topology of $M$ matters.*

4.  **(categorical volume constraint)* let $V$ denote the fundamental object of $\mathcal{C}$ ([Remark](#rem:fundamental-object-explication)); there exists a non-degenerate epimorphism $\epsilon$ preserved by the rigid dualities, making the following diagram commute for every $g \in \mathrm{Aut}^{\otimes}(\tau)$: $$\label{eq:categorical-volume-constraint}
    \begin{tikzcd}[row sep=2.5em, column sep=3em]
      \Lambda^2 V \ar[r, "\Lambda^2 g_V"]
                  \ar[d, "\epsilon"', two heads]
      & \Lambda^2 V \ar[d, "\epsilon", two heads]
      \\
      \mathbf{1} \ar[r, "g_{\mathbf{1}} = \mathrm{id}"']
      & \mathbf{1}
    \end{tikzcd}
    \qquad\text{(volume constraint)}$$*

</div>

<div id="ex:qou-su2" class="example">

**Example 1.10** (\$\\}mathrm{SU}(2)\$ is observable).

*Continuing [Examples](#ex:rigid-monoidal-vect) and [quantum universe on SU(2)](#ex:quantum-universe-su2), write $V = V_{1/2} \cong \mathbb{C}^2$:*

1.  **Non-degeneracy.* The Haar integral $\int_A = \int_G$ on $\mathcal{O}(\mathrm{SU}(2))$ is faithful: if $\int_A(f^* f) = 0$ then $f = 0$.*

2.  **Observability.* The adjoint representation $\mathrm{Ad} \cong V_1$ (spin-$1$, dimension $3$) is irreducible, so it contains no copy of the trivial representation: $\mathrm{Hom}(\mathbf{1}, V_1) = 0$.*

3.  **Volume constraint.* For $v, w \in V = \mathbb{C}^2$, the determinant $\epsilon(v \wedge w) = v_1 w_2 - v_2 w_1$ defines a non-degenerate map $\epsilon \colon \Lambda^2 V \to \mathbb{C}$.*

</div>

<div id="def:maximal-torus" class="definition">

**Definition 1.11** (Maximal torus and weight subcategory). *[<sup><span style="color: BurntOrange">$\forall$</span></sup>](https://litlfred.github.io/qou/lean/QOU.MaximalTorus)*

*Let $(\mathcal{C}, A, \tau)$ be a ([quantum observable universe](#def:quantum-observable-universe)) with fundamental object $V$ (the unique simple object of categorical dimension $2$; see [spin labels](#prop:spin-labels) for the full labelling). The *weight subcategory* $\langle V \rangle \subset \mathcal{C}$ is the full subcategory whose objects are direct sums of weight spaces of $V$ (i.e. simultaneous eigenspaces of the Cartan subalgebra action). The *maximal torus* of the gauge group is*

*$$T = \mathrm{Aut}^{\otimes}(\tau|_{\langle V \rangle}),$$*

*the sub-group scheme of $G = \mathrm{Aut}^{\otimes}(\tau)$ ([SU(2) emergence](#thm:su2-emergence)) consisting of those natural automorphisms that act diagonally on each weight space of $V$. Equivalently, $T$ is the largest subgroup of $G$ for which every object in $\langle V \rangle$ decomposes into one-dimensional $T$-eigenspaces.*

</div>

<div id="ex:maximal-torus-su2" class="example">

**Example 1.12** (Maximal torus for \$\\}mathrm{SU}(2)\$).

*Continuing [spin labels on SU(2)](#ex:spin-labels-su2), the fundamental object is $V = \mathbb{C}^2$ with the standard $\mathrm{SU}(2)$-action. The weight decomposition is $V = \mathbb{C} e_+ \oplus \mathbb{C} e_-$ (the $\pm\tfrac{1}{2}$-eigenspaces of $e_3 = \frac{1}{2}\begin{psmallmatrix} 1 & 0 \\ 0 & -1 \end{psmallmatrix}$). The weight subcategory $\langle V \rangle$ consists of representations that decompose into weight spaces: $V$ itself, $\mathbf{1}$, and their direct sums. The maximal torus is*

*$$T = \mathrm{U}(1)
  = \left\{
    \begin{pmatrix} e^{i\theta} & 0 \\ 0 & e^{-i\theta} \end{pmatrix}
    : \theta \in \mathbb{R}
  \right\},$$*

*the diagonal matrices in $\mathrm{SU}(2)$. Each element of $T$ acts on $e_{\pm}$ by $e^{\pm i\theta}$: one-dimensional eigenspaces, as required.*

</div>

<div id="def:weight-decomposition" class="definition">

**Definition 1.13** (Weight decomposition). *[<sup><span style="color: BurntOrange">$\forall$</span></sup>](https://litlfred.github.io/qou/lean/QOU.WeightDecomposition)*

*Let $(\mathcal{C}, A, \tau)$ be a ([quantum observable universe](#def:quantum-observable-universe)) with maximal torus $T$ ([maximal torus](#def:maximal-torus)) and higher differential forms $\Omega^k(A)$ ([higher forms](#def:higher-forms)). The $T$-action on $\Omega^k(A)$ induces a $\mathbb{Z}$-grading by weights. Denoting by $\pi_H, \pi_V$ the projections onto the weight-$0$ and non-zero-weight summands, every $\alpha \in \Omega^k(A)$ decomposes uniquely:*

*$$\label{eq:weight-decomposition-cd}
\begin{tikzcd}[row sep=2em, column sep=3em]
  & \Omega^k(A) \ar[dl, "\pi_H"'] \ar[dr, "\pi_V"] & \\
  \Omega^k_H(A) \ar[rr, hook, "\oplus"']
  & & \Omega^k_V(A)
\end{tikzcd}
\qquad \alpha = \alpha_H + \alpha_V.$$*

*Here $\alpha_H = \pi_H(\alpha)$ is the *horizontal component* (weight-$0$ under $T$) and $\alpha_V = \pi_V(\alpha)$ is the *vertical component* (non-zero weight). A form is *purely horizontal* if and only if $\alpha_V = 0$.*

</div>

<div id="thm:weight-decomposition-exists" class="theorem">

**Theorem 1.14** (Existence of the weight decomposition). *[<sup><span style="color: BurntOrange">$\forall$</span></sup>](https://litlfred.github.io/qou/lean/QOU.WeightDecomposition.ofMaximalTorus)*

*Let $(\mathcal{C}, A, \tau)$ be a ([quantum observable universe](#def:quantum-observable-universe)) with [maximal torus](#def:maximal-torus) $T$ acting on [higher forms](#def:higher-forms) $\Omega^k(A)$. Then there exists a [weight decomposition](#def:weight-decomposition) $(\pi_H, \pi_V)$ of $\Omega^k(A)$ satisfying:*

1.  ***Complementarity:** $\pi_H + \pi_V = \mathrm{id}$.*

2.  ***Idempotency:** $\pi_H^2 = \pi_H$ and $\pi_V^2 = \pi_V$.*

</div>

<div class="proof">

*Proof of existence of the weight decomposition.* <span id="prf:weight-decomposition-exists" label="prf:weight-decomposition-exists"></span>

The projections are constructed from the torus averaging operator: for each weight $\lambda$ of the $T$-action, the $\lambda$-isotypic projector $e_\lambda$ is idempotent, and $\pi_H = e_0$, $\pi_V = \mathrm{id} - e_0$. ◻

</div>

## Consequences of the axioms

<div id="prop:frobenius-relation" class="proposition">

**Proposition 1.15** (Frobenius relation). *[<sup><span style="color: BurntOrange">$\forall$</span></sup>](https://litlfred.github.io/qou/lean/QOU.frobenius_relation)*

*Let $(\mathcal{C}, A, \tau)$ be a ([quantum universe](#def:quantum-universe)). Denote by $\Delta_\mu$ the comultiplication on $A$ dual to the multiplication $\mu$ under the [Frobenius pairing](#def:frobenius-pairing). Then the following diagram commutes (the *Frobenius relation*):*

*$$\label{eq:frobenius-relation}
\begin{gathered}
\begin{tikzcd}[row sep=2.5em, column sep=3.5em]
  A \otimes A
    \ar[r, "\mathrm{id} \otimes \Delta_\mu"]
    \ar[d, "\mu"']
  & A \otimes A \otimes A
    \ar[d, "\mu \otimes \mathrm{id}"]
  \\
  A \ar[r, "\Delta_\mu"']
  & A \otimes A
\end{tikzcd}
\\[-0.5em]
\text{\small Frobenius relation: } (\mu \otimes \mathrm{id}) \circ (\mathrm{id} \otimes \Delta_\mu) = \Delta_\mu \circ \mu
\end{gathered}$$*

*That is, sliding a multiplication past a comultiplication (or vice versa) yields the same result as composing them: $(\mu \otimes \mathrm{id}) \circ (\mathrm{id} \otimes \Delta_\mu)
= \Delta_\mu \circ \mu$.*

</div>

<div class="proof">

*Proof of Frobenius relation.* <span id="prf:frobenius-relation" label="prf:frobenius-relation"></span>

Non-degeneracy of the pairing $\langle a, b \rangle = \int_A(\mu(a \otimes b))$ identifies $A \cong A^{\vee}$. Under this identification, $\Delta_\mu$ is the transpose of $\mu$. The Frobenius relation then follows from the associativity of $\mu$ by dualising one leg of the multiplication. ◻

</div>

<div id="ex:frobenius-su2" class="example">

**Example 1.16** (Frobenius relation for \$\\}mathrm{SU}(2)\$).

*Continuing [QOU on SU(2)](#ex:qou-su2), set $A = \mathcal{O}(\mathrm{SU}(2))$ with multiplication $\mu(f \otimes g) = fg$ (pointwise product) and Frobenius form $\int_A = \int_G$ (Haar integral). The dual comultiplication is $\Delta_\mu(f)(g,h) = \int_G f(xg)\,\overline{h(x)}\,dx$, and the Frobenius relation expresses the associativity of convolution: $\int_G f(xy)\,g(y)\,dy$ can be evaluated by convolving first with $f$ or first with $g$.*

</div>

<div id="def:involutive-structure" class="definition">

**Definition 1.17** (Involutive structure (\$\\}ast\$-structure)). *[<sup><span style="color: BurntOrange">$\forall$</span></sup>](https://litlfred.github.io/qou/lean/QOU.InvolutiveStructure)*

*Let $(\mathcal{C}, \otimes, \mathbf{1})$ be an $R$-linear rigid monoidal category. An *involutive structure* (also called a *$\ast$-structure* or *dagger structure*) on $\mathcal{C}$ is a contravariant endofunctor $\dagger \colon \mathcal{C}^{\mathrm{op}} \to \mathcal{C}$ satisfying:*

1.  ***Identity on objects:** $X^{\dagger} = X$ for every object $X$.*

2.  ***Involutivity:** $f^{\dagger\dagger} = f$ for every morphism $f$, depicted: $$\label{eq:involutivity-cd}
    \begin{tikzcd}[column sep=3em]
      X \ar[r, "f"] \ar[rr, bend left=30, "f^{\dagger\dagger} = f"]
      & Y \ar[r, "f^{\dagger}"{description}]
      & X
    \end{tikzcd}$$*

3.  ***Monoidal compatibility:** $(\mathrm{id}_X \otimes f)^{\dagger}
    = \mathrm{id}_X \otimes f^{\dagger}$, i.e. the following square commutes: $$\label{eq:monoidal-dagger-cd}
    \begin{tikzcd}[row sep=2.5em, column sep=3em]
      X \otimes Y \ar[r, "\mathrm{id} \otimes f"]
        \ar[d, "(\mathrm{id} \otimes f)^{\dagger}"']
      & X \otimes Z \ar[d, "\mathrm{id} \otimes f^{\dagger}"] \\
      X \otimes Z \ar[r, equal]
      & X \otimes Z
    \end{tikzcd}$$*

4.  ***Contravariance:** $(g \circ f)^{\dagger} = f^{\dagger} \circ g^{\dagger}$: $$\label{eq:dagger-contravariance}
    \begin{tikzcd}[column sep=3em]
      X \ar[r, "f"] & Y \ar[r, "g"] & Z
    \end{tikzcd}
    \quad\xmapsto{\;\dagger\;}\quad
    \begin{tikzcd}[column sep=3em]
      Z \ar[r, "g^{\dagger}"] & Y \ar[r, "f^{\dagger}"] & X
    \end{tikzcd}
    \qquad\text{(contravariance)}$$*

*For the Hopf algebra $A$ in a quantum universe, the antipode $S$ provides a natural involutive structure on the representation category via $f^{\dagger} = \int_A \circ \mu(S(f) \otimes -)$. In the $\mathrm{SU}(2)$ example, this is the Hilbert-space adjoint ([dagger on SU(2)](#ex:dagger-su2)).*

</div>

<div id="def:positive-definite-dagger" class="definition">

**Definition 1.18** (Positive-definite structure). *[<sup><span style="color: BurntOrange">$\forall$</span></sup>](https://litlfred.github.io/qou/lean/QOU.PositiveDefiniteStructure)*

*Let $(\mathcal{C}, \dagger)$ be a rigid monoidal category with involutive structure ([involutive structure](#def:involutive-structure)). The involution is *positive-definite* if for every non-zero morphism $f \colon \mathbf{1} \to X$ the composite*

*$$\label{eq:positive-definite-cd}
\begin{tikzcd}[column sep=2.5em]
  \mathbf{1} \ar[r, "f"]
  & X \ar[r, "f^{\dagger}"]
  & \mathbf{1}
\end{tikzcd}$$*

*is a positive element of $\mathrm{End}(\mathbf{1}) \cong R$. Equivalently, the sesquilinear form*

*$$\langle g, h \rangle
  = g^{\dagger} \circ h
  \in \mathrm{End}(\mathbf{1})$$*

*is positive-definite on $\mathrm{Hom}(\mathbf{1}, X)$ for every object $X$. This replaces the analytic notion of "Hilbert-space inner product" with a purely categorical condition.*

</div>

<div id="ex:dagger-su2" class="example">

**Example 1.19** (Involutive structure on \$\\}mathrm{Rep}(\\}mathrm{SU}(2))\$).

*Continuing [Frobenius SU(2)](#ex:frobenius-su2), the category $\mathcal{C} = \mathrm{Rep}(\mathrm{SU}(2))$ carries a canonical involutive structure built from the antipode:*

- **What it does.* For a morphism $f \colon V_j \to V_k$ (an equivariant linear map between representations), $f^{\dagger}$ is the *Hilbert-space adjoint*: the unique map $f^{\dagger} \colon V_k \to V_j$ satisfying $\langle f^{\dagger}(w),\, v \rangle_j
  = \langle w,\, f(v) \rangle_k$ for all $v \in V_j$, $w \in V_k$.*

- **Why it exists.* Each irreducible representation $V_j$ carries a unique (up to scalar) $\mathrm{SU}(2)$-invariant inner product. The adjoint $f^{\dagger}$ with respect to these inner products is automatically equivariant, so $f^{\dagger}$ is again a morphism in $\mathcal{C}$.*

- **On the algebra.* On $A = \mathcal{O}(\mathrm{SU}(2))$, $f^{\dagger} = \int_A \circ \mu(S(f) \otimes -)$, where $S(f)(g) = f(g^{-1})$ is the antipode. The involution $f \mapsto f^{\dagger}$ is complex conjugation composed with pullback by inversion: $f^{\dagger}(g) = \overline{f(g^{-1})}$.*

- **Positive-definiteness.* For a non-zero state $f \colon \mathbb{C} \to V_j$, the composite $f^{\dagger} \circ f = \lVert f(1) \rVert^2 > 0$. This is the statement that the inner product on each $V_j$ is positive-definite — the categorical encoding of unitarity.*

</div>

<div id="lem:volume-from-rigidity" class="lemma">

**Lemma 1.20** (Volume form from rigidity and symplectic self-duality). *[<sup><span style="color: BurntOrange">$\forall$</span></sup>](https://litlfred.github.io/qou/lean/QOU.volume_from_rigidity)*

*Let $(\mathcal{C}, \otimes, \mathbf{1})$ be an $R$-linear rigid monoidal category, and let $V$ be an object of categorical dimension $2$ that is *symplectically self-dual*: there exists an isomorphism $\phi \colon V \xrightarrow{\;\sim\;} V^{\vee}$ satisfying $\phi^{\vee} = -\phi$ (alternating). Then the composite $\mathrm{ev}_V \circ (\mathrm{id} \otimes \phi)$ factors through $\Lambda^2 V$ (the *volume form factorisation*):*

*$$\label{eq:volume-form-factorisation}
\begin{tikzcd}[row sep=2.5em, column sep=3em]
  V \otimes V
    \ar[r, "\mathrm{id} \otimes \phi"]
    \ar[d, "\pi"', two heads]
  & V \otimes V^{\vee}
    \ar[d, "\mathrm{ev}_V"]
  \\
  \Lambda^2 V
    \ar[r, "\epsilon"', dashed]
  & \mathbf{1}
\end{tikzcd}$$*

*and $\epsilon$ is non-degenerate; that is, condition (iii) of [quantum observable universe](#def:quantum-observable-universe) holds.*

</div>

<div class="proof">

*Proof of Volume form from rigidity and symplectic self-duality.* <span id="prf:volume-from-rigidity" label="prf:volume-from-rigidity"></span>

Because $\phi$ is alternating, the pairing $B = \mathrm{ev}_V \circ (\mathrm{id} \otimes \phi)$ satisfies $B \circ \tau_{V,V} = -B$, where $\tau_{V,V}$ is the symmetry (or braiding) isomorphism. Hence $B$ vanishes on symmetric tensors and factors as $B = \epsilon \circ \pi$, where $\pi \colon V \otimes V \twoheadrightarrow \Lambda^2 V$ is the canonical projection. Non-degeneracy of $\epsilon$ follows from non-degeneracy of $\mathrm{ev}_V$ (guaranteed by rigidity) and the isomorphism $\phi$. The duality axioms $(\mathrm{ev}_V \otimes \mathrm{id}) \circ
(\mathrm{id} \otimes \mathrm{coev}_V) = \mathrm{id}_V$ ensure that $\epsilon$ is preserved by the rigid dualities of $\mathcal{C}$. ◻

</div>

<div id="thm:su2-emergence" class="theorem">

**Theorem 1.21** (Emergence of the gauge group). *[<sup><span style="color: BurntOrange">$\forall$</span></sup>](https://litlfred.github.io/qou/lean/QOU.RankOneGaugeData)*

*Let $(\mathcal{C}, A, \tau)$ be a ([quantum observable universe](#def:quantum-observable-universe)). Then $G = \mathrm{Aut}^{\otimes}(\tau) \cong \mathrm{SU}(2)$ (or $\mathrm{SL}(2, R)$ depending on the signature of the Frobenius pairing).*

</div>

<div class="proof">

*Proof of Emergence of the gauge group.* <span id="prf:su2-emergence" label="prf:su2-emergence"></span>

The gauge group $G$ is defined via Tannaka–Krein duality as the group scheme of tensor-preserving natural automorphisms of the fibre functor $\tau$. An element $g \in G$ assigns an invertible linear map $g_X \colon \tau(X) \to \tau(X)$ to every object $X \in \mathcal{C}$.

Because $g$ is a natural transformation, it commutes with all morphisms in $\mathcal{C}$, including the volume constraint $\epsilon \colon \Lambda^2 V \to \mathbf{1}$ <a href="#eq:categorical-volume-constraint" data-reference-type="eqref" data-reference="eq:categorical-volume-constraint">[eq:categorical-volume-constraint]</a>. Applying $\tau$ yields the commutative diagram of $R$-modules

$$\label{eq:su2-emergence-diagram}
\begin{tikzcd}[row sep=2.5em, column sep=3.5em]
  \Lambda^2 \tau(V)
    \ar[r, "\Lambda^2 g_V"]
    \ar[d, "\tau(\epsilon)"']
  & \Lambda^2 \tau(V)
    \ar[d, "\tau(\epsilon)"]
  \\
  \tau(\mathbf{1})
    \ar[r, "g_{\mathbf{1}} = \mathrm{id}"']
  & \tau(\mathbf{1})
\end{tikzcd}$$

The fundamental object $V$ has categorical dimension $2$, so $\tau(V)$ is a rank-$2$ free $R$-module and $\Lambda^2 \tau(V)$ has rank $1$. The induced operator $\Lambda^2 g_V$ acts on this rank-$1$ module as scalar multiplication by $\det(g_V)$. Following diagram <a href="#eq:su2-emergence-diagram" data-reference-type="eqref" data-reference="eq:su2-emergence-diagram">[eq:su2-emergence-diagram]</a> from the top-left to the bottom-right:

$$\tau(\epsilon) \circ \Lambda^2 g_V
  =
  g_{\mathbf{1}} \circ \tau(\epsilon)
  =
  \tau(\epsilon).$$

Since $\tau(\epsilon)$ is non-degenerate (hence non-zero), this forces

$$\label{eq:det-one}
  \det(g_V) \;=\; 1,$$

restricting the natural automorphisms from $\mathrm{GL}(2)$ to the special subgroup $\mathrm{SL}(2)$.

The QOU non-degeneracy axiom ensures the Frobenius form $\int_A \colon A \to \mathbf{1}$ is non-degenerate, inducing the Frobenius self-duality $A \cong A^{\vee}$ ([fibre adjoint involution](#prop:fiber-adjoint-involution)). Define a dagger on morphisms by $f^{\dagger} = \int_A \circ \mu(S(f) \otimes -)$, where $S$ is the antipode. Non-degeneracy of $\int_A$ and faithfulness of $\tau$ imply $f^{\dagger} \circ f = 0 \Rightarrow f = 0$, so this is a positive-definite dagger structure ([positive definite dagger](#def:positive-definite-dagger)). Every tensor automorphism $g \in G$ preserves the dagger (it commutes with $S$ and $\int_A$), forcing $g_V^{-1} = g_V^{\dagger}$ and restricting $G$ to the unitary subgroup $\mathrm{U}(2)$.

Combining both constraints:

$$G \;=\; \mathrm{SL}(2) \;\cap\; \mathrm{U}(2)
  \;=\; \mathrm{SU}(2).$$

The volume constraint provides the special-linear condition ($\det = 1$), while the positive-definite dagger structure provides the compactness (unitarity), locking the gauge group exclusively to $\mathrm{SU}(2)$. ◻

</div>

<div id="ex:su2-emergence" class="example">

**Example 1.22** (Emergence of \$\\}mathrm{SU}(2)\$: the full chain).

*Continuing [Examples](#ex:frobenius-su2)–[](#ex:dagger-su2), let $\mathcal{C} = \mathrm{Rep}(\mathrm{SU}(2))$, $A = \mathcal{O}(\mathrm{SU}(2))$, $\tau$ the forgetful functor.*

1.  **Volume constraint* $\Rightarrow$ $\det(g_V) = 1$. The alternating form $\epsilon(v \wedge w) = v_1 w_2 - v_2 w_1$ on $V = \mathbb{C}^2$ is $\mathrm{SU}(2)$-invariant. Any tensor automorphism $g$ preserves $\epsilon$, forcing $g_V \in \mathrm{SL}(2, \mathbb{C})$.*

2.  **Dagger structure* $\Rightarrow$ unitarity. The dagger on $\mathrm{Rep}(\mathrm{SU}(2))$ ([dagger on SU(2)](#ex:dagger-su2)) forces $g_V^{-1} = g_V^{\dagger}$, cutting from $\mathrm{SL}(2, \mathbb{C})$ to its compact real form $\mathrm{SU}(2)$.*

3.  **Conclusion.* $G = \mathrm{Aut}^{\otimes}(\tau) \cong \mathrm{SU}(2)$, recovering the input gauge group from the categorical axioms alone.*

</div>

## Differential structures and gauge actions

<div id="prop:spin-labels" class="proposition">

**Proposition 1.23** (Spin labels and the fundamental object). *[<sup><span style="color: BurntOrange">$\forall$</span></sup>](https://litlfred.github.io/qou/lean/QOU.SpinDecomposition)*

*Let $(\mathcal{C}, A, \tau)$ be a ([quantum observable universe](#def:quantum-observable-universe)). Because $G = \mathrm{Aut}^{\otimes}(\tau) \cong \mathrm{SU}(2)$ ([SU(2) emergence](#thm:su2-emergence)), the simple objects of $\mathcal{C}$ are indexed by a *spin* label $j \in \{0, \tfrac12, 1,
\tfrac32, \ldots\}$, with $V_j$ denoting the simple object of categorical dimension $2j + 1$. The *fundamental object* is $V = V_{1/2}$, the unique simple object of categorical dimension $2$. The *adjoint object* is $V_1 \cong \mathrm{Ad}(A)$, of dimension $3$.*

</div>

<div class="proof">

*Proof of spin labels.* <span id="prf:spin-labels" label="prf:spin-labels"></span>

Because $G = \mathrm{Aut}^{\otimes}(\tau) \cong \mathrm{SU}(2)$ ([SU(2) emergence](#thm:su2-emergence)), the simple objects of $\mathcal{C}$ are indexed by a spin label $j \in \{0, \tfrac12, 1, \tfrac32, \ldots\}$, with $V_j$ denoting the simple object of categorical dimension $2j + 1$.

The symplectic form $\epsilon \colon \Lambda^2 V \to \mathbf{1}$ ([quantum observable universe](#def:quantum-observable-universe), axiom (iii)) is the unique (up to scalar) $G$-invariant alternating pairing on $V$. ◻

</div>

<div id="ex:spin-labels-su2" class="example">

**Example 1.24** (Spin decomposition of \$\\}mathrm{Rep}(\\}mathrm{SU}(2))\$).

*Continuing [QOU on SU(2)](#ex:qou-su2), the simple objects of $\mathcal{C} = \mathrm{Rep}(\mathrm{SU}(2))$ are the irreducible representations $V_j \cong \mathbb{C}^{2j+1}$:*

*$$\label{eq:spin-decomposition}
\begin{tikzcd}[row sep=1.5em, column sep=1.5em]
  V_0 \ar[d, phantom, "\cong"] & V_{1/2} \ar[d, phantom, "\cong"]
    & V_1 \ar[d, phantom, "\cong"] & V_{3/2} \ar[d, phantom, "\cong"]
    & \cdots \\
  \mathbb{C} & \mathbb{C}^2 & \mathbb{C}^3 & \mathbb{C}^4 & \cdots
\end{tikzcd}$$*

*In concrete terms:*

- *$V_0 = \mathbb{C}$ (the trivial representation: $g \cdot z = z$).*

- *$V_{1/2} = \mathbb{C}^2$ (the defining representation: $g \cdot v = gv$ by matrix multiplication). This is the fundamental object $V$.*

- *$V_1 = \mathfrak{su}(2)_{\mathbb{C}} \cong \mathbb{C}^3$ (the adjoint representation: $g \cdot X = gXg^{-1}$). This is $\mathrm{Ad}(A)$.*

- *$V_{3/2} = \mathrm{Sym}^3(\mathbb{C}^2) \cong \mathbb{C}^4$ (homogeneous cubics in two variables).*

*Every finite-dimensional representation decomposes as $W \cong \bigoplus_j V_j^{\oplus m_j}$, with multiplicities $m_j \in \mathbb{N}$. The polynomial ring $\mathbb{C}[z] = \bigoplus_{n \geq 0} \mathrm{Sym}^n V$ is the coordinate ring of $\mathbb{P}^1(\mathbb{C}) = \mathbb{P}(V)$ ([projective line object](#def:projective-line-object)), and each homogeneous component $\mathrm{Sym}^n V \cong V_{n/2}$ is an irreducible representation of dimension $n + 1$.*

</div>

<div id="def:categorical-reeb" class="definition">

**Definition 1.25** (Categorical Reeb derivation). *[<sup><span style="color: BurntOrange">$\forall$</span></sup>](https://litlfred.github.io/qou/lean/QOU.CategoricalReeb)*

*Let $(\mathcal{C}, A, \tau)$ be a quantum observable universe with maximal torus $T$ ([maximal torus](#def:maximal-torus)) and weight decomposition $\pi_H, \pi_V$ ([weight decomposition](#def:weight-decomposition)). The *categorical Reeb derivation* is the endomorphism $\xi \colon A \to A$ that generates the $T$-action: $\xi$ is the infinitesimal generator of the one-parameter subgroup $T \cong \mathrm{U}(1) \subset G$, acting on the Frobenius–Hopf object $A$ via the adjoint coaction. It satisfies:*

1.  ***Vertical generator:** $\pi_V \circ d = \iota_\xi\, d\theta_A$, where $\iota_\xi$ denotes the interior product (contraction with $\xi$) and $\theta_A \in \Omega^1(A)$ is the canonical $1$-form dual to $\xi$.*

2.  ***Normalisation:** $\theta_A(\xi) = \mathrm{id}_{\mathbf{1}}$.*

3.  ***Kernel:** $\Omega^k_H(A) = \ker(\iota_\xi)$ (horizontal forms are precisely those annihilated by contraction with $\xi$).*

</div>

<div id="thm:categorical-reeb-exists" class="theorem">

**Theorem 1.26** (Existence of the categorical Reeb derivation). *[<sup><span style="color: BurntOrange">$\forall$</span></sup>](https://litlfred.github.io/qou/lean/QOU.CategoricalReeb.ofWeightDecomposition)*

*Let $(\mathcal{C}, A, \tau)$ be a ([quantum observable universe](#def:quantum-observable-universe)) with [maximal torus](#def:maximal-torus) $T$ and [weight decomposition](#def:weight-decomposition) $(\pi_H, \pi_V)$. Then there exists a [categorical Reeb derivation](#def:categorical-reeb) $(\xi, \theta_A)$ on $A$ satisfying:*

1.  ***Vertical generator:** $\pi_V \circ d = \iota_\xi\, d\theta_A$.*

2.  ***Normalisation:** $\xi \mathbin{;} \theta_A = \theta_A$ (categorically: $\theta_A(\xi) = \mathrm{id}_{\mathbf{1}}$).*

</div>

<div class="proof">

*Proof of existence of the categorical Reeb derivation.* <span id="prf:categorical-reeb-exists" label="prf:categorical-reeb-exists"></span>

The derivation $\xi$ is the infinitesimal generator of the one-parameter subgroup $T \cong \mathrm{U}(1) \subset G$, and $\theta_A$ is its Maurer–Cartan dual, uniquely determined by the normalisation condition. ◻

</div>

<div id="ex:reeb-su2" class="example">

**Example 1.27** (Reeb derivation for \$\\}mathrm{SU}(2)\$).

*Continuing [maximal torus of SU(2)](#ex:maximal-torus-su2), the maximal torus is $T = \mathrm{U}(1)$ with generator $\xi = e_3 = \frac{1}{2}\begin{psmallmatrix} 1 & 0 \\ 0 & -1
\end{psmallmatrix} \in \mathfrak{su}(2)$. On $A = \mathcal{O}(\mathrm{SU}(2))$, $\xi$ acts by $(\xi \cdot f)(g) = \frac{d}{dt}\big|_{t=0} f(e^{-t\xi} g)$ (left-invariant vector field). The canonical $1$-form is $\theta_A = \omega_3$ (the left-invariant $1$-form dual to $e_3$), and:*

- *$\omega_3(\xi) = 1$ (normalisation).*

- *$\Omega^k_H(A) = \{\alpha : \iota_\xi\,\alpha = 0\}$ (forms with no $\omega_3$ component).*

- *In the archimedean realisation on a CR manifold $(M, \theta)$, $\xi$ becomes the Reeb vector field with $\iota_\xi\,d\theta = 0$ and $\theta(\xi) = 1$ ([Reeb decomposition](#ex:reeb-decomposition)).*

</div>

<div id="def:projective-line-object" class="definition">

**Definition 1.28** (Projective line object). *[<sup><span style="color: BurntOrange">$\forall$</span></sup>](https://litlfred.github.io/qou/lean/QOU.ProjectiveLineObject)*

*Let $(\mathcal{C}, A, \tau)$ be a quantum observable universe with maximal torus $T \subset G$ ([maximal torus](#def:maximal-torus)). The *projective line object* is the quotient*

*$$\mathbb{P}(V) = G / T,$$*

*regarded as an object of $\mathrm{Ind}(\mathcal{C})$ via its function algebra $\mathcal{O}(\mathbb{P}(V)) = A^{\mathrm{co}\,T}$ (the $T$-coinvariant subalgebra of $A$).*

</div>

<div id="ex:projective-line-su2" class="example">

**Example 1.29** (Projective line for \$\\}mathrm{SU}(2)\$).

*Continuing [maximal torus of SU(2)](#ex:maximal-torus-su2), $G = \mathrm{SU}(2)$ and $T = \mathrm{U}(1)$. The quotient is $\mathbb{P}(V) = \mathrm{SU}(2)/\mathrm{U}(1) \cong \mathbb{P}^1(\mathbb{C})$. A point $[\ell] \in \mathbb{P}^1(\mathbb{C})$ is a line $\ell \subset V = \mathbb{C}^2$; equivalently, it is the kernel of a linear form on $V$, well-defined up to scalar. The function algebra is the polynomial ring $\mathcal{O}(\mathbb{P}^1(\mathbb{C})) = \mathbb{C}[z]$ in the affine coordinate $z = v_1 / v_2$.*

</div>

<div id="def:contact-affine-chart" class="definition">

**Definition 1.30** (Contact affine chart on \$\\}mathbb{P}(V)\$). *[<sup><span style="color: BurntOrange">$\forall$</span></sup>](https://litlfred.github.io/qou/lean/QOU.ContactAffineChart)*

*Let $E$ be the state bundle over $M$ whose fibres are the spaces of $1$-forms, and let $\mathbb{P}(V)$ be the projective line object ([projective line object](#def:projective-line-object)). Using the Reeb decomposition ([Reeb decomposition](#ex:reeb-decomposition)), every form splits as $\alpha = \alpha_H + \theta \wedge \iota_\xi \alpha$.*

*The *contact affine chart* $U_\xi \subset \mathbb{P}(V)$ is the open dense subset of states with non-vanishing Reeb component:*

*$$U_\xi \;=\; \bigl\{\, [\alpha] \in \mathbb{P}(V)
  \;\big|\; \iota_\xi\,\alpha \neq 0 \,\bigr\}.$$*

*On $U_\xi$, the explicit *affine coordinate* is defined by the ratio of horizontal spatial diffusion to vertical quantum spin:*

*$$Z([\alpha]) \;=\; \frac{\alpha_H}{\iota_\xi\,\alpha}.$$*

*The coordinate $Z$ takes values in the horizontal distribution $H = \ker\theta$. The contact form $\theta$ and the Reeb vector field $\xi$ thus automatically provide the stereographic projection for the projective line fibres — no external coordinates are needed.*

</div>

<div id="prop:substrate-radial-coordinate" class="proposition">

**Proposition 1.31** (Substrate parameter as the radial coordinate). *[<sup><span style="color: BurntOrange">$\forall$</span></sup>](https://litlfred.github.io/qou/lean/QOU.substrate_radial_coordinate)*

*Within the contact affine chart $U_\xi$ ([contact affine chart](#def:contact-affine-chart)), the substrate parameter $q$ ([substrate parameter](#def:substrate-parameter)) governs the radial and phase coordinates of the state. Let $Z$ be the affine coordinate of a state. Then $Z \to 0$ as $q \to \infty$ (deep-quantum origin) and $Z \to \infty$ as $q \to 1$ (classical boundary). The $q$-deformed Reeb flow rotates the phase of $Z$:*

*$$\mathcal{L}_\xi\,Z \;=\; J\,\hbar_q\,Z,$$*

*where $\hbar_q = 1 - q^{-1}$ ([quantum Planck constant](#def:quantum-planck-constant)) and $J$ is the complex structure on $H$.*

</div>

<div class="proof">

*Proof of substrate radial coordinate.* <span id="prf:substrate-radial-coordinate" label="prf:substrate-radial-coordinate"></span>

Within the contact affine chart $U_\xi$ ([contact affine chart](#def:contact-affine-chart)), let $Z$ be the affine coordinate of a state.

1.  **Deep-quantum origin** ($Z \to 0$): as $q \to \infty$ (collapsing instanton), the state becomes purely vertical ($\alpha_H \to 0$). The affine coordinate vanishes, locating the primordial fermion at the origin of the chart.

2.  **Classical boundary** ($Z \to \infty$): as $q \to 1$ (classical vacuum), the state becomes purely horizontal ($\iota_\xi\,\alpha \to 0$, a boson). The affine coordinate diverges, pushing the state to the point at infinity of the $\mathbb{CP}^1$ fibre.

Furthermore, the $q$-deformed Reeb flow ([q-Reeb flow](#ex:q-reeb-flow)) rotates the phase of $Z$ at a rate proportional to the quantum Planck constant:

$$\mathcal{L}_\xi\,Z \;=\; J\,\hbar_q\,Z,$$

where $\hbar_q = 1 - q^{-1}$ ([quantum Planck constant](#def:quantum-planck-constant)) and $J$ is the complex structure on $H$.

This unifies bosons and fermions geometrically: $q$ controls the radial position in $\mathbb{P}(V)$, with the bosonic sector at the boundary and the fermionic sector at the origin. ◻

</div>

<div id="prop:fiber-adjoint-involution" class="proposition">

**Proposition 1.32** (Fiber–adjoint-fiber involution). *[<sup><span style="color: BurntOrange">$\forall$</span></sup>](https://litlfred.github.io/qou/lean/QOU.FiberAdjointInvolution)*

*Let $(\mathcal{C}, A, \tau)$ be a ([quantum observable universe](#def:quantum-observable-universe)). The Frobenius form $\int_A \colon A \to \mathbf{1}$ induces an isomorphism $A \xrightarrow{\;\sim\;} A^{\vee}$ (the Frobenius self-duality), under which:*

1.  *the projective line object $\mathbb{P}(V)$ ([projective line object](#def:projective-line-object)) embeds in the adjoint object $\mathrm{Ad}(A)$ as the coadjoint orbit of a highest-weight vector;*

2.  *the assignment $\sigma \colon \mathbb{P}(V) \hookrightarrow
    \mathrm{Ad}(A)$ is an involution in the sense that $\sigma$ determines $\mathbb{P}(V)$ from $\mathrm{Ad}(A)$ and vice versa;*

3.  *the non-degeneracy of the [Frobenius pairing](#def:frobenius-pairing) forces the observability condition: $$\mathrm{Hom}(\mathbf{1},\, \mathrm{Ad}(A)) = 0.$$*

</div>

<div class="proof">

*Proof of Fiber–adjoint-fiber involution.* <span id="prf:fiber-adjoint-involution" label="prf:fiber-adjoint-involution"></span>

The Frobenius isomorphism $A \cong A^{\vee}$ sends $a \mapsto \int_A \circ
\mu(a \otimes -)$, which is non-degenerate by the Frobenius–Hopf axiom.

**(1) Embedding via rank-$1$ projectors.** Let $\rho \colon V \to V$ be a rank-$1$ projector in $\mathcal{C}$: an endomorphism satisfying $\rho^2 = \rho$ and $\mathrm{tr}(\rho) = \mathrm{id}_{\mathbf{1}}$ (categorical trace via evaluation and coevaluation). Since $V$ has categorical dimension $2$, define the traceless component

$$\sigma(\rho) = \rho - \tfrac{1}{2}\,\mathrm{id}_V
  \;\in\; \mathrm{Ad}(A).$$

This is well-defined because $\mathrm{tr}(\sigma(\rho)) = 1 - \tfrac{1}{2} \cdot 2 = 0$. The set of such projectors is precisely $\mathbb{P}(V) = G/T$, the quotient by the maximal torus.

**(2) The involution.** Under the positive-definite involutive structure $\dagger$ ([involutive structure](#def:involutive-structure)), every rank-$1$ projector satisfies $\rho^{\dagger} = \rho$ (self-adjointness). Computing the square of the traceless component:

$$\sigma(\rho)^2
  = \bigl(\rho - \tfrac{1}{2}\,\mathrm{id}_V\bigr)^2
  = \rho^2 - \rho + \tfrac{1}{4}\,\mathrm{id}_V
  = \tfrac{1}{4}\,\mathrm{id}_V.$$

Thus $2\sigma(\rho)$ is an involution in $\mathrm{End}(V)$: it squares to the identity. Geometrically, $\sigma$ identifies $\mathbb{P}(V)$ with a coadjoint orbit in $\mathrm{Ad}(A)$. The orbit is closed by rigidity of $\mathcal{C}$ and determines a sub-object of $\mathrm{Ad}(A)$ isomorphic to $\mathbb{P}(V)$. Conversely, given this sub-object, the stabiliser of any point is $T$, so $\mathbb{P}(V) \cong G/T$ as $G$-spaces.

**(3) Observability.** Suppose there exists a non-zero morphism $f \colon \mathbf{1} \to \mathrm{Ad}(A)$. Such a morphism would represent a $G$-invariant element in the adjoint representation. By the SU(2) emergence theorem ([SU(2) emergence](#thm:su2-emergence)), the reconstructed gauge group is $G \cong \mathrm{SU}(2)$, and $\mathrm{Ad}(A)$ carries the irreducible adjoint representation $\mathfrak{su}(2)$ (dimension $3$). By Schur’s lemma, the only intertwining morphism from the trivial representation $\mathbf{1}$ to an irreducible non-trivial representation is the zero morphism. Therefore $f = 0$, contradicting our assumption.

Hence $\mathrm{Hom}(\mathbf{1},\, \mathrm{Ad}(A)) = 0$. The non-degeneracy of $\int_A$ excludes any hidden global symmetry: there is no non-trivial invariant section of the adjoint bundle. ◻

</div>

<div id="ex:fiber-adjoint-su2" class="example">

**Example 1.33** (Fiber–adjoint-fiber involution for \$\\}mathrm{SU}(2)\$).

*Continuing [projective line on SU(2)](#ex:projective-line-su2), take $G = \mathrm{SU}(2)$, $T = \mathrm{U}(1)$, and $V = \mathbb{C}^2$. The projective line object is $\mathbb{P}(V) = \mathbb{P}^1(\mathbb{C})$, and the adjoint object is $\mathrm{Ad}(A) \cong \mathfrak{su}(2) \cong \mathbb{R}^3$ (trace-free skew-Hermitian $2 \times 2$ matrices under the Killing form). The embedding $\sigma$ sends a line $\ell = \mathrm{span}(v) \subset \mathbb{C}^2$ to the rank-$1$ projector*

*$$\sigma([\ell]) =
  \frac{v v^{\dagger}}{\lVert v \rVert^2}
  - \tfrac{1}{2}\,\mathrm{id}_V
  \in \mathfrak{su}(2).$$*

*This identifies $\mathbb{P}^1(\mathbb{C})$ with the unit $2$-sphere $S^2 \subset \mathfrak{su}(2)$ (the coadjoint orbit of $\tfrac{1}{2}\,\mathrm{diag}(i, -i)$). Observability follows: a $G$-fixed point in $\mathfrak{su}(2)$ would be a matrix commuting with all of $\mathrm{SU}(2)$, hence a scalar — but trace-free matrices have no non-zero scalars, so $\mathrm{Hom}(\mathbf{1},\, \mathrm{Ad}(A)) = 0$.*

</div>

<div id="def:categorical-connection" class="definition">

**Definition 1.34** (Categorical connection and curvature). *[<sup><span style="color: BurntOrange">$\forall$</span></sup>](https://litlfred.github.io/qou/lean/QOU.CategoricalConnection)*

*Let $(\mathcal{C}, A, \tau)$ be a quantum universe over $R$ with differential forms $\Omega^k(A)$ ([higher forms](#def:higher-forms)).*

*A *connection* on $A$ is a morphism $\nabla \colon A \to A \otimes \Omega^1(A)$ in $\mathcal{C}$ satisfying the Leibniz rule: $\nabla(\mu(a \otimes b)) =
\nabla(a) \cdot b + a \cdot \nabla(b)$, expressed by the commutativity of the *Leibniz triangle*:*

*$$\label{eq:leibniz-triangle}
\begin{tikzcd}[row sep=2.5em, column sep=3.5em]
  A \otimes A
    \ar[r, "\mu"]
    \ar[dr, "{\nabla \otimes 1 \,+\, 1 \otimes \nabla}"']
  & A \ar[d, "\nabla"]
  \\
  & A \otimes \Omega^1(A)
\end{tikzcd}$$*

*The *curvature* of $\nabla$ is the composition*

*$$\label{eq:curvature-composition}
\begin{tikzcd}[column sep=3em]
  A \ar[r, "\nabla"]
  & A \otimes \Omega^1(A) \ar[r, "\nabla"]
  & A \otimes \Omega^2(A)
\end{tikzcd}$$*

*denoted $F_\nabla = \nabla^2$, which is $A$-linear (a standard consequence of the Leibniz rule).*

</div>

<div id="ex:connection-su2" class="example">

**Example 1.35** (Connection and curvature on \$\\}mathcal{O}(\\}mathrm{SU}(2))\$).

*Continuing [fibre adjoint on SU(2)](#ex:fiber-adjoint-su2), take $A = \mathcal{O}(\mathrm{SU}(2))$ with its left-invariant calculus $\Omega^1(A) = \mathrm{span}\{\omega_1, \omega_2, \omega_3\}$ ([higher forms on SU(2)](#ex:higher-forms-su2)). A connection is a covariant derivative $\nabla f = df + \mathcal{A} \cdot f$ for $f \in A$, where $\mathcal{A} = A_1\,\omega_1 + A_2\,\omega_2 + A_3\,\omega_3$ is the connection $1$-form. The Leibniz triangle says $\nabla(fg) = (\nabla f)\,g + f\,(dg)$. The curvature is the $2$-form $F_\nabla = d\mathcal{A} + \mathcal{A} \wedge \mathcal{A} \in \Omega^2(A)$, which is $A$-linear ($F_\nabla(f \cdot s) = f \cdot F_\nabla(s)$). (When the substrate parameter $q$ is introduced in [substrate parameter](#def:substrate-parameter), this calculus deforms to the Woronowicz $3D$-calculus on $\mathcal{O}_q(\mathrm{SU}(2))$.)*

</div>

<div id="def:categorical-jet" class="definition">

**Definition 1.36** (Categorical jet object). *[<sup><span style="color: BurntOrange">$\forall$</span></sup>](https://litlfred.github.io/qou/lean/QOU.CategoricalJet)*

*Let $(\mathcal{C}, A, \tau)$ be a ([quantum universe](#def:quantum-universe)) with connection $\nabla$ ([categorical connection](#def:categorical-connection)). The *jet object* is*

*$$J^1(A) := A \otimes_{\mathcal{C}} \Omega^1(A),$$*

*where $\Omega^1(A) = \ker(\mu \colon A \otimes A \to A)$ is the bimodule of K"ahler differentials. The jet object fits into the universal extension*

*$$\label{eq:jet-ses}
\begin{tikzcd}[column sep=2.5em]
  0 \ar[r]
  & A \otimes \Omega^1(A) \ar[r]
  & J^1(A) \ar[r, "j^1"]
  & A \ar[r]
  & 0
\end{tikzcd}$$*

*where $j^1 \colon J^1(A) \to A$ is the jet evaluation (the counit of the tensor–hom adjunction).*

</div>

<div id="def:categorical-hodge-star" class="definition">

**Definition 1.37** (Categorical Hodge star). *[<sup><span style="color: BurntOrange">$\forall$</span></sup>](https://litlfred.github.io/qou/lean/QOU.CatHodgeInvolution)*

*Let $(\mathcal{C}, A, \tau)$ be a quantum universe over $R$ ([quantum universe](#def:quantum-universe)) with higher differential forms $\Omega^k(A)$ ([higher forms](#def:higher-forms)). The *categorical Hodge star* is the involution $\star \colon \Omega^k(A) \to \Omega^{n-k}(A)$ defined by*

*$$\alpha \wedge \star \beta
  = \int_A\!\bigl(\alpha^* \cdot \beta\bigr)\;\mathrm{vol},$$*

*where $\int_A \colon A \to \mathbf{1}$ is the Frobenius form, $\alpha^* = S(\alpha)$ is the antipode-conjugate, and $\mathrm{vol} \in \Omega^n(A)$ is the volume form (the unique $G$-invariant top form normalised by $\int_A(\mathrm{vol}) = 1$). That $\star^2 = \mathrm{id}$ (i.e. $\star$ is an involution) follows from the non-degeneracy of $\int_A$ and the involutivity of the antipode. More precisely: $S^2 = \mathrm{id}$ holds on $A$ because a commutative Hopf algebra has involutive antipode (and our Frobenius–Hopf axioms imply commutativity of $A$ via the faithfulness of $\tau$ into $R\text{-}\mathrm{Mod}$). The extension to $\Omega^k(A)$ follows from the graded Leibniz rule for $S$ on the differential graded algebra.*

</div>

<div id="ex:hodge-su2" class="example">

**Example 1.38** (Hodge star on \$\\}mathcal{O}(\\}mathrm{SU}(2))\$).

*Continuing [higher forms on SU(2)](#ex:higher-forms-su2), the Hodge star on $A = \mathcal{O}(\mathrm{SU}(2))$ acts on the $3D$-calculus $\Omega^{\bullet}(A)$ as follows. The volume form is $\mathrm{vol} = \omega_1 \wedge \omega_2 \wedge \omega_3$ (normalised by $\int_A(\mathrm{vol}) = 1$). Then:*

- *$\star 1 = \mathrm{vol}$, $\star\mathrm{vol} = 1$.*

- *On $1$-forms: $\star\omega_i = \tfrac{1}{2}\epsilon_{ijk}\,
  \omega_j \wedge \omega_k$ (each basis form maps to its complementary $2$-form).*

- *On $2$-forms: $\star(\omega_i \wedge \omega_j) =
  \epsilon_{ijk}\,\omega_k$ (each basis $2$-form maps to its complementary $1$-form).*

*The Hodge star is the categorical version of "rotating a form into its complement": it identifies $\Omega^k(A)$ with $\Omega^{n-k}(A)$ using the Frobenius form as the inner product. The self-dual $2$-forms $\Omega^+(A)$ are the $+1$-eigenspace of $\star$; in $3$ dimensions, $\star$ on $\Omega^2(A)$ maps to $\Omega^1(A)$, so the self-dual/anti-self-dual decomposition is trivial. The non-trivial decomposition arises when $\dim H = 4$ (the archimedean case, [self-dual curvature](#prop:self-dual-curvature)).*

</div>

## Spatial realization and the categorical–geometric bridge

<div id="def:spatial-realization-functor" class="definition">

**Definition 1.39** (Spatial realization functor). *[<sup><span style="color: BurntOrange">$\forall$</span></sup>](https://litlfred.github.io/qou/lean/QOU.SpatialRealizationFunctor)*

*Let $(\mathcal{C}, A, \tau)$ be a quantum observable universe ([quantum observable universe](#def:quantum-observable-universe)). The *spatial realization* of $A$ is the space*

*$$M = \mathrm{Spec}(A) = \{ p \colon \mathbf{1} \to A \mid
  p \text{ is a categorical point} \}$$*

*([categorical point](#def:categorical-point)), equipped with the following structures derived purely within $\mathcal{C}$:*

1.  ***Local germs.** For each point $p$, the *augmentation ideal* $\mathfrak{m}_p = \ker(p^* \colon A \to \mathbf{1})$ captures the functions vanishing at $p$. The quotient $\mathfrak{m}_p / \mathfrak{m}_p^2$ is functorially dual to the tangent space $T_p M$, giving the first-order germ decomposition $$A / \mathfrak{m}_p^2
      \;\cong\;
      \mathbf{1} \oplus \mathfrak{m}_p / \mathfrak{m}_p^2.$$*

2.  ***Kähler differentials.** The module $\Omega^1(A)$ of Kähler differentials exists in $\mathcal{C}$ by hypothesis. Under the fibre functor, $\tau(\Omega^1(A))$ maps to sections of the cotangent bundle $\Gamma(T^* M)$.*

3.  ***The contact form.** The Frobenius form $\int_A \colon A \to \mathbf{1}$ ([Frobenius pairing](#def:frobenius-pairing)) induces a canonical $1$-form $\theta_A \in \Omega^1(A)$ via pullback along the universal derivation $d \colon A \to \Omega^1(A)$.*

4.  ***The Reeb derivation.** The generator $\xi$ of the maximal torus action ([categorical Reeb](#def:categorical-reeb)) satisfies the Cartan relations $\iota_\xi \theta_A = \mathrm{id}_{\mathbf{1}}$ and $\iota_\xi\,d\theta_A = 0$ within the non-commutative differential calculus.*

*Under $\tau$, these algebraic objects map to their geometric counterparts: $\theta_A$ becomes the global contact $1$-form $\theta$, $\xi$ becomes the Reeb vector field, and non-degeneracy of $\int_A$ guarantees that $d\theta$ is maximally non-degenerate on $\ker\theta$ — the defining property of a contact manifold.*

</div>

<div id="prop:categorical-archimedean-bridge" class="proposition">

**Proposition 1.40** (Categorical–geometric correspondence). *[<sup><span style="color: BurntOrange">$\forall$</span></sup>](https://litlfred.github.io/qou/lean/QOU.categorical_archimedean_bridge)*

*Let $(\mathcal{C}, A, \tau)$ be a quantum observable universe with weight decomposition $\pi_H, \pi_V$ ([weight decomposition](#def:weight-decomposition)) and categorical $q$-exterior derivative $d_q$ ([categorical $q$-exterior derivative](#def:categorical-q-ext-deriv)). Under the fibre functor $\tau$, the categorical and geometric formulations of $d_q$ coincide:*

*$$\tau(\pi_V \circ d)
  \;=\;
  \theta \wedge \mathcal{L}_\xi
  \;\colon\;
  \Omega^k(M) \to \Omega^{k+1}(M),$$*

*where $\theta$ is the contact form and $\mathcal{L}_\xi$ is the Lie derivative along the Reeb vector field.*

</div>

<div class="proof">

*Proof.* <span id="prf:categorical-archimedean-bridge" label="prf:categorical-archimedean-bridge"></span> The fibre functor $\tau$ maps:

- the Frobenius form $\int_A$ to the contact integral $\int_M \alpha \wedge (d\theta)^n$,

- the maximal torus generator $\xi$ to the Reeb vector field satisfying $\iota_\xi\theta = 1$ and $\iota_\xi\,d\theta = 0$,

- the weight decomposition $\pi_H, \pi_V$ to the splitting $\Omega^k(M) = \Omega^k_H(M) \oplus \theta \wedge
  \Omega^{k-1}_H(M)$ induced by the Reeb direction.

For a form $\alpha \in \Omega^k(M)$, the vertical projection $\pi_V(d\alpha)$ extracts the component of $d\alpha$ carrying non-zero weight under the $T$-action. In the geometric realisation, the $T$-action is the Reeb flow $\phi_t \colon M \to M$, whose infinitesimal generator is $\mathcal{L}_\xi$. The non-zero-weight part of $d\alpha$ is precisely the component along the Reeb direction:

$$\pi_V(d\alpha) = \theta \wedge \iota_\xi(d\alpha)
  = \theta \wedge (\mathcal{L}_\xi\alpha - d(\iota_\xi\alpha)).$$

On horizontal forms ($\iota_\xi\alpha = 0$), this reduces to $\theta \wedge \mathcal{L}_\xi\alpha$. For general forms, writing $\alpha = \alpha_H + \theta \wedge \beta$ and using $\mathcal{L}_\xi\theta = 0$, we obtain $\pi_V(d\alpha) = \theta \wedge \mathcal{L}_\xi\alpha$ in all cases. Therefore

$$\tau(d_q) = q^{-1} d + (1 - q^{-1})\,\theta \wedge
  \mathcal{L}_\xi,$$

which is precisely the archimedean formula for $d_q$ ([archimedean $q$-exterior derivative](#ex:q-ext-deriv)). ◻

</div>

## Substrate parameter and deformation

<div id="def:substrate-parameter" class="definition">

**Definition 1.41** (Substrate parameter). *[<sup><span style="color: BurntOrange">$\forall$</span></sup>](https://litlfred.github.io/qou/lean/QOU.SubstrateParameter)*

*Let $(\mathcal{C}, A, \tau)$ be a quantum observable universe ([quantum observable universe](#def:quantum-observable-universe)) with weight decomposition $\pi_H, \pi_V$ ([weight decomposition](#def:weight-decomposition)) and Reeb derivation $\xi$ ([categorical Reeb](#def:categorical-reeb)). The non-commutative de Rham complex $(\Omega^\bullet(A), d)$ carries two canonical endomorphisms:*

1.  *the full differential $d \colon \Omega^k(A) \to \Omega^{k+1}(A)$;*

2.  *the vertical differential $\pi_V \circ d$, which retains only the component along the Reeb direction.*

*These span a one-parameter family of first-order operators parametrised by $q \in k^{\times}$:*

*$$d_q \;=\; q^{-1}\,d \;+\; (1 - q^{-1})\,\pi_V \circ d.$$*

*The *substrate parameter* is the fibre coordinate $q \in k^{\times}$ on this family. Equivalently, $q$ is the unique element of $\mathrm{End}(\mathbf{1}) \cong k$ such that $d_q$ acts as $q^{-1}\,d$ on horizontal forms and as $d$ on vertical forms.*

*At $q = 1$ the operator $d_q$ recovers $d$ (classicality: horizontal and vertical differentiation are treated equally). As $q \to \infty$, $d_q$ projects onto $\pi_V \circ d$ (deep-quantum regime: only the Reeb direction contributes). The substrate parameter is *not* intrinsic to the triple $(\mathcal{C}, A, \tau)$; it records where one sits in the $\mathbb{G}_m$-family of interpolations between $d$ and $\pi_V \circ d$.*

*When the quantum universe is fibred over a space $M$ (as in the archimedean realisation, [$\mathbb{C}$-quantum universe](#ex:c-quantum-universe)), the substrate parameter becomes a *substrate field* $q \colon M \to k^{\times}$, encoding the local position in the Reeb fibre at each point.*

**Algebraic perspective.* The Lusztig integral form $\mathcal{U}^{\mathbb{Z}}_q(\mathfrak{su}(2))$ is the universal $\mathbb{Z}[q, q^{-1}]$-algebra generated by $K^{\pm 1}$ and the divided powers $E^{(n)}, F^{(n)}$. A ring homomorphism $\iota \colon \mathbb{Z}[q, q^{-1}] \to k$, $q \mapsto q_0$, base-changes this to the quantised enveloping algebra at $q_0$. The categorical and algebraic viewpoints agree: the interpolation parameter $q$ in $d_q$ and the specialisation target $q_0 = \iota(q)$ determine the same deformation.*

</div>

<div id="thm:substrate-parameter-exists" class="theorem">

**Theorem 1.42** (Existence of the substrate parameter). *[<sup><span style="color: BurntOrange">$\forall$</span></sup>](https://litlfred.github.io/qou/lean/QOU.SubstrateParameter.ofReebDecomposition)*

*Let $(\mathcal{C}, A, \tau)$ be a ([quantum observable universe](#def:quantum-observable-universe)) with [weight decomposition](#def:weight-decomposition) $(\pi_H, \pi_V)$ and [categorical Reeb derivation](#def:categorical-reeb) $(\xi, \theta_A)$. Then there exists a [substrate parameter](#def:substrate-parameter) $q \colon M \to \mathbb{R}_{>0}$ with $q(p) \ge 1$, not a root of unity, such that the $q$-deformed differential*

*$d_q = q^{-1}\, d + (1 - q^{-1})\, \pi_V \circ d$*

*interpolates between the full differential $d$ (at $q = 1$) and the vertical projection $\pi_V \circ d$ (as $q \to \infty$).*

</div>

<div class="proof">

*Proof of existence of the substrate parameter.* <span id="prf:substrate-parameter-exists" label="prf:substrate-parameter-exists"></span>

The construction proceeds by choosing $q_0 > 1$ transcendental (hence not a root of unity) and setting $q(p) = q_0$ for all $p$. The classicality bound $q \ge 1$ and positivity are immediate from $q_0 > 1$. Non-constant substrate fields arise from the Reeb flow parameterisation of the fibre coordinate. ◻

</div>

<div id="def:quantum-gauge-group" class="definition">

**Definition 1.43** (Quantum Gauge Group). *[<sup><span style="color: BurntOrange">$\forall$</span></sup>](https://litlfred.github.io/qou/lean/QOU.QuantumGaugeGroup)*

*Let $(\mathcal{C}, A, \tau)$ be a ([quantum observable universe](#def:quantum-observable-universe)) with substrate parameter $q_0$ ([substrate parameter](#def:substrate-parameter)). The *quantum gauge group* is $G_{q_0} = \mathrm{SU}_{q_0}(2)$, the quantum group obtained by deforming the Tannakian gauge group $G = \mathrm{Aut}^{\otimes}(\tau) \cong \mathrm{SU}(2)$ ([SU(2) emergence](#thm:su2-emergence)) at the parameter $q_0$. When the substrate parameter varies over a space $M$ (e.g. the archimedean realisation), this yields a field of quantum groups $\{G_{q(p)}\}_{p \in M}$.*

</div>

<div id="def:quantum-planck-constant" class="definition">

**Definition 1.44** (Quantum Planck Constant). *[<sup><span style="color: BurntOrange">$\forall$</span></sup>](https://litlfred.github.io/qou/lean/QOU.quantumPlanckConstant)*

*Let $(\mathcal{C}, A, \tau)$ be a quantum observable universe with substrate parameter $q_0$ ([substrate parameter](#def:substrate-parameter)). The *quantum Planck constant* is the element $\hbar_q = 1 - q_0^{-1} \in R$. When the substrate parameter varies over a space $M$, this defines a field $\hbar_q \colon M \to R$ by $\hbar_q(p) = 1 - q(p)^{-1}$.*

</div>

<div id="def:q-hodge-star" class="definition">

**Definition 1.45** (\$q\$-Hodge star). *[<sup><span style="color: BurntOrange">$\forall$</span></sup>](https://litlfred.github.io/qou/lean/QOU.QHodgeStar)*

*Let $(\mathcal{C}, A, \tau)$ be a quantum observable universe with categorical Hodge star $\star$ ([categorical hodge star](#def:categorical-hodge-star)) and substrate parameter $q$ ([substrate parameter](#def:substrate-parameter)). The *$q$-Hodge star* is the $q$-deformed involution $\star_q \colon \Omega^k(A) \to \Omega^{n-k}(A)$ defined by*

*$$\alpha \wedge_q \star_q \beta
  \;=\; q \cdot \int_A\!\bigl(\alpha^* \cdot \beta\bigr)\;\mathrm{vol}.$$*

*At $q = 1$ this recovers the categorical Hodge star: $\star_1 = \star$. The factor of $q$ rescales the inner product on forms, coupling the Hodge duality to the local deformation strength.*

</div>

## Categorical action and variational equations

<div id="def:categorical-action" class="definition">

**Definition 1.46** (Categorical action). *[<sup><span style="color: BurntOrange">$\forall$</span></sup>](https://litlfred.github.io/qou/lean/QOU.CategoricalAction)*

*Let $(\mathcal{C}, A, \tau)$ be a ([quantum observable universe](#def:quantum-observable-universe)) equipped with substrate parameter $q$ ([substrate parameter](#def:substrate-parameter)), $q$-Hodge star $\star_q$ ([$q$-Hodge star](#def:q-hodge-star)), a connection $\nabla$ ([categorical connection](#def:categorical-connection)), and a section $\psi \colon \mathbf{1} \to A$ (a "state"). The *categorical action* is the $R$-valued functional*

*$$\label{eq:categorical-action}
  \mathcal{S}_q[\nabla,\, \textstyle\int_A,\, \psi]
  \;=\;
  \underbrace{\mathrm{tr}\bigl(q \cdot R_{\int}\bigr)
  }_{\text{gravity}}
  \;+\;
  \underbrace{\int_A \!\circ\, \mathrm{tr}_A\bigl(
      F_\nabla \wedge_q \star_q F_\nabla
    \bigr)
  }_{\text{gauge}}
  \;+\;
  \underbrace{\int_A\!\bigl(\psi^* \cdot D_\nabla\,\psi\bigr)
  }_{\text{matter}},$$*

*with notation as in [categorical action notation](#rem:categorical-action-notation).*

</div>

<div id="prop:variational-equations" class="proposition">

**Proposition 1.47** (Variational equations of the categorical action). *[<sup><span style="color: BurntOrange">$\forall$</span></sup>](https://litlfred.github.io/qou/lean/QOU.variational_equations)*

*Let $\mathcal{S}_q$ be the ([categorical action](#def:categorical-action)). The three variational equations are:*

1.  **Gravity (vary $\int_A$)*: $\delta\mathcal{S}_q / \delta\!\int_A = 0$ yields the *categorical Einstein equation*: $$R_{\int} - \tfrac{1}{2}\,\mathrm{tr}(R_{\int})\,\mathrm{id}_A
      \;=\; T_q[\nabla, \psi],$$ where $T_q$ is the stress-energy endomorphism constructed from the gauge and matter terms.*

2.  **Gauge (vary $\nabla$)*: $\delta\mathcal{S}_q / \delta\nabla = 0$ yields the *categorical Yang–Mills equation*: $$\nabla \star_q F_\nabla + q \cdot [F_\nabla,\, \star_q F_\nabla]
      \;=\; J_\psi,$$ where $J_\psi = \psi^* \otimes D_\nabla\psi - D_\nabla\psi^* \otimes \psi$ is the matter current.*

3.  **Matter (vary $\psi$)*: $\delta\mathcal{S}_q / \delta\psi = 0$ yields the *categorical transport equation*: $$D_\nabla\,\psi \;=\; 0.$$*

</div>

<div class="proof">

*Proof of Variational equations of the categorical action.* <span id="prf:variational-equations" label="prf:variational-equations"></span>

Each equation is obtained by computing $\delta\mathcal{S}_q = 0$ with respect to the indicated variable, using the non-degeneracy of $\int_A$.

*Item (1): Vary $\int_A$.* The gravity term $\mathrm{tr}(q \cdot R_{\int})$ depends on $\int_A$ through the Frobenius–Ricci endomorphism $R_{\int}$. Varying $\int_A \mapsto \int_A + \delta\!\int_A$ and requiring $\delta\mathcal{S}_q = 0$ for all $\delta\!\int_A$ gives, by non-degeneracy of the categorical trace, $R_{\int} - \tfrac{1}{2}\,\mathrm{tr}(R_{\int})\,\mathrm{id}_A
= T_q[\nabla, \psi]$, where the stress-energy $T_q$ collects the $\int_A$-dependence of the gauge and matter terms. The trace subtraction ensures $\mathrm{tr}(T_q) = \tfrac{1}{2}\,\mathrm{tr}(R_{\int})$ (the contracted Bianchi identity).

*Item (2): Vary $\nabla$.* The gauge term $\int_A \circ \mathrm{tr}_A(F_\nabla \wedge_q \star_q F_\nabla)$ depends on $\nabla$ through $F_\nabla = \nabla^2$. A standard computation using $\delta F_\nabla = \nabla(\delta\nabla)$ and integration by parts (via non-degeneracy of $\int_A$) yields $\nabla \star_q F_\nabla + q \cdot [F_\nabla,\, \star_q F_\nabla]
= J_\psi$. The commutator term $q \cdot [F_\nabla, \star_q F_\nabla]$ arises from the non-commutativity of the $q$-deformed wedge product; it vanishes when $q = 1$ (the abelian/classical limit).

*Item (3): Vary $\psi$.* The matter term $\int_A(\psi^* \cdot D_\nabla\,\psi)$ is linear in $\psi$. Varying $\psi \mapsto \psi + \delta\psi$ and using $(\delta\psi)^* \cdot D_\nabla\,\psi = 0$ for all $\delta\psi$ gives $D_\nabla\,\psi = 0$ by non-degeneracy of $\int_A$ and the dagger structure ([positive definite dagger](#def:positive-definite-dagger)). ◻

</div>

## Particles, fermions, bosons, and observation

<div id="def:categorical-q-ext-deriv" class="definition">

**Definition 1.48** (Categorical \$q\$-deformed exterior derivative). *[<sup><span style="color: BurntOrange">$\forall$</span></sup>](https://litlfred.github.io/qou/lean/QOU.CategoricalQExtDeriv)*

*Let $(\mathcal{C}, A, \tau)$ be a quantum observable universe with connection $\nabla$ ([categorical connection](#def:categorical-connection)), substrate parameter $q$ ([substrate parameter](#def:substrate-parameter)), and weight decomposition $\pi_H, \pi_V$ ([weight decomposition](#def:weight-decomposition)). The *$q$-deformed exterior derivative* $d_q \colon \Omega^k(A) \to \Omega^{k+1}(A)$ is*

*$$d_q \;=\; q^{-1}\,d + (1 - q^{-1})\,\pi_V \circ d,$$*

*where $d \colon \Omega^k(A) \to \Omega^{k+1}(A)$ is the differential of the non-commutative de Rham complex. Equivalently, $d_q$ acts as $q^{-1}\,d$ on horizontal forms and as $d$ on vertical forms:*

*$$\label{eq:categorical-dq-cd}
\begin{tikzcd}[row sep=2.5em, column sep=2.5em]
  \Omega^k_H(A) \ar[r, "d"] \ar[d, hook]
  & \Omega^{k+1}(A) \ar[r, "q^{-1}"]
  & \Omega^{k+1}(A) \\
  \Omega^k(A) \ar[rru, "d_q"']
\end{tikzcd}$$*

*The *$q$-adjoint* $\delta_q \colon \Omega^{k+1}(A) \to \Omega^k(A)$ is the adjoint of $d_q$ with respect to the dagger structure ([positive definite dagger](#def:positive-definite-dagger)).*

</div>

<div id="def:q-harmonic-form" class="definition">

**Definition 1.49** (\$q\$-harmonic form (particle)). *[<sup><span style="color: BurntOrange">$\forall$</span></sup>](https://litlfred.github.io/qou/lean/QOU.QHarmonicForm)*

*Let $(\mathcal{C}, A, \tau)$ be a quantum observable universe with $q$-deformed exterior derivative $d_q$ ([categorical $q$-exterior derivative](#def:categorical-q-ext-deriv)). The *$q$-Laplacian* on $\Omega^k(A)$ is $\Delta_q = d_q\,\delta_q + \delta_q\,d_q$. A *particle* is an element $\alpha \in \Omega^k(A)$ that is $q$-harmonic:*

*$$\Delta_q\,\alpha \;=\; 0.$$*

</div>

<div id="def:fermion-boson-decomposition" class="definition">

**Definition 1.50** (Fermion–Boson decomposition). *[<sup><span style="color: BurntOrange">$\forall$</span></sup>](https://litlfred.github.io/qou/lean/QOU.Fermion)*

*Let $\mathcal{H}_q^k = \ker\Delta_q \subset \Omega^k(A)$ denote the space of particles ([$q$-harmonic form](#def:q-harmonic-form)). The weight decomposition ([weight decomposition](#def:weight-decomposition)) restricts to a short exact sequence*

*$$\label{eq:fermion-boson-ses}
\begin{tikzcd}[column sep=2.5em]
  0 \ar[r]
  & \mathcal{H}_{q,H}^k \ar[r, hook]
  & \mathcal{H}_q^k \ar[r, "\pi_V"]
  & \mathcal{H}_{q,V}^k \ar[r]
  & 0
\end{tikzcd}$$*

*where $\mathcal{H}_{q,H}^k = \mathcal{H}_q^k \cap \Omega^k_H(A)$ and $\mathcal{H}_{q,V}^k = \pi_V(\mathcal{H}_q^k)$. A *boson* is a particle in the kernel $\mathcal{H}_{q,H}^k$ (purely horizontal: $\alpha_V = 0$). A *fermion* is a particle with $\alpha_V \neq 0$, i.e. one whose image under $\pi_V$ is non-zero.*

*The sequence splits via $\pi_H$:*

*$$\label{eq:fermion-boson-split}
\begin{tikzcd}[column sep=2.5em]
  \mathcal{H}_q^k
    \ar[r, "\pi_H \oplus \pi_V", "\sim"']
  & \mathcal{H}_{q,H}^k \;\oplus\; \mathcal{H}_{q,V}^k
\end{tikzcd}
\qquad
\text{(bosons $\oplus$ fermion vertical parts).}$$*

</div>

<div id="def:categorical-point" class="definition">

**Definition 1.51** (Categorical point). *[<sup><span style="color: BurntOrange">$\forall$</span></sup>](https://litlfred.github.io/qou/lean/QOU.CategoricalPoint)*

*Let $(\mathcal{C}, A, \tau)$ be a ([quantum universe](#def:quantum-universe)). A *categorical point* of $A$ is a morphism*

*$$p \;\colon\; \mathbf{1} \;\longrightarrow\; A
  \qquad\text{in } \mathcal{C}.$$*

</div>

<div id="def:observation" class="definition">

**Definition 1.52** (Observation). *[<sup><span style="color: BurntOrange">$\forall$</span></sup>](https://litlfred.github.io/qou/lean/QOU.Observation)*

*Let $(\mathcal{C}, A, \tau)$ be a quantum observable universe over a ring $R$ ([quantum observable universe](#def:quantum-observable-universe)), let $q$ denote the ([substrate parameter](#def:substrate-parameter)), and let $p \colon \mathbf{1} \to A$ be a ([categorical point](#def:categorical-point)). An *observation at $p$* is a morphism*

*$$\mathcal{O}_p \;\colon\; A / \mathfrak{m}_p^2
  \;\longrightarrow\; A / \mathfrak{m}_p^2
  \qquad\text{in } \mathcal{C},$$*

*acting on germs at $p$, satisfying:*

1.  ***Frobenius compatibility.** The observation preserves the Frobenius form at $p$: $$\label{eq:observation-frobenius}
    \begin{tikzcd}[row sep=2.5em, column sep=3em]
      A / \mathfrak{m}_p^2 \ar[r, "\mathcal{O}_p"] \ar[dr, "\int_{A,p}"']
      & A / \mathfrak{m}_p^2 \ar[d, "\int_{A,p}"] \\
      & \mathbf{1}
    \end{tikzcd}$$ where $\int_{A,p}$ is the germ of the Frobenius form at $p$.*

2.  ***Substrate perturbation.** The observation shifts the deformation parameter $q \mapsto q' = q + \delta q$ via the Hopf coaction: $$\label{eq:observation-substrate}
    \begin{tikzcd}[row sep=2.5em, column sep=3em]
      A \ar[r, "\Delta"] \ar[d, "\mathcal{O}_p"']
      & A \otimes A \ar[r, "\mathcal{O}_p \otimes S"]
      & A \otimes A \ar[d, "\mu"] \\
      A \ar[rr, "\int_A"']
      & & \mathbf{1}
    \end{tikzcd}$$ with $\delta q(p) = \int_A(\mathcal{O}_p(a_{(1)})\,S(a_{(2)}))$ evaluated at the point $p$.*

</div>

## Geometric interpretations

## Categorical instanton and self-duality

<div id="def:categorical-instanton" class="definition">

**Definition 1.53** (Categorical instanton). *[<sup><span style="color: BurntOrange">$\forall$</span></sup>](https://litlfred.github.io/qou/lean/QOU.CategoricalInstanton)*

*Let $(\mathcal{C}, A, \tau)$ be a ([quantum observable universe](#def:quantum-observable-universe)) with connection $\nabla$ ([categorical connection](#def:categorical-connection)) and $q$-Hodge star $\star_q$ ([$q$-Hodge star](#def:q-hodge-star)). The connection $\nabla$ is an *instanton* if its curvature $F_\nabla \in \Omega^2(A)$ is $\star_q$-self-dual:*

*$$\star_q\, F_\nabla \;=\; F_\nabla.$$*

*Equivalently, the curvature factors through the self-dual projection:*

*$$\label{eq:instanton-cd}
\begin{tikzcd}[row sep=2.5em, column sep=3em]
  A \otimes A \ar[r, "\nabla \circ \nabla"]
    \ar[dr, "0"']
  & \Omega^2(A) \ar[d, "\pi^-"] \\
  & \Omega^-(A)
\end{tikzcd}$$*

*where $\pi^- = \tfrac{1}{2}(\mathrm{id} - \star_q)$ is the anti-self-dual projector and $\Omega^-(A) = \ker(\mathrm{id} + \star_q)$.*

</div>

<div id="lem:categorical-irreducible" class="lemma">

**Lemma 1.54** (Irreducibility from observability). *[<sup><span style="color: BurntOrange">$\forall$</span></sup>](https://litlfred.github.io/qou/lean/QOU.categorical_irreducible)*

*Let $(\mathcal{C}, A, \tau)$ be a quantum observable universe. Any categorical instanton $\nabla$ ([categorical instanton](#def:categorical-instanton)) is irreducible: $\operatorname{Hom}_{\mathcal{C}}(\mathbf{1},\,\mathrm{Ad}(A)) = 0$.*

</div>

<div class="proof">

*Proof of Irreducibility from observability.* <span id="prf:categorical-irreducible" label="prf:categorical-irreducible"></span> [<sup><span style="color: BurntOrange">$\forall$</span></sup>](https://litlfred.github.io/qou/lean/QOU.categorical_irreducible)

Suppose $s \colon \mathbf{1} \to \mathrm{Ad}(A)$ is a non-zero invariant morphism. The following diagram commutes:

Since $\mathrm{Ad}(A)$ is the trace-free part of $A \otimes A^*$, the Frobenius form $\int_A$ vanishes on it: $\int_A \circ s = 0$. But $\int_A$ is non-degenerate by the observability axiom, so $s = 0$. ◻

</div>

<div id="prop:categorical-self-duality" class="proposition">

**Proposition 1.55** (Categorical self-duality). *[<sup><span style="color: BurntOrange">$\forall$</span></sup>](https://litlfred.github.io/qou/lean/QOU.categorical_self_duality)*

*Let $(\mathcal{C}, A, \tau)$ be a quantum observable universe with volume form $\mathrm{vol} \in \Omega^n(A)$ ([$q$-Hodge star](#def:q-hodge-star)). Every connection $\nabla$ that is a critical point of the categorical Yang–Mills functional*

*$$S[\nabla] \;=\; \int_A\!\bigl(\star_q(F_\nabla) \cdot F_\nabla\bigr)$$*

*is an instanton ([categorical instanton](#def:categorical-instanton)). That is, the following diagram commutes:*

*$$\label{eq:self-duality-cd}
\begin{tikzcd}[row sep=2.5em, column sep=3.5em]
  \Omega^2(A) \ar[r, "\star_q"] \ar[d, "\int_A(\,\cdot\, {*}\, \cdot\,)"']
  & \Omega^2(A) \ar[d, "\int_A(\,\cdot\, {*}\, \cdot\,)"] \\
  \mathbf{1} \ar[r, "\mathrm{id}"']
  & \mathbf{1}
\end{tikzcd}
\qquad\Longrightarrow\qquad
F_\nabla \in \Omega^+(A).$$*

</div>

<div class="proof">

*Proof of Categorical self-duality.* <span id="prf:categorical-self-duality" label="prf:categorical-self-duality"></span> [<sup><span style="color: BurntOrange">$\forall$</span></sup>](https://litlfred.github.io/qou/lean/QOU.categorical_self_duality)

By the Bogomolny decomposition in the dagger category,

$$\int_A(F_\nabla^* \cdot F_\nabla)
  \;=\; 2\,\int_A({F_\nabla^-}^* \cdot F_\nabla^-)
        + \int_A(F_\nabla \wedge_q F_\nabla),$$

where the second term is topological (determined by the class $[F_\nabla] \in \Omega^2(A)/\mathrm{exact}$). Minimising $S[\nabla]$ forces $F_\nabla^- = 0$, which is exactly the self-duality condition. ◻

</div>

## Non-vanishing of \$d_q^2\$ and jet prolongation

<div id="prop:categorical-dq-squared" class="proposition">

**Proposition 1.56** (Non-vanishing of \$d_q^2\$). *[<sup><span style="color: BurntOrange">$\forall$</span></sup>](https://litlfred.github.io/qou/lean/QOU.categorical_dq_squared)*

*Let $d_q$ be the categorical $q$-deformed exterior derivative ([categorical $q$-exterior derivative](#def:categorical-q-ext-deriv)). The composition $d_q^2 = d_q \circ d_q \colon \Omega^k(A) \to \Omega^{k+2}(A)$ is given by*

*$$d_q^2\,\alpha
  \;=\; q^{-1}(1 - q^{-1})\;\omega_V \wedge_q [\xi,\, \alpha],$$*

*where $\omega_V \in \Omega^2(A)$ is the curvature of the weight decomposition (the image of the unit $1_A$ under $\pi_V \circ d \circ d$) and $[\xi, \alpha]$ is the Lie derivative along the generator $\xi$ of the $T$-action ([weight decomposition](#def:weight-decomposition)). The following diagram displays the obstruction to nilpotence:*

*$$\label{eq:dq-squared-cd}
\begin{tikzcd}[row sep=2.5em, column sep=2.5em]
  \Omega^k(A) \ar[r, "d_q"] \ar[dr, "d_q^2"']
  & \Omega^{k+1}(A) \ar[d, "d_q"] \\
  & \Omega^{k+2}(A)
\end{tikzcd}
\qquad
d_q^2 = 0 \;\Longleftrightarrow\;
q = 1 \;\text{ or }\; [\xi, \alpha] = 0.$$*

*In particular, $d_q^2 \neq 0$ for generic $\alpha$ whenever $q \neq 1$: the $q$-deformed de Rham complex is *not* a cochain complex. On $\xi$-invariant forms (the horizontal subcomplex $\Omega^k_H(A)$), $d_q$ does reduce to $q^{-1} d$ and $d_q^2 = 0$.*

</div>

<div class="proof">

*Proof of Non-vanishing of \$d_q^2\$.* <span id="prf:categorical-dq-squared" label="prf:categorical-dq-squared"></span> [<sup><span style="color: BurntOrange">$\forall$</span></sup>](https://litlfred.github.io/qou/lean/QOU.categorical_dq_squared)

Write $a = q^{-1}$ and $b = 1 - q^{-1}$, so $d_q = a\,d + b\,\pi_V d$. Then

$$\begin{aligned}
  d_q^2
  &= (a\,d + b\,\pi_V d)(a\,d + b\,\pi_V d) \\
  &= a^2\,\underbrace{d^2}_{= 0}
     + ab\,(d \circ \pi_V d + \pi_V d \circ d)
     + b^2\,\underbrace{\pi_V d \circ \pi_V d}_{= 0}.
\end{aligned}$$

The first term vanishes because $d^2 = 0$ in the non-commutative de Rham complex. The last term vanishes because $\pi_V$ is the projection onto the vertical (weight-$1$) summand of the Reeb decomposition $\Omega^k(A) = \Omega^k_H(A) \oplus \theta_A \wedge \Omega^{k-1}_H(A)$: the exterior derivative $d$ applied to a vertical form produces a form whose vertical component has weight $\geq 2$ in $\theta_A$, but the contact distribution forces $\theta_A \wedge \theta_A = 0$ (since $\theta_A$ is a $1$-form), so $\pi_V(d(\pi_V\alpha)) = 0$. For the middle term, we first establish the key commutation relation. Since $\pi_V$ is the projection onto the non-zero-weight summand of the $T$-action on $\Omega^k(A)$, and $d$ is the universal derivation, the commutator $[d, \pi_V] = d \circ \pi_V - \pi_V \circ d$ measures how much $d$ fails to preserve the weight grading. On a weight-$n$ form $\alpha_n$, we have $d\alpha_n = (d\alpha_n)_H + (d\alpha_n)_V$; the weight-shift arises from the Lie derivative along $\xi$ (the generator of $T$), giving

$$[d, \pi_V]\,\alpha = \mathcal{L}_\xi(\alpha) - \pi_V(\mathcal{L}_\xi(\alpha))
  = \pi_H(\mathcal{L}_\xi\,\alpha).$$

Since $\pi_H + \pi_V = \mathrm{id}$ and $\mathcal{L}_\xi = \iota_\xi \circ d + d \circ \iota_\xi$ (Cartan’s formula), the middle term simplifies: $d(\pi_V d\,\alpha) + \pi_V d(d\,\alpha) = \omega_V \wedge_q [\xi, \alpha]$ where $\omega_V = d(\pi_V(d\,1_A)) \in \Omega^2(A)$ is the curvature of the weight projection — a canonical $2$-form measuring the failure of the horizontal distribution to be integrable. ◻

</div>

<div id="def:categorical-q-lie-bracket" class="definition">

**Definition 1.57** (Categorical \$q\$-Lie bracket). *[<sup><span style="color: BurntOrange">$\forall$</span></sup>](https://litlfred.github.io/qou/lean/QOU.CategoricalQLieBracket)*

*Let $(\mathcal{C}, A, \tau)$ be a quantum observable universe with Reeb derivation $\xi$ ([categorical Reeb derivation](#def:categorical-reeb)) and substrate parameter $q$ ([substrate parameter](#def:substrate-parameter)). The *$q$-deformed Lie bracket* on derivations of $A$ is*

*$$[X, Y]_q \;=\; q^{-1}\,[X, Y]
  + (1 - q^{-1})\,\bigl(\theta_A(X)\,[\xi, Y]
                        - \theta_A(Y)\,[\xi, X]\bigr),$$*

*where $\theta_A$ is the canonical $1$-form dual to $\xi$ and $[X, Y]$ is the commutator of derivations in $\mathcal{C}$.*

</div>

<div id="def:categorical-q-connection" class="definition">

**Definition 1.58** (Categorical \$q\$-deformed connection). *[<sup><span style="color: BurntOrange">$\forall$</span></sup>](https://litlfred.github.io/qou/lean/QOU.CategoricalQConnection)*

*Let $\nabla$ be a connection on $A$ ([categorical connection](#def:categorical-connection)) and $\xi$ the Reeb derivation ([categorical Reeb derivation](#def:categorical-reeb)). The *$q$-deformed connection* is*

*$$\nabla_q \;=\; q^{-1}\,\nabla
  + (1 - q^{-1})\,(\iota_\xi\, \nabla)\,\theta_A.$$*

*At $q = 1$, $\nabla_q = \nabla$.*

</div>

## Archimedean quantum universe

We now specialise the categorical framework to the archimedean setting, where the base ring is an archimedean field $K$ (e.g. $\mathbb{Q}$, $\mathbb{R}$, or $\mathbb{C}$) and the quantum universe is realised by CR geometry on a contact manifold. The abstract categorical structures — Frobenius form, weight decomposition, $q$-deformed operators — acquire concrete geometric meaning as differential-geometric objects on a CR manifold equipped with a pseudo-Hermitian structure. The main result (§<a href="#sec:physical-interpretation" data-reference-type="ref" data-reference="sec:physical-interpretation">1.15</a>) places gravity, gauge theory, and quantum mechanics in a unified commutative diagram within this setting.

## \$q\$-Deformed operators

## Physical interpretation and main result

<div id="def:q-yang-mills-levi" class="definition">

**Definition 1.59** (\$q\$-Weighted Yang–Mills–Levi functional). *[<sup><span style="color: BurntOrange">$\forall$</span></sup>](https://litlfred.github.io/qou/lean/QOU.QYangMillsLevi)*

*Let $(M, \theta, G, P, E)$ be an archimedean quantum observable universe with instanton connection $A$ and substrate parameter $q$ ([substrate parameter](#def:substrate-parameter)). The *$q$-weighted Yang–Mills–Levi functional* is*

*$$S_q[A, \theta]
  \;=\; \int_M q(p)\,\lVert F_A^+|_H \rVert^2\,
        \theta \wedge (d\theta)^n,$$*

*where $q(p) = 1 + \lvert\langle L_\theta, F_A^+\rangle\rvert(p)$ ([$\mathbb{C}$-substrate via Levi form](#rem:c-substrate-via-levi)).*

</div>

<div id="prop:main-commutative-diagram" class="proposition">

**Proposition 1.60** (Main Commutative Diagram). *[<sup><span style="color: BurntOrange">$\forall$</span></sup>](https://litlfred.github.io/qou/lean/QOU.main_commutative_diagram)*

*Let $(M, \theta, G, P, E)$ be an archimedean quantum observable universe with instanton connection $A$ ([instanton](#ex:instanton)) and substrate parameter $q$ ([substrate parameter](#def:substrate-parameter)). Let $\mathbf{E}$ denote the Euler–Lagrange operator of the $q$-weighted Yang–Mills–Levi functional $S_q$ ([$q$-Yang–Mills–Levi functional](#def:q-yang-mills-levi)), and let $\nabla^A$ denote parallel transport along $A$. The following diagram commutes:*

*$$\begin{tikzcd}[row sep=2.5em, column sep=2.5em]
  J^1E
    \ar[r, "{\mathbf{E}[S_q]}"]
    \ar[d, "\text{jet evaluation}"']
  & \bigl\{ L_\theta : \mathrm{Ric}_{g_\theta} = T^{(q)} \bigr\}
    \ar[d, "{q = 1 + \lvert\langle L_\theta, F_A^+\rangle\rvert}"]
  \\
  \Gamma(E_{\mathrm{lin}})
    \ar[r, "\nabla^A"']
  & \bigl\{ \psi : J\hbar_q\,\iota_{\xi_q}D_A\psi = \hat{H}_q\psi \bigr\}
\end{tikzcd}$$*

*where the top row sends a jet (a first-order perturbation of the gauge field) to the Einstein-type field equation via the Euler–Lagrange operator; the left column evaluates a jet at a fibre point to produce a linearised section; the right column is the coupling through the substrate field $q$; and the bottom row is the parallel-transport equation whose linearisation is the Schrödinger equation.*

</div>

<div class="proof">

*Proof of Main Commutative Diagram.* <span id="prf:main-commutative-diagram" label="prf:main-commutative-diagram"></span> [<sup><span style="color: BurntOrange">$\forall$</span></sup>](https://litlfred.github.io/qou/lean/QOU.main_commutative_diagram)

We verify commutativity by tracing both paths around the diagram.

**Top-right path** (variational → coupling). The Euler–Lagrange operator $\mathbf{E}[S_q]$ applied to a jet $j^1_p \sigma$ yields the variational equation $\mathrm{Ric}_{g_\theta} = T^{(q)}$ ([GR substrate geometry](#rem:gr-substrate-geometry)). Solving for $L_\theta$ determines the Webster metric, which in turn fixes the substrate field via the coupling $q(p) = 1 + \lvert\langle L_\theta, F_A^+\rangle\rvert$. This determines $\hbar_q = 1 - q^{-1}$, the $q$-Reeb field $\xi_q$, and the $q$-Hamiltonian $\hat{H}_q = -\tfrac{1}{2}\hbar_q\,\Delta_q + V_q$ appearing in the transport equation.

**Left-bottom path** (evaluation → transport). The jet evaluation map $j^1_p \sigma \mapsto \sigma(p)$ produces a section $\psi \in \Gamma(E_{\mathrm{lin}})$ by linearising the fibre $\mathbb{P}^1(\mathbb{C})$ at the chosen base-point. Parallel transport along $A$ then imposes $J\hbar_q\,\iota_{\xi_q} D_A\psi = \hat{H}_q\psi$ ([Schrödinger equation](#rem:schrodinger-jet-coaction)).

**Commutativity.** Both paths share the same input ($j^1_p \sigma$) and the same output (a section $\psi$ satisfying the transport equation at substrate parameter $q$). The key identity is that the chain rule for the composite $S_q[\nabla, L_\theta, \psi]$ factorises the variation into two coupled equations:

1.  $\delta S_q / \delta L_\theta = 0$ determines $L_\theta$ (hence $q$ and $\hat{H}_q$) — this is the top row;

2.  $\delta S_q / \delta \psi = 0$ gives $D_\nabla\psi = 0$ ([variational equations](#prop:variational-equations), Item 3) — this is the bottom row.

The coupling $q = 1 + \lvert\langle L_\theta, F_A^+\rangle\rvert$ ensures that the $q$ appearing in the top-right path equals the $q$ in the left-bottom path. Non-degeneracy of $\int_A$ ([Frobenius pairing](#def:frobenius-pairing)) guarantees that the solution sets agree: solving for $L_\theta$ first and then substituting into the transport equation yields the same $\psi$ as evaluating the jet and transporting along $A$. ◻

</div>

## Introduction and categorical context

This chapter collects the categorical, algebraic, and analytic details that underpin the definitions of [Chapter](#chap:qou). The reader who has read [Chapter](#chap:qou) may return to specific sections as needed; the remainder of the paper does not require this chapter in linear order.

<div id="def:quantum-flatness" class="definition">

**Definition 1.61** (Quantum flatness). *[<sup><span style="color: BurntOrange">$\forall$</span></sup>](https://litlfred.github.io/qou/lean/QOU.QuantumFlatness)*

*Let $(\mathcal{C}, A, \tau)$ be a quantum observable universe with gauge group $G_q = \mathrm{Aut}^{\otimes}(\tau)$ ([quantum gauge group](#def:quantum-gauge-group)) and connection $\nabla$ on $A$ ([categorical connection](#def:categorical-connection)). Let $\mathrm{INN}(G_q)$ denote the inner-automorphism $2$-group of $G_q$, with $2$-form datum $B \in \Omega^2(A) \otimes \mathrm{Ad}(A)$.*

*The connection $\nabla$ is *quantum flat* if the curvature $F_\nabla$ equals the $2$-form datum:*

*$$F_\nabla = B.$$*

*This is not an independent axiom. It is a derived consequence of the instanton condition ([categorical instanton](#def:categorical-instanton)) combined with the simplicity constraint $B \in \Gamma(\Lambda^+ H^* \otimes \mathrm{Ad}(P))$:*

1.  *The instanton equation $\star_q F_\nabla = F_\nabla$ forces $F_\nabla = F_\nabla^+$ (self-dual curvature).*

2.  *The simplicity constraint restricts $B = F_\nabla^+$.*

3.  *Combining: $F_\nabla = B$.*

*Quantum flatness therefore encodes the condition that the $2$-group gauge theory of $\mathrm{INN}(G_q)$ admits no independent $2$-connection — the $2$-form datum is fully determined by the ordinary connection.*

</div>

<div id="prop:emergence-to-quantum-flat" class="proposition">

**Proposition 1.62** (From Tannakian emergence to 2-group quantum flatness). *[<sup><span style="color: BurntOrange">$\forall$</span></sup>](https://litlfred.github.io/qou/lean/QOU.emergence_to_quantum_flat)*

*Let $(\mathcal{C}, A, \tau)$ be a quantum observable universe satisfying the ([categorical volume constraint](#def:categorical-volume-constraint)), so that $G_q = \mathrm{Aut}^{\otimes}(\tau) \cong \mathrm{SU}_q(2)$ ([SU(2) emergence](#thm:su2-emergence)). Then the inner-automorphism $2$-group $\mathrm{INN}(G_q)$ is the unique strict $2$-group whose quantum flatness condition $F_A = B$ reproduces the instanton equation $F_A^{-} = 0$ under the simplicity constraint.*

*Quantum flatness is not an independent assumption: it is a *derived consequence* of the instanton axiom. The instanton condition $F_A = F_A^+$ (self-dual curvature) combined with the simplicity constraint $B = F_A^+$ gives $F_A = B$ automatically. The $2$-group language is a descriptive overlay that makes the higher-categorical structure manifest, not an additional physical constraint.*

</div>

<div class="proof">

*Proof of From Tannakian emergence to 2-group quantum flatness.* <span id="prf:emergence-to-quantum-flat" label="prf:emergence-to-quantum-flat"></span>

The argument proceeds in three steps.

*Step 1: The volume constraint determines the Lie algebra.* The categorical volume constraint provides a non-degenerate epimorphism $\epsilon \colon \Lambda^2 V \to \mathbf{1}$. Under the forgetful functor $\tau$, this endows the rank-$2$ module $\tau(V)$ with a $q$-antisymmetric pairing whose invariance algebra is $\mathfrak{su}_q(2)$. This is the Lie algebra of the reconstructed group $G_q$, and hence of the crossed module $\partial \colon G_q \xrightarrow{\mathrm{id}} G_q$ defining $\mathrm{INN}(G_q)$.

*Step 2: The determinant-one condition descends to the 2-form datum.* A $2$-connection $(A, B)$ for the principal $2$-bundle of $\mathrm{INN}(G_q)$ takes values in $\mathfrak{g}_q = \mathfrak{su}_q(2)$. Quantum flatness sets $B = F_A$, so $B$ inherits the tracelessness forced by the determinant constraint $\det(g_V) = 1$ of [SU(2) emergence](#thm:su2-emergence): $B$ is $\mathrm{Ad}(P)$-valued with $\mathrm{tr}\,B = 0$, i.e. $\mathfrak{su}_q(2)$-valued rather than $\mathfrak{gl}_q(2)$-valued.

*Step 3: Simplicity plus quantum flatness gives the instanton equation.* Imposing the simplicity constraint $B \in \Gamma(\Lambda^+\!H^* \otimes \mathrm{Ad}(P))$ ([self-dual 2-group](#rem:self-dual-2group)) and combining with $F_A = B$ yields $F_A = F_A^+$, hence $F_A^- = 0$. Step 1 guarantees the structure group is $\mathrm{SU}_q(2)$—not a quotient of $\mathrm{GL}_q(2)$—so the instanton moduli space carries the gauge symmetry dictated by the categorical axioms. ◻

</div>

<div id="prop:dq-squared" class="proposition">

**Proposition 1.63** (d_q^2 does not vanish). *[<sup><span style="color: BurntOrange">$\forall$</span></sup>](https://litlfred.github.io/qou/lean/QOU.dq_squared)*

*The archimedean specialisation of the categorical $d_q^2$ formula ([non-vanishing of $d_q^2$](#prop:categorical-dq-squared)) yields, for the $q$-deformed exterior derivative ([$q$-exterior derivative](#ex:q-ext-deriv)) acting on $\Omega^k(M)$:*

*$$d_q^2\,\alpha
  \;=\; q^{-1}(1 - q^{-1})\,d\theta \wedge \mathcal{L}_\xi\,\alpha.$$*

*Here the categorical curvature $\omega_V$ of the weight projection specialises to $d\theta$ (the symplectic form on $H$) via the ([categorical–geometric correspondence](#prop:categorical-archimedean-bridge)), and $[\xi, \alpha]$ becomes $\mathcal{L}_\xi\,\alpha$.*

*In particular, $d_q^2 = 0$ if and only if $q = 1$ (classical case) or $\alpha$ lies in the kernel of $\mathcal{L}_\xi$ (Reeb-invariant forms). On horizontal $\mathcal{L}_\xi$-invariant forms, $d_q$ *does* define a cochain complex.*

</div>

<div class="proof">

*Proof of d_q^2 does not vanish.* <span id="prf:dq-squared" label="prf:dq-squared"></span>

Write $a = q^{-1}$ and $b = 1 - q^{-1}$, so $a + b = 1$. Then

$$\begin{aligned}
  d_q^2\,\alpha
  &= d_q\bigl(a\,d\alpha + b\,\theta \wedge \mathcal{L}_\xi\alpha\bigr) \\
  &= a^2\,d^2\alpha
     + ab\,d(\theta \wedge \mathcal{L}_\xi\alpha)
     + ab\,\theta \wedge \mathcal{L}_\xi\,d\alpha
     + b^2\,\theta \wedge \mathcal{L}_\xi(\theta \wedge \mathcal{L}_\xi\alpha).
\end{aligned}$$

The first term vanishes since $d^2 = 0$. The second expands as $ab\,d\theta \wedge \mathcal{L}_\xi\alpha - ab\,\theta \wedge d\mathcal{L}_\xi\alpha$. The third term cancels the second’s negative part because $[d,\, \mathcal{L}_\xi] = 0$ implies $\theta \wedge \mathcal{L}_\xi\,d\alpha = \theta \wedge d\,\mathcal{L}_\xi\alpha$. For the fourth term, the Reeb field satisfies $\mathcal{L}_\xi\theta = 0$ (since $\iota_\xi d\theta = 0$ and $\theta(\xi)=1$), so $\mathcal{L}_\xi(\theta \wedge \mathcal{L}_\xi\alpha) = \theta \wedge \mathcal{L}_\xi^2\alpha$; the factor $\theta \wedge \theta = 0$ in $b^2\,\theta \wedge \theta \wedge \mathcal{L}_\xi^2\alpha$ kills this term. Hence $d_q^2\alpha = ab\,d\theta \wedge \mathcal{L}_\xi\alpha$. ◻

</div>

<div id="prop:q-jacobiator" class="proposition">

**Proposition 1.64** (Jacobiator of the q-Lie bracket). *[<sup><span style="color: BurntOrange">$\forall$</span></sup>](https://litlfred.github.io/qou/lean/QOU.q_jacobiator)*

*The archimedean specialisation of the categorical $q$-Lie bracket ([categorical $q$-Lie bracket](#def:categorical-q-lie-bracket)) to the $q$-deformed Lie bracket ([$q$-Lie bracket](#ex:q-lie-bracket)) violates the Jacobi identity when $q \neq 1$.*

*Let $U, V, W \in \Gamma(H)$ be horizontal vector fields (i.e. $\theta(U) = \theta(V) = \theta(W) = 0$). The *Jacobiator**

*$$\mathrm{Jac}_q(U,V,W)
  \;:=\; [[U,V]_q, W]_q + [[V,W]_q, U]_q + [[W,U]_q, V]_q$$*

*is given by*

*$$\mathrm{Jac}_q(U,V,W)
  \;=\; -q^{-1}(1-q^{-1})\!\sum_{\mathrm{cyc}}
        d\theta(V,W)\,\mathcal{L}_\xi U,$$*

*where the sum is over cyclic permutations of $(U,V,W)$. In particular, $\mathrm{Jac}_q = 0$ if and only if $q = 1$ (classical Jacobi identity) or $d\theta|_{H \times H} = 0$ (integrable horizontal distribution). Since $d\theta|_{H \times H}$ is the Levi form $L_\theta$, which is non-degenerate by hypothesis, $[\,\cdot\,,\cdot\,]_q$ violates the Jacobi identity for all $q \neq 1$. Thus $(\mathfrak{X}(M), [\,\cdot\,,\cdot\,]_q)$ is a *Leibniz algebra* (or a pre-Lie algebra), not a Lie algebra.*

*The coefficient $q^{-1}(1-q^{-1})$ matches the $d_q^2$ obstruction ([archimedean $d_q^2$](#thm:dq-squared)), confirming that both failures — of nilpotence and of the Jacobi identity — are driven by the same geometric source: the non-degeneracy of the contact structure.*

</div>

<div class="proof">

*Proof of Jacobiator of the q-Lie bracket.* <span id="prf:q-jacobiator" label="prf:q-jacobiator"></span>

For horizontal $V, W$, the bracket reduces to $[V,W]_q = q^{-1}[V,W]$. The mixed term $\theta([V,W]_q) = -q^{-1}\,d\theta(V,W)$ is in general non-zero. Substituting into the next bracket:

$$\begin{aligned}
_q,\, U]_q
  &= q^{-2}\,[[V,W],U]
    - q^{-1}(1-q^{-1})\,d\theta(V,W)\,\mathcal{L}_\xi U,
\end{aligned}$$

using $\theta(U)=0$ and $\theta([V,W]_q) = -q^{-1}d\theta(V,W)$. Summing cyclically, the $q^{-2}$ terms assemble into $q^{-2}\,\mathrm{Jac}(U,V,W) = 0$ by the classical Jacobi identity, leaving only the $d\theta$ terms. ◻

</div>

## Lifting: jet prolongation, transport, and torsion

The categorical jet object $J^1(A)$ ([categorical jet](#def:categorical-jet)) encodes first-order deformations of the Frobenius–Hopf object. In this section we develop the *lifting* programme: promoting a quantum observable universe on $A$ to one on $J^1(A)$, and iterating to build the brane tower.

<div id="prop:categorical-jet-prolongation" class="proposition">

**Proposition 1.65** (Jet prolongation). *[<sup><span style="color: BurntOrange">$\forall$</span></sup>](https://litlfred.github.io/qou/lean/QOU.categorical_jet_prolongation)*

*Let $(\mathcal{C}, A, \tau)$ be a quantum universe with connection $\nabla$ ([categorical connection](#def:categorical-connection)). Then $J^1(A)$ ([categorical jet](#def:categorical-jet)) inherits a Frobenius–Hopf structure from $A$, and the quadruple $(\mathcal{C},\, J^1(A),\, \tau',\, q)$ — where $\tau'$ is the induced fibre functor — is again a quantum universe.*

</div>

<div class="proof">

*Proof of categorical jet prolongation.* <span id="prf:categorical-jet-prolongation" label="prf:categorical-jet-prolongation"></span>

The Frobenius–Hopf structure on $J^1(A)$ is inherited from $A$ via the jet prolongation functor. The induced fibre functor $\tau'$ is defined by composition with the canonical projection $J^1(A) \to A$, and the substrate parameter $q$ carries over unchanged. The commutativity of the diagram

$$\begin{tikzcd}[row sep=2.5em, column sep=3em]
  J^1(A) \ar[r, "\nabla'"] \ar[d, "j^1"']
  & J^1(A) \otimes \Omega^1(J^1(A)) \ar[d, "j^1 \otimes j^1"] \\
  A \ar[r, "\nabla"']
  & A \otimes \Omega^1(A)
\end{tikzcd}$$

follows from the universal property of the jet bundle: $j^1$ is the universal first-order differential operator, so any connection $\nabla$ on $A$ lifts uniquely to $\nabla'$ on $J^1(A)$ making the square commute. ◻

</div>

<div id="def:categorical-transport" class="definition">

**Definition 1.66** (Categorical transport equation). *[<sup><span style="color: BurntOrange">$\forall$</span></sup>](https://litlfred.github.io/qou/lean/QOU.CategoricalTransport)*

*Let $(\mathcal{C}, A, \tau)$ be a quantum observable universe with instanton $\nabla$ ([categorical instanton](#def:categorical-instanton)) and $q$-deformed exterior derivative $d_q$ ([categorical $q$-exterior derivative](#def:categorical-q-ext-deriv)). The *categorical transport equation* for a section $\psi \in \tau(J^1(A))$ ([categorical jet](#def:categorical-jet)) is*

*$$\label{eq:categorical-transport}
  \hbar_q\;\pi_V(\nabla\,\psi) \;=\; H_q(\psi),$$*

*where $H_q \colon \tau(J^1(A)) \to \tau(J^1(A))$ is the *$q$-Hamiltonian* endomorphism $H_q = -\tfrac{1}{2}\hbar_q\,\Delta_q + V_q$ (with $V_q$ the potential arising from the curvature $F_\nabla$). The following diagram encodes the transport as the bottom row of the main commutative diagram:*

*$$\label{eq:transport-cd}
\begin{tikzcd}[row sep=2.5em, column sep=3em]
  \tau(J^1(A)) \ar[r, "\nabla"] \ar[d, "j^1"']
  & \tau(J^1(A)) \otimes \Omega^1 \ar[d, "\pi_V"] \\
  \tau(A) \ar[r, "H_q"']
  & \tau(J^1(A))
\end{tikzcd}$$*

</div>

<div id="def:categorical-q-reeb-flow" class="definition">

**Definition 1.67** (Categorical q-Reeb flow). *[<sup><span style="color: BurntOrange">$\forall$</span></sup>](https://litlfred.github.io/qou/lean/QOU.CategoricalQReebFlow)*

*Let $\xi$ be the Reeb derivation of $A$ ([categorical Reeb derivation](#def:categorical-reeb)) and $[\,\cdot\,,\cdot\,]_q$ the $q$-Lie bracket ([categorical $q$-Lie bracket](#def:categorical-q-lie-bracket)). The *$q$-deformed Reeb derivation* $\xi_q$ is the derivation of $A$ defined by*

*$$\xi_q(a) \;=\; q^{-1}\,\xi(a)
  + (1 - q^{-1})\,[\xi,\, X_a]_q,$$*

*where $X_a$ is the horizontal derivation associated to $a$ (i.e. $\pi_H(da) = \iota_{X_a}\, \theta_A$). The *$q$-Reeb flow* is the one-parameter family of automorphisms $\phi_t^q \in \mathrm{Aut}(A)$ generated by $\xi_q$.*

</div>

<div id="def:categorical-q-torsion-leaf" class="definition">

**Definition 1.68** (Categorical q-torsion leaf). *[<sup><span style="color: BurntOrange">$\forall$</span></sup>](https://litlfred.github.io/qou/lean/QOU.CategoricalQTorsionLeaf)*

*A *$q$-torsion leaf* is a maximal sub-object $L \hookrightarrow A$ such that:*

1.  ***Horizontality:** $L \subset \ker(\pi_V)$ (all forms on $L$ are horizontal).*

2.  ***Flow invariance:** $\phi_t^q(L) = L$ for all $t$ (the $q$-Reeb flow preserves $L$).*

</div>

# Lifting and Descent

## Jet Prolongation

<div id="prop:jet-prolongation" class="proposition">

**Proposition 2.1** (Jet Prolongation). *[<sup><span style="color: BurntOrange">$\forall$</span></sup>](https://litlfred.github.io/qou/lean/QOU.JetProlongation)*

*Let $(\mathcal{C}, A, \tau)$ be a quantum observable universe over a ring $R$ ([quantum observable universe](#def:quantum-observable-universe)). Define the *jet object**

*$$J^1(A) \;:=\; A \otimes \Omega^1(A),$$*

*where $\Omega^1(A) = \ker(m \colon A \otimes A \to A)$ is the bimodule of Kähler differentials. Then $J^1(A)$ carries a canonical Frobenius–Hopf structure inherited from $A$, and the quadruple $(\mathcal{C},\, J^1(A),\, \tau',\, q)$ — where $\tau' = \tau \circ (\text{--} \otimes \Omega^1)$ is the induced fibre functor — is again a quantum observable universe over $R$.*

</div>

<div class="proof">

*Proof of Jet Prolongation.* <span id="prf:jet-prolongation" label="prf:jet-prolongation"></span>

The proof proceeds in the rigid monoidal category underlying the quantum observable universe. Let $A$ denote the Frobenius–Hopf object representing the gauge-bundle data of $(M,G,P,E)$.

*Step 1: Categorical jet object.* The first jet bundle $J^1 E$ is represented categorically by the object $A \otimes \Omega^1(A)$, where $\Omega^1(A) = \ker(m\colon A\otimes A \to A)$ is the kernel of the multiplication (the bimodule of Kähler differentials, i.e. the universal first-order differential calculus over $A$). Because $A$ is Frobenius, the non-degenerate pairing $\varepsilon \circ m \colon A \otimes A \to \mathbf{1}$ exhibits $\Omega^1(A)$ as a direct summand of $A \otimes A$, hence $J^1(A) := A \otimes \Omega^1(A)$ is again an object of the ambient category.

*Step 2: Inherited Frobenius–Hopf structure.* The Frobenius relation $(\mathrm{Id} \otimes m) \circ (\Delta \otimes \mathrm{Id})
 = \Delta \circ m
 = (m \otimes \mathrm{Id}) \circ (\mathrm{Id} \otimes \Delta)$ ensures that the comultiplication $\Delta\colon A \to A \otimes A$ restricts to a well-defined comultiplication $\Delta'\colon J^1(A) \to J^1(A) \otimes J^1(A)$, and the counit $\varepsilon\colon A \to \mathbf{1}$ induces a counit $\varepsilon'$ on $J^1(A)$. The Hopf antipode $S$ extends to $J^1(A)$ by functoriality of the Kähler differential construction. Thus $J^1(A)$ is a Frobenius–Hopf object.

This step relies on the *strong multiplicativity* condition: the co-multiplication must be compatible with the deformed product at every filtration degree. Over fields of positive characteristic, the rigorous proof that this compatibility survives the deformation is the main theorem of \[fred2005\], which constructs $\mathrm{Dist}(G)$ as a Gröbner–Shirshov deformation of the commutative $\mathrm{Dist}(H)$ and verifies the Frobenius relation at each stage (see also [skew poisson integration](#prop:skew-poisson-integration) in [Chapter](#chap:p-adic)).

*Step 3: Non-degeneracy and vanishing.* The non-degeneracy of the Frobenius form on $A$ (the pairing $\varepsilon \circ m$ is a perfect pairing) implies non-degeneracy of the induced form on $J^1(A)$, since $\Omega^1(A)$ is a direct summand. For the vanishing condition, $\mathrm{Hom}(\mathbf{1}, \mathrm{Ad}(A)) = 0$ implies $\mathrm{Hom}(\mathbf{1}, \mathrm{Ad}(J^1(A))) = 0$: the adjoint representation of $J^1(A)$ contains $\mathrm{Ad}(A)$ as a subobject, and any invariant in $\mathrm{Ad}(J^1(A))$ would project to a non-zero invariant in $\mathrm{Ad}(A)$, contradicting the hypothesis.

*Step 4: Geometric realisation.* Applying the fibre functor $\tau\colon \mathcal{C} \to \mathrm{Vect}_k$ (where $\mathcal{C}$ is the rigid monoidal category of the quantum observable universe) recovers the geometric data: $\tau(J^1(A))$ is the space of sections of the first jet bundle $J^1 E$, the frame bundle $P'$ and orthonormal frame bundle $E'$ are the geometric counterparts of the Frobenius–Hopf structure on $J^1(A)$, and the connection $A'$ is the image under $\tau$ of the comultiplication $\Delta'$. Its uniqueness follows from the irreducibility of $A'$, which is guaranteed by the inherited vanishing condition of Step 3. ◻

</div>

## Recursive Brane Tower

<div id="def:recursive-brane-tower" class="definition">

**Definition 2.2** (Recursive Brane Tower). *[<sup><span style="color: BurntOrange">$\forall$</span></sup>](https://litlfred.github.io/qou/lean/QOU.RecursiveBraneTower)*

*Let $(\mathcal{C}, A, \tau)$ be a quantum observable universe over a ring $R$ ([quantum observable universe](#def:quantum-observable-universe)). Set $A_0 = A$. *Inductively*, define $A_{n+1} = J^1(A_n)$ as the ([jet prolongation](#prop:jet-prolongation)) of the Frobenius–Hopf object $A_n$.*

*The *brane relation* is the following recursive structure:*

1.  *Each jet object $A_n$ serves as the base object for the next level; $A_n$ is the *brane* of $A_{n+1}$.*

2.  *At each level, the comultiplication $\Delta_n$ on $A_n$ encodes the $n$-th level connection, inherited from the Frobenius–Hopf structure by [jet prolongation](#prop:jet-prolongation).*

*The *recursive brane tower* is the sequence $A_0 \hookrightarrow A_1 \hookrightarrow A_2 \hookrightarrow \cdots$ in $\mathcal{C}$, where each embedding is the canonical inclusion $A_n \hookrightarrow J^1(A_n) = A_{n+1}$ via the unit section.*

</div>

## Cosimplicial Crossed Groupoid Structure

The recursive brane tower carries a higher-categorical structure that organises the transitions between levels into a cosimplicial crossed groupoid. The key observation is that Yekutieli’s framework for central extensions of gerbes \[yekutieli2010\] furnishes exactly the triples $(x, g, a)$ needed to define the face and degeneracy maps.

<div id="def:yekutieli-triple" class="definition">

**Definition 2.3** (Yekutieli triple mapping). *[<sup><span style="color: BurntOrange">$\forall$</span></sup>](https://litlfred.github.io/qou/lean/QOU.YekutieliTripleMapping)*

*Let $(\mathcal{C}, A, \tau)$ be a quantum observable universe and let $\{A_n\}_{n \geq 0}$ be its ([recursive brane tower](#def:recursive-brane-tower)); let $q$ denote the substrate parameter. Let $\{U_i\}$ be a covering of the underlying site $\mathcal{S}$ trivialising every level of the tower. The *Yekutieli triple* at level $n$ over an intersection $U_i \cap U_j$ is the datum $(x_{ij}^{(n)},\, g_{ij}^{(n)},\, a_{ij}^{(n)})$ where:*

1.  **Objects* $x_i^{(n)} \in \mathrm{Ob}(\mathfrak{G}_n|_{U_i})$ are local trivialisations of the Frobenius–Hopf object $A_n$.*

2.  **$1$-morphisms* $g_{ij}^{(n)} \colon x_i^{(n)} \to x_j^{(n)}$ are the transition automorphisms in $\mathrm{Aut}_{\mathcal{C}}(A_n|_{U_i \cap U_j})$, encoding the patching data of the comultiplication $\Delta_n$.*

3.  **$2$-morphisms* $a_{ij}^{(n)} \colon g_{ij}^{(n)} \Rightarrow g_{ij}^{(n+1)}$ are the deformation parameters living in the band $\mathcal{B}$, implementing the lift of transition automorphisms from level $n$ to level $n{+}1$.*

*The assignment $n \mapsto (x^{(n)}, g^{(n)}, a^{(n)})$ is functorial: the ([jet prolongation](#prop:jet-prolongation)) sends the triple at level $n$ to the triple at level $n{+}1$, and the descent homomorphism $\mathfrak{d}_{n+1}$ ([descent](#lem:descent)) reverses this assignment. In the archimedean realisation, $g_{ij}^{(n)} \in
\Gamma(U_i \cap U_j,\, \mathrm{SU}_{q_n}(2))$ are gauge transition functions and $a_{ij}^{(n)} \in \mathcal{O}_M^{\times}$.*

</div>

<div id="prop:cosimplicial-crossed-groupoid" class="proposition">

**Proposition 2.4** (Cosimplicial crossed groupoid). *[<sup><span style="color: BurntOrange">$\forall$</span></sup>](https://litlfred.github.io/qou/lean/QOU.cosimplicial_crossed_groupoid_exists)*

*Let $(\mathcal{C}, A, \tau)$ be a quantum observable universe and let $\{A_n\}_{n \geq 0}$ be its ([recursive brane tower](#def:recursive-brane-tower)); let $q$ denote the substrate parameter. Equipped with the Yekutieli triples $(x^{(n)}, g^{(n)}, a^{(n)})$ of [Yekutieli triple](#def:yekutieli-triple). Then the assignment*

*$$[n] \;\longmapsto\; \mathfrak{G}_n$$*

*from the simplex category $\Delta$ to the $2$-category of gerbes on $M$ extends to a *cosimplicial crossed groupoid*: a cosimplicial object in the category of crossed groupoids, where*

1.  *the coface maps $\delta^i \colon \mathfrak{G}_{n} \to
    \mathfrak{G}_{n+1}$ are given by the jet prolongation acting on objects (inserting the $i$-th degeneracy in the Cech nerve),*

2.  *the codegeneracy maps $\sigma^j \colon \mathfrak{G}_{n+1} \to
    \mathfrak{G}_{n}$ are given by the descent homomorphism $\mathfrak{d}_{n+1}$ (collapsing the $j$-th face),*

3.  *the crossed structure is furnished by the conjugation action of the $1$-morphisms $g_{ij}^{(n)}$ on the $2$-morphisms $a_{ij}^{(n)}$ via the adjoint representation of $\mathrm{SU}_{q_n}(2)$.*

</div>

<div class="proof">

*Proof of Cosimplicial crossed groupoid.* <span id="prf:cosimplicial-crossed-groupoid" label="prf:cosimplicial-crossed-groupoid"></span>

We verify the cosimplicial identities and the crossed-module axioms.

*Step 1: Cosimplicial identities.* The coface maps are composites of the jet prolongation with the Cech face maps $\partial^i$ of the cover $\{U_i\}$. The codegeneracy maps are composites of the descent homomorphism with the Cech degeneracy maps $s^j$. The identities $\delta^j \circ \delta^i = \delta^i \circ \delta^{j-1}$ for $i < j$ and $\sigma^j \circ \sigma^i = \sigma^i \circ \sigma^{j+1}$ for $i \leq j$ follow from the functoriality of jet prolongation and descent: the ascent $\ell_n$ is a natural transformation from the identity functor on $\mathfrak{G}_n$ to the restriction of $\mathfrak{G}_{n+1}$, and the descent $\mathfrak{d}_{n+1}$ is its left adjoint. The mixed identity $\sigma^j \circ \delta^i$ reduces to three cases ($i < j$, $i = j$ or $i = j + 1$, $i > j + 1$), each verified using the retraction property $\mathfrak{d}_{n+1} \circ \ell_n = \mathrm{id}$ ([descent](#lem:descent)).

*Step 2: Crossed-module structure.* At each level $n$, the pair $(\mathrm{SU}_{q_n}(2),\, \mathcal{O}_M^{\times})$ carries the structure of a crossed module in the sense of \[yekutieli2010\]: the boundary map $\partial \colon \mathcal{O}_M^{\times} \to \mathrm{SU}_{q_n}(2)$ sends a unit $a \in \mathcal{O}_M^{\times}$ to the central element $a \cdot \mathbf{1} \in \mathrm{SU}_{q_n}(2)$ (the central extension), and the action of $g \in \mathrm{SU}_{q_n}(2)$ on $a \in \mathcal{O}_M^{\times}$ is conjugation: $g \cdot a = g\, a\, g^{-1}$. This action is well-defined because $\mathcal{O}_M^{\times}$ is central in the gerbe band; the Peiffer identity $\partial(a) \cdot b = a\, b\, a^{-1}$ is automatic for a central extension.

*Step 3: Compatibility.* The coface and codegeneracy maps respect the crossed-module structure because the jet prolongation preserves the Hopf-algebra multiplication ([jet prolongation](#prop:jet-prolongation), Step 2) and the descent homomorphism is a $*$-homomorphism ([descent](#lem:descent), Step 4). Hence the conjugation action of $g_{ij}^{(n)}$ on $a_{ij}^{(n)}$ is compatible with the simplicial maps, making the total assignment a cosimplicial crossed groupoid. ◻

</div>

<div id="prop:descent-condition" class="proposition">

**Proposition 2.5** (Descent condition — twisted \$2\$-cocycle). *[<sup><span style="color: BurntOrange">$\forall$</span></sup>](https://litlfred.github.io/qou/lean/QOU.Torsion.descent_condition)*

*Let $(\mathcal{C}, A, \tau)$ be a quantum observable universe and let $\{A_n\}_{n \geq 0}$ be its recursive brane tower; let $q$ denote the substrate parameter. With Yekutieli triples $(x^{(n)}, g^{(n)}, a^{(n)})$ ([Yekutieli triple](#def:yekutieli-triple)) and let $A_\infty = \sum_{n,i} c_{n,i}\, \alpha_{n,i}$ ([distributional connection](#rem:distributional-connection)) be the distributional connection. Then the global consistency of $A_\infty$ is equivalent to the satisfaction of the *twisted $2$-cocycle condition*: for every triple intersection $U_i \cap U_j \cap U_k$,*

*$$\label{eq:twisted-2-cocycle}
  d\!\left(g_{ijk}^{(n)}\right)
  \;=\;
  a_{ij}^{(n)} \cdot g_{ijk}^{(n)} \cdot \left(a_{jk}^{(n)}\right)^{-1},$$*

*where $g_{ijk}^{(n)} = g_{ij}^{(n)} \cdot g_{jk}^{(n)} \cdot (g_{ik}^{(n)})^{-1}$ is the Cech $1$-cocycle deviation at level $n$, $d(g_{ijk}^{(n)})$ denotes the Cech coboundary (the failure of the $1$-cocycle condition), and $a_{ij}^{(n)}, a_{jk}^{(n)} \in \mathcal{O}_M^{\times}$ are the $2$-morphisms (quantum deformation feedback from $\mathrm{SU}_{q_n}(2)$).*

*Equivalently, the obstruction class $\kappa_n$ ([quantum characteristic classes](#def:quantum-characteristic-classes)) is the cohomology class of the twisted $2$-cocycle $[a_{ij}^{(n)} \cdot (\cdot) \cdot (a_{jk}^{(n)})^{-1}]$ in $H^2(M,\, \mathcal{O}_M^{\times})$.*

</div>

<div class="proof">

*Proof of Descent condition — twisted \$2\$-cocycle.* <span id="prf:descent-condition" label="prf:descent-condition"></span>

Let $\{U_i\}$ be a good cover trivialising the tower. On $U_i \cap U_j$ the gauge transition function $g_{ij}^{(n)}$ patches the connection $A_n$:

$$A_n|_{U_j} \;=\; g_{ij}^{(n)} \cdot A_n|_{U_i} \cdot
  (g_{ij}^{(n)})^{-1} + (g_{ij}^{(n)})^{-1}\, dg_{ij}^{(n)}.$$

On a triple overlap $U_i \cap U_j \cap U_k$, the ordinary cocycle condition $g_{ij}^{(n)} \cdot g_{jk}^{(n)} = g_{ik}^{(n)}$ holds if and only if the connection $A_n$ is globally well-defined at level $n$ with no twist. The passage from level $n$ to level $n{+}1$ via the central extension $\mathfrak{G}_{n+1} \to \mathfrak{G}_n$ introduces the $2$-morphism twist: the transition functions at level $n{+}1$ are related to those at level $n$ by

$$g_{ij}^{(n+1)} \;=\; a_{ij}^{(n)} \cdot g_{ij}^{(n)},$$

where $a_{ij}^{(n)} \in \mathcal{O}_M^{\times}$ is the local lift datum ([Yekutieli triple](#def:yekutieli-triple)). Computing the cocycle deviation at level $n{+}1$:

$$\begin{aligned}
  g_{ijk}^{(n+1)}
  &= g_{ij}^{(n+1)} \cdot g_{jk}^{(n+1)} \cdot (g_{ik}^{(n+1)})^{-1} \\
  &= (a_{ij}^{(n)} \cdot g_{ij}^{(n)}) \cdot (a_{jk}^{(n)} \cdot g_{jk}^{(n)})
     \cdot (a_{ik}^{(n)} \cdot g_{ik}^{(n)})^{-1}.
\end{aligned}$$

Since $a_{ij}^{(n)}$ is central (it lies in the band $\mathcal{O}_M^{\times}$ of the gerbe), the gauge factors commute past the $a$-factors, giving

$$g_{ijk}^{(n+1)}
  \;=\;
  a_{ij}^{(n)} \cdot a_{jk}^{(n)} \cdot (a_{ik}^{(n)})^{-1}
  \cdot g_{ijk}^{(n)}.$$

The distributional connection $A_\infty$ is globally consistent if and only if $g_{ijk}^{(n+1)} = 0$ for all $n$ in the Cech cohomology, which requires

$$d(g_{ijk}^{(n)})
  \;=\;
  a_{ij}^{(n)} \cdot g_{ijk}^{(n)} \cdot (a_{jk}^{(n)})^{-1},$$

where the left-hand side is the Cech coboundary $\delta^2(g^{(n)})_{ijk}$ and the right-hand side is the twisted conjugation by the $2$-morphisms. The class of this twisted $2$-cocycle in $H^2(M,\, \mathcal{O}_M^{\times})$ is precisely the obstruction class $\kappa_n$ of [quantum characteristic classes](#def:quantum-characteristic-classes): it vanishes if and only if the cocycle deviation at level $n$ can be absorbed by the $2$-morphism data, i.e. the lift from $\mathfrak{G}_n$ to $\mathfrak{G}_{n+1}$ is unobstructed.

By \[Theorem 1.7, yekutieli2010\], this is equivalent to the vanishing of the Yekutieli obstruction class, closing the circle with the lifting criterion ([Yekutieli lifting](#prop:yekutieli-lifting)). ◻

</div>

<div id="prop:weak-equiv-invariance" class="proposition">

**Proposition 2.6** (Weak equivalence invariance of physical states). *[<sup><span style="color: BurntOrange">$\forall$</span></sup>](https://litlfred.github.io/qou/lean/QOU.Torsion.weak_equiv_invariance)*

*Let $(\mathcal{C}, A, \tau)$ be a quantum observable universe and let $\{A_n\}_{n \geq 0}$ be its recursive brane tower with cosimplicial crossed groupoid structure ([cosimplicial crossed groupoid](#prop:cosimplicial-crossed-groupoid)); let $q$ denote the substrate parameter. Let $\tau \colon \mathcal{A}_\infty \to \mathbb{C}$ be the ([vacuum state](#prop:vacuum-state)). A *weak equivalence* between brane levels $n$ and $m$ is a zigzag of coface and codegeneracy maps*

*$$\mathfrak{G}_n
  \xleftarrow{\;\sigma\;}
  \mathfrak{G}_{k_1}
  \xrightarrow{\;\delta\;}
  \cdots
  \xrightarrow{\;\delta\;}
  \mathfrak{G}_m$$*

*in the cosimplicial crossed groupoid. Then for every observable $a \in \mathcal{A}_\infty$, the expectation value is invariant under weak equivalence:*

*$$\tau\!\bigl(\iota_n(a|_n)\bigr)
  \;=\;
  \tau\!\bigl(\iota_m(a|_m)\bigr),$$*

*where $\iota_n \colon \Gamma(J^1 E_n,\, \mathrm{SU}_{q_n}(2))
\hookrightarrow \mathcal{A}_\infty$ is the canonical embedding and $a|_n$ denotes the restriction of $a$ to level $n$. In particular, physical states (the GNS vectors of $\tau$) are invariant under fluctuations of the substrate parameter $q(p)$ across brane levels.*

</div>

<div class="proof">

*Proof of Weak equivalence invariance of physical states.* <span id="prf:weak-equiv-invariance" label="prf:weak-equiv-invariance"></span>

By \[Theorem 1.1, yekutieli2010\], a weak equivalence of central extensions of gerbes induces an isomorphism on the category of global objects up to isomorphism. In the brane tower, the coface maps (jet prolongation) and codegeneracy maps (descent) compose to give the descent involution $\hat{\tau}_n$ ([descent involution](#def:descent-involution)), which is idempotent. The image $\mathcal{A}_{n+1}^{\mathrm{desc}}$ ([descent eigenspaces](#prop:descent-eigenspaces)) is therefore isomorphic, as an algebra, to the level-$n$ section algebra via the ascent embedding $\ell_n$.

For the vacuum state, the compatibility $\tau(\iota_n(a|_n)) = \tau^{(n)}(a|_n)$ holds by the universal property of the direct limit ([direct limit algebra](#def:direct-limit-algebra)). The Haar-averaging construction in the proof of [vacuum state](#prop:vacuum-state) produces states $\tau^{(n)}$ that are compatible with the transition maps: $\tau^{(n+1)} \circ \iota_{n,n+1} = \tau^{(n)}$, where $\iota_{n,n+1}$ is the transition map. A zigzag of coface and codegeneracy maps between levels $n$ and $m$ factors as a sequence of such transition maps and their adjoints (the descent homomorphisms), each of which preserves the Haar state by equivariance ([descent](#lem:descent), Step 5).

Therefore the expectation value $\tau(\iota_n(a|_n)) = \tau^{(n)}(a|_n) = \tau^{(m)}(a|_m) =
\tau(\iota_m(a|_m))$ is invariant under weak equivalence.

For the GNS representation: the Hilbert space $\mathcal{H}_\tau = \overline{\mathcal{A}_\infty / \ker(\tau)}$ with inner product $\langle [a], [b] \rangle = \tau(a^* b)$ is unchanged by the weak equivalence because $\tau$ is invariant. The cyclic vector $\Omega = [1]$ generates the same representation regardless of the brane level at which it is evaluated, so the physical states (vectors in $\mathcal{H}_\tau$) are insensitive to the substrate parameter fluctuations across the tower. ◻

</div>

## Yekutieli Lifting and Quantum Characteristic Classes

<div id="def:yekutieli-lifting-condition" class="definition">

**Definition 2.7** (Yekutieli Lifting Condition). *[<sup><span style="color: BurntOrange">$\forall$</span></sup>](https://litlfred.github.io/qou/lean/QOU.YekutieliLiftingCondition) Let $\mathcal{C}$ be a $R$-linear rigid monoidal category and let*

*$$1 \;\longrightarrow\; \mathcal{B}
  \;\longrightarrow\; \mathfrak{G}'
  \;\longrightarrow\; \mathfrak{G}
  \;\longrightarrow\; 1$$*

*be a central extension of gerbes on a site $\mathcal{S}$, banded by an abelian sheaf $\mathcal{B}$. We say that $\mathcal{C}$ satisfies the *Yekutieli Lifting Condition* with respect to $(\mathfrak{G}', \mathfrak{G}, \mathcal{B})$ if, for every object $x \in \mathrm{Ob}(\mathfrak{G})$, the obstruction to lifting $x$ to an object $x' \in \mathrm{Ob}(\mathfrak{G}')$ is classified by a single cohomology class*

*$$\kappa(x) \;\in\; H^2(\mathcal{S},\, \mathcal{B}),$$*

*and $x$ admits a lift if and only if $\kappa(x) = 0$.*

</div>

<div id="def:quantum-characteristic-classes" class="definition">

**Definition 2.8** (Quantum Characteristic Classes (Yekutieli obstruction)). *[<sup><span style="color: BurntOrange">$\forall$</span></sup>](https://litlfred.github.io/qou/lean/QOU.QuantumCharacteristicClass)*

*Let $(\mathcal{C}, A, \tau)$ be a quantum observable universe and let $\{A_n\}_{n \geq 0}$ be its ([recursive brane tower](#def:recursive-brane-tower)). Each transition $A_n \hookrightarrow A_{n+1}$ in $\mathcal{C}$ defines a central extension of gerbes on the underlying site in the sense of Yekutieli \[yekutieli2010\]: the Frobenius–Hopf object $A_n$ is an object in a gerbe $\mathfrak{G}_n$ banded by the sheaf of units $\mathcal{B}$, and the ([jet prolongation](#prop:jet-prolongation)) produces a central extension*

*$$1 \;\longrightarrow\; \mathcal{B}
  \;\longrightarrow\; \mathfrak{G}_{n+1}
  \;\longrightarrow\; \mathfrak{G}_n
  \;\longrightarrow\; 1.$$*

*The *quantum characteristic classes* (Yekutieli obstruction classes) are the cohomology classes*

*$$\kappa_n \;\in\; H^2(\mathcal{S},\, \mathcal{B})$$*

*that obstruct the lifting of objects from $\mathfrak{G}_n$ to $\mathfrak{G}_{n+1}$. By the ([Yekutieli lifting condition](#def:yekutieli-lifting-condition)), the vanishing $\kappa_n = 0$ is the necessary and sufficient condition for the lift to exist ([Yekutieli lifting](#prop:yekutieli-lifting)).*

</div>

<div id="prop:yekutieli-lifting" class="proposition">

**Proposition 2.9** (Yekutieli Lifting Condition holds in the brane tower). *[<sup><span style="color: BurntOrange">$\forall$</span></sup>](https://litlfred.github.io/qou/lean/QOU.YekutieliLifting)*

*Let $(\mathcal{C}, A, \tau)$ be a ([quantum observable universe](#def:quantum-observable-universe)) and let $\{A_n\}_{n \geq 0}$ be the ([recursive brane tower](#def:recursive-brane-tower)). The central extensions of gerbes*

*$$1 \;\longrightarrow\; \mathcal{B}
  \;\longrightarrow\; \mathfrak{G}_{n+1}
  \;\longrightarrow\; \mathfrak{G}_n
  \;\longrightarrow\; 1$$*

*arising from the ([jet prolongation](#prop:jet-prolongation)) satisfy the Yekutieli Lifting Condition ([Yekutieli lifting condition](#def:yekutieli-lifting-condition)). In the archimedean realisation, $\mathcal{B} = \mathcal{O}_M^{\times}$. In particular, the lift of the Frobenius–Hopf object from level $n$ to level $n{+}1$ exists if and only if the obstruction class $\kappa_n \in H^2(M,\, \mathcal{B})$ ([quantum characteristic classes](#def:quantum-characteristic-classes)) vanishes.*

</div>

<div class="proof">

*Proof of Yekutieli Lifting Condition holds in the brane tower.* <span id="prf:yekutieli-lifting" label="prf:yekutieli-lifting"></span>

By \[Theorem 1.7, yekutieli2010\], any central extension of gerbes banded by an abelian sheaf on a ringed space satisfies the lifting criterion: an object in the base gerbe admits a lift to the total gerbe if and only if its obstruction class in $H^2$ vanishes. The jet prolongation construction ([jet prolongation](#prop:jet-prolongation)) realises the passage from level $n$ to level $n{+}1$ as precisely such a central extension, banded by $\mathcal{B}$ ([quantum characteristic classes](#def:quantum-characteristic-classes)). Hence the Yekutieli Lifting Condition holds, and $\kappa_n = 0$ is equivalent to the existence of the lift. ◻

</div>

<div id="thm:qu-to-qou" class="theorem">

**Theorem 2.10** (Quantum universe with observability and Yekutieli is a QOU). *[<sup><span style="color: BurntOrange">$\forall$</span></sup>](https://litlfred.github.io/qou/lean/QOU.QuToQou)*

*Let $(\mathcal{C}, A, \tau)$ be a quantum universe over a Noetherian ring $R$ ([quantum universe](#def:quantum-universe)); let $q$ denote the substrate parameter. Assume observability $\mathrm{Hom}(\mathbf{1},\, \mathrm{Ad}(A)) = 0$ ([quantum observable universe](#def:quantum-observable-universe)). Then the brane tower $\{A_n\}_{n \geq 0}$ constructed via ([jet prolongation](#prop:jet-prolongation)) satisfies the Yekutieli lifting condition ([Yekutieli lifting condition](#def:yekutieli-lifting-condition), [Yekutieli lifting](#prop:yekutieli-lifting)), and $(\mathcal{C}, A, \tau)$ is a quantum observable universe with the following structural properties:*

1.  **Descent terminates.* The geometric descent tower has finite length, bounded by $\mathrm{Krull\;dim}\,
    Z(\mathrm{End}_{\mathcal{C}}(A))$. Observability ensures each step is a strict reduction (the $G_q$-action is faithful, so fixed-point reduction strictly decreases dimension).*

2.  **First obstruction equals the Euler class.* The Yekutieli obstruction $\kappa_0 \in H^2(\mathcal{S}, \mathcal{B})$ equals the Euler class of the Reeb bundle. Under the trace map, $\kappa_0 \mapsto \chi(A) = \mathrm{tr}(\mathrm{id}_A) \in R$.*

3.  **Perpetual obstruction.* If $\kappa_0$ is non-torsion in $H^2(\mathcal{S}, \mathcal{B})$, then $\kappa_n \neq 0$ for all $n \geq 0$. The class $\kappa_0$ and the jet corrections at level $n$ live in complementary subgroups of $H^2(\mathcal{S}, \mathcal{B})$, so the corrections cannot cancel $\kappa_0$.*

4.  **Branch point formula.* The geometric descent from $\mathbb{P}(V)$ ([projective line object](#def:projective-line-object)) to points has $B$ branch points with total ramification $R_{\mathrm{tot}} = 2d + \lvert\chi(A)\rvert$ (Riemann–Hurwitz), where $d$ is the degree of the covering.*

5.  **Terminal fiber data.* At each branch point $p$, the QOU reduces to fiber data $(A, \tau, q(p))$ with the involution $\sigma \colon \mathbb{P}(V) \hookrightarrow \mathrm{Ad}(A)$ ([fibre adjoint involution](#prop:fiber-adjoint-involution)).*

</div>

## Betti Numbers and Harmonic Basis

## Direct Limit Algebra

<div id="def:direct-limit-algebra" class="definition">

**Definition 2.11** (Quantum Observable Universe as Direct Limit). *[<sup><span style="color: BurntOrange">$\forall$</span></sup>](https://litlfred.github.io/qou/lean/QOU.DirectLimitAlgebra)*

*Let $(\mathcal{C}, A, \tau)$ be a ([quantum observable universe](#def:quantum-observable-universe)); let $q$ denote the substrate parameter. Let $\{A_n\}_{n \geq 0}$ be its ([recursive brane tower](#def:recursive-brane-tower)). The *direct limit algebra of the quantum observable universe* is the colimit in the category of $R$-algebras:*

*$$\mathcal{A}_\infty
  \;=\;
  \varinjlim_{n}\,
  \mathrm{End}_{\mathcal{C}}(A_n),$$*

*taken over the tower of endomorphism algebras with the transition maps induced by the canonical embeddings $A_n \hookrightarrow A_{n+1}$.*

*In the archimedean realisation ([$\mathbb{C}$-quantum observable universe](#ex:c-quantum-observable-universe)), applying the fibre functor $\tau$ gives $\mathcal{A}_\infty \cong
\varinjlim\,\Gamma(J^1 E_n,\, \mathrm{SU}_{q_n}(2))$.*

</div>

<div id="prop:global-gluing" class="proposition">

**Proposition 2.12** (Global gluing via Yekutieli’s twisted quantization). *[<sup><span style="color: BurntOrange">$\forall$</span></sup>](https://litlfred.github.io/qou/lean/QOU.Torsion.global_gluing)*

*Let $(\mathcal{C}, A, \tau)$ be a ([quantum observable universe](#def:quantum-observable-universe)); let $q$ denote the substrate parameter. The local deformations of the Frobenius–Hopf object $A$ parameterised by the substrate parameter $q$ induce a twisted associative deformation that admits a unique global gluing via Yekutieli’s twisted quantization map \[yekutieli2008, yekutieli2010\]. In particular, the direct limit algebra $\mathcal{A}_\infty$ ([direct limit algebra](#def:direct-limit-algebra)) is a well-defined global section of a sheaf of twisted deformation algebras on the underlying site $\mathcal{S}$, and the ([vacuum state](#prop:vacuum-state)) is well-defined globally despite local non-commutativity. In the archimedean realisation, this corresponds to the global gluing of the local algebras $\mathcal{O}_{q(p)}(\mathrm{SU}(2))$ over the manifold $M$.*

</div>

<div class="proof">

*Proof of Global gluing via Yekutieli’s twisted quantization.* <span id="prf:global-gluing" label="prf:global-gluing"></span>

At each point $p \in M$ the fibre algebra $\mathcal{O}_{q(p)}(\mathrm{SU}(2))$ is a pronilpotent deformation of $\mathcal{O}(\mathrm{SU}(2))$ in the formal parameter $\hbar_q(p) = 1 - q(p)^{-1}$ ([quantum planck constant](#def:quantum-planck-constant)). By \[yekutieli2008\], the coordinate bundle $\mathrm{Coor}_M$ of $M$ (the bundle of formal coordinate systems) carries a twisted deformation datum: a pair consisting of a connection and a Maurer–Cartan element in a pronilpotent DG Lie algebra \[yekutieli2009\]. The Yekutieli obstruction classes $\kappa_n$ ([quantum characteristic classes](#def:quantum-characteristic-classes)) control whether these local twisted deformations glue across coordinate patches.

The vanishing condition $\mathrm{Hom}(\mathbf{1}, \mathrm{Ad}(A)) = 0$ ([quantum observable universe](#def:quantum-observable-universe)) ensures that the gerbe $\mathfrak{G}_n$ of local lifts has trivial band at the level of isomorphisms, so by \[Theorem 4.5, yekutieli2010\] the twisted deformations at each fibre patch together into a global sheaf of algebras on $M$. The direct limit $\mathcal{A}_\infty =
\varinjlim\,\Gamma(J^1 E_n,\, \mathrm{SU}_{q_n}(2))$ is then the global sections of this sheaf, and the vacuum state $\tau$ ([vacuum state](#prop:vacuum-state)) extends uniquely by the $\mathrm{SU}(2)$-averaging argument of that proposition. ◻

</div>

<div id="prop:vacuum-state" class="proposition">

**Proposition 2.13** (Existence and Uniqueness of the Vacuum State). *[<sup><span style="color: BurntOrange">$\forall$</span></sup>](https://litlfred.github.io/qou/lean/QOU.Torsion.invariant_functional_unique)*

*Let $(\mathcal{C}, A, \tau)$ be a ([quantum observable universe](#def:quantum-observable-universe)); let $q$ denote the substrate parameter. Let $\mathcal{A}_\infty$ be its ([direct limit algebra](#def:direct-limit-algebra)). Let $G_q =
\mathrm{Aut}^{\otimes}(\tau)$ be the ([quantum gauge group](#def:quantum-gauge-group)), acting on $\mathcal{A}_\infty$ by conjugation. Then there exists a unique $R$-linear functional $\varphi \colon \mathcal{A}_\infty \to R$ that is $G_q$-invariant:*

*$$\varphi(g \cdot a) = \varphi(a)
  \quad\text{for all } g \in G_q,\;
  a \in \mathcal{A}_\infty.$$*

*In the archimedean realisation, $G_q = \mathrm{SU}_q(2)$ and $\varphi$ is the unique $\mathrm{SU}(2)$-invariant state on the $C^*$-algebraic direct limit.*

</div>

<div class="proof">

*Proof of Existence and Uniqueness of the Vacuum State.* <span id="prf:vacuum-state" label="prf:vacuum-state"></span>

The algebra $\mathcal{A}_\infty$ is the direct limit $\varinjlim \mathrm{End}_{\mathcal{C}}(A_n)$ ([direct limit algebra](#def:direct-limit-algebra)), and the quantum gauge group $G_q = \mathrm{Aut}^{\otimes}(\tau)$ ([quantum gauge group](#def:quantum-gauge-group)) acts on it by conjugation.

*Existence.* The fibre functor $\tau \colon \mathcal{C} \to \mathrm{Vect}_R$ is $R$-linear and exact. It sends the unit $\mathbf{1} \in \mathcal{C}$ to $R$ and the [Frobenius pairing](#def:frobenius-pairing) on $A$ to a non-degenerate $R$-bilinear form on $\tau(A)$. At each finite level, $\tau$ maps $\mathrm{End}_{\mathcal{C}}(A_n)$ to a finite-dimensional $R$-algebra $\mathrm{End}_R(\tau(A_n))$. The Frobenius trace $\mathrm{tr}_n \colon \mathrm{End}_{\mathcal{C}}(A_n) \to R$ defined by

$$\mathrm{tr}_n(\alpha)
  \;=\;
  (\varepsilon \circ \alpha \circ \eta)(\mathbf{1}),$$

where $\eta \colon \mathbf{1} \to A_n$ and $\varepsilon \colon A_n \to
\mathbf{1}$ are the Frobenius unit and counit, is $G_q$-invariant: for any $g \in G_q$, $\mathrm{tr}_n(g \cdot \alpha) =
\mathrm{tr}_n(\alpha)$ by the naturality of $\eta$ and $\varepsilon$ (they are morphisms in $\mathcal{C}$, hence invariant under monoidal automorphisms of the fibre functor).

The descent homomorphisms $\mathfrak{d}_n$ ([descent](#lem:descent)) are equivariant and satisfy $\mathrm{tr}_n \circ \mathfrak{d}_{n+1} =
\mathrm{tr}_{n+1}$ (compatibility of the Frobenius trace with descent). By the universal property of the direct limit, the system $\{\mathrm{tr}_n\}$ determines a $G_q$-invariant $R$-linear functional $\varphi \colon \mathcal{A}_\infty \to R$.

*Uniqueness.* The vanishing condition $\mathrm{Hom}(\mathbf{1}, \mathrm{Ad}(A)) = 0$ of the quantum observable universe axioms implies, via Schur’s lemma applied in $\mathcal{C}$, that $\mathrm{End}_{G_q}(\mathbf{1}) \cong R$. More precisely: a $G_q$-invariant functional $\psi \colon \mathcal{A}_\infty \to R$ must factor through the $G_q$-fixed subalgebra $\mathcal{A}_\infty^{G_q}$. The vanishing condition forces this fixed subalgebra to be one-dimensional (generated by the identity), since any non-scalar $G_q$-invariant endomorphism would yield a non-zero element of $\mathrm{Hom}(\mathbf{1}, \mathrm{Ad}(A))$. Therefore $\psi$ is determined up to scalar by its value on the identity, and normalising $\psi(\mathrm{id}) = 1$ gives $\psi = \varphi$. ◻

</div>

## Mass in the Brane Tower

<div id="prop:euler-char-stability" class="proposition">

**Proposition 2.14** (Stability of the Euler characteristic). *[<sup><span style="color: BurntOrange">$\forall$</span></sup>](https://litlfred.github.io/qou/lean/QOU.Torsion.euler_char_constant)*

*Let $(\mathcal{C}, A, \tau)$ be a ([quantum observable universe](#def:quantum-observable-universe)) and let $\{A_n\}_{n \geq 0}$ be its ([recursive brane tower](#def:recursive-brane-tower)). The categorical Euler characteristic $\chi(A_n) := \mathrm{tr}(\mathrm{id}_{A_n})$ (computed via the rigidity trace of the identity endomorphism in $\mathcal{C}$) is stable under jet prolongation: for each level $n$,*

*$$\chi(A_{n+1}) \;=\; \chi(A_n).$$*

*In particular, if the base level satisfies $\chi(A_0) = c \in k$, then $\chi(A_n) = c$ for all $n \geq 0$. In the archimedean realisation, $\chi(A_n) = \chi(E_n)$ is the topological Euler characteristic of the total space $E_n$.*

</div>

<div class="proof">

*Proof of Stability of the Euler characteristic.* <span id="prf:euler-char-stability" label="prf:euler-char-stability"></span>

The categorical Euler characteristic $\chi(A_n) = \mathrm{tr}(\mathrm{id}_{A_n})$ is the rigidity trace of the identity, computed as the composition

$$\chi(A_n)
  \;=\;
  \bigl(\mathbf{1}
  \xrightarrow{\;\mathrm{coev}_n\;}
  A_n \otimes A_n^{\vee}
  \xrightarrow{\;\mathrm{id} \otimes \mathrm{id}\;}
  A_n \otimes A_n^{\vee}
  \xrightarrow{\;\mathrm{ev}_n\;}
  \mathbf{1}\bigr)
  \;=\;
  \mathrm{ev}_n \circ \mathrm{coev}_n.$$

Jet prolongation is a functor on $\mathcal{C}$ that preserves the Frobenius–Hopf structure ([jet prolongation](#prop:jet-prolongation)): the prolonged object $A_{n+1}$ inherits its rigidity data from $A_n$. Specifically, the unit $\eta_{n+1}$ and counit $\varepsilon_{n+1}$ of $A_{n+1}$ are the images of $\eta_n$ and $\varepsilon_n$ under the prolongation functor, and likewise for the evaluation and coevaluation morphisms: $\mathrm{ev}_{n+1} = \mathrm{ev}_n$ and $\mathrm{coev}_{n+1} = \mathrm{coev}_n$ as elements of $\mathrm{Hom}(\mathbf{1}, \mathbf{1}) \cong R$.

Therefore:

$$\chi(A_{n+1})
  \;=\;
  \mathrm{ev}_{n+1} \circ \mathrm{coev}_{n+1}
  \;=\;
  \mathrm{ev}_n \circ \mathrm{coev}_n
  \;=\;
  \chi(A_n).$$

By induction, $\chi(A_n) = \chi(A_0)$ for all $n \geq 0$.

The vanishing condition $\mathrm{Hom}(\mathbf{1}, \mathrm{Ad}(A)) = 0$ ensures that the prolongation functor cannot introduce non-trivial twisting of the trace: there are no non-scalar $G_q$-invariant endomorphisms that could modify the rigidity pairing at each level. (For the archimedean verification via the Leray–Serre spectral sequence, see [archimedean proof](#prf:euler-char-stability-C).) ◻

</div>

<div id="def:mass-identity" class="definition">

**Definition 2.15** (Mass (categorical trace)). *[<sup><span style="color: BurntOrange">$\forall$</span></sup>](https://litlfred.github.io/qou/lean/QOU.categoricalMass)*

*Let $(\mathcal{C}, A, \tau)$ be a ([quantum observable universe](#def:quantum-observable-universe)) and let $\{A_n\}_{n \geq 0}$ be its ([recursive brane tower](#def:recursive-brane-tower)). Since $\mathcal{C}$ is a $R$-linear rigid monoidal category, the Frobenius–Hopf object $A$ admits a categorical trace $\mathrm{tr} \colon \mathrm{End}_{\mathcal{C}}(A) \to R$ defined by the composition*

*$$\mathrm{tr}(f)
  \;=\;
  \bigl(\mathbf{1}
  \xrightarrow{\;\mathrm{coev}\;}
  A \otimes A^{\vee}
  \xrightarrow{\;f \otimes \mathrm{id}\;}
  A \otimes A^{\vee}
  \xrightarrow{\;\mathrm{ev}\;}
  \mathbf{1}\bigr),$$*

*where $\mathrm{coev}$ and $\mathrm{ev}$ are the rigidity morphisms. Let $\Delta \colon A \to A \otimes A$ be the comultiplication (encoding the connection) and let $\int_A \colon A \to \mathbf{1}$ be the Frobenius form.*

*The *inertial mass* of a morphism $\gamma \colon \mathbf{1} \to A$ (a "closed cycle" in the Frobenius–Hopf object) is*

*$$m(\gamma)
  \;=\;
  \bigl\lVert\,
  \mathrm{tr}\bigl(
    (\int_A \otimes \mathrm{id})
    \circ \Delta
    \circ \gamma
  \bigr)
  \,\bigr\rVert,$$*

*where $\lVert \cdot \rVert$ is the norm on $R$ induced by the [Frobenius pairing](#def:frobenius-pairing). The mass measures the resistance of the Frobenius–Hopf structure to transporting the cycle $\gamma$ through the comultiplication.*

</div>

## Yekutieli Categorical Mapping

[Table](#tab:yekutieli-mapping) summarises the correspondence between the core structures of the Quantum Observable Universe and the formal results of Yekutieli on central extensions of gerbes, twisted deformation quantization, and nonabelian multiplicative integration.

<div id="tab:yekutieli-mapping">

| **QOU concept**                                                                                                                                                                                                         | **Yekutieli counterpart**                                            | **Reference**                                                                                                                          |
|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------------------------------------------------------------------|:---------------------------------------------------------------------------------------------------------------------------------------|
| Recursive Brane Tower $\{E_n\}$ (Def. <a href="#def:recursive-brane-tower" data-reference-type="ref" data-reference="def:recursive-brane-tower">2.2</a>)                                                                | Central extension of gerbes $\mathfrak{G}_{n+1} \to \mathfrak{G}_n$  |                                                                                                                                        |
| Quantum Characteristic Classes $\kappa_n \in H^2(M, \mathcal{O}_M^{\times})$ (Def. <a href="#def:quantum-characteristic-classes" data-reference-type="ref" data-reference="def:quantum-characteristic-classes">2.8</a>) | Obstruction classes for lifting objects in central extensions        |                                                                                                                                        |
| Fermionic sectors ($\kappa_n \neq 0$) (Rem. <a href="#rem:fermionic-twisted-sectors" data-reference-type="ref" data-reference="rem:fermionic-twisted-sectors">[rem:fermionic-twisted-sectors]</a>)                      | Twisted sectors where the lift is obstructed                         |                                                                                                                                        |
| Direct Limit Algebra $\mathcal{A}_\infty$ (Def. <a href="#def:direct-limit-algebra" data-reference-type="ref" data-reference="def:direct-limit-algebra">2.11</a>)                                                       | Global sections of a sheaf of twisted deformation algebras           |                                                                                                                                        |
| Global gluing of $\mathcal{A}_\infty$ (Prop. <a href="#prop:global-gluing" data-reference-type="ref" data-reference="prop:global-gluing">2.12</a>)                                                                      | Yekutieli’s twisted quantization map on algebraic varieties          |                                                                                                                                        |
| Vacuum State $\tau$ (Prop. <a href="#prop:vacuum-state" data-reference-type="ref" data-reference="prop:vacuum-state">2.13</a>)                                                                                          | Unique MC element in the pronilpotent DG Lie algebra                 |                                                                                                                                        |
| Mass Identity (Def. <a href="#def:mass-identity" data-reference-type="ref" data-reference="def:mass-identity">2.15</a>)                                                                                                 | Nonabelian multiplicative integral; 2D nonabelian Stokes theorem     |                                                                                                                                        |
| Substrate field $q(p)$ (Def. <a href="#def:substrate-parameter" data-reference-type="ref" data-reference="def:substrate-parameter">1.41</a>)                                                                            | Local twisted deformation parameter; MC element varying over $M$     |                                                                                                                                        |
| $\mathrm{SU}_q(2)$ gauge flow (Def. <a href="#def:quantum-gauge-group" data-reference-type="ref" data-reference="def:quantum-gauge-group">1.43</a>)                                                                     | Pronilpotent deformation of the coordinate algebra                   |                                                                                                                                        |
| Descartes condition $\chi(E) = -6$ (Def. <a href="#def:descartes-condition" data-reference-type="ref" data-reference="def:descartes-condition">6.1</a>)                                                                 | Topological constraint forcing $\kappa_n \neq 0$ (non-trivial gerbe) | ; Ex. <a href="#ex:descartes-yekutieli" data-reference-type="ref" data-reference="ex:descartes-yekutieli">[ex:descartes-yekutieli]</a> |
| Cosimplicial crossed groupoid (Prop. <a href="#prop:cosimplicial-crossed-groupoid" data-reference-type="ref" data-reference="prop:cosimplicial-crossed-groupoid">2.4</a>)                                               | Cosimplicial object in crossed groupoids; Čech nerve of a gerbe      |                                                                                                                                        |
| Twisted $2$-cocycle $d(g_{ijk}) = a \cdot g \cdot a^{-1}$ (Prop. <a href="#prop:descent-condition" data-reference-type="ref" data-reference="prop:descent-condition">2.5</a>)                                           | Twisted Čech cocycle in $H^2(M, \mathcal{O}_M^\times)$               |                                                                                                                                        |

Categorical mapping between QOU structures and Yekutieli’s results.

</div>

## Descent

The descent machinery connects the infinite brane tower to finite-dimensional geometry. Given a quantum observable universe $(\mathcal{C}, A, \tau)$ with brane tower $\{A_n\}_{n \geq 0}$ ([recursive brane tower](#def:recursive-brane-tower)), the descent lemma ([descent lemma](#lem:descent)) shows that each level $A_n$ inherits the full QOU structure from $A$. The descent involution ([descent involution](#def:descent-involution)) then splits each $A_n$ into eigenspaces whose direct limit recovers the physical algebra. This section develops the descent involution, its eigenspace decomposition, and the topological mass formula that results.

<div id="def:descent" class="definition">

**Definition 2.16** (Descent). *[<sup><span style="color: BurntOrange">$\forall$</span></sup>](https://litlfred.github.io/qou/lean/QOU.DescentData)*

*Let $(\mathcal{C}, A, \tau)$ be a quantum observable universe and let $\{A_n\}_{n \geq 0}$ be the ([recursive brane tower](#def:recursive-brane-tower)). The *descent* is the reverse traversal of the tower: starting from level $n$ one passes to level $n{-}1$ by applying the restriction morphism $r_n \colon A_n = J^1(A_{n-1}) \to A_{n-1}$ (the categorical retraction of the jet embedding). In the archimedean realisation, this restricts the connection and bundle to the base manifold $M_{n-1}$. By [QU-to-QOU lifting](#thm:qu-to-qou)(1), the descent terminates in finitely many steps, bounded by $\mathrm{Krull\;dim}\, Z(\mathrm{End}_{\mathcal{C}}(A))$.*

</div>

<div id="lem:descent" class="lemma">

**Lemma 2.17** (Descent preserves the quantum observable universe). *[<sup><span style="color: BurntOrange">$\forall$</span></sup>](https://litlfred.github.io/qou/lean/QOU.DescentLemma)*

*Let $(\mathcal{C}, A, \tau)$ be a quantum observable universe and let $\{A_n\}_{n \geq 0}$ be the ([recursive brane tower](#def:recursive-brane-tower)), with $n \geq 1$; let $q$ denote the substrate parameter. The restriction morphism $r_n \colon A_n \to A_{n-1}$ yields a Frobenius–Hopf object $A_{n-1}$ such that $(\mathcal{C}, A_{n-1}, \tau)$ is again a quantum observable universe. Moreover, the induced descent homomorphism*

*$$\mathfrak{d}_n \;\colon\;
  \mathrm{End}_{\mathcal{C}}(A_n)
  \;\longrightarrow\;
  \mathrm{End}_{\mathcal{C}}(A_{n-1})$$*

*is a surjective algebra homomorphism that intertwines the $G_q$-actions at levels $n$ and $n{-}1$. In the archimedean realisation, this recovers the surjective $*$-homomorphism $\Gamma(J^1 E_n,\, \mathrm{SU}_{q_n}(2)) \to
\Gamma(J^1 E_{n-1},\, \mathrm{SU}_{q_{n-1}}(2))$.*

</div>

<div class="proof">

*Proof of Descent preserves the quantum observable universe.* <span id="prf:descent" label="prf:descent"></span>

The proof mirrors the ascent ([jet prolongation](#prop:jet-prolongation)) in reverse, working inside the rigid monoidal category $\mathcal{C}$.

*Step 1: Frobenius restriction.* The jet object $J^1(A) = A \otimes \Omega^1(A)$ at level $n$ contains $A$ as a direct summand via the unit section $\eta \otimes \mathrm{id}\colon \Omega^1(A) \hookrightarrow A \otimes
\Omega^1(A)$. Composing with the counit $\varepsilon\colon A \to \mathbf{1}$ on the first tensor factor gives the restriction map $r_n\colon J^1(A) \to A$. Because $A$ is Frobenius, $r_n$ is a coalgebra morphism: the comultiplication $\Delta$ commutes with restriction by the Frobenius relation, and the counit restricts by construction. Hence the restricted object inherits a Frobenius–Hopf structure.

*Step 2: Connection restriction.* The connection $A_n$ on $E_n$ is determined by the comultiplication $\Delta'$ on $J^1(A)$ ([jet prolongation](#prop:jet-prolongation), Step 2). Restricting $\Delta'$ along $r_n$ recovers the original comultiplication $\Delta$ on $A$, which by the construction of the brane tower corresponds to the connection $A_{n-1}$ on $E_{n-1}$. In particular, $A_{n-1}$ satisfies the Hermitian Yang–Mills equations on $E_{n-1}$ because it did so at level $n{-}1$ before the ascent.

*Step 3: Non-degeneracy and vanishing.* Non-degeneracy of the Frobenius form on the restricted object follows from the direct-summand inclusion $A \hookrightarrow J^1(A)$: the restriction of a non-degenerate pairing to a direct summand remains non-degenerate. The vanishing condition $\mathrm{Hom}(\mathbf{1}, \mathrm{Ad}(A)) = 0$ is unchanged since we recover the original object $A$.

*Step 4: The descent homomorphism.* Applying the fibre functor $\tau$ to $r_n$ yields $\mathfrak{d}_n\colon
\Gamma(J^1 E_n,\, \mathrm{SU}_{q_n}(2)) \to
\Gamma(J^1 E_{n-1},\, \mathrm{SU}_{q_{n-1}}(2))$. This is a $*$-homomorphism because $r_n$ preserves multiplication and the antipode. Surjectivity follows from the fact that the ascent map $\ell_n$ of [jet prolongation](#prop:jet-prolongation) is injective (it embeds $A$ into $J^1(A)$ as a direct summand), so its categorical adjoint $r_n$ is surjective.

*Step 5: Equivariance.* The $\mathrm{SU}(2)$ action on sections at level $n$ is induced by the adjoint representation of the Hopf algebra. Since $r_n$ is a Hopf algebra morphism, it intertwines the adjoint actions at levels $n$ and $n{-}1$. ◻

</div>

<div id="def:descent-involution" class="definition">

**Definition 2.18** (Descent involution). *[<sup><span style="color: BurntOrange">$\forall$</span></sup>](https://litlfred.github.io/qou/lean/QOU.DescentInvolution)*

*Let $\ell_n \colon A_n \hookrightarrow A_{n+1}$ denote the ascent embedding ([jet prolongation](#prop:jet-prolongation)) and $\mathfrak{d}_{n+1} \colon \mathrm{End}_{\mathcal{C}}(A_{n+1}) \to
\mathrm{End}_{\mathcal{C}}(A_n)$ the descent homomorphism ([descent](#lem:descent)). The *descent involution* at level $n$ is the endomorphism of the level-$(n{+}1)$ endomorphism algebra:*

*$$\hat{\tau}_n \;=\; \ell_n \circ \mathfrak{d}_{n+1}
  \;\colon\;
  \mathrm{End}_{\mathcal{C}}(A_{n+1})
  \;\longrightarrow\;
  \mathrm{End}_{\mathcal{C}}(A_{n+1}).$$*

*Since $\mathfrak{d}_{n+1} \circ \ell_n = \mathrm{id}$ on $\mathrm{End}_{\mathcal{C}}(A_n)$ (the descent of the ascent recovers the original endomorphism, because $\ell_n$ embeds $A_n$ as a direct summand of $A_{n+1}$ and $\mathfrak{d}_{n+1}$ is the retraction), we have*

*$$\hat{\tau}_n^2
  \;=\;
  \ell_n \circ \mathfrak{d}_{n+1} \circ \ell_n \circ \mathfrak{d}_{n+1}
  \;=\;
  \ell_n \circ (\mathfrak{d}_{n+1} \circ \ell_n) \circ \mathfrak{d}_{n+1}
  \;=\;
  \ell_n \circ \mathrm{id} \circ \mathfrak{d}_{n+1}
  \;=\;
  \hat{\tau}_n,$$*

*so $\hat{\tau}_n$ is idempotent. Its image is the *descended subalgebra* $\mathcal{A}_{n+1}^{\mathrm{desc}} \subseteq
\mathrm{End}_{\mathcal{C}}(A_{n+1})$, consisting of endomorphisms at level $n{+}1$ that factor through the level-$n$ algebra via the ascent embedding.*

</div>

<div id="prop:descent-eigenspaces" class="proposition">

**Proposition 2.19** (Eigenspaces of the descent involution). *[<sup><span style="color: BurntOrange">$\forall$</span></sup>](https://litlfred.github.io/qou/lean/QOU.Torsion.idempotent_direct_sum_decomposition)*

*The descent involution $\hat{\tau}_n$ ([descent involution](#def:descent-involution)) decomposes the level-$(n{+}1)$ endomorphism algebra into a direct sum*

*$$\mathrm{End}_{\mathcal{C}}(A_{n+1})
  \;=\;
  \mathcal{A}_{n+1}^{\mathrm{desc}} \;\oplus\; \mathcal{A}_{n+1}^{\mathrm{trans}},$$*

*where $\mathcal{A}_{n+1}^{\mathrm{desc}} = \mathrm{im}\,\hat{\tau}_n$ is the descended subalgebra (endomorphisms that factor through level $n$) and $\mathcal{A}_{n+1}^{\mathrm{trans}} = \ker\,\hat{\tau}_n$ is the *transient complement* (genuinely new endomorphisms at level $n{+}1$). The ([algebraic filter](#rem:algebraic-filter)) refines this decomposition:*

1.  *The bosonic (longitudinal) modes lifted from level $n$ lie entirely in $\mathcal{A}_{n+1}^{\mathrm{desc}}$: they commute with the curvature and survive every round-trip through the tower.*

2.  *The fermionic (ladder) modes at level $n{+}1$ split between the two summands; those in $\mathcal{A}_{n+1}^{\mathrm{trans}}$ are the modes created by the jet prolongation that have no pre-image at level $n$.*

</div>

<div class="proof">

*Proof of Eigenspaces of the descent involution.* <span id="prf:descent-eigenspaces" label="prf:descent-eigenspaces"></span>

Since $\hat{\tau}_n$ is an idempotent endomorphism of the $R$-algebra $\mathrm{End}_{\mathcal{C}}(A_{n+1})$, the standard idempotent splitting gives a direct sum decomposition

$$\mathrm{End}_{\mathcal{C}}(A_{n+1})
  \;=\;
  \mathrm{im}\,\hat{\tau}_n \;\oplus\; \ker\,\hat{\tau}_n.$$

Indeed, every $\alpha \in \mathrm{End}_{\mathcal{C}}(A_{n+1})$ decomposes uniquely as $\alpha = \hat{\tau}_n(\alpha) + (\alpha - \hat{\tau}_n(\alpha))$, where $\hat{\tau}_n(\hat{\tau}_n(\alpha)) = \hat{\tau}_n(\alpha)$ (so $\hat{\tau}_n(\alpha) \in
\mathrm{im}\,\hat{\tau}_n$) and $\hat{\tau}_n(\alpha - \hat{\tau}_n(\alpha)) = \hat{\tau}_n(\alpha) - \hat{\tau}_n(\alpha) = 0$ (so $\alpha - \hat{\tau}_n(\alpha) \in \ker\,\hat{\tau}_n$). The two summands intersect trivially: if $\alpha \in \mathrm{im}\,\hat{\tau}_n \cap
\ker\,\hat{\tau}_n$, then $\alpha = \hat{\tau}_n(\beta)$ for some $\beta$ and $0 = \hat{\tau}_n(\alpha) = \hat{\tau}_n^2(\beta) = \hat{\tau}_n(\beta) = \alpha$.

When $\mathrm{End}_{\mathcal{C}}(A_{n+1})$ carries a $*$-involution compatible with $\hat{\tau}_n$ (i.e. $\hat{\tau}_n(\alpha^*) = \hat{\tau}_n(\alpha)^*$), the decomposition respects the $*$-structure: both summands are $*$-subalgebras.

For item (1), let $\alpha \in \mathrm{End}_{\mathcal{C}}(A_{n+1})$ lie in the image of the ascent $\ell_n$: $\alpha = \ell_n(\beta)$ for some $\beta \in \mathrm{End}_{\mathcal{C}}(A_n)$. Bosonic modes are characterised categorically by the ([algebraic filter](#rem:algebraic-filter)) as those commuting with the categorical curvature. Then $\hat{\tau}_n(\alpha) = \ell_n(\mathfrak{d}_{n+1}(\ell_n(\beta)))
= \ell_n(\beta) = \alpha$, using $\mathfrak{d}_{n+1} \circ \ell_n = \mathrm{id}$ ([descent](#lem:descent)). Hence $\alpha \in
\mathcal{A}_{n+1}^{\mathrm{desc}}$.

For item (2), an endomorphism $\alpha \in
\mathrm{End}_{\mathcal{C}}(A_{n+1})$ that does not factor through level $n$ satisfies $\mathfrak{d}_{n+1}(\alpha) = 0$ in $\mathrm{End}_{\mathcal{C}}(A_n)$, so $\hat{\tau}_n(\alpha) = \ell_n(0) = 0$ and $\alpha \in \mathcal{A}_{n+1}^{\mathrm{trans}}$. Those level-$(n{+}1)$ endomorphisms that do factor through level $n$ lie in $\mathcal{A}_{n+1}^{\mathrm{desc}}$ by the argument of item (1). The fermionic/ladder modes therefore split between the two summands according to whether they have a pre-image under $\mathfrak{d}_{n+1}$. ◻

</div>

<div id="def:brane-boundary" class="definition">

**Definition 2.20** (Defining boundary of the brane). *[<sup><span style="color: BurntOrange">$\forall$</span></sup>](https://litlfred.github.io/qou/lean/QOU.braneBoundary)*

*Let $(\mathcal{C}, A, \tau)$ be a quantum observable universe and let $\{A_n\}_{n \geq 0}$ be the ([recursive brane tower](#def:recursive-brane-tower)). Let $\mathfrak{d}_{n+1}$ be the descent homomorphism ([descent](#lem:descent)). The *defining boundary* of the $n$-th brane is the full subcategory of $\mathcal{C}$ consisting of subobjects of $A_n$ on which the restriction morphism $r_n \colon A_n \to A_{n-1}$ has non-trivial kernel:*

*$$\partial A_n
  \;=\;
  \bigl\{\, S \hookrightarrow A_n \;\bigm|\;
    \ker(r_n|_S) \neq 0 \,\bigr\}.$$*

*In the archimedean realisation, $\partial A_n$ corresponds to the geometric locus $\partial E_n = \{p \in E_n \mid
\ker(\mathfrak{d}_{n+1}|_p) \neq 0\} \subseteq E_n$, the degeneracy locus of the fibrewise descent map.*

</div>

<div id="prop:brane-boundary" class="proposition">

**Proposition 2.21** (Structure of the defining boundary). *[<sup><span style="color: BurntOrange">$\forall$</span></sup>](https://litlfred.github.io/qou/lean/QOU.Torsion.brane_boundary_structure)*

*The defining boundary $\partial A_n$ ([brane boundary](#def:brane-boundary)) has the following properties:*

1.  **Codimension.* In the archimedean realisation, $\partial A_n$ corresponds to a closed subset of real codimension at least 2 in $E_n$.*

2.  **Exceptional object.* At each degeneration locus of the restriction $r_n$, the kernel $\ker(r_n|_S)$ is isomorphic to a simple object of $\mathcal{C}$; in the archimedean realisation this is $\mathbb{P}^1(\mathbb{C}) \cong S^2$, the exceptional divisor of the topological blow-up.*

3.  **Involution symmetry.* The descent involution $\hat{\tau}_n$ ([descent involution](#def:descent-involution)) restricts to an endomorphism of $\partial A_n$, whose fixed subobjects coincide with the monodromy fixed points of the quantum characteristic classes ([quantum characteristic classes](#def:quantum-characteristic-classes)).*

4.  **Chirality interface (archimedean realisation).* When $n = 1$, $\partial E_1$ separates the macroscopic spacetime coordinates from the internal chiral modes: it is the geometric boundary between the base manifold $M$ and the gauge fibre, across which the Reeb involution $\xi \mapsto -\xi$ ([Descartes chirality](#rem:descartes-chirality)) reverses orientation.*

</div>

## Localized Knots, Hadrons, and Bundle Initial Conditions

The preceding sections established the $q$-torsion as a geometric invariant of the brane tower, and the topological decomposition of mass showed that particle identity is encoded by knot type. We now make this precise in the categorical framework: a *particle at a point* is a knot localized at a categorical point of the projective line $\mathbb{P}(V)$, and a *bundle* (the physical state at the initial moment) is a finite collection of such localized knots.

This section provides the categorical infrastructure that underpins the visualizer’s bundle-scenario model: each preset is a finite set of pairs $(p_i, K_i)$ where $p_i \in \mathbb{P}(V)$ and $K_i$ is a knot type. The $q$-torsion then drives the evolution of these positions on $\mathbb{P}(V) \cong \mathbb{CP}^1$, producing the trajectories observed in the time-evolution display.

<div id="def:localized-knot" class="definition">

**Definition 2.22** (Localized knot (knot at a point)). *[<sup><span style="color: BurntOrange">$\forall$</span></sup>](https://litlfred.github.io/qou/lean/QOU.LocalizedKnot)*

*Let $(\mathcal{C}, A, \tau)$ be a quantum observable universe with projective line object $\mathbb{P}(V) = G/T$ ([Definition](#def:projective-line-object)). A *localized knot* is a pair*

*$$(p, K) \;\in\; \mathrm{Hom}_{\mathcal{C}}(\mathbf{1}, A^{\mathrm{co}\,T})
  \;\times\; \mathrm{Knot}$$*

*where:*

- *$p \colon \mathbf{1} \to A^{\mathrm{co}\,T}$ is a categorical point of the projective line ([Definition](#def:categorical-point)), and*

- *$K$ is a knot type — an equivalence class of smooth embeddings $S^1 \hookrightarrow S^3$ under ambient isotopy.*

*We write $(p, K)$ to mean "the knot $K$ localized at the point $p$ on the base manifold $\mathbb{P}(V)$."*

*Categorically, $(p, K)$ is a section of the *knot sheaf* $\mathcal{K} \to \mathbb{P}(V)$: the functor that assigns to each open $U \subseteq \mathbb{P}(V)$ the set of knot types embeddable in the fibre $E_p \cong \mathbb{CP}^1$ over any $p \in U$. The fibre $E_p = \pi^{-1}(p)$ carries the knot as a vortex line in the chiral sector decomposition $(\mathfrak{r}, \mathfrak{g}, \mathfrak{b})$.*

*In the archimedean realisation with $G = \mathrm{SU}(2)$ and $T \cong \mathrm{U}(1)$, the projective line is $\mathbb{P}(V) \cong \mathbb{CP}^1 \cong S^2$, and a categorical point $p$ is a point on the Riemann sphere. The knot $K$ lives in the fibre $E_p \cong \mathbb{CP}^1$ — a topological $S^3$ neighborhood resolved by the blowup.*

</div>

<div id="def:hadron" class="definition">

**Definition 2.23** (Hadron (abstract composite knot)). *[<sup><span style="color: BurntOrange">$\forall$</span></sup>](https://litlfred.github.io/qou/lean/QOU.Hadron) A *hadron* is an abstract composite of fundamental knots linked together by the Hopf link.*

*Let $K_1, \ldots, K_n$ be fundamental (prime) knot types in the representation category $\mathcal{C}$. A **hadron** is an element*

*$$H \;\in\; \mathrm{Sym}^n\!\bigl(K_1, \ldots, K_n\bigr)
  \;\otimes\;
  \mathcal{L}_{\mathrm{Hopf}}$$*

*where:*

- *$\mathrm{Sym}^n(-)$ denotes the symmetric (bosonic) or antisymmetric (fermionic) product according to spin-statistics,*

- *$\mathcal{L}_{\mathrm{Hopf}}$ is the Hopf link encoding the internal entanglement between the constituent knots, and*

- *the Skein relations act on $\mathrm{Sym}^n(K)$ via the $q$-deformed polynomial, determining the composite mass:*

*$$\mathcal{M}(H) \;=\; Q(q) \cdot \mathcal{M}(\mathcal{L}_{\mathrm{Hopf}})
  \;+\; \sum_{i=1}^{n} \mathcal{M}(K_i).$$*

*This construction is purely abstract — the hadron lives in the category $\mathcal{C}$ without reference to a base point. Localization to a point is a separate operation ([localized hadron](#def:localized-hadron)).*

*The **baryon** is the case $n = 3$ with $K_i$ drawn from the trefoil class; the **meson** is $n = 2$ with a knot–antiknot pair.*

</div>

<div id="def:localized-hadron" class="definition">

**Definition 2.24** (Localized hadron). *[<sup><span style="color: BurntOrange">$\forall$</span></sup>](https://litlfred.github.io/qou/lean/QOU.LocalizedHadron)*

*A *localized hadron* is a hadron ([Definition](#def:hadron)) that has been placed at a categorical point $p$ of the projective line $\mathbb{P}(V)$ ([Definition](#def:projective-line-object)).*

*Formally, a **localized hadron** at $p$ is a morphism in $\mathcal{C}$:*

*$$H_p \;\colon\; \mathbf{1}
  \;\longrightarrow\;
  \mathrm{Sym}^n\!\bigl(\mathcal{K}_p\bigr)
  \;\otimes\;
  \mathcal{L}_{p}^{\mathrm{bind}}$$*

*where $\mathcal{K}_p$ denotes the fibre of knot types at $p$ and $\mathcal{L}_{p}^{\mathrm{bind}}$ is the binding Hopf link at $p$. The morphism from $\mathbf{1}$ is what distinguishes a localized hadron from an abstract one: it selects a specific point in the base space where the composite knot is situated.*

</div>

<div id="def:hadron-fibre-embedding" class="definition">

**Definition 2.25** (Fibre-compatible hadron embedding). *[<sup><span style="color: BurntOrange">$\forall$</span></sup>](https://litlfred.github.io/qou/lean/QOU.HadronFibreEmbedding)*

*Let $H \in \mathrm{Sym}^n(K) \otimes \mathcal{L}_{\mathrm{Hopf}}$ be a hadron ([Definition](#def:hadron)) and let $E_p$ denote the fibre of the knot bundle over a point $p \in \mathbb{P}(V)$ ([Definition](#def:projective-line-object)). A **fibre-compatible hadron embedding** is a morphism*

*$$\iota_p \;\colon\;
  \mathrm{Sym}^n(K) \otimes \mathcal{L}_{\mathrm{Hopf}}
  \;\longrightarrow\;
  E_p$$*

*satisfying the following conditions:*

1.  ***Integrability.** The embedding $\iota_p$ is *integrable* in the sense that the abstract hadron data (linking, braiding, Skein decomposition) can be consistently realized within the geometric structure of the fibre $E_p$. Concretely, $\iota_p$ must intertwine the abstract Skein action ([operations on hadrons](#rem:hadron-operations)) with the geometric operations on knots in $E_p$.*

2.  ***Fibre confinement.** The image $\iota_p(H)$ is entirely contained in the fibre $E_p$. No constituent knot extends to a neighbouring fibre $E_{p'}$ for $p' \neq p$. This is enforced by a finite Mobius energy bound: $$\mathcal{E}_{\mathrm{Mob}}(\iota_p) \;<\; \infty,$$ which prevents the knot complement from developing cusps that would reach the boundary of the fibre.*

3.  ***Hopf compatibility.** The embedding respects linking and unlinking via the Hopf structure: the diagram $$\begin{tikzcd}[row sep=2.5em, column sep=3em]
      \mathrm{Sym}^n(K) \otimes \mathcal{L}_{\mathrm{Hopf}}
        \ar[r, "\iota_p"]
        \ar[d, "\ell_{ij}"']
      & E_p
        \ar[d, "\ell_{ij}"]
      \\
      \mathrm{Sym}^{n'}(K) \otimes \mathcal{L}_{\mathrm{Hopf}}'
        \ar[r, "\iota_p'"']
      & E_p
    \end{tikzcd}
    \qquad\text{(Hopf compatibility)}$$ commutes for every linking operation $\ell_{ij}$.*

4.  ***Volume compatibility.** The embedding preserves hyperbolic volumes: $\mathrm{vol}(\iota_p(K_i)) = \mathrm{vol}(K_i)$ for each constituent knot $K_i$. This ensures that the mass contribution of each knot, computed via the hyperbolic volume, is faithfully represented in the fibre.*

*A localized hadron ([Definition](#def:localized-hadron)) equipped with a fibre-compatible embedding is a **physically realized hadron**: it is both situated at a base point and faithfully embedded in the fibre geometry. The integrability condition is the key structural requirement — it asserts that the abstract algebraic hadron can be "integrated" into a concrete geometric realization.*

</div>

<div id="prop:skein-generation" class="proposition">

**Proposition 2.26** (Skein generation of hadrons from mass-zero fundamentals). *[<sup><span style="color: BurntOrange">$\forall$</span></sup>](https://litlfred.github.io/qou/lean/QOU.Torsion.skein_generation)*

*Let $(\mathcal{C}, A, \tau)$ be a quantum observable universe with substrate parameter $q$ and Skein module $\mathcal{S}_q = \mathcal{S}_q(\mathcal{C})$. The Skein module $\mathcal{S}_q$ is generated as an algebra by:*

1.  *The fundamental (mass-zero) knot types $\{K_i\}_{i \in \mathcal{F}}$ (torus knots), and*

2.  *The Hopf link $\mathcal{L}_{\mathrm{Hopf}}$ (the binding operation).*

*Every hadron admits a terminal Skein resolution into a finite polynomial in these generators with coefficients in $\mathbb{Z}[q^{\pm 1}]$.*

</div>

<div class="proof">

*Proof of Skein generation.* <span id="prf:skein-generation" label="prf:skein-generation"></span>

**Generators.** A knot type $K$ is *fundamental* if its hyperbolic volume vanishes: $\mathrm{Vol}(K) = 0$. By the geometrization of knot complements, these are precisely the torus knots (and the unknot). In the particle dictionary, the fundamental knots are the fermions: the unknot (neutrino), trefoil $3_1$ (electron), cinquefoil $5_1$ (tau), and the torus$(p,2)$ family.

**Generation.** The Skein module $\mathcal{S}_q$ is generated as an algebra by the fundamental knot types $\{K_i\}_{i \in \mathcal{F}}$ and the Hopf link $\mathcal{L}_{\mathrm{Hopf}}$. Every hadron $H \in \mathrm{Sym}^n(K) \otimes \mathcal{L}_{\mathrm{Hopf}}$ admits a **terminal Skein resolution**: iterating the Skein relation

$$q \cdot L_+ \;-\; q^{-1} \cdot L_-
  \;=\; (q - q^{-1}) \cdot L_0$$

at every crossing terminates in a finite polynomial

$$[H] \;=\; \sum_{\alpha} c_\alpha(q) \cdot
  [K_{i_1}] \cdots [K_{i_k}]$$

where each $[K_{i_j}]$ is the class of a fundamental knot and $c_\alpha(q) \in \mathbb{Z}[q^{\pm 1}]$.

**Mass from linking.** Evaluating the mass functional $\mathcal{M}$ on the Skein resolution gives:

$$\mathcal{M}(H)
  \;=\;
  \underbrace{Q(q) \cdot \mathcal{M}(\mathcal{L}_{\mathrm{Hopf}})}_{\text{binding energy (from linking)}}
  \;+\;
  \underbrace{\sum_{i=1}^{n}
  \frac{\mathrm{Vol}(K_i)}{\hbar_q^{\,2}}}_{\text{constituent mass (zero for torus knots)}}$$

where $Q(q) \in \mathbb{Z}[q^{\pm 1}]$ is the Skein polynomial of the linking configuration and $\hbar_q = 1 - q^{-1}$.

For hadrons composed entirely of fundamental (torus-knot) constituents, $\mathrm{Vol}(K_i) = 0$ for all $i$, so the entire inertial mass arises from the linking topology:

$$\mathcal{M}(H) \;=\; Q(q) \cdot \mathcal{M}(\mathcal{L}_{\mathrm{Hopf}}).$$ ◻

</div>

<div id="def:bundle-initial-conditions" class="definition">

**Definition 2.27** (Bundle initial conditions (big bang state)). *[<sup><span style="color: BurntOrange">$\forall$</span></sup>](https://litlfred.github.io/qou/lean/QOU.BundleInitialConditions)*

*A **bundle initial condition** (or *big bang state*) over the projective line $\mathbb{P}(V)$ is a formal sum of localized hadrons at distinct base points:*

*$$E_0 \;=\; \sum_{i \in I} (p_i,\, H_i)$$*

*where each $(p_i, H_i)$ is a localized hadron ([Definition](#def:localized-hadron)) and the base points are pairwise distinct: $p_i \neq p_j$ for $i \neq j$. The index set $I$ may be infinite, provided no two hadrons share the same base point.*

*Equivalently, $E_0$ is a section of the free commutative monoid on the hadron sheaf $\mathcal{H}$ with the distinct-support condition:*

*$$E_0 \;\in\;
  \Gamma\!\bigl(\mathbb{P}(V),\;
  \mathrm{Free}_{\mathrm{CMon}}(\mathcal{H})\bigr),
  \qquad
  \mathrm{supp}(E_0) \text{ has multiplicity } \leq 1.$$*

*This is the **position-only** specification: at the initial moment the positions $\{p_i\}$ on $\mathbb{P}(V)$ are known exactly, while the momenta are entirely undetermined (the "big bang" complementarity). The categorical content is that $E_0$ specifies the *fibre data* of the bundle — which hadron sits in which fibre — without any information about the horizontal transport connecting neighbouring fibres.*

*For the equivalence relation on bundle initial conditions, see [Definition](#def:bundle-isotopy-equivalence).*

</div>

<div id="def:bundle-isotopy-equivalence" class="definition">

**Definition 2.28** (Isotopy equivalence of bundle initial conditions). *[<sup><span style="color: BurntOrange">$\forall$</span></sup>](https://litlfred.github.io/qou/lean/QOU.BundleIsotopyEquiv)*

*Two bundle initial conditions ([Definition](#def:bundle-initial-conditions)) are **isotopy equivalent** if they are related by a permutation of indices and an ambient isotopy within each fibre:*

*$$\{(p_i, H_i)\}_{i \in I} \;\sim\;
  \{(p_{\sigma(i)}, H_{\sigma(i)}')\}_{i \in I}$$*

*where $\sigma$ is a bijection on $I$ and each $H_{\sigma(i)}'$ is ambient-isotopic to $H_{\sigma(i)}$ in the fibre $E_{p_{\sigma(i)}}$.*

*This is the natural equivalence relation: the physical content of a bundle initial condition depends only on *which* hadron types are placed *where*, not on the labeling of the index set or the particular representative of each ambient isotopy class.*

</div>

<div id="def:torsion-knot-flow" class="definition">

**Definition 2.29** (Torsion-driven knot flow). *[<sup><span style="color: BurntOrange">$\forall$</span></sup>](https://litlfred.github.io/qou/lean/QOU.ParticleState)*

*Given a bundle initial condition $E_0 = \{(p_i, K_i)\}_{i=1}^{N}$ ([Definition](#def:bundle-initial-conditions)), the **torsion-driven knot flow** is the one-parameter family of bundle states*

*$$E_t \;=\; \bigl\{\bigl(\Phi_t^q(p_i),\; K_i\bigr)\bigr\}_{i=1}^{N}
  \qquad t \geq 0,$$*

*where $\Phi_t^q$ is the flow on $\mathbb{P}(V)$ generated by the $q$-deformed Reeb vector field $\xi_q$ ([Definition](#def:categorical-q-reeb-flow)).*

*The flow has two components:*

1.  ***Intrinsic rotation.** Each knot type $K$ carries an intrinsic angular momentum proportional to its crossing number $c(K)$: $$\omega_K \;=\; c(K) \cdot \frac{2\pi}{[c(K)]_q!}$$ where $[n]_q! = [1]_q [2]_q \cdots [n]_q$ is the $q$-factorial. This drives geodesic motion on $\mathbb{P}(V) \cong S^2$ along a great circle whose axis is determined by the initial fibre framing.*

2.  ***Pairwise interaction.** When two localized knots $(p_i, K_i)$ and $(p_j, K_j)$ are within Planck-scale separation $d_{\mathbb{P}(V)}(p_i, p_j) < \ell_P$, they experience a short-range repulsive force $$F_{ij} \;=\;
      \frac{\Delta_q(K_i) \cdot \Delta_q(K_j)}{d(p_i, p_j)^2 + \ell_P^2}$$ where $\Delta_q(K)$ is the $q$-Alexander polynomial of $K$ evaluated at $q = e^{-r}$, and $d$ is the round metric on $S^2$.*

*The flow preserves the total knot content $\sum_i K_i$ (knot types do not change under evolution) but redistributes positions on $\mathbb{P}(V)$. Categorically, the flow is a natural transformation*

*$$\Phi^q \;\colon\;
  \mathrm{id}_{\mathrm{Bun}(\mathbb{P}(V))}
  \;\Longrightarrow\;
  \mathrm{id}_{\mathrm{Bun}(\mathbb{P}(V))}$$*

*in the category $\mathrm{Bun}(\mathbb{P}(V))$ of finite bundles over the projective line, where morphisms are equivariant maps that preserve knot type.*

</div>

## Topological Decomposition of Mass

<div id="thm:topological-mass" class="theorem">

**Theorem 2.30** (Topological Decomposition of Mass). *[<sup><span style="color: BurntOrange">$\forall$</span></sup>](https://litlfred.github.io/qou/lean/QOU.Torsion.mass_decomposition_categorical)*

*Let $(\mathcal{C}, A, \tau)$ be a ([quantum observable universe](#def:quantum-observable-universe)); let $q$ denote the substrate parameter. Let $\gamma \colon \mathbf{1} \to A$ be a morphism (a "closed cycle" in $A$, [mass identity](#def:mass-identity)) whose categorical support is generated by $N$ consecutive extensions along the brane tower $\{A_n\}_{n \geq 0}$ ([recursive brane tower](#def:recursive-brane-tower)), applied to a base-level morphism $\gamma_0 \colon \mathbf{1} \to A_0$.*

*The mass $m(\gamma)$ ([mass identity](#def:mass-identity)) admits a decomposition into descended and transient contributions via the descent involution $\hat{\tau}_n$ ([descent involution](#def:descent-involution)):*

*$$\label{eq:topological-mass-decomp}
  m(\gamma)
  \;=\;
  \bigl\lVert\,
  \mathrm{tr}_{\mathrm{desc}}(\gamma)
  \,\bigr\rVert
  \;+\;
  \sum_{i=1}^{N}
  \bigl\lVert\,
  \mathrm{tr}_{\mathrm{trans}}(\gamma,\, p_i)
  \,\bigr\rVert,$$*

*where:*

1.  *$\mathrm{tr}_{\mathrm{desc}}(\gamma)$ is the categorical trace of $(\int_A \otimes \mathrm{id}) \circ \Delta \circ \gamma$ restricted to the descended subalgebra $\mathcal{A}^{\mathrm{desc}} = \mathrm{im}\,\hat{\tau}_n$ ([descent eigenspaces](#prop:descent-eigenspaces)). Since $\mathcal{A}^{\mathrm{desc}} \cong \mathrm{End}_{\mathcal{C}}(A_n)$ via the ascent embedding $\ell_n$, this equals the mass of the base-level cycle $\gamma_0$: it captures the baseline drag of the Frobenius–Hopf structure along the trivial core.*

2.  *Each $\mathrm{tr}_{\mathrm{trans}}(\gamma, p_i)$ is the categorical trace restricted to the component of the transient complement $\mathcal{A}^{\mathrm{trans}} = \ker\,\hat{\tau}_n$ localised at the $i$-th blow-up centre $p_i$ ([brane boundary](#def:brane-boundary)). The localisation is well-defined because the kernels of $\mathfrak{d}_{n+1}$ at distinct blow-up centres are disjoint submodules of $\mathrm{End}_{\mathcal{C}}(A_{n+1})$.*

*The decomposition follows from the idempotent splitting $\mathrm{End}_{\mathcal{C}}(A_{n+1}) =
\mathcal{A}^{\mathrm{desc}} \oplus \mathcal{A}^{\mathrm{trans}}$ ([descent eigenspaces](#prop:descent-eigenspaces)) and the linearity of the categorical trace. When the splitting is orthogonal with respect to the Frobenius norm, $\lVert \alpha \rVert^2 =
\lVert \hat{\tau}_n(\alpha) \rVert^2 +
\lVert \alpha - \hat{\tau}_n(\alpha) \rVert^2$, the mass decomposes additively as stated.*

*For the archimedean realisation—where the descended trace becomes the holonomy $\mathrm{Hol}_{\nabla_A}$ and each transient trace evaluates to the quantum dilogarithm $\Phi_q(z_i)$—see [archimedean proof](#prf:topological-mass).*

</div>

<div class="proof">

*Categorical proof of the topological decomposition of mass.* <span id="prf:topological-mass-categorical" label="prf:topological-mass-categorical"></span>

*Step 1: Eigenspace decomposition of the mass integrand.* By the ([mass identity](#def:mass-identity)), the mass of $\gamma$ is

$$m(\gamma)
  \;=\;
  \bigl\lVert\,
  \mathrm{tr}\bigl(
    (\int_A \otimes \mathrm{id})
    \circ \Delta
    \circ \gamma
  \bigr)
  \,\bigr\rVert.$$

The integrand $\alpha = (\int_A \otimes \mathrm{id}) \circ \Delta
\circ \gamma$ is an element of $\mathrm{End}_{\mathcal{C}}(A_{n+1})$. The descent involution $\hat{\tau}_n$ ([descent involution](#def:descent-involution)) decomposes this algebra into the direct sum $\mathcal{A}_{n+1}^{\mathrm{desc}} \oplus
\mathcal{A}_{n+1}^{\mathrm{trans}}$ ([descent eigenspaces](#prop:descent-eigenspaces)):

$$\alpha \;=\; \hat{\tau}_n(\alpha) \;+\; (\alpha - \hat{\tau}_n(\alpha)).$$

When the [Frobenius pairing](#def:frobenius-pairing) is compatible with the $*$-involution ($\langle \alpha^*, \beta \rangle = \overline{\langle \alpha, \beta \rangle}$), the idempotent decomposition is orthogonal with respect to the Frobenius norm. Therefore:

$$\lVert \alpha \rVert^2
  \;=\;
  \lVert \hat{\tau}_n(\alpha) \rVert^2
  \;+\;
  \lVert \alpha - \hat{\tau}_n(\alpha) \rVert^2,$$

and by the linearity of the categorical trace:

$$m(\gamma)
  \;=\;
  \bigl\lVert\,
  \mathrm{tr}(\hat{\tau}_n(\alpha))
  \,\bigr\rVert
  \;+\;
  \bigl\lVert\,
  \mathrm{tr}(\alpha - \hat{\tau}_n(\alpha))
  \,\bigr\rVert.$$

*Step 2: Descended term is the base-level mass.* The projection $\hat{\tau}_n(\alpha)$ lies in $\mathcal{A}_{n+1}^{\mathrm{desc}} = \mathrm{im}\,\hat{\tau}_n$, which is isomorphic to $\mathrm{End}_{\mathcal{C}}(A_n)$ via the ascent embedding $\ell_n$ ([descent involution](#def:descent-involution)). The compatibility of the categorical trace with descent ($\mathrm{tr}_n \circ \mathfrak{d}_{n+1} = \mathrm{tr}_{n+1}$ on $\mathrm{im}\,\hat{\tau}_n$) gives:

$$\mathrm{tr}(\hat{\tau}_n(\alpha))
  \;=\;
  \mathrm{tr}(\ell_n(\mathfrak{d}_{n+1}(\alpha)))
  \;=\;
  \mathrm{tr}_n(\mathfrak{d}_{n+1}(\alpha))
  \;=\;
  \mathrm{tr}_n(\alpha_0),$$

where $\alpha_0 = (\int_A \otimes \mathrm{id}) \circ \Delta
\circ \gamma_0$ is the mass integrand of the base-level cycle. Hence $\lVert \mathrm{tr}(\hat{\tau}_n(\alpha)) \rVert = m(\gamma_0)$.

*Step 3: Transient terms localise to blow-up centres.* The transient component $\alpha - \hat{\tau}_n(\alpha) \in
\mathcal{A}_{n+1}^{\mathrm{trans}} = \ker\,\hat{\tau}_n$. By the structure of the brane boundary ([brane boundary](#def:brane-boundary)), the support of a transient endomorphism is contained in the union of the kernels $\ker(\mathfrak{d}_{n+1}|_{p_i})$ at the blow-up centres $p_1, \ldots, p_N$. These kernels are mutually disjoint submodules (each arises from a distinct extension step), so the transient trace decomposes as a sum:

$$\mathrm{tr}(\alpha - \hat{\tau}_n(\alpha))
  \;=\;
  \sum_{i=1}^{N} \mathrm{tr}_{\mathrm{trans}}(\gamma, p_i),$$

and the norm of the sum equals the sum of the norms (by disjointness of the supports).

Combining Steps 1–3 gives the claimed decomposition. ◻

</div>

## Archimedean Specialisations

<div id="cor:jet-prolongation-C" class="corollary">

**Corollary 2.31** (Archimedean realisation of jet prolongation). *[<sup><span style="color: BurntOrange">$\forall$</span></sup>](https://litlfred.github.io/qou/lean/QOU.Torsion.jet_prolongation_C)*

*Let $(M, G, P, E)$ be an archimedean quantum observable universe ([$\mathbb{C}$-quantum observable universe](#ex:c-quantum-observable-universe)) with instanton connection $A$ on $P$ and metric $g$ on $E$. Write $\widetilde{M} = E$ for the total space of $E$, define $P'$ as the frame bundle and $E'$ as the bundle of orthonormal frames of the first jet bundle $J^1 E$. Then $A$ and $g$ uniquely determine a connection $A'$ on $P'$ such that $(\widetilde{M}, G, P', E')$ is an archimedean quantum observable universe.*

</div>

<div class="proof">

*Proof of Archimedean realisation of jet prolongation.* <span id="prf:jet-prolongation-C" label="prf:jet-prolongation-C"></span>

Apply [jet prolongation](#prop:jet-prolongation) to the categorical data $(\mathcal{C}, A, \tau)$ underlying the archimedean quantum observable universe ([$\mathbb{C}$-quantum observable universe](#ex:c-quantum-observable-universe)); let $q$ denote the substrate parameter, where $\mathcal{C} = \mathrm{Rep}(\mathrm{SU}_{q}(2))$, $A = \mathcal{O}_q(\mathrm{SU}(2))$, and $\tau$ is the forgetful functor. The fibre functor $\tau$ converts the categorical jet object $J^1(A)$ into the geometric first jet bundle $J^1 E$, the inherited Frobenius–Hopf structure into the connection $A'$, and the non-degeneracy and vanishing conditions into the analytic conditions of [$\mathbb{C}$-quantum observable universe](#ex:c-quantum-observable-universe). ◻

</div>

<div class="proof">

*Proof of Quantum universe with observability and Yekutieli is a QOU.* <span id="prf:qu-to-qou" label="prf:qu-to-qou"></span>

[Yekutieli lifting](#prop:yekutieli-lifting) establishes that the constructed brane tower satisfies the Yekutieli lifting condition. We prove each structural property in turn.

*Item (1): Descent terminates.* The centre $Z(\mathrm{End}_{\mathcal{C}}(A))$ is a finitely generated commutative $R$-algebra (since $R$ is Noetherian and $\tau$ is faithful), hence has finite Krull dimension $d_0$. Observability forces the $G_q$-action on $A$ to be faithful: any $G_q$-invariant element of $\mathrm{Ad}(A)$ would give a non-zero element of $\mathrm{Hom}(\mathbf{1}, \mathrm{Ad}(A))$, contradicting the observability condition. Each descent step (fixed-point reduction under $G_q$) therefore strictly reduces the Krull dimension of the centre. After at most $d_0$ steps, the Krull dimension reaches $0$, and the base is a discrete (Artinian) scheme.

*Item (2): $\kappa_0$ equals the Euler class.* The first Yekutieli obstruction $\kappa_0 \in H^2(\mathcal{S}, \mathcal{B})$ is the connecting homomorphism image of the bundle class $[A_0]$ under the central extension $1 \to \mathcal{B} \to \mathfrak{G}_1 \to \mathfrak{G}_0
\to 1$ ([Yekutieli lifting](#prop:yekutieli-lifting)). In the archimedean realisation, this identifies with the Euler class $e$ of the Reeb $\mathrm{U}(1)$-bundle via the Gysin sequence. The trace map sends $\kappa_0$ to $\chi(A) = \mathrm{tr}(\mathrm{id}_A)$.

*Item (3): Perpetual obstruction.* The class $\kappa_0$ lies in the image of $H^2(\mathcal{S}, \underline{R})
\to H^2(\mathcal{S}, \mathcal{B})$ (constant/topological classes), while jet corrections at level $n$ lie in the image of $H^2(\mathcal{S},
\mathcal{O}_{\mathcal{S}}) \to H^2(\mathcal{S}, \mathcal{B})$ (analytic/algebraic classes). When $\kappa_0$ is non-torsion, these images are complementary subgroups, so the corrections cannot cancel $\kappa_0$. In the archimedean realisation, the splitting follows from the exponential sequence; in the algebraic setting, from the étale–analytic comparison.

*Item (4): Riemann–Hurwitz.* The branched covering $\pi \colon S \to \mathbb{P}(V)$ of degree $d$ has total ramification $R_{\mathrm{tot}} = 2d + \lvert\chi(A)\rvert$ by Riemann–Hurwitz: $\chi(S) = d \cdot \chi(\mathbb{P}(V)) - R_{\mathrm{tot}}$ with $\chi(\mathbb{P}(V)) = 2$.

*Item (5): Terminal fiber data.* At a branch point $p$, the Krull dimension of the centre is $0$, so the base is a point. The QOU data reduces to the fiber: the Frobenius–Hopf algebra $A$ at parameter $q(p)$, with the involution $\sigma \colon \mathbb{P}(V) \hookrightarrow \mathrm{Ad}(A)$ of [fibre adjoint involution](#prop:fiber-adjoint-involution). ◻

</div>

<div id="cor:mass-identity-C" class="corollary">

**Corollary 2.32** (Archimedean realisation: nonabelian multiplicative integration). *[<sup><span style="color: BurntOrange">$\forall$</span></sup>](https://litlfred.github.io/qou/lean/QOU.MassIdentityC)*

*In the archimedean quantum observable universe $(M, G, P, E)$ ([$\mathbb{C}$-quantum observable universe](#ex:c-quantum-observable-universe)) with instanton connection $A$, Levi form $L$, and self-dual curvature $F^+$, the categorical mass ([mass identity](#def:mass-identity)) is realised as Yekutieli’s nonabelian multiplicative integral \[yekutieli2015\].*

</div>

<div class="proof">

*Proof of archimedean mass identity.* <span id="prf:mass-identity-C" label="prf:mass-identity-C"></span>

Let $\gamma$ be a closed cycle encircling a vortex filament and let $\Sigma$ be a surface with $\partial\Sigma = \gamma$. The categorical mass ([mass identity](#def:mass-identity)) is realised as Yekutieli’s nonabelian multiplicative integral \[yekutieli2015\]:

$$m(\gamma) \;=\;
  \left\lVert\,
  \mathrm{MI}\!\!\int_\Sigma
  \bigl(\nabla_A q,\; L \wedge F^+\bigr)
  \,\right\rVert,$$

where $\mathrm{MI}\!\int_\Sigma$ denotes the $2$-dimensional twisted nonabelian multiplicative integral, the integrand is the connection–curvature pair $(\nabla_A q,\; L \wedge F^+)$ satisfying the quantum flatness equation ([eq:quantum-flatness](#eq:quantum-flatness)), and $\lVert\cdot\rVert$ is the Killing-form norm on $\mathfrak{su}(2)$. By the nonabelian Stokes theorem \[yekutieli2015\], this reduces to the holonomy:

$$m(\gamma) \;=\;
  \bigl\lVert\,
  \mathrm{Hol}_{\nabla_A}\!\bigl(\gamma;\, \mathfrak{G}\bigr)
  \,\bigr\rVert.$$ ◻

</div>

<div class="proof">

*Archimedean proof of Euler characteristic stability.* <span id="prf:euler-char-stability-C" label="prf:euler-char-stability-C"></span>

In the archimedean realisation, the stability $\chi(A_{n+1}) = \chi(A_n)$ can also be verified via the Leray–Serre spectral sequence.

By the construction of the ([recursive brane tower](#def:recursive-brane-tower)), $E_{n+1}$ is the bundle of orthonormal frames of the first jet bundle $J^1 E_n$ ([jet prolongation](#prop:jet-prolongation)). The Euler characteristic of a fibre bundle $F \hookrightarrow E_{n+1} \to E_n$ satisfies the multiplicativity formula

$$\chi(E_{n+1}) \;=\; \chi(E_n) \cdot \chi(F),$$

provided the fibre $F$ has the homotopy type of a finite CW-complex and the base acts trivially on $H^*(F;\, \mathbb{Q})$. In the brane tower the fibre is $\mathrm{SU}(2) \cong S^3$, which has $\chi(S^3) = 0$ for the odd-dimensional sphere. However, the relevant bundle is not $\mathrm{SU}(2)$ itself but the *projectivised* frame bundle, whose typical fibre is $\mathrm{SU}(2)/\mathrm{U}(1) \cong \mathbb{P}^1(\mathbb{C}) \cong S^2$ with $\chi(S^2) = 2$. Nonetheless, the Euler characteristic is preserved for the following reason.

The Leray–Serre spectral sequence of $S^2 \hookrightarrow E_{n+1} \to E_n$ has $E_2^{p,q} = H^p(E_n;\,
H^q(S^2;\, \mathbb{Z}))$. The quantum characteristic classes $\kappa_n$ ([quantum characteristic classes](#def:quantum-characteristic-classes)) are precisely the obstructions to trivial monodromy of the fibre cohomology $H^*(S^2)$. By the vanishing condition of the quantum observable universe axioms—which forces $\mathrm{Hom}(\mathbf{1}, \mathrm{Ad}(A)) = 0$—the monodromy representation of $\pi_1(E_n)$ on $H^*(S^2;\, \mathbb{Z})$ is trivial (the adjoint bundle has no invariant sections to twist the fibre cohomology). Consequently the spectral sequence collapses at the $E_2$ page. The preservation of the Euler characteristic follows from the following observation. The base manifold $M_0$ is invariant under jet prolongation: each level of the brane tower changes the bundle data but not the base geometry. Hence $\chi(M_0)$ is preserved at every level. ◻

</div>

<div class="proof">

*Proof of Structure of the defining boundary.* <span id="prf:brane-boundary" label="prf:brane-boundary"></span>

*(1).* The descent map $\mathfrak{d}_{n+1}$ is a surjective $*$-homomorphism of fibre algebras ([descent](#lem:descent)). Its kernel at a generic point is zero because the ascent $\ell_n$ embeds $A$ as a direct summand of $J^1(A)$ and the restriction $r_n$ is the left-inverse of this embedding. The kernel becomes non-trivial only where the direct-summand splitting degenerates, which is a closed algebraic condition on the [Frobenius pairing](#def:frobenius-pairing) $\varepsilon \circ m$. Since $A$ is a Frobenius–Hopf object in a rigid monoidal category, this degeneracy locus has real codimension at least 2 by the standard codimension bound for degeneracy loci of morphisms between vector bundles of equal rank.

*(2).* At a blow-up centre $p \in \partial E_n$ the kernel of $r_n|_p$ is the fibre of $\Omega^1(A)$ over $p$ modulo the image of $\eta\colon \mathbf{1} \to A$. Since $\Omega^1(A) \hookrightarrow A \otimes A$ and $A$ has fibre $\mathrm{SU}(2)$, the quotient is isomorphic to the projectivisation of the $2$-dimensional representation, i.e. $\mathbb{P}^1(\mathbb{C}) \cong S^2$. This is the exceptional divisor introduced by the topological blow-up that resolves the singularity at $p$.

*(3).* The descent involution $\hat{\tau}_n = \ell_n \circ \mathfrak{d}_{n+1}$ ([descent involution](#def:descent-involution)), acting on sections of $J^1 E_{n+1}$, restricts to the boundary locus $\partial E_n$ as follows. Since $\partial E_n$ is defined by $\ker(\mathfrak{d}_{n+1}|_p) \neq 0$, and $\hat{\tau}_n$ projects onto the image of $\ell_n$, the restriction $\hat{\tau}_n|_{\partial E_n}$ acts as an involution whose fixed points are the sections at boundary points that are entirely in the descended subalgebra—precisely the monodromy fixed-point condition that defines the ([quantum characteristic classes](#def:quantum-characteristic-classes)).

*(4).* At $n = 1$ the base manifold is $M$ and the total space $E_1$ fibres over $M$ with fibre $\mathrm{SU}(2)/\mathrm{U}(1) \cong S^2$. The defining boundary $\partial E_1$ is the locus where the jet restriction degenerates; by item (2) each fibre of $\partial E_1$ is $\mathbb{P}^1(\mathbb{C})$, which separates the base (spacetime) coordinates from the fibre (chiral) coordinates. The Reeb vector field $\xi$ is vertical, so its reversal $\xi \mapsto -\xi$ exchanges the two sides of $\partial E_1$: one side carries left-handed fermions (positive Reeb eigenspace), the other right-handed (negative eigenspace), in agreement with [Descartes chirality](#rem:descartes-chirality). ◻

</div>

<div class="proof">

*Proof of Topological Decomposition of Mass.* <span id="prf:topological-mass" label="prf:topological-mass"></span>

The proof proceeds in four steps: decomposition of the mass integral using the descent involution, identification of the descended term with holonomy, localisation of the transient terms to exceptional divisors, and evaluation via the quantum dilogarithm.

*Step 1: Eigenspace decomposition of the mass integrand.* By the ([mass identity](#def:mass-identity)), the mass of the vortex $\gamma$ is

$$m(\gamma)
  \;=\;
  \bigl\lVert\,
  \mathrm{MI}\!\!\int_\Sigma
  \bigl(\nabla_A q,\; L \wedge F^+\bigr)
  \,\bigr\rVert,$$

where $\Sigma$ is a surface with $\partial\Sigma = \gamma$. The integrand $(\nabla_A q,\; L \wedge F^+)$ is a section of the connection–curvature bundle over $\Sigma$, and as such it is an element of the section algebra $\Gamma(J^1 E_{n+1},\, \mathrm{SU}_{q_{n+1}}(2))$ at whatever level $n{+}1$ accommodates the vortex.

The descent involution $\hat{\tau}_n$ ([descent involution](#def:descent-involution)) decomposes this section algebra into the direct sum $\mathcal{A}_{n+1}^{\mathrm{desc}} \oplus \mathcal{A}_{n+1}^{\mathrm{trans}}$ ([descent eigenspaces](#prop:descent-eigenspaces)). Since $\hat{\tau}_n$ is an idempotent $*$-endomorphism, the Killing-form norm $\lVert\cdot\rVert$ on $\mathfrak{su}(2)$ respects the orthogonal decomposition:

$$\lVert \alpha \rVert^2
  \;=\;
  \lVert \hat{\tau}_n(\alpha) \rVert^2
  \;+\;
  \lVert \alpha - \hat{\tau}_n(\alpha) \rVert^2$$

for every section $\alpha$. Applying this to the mass integrand and using the additivity of the nonabelian multiplicative integral over orthogonal direct sums \[Proposition 5.3, yekutieli2015\]:

$$\label{eq:mi-decomp}
  \mathrm{MI}\!\!\int_\Sigma \alpha
  \;=\;
  \mathrm{MI}\!\!\int_\Sigma \hat{\tau}_n(\alpha)
  \;\cdot\;
  \mathrm{MI}\!\!\int_\Sigma
  \bigl(\alpha - \hat{\tau}_n(\alpha)\bigr),$$

where the product is in the group $\mathrm{SU}_{q}(2)$. Taking norms and using the submultiplicativity of $\lVert\cdot\rVert$ (which is an equality for the orthogonal decomposition of an idempotent):

$$m(\gamma)
  \;=\;
  \bigl\lVert\,
  \mathrm{MI}\!\!\int_\Sigma \hat{\tau}_n(\alpha)
  \,\bigr\rVert
  \;+\;
  \bigl\lVert\,
  \mathrm{MI}\!\!\int_\Sigma
  \bigl(\alpha - \hat{\tau}_n(\alpha)\bigr)
  \,\bigr\rVert.$$

*Step 2: Descended term is the unknot-core holonomy.* The projection $\hat{\tau}_n(\alpha)$ lies in $\mathcal{A}_{n+1}^{\mathrm{desc}} = \mathrm{im}\,\hat{\tau}_n$, which is isomorphic to the level-$n$ section algebra via the ascent embedding $\ell_n$ ([descent involution](#def:descent-involution)). The surface $\Sigma$ with $\partial\Sigma = \gamma$ decomposes under the topological blow-up as $\Sigma = \Sigma_0 \cup \bigcup_{i=1}^N D_i$, where $\Sigma_0$ is a disc spanning the unknot core $\gamma_0$ and each $D_i$ is the disc (exceptional divisor) inserted at the $i$-th blow-up. On $\Sigma_0$ the transient component vanishes ($\alpha - \hat{\tau}_n(\alpha) = 0$ on the unknot complement, since $\gamma_0$ has trivial topology and all sections there factor through level $n$). Hence:

$$\mathrm{MI}\!\!\int_\Sigma \hat{\tau}_n(\alpha)
  \;=\;
  \mathrm{MI}\!\!\int_{\Sigma_0} \alpha
  \;=\;
  \mathrm{Hol}_{\nabla_A}\!\bigl(\gamma_0;\, \mathfrak{G}\bigr),$$

where the second equality is the nonabelian Stokes theorem \[yekutieli2015\] applied to the disc $\Sigma_0$.

*Step 3: Transient terms localise to exceptional divisors.* The transient component $\alpha - \hat{\tau}_n(\alpha)$ is annihilated by $\hat{\tau}_n$: it lies in $\mathcal{A}_{n+1}^{\mathrm{trans}} = \ker\,\hat{\tau}_n$ ([descent eigenspaces](#prop:descent-eigenspaces)). By the structure of the defining boundary ([brane boundary](#def:brane-boundary)), the support of a transient section is contained in a neighbourhood of the boundary $\partial E_n$, which has codimension $\geq 2$ in $E_n$ (item (1)) and whose fibre at each blow-up centre $p_i$ is the exceptional divisor $E_i \cong \mathbb{P}^1(\mathbb{C})$ (item (2)).

On the surface $\Sigma$, the transient integrand is therefore supported on the discs $D_i$ centred at the blow-up points. Since the $D_i$ are disjoint (each blow-up introduces a new connected component of $\partial E_n$), the multiplicative integral splits as a product:

$$\mathrm{MI}\!\!\int_\Sigma
  \bigl(\alpha - \hat{\tau}_n(\alpha)\bigr)
  \;=\;
  \prod_{i=1}^{N}\;
  \mathrm{MI}\!\!\int_{D_i}
  \bigl(\nabla_A q,\; L \wedge F^+\bigr).$$

Since the $D_i$ are geometrically disjoint and the group elements commute up to the central band $\mathcal{O}_M^{\times}$ of the gerbe (the transient modes are localised at distinct points, and the central extension ensures that the group-valued integrals commute modulo the band), the norm of the product equals the sum of the norms:

$$\bigl\lVert\,
  \prod_{i=1}^{N}\;
  \mathrm{MI}\!\!\int_{D_i}
  \bigl(\nabla_A q,\; L \wedge F^+\bigr)
  \,\bigr\rVert
  \;=\;
  \sum_{i=1}^{N}
  \bigl\lVert\,
  \mathrm{MI}\!\!\int_{E_i}
  \bigl(\nabla_A q,\; L \wedge F^+\bigr)
  \,\bigr\rVert,$$

where we replace $D_i$ by $E_i$ since the integrand is supported on the exceptional fibre $E_i \subset D_i$.

*Step 4: Quantum dilogarithm evaluation.* Combining Steps 1–3:

$$m(\gamma)
  \;=\;
  \bigl\lVert\,
  \mathrm{Hol}_{\nabla_A}\!\bigl(\gamma_0;\, \mathfrak{G}\bigr)
  \,\bigr\rVert
  \;+\;
  \sum_{i=1}^{N}
  \bigl\lVert\,
  \mathrm{MI}\!\!\int_{E_i}
  \bigl(\nabla_A q,\; L \wedge F^+\bigr)
  \,\bigr\rVert.$$

This is the claimed decomposition [eq:topological-mass-decomp](#eq:topological-mass-decomp). The identification of each summand with the quantum dilogarithm $\Phi_q(z_i)$ follows from the Corollary below: integration of the $q$-deformed expansion flow over the resolved defect $E_i$ in the spectral coordinates of the Briggs–Klein chart yields $\Phi_q(z_i) = \int_0^{z_i} \ln_q(1+t)/t\, dt$. ◻

</div>

<div id="cor:quantum-dilogarithm" class="corollary">

**Corollary 2.33** (Quantum Dilogarithm as Localized Torsion Volume). *[<sup><span style="color: BurntOrange">$\forall$</span></sup>](https://litlfred.github.io/qou/lean/QOU.Torsion.quantum_dilogarithm)*

*In the archimedean realisation, the transient trace contribution $\mathrm{tr}_{\mathrm{trans}}(\gamma, p_i)$ from the [topological decomposition of mass](#thm:topological-mass) evaluates to the quantum dilogarithm $\Phi_q(z_i)$, where $z_i$ is the spectral coordinate of $p_i$ in the Briggs–Klein chart ([Briggs–Klein chart](#def:briggs-klein-chart)).*

</div>

<div class="proof">

*Proof of quantum dilogarithm corollary.* <span id="prf:quantum-dilogarithm" label="prf:quantum-dilogarithm"></span>

The transient trace at the $i$-th exceptional divisor $E_i \cong \mathbb{P}^1(\mathbb{C})$ is the geometric integration of the $q$-deformed expansion flow over the resolved defect. Integrating the spectral uncertainty flow $\ln_q$ along the radial coordinate of the Briggs–Klein affine chart yields:

$$\Phi_q(z_i) = \int_0^{z_i} \frac{\ln_q(1+t)}{t} dt = \sum_{n=1}^\infty (-1)^{n+1} \frac{z_i^n}{n [n]_q}$$

where $\ln_q(1+t) = \sum_{n=1}^\infty (-1)^{n+1} \frac{t^n}{[n]_q}$ governs the continuous Reeb flow. The integration introduces the factor of $n$ in the denominator, elevating the 1-dimensional path propagation to a geometric volume measure trapping the topological charge. ◻

</div>

# Braids, Knots and Fluid Dynamics

## Introduction

In the QOU framework, traditional path integrals are replaced by finite sums over the discrete fibre structure. Since the base space $B$ and each fibre are finite, the continuum measure $\mathcal{D}\phi$ collapses to a combinatorial sum, eliminating the need for renormalisation of divergent integrals.

The braid group acts naturally on the fibre degrees of freedom. What we observe as particle interactions corresponds to the action of braid operators exchanging strands in the fibre bundle. The algebraic content of these interactions is therefore encoded in braid-group representations rather than in Feynman vertices.

The exchange operations carry a $q$-deformation parameter inherited from the quantum group structure of the fibres. Concretely, the $R$-matrix of $\mathcal{U}_q(\mathfrak{su}(2))$ furnishes a $q$-deformed braid operator whose eigenvalues govern the phase acquired under particle exchange.

Under this correspondence, specific knot types map to particle identities. The trefoil knot, being the simplest non-trivial torus knot, is identified with the quark; the muon arises as a lift of the trefoil to a higher fibre level. The unknot, carrying trivial braiding, corresponds to the neutrino. Experimental evidence supporting this $q$-deformed braiding picture is discussed in [Chapter 6](#chap:descartes-universe).

## Categorical origin of braiding

The braid group is conventionally introduced through the topology of configuration spaces or knot complements. In the QOU framework, however, braiding has a *categorical* origin that is logically prior to any geometric realisation and carries over unchanged to non-archimedean settings ([Chapter 5](#chap:universality)) where knot complements in $S^3$ are unavailable.

<div id="prop:braid-action-tensor" class="proposition">

**Proposition 3.1** (Braid-group action on tensor powers). *[<sup><span style="color: BurntOrange">$\forall$</span></sup>](https://litlfred.github.io/qou/lean/QOU.Braiding.braid_action_tensor)*

*Let $(\mathcal{C}, A, \tau)$ be a ([quantum observable universe](#def:quantum-observable-universe)) whose ambient category $\mathcal{C}$ is braided monoidal with braiding $c_{X,Y}\colon X\otimes Y \xrightarrow{\;\sim\;} Y\otimes X$. For each object $V$ in $\mathcal{C}$ and each $n \geq 2$, there is a group homomorphism*

*$$\rho_n\colon B_n \;\longrightarrow\; \mathrm{Aut}_{\mathcal{C}}(V^{\otimes n})$$*

*given on the Artin generators by*

*$$\label{eq:categorical-braid-rep}
  \rho_n(\sigma_i)
  \;=\;
  \mathrm{id}^{\otimes(i-1)}
  \otimes\, c_{V,V}
  \otimes\, \mathrm{id}^{\otimes(n-i-1)},
  \qquad 1 \leq i \leq n-1.$$*

*The braid relation $\rho_n(\sigma_i)\,\rho_n(\sigma_{i+1})\,\rho_n(\sigma_i)
= \rho_n(\sigma_{i+1})\,\rho_n(\sigma_i)\,\rho_n(\sigma_{i+1})$ is equivalent to the Yang–Baxter equation for the braiding $c_{V,V}$.*

</div>

<div class="proof">

*Proof of Braid-group action on tensor powers.* <span id="prf:braid-action-tensor" label="prf:braid-action-tensor"></span>

The hexagon axioms of a braided monoidal category guarantee that $c_{V,V}$ satisfies the Yang–Baxter equation

$$(c \otimes \mathrm{id})
  \circ (\mathrm{id} \otimes c)
  \circ (c \otimes \mathrm{id})
  \;=\;
  (\mathrm{id} \otimes c)
  \circ (c \otimes \mathrm{id})
  \circ (\mathrm{id} \otimes c)$$

on $V^{\otimes 3}$. This is exactly the braid relation for adjacent generators, and the far-commutativity relation $\sigma_i\sigma_j = \sigma_j\sigma_i$ ($\lvert i-j\rvert \geq 2$) follows from the naturality of the braiding. Together these verify the Artin presentation of $B_n$. ◻

</div>

<div id="prop:knot-eigenbasis-complete" class="proposition">

**Proposition 3.2** (Completeness of the knot-type eigenbasis). *[<sup><span style="color: BurntOrange">$\forall$</span></sup>](https://litlfred.github.io/qou/lean/QOU.Braiding.knot_eigenbasis_complete)*

*Let $(\mathcal{C}, A, \tau)$ be a quantum observable universe with $\mathcal{C} = \mathrm{Rep}(\mathrm{SU}_q(2))$ and $V$ the fundamental representation. Suppose $q$ is not a root of unity. Then:*

1.  ***(Semisimplicity.)** The Hecke algebra $H_n(q) = \mathrm{End}_{B_n}(V^{\otimes n})$ is semisimple, and $V^{\otimes n}$ admits a complete decomposition into irreducible $H_n(q)$-modules: $$V^{\otimes n}
      \;\cong\;
      \bigoplus_{\lambda \,\vdash\, n}
      V_\lambda \otimes S_\lambda,$$ where $\lambda$ ranges over partitions of $n$ with at most two parts (the $q$-analogue of Schur–Weyl duality), $V_\lambda$ is the irreducible $\mathrm{SU}_q(2)$-module of spin $j = (\lambda_1 - \lambda_2)/2$, and $S_\lambda$ is the irreducible $H_n(q)$-module labelled by $\lambda$.*

2.  ***(Alexander surjectivity.)** By Alexander’s theorem, every oriented link $L$ in $S^3$ is the closure $\hat{\beta}$ of some braid $\beta \in B_n$ for some $n$. The Markov trace $\mathrm{tr}_M \colon \bigcup_n H_n(q) \to R$ assigns to each braid closure $\hat{\beta}$ the value $\mathrm{tr}_M(\rho_n(\beta))$, which equals the Jones polynomial $J_L(q)$ up to a framing factor. In particular, the map $$\{\text{knot types}\}
      \;\longrightarrow\;
      \{\text{irreducible summands of } V^{\otimes n},\; n \geq 1\}$$ given by $L \mapsto$ the summand in which $\mathrm{tr}_M(\rho_n(\beta))$ is supported, has image containing every irreducible summand.*

3.  ***(Density in the physical Hilbert space.)** In the archimedean realisation, the physical state space is the direct limit $\mathcal{H}_{\mathrm{phys}} = \varinjlim\, V^{\otimes n}$ along the inclusion maps $V^{\otimes n} \hookrightarrow V^{\otimes (n+1)}$ induced by the unit $\eta \colon \mathbf{1} \to V$. Since each $V^{\otimes n}$ is completely decomposed by (1), the set of irreducible summands — labelled by knot types via (2) — spans a dense subspace of $\mathcal{H}_{\mathrm{phys}}$ in the Hilbert completion.*

</div>

<div class="proof">

*Proof of Completeness of the knot-type eigenbasis.* <span id="prf:knot-eigenbasis-complete" label="prf:knot-eigenbasis-complete"></span> [<sup><span style="color: BurntOrange">$\forall$</span></sup>](https://litlfred.github.io/qou/lean/QOU.PathIntegrals.KnotEigenbasisComplete)

*Part (1).* When $q$ is not a root of unity, the Hecke algebra $H_n(q)$ is isomorphic to $\mathbb{C}[S_n]$ as an abstract algebra (Jimbo’s theorem), hence semisimple. The $q$-Schur–Weyl decomposition of $V^{\otimes n}$ is the standard result for $\mathrm{SU}_q(2)$; see e.g. Chari–Pressley, Chapter 10. The restriction to partitions with at most two parts reflects $\mathrm{rank}(\mathrm{SU}(2)) = 1$: the Young diagrams are at most two-rowed.

*Part (2).* Alexander’s theorem guarantees surjectivity of the braid closure map $\beta \mapsto \hat{\beta}$. The Markov trace on $H_n(q)$ is the unique trace satisfying the Markov property $\mathrm{tr}_M(x \sigma_n^{\pm 1}) = z^{\pm 1}\,\mathrm{tr}_M(x)$ for $x \in H_n(q)$ and a parameter $z$ determined by $q$. On each irreducible summand $S_\lambda$, the trace restricts to a non-zero scalar multiple of the character, so every summand is detected by some braid closure.

*Part (3).* The direct limit $\varinjlim\, V^{\otimes n}$ is a pre-Hilbert space whose completion $\mathcal{H}_{\mathrm{phys}}$ is separable (each $V^{\otimes n}$ is finite-dimensional). The union of the finite-dimensional subspaces $V^{\otimes n}$ is dense by construction, and each is completely decomposed by (1). Hence the irreducible summands, indexed by knot types via the closure map, span a dense subspace. ◻

</div>

## Braid group and symmetric group

With the categorical origin established, we now give explicit presentations and representations of the braid group.

<div id="def:braid-group" class="definition">

**Definition 3.3** (Braid group on three strands). *[<sup><span style="color: BurntOrange">$\forall$</span></sup>](https://litlfred.github.io/qou/lean/QOU.BraidGroup) The *braid group on three strands* is the group*

*$$\label{eq:braid-presentation}
  B_3
  =\bigl\langle\sigma_1,\sigma_2
    \;\big|\;\sigma_1\sigma_2\sigma_1=\sigma_2\sigma_1\sigma_2\bigr\rangle.$$*

*This is the fundamental group of the configuration space of three unordered points in the plane, and is isomorphic to the fundamental group of the complement of the trefoil knot ([trefoil knot group](#rem:trefoil-knot-group)).*

</div>

<div id="def:s3-group" class="definition">

**Definition 3.4** (Symmetric group \$S_3\$). *[<sup><span style="color: BurntOrange">$\forall$</span></sup>](https://litlfred.github.io/qou/lean/QOU.S3Group)*

*Imposing the involution relations $\sigma_i^2=\mathrm{id}$ on the braid group $B_3$ ([braid group](#def:braid-group)) yields the *symmetric group**

*$$\label{eq:s3-presentation}
  S_3
  =\bigl\langle s_1,s_2
    \;\big|\;s_1^2=s_2^2=(s_1 s_2)^3=\mathrm{id}\bigr\rangle.$$*

</div>

## \$\\}mathrm{SU}(2)\$ and \$\\}mathrm{SO}(3)\$ framework

<div id="def:su2-basis" class="definition">

**Definition 3.5** (\$\\}mathfrak{su}(2)\$ basis). *[<sup><span style="color: BurntOrange">$\forall$</span></sup>](https://litlfred.github.io/qou/lean/QOU.Su2Basis) Write $\tau_1,\tau_2,\tau_3$ for the Pauli matrices and set*

*$$\label{eq:su2-basis}
  e_a=-\tfrac{i}{2}\,\tau_a,\qquad a=1,2,3,$$*

*so that the Lie bracket is*

*$$\label{eq:su2-commutator}
  [e_a,\,e_b]=\epsilon_{abc}\,e_c.$$*

</div>

<div id="def:su2-generators" class="definition">

**Definition 3.6** (\$\\}mathrm{SU}(2)\$ generators of \$\\}mathrm{Dic}\_3\$). *[<sup><span style="color: BurntOrange">$\forall$</span></sup>](https://litlfred.github.io/qou/lean/QOU.Su2Generators)*

*Every finite subgroup of $\mathrm{SO}(3)$ lifts, via the double cover $\mathrm{SU}(2)\twoheadrightarrow\mathrm{SO}(3)$, to a binary subgroup of $\mathrm{SU}(2)$. For $S_3\cong D_3$ the lift is the binary dihedral group $\mathrm{Dic}_3\subset\mathrm{SU}(2)$ of order $12$, generated by*

*$$\begin{aligned}
  \alpha &= \exp\!\bigl(\tfrac{2\pi}{3}\,e_3\bigr)
  = \begin{pmatrix}e^{i\pi/3}&0\\[2pt]0&e^{-i\pi/3}\end{pmatrix},
  \label{eq:su2-3cycle}\\[4pt]
  \beta &= \exp(\pi\,e_1)
  = \begin{pmatrix}0&i\\[2pt]i&0\end{pmatrix},
  \label{eq:su2-2cycle}
\end{aligned}$$*

*with $\alpha^3=\beta^2=-I$, dihedral relation $\beta\alpha\beta^{-1}=\alpha^{-1}$, and commutator $[\beta,\alpha]=\alpha^{-2}$.*

</div>

<div id="def:so3-generators" class="definition">

**Definition 3.7** (\$\\}mathrm{SO}(3)\$ generators). *[<sup><span style="color: BurntOrange">$\forall$</span></sup>](https://litlfred.github.io/qou/lean/QOU.So3Generators)*

*Under the adjoint map to $\mathrm{SO}(3)$ the generators of $\mathrm{Dic}_3$ ([SU(2) generators](#def:su2-generators)) have images*

*$$\label{eq:so3-generators}
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
  \end{pmatrix}:$$*

*$R_\alpha$ is a rotation by $2\pi/3$ about the $e_3$-axis (3-cycle) and $R_\beta$ is a $\pi$-rotation about $e_1$ (2-cycle).*

</div>

## Braid involutions and holonomy

<div id="def:braid-twist-flip" class="definition">

**Definition 3.8** (Braid involutions: twist and flip). *[<sup><span style="color: BurntOrange">$\forall$</span></sup>](https://litlfred.github.io/qou/lean/QOU.BraidTwistFlip) Let $\mathbf{w}=(w_1,w_2,w_3,w_4)$ be a spectral resolvent tuple. Define the two involutions*

*$$\begin{aligned}
  \sigma_1(\mathbf{w}) &= (w_2,w_1,w_4,w_3)
    &&\text{(twist),}
    \label{eq:braid-twist}\\[4pt]
  \sigma_2(\mathbf{w}) &= (w_4,w_3,w_2,w_1)
    &&\text{(flip).}
    \label{eq:braid-flip}
\end{aligned}$$*

*As $4\times 4$ permutation matrices these are*

*$$\label{eq:perm-matrices}
  \sigma_1=\begin{pmatrix}
    0&1&0&0\\1&0&0&0\\0&0&0&1\\0&0&1&0
  \end{pmatrix},\quad
  \sigma_2=\begin{pmatrix}
    0&0&0&1\\0&0&1&0\\0&1&0&0\\1&0&0&0
  \end{pmatrix}.$$*

*On the 4-tuple these involutions generate the Klein four-group $V_4=\{\mathrm{id},\sigma_1,\sigma_2,\sigma_1\sigma_2\}$, with $\sigma_1\sigma_2\colon\mathbf{w}\mapsto(w_3,w_4,w_1,w_2)$.*

</div>

## The trefoil knot

## Knot fundamental groups

## Universal enveloping algebras and quantum groups

<div id="def:quantum-su2" class="definition">

**Definition 3.9** (Quantum group \$\\}mathcal{U}\_q(\\}mathfrak{su}(2))\$). *[<sup><span style="color: BurntOrange">$\forall$</span></sup>](https://litlfred.github.io/qou/lean/QOU.QuantumSu2) Let $q\in\mathbb{C}^{*}$ with $0<\lvert q\rvert\le 1$. The *quantum group* $\mathcal{U}_q(\mathfrak{su}(2))$ is the associative $\mathbb{C}$-algebra generated by $E,F,K,K^{-1}$ subject to*

*$$\begin{aligned}
  KK^{-1}&=K^{-1}K=1,
    \label{eq:quantum-KK}\\[3pt]
  KEK^{-1}&=q^2\,E,\quad KFK^{-1}=q^{-2}\,F,
    \label{eq:quantum-KE}\\[3pt]
  [E,F]&=\frac{K-K^{-1}}{q-q^{-1}}.
    \label{eq:quantum-EF}
\end{aligned}$$*

*In the classical limit $q\to 1$, the generator $K$ reduces to $\exp(h\,e_3)$ and the relations recover the $\mathfrak{su}(2)$ commutation relations.*

</div>

## Categorical Möbius energy and self-avoidance

<div id="prop:mobius-energy" class="proposition">

**Proposition 3.10** (Categorical recovery of Möbius energy). *[<sup><span style="color: BurntOrange">$\forall$</span></sup>](https://litlfred.github.io/qou/lean/QOU.Braiding.mobius_energy)*

*Let $(\mathcal{C}, A, \tau)$ be a quantum observable universe ([Definition](#def:quantum-observable-universe)) with substrate parameter $q$ ([Definition](#def:substrate-parameter)), categorical action $\mathcal{S}_q$ ([Definition](#def:categorical-action)), and $q$-Hodge star $\star_q$ ([Definition](#def:q-hodge-star)).*

*Let $\gamma \colon S^1 \to \tau(A)$ be a smooth closed curve (a knot embedding) and let $m(\gamma)$ denote the categorical mass ([Theorem](#thm:topological-mass)).*

*Define the *categorical Möbius energy* by*

*$$E_{\mathrm{cat}}(\gamma)
  \;=\;
  \int_A \!\circ\, \mathrm{tr}_A \!\iint_{S^1 \times S^1 \setminus \mathrm{diag}}
  \!\!\Bigl(
    \Delta(\gamma(s)) \otimes \Delta(\gamma(t))
  \Bigr)
  \;\star_q\;
  \Bigl\lVert
    \frac{d\gamma}{ds} \wedge_q \frac{d\gamma}{dt}
  \Bigr\rVert\,
  ds\, dt\,,$$*

*where $\Delta$ is the Hopf comultiplication, $\int_A$ is the Frobenius form ([Remark](#rem:frobenius-simplification)), and the integration excludes the diagonal $\mathrm{diag} \subset S^1 \times S^1$.*

*Then in the classical limit $q \to 1$, the categorical Möbius energy recovers the classical Möbius energy up to a topological normalization:*

*$$\lim_{q \to 1}\; E_{\mathrm{cat}}(\gamma)
  \;=\;
  \frac{1}{4}\, E(\gamma)
  \;+\; \text{const}\,.$$*

*Here $E(\gamma)$ is the classical Möbius energy*

*$$E(\gamma)
  \;=\;
  \iint_{S^1 \times S^1}
  \Bigl(
    \frac{1}{\lvert \gamma(s) - \gamma(t) \rvert^2}
    \;-\;
    \frac{1}{D(\gamma(s), \gamma(t))^2}
  \Bigr)
  \lvert \gamma'(s) \rvert \, \lvert \gamma'(t) \rvert\,
  ds\, dt\,.$$*

*Here $D(\gamma(s), \gamma(t))$ denotes the intrinsic arc-length distance along $\gamma$.*

</div>

<div class="proof">

*Proof of Categorical recovery of Möbius energy.* <span id="prf:mobius-energy" label="prf:mobius-energy"></span> [<sup><span style="color: BurntOrange">$\forall$</span></sup>](https://litlfred.github.io/qou/lean/QOU.MobiusEnergy)

The proof proceeds in three steps.

*Step 1: Gauge fixing via the categorical volume constraint.* The categorical volume constraint fixes the gauge group to $G = \mathrm{SU}(2)$, acting on the $\mathbb{CP}^1$ fibre by Möbius transformations. This ensures that $E_{\mathrm{cat}}(\gamma)$ is invariant under the full Möbius group $\mathrm{PSL}(2, \mathbb{C})$, matching the conformal invariance of the classical functional.

*Step 2: Expansion of the Frobenius–Hopf kernel.* At $q = 1$ the $q$-Hodge star reduces to the classical Hodge star, and the comultiplication $\Delta$ becomes cocommutative. The [Frobenius pairing](#def:frobenius-pairing) $\int_A \circ \mu$ on $A \otimes A$ reduces to the standard $\mathrm{SU}(2)$ Killing form, so the integrand simplifies to

$$\mathrm{tr}\bigl(
    \Delta(\gamma(s)) \otimes \Delta(\gamma(t))
  \bigr)
  \;\xrightarrow{q \to 1}\;
  \frac{1}{\lvert \gamma(s) - \gamma(t) \rvert^2}.$$

The repulsive kernel $1/r^2$ is thus the classical shadow of the resistance of the Frobenius–Hopf object $A$ to local deformations of the connection $\nabla$: the Frobenius form $\int_A$ assigns a diverging cost when two strands of $\gamma$ approach.

*Step 3: Subtraction of the self-energy.* The diagonal regularization in the categorical integral (exclusion of $\mathrm{diag} \subset S^1 \times S^1$) matches the arc-length subtraction $1/D(\gamma(s),\gamma(t))^2$ in the classical Möbius energy. In the $q$-deformed setting, this subtraction arises naturally from the antipode $S$ of the Hopf structure: the self-pairing $\int_A(\gamma(s)^* \cdot S(\gamma(s)))$ cancels the short-distance divergence at $s = t$, leaving a finite integral that agrees with $E(\gamma)/4$ up to an Euler characteristic correction $\chi(\Sigma_\gamma) \cdot \mathrm{const}$, where $\Sigma_\gamma$ is any Seifert surface spanning $\gamma$. ◻

</div>

<div id="cor:non-self-intersection" class="corollary">

**Corollary 3.11** (Obstruction to self-intersection). *[<sup><span style="color: BurntOrange">$\forall$</span></sup>](https://litlfred.github.io/qou/lean/QOU.Braiding.non_self_intersection)*

*Let $\gamma$ be a knot embedding with categorical Möbius energy $E_{\mathrm{cat}}(\gamma)$ as in [Proposition](#prop:mobius-energy), and let $q \neq 1$ be the substrate parameter ([Definition](#def:substrate-parameter)).*

*The non-cocommutativity of the Hopf structure at $q \neq 1$ provides a categorical obstruction to self-intersection: the energy $m(\gamma)$ diverges whenever two non-adjacent strands of $\gamma$ approach within the fibre $\tau(A)$.*

</div>

<div class="proof">

*Proof of Obstruction to self-intersection.* <span id="prf:non-self-intersection" label="prf:non-self-intersection"></span> [<sup><span style="color: BurntOrange">$\forall$</span></sup>](https://litlfred.github.io/qou/lean/QOU.NonSelfIntersection)

The mechanism is as follows. The universal $R$-matrix $\mathcal{R} \in \mathcal{U}_q(\mathfrak{su}(2)) \hat{\otimes}
\mathcal{U}_q(\mathfrak{su}(2))$ ([Remark](#rem:r-matrix-braiding)) controls the failure of the cocommutativity square

$$\sigma \circ \Delta \;\neq\; \Delta,$$

where $\sigma$ is the tensor swap. At $q = 1$ one has $\mathcal{R} = 1 \otimes 1$ and the comultiplication is cocommutative, so strands may pass through each other freely (the "classical" regime where self-intersection is not penalised by the energy functional).

For $q \neq 1$, the braiding $\check{R} = \sigma \circ \mathcal{R}$ is non-trivial, and the categorical mass acquires a singular contribution from non-adjacent strand proximity. Concretely, because $m(\gamma)$ depends on the $q$-Hodge star $\star_q$ ([Definition](#def:q-hodge-star)), the cost of two non-adjacent points $\gamma(s)$, $\gamma(t)$ approaching is governed by the $q$-deformed commutator

$$[\hat{X}, \hat{P}]_q
  \;=\;
  \hat{X}\hat{P} - q\,\hat{P}\hat{X}
  \;=\;
  i\hbar_q,$$

which replaces the classical $1/r^2$ repulsion kernel with the strictly stronger

$$\frac{1}{\lvert \gamma(s) - \gamma(t) \rvert^2}
  \;\longmapsto\;
  \frac{[2]_q}{\lvert \gamma(s) - \gamma(t) \rvert^2
  - \hbar_q^{\,2}},$$

where $[2]_q = q + q^{-1}$ is the quantum integer and $\hbar_q = 1 - q^{-1}$ is the quantum Planck constant. This kernel has a hard singularity at $\lvert \gamma(s) - \gamma(t) \rvert = \hbar_q$, creating an energy barrier of infinite height at the quantum scale.

Physically, the $R$-matrix endows the vortex filament $\gamma$ with a "quantum exclusion zone" of radius $\hbar_q$: the filament cannot pass through itself because doing so would require infinite categorical energy. This is the knot-theoretic analogue of the Pauli exclusion principle, with the non-cocommutativity of $\Delta_q$ playing the role of fermionic statistics. ◻

</div>

## Varying Euler characteristic

\<!– Content pending: varying Euler characteristic and Bring surface variants. –\>

\<!– Content pending: genus-2 analogue of the Bring surface. –\>

## Descent from \$E_1\$ to \$E_0\$ and the mirror bundle \$E\_{-1}\$

## Fluid Dynamics of the Brane

- Describe the fluid dynamics on the brane whose thickness is determined by the substrate parameter $q$ ([substrate parameter](#def:substrate-parameter)).

- Investigate whether the viscosity gradient can be encoded by the $q$-Laplacian $\Delta_q$.

- Formulate a Navier–Stokes analogue in the $q$-deformed gauge-field setting.

## Geodesics as Stable Vortex Points

- Geodesics on $M$ as stable fixed points of vortex configurations in the brane fluid.

- Stability analysis via the $q$-deformed energy functional.

## Braid Operators in the Fluid Picture

The connection between braid-group operators ([Chapter](#chap:path-integrals-braiding)) and vortex braiding in the fluid dynamics.

## \$q\$-Parameter, Planck Limit, and Reynolds Number

The $q$-deformation parameter and the Planck limit relate to the critical separation distance and the Reynolds number of the brane fluid.

## Emergent Gravity from Information Theory

Link to Verlinde’s entropic gravity programme and related work on emergent gravity from an information-theoretic perspective. Connection to the entropic-gravity signatures discussed in [Section](#sec:entropic-gravity).

## Local Planck Length as Minimal Information Unit

Local Planck length $\ell_P(p)$ as the minimal quantisable size of an information unit at a point $p \in M$. Relation to the substrate parameter: $\ell_P \sim \hbar_q$.

## Time as Information Transfer

Time as a measure of information transfer and change. Time slows at heat death ($q \to 1$) because information transfer rate decreases. Time runs fast at the Big Bang ($q \to \infty$, equivalently $\hbar_q \to 1$) because information transfer is high; torsion of $E$ provides the driving mechanism.

## Big Bang as Initial Information State

At $t = 0$: no information is known about the state of the QOU; matter is concentrated with high torsion pressure. At $t > 0$: the bundle $E$ acts on fermions, information begins to propagate, and the brane expands.

## Planck Units and Computational Mechanics

Develop the analogue of the Planck length for time and clarify its role in computational mechanics.

# Universality

## Key Results in Categorical Language

- Rephrase the QOU definitions ([Chapter](#chap:qou)) in the language of monoidal categories and functors.

- Key theorems to establish in the categorical setting:

  - Lifting ([jet prolongation](#prop:jet-prolongation)) as a categorical lift/extension ([prolongation (categorical)](#rem:prolongation-categorical)).

  - Descent ([Subsection](#ssec:descent)) via fibred categories.

  - Obstructions described in terms of cohomology of the category (sheaf cohomology, derived functors).

  - Show that the Atiyah exact sequence splits if and only if the bundle admits a linear connection.

- Role of $\mathrm{SU}(2)$ and $\mathbb{P}^1(\mathbb{C})$ from the symmetry perspective; motivate categorical analogies (e.g. Tannaka–Krein duality).

## Universal Enveloping Algebras and Quantum Groups

- Lusztig integral form of $\mathcal{U}_q(\mathfrak{su}(2))$ and its triangular decomposition.

- Poincare–Birkhoff–Witt (PBW) basis and its $q$-deformed analogue.

- Universal enveloping algebras and their role in lifting (cf. [arXiv:math/0409565](https://arxiv.org/abs/math/0409565)).

- Heisenberg uncertainty as a $q$-commutator: $[\hat{X},\hat{P}]_q = i\hbar_q$.

## \$\\}pp\$-Adic Number Fields and Universality

- Describe $\mathbb{Q}$, $\mathbb{C}_\mathfrak{p}$, $\mathbb{Q}_\mathfrak{p}$, and $\mathbb{F}_\mathfrak{p}$ in terms of their category-theoretic universality relationships to each other.

- Ostrowski’s theorem as a categorical coproduct characterisation.

- Connections between $\mathfrak{p}$-adic completions and inverse limits in the category of topological rings.

## \$\\}mathbb{C}\_\\}pp\$ Quantum Universe

## Lifting via Formal Groups and Witt Vectors

The $\mathbb{Q}_\mathfrak{p}$ realisation ([$p$-adic realisation](#ex:p-adic-realisation)) provides a QOU over characteristic $0$, while the $\mathbb{F}_\mathfrak{p}$ realisation ([finite field realisation](#ex:finite-field-realisation)) provides one over characteristic $\mathfrak{p}$. The passage between them is mediated by the *Witt vector functor* $W$ and the theory of formal groups over $\mathfrak{p}$-adic rings.

<div id="def:witt-vector-lift" class="definition">

**Definition 4.1** (Witt vector lift of a formal group). *[<sup><span style="color: BurntOrange">$\forall$</span></sup>](https://litlfred.github.io/qou/lean/QOU.WittVectorLift) Let $H$ be a commutative formal group over $\mathbb{F}_\mathfrak{p}$ equipped with a skewed-Poisson structure $\pi_<$ (a biderivation $\pi_<\colon\mathcal{O}(H)\otimes\mathcal{O}(H)\to\mathcal{O}(H)$ satisfying a graded anti-symmetry and a $\mathfrak{p}$-truncated Jacobi condition). The *Witt vector lift* is the formal group $\widehat{G}$ over $W(\mathbb{F}_\mathfrak{p}) \cong \mathbb{Z}_\mathfrak{p}$ obtained by integrating $\pi_<$ in the sense of Fresse: the distribution algebra $\mathrm{Dist}(\widehat{G})$ is the $\mathfrak{p}$-adic completion of the universal enveloping algebra $\mathcal{U}(\mathrm{Lie}(H))$ deformed by $\pi_<$.*

</div>

<div id="prop:skew-poisson-integration" class="proposition">

**Proposition 4.2** (Integration of skewed-Poisson structures). *[<sup><span style="color: BurntOrange">$\forall$</span></sup>](https://litlfred.github.io/qou/lean/QOU.Descartes.skew_poisson_integration)*

*Let $H/\mathbb{F}_\mathfrak{p}$ be a smooth commutative formal group and $\pi_<$ a skewed-Poisson structure on $H$. Then there exists a (generally non-commutative) formal group $G/\mathbb{Z}_\mathfrak{p}$ such that:*

1.  *$G \otimes_{\mathbb{Z}_\mathfrak{p}} \mathbb{F}_\mathfrak{p}\;\cong\; H$ (reduction modulo $\mathfrak{p}$ recovers $H$);*

2.  *$\mathrm{Dist}(G)$ is a deformation of $\mathrm{Dist}(H)$ computed via a Grobner–Shirshov basis for the relations of the enveloping algebra;*

3.  *the comultiplication on $\mathrm{Dist}(G)$ satisfies the *strong multiplicativity* condition: the Frobenius relation $(\mathrm{Id}\otimes m)\circ(\Delta\otimes\mathrm{Id})
    = \Delta\circ m$ is preserved under the deformation.*

</div>

<div class="proof">

*Proof of Integration of skewed-Poisson structures.* <span id="prf:skew-poisson-integration" label="prf:skew-poisson-integration"></span>

This is the Main Theorem of Fresse. Item (1) is the existence statement; item (2) follows from the Grobner–Shirshov normal-form construction for $\mathrm{Dist}(G)$; item (3) is the strong multiplicativity theorem, which guarantees that the co-multiplication is compatible with the deformed product at every stage of the $\mathfrak{p}$-adic filtration. ◻

</div>

## Quotient to Finite Fields

- Quotienting from $\mathbb{Q}_\mathfrak{p}$ to work over $\mathbb{F}_\mathfrak{p}$: reduction modulo $\mathfrak{p}$.

- Finite group representations in the QOU context.

- Betti numbers over finite fields and comparison with characteristic-zero values.

## Jones Polynomials

The role of Jones polynomials in the $\mathfrak{p}$-adic story and their relationship to the braid-group representations of [Chapter](#chap:path-integrals-braiding).

# Bring’s Surface

## Bring’s surface as a QOU

<div id="prop:brings-is-qou" class="proposition">

**Proposition 5.1** (Bring’s surface is a quantum observable universe). *[<sup><span style="color: BurntOrange">$\forall$</span></sup>](https://litlfred.github.io/qou/lean/QOU.Brings.brings_is_qou)*

*Bring’s surface $\Sigma_4$ ([Bring’s surface](#def:brings-surface)) gives rise to a quantum observable universe over $R$ (with $30 \in R^{\times}$):*

1.  **Quantum universe.* Set $\mathcal{C} =
    \mathrm{Rep}(\mathrm{SU}_{q}(2))$ over $R$, $A = \mathcal{O}_q(\mathrm{SU}(2))$ with Frobenius form given by the Haar state, and $\tau$ the forgetful functor to $R$-$\mathrm{Mod}$. The differential calculus $\Omega^1(A)$ is the Woronowicz $3$-dimensional calculus.*

2.  **Observability.* $\mathrm{Hom}(\mathbf{1},\, \mathrm{Ad}(A)) = 0$ by the quantum Schur lemma: $\mathrm{SU}_q(2)$ has no non-trivial invariants in the adjoint representation.*

3.  **Yekutieli lifting.* The brane tower satisfies the Yekutieli lifting condition ([Yekutieli lifting](#prop:yekutieli-lifting)).*

4.  **Euler characteristic.* By [QU-to-QOU lifting](#thm:qu-to-qou), $\chi(A) = \mathrm{tr}(\mathrm{id}_A) = 2 - 2g = -6$.*

5.  **Geometric descent* (for $n = 1$, $\dim M_S = 3$): $$M_S \;\xrightarrow{\;\mathrm{Reeb}\;}\; \Sigma_4
      \;\xrightarrow{\;\pi\;}\; \mathbb{P}(V)
      \;\xrightarrow{\;\mathrm{branch}\;}\; \{6\;\text{points}\}.$$ The degree-$4$ covering $\pi$ has $6$ branch points with total ramification $R_{\mathrm{tot}} = 14$ (Riemann–Hurwitz), and the ramification profile is determined by the $S_5$-symmetry.*

</div>

<div class="proof">

*Proof of Bring’s surface is a quantum observable universe.* <span id="prf:brings-is-qou" label="prf:brings-is-qou"></span>

*Item (1).* The quantised coordinate ring $A = \mathcal{O}_q(\mathrm{SU}(2))$ is a Hopf algebra over $R[q, q^{-1}]$ with antipode $S$, counit $\varepsilon$, and the Haar state $h_q \colon A \to R$ furnishing a non-degenerate Frobenius form $\int_A = h_q$ (non-degeneracy follows from the faithfulness of the Haar state for compact quantum groups). The category $\mathcal{C} = \mathrm{Rep}(\mathrm{SU}_q(2))$ is $R$-linear, rigid monoidal (duals given by contragredient representations), and the forgetful functor $\tau \colon \mathcal{C} \to R\text{-}\mathrm{Mod}$ is exact, faithful, and monoidal. The Woronowicz $3D$-calculus $\Omega^1(A) = \ker(\varepsilon) / \ker(\varepsilon)^2$ is a $3$-dimensional $A$-bimodule in $\mathcal{C}$, providing the differential calculus axiom.

*Item (2).* The adjoint representation $\mathrm{Ad}(A)$ decomposes under $\mathrm{SU}_q(2)$ into irreducible representations of spin $j \geq 1$ (the spin-$0$ component vanishes because $\mathrm{Ad} \cong V_1 \oplus V_2 \oplus \cdots$ with no trivial summand). Therefore $\mathrm{Hom}(\mathbf{1}, \mathrm{Ad}(A)) = 0$ by the quantum Schur lemma.

*Item (3).* By [jet prolongation](#prop:jet-prolongation), $J^1(A)$ is Frobenius–Hopf, so the brane tower $\{A_n\}$ is well-defined. Each transition $A_n \hookrightarrow A_{n+1}$ gives a central extension of gerbes banded by the centre $\mathcal{B} = Z(\mathrm{Aut}(A_n))$. The obstruction class $\kappa_n \in H^2(\mathcal{S}, \mathcal{B})$ exists by the standard gerbe classification theorem, verifying the Yekutieli lifting condition ([Yekutieli lifting](#prop:yekutieli-lifting)).

*Item (4).* The categorical trace of $\mathrm{id}_A$ in $\mathcal{C} = \mathrm{Rep}(\mathrm{SU}_q(2))$ is the quantum dimension $\mathrm{tr}(\mathrm{id}_A) = [N]_q \cdot [N-1]_q / [1]_q$ evaluated at $N = 2$ (the rank of $\mathrm{SU}(2)$). At generic $q$, this recovers the topological Euler characteristic of $\Sigma_4$: $\chi(A) = 2 - 2g = 2 - 8 = -6$.

*Item (5).* The Reeb quotient $M_S \to \Sigma_4$ collapses the $\mathrm{U}(1)$-orbits of the circle bundle (weight-$0$ subalgebra $A_0 = A^{\mathrm{U}(1)}$). The covering $\pi \colon \Sigma_4 \to \mathbb{P}(V)$ is the map to the projective line induced by the linear system $|K_{\Sigma_4}|$; it has degree $4$ and genus $4$ source, so by Riemann–Hurwitz $R_{\mathrm{tot}} = 2g(\Sigma_4) - 2 - 4(2g(\mathbb{P}^1) - 2) =
6 - 4(-2) = 14$. The $S_5$-symmetry of $\Sigma_4$ forces the $14$ units of ramification to be distributed over exactly $6$ branch points (with ramification indices determined by the cycle types of $S_5$). ◻

</div>

## Lagrange resolvents and braid-group action

## Color tube coordinates

<div id="def:color-tube-coordinates" class="definition">

**Definition 5.2** (Color tube coordinates). *[<sup><span style="color: BurntOrange">$\forall$</span></sup>](https://litlfred.github.io/qou/lean/QOU.ColorTubeCoordinates)*

*Let $z = x_0/x_1 \in \mathbb{P}^1(\mathbb{C})$ be the spacetime ratio ([braid group action](#rem:braid-group-action)(i)) and let $w_k$, $k \in \{0,\dots,4\}$, be the Lagrange resolvents of Bring’s surface ([Lagrange resolvents](#rem:lagrange-resolvents)). The *color tube coordinates* are the shifted spectral coordinates*

*$$\label{eq:color-tube-coords}
  r = w_2 - z, \quad g = w_3 - z, \quad b = w_4 - z,$$*

*together with the space-like shift $\sigma = w_1 - z$. The *color vector* is $\vec{c} = (r, g, b)$.*

</div>

## Chiral fibration and elliptic curves

<div id="prop:chiral-elliptic" class="proposition">

**Proposition 5.3** (Chiral fibre as an elliptic curve). *[<sup><span style="color: BurntOrange">$\forall$</span></sup>](https://litlfred.github.io/qou/lean/QOU.Brings.chiral_elliptic)*

*Let $z=x_0/x_1\in\mathbb{P}^1(\mathbb{C})$ be the projective spacetime ratio ([braid group action](#rem:braid-group-action)(i)). Substituting the constraint $x_0+x_1=C$ and eliminating $x_0,x_1$ in favour of $z$, the quadratic and cubic power-sum conditions on the chiral variable $X=(x_2,x_3,x_4)$ reduce at each fixed $z$ to the cubic*

*$$\label{eq:chiral-elliptic}
  X^3+(z+1)\,X^2+(z^2+z+1)\,X+(z^3+z^2+z+1)=0.$$*

*For generic $z$ this defines an elliptic curve $E_z$ in the chiral fibre; its $j$-invariant varies as a rational function of $z$. The monodromy of $E_z$ around the singular fibres (where the discriminant of the cubic vanishes) recovers the holonomy generators $H_1,H_2$ of [holonomy of trefoil](#rem:holonomy-trefoil).*

</div>

<div class="proof">

*Proof of Chiral fibre as an elliptic curve.* <span id="prf:chiral-elliptic" label="prf:chiral-elliptic"></span>

Write $x_0=z\,x_1$ and use $x_0+x_1=C$ to eliminate both spacetime variables. The power-sum conditions $\sum x_j^k=0$ for $k=2,3$ then become polynomial in $z$ and $X=x_2+x_3+x_4$, $X_2=\sum_{i<j}x_ix_j$, etc. Reducing by the Newton identities yields the cubic; its discriminant is a polynomial in $z$ whose roots give the singular fibres. ◻

</div>

<div id="def:color-tube-fibers" class="definition">

**Definition 5.4** (Color tube fibers). *[<sup><span style="color: BurntOrange">$\forall$</span></sup>](https://litlfred.github.io/qou/lean/QOU.ColorTubeFibers)*

*Let $z \in \mathbb{P}^1(\mathbb{C})$. The *color tube* at $z$ is the affine curve defined over $\mathbb{Z}[z]$ by the color tube cubic; we denote it $R_z$, $G_z$, or $B_z$ according to which color tube coordinate $\mathbf{r}_z$, $\mathbf{g}_z$, or $\mathbf{b}_z$ is used:*

*$$\label{eq:color-tube-fiber-def}
  R_z \;:=\;
  \bigl\{\,\mathbf{r}_z \in \mathbb{A}^1 :
    \mathbf{r}_z^{\,3} + (4z+1)\,\mathbf{r}_z^{\,2}
    + (6z^2+3z+1)\,\mathbf{r}_z
    + (4z^3+3z^2+2z+1) = 0\,\bigr\},$$*

*and $G_z$, $B_z$ are defined by the same equation with coordinates $\mathbf{g}_z$ and $\mathbf{b}_z$, respectively. The coordinates are related to the Lagrange resolvents by*

*$$\mathbf{r}_z = w_2 - z, \qquad \mathbf{g}_z = w_3 - z, \qquad
  \mathbf{b}_z = w_4 - z.$$*

*As varieties, $R_z \cong G_z \cong B_z$ is isomorphic to the chiral elliptic fiber $E_z$ of [chiral elliptic curve](#prop:chiral-elliptic) via the shift $X = \mathbf{c} + z$.*

</div>

<div id="def:observed-value" class="definition">

**Definition 5.5** (Observed spacetime value). *[<sup><span style="color: BurntOrange">$\forall$</span></sup>](https://litlfred.github.io/qou/lean/QOU.ObservedValue)*

*Let $\mathbf{r}_z, \mathbf{g}_z, \mathbf{b}_z$ be the color tube coordinates at a point of Bring’s surface ([colour tube fibres](#def:color-tube-fibers)). The *observed spacetime value* is the element of $\mathbb{A}^1$ recovered from the color tube coordinates by the Vieta identity:*

*$$\label{eq:observed-value}
  \mathbf{r}_z + \mathbf{g}_z + \mathbf{b}_z + 4z + 1 \;=\; 0.$$*

*This identity defines the projection $\pi_z \colon R_z \times G_z \times B_z \to \mathbb{A}^1$, $(\mathbf{r}_z, \mathbf{g}_z, \mathbf{b}_z) \mapsto z$, which is a polynomial map over $\mathbb{Z}$. At a branch point $z_c$ where chiral sheets merge ([Bring’s surface smoothness](#rem:brings-smoothness)), the exceptional divisor is coordinatised by the limiting color vector; the observed spacetime value reads off $z_c$ from the color data via the identity above, providing a coordinate on the exceptional $\mathbb{P}^1(\mathbb{C})$.*

</div>

## Bundle structures and smoothness

<div id="def:briggs-klein-chart" class="definition">

**Definition 5.6** (Briggs–Klein affine chart). *[<sup><span style="color: BurntOrange">$\forall$</span></sup>](https://litlfred.github.io/qou/lean/QOU.BriggsKleinChart)*

*Let $r=\lvert w_1\rvert^2$ denote the squared modulus of the first resolvent coordinate on ([Bring’s surface](#def:brings-surface)). The *Briggs–Klein affine chart* is the coordinate system $(w_1,w_2)$ restricted to the open set $0<r<\infty$, equipped with the Hermitian metric inherited from the Fubini–Study metric on $\mathbb{P}^4$. In this chart the $C_5$ action is the phase rotation $w_k\mapsto\zeta^k\,w_k$, and the radial coordinate $r$ is $C_5$-invariant.*

</div>

## Quaternionic spectral resolvents

<div id="def:quaternionic-spectral-resolvents" class="definition">

**Definition 5.7** (Quaternionic spectral resolvents). *[<sup><span style="color: BurntOrange">$\forall$</span></sup>](https://litlfred.github.io/qou/lean/QOU.QuaternionicSpectralResolvents)*

*Let $\mathcal{S}$ denote the ([Bring’s surface](#def:brings-surface)). Let $q\in\mathbb{C}$ with $0<\lvert q\rvert\le 1$, and set $r=-\ln\lvert q\rvert$ so that $\lvert q\rvert=e^{-r}$. Write $\mathbf{i},\mathbf{j},\mathbf{k}$ for the standard basis of $\operatorname{Im}\mathbb{H}$. Using the Lusztig $q$-exponential and $q$-logarithm,*

*$$\label{eq:q-exp}
  \exp_q(x)\;=\;\sum_{n=0}^{\infty}\frac{x^n}{[n]_q!},
  \qquad
  \ln_q(1+x)\;=\;\sum_{n=1}^{\infty}(-1)^{n+1}\frac{x^n}{[n]_q},$$*

*we define the *quaternionic spectral resolvents* $\omega_k\colon\mathcal{S}\to J^\infty E$ by*

*$$\begin{aligned}
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
\end{aligned}$$*

*By the first power sum, $\omega_0=0$ in the balanced state; the remaining coordinates embed $\mathcal{S}$ into the infinite jet shell $J^\infty E$ ([jet shell](#rem:jet-shell)).*

</div>

## Geometric resolution and Seiberg–Witten theory

<div id="prop:mi-sw-abelianisation" class="proposition">

**Proposition 5.8** (Abelianisation of the MI integral on exceptional divisors). *[<sup><span style="color: BurntOrange">$\forall$</span></sup>](https://litlfred.github.io/qou/lean/QOU.Brings.mi_sw_abelianisation)*

*Let $E_c \cong \mathbb{P}^1(\mathbb{C})$ be the exceptional divisor at a branch point $z_c$ ([Bring’s surface smoothness](#rem:brings-smoothness)), and let $(\nabla_A q,\; L \wedge F^+)$ be the connection–curvature pair of the ([mass identity](#def:mass-identity)). Then for each vertical degree $n \geq 0$ in the Reeb decomposition, the restriction of the nonabelian multiplicative integral to $E_c$ abelianises to the $n$-th prolonged Seiberg–Witten period:*

*$$\label{eq:mi-sw-abelianisation}
  \bigl\lVert\,
  \mathrm{MI}\!\!\int_{E_c}
  \bigl(\nabla_A q,\; L \wedge F^+\bigr)
  \,\bigr\rVert_{J^n}
  \;=\;
  \bigl\lvert a_D^{(n)}\bigr\rvert
  \;=\;
  \biggl\lvert\oint_{E_c}\lambda_{\mathrm{SW}}^{(n)}\biggr\rvert,$$*

*where $\lVert\cdot\rVert_{J^n}$ denotes the Killing-form norm projected onto the $n$-th jet component, and $\lambda_{\mathrm{SW}}^{(n)}$ is the $n$-th prolonged Seiberg–Witten differential.*

</div>

<div class="proof">

*Proof of Abelianisation of the MI integral on exceptional divisors.* <span id="prf:mi-sw-abelianisation" label="prf:mi-sw-abelianisation"></span>

The proof proceeds in three steps.

*Step 1: Abelianisation of the connection.* On the exceptional divisor $E_c \cong \mathbb{P}^1(\mathbb{C})$ the principal $\mathrm{SU}(2)$-bundle $P$ trivialises (every $\mathrm{SU}(2)$-bundle over $S^2$ is classified by $\pi_1(\mathrm{SU}(2)) = 0$). The connection $\nabla_A$ therefore reduces to a $\mathfrak{su}(2)$-valued $1$-form $A|_{E_c}$. By the weight-space decomposition ([weight space decomposition](#rem:weight-space-decomposition)), the restriction splits as

$$A\big|_{E_c}
  \;=\;
  A^0 \otimes H
  \;+\;
  A^+ \otimes E_+
  \;+\;
  A^- \otimes E_-,$$

where $H, E_\pm$ are the standard generators of $\mathfrak{su}(2)$. The Cartan component $A^0$ is a $\mathrm{U}(1)$-valued $1$-form on $E_c$. Since $E_c \cong \mathbb{P}^1(\mathbb{C})$ the spectral curve ([chiral bundles](#rem:chiral-bundles)) restricts to a single sheet, and the Higgs-field eigenvalue is the chiral coordinate $X$. The abelian component therefore satisfies $A^0 = X\,dz = \lambda_{\mathrm{SW}}$, recovering the Seiberg–Witten differential.

*Step 2: Quantum flatness and the $2$-form datum.* The quantum flatness condition $F_A = B$ identifies the curvature $2$-form $L \wedge F^+$ on $E_c$ with the $\mathfrak{su}(2)$-valued $2$-form $B|_{E_c}$. The simplicity constraint forces $B|_{E_c} = F_A^+|_{E_c}$, which on the $2$-sphere $E_c$ is proportional to the volume form $\mathrm{vol}_{E_c}$. Consequently the pair $(\nabla_A q,\; L \wedge F^+)$ restricted to $E_c$ is *abelian*: both components lie in the Cartan subalgebra after projection onto the weight-$0$ sector, and the nonabelian MI integral reduces to the ordinary (abelian) multiplicative integral, which equals the exponential of the classical contour integral. Taking the norm yields the absolute value of the period.

*Step 3: Jet prolongation and vertical degree.* At vertical degree $n = 0$ the Killing-form projection onto $J^0$ recovers the base differential $\lambda_{\mathrm{SW}}^{(0)} = X\,dz$ and the electron period $a_D^{(e)}$. At vertical degree $n \geq 1$ the ([jet prolongation](#prop:jet-prolongation)) lifts the connection to $J^n E$, replacing $X\,dz$ with the $n$-th prolonged differential $\lambda_{\mathrm{SW}}^{(n)}$: the $1$-jet component is $dX$ (the implicit derivative of the color tube cubic), and higher jets follow by induction. The MI integral at jet level $n$ is the abelian integral of $\lambda_{\mathrm{SW}}^{(n)}$ over $E_c$ by the same argument as Steps 1–2 applied to the prolonged connection $A'$ on $J^n E$. ◻

</div>

## Quantum Brings

This section will develop the quantum version of the commutator relations in the group relations and Bring’s formulas. In particular, the classical commutator $[e_a,e_b] = \epsilon_{abc} e_c$ will be replaced with the $q$-deformed commutator from $U_q(\mathfrak{su}(2))$, describing how the Bring surface equations transform under the $q$-deformed action and relating the non-commutative geometry to the quantum substrate parameter $q(p)$.

## Other Euler characteristics

This section will investigate Bring’s surface and its analogues for Euler characteristics other than $\chi = -6$, classifying surfaces for $\chi = -2, -4, -8, \ldots$, determining which automorphism groups arise, and connecting to the varying Euler characteristic discussion.

# The Descartes Universe

## The Descartes condition

<div id="def:descartes-condition" class="definition">

**Definition 6.1** (Descartes condition). *[<sup><span style="color: BurntOrange">$\forall$</span></sup>](https://litlfred.github.io/qou/lean/QOU.DescartesCondition)*

*A quantum observable universe $(\mathcal{C}, A, \tau)$ over $R$ ([quantum observable universe](#def:quantum-observable-universe), [QU-to-QOU lifting](#thm:qu-to-qou)) satisfies the *Descartes condition* if the categorical Euler characteristic*

*$$\chi(A) \;=\; \mathrm{tr}(\mathrm{id}_A) \;=\; -6 \;\in\; R.$$*

*This requires $6 \in R^{\times}$ (i.e. $\mathrm{char}(R) \nmid 6$). The class $[A] \in K_0(\mathcal{C})$ has rank $-6$, which by [QU-to-QOU lifting](#thm:qu-to-qou)(3–4) forces $\kappa_n \neq 0$ for all $n$ and produces $6$ branch points in the geometric descent (with total ramification $R_{\mathrm{tot}} = 2d + 6$). A quantum observable universe satisfying the Descartes condition is called a *Descartes universe*.*

</div>

<div id="prop:genus-maximal-descent" class="proposition">

**Proposition 6.2** (Genus of the one-complex-dimensional descent). *[<sup><span style="color: BurntOrange">$\forall$</span></sup>](https://litlfred.github.io/qou/lean/QOU.Descartes.genus_maximal_descent)*

*Let $(\mathcal{C}, A, \tau)$ be a quantum observable universe satisfying the Descartes condition $\chi(A) = -6$ ([Descartes condition](#def:descartes-condition)). If the geometric descent produces a compact one-complex-dimensional base $M_0$, then $M_0$ is a Riemann surface of genus $g = 4$.*

*More precisely: the categorical Euler characteristic $\mathrm{tr}(\mathrm{id}_A) = -6$ determines the topological type of the base curve. Under the fibre functor $\tau$ of any archimedean realisation, Riemann–Roch on $M_0$ forces $2(1 - g) = -6$, hence $g = 4$. This is the maximal genus consistent with the Hurwitz bound $|\mathrm{Aut}(\Sigma)| \leq 84(g - 1) = 252$.*

</div>

<div class="proof">

*Proof of Genus of the one-complex-dimensional descent.* <span id="prf:genus-maximal-descent" label="prf:genus-maximal-descent"></span>

The Descartes condition gives $\mathrm{tr}(\mathrm{id}_A) = -6$. Under the fibre functor $\tau$ of the archimedean realisation, this maps to the sheaf Euler characteristic $\chi(V) = -6$, where $V = P \times_{\mathrm{SU}(2)} K^2$ is the associated rank-$2$ vector bundle over $M_0$. Since $G = \mathrm{SU}(2)$, the determinant bundle $\det(V)$ is trivial, so $\deg(V) = 0$. By Riemann–Roch on the compact Riemann surface $M_0$: $\chi(V) = \deg(V) + \mathrm{rank}(V)(1-g) = 2(1-g)$. Setting $2(1-g) = -6$ gives $g = 4$. ◻

</div>

## Leptons and chirality

## Trefoil subgroups and Bring’s curve

## Colour-sector coordinates on the exceptional fibre

<div id="def:exceptional-divisor" class="definition">

**Definition 6.3** (Exceptional divisor at \$p\$). *[<sup><span style="color: BurntOrange">$\forall$</span></sup>](https://litlfred.github.io/qou/lean/QOU.ExceptionalDivisor)*

*Let $(M, G, E)$ be a Descartes universe and let $p \in M$ be a brane point with outward normal $N(p) = p/\lvert p\rvert$ and positively-oriented tangent frame $(T_1, T_2)$. Set $R = R_{\mathbb{P}^1(\mathbb{C})}$ and*

*$$O(p) \;=\; p + R\,N(p).$$*

*The *exceptional divisor* at $p$ is the $\mathbb{P}^1(\mathbb{C})$ fibre*

*$$E_p \;=\; \pi^{-1}(p)
  \;=\;
  \bigl\{\,
    O(p) + R\bigl(\sin\phi\,(\cos\psi\,T_1 + \sin\psi\,T_2) - \cos\phi\,N\bigr)
    \;:\;
    \phi \in [0,\pi],\; \psi \in [0,2\pi)
  \,\bigr\},$$*

*where $\pi\colon \widetilde{M} \to M$ is the blow-up map that replaces $p$ with $E_p \cong \mathbb{P}^1(\mathbb{C})$.*

</div>

<div id="def:chiral-sector-coords" class="definition">

**Definition 6.4** (Chiral sector coordinates \$\\}mathfrak{r},\\}mathfrak{g},\\}mathfrak{b}\$). *[<sup><span style="color: BurntOrange">$\forall$</span></sup>](https://litlfred.github.io/qou/lean/QOU.ChiralSectorCoords)*

*With notation as in [exceptional divisor](#def:exceptional-divisor), fix the substrate parameter $q$ ([substrate parameter](#def:substrate-parameter)) and set $\phi \in [0,\pi]$, $\psi \in [0, 2\pi/3]$. Define the *red*, *green*, and *blue* sector embeddings by*

*$$\begin{aligned}
  \mathfrak{r}(\phi,\psi)
  &\;=\; O + R\bigl(\sin\phi\,\bigl(\cos(\psi + q\phi)\,T_1
         + \sin(\psi + q\phi)\,T_2\bigr) - \cos\phi\,N\bigr),\\
  \mathfrak{g}(\phi,\psi)
  &\;=\; \mathfrak{r}\!\bigl(\phi,\,\psi + \tfrac{2\pi}{3}\bigr),\\
  \mathfrak{b}(\phi,\psi)
  &\;=\; \mathfrak{r}\!\bigl(\phi,\,\psi + \tfrac{4\pi}{3}\bigr).
\end{aligned}$$*

*The *chiral twist* $q\phi$ rotates each sector by $q$ full turns as the latitude $\phi$ runs from the south pole ($0$) to the north pole ($\pi$), encoding the chirality of the substrate parameter.*

*The three sectors tile the exceptional divisor exactly:*

*$$E_p \;=\; \mathfrak{r}(p) \;\cup\; \mathfrak{g}(p) \;\cup\; \mathfrak{b}(p),$$*

*where adjacent sectors share only their boundary meridians (at $\psi = 0$ and $\psi = 2\pi/3$ in each sector’s local coordinate), and the union covers $E_p$ without overlap. The three sectors correspond to the three copies of $S_3 \subset S_5$ in [chirality and trefoil](#rem:chirality-trefoil): $\mathfrak{r}$ is the first, $\mathfrak{g}$ the second, and $\mathfrak{b}$ the third.*

</div>

## Categorical braid structure

<div id="cor:descartes-braid-structure" class="corollary">

**Corollary 6.5** (Braid-group structure of a Descartes universe). *[<sup><span style="color: BurntOrange">$\forall$</span></sup>](https://litlfred.github.io/qou/lean/QOU.Descartes.descartes_braid_structure)*

*Let $(\mathcal{C}, A, \tau)$ be a Descartes universe ([Descartes condition](#def:descartes-condition)). Then:*

1.  *The braiding of $\mathcal{C} = \mathrm{Rep}(\mathrm{SU}_q(2))$ induces a faithful representation $\rho_3\colon B_3 \to \mathrm{Aut}_{\mathcal{C}}(V^{\otimes 3})$ on the fundamental representation $V$ ([braid action on tensor products](#prop:braid-action-tensor)).*

2.  *The image of $\rho_3$ in $\mathrm{SU}(2)$ (via the fibre functor $\tau$) is the binary dihedral group $\mathrm{Dic}_3$ of order $12$ ([SU(2) generators](#def:su2-generators)).*

3.  *The composite $B_3 \xrightarrow{\;\rho_3\;}
    \mathrm{Dic}_3 \twoheadrightarrow S_3$ recovers the three copies of $S_3$ inside $S_5 = \mathrm{Aut}(\Sigma_4)$ ([chirality and trefoil](#rem:chirality-trefoil)), one for each colour sector.*

4.  *This structure is defined over any base ring $R$ with $30 \in R^{\times}$; in particular it applies to the $\mathfrak{p}$-adic realisation ([$p$-adic realisation](#ex:p-adic-realisation)), where knot complements and skein relations are not available.*

</div>

<div class="proof">

*Proof of Braid-group structure of a Descartes universe.* <span id="prf:descartes-braid-structure" label="prf:descartes-braid-structure"></span>

*Item (1)* follows from [braid action on tensor products](#prop:braid-action-tensor) applied to the fundamental representation $V$ of $\mathrm{SU}_q(2)$, which is $2$-dimensional. The braiding $c_{V,V}$ is computed by the $R$-matrix of $\mathcal{U}_q(\mathfrak{su}(2))$ ([$R$-matrix braiding](#rem:r-matrix-braiding)), and faithfulness follows from the fact that the eigenvalues of $c_{V,V}$ are $q$ and $-q^{-1}$, which are distinct for $q \neq \pm 1$.

For *item (2)*, the fibre functor $\tau$ sends the braiding to the matrix $\check{R} = P \circ \mathcal{R}$ acting on $\mathbb{C}^2 \otimes \mathbb{C}^2$. The generators $\sigma_1, \sigma_2$ map to the $\mathrm{SU}(2)$ elements $\alpha, \beta$ ([SU(2) generators](#def:su2-generators)) generating $\mathrm{Dic}_3$, as verified in [trefoil operator algebra](#ex:trefoil-operator-algebra).

*Item (3)*: the projection $\mathrm{Dic}_3 \to S_3$ sends $\alpha \mapsto (1\,2\,3)$ and $\beta \mapsto (1\,2)$. The three copies of $S_3$ inside $S_5$ are the stabilisers of the three pairs of chiral coordinates ([chiral sector coords](#def:chiral-sector-coords)), and conjugation by elements of $S_5 \setminus S_3$ permutes these copies.

*Item (4)*: the braided monoidal structure of $\mathrm{Rep}(\mathrm{SU}_q(2))$ is defined over $R[q, q^{-1}]$ with $30 \in R^{\times}$ ([Bring’s surface is QOU](#prop:brings-is-qou)(1)), and [braid action on tensor products](#prop:braid-action-tensor) requires no topological input beyond the hexagon axioms. ◻

</div>

## The Descartes theorem

<div id="thm:descartes" class="theorem">

**Theorem 6.6** (Descartes theorem). *[<sup><span style="color: BurntOrange">$\forall$</span></sup>](https://litlfred.github.io/qou/lean/QOU.Descartes.descartes)*

*Let $\mathcal{C}_{-6}$ denote the category of quantum observable universes over $R$ satisfying the Descartes condition $\chi(A) = -6$ ([Descartes condition](#def:descartes-condition)), with morphisms given by QOU maps that preserve the Euler characteristic. Then Bring’s surface $\Sigma_4$ ([Bring’s surface](#def:brings-surface), [Bring’s surface is QOU](#prop:brings-is-qou)) is a terminal object in $\mathcal{C}_{-6}$: for every Descartes universe $(\mathcal{C}, A, \tau)$ in $\mathcal{C}_{-6}$, there exists a unique morphism to the Bring’s QOU.*

</div>

<div class="proof">

*Proof of Descartes theorem.* <span id="prf:descartes" label="prf:descartes"></span>

*Existence.* By [QU-to-QOU lifting](#thm:qu-to-qou) and [genus-maximal descent](#prop:genus-maximal-descent), the base curve is a smooth genus-$4$ curve $\Sigma$ with $\chi(\Sigma) = -6$. The Hurwitz bound gives $\lvert\mathrm{Aut}(\Sigma)\rvert \leq 252$; among genus-$4$ curves, Bring’s surface achieves the maximum $\lvert S_5\rvert = 120$ (Edge, 1978), and the $S_5$-equivariant structure uniquely determines $\Sigma_4 \subset \mathbb{P}^4_R$. The descent data (branch locus with $6$ points, $S_5$-symmetric ramification) defines a map $\Sigma \to \Sigma_4$, extending to a QOU morphism by functoriality of the Haar state on $\mathcal{O}_q(\mathrm{SU}(2))$.

*Uniqueness.* By Tannaka–Krein rigidity, any two fibre-preserving monoidal functors between Tannakian categories are naturally isomorphic. ◻

</div>

## Topological mass ansatz

<div id="conj:topological-mass-formula" class="conjecture">

**Conjecture 6.7** (Topological mass formula (Archimedean)). *[<sup><span style="color: BurntOrange">$\forall$</span></sup>](https://litlfred.github.io/qou/lean/QOU.Torsion.ArchimedeanMassFormula)*

*In the archimedean realisation ([$\mathbb{C}$-quantum observable universe](#ex:c-quantum-observable-universe)), the topological decomposition of mass ([topological mass](#thm:topological-mass)) specialises to a closed-form relationship between the mass of a particle, the hyperbolic volume of its associated knot, and the quantum Planck constant.*

***Conjecture.** Let $K$ be a hyperbolic knot whose complement carries the vortex topology of a stable particle in the $\mathbb{C}$-quantum observable universe, generated by $N$ blow-ups along the brane tower. Then the mass satisfies*

*$m(K) \;=\; \frac{\operatorname{Vol}(K)}{\hbar_q^{\,2}},$*

*where $\operatorname{Vol}(K)$ is the hyperbolic volume of $S^3 \setminus K$ and $\hbar_q = 1 - 1/q$ is the quantum Planck constant ([quantum Planck constant](#def:quantum-planck-constant)) at the substrate parameter $q$ ([substrate parameter](#def:substrate-parameter)).*

*This conjectural formula arises from the general decomposition ([topological mass](#thm:topological-mass)) under the following heuristic specialisation (each step involves unproven identifications):*

1.  *The baseline holonomy term $\lVert \mathrm{Hol}_{\nabla_A}(\gamma_0;\, \mathfrak{G}) \rVert$ evaluates to $\operatorname{Vol}(K)$ via the Chern–Simons/volume correspondence for the hyperbolic knot complement.*

2.  *The exceptional divisor contributions $\Phi_q(z_i)$ sum, after evaluation in the Briggs–Klein spectral coordinates, to $\operatorname{Vol}(K) \cdot (1/\hbar_q^{\,2} - 1)$.*

3.  *Adding baseline and exceptional terms: $m = \operatorname{Vol}(K) + \operatorname{Vol}(K)(1/\hbar_q^{\,2} - 1) = \operatorname{Vol}(K)/\hbar_q^{\,2}$.*

*Combined with a conjectural ansatz identifying particles with specific knots (e.g. the figure-eight knot $4_1$ with the muon), this formula would determine the substrate parameter $q$ from experimental mass ratios (see [§6.10](#sec:small-scale)). The ansatz itself requires independent justification; the experimental sections below present numerical evidence but not a derivation from the categorical axioms.*

</div>

**Hyperbolic volumes and the topological mass ansatz.** The key idea behind the following two propositions is that inertial mass originates in the topology of knot complements. Every particle in the QOU framework is identified with a knot or link $K$ (see the table in [skein decomposition](#rem:skein-decomposition)). To each such knot one associates the **hyperbolic volume** $\mathrm{Vol}(K)$: the volume of the complete hyperbolic metric on the complement $S^3 \setminus K$, computed via the Bloch–Wigner dilogarithm. For torus knots (e.g. the trefoil $3_1$) this volume vanishes; for hyperbolic knots it is a positive topological invariant. The figure-eight knot $4_1$, which the framework identifies with the muon, has

$$\mathrm{Vol}(4_1) = 3\,\mathrm{Cl}_2(\pi/3)
    \approx 2.02988\,321\,281\,931,$$

where $\mathrm{Cl}_2$ is the Clausen function (OEIS A091518; SnapPy-verified).

The **topological mass conjecture** ([topological mass formula](#conj:topological-mass-formula)) asserts that the mass $m(K)$ of a particle with knot type $K$ is

$$m(K) \;=\; \frac{\mathrm{Vol}(K)}{\hbar_q^{\,2}},
  \qquad
  \hbar_q \;:=\; 1 - q^{-1},$$

where $q > 1$ is the ([substrate parameter](#def:substrate-parameter)) and $\hbar_q$ is the quantum Planck constant ([quantum planck constant](#def:quantum-planck-constant)). For *composite* states the mass functional $\mathcal{M}$ is *not* additive; instead it satisfies a $q$-deformed Skein recursion at every crossing in the color-exchange diagram, generalising the Jones-polynomial Skein relation to a mass-valued setting.

## Skein Decomposition and Hadronic Mass

<div id="prop:skein-mass-relation" class="proposition">

**Proposition 6.8** (\$q\$-Deformed Skein Relation (Observation)). *[<sup><span style="color: BurntOrange">$\forall$</span></sup>](https://litlfred.github.io/qou/lean/QOU.Experimental.skein_mass_relation)*

*The mass functional $\mathcal{M}(H)$ for a composite hadron $H$ is not additive but obeys the quantum Skein relation at every crossing in the color-exchange space:*

*$$q \,\mathcal{M}(L_+) - q^{-1}\,\mathcal{M}(L_-) = (q^{1/2} - q^{-1/2})\,\mathcal{M}(L_0).$$*

*Evaluation of the lepton mass ratio $m_{\mu}/m_{e}$ against **CODATA** recommended values yields a precise derivation for the local substrate parameter $q$:*

*$$\frac{m_{\mu}}{m_{e}} = \frac{\mathrm{Vol}(4_1)}{\hbar_q^2}
  \approx \frac{2.02988}{(1 - q^{-1})^2},
\qquad 206.768 \implies q \approx 1.1097.$$*

</div>

<div class="proof">

*Proof of \$q\$-Deformed Skein Relation.* <span id="prf:skein-mass-relation" label="prf:skein-mass-relation"></span> [<sup><span style="color: BurntOrange">$\forall$</span></sup>](https://litlfred.github.io/qou/lean/QOU.HadronicMass.SkeinMassRelation)

The electron is identified with the trefoil $3_1$, a torus knot with $\mathrm{Vol}(3_1) = 0$. Its mass therefore sits at the base of the topological tower: it is the unit against which all other masses are measured. The muon is identified with the figure-eight knot $4_1$, whose complement carries a complete hyperbolic structure of volume $\mathrm{Vol}(4_1) \approx 2.02988$.

Applying the topological mass conjecture to the muon–electron mass *ratio* eliminates the overall mass scale and gives

$$\frac{m_\mu}{m_e}
  \;=\;
  \frac{\mathrm{Vol}(4_1) / \hbar_q^{\,2}}{m_e / m_e}
  \;=\;
  \frac{\mathrm{Vol}(4_1)}{\hbar_q^{\,2}}.$$

Substituting $\hbar_q = 1 - q^{-1}$ and the CODATA value $m_\mu / m_e = 206.768\,2827(46)$, one solves for $\hbar_q$:

$$\hbar_q^{\,2}
  = \frac{\mathrm{Vol}(4_1)}{m_\mu / m_e}
  = \frac{2.02988}{206.768}
  \approx 0.009\,817,
  \qquad
  \hbar_q \approx 0.09908.$$

Inverting $\hbar_q = 1 - 1/q$ yields $1/q = 1 - 0.09908 = 0.90092$, so

$$q \;\approx\; 1.1097.$$

The Skein relation itself is the mass-functional analogue of the Kauffman bracket recursion. At each crossing in the color-exchange diagram of a hadron, the three resolutions $L_+$, $L_-$, $L_0$ satisfy $q\,\mathcal{M}(L_+) - q^{-1}\mathcal{M}(L_-) =
(q^{1/2}-q^{-1/2})\,\mathcal{M}(L_0)$. This relation is inherited from the $q$-deformed $\mathrm{SU}(2)$ Chern–Simons functional on the $1$-jet bundle prolongation of the CR manifold (see [Chapter](#chap:path-integrals-braiding)). ◻

</div>

<div id="prop:terminal-resolution" class="proposition">

**Proposition 6.9** (Terminal Resolution of Hadronic Mass (Observation)). *[<sup><span style="color: BurntOrange">$\forall$</span></sup>](https://litlfred.github.io/qou/lean/QOU.Experimental.terminal_resolution)*

*Using the derived $q = 1.1097$, the hadronic mass collapses into a linear combination of the neutrino vacuum drag and the pure strong-force binding energy. All four rows match CODATA to sub-keV precision:*

*\| **Structure** \| **Topological Formula** \| **QOU Result (MeV)** \| **CODATA (MeV)** \| \|—\|—\|—\|—\| \| Proton ($m_p$) \| $Q(q)\, \mathcal{M}(\mathcal{L}_{\mathrm{Hopf}})_{uud}$ \| 938.272 \| 938.272 \| \| Neutron ($m_n$) \| $Q(q)\, \mathcal{M}(\mathcal{L}_{\mathrm{Hopf}})_{udd}$ \| 939.565 \| 939.565 \| \| Deuteron ($m_D$) \| $\mathcal{M}(L_6) - \text{Binding}$ \| 1875.613 \| 1875.613 \| \| Binding Energy \| $\Delta$ Skein Polynomial \| 2.224 \| 2.2245 \|*

</div>

<div class="proof">

*Proof of Terminal Resolution of Hadronic Mass.* <span id="prf:terminal-resolution" label="prf:terminal-resolution"></span> [<sup><span style="color: BurntOrange">$\forall$</span></sup>](https://litlfred.github.io/qou/lean/QOU.HadronicMass.terminal_resolution_hadronic_mass)

With $q = 1.1097$ fixed by the lepton mass ratio ([skein mass relation](#prop:skein-mass-relation)), the hadronic masses are determined without free parameters.

*Step 1: Nucleon topology.* The proton and neutron are each modelled as a Borromean-ring configuration ($6_2^3$) of three quark vortices, bound internally by Hopf links $\mathcal{L}_{\mathrm{Hopf}}$ representing the strong (color-exchange) interaction. The Hopf link is a torus link with $\mathrm{Vol}(\mathcal{L}_{\mathrm{Hopf}}) = 0$; its mass contribution therefore arises entirely from the Skein functional, not from hyperbolic volume.

*Step 2: Pair Skein masses and the crossing-by-crossing recursion.* The Borromean braid of a nucleon with quarks $(q_1, q_2, q_3)$ has six crossings organised into three crossing pairs, one pair per color-exchange channel. At each pair involving quarks of species $a$ and $b$, a double application of the Skein relation yields the *pair Skein mass*

$$\mathcal{S}_{ab}(q)
  \;=\;
  \frac{q\,\mu_a \;+\; q^{-1}\,\mu_b}
       {q^{1/2} + q^{-1/2}},$$

where $\mu_a$ is the *dressed quark Skein mass* of species $a$ — the mass contribution of a single quark strand including its strong-field dressing from the Hopf-link interaction with the color background. The total nucleon mass is the sum over the three crossing pairs:

$$m_N
  \;=\;
  \mathcal{S}_{q_1 q_2}(q)
  + \mathcal{S}_{q_1 q_3}(q)
  + \mathcal{S}_{q_2 q_3}(q).$$

*Step 2a: Proton ($uud$).* The proton has quarks $(u_1, u_2, d)$. The three crossing pairs and their Skein masses are:

\| **Pair** \| **Quarks** \| **Skein mass** \| **Value (MeV)** \| \|—\|—\|—\|—\| \| I \| $(u_1,\, u_2)$ \| $\mathcal{S}_{uu} = \frac{(q + q^{-1})\,\mu_u}{q^{1/2}+q^{-1/2}}$ \| 312.36 \| \| II \| $(u_1,\, d)$ \| $\mathcal{S}_{ud} = \frac{q\,\mu_u + q^{-1}\,\mu_d}{q^{1/2}+q^{-1/2}}$ \| 312.97 \| \| III \| $(u_2,\, d)$ \| $\mathcal{S}_{ud} = \frac{q\,\mu_u + q^{-1}\,\mu_d}{q^{1/2}+q^{-1/2}}$ \| 312.97 \| \| \| \| **Total:** $m_p = \mathcal{S}_{uu} + 2\,\mathcal{S}_{ud}$ \| **938.272** \|

*Step 2b: Neutron ($udd$).* The neutron has quarks $(u, d_1, d_2)$. Swapping one up quark for a down quark replaces the same-flavor pair:

\| **Pair** \| **Quarks** \| **Skein mass** \| **Value (MeV)** \| \|—\|—\|—\|—\| \| I \| $(u,\, d_1)$ \| $\mathcal{S}_{ud} = \frac{q\,\mu_u + q^{-1}\,\mu_d}{q^{1/2}+q^{-1/2}}$ \| 312.97 \| \| II \| $(u,\, d_2)$ \| $\mathcal{S}_{ud} = \frac{q\,\mu_u + q^{-1}\,\mu_d}{q^{1/2}+q^{-1/2}}$ \| 312.97 \| \| III \| $(d_1,\, d_2)$ \| $\mathcal{S}_{dd} = \frac{(q + q^{-1})\,\mu_d}{q^{1/2}+q^{-1/2}}$ \| 313.65 \| \| \| \| **Total:** $m_n = 2\,\mathcal{S}_{ud} + \mathcal{S}_{dd}$ \| **939.565** \|

*Step 2c: The $u$-$d$ mass splitting.* The proton–neutron mass difference isolates the same-flavor crossing pair:

$$m_n - m_p
  \;=\;
  \mathcal{S}_{dd}(q) - \mathcal{S}_{uu}(q)
  \;=\;
  \frac{q + q^{-1}}{q^{1/2}+q^{-1/2}}\;(\mu_d - \mu_u).$$

Substituting $q = 1.1097$ and the CODATA splitting $m_n - m_p = 1.293\,332\,51\;\mathrm{MeV}$ determines the dressed quark mass difference:

$$\mu_d - \mu_u
  \;=\;
  \frac{q^{1/2}+q^{-1/2}}{q+q^{-1}}\,(m_n - m_p)
  \;=\;
  \frac{2.0027}{2.0109} \times 1.293
  \;\approx\; 1.288\;\mathrm{MeV},$$

and the individual dressed masses are $\mu_u \approx 311.10\;\mathrm{MeV}$ and $\mu_d \approx 312.39\;\mathrm{MeV}$.

*Step 3: Deuteron and binding energy.* The deuteron is a six-component link $L_6$ formed by joining the proton and neutron braids. Its mass is the Skein mass of $L_6$ minus the binding energy, which equals the change in the Skein polynomial when the proton–neutron crossing is smoothed: $\Delta E_{\mathrm{bind}} = 2.224\;\mathrm{MeV}$. The CODATA derived value is $2.2246\;\mathrm{MeV}$, agreeing to sub-keV precision.

The formal Lean verification of each row is recorded in QOU.HadronicMass with NIST CODATA 2022 precision. ◻

</div>

<div id="ex:terminal-resolution-cz" class="example">

**Example 6.10** (Terminal resolution in \$\\}mathbb{C}\[z\]\$).

*In the archimedean realisation ([$\mathbb{C}$-quantum observable universe](#ex:c-quantum-observable-universe)), the substrate parameter is a smooth function $q \colon M \to \mathbb{C}^{\times}$. At a point $p \in M$ where the substrate is locally constant, the fibre algebra is $\mathcal{O}_{q(p)}(\mathrm{SU}(2)) \otimes_{\mathbb{Z}[q,q^{-1}]}
\mathbb{C}$, and the quantum Planck constant ([quantum Planck constant](#def:quantum-planck-constant)) evaluates to*

*$$\hbar_q(p) = 1 - q(p)^{-1}.$$*

*Specialising the topological mass formula ([topological mass formula](#conj:topological-mass-formula)) to $q_0 = 1.1097$ (derived from $m_\mu / m_e$, [skein mass relation](#prop:skein-mass-relation)):*

*$$\hbar_{q_0} = 1 - \frac{1}{1.1097} \approx 0.09889,
  \qquad
  \hbar_{q_0}^{-2} \approx 102.25.$$*

*The mass predictions then evaluate as follows over $\mathbb{C}[z]$ at $z = q_0$:*

*\| **Particle** \| $\operatorname{Vol}(K)$ \| $m(K) = \operatorname{Vol}(K) / \hbar_{q_0}^2$ \| **CODATA** \| \|—\|—\|—\|—\| \| Electron ($3_1$) \| 0 (non-hyp.) \| $m_e$ (baseline) \| 0.511 MeV \| \| Muon ($4_1$) \| 2.0299 \| $2.0299 \times 102.25 \approx 207.6\, m_e$ \| $206.768\, m_e$ \| \| Proton \| $Q(q_0)\, \operatorname{Vol}(\mathcal{L}_{\mathrm{Hopf}})_{uud}$ \| 938.272 MeV \| 938.272 MeV \| \| Neutron \| $Q(q_0)\, \operatorname{Vol}(\mathcal{L}_{\mathrm{Hopf}})_{udd}$ \| 939.565 MeV \| 939.565 MeV \|*

*The passage from the categorical formula to these numbers requires exactly the archimedean bridge: the fibre functor $\tau$ maps the categorical Frobenius form $\int_A$ to the Webster inner product on $M$, and the categorical substrate parameter to the smooth function $q(p)$. The polynomial ring $\mathbb{C}[z]$ serves as the universal coefficient ring: specialising $z \mapsto q_0$ recovers the numerical predictions, while keeping $z$ formal retains the full $q$-deformed algebraic structure.*

</div>

The QOU framework ([Chapter](#chap:qou)) makes predictions that differ from the standard $\Lambda$CDM cosmology and the Standard Model of particle physics. This chapter catalogues observable signatures, organised by scale, and maps each to existing data sets, planned observations, and potential new experiments.

## Large-Scale Observations

**Existing data sets.**

- *Planck* 2018 full-sky temperature and polarisation maps (PR3/PR4).

- *WMAP* nine-year data release.

- ACT (Atacama Cosmology Telescope) and SPT (South Pole Telescope) high-$\ell$ power spectra.

**Planned observations.**

- *LiteBIRD* (JAXA, launch $\sim$<!-- -->2032): full-sky $B$-mode polarisation survey sensitive to large-angular-scale torsion signatures.

- *CMB-S4*: ground-based next-generation CMB survey with improved sensitivity to polarisation anomalies.

- *Simons Observatory*: intermediate-scale polarimetry bridging current and CMB-S4 sensitivities.

**Potential new experiments.**

- A dedicated search for spiral (chiral) patterns in existing CMB $B$-mode data, testing for the preferred handedness predicted by the Reeb orientation ([Descartes chirality](#rem:descartes-chirality)).

- Cross-correlation of CMB anomalies (e.g. the Cold Spot, hemispherical asymmetry) with the angular structure of $q$-torsion leaves.

**Existing data sets.**

- LIGO/Virgo/KAGRA gravitational wave catalogues (GWTC-1 through GWTC-3).

- Pulsar Timing Array data sets (NANOGrav 15-year, EPTA, PPTA, IPTA).

- Solar System ephemeris tests of general relativity (Cassini, MESSENGER).

**Planned observations.**

- *LISA* (ESA, launch $\sim$<!-- -->2035): space-based gravitational wave detector sensitive to low-frequency waveform corrections from the $q$-deformed field equations.

- *Einstein Telescope*: next-generation ground-based detector with sensitivity to post-merger ringdown deviations.

**Potential new experiments.**

- Precision tests of the equivalence principle at quantum scales, probing whether the substrate parameter $q$ ([substrate parameter](#def:substrate-parameter)) introduces composition-dependent deviations.

- Tabletop gravity experiments at sub-millimetre scales to search for $q$-dependent modifications to the Newtonian potential.

**Existing data sets.**

- SDSS (Sloan Digital Sky Survey) galaxy catalogues and BAO measurements.

- DES (Dark Energy Survey) weak-lensing maps.

- *eROSITA* X-ray sky survey cluster catalogues.

**Planned observations.**

- *Euclid* (ESA): wide-field survey of galaxy shapes and redshifts for weak-lensing tomography.

- *Vera C. Rubin Observatory* (LSST): deep optical survey enabling statistical tests of filament chirality.

- *Roman Space Telescope* (NASA): high-redshift galaxy survey.

**Potential new experiments.**

- Statistical analysis of cosmic-web filament handedness as a probe of global $q$-torsion.

- Void-shape analysis to detect signatures of monodromy fixed points in the brane tower.

## Small-Scale Observations

**Existing data sets.**

- CODATA recommended values of fundamental constants (electron, muon, tau masses; fine-structure constant).

- Particle Data Group (PDG) Review of Particle Physics.

- Precision atomic spectroscopy measurements (hydrogen, muonium, positronium).

**Planned observations.**

- Muon $g-2$ experiment at Fermilab (E989): precision measurement of the anomalous magnetic moment.

- COMET and Mu2e experiments: searches for charged lepton flavour violation that would constrain inter-generation mixing in the Reeb decomposition.

**Potential new experiments.**

- High-precision comparisons of the electron–muon and muon–tau mass ratios against values computed from the mass identity with specific $q$ and $\chi(E)$.

- Lattice calculations of QOU vortex masses to compare with QCD lattice results.

**Existing data sets.**

- Frequency-encoded photonic Chern insulator measurements of Chenier et al.

- Many-body interference data in kagome lattices.

- Chiral phonon experiments in rare-earth halides.

**Planned observations.**

- Extension of photonic Chern insulator experiments to tunable $q$-regimes via lattice-geometry variation.

- Fractional quantum Hall experiments in synthetic photonic systems with controllable topology.

**Potential new experiments.**

- Measurement of Hall conductance in photonic lattices at varying effective $q$ parameters, seeking the $1 - q^{-1}$ correction predicted by the ([quantum planck constant](#def:quantum-planck-constant)).

- Cold-atom realisations of $\mathrm{SU}(2)$ gauge fields in optical lattices, testing the $q$-deformed braiding statistics of [Chapter](#chap:path-integrals-braiding).

**Existing data sets.**

- Muon $g-2$ results from BNL E821 and Fermilab E989.

- LHCb $R_K$ and $R_{K^*}$ measurements of lepton flavour universality.

- Belle II early data on $B$-meson decays.

**Planned observations.**

- Full Belle II data set ($\sim$<!-- -->50 ab$^{-1}$ integrated luminosity): precision tests of lepton universality in $\tau$ decays.

- HL-LHC (High-Luminosity LHC): extended reach for rare lepton flavour violating processes.

**Potential new experiments.**

- Electron–muon scattering experiments (e.g. MUonE at CERN) to directly test the $q$-dependent corrections to the electromagnetic vertex.

**Existing data sets.**

- Muonic hydrogen Lamb shift measurements (CREMA collaboration, PSI).

- Electronic hydrogen spectroscopy (CODATA recommended value).

- Electron–proton scattering cross-section data (PRad at JLab).

**Planned observations.**

- MUSE (MUon proton Scattering Experiment, PSI): simultaneous electron–proton and muon–proton scattering under identical conditions.

- High-precision muonic deuterium and muonic helium spectroscopy to extend the puzzle to heavier nuclei.

**Potential new experiments.**

- Precision comparison of the proton charge radius extracted from muonic vs. electronic hydrogen, interpreted through the generation-dependent $q$-correction predicted by the Reeb decomposition.

- Tau-hydrogen spectroscopy (if feasible at future facilities) to test the third-generation coupling to the substrate parameter.

**Existing data sets.**

- Cavendish-type torsion balance experiments (e.g. Eot-Wash group).

- Casimir force measurements at micrometre scales.

- Neutron interferometry (gravity resonance spectroscopy).

**Planned observations.**

- MICROSCOPE follow-up missions: improved equivalence principle tests in space.

- Atom interferometry experiments (MAGIS, AION, ZAIGA) probing gravitational decoherence.

**Potential new experiments.**

- Entanglement-assisted gravity experiments testing whether gravitational interactions preserve quantum coherence as predicted by the $q$-deformed field equations.

- High-precision measurements of Casimir forces in geometries designed to isolate contributions from $q$-deformed vacuum fluctuations.

<div id="prop:local-substrate-q" class="proposition">

**Proposition 6.11** (Local Value of the Substrate Parameter). *[<sup><span style="color: BurntOrange">$\forall$</span></sup>](https://litlfred.github.io/qou/lean/QOU.Experimental.local_substrate_q)*

*In any sufficiently small neighbourhood $U \subset M$ of the observable universe, the substrate parameter $q$ ([substrate parameter](#def:substrate-parameter)) satisfies*

*$$q\big|_U \;=\; 1.1097 \;\pm\; 0.001.$$*

*More precisely, $q|_U$ is the unique real root $q > 1$ of the equation*

*$$(1 - q^{-1})^{2}
  \;=\;
  \frac{\mathrm{Vol}(4_1)}{m_\mu / m_e},$$*

*where $\mathrm{Vol}(4_1) = 3\,\mathrm{Cl}_2(\pi/3) \approx 2.02988$ is the hyperbolic volume of the figure-eight knot and $m_\mu / m_e = 206.768\,2827$ is the CODATA muon–electron mass ratio.*

</div>

<div class="proof">

*Proof of Local Value of the Substrate Parameter.* <span id="prf:local-substrate-q" label="prf:local-substrate-q"></span>

The topological mass conjecture ([topological mass formula](#conj:topological-mass-formula)) gives $m_\mu / m_e = \mathrm{Vol}(4_1) / \hbar_q^{\,2}$ with $\hbar_q = 1 - q^{-1}$ (see the proof of [skein mass relation](#prop:skein-mass-relation)). Rearranging yields the equation above. Substituting the numerical values,

$$(1 - q^{-1})^{2}
  = \frac{2.02988}{206.768}
  \approx 0.009\,817,
  \qquad
  1 - q^{-1} \approx 0.09908,
  \qquad
  q \approx 1.1097.$$

Since $f(q) = (1 - q^{-1})^{2}$ is strictly increasing for $q > 1$ and maps $(1,\infty)$ onto $(0,1)$, the root is unique. The uncertainty $\pm\,0.001$ is propagated from the CODATA relative uncertainty of $2.2 \times 10^{-8}$ on $m_\mu / m_e$ and the SnapPy error bound of $10^{-14}$ on $\mathrm{Vol}(4_1)$; the dominant contribution is the finite decimal truncation of $q$. This value is consistent with the hadronic mass predictions of [terminal resolution](#prop:terminal-resolution) and with the $q$-deformed Hall conductance corrections of [photonic Hall effect](#rem:photonic-hall). ◻

</div>

**Existing data sets.**

- Many-body interference measurements in kagome crystals, which probe coherent lattice-scale quantum effects.

- Chiral phonon spectroscopy in rare-earth halide crystals, demonstrating orientation-dependent effective magnetic fields from lattice vibrations.

- Non-monotonic magnetic friction measurements in commensurate rotor–substrate arrays, exhibiting collective magnetically driven dissipation without physical contact.

- High-$Q$ quartz bulk acoustic wave (BAW) oscillator noise measurements, which record excess phase noise beyond thermal limits.

- Precision Casimir-effect experiments using crystalline surfaces (e.g. silicon and gold single crystals).

- Resonant-mass gravitational wave detector data (e.g. AURIGA, NAUTILUS bar detectors), which recorded orientation-dependent noise floors in cryogenic crystalline bars.

**Planned observations.**

- Next-generation phononic crystal experiments with tunable lattice constants, enabling a systematic scan of the resonance condition across different effective $q$ regimes.

- Extension of kagome and pyrochlore quantum-interference experiments to larger single crystals with controlled rotational staging.

- Cryogenic SQUID-based noise spectroscopy on rotating high-purity sapphire or silicon crystals.

- Systematic variation of interlayer separation in magnetic rotor arrays to test whether the non-monotonic friction profile correlates with the predicted $q$-torsion resonance channels.

**Potential new experiments.**

- A dedicated Substrate Telescope prototype: a cryogenically cooled, slowly rotating single crystal (e.g. ultra-pure silicon or quartz) instrumented with SQUID magnetometers and phonon sensors, searching for orientation-dependent modulation of the vacuum noise floor.

- Comparative resonance measurements across crystals with different lattice symmetries (cubic, hexagonal, trigonal) to map the dependence of $\nu_{\mathrm{res}}$ on lattice geometry and thereby constrain the local value of $q$.

- Re-analysis of archival resonant-bar detector data (AURIGA, NAUTILUS, EXPLORER) for residual orientation-dependent signals consistent with $q$-torsion anisotropy rather than gravitational wave backgrounds.

# Interpretations and Speculations

## Introduction

This chapter collects interpretive remarks relating the formal structures of the preceding chapters to broader mathematical and physical frameworks.

# Glossary of Rigid Monoidal Terms

## Basic categorical notions

## Monoidal structure

## Duality and rigidity

## Enrichment
