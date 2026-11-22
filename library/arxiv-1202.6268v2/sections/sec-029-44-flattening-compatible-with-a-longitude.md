---
doc_id: arxiv-1202.6268v2
doc_title: "THE QUANTUM CONTENT OF THE GLUING EQUATIONS"
section_id: sec-029-44-flattening-compatible-with-a-longitude
section_title: "Flattening compatible with a longitude"
section_number: 4.4
pages: 25-26
source_pdf: 1202.6268v2.pdf
source_sha256: 209af6ae25439050
toc_source: outline
text_source: latex
latex_prose_ratio: 0.892
latex_coverage_ratio: 0.963
doc_brief: "THE QUANTUM CONTENT OF THE GLUING EQUATIONS — The gluing equations of a cusped hyperbolic 3-manifold M are a system of polynomial equations in the shapes of an ideal triangulation T of M that"
---
[]{#sec.uflat label="sec.uflat"}

In this section we define a restricted combinatorial flattening that is compatible with a longitude.

Recall what is a combinatorial flattening of an ideal triangulation $\mathcal{T}$ from Definition [\[def.flattening\]](#def.flattening){reference-type="ref" reference="def.flattening"}. Given a simple peripheral curve $\lambda$ on the boundary of $M$ that represents a longitude --- in particular, having intersection number one with the chosen meridian $\mu$ --- we can construct the sum of combinatorial edge parameters along $\lambda$, just as in Section [\[sec.glue\]](#sec.glue){reference-type="ref" reference="sec.glue"}. It takes the form

$$\lambda\;:\quad \sum_{i=1}^N \big( \mathbf G_{N+2,i}Z_i+\mathbf G_{N+2,i}'Z_i'
+\mathbf G_{N+2,i}''Z_i''\big)\,,$$

for integer vectors $\mathbf G_{N+1}$, $\mathbf G'_{N+2}$, $\mathbf G''_{N+2}$. Just as we obtained $\mathbf A$, $\mathbf B$, and $\nu$ from the edge and meridian equations (with or without deformation), we may also now define

$$\label{defCD} C_i = \frac12(\mathbf G_{N+2,i}-\mathbf G_{N+2,i}')\,,\quad
    D_i = \frac12(\mathbf G_{N+2,i}''-\mathbf G_{N+2,i}')\,,\quad \nu_\lambda = -\frac12\sum_{i=1}^N \mathbf G_{N+2,i}'\,.$$

::: definition
[]{#def.flattening.long label="def.flattening.long"} A combinatorial flattening $(f,f',f'')$ is compatible with a longitude if in addition to Equations [\[flattrip\]](#flattrip){reference-type="eqref" reference="flattrip"}--[\[flatG\]](#flatG){reference-type="eqref" reference="flatG"}, it also satisfies $$\label{flatGlon}
\mathbf G_{N+2,i}f+\mathbf G_{N+2,i}'f'+\mathbf G_{N+2,i}''f''=0 \,.$$ Equivalently, a combinatorial flattening compatible with the longitude is a vector $(f,f'') \in \mathbb Z^{2N}$ that satisfies

$$\label{uflat} \mathbf A f+\mathbf B f'' = \nu\,,\qquad C\cdot f+D\cdot f'' = \nu_\lambda\,,$$
:::

A combinatorial flattening compatible with a longitude always exists [@Neumann-combi Lem.6.1].

In the context of functions on the character variety, it is natural to deform the meridian gluing equation, and simultaneously to introduce a longitude gluing equation, in the form $$\begin{equation} \label{umerid}
\mu\;:\quad 
\sum_{i=1}^N \big( \mathbf G_{N+1,i}Z_i+\mathbf G_{N+1,i}'Z_i'
+\mathbf G_{N+1,i}''Z_i''\big)=2u
  \end{equation} 
  \begin{equation} 
\label{long}
\lambda\;:\quad \sum_{i=1}^N \big( \mathbf G_{N+2,i}Z_i+\mathbf G_{N+2,i}'Z_i'
+\mathbf G_{N+2,i}''Z_i''\big)=2v\,, 
  \end{equation}$$

for some complex parameters $u$ and $v$. Upon exponentiation, these equations reduce to the expected [\[uglue\]](#uglue){reference-type="eqref" reference="uglue"}--[\[uglueL\]](#uglueL){reference-type="eqref" reference="uglueL"} if

$$m^2 = e^{2u}\,,\qquad \ell^2 = e^{2v}\,.$$

(It is easy to show, following [@NZ], that $C$ and $D$ as defined by [\[uflat\]](#uflat){reference-type="eqref" reference="uflat"} are the correct exponents for the exponentiated longitude equation [\[uglueL\]](#uglueL){reference-type="eqref" reference="uglueL"}.) If $M$ is a knot complement and we want to lift from $PSL(2,\mathbb{C})$ to $SL(2,\mathbb{C})$ representations, we should take $m=e^u$ and $\ell=-e^v$ and divide [\[long\]](#long){reference-type="eqref" reference="long"} by two before exponentiating. This provides the correct way to take a square root of the exponentiated gluing equation, *cf.* [@Calegari].

The remarkable symplectic property of $\mathbf A$ and $\mathbf B$ may be extended to $C$ and $D$, even though in general $C$, $D$ are vectors of half-integers rather than integers. Namely, there exists a completion of $(\mathbf A\;\mathbf B)$ to a full symplectic matrix $\left(\begin{smallmatrix}\mathbf A & \mathbf B \\ \mathbf C & \mathbf D\end{smallmatrix}\right)$ such that the *bottom rows* of $\mathbf C$ and $\mathbf D$ are the vectors $C$ and $D$ [@NZ]. In particular, this means that

$$\mathbf A_N\cdot D-\mathbf B_N\cdot C = 1\,,$$

where $\mathbf A_N,\mathbf B_N$ are the bottom (meridian) rows of $\mathbf A,\mathbf B$.
