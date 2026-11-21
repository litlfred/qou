---
doc_id: arxiv-2203.17029v1
doc_title: "MODULAR q -HOLONOMIC MODULES"
section_id: sec-014-31-solutions
section_title: "Solutions"
section_number: 3.1
pages: 24-25
source_pdf: 2203.17029v1.pdf
source_sha256: 5557f7f272cb8a43
toc_source: outline
text_source: latex
latex_prose_ratio: 0.689
latex_coverage_ratio: 0.943
doc_brief: "MODULAR q-HOLONOMIC MODULES — We introduce the notion of modular q-holonomic modules whose fundamental matrices deﬁne a cocycle with improved analyticity properties and show that the generalised"
duplicate_of: "modularqholonomicmodules"
---
In this section we describe the solutions of the generalised $q$-hypergeometric
equation~\eqref{gener.qhyper}. Since that equation depends on parameters, it will
be convenient to consider the following system of equations
\be
\label{heine.equs}
\begin{aligned}
  \left(\prod_{j=0}^{r-1}(1-q^{-1}b_{j}\sigma_{t})-t\prod_{j=1}^{r}(1-a_{j}\sigma_{t})
  \right)f
  &=0\\
  \left(\sigma_{a_{i}}^{-1}-q^{-1}a_{i}\sigma_{t}\sigma_{a_{i}}^{-1}-(1-q^{-1}a_{i})
  \right)f
  &=0\\
  \left(1-q^{-1}b_{i}\sigma_{t}-(1-q^{-1}b_{i})\sigma_{b_{i}}^{-1}\right)f
  &=0\,.
\end{aligned}
\ee
The first equation describes the $q$-difference equation in $t$, namely Equation
~\eqref{gener.qhyper} whose Newton polygon shown in Figure~\ref{f.heine}.

\begin{figure}[!htpb]
\begin{center}
\begin{tikzpicture}[scale=0.8,baseline=-3]
\draw[<-,thick] (-1.5,0) -- (3.5,0);
\draw[->,thick] (5.5,0) -- (10.5,0);
\draw[<->,thick] (0,-1.5) -- (0,3.5);
\filldraw (0,0) circle (2pt);
\filldraw (0,2) circle (2pt);
\filldraw (2,0) circle (2pt);
\filldraw (2,2) circle (2pt);
\filldraw (7,0) circle (2pt);
\filldraw (7,2) circle (2pt);
\filldraw (9,0) circle (2pt);
\filldraw (9,2) circle (2pt);
\filldraw (4,1) circle (1pt);
\filldraw (4.5,1) circle (1pt);
\filldraw (5,1) circle (1pt);
\node at (1,2.4) {$g^{(a_{1}^{-1})}$};
\node at (8,2.4) {$g^{(a_{r}^{-1})}$};
\node at (1,-0.4) {$f^{(1)}$};
\node at (8,-0.4) {$f^{(qb_{r-1}^{-1})}$};
\draw (0,2) -- (3.5,2);
\draw (5.5,2) -- (9,2) -- (9,0);
\fill[blue,opacity=0.2] (0,0) -- (0,2) -- (3.5,2) -- (3.5,0) -- cycle;
\fill[blue,opacity=0.1] (3.5,0) -- (5.5,0) -- (5.5,2) -- (3.5,2) -- cycle;
\fill[blue,opacity=0.2] (5.5,0) -- (5.5,2) -- (9,2) -- (9,0) -- cycle;
\end{tikzpicture}
\caption{The Newton polygon of the first Equation~\eqref{heine.equs}.}
\label{f.heine}
\end{center}
\end{figure}

We see that there are no slopes of the Newton polygon and therefore all solutions
are determined by the top and bottom edges and their indicial polynomials. We will
normalise the solutions coming from the Frobenius algorithm so that they satisfy
the full system of Equations~\eqref{heine.equs}. The bottom edge of the Newton
polygon in Figure~\ref{f.heine} has indicial polynomial
\be
  (1-\rho)(1-q^{-1}b_{1}\rho)\dots(1-q^{-1}b_{r-1}\rho)=0\,.
\ee
The solutions corresponding to the roots are given by $f^{(q^{-1}b_{j})}$ in
Equation~\eqref{heine.bjsols}, with the convention that $b_0=q$. The top
edge of the Newton polygon in Figure~\ref{f.heine} has indicial polynomial
\be
  (1-a_{1}\rho)\dots(1-a_{r}\rho)=0\,.
\ee
The solutions corresponding to the roots are given by $g^{(a_{j}^{-1})}$ in
Equation~\eqref{heine.ajsols}. The companion matrix of Equation~\eqref{gener.qhyper}
is given by
\be
  A(t,a,b,q)
  =
  \begin{pmatrix}
    0 & 1  & \dots & 0\\
    : & : & \dots & :\\
    0 & 0 & \dots & 1\\
    -(-1)^{r}\frac{1-t}{e_{r}(b/q)-te_{r}(a)}
    & (-1)^{r}\frac{e_{1}(b/q)-te_{1}(a)}{e_{r}(b/q)-te_{r}(a)} & \dots
    & \frac{e_{r-1}(b/q)-te_{r-1}(a)}{e_{r}(b/q)-te_{r}(a)}
  \end{pmatrix}
\ee
where
\be
  e_{k}(x)
  =
  \sum_{1\leq j_{1}<\dots<j_{k}\leq r}x_{j_{1}}\dots x_{j_{k}}
  \ee are the elementary symmetric polynomials and so with $U$ and $V$ in
  Equation~\eqref{UVheine},
\be
  U(qt,a,b,q)
  =
  A(t,a,b,q)U(t,a,b,q)
  \quad\text{and}\quad
  V(qt,a,b,q)
  =
  A(t,a,b,q)V(t,a,b,q)\,.
\ee
