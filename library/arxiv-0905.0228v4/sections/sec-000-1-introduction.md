---
doc_id: arxiv-0905.0228v4
doc_title: "A CURIOUS q-ANALOGUE OF HERMITE POLYNOMIALS"
section_id: sec-000-1-introduction
section_title: "Introduction"
section_number: 1
pages: 1-4
source_pdf: 0905.0228v4.pdf
source_sha256: 1744545d0f210949
toc_source: outline
text_source: latex
latex_prose_ratio: 0.709
latex_coverage_ratio: 0.916
doc_brief: "A CURIOUS q-ANALOGUE OF HERMITE POLYNOMIALS — Two well-known q-Hermite polynomials are the continuous and discrete q-Hermite polynomials."
---
There are many ways to construct Hermite polynomials. 
For example, the normalized Hermite polynomials $H_n(x,s)=s^{n/2}H_n(x/\sqrt{s}, 1)$ ($n\geq 0$) may be defined by
the recurrence relation:
\begin{align}\label{eq:rec1}
H_{n+1}(x,s)=xH_n(x,s)-nsH_{n-1}(x,s),
\end{align}
with initial values $H_0(x,s)=1$ and $H_{-1}(x,s)=0$.
By induction, we have 
\begin{align}\label{eq:op}
H_n(x,s)=(x-s{\D})^n\cdot 1,
\end{align}
where ${\D}=\frac{d}{dx}$ denotes the differentiation operator. It follows that 
\begin{align}\label{eq:rec2}
{\D}\,H_n(x,s)=nH_{n-1}(x,s).
\end{align}
They have  the explicit formula (see \cite[Chapter 6]{AAR})  
$$
H_n(x,s)=\sum_{k=0}^n{n\choose 2k}(-s)^k(2k-1)!! x^{n-2k}.
$$
The first terms are
$$
1,\;x, \; -s+x^2,\; -3sx+x^3,\; 3s^2-6sx^2+x^4,\; 15s^2x-10sx^3+x^5.
$$
The Hermite polynomials are orthogonal with respect  to the the linear functional defined by the moments
$$
\mu_n=\frac{1}{\sqrt{2\pi}}\int_{-\infty}^{\infty} x^ne^{-x^2/2}dx=
\left\lbrace\begin{array}{cc}
(n-1)!!& \text{if $n$ is even},\\
0& \text{otherwise}.
\end{array}\right.
$$
In other words,  the $n$-th moment $\mu_n$ of the measure of  the Hermite polynomials is the number of the {\em complete matchings} 
on $[n]:=\{1,\ldots, n\}$, i.e., $\mu_{2n}=(2n-1)!!$ and $\mu_{2n+1}=0$.

Consider the rescaled Hermite polynomials $p_n(z,x,s)=H_n(z-x, -s)$ defined by
\begin{align}
p_{n+1}(z,x,s)=(z-x)p_n(z,x,s)+snp_{n-1}(z,x,s)
\end{align}
with initial values $p_0(z,x,s)=1$ and $p_{-1}(z,x,s)=0$.
Let $\mathcal{F}$ be the linear functional on the polynomials in $z$ defined by
$\mathcal{F}(p_n(z,x,s))=\delta_{n,0}$. Then, the moments
 $\mathcal{F}(z^n)$ are again the Hermite polynomials
\begin{align}
\mathcal{F}(z^n)=(\sqrt{-s})^n 
\sum_{k=0}^n {n\choose k}(x/\sqrt{-s})^{n-k}\mu_k=H_n(x,s).
\end{align}
This is equivalent to say that the generating function  of the  Hermite polynomials $H_n(x,s)$ has the  following
continued fraction expansion:
\begin{align}
H(z,x,s)=\sum_{n\geq 0} H_n(x,s)z^n=
\cfrac{1}{1-xz+\cfrac{sz^2}{1-xz+\cfrac{2sz^2}{1-xz+\cfrac{3sz^2}{\ddots}}}}.
\end{align}












Several $q$-Hermite polynomials were introduced in the literature (see \cite{KK, ISV}).
Two important classes of orthogonal $q$-analogues of $H_n(x,s)$ are 
the continuous and the discrete $q$-Hermite I polynomials,  which are special cases of the Al-Salam-Chihara polynomials. 

We first introduce some standard $q$-notations.   For $n\geq 1$  let
$$
 [n]:=[n]_q=\frac{1-q^n}{1-q}, \quad [n]_q!=\prod_{k=1}^n[k]_q,\quad [2n-1]_q!!=\prod_{k=1}^n[2k-1]_q,
$$
and $(a;q)_n=(1-a)(1-aq)\cdots (1-aq^{n-1})$ with $(a;q)_0=1$. The $q$-binomial coefficient is defined by
$$
{n\brack k}:={n\brack k}_q=\frac{(q;q)_n}{(q;q)_k(q;q)_{n-k}}
$$
for  $0\leq k\leq n$ and zero otherwise. 

 Recall \cite{IS} that 
the Al-Salam-Chihara polynomials $P_n(x;a,b,c)$ satisfy the three term recurrence:
\begin{align}\label{eq:ACR}
P_{n+1}(x; a,b,c)=(x-aq^n)P_n(x;a,b,c)-(c+bq^{n-1})[n]_qP_{n-1}(x;a,b,c)
\end{align}
with initial values $P_{-1}(x;a,b,c)=0$ and $P_{0}(x;a,b,c)=1$.

\begin{defn} Let $\F_{a,b,c}$ be the linear functional on the polynomials in $z$ which satisfy
\begin{align}\label{eq:moment}
\F_{a,b,c}(P_n(z;a,b,c))=\delta_{n,0}.
\end{align}
\end{defn}

Note that the continuous $q$-Hermite polynomials are
\begin{align}\label{eq:contherm}
\tilde{H}_n(x,s|q)=P_n(x;0,0,s)
\end{align}
and are also the moments  (see \cite{IS} and Proposition~16):
\begin{align}\label{eq:contherm2}
\tilde{H}_n(x,s|q)=\F_{x,-s,0}(z^n).
\end{align}
The discrete $q$-Hermite polynomials  I are
\begin{align}\label{eq:disch}
\tilde{h}_n(x,s;q)=P_n(x;0,(1-q)s,0).
\end{align}
The discrete $q$-Hermite polynomials  II  are
\begin{align}\label{eq:disch}
\tilde{h}_n(x;q)=(-i)^n \tilde{h}_n(ix,1;q^{-1}).
\end{align}
Besides, as we will see in Section~4,  the polynomials
\begin{align}\label{eq:H2}
h_n(x,s;q):=P_n(0; -x,0, s)
\end{align}
 are actually a rescaled version of $\tilde{h}_n(x;q)$.
The main purpose of this paper is to study   another  $q$-analogue of Hermite polynomials.
\begin{defn} The new $q$-Hermite polynomials are defined by
\begin{align}\label{eq:H1}
H_n(x,s|q):=\F_{x,0,-s}(z^n).
\end{align}

\end{defn}


The q-Hermite polynomials $\tilde H_n(x,s|q)$ have, 
amongst other facts, 

\begin{itemize}
\item[(1)] orthogonality with an explicit measure, 
\item[(2)] an explicit 3-term recurrence relation, 
\item[(3)]  explicit expressions,
\item[(4)]  a combinatorial model using matchings, 
\item[(5)]  are moments for other orthogonal polynomials, 
\item[(6)]  evaluable Hankel determinants because of (5), 
\item[(7)] Jacobi continued fractions as generating  functions because of (5). 
\end{itemize}

The new $q$-Hermite polynomials  $H_n(x,s|q)$ are not orthogonal,  i.e., they do not have (1) and (2). 
Instead they have  a nice $q$-analogue of  the operator formula \eqref{eq:op} for the ordinary Hermite polynomials (see Theorem~\ref{thm:main}), 
  the coefficients in  $H_n(x,s|q)$  appear in the inverse matrix of the coefficients in the continuous 
  $q$-Hermite polynomials (cf. Theorem~\ref{thm:HH}),  they have simple connection coefficients  with  
   $q$-Lucas  and $q$-Fibonacci polynomials  (cf. Theorem~\ref{thm:hf}). 
  The discrete q-Hermite polynomials $h_n(x,s;q)$ also have (1)-(4), and we will show in Theorem~\ref{thm4.4}
   that they are also moments. 
Moreover,  the quotients of two consecutive  polynomials $h_n(x,s;q)$ (see Eq.\eqref{eq:coeff}) appear as coefficients 
 in the expansion of the S-continued fraction of the generating function of
 $H_n(x, s|q)$'s, which  leads to a second proof of   Theorem~\ref{thm:main}.
 
 This paper is organized as follows:  we prove the main properties of $H_n(x,s|q)$ and $h_n(x,s;q)$  in Section~2 and  Section~3, respectively. In Section~4 we shall establish the connection of our new $q$-Hermite polynomials with the $q$-Fibonacci and $q$-Lucas polynomials. This yields,  in particular,  a generalization of Touchard-Riordan's formula for the moments of continuous $q$-Hermite polynomials (cf. Proposition~\ref{prop:mathieu}), first obtained by Josuat-Verg\`es~\cite{JV}. Finally,  in Section~5, we recall some well-known facts about the general theory of orthogonal polynomials and give another proof of the generalized Touchard-Riordan formula by using the orthogonality of continuous $q$-Hermite polynomials.


\section{The  $q$-Hermite polynomials  $H_n(x,s|q)$}

By  \eqref{eq:moment}  the  $q$-Hermite polynomials $H_n(x,s|q)$ are  the moments of the measure of the orthogonal polynomials
$P_n(z)$ satisfying the recurrence:
\begin{align}\label{eq:defP}
P_{n+1}(z)=(z-xq^n) P_n(z)+s[n]_qP_{n-1}(z).
\end{align}
Recall \cite[p.80]{KK} that 
the Al-Salam-Chihara polynomials $Q_n(x):=Q_n(x;\alpha, \beta)$ satisfy the three term recurrence:
\begin{align}\label{eq:AC}
Q_{n+1}(x)=(2x-(\alpha+\beta)q^n)Q_n(x)-(1-q^n)(1-\alpha\beta q^{n-1})Q_{n-1}(x),
\end{align}
with $Q_0(x)=1$ and $Q_{-1}(x)=0$. They have the following explicit formulas:
\begin{align}
Q_n(x;\alpha,\beta|q)





&=(\alpha e^{i\theta};q)_n e^{-i\theta}{}_2\phi_1
\left(\begin{array}{cl}
q^{-n},&\beta e^{-i\theta}\\
\quad \alpha^{-1} q^{-n+1}e^{-i\theta}&
\end{array}|q;\alpha^{-1} q e^{i\theta}\right),\label{eq:Q2}
\end{align}
where $x=\cos \theta$.

Comparing \eqref{eq:defP} and \eqref{eq:AC}  we have 



$P_n(z)=\frac{1}{(2a)^n}Q_n(az; \alpha, 0)$ with 
\begin{align}
a=\frac{1}{2}\sqrt{\frac{q-1}{s}}\quad\textrm{and}\quad 
\alpha=x\sqrt{\frac{q-1}{s}}.
\end{align}


Using the known formula for Al-Salam-Chihara polynomials we obtain
\begin{align}
P_n(z)&=\frac{1}{(2a\alpha)^n}\sum_{k=0}^n\frac{(q^{-n};q)_k}{(q;q)_k}q^k
\prod_{i=0}^{k-1}(1+\alpha^2q^{2i}-2q^i a\alpha z)\nonumber\\
&=\left(\frac{s}{x(q-1)}\right)^n
\sum_{k=0}^n\frac{(q^{-n};q)_k}{(q;q)_k}\left(\frac{-q}{s}\right)^k
\prod_{i=0}^{k-1}\left((q-1)q^ixz-s-(q-1)q^{2i}x^2\right).\label{rescal}
\end{align}

The first values of these polynomials are
\begin{align*}
 P_1(z)&=z-x,\\
P_2(z)&=z^2-x(1+q)z+(s+qx^2),\\
P_3(z)&=z^3-x[3]_q z^2+(2s+qs+q[3]_q x^2)z
-(s+qs+q^2s+q^3x^2)x.
\end{align*}

A matching $m$ of $\{1,2,\ldots, n\}$ is a set of pairs $(i,j)$ such that $i<j$ and $i,j\in [n]$. 
Each pair $(i,j)$ is called an edge of the matching. Let $\ed(m)$ be the number of edges of $m$, so $n-2\ed(m)$ is the number of unmatched vertices. Two edges $(i,j)$ and $(k,l)$ have a crossing if $i<k<j<l$ or $k<i<l<j$. Let 
$\cro(m)$ be the number of crossing numbers in the matching $m$. 
Using the combinatorial theory of Viennot~\cite{Vi},  Ismail and  Stanton \cite[Theorem 6]{IS} gave a combinatorial interpretation of the moments of Al-Salam-Chihara polynomials.  In particular  we derive   the  following result from  \cite[Theorem 6]{IS}.
\begin{lem} The moments  of the measure of  the orthogonal polynomials  $\{P_n(x)\}$ 
 are  the generating functions for all matchings $m$ of 
$[n]$:
\begin{align}\label{eq:combmoment}
\F_{x,0,-s}(z^n)=\sum_{m}x^{n-2\ed(m)}(-s)^{\ed(m)}
q^{\c(m)+\cro(m)},
\end{align}
where  
$c(m)=\sum_{\mathrm{a-vertices}}
|\{\mathrm{edges}\; i<j:\; i<a<j\}|$  and the sum extends over all matchings $m$ of $[n]$.
\end{lem}


Let $M(n,k)$ be  the set of matchings of $\{1, \ldots, n\}$ with $k$ unmatched vertices. Then
\begin{align}\label{eq:cig11}
\F_{x,0,-s}(z^n)=\sum_{k}c(n,k,q)x^k(-s)^\frac{n-k}{2},
\end{align}
where
\begin{align}\label{eq:key}
c(n,k,q)=\sum_{m\in M(n,k)}
q^{c(m)+\cro(m)}.
\end{align}
It is easy to verify that
\begin{align}\label{eq:cig2}
c(n,k,q)=c(n-1,k-1,q)+[k+1]_q c(n-1,k+1,q)
\end{align}
with $c(0,k,q)=\delta_{k,0}$ and $c(n,0,q)=c(n-1,1,q)$.

Indeed, if $n$ is an unmatched vertex then for the restriction $m_0$ of $m$ to $[n-1]$ we get $c(m_0)=c(m)$
and $\cro(m_0)=\cro(m)$. If $n$ is matched with $m(n)$, such that there are $i$ unmatched vertices and $j$ endpoints of edges which cross the edge $(m(n),\;n)$ between $m(n)$ and $n$, then $c(m)=c(m_0)+i-j$ and 
$\cro(m)=\cro(m_0)+j$. Thus 
$c(m)+\cro(m)=c(m_0)+\cro(m_0)+i$. Since each $i$ with $0\leq i\leq k$ can occur we get \eqref{eq:cig2}.


Let now  ${\D}_q$ be the  $q$-derivative operator defined by
 $$
 {\D}_qf(z)=\frac{f(z)-f(qz)}{(1-q)z}.
 $$ 
 We have then the following $q$-analogue of \eqref{eq:op}.
\begin{thm}\label{thm:main} The $q$-Hermite polynomials $H_n(x,s|q)$, defined as 
moments $\F_{x,0,-s}(z^n)$, have the following operator formula:
\begin{align}\label{eq:qop}
H_n(x,s|q)=(x-s {\D}_q)^n1.
\end{align}
\end{thm}
\begin{proof}
We know that
\begin{align}\label{eq:cig1}
H_n(x,s|q)=\sum_{k}c(n,k,q)x^k(-s)^\frac{n-k}{2},
\end{align}
where $c(n,k,q)$ satisfies \eqref{eq:cig2}.   Therefore
\begin{align*}
H_n(x,s|q)&=\sum_kc(n-1,k-1,q)x^k(-s)^\frac{n-k}{2}+\sum_k[k+1]_qc(n-1,k+1,q)x^k(-s)^\frac{n-k}{2}\\
&=xH_{n-1}(x,s|q)-s{\D}_q H_{n-1}(x,s|q).
\end{align*}
The result follows then by induction on $n$.
\end{proof}

\noindent{\bf Remark.}  It should be noted that the method of  Varvak \cite{Va}  (see also \cite{JV}) can also be applied to prove Theorem~\ref{thm:main}. In fact her
 method proves first that $(x-sD_q)^n1$ is a generating function of some rook placements, which 
 is then shown to count  involutions  with respect to the statistic 
 ${\c(m)+\cro(m)}$ (see  \cite[Theorem 6.4]{Va}). We will give another proof of \eqref{eq:qop} by  using continued fraction, see 
the remark after Theorem~\ref{thm:Hh}. 

\medskip
The first terms  of the sequence $H_n(x,s|q)$ are 
\begin{align*}
&1,\; x,\; -s+x^2,\; x(-(2+q)s+x^2),\; (2+q)s^2-(3+2q+q^2)sx^2+x^4,
\\ 
&\qquad\qquad x((5+6q+3q^2+q^3)s^2-(4+3q+2q^2+q^3)sx^2+x^4),\ldots
\end{align*}

Let 
\begin{align}\label{eq:bcoeff}
\tilde H_n(x,s|q)=\sum_{k}b(n,k,q)x^k(-s)^\frac{n-k}{2}.
\end{align}

\begin{thm}\label{thm:HH} The matrices $(c(i,j,q))_{i,j=0}^{n-1}$ and $(b(i,j,q)(-1)^\frac{i-j}{2})_{i,j=0}^{n-1}$ are mutually inverse.
\end{thm}

\begin{proof}
We first show by induction that
\begin{align}\label{eq1.1}
\tilde H_n(x+s{\D}_q,s|q)1=x^n.
\end{align}
For this is obvious for $n=0$. If it is already shown for $n$ we get
\begin{align*}
\tilde H_{n+1}(x+s{\D}_q,s|q)1&=(x+s{\D}_q)\tilde H_n(x+s{\D}_q,s|q)1-s[n]_q\tilde H_{n-1}(x+s{\D}_q,s|q)1\\
&=(x+s{\D}_q)x^n-s[n]_qx^{n-1}=x^{n+1}.
\end{align*}
On the other hand we have
\begin{align}\label{eq1.2}
\tilde H_{n}(x+s{\D}_q,s|q)1&=\sum_{k=0}^nb(n,k,q)(-s)^\frac{n-k}{2}(x+s{\D}_q)^k1\nonumber\\
&=\sum_{k=0}^nb(n,k,q)(-s)^\frac{n-k}{2}\sum_{j=0}^kc(k,j,q)s^\frac{k-j}{2}x^j\nonumber\\
&=\sum_{j=0}^n s^\frac{n-j}{2}x^j\sum_{k=j}^n b(n,k,q)(-1)^\frac{n-k}{2}c(k,j,q).
\end{align}
The result follows then by comparing \eqref{eq1.1} and \eqref{eq1.2}.
\end{proof}

\noindent
{\bf Remark.}
If we set $q=0$ then \eqref{eq:cig2} reduces to the well-known Catalan triangle (see \cite[Chap. 7]{aigner}), which implies 
\begin{align*}
 c(2n,0,0)&=C_n=\frac{1}{n+1}{2n\choose n},\\
c(2n,2k,0)&=\frac{2k+1}{n+k+1}{2n\choose n-k}={2n\choose n-k}-{2n\choose n-k-1},\\
c(2n+1,2k+1,0)&=\frac{2k+2}{n+k+2}{2n+1\choose n-k}={2n+1\choose n-k}-{2n+1\choose n-k-1}.
\end{align*}





















We shall use the standard $q$-notations in \cite{GR}.   
The recurrence \eqref{eq:defP} implies that the  Hankel determinants of $H_n(x,s|q)$ are
\begin{align}
\det(H_{i+j}(x,s|q))_{i,j}^{n-1}=(-s)^{n\choose 2}\prod_{j=0}^{n-1}[j]_q! 
\end{align}
and 
\begin{align}
\det(H_{i+j+1}(x,s;q))_{i,j}^{n-1}
=h_n(x,-s;q)(-s)^{n\choose 2}\prod_{j=0}^{n-1}[j]_q! ,
\end{align}
where
$$
h_n(x, -s;q)=(-1)^nP_n(0)=\left(\frac{s}{x(1-q)}\right)^n\sum_{k=0}^n\frac{(q^{-n};q)_k}{(q;q)_k}q^k
\prod_{i=0}^{k-1}(1+x^2(q-1)q^{2i}/s).
$$
