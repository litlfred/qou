---
doc_id: arxiv-1211.1812v5
doc_title: "Presheaves of superselection structures in curved spacetimes"
section_id: sec-005-3-presheaves-in-quantum-field-theory
section_title: "Presheaves in quantum field theory."
section_number: 3
pages: 13-14
source_pdf: 1211.1812v5.pdf
source_sha256: 211667ea1312d47f
toc_source: outline
text_source: latex
latex_prose_ratio: 0.99
latex_coverage_ratio: 0.995
doc_brief: "Presheaves of superselection structures in curved spacetimes — We show that superselection structures on curved spacetimes, that are expected to describe quantum charges aﬀected by the underlying"
---
[]{#sec.qft label="sec.qft"}

In the present section we give the main result of the present paper, showing that the superselection structures over globally hyperbolic spacetimes introduced by Brunetti and Ruzzi ([@BR08]) can be interpreted as section categories of simple, symmetric tensor presheaves.

Actually, the fact that a superselection structure defines a *net* $\EuFrak{T}$ of tensor *C\**-categories was recognized in [@GLRV01 §3], [@Rob §27] (see Ex.[\[ex.Rob\]](#ex.Rob){reference-type="ref" reference="ex.Rob"}). Nevertheless $\EuFrak{T}$ does not suffice to characterize the superselection structure itself (see [@GLRV01 §3.3], [@BR08 §5.1]), so, rather than \*-endomorphisms as in [@GLRV01; @Rob], we make use of cocycles, a point of view introduced by J.E. Roberts ([@Rob0]).

#### Sectors with nontrivial holonomy.

Let $M$ be a globally hyperbolic spacetime. Then we have a *causal disjointness relation*, that is, a binary, symmetric relation $\perp$ defined on subsets of $M$, see [@GLRV01 §2.1]. The physical meaning of $\perp$ is that it encodes Einstein causality, which states that events localized in causally disjoint regions of $M$ do not interfere one each other.

In the following $\Delta$ shall denote the base of diamonds generating the topology of $M$ (see [@GLRV01 §2.1] or, more shortly, [@BR08 §3.1]), thus the abstract results of the previous section apply.

We note that any $a \in \Delta$ has proper, compact closure $\overline{a}$.

To be concise we write $e < a$ whenever the closure of $e \in \Delta$ is a proper subset of $a \in \Delta$, and set $\Delta^a := \{ e \in \Delta : e < a \}$. By [@BR08 Lemma B.5], for any $e \in \Delta^a$ there is $o \in \Delta^a$ with $o \perp e$.

Given the Hilbert space $H$, a *Haag-Kastler net* over $M$ is given by a net of von Neumann algebras

$\EuFrak{R}= (R,j)_\Delta \subset BH$,

fulfilling the following properties:

1.  Einstein causality: $R_o \subseteq R_e'$ for any $e \perp o$;

2.  Irreducibility: $\cap_a R_a' = {\mathbb C}1$;

3.  Outer regularity: $R_a = \cap_{a < o} R_o$ for any $a \in \Delta$;

4.  Borchers property: for any $a \in \Delta$, $e < a$ and projection $E \in R_e$ there is an isometry $V_a \in R_a$ such that $E = V_aV_a^*$.

5.  Punctured Haag duality: if $x \in M$, then we have

    $R_a = \cap \{ R_o' : o \in \Delta , o \perp a , \overline o \perp \{ x \} \}$

    for any $a \in \Delta$ with $\overline a \perp \{ x \}$.

The crucial property from the viewpoint of physical significance is Einstein causality, which states the principle that spacelike separated quantum observables must commute and hence there is not uncertainty between them.

The standard way to construct Haag-Kastler nets on curved spacetimes is the use of free fields ([@Dim80; @Dim82; @BFM09]).

About (punctured) Haag duality, see [@Ver97; @Ruz05a] and related references.

We now define the $C^*$-category

$Z^1(\EuFrak{R})$

with objects unitary cocycles

$$z := \{ z(b) \in UR_{|b|} \}_{b \in \Sigma_1(\Delta)}
\ \ : \ \
dz(c) := z(\partial_0c) z(\partial_2c) z(\partial_1c)^* = 1
\ , \
\forall c \in \Sigma_2(\Delta)
\ ,$$

and arrows

$$(z,z')
\ := \
\{ \ t = \{ t_a \in R_a \}_{a \in {\Delta}} 
     \ : \
     t_{\partial_0b} z(b)  =  z'(b) t_{\partial_1b}
     \ , \
     \forall b \in \Sigma_1(\Delta) \ \} \ .$$

For any path $p : a \to o$, we set

$$z(p) := z(b_n) \cdots z(b_1)
\ \ , \ \
p = b_n * \ldots * b_1 \ .$$

In particular, we have the identity cocycle $\iota(b) := 1$, $\forall b \in \Sigma_1(\Delta)$. Note that if $t \in (\iota,\iota)$ then $t_a \equiv t_0$, $\forall a \in \Delta$, with $t_0 \in \cap_a R_a$; we have

$$\label{eq.Ap1}
\cap_{a \ni x} R_a = {\mathbb C}1 
\ \ , \ \
\forall x \in M$$

(see [@BR08 §3.2],[@Ruz05 Eq.23]) and this implies $(\iota,\iota) = {\mathbb C}1$.

 

As argued in [@BR08 §4], $Z^1(\EuFrak{R})$ encodes a superselection structure that gives rise to quantum charges affected by the topology of $M$: for any $z \in {\bf obj \ }Z^1(\EuFrak{R})$ we define $H^z_a := H$, $a \in \Delta$, and unitaries

$$U^z_{a'a} := z(a,a';a') : H^z_a \to H^z_{a'}
\ \ \Rightarrow \ \ 
U^z_{a''a'} U^z_{a'a} = U^z_{a''a}
\ , \
\forall a \subseteq a' \subseteq a''
\ .$$

This defines the Hilbert net bundle $\EuFrak{H}^z := (H^z,U^z)_\Delta$, which, on turns, yields the *C\**-net bundle $\EuFrak{B}\EuFrak{H}^z = ( BH^z , {\mathrm{ad}}U^z )_\Delta$ and the representation

$$\label{eq.C00}
\pi^z : \EuFrak{R}\to \EuFrak{B}\EuFrak{H}^z
\ \ , \ \
\pi^z_a(t) := z(p) t z(p)^*
\ \ , \ \qquad
\forall a \in \Delta
\ , \
t \in R_a \ ,
\ {\mathrm{with}} \
p : a \to o
\ , \
o \perp a$$

(see [@BR08 Appendix A]). When $\EuFrak{H}^z$ is trivial we have sectors in the classical sense (topologically trivial sectors), that define representations of Fredenhagen's universal algebra $\vec{R}$ ([@Fre]). When $M$ is the Minkowski spacetime $Z^1(\EuFrak{R})$ is the well-known DHR-superselection structure (see [@Rob0]).

The conjugation structure on $Z^1(\EuFrak{R})$, which encodes the particle-antiparticle correspondence in the setting of superselection sectors, is defined in the following standard way ([@DR89; @DR90; @GLRV01; @Ruz05; @BR08]): a cocycle $\bar z \in {\bf obj \ }Z^1(\EuFrak{R})$ is said to be a *conjugate* of $z \in {\bf obj \ }Z^1(\EuFrak{R})$ whenever there are

$r \in (\iota,\bar z \otimes z)$ and $\bar{r} \in (\iota,z \otimes \bar z)$

fulfilling the conjugate equation

$$\bar{r}^* \otimes 1_z \cdot 1_z \otimes r \, = \, 1_z
\ \ , \ \
r^* \otimes 1_{\bar z} \cdot 1_{\bar z} \otimes \bar{r} \, = \, 1_{\bar z}$$

(about the meaning of $\otimes$ we refer the reader to [@BR08 §5], anyway it should be clear by reading the next subsection).

In accord with the discussion of [@BR08 §5.3], the full subcategory $Z^{1,\bullet}(\EuFrak{R})$ of $Z^1(\EuFrak{R})$ with objects cocycles admitting a conjugate is a DR-category and yields the set of sectors with finite statistics.

The rest of the section is devoted to the proof that $Z^1(\EuFrak{R})$ is the section category of a simple, symmetric tensor presheaf. This automatically gives to $Z^1(\EuFrak{R})$ the structure of a symmetric tensor *C\**-category with simple unit, that, as we shall see, coincides with the one defined in [@BR08 §5].

For reader's convenience, and due to the fact that we shall work with restricted nets that may not fulfill Haag duality, often we shall write explicitly standard computations.
