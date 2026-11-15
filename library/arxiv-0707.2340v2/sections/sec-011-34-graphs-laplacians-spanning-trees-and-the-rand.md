---
doc_id: arxiv-0707.2340v2
doc_title: "NEGATIVE DEPENDENCE AND THE GEOMETRY OF POLYNOMIALS"
section_id: sec-011-34-graphs-laplacians-spanning-trees-and-the-rand
section_title: "Graphs, Laplacians, Spanning Trees and the Random Cluster Model"
section_number: 3.4
pages: 18-20
source_pdf: 0707.2340v2.pdf
source_sha256: bf0f91277a5874ff
toc_source: outline
text_source: latex
latex_prose_ratio: 0.971
latex_coverage_ratio: 0.952
doc_brief: "NEGATIVE DEPENDENCE AND THE GEOMETRY OF POLYNOMIALS — We introduce the class of strongly Rayleigh probability measures by means of geometric properties of their generating polynomials that amount to"
---
\label{ss-trees}

Let $G=(V,E)$ be a graph with vertex set $V=[n]$ and edge set $E$. Associate 
to each edge $e \in E$ a variable $w_e$. If $e$ connects $i$ and $j$ let 
$A_e$ be the $n \times n$ positive semi-definite matrix with the $ii$-entry 
and 
the $jj$-entry equal to $1$, the $ij$-entry and $ji$-entry equal to $-1$, 
and all other entries equal to $0$. The {\em Laplacian}, $L(G)$,  of $G$ is 
defined by 
$$
L(G)= \sum_{e \in E}w_eA_e.
$$
Let
$$
f_G(z,w)= \det(L(G)+Z).
$$
Thus, by \eqref{pencil}, $f_G$ is a multi-affine real stable polynomial with 
non-negative coefficients.   
The Principal Minors Matrix-Tree Theorem (see, e.g., \cite{Chaiken}) says that 
$$
 f_G(z,w)= \sum_{F}z^{\roots(F)}w^{\edges(F)}, 
$$ 
where the sum is over all rooted spanning forests $F$ in $G$, $\roots(F) 
\subseteq V$ is the set of roots 
of $F$ and $\edges(F) \subseteq E$ is the set of edges used in $F$. 
Alternatively, we may write $f_G$ as 
$$
f_G(z,w)= \sum_{F} w^F \prod_{C \in \mathcal{C}(F)} (\sum_{j \in C}z_j),
$$
where $\mathcal{C}(F)$ is the partition of $V$ whose parts are the vertices 
in the maximal trees in $F$ and the sum is over all forests in $G$.  Since 
the class of stable polynomials is closed under differentiation and 
specialization of  variables at real values (see, e.g., \cite{BBS2}) we have 
that the {\em spanning tree polynomial} $T_G(w)= \sum_Tw^T$, where the sum is 
over all spanning trees, is real stable (which is widely known).  The 
corresponding probability measure is usually called the uniform random 
spanning tree measure and is consequently strongly Rayleigh. Now if 
$\ben$ denotes the vector of all ones as in \S \ref{s2-plet} then 
$$
f_G(\ben,w)= \sum_{F} \omega_G(F)w^F,
$$
where the sum is over all spanning forests (independent sets) in $G$ and 
 $\omega_G(F)$ is the product of the sizes of the connected components of 
$F$. In \cite[Conjecture~5.10]{W} Wagner conjectured that $f_G(\ben,w)$ is a 
Rayleigh polynomial. By the above discussion we have shown that more is 
actually true, namely:

\begin{theorem}\label{t-fg}
For any graph $G$ the polynomial $f_G(\ben,w)$ is real stable.
\end{theorem}

Let $G=(V,E)$ be a graph and let $q>0$ and $0 \leq p \leq 1$ be parameters. 
The {\em random cluster (RC) model}, see \cite{grimmett},  
is the measure $\mu$ on $2^E$ defined 
by 
$$
\mu(F) = \frac 1 {Z_{\text{RC}}} q^{k(F)}p^{|F|}(1-p)^{|E \setminus F|},  
\quad F \subseteq E, 
$$
where $k(F)$ is the number of connected components in the graph $(V,F)$ and 
$Z_{\text{RC}}$ is the appropriate normalizing factor.  
The uniform spanning tree measure can be obtained
from this model by letting $p\to 0$ and $q/p \to 0$, see 
\cite[Section 1.5]{grimmett}. If
$q\geq 1$, the
RC model satisfies PLC and is therefore positively associated. 
If $q\leq1$, NLC is
satisfied, but other negative correlation properties are largely a matter of
conjecture. 
We are interested in properties closed under external fields so we assume 
that $p=1/2$. The generating polynomial of $\mu$ is then a constant multiple 
of the multivariate Tutte polynomial (see \cite{sok}):
$$
Z_G(z,q)= \sum_{F \subseteq E}q^{k(F)}z^F, \quad z=(z_e)_{e\in E}.
$$

If $G=C_n, n \geq 3$, is a cycle and $E=[n]$, then  
$$
Z_G(z,q)= \prod_{j=1}^n(q+z_j) +(q-1)z_1\cdots z_n 
$$
and 
$$
\frac{\partial Z_G}{\partial z_1}\frac{\partial Z_G}{\partial
z_2}-Z_G\frac{\partial^2 Z_G}
{\partial z_1\partial z_2}=  q^2(1-q)\prod_{j=3}^n z_j(q+z_j),
$$
so in this case the RC measure is Rayleigh, but not strongly Rayleigh. 

If $G$ is a tree, then 
$$
Z_G(z,q)= q\prod_{e\in E}(q+z_e),
$$
so the RC model is strongly Rayleigh. 
We conclude that on a
general graph $G$, the RC model is strongly Rayleigh if and only if $G$ is 
acyclic.  

With the help of {\em Mathematica}$^\copyright$, the
third author has verified that the RC model is Rayleigh for all simple 
graphs with at most five vertices.
