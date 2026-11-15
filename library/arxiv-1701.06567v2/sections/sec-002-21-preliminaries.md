---
doc_id: arxiv-1701.06567v2
doc_title: "BPS spectra and 3-manifold invariants"
section_id: sec-002-21-preliminaries
section_title: "Preliminaries"
section_number: 2.1
pages: 6-7
source_pdf: 1701.06567v2.pdf
source_sha256: c1610b50f5a7e22c
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.849
latex_coverage_ratio: 0.973
doc_brief: "BPS spectra and 3-manifold invariants — We provide a physical deﬁnition of new homological invariants Ha(M3) of 3- manifolds (possibly, with knots) labeled by abelian ﬂat connections."
---
[]{#sec:preliminaries label="sec:preliminaries"}

Before we present a mathematically-friendly summary of our proposal and the physics behind it, we need to introduce some notations, especially those relevant to abelian flat connections that will be central in our discussion.

Consider a closed and connected 3-manifold $M_3$, with $\partial M_3=\emptyset$. In order to present the results in full generality, it will be useful to consider the linking pairing on the torsion part of $H_1(M_3,{\mathbb Z})$: $$\begin{array}{cccc}
        {\ell k}: & {\mathrm{Tor}\,}H_1(M_3)\otimes {\mathrm{Tor}\,}H_1(M_3) & \longrightarrow & {\mathbb Q}/{\mathbb Z}\\
        & [a]\otimes [b] & \longmapsto & {\#(a\cap b')}/{n} \\
    \end{array}$$ where $b'$ is a 2-chain such that $\partial b'=nb$ for an integer $n$. Such $b'$ and $n$ exist because $[b]$ is torsion. As usual, $\#(a\cap b')$ denotes the number of intersection points counted with signs determined by the orientation. Note that the linking form provides an isomorphism between ${\mathrm{Tor}\,}H_1(M_3)$ and its Pontryagin dual $({\mathrm{Tor}\,}H_1(M_3))^*\equiv\mathrm{Hom}({\mathrm{Tor}\,}H_1(M_3),U(1))$ via the pairing $e^{2\pi i{\ell k}(\cdot,\cdot)}$.

The ${\mathbb Z}_2$ Weyl group acts on the elements $a\in{\mathrm{Tor}\,}H_1(M_3,{\mathbb Z})$ via $a\mapsto -a$. The set of orbits is the set of connected components of abelian flat $SU(2)$ connections on $M_3$ (*i.e.*, connections in the image of $\rho: {\mathcal M}_\text{flat}\left(M_3,U(1)\right)\rightarrow {\mathcal M}_\text{flat}\left(M_3,SU(2)\right)$ from the embedding $U(1)\subset SU(2)$),[^1] $${\mathrm{Tor}\,}H_1(M_3,{\mathbb Z})/{\mathbb Z}_2 \; \cong \; \pi_0{\mathcal M}_\text{flat}^\text{ab}(M_3,SU(2)) \,.$$ It is also useful to introduce a shorthand notation for the stabilizer subgroup: $${\mathcal W}_a \; \equiv \; \text{Stab}_{{\mathbb Z}_2}(a) \; = \; \left\{
    \begin{array}{cl}
        {\mathbb Z}_2, & a=-a \,, \\
        1, & \text{otherwise\,.}
    \end{array}
    \right.$$

[^1]: It is in fact $\left({\mathrm{Tor}\,}H_1(M_3,{\mathbb Z})\right)^*/{\mathbb Z}_2$ that is canonically identified with components of abelian flat connections. However, as the distinction between ${\mathrm{Tor}\,}H_1(M_3,{\mathbb Z})$ and its dual is only important in section [\[sec:summaryConj\]](#sec:summaryConj){reference-type="ref" reference="sec:summaryConj"}, we will use the same set of labels $\{a, b, \ldots\}$ for elements in both groups.
