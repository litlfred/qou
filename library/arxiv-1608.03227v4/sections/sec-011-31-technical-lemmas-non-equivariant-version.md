---
doc_id: arxiv-1608.03227v4
doc_title: "Knot homology and sheaves on the Hilbert scheme of points on the plane"
section_id: sec-011-31-technical-lemmas-non-equivariant-version
section_title: "Technical lemmas: non-equivariant version"
section_number: 3.1
pages: 12-14
source_pdf: 1608.03227v4.pdf
source_sha256: c71128e9a6c35343
toc_source: outline
text_source: latex
latex_prose_ratio: 0.952
latex_coverage_ratio: 0.968
doc_brief: "Knot homology and sheaves on the Hilbert scheme of points on the plane — For each braid β ∈Brn we construct a 2-periodic complex Sβ of quasi-coherent C∗× C∗- equivariant sheaves on the"
---
We keep notations consistent with the previous section. Let $\SymbolPrint{\Mod_{per}}(\calZ)$ be a category of $\mathbb{Z} _2$-graded free $\CC[\calZ]$ modules with endomorphisms. An object $\calF\in \Mod_{per}(\calZ)$ is a pair $(M,D)$, $M=M^0\oplus M^1$, $M^i=\CC[\calZ]^{d_i}$ and $D\in \Hom_{\CC[\calZ]}(M^1,M^0)\oplus \Hom_{\CC[\calZ]}(M^0,M^1)$. The space of morphisms between two elements of $\Mod_{per}(\calZ)$ consists of morphisms of the corresponding $\CC[\calZ]$-modules that intertwine the endomorphisms.

We denote by $\SymbolPrint{\Com_{per}}(\calZ)$ be the category of complexes of $\mathbb{Z} _2$-graded modules with endomorphisms. We denote by $\Mod_{per}(\calZ)$ the abelian category with objects $(M,D)$ where $M=M^0\oplus M^1$ is a $\mathbb{Z} _2$-graded $\CC[\calZ]$-module and $D\in \Hom_{\CC[\calZ]}(M^i,M^{i+1})$. The morphisms in $\Mod_{per}(\calZ)$ preserve $\mathbb{Z} _2$-grading and intertwine the endomorphisms. We would like to emphasize that the elements of $\Mod_{per}(\calZ)$ are not matrix factorizations in general since we do not impose constraint $D^2=W$ and do not require the modules $M_i$ to be free.

An object of $\Com_{per}(\calZ)$ is a collection of objects $\calF_i\in \Mod_{per}(\calZ)$, $\calF_i=(M_i,D_i)$, $M_i=\CC[\calZ]^{r_i}$ and morphisms $d^+_i: M_i\to M_{i-1}$ which are morphisms of elements of $\Mod_{per}(\calZ)$ and $(d^+)^2=0$ as a linear map $M_i\to M_{i-2}$. Since $d^+_i$ intertwines the endomorphisms $D_{i-1}$ and $D_i$ the kernel $\ker d^+_i\subset M_i$ and image $\im d^+_i\subset M_{i-1}$ are elements of $\Mod_{per}(\calZ)$ and we use notation $H^i(\calF)$ for the quotient $\ker d^+_i/\im d^+_{i+1}$. For subset of $\Com_{per}(\calZ)$ consisting of complexes $\calF$ such that $M_i=0$ for $i\notin [0,\ell]$ we use notation $\SymbolPrint{\Com^\ell_{per}}(\calZ)$.

Analogously to the previous case we introduce notation $\Hom^k(\calF_\bullet,\calF_\bullet)=\oplus_i \Hom(\calF_i,\calF_{i-k})$ respectively we use notation $\xExt^k_{d^+}(\calF_\bullet,\calF_\bullet)$ for the elements of $\Hom^k(\calF_\bullet,\calF_\bullet)$ that commute with the differential $d^+$. The homotopy relations between the elements of $\xExt^k_{d^+}(\calF_\bullet,\calF_\bullet)$ is defined in the natural way: $$f\sim g,\mbox{ iff there is } h\in \Hom^{k-1}(\calF_\bullet,\calF_\bullet), \quad f-g=d^+\circ h-h\circ d^+.$$

The technical lemma that we need later is a generalization of lemmas [\[lem: ext MF\]](#lem: ext MF){reference-type="ref" reference="lem: ext MF"} and [\[lem: ext uniq\]](#lem: ext uniq){reference-type="ref" reference="lem: ext uniq"}, the proof is essentially identical to the proof of the above mentioned lemmas.

::: lemma
[]{#lem: ext MF+ label="lem: ext MF+"} Let $(\calF_\bullet,d_\bullet^+)$, $\calF_i=(M_i,D_i)$ be an element of $\Com^\ell_{per}(\calZ)$ and $F\in \CC[\calZ]$ such that $M_i$ are free $\CC[\calZ]$-modules and

1.  Elements of $\xExtdpv{<0}(\calF_\bullet,\calF_\bullet)$ are homotopic to $0$

2.  Element $F-D^2\in \xExtdpv{0}(\calF_\bullet,\calF_\bullet)$ is homotopic to $0$

Then there are maps $d_{ij}^-\in \Hom( \calF_i, \calF_j)$, $j>i$ such that $$[(\calF_\bullet, D+d^++d^-)]_{per}\in \MFs(\calZ,F).$$
:::

::: proof
*Proof.* By assumption of the lemma there exist morphisms of $\CC[\calZ]$ modules $h^{(-1)}_i\in\Hom( \calF_i, \calF_{i+1})$ such that $F-D^2=h^{(-1)}_i\circ d_{i+1}^++d_i^+\circ h^{(-1)}_{i-1}$. Then a new differential $D^{(-1)}:=D+d^++h^{(-1)}$ satisfies the relation $$\left(D^{(-1)}\right)^2-F =(h^{(-1)})^2\in \yHom^{\leq-2}(C_\bullet,C_\bullet).$$

Thus $D^{(-1)}$ provides a base

of induction for the proof of existence $h^{(-2i-1)}\in \yHom^{-2i-1}(\calF_\bullet,\calF_\bullet)$, $i\ge 0$ such that

1.  $[h^{(-1)},d^+]_+=F-D^2$

2.  $[h^{(-2i-1)},d^+]_+=\sum_{j=0}^{i-1} h^{(-2j-1)} h^{(-2i+2j+1)}$, $i>0$

were we used the notation $[a,b]_+=ab+ba$.

Indeed, suppose we constructed $h^{(-2i-1)}$ for all $i<j$. Define $D^{(-2j+1)}=D+d^++\sum_{k=0}^{j-1} h^{(-1-2k)}$, then the inductive assumption implies: $$\label{eq: D2 ext}
  \begin{aligned}
    \left( D^{(-2j+1)}\right)^2-F+D^2-R^{(-2j)}\in \yHom^{<-2j}(\calF_\bullet,\calF_\bullet),\\
    R^{(-2j)}=\sum_{k=0}^{j-1} h^{(-2k-1)} h^{(-2j+1+2k)}
    \end{aligned}$$ On the other hand, a direct computation using the inductive assumptions and the fact that $F$ commutes with all $h^{(2i-1)}$ and $d^+$ implies $$\label{eq: com d+ ext}
 [d^+,R^{(-2j)}]=0.$$ In more details, let us introduce notation $R^{(<-2j)}:=(D^{(-2j-1)})^2-F-R^{(-2j)}$ then $$\begin{gathered}
0=[D^{(-2j-1)}, (D^{(2j-1)})^2]=[D+d^+ +\sum_i h^{(-2i-1)}, F-D^2+R^{(-2j)}+R^{(<-2j)}]\\=[d^+,R^{(-2j)}]+[d_++\sum_i h^{(-2i-1)},R^{(<-2j)}]+[\sum_i h^{(-2j-1)},R^{(-2j)}+R^{(-2j-1)}].
\end{gathered}$$ The first term in the last sum is from $\xHom^{-2j+1}(\calF_\bullet,\calF_\bullet)$, on the other hand the last two are from $\xHom^{<-2j+1}(\calF_\bullet,\calF_\bullet)$ thus ([\[eq: com d+ ext\]](#eq: com d+ ext){reference-type="ref" reference="eq: com d+ ext"}) follows.

Thus $R^{(-2j)}$ is the morphism of the complex $(\calF_\bullet,d^+)$ of degree $-2j$, that is, an element of $\Hom^{-2j}(\calF_\bullet,\calF_\bullet)$. The assumption of our lemma implies that such morphism is homotopic to zero and the homotopy morphism $h^{(-2j-1)}\in \xHom^{-2j-1}(\calF_\bullet,\calF_\bullet)$ provides the induction step since $[h^{(-2j-1)},d^+]_+=R^{(-2j)}$.

Thus by setting $d_i^-=\sum_i h^{(-2i-1)}$ we obtain the desired extension because of ([\[eq: D2 ext\]](#eq: D2 ext){reference-type="ref" reference="eq: D2 ext"}). ◻
:::

::: lemma
[]{#lem: uniq MF+ label="lem: uniq MF+"} Let $(\calF_\bullet,d_\bullet^+)$ be an element of $\Com^\ell(\calZ)$ and $F\in \CC[\calZ]$ that satisfy conditions of the previous lemma. Suppose there two sets of differentials $d^-_{ij},\hat{d}^-_{ij}: \calF_i\to \calF_j$, $j>i$ such that $$[(\calF_\bullet, D+d^++d^-)]_{per}\in \MFs(\calZ,F),\quad [(\calF_\bullet, D+d^++\hat{d}^-)]_{per}\in \MFs(\calZ,F)$$ then there is $\Psi=\sum_{i\le 0}\Psi_i$, $\Psi_i\in \Hom^{-i}(\calF_\bullet,\calF_\bullet)$, $\Psi=\mathrm{Id}$ such $$\Psi\circ (D+d^++d^-)\circ \Psi^{-1}= D+d^++\hat{d}^-.$$
:::

Proof of the this lemma is identical to the proof of lemma [\[lem: ext uniq\]](#lem: ext uniq){reference-type="ref" reference="lem: ext uniq"} and we omit it.
