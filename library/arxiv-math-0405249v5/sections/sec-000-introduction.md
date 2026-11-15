---
doc_id: arxiv-math-0405249v5
doc_title: "Twisted homology of quantum SL (2)"
section_id: sec-000-introduction
section_title: "Introduction"
section_number: null
pages: 1-4
source_pdf: 0405249v5.pdf
source_sha256: bc699482e5cd7679
toc_source: outline
text_source: latex
latex_prose_ratio: 0.984
latex_coverage_ratio: 0.975
doc_brief: "Twisted homology of quantum SL (2) — We calculate the twisted Hochschild and cyclic homology (in the sense of Kustermans, Murphy and Tuset) of the coordinate algebra of the quan- tum SL(2) group"
---
Cyclic homology and cohomology were independently discovered by Alain Connes [@connes0] and Boris Tsygan [@tsygan] in the early 1980's, and should be thought of as extensions of de Rham (co)homology to various categories of noncommutative algebras. Quantum groups also appeared in the same period, with the first example of a "compact quantum group" in the C\*-algebraic setting being Woronowicz's "quantum $SU(2)$" [@wo_suq2].

The noncommutative differential geometry (in the sense of Connes) of quantum $SU(2)$ was thoroughly investigated by Masuda, Nakagami and Watanabe [@mnw]. They calculated the Hochschild and cyclic homology of the coordinate algebra $\mathcal{A}(SL_q(2))$ of quantum $SL(2)$ as well as the K-theory and K-homology of the C\*-algebra of the compact quantum $SU(2)$ group. This work was extended by Feng and Tsygan [@FT], who computed the Hochschild and cyclic homology of the standard quantized coordinate algebra $\mathcal{A}(G_q)$ associated to an arbitrary complex semisimple Lie group $G$. The homologies are roughly speaking those of a classical space labelling the symplectic leaves of the Poisson-Lie group $G$ (the semi-classical limit of $\mathcal{A}(G_q)$). In particular, the Hochschild dimension of $\mathcal{A}(G_q)$ equals the rank of $G$. This "dimension drop\" had already been observed for other quantizations of Poisson algebras. Many authors regarded it as an unpleasant feature and asked for generalizations of cyclic homology which detect the quantized parts of quantum groups as well.

One candidate is twisted Hochschild and cyclic (co)homology defined by Kustermans, Murphy and Tuset [@kmt], relative to a pair of an algebra $\mathcal{A}$ and automorphism $\sigma$. This reduces to ordinary Hochschild and cyclic (co)homology of $\mathcal{A}$ on taking $\sigma$ to be the identity. The standard theory is intimately related with the idea of considering tracial functionals on noncommutative algebras as analogues of integrals, whereas the twisted theory arises naturally from functionals whose tracial properties are of the form $h(ab)=h(\sigma(b)a)$. Noncommutative spaces equipped with such functionals include duals of nonunimodular groups, type III von Neumann algebras and compact quantum groups. The aim of [@kmt] was to adapt Connes' constructions relating cyclic cohomology and differential calculi to covariant differential calculi in the sense of Woronowicz, since the volume forms of such calculi define in general twisted cocycles rather than usual ones [@sw1]. The possibility of pairing twisted cyclic cocycles (e.g. over quantum homogeneous spaces) with equivariant K-theory was demonstrated in [@NT04], and it seems an interesting problem to investigate how far this original motivation of cyclic cohomology extends to the twisted setting.

In this paper we compute the twisted Hochschild and cyclic homologies $HH_\ast^\sigma(\mathcal{A})$, $HC_\ast^\sigma(\mathcal{A})$ for the coordinate algebra $\mathcal{A}=\mathcal{A}(SL_q(2))$ of the quantum $SL(2)$ group, with generic deformation parameter $q$. We consider all automorphisms $\sigma$ of the form $a,b,c,d \mapsto \lambda a, \mu b, \mu^{-1} c, \lambda^{-1} d$, where $a, b, c, d$ are the standard generators, and $\lambda$, $\mu$ are nonzero elements of $k$. As an overview we collect the dimensions of $HH_n^\sigma(\mathcal{A})$ as a $k$-vector space, see the main text for explicit formulas for generators:

::: thm
[]{#erga label="erga"} We have $$\begin{aligned}
&& \mathrm{dim}\,HH_n^\sigma(\mathcal{A})=0,\quad n > 3,\nonumber\\   
&& \mathrm{dim}\,HH_3^\sigma(\mathcal{A})=\left\{
    \begin{array}{ll}
    N+1 \quad &\lambda=q^{-(N+2)},\mu=1,\\
    0 \quad &\mathrm{otherwise},
    \end{array}\right.\nonumber\\
&& \mathrm{dim}\,HH_2^\sigma(\mathcal{A})=\left\{
    \begin{array}{ll}
    N+1 \quad &
    \lambda=q^{-(N+2)},\mu=1,\\
    2 \quad & \lambda=q^{-(N+1)},\mu=q^{\pm(M+1)},\\
    0 \quad & \mathrm{otherwise},
    \end{array}\right.\nonumber\\
&& \mathrm{dim}\,HH_1^\sigma(\mathcal{A})=\left\{
    \begin{array}{ll}
    0 \quad & 
    \lambda \notin q^{-\mathbb{N}},
    \mu=q^{\pm(M+1)},\\
    0 \quad & 
    \lambda \neq 1,\mu \notin q^\mathbb{Z},\\
    4 \quad &
    \lambda=q^{-(N+1)},\mu=q^{\pm(M+1)},\\
    \infty \quad & \mathrm{otherwise},
    \end{array}\right.\nonumber\\
&& \mathrm{dim}\,HH_0^\sigma(\mathcal{A})=\left\{
    \begin{array}{ll}
    \infty \quad & \mu=1,\\
    2 \quad & \lambda=q^{-(N+1)},\mu=q^{\pm(M+1)},\\
    0 \quad & \mathrm{otherwise},
    \end{array}\right.\nonumber 
\end{aligned}$$ for $M, N \in \mathbb{N}$.
:::

Strikingly (Theorem [\[HH_3_for_any_sigma\]](#HH_3_for_any_sigma){reference-type="ref" reference="HH_3_for_any_sigma"}), there exists a family of automorphisms for which the twisted Hochschild dimension takes the classical value three (note also that the homological dimension of $\mathcal{A}(SL_q(2))$ is three [@ls]) - the twisted theory avoids the "dimension drop\". Remarkably, the simplest such automorphism ($\lambda= q^{-2},\mu=1$) is the canonical modular automorphism associated to the Haar functional on $\mathcal{A}$. Similar results were obtained for $\mathrm{Podle{\acute{s}}}$ quantum spheres [@tom] and quantum hyperplanes [@si].

In [@FT], Feng and Tsygan considered formal quantizations, with $\mathcal{A}(G_q)$ a Hopf algebra over $\mathbb{C}[[\hbar]]$ with $q=e^\hbar$. They showed that for a Hopf algebra $\mathcal{A}$ over a field $k$, with coproduct $\Delta$, counit $\varepsilon$ and antipode $S$, and an $\mathcal{A}$-bimodule $\mathcal{M}$, there is an isomorphism $$H_n(\mathcal{A},\mathcal{M}) \simeq 
\mathrm{Tor}_n^\mathcal{A}(\mathcal{M}',k)$$ Here, $\mathcal{M}'$ is $\mathcal{M}$ as a linear space with right action given by $$m \blacktriangleleft a:= \sum \; S(a_{(2)})ma_{(1)}$$ using Sweedler's notation for the coproduct, and $k=\mathcal{A}/ \mathrm{ker}\,\varepsilon$ is the trivial left $\mathcal{A}$-module. Then they computed these $\mathrm{Tor}$-groups using the spectral sequence associated to the filtration induced by $\hbar$.

In this paper we compute $\mathrm{Tor}_n^\mathcal{A}(\mathcal{M}',k)$ from a Koszul-type free resolution $$0 \rightarrow \mathcal{A}\rightarrow \mathcal{A}^3 \rightarrow \mathcal{A}^3 
    \rightarrow \mathcal{A}\rightarrow k \rightarrow 0$$ of $k$. Noncommutative Koszul resolutions were studied by several authors, in particular Wambst [@wambst], but as far as we know were not applied to quantum groups. In our opinion this resolution shows very clearly the geometric mechanisms behind the computations. We will see that the maps of the resulting complex computing the twisted Hochschild homology become zero for $q=1$, so one obtains the Hochschild-Kostant-Rosenberg theorem for $SL(2)$ (the algebraic cotangent bundle of $SL(2)$ is trivial). However, for $q \neq 1$ this does not happen for any twisting automorphism.

A summary of this paper is as follows. In section [\[section_thch\]](#section_thch){reference-type="ref" reference="section_thch"} we recall how the twisted theory was discovered [@kmt], then give the definitions of $HH_\ast^\sigma(\mathcal{A})$ and $HC_\ast^\sigma(\mathcal{A})$, and the underlying cyclic object. We specialize to Hopf algebras and explain the methods adapted from [@FT]. We then present the general scheme of the noncommutative Koszul complexes used here. In section [\[section_slq2_suq2\]](#section_slq2_suq2){reference-type="ref" reference="section_slq2_suq2"} we introduce the quantum $SL(2)$ group. In section [\[section_th_slq2\]](#section_th_slq2){reference-type="ref" reference="section_th_slq2"} we present our calculations of $HH_\ast^\sigma(\mathcal{A})$ for $\mathcal{A}=\mathcal{A}(SL_q (2))$.

Twisted cyclic homology is defined as the total homology of Connes' mixed $(b,B)$-bicomplex coming from the underlying cyclic object, as in [@loday]. In section [\[section_tc_slq2\]](#section_tc_slq2){reference-type="ref" reference="section_tc_slq2"} we compute this homology via a spectral sequence.

Finally, in section [\[section_diff_calc_suq2\]](#section_diff_calc_suq2){reference-type="ref" reference="section_diff_calc_suq2"} we discuss the relation of our results to previously known twisted cyclic cocycles coming from the three covariant differential calculi over $\mathcal{A}(SL_q(2))$ discovered by Woronowicz. The twisted cyclic 3-cocycle arising from the three dimensional left covariant calculus was given explicitly in [@kmt] and [@sw1]. We show (Theorem [\[3dcalc_cocycle_is_trivial\]](#3dcalc_cocycle_is_trivial){reference-type="ref" reference="3dcalc_cocycle_is_trivial"}) that this 3-cocycle is a trivial element of twisted cyclic cohomology. Further, the twisted 4-cocycles arising from the two bicovariant four dimensional calculi both correspond to the twisted 0-cocycle coming from the Haar functional (as elements of even periodic twisted cyclic cohomology).
