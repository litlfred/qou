---
doc_id: arxiv-1211.1812v5
doc_title: "Presheaves of superselection structures in curved spacetimes"
section_id: sec-002-21-geometry-of-posets
section_title: "Geometry of posets."
section_number: 2.1
pages: 5-7
source_pdf: 1211.1812v5.pdf
source_sha256: 211667ea1312d47f
toc_source: outline
text_source: latex
latex_prose_ratio: 0.983
latex_coverage_ratio: 0.989
doc_brief: "Presheaves of superselection structures in curved spacetimes — We show that superselection structures on curved spacetimes, that are expected to describe quantum charges aﬀected by the underlying"
---
[]{#sec.back.posets label="sec.back.posets"}

Let $M$ be a connected manifold. We say that a base $\Delta$ for the topology of $M$ is *good* whenever any $a \in \Delta$ has compact closure and is arcwise and simply connected. For example, we have the Minkowski spacetime, that has a good base given by the set of double cones, or, more generally, a globally hyperbolic spacetime, that has a good base base given by the set of diamonds ([@GLRV01; @BR08]). In the present paper we shall always consider good bases.

Now, $\Delta$ becomes a *poset* (partially ordered set) when endowed with the order relation given by the inclusion, and encodes some geometric invariants of $M$. As a first step we consider the simplicial set defined by $\Delta$, whose sets at lower degrees are defined as follows ([@RR06; @RRV07]):

-   $\Sigma_0(\Delta) := \Delta$, the set of $0$-simplices, that are the analogues of \"points\";

-   $\Sigma_1(\Delta)$, the set of $1$-simplices, is the set of \"oriented lines\" of the type

    $$b := ( \partial_1b , \partial_0b ; |b| ) 
    \ \ : \ \ 
    \partial_1b , \partial_0b , |b| \in \Delta \ \ {\mathrm{and}} \ \ 
    \partial_1b , \partial_0b \subseteq |b| \ .$$

-   Finally we define the set $\Sigma_2(\Delta)$ of $2$-simplices (\"oriented triangles\") with elements quadruples

    $c = ( \partial_0c , \partial_1c , \partial_2c \in \Sigma_1(\Delta) ; |c| \in \Delta)$

    such that

    $$\label{eq.dd}
    \partial_{hk}c := \partial_h \partial_k c = \partial_k \partial_{h+1}c
    \ \ , \ \
    |\partial_hc| \subseteq |c|
    \ \ , \ \
    \forall h \geq k
    \ .$$

Using $1$-simplices we define *paths*, in terms of sequences

$$p := b_n * \ldots * b_1
\ \ : \ \ 
\partial_0b_k = \partial_1b_{k+1}
\ , \
\forall k = 1  , \ldots , n \ .$$

To emphasize the initial and ending \"points\" of $p$ we use the notation

$$p : a \to o \ \ , \ \ a = \partial_1b_1 \ , \ o = \partial_0b_n \ .$$

The *opposite path* of $p$ is given by

$\overline p := \overline b_1 * \ldots * \overline b_n : o \to a$,

where any $\overline b_k$, $k = 1 , \ldots , n$, is the 1-simplex defined by

$$\partial_1 \overline b_k := \partial_0 b_k \ \ , \ \
\partial_0 \overline b_k := \partial_1 b_k \ \ , \ \
| \overline b_k | := | b_k | \ .$$

A *path frame* with pole $\omega \in \Delta$ is a set

$$\label{def.pf}
P_\omega = \{ p_{a \omega} : \omega \to a \ , \ \forall a \in \Delta \}$$

such that $p_{\omega \omega} = b_\omega := (\omega,\omega;\omega) \in \Sigma_1(\Delta)$. To be concise we write

$$p_{\omega a} := \overline p_{a \omega} \ .$$

Paths of the type $p : a \to o$, $p' : o \to e$ can be composed by defining

$p'*p := b'_m * \ldots * b'_1 * b_n * \ldots b_1$,

so in particular the set of paths of the type $p : a \to a$, called *loops*, is a semigroup. There is an equivalence relation on paths, called *homotopy*, and the quotient

$\pi_1(\Delta)$

of the set of loops starting and ending at $a \in \Delta$ is a group, whose isomorphism class does not depend on $a$. There is an isomorphism

$$\label{eq.back1}
\pi_1(\Delta) \ \simeq \ \pi_1(M) \ ,$$

where $\pi_1(M)$ is the fundamental group; this implies $\pi_1(M) = 0$ when $\Delta$ is directed (see [@Ruz05]).

 

Finally, in the spirit of [@Qui], we mention that the above constructions apply to a category $C$ in place of a poset

[^1],

as for example the category of globally hyperbolic spacetimes at the root of locally covariant quantum field theory [@BFV03].

One defines $\Sigma_0(C) = {\bf obj \ }C$, $\Sigma_1(C)$ as the set of pairs $b=(b_1,b_0)$ of arrows having the same target $|b| \in {\bf obj \ }C$ and so on, obtaining the notion of fundamental group of $C$.

#### Characteristic classes for representations of $\pi_1(\Delta)$.

Let $G$ be a topological group and

$$\chi : \pi_1(\Delta) \to G$$

a morphism. Using ([\[eq.back1\]](#eq.back1){reference-type="ref" reference="eq.back1"}) we identify $\pi_1(\Delta)$ with the fundamental group and recall that the universal cover $\tilde M$ defines a principal $\pi_1(\Delta)$-bundle

$q : \tilde M \to M$,

so any fibre $q^{-1}(x)$, $x \in M$, is a right $\pi_1(\Delta)$-space. Given a left $G$-space $F$ with action $g,v \mapsto gv$, $g \in G$, $v \in F$, this yields the induced $F$-bundle

$$\label{eq.back2}
q_\chi : P_\chi \to M \ ,$$

where $P_\chi$ is the quotient of $\tilde M \times F$ by the equivalence relation

$$(y,v) \sim (yp,\chi(p)v) \ \ , \ \ p \in \pi_1(\Delta) 
\ ,$$

and $q_\chi (y,v)_\sim := q(y)$, for any $(y,v)_\sim \in P_\chi$. A $F$-bundle of the above kind is called *locally constant bundle*, see [@Kob §I.2].

 

Let now $F$ be a manifold and $G$ a Lie group. We consider a $F$-bundle $P \to M$, not necessarily locally constant, and a characteristic class $\zeta$ defining the $2k$-form

$\zeta(P) \in Z^{2k}_{deRham}(M)$, $k \in {\mathbb N}$.

We say that $\zeta$ has periods in the ring ${\mathbb K}\subset {\mathbb R}$ whenever

$$\int_c \zeta(P) \ \in {\mathbb K}$$

for any $2k$-cycle $c \in Z_{2k}(M)$. In [@CS85] it is proved that there is a unique morphism

$$\zeta^\uparrow(P) : C_{2k-1}(M) \to {\mathbb R}/ {\mathbb K}\ ,$$

where $C_{2k-1}(M)$ is the group of singular $(2k-1)$-chains, such that

$$\{ \zeta^\uparrow(P) \} (\partial \ell) \ = \ \int_\ell \zeta(P) \, {\mathrm{mod}} {\mathbb K}
\ \ , \ \
\forall \ell \in C_{2k}(M)
\ ,$$

where $\partial : C_{2k}(M) \to Z_{2k-1}(M)$ is the boundary map.

Since it is well-known that $\zeta(P_\chi) = 0$ for any locally constant bundle

$P_\chi$

(see [@Kob §II.3]), we have that $\zeta^\uparrow(P_\chi)$ vanishes on $\partial C_{2k}(M)$, so it yields a cocycle defining a class in singular cohomology,

$$\label{eq.ccs0}
\zeta^\uparrow(\chi) := [\zeta^\uparrow(P_\chi)] \in H^{2k-1}(M,{\mathbb R}/ {\mathbb K}) \ ,$$

which by construction vanishes when $\chi$ is the trivial morphism.

For example, it is well-known that the Chern classes

$c_k(P) \in Z^{2k}_{deRham}(M)$, $k \in {\mathbb N}$,

have periods in ${\mathbb Z}$, so for any representation

$\chi : \pi_1(\Delta) \to {{\mathbb U}(d)}$

there are classes

$$\label{eq.ccs}
c_k^\uparrow(\chi) \in H^{2k-1}(M,{\mathbb R}/ {\mathbb Z})
\ \ , \ \
k = 1 , \ldots , d \ .$$

[^1]: This approach has been object of (unpublished) work by J. Roberts, G. Ruzzi and the author.
