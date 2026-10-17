---
doc_id: arxiv-0905.0228v4
doc_title: "A CURIOUS q-ANALOGUE OF HERMITE POLYNOMIALS"
section_id: sec-002-3-the-rescaled-discrete-q-hermite-polynomials-ii
section_title: "The rescaled discrete q-Hermite polynomials II"
section_number: 3
pages: 7-12
source_pdf: 0905.0228v4.pdf
source_sha256: 1744545d0f210949
toc_source: outline
text_source: latex
latex_prose_ratio: 0.936
latex_coverage_ratio: 0.917
doc_brief: "A CURIOUS q-ANALOGUE OF HERMITE POLYNOMIALS — Two well-known q-Hermite polynomials are the continuous and discrete q-Hermite polynomials."
---
By definition \eqref{eq:H2} and \eqref{eq:ACR} we have 
\begin{align}
h_{n+1}(x,s;q)=q^nx h_n(x,s;q)-[n]_q s h_{n-1}(x,s;q).
\end{align}
We derive then
\begin{align}
h_n(x,s;q)&=q^{n\choose 2}\sqrt{s^n} \tilde h_n\left(\frac{x}{\sqrt{s}};q\right)\\
&=\sum_{k=0}^nq^{n-2k\choose 2}{n\brack 2k}[2k-1]_q!! (-s)^k x^{n-2k},
\end{align}
where $\tilde h_n(x;q)$ are the discrete $q$-Hermite polynomials II, see \eqref{eq:H2}.

Since ${\D}_q(fg)={\D}_q(f)g+f(qx){\D}_q(g)$ and ${\D}_q(x)=1$, we see that
$$
{\D}_q(h_{n+1}(x))=q^nx{\D}_q(h_n(x))+q^nh_n(qx)-[n]_qs{\D}_q(h_{n-1}(x)).
$$
We derive by induction on $n$ that
\begin{align}\label{eq:qdif}
{\D}_q h_n(x,s;q)=[n]_q h_{n-1}(qx,s;q).
\end{align}

The first terms of these polynomials are
$$
1,\quad x,\quad qx^2-s,\quad q^3x^3-s[3]_qx,\quad 
q^6x^4-s(q^5+q^4+2q^3+q^2+q)x^2+s^2[3]_q. 
$$
The following result shows that  the polynomials $h_n(x,s;q)$ are moments of some orthogonal polynomials.
\begin{thm}\label{thm4.4}
The generating function of  $h_n(x,s;q)$  has the  continued fraction expansion:
 $$
 \sum_{m\geq 0}h_n(x,s;q)t^n=\cfrac{1}{ 1 -b_0 t-
\cfrac{\la_1 t^2}{1 -b_1 t-
 \cfrac{\la_2t^2}{1 - b_2 t-
 \cfrac{\la_3t^2}{1 -
 \ddots}}}},
 $$
 with
\begin{align}\label{eq:parameter}
b_n=q^{n-1}(q^n+q^{n+1}-1)x\quad \text{and}\quad \la_n=-q^{n-1}[n]_q(s+q^{2n-2}(1-q)x^2).
\end{align}
\end{thm}
\begin{proof}
To prove this it suffices to show that the Stieltjes tableau \eqref{eq:stableau} is satisfied with 
$$
a(n,k)={n\brack k}h_{n-k}(q^kx,s;q).
$$
This is easily verified.
\end{proof}

This implies that their Hankel determinants are
\begin{align}
\det(h_{i+j}(x,s;q))_{i,j}^{n-1}=(-1)^{n\choose 2}q^{n\choose 3}\prod_{j=0}^{n-1}\left([j]_q! (s+q^{2j}(1-q)x^2)^{n-1-j}\right)
\end{align}
and 
\begin{align}
\frac{\det(h_{i+j+1}(x,s;q))_{i,j}^{n-1}}
{\det(h_{i+j}(x,s;q))_{i,j}^{n-1}}
=w(n),
\end{align}
where  $w(n)$ satisfies
$$
w(n+1)=q^{n-1}(q^n+q^{n+1}-1)xw(n)+q^{n-1}[n]_q (s+q^{2n-2}(1-q)x^2)w(n-1).
$$
It is easily verified that
\begin{align}
 w(n)=\sum_{k=0}^nq^{2{n-k\choose 2}}{n\brack 2k}[2k-1]_q!! s^k x^{n-2k}
\end{align}
satisfies the same recurrence with the same initial values.





\begin{lem} Let $L_n(x):=h_{n}(x,(1-q)s;q)$. Then 
\begin{align}\label{eq:basic}
s L_n(x)+xL_{n+1}(x)=(x^2+s)L_n(qx).
\end{align}
\end{lem}
\begin{proof} First we note that the constant terms of both sides of \eqref{eq:basic} are equal to $sL_n(0)$. So it suffices to 
show that the derivatives of the two sides are equal.  
Applying ${\D}_q$ to \eqref{eq:basic} and using \eqref{eq:qdif}  we obtain, after replacing $x$ by $x/q$,
$$
s[n]L_{n-1}(x)+xq[n-1]L_n(x)+L_{n+1}(x)=(x^2+s)q[n]L_{n-1}(qx).
$$
Since $L_{n+1}(x)=q^nxL_n(x)-(1-q^n)sL_{n-1}(x)$, we can rewrite the above equation as follows:
\begin{align}
sL_{n-1}(x)+xL_n(x)=(x^2+s)L_{n-1}(qx).
\end{align}
The proof is thus completed by induction on $n$.
\end{proof}

We shall prove the following Jacobi  continued fraction expansion for the 
generating function of $(x+(1-q)s{\D}_q)^n\cdot 1$. This is equivalent to Theorem~\ref{thm:main}.
\begin{thm} \label{thm:Hh} Let $T_n(x,s)=(x+(1-q)s{\D}_q)^n\cdot 1$. Then
\begin{align}
\sum_{n\geq 0} T_n(x,s) t^n=
\cfrac{1}{1-b_0 t-
\cfrac{\lambda_1 t^2}{1-b_1 t-
\cfrac{\lambda_2 t^2}{1-\ddots}}},
\end{align}
where the coefficients are 
\begin{equation}\label{eq:coeff} 
b_n=q^n x,\quad \text{for $n\geq 0$};\quad\text{and}\quad  
\lambda_n=(1-q^n) s,\quad \text{for $n\geq 1$}.
\end{equation}
\end{thm}
\begin{proof}
Since $T_n(x,s)=(x+(1-q)s{\D}_q) T_{n-1}(x,s)$, we have
$$
T_n(x,s)=(x+\frac{s}{x})T_{n-1}(x,s)-\frac{s}{x}T_{n-1}(qx,s).
$$
Equivalently the generating function
$G(x,t)=\sum_{n\geq 0}T_n(x,s)t^n$ satisfies
the functional equation:
\begin{equation}\label{func-eq}
\left(1-\frac{x^2+s}{x}t\right)G(x,t)=1-\frac{s}{x}tG(qx,t).
\end{equation}
Suppose that
\begin{align}\label{eq:cfstieltjes}
G(x,t)=\cfrac{1}{ 1 -
\cfrac{c_1t}{1 -
 \cfrac{c_2t}{1 - 
 \cfrac{c_3t}{1 -
 \ddots}}}},
 \end{align}
where  $c_n=(g_n-1)g_{n-1}A$ with $A:=A(x)=-\frac{x^2+s}{x}$ and $g_i:=g_i(x)$. 

Substituting \eqref{eq:cfstieltjes} in \eqref{func-eq}  and then replacing $t$ by $t/A$  we obtain
\begin{align}
{1+t\over \displaystyle 1 -{(g_1-1)t\over
\displaystyle 1 - {(g_2-1)g_1t\over
\displaystyle 1 - {(g_3-1)g_2t\over
\displaystyle 1 - {(g_4-1)g_3t\over
\displaystyle 1 - \ldots}}}}}
=1 +{\frac{s}{x^2+s}t\over
\displaystyle 1 - {(g_1'-1)\frac{A'}{A}t\over
\displaystyle 1 - {(g_2'-1)g_1'\frac{A'}{A}t\over
\displaystyle 1 - {(g_3'-1)g_2'\frac{A'}{A}t\over
\displaystyle 1 - \ldots}}}},
\end{align}
where $A':=A(qx)$ and $g_i':=g_i(qx)$.
Comparing this with  Wall's formula (see \cite{KZ}):
\begin{align}
{1+z\over \displaystyle 1 -{(g_1-1)z\over
\displaystyle 1 - {(g_2-1)g_1z\over
\displaystyle 1 - {(g_3-1)g_2z\over
\displaystyle 1 - {(g_4-1)g_3z\over
\displaystyle 1 - \ldots}}}}}
=1 +{g_1z\over
\displaystyle 1 - {(g_1-1)g_2z\over
\displaystyle 1 - {(g_2-1)g_3z\over
\displaystyle 1 - {(g_3-1)g_4z\over
\displaystyle 1 - \ldots}}}},
\end{align}
we derive that $g_0=1$ and for $n\geq 1$, 
\begin{equation}\label{eq1}\left\{\begin{split}
g_{2n}&=\frac{A'}{A}\,\frac{g_{2n-1}'-1}{g_{2n-1}-1}\,g_{2n-2}',\\
g_{2n+1}&=\frac{A'}{A}\,\frac{g_{2n}'-1}{g_{2n}-1}\,g_{2n-1}'.
\end{split}\right.
\end{equation}

For example,
\begin{align*}
g_1&=\frac{s}{x^2+s},\quad 
&g_3&=\frac{A'}{A}\frac{g_2'-1}{g_2-1}g_1'=\frac{s}{x^2+s}\frac{1}{q},\\
g_2&=\frac{A'}{A}\frac{g_1'-1}{g_1-1}=q,\quad
&g_4&=\frac{A'}{A}\frac{g_3'-1}{g_3-1}g_2'={\frac {-s+qs+{q}^{3}{x}^{2}}{-s+qs+q{x}^{2}}}.
\end{align*}
In general we have the following result.
\begin{equation}\label{keystep}\left\{\begin{split}
g_{2n}&=\frac{sL_n(x)+xL_{n+1}(x)}{(x^2+s)L_{n}(x)},\\
g_{2n+1}&=\frac{s L_{n}(x)} {sL_{n}(x)+xL_{n+1}(x)}.
\end{split}\right.\qquad (n\geq 0).
\end{equation}
This can be verified by induction on $n$.  Suppose that the formula~\eqref{keystep}  is true for $n\geq 0$. 
We prove that the formula holds for $n+1$. By \eqref{eq1} we have
\begin{align*}
g_{2n+2}=\frac{A'}{A}\,\frac{g_{2n+1}'-1}{g_{2n+1}-1}\,g_{2n}'
=\frac{s L_n(x)+xL_{n+1}(x)}{(x^2+s)L_{n+1}(x)}\, \frac{L_{n+1}(qx)}{L_n(qx)}.
\end{align*}
It follows from Lemma 1 that 
\begin{align}\label{eq:induction}
g_{2n+2}=\frac{s L_{n+1}(x)+xL_{n+2}(x)}{(x^2+s)L_{n+1}(x)}.
\end{align}
Since 
\begin{align}\label{eq:l1}
L_{n+1}(x)-xL_n(x)=(q^n-1)(xL_n(x)+sL_{n-1}(x)),
\end{align}
the  verification for   $g_{2n+3}$ is then straightforward.
We  derive  from \eqref{eq:cfstieltjes} and \eqref{keystep} that
\begin{equation}\label{eq:coeff} 
\left\{\begin{split}
c_{2n}&=(g_{2n}-1)g_{2n-1}A=(1-q^n)s\frac{L_{n-1}(x)}{L_n(x)},\quad \text{for $n\geq 1$};\\
c_{2n+1}&=(g_{2n+1}-1)g_{2n}A=\frac{L_{n+1}(x)}{L_n(x)},\quad \text{for $n\geq 0$}.
\end{split}\right.
\end{equation}
Invoking the \emph{contraction formula} (see \cite{zeng}), which transforms 
a S-continued fraction to a J-continued fraction, 
\begin{align}\label{eq:contraction}
 {1\over \displaystyle 1 -{c_1z\over
\displaystyle 1 - {c_2z\over
\displaystyle 1 - {c_{3}z\over
\displaystyle 1-{c_4z\over
\displaystyle  \ddots
}}}}}=\cfrac{1}{1-c_1z-\cfrac{c_1c_2 z^2}{
 1 -(c_2+c_3)z-\cfrac{c_3c_4z^2}{\ddots}}},
\end{align}
we obtain
\begin{equation}\label{eq:jacobi}
\left\{\begin{split}
 b_n&=\frac{h_{n+1}(x,(1-q)s;q)}{h_n(x,(1-q)s;q)}+(1-q^n)s\frac{h_{n-1}(x,(1-q)s;q)}{h_n(x,(1-q)s;q)}=q^nx,\\
\la_n&=\frac{h_{n}(x, (1-q)s;;q)}{h_{n-1}(x, (1-q)s;q)}\cdot (1-q^n)s\frac{h_{n-1}(x, (1-q)s;;q)}{h_n(x, (1-q)s;;q)}=(1-q^n) s.
\end{split}\right.
\end{equation}
This completes the proof. 
\end{proof}

\noindent{\bf Remark.}  Instead of the contraction formula~\eqref{eq:contraction}, we can also proceed as follows. Define a table $(A(n,k))_{n,k\geq 0}$ by
\begin{align}
 A(0,k)&=\delta_{k,0},\nonumber\\
A(n,0)&=c_1 A(n-1,1),\label{ctable}\\
A(n,k)&=A(n-1,k-1)+c_{k+1}A(n-1,k+1).\nonumber
\end{align}

In this case $A(2n,2k+1)=A(2n+1,2k)=0$ for all $n,k$.
If we define 
$$
a(n,k)=A(2n,2k),
$$
then it is easily verified that $a(n,k)$ satisfy \eqref{eq:stableau} with
\begin{align}
b_0=c_1,\quad b_n=c_{2n}+c_{2n+1},\quad \la_n=c_{2n}c_{2n-1}.
\end{align}
Substituting the values in \eqref{eq:coeff} for $c_n$ 
we obtain \eqref{eq:jacobi}.
Therefore 
$$\sum_{n}A(2n,0)t^n=\sum_n a(n,0)t^n=\sum_n T_n(x,s)t^n.
$$


As another application of this remark  we prove the following result.

\begin{prop}
 Let $w_n(m,q)=q^\frac{n((2m+1)n+1)}{2}$. Then
 $$
 \sum_{m\geq 0}w_n(m,q)t^n=\cfrac{1}{ 1 -b_0 t-
\cfrac{\la_1 t^2}{1 -b_1 t-
 \cfrac{\la_2t^2}{1 - b_2 t-
 \cfrac{\la_3t^2}{1 -
 \ddots}}}},
 $$
 where
\begin{align*}
b_n&=q^{(2m+1)n-m}(q^{(2m+1)n}-1)+q^{(2m+1)(2n+1)-m},\\
\la_n&=q^{(2m+1)(3n-1)-2m}(q^{(2m+1)n}-1).
\end{align*}
\end{prop}
\begin{proof}
 Let 
$$
A(2n,2k)=\frac{w_n(m,q)}{w_k(m,q)}{n\brack k}_{q^{2m+1}}\quad
\text{and}\quad A(2n+1,2k+1)=\frac{w_{n+1}(m,q)}{w_{k+1}(m,q)}{n\brack k}_{q^{2m+1}}.
$$
Then it is easily verified that the table \eqref{ctable} holds with 
$c_{2n}=q^{(2m+1)n-m}(q^{(2m+1)n}-1)$ and $c_{2n+1}=q^{(2m+1)(2n+1)-m}$.
Therefore 
$$
\sum_{n}A(2n,0)t^n=\sum_n a(n,0)t^n=\sum_n w_n(m,q)t^n.
$$
\end{proof}
