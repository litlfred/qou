---
doc_id: arxiv-1608.03227v4
doc_title: "Knot homology and sheaves on the Hilbert scheme of points on the plane"
section_id: sec-047-91-general-method-of-the-proof
section_title: "General method of the proof"
section_number: 9.1
pages: 47-50
source_pdf: 1608.03227v4.pdf
source_sha256: c71128e9a6c35343
toc_source: outline
text_source: latex
latex_prose_ratio: 0.977
latex_coverage_ratio: 0.991
doc_brief: "Knot homology and sheaves on the Hilbert scheme of points on the plane — For each braid β ∈Brn we construct a 2-periodic complex Sβ of quasi-coherent C∗× C∗- equivariant sheaves on the"
---
It is easier to discuss the reduced convolution and we focus on this operation. From construction of the reduced convolution $\bar{\star}$ we see that the key step of computation of $\calG\bar{\star}\calF$ is the \"computation\" of $\CE_{\frn^{2}}(\bar{\pi}_{12}^*\otimes_B \bar{\pi}_{23}^*)(\calG\boxtimes\calF)$. The latter complex is a matrix factorization with non-trivial potential, we can not compute its cohomology in conventional sense, since the differential does not square to $0$. However, we can get quite close to that by contracting the part of the complex with non-trivial action of $\frn^{(2)}$. We give details below.

To simplify notations we consider problem of simplifying of the complex $\CE_{\frn}(\calF)^T$ where $\calF\in \MF_B(G\times Z, F)$, $F\in \CC[G\times Z]^B$ and $B$ acts on $G$ by the left multiplication and acts trivially on $Z$. Let $R=\CC[G]$ and $R\langle \chi\rangle$ is the ring with $B$-equivariant structure twisted by the character $\chi\in \Hom(T,\CC^*)$: $b\cdot 1=\chi(b) 1$ for $b\in B$ and $1\in R\langle\chi\rangle$ is the generator of $R$-module $R\langle \chi\rangle$. We assume that the matrix factorization that we study is the sum of free $R$-modules $\calF=(M,D)$ $M=\oplus_{i=1}^N M_i$ and $M_i=\CC[Z]\otimes R\langle \chi^i\rangle$. It is well known that the CE homology of such free modules has a geometric interpretation, we were unable to pinpoint a proof of the interpretation and provide an outline of a proof for it

::: proposition
[]{#prop: homs G/B label="prop: homs G/B"} For any $\chi\in \Hom(T,\CC^*)$ $$\textup{H}^*_{\Lie}(\frn,R\langle -\chi\rangle)^T=\textup{H}^*(G/B,L_\chi),$$ where LHS is the coherent sheaf cohomology.
:::

::: proof
*Proof.* Let $S_n$ be the symmetric group and $B_-\subset G=GL_n$ the subgroup of lower triangular matrices. The Bruhat decomposition $G=B S_n B$ implies $G=B_- S_n B$ because $B_-=w_0 B w_0$ with $w_0\in S_n$ being the longest element of $S_n$. Each subset $G_w=B_- w B\subset G$ is an open $B$-invariant subset of $G$ and let us denote by $R_w$ the ring of regular functions on $G_w$. Respectively, we denote by $G_{S}:=\cap_{w\in S} G_{w}$ where $S\subset S_n$ is a finite subset and we use notation $R_S$ for the ring of regular functions on $G_S$. In particular, we have $R=R_\emptyset$.

There are natural inclusion maps $R_S\to R_{S'}$ for $S\subset S'$ and these inclusions maps with appropriate sings form a Cech resolution $\check{C}_\bullet(R)$ of $R$ by free $\frn$-modules $\check{C}_i(R)=\sum_{|S|=i} R_S$. On other hand let us observe that the decomposition above turns in a Cech cover $\check{C}_\bullet(G/U)$ of $G/U$, $G/U=\cup_{w\in S_n} B_-w$, we use same notation for the resolution of the sheaf of regular functions on $G/U$ induced by the cover.

Next we observe that $R_w=\CC[B_-]\otimes \CC[U]$, $\mathrm{Lie}(U)=\frn$ and $\frn$ does not act on the first factor. Since $H^*_{Lie}(\frn,\CC[U])=\CC$ we see that $H^*_{Lie}(\frn,R)=\check{C}_*(G/U)$. The last isomorphism is $T$-equivariant hence the proposition follows. ◻
:::

LHS of the last equation is the total space cohomology of the line bundle $L_\chi$. The fiber of $L_\chi$ at $V^\bullet=\{V^1\subset \dots\subset V^n \}\in G/B$ is equal to $\bigotimes_i (V^{i+1}/V^i)^{d_i}$ where $\chi=\sum d_i \alpha_i$. The most important case of this theorem is the case $n=2$: $$\textup{H}^*_{\Lie}(\frn, R\langle -k\alpha \rangle)=\textup{H}^*(\mathbb{P}^1,\calO(k)).$$

The other way to present previous proposition is to say that we use homotopy equivalence $\CE_{\frn}(R\langle\chi\rangle)^T\sim \oplus_i H^i(G/B,L_\chi)$ where the RHS is complex with zero differential. The homotopy could be constructed explicitly by combining Chech resolution technique with the Gauss elimination method from below.

::: proposition
Let $\calF=(M,D)\in \MFs_B(G\times Z,F)$ as above then there is a homotopy equivalence $$\CE_{\frn}(\calF)^T\sim (\oplus_{i=1}^N H^*(G/B, L_{\rho_i}), \bar{D})\in \MFs(Z,F),$$ where $\bar{D}$ is the differential induced by the differential $D$.
:::

::: proof
*Proof.* As in the proof of proposition [\[prop: homs G/B\]](#prop: homs G/B){reference-type="ref" reference="prop: homs G/B"} we can construct the Cech resolution $\check{C}_\bullet(M)$ of $M$. Since the Chevalley-Eilenberg differential $d_{CE}$ is acyclic on term of the $\check{C}_\bullet(M)$ we apply Gauss elimination to construct homotopy $\CE_{\frn}(\calF)\sim (H^0_{Lie}(\frn,\check{C}_\bullet(M),D')$ with $D'$ induced by $D$. As it is explained in proposition [\[prop: homs G/B\]](#prop: homs G/B){reference-type="ref" reference="prop: homs G/B"} $H^*(H^0(\frn,\check{C}_\bullet(M)),d_{\check{C}})=H^*(G/B,M)=\oplus_i H^*(B/G,L_{\rho_i})$ hence we again can apply the Gauss elimination and obtain the homotopy from the statement of the proposition. ◻
:::

The Gauss elimination lemma is the standard tool of homological algebra, one can find more discussion (and applications) of this lemma in [@BN] in the case of complexes of vector spaces. Our proof below is very close to the argument of [@BN].

::: lemma
Suppose $M= W\oplus V$, $V=V^0\oplus V^1$, $W=W^0\oplus W^1$ and $$D^{i,i+1}=d_{VV}^{i,i+1}+d_{VW}^{i,i+1}+d_{Wv}^{i,i+1}+d_{WW}^{i,i+1},$$ $d_{AB}^{i,i+1}\in Hom(B^{i+1},A^i)$ form the matrix factorization $(M,D)\in \textup{MF}(Z,F)$, $D=D^{01}+D^{10}$. Let us also assume $d^{10}_{VV}=\phi$ is an isomorphism.

Then there is a homotopy equivalence in the category of matrix factorizations $$(M,D)\sim (W,D_W),\quad D_W=D_W^{10}+D_W^{01},$$ $$D_W^{10}=d_{WW}^{10}-d_{WV}^{10}\circ\phi^{-1}\circ d_{VW}^{10},\quad D_W^{01}=d_{WW}^{01}.$$
:::

::: proof
*Proof.* Let us that $(W,D_W)\in \textup{MF}(Z,F)$. First, let us first compute $D^2_W|_{W^0}$: $$d_{WW}^{01}\circ (d_{WW}^{10}-d_{WV}^{10}\circ\phi^{-1}\circ d_{VW}^{10})=d_{WW}^{01}\circ d_{WW}^{10}+d^{01}_{WV}\circ d^{10}_{VV}\circ \phi^{-1}\circ d_{VW}^{10}=F,$$ where we used $d_{WW}^{01}\circ d_{WV}^{10}+d_{WV}^{01}\circ d_{VV}^{10}=0$ for the first equality. The check that $D^2_W|_{W^1}=F$ is similar.

Next we define morphisms $i:W\rightarrow M$ and $\pi:M\rightarrow W$: $$i=
    \begin{bmatrix}
      1\\
      \psi
    \end{bmatrix},\quad
   \pi= \begin{bmatrix}
      1&\rho
    \end{bmatrix},$$ here $\psi=\psi_{VW}^{00}+\psi_{VW}^{11},\rho=\rho_{WV}^{00}+\rho_{WV}^{11}$ and $\psi_{VW}^{00}=-\phi^{-1}\circ d_{VW}^{10}$, $\psi_{VW}^{11}=0$, $\rho_{WV}^{00}=0$, $\rho_{WV}^{11}=-d_{WV}^{10}\circ \phi^{-1}$.

It is immediate to see that $D\circ i=i\circ D_W$ and $D_W\circ \pi=\pi\circ D$. Also since $\psi\circ \pi=0$ and $\pi\circ\psi=0$ we get $\pi\circ i=1$. On the other hand we can extend by $0$ the map $\phi^{-1}$ to obtain $\phi'\in \oplus_i\Hom(V^{i},V^{i+1})$ and $$\chi=
    \begin{bmatrix}
    \phi'&0\\0&0  
    \end{bmatrix}.$$ Since $\phi^{-1}\circ d_{VV}^{10}=1$ and $d_{VV}^{10}\circ \phi^{-1}=1$ we see that $i\circ \pi-1=\chi\circ D+D\circ \chi$ ◻
:::

Thus to obtain the reduction $\bar{D}$ from the lemma we apply previous lemma to our complex $\CE_{\frn}(\calF)^T$. To keep exposition clear let us explain one would apply the elimination lemma to construct homotopy $(\oplus_{i=0}^N C_i, d_\bullet)\sim (H^\bullet(C,d),0)$: the case of matrix factorizations from proposition [\[prop: homs G/B\]](#prop: homs G/B){reference-type="ref" reference="prop: homs G/B"} differs from this model case by feature that on every step of our construction we need to compute correction differentials.

Indeed, in our model case we can construct a non-canonical splitting $C_0=\textup{Im} d_1\oplus H^0(C,d)$, $C_1=\Ker d_1\oplus C_1/\Ker d_1$. The differential $d_1$ provides an isomorphism between $\textup{Im} d_1$ and $C_1/\Ker d_1$ and we can apply elimination lemma to obtain homotopy equivalent complex $(C',d)\oplus (\textup{H}^0(C,d),0)$: $C_i'=C_i$, $i>1$, $C'_1=\Ker d_1$. Now we can apply the case method to the complex $(C',d)$ and so on.

To simplify notations, we assume for the rest of the section that $G=G_2=SL_2$, $B=B_2\subset G_2$, $\frb=\textup{Lie}(B_2)$. Respectively, character group of $B_2$ under this assumption is $\mathbb{Z}$, $1\in\mathbb{Z}$ corresponds to the character $\chi_1$ from the section [\[ssec:gens\]](#ssec:gens){reference-type="ref" reference="ssec:gens"}
