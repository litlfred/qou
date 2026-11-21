---
doc_id: arxiv-math-0606435v2
doc_title: "arXiv:math/0606435v2 [math.GT] 10 Oct 2007"
section_id: sec-035-761-3-braids
section_title: "3-braids"
section_number: 7.6.1
pages: 56-58
source_pdf: 0606435v2.pdf
source_sha256: 6dddaf838a19f0f5
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.995
latex_coverage_ratio: 0.963
doc_brief: "arXiv:math/0606435v2 [math.GT] 10 Oct 2007 — We show that 3-braid links with given (non-zero) Alexander or Jones polynomial are ﬁnitely many, and can be effectively determined."
---
The material in section \reference{SBurau} originated from
a question of S.~Kamada whether the Alexander polynomial
Mahler measure $M(\Dl)$ is bounded on closed 3-braids. 

\begin{defi}
For a Laurent polynomial $p\in\bZ[t^{\pm 1}]$, and $n\in\bN_+$,
we define the $n$-norm of $p$ by
\[
||p||_n\,:=\,\sqrt[n]{\sum_{k=-\infty}^{\infty}\bigl([p]_k\bigr)^n}\,,
\]
and its Mahler measure by
\[
M(p)\,:=\,\prod_{|t|\ge 1,\,p(t)=0}\,|t|\,.
\]
This is extended to $p\in\bZ[t^{\pm 1/2}]$ in the obvious way.
See \cite{SSW,CK}.
\end{defi}

Kamada's question is related to controlling $|V(t)|$ and $|\Dl(t)|$
for $t\in S^1$, since the 2-norm $||\,.\,||_2$ and the Mahler
measure $M$ of polynomials have circle integral formulas (see
\eqref{55'} and \eqref{Ji}). One
can thus ask whether $||\Dl\cdot W_n||_2$ is bounded for proper
$W_n\in \bZ[t,1/t]$, or (weaker) whether $M(\Dl)$ is bounded
(and similarly $M(V)$ and $||V\cdot W_n||_2$) for braid
index $\le n$.

For values of $t$ where $J_0$ is not definite, however, there
seems little one can say on the range (on closed 3-braids)
of $|V(t)|$ or $|\Dl(t)|$. Likely they are dense in $\bR_+$.



We can conclude boundedness properties in
special cases where the indefinite $J_0$ values of $t$ are
controllable. For example the following can be proved easily.
(Note that for polynomials with integer coefficients the properties
a set of polynomials to have bounded $2$-norms, or finitely many
distinct $2$-norms, are equivalent, and also equivalent to the same
two properties for the $1$-norm.)

\begin{prop}
The set
\[
\{\,||(1-t^{2n})\Dl_{\hat\bt}(t)||_2\,:\,
\bt\in B_{2n},\,\Dl_{\hat\bt}\in\bZ[t^{\pm n}]\,\}
\]
is finite for any $n\ge 2$.
\end{prop}

\proof We have 
\begin{eqn}\label{55'}
||X||_2^2\,=\,\int_{0}^{1}\,\big|\,X(e^{2\pi is})\,\big|^2\,ds\,.
\end{eqn}
If $\Dl\in\bZ[t^{\pm n}]$, then this integral for 
\[
X=\frac{(1-t^{2n})\Dl(t)}{1-t}=\det(1-\psi_{2n-1})
\]
is controlled from its part over $0<s<\ffrac{1}{2n}$, and
this in turn is controlled by the unitarity of $\psi_{2n-1}$.
To eliminate the denominator, observe that the norm in
\eqref{55'} is just the one in $L^2(S^1)$, and so
$||P\cdot Q||_2\le ||P||_2\cdot ||Q||_2$. \qed

However, in general a bound on the Mahler measure of
arbitrary polynomials of closed $n$-braids does not exist
even for $n=3$.

\begin{prop}
The Mahler measure of $\Dl$ and $V$ is unbounded on closed
3-braids.
\end{prop}

{\def\gm{g_{\min}'}
\proof In the following $x\le O(y)$ means $\limsup |x/y|<\infty$
(the limit following from the context), $x\ge O(y)$ means $\liminf
|x/y|>0$ and $x=O(y)$ means both $x\le O(y)$ and $x\ge O(y)$.
The quantities $C$ and $C'$ will stand for real constants, with
$C$ being positive. They are understood to be independent on the
indices of the terms in the formula they occur in, but
may vary between the various inequalities.

We consider the links $L_n$ given by the closed 3-braids
$(\sg_1\sg_2^{-1})^n$. Using the Burau matrix eigenvalues, we find
\[
V_n\,:=V(L_n)\,=\,t+\frac{1}{t}+e_-^n(t)+e_+^n(t)\,,
\]
where 
\[
e_{\pm}(t)\,=\,-\frac{t+1/t-1}{2}\,\pm
\sqrt{\left( \frac{t+1/t-1}{2} \right)^2-1 }\,.
\]
Similarly
\[
\Dl_n\,:=\,\Dl(L_n)\,=\,\frac{1}{t+1/t+1}\left(2-e_-^n(t)-e_+^n(t)
\right)\,.
\]
Now the Jensen integral gives
\begin{eqn}\label{Ji}
\log\,M(V_n)\,=\,\int_0^1\,\log\,|V_n(e^{2\pi is})|\,ds\,.
\end{eqn}
Since $V_n$ is reciprocal, it suffices to consider the integral
over $s\in[0,1/2]$. Herein, with $t = e^{2\pi is}$, for
$s\in (1/3,1/2]$, we have real $e_{\pm}(t)$, one with norm $>1$. So
\[
\int_{1/3}^{1/2}\,\log\,|V_n(e^{2\pi is})|\,ds\,\ge\,O(n)\,.
\]
We must argue about $s\in[0,1/3]$. In that case, $e_{\pm}(t)$
are conjugate complex numbers of unit norm. This implies that
the integrand is bounded above when $n\to\infty$, but our problem
is to show that it does not decrease too quickly with $n$.
The assignment (with $i=\sqrt{-1}$)
\[
t\,\longmapsto\,f(t)\,=\,-\frac{t+1/t-1}{2}\,+
i\sqrt{ 1-\left( \frac{t+1/t-1}{2} \right)^2 }\,
\]
maps $e^{2\pi i[0,1/3]}\to e^{2\pi i[1/6,1/2]}$, so
\[
\frac{1}{2\pi}\,\arg t\,\stackrel{g}{\longmapsto}\,
\frac{1}{2\pi}\,\arg f(t)
\]
is a map $g\,:\,[0,1/3]\to[1/6,1/2]$, which is
bijective and monotonous, and $C^1$ except in $t=1/3$
where $g'\to\infty$. In particular,
\[
\gm\,=\,\min\,\{\,g'(s)\,:\,s\in[0,1/3]\,\}\,>0\,.
\]
Now consider the functions 
\[
h(s)\,:=\,2\cos 2\pi ng(s)\quad\mbox{and}\quad
m(s)\,:=\,-2\cos 2\pi s
\]
for $s\in[0,1/3]$. The singularities of the Jensen integral \eqref{Ji}
correspond to the intersections of the graphs of $h$ and $m$.

If $n\gg \gm$, then all intersection points\footnote{For the rest
of the proof $i$ is used as an index rather than the complex unit.}
$s_i$ of the graphs of $h$ and $m$ have $|m'(s_i)|>|h'(s_i)|$. (Here
we use also that $m\ne h$ when $s=0$.) In particular, between two
critical points $x_i$ of $h$, it intersects $m$ at most once. So the
number $n'$ of intersections $s_i$ satisfies
\[
\left|\,n'-\frac{2}{3}n\,\right|\,\le\,O(1)\,,\mbox{\quad
and therefore\quad}\,n'=O(n)\,.
\]

Moreover, 
\begin{eqn}\label{20.5}
|m'(s_i)|-|h'(s_i)|\,\ge\,(2-|m(s_i)|)\,\cdot C\,,
\end{eqn}
for a constant $C$ independent on $i$ and $n$. Now when $n$
increases, the $s_i$ will concentrate around $s=\frac{1}{3}$,
but since $\gm>0$, for $s$ small, the $x_i$ will be at distance
$\ge O(\frac{1}{n})$. So
\begin{eqn}\label{20.6}
2-|m(x_i)|\ge C\cdot \frac{i^2}{n^2}
\end{eqn}
for a constant $C$ independent on $i$ and $n$. Then
if $s_1,\dots,s_{n'}$ are the $n'$ intersection points
of $h$ and $m$, we can estimate for values of $s$
between the critical points $x_i$ and $x_{i+1}$ of $h$
\def\tsi{\bigl(2-|m(s_i)|\bigr)}
\begin{eqn}\label{x5}
|m(s)-h(s)|\,\ge\,C\,\cdot \tsi\,\cdot |s-s_i|^2
\end{eqn}
for a number $C$ independent on $i$ and $s$. Inequality
\eqref{x5} follows because we can control the behaviour
of $|m(s)-h(s)|$ from \eqref{20.5} for $s$ around $s_i$,
and though $|m-h|$ decreases slightly around the endpoints
of the interval $[x_i,x_{i+1}]$, this decrease can be
controlled by \eqref{20.6}. So
\begin{eqn}\label{x4}
\int_{x_i}^{x_{i+1}}\,\log\,|\,m(s)-h(s)\,|\,ds\,\ge\,
(x_{i+1}-x_i)\Bigl(\,\log\,\tsi\,+\log C\,\Bigr)\,+\,
\,2\,\int_{x_i}^{x_{i+1}}\,\log |s-s_i|\,ds\,.
\end{eqn}
Since for small $i$ (when $2-|m(s_i)|$ is
small), the $x_i$ will be at distance $\ge O(\frac{1}{n})$, using
\eqref{20.6} and $m(s)\le 1$ when $0\le s\le \myfrac{1}{3}$ we have
\begin{eqn}\label{x2}
\sum_{i=1}^{n'}\,\Bigl|\,\log\,\tsi\,\Bigr|\,\le\,n'\cdot
\left(\,C\cdot\left|\int_{0}^{1}\log |x|\,dx\right|+C'\,\right)\,=
\,O(n)\,.
\end{eqn}

Let $d_i:=x_{i+1}-x_i$. Because of $\gm>0$, we have 
\begin{eqn}\label{63'}
\max_{i}\,d_i\,\le\,O(1/n)\,.
\end{eqn}
So, similarly as in \eqref{x2}
\begin{eqn}\label{x3}
\sum_{i=1}^{n'}\,\Bigl|\,d_i\,\log\,\tsi\,\Bigr|\,
\le O(1)\,.
\end{eqn}
Also, because of \eqref{63'} and $\int 1+\log x\ dx=x\cdot\log x+C$,
for $n$ large
\[
\left|\,\int_{x_i}^{x_{i+1}}\,\bigl(\,1+\log |s-s_i|\,\bigr)\,ds\,
\right|\,\le\,
-C\cdot d_i\cdot \left[\,\log d_i\,+\,C'\,\right]\,\le\,
\sqrt{d_i}\,\le\,O\left(\frac{1}{\sqrt{n}}\right)\,
\]
for some real number $C'$ independent on $i$ and $n$, and so
\[
\sum_{i=1}^{n'}\,\left|\,\int_{x_i}^{x_{i+1}}\,2\cdot
\log |s-s_i|\,ds\,\right|\,\le\,O(\sqrt{n})\,.
\]
This, \eqref{x3} and \eqref{x4} imply that for $s\in[0,1/3]$ the
(part of the) Jensen integral
\eqref{Ji} has a lower bound that behaves like $-O(\sqrt{n})$, so the
dominating part is for $s\in[1/3,1/2]$, and we are done for $V$.

For $\Dl$ the argument is similar. There $m(s)\equiv 2$, so
instead of \eqref{x5} we have for $s\in[x_i,x_{i+1}]$ the estimate
$|m(s)-h(s)|\ge |s-s_i|^2\cdot C\cdot \gm$, with the same further
reasoning.  \qed
}

\begin{rem}
Dan Silver pointed out that for the Alexander polynomial a proof
can be obtained (possibly more elegantly, but not immediately)
from the ideas in \cite{SW}.
\end{rem}
