---
doc_id: arxiv-1608.03227v4
doc_title: "January 30, 2018"
section_id: sec-012-33-chevalley-eilenberg-complex
section_title: "Chevalley-Eilenberg complex"
section_number: 3.3
pages: 14-15
source_pdf: 1608.03227v4.pdf
source_sha256: c71128e9a6c35343
doc_brief: "January 30, 2018 — For each braid β ∈ Brn we construct a 2-periodic complex Sβ of quasi-coherent C∗ × C∗ - equivariant sheaves on the non-commutative nested Hilbert scheme Hilb f ree 1,n ."
text_source: latex
latex_prose_ratio: 0.992
latex_coverage_ratio: 0.976
---
Let us remind the general setting of Chevalley-Eilenberg homology. Suppose that $\frh$ is a Lie algebra. Chevalley-Eilenberg complex $\SymbolPrint{\CE_\frh}$ is the complex $(V_\bullet(\frh),d)$ with $V_p(\frh)=U(\frh)\otimes_\CC\Lambda^p \frh$ and differential $\SymbolPrint{d_{ce}}=d_1+d_2$ where: $$d_1(u\otimes x_1\wedge\dots \wedge x_p)=\sum_{i=1}^p (-1)^{i+1} ux_i\otimes x_1\wedge\dots \wedge \hat{x}_i\wedge\dots\wedge x_p,$$ $$d_2(u\otimes x_1\wedge\dots \wedge x_p)=\sum_{i<j} (-1)^{i+j} u\otimes [x_i,x_j]\wedge x_1\wedge\dots \wedge \hat{x}_i\wedge\dots\wedge \hat{x}_j\wedge\dots \wedge x_p,$$

For $\frh$ module $V$ we define $\SymbolPrint{\CE_\frh(V)}:=\Hom_{U(\frh)}(\CE_\frh,V)$. The homology of this complex is called Chevalley-Eilenberg cohomology of $V$: $\mathrm{H}^*_{\Lie}(\frh,V)$. Consider a group $H$ such that $\mathrm{Lie}(H)=\frh$, $\calZ$ is an affine variety with $H$-action and $H$-invariant function $F$. Suppose we are given $\calF\in \MFs_\frh(\calZ,F)$, that is, we have a $\mathbb{Z} _2$-graded $\CC[\calZ]$ module $M$ with differential $D$ such that $D^2=F\cdot \mathrm{Id}$ and $D(h\cdot m)=h\cdot D(m)$ for any $h\in H$. The complex $\Hom_{U(\frh)}(\CE_\frh,M)$ is a $\mathbb{Z} \times \mathbb{Z} _2$-graded module and we collapse the first $\mathbb{Z}$-grading to $\mathbb{Z} _2$-grading.

The map $D+d_{ce}$ respects $\mathbb{Z} _2$-grading and the direct computation shows that $D$ and $d_{ce}$ anti-commute. Hence $(D+d_{ce})^2=F$ and we define $\CE_\frh(\calF):=(\Hom_{U\frh}(\CE_\frh,M),D+d_{ce})$. The differential $d_{ce}$ commutes with the elements of the ring invariants $\CC[\calZ]^\frh$, thus the complex $\CE_\frh(\calF)\in \MFs(\calZ/H,F)$ where $\calZ/H=Spec(\CC[\calZ]^\frh)$.

Later on we will need an analog for the lemma [\[lem: ext MF\]](#lem: ext MF){reference-type="ref" reference="lem: ext MF"} in the case of equivariant matrix factorizations. Our proof the lemma [\[lem: ext MF\]](#lem: ext MF){reference-type="ref" reference="lem: ext MF"} relies on the fact that every map from $\Hom^{<0}(C^+,C^+)$ is homotopically trivial and hence we can construct a homotopy that connects this map to $0$. It appears to us that the analog of this statement does not hold in the equivariant setting: the homotopy connecting the map to $0$ in general is equivariant up to homotopy.

Thus to make our proof of lemma [\[lem: ext MF\]](#lem: ext MF){reference-type="ref" reference="lem: ext MF"} work in equivariant setting one would have to enlarge our category of equivariant complexes to the category of $L_\infty$-complexes. That would make our theory extremely technical and we postpone this development for subsequent publications. Below we explain more elementary way to get around this problem: we incorporate Eilenberg-Chevalley complex in our definition of equivariant matrix factorizations. We give details below and we start with some preliminary material.

Let us define by $\Delta$ the standard map $\frh\to \frh\otimes \frh$ defined by $x\mapsto x\otimes 1+1\otimes x$. Suppose $V$ and $W$ are modules over Lie algebra $\frh$ then we use notation $\SymbolPrint{V\stackon{\otimes}{\scriptstyle\Delta} W}$ for $\frh$-module which is isomorphic to $V\otimes W$ as vector space, the $\frh$-module structure being defined by $\Delta$. Respectively, for a given $\frh$-equivariant matrix factorization $\calF=(M,D)$ we denote by $\SymbolPrint{\CE_{\frh}\stackon{\otimes}{\scriptstyle\Delta} \calF}$ the $\frh$-equivariant matrix factorization $(CE_\frh \stackon{\otimes}{\scriptstyle\Delta}\calF, D+d_{ce})$. The $\frh$-equivariant structure on $\CE_{\frh}\stackon{\otimes}{\scriptstyle\Delta} \calF$ originates from the left action of $U(\frh)$ that commutes with right action on $U(\frh)$ used in the construction of $\CE_\frh$.

In more details, for a given $\frh$-module $M$ the complex $\CE_\frh\stackon{\otimes}{\scriptstyle\Delta} M$ has terms $U(\frh)\otimes \Lambda^i(\frh)\otimes M$ with $\frh$-module structure $$x\cdot(u\otimes \omega\otimes m)=x\cdot u\otimes \omega\otimes m,$$ and the differential of the complex is $d_{ce}=d_1+d_2$ where: $$\begin{gathered}
  d_1(u\otimes x_1\wedge\dots \wedge x_p\otimes m)=\sum_{i=1}^p (-1)^{i+1} \left(ux_i\otimes m x_1\wedge\dots \wedge \hat{x}_i\wedge\dots\wedge x_p\otimes m+\right.\\
\left. x_1\wedge\dots \wedge \hat{x}_i\wedge\dots\wedge x_p\otimes x_i\cdot m\right) ,
\end{gathered}$$ $$d_2(u\otimes x_1\wedge\dots \wedge x_p)=\sum_{i<j} (-1)^{i+j} u\otimes [x_i,x_j]\wedge x_1\wedge\dots \wedge \hat{x}_i\wedge\dots\wedge \hat{x}_j\wedge\dots \wedge x_p.$$

A slight modification of the standard fact that $\CE_\frh$ is the resolution of the trivial module implies that $\CE_\frh\stackon{\otimes}{\scriptstyle\Delta} M$ is a free resolution of the $\frh$-module $M$.
