---
doc_id: arxiv-1203.6551v1
doc_title: "On the number of hyperbolic 3-manifolds of a given volume"
section_id: sec-000-1-introduction
section_title: "Introduction"
section_number: 1
pages: 1-5
source_pdf: 1203.6551v1.pdf
source_sha256: a8e84f8ed63dbcca
toc_source: outline
text_source: latex
latex_prose_ratio: 0.967
latex_coverage_ratio: 0.992
doc_brief: "On the number of hyperbolic 3-manifolds of a given volume — The work of Jørgensen and Thurston shows that there is a ﬁnite number N(v) of orientable hyperbolic 3-manifolds with any given volume v."
---
Thurston and Jørgensen (see [@Th]) showed that the set of volumes of finite volume orientable complete hyperbolic $3$-manifolds is a closed, non-discrete, well ordered subset of $\mathbb{R}_{>0}$ of order type $\omega^\omega$. Further, the number $N(v)$ of complete orientable hyperbolic $3$-manifolds of volume $v$ is finite for all $v\in \mathbb{R}_{>0}$. In this paper we study how $N(v)$ varies with $v$.

There has been much work on determining the lowest volumes in various classes of hyperbolic 3-manifolds. The work of Gabai-Meyerhoff-Milley ([@GMM1; @GMM2; @M]) shows that the Weeks manifold with volume $v_1 = 0.9427 \ldots$ is the unique orientable hyperbolic 3-manifold of lowest volume, so that $N(v_1)=1$. Prior to our work, this was the only known exact value for $N(v)$.

It is also interesting to look at the number of hyperbolic 3-manifolds of a given volume in various special classes. For example, we could study the numbers $N_C (v)$, $N_A(v)$, $N_L(v)$, $N_G(v)$ of orientable hyperbolic 3-manifolds of volume $v$ that are cusped, arithmetic, link complements, or with geodesic boundary, respectively.

The work of Cao-Meyerhoff [@CM] shows there are precisely two orientable cusped hyperbolic 3-manifolds of lowest volume $v_\omega \approx 2.029883\ldots$, the figure eight knot complement and its sister (obtained by (-5,1) surgery on the Whitehead link complement). (See Figure [1](#fig8_fig8sister){reference-type="ref" reference="fig8_fig8sister"}.)

<figure id="fig8_fig8sister">
<p><embed src="fig8.eps" /> <embed src="fig8sister_new.eps" /></p>
<figcaption>The figure eight knot and its sister, with complements denoted <span class="math inline"><em>m</em>004</span> and <span class="math inline"><em>m</em>003</span> respectively in SnapPea notation.</figcaption>
</figure>

Gabai-Meyerhoff-Milley [@GMM1] determined the first 10 low volume orientable cusped hyperbolic 3-manifolds. This shows that the next 4 limit volumes are: $$v_{2\omega} = 2.568970\ldots, v_{3\omega}=2.666744\ldots ,
v_{4\omega}= 2.781833\ldots, v_{5\omega} = 2.828122\ldots$$ and that $N_C(v_\omega) = 2 ,  N_C(v_{2\omega})=2,  N_C(v_{3\omega})=2, 
N_C(v_{4\omega})=1, N_C(v_{5\omega})=3.$

The work of Agol [@agol_2cusp] shows that there are exactly two orientable 2-cusped hyperbolic 3-manifolds of lowest volume $v_{\omega^2} = 3.663862\ldots$, namely the Whitehead link complement and the $(-2,3,8)$-pretzel link complement. (See Figure [2](#fig.WL_WS){reference-type="ref" reference="fig.WL_WS"}.)

<figure id="fig.WL_WS">
<p><embed src="Whitehead.eps" /> <embed src="p-238.eps" /></p>
<figcaption>The Whitehead link and the <span class="math inline">(−2,3,8)</span>-pretzel link, with complements <span class="math inline"><em>m</em>129</span> and <span class="math inline"><em>m</em>125</span> in SnapPea notation.</figcaption>
</figure>

Chinburg-Friedman-Jones-Reid [@CFJR] showed that the Weeks manifold and the Meyerhoff manifold are the unique arithmetic hyperbolic 3-manifolds of lowest volume; hence $N_A(0.942707\ldots) = 1$ and $N_A(0.981368\ldots) = 1$.

Kojima and Miyamoto [@KojMiy; @miyamoto] showed the lowest volume for a compact hyperbolic 3-manifold with geodesic boundary is $6.451990\ldots$, and Fujii [@Fu] showed that there are exactly 8 such manifolds with this volume.

The graphs in Figures [3](#closed_cusped_vols){reference-type="ref" reference="closed_cusped_vols"} and [4](#cusped_vols){reference-type="ref" reference="cusped_vols"} below show the frequencies of volumes arising from the manifolds contained in the Callahan-Hildebrand-Weeks census of cusped hyperbolic 3-manifolds (see [@CaHiWe]), and the Hodgson-Weeks census of closed hyperbolic 3-manifolds (see [@HW]). These give *lower bounds* on $N(v)$, but note that infinitely many manifolds are definitely missing in these pictures. Nevertheless, the results suggest that there are often very few manifolds with any given volume.

![Frequencies of volumes of hyperbolic 3-manifolds in the closed and cusped censuses.](vol_cusped_closed_list.eps){#closed_cusped_vols}

![Frequencies of volumes of hyperbolic 3-manifolds in the cusped census.](vol_cusped_list.eps){#cusped_vols}

The first main result of this paper (Theorem [\[closed_unique\]](#closed_unique){reference-type="ref" reference="closed_unique"}) shows that there is an infinite sequence of closed hyperbolic 3-manifolds determined by their volumes, obtained by Dehn fillings on the figure eight knot complement. Hence $N(x_i)=1$ for an infinite sequence of volumes $x_i$ converging to $v_\omega$ from below.

The proof of Theorem [\[closed_unique\]](#closed_unique){reference-type="ref" reference="closed_unique"} uses the asymptotic formula of Neumann-Zagier [@NZ] for the change in volume during hyperbolic Dehn filling and a study of the quadratic form giving the squares of lengths of closed geodesics on a horospherical torus cusp cross section, together with some elementary number theory.

Our second major result (Theorem [\[cusped_unique\]](#cusped_unique){reference-type="ref" reference="cusped_unique"}) shows that there is an infinite sequence of 1-cusped hyperbolic 3-manifolds determined by their volumes amongst orientable cusped hyperbolic 3-manifolds. These manifolds are obtained by Dehn fillings on one cusp of the $(-2,3,8)$-pretzel link complement. Hence $N_C(y_i)=1$ for an infinite sequence of volumes $y_i$ converging to $v_{\omega^2}$ from below.

The proof of Theorem [\[cusped_unique\]](#cusped_unique){reference-type="ref" reference="cusped_unique"} is similar to the proof of Theorem [\[closed_unique\]](#closed_unique){reference-type="ref" reference="closed_unique"}, but there are some additional complications that require us to study higher order terms in the Neumann-Zagier asymptotic formula.

Another obvious feature of the graphs in Figures [3](#closed_cusped_vols){reference-type="ref" reference="closed_cusped_vols"} and [4](#cusped_vols){reference-type="ref" reference="cusped_vols"} is that there are special values of $v$ for which $N(v)$ is particularly large. So it is natural to ask how fast $N(v)$ can grow with $v$.

If we fix a natural number $n$, then Wielenberg [@Wie] showed that there exists $v$ such that $N(v)>n$, and Zimmerman [@Zim] constructed $n$ distinct closed hyperbolic $3$-manifolds which share the same volume. In both results, the number of manifolds of volume $v$ constructed was at most linear in $v$.

More generally, by considering covering spaces of a fixed non-arithmetic hyperbolic 3-manifold whose fundamental group surjects onto a free group of rank 2, it is possible to find sequences of volumes $x_i \to \infty$ and a constant $c >0$ such that $N(x_i) > x_i^{c \,x_i}$ for all $i$. This argument, known to Thurston and Lubotzky, can be found in [@carlip pp2633-2634] or [@BGLM p1162].

Recent work of Belolipetsky-Gelander-Lubotzky-Shalev [@BGLS] gives very precise upper and lower bounds on the number $N_A(v)$ of *arithmetic* hyperbolic 3-manifolds of volume $v$: there exist constants $a,b>0$ such that for $x >>0$, $$x^{ax} \le \sum_{x_i \le x} N_{A}(x_i) \le  x^{bx}.$$ In particular, this implies that for all sufficiently large $x$, $$x^{ax} \le ~\max_{x_i \le x} N_{A}(x_i)~ \le  x^{bx}.$$

In [@FMP2] (and [@FMP1]), Frigerio, Martelli and Petronio constructed explicit families of hyperbolic $3$-manifolds with totally geodesic boundary giving sequences $x_i \to \infty$ such that the number $N_{G} (x_i)$ of hyperbolic 3-manifolds of volume $x_i$ with geodesic boundary grows at least as fast as $x_i^{c x_i}$ for some $c>0$.

In the last part of this paper, we investigate the number $N_L(v)$ of hyperbolic link complements in $S^3$ with volume $v$. In Theorem [\[thm.expo\]](#thm.expo){reference-type="ref" reference="thm.expo"} we construct sequences of volumes $v_n \to \infty$ such that the number $N_L(v_n)$ of hyperbolic link complements with volume $v_n$ grows at least exponentially fast with $v_n$.

Our main tool is mutation along totally geodesic thrice punctured spheres in fully augmented link complements. It is well known that mutation along certain special surfaces leaves the hyperbolic volume and many other invariants unchanged (see for example [@Ada], [@Rub], [@DGST]). We distinguish the manifolds produced using information about their cusp shapes and maximal horoball cusp neighbourhoods.

Recent independent work of Chesebro-DeBlois [@CD] uses mutations along 4-punctured spheres to show that $N_L(v)$ grows at least exponentially fast with $v$, and that the number of commensurability classes of link complements with a given volume can be arbitrarily large.

Mutation along thrice punctured spheres can be studied by using spatial trivalent graphs. We will say that a spatial trivalent graph is *hyperbolic* if its complement admits a hyperbolic metric with parabolic meridians and geodesic boundaries (see section [\[sec.Vol\]](#sec.Vol){reference-type="ref" reference="sec.Vol"}, [@HHMP] and [@Mas]). In [@Mas], the second author exhibited volume preserving moves on hyperbolic graphs and hyperbolic links, which correspond to cutting and gluing along thrice punctured spheres. By applying these moves, each hyperbolic graph with a planar diagram corresponds to a *fully augmented link*. Such links have been well studied, and we can easily compute the moduli of their cusps (see [@FP] and [@Pur]).

Here is a brief outline of the remainder of the paper. In section 2, we recall the results of Neumann and Zagier relating the decrease in volume during hyperbolic Dehn filling to the length of the surgery curve. We then explain the key ideas that will allow us to obtain manifolds uniquely determined by their volumes. In section 3 (resp. 4), we apply these ideas to the manifolds denoted $m003$ and $m004$ (resp. $m125$ and $m129$) in SnapPea notation, and produce infinitely many manifolds that are determined by their volumes amongst all (resp. all cusped) orientable hyperbolic 3-manifolds. In section 5, we compute some higher order terms in the Neumann-Zagier asymptotic formula for the examples considered in sections 3 and 4; some of those computations are used in section 4. In section [\[sec.Vol\]](#sec.Vol){reference-type="ref" reference="sec.Vol"}, we review some of the volume preserving moves on graphs from [@Mas]. In section [\[pack\]](#pack){reference-type="ref" reference="pack"}, we compute the moduli of the cusps of the manifolds that are obtained from the graph in Figure [\[fig.graphW\]](#fig.graphW){reference-type="ref" reference="fig.graphW"}. Then in section [\[const\]](#const){reference-type="ref" reference="const"}, we construct manifolds corresponding to binary cyclic words of $n$ letters and show that these manifolds are isometric if and only if their cyclic words are related by the natural action of the dihedral group $D_n$. Since the volume of these manifolds is a constant multiple of $n$, this gives a sequence $\mathcal{L}_n$ of families of distinct hyperbolic link complements which share the same volume $v_n$, such that the growth rate of $\#\mathcal{L}_n$ is at least exponential in $v_n$. Finally, in section 9, we collect some open problems related to the work in this paper.

**Acknowledgments:** We thank Sadayoshi Kojima and Danny Calegari for asking questions that led to this paper. We also thank Alan Reid, Rob Meyerhoff, Ze'ev Rudnick and Peter Sarnak for their helpful comments. The work of the first author was partially supported by the Australian Research Council grant DP1095760. The work of the second author was partially supported by the Global COE program "Computationism as a Foundation for the Sciences\". Much of this work was done during the second author's visit to the University of Melbourne; this visit was supported by the above Global COE program.
