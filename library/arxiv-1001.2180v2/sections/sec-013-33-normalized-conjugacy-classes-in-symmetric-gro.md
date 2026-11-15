---
doc_id: arxiv-1001.2180v2
doc_title: "ASYMPTOTICS OF q-PLANCHEREL MEASURES"
section_id: sec-013-33-normalized-conjugacy-classes-in-symmetric-gro
section_title: "Normalized conjugacy classes in symmetric group algebras"
section_number: 3.3
pages: 10-10
source_pdf: 1001.2180v2.pdf
source_sha256: f4225d7b024940aa
toc_source: outline
text_source: latex
latex_prose_ratio: 0.972
latex_coverage_ratio: 1.0
doc_brief: "ASYMPTOTICS OF q-PLANCHEREL MEASURES — In this paper, we are interested in the asymptotic size of the rows and columns of a random Young diagram under a natural deformation of the Plancherel measure"
---
If $G$ is a group and $G^\vee$ a set indexing its irreducible representations, one has a ring isomorphism, called abstract Fourier transform, between the center of the group algebra and the algebra of functions on $G^\vee$: $$\begin{aligned}
    Z(\mathbb{C}G) &\stackrel{\sim}{\rightarrow} \mathcal{F}(G^\vee,\mathbb{C}) \\
    x &\mapsto \big( \lambda \mapsto \chi^\lambda(x) \big)
\end{aligned}$$ It is indeed a ring isomorphism because the element in $Z(\mathbb{C}G)$ acts, by Schur lemma, as an homothetic transformation on each irreducible representation.

In the case $G=\mathfrak{S}_n$, this means that a function on Young diagrams with $n$ boxes corresponds to an element of the center of the group algebra $\mathbb{C}\mathfrak{S}_n$. Thus a function $f$ on all Young diagrams can be seen as sequences of elements $(f_n)_{n \geq 1}$ with $f_n \in Z(\mathbb{C}\mathfrak{S}_n)$ for all $n$. In the case of the normalized characters $\varSigma_\rho$, this sequence has a very nice expression, see [@Sniady06]: $$\begin{aligned}
\left(\varSigma_{\rho_1,\rho_2,\ldots,\rho_r}\right)_n & = \sum_{\substack{a_{(i,j)} \in \left[\!\left[1,n \right]\!\right]\\ a_{i,j}\neq a_{(i,j)'}}} (a_{11},a_{12},\ldots,a_{1\rho_1})\,(a_{21},a_{22},\ldots,a_{2\rho_2})\,\cdots\,(a_{r1},a_{r2},\ldots,a_{r\rho_r}) \nonumber\\
\label{eq:sigma_alg} &= \sum_{\substack{\forall i,\,\,A_i \in \mathcal{A}(n,\,\rho_i)\\ \forall i\neq j,\,\,A_i\cap A_j=\emptyset}} C(A_1)\,C(A_2)\,\cdots \,C(A_r),
\end{aligned}$$ where $\mathcal{A}(n,k)$ is the set of $k$-arrangements of $\left[\!\left[1,n \right]\!\right]$ and $C(A)$ is the cycle corresponding to a sequence $A$ of distinct numbers. It is easy to check that these elements verify $$\forall \lambda \in \mathscr{Y}, \ \ \varSigma_\rho(\lambda)
=\chi^\lambda\big((\varSigma_\rho)_{|\lambda|}\big).$$ Hence, the element in equation ([\[eq:sigma_alg\]](#eq:sigma_alg){reference-type="ref" reference="eq:sigma_alg"}) corresponds to the function $\varSigma_\rho$ on Young diagrams *via* the abstract Fourier transform, so the notation is coherent. Moreover, formula [\[eq:sigma_alg\]](#eq:sigma_alg){reference-type="eqref" reference="eq:sigma_alg"} allows us to do computations for all $n$ simultaneously and in this case, we will forget the index $n$ (for example in next paragraph).
