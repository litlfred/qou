---
doc_id: arxiv-1701.06567v2
doc_title: "BPS spectra and 3-manifold invariants"
section_id: sec-010-26-further-refinement
section_title: "Further refinement"
section_number: 2.6
pages: 19-20
source_pdf: 1701.06567v2.pdf
source_sha256: c1610b50f5a7e22c
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.984
latex_coverage_ratio: 0.56
doc_brief: "BPS spectra and 3-manifold invariants — We provide a physical deﬁnition of new homological invariants Ha(M3) of 3- manifolds (possibly, with knots) labeled by abelian ﬂat connections."
---
As we discussed above, for Seifert 3-manifolds the theory $T[M_3]$ has an extra $U(1)_{\beta}$ flavor symmetry. In particular, this is the case for $M_3=L(p,1)$, which will serve as an important example to us later. This flavor symmetry in $T[M_3]$ results in the presence of an extra ${\mathbb Z}$-grading in homological invariants ${\mathcal H}_{D^2}$ and ${\mathcal H}_{S^2}$ considered in the previous sections and a possibility to consider the corresponding refined indices (equivariant Euler characteristics): $$\widehat{Z}_a(q;t)=\sum_{i\in {\mathbb Z}+\Delta_a,\atop j,\ell \in{\mathbb Z}}q^{i}t^{\ell}(-1)^j\dim{\mathcal H}^{i,j;\,\ell}_a,
    \label{BlockEuler}$$ and $${\mathcal I}(q;t)=\sum_{i,j,\ell\in{\mathbb Z}}q^{i}t^{\ell}(-1)^j\dim{\mathcal H}_{S^2}^{i,j;\,\ell}.$$ where, from the physics point of view, $\ell$ is the $U(1)_{\beta}$ charge. The refined indices obviously provide more information about the underlying vector spaces and, as we will see in examples, can be used sometimes to compute (conjecturally) the full homological invariants via the "homological-flavor locking" phenomenon that we will explain later.

The refined version of the factorization formula [\[IndexFactorization\]](#IndexFactorization){reference-type="eqref" reference="IndexFactorization"} reads $${\mathcal I}(q;t)=\sum_{a\,\in\, {\mathrm{Tor}\,}H_1(M_3,{\mathbb Z})/{\mathbb Z}_2}\, |{\mathcal W}_a|\widehat{Z}_a(q;t)\widehat{Z}_a(q^{-1};t^{-1}).
        \label{IndexRefDecomp}$$
