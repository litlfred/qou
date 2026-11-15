---
doc_id: arxiv-1608.03227v4
doc_title: "Knot homology and sheaves on the Hilbert scheme of points on the plane"
section_id: sec-074-143-glmn-homology-differential
section_title: "gl(m|n)-homology differential"
section_number: 14.3
pages: 80-81
source_pdf: 1608.03227v4.pdf
source_sha256: c71128e9a6c35343
toc_source: outline
text_source: latex
latex_prose_ratio: 0.939
latex_coverage_ratio: 0.98
doc_brief: "Knot homology and sheaves on the Hilbert scheme of points on the plane — For each braid β ∈Brn we construct a 2-periodic complex Sβ of quasi-coherent C∗× C∗- equivariant sheaves on the"
---
Recall that the vector bundle $\calB_n^\vee$ over $\widetilde{\Hilb}^{free}_{1,n}$ is a vector bundle with the fiber $V$ over the point $(X,Y,v)$ where $V=\CC^n$ and $v$ is the cyclic vector. Define a section $\varphi_{m|n}$ of $\calB_n^\vee$ with the value $X^mY^n v\in V$ at the fiber at the point $(X,Y,v)$. Contraction with this section $$i_{\varphi_{m|n}}: \Lambda^\bullet \calB_n\to \Lambda^{\bullet-1}\calB_n.$$

induces the differential $d_{m|n}: \bbS_\beta\otimes \Lambda^\bullet\calB_n\to \bbS_\beta\otimes \Lambda^{\bullet-1}\calB_n$, which

commutes with the Čech differential $d_c$, the Chevalley-Eilenberg differential $d_{ce}$, the equivariant correction differentials $\partial_l+\partial_r$ and the matrix factorization differential $D$. Thus we can define following homology $$\mathbb{H}_{m|n}(\beta)=(\oplus_{i=0}^n \bbS_\beta\otimes \Lambda^\bullet\calB_n, D_{tot}^{m|n}),\quad D_{tot}^{m|n}:=D+\partial_l+\partial_r+d_{ce}+d_{c}+d_{m|n}.$$ The homology $\mathbb{H}_{m|n}(\beta)$ is only doubly graded. In forthcoming paper we prove the following

::: theorem
[@OR] $\mathbb{H}_{m|n}(\beta)$ is an isotopy invariant of $L(\beta)$.
:::

The differential $d_{m|n}$ is very much in spirit of the conjectures in the papers [@ORS; @GGS] and thus we propose the conjecture:

::: conjecture
The homology $\mathbb{H}_{m|n}$ categorifies the quantum invariant of type $gl(m|n)$.
:::
