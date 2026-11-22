---
doc_id: arxiv-2111.06645v3
doc_title: "Knots, Perturbative Series and Quantum Modularity"
section_id: sec-030-72-the-j-matrix-for-the-5-2-knot
section_title: "The J-matrix for the 5_2 knot"
section_number: 7.2
pages: 54-55
source_pdf: 2111.06645v3.pdf
source_sha256: 2a4826bd1c2f0823
toc_source: outline
text_source: latex
latex_prose_ratio: 0.958
latex_coverage_ratio: 1.0
doc_brief: "Knots, Perturbative Series and Quantum Modularity — We introduce an invariant of a hyperbolic knot which is a map α 7→Φα(h) from Q/Z to matrices with entries in Q[[h]] and with rows and columns"
---
[]{#sub.52statesum label="sub.52statesum"}

In this subsection, we describe that analogues of the formulas just given for our second standard knot $5_2$, because as usual the figure 8 knot has such special properties that some of the interesting features are obscured.

The Kashaev invariant of the $5_2$ knot is given by $$\label{Kashaev.52}
 \mathcal J^{(5_2)}(q) =\sum_{m=0}^{\infty} \sum_{k=0}^m
q^{-(m+1)k} \frac{(q;q)_m^2}{\big(q^{-1};q^{-1}\big)_k} .$$ (See [@K97 equation 2.3].) This is manifestly an element of the Habiro ring. We generalize it to the two-parameter family of elements of the Habiro ring given by $$\label{52desc}
\mathcal H^{(0)}_{a,b}(q) =\sum_{m=0}^{\infty} \sum_{k=0}^m
q^{-(m+1)k + am+bk} \frac{(q;q)_m^2}{\big(q^{-1};q^{-1}\big)_k}, \qquad a,b \in \mathbb Z.$$ These again form a $q$-holonomic module in the sense of [@WZ], meaning that they satisfy recursions like [\[rec41\]](#rec41){reference-type="eqref" reference="rec41"} (though in this case more complicated, and omitted here) and hence generate a $\mathbb Q\big[q,q^{-1}\big]$-module of finite rank. Here the rank is 4 and the $q$-holonomic module is generated (as we expect to hold for every knot) by the first row of the matrix $\mathbf{J}$ of the knot, $$\begin{aligned}
 \mathcal{J}^{(0,0)}(q) &
 =- \mathcal H^{(0)}_{0,0}(q)+q^{-1} \mathcal H^{(0)}_{-1,0}(q)+\mathcal H^{(0)}_{0,-1}(q)=1 , \qquad
\mathcal{J}^{(0,1)}(q) =\mathcal H^{(0)}_{0,0}(q) , \\
\mathcal{J}^{(0,2)}(q) & =\mathcal H^{(0)}_{0,0}(q)  - q^{-1}\mathcal H^{(0)}_{-1,0}(q) , \qquad
\mathcal{J}^{(0,3)}(q) = 2\mathcal H^{(0)}_{0,0}(q)  - q^{-1} \mathcal H^{(0)}_{-1,0}(q)
+ \mathcal H^{(0)}_{-1,1}(q) .
\end{aligned}$$

Just as in the case of the $4_1$ knot, we find that the further three rows are given by the *same* linear combinations of three other two-parameter families $\mathcal H^{(i)}_{a,b}$ ($1\le i\le3$) of functions, i.e., we have $$\begin{aligned}
 \mathcal{J}^{(i,0)}(q) &
 = - \mathcal H^{(i)}_{0,0}(q)+ q^{-1}\mathcal H^{(i)}_{-1,0}(q) - \mathcal H^{(i)}_{0,-1}(q) ,\qquad
\mathcal{J}^{(i,1)}(q) =\mathcal H^{(i)}_{0,0}(q) , \\
\mathcal{J}^{(i,2)}(q) & =\mathcal H^{(i)}_{0,0}(q)  - q^{-1}\mathcal H^{(i)}_{-1,0}(q) , \qquad
\mathcal{J}^{(i,3)}(q) = 2\mathcal H^{(i)}_{0,0}(q)  - q^{-1} \mathcal H^{(i)}_{-1,0}(q)
+ \mathcal H^{(i)}_{-1,1}(q)
\end{aligned}$$ for $i=0,1,2,3$. The formulas for the functions for $i\ne0$, whose origin will be indicated in Section [\[sub.statesum\]](#sub.statesum){reference-type="ref" reference="sub.statesum"}, are of the same type as the corresponding ones for the $4_1$ knot (equation [\[Q41abcd\]](#Q41abcd){reference-type="eqref" reference="Q41abcd"}), though considerably more complicated, but are completely different from [\[52desc\]](#52desc){reference-type="eqref" reference="52desc"}, namely $$\label{52H}
\mathcal H_{a,b}^{(i)}(x) = \frac 1{c \sqrt{3\xi_i-2}}  \frac{\theta_{1,i}^{c-1}
 \mathcal D_{\zeta}(\zeta\theta_{1,i})^2}{\mathcal D_{\zeta}\big(\zeta^{-1} \theta_{2,i}^{-1}\big)}
\sum_{k,m \bmod c} \zeta^{-(k+1)m} \theta_{1,i}^{-m} \theta_{2,i}^{-k}
\frac{(\zeta \theta_{1,i};\zeta)_k^2 }{\big(\zeta^{-1}\theta_{2,i}^{-1};\zeta^{-1}\big)_m} ,$$ where $c=\mathrm{den}(x)$, $\zeta=\mathbf{e}(-x)$ and and are any choice of $c$-th roots of  and $\xi_{i}^{-2}$ and $\xi_1$ (resp., $\xi_2$, $\xi_3$) the complex root of the equation $\xi^3-\xi^2+1=0$ (as in Section [\[sub.p\]](#sub.p){reference-type="ref" reference="sub.p"}) with negative (resp., positive, zero) imaginary part. Here $\mathcal D_\zeta(x)$ is the renormalized version of the cyclic quantum dilogarithm $D_\zeta(x)$ defined for $q=\mathbf{e}(a/c)$ by $$\label{Dm}
\mathcal D_q(x) = {\rm e}^{-2 \pi {\rm i} s(a,c)/2} D_q(x)
= {\rm e}^{-2 \pi {\rm i} s(a,c)/2}
\exp \Biggl(\sum_{j=1}^{c-1} \frac{j}{c} \log\big(1-q^j x\big) \Biggr) ,$$ where $s(a,c)$ is the Dedekind sum (cf. [@HZ; @Rademacher]) and where the logarithm is the principal one away from the cut at the negative real axis and is defined on the cut as the average of the principal branches just above and just below. The cyclic quantum dilogarithm appears in the expansion of Faddeev's quantum dilogarithm at roots of unity (see, for example, [@GK:evaluation; @Kashaev:star]) and plays a key role in the definition of the near units associated to elements of the Bloch group [@CGZ].

It is worth mentioning that the formulas [\[Q41abcd\]](#Q41abcd){reference-type="eqref" reference="Q41abcd"} and [\[41holonomy12\]](#41holonomy12){reference-type="eqref" reference="41holonomy12"} for the $4_1$ knot can also be written in terms of the modified cyclic quantum dilogarithm $\mathcal D_q$, because can be rewritten as $\mathcal D_q(Z) \mathcal D_{q^{-1}}\big(Z^{-1}\big)$. In fact, we expect formulas of this type, involving multiplicative combinations of the $\mathcal D_q$'s corresponding to the combinations defining the element of the Bloch group of $F$ corresponding to the knot, to exist for all knots.
