---
doc_id: arxiv-1303.5278v1
doc_title: "1-EFFICIENT TRIANGULATIONS AND THE INDEX OF A CUSPED HYPERBOLIC 3-MANIFOLD"
section_id: sec-008-41-the-tetrahedron-index-and-its-properties
section_title: "The tetrahedron index and its properties"
section_number: 4.1
pages: 16-17
source_pdf: 1303.5278v1.pdf
source_sha256: 92e417c93f8b883a
toc_source: outline
text_source: latex
latex_prose_ratio: 0.816
latex_coverage_ratio: 0.816
doc_brief: "1-EFFICIENT TRIANGULATIONS AND THE INDEX OF A CUSPED HYPERBOLIC 3-MANIFOLD — In this paper we will promote the 3D index of an ideal triangulation T of an oriented cusped 3-manifold M (a collection of"
duplicate_of: "topologicalinvariance3dindex"
---
In this section we review the definition and the identities satisfied by the tetrahedron index of [@DGG2]. For a detailed discussion, see [@Ga:index].

The building block of the index $I_{\mathcal{T}}$ of an ideal triangulation $\mathcal{T}$ is the *tetrahedron index $I_{\Delta}(m,e)(q) \in \mathbb Z[[q^{1/2}]]$* defined by $$\label{eq.ID}
I_{\Delta}(m,e)=\sum_{n=(-e)_+}^\infty (-1)^n \frac{q^{\frac{1}{2}n(n+1)
-\left(n+\frac{1}{2}e\right)m}}{(q)_n(q)_{n+e}}$$ where $$e_+=\max\{0,e\}$$ and $(q)_n=\prod_{i=1}^n (1-q^i)$. If we wish, we can sum in the above equation over the integers, with the understanding that $1/(q)_n=0$ for $n < 0$.

The tetrahedron index satisfies the following *linear* recursion relations $$\begin{equation} 
\label{eq.rec1}
 q^{\frac{e}{2}} I_{\Delta}(m + 1, e) + q^{-\frac{m}{2}} I_{\Delta}(m, e + 1) - I_{\Delta}(m, e)=0
  \end{equation} 
  \begin{equation} 
\label{eq.rec2} 
 q^{\frac{e}{2}} I_{\Delta}(m - 1, e) + q^{-\frac{m}{2}} I_{\Delta}(m, e - 1) - I_{\Delta}(m, e)=0
  \end{equation}$$ and $$\begin{equation} 
\label{eq.rec1a}
I_{\Delta}(m, e+1) + (q^{e + \frac{m}{2}} - q^{-\frac{m}{2}} - q^{\frac{m}{2}}) 
I_{\Delta}(m, e) + I_{\Delta}(m, e - 1)  = 0
  \end{equation} 
  \begin{equation} 
\label{eq.rec2a} 
I_{\Delta}(m+1, e) + (q^{- \frac{e}{2} - m} - q^{-\frac{e}{2}} - q^{\frac{e}{2}}) 
I_{\Delta}(m, e) +  I_{\Delta}(m - 1, e) =   0 
  \end{equation}$$ and the *duality* identity $$\label{eq.Z2}
I_{\Delta}(m,e)(q)=I_{\Delta}(-e,-m)$$ and the *triality* identity $$\label{eq.Z3}
I_{\Delta}(m,e)(q)=(-q^{\frac{1}{2}})^{-e}I_{\Delta}(e,-e-m)(q) \,
=(-q^{\frac{1}{2}})^m I_{\Delta}(-e-m,m)(q)$$ and the *pentagon* identity $$\label{eq.pentagon}
I_{\Delta}(m_1-e_2,e_1)I_{\Delta}(m_2-e_1,e_2)=\sum_{e_3 \in \mathbb Z}
q^{e_3} I_{\Delta}(m_1,e_1+e_3)I_{\Delta}(m_2,e_2+e_3)I_{\Delta}(m_1+m_2,e_3)\,,$$ and the *quadratic* identity $$\label{eq.IDquadratic}
\sum_{e \in \mathbb Z} I_{\Delta}(m,e)I_{\Delta}(m,e+c)q^e =\delta_{c,0}=
\left\{\begin{array}{l}
 1 \text{ if } c=0\\  
 0 \text{ if } c\neq0\\  
 \end{array}\right.$$ The above relations are valid for all integers $m,e,m_i,e_i,c$.
