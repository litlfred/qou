---
doc_id: arxiv-1912.10638v2
doc_title: "Asymptotics of some quantum invariants of the Whitehead chains Ka Ho WONG"
section_id: sec-005-132-asymptotic-of-the-quantum-invariants-of-the
section_title: "Asymptotic of the quantum invariants of the Whitehead chains"
section_number: 1.3.2
pages: 5-7
source_pdf: 1912.10638v2.pdf
source_sha256: 612e44871d91d2e2
doc_brief: "Asymptotics of some quantum invariants of the Whitehead chains Ka Ho WONG — In this paper, we study the asymptotics of the colored Jones polynomials of the Whitehead chains with one belt colored by"
text_source: latex
latex_prose_ratio: 0.955
latex_coverage_ratio: 0.945
---
In the second part of this paper, we generalize the previous results on the Whitehead link to the Whitehead chains.

::: theorem
[]{#CJWNN label="CJWNN"} We have $$\begin{aligned}
\lim_{N\to \infty} \frac{2\pi}{N+\frac{1}{2}} \log| J_{\vec{N}} (W_{a,1,c,d}, e^{\frac{2\pi i}{N+\frac{1}{2}}})| 
= \operatorname{Vol}({\mathbb S}^3 \backslash W_{a,1,c,d})
\end{aligned}$$
:::

As a consequence, we can show that

::: corollary
[]{#TVW label="TVW"}For any $a\in {\mathbb Z}$, $b\geq 1$, $c,d \in {\mathbb N}$ with $c+d\geq 1$, Conjectures [\[tvGM\]](#tvGM){reference-type="ref" reference="tvGM"} is true for $TV_r({\mathbb S}^3\backslash W_{a,b,c,d})$.
:::

Moreover, if we colored the belt by $M_1$ and all the clasps by $M_2$ (see Figure [1](#W0120){reference-type="ref" reference="W0120"} for an example), we have the following result.

::: theorem
[]{#mainthmWa1c0 label="mainthmWa1c0"} There exists some $\delta>0$ such that for any $1-\delta < s_1,s_2 < 1$, we have $$\begin{aligned}
&\quad\lim_{N\to \infty} \frac{2\pi}{N+\frac{1}{2}} \log| J_{M_1, M_2} (W_{0,1,c,0}, e^{\frac{2\pi i}{N+\frac{1}{2}}})| \\
&= \operatorname{Vol}({\mathbb S}^3 \backslash W_{0,1,c,0} , u_1=2\pi i (1-s_1), v_2 = v_3 = \dots v_{c+1} = 4\pi i (1 - s_2))
\end{aligned}$$
:::

![the link $W_{0,1,2,0}$ with belt colored by $M_1$ and all other components colored by $M_2$](W1120){#W0120 width="0.65\\linewidth"}

Note that Theorem [\[mainthmWa1c0\]](#mainthmWa1c0){reference-type="ref" reference="mainthmWa1c0"} gives a positive answer to Conjecture [\[GVCHL\]](#GVCHL){reference-type="ref" reference="GVCHL"} for the sequence of colors $(M_1,M_2,\dots,M_2)$ with $s_2=1$.

### Differential formula for the potential function and relation to hyperbolic geometry

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
