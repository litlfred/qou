---
doc_id: arxiv-math-0411505v2
doc_title: "A NON-COMMUTATIVE FORMULA FOR THE COLORED JONES FUNCTION"
section_id: sec-012-7-sortings-and-multiplicities-of-flows
section_title: "Sortings and multiplicities of flows"
section_number: 7
pages: 12-13
source_pdf: 0411505v2.pdf
source_sha256: a38cec365e0a227e
toc_source: outline
text_source: latex
latex_prose_ratio: 0.91
latex_coverage_ratio: 0.928
doc_brief: "A NON-COMMUTATIVE FORMULA FOR THE COLORED JONES FUNCTION — The colored Jones function of a knot is a sequence of Laurent polynomials that encodes the Jones polynomial of a knot and its parallels."
---
\lbl{sec.categorifying}



\subsection{Sortings}
\lbl{sub.CAlex}

In this section we introduce one of our key tools, which is a categorification
of multiplicities of the flows on  $G_K$. Let $f$ be a flow on $G_K$. If $e$ 
is an edge of $G_K$
then we let $F(e)\subset F$ be the set of $f(e)$ copies of $e$; we choose
an {\em arbitrary} total order on each $F(e)$.

Let $F= \cup_{e\in E_K}F(e)$ and let $F_r\subset F$ consists of the union of 
$F(e)$, $e$ red.
Further let $F^+_r$ denote the subset of $F_r$ consisting of the red edges 
which leave a vertex with 
$+$ sign, and we let $f^+_r=|F^+_r|$. Analogously we define  $F^-_r, \dots $.

\begin{definition}
\lbl{def.conf}
Fix a flow $f$ on $G_K$. A {\em sorting} $C$ of $f$
is a function
$$
C : \text{Vertices}(G_K) \to 2^{F_r}
$$
such that 
\begin{itemize}
\item
$C_1$ is a collection of red edges that terminate in vertex $1$, of
cardinality $f(e^b_1)$.
\item
For each $2\leq i \leq r$,
$C_{i} \sub C_{i-1}\cup \{e\in F_r; e$ terminates in vertex $i\}$ 
of $f(e^b_i)$ elements.
\end{itemize}
Let $\C(f)$ denote the set of all sortings of $f$. 
\end{definition}


\begin{lemma}
\lbl{lem.conf1}
Every flow $f$ has $\mult(f)$ sortings.
\end{lemma}

\begin{proof}
Use that $\mult(f,r)=1$, $\{e\in F_r; e$ terminates in vertex $1\} 
=\{e\in F; e$ 
terminates in vertex $1\}$ and for each $2\leq i <r$, $\sum f(e): e$ terminates
at vertex $i$ equals $|C_{i-1}\cup \{e\in F_r; e$ terminates in vertex $i\}|$.
\end{proof}


\begin{definition}
\lbl{def.Ifn}
We define  $\I(f,n)=\{0,\dots,n-1\}^{F_r}$. 
If $v\in \I(f,n)$ then we define
$f^-_r(v)=\sum_{e\in F^-_r}v_e$ and we define $f^+_r(v)$ analogously. 
\end{definition}


\begin{definition}
\lbl{def.filled}
{\rm (a)}
Fix a flow $f$ on $G_K$ and a natural number $n$.
An {\em n-sorting of $f$ } is a pair
$P=(C,v)$ where $C\in \C(f)$ and $v\in \I(f,n)$. 
\newline
{\rm (b)} If $P=(C,v)$ is an n-sorting of $f$ 
then we define its weight $b(P)$ to be
$$
b(P)= t^{n(f^-_w-f^+_w)}
 (1-t)^{f^-_r}t^{f^-_r(v)}(1-t^{-1})^{f^+_r}t^{-(f^+_r)(n-1)+ f^+_r(v)}.     
$$
{\rm (c)}
Let $\C_n(f)$ denote the {\em set of all n-sortings of $f$}.
\end{definition}


The following lemma states that 
the n-sortings of $f$ categorify 
multiplicities and weights of flows.


\begin{lemma}
\lbl{lem.geomseries}
 For every flow $f$ on $G_K$ and every $n$
we have
$$
 \b(f)|_{t\to t^n} \mult(f)=
\sum_{P\in \C_n(f)} b(P).
$$
\end{lemma}

\begin{proof}
It follows by Lemma \ref{lem.conf1} that
$$
\sum_{P\in \CI(f,n)} b(P)= \mult(f) t^{n(f^-_b-f^+_b)}(1-t)^{f^-_r}
(1-t^{-1})^{f^+_r}
 \left(\sum_{v\in \I(f,n)}t^{f^-_r(v)}t^{-(f^+_r)(n-1)+ f^+_r(v)}\right)=
$$
by a simple rearrangement
$$
\mult(f) t^{n(f^-_b-f^+_b)}
 \left((1-t)^{f^-_r}\sum_{v\in \I(f,n)}t^{f^-_r(v)}\right)
\left((1-t^{-1})^{f^+_r}\sum_{v\in \I(f,n)}t^{-(f^+_r)(n-1)+ f^+_r(v)}\right)=
$$
by a {\em geometric series summation}
$$
 \b(f)|_{t\to t^n} \mult(f).
$$
\end{proof}
