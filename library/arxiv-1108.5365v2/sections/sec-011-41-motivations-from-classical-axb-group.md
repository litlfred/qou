---
doc_id: arxiv-1108.5365v2
doc_title: "Representation of the Quantum Plane, its Quantum Double and Harmonic Analysis on GL+_q(2,R)"
section_id: sec-011-41-motivations-from-classical-axb-group
section_title: "Motivations from classical ax+b group"
section_number: 4.1
pages: 23-23
source_pdf: 1108.5365v2.pdf
source_sha256: 000961ede2234231
toc_source: outline
text_source: latex
latex_prose_ratio: 0.956
latex_coverage_ratio: 0.967
doc_brief: "Representation of the Quantum Plane, its Quantum Double and Harmonic Analysis on GL+_q(2,R) — We give complete detail of the description of the GNS representation of the quantum plane A and its dual"
---
\label{sec:QPlane:ax+b}
Recall that the classical $ax+b$ group is the group $G$ of affine transformations on the real line $\R$, where $a>0$ and $b\in\R$, and they can be represented by a matrix of the form (we use the transposed version):
\Eq{g(a,b)=\veca{a&0\\b&1},}
where the multiplication is given by
\Eq{\label{ax+bprod} g(a_1,b_1)g(a_2,b_2)=\veca{a_1a_2&0\\b_1a_2+b_2&1}.}
We can then talk about the space $C_\oo(G)$ of functions on $G$ vanishing at infinity, and a dense subspace of functions $\cW_G$ of the form
\Eq{\cW_G=\{g(\log a)f(b): f,g\in \cW\sub L^2(\R)\},}
where $f,g\in \cW$ are the rapidly decaying functions defined in Definition \ref{WDef}. Then $C_\oo(G)$ is the sup-norm closure of $\cW_G$.

In the study of quantum plane, it is necessary to consider the semigroup $G_+$ of positive elements. Restricting $f(a,b)\in\cW_G$ to $b>0$, we can use the Mellin transform and express the functions as
\Eq{f(a,b)=\int_{\R+i0}\int_\R  F(s,t)a^{is}b^{it}dsdt.}
Since the function is continuous at $b=0$, it has at most $O(1)$ growth as $b\to 0^+$. Hence from Theorem \ref{MTpole}, we conclude that $F(s,t)$ is entire analytic with respect to $s$, and holomorphic on Im$(t)>0$. Furthermore, it has rapid decay in $s,t$ along the real direction, and can be analytically continued to Im$(t)\leq 0$. Moreover, since $f(a,b)$ is analytic at $b=0$, the analytic structure of $f(a,b)$ on $b$ is given by $\sum_{k=0}^\oo A_k b^k$ for some constants $A_k$. Hence $F(s,t)$ has possible simple poles at $t=-in, n=0,1,2,...$.

Finally according to the Parseval's Formula for Mellin transform, there is an $L^2$ norm on functions of $G_+$ given by
\Eq{\|f(a,b)\|^2 = \int_\R \int_\R|F(s,t+\frac{1}{2}i)|^2 dt ds}
induced from the Haar measure $\frac{da}{a} db$. However, it is no longer left invariant due to the lack of inverses.
