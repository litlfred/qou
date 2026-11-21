---
doc_id: arxiv-1608.03227v4
doc_title: "Knot homology and sheaves on the Hilbert scheme of points on the plane"
section_id: sec-015-35-extension-lemmas
section_title: "Extension lemmas"
section_number: 3.5
pages: 16-18
source_pdf: 1608.03227v4.pdf
source_sha256: c71128e9a6c35343
toc_source: outline
text_source: latex
latex_prose_ratio: 0.946
latex_coverage_ratio: 0.946
doc_brief: "Knot homology and sheaves on the Hilbert scheme of points on the plane — For each braid β ∈Brn we construct a 2-periodic complex Sβ of quasi-coherent C∗× C∗- equivariant sheaves on the"
---
We have the following analog of Lemma [\[lem: ext MF\]](#lem: ext MF){reference-type="ref" reference="lem: ext MF"} and respective uniqueness result.

::: lemma
[]{#lem: ext MF eq label="lem: ext MF eq"} Let $(C_\bullet,d_\bullet^+)$ be a $\frh$-equivariant complex $$C_0\xleftarrow{d_1^+}C_1\xleftarrow{d_2^+}\dots\xleftarrow{d_\ell^+} C_\ell$$ of $\CC[\calZ]$ modules and $F\in \CC[\calZ]^\frh$ such that

1.  Elements of $\xExtdpv{<0}(C_\bullet,C_\bullet)$ are homotopic to $0$

2.  The element $F\in \xExtdpv{0}(C_\bullet,C_\bullet)$ is homotopic to $0$.

Then there are homomophisms $d^-_{ij}: C_i\to C_j$, $i>j$ of $\CC[\calZ]$-modules such that $$[(C_\bullet,d^++d^-)]_{per}\in \MFs(\calZ,F)$$ and there are homomorphisms of $\CC[\calZ]$, $\partial_{ij}^-: \Lambda^\bullet\frh\otimes C_i\to \Lambda^{<\bullet}\frh\otimes C_j$, $j>i$ such that $$[(C_\bullet, d^-+d^+,\partial^-)]_{per}\in \MFs_\frh(\calZ,F).$$
:::

We do not provide a proof of this lemma since it is a particular case of a more general statement that is proven below. The more general statement is an equivariant version of lemmas [\[lem: ext MF+\]](#lem: ext MF+){reference-type="ref" reference="lem: ext MF+"} and [\[lem: uniq MF+\]](#lem: uniq MF+){reference-type="ref" reference="lem: uniq MF+"}.

Let $\Mod^{\frh}_{per}(\calZ)$ be a category of $\mathbb{Z} _2$-graded free $\CC[\calZ]$ modules with endomorphisms equipped with $\frh$-equivariant structure. That is an object $\calF\in \Mod^\frh_{per}(\calZ)$ is the triple $(M,D,\partial)$, $M=M^0\oplus M^1$, $M^i=\CC[\calZ]\otimes W^i$ where $W^i\in \Mod_\frh$, $D\in \Hom_{\CC[\calZ]}(M^1,M^0)\oplus \Hom_{\CC[\calZ]}(M^0,M^1)$, $\partial=\sum_{i> j} \partial_{ij}$, $\partial_{ij}\in \Hom_{\CC[\calZ]}(\Lambda^i\frh\otimes M, \Lambda^j\frh\otimes M)$.

The $\frh$-action on $M_i$ is defined by the Hopf formula and using this action one define differential $d_{ce}$ on $\CE_\frh\odel M$. The space of morphism between two objects $(M,D,\partial),  (\tilde{M},\tilde{D},\tilde{\partial})\in \Mod^{\frh}_{per}(\calZ)$ consists of morphisms $\Psi\in \Hom_{\CC[\calZ]}(M,\tilde{M})$ that intertwine the endomorphisms: $$\Psi\circ(D+d_{ce}+\partial)=(\tilde{D}+\tilde{d}_{ce}+\tilde{\partial})\circ \Psi.$$ We do not require $\frh$-equivariance for the morphisms in the category and we do not require $\frh$-equivariance of $D$.

Similarly we define $\Com^{\frh}_{per}(\calZ)$ to be the category of (not necessarily $\frh$-equivariant) complexes of objects of $\Mod_{per}^\frh(\calZ)$, we do not impose $\frh$-equivariance conditions on the morphisms and homotopies in $\Com^{\frh}_{per}(\calZ)$. In this setting we have the following equivariant version lemma [\[lem: ext MF+\]](#lem: ext MF+){reference-type="ref" reference="lem: ext MF+"},[\[lem: uniq MF+\]](#lem: uniq MF+){reference-type="ref" reference="lem: uniq MF+"}:

::: lemma
[]{#lem: ext MF+eq label="lem: ext MF+eq"} Let $(\calF_\bullet,d_\bullet^+)$, $\calF_i=(M_i,D_i,\partial_i)$ be an element of $\Com^{\frh,\ell}_{per}(\calZ)$ and $F\in \CC[\calZ]^\frh$ such that

1.  Elements of $\xExtdpv{<0}(\calF_\bullet,\calF_\bullet)$ are homotopic to $0$

2.  Element $F-D^2\in \xExtdpv{0}(\calF_\bullet,\calF_\bullet)$ is homotopic to $0$

3.  Element $F-(D+\partial+d_{ce})^2\in \xExtdpv{0}(\CE_\frh\odel \calF_\bullet,\CE_\frh\odel \calF_\bullet)$ is homotopic to $0$.

Then there are maps $d^-_{ij}: \calF_i\to \calF_j$, $i>j$ of elements of $\Mod_{per}(\calZ)$ such that $$[(\calF_\bullet,d^++D+d^-)]_{per}\in \MFs(\calZ,F)$$ and there are maps of elements of $\Mod_{per}(\calZ)$, $\partial_{ij}^-: \Lambda^\bullet\frh\otimes\calF_i\to \Lambda^{<\bullet}\frh\otimes \calF_j$, $j>i$ such that $$[(\calF_\bullet, D+d^-+d^+,\partial+\partial^-)]_{per}\in \MFs_\frh(\calZ,F).$$
:::

::: proof
*Proof.* In the proof we would use short hand notations $\Hom^{i}$, $\xExtdpv{i}$ for space morphisms $\xHom^i(\calF_\bullet,\calF_\bullet)$ and $\xExtdpv{i}(\calF_\bullet,\calF_\bullet)$. We also assume that we have chosen the signs in our construction of $d_+$ in such that the equivariance condition is equivalent to $[d_++D,d_{ce}+\partial]_+=0$. Given linear map $A\in \xHom(\CE_\frh\odel \calF_\bullet,\CE_\frh\odel \calF_\bullet)$ we denote by $[A]_{k}$ the part of $A$ that is in $\xHom(\CE_\frh,\CE_\frh)\otimes \xHom^i$.

As first step of our construction we apply the lemma [\[lem: ext MF+\]](#lem: ext MF+){reference-type="ref" reference="lem: ext MF+"} to construct differentials $d^-_{ij}: \calF_i\to \calF_j$ such that $$[(\calF_\bullet,D+d^++d^-)]_{per}\in \MFs(\calZ,F).$$

By the first step and the assumption of the lemma we have $$\begin{gathered}
 (d^++d^-+D+\partial+d_{ce})^2-F=[d^++d^-+D,\partial +d_{ce}]_+\\+(\partial+d_{ce})^2\in \Hom(\Lambda^*\frh,\Lambda^*\frh)\otimes \Hom^{\le 0}.
\end{gathered}$$

Since $\partial+d_{ce}\in \Hom(\Lambda^\bullet \frh,\Lambda^{<\bullet}\frh)\otimes \Hom^0$, we conclude that there is $h^{(-1)}\in \Hom(\Lambda^\bullet \frh,\Lambda^{<\bullet}\frh)\otimes \Hom^{-1}$ such that $[h^{(-1)},d_+]_+=(\partial+d_{ce})^2$ and hence $$\begin{gathered}
  d^{(-1)}:= (d^++d^-+D+\partial+d_{ce})^2-F-[h^{(-1)},d_+]_+\\
  =[d^-,\partial+d_{ce}]\in \Hom(\Lambda^*\frh,\Lambda^*\frh)\otimes \Hom^{<0}.
  
\end{gathered}$$

Let us define $D^{(0)}:=d^++D+\partial+d_{ce}+d^-+h^{(-1)}$ then we see that $$(D^{(0)})^2-F=d^{(-1)}+[h^{(-1)},d^-+D+\partial+d_{ce}]_++(h^{(-1)})^2\in \Hom(\Lambda^\bullet\frh,\Lambda^{<\bullet})\otimes \Hom^{<0}.$$

We have proved the seed of induction for the following statement. For any $k$ there is $h^{(k)}\in \Hom(\Lambda^{\bullet}\frh,\Lambda^{<\bullet}\frh)\otimes \Hom^{-k}$ such that $$(D^{(k)})^2-F\in \Hom( \Lambda^\bullet\frh,\Lambda^{<\bullet}\frh) \otimes \Hom^{<-k},\quad  D^{(k)}=D^{(k-1)}+h^{(-k-1)}.$$

Suppose we have constructed $D^{(k)}$ and $h^{(-i)}$, $i\le k+1$. By induction assumption we have $(D^{(k)})^2=
F+[(D^{(k)})^2]_{<-k}$ and we see that

$$\begin{gathered}
0=[D^{(k)}, (D^{(k)})^2]=[D^{(k)},[(D^{(k)})^2]_{<-k}]=[d_+, [(D^{(k)})^2)]_{-k-1}]\\+[d_+,[(D^{(k)})^2]_{<-k-1}]+[D+\partial+d_{ce}+d^-+\sum_i h^{(-i)},[(D^{(k)})^2]_{<-k}].
\end{gathered}$$ the first summand of the last expression is from $\Hom(\Lambda^\bullet\frh,\Lambda^{<\bullet}\frh)\otimes \Hom^{-k}$ and the last two summands are from $\Hom(\Lambda^\bullet\frh,\Lambda^{<\bullet}\frh)\otimes \Hom^{<-k}$. Hence $[(D^{(k)})^2]_{-k-1}\in \Hom_{d_+}^{-k-1}$ and hence it is homotopic to $0$ and thus there is $$h^{(-k-2)}\in \Hom(\Lambda^\bullet\frh,\Lambda^{<\bullet}\frh)\otimes \Hom^{-k-2}$$ such that $[(D^{(k)})^2]_{-k-1}=[d_+,h^{(-k-2)}]_+$. The differential $D^{(k+1)}=D^{(k)}+h^{(-k-2)}$ provides the induction step.

By setting $\partial^-=\sum_{i} h^{(-i)}$ we complete our proof. ◻
:::

::: lemma
[]{#lem: uniq MF+eq label="lem: uniq MF+eq"} Let $(\calF_\bullet,d_\bullet^+)$ be an element of $\Com^{\frh,\ell}(\calZ)$ and $F\in \CC[\calZ]^H$ that satisfy conditions of the previous lemma. Suppose there two sets of differentials $d^-,\hat{d}^-: \calF_i\to \calF_j$, $\partial_{ij}^-,\hat{\partial}_{ij}: \Lambda^\bullet\frh\otimes\calF_i\to \Lambda^{<\bullet}\frh\otimes \calF_j$, $j>i$ such that $$[(\calF_\bullet, D+\partial+d^++d^-+d_{ce}+\partial^-)]_{per}, [(\calF_\bullet, D+\partial+d^++d_{ce}+\hat{d}^-+\hat{\partial}^-)]_{per}\in \MFs(\calZ,F)$$ then there is $\Psi=\sum_{i\le 0}\Psi_i$, $\Psi_{-i}\in \Hom^{-i}(\CE_\frh\odel \calF_\bullet,\CE_\frh\odel\calF_\bullet)$, $\Psi_0=\mathrm{Id}$, $\Psi_{-1}=0$,

such $$\Psi\circ (D+\partial+d^++d^-+d_{ce}+\partial^-)\circ \Psi^{-1}= D+\partial+d^++\hat{d}^-+d_{ce}+\hat{\partial}^-.$$
:::

::: proof
*Proof.* Let $d_0=D+\partial+d_{ce}$, $d_-=d^-+\partial^-$ and $D_{tot}=d^++d_0+d_-$, $\hat{d}_-=\hat{\partial}^-+\hat{d}^-$, $\hat{D}_{tot}=d^++d_0+\hat{d}_-$. Suppose we constructed $\Psi_{-i}\in \Hom^{-i}(\CE_\frh\odel \calF_\bullet,\CE_\frh\odel\calF_\bullet)$, $k>i\ge 0$ such that $\Psi^{(k)}:=\sum_{0\le i<k}\Psi_{-i}$ satisfies $$\hat{D}_{tot}-D^{(k)}_{tot}\in \Hom^{\ge -k+1},\quad  D^{(k)}_{tot}=\Psi^{(k)}\circ D_{tot}\circ (\Psi^{(k)})^{-1}.$$

Let us use notation $\Delta=-\hat{D}_{tot}+D^{(k)}_{tot}$ then we have $$0=(\hat{D}_{tot}+\Delta)^2-(\hat{D}_{tot})^2=[[\Delta]_{-k+1},d_+]_+  + [[\Delta]_{\le -k},d_+]_++[\Delta,d_0+\hat{d}_-]_++\Delta^2.$$ Since the first summand is from $\Hom^{-k+2}$ and the rest of summands are from $\Hom^{\le -k+1}$ we get that $[[\Delta]_{-k+1},d_+]_+=0$. Thus there is $\Psi_{-k}\in \Hom^{-k}$ such that $[\Delta]_{-k+1}=[d^+,\Psi_{-k}]$. The element $\Psi^{(k+1)}:=\Psi^{(k)}+\Psi_{-k}$ prove our inductive statement. ◻
:::
