---
doc_id: arxiv-1208.1663v2
doc_title: "THE 3D INDEX OF AN IDEAL TRIANGULATION AND ANGLE STRUCTURES"
section_id: sec-000-1-introduction
section_title: "Introduction"
section_number: 1
pages: 2-3
source_pdf: 1208.1663v2.pdf
source_sha256: 87e94e429d58386c
toc_source: outline
text_source: latex
latex_prose_ratio: 0.971
latex_coverage_ratio: 0.985
doc_brief: "THE 3D INDEX OF AN IDEAL TRIANGULATION AND ANGLE STRUCTURES — The 3D index of Dimofte-Gaiotto-Gukov a partially deﬁned function on the set of ideal triangulations of 3-manifolds with r torii boundary"
---
[]{#sec.intro label="sec.intro"}

In a series of papers [@DGG1; @DGG2], Dimofte-Gaiotto-Gukov studied topological gauge theories using as input an ideal triangulation $\mathcal T$ of a 3-manifold $M$. These gauge theories

play an important role in

-   Chern-Simons perturbation theory (that fits well with the earlier work on quantum Riemann surfaces of [@D1] and the later work on the perturbative invariants of [@DG]),

-   categorification and Khovanov Homology, that fits with the earlier work [@Witten-fivebranes].

Although the gauge theory depends on the ideal triangulation $\mathcal T$, and the 3D index in general may not converge, physics predicts that the gauge theory ought to be a topological invariant of the underlying 3-manifold $M$. When $\partial M$ consists of $r$ torii, the low energy description of these gauge theories gives rise to a *partially* defined function $$\label{eq.ICT}
I: \{\text{ideal triangulations}\}


\longrightarrow\mathbb Z((q^{1/2}))^{\mathbb Z^r \times \mathbb Z^r}, \qquad \mathcal T\mapsto 
I_{\mathcal T}(m_1,\dots,m_r,e_1,\dots,e_r) \in \mathbb Z((q^{1/2}))$$ for integers $m_i$ and $e_i$, which is invariant under some *partial* 2-3 moves. The building block of the 3D index $I_{\mathcal T}$ is the *tetrahedron index $I_{\Delta}(m,e)(q) \in \mathbb Z[[q^{1/2}]]$* defined by [^1] $$\label{eq.ID}
I_{\Delta}(m,e)=\sum_{n=(-e)_+}^\infty (-1)^n \frac{q^{\frac{1}{2}n(n+1)
-\left(n+\frac{1}{2}e\right)m}}{(q)_n(q)_{n+e}}$$ where $$e_+=\max\{0,e\}$$ and $(q)_n=\prod_{i=1}^n (1-q^i)$. If we wish, we can sum in the above equation over the integers, with the understanding that $1/(q)_n=0$ for $n < 0$.

Roughly, the 3D index $I_{\mathcal T}$ of an ideal triangulation $\mathcal T$ is a sum over tuples of integers of a finite product of tetrahedron indices evaluated at some linear forms in the summation variables. Convergence of such sums is not obvious, and not always expected on physics grounds. For instance, the following sum $$\sum_{e \in \mathbb Z} I_{\Delta}(0,e) q^{v e}$$ converges in $\mathbb Z((q^{1/2}))$ if and only if $v >0$. This follows easily from the fact that the degree $\delta(e)$ of the summand is given by $$\delta(e)=e + \begin{cases} 0 & \text{if} \,\,  e \geq 0 \\
\frac{e^2}{2}-\frac{e}{2} & \text{if} \,\,  e \leq 0
\end{cases}$$ Our goal is to

-   prove that the 3D index $I_{\mathcal T}$ exists if and only if $\mathcal T$ admits an index structure (a generalization of a strict angle structure); see Theorem [\[thm.3\]](#thm.3){reference-type="ref" reference="thm.3"} below.

-   give a complete axiomatic definition of the tetrahedron index $I_{\Delta}$ focusing on the combinatorial and $q$-holonomic aspects; see Section [\[sec.axioms\]](#sec.axioms){reference-type="ref" reference="sec.axioms"}.

-   to show that the 3D index is invariant under $3 \to 2$ moves, but not in general under $2 \to 3$ moves, and give a necessary and sufficient criterion for invariance under $2 \leftrightarrow 3$ moves; see Section [\[sec.23\]](#sec.23){reference-type="ref" reference="sec.23"}.

[^1]: The variables $(m,e)$ are named after the magnetic and electric charges of [@DGG2].
