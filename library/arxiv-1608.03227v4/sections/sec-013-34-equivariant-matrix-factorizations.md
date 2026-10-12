---
doc_id: arxiv-1608.03227v4
doc_title: "January 30, 2018"
section_id: sec-013-34-equivariant-matrix-factorizations
section_title: "Equivariant matrix factorizations"
section_number: 3.4
pages: 15-16
source_pdf: 1608.03227v4.pdf
source_sha256: c71128e9a6c35343
doc_brief: "January 30, 2018 — For each braid β ∈ Brn we construct a 2-periodic complex Sβ of quasi-coherent C∗ × C∗ - equivariant sheaves on the non-commutative nested Hilbert scheme Hilb f ree 1,n ."
text_source: latex
latex_prose_ratio: 0.902
latex_coverage_ratio: 0.906
---
We keep previous notations: $\calZ$ is an affine variety with $H$-action and $F\in \CC[\calZ]^\frh$. Define a category $\Mod_{\frh}$ whose objects are finite-dimensional $H$-representations $V$. Now define the category $\SymbolPrint{\MFs_\frh}(\calZ,F)$ whose objects are triples $(M,D,\partial)$ where $M=M^0\oplus M^1$ and $M^i=\CC[\calZ]\otimes V^i$, $V^i \in \Mod_{H}$, $\SymbolPrint{\partial}\in \oplus_{i>j} \Hom_{\CC[\calZ]}(\Lambda^i\frh\otimes M, \Lambda^j\frh\otimes M)$ and $D$ is an odd endomorphism $D\in \Hom_{\CC[\calZ]}(M,M)$ such that $$D^2=F,\quad \SymbolPrint{ D_{tot}}^2=F,\quad D_{tot}=D+d_{ce}+\partial,$$ where the total differential $D_{tot}$ is an endomorphism of $\CE_\frh\odel M$, that commutes with the $U(\frh)$-action.

Note that we do not impose the equivariance condition on the differential $D$ in our definition of matrix factorizations. On the other hand, if $\calF=(M,D)\in \MFs(\calZ,F)$ is a matrix factorization with $D$ that commutes with $\frh$-action on $M$ then $(M,D,0)\in \MFs_\frh(\calZ,F)$.

There is a natural forgetful functor $\MFs_\frh(\calZ,F)\to \MFs(\calZ,F)$ that forgets about the correction differentials: $$\calF=(M,D,\partial)\mapsto \SymbolPrint{\calF^\sharp}:=(M,D).$$

Given two $\frh$-equivariant matrix factorizations $\calF=(M,D,\partial)$, $\tilde{\calF}=(\tilde{M},\tilde{D},\tilde{\partial})$ the space of morphisms $\Hom(\calF,\tilde{\calF})$ consists of homotopy equivalence classes of elements $\Psi\in \Hom_{\CC[\calZ]}(\CE_\frh\odel M, \CE_\frh\odel \tilde{M})$ such that $\Psi\circ D_{tot}=\tilde{D}_{tot}\circ \Psi$ and $\Psi$ commutes with $U(\frh)$-action on $\CE_\frh\odel M$. Two map $\Psi,\Psi'\in \Hom(\calF,\tilde{\calF})$ are homotopy equivalent if there is $h\in  \Hom_{\CC[\calZ]}(\CE_\frh\odel M,\CE\frh\odel\tilde{M})$ such that $\Psi-\Psi'=\tilde{D}_{tot}\circ h+ h\circ D_{tot}$ and $h$ commutes with $U(h)$-action on $\CE_\frh\odel M$.

Given two $\frh$-equivariant matrix factorizations $\calF=(M,D,\partial)\in \MFs_\frh(\calZ,F)$ and $\tilde{\calF}=(\tilde{M},\tilde{D},\tilde{\partial})\in \MFs_\frh(\calZ,\tilde{F})$ $\calF\otimes\tilde{\calF}\in \MFs_\frh(\calZ,F+\tilde{F})$ as the equivariant matrix factorization $(M\otimes \tilde{M},D+\tilde{D},\partial+\tilde{\partial})$.
