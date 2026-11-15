---
doc_id: arxiv-1211.1812v5
doc_title: "Presheaves of superselection structures in curved spacetimes"
section_id: sec-003-22-nets-of-c-algebras
section_title: "Nets of C*-algebras."
section_number: 2.2
pages: 7-9
source_pdf: 1211.1812v5.pdf
source_sha256: 211667ea1312d47f
toc_source: outline
text_source: latex
latex_prose_ratio: 0.985
latex_coverage_ratio: 0.979
doc_brief: "Presheaves of superselection structures in curved spacetimes — We show that superselection structures on curved spacetimes, that are expected to describe quantum charges aﬀected by the underlying"
---
[]{#sec.back.nets label="sec.back.nets"}

A *net*

[^1]

of *C\**-algebras over $\Delta$ is given by a family $A = \{ A_a \}_{a \in \Delta}$ of unital *C\**-algebras, and unital \*-monomorphisms (called *the net structure*)

$$\jmath_{a'a} : A_a \to A_{a'}
\ \ : \ \
\jmath_{a''a'} \circ \jmath_{a'a} = \jmath_{a''a}
\ \ , \ \
\forall a \subseteq a' \subseteq a''
\ .$$

We shall use the notation $\EuFrak{A}= (A,\jmath)_\Delta$. Morphisms

$\nu : \EuFrak{A}\to \EuFrak{A}'$

of nets of *C\**-algebras are defined by families of \*-morphisms

$$\nu_a : A_a \to A'_a
\ \ : \ \
\nu_{a'} \circ \jmath_{a'a} = \jmath'_{a'a} \circ \nu_a
\ \ , \ \
\forall a \subseteq a'
\ .$$

In algebraic quantum field theory it is customary to consider nets such that there is a Hilbert space $H$ with $A_a \subseteq BH$ for any $a \in \Delta$, and any

$\jmath_{a'a}$, $a \subseteq a'$,

is the inclusion map. In this case we write

$$\EuFrak{A}= (A,\jmath)_\Delta \subset BH \ .$$

#### Net bundles ([@RRV07; @RRV08; @RV11]).

When every $\jmath_{a'a}$ is an isomorphism we say that $\EuFrak{A}$ is a *C\**-*net bundle*; picking a family $\nu$ of \*-isomorphisms

$\nu_a : A_a \to A_*$, $\forall a \in \Delta$,

and defining

$$\jmath'_{a'a} \in {\bf aut}A_*
\ \ , \ \
\jmath'_{a'a} := \nu_{a'} \circ \jmath_{a'a} \circ \nu_a^{-1}
\ \ , \ \
\forall a \subseteq a'
\ ,$$

we obtain a *C\**-net bundle $\EuFrak{A}' = (A',\jmath')_\Delta$ with constant fibre $A'_a \equiv A_*$ and isomorphic to $\EuFrak{A}$. We call $\nu$ a *choice of the standard fibre* of $\EuFrak{A}$,

and denote the set of *C\**-net bundles with fibre isomorphic to $A_*$ by

$${\bf bun}(\Delta,A_*) \ .$$

To be concise we write $\jmath_{aa'} := \jmath_{a'a}^{-1}$, $\forall a \subseteq a'$. For any $b \in \Sigma_1(\Delta)$ we define

$\jmath_b := \jmath_{\partial_0b \, |b|} \circ \jmath_{|b| \, \partial_1b}$,

and, assuming that a choice of the standard fibre $A_*$ has been made,

$$\label{eq.back3a}
\chi_p :=  \jmath_{b_n} \circ \ldots \circ \jmath_{b_1} \ \in {\bf aut}A_*
\ \ , \ \
\forall p = b_n * \ldots * b_1 : a \to a
\ .$$

The map $\chi_p$, $p : a \to a$, factorizes through homotopy, so it yields the *C\**-dynamical system

$\chi : \pi_1(\Delta) \to {\bf aut}A_*$.

Indeed, assigning the *holonomy*

$$\label{eq.back3}
\EuFrak{A}\mapsto \chi$$

defines an equivalence from the category of *C\**-net bundles to the one of $\pi_1(\Delta)$-dynamical *C\**-systems.

Analogous definitions, notations and properties hold in the cases of group net bundles and Hilbert net bundles. In the first case we have group isomorphisms

$\imath_{a'a}: G_a \to G_{a'}$, $\forall a \subseteq a'$,

defining the *group net bundle* $\EuFrak{G}= (G,\imath)_\Delta$, whilst in the second case we have unitaries

$U_{a'a}: H_a \to H_{a'}$, $\forall a \subseteq a'$,

defining the *Hilbert net bundle* $\EuFrak{H}= (H,U)_\Delta$.

We have the composition of equivalences

$$\label{eq.hol}
\EuFrak{P}\ \stackrel{ (\ref{eq.back3}) }{\longrightarrow} \ 
\chi \ \stackrel{ (\ref{eq.back2}) }{\longrightarrow} \ 
P_\chi \ ,$$

assigning to any net bundle $\EuFrak{P}$ the locally constant bundle $P_\chi$, which holds when the fibres are *C\**-algebras, Hilbert spaces and topological groups. The geometric content of ([\[eq.hol\]](#eq.hol){reference-type="ref" reference="eq.hol"}) is that $\chi$ is the holonomy of $\EuFrak{P}$ or, equivalently, the monodromy of $P_\chi$, whilst $\EuFrak{P}$ can be understood as a precosheaf of local sections of $P_\chi$.

#### Representations ([@BR08; @RV11]).

Let $\EuFrak{A}= (A,\jmath)_\Delta$ be a net of *C\**-algebras. A *representation* of $\EuFrak{A}$ is a pair $(\pi,U)$, where

$H = \{ H_a \}_{a \in \Delta}$

is a family of Hilbert spaces,

$U = \{ U_{a'a} : H_a \to H_{a'} \}_{a \subseteq a'}$

is a family of unitary operators and

$\pi_a : A_a \to BH_a$, $a \in \Delta$,

is a family of Hilbert space representations such that

$$U_{a''a} = U_{a''a'} U_{a'a} 
\ \ , \ \
{\mathrm{ad}}U_{a'a} \circ \pi_a = \pi_{a'} \circ \jmath_{a'a}
\ \ , \ \
a \subseteq a' \subseteq a'' 
\ .$$

Defining the Hilbert net bundle $\EuFrak{H}= (H,U)_\Delta$ we obtain the *C\**-net bundle $\EuFrak{B}\EuFrak{H}= (BH,{\mathrm{ad}}U)_\Delta$ and $(\pi,U)$ can be regarded as a morphism

$\pi : \EuFrak{A}\to \EuFrak{B}\EuFrak{H}$.

When $\EuFrak{H}$ is trivial

[^2]

we have Hilbert space representations, that are those commonly used in algebraic quantum field theory.

#### Commutators on Hilbert net bundles.

We give a notion of commutator for operators on Hilbert net bundles, designed to be coherent with the underlying net structure and not depending, like the one used in [@BR08 Eq.3.6], on the choice of the standard fibre. We shall use this notion to propose a refined notion of causality for nets in generic spacetimes (see §[\[sec.gauge\]](#sec.gauge){reference-type="ref" reference="sec.gauge"}).

Let $\EuFrak{H}= (H,U)_\Delta$ be a Hilbert net bundle. We say that $\EuFrak{H}$ is trivial on $\Omega \subseteq \Delta$ whenever the restriction

$\EuFrak{H}_\Omega := (H,U)_\Omega$

is a trivial Hilbert net bundle.

Given $a,o \in \Delta$, we say that a path

$p : o \to a$, $p=b_n * \ldots * b_1$,

is *trivialized* by $\EuFrak{H}$ whenever there is $\Omega \subseteq \Delta$ such that: (1) $\EuFrak{H}$ is trivial on $\Omega$; (2) $b_i \in \Sigma_1(\Omega)$, $\forall i=1,\ldots,n$.

We denote the set of paths trivialized by $\EuFrak{H}$ by $\pi_0(\Delta,\EuFrak{H})$.

Given $a,o \in \Delta$ and $T \in BH_a$, $T' \in BH_o$, we write

$[T,T']^{net}_\pm = 0$

whenever

$$\label{eq.nets1}
[T,T']^p_\pm \ := \ T \cdot U_p T'U_p^* \pm U_p T'U_p^* \cdot T \ = \ 0 
\ \ , \ \
\forall p : o \to a \ , \ p \in \pi_0(\Delta,\EuFrak{H})
\ ,$$

where $U_p := U_{b_n} \cdots U_{b_1}$, $p = b_n * \ldots * b_1$ (recall that we set $U_b := U_{{\partial_0 b}|b|} U_{|b| {\partial_1 b}}$, $\forall b \in \Sigma_1(\Delta)$).

Note that the previous expression makes sense since $U_p T'U_p^* \in BH_a$. Moreover ([\[eq.nets1\]](#eq.nets1){reference-type="ref" reference="eq.nets1"}) is symmetric in the sense that $[T,T']^p_\pm = 0$ if, and only if,

$${}^p[T,T']_\pm \ := \ U_{\overline p}TU_{\overline p}^* \cdot T' \pm T' \cdot U_{\overline p}TU_{\overline p}^* \ = \ 0 \ ,$$

where $\overline p \in \pi_0(\Delta,\EuFrak{H})$, $\overline p : a \to o$, is the opposite path. Note that:

-   the fact that $p$ is trivialized by $\EuFrak{H}$ means that there is a Hilbert space $H'$ with unitaries $V_e : H_e \to H'$, $e \in \Omega$, such that

    $U_{e'e} = V_{e'}^*V_e$, $\forall e \subseteq e' \in \Omega$.

    So we have

    $$U_p \ = \ V_a^* V_{|b_n|} \cdots V_{|b_1|}^* V_o \ = \ V_a^* V_o \ ,$$

    and $U_p$ is independent of the choice of the path $p$ with 1-simplices in $\Sigma_1(\Omega)$. When $a=o$ we have $U_p=1$ for any $p \in \pi_0(\Delta,\EuFrak{H})$, $p : a \to a$; thus $[T,T']^{net}_\pm$ is the usual (anti)commutator of $BH_a$.

-   if $\EuFrak{H}$ is trivial then any path is trivialized by $\EuFrak{H}$. In particular, when $\EuFrak{H}$ is the constant Hilbert net bundle, $U_p \equiv 1$ and we have the usual (anti)commutator;

-   if $\Omega \subseteq \Delta$ is such that $\pi_1(\Omega)= {\bf 0}$ and $p$ is made of 1-simplices in $\Sigma_1(\Omega)$, then $p$ is automatically trivialized by $\EuFrak{H}$; for example, we may take $\Omega$ directed.

    Note that restrictions to simply connected subsets of $\Delta$ appear in [@BR08 §3.2] to define sharp excitations of the vacuum state.

#### Gauge actions ([@Vas12]).

Let $\EuFrak{A}= (A,\jmath)_\Delta$ be a net of *C\**-algebras and $\EuFrak{G}= (G,\imath)_\Delta$ a group net bundle (we assume that the fibres of $\EuFrak{G}$ are locally compact and Hausdorff). A *gauge action* of $\EuFrak{G}$ on $\EuFrak{A}$ is given by a family of strongly continuous actions

$\alpha_o : G_o \to {\bf aut}A_o$, $\forall o \in \Delta$,

such that

$$\label{eq.GA00}
\{ \alpha_{o'} (\imath_{o'o} (g)) \} \circ \jmath_{o'o}
=
\jmath_{o'o} \circ \alpha_o (g)
\ \ , \ \
\forall g \in G_o
\ , \
o \subseteq o'
\ .$$

When $\EuFrak{G}$ is the constant net bundle (that is, any $\imath_{o'o}$ is the identity of a fixed group $G_*$), we have a group action of $G_*$ on $\EuFrak{A}$ by net automorphisms. A morphism $\nu : \EuFrak{A}\to \EuFrak{A}'$ is said to be $\EuFrak{G}$-*equivariant* whenever

$$\nu_a \circ \alpha_a(g) \ = \ \alpha'_a(g) \circ \nu_a
\ \ , \ \
\forall a \in \Delta \ , \ g \in G_a \ .$$

The notion of gauge action can be defined for a Hilbert net bundle

$\EuFrak{H}= (H,U)_\Delta$

as above, requiring that each

$\alpha_o(g)$, $o \in \Delta$, $g \in G_o$,

is a unitary operator on $H_o$. The category of $\EuFrak{G}$-equivariant Hilbert net bundles over $\Delta$, that we denote by

$${\bf Hilb}_\EuFrak{G}(\Delta) \ ,$$

is a symmetric tensor *C\**-category (see §[\[sec.back.presheaves\]](#sec.back.presheaves){reference-type="ref" reference="sec.back.presheaves"} for an explanation of these terms); it has a simple unit in the cases of interest, that is, when $\Delta$ is path-connected or, equivalently, when $M$ is arcwise connected (see [@RRV08 §5]).

[^1]: Here we should use the term *precosheaf*, nevertheless we prefer to maintain the traditional terminology.

[^2]: That is, $\EuFrak{H}$ is isomorphic to the constant Hilbert net bundle

    $\EuFrak{H}^0 = (H^0,U^0)_\Delta$,

    $H^0_a \equiv H_*$, $U^0_{a'a} \equiv 1_{H_*}$.
