---
doc_id: arxiv-1701.06567v2
doc_title: "BPS spectra and 3-manifold invariants"
section_id: sec-009-25-superconformal-index-of-tm-3-and-its-factoriz
section_title: "Superconformal index of $T[M_3]$ and its factorization"
section_number: 2.5
pages: 18-19
source_pdf: 1701.06567v2.pdf
source_sha256: c1610b50f5a7e22c
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.693
latex_coverage_ratio: 0.828
doc_brief: "BPS spectra and 3-manifold invariants — We provide a physical deﬁnition of new homological invariants Ha(M3) of 3- manifolds (possibly, with knots) labeled by abelian ﬂat connections."
---
Although the new invariants $\widehat{Z}_a(q)$ and their categorification ${\mathcal H}_a[M_3]$ have a direct connection to the WRT invariant via ([\[WRT-decomposition\]](#WRT-decomposition){reference-type="ref" reference="WRT-decomposition"}), from the viewpoint of 3d ${\mathcal N}=2$ theory $T[M_3;SU(2)]$, it is not the most natural or simplest object to consider. The main reason is that, in principle, there are infinitely many possible boundary conditions that could be considered.[^1] Identifying the correct subset that appears in ([\[BlockD2S1\]](#BlockD2S1){reference-type="ref" reference="BlockD2S1"}) may be subtle, yet possible, as we shall see in concrete examples.

The more natural object is the superconformal index of $T[M_3]$ or, equivalently, the partition function on $S^2\times S^1$ with a certain supersymmetry preserving background: $${\mathcal I}(q) \; \equiv \; {\rm Tr}_{{\mathcal H}_{S^2}}(-1)^Fq^{R/2+J_3} \; = \; Z_{T[M_3]}(S^2\times_q S^1)$$ where ${\mathcal H}_{S^2}$ is the space of BPS states of 3d ${\mathcal N}=2$ SCFT $T[M_3]$ or, equivalently, $Q$-cohomology of all physical local operators, $F$ is the fermion number, $R$ is the generator of the $U(1)_R$ R-symmetry and $J_3$ is the Cartan generator of the $SO(3)$ isometry of $S^2$. By construction, this index has the desired integrality property[^2] and can be categorified, $${\mathcal H}_{S^2}=\bigoplus_{i,j}{\mathcal H}^{i,j}_{S^2} \,,\qquad {\mathcal I}(q)=\sum_{i,j\in{\mathbb Z}}q^{i}(-1)^j\dim{\mathcal H}_{S^2}^{i,j}\;\in {\mathbb Z}[[q]] \,.
    \label{IndexEuler}$$ Another advantage of ${\mathcal H}_{S^2}$ compared to ${\mathcal H}_{D^2}$ is that it has a natural ring structure which is given by multiplication of BPS operators. One of the statements of 3d/3d correspondence is that the partition function $Z_{T[M_3]}(S^2\times_q S^1)$ computes the partition function of complex Chern-Simons on $M_3$ with real part of the "level" being $0$ and analytically continued imaginary part $\propto \tau\equiv \log q/(2\pi i)$. Motivated by the topological/anti-topological fusion [@Cecotti:1991me] and its recent 3d incarnation [@Pasquetti:2011fj; @Beem:2012mb; @Cecotti:2013mba; @Blau:2016vfc], we would like to make the following conjecture:

::: conj
For $\widehat{Z}_a(q)$ as in Conjecture [\[Conjecture1\]](#Conjecture1){reference-type="ref" reference="Conjecture1"}, the following holds $${\mathcal I}(q)=\sum_{a\,\in\, {\mathrm{Tor}\,}H_1(M_3,{\mathbb Z})/{\mathbb Z}_2}\, |{\mathcal W}_a|\widehat{Z}_a(q)\widehat{Z}_a(q^{-1})
        \qquad \in{\mathbb Z}[[q]]
        \label{IndexFactorization}$$ where $\widehat{Z}_a(1/q)$ is an apropriate extension[^3] of $\widehat{Z}_a(q)$ to the region $|q|>1$. []{#Conjecture2 label="Conjecture2"}
:::

[^1]: If we understand the boundary condition as a coupling of the 3d theory to a 2d theory living on the boundary, then the infinite number of possibilities can be seen, for example, from the fact that we can always introduce a 2d theory decoupled from the bulk.

[^2]: For reasons similar to the ones described at the end of the previous section, in general a negative power of 2 can appear as an overall factor. We omit it in some generic formulas to avoid clutter and instead focus attention on the conceptual structure. As mentioned earlier and as we shall see in examples, the effect of such fractions on categorification can typically be traced to the existence of bosonic modes with zero $q$-grading.

[^3]: For a generic 3-manifold $M_3$, the analytic continuation of the series $\widehat{Z}_a(q)\in {\mathbb Z}[[q]]$ convergent in $|q|<1$ may not exist outside $|q|=1$, at least in the standard way. However, one possible way to define it for general $M_3$ is $$\widehat{Z}_a(q^{-1}) \; \equiv \; \left.\widehat{Z}_a(q)\right|_{M_3\rightarrow \overline{M}_3},$$ where $\overline{M}_3$ denotes $M_3$ with the reversed orientation. Note that therefore ${\mathcal I}(q)$, unlike $\widehat{Z}_a(q)$, is insensetive to the orientation.
