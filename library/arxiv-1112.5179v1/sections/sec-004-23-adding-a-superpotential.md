---
doc_id: arxiv-1112.5179v1
doc_title: "3-Manifolds and 3d Indices"
section_id: sec-004-23-adding-a-superpotential
section_title: "Adding a superpotential"
section_number: 2.3
pages: 11-12
source_pdf: 1112.5179v1.pdf
source_sha256: b58af08336c40994
toc_source: outline
text_source: latex
latex_prose_ratio: 0.989
latex_coverage_ratio: 0.832
doc_brief: "3-Manifolds and 3d Indices — We identify a large class R of three-dimensional N = 2 superconformal ﬁeld the- ories."
---
[]{#sec:W label="sec:W"}

In the framework of [@DGG], another important operation on a 3d $\mathcal{N}=2$ SCFT $\mathcal{T}$ was the addition of a superpotential. The index is affected by superpotential terms in a simple fashion; one just has to drop, in an appropriate way, any flavor symmetry broken by the superpotential.

This has three basic consequences. To illustrate them, suppose that we add a superpotential $\mathcal{W}$ charged only under the first $U(1)$ of the flavor symmetry group $U(1)^N$; in other words, $\mathcal{W}$ has electric charge $c_\mathcal{W}= (1,0,...,0)$. Suppose that $\mathcal{W}$ also has R-charge $R_\mathcal{W}$. Then:

1.  In order for $\mathcal{W}$ not to break R-symmetry, its R-charge must equal 2. This requires an electric R-charge shift by $\alpha_e = (R_\mathcal{W}-2,0,...,0)$, so that $R_\mathcal{W}- \alpha_e\cdot c_\mathcal{W}=2$, thereby multiplying the index by $q^{(1-R_\mathcal{W}/2)e_1}$, where $e = (e_1,...,e_N)$.

2.  The theory cannot be coupled to flux for a broken flavor symmetry. Therefore, we must restrict $m=(0,m')$, where $m'=(m_2,...,m_N)$.

3.  The Hilbert space cannot be graded by the broken flavor charge, and states whose difference in charge is a multiple of $c_\mathcal{W}$ will now live in the same charge sector. This means that we must sum over $e_1$.

Altogether, we find that the addition of $\mathcal{W}$ amounts to

$$\mathcal{I}_\mathcal{T}(\gamma;q)\;\overset{+\mathcal{W}}{\longrightarrow}\; \mathcal{I}_{\mathcal{T}'}(\gamma';q) = \sum_{e_1\in {\mathbb Z}}q^{\big(1-\frac{R_\mathcal{W}}{2}\big)e_1} \mathcal{I}_\mathcal{T}(\gamma;q)\,\big|_{\,m_1=0}\,,$$

with a new reduced charge vector $\gamma' = (m',e') = (m_2,...,m_N,e_2,...,e_N)$.

In general, a superpotential might contain a sum of several operators $\mathcal{O}_i$, with general electric charges $c_i$ and R-charges $R_i$. We can add these operators one at a time, in any order. Each of them transforms the index as

$$\mathcal{I}_\mathcal{T}(\gamma;q)\;\overset{+\mathcal{O}_i}{\longrightarrow}\; \mathcal{I}_{\mathcal{T}'}(\gamma';q) = \sum_{n\in {\mathbb Z}} q^{\big(1-\frac{R_i}{2}\big)n}\mathcal{I}_\mathcal{T}(e+n\hspace{.04cm}c_i,m;q)\,\big|_{\,m\cdot c_i = 0}\,.$$

This can be thought of as a discrete version of a "symplectic quotient," with respect to a moment map $\langle c_i, m \rangle$. After adding all the operators $\mathcal{O}_i$, we will be left with a charge vector $\gamma'=(m',e')$ that obeys $m'\cdot c_i = 0$ and $e'\equiv e'+n_ic_i$  ($n_i\in {\mathbb Z}$), for all $i$.
