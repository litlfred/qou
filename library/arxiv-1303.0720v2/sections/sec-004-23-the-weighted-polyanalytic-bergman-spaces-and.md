---
doc_id: arxiv-1303.0720v2
doc_title: "ASYMPTOTIC EXPANSION OF POLYANALYTIC BERGMAN KERNELS"
section_id: sec-004-23-the-weighted-polyanalytic-bergman-spaces-and
section_title: "The weighted polyanalytic Bergman spaces and kernels"
section_number: 2.3
pages: 2-4
source_pdf: 1303.0720v2.pdf
source_sha256: 389ab465e81a0667
toc_source: outline
text_source: latex
latex_prose_ratio: 0.968
latex_coverage_ratio: 0.952
doc_brief: "ASYMPTOTIC EXPANSION OF POLYANALYTIC BERGMAN KERNELS — We consider the q-analytic functions on a given planar domain Ω, square integrable with respect to a weight."
---
Given an integer $q=1,2,3,\ldots$, a continuous function $f:\Omega\to{\mathbb C}$ is said to be *$q$-analytic (or $q$-holomorphic) in $\Omega$* if it solves the partial differential equation $$\bar\partial_z^q f(z)=0,\qquad z\in\Omega,$$ in the sense of distribution theory. So the $1$-analytic functions are just the ordinary holomorphic functions. A function $f$ is said to be *polyanalytic* if it is $q$-analytic for some $q$; then the number $q-1$ is said to be the *polyanalytic degree* of $f$. By solving the $\bar\partial$-equation repeatedly, it is easy to see that $f$ is $q$-holomorphic if and only if it can be expressed in the form $$f(z)=f_1(z)+\bar zf_2(z)+\cdots+\bar z^{q-1}f_q(z) ,
\label{eq-Alm-1}$$ where each $f_j$ is holomorphic in $\Omega$, for $j=1,\ldots,q$. So the dependence on $\bar z$ is polynomial of degree at most $q-1$. We observe quickly that the vector-valued holomorphic function $$\mathbf{V}[f](z):=(f_1(z),f_2(z),\ldots,f_q(z)),$$ is in a one-to-one relation with the $q$-analytic function $f$. We will think of $\mathbf{V}[f](z)$ as a *column vector*. In a way, this means that we may think of a polyanalytic function as a vector-valued holomorphic function supplied with the additional structure of scalar point evaluations ${\mathbb C}^q\to{\mathbb C}$ given by $$(f_1(z),f_2(z),\ldots,f_q(z)) \mapsto 
f_1(z)+\bar zf_2(z)+\cdots+\bar z^{q-1}f_q(z).$$ We associate to $f$ not only the vector-valued holomorphic function $\mathbf{V}[f]$ but also the function of two complex variables $$\mathbf{E}[f](z,z')=f_1(z)+\bar z' f_2(z)+\cdots+(\bar z')^{q-1}f_q(z),
\label{eq-Alm-2}$$ which we call the *extension* of $f$. The function $\mathbf{E}[f](z,z')$ is holomorphic in $(z,\bar z')\in\Omega\times{\mathbb C}$, with polynomial dependence on $\bar z'$. To recover the function $f$, we just restrict to the diagonal: $$\mathbf{E}[f](z,z)=f(z),\qquad z\in\Omega.
\label{eq-Alm-3}$$ We observe here for the moment that $$\vert f(z)\vert^2=\mathbf{V}[f](z)^\ast\mathbf{A}(z) \mathbf{V}[f](z),
\label{expsq1}$$ where the asterisk indicates the adjoint, and $\mathbf{A}(z)$ is the singular $q\times q$ matrix $$\mathbf{A}(z)=
\begin{pmatrix}
1
&\cdots&
{\bar z}^{q-1}
\\
 \vdots & \ddots & \vdots  \\
z^{q-1}
&\cdots&
z^{q-1}\bar z^{q-1}
\end{pmatrix}
.
\label{eq-singmat1}$$ For some general background material on polyanalytic functions, we refer to the book [@balk].

As before, we let the weight $\omega:\Omega\to{\mathbb R}_+$ be continuous, and define $\mathrm{PA}^2_{q}(\Omega,\omega)$ to be the linear subspace of $L^2(\Omega,\omega)$ consisting of $q$-analytic functions in $\Omega$. Then $\mathrm{PA}^2_{1}(\Omega,\omega)=\mathrm{A}^2(\Omega,\omega)$, the usual weighted Bergman we encountered in Subsection [\[subsec-wB\]](#subsec-wB){reference-type="ref" reference="subsec-wB"}. For general $q=1,2,3,\ldots$, it is not difficult to show that point evaluations are locally uniformly bounded on $\mathrm{PA}^2_{q}(\Omega,\omega)$, and therefore, $\mathrm{PA}^2_{q}(\Omega,\omega)$ is a norm-closed subspace of $L^2(\Omega,\omega)$. We will refer to $\mathrm{PA}^2_{q}(\Omega,\omega)$ as a *weighted $q$-analytic Bergman space*, or as a *weighted polyanalytic Bergman space of degree $q-1$*. In view of [\[expsq1\]](#expsq1){reference-type="eqref" reference="expsq1"} and [\[eq-singmat1\]](#eq-singmat1){reference-type="eqref" reference="eq-singmat1"}, we may view $\mathrm{PA}^2_{q}(\Omega,\omega)$ as a space of vector-valued holomorphic functions on $\Omega$, supplied with the singular matrix-valued weight $\omega(z)\mathbf{A}(z)$.

If we let $\phi_1,\phi_2,\phi_3,\ldots$ be an orthonormal basis for $\mathrm{PA}^2_{q}(\Omega,\omega)$, we can form the *weighted polyanalytic Bergman kernel* $K_q=K_{q,\Omega,\omega}$ given by $$K_q(z,w):=\sum_{j=1}^{+\infty}\phi_j(z)\overline{\phi_j(w)},\qquad
(z,w)\in\Omega\times\Omega.
\label{eq-bk2}$$ As was the case with the weighted Bergman kernel, $K_q$ is independent of the choice of basis $\phi_j$, $j=1,2,3,\ldots$, and has the reproducing property $$f(w)=\langle f,K_q(\cdot,w)\rangle_{L^2(\Omega,\omega)},\qquad w\in\Omega,
\label{eq-reprprop2}$$ for all $f\in\mathrm{PA}_q^2(\Omega,\omega)$. Alongside with the kernel $K_q$, we should also be interested in its *lift* $$\mathbf{E}_{\otimes2}[K_q](z,z';w,w'):=
\sum_{j=1}^{+\infty}\mathbf{E}[\phi_j](z,z')\overline{\mathbf{E}[\phi_j](w,w')},
\qquad (z,z',w,w')\in\Omega\times{\mathbb C}\times\Omega\times{\mathbb C}.
\label{eq-bk3}$$ The lifted kernel $\mathbf{E}_{\otimes2}[K_q]$ is also independent of the choice of basis, just like the kernel $K_q$ itself. If $\mathrm{PA}^2_{q}(\Omega,\omega)$ would happen to be finite-dimensional, the above sums defining kernels should be replaced by sums ranging over a finite set of indices $j$.
