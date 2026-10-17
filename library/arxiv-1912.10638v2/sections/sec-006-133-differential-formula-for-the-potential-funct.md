---
doc_id: arxiv-1912.10638v2
doc_title: "Asymptotics of some quantum invariants of the Whitehead chains"
section_id: sec-006-133-differential-formula-for-the-potential-funct
section_title: "Differential formula for the potential function and relation to hyperbolic geometry"
section_number: 1.3.3
pages: 5-7
source_pdf: 1912.10638v2.pdf
source_sha256: 612e44871d91d2e2
toc_source: outline
text_source: latex
latex_prose_ratio: 0.98
latex_coverage_ratio: 0.955
doc_brief: "Asymptotics of some quantum invariants of the Whitehead chains — In this paper, we study the asymptotics of the colored Jones polynomials of the Whitehead chains with one belt colored by M1 and all"
---
From the discussion in subsection [\[strate\]](#strate){reference-type="ref" reference="strate"}, we have already seen the importance of the potential function. Thus, it is necessary to have a better understanding about how the geometric information of a link complement is encoded in the potential function of the link. In the study of the asymptotics of the colored Jones polynomials, we discover the following formula satisfied by the potential function of the Whitehead link.

::: lemma
[]{#dformula label="dformula"} Write $z_k = x_k + i y_k$ for $k=1,2$. The real part of the potential function satisfies the following differential equation: $$\begin{aligned}
 \label{DF}
\Re \Phi^{+(s_1,s_2)}(z_1,z_2) = \frac{1}{2\pi} V^{+(s_1,s_2)}(z_1,z_2) + \sum_{k=1}^2 y_k \frac{\partial}{\partial y_k} \Re \Phi^{s_1,s_2}(z_1,z_2),
\end{aligned}$$ where $$\begin{aligned}
V^{+(s_1,s_2)}(z_1,z_2) 
&= D(e^{2\pi i(s_2-1) - 2\pi i z_1 - 2\pi i z_2}) - D(e^{2\pi i (s_2-1) - 2\pi i z_2}) + D(e^{2\pi i z_2}) \\
&\qquad - D(e^{2\pi i z_1 + 2\pi i z_2}) + D(e^{2\pi i z_1}) 
\end{aligned}$$ and $D(z)$ is the Bloch-Wigner function.
:::

This formula has two immediate consequences. First, from Theorem [\[mainthmWL\]](#mainthmWL){reference-type="ref" reference="mainthmWL"})1)a), there exists a family of critical point $\mathbf{z}^{+(s_1,s_2)}$ for the potential function $\Phi^{+(s_1,s_2)}(z_1,z_2)$ such that the critical point equations coincide with the hyperbolic gluing equations for a particular triangulation of the Whitehead link complement. In particular, at this crtical point, by definition we have $$\frac{\partial}{\partial y_k} \Re \Phi^{+(s_1,s_2)}(\mathbf{z}^{+(s_1,s_2)}) = 0
 \text{ for $k=1,2$.}$$ From this, using lemma above, we can see that the real part of the critical value of the potential function is the sum of the volume of the ideal tetrahedra which satisfy the hyperbolic gluing equations, i.e. the hyperbolic volume of the link complement.

Next, the formula relates the potential function to the theory of angle structures. Note that every points on the subset $$\mathfrak{A} = \left\{(z_1,z_2) \mid \im \frac{d}{dz_i} \Phi^{+(s_1,s_2)}(z_1,z_2) =  \frac{\partial}{\partial y_k} \Re \Phi^{\pm(s_1,s_2)}(z_1,z_2) = 0 \text{ for $k=1,2$}\right\}$$ satisfies the property that the sum of the angles around the vertices are $2\pi$. Therefore, $\mathfrak{A}$ is a subset of the space of angle structures and the potential function restricted on $\mathfrak{A}$ is exactly the volume function. In particular, by the theorem of angle structures, we know that the maximum point on $\mathfrak{A}$ is exactly the hyperbolic volume of the link complement.

Moreover, it is interesting to compare the differential formula ([\[DF\]](#DF){reference-type="ref" reference="DF"}) with the covolume function discussed in [@LY18]. Recall that every hyper-ideal tetrahedron is determined (up to isometry) by six dihedral angles $\{a_{ij}\}_{1\leq i <j \leq 4}$, where $a_{ij}$ is the dihedral angle between the faces $i$ and $j$. Let $l_{ij}$ be the length of the edge between the face $i$ and the face $j$. Then $a_{ij}$ and $l_{ij}$ uniquely determine each other. Moreover, the volume function $vol$ satisfies the Sch$\ddot{\text{a}}$lfi's formula: $$\frac{\partial vol}{\partial a_{ij}} = - \frac{l_{ij}}{2}$$ The Legendre transform of the volume function is called the covolume function $cov$, which is given by [@LY18] $$cov (l_{ij}) = vol(a_{ij}) + \sum_{i<j } l_{ij} \cdot \frac{a_{ij}}{2}$$ Note that by the Sch$\ddot{\text{a}}$lfi's formula, $$\frac{\partial cov}{\partial l_{ij}} = \sum_{i<j}  \frac{\partial vol}{\partial a_{ij}}\frac{\partial a_{ij}}{\partial l_{ij}} + \sum_{i<j} \frac{l_{ij}}{2}\frac{\partial a_{ij}}{\partial l_{ij}} + \frac{a_{ij}}{2} = \frac{a_{ij}}{2}$$ Thus, we have $$\begin{aligned}
\label{cov}
cov(l_{ij}) = vol(a_{ij}) + \sum_{i<j} l_{ij}\frac{\partial cov}{\partial l_{ij}} 
\end{aligned}$$ Now, given a triangulation $\{\Delta_1,\dots, \Delta_n\}$ of a 3-manifold $M$ with edge lengths $\{l^1_{ij},\dots,l^n_{ij}\}$, where we identify $l^a_{pq}$ with $l^b_{rs}$ whenever these two edges are glued together, we can define the covolume function $cov_M$ of $M$ to be $$\begin{aligned}
\label{cov2}
cov_M (l^1_{ij}, \dots, l^n_{ij}) = \sum_{k=1}^n cov_k (l_{ij}) = \sum_{k=1}^n vol_k(a_{ij}) + \sum_{i,j}  l_{ij} A_{ij}
\end{aligned}$$ where $A_{ij} = \frac{\partial cov_M}{\partial l_{ij}}$ is the sum of the dihedral angles around the edge $l_{ij}$. Equations ([\[DF\]](#DF){reference-type="ref" reference="DF"}), ([\[cov\]](#cov){reference-type="ref" reference="cov"}) and ([\[cov2\]](#cov2){reference-type="ref" reference="cov2"}) suggest that we should think of $y_k$ as some sort of 'length'. We hope that this formula will help us to understand the theory of potential function.

The final remark for this equation is that the proof of Lemma [\[DF\]](#DF){reference-type="ref" reference="DF"} is based on some basic properties of the dilogarithm function and the Lobachevsky function. In particular, by using the argument, one can show that the potential functions discussed in [@O52; @O6; @O7], and the potential functions in [@KO05; @CMY09] after the reparametrization $z \mapsto e^{2\pi i z}$, also satisfy the same type of differential formula.
