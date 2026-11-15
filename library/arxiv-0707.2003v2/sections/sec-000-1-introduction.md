---
doc_id: arxiv-0707.2003v2
doc_title: "A geometric model for Hochschild homology of Soergel bimodules"
section_id: sec-000-1-introduction
section_title: "Introduction"
section_number: 1
pages: 1-5
source_pdf: 0707.2003v2.pdf
source_sha256: 0b8fe37aabeee412
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.997
latex_coverage_ratio: 0.887
doc_brief: "A geometric model for Hochschild homology of Soergel bimodules — An important step in the calculation of the triply graded link homology theory of Khovanov and Rozansky is the determination of the"
---
[]{#sec:introduction label="sec:introduction"}

In this paper, we consider the Hochschild homology of Soergel bimodules, and construct a geometric interpretation of it. This will allow us to explicitly compute the Hochschild homology of a special class of Soergel bimodules.

Soergel bimodules are bimodules over a polynomial ring, which appear naturally both in the study of perverse sheaves on flag varieties and of the semiring of projective functors on the BGG category $\O$. Recently interest in them has been rekindled by the appearance of connections with link homology as shown by Khovanov [@Kho05].

Khovanov's work showed that one aspect of Soergel bimodules which had not been carefully studied up to that date was, in fact, of great importance: their Hochschild homology. While the operation of taking Hochschild homology is hard to motivate from a representation theoretic perspective, we argue that it is, in fact, naturally geometric, rather than purely combinatorial/algebraic.

Let $G$ be a connected reductive complex algebraic group, with Lie algebra $\g$.

Let $B$ be a Borel of $G$, $T$ a Cartan subgroup of $G$, $\mathfrak t$ be its Lie algebra, $n=\dim T$ be the rank of $G$,

and $W=N_G(T)/T$ be the Weyl group of $G$. For any $w\in W$, we let $\Gw=\overline{BwB}$. Note that $T$ is a deformation retract of $B$, so, we have $H^*_B(X)\cong H^*_T(X)$ for all $B$-spaces $X$. We will freely switch between $B$- and $T$-equivariant cohomology throughout this paper.

We note that $\Gw$ is a closed subvariety of $G$ which is smooth if and only if the corresponding Schubert variety $\B_w\subset G/B=\B$ is (and thus $\Gw$ typically singular). Note that $B\times B$ acts on $\Gw$ by left and right multiplication, and that restricting to the diagonal, we get the action of $B$ by conjugation. Of course, we also have left and right actions of $B$ but we will never consider these separately. We will **always** mean the conjugation action.

Now consider the graded ring $\HT=H_T^*(pt,\C)=\C[\td]$, which is endowed with the obvious $W$-action.

Given a simple reflection $s$, denote by $\S{s}$ the bimodule $\HT \otimes_{\HT^{s}} \HT[1]$ where $S^s$ is the subring of invariants under the reflection $s$ and, by convention, $[a]$ denotes the grading shift $(M[a])^i=M^{i+a}$.

We now come to the definition of Soergel bimodules:

::: defi
A **Soergel bimodule** is (up to grading shift) a direct summand of the tensor product $\S{\Bi} = \S s \otimes_S \S t \otimes_S \dots
  \otimes_S \S u$ in the category of graded $S$-bimodules, where $\Bi
  = (s, t, \dots, u)$ is a sequence of (not necessarily distinct) simple reflections.
:::

The motivation for studying Soergel bimodules comes from representation theory, geometry and connections between the two. In fact, one has the following theorem:

::: thm
(Soergel) The indecomposable Soergel bimodules are parameterized (up to a shift in the grading) by the Weyl group [@Soe05 Satz 6.14].

The irreducible Soergel bimodule corresponding to $w \in W$ may be obtained as

$\S w\cong I\!H^*_{\BB}(\Gw)$ [@Soe01 Lemma 5], where $I\!H^*$ denotes intersection cohomology as defined by Goresky and MacPherson [@GM1].
:::

We choose our grading conventions on $I\!H^*$ so that the 0th degree is the mirror of Poincaré duality, that is, so that the lowest degree component of $\S w$ sits in degree $-\ell(w)$.

More generally, Soergel bimodules can be identified with the $\BB$-equivariant hypercohomology $\hcBB(G,\mc F)$ of sums $\mc F$ of shifts of $\BB$-equivariant semi-simple perverse sheaves on $G$.

Our central result is a geometric description of Hochschild homology $\HH_*(-)$ of these modules.

::: thm
[]{#sec:introduction-1 label="sec:introduction-1"} Let $\mc F$ be a semi-simple $\BB$-equivariant perverse sheaf on $G$ and let $R$ be its $\BB$-equivariant cohomology. Then $$\HH_*(\S{})\cong \hc_{B}(G,\mc F),$$ where $B$ acts by conjugation (i.e., by the diagonal inclusion $B\hookrightarrow\BB$). In particular, we have $$\HH_*(\S w)\cong\IH_{B}^*(\Gw).$$
:::

Unfortunately, $\IH_{B}^*(\Gw)$ has a single grading, whereas $\HH_*(\S w)$ has two: by decomposition into the components $\HH_i$ ("the Hochschild grading"), and one coming from the grading on $\S
w$ ("the polynomial grading"). This isomorphism takes the single grading on $\IH_B^*(\Gw)$ to the difference of the two gradings on $\HH_*(\S w)$.

We can give a geometric interpretation of these gradings, but in a somewhat roundabout manner. A result of Rasmussen [@Ras06] shows that

::: thm
[]{#intro-e-f label="intro-e-f"} Assume $G=\SL n$ or $\GL n$. Then $\IC({G_w})$ is equivariantly formal. Thus, the map $$i^*_T: \IH^*_T(G_w)\to \hc_T(T,\IC({G_w}))\cong H^*_T(T)\otimes \IC({G_w})_e$$ is injective and an isomorphism after tensoring with the fraction field of $S$.
:::

Furthermore, since $H^*_T(T,\IC({G_w}))\cong S\otimes_\C
H^*(T,\IC({G_w}))$ by the Künneth theorem, we can equip this $S$ module with a bigrading, with an "equivariant" grading from the first factor, and a "topological" grading from the second.

::: thm
[]{#grading-match label="grading-match"} The intersection cohomology $\IH^*_B(G_w)$ obtains "topological" and "equivariant" gradings by transport of structure from the map $i^*$ and $\HH_*(\S w)$ obtains the same by the isomorphism of Theorem [\[sec:introduction-1\]](#sec:introduction-1){reference-type="ref" reference="sec:introduction-1"}. These are related to the "Hochschild" and "polynomial" gradings by $$\deg_t(\ga)=\deg_h(\ga) \hspace{15mm} \deg_e(\ga)=\deg_p(\ga)-2\deg_h(\ga)$$ where $\deg_*(x)$ denotes the degree of $x$ in the grading whose name begins with the letter $*$.
:::

The case where $\Gw$ is smooth is of special interest to us, so any reader who is unhappy with the presence of intersection cohomology and perverse sheaves can restrict to that case, in which case intersection cohomology is canonically isomorphic to Čech cohomology.

::: thm
[]{#ind-HH label="ind-HH"} If $\Gw$ is smooth (in any type), then the Hochschild homology of $\S w$ is of the form $$\HH_*(\S w)=\land^\bullet(\ga_1,\ldots, \ga_n)\otimes_{\C}\HT$$ where $\{\ga_i\}_{i=1,\ldots,m}$ are generators with $$\deg_h(\ga_i)=1\hspace{15mm}\deg_p(\ga_i)=2k_i$$ for positive integers $k_i$ determined by the geometry of $\Gw$.
:::

These integers can be calculated using the action of $w$ on the root system, or in $\SL n$ by presenting $\Gw/B$ as an iterated Grassmannian bundle.

While the indecomposable modules $\S w$ are perhaps most natural from the perspective of geometry or representation theory, definition (1) (and the study of knot homology, which we discuss briefly in Section [\[sec:knot-homol-soerg\]](#sec:knot-homol-soerg){reference-type="ref" reference="sec:knot-homol-soerg"}) encourages us to concentrate on the modules $\S{\Bi}$. We call these particular Soergel bimodules **Bott-Samelson** for reasons which will be clarified in Section [\[sec:geom-soerg-bimod\]](#sec:geom-soerg-bimod){reference-type="ref" reference="sec:geom-soerg-bimod"}.

Bott-Samelson modules are naturally identified with the equivariant homology of the "groupy" Bott-Samelson space $$\BSi\cong P_{s}\times_{B} P_{t} \times_{B} \cdots\times_{B}P_{u}.$$ and essentially the analogues of all appropriate theorems connecting the $\BB$-orbit closures in $G$ with Soergel bimodules are true here.

::: thm
[]{#BS-match label="BS-match"} If $G=\SL n$ or $\GL n$, then for all $\Bi$, we have $$\S{\Bi}\cong H^*_{\BB}(\BSi)\hspace{15mm}\HH_*(\S{\Bi})\cong H^*_{B}(\BSi).$$ The $T$-conjugation on $\BSi$ is equivariantly formal, and the injection $$i^*_T:H^*_T(\BSi)\to H_T^*(\BSi^T)$$ induces a bigrading on $H^*_T(\BSi)$ matching that on $\HH_*(\S{\Bi})$ as in Theorem [\[grading-match\]](#grading-match){reference-type="ref" reference="grading-match"}.
:::

The structure of the paper is as follows: In Section [\[sec:knot-homol-soerg\]](#sec:knot-homol-soerg){reference-type="ref" reference="sec:knot-homol-soerg"}, we discuss the importance of the Hochschild homology of Soergel bimodules in knot theory. In Section [\[sec:hochsch-homol-dg\]](#sec:hochsch-homol-dg){reference-type="ref" reference="sec:hochsch-homol-dg"}, we prove Theorem [\[sec:introduction-1\]](#sec:introduction-1){reference-type="ref" reference="sec:introduction-1"}, using the formalism of dg-modules, the relevant points of which we will summarize in Section [\[sec:equi-derived-cat\]](#sec:equi-derived-cat){reference-type="ref" reference="sec:equi-derived-cat"}. In Section [\[sec:geom-soerg-bimod\]](#sec:geom-soerg-bimod){reference-type="ref" reference="sec:geom-soerg-bimod"}, we will cover in more detail how to construct Soergel bimodules as equivariant intersection cohomology of various varieties. Finally, in Section [\[sec:equiv-form\]](#sec:equiv-form){reference-type="ref" reference="sec:equiv-form"}, we prove Theorems [\[intro-e-f\]](#intro-e-f){reference-type="ref" reference="intro-e-f"} -- [\[BS-match\]](#BS-match){reference-type="ref" reference="BS-match"}.
