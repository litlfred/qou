---
doc_id: arxiv-0905.0228v4
doc_title: "A CURIOUS q-ANALOGUE OF HERMITE POLYNOMIALS"
section_id: sec-003-4-connection-with-q-fibonacci-polynomials-and-q
section_title: "Connection with q-Fibonacci polynomials and q-Lucas polynomials"
section_number: 4
pages: 12-16
source_pdf: 0905.0228v4.pdf
source_sha256: 1744545d0f210949
toc_source: outline
text_source: latex
latex_prose_ratio: 0.93
latex_coverage_ratio: 0.955
doc_brief: "A CURIOUS q-ANALOGUE OF HERMITE POLYNOMIALS — Two well-known q-Hermite polynomials are the continuous and discrete q-Hermite polynomials."
---
We define the Lucas polynomials  by
$$
l_n(x,s)=xl_{n-1}(x,s)+sl_{n-2}(x,s)\quad \text{for}�\quad n>2,
$$
with initial values $l_1(x,s)=x$ and $l_2(x,s)=x^2+2s$. They have the explicit formula
\begin{align}\label{eq:luc1}
l_n(x,s)=\sum_{2k\leq n}
\frac{n}{n-k} {n-k\choose k}s^k x^{n-2k}  \quad (n>0).
\end{align}
Furthermore we define $l_0(x,s)=1$. Note that this definition differs from the usual one in which 
$l_0(x,s)=2$. 

The Fibonacci polynomials are defined by
$$
f_n(x,s)=xf_{n-1}(x,s)+sf_{n-2}(x,s)
$$
with $f_0(x,s)=0$ and $f_1(x,s)=1$.  They have the explicit formula
\begin{align}\label{eq:fib1}
f_n(x,s)=\sum_{k=0}^{\left\lfloor\frac{n-1}{2}\right\rfloor} {n-1-k\choose k}s^k x^{n-1-2k}.
\end{align}

We first establish the following inversion of  \eqref{eq:luc1} and \eqref{eq:fib1}.
\begin{lem}
\begin{align}\label{eq:lem}
x^n&=\sum_{2k\leq n}{n\choose k} s^kl_{n-2k}(x,-s),\\
x^n&=\sum_{2k\leq n+1}\left({n\choose k}-{n\choose k-1}\right)s^k f_{n+1-2k}(x,-s).\label{eq:lemfib}
\end{align}
\end{lem}
\begin{proof}
Recall the Tchebyshev inverse relations~\cite[p. 54-62]{Ri}:
\begin{align}\label{eq:tch1}
b_n=\sum_{k=0}^{\left\lfloor\frac{n}{2}\right\rfloor} 
(-1)^k\frac{n}{n-k}{n-k\choose k}a_{n-2k}
\Longleftrightarrow
a_n=\sum_{k=0}^{\left\lfloor\frac{n}{2}\right\rfloor}
{n\choose k}
b_{n-2k},
\end{align}
where $a_0=b_0=1$, and 
\begin{align}\label{eq:tch}
b_n=\sum_{k=0}^{\left\lfloor\frac{n}{2}\right\rfloor} 
(-1)^k{n-k\choose k}a_{n-2k}
\Longleftrightarrow
a_n=\sum_{k=0}^{\left\lfloor\frac{n}{2}\right\rfloor}
\left[{n\choose k}-{n\choose k-1}\right]
b_{n-2k}.
\end{align}
We derive immediately \eqref{eq:lem} from \eqref{eq:luc1} and \eqref{eq:tch1}.
Clearly \eqref{eq:fib1} is equivalent to the left identity in \eqref{eq:tch} with $a_n=\left(\frac{x}{\sqrt{s}}\right)^n$ and $b_n=\frac{f_{n+1}(x,-s)}{(\sqrt{s})^n}$. By inversion we find
\begin{align}\label{eq:lem'}
x^n=\sum_{k=0}^{\left\lfloor\frac{n}{2}\right\rfloor}
\left({n\choose k}-{n\choose k-1}\right)
s^k f_{n+1-2k}(x,-s).
\end{align}
To see the equivalence of \eqref{eq:lemfib} and \eqref{eq:lem'} we notice that 
\begin{itemize}
\item if $n$ is odd, then
${n\choose k}={n\choose k-1}$ for $k=\left\lfloor\frac{n+1}{2}\right\rfloor$,
\item if $n$ is even, then $\left\lfloor\frac{n+1}{2}\right\rfloor=\left\lfloor\frac{n}{2}\right\rfloor$.
\end{itemize}
\end{proof}

\medskip
Define the $q$-Lucas and $q$-Fibonacci polynomials by
\begin{align}
L_n(x,s)&=l_n(x+(q-1)s\D_q,s)\cdot 1,\\
F_n(x,s)&=f_n(x+(q-1)s{\D}_q, s)\cdot 1. 
\end{align}
It is known (see \cite{Cigler03} and \cite{Cigler09} ) that  they have the explicit formulae
\begin{align}
L_n(x,s)&=\sum_{k=0}^{\left\lfloor \frac{n}{2}\right\rfloor}q^{k\choose 2} \frac{[n]}{[n-k]}{n-k\brack k}s^kx^{n-2k},\label{eq:qluc}\\
F_n(x,s)&=\sum_{k=0}^{\left\lfloor \frac{n-1}{2}\right\rfloor}q^{k+1\choose 2}{n-1-k\brack k}s^kx^{n-1-2k},\label{eq:qfib}
\end{align}
for $n>0$,  with $L_0(x,s)=1$ and  $F_0(x,s)=0$.

\begin{thm}\label{thm:hf}
We have 
\begin{align}\label{eq:explicit}
H_n(x, (q-1)s|q)
&=\sum_{k=0}^{\left\lfloor \frac{n}{2}\right\rfloor}
{n\choose  k}s^kL_{n-2k}(x,-s)\\
&=\sum_{k=0}^{\left\lfloor \frac{n+1}{2}\right\rfloor}\left({n\choose k}-{n\choose k-1}\right) s^k F_{n+1-2k}(x,-s).\label{eq:explicit2}
\end{align}
\end{thm}
\begin{proof}
Since
\begin{align*}
L_n(x,-s)&=l_n(x-(q-1)s{\D}_q,s)\cdot 1,\\
F_n(x,-s)&=f_n(x-(q-1)s{\D}_q,s)\cdot 1,
\end{align*}
the theorem follows by applying the homomorphism $x\mapsto x-(q-1)s\D_q$ to
\eqref{eq:lem} and \eqref{eq:lemfib}.
\end{proof}

We derive some consequences of  the formula \eqref{eq:explicit2}. 
 \begin{cor} We have 
\begin{align}\label{ex1}
\begin{split}
H_n(1,q-1|q)&=\sum_{k=-n}^{n}(-1)^k
q^{\frac{k(3k+1)}{2}}       {n\choose \left\lfloor\frac{n-3k}{2}\right\rfloor}\\
&=\sum_{k=0}^{n}(-1)^k q^{\frac{k(3k+1)}{2}} 
{n\choose \left\lfloor\frac{n-3k}{2}\right\rfloor}+
\sum_{k=1}^{n}(-1)^kq^{\frac{k(3k-1)}{2}}{n\choose \left\lfloor\frac{n-3k+1}{2}\right\rfloor}.
\end{split}
\end{align}
\end{cor}
\begin{proof}
Let $r(k)=\frac{k(3k+1)}{2}$. Then, it  follows from \cite{Cigler03} that 
$$
F_{3n}(1,-1)=\sum_{k=-n}^{n-1}(-1)^k q^{r(k)},\quad F_{3n+1}(1,-1)=F_{3n+2}(1,-1)=\sum_{k=-n}^{n}(-1)^k q^{r(k)},
$$
or 
\begin{align}
F_{n}(1,-1)=\sum_{-n\leq 3j\leq n-1}(-1)^j q^{\frac{j(3j+1)}{2}}.
\end{align}

Let $w(n)=\sum_{k=0}^{ \left\lfloor\frac{n+1}{2}\right\rfloor}
\left({n\choose k}-{n\choose k-1}\right)F_{n+1-2k}(1,-1) $. Consider a fixed term $(-1)^jq^{r(j)}$. This term occurs in $F_n(1,-1)$ if $-\frac{n}{3}\leq j\leq \frac{n-1}{3}$.
We are looking for all $k$, such that this term occurs in 
$F_{n+1-2k}(1,-1)$. For $j\geq 0$ the largest such number is
$k_0= \left\lfloor\frac{n-3j}{2}\right\rfloor$. For $j\leq \frac{n-2k}{3}$ is equivalent with $k\leq k_0$. Therefore the coefficient of
$(-1)^jq^{r(j)}$ in $w(n)$ is $\sum_{k=0}^{k_0}\left({n\choose k}-{n\choose k-1}\right)={n\choose k_0}$. For $j<0$ we have 
$-\frac{n+1-2k}{3}\leq j$ is equivalent with $k\leq \lfloor \frac{n+1-3j}{2}\rfloor$. This gives the last sum in \eqref{ex1}.
\end{proof}

\begin{cor}
We have
\begin{align}\label{eq:H2n}
H_{2n}\left(1, \frac{q-1}{q} |q \right)=q^{-n} \sum_{j=-n}^n 
\left({2n\choose n-3j}-{2n\choose n-3j-1}\right)q^{2j(3j+1)},
\end{align}
and 
\begin{align}\label{eq:H2n1}
H_{2n+1}(1,\frac{q-1}{q}|q )=q^{-n}\sum_{j=-n}^n\left({2n+1\choose n-3j}-{2n+1\choose n-3j-1}\right)q^{2j(3j+2)}.
\end{align}
\end{cor}
\begin{proof}
Note that 
\begin{align}
H_{2n}(1, \frac{q-1}{q}|q)&=\frac{1}{q^n}\sum_{k=0}^n \left({2n\choose n-k}-{2n\choose n-k-1}\right)q^{k}F_{2k+1}(1,-\frac{1}{q}),\label{eq:step1}\\
H_{2n+1}(1, \frac{q-1}{q}|q)&=\frac{1}{q^n}\sum_{k=0}^{n+1} \left({2n+1\choose n+1-k}-{2n+1\choose n-k}\right)q^{k-1}F_{2k}(1,-\frac{1}{q}).\label{eq:step2}
\end{align}
Recall  (see \cite{Cigler03}) that
\begin{align}
F_{3n}(1, -\frac{1}{q})=0, \quad F_{3n+1}(1, -\frac{1}{q})=(-1)^n q^{r(n)},\quad F_{3n+2}(1, -\frac{1}{q})=(-1)^nq^{r(-n)}.
\end{align}
Hence
\begin{itemize}
\item if $k=3j$ then $2k+1=6j+1$ and $q^kF_{2k+1}(1,-\frac{1}{q})=q^{3j}F_{6j+1}(1,-\frac{1}{q})=q^{2j(3j+1)}$.
\item if $k=3j+1$ then $2k+1=6j+3$ and $q^{k}F_{2k+1}(1,-\frac{1}{q})=0$.
\item If $k=3j+2$ then $2k+1=6j+5$ and $q^{k}F_{2k+1}(1,-\frac{1}{q})=q^{3j+2}$.
\item if $k=3j$ then $2k=6j$ and $q^{k-1}F_{2k}(1,-\frac{1}{q})=0$.
\item if $k=3j+1$ then $2k=6j+2$ and $q^{k-1}F_{2k}(1,-\frac{1}{q})=q^{2j(3j+2)}$.
\item If .$k=3j+2$ then $2k=6j+4$ and $q^{k-1}F_{2k}(1,-\frac{1}{q})=-q^{(3j+1)(2j+2)}$.
\end{itemize}
Substituting the above values into \eqref{eq:step1} and \eqref{eq:step2} yields \eqref{eq:H2n} and \eqref{eq:H2n1}.
\end{proof}

Finally, from \eqref{eq:explicit} and  \eqref{eq:key} we derive two explicit formulae for the coefficient $c(n,k,q)$.

\begin{prop}\label{prop:mathieu}
 If $k\equiv n\pmod{2}$ then
\begin{align}
c(n,k,q)&=\sum_{m\in M(n,k)}q^{c(m)+\cro(m)} \nonumber\\
&=(1-q)^{-\frac{n-k}{2}}\sum_{j\geq 0}{n\choose \frac{n-k-2j}{2}} (-1)^j  
q^{j\choose 2} \frac{[k+2j]}{[k+j]}{k+j\brack j}\label{eq:lucasformula}\\
&=(1-q)^{-\frac{n-k}{2}}\sum_{j\geq 0}
\left({n\choose \frac{n-k-2j}{2}}-{n\choose \frac{n-k-2j-2}{2}}\right)
(-1)^j q^{{j+1\choose 2}}{k+j\brack k}.\label{eq:cn}
\end{align}
\end{prop}
In the next section we shall give another proof by using the orthogonality of the continuous $q$-Hermite polynomials.
Some remarks about the above formula are in order.
\begin{itemize}
\item[(a)] Formula  \eqref{eq:cn} has been obtained with different means by Josuat-Verg\`es \cite[Proposition 12]{JV} and is also used in \cite{CJPR}. It is easy to see that \eqref{eq:lucasformula} and \eqref{eq:cn} are equal by writing
$$
 \frac{[k+2j]}{[k+j]}= q^j+\frac{[j]}{[k+j]}.
$$
\item[(b)] When $k=0$, 
we recover 
a formula of Touchard-Riordan (see \cite{aigner,ISV,Pe}):
\begin{align}\label{eq:TR}
c(2n,0,q)=\sum_{m\in M(2n,0)} q^{\cro(m)}=\frac{1}{(1-q)^n}\sum_{j=-n}^n{2n\choose n+j}(-1)^jq^{j\choose 2}.
\end{align}
\item[(c)] Notice that  $H_{2n}(0,-1|q)=c(2n,0,q)$ and $H_{2n+1}(0,-1|q)=c(2n+1,0,q)=0$. Hence 
$$
\sum_{n\geq 0}c(n,0,q)t^n=\cfrac{1}{1-\cfrac{t^2}{1-\cfrac{[2]_q t^2}{1-\cfrac{[3]_qt^2}{1-\cdots}}}}.
$$
We derive then a known result
(see \cite{ISV}): the coefficient $c(n,0,q)$  coincides with the $n$-th  moment of the continuous $q$-Hermite polynomials $\tilde H(x,1|q)$, i.e., 
$$
\F(z^n)=c(n,0,q),
$$
where $\F$ is the linear functional on the polynomials in $z$ defined by $\F(\tilde H_n(x,1|q))=\delta_{n,0}$.  
\end{itemize}

As in \cite{KSZ} we can derive another double sum expression for $H_n(x,s|q)$. We omit the proof.
 
\begin{prop} We have
\begin{align}
H_n(x,s|q)&=
\sum_{k=0}^n(-1)^kq^{-{k\choose 2}}\sum_{i=0}^{k}
\left(\frac{s}{x(q-1)}q^{-i}+xq^i\right)^{n}\nonumber\\
&\qquad\qquad \times \prod_{j=0, j\neq i}^{k}\frac{1}{q^{-i}-q^{-j}+x^2\frac{q-1}{s}(q^i-q^j)}.\label{eq:explicitbis}
\end{align}
\end{prop}
