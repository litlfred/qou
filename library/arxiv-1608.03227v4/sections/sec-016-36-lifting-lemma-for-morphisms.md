---
doc_id: arxiv-1608.03227v4
doc_title: "Knot homology and sheaves on the Hilbert scheme of points on the plane"
section_id: sec-016-36-lifting-lemma-for-morphisms
section_title: "Lifting lemma for morphisms"
section_number: 3.6
pages: 18-20
source_pdf: 1608.03227v4.pdf
source_sha256: c71128e9a6c35343
toc_source: outline
text_source: latex
latex_prose_ratio: 0.941
latex_coverage_ratio: 0.964
doc_brief: "Knot homology and sheaves on the Hilbert scheme of points on the plane — For each braid β ∈Brn we construct a 2-periodic complex Sβ of quasi-coherent C∗× C∗- equivariant sheaves on the"
---
To define equivariant push-forward below we need to state few extra facts about our lifting procedure.

::: lemma
[]{#lem: ext mor label="lem: ext mor"} Suppose we are are given $(\calF_\bullet,d_\bullet^+)$, $\calF_i=(M_i,D_i)$ and $(\tilde{\calF}_\bullet,\tilde{d}_\bullet^+)$, $\tilde{\calF}_i=(\tilde{M}_i,\tilde{D}_i)$ be an element of $\Com^{\frh,\ell}_{per}(\calZ)$ and $F\in \CC[\calZ]^\frh$ such that they satisfy conditions of lemma [\[lem: ext MF+eq\]](#lem: ext MF+eq){reference-type="ref" reference="lem: ext MF+eq"} and $\partial,d^-$, $\tilde{\partial},\tilde{d}^-$ are as in conclusion of lemma [\[lem: ext MF+eq\]](#lem: ext MF+eq){reference-type="ref" reference="lem: ext MF+eq"}. Let us also assume that elements of $\mathrm{\xExt}^{<0}_{d^+,\tilde{d}^+}(\calF_\bullet,\tilde{\calF}_\bullet)$ are homotopic to $0$

Suppose also that there is a map $\Psi\in \Hom^{k}(\CE_\frh\odel \calF_\bullet,\CE_\frh\odel\tilde{\calF}_\bullet)$, $k\le  0$ such that $\tilde{d}^+\circ \Psi=-\Psi\circ d^+$ and $(\tilde{D}+\tilde{d}_{ce}+\partial)\circ \Psi-\Psi\circ (D+d_{ce}+\tilde{\partial})$ is $d^+,\tilde{d}^+$ homotopic to $0$. Then there are $\frh$-equivariant elements $\Psi_i  \in \Hom^{k-i}(\CE_\frh\odel \calF_\bullet,\CE_\frh\odel\tilde{\calF}_\bullet)$, $i>0$ such that $$\tilde{D}_{tot}\circ(\Psi+\sum_i \Psi_i)=(\Psi+\sum_i \Psi_i)\circ D_{tot},$$ $$\tilde{D}_{tot}:=\tilde{d}^++\tilde{D}+\partial+\tilde{d}^-+\tilde{d}_{ce}+\tilde{\partial}^-,\quad
D_{tot}:= d^++D+\partial+d_{ce}+\partial^-,$$

The elements $\Psi_i$ are unique up-to the homotopy: if $$\Psi'_i \in \Hom^{k-i}(\CE_\frh\odel \calF_\bullet,\CE_\frh\odel\tilde{\calF}_\bullet)$$ is another collection of elements satisfying previous equation then there is $h$ such that $$\sum_i \Psi_i-\Psi'_i=\tilde{D}_{tot}\circ h- h\circ D_{tot}$$
:::

::: proof
*Proof.* Let us introduce short-hand notations $d_0=D+\partial+d_{ce}$ and $\tilde{d}_0=\tilde{D}+\tilde{\partial}+\tilde{d}_{ce}$, $d_-=d^-+\partial^-$, $\tilde{d}^-=\tilde{d}^-+\tilde{\partial}^-$. We also use notations $\Hom^i$, $\xExtdpv{i}$ as in the previous lemmas.

First let us notice that $$\tilde{D}_{tot}\circ \Psi-\Psi\circ D_{tot}=\left( \tilde{d}_0\circ \Psi-\Psi\circ d_0\right)+\left(\tilde{d}_-\circ \Psi-\Psi\circ d_-\right).$$ The first summand is homotopic to $0$ by the theorem assumption and the second term is from $\Hom^{<k}$ and $$[d^+,\tilde{d}_-\circ \Psi-\Psi\circ d_-]= [d^+,\tilde{d}_-]_+\circ \Psi-\Psi\circ [d^+,d_-]_+=(F-\tilde{d}_0^2)\circ\Psi-\Psi\circ (F-d_0^2)=0.$$

Thus there are maps $\Psi_1\in \Hom^{k-1}, \Psi_2\in \Hom^{k-2}$ such that $[d^+,\Psi_2]_+=[\tilde{d}_-\circ \Psi-\Psi\circ d_-]_{k-1}$ and $[d^+,\Psi_1]_+= \tilde{d}_0\circ \Psi-\Psi\circ d_0$. Hence $\Psi^{(2)}=\Psi+\Psi_1+\Psi_2$ such that $$\tilde{D}_{tot}\circ \Psi^{(2)}-\Psi^{(2)}\circ D_{tot}\in \Hom^{\le k-2}.$$ That is the seed to the inductive construction of $\Psi^{(m)}=\Psi+\sum_{i=1}^m \Psi_m$ such that $$\tilde{D}_{tot}\circ \Psi^{(m)}-\Psi^{(m)}\circ D_{tot}\in \Hom^{\le k-m}.$$ To prove the step of induction we observe that $$\tilde{D}_{tot}\circ\left(  \tilde{D}_{tot}\circ \Psi^{(m)}-\Psi^{(m)}\circ D_{tot}\right)-\left(  \tilde{D}_{tot}\circ \Psi^{(m)}-\Psi^{(m)}\circ D_{tot}\right)\circ D_{tot}=0$$ because $D_{tot}^2=F$ and $\tilde{D}_{tot}=F$. If we denote by $R$ the expression $\tilde{D}_{tot}\circ \Psi^{(m)}-\Psi^{(m)}\circ D_{tot}$ then we get: $$\begin{gathered}
  0=\tilde{D}_{tot}\circ R-R\circ D_{tot}=[d^+, [R]_{k-m}]+\left((\tilde{d}_0+\tilde{d}_-)\circ [R]_{k-m}\right.\\
  \left.-
[R]_{k-m}\circ(d_0+d_-)\right)+\left(\tilde{D}_{tot}\circ [R]_{<k-m}-[R]_{<k-m}\circ D_{tot}\right).
\end{gathered}$$ Since the first summand of the last expression is from $\Hom^{k-m+1}$ and the last two terms are from $\Hom^{\le k+m}$ we conclude that $[d^+,[R]_{k-m}]=0$. Thus $[R]_{k-m}\in \xExtdpv{k-m}$ and there is $\Psi_{m+1}\in \Hom^{k-m-1}$ such that $[R]_{k-m}=[\Psi_{m+1},d^+]_+$. Hence $\Psi^{(m+1)}=\Psi^{(m)}+\Psi_{m+1}$ proves the induction step.

The last part of the lemma follows from the following statement. Suppose $\Psi\in \Hom^{<k}$, $k\le 0$ is such that $\tilde{D}_{tot}\circ \Psi=\Psi\circ D_{tot}$ then there is $h\in \Hom^{<k+1}$ such that $\Psi'=\Psi-(\tilde{D}_{tot}\circ h+ h\circ D_{tot})\in \Hom^{<k-1}$. Indeed, since $$\tilde{D}_{tot}\Psi'-\Psi'\circ D_{tot}=(\tilde{D}_{tot})^2\circ h-h\circ (D_{tot})^2=0,$$ we can run inductive argument and construct $g$ such that $\Psi=\tilde{D}_{tot}\circ g+ g\circ D_{tot}$.

The statement itself follows from the computation below: $$\begin{gathered}
  0=\tilde{D}_{tot}\circ \Psi-\Psi\circ D_{tot}=[d^+,[\Psi]_{k-1}]+\left( (\tilde{d}_0+\tilde{d}_-)\circ[\Psi]_{k-1}]\right.
  \\\left.-[\Psi]_{<k-1}\circ (d_0+d_-)\right)
+\left(\tilde{D}_{tot}\circ [\Psi]_{<k-1}-[\Psi]_{<k-1}\circ D_{tot}\right)
\end{gathered}$$ since the first summand is from $\Hom^k$ and the other summands are from $\Hom^{<k}$ and thus $[d^+,[\Psi]_{k-1}]=0$ and $[\Psi]_{k-1}$ is homotopically trivial with respect to $d_+$. It is easy to check that $h$, such that $[d^+,h]_-=[\Psi]_{k-1}$ provides a proof of the statement. ◻
:::
