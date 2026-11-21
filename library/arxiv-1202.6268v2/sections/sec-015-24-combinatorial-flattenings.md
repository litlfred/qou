---
doc_id: arxiv-1202.6268v2
doc_title: "THE QUANTUM CONTENT OF THE GLUING EQUATIONS"
section_id: sec-015-24-combinatorial-flattenings
section_title: "Combinatorial flattenings"
section_number: 2.4
pages: 13-14
source_pdf: 1202.6268v2.pdf
source_sha256: 209af6ae25439050
toc_source: outline
text_source: latex
latex_prose_ratio: 0.839
latex_coverage_ratio: 0.915
doc_brief: "THE QUANTUM CONTENT OF THE GLUING EQUATIONS — The gluing equations of a cusped hyperbolic 3-manifold M are a system of polynomial equations in the shapes of an ideal triangulation T of M that"
---
[]{#sub.flat label="sub.flat"}

We now have all ingredients to define what is a combinatorial flattening.

::: definition
[]{#def.flattening label="def.flattening"} Given an ideal triangulation $\mathcal T$ of $M$, a *combinatorial flattening*

is a collection of $3N$ integers $(f_i,f_i',f_i'') \in \mathbb Z^3$ for $i=1,\dots,N$ that satisfy

$$\begin{equation} f_i+f_i'+f_i'' = 1\,,\qquad i=1,...,N\,, \label{flattrip}   \end{equation} 

  \begin{equation} \label{flatG} 
\sum_{i=1}^N \big(\mathbf{G}_{Ii}f_i+\mathbf{G}_{Ii}'f_i'+\mathbf{G}_{Ii}''f_i''\big) 
= \begin{cases} 2 & I=1,...,N \\
0 & I=N+1 \end{cases} \,.
  \end{equation}$$
:::

Note that if we eliminate $f'$ using Equation [\[flattrip\]](#flattrip){reference-type="eqref" reference="flattrip"}, a flattening is a pair of vectors $(f,f'') \in \mathbb Z^{2N}$ that satisfies

$$\label{flatAB} \mathbf A f+\mathbf B f'' = \nu\,.$$ Evidently, Equation [\[flatAB\]](#flatAB){reference-type="eqref" reference="flatAB"} is a system of linear Diophantine equations. Neumann proved in [@Neumann-combi Lem.6.1] that every ideal triangulation $\mathcal{T}$ has a flattening.

::: remark
[]{#rem.Nflattening label="rem.Nflattening"} Combinatorial flattenings should not be confused with the (geometric) flattenings of [@N Defn.3.1]. The latter flattenings are coherent choices of logarithms for the shape parameters $z,z',z''$ of a complex solution to the gluing equations. On the other hand, our combinatorial flattenings are independent of a solution to the gluing equations. In the rest of the paper, the term *flattening* will mean a *combinatorial flattening* in the sense of Definition [\[def.flattening\]](#def.flattening){reference-type="ref" reference="def.flattening"}.
:::
