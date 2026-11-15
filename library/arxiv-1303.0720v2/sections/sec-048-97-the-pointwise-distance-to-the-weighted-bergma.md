---
doc_id: arxiv-1303.0720v2
doc_title: "ASYMPTOTIC EXPANSION OF POLYANALYTIC BERGMAN KERNELS"
section_id: sec-048-97-the-pointwise-distance-to-the-weighted-bergma
section_title: "The pointwise distance to the weighted Bergman kernel"
section_number: 9.7
pages: 37-37
source_pdf: 1303.0720v2.pdf
source_sha256: 389ab465e81a0667
toc_source: outline
text_source: latex
latex_prose_ratio: 0.941
latex_coverage_ratio: 0.987
doc_brief: "ASYMPTOTIC EXPANSION OF POLYANALYTIC BERGMAN KERNELS — We consider the q-analytic functions on a given planar domain Ω, square integrable with respect to a weight."
---
Here, we apply the estimates [\[eq-9.2.8\]](#eq-9.2.8){reference-type="eqref" reference="eq-9.2.8"} and [\[eq-9.6.3\]](#eq-9.6.3){reference-type="eqref" reference="eq-9.6.3"} with the (basic) estimate [\[glob1\]](#glob1){reference-type="eqref" reference="glob1"}. As before, the integer $k$ is fixed.

::: thm
[]{#thm-9.3 label="thm-9.3"} Let $\Omega$ be a domain in ${\mathbb C}$ and suppose $Q:\Omega\to{\mathbb R}$ is $C^4$-smooth with both $\varDelta Q>0$ on $\Omega$ and $$\kappa:=\sup_{\Omega}\frac{1}{2\varDelta Q}\varDelta
\log\frac{1}{\varDelta Q}<+\infty.$$ Assume moreover that $Q$ has the properties (A:i)--(A:iv) (see Subsection [\[subsec-assQ\]](#subsec-assQ){reference-type="ref" reference="subsec-assQ"}) on the disk ${\mathbb D}(z_0,r)\subset\Omega$. We fix an integer $k\ge0$ and assume that the approximate local Bergman kernel $K_{2,m}^{\langle k\rangle}(z,w)=\Lfun^{\langle2,k\rangle}\mathrm{e}^{2mQ(z,w)}$ extends to a separately bianalytic function of the variables $(z,\bar w)$ in the small bidisk ${\mathbb D}(z_0,r)\times{\mathbb D}(z_0,r)$. Then, for $m\ge\max\{2\kappa,1\}$, we have that $$K_{2,m}(z,w)=K^{\langle k\rangle}_{2,m}(z,w)+\mathrm{O}(m^{-k}\mathrm{e}^{mQ(z)+mQ(w)}),\qquad
z,w\in{\mathbb D}(z_0,\tfrac13r),$$ where the implied constant depends only on the triple $(Q,z_0,r)$.
:::

This means that the approximate kernel $K_{2,m}^{\langle k\rangle}$ is close to the true kernel $K_{2,m}$ locally near $z_0$.

::: proof
*Proof of Theorem [\[thm-9.3\]](#thm-9.3){reference-type="ref" reference="thm-9.3"}.* Since $\chi_0(z)=1$ for $z\in{\mathbb D}(z_0,\frac23r)$, the assertion follows from [\[eq-9.2.8\]](#eq-9.2.8){reference-type="eqref" reference="eq-9.2.8"} and [\[eq-9.6.3\]](#eq-9.6.3){reference-type="eqref" reference="eq-9.6.3"} once we observe that exponential decay is faster than power decay. ◻
:::

::: proof
*Proof of Theorem [\[blowupthm\]](#blowupthm){reference-type="ref" reference="blowupthm"}.* We express $\Lfun^{\langle 2,0\rangle}=m^2\Lfun^2_0+m\Lfun_1^2$ using the formulae obtained for $\Lfun^2_j$ for $j=0,1$ (see Remark [\[rem-AA\]](#rem-AA){reference-type="ref" reference="rem-AA"}). We also use that $2\mathop{\mathrm{Re}}Q(z,w)-Q(w)-Q(z)=-|w-z|^2\varDelta Q(z)+\mathrm{O}(|z-w|^3)$. The assertion follows after a number of tedious computations based on Taylor's formula. ◻
:::

::: rem
We have already obtained $K^{\langle k\rangle}_{2,m}$ explicitly for $k\le1$ and the assumptions made on $K^{\langle k\rangle}_{2,m}$ in the theorem are clearly fulfilled then. We believe that they are fulfilled for all other values of $k$ as well.
:::
