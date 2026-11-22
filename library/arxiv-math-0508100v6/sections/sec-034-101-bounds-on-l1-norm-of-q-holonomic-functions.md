---
doc_id: arxiv-math-0508100v6
doc_title: "ASYMPTOTICS OF THE COLORED JONES FUNCTION OF A KNOT"
section_id: sec-034-101-bounds-on-l1-norm-of-q-holonomic-functions
section_title: "Bounds on l1-norm of q-holonomic functions"
section_number: 10.1
pages: 23-24
source_pdf: 0508100v6.pdf
source_sha256: 9cc100a86b40c336
toc_source: outline
text_source: latex
latex_prose_ratio: 0.943
latex_coverage_ratio: 0.965
doc_brief: "ASYMPTOTICS OF THE COLORED JONES FUNCTION OF A KNOT — To a knot in 3-space, one can associate a sequence of Laurent polynomials, whose nth term is the nth colored Jones polynomial."
---
\lbl{sub.qholo}


The main result of \cite{GL} is that for every knot $K$, the
functions $J_K$ and $H_K$ are $q$-holonomic. Recall that a sequence
$f:\BN\longto\BQ(q)$ is $q$-{\em holonomic} if satisfies a
$q$-{linear difference equation}. In other words, there exists a
natural number $d$ and polynomial $a_j(u,v) \in \BQ[u,v]$ for
$j=0,\dots,d$ with $a_d \neq 0$ such that for all $n \in \BN$ we
have:
\begin{equation}
\sum_{j=0}^d a_j(q^n,q) f_{n+j}(q)=0.
\label{e0001}
\end{equation}


In this section we observe that $q$-holonomic functions satisfy {\em
a priori} upper bounds on their degrees and (under an integrality
assumption) on their $l^1$-norm. As a simple corollary, we obtain
another proof of the  quadratic bounds in   Proposition \ref{21}, though not as explicit.




\begin{definition}
\lbl{eq.integral} We say that a sequence $f:\BN\longto\BZ[q^{\pm 1}]$
is $q$-{\em integral holonomic} if it satisfies an {\em
$q$-difference equation} as above with $a_d=1$.
\end{definition}


\begin{question}
\lbl{que.1}
Is it true that $J_K$ and $C_K$ are $q$-integral holonomic for every knot $K$?
\end{question}

For a partial answer, see \cite{GS}.


\begin{theorem}
\lbl{thm.L1bound}
$\mathrm{(a)}$
If $f:\BN\longto \BZ[q^{\pm 1}]$ is $q$-holonomic, then for all $n$ we have:
$$
\maxdeg(f_n)=O(n^2)   \qquad
\text{and} \qquad \mindeg(f_n) =O(n^2).
$$
\newline
$\mathrm{(b)}$ If $f$ is $q$-integral holonomic, then for all $n$ we have:
$$
||f_n||_1 \leq C^n
$$
for some constant $C$. In particular,

$$
\limsup_{n \to \infty} \frac{\log|f_n(e^{\a/n})|}{n}
\leq C_{\a}
$$
for all $\a \in \BC$.
\end{theorem}

In other words, integral $q$-holonomic functions grow at most
exponentially.


\begin{proof}
Suppose $f$ satisfies \eqref{e0001}.
It is easy to see that for every $a(u,v)\in \BQ[u,v]$, there exists a 
constant $C'$ such that $\deg_+(a(q^n,q)) < C' n $  for every $n \ge 1$. 
We choose such a common $C'$ for  all
$a_j(q^n,q)$, $j=0,1,\dots,d$, and, in addition,  $C' > \maxdeg f(n)$ for 
$n=0, 1,\dots,d$.

We will prove by induction on $n\ge 1 $ that $\maxdeg f(n) \leq C' n^2$.
By assumption, it is true for $n=1, \dots, d$. For $n \ge 1$,
Then, by induction we have:
\begin{eqnarray*}
\maxdeg  f_{n+d}(q) & = &
\maxdeg \Big(  a_d(q^n,q) \, f_{n+d}(q)\Big) - \maxdeg  a_d(q^n,q) \\
&=& \maxdeg  \left(-\sum_{j=0}^{d-1} a_j(q^n,q) f_{n+j}(q)\right)   - \maxdeg  
a_d(q^n,q) \\
&< & C'n + C'(n+d-1)^2 + C'n \le C'(n+d)^2.
\end{eqnarray*}
The second claim in (a) follows similarly.

For (b), let $c_j=||a_j(Q,q)||_1$ for $j=0, \dots, d-1$, and choose $C$
so that
\begin{itemize}
\item
$C^d \geq c_{d-1} C^{d-1} + \dots + c_0 C^0$, and
\item
$||f_n(q)||_1 \leq C^n$ for $n=0, \dots, d-1$.
\end{itemize}
Then, it is easy to see by induction that (b) holds for all $n$.
\end{proof}


\begin{remark}
\lbl{rem.holosharp}
It is easy to see that the bounds of Theorem \ref{thm.L1bound} are sharp.
For example,
consider the sequence $f_n(q)=(1+q)(1+q^2)\dots(1+q^n)$.
\end{remark}


 Theorem \ref{thm.L1bound} gives an alternative proof of the quadratic bounds for the degrees of the color Jones polynomial, though not as
 explicit as in
Proposition \ref{21}.  If Question
\ref{que.1} has a positive answer then Theorem \ref{thm.L1bound} also gives an alternative proof of Theorem \ref{thm.3}.
