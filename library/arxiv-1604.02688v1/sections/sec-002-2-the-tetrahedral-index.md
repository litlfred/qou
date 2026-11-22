---
doc_id: arxiv-1604.02688v1
doc_title: "THE 3D-INDEX AND NORMAL SURFACES"
section_id: sec-002-2-the-tetrahedral-index
section_title: "The tetrahedral index"
section_number: 2
pages: 4-5
source_pdf: 1604.02688v1.pdf
source_sha256: bdcafe379519287c
toc_source: outline
text_source: latex
latex_prose_ratio: 0.956
latex_coverage_ratio: 0.969
doc_brief: "THE 3D-INDEX AND NORMAL SURFACES — Dimofte, Gaiotto and Gukov introduced a powerful invariant, the 3D-index, associated to a suitable ideal triangulation of a 3-manifold with torus boundary"
---
The index for a triangulation is built up from the \emph{tetrahedron index}  
$\ID \colon \mathbb{Z}^2\rightarrow \mathbb{Z}[[q^\frac{1}{2}]]$, defined 
for $m,e \in \Z$ by
\be
\ID(m,e)(q)=\sum^{\infty}_{n=\max\{0,-e\}}(-1)^n 
\frac{q^{\frac{1}{2}n(n+1)-(n+\frac{1}{2}e)m}}{(q)_n(q)_{n+e}}
\label{ID_def}
\ee
where $(q)_n=\Pi_{i=1}^{n}(1-q^i)$ is the $q$-Pochhammer symbol 
(by convention $(q)_0=1$). The index coincides with the coefficients 
of $z^e$ in the generating function
\be
I(m,q,z)=\sum_{e \in \Z}  \ID(m,e)(q) z^e 
= \frac{(q^{-\frac{m}{2}+1} 
\, z^{-1};q)_\infty}{(q^{-\frac{m}{2}} \,z;q)_\infty}
\label{ID_gen_func}
\ee
where
\be
(z; q)_\infty = \prod_{n=0}^\infty (1- z q^n) .
\label{zq-Poch}
\ee
(see \cite{Gar}). It follows that for any fixed $q \in \C$ with $0 < |q|<1$,
 the product for $I(m,q,z)$ converges for all $z\in \C$ with $z\ne 0$, 
and defines a holomorphic function of $z$ in the annulus $0<|z|<1$
with Laurent series given  by $\sum_{e \in \Z}  \ID(m,e)(q) z^e$.

\medskip
A more symmetric version of the tetrahedral index was defined in \cite{GHRS}  
 for $a,b,c \in \Z$ by
\be
\JD(a,b,c)= (-q^{\frac{1}{2}})^{-b} \ID(b-c,a-b)
= (-q^{\frac{1}{2}})^{-c} \ID(c-a,b-c) = (-q^{\frac{1}{2}})^{-a} \ID(a-b,c-a).
\ee
Then $\JD(a,b,c)$ is \emph{invariant under all permutations of its 
arguments} $a,b,c$ and satisfies
\be
\JD(a,b,c) = (-q^{\frac{1}{2}})^{s} \JD(a+s,b+s,c+s)  
\text{ for all } s \in \Z.
\label{J_plus_tets}
\ee

In particular, if $a, b\ge 0$ then (\ref{ID_def}) gives 
\be
\JD(a,b,0) =\ID(-a,b) = q^{\frac{1}{2}ab} + \text{ higher order terms},
\label{min_j_deg}
\ee
and (\ref{J_plus_tets}) shows that, in general, the lowest degree term 
in $\JD(a,b,c)$ has $q$-degree 
\be
\deg \JD(a,b,c) = 
\frac{1}{2}\left( (a-m)(b-m) +(b-m)(c-m)+(c-m)(a-m) - m \right) 
\ee
and coefficient $(-1)^m$,  where $m=\min\{a,b,c\}$.

The tetrahedral index also satisfies many other interesting algebraic 
identities including the \emph{quadratic identity} 
\be
\label{eq.IDquadratic}
\sum_{e \in \BZ} \ID(m,e)\ID(m,e+c)q^e =\delta_{c,0},
\ee
the \emph{pentagon identity}
\begin{align}
\sum_{e_0 \in \BZ}
& q^{e_0} \ID(m_1,x_1+e_0)\ID(m_2,x_2+e_0)\ID(m_1+m_2,x_3+e_0)
\label{pent_eq} \\
&=q^{-x_3} \ID(m_1-x_2+x_3,x_1-x_3)\ID(m_2-x_1+x_3,x_2-x_3) ,\nonumber
\end{align}
and some important {\em recurrence relations}. 
(See \cite{Gar} for the details.)
