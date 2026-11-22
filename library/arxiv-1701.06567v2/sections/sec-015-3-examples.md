---
doc_id: arxiv-1701.06567v2
doc_title: "BPS spectra and 3-manifold invariants"
section_id: sec-015-3-examples
section_title: "Examples"
section_number: 3
pages: 27-29
source_pdf: 1701.06567v2.pdf
source_sha256: c1610b50f5a7e22c
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.969
latex_coverage_ratio: 0.994
doc_brief: "BPS spectra and 3-manifold invariants — We provide a physical deﬁnition of new homological invariants Ha(M3) of 3- manifolds (possibly, with knots) labeled by abelian ﬂat connections."
---
In this section, we present many examples, illustrating the general proposal outlined in the previous section. In particular, our goal is two-fold: first, we wish to use the proposed physics definition of the new homological invariants ${\mathcal H}_a[M_3]$ to compute them in many concrete examples, to the extent that one can start exploring the structure of the results and explicitly test the Conjectures [\[Conjecture1\]](#Conjecture1){reference-type="ref" reference="Conjecture1"} and [\[Conjecture2\]](#Conjecture2){reference-type="ref" reference="Conjecture2"}, which is our second goal. We start with the simplest three-manifold and gradually move to the study of more complex ones.

## ${M_3=S^3}$ {#sec:S3}

For $M_3=S^3$ and $G=U(N)$, the 3d ${\mathcal N}=2$ theory $T[S^3]$ is a 3d ${\mathcal N}=2$ Chern-Simons theory with gauge group $U(N)$ at level $1$ and an adjoint chiral multiplet $\phi$, whose R-charge is equal to 2 [@equivariant]. This theory is dual (the duality is usually referred to as the "duality appetizer" [@Jafferis:2011ns; @Kapustin:2011vz; @appetizer]) to a system of $N$ free chirals, making it simple to analyze. The R-charges of the free chirals are given by $R=2,4,\ldots, 2N$, and they have charges $1, 2,\ldots, N$ under the $U(1)_{\beta}$ flavor symmetry that rotates the original adjoint chiral $\phi$ by a phase.

As a result, the superconformal index of the theory $T[S^3]$ can be expressed a simple product, $${{\mathcal I}}_{U(N)}(q,t)=\prod_{i=1}^N\frac{(t^{-i}q^{1-i};q)_\infty}{(t^iq^i;q)_\infty},
    \label{Index-UN-free}$$ where, as usual, the $q$-Pochhammer symbol is defined as $$(z; q)_n = \prod_{j=0}^{n-1} (1-z q^j).$$ Since $H_1(S^3)=0$, there is only one homological block $\widehat{Z}_0(q,t)$, realized as the $S^1\times D^2$ partition function of the $N$ free chirals with Neumann boundary conditions, $$\widehat{Z}_0(q,t)=\prod_{i=1}^N\frac{1}{(t^iq^i;q)_\infty}.$$ In the terminology of [@Gukov:2016gkn] this is an *unreduced* homological block.[^1] In order to relate it to the WRT invariant of $S^3$ as in Conjecture [\[Conjecture1\]](#Conjecture1){reference-type="ref" reference="Conjecture1"}, before taking the unrefined limit $t\rightarrow 1$, one has to divide by the contribution of the Cartan components of the adjoint chiral $\phi$. The result looks like $$\widehat{Z}_0(q)=\left.{(tq;q)^N_\infty}\,\widehat{Z}_0(q,t)\right|_{t\rightarrow 1}=
\prod_{j=1}^{N-1}(1-q^j)^{N-j}.$$ In the case of $G=SU(2)$, the dual theory consists of just one free chiral multiplet with R-charge $4$ and $U(1)_{\beta}$ charge $2$, whose index is $${\mathcal I}_{SU(2)}(q,t)=\frac{(t^{-2}q^{-1};q)_\infty}{(t^2q^2;q)_\infty}.$$ and we have $$\widehat{Z}_0(q,t)=\frac{1}{(t^2q^2;q)_\infty},\qquad \widehat{Z}_0(q)=(1-q^2).$$ Using the standard prescription for extending the quantum dilogarithm outside $|q|<1$,[^2] $$(x;q^{-1})_\infty\propto \frac{1}{(xq;q)_\infty},
    \label{poch-cont}$$ we have, for $G=U(N)$,[^3] $$\widehat Z_0(1/q,1/t)=\prod_{i=1}^N\frac{1}{(t^{-i}q^{-i};1/q)_\infty}=
    \frac{1}{N!}\prod_{i=1}^N{(t^{-i}q^{1-i};q)_\infty}.
    \label{S3-anti-block}$$ We see that the superconformal index [\[Index-UN-free\]](#Index-UN-free){reference-type="eqref" reference="Index-UN-free"} indeed admits a factorization *à la* ([\[IndexRefDecomp\]](#IndexRefDecomp){reference-type="ref" reference="IndexRefDecomp"}), $${\mathcal I}(q,t)=|{\mathcal W}_0|\,\widehat{Z}_0(q,t)\widehat{Z}_0(q^{-1},t^{-1}),$$ with only one homological block in this case.

[^1]: Although the terminology "reduced" and "unreduced" here is very similar to the one used in knot homology, there is no direct connection.

[^2]: Note that this is not an ordinary analytic continuation. The latter actually does not exists because $|q|=1$ is a natural boundary.

[^3]: Note that there is an ambiguous overall constant in ([\[poch-cont\]](#poch-cont){reference-type="ref" reference="poch-cont"}). We fix it in ([\[S3-anti-block\]](#S3-anti-block){reference-type="ref" reference="S3-anti-block"}) by requiring that the unrefined quantities are related by the ordinary analytic continuation. Namely, $$\left.\widehat Z_0(1/q,1/t)\cdot(t^{-1}q^{-1};q^{-1})^N_\infty\right|_{t\rightarrow 1}=
    \left.\widehat Z_0(1/q,1/t)\cdot(1/t;q)^{-N}_\infty\right|_{t\rightarrow 1}=
    \widehat{Z}_0(1/q)=\prod_{j=1}^{N-1}(1-q^{-j})^{N-j}.$$
