---
doc_id: arxiv-1608.03227v4
doc_title: "Knot homology and sheaves on the Hilbert scheme of points on the plane"
section_id: sec-017-37-equivariant-push-forward
section_title: "Equivariant push-forward"
section_number: 3.7
pages: 20-20
source_pdf: 1608.03227v4.pdf
source_sha256: c71128e9a6c35343
toc_source: outline
text_source: latex
latex_prose_ratio: 0.915
latex_coverage_ratio: 0.97
doc_brief: "Knot homology and sheaves on the Hilbert scheme of points on the plane — For each braid β ∈Brn we construct a 2-periodic complex Sβ of quasi-coherent C∗× C∗- equivariant sheaves on the"
---
[]{#ssec: eq push f label="ssec: eq push f"} Let $S=\CC[\calZ]$ and Lie algebra $\frh$ acts on $\calZ$. Let us assume that $R=S/I$ where $I=(f_1,\dots,f_n)$ and functions $f_i$ form a regular sequence in $S$ and $I$ is $\frh$-invariant. Let $\calZ_0=\mathrm{Spec}(R)$. The Koszul complex $K(I)=(\Lambda^\bullet W\otimes \CC[\calZ],d_K)$, $W=\CC^n$ is $\frh$-equivariant and has homologies only in degree $0$. Let $w\in R^\frh$ and $W\in S^\frh$ such that $W-w\in I$. Let us choose $\calF=(M,D,\partial)\in \MFs_\frh(\calZ_0,w)$, $M=S^k$ then we can construct a matrix factorization ${}^\frh j_*(\calF)\in \MFs_\frh(\calZ,W)$ in two steps.

*Step 1:* We apply method of subsection [\[ssec: noneq push f\]](#ssec: noneq push f){reference-type="ref" reference="ssec: noneq push f"} to construct $j_*(\calF)=(\tilde{M},\tilde{D}+d_K+d^-)\in \MFs(\calZ,W)$.

*Step 2 :* Use lemma [\[lem: ext MF+eq\]](#lem: ext MF+eq){reference-type="ref" reference="lem: ext MF+eq"} to construct $\partial^-$ such that $\tilde{\calF}:=(\tilde{M}, \tilde{D}+d_K+d^-,\partial^-+\partial)\in \MFs_\frh(\calZ,W)$. The element $\calF$ is defined up to isomorphism according to lemma [\[lem: uniq MF+eq\]](#lem: uniq MF+eq){reference-type="ref" reference="lem: uniq MF+eq"} and we set $j^*(\calF):=\tilde{\calF}$. To complete our construction of the functor: $$\label{eq: push f eq}
   j_*: \MFs_\frh(\calZ_0,w)\to \MFs_\frh(\calZ,W).$$ we still need to discuss the action of the functor on the space of morphisms and homotopies between the morphisms and that is done below.

Let $\calF=(M,D,\partial)$, $\tilde{\calF}=(\tilde{M},\tilde{D},\partial)\in \MFs_\frh (\calZ_0,w)$ and $\psi$ is the morphism between $\calF$ and $\tilde{\calF}$ in the category $\MFs_\frh(\calZ_0,w)$. Let us constrict $\calF'=(M',D',\partial')=j_*(\calF)$ and $\tilde{\calF}'=(\tilde{M}',\tilde{M}',\tilde{\partial}')=  j_*(\tilde{\calF})$ as above. The lemma [\[lem: ext mor\]](#lem: ext mor){reference-type="ref" reference="lem: ext mor"} implies that we extend it to the morphism $\Psi$ in $\MFs_\frh(\calZ,W)$. Indeed if we choose a extension $\tilde{\psi}\in \Hom_{\CC[\calZ]}(M,\tilde{M})$, of $\psi$ then $\tilde{\psi}$ satisfies the assumptions of the lemma [\[lem: ext mor\]](#lem: ext mor){reference-type="ref" reference="lem: ext mor"} and the lift $\Psi=\tilde{\psi}+\sum_{i>0}\tilde{\psi}_i$ exists. Moreover the second part of the lemma implies that the lift is unique up to the homotopy thus we have the map: $$j_*:  \Hom_{\MFs_\frh(\calZ_0,w)}(\calF,\tilde{\calF})\to    \Hom_{\MFs_\frh(\calZ_0,w)}(\calF',\tilde{\calF}').$$

Thus completed our construction of the functor of homotopic categories ([\[eq: push f eq\]](#eq: push f eq){reference-type="ref" reference="eq: push f eq"}).
