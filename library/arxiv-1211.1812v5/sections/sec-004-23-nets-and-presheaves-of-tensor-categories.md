---
doc_id: arxiv-1211.1812v5
doc_title: "Presheaves of superselection structures in curved spacetimes"
section_id: sec-004-23-nets-and-presheaves-of-tensor-categories
section_title: "Nets and presheaves of tensor categories."
section_number: 2.3
pages: 9-13
source_pdf: 1211.1812v5.pdf
source_sha256: 211667ea1312d47f
toc_source: outline
text_source: latex
latex_prose_ratio: 0.986
latex_coverage_ratio: 0.962
doc_brief: "Presheaves of superselection structures in curved spacetimes — We show that superselection structures on curved spacetimes, that are expected to describe quantum charges aﬀected by the underlying"
---
[]{#sec.back.presheaves label="sec.back.presheaves"}

In the present section we recall some properties of nets and presheaves of tensor categories, that constitute one of the main objects of study in the present paper. More detailed references on this topic are [@Rob; @Vas12].

#### DR-categories.

A *C\**-*category* is a category $C$ whose spaces of arrows are Banach spaces endowed with an antilinear involution

$* : (\rho,\sigma) \to (\sigma,\rho)$, $\forall \rho,\sigma \in {\bf obj \ }C$,

such that

$(t \circ t')^* = t'^* \circ t^*$, $\| t^* \circ t \| = \| t \|^2$

for any pair of composable arrows $t,t'$. Since the composition of arrows is assumed to be linear, this implies that any $(\rho,\rho)$, $\rho \in {\bf obj \ }C$, is a *C\**-algebra.

We assume that functors between *C\**-categories preserve the involution structure. Following the terminology of [@ML §I.3], we say that a functor:

is an *embedding*, whenever it is faithful on the spaces of arrows; is *full*, whenever it is surjective on the spaces of arrows; is an *isomorphism*, whenever it has an inverse functor and, in particular, an *automorphism*, whenever the initial and target categories coincide.

A *tensor product* on $C$ is given by a bilinear bifunctor

$\otimes : C \times C \to C$,

and the *identity object* $\iota \in {\bf obj \ }C$ is characterized by the property that $\iota \otimes \rho = \rho \otimes \iota = \rho$ for any $\rho \in {\bf obj \ }C$. To be concise, in the sequel we shall write $\rho \sigma := \rho \otimes \sigma$, $\forall \rho,\sigma \in {\bf obj \ }C$. We say that $C$ has a *simple unit* whenever $(\iota,\iota) = {\mathbb C}1_\iota$, where $1_\iota$ is the identity arrow.

We say that the tensor product is *symmetric* whenever there is a family

$\epsilon_{\rho,\sigma} \in (\rho \sigma , \sigma \rho)$

of unitary arrows, inducing the flip

$(t \otimes t') \circ \epsilon_{\rho,\rho'} = \epsilon_{\sigma,\sigma'} \circ(t' \otimes t)$, $t \in (\rho,\sigma)$, $t' \in (\rho',\sigma')$,

and fulfilling the properties in [@DR89 §1]. In this case we write $C_{\otimes,\epsilon}$.

The category of finite dimensional, unitary representations (that is, the *dual*) of a compact group is the basic class of examples for a symmetric tensor *C\**-category with simple unit. A symmetric tensor *C\**-category with simple unit, conjugates, direct sums and subobjects in the sense of [@DR89 §1] is said to be a *DR-category*, and is automatically isomorphic to the dual of a compact group, unique up to isomorphism ([@DR89 Theorem 6.9]).

#### Nets of tensor categories.

A *net of tensor *C\**-categories* over $\Delta$ is given by a family $T = \{ T_a \}_{a \in \Delta}$ of tensor *C\**-categories and a family of tensor embeddings

$$\jmath_{a'a} : T_a \to T_{a'}
\ \ : \ \
\jmath_{a''a'} \circ \jmath_{a'a} = \jmath_{a''a}
\ \ , \ \
\forall a \subseteq a' \subseteq a''
\ .$$

We shall use the notation $\EuFrak{T}_\otimes = (T,\jmath)_\Delta$. We say that $\EuFrak{T}_\otimes$ is *simple* whenever every $T_a$, $a \in \Delta$, has a simple unit.

When every $\jmath_{a'a}$ is an isomorphism we say that $\EuFrak{T}_\otimes$ is a *net bundle* of tensor *C\**-categories.

When every $T_a$, $a \in \Delta$, has symmetry $\xi_a$ and

$\jmath_{a'a}(\xi_{a;\rho,\sigma}) = \xi_{a'; \jmath_{a'a}(\rho) , \jmath_{a'a}(\sigma)}$

for any $a \subseteq a'$, $\rho,\sigma \in {\bf obj \ }T_a$, we say that $\EuFrak{T}_\otimes$ is *symmetric* and write $\EuFrak{T}_{\otimes,\xi}$.

The next class of examples is motivated by the analysis of superselection structures in algebraic quantum field theory.

::: ex
(See [@Rob §27] and [@GLRV01 §3.3]). []{#ex.Rob label="ex.Rob"}

*Let $A$ be a unital *C\**-algebra. Then the semigroup ${\bf end}A$ of unital \*-endomorphisms of $A$ defines a tensor *C\**-category with sets of arrows*

$$\label{eq.intro0}
(\rho,\sigma) := \{ t \in A \ : \ t \rho(v) = \sigma(v)t \ , \ \forall v \in A \}
\ \ , \ \ 
\forall \rho,\sigma \in {\bf end}A
\ ,$$

whose composition is given by the product of $A$; the tensor product is given by

$$\label{eq.intro1}
\rho \otimes \sigma := \rho \sigma := \rho \circ \sigma
\ \ , \ \
t \otimes t' := t \rho(t')
\ \ , \ \
\forall \rho,\sigma,\rho',\sigma' \in {\bf end}A
\ , \ 
t \in (\rho,\sigma) \ , \  t' \in (\rho',\sigma')
\ .$$

Let now $H$ be a Hilbert space and $\EuFrak{R}= (R,\jmath)_\Delta \subset BH$ a net of *C\**-algebras on $H$. For any $a \in \Delta$ we consider the *C\**-algebra

$$R^a \, := \, C^* \{ R_o \}_{o \supseteq a } \subseteq BH$$

(note that $R_a \subseteq R^a$) and, given $\rho,\sigma \in {\bf end}R^a$, the space $(\rho,\sigma) \subseteq R^a$ of ([\[eq.intro0\]](#eq.intro0){reference-type="ref" reference="eq.intro0"}). We define the categories

$$T_a := 
\left\{
\begin{array}{ll}
{\bf obj \ }T_a \ := \ \{ \rho \in {\bf end}R^a : \rho(R_o) \subseteq R_o , \forall o \supset a \} \ ,
\\
{\bf arr}T_a \ := \ \{ (\rho,\sigma)_a := R_a \cap (\rho,\sigma) \ , \ \forall \rho,\sigma \in {\bf obj \ }T_a  \} \ ,
\end{array}
\right.$$

having tensor product ([\[eq.intro1\]](#eq.intro1){reference-type="ref" reference="eq.intro1"}). We have

$$R_a \subseteq R_{a'} \ \ , \ \ R^{a'} \subseteq R^a 
\ \ , \ \
\forall a \subseteq a' \ ,$$

and by definition any $\rho \in {\bf obj \ }T_a$ restricts to an endomorphism

$\jmath_{a'a}\rho \in {\bf obj \ }T_{a'}$.

Moreover we have inclusions

$$\jmath_{a'a} : (\rho,\sigma)_a \to ( \jmath_{a'a}\rho , \jmath_{a'a}\sigma )_{a'}
\ \ , \ \
\rho,\sigma \in {\bf obj \ }T_a \ ,$$

and this yields the net $\EuFrak{T}= (T,\jmath)_\Delta$. Finally, it is trivial to verify that $\jmath$ preserves the tensor structure, so $\EuFrak{T}_\otimes$ is a tensor net. Note that the identity of $T_a$ is the identity automorphism $\iota_a \in {\bf end}R^a$, so

$(\iota_a,\iota_a)_a = R_a \cap (R^a)'$.
:::

#### Presheaves.

There is a natural notion dual to the one of net: a *presheaf* of *C\**-categories is given by a family of embeddings

$$r_{aa'} : T_{a'} \to T_a
\ \ : \ \
r_{aa'} \circ r_{a'a''} = r_{aa''} 
\ \ , \ \
\forall a \subseteq a' \subseteq a''
\ .$$

We shall write $\EuFrak{T}= (T,r)^\Delta$. A *presheaf morphism* $\eta : \EuFrak{T}\to \EuFrak{T}'$ is a family of functors

$$\eta_a : T_a \to T'_a
\ \ : \ \
\eta_a \circ r_{aa'} = r'_{aa'} \circ \eta_{a'}
\ \ , \ \
\forall a \subseteq a' \ .$$

Notation and terminology for presheaves are analogous to the ones of nets, so we say that $\EuFrak{T}_\otimes$ is *simple* whenever every $T_a$, $a \in \Delta$, is simple, and write $\EuFrak{T}_{\otimes,\xi}$ to indicate presheaves endowed with a symmetric tensor structure. In particular, we say that $\eta$ is a *symmetric tensor* presheaf morphism whenever the involved structures are preserved by $\eta$.

We say that $\EuFrak{T}$ is *full* whenever every $r_{aa'}$, $a \subseteq a'$, is a full functor. In particular, a *presheaf bundle* is a presheaf $\EuFrak{T}= (T,r)^\Delta$ where any $r_{aa'}$ is an isomorphism. The map

$$\EuFrak{T}= (T,\jmath)_\Delta \ \mapsto \ \EuFrak{T}' = (T,r)^\Delta \ , \ 
r_{aa'} := \jmath_{a'a}^{-1} \ , \ 
\forall a \subseteq a' \ ,$$

yields an isomorphism from the category of net bundles to the one of presheaf bundles. Given a symmetric tensor *C\**-category $T_{\otimes,\epsilon}$, we denote the set of symmetric tensor presheaf bundles with fibre $T_{\otimes,\epsilon}$ by

${\bf pbun}^\uparrow(\Delta,T_{\otimes,\epsilon})$.

Reasoning as in ([\[eq.back3a\]](#eq.back3a){reference-type="ref" reference="eq.back3a"}), we obtain the one-to-one correspondence

$${\bf pbun}^\uparrow(\Delta,T_{\otimes,\epsilon}) \ \leftrightarrow\ \hom( \pi_1(\Delta) , {\bf aut}T_{\otimes,\epsilon} )
\ \ , \ \
\EuFrak{T}_{\otimes,\xi} \mapsto \chi \ ,$$

where ${\bf aut}T_{\otimes,\epsilon}$ is the group of symmetric tensor automorphisms of $T_{\otimes,\epsilon}$. We call $\chi$ the *holonomy of* $\EuFrak{T}_{\otimes,\xi}$.

::: ex
[]{#ex.back1 label="ex.back1"}

*Let $d \in {\mathbb N}$ and $\pi_G : G \to {{\mathbb U}(d)}$ denote the defining representation of a compact Lie group $G \subseteq {{\mathbb U}(d)}$.*

We denote the category of tensor powers of $\pi_G$ by $\widehat\pi_G$, which is a tensor *C\**-category with symmetry $\theta$.

The group $G$ defines a *C\**-algebra $\mathcal O_G$, the fixed-point algebra of the natural $G$-action on the Cuntz algebra $\mathcal O_d$ ([@DR87]). We define

$$QG \ := \ NG / G \ ,$$

where $NG \subseteq {{\mathbb U}(d)}$ is the normalizer of $G$. Since there are maps

$$QG \to {\bf aut}\widehat\pi_{G;\otimes,\theta}
\ \ , \ \
QG \to {\bf aut}\mathcal O_G$$

(see [@Vas09 §3]), by the previous considerations we obtain maps

$$\label{eq.FL08}
{\hom}( \pi_1(\Delta) , QG ) \ \to \ {\bf pbun}^\uparrow(\Delta,\widehat\pi_{G;\otimes,\theta}) 
\ \ , \ \
{\hom}( \pi_1(\Delta) , QG )    \ \to \ {\bf bun}(\Delta,\mathcal O_G) 
\ .$$
:::

#### Sections.

By definition, the *category of sections* of the symmetric tensor presheaf

$\EuFrak{T}_{\otimes,\xi} = (T,r)^\Delta$

has objects and, respectively, arrows

$$\left\{
\begin{array}{lllll}
\varrho = \{ \varrho_a \in {\bf obj \ }T_a \}_{a \in \Delta} 
& : &
r_{aa'}(\varrho_{a'}) = \varrho_a 
& , & 
\forall a \subseteq a' \ ,

\\

t = \{ t_a \in (\varrho_a,\varsigma_a) \}_{a \in \Delta}
& : &
r_{aa'}(t_{a'}) = t_a
& , &
\forall a \subseteq a' \ .
\end{array}
\right.$$

We denote it by $\widetilde\EuFrak{T}_{\otimes,\xi}$. It is easily verified that $\widetilde\EuFrak{T}_{\otimes,\xi}$ is a symmetric tensor *C\**-category, and we say that $\EuFrak{T}_{\otimes,\xi}$ is a *DR-presheaf* whenever $\widetilde\EuFrak{T}_{\otimes,\xi}$ is a DR-category.

::: rem
[]{#rem.back1 label="rem.back1"} Given the symmetric tensor presheaf $\EuFrak{T}_{\otimes,\xi} = (T,r)^\Delta$, for any $a \in \Delta$ we denote the full subcategory of $T_a$ with objects

$\varrho_a$, $\varrho \in {\bf obj \ }\widetilde\EuFrak{T}_{\otimes,\xi}$,

by $T^\downarrow_a$. Any $r_{aa'}$, $a \subseteq a'$, restricts to an embedding

$r^\downarrow : T^\downarrow_{a'} \to T^\downarrow_a$, $\forall a \subseteq a'$,

and this yields the symmetric tensor presheaf

$\EuFrak{T}^\downarrow_{\otimes,\xi} = (T^\downarrow,r^\downarrow)^\Delta$.

By construction the section categories of

$\EuFrak{T}_{\otimes,\xi}$, $\EuFrak{T}^\downarrow_{\otimes,\xi}$

coincide, that is

$\widetilde\EuFrak{T}_{\otimes,\xi}  =  \widetilde\EuFrak{T}^\downarrow_{\otimes,\xi}$.
:::

To illustrate a Tannaka duality for categories of sections we give the notion of *embedding*, that is, a symmetric tensor presheaf morphism

$$I \ : \ \EuFrak{T}_{\otimes,\xi} = (T,r)^\Delta \  \to \ \EuFrak{C}_{\otimes,\vartheta} = (C,r')^\Delta \ ,$$

such that:

\(1\) $\EuFrak{C}_{\otimes,\vartheta}$ is a full presheaf; (2) any $C_a$, $a \in \Delta$, is a full symmetric tensor subcategory of the one of finite-dimensional Hilbert spaces; (3) any $I_a$, $a \in \Delta$, is an embedding.

::: thm
[]{#thm_DUAL label="thm_DUAL"} Let $\EuFrak{T}_{\otimes,\xi} = (T,r)^\Delta$ be a simple, symmetric tensor presheaf having an embedding. Then there is a group net bundle $\EuFrak{G}= (G,i)_\Delta$ with a full symmetric tensor embedding

$\widetilde\EuFrak{T}_{\otimes,\xi} \to {\bf Hilb}_\EuFrak{G}(\Delta)$.
:::

Now, any section $\varrho \in {\bf obj \ }\widetilde\EuFrak{T}_{\otimes,\xi}$ defines a presheaf bundle

${}_\beta \widehat\varrho = ( \widehat\varrho , r^\varrho )_\Delta$,

constructed as follows. Given $a \in \Delta$, the fibre $\widehat\varrho_a$ has objects the tensor powers

$\varrho_a^n = \varrho \otimes \ldots \otimes \varrho$, $n \in {\mathbb N}$,

and arrows

$$\label{eq.beta}
{}_\beta (\varrho_a^n , \varrho_a^m ) 
\ := \
\{ t_a \ : \ t \in (\varrho^n , \varrho^m )_{\geq a}  \} \ ,$$

where, for any $\varrho , \varsigma \in {\bf obj \ }\widetilde\EuFrak{T}_{\otimes,\xi}$, we use the notation

$$(\varrho , \varsigma )_{\geq a} \ := \ 
\{  t = \{ t_o \in (\varrho_o,\varsigma_o) \}_{o \supseteq a} \ : \ 
    r_{oo'}(t_{o'}) = t_o \ , \ \forall o \subseteq o'  \}$$

(see [@Vas12 Prop.3.4] for details). The restriction functors

$r^\varrho_{aa'} : \widehat\varrho_{a'} \to \widehat\varrho_a$, $a \subseteq a'$,

are defined by the identity on the objects and by restricting $r_{aa'}$ to $\widehat\varrho_{a'}$ on the arrows. The following result describes ${}_\beta \widehat\varrho$ in terms of the presheaf bundles of Ex.[\[ex.back1\]](#ex.back1){reference-type="ref" reference="ex.back1"}:

::: thm
[]{#lem_CCS00 label="lem_CCS00"} Let $\EuFrak{T}_{\otimes,\xi} = (T,r)^\Delta$ be a DR-presheaf. Then for any section $\varrho \in {\bf obj \ }\widetilde\EuFrak{T}_{\otimes,\xi}$ there are a compact Lie group

$G_\varrho \subseteq {{\mathbb U}(d)}$

such that, up to isomorphism of the fibre,

$${}_\beta \widehat\varrho \ \in \ {\bf pbun}^\uparrow(\Delta,\widehat\pi_{G_\varrho;\otimes,\theta})$$

and a morphism

$$\chi_\varrho : \pi_1(\Delta) \to QG_\varrho := NG_\varrho / G_\varrho \ ,$$

which is the holonomy of ${}_\beta \widehat\varrho$. If there is an embedding of $\EuFrak{T}_{\otimes,\xi}$ then for any section $\varrho$ there must be a lift

$\widehat\chi_\varrho : \pi_1(\Delta) \to NG_\varrho$, $\chi_\varrho = \widehat\chi_\varrho \mod G_\varrho$.
:::

The existence of embeddings can be described in cohomological terms:

::: thm
[]{#thm.gerbe label="thm.gerbe"} Any section $\varrho$ of a DR-presheaf defines the cochain

$$u_\varrho : \Sigma_1(\Delta) \to NG_\varrho
\ \ : \ \
du_\varrho(c) := 
u_\varrho(\partial_0c) u_\varrho(\partial_2c) u_\varrho(\partial_1c)^* \in G_\varrho
\ , \ 
\forall c \in \Sigma_2(\Delta)
\ .$$

(Eventual) lifts of $\chi_\rho$ are in one-to-one correspondence with pairs $(v,g)$,

$v : \Sigma_0(\Delta) \to NG_\varrho$, $g : \Sigma_1(\Delta) \to  G_\varrho$,

such that

$$\label{eq.gerbe}
z(b) := v(\partial_0b) g(b) u_\varrho(b) v(\partial_1b)^* \ \in NG_\varrho
\ \ , \ \
\forall b \in \Sigma_1(\Delta)
\ ,$$

is a cocycle, i.e. $dz(c) = 1$, $\forall c \in \Sigma_2(\Delta)$.
:::
