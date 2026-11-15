---
doc_id: arxiv-1701.06567v2
doc_title: "BPS spectra and 3-manifold invariants"
section_id: sec-012-28-generalization-to-un
section_title: "Generalization to $U(N)$"
section_number: 2.8
pages: 21-22
source_pdf: 1701.06567v2.pdf
source_sha256: c1610b50f5a7e22c
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.951
latex_coverage_ratio: 0.99
doc_brief: "BPS spectra and 3-manifold invariants — We provide a physical deﬁnition of new homological invariants Ha(M3) of 3- manifolds (possibly, with knots) labeled by abelian ﬂat connections."
---
[]{#sec:higherrk label="sec:higherrk"}

For simplicity, in this paper we mostly consider Chern-Simons theory on $M_3$ with gauge group being $G=SU(2)$ and the 3d/3d dual theory $T[M_3;SU(2)]$. However, in principle, everything we say above and below for $SU(2)$ can be easily generalized to the $SU(N)$ or $U(N)$ case; there are no obstructions for that. In particular, the formulae appearing in Conjecture [\[Conjecture1\]](#Conjecture1){reference-type="ref" reference="Conjecture1"} generalize as follows for $G = U(N)$: $$Z_{U(N)_k}[M_3]=(i\sqrt{2k})^{N(b_1(M_3)-1)/2}\sum_{a\;\in \;({\mathrm{Tor}\,}H_1(M_3,{\mathbb Z}))^{N}/S_N}e^{\pi ik\,\sum_{i=1}^N{\ell k}(a_i,a_i)}\,Z_a(q),
\label{WRT-UN-decomp}$$ $$Z_a(q)=\sum_{b\;\in \;({\mathrm{Tor}\,}H_1(M_3,{\mathbb Z}))^{N}/S_N}e^{\pi ik\,\sum_{i=1}^N{\ell k}(a_i,a_i)}\,S_{ab}
    \, \left.\widehat{Z}_b(q)\right|_{q\rightarrow e^{\frac{2\pi i }{k}}},$$ $$S_{ab}=\frac{\sum_{\sigma\in S_N}e^{2\pi i \sum_{i=1}^N{\ell k}(a_i,b_{\sigma(i)})}}{|\mathrm{Stab}_{S_N}(a)|\cdot|{\mathrm{Tor}\,}H_1(M_3,{\mathbb Z})|^{N/2}},$$ $$\widehat{Z}_a(q)\in (N!)^{-c}\,q^{\Delta_a}{\mathbb Z}[[q]].$$ As before, using the linking pairing one can identify $({\mathrm{Tor}\,}H_1(M_3))^N/S_N$ with the set of connected components of abelian flat connections: $$\begin{gathered}
    ({\mathrm{Tor}\,}H_1(M_3))^N/S_N\stackrel{{\ell k}}{\cong}\, \mathrm{Hom}\left({\mathrm{Tor}\,}H_1(M_3),U(1)^N\right)/S_N
 \cong \pi_0{\mathcal M}_\text{flat}^\text{ab}(M_3,U(N))
\label{UN-ab-set}
\end{gathered}$$ where $S_N$ is the permutation group of a set with $N$ elements. The factorization formulae ([\[IndexRefDecomp\]](#IndexRefDecomp){reference-type="ref" reference="IndexRefDecomp"}) and ([\[Itop-decomp\]](#Itop-decomp){reference-type="ref" reference="Itop-decomp"}) generalize as follows $${\mathcal I}(q,t)\quad = \sum_{a\,\in\, ({\mathrm{Tor}\,}H_1(M_3,{\mathbb Z}))^N/S_N}\, |{\mathcal W}_a|\widehat{Z}_a(q,t)\widehat{Z}_a(q^{-1},t^{-1}),
\label{I-UN-decomp}$$ $${\mathcal I}_{\text{top}}(q,t) \quad =\sum_{a\,\in\, ({\mathrm{Tor}\,}H_1(M_3,{\mathbb Z}))^N/S_N}\, |{\mathcal W}_a|\widehat{Z}_a(q,t)\widehat{Z}_a(q^{-1},t),
\label{Itop-UN-decomp}$$ with $${\mathcal W}_a\equiv \text{Stab}_{S_N}(a).$$

Physically, there are several ways to understand the special role of abelian flat connections or, more generally, reducible flat connections for $G$ of higher rank. As we already mentioned in section [\[sec:summaryConj\]](#sec:summaryConj){reference-type="ref" reference="sec:summaryConj"}, from the viewpoint of quantum field theory (on fivebrane world-volume or its various reductions and limits) this follows directly from the resurgent analysis. On the other hand, by looking at the same system [\[CatGeom1\]](#CatGeom1){reference-type="eqref" reference="CatGeom1"} from the vantage point of the Calabi-Yau 3-fold, the set [\[UN-ab-set\]](#UN-ab-set){reference-type="eqref" reference="UN-ab-set"} which labels the new invariants $\widehat{Z}_a(q)$ and their categorification ${\mathcal H}_a[M_3]$ can be understood as charges of the BPS states or enumerative invariants of the Calabi-Yau 3-fold. We elaborate on this perspective in the following two subsections, expanding the web of dualities and interpretations.
