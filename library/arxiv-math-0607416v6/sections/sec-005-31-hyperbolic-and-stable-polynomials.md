---
doc_id: arxiv-math-0607416v6
doc_title: "PÓLYA-SCHUR MASTER THEOREMS FOR CIRCULAR DOMAINS AND THEIR BOUNDARIES"
section_id: sec-005-31-hyperbolic-and-stable-polynomials
section_title: "Hyperbolic and Stable Polynomials"
section_number: 3.1
pages: 9-14
source_pdf: 0607416v6.pdf
source_sha256: 0705075947ce4a3d
toc_source: outline
text_source: latex
latex_prose_ratio: 0.947
latex_coverage_ratio: 0.952
doc_brief: "PÓLYA-SCHUR MASTER THEOREMS FOR CIRCULAR DOMAINS AND THEIR BOUNDARIES — We characterize all linear operators on ﬁnite or inﬁnite-dimensio- nal polynomial spaces that preserve the property of having"
---
\label{ss31}

If the zeros of two hyperbolic polynomials $f,g\in\HH_1(\bR)$ interlace then 
the {\em Wronskian} 
$W[f,g]:=f'g-fg'$ is either non-negative or non-positive on the whole real 
axis $\RR$. 

\begin{definition}\label{def-pp}
Given $f,g \in \HH_1(\bR)$ we say that $f$ and $g$ 
are in {\em proper position}, denoted $f \ll g$, if the zeros of $f$ and $g$ 
interlace and $W[f,g] \leq 0$. 
\end{definition}

For technical reasons we also say that the zeros of the polynomial $0$ 
interlace the zeros of any (non-zero) hyperbolic polynomial and write 
$0 \ll f$ and $f \ll 0$. Note 
that if $f \ll g$ and $g \ll f$ then $f$ and $g$ must be constant multiples 
of each other, that is, $W[f,g]\equiv 0$.

The following theorem is a version of the classical Hermite-Biehler 
theorem \cite{RS}.

\begin{theorem}[Hermite-Biehler theorem]
Let $h := f +ig \in \CC[z]$, where $f,g \in \RR[z]$. Then 
$h \in \HH_1(\CC)$ if and only if $f,g\in\HH_1(\bR)$ and $g \ll f$. 
Moreover, $h$ is strictly stable  if and only if 
$f$ and $g$ are strictly hyperbolic polynomials with no common zeros and 
$g \ll f$.
\end{theorem}  

The next theorem is often attributed to Obreschkoff \cite{obreschkoff}.
 
\begin{theorem}[Obreschkoff theorem]
Let $f,g \in \RR[z]$. Then 
$\alpha f + \beta g \in \HH_1(\RR)\cup \{0\}$ for all $\alpha, \beta \in \RR$ 
if and only if either 
$f \ll g$, $g \ll f$, or  $f=g\equiv 0$.  
Moreover,  $\alpha f + \beta g$ is strictly hyperbolic for all 
$\alpha, \beta \in \RR$ with 
$\alpha^2 + \beta^2 \neq 0$ if and only if  $f$ and $g$ are strictly 
hyperbolic polynomials with no common zeros and either $f \ll g$ or $g \ll f$. 
\end{theorem}

\begin{remark}\label{obremark}
Note that if $T : \pi_n(\RR) \rightarrow \pi(\RR)$ is an $\RR$-linear 
operator then by Obreschkoff's theorem  $T$ also preserves 
interlacing in the following manner: if $f$ and $g$ are hyperbolic 
polynomials of degree 
at most $n$ whose zeros interlace then the zeros of $T(f)$ and $T(g)$ 
interlace 
provided that $T(f)T(g) \neq 0$. 
\end{remark} 

\begin{lemma}\label{degenerate}
Let $n \in \NN$. 
Suppose that  $T : \RR_{n+1}[z] \rightarrow \RR[z]$ preserves hyperbolicity 
and 
that $f \in \RR[z]$ is a strictly hyperbolic polynomial of degree $n$ or 
$n+1$ for which $T(f)=0$. Then 
$T(g)$ is hyperbolic for all $g \in \RR[z]$ with $\deg g \leq n+1$. 

Let $T : \CC_n[z] \rightarrow \CC[z]$ be a stability preserver and suppose 
that $f \in \CC[z]$ is a strictly stable polynomial of degree $n$ for which 
$T(f)=0$. Then 
$T(g)$ is stable for all $g \in \CC[z]$ with $\deg g \leq n$. 
\end{lemma}

\begin{proof}
Let $f$ be a strictly hyperbolic polynomial of degree $n$ or $n+1$ for which 
$T(f)=0$ and let $g \in \RR[z]$ be a 
polynomial with $\deg g \leq n+1$. From Hurwitz' theorem it follows that for 
$\epsilon \in \RR$ with $|\epsilon|$ small enough 
the polynomial $f+\epsilon g$ is strictly hyperbolic. Since 
$\deg (f+\eps g)\le n+1$ and $T$ preserves hyperbolicity up to degree $n+1$ 
we get that $T(g)=\epsilon^{-1} T(f+\eps g)$ is 
hyperbolic. 

Suppose that  $f \in \CC[z]$ is a strictly stable polynomial of degree $n$ 
such that 
$T(f)=0$ and that the degree of $g \in \CC[z]$ does not exceed $n$. By 
Hurwitz' theorem 
$f+\epsilon g$ is strictly stable for all sufficiently small $|\epsilon|$. 
Since $\deg (f+\eps g)\le n$ and $T$ preserves stability up to degree $n$ it 
follows that $T(g)=\epsilon^{-1} T(f+\epsilon g)$ is stable. 
\end{proof}
 

\begin{lemma}\label{spaces}
Suppose that $V \subseteq \RR[z]$ is an $\RR$-linear space whose every 
non-zero element is hyperbolic. Then $\dim V \leq 2$. 

Suppose that $V \subseteq \CC[z]$ is a $\CC$-linear space whose every 
non-zero element is stable. Then $\dim V \leq 1$. 
\end{lemma}

\begin{proof}
We first deal with the real case. Suppose that there are three linearly 
independent polynomials $f_1,f_2$  and $f_3$ 
in $V$. By Obreschkoff's theorem the zeros of these polynomials mutually 
interlace. Wlog we may assume that 
$f_1 \ll f_2$ and $f_1 \gg f_3$. Consider the line  segment 
$\ell_\theta =\theta f_3 + (1-\theta) f_2$, 
$0 \leq \theta \leq 1$. Since $f_1 \ll \ell_0$ and $f_1 \gg \ell_1$ by 
Hurwitz' theorem  
there is a real number $\eta$ between $0$ and $1$ such that 
$f_1 \ll \ell_\eta$ and $f_1 \gg \ell_\eta$. This 
means that $f_1$ and $\ell_\eta$ are constant multiples of each other 
contrary to the assumption that 
$f_1,f_2$  and $f_3$ are linearly independent. 

For the complex case 
let $V_R= \{ p : p+iq \in V\text{ with } p,q\in \RR[z] \}$ be the 
``real component'' of $V$. By the Hermite-Biehler theorem 
all polynomials in $V_R$ are hyperbolic,  so by the above we have 
$\dim_{\bR} V_R \leq 2$. Clearly, 
$V$ is the complex span of $V_R$. If $\dim_{\bR} V_R \leq 1$ we are done 
so we may assume that 
$\{p,q\}$ is a basis for $V_R$ with $f:=p+iq \in V$. By definition 
$W[p,q] \geq 0$ on the whole of $\RR$ and 
the Wronskian is not identically zero. Assume now that $g$ is another 
polynomial in $V$. Then 
$$
g= ap+bq+i(cp+dq) 
$$
for some $a,b,c,d \in \RR$. We have to show that $g$ is a (complex) constant 
multiple of $f$. Since $g \in V$ we have  
$$
W[ap+bq,cp+dq] = (ad-bc)W[p,q] \geq 0,
$$
so that $ad-bc \geq 0$. Now by linearity we have that 
$$g+(u+iv)f =(a+u)p+(b-v)q+i( (c+v)p+(d+u)q)    \in V
$$ 
for all $u,v \in \RR$ which, as above, gives 
$$
H(u,v):=(a+u)(d+u)-(b-v)(c+v) \geq 0 
$$
for all $u,v \in \RR$. But 
$$
4H(u,v)=(2u+a+d)^2+(2v+c-b)^2-(a-d)^2-(b+c)^2,
$$
so $H(u,v) \geq 0$ for all $u,v \in \RR$ if and only if $a=d$ and $b=-c$. 
This gives  
$$
g=ap-cq+i(cp+aq)=(a+ic)(p+iq)=(a+ic)f,
$$
as was to be shown.
 \end{proof}

\begin{notation}\label{not4}
Let $\HH_1^-(\CC)=\{f \in \CC[z]:f(z) \neq 0\text{ if } \Im(z)<0\}$. By the 
Hermite-Biehler theorem and Definition~\ref{def-pp} if $f,g \in \RR[z]$ then 
$f+ig \in \HH_1^-(\CC)$ if and only if $f,g\in\HH_1(\RR)$ and $f \ll g$. 
Given a linear subspace $V$ of $\CC[z]$ and $M\subseteq V$ 
we say that a linear operator $T$  
on $V$ is {\em stability reversing} on $M$ if 
$T(\HH_1(\CC)\cap M)\subseteq \HH_1^-(\CC) \cup \{0\}$. Note that if 
$S : \CC[z] \rightarrow \CC[z]$ is the 
linear involution defined by $S(f)(z)= f(-z)$ then $T$ is stability reversing 
if and only if $S\circ T$ is stability  preserving. 
\end{notation}

\begin{lemma}\label{trichotomy}
Suppose that  $T : \RR_n[z] \rightarrow \RR[z]$  maps all hyperbolic 
polynomials of degree at most $n$ 
to hyperbolic polynomials. Then 
$T$ is either stability preserving or stability reversing or the range of 
$T$ has dimension at most two. In the latter case 
$T$ is given by 
\begin{equation}\label{form2}
T(f) = \alpha(f)P + \beta(f)Q,\quad f\in\bR_n[z],
\end{equation}
where $P,Q$ are hyperbolic polynomials whose zeros interlace and 
$\alpha, \beta $ are real-valued linear functionals on $\RR_n[z]$.  
\end{lemma}

\begin{proof} 
The lemma is obvious for $n=0$ so we may and do assume that $n$ is a positive 
integer. 
By Remark \ref{obremark} and the Hermite-Biehler theorem we know that $T$ 
maps all
 stable polynomials of degree $n$ into 
the set $\HH_1(\CC)\cup \HH_1^-(\CC) \cup\{0\}$. We now distinguish two 
cases. Suppose first that there are two strictly 
stable polynomials $f,g$ of degree $n$ such that $T(f) \in \HH_1(\CC)$ and 
$T(g) \in \HH_1^-(\CC)$. 

\medskip

{\em Claim.} If the above conditions are satisfied then the kernel of $T$ 
must contain a strictly hyperbolic polynomial of degree at least $n-1$.

\medskip

From Lemma \ref{degenerate} and the Claim we deduce that 
$T : \RR_n[z] \rightarrow \pi(\RR)\cup\{0\}$. Hence 
all non-zero polynomials in the image of $T$ are hyperbolic, which by 
Lemma \ref{spaces} 
gives that $\dim T(\RR_n[z]) \leq 2$ and thus $T$ must be of the 
form~\eqref{form2}. 

\medskip

{\em Proof of Claim.} Suppose that $f_1,f_2$ are two strictly stable 
polynomials of degree $n$ 
for which 
$T(f_1) \in \HH_1(\CC)$ and $T(f_2) \in \HH_1^-(\CC)$, respectively. By a 
homotopy argument, invoking again 
Hurwitz' theorem, there is a strictly stable polynomial $h$ of degree $n$ for 
which 
$T(h) \in \HH_1(\CC)\cap \HH_1^-(\CC) \cup\{0\}$. Writing $h$ as $h=p+iq$, 
where $p$ and $q$ are 
strictly hyperbolic polynomials (by the Hermite-Biehler theorem) gives that 
$T(p)$ and $T(q)$ are constant multiples of each other. Suppose that 
$\deg p =n$.  Then $\deg q \geq n-1$ since the zeros of $p$ and $q$ 
interlace. If  $T(q)=0$ 
the claim is obviously true so suppose that $T(q) \neq 0$. Then 
$T(p)= \lambda T(q)$ for some $\lambda \in \RR$. 
By the Obreschkoff Theorem $p-\lambda q$ is strictly hyperbolic and of 
degree at least $n-1$. Clearly, $T(p-\lambda q)=0$,  
which proves the Claim.  

Suppose now that $T$ maps all strictly stable polynomials of degree $n$ into
the set $\HH_1(\CC)\cup\{0\}$ (the case when $T$ maps all such polynomials
into $\HH_1^-(\CC) \cup\{0\}$ is treated similarly). Let $f$ be a strictly 
stable polynomial with $\deg f<n$ and set 
$f_{\eps}(z)=(1-\eps iz)^{n-\deg f}f(z)$. Then $f_{\eps}$ is strictly stable 
whenever $\eps>0$ and $T(f_{\eps})\in
\HH_1(\CC)\cup\{0\}$ since $\deg f_{\eps}=n$. Letting $\eps\to 0$ we get
$T(f)\in \HH_1(\CC)\cup\{0\}$ and since strictly stable polynomials are 
dense in $\HH_1(\CC)$ it follows that $T$ is stability preserving.
\end{proof}

As a final tool we will need the Grace-Walsh-Szeg\"o coincidence theorem 
\cite{grace,szego,walsh}.  
Recall that a multivariate polynomial is {\em multi-affine} if it has degree 
at most 
one in each variable. 

\begin{theorem}[Grace-Walsh-Szeg\"o coincidence theorem]
Let $f \in \CC[z_1,\ldots, z_n]$ be symmetric and multi-affine and let $C$ be 
a circular domain 
containing the points $\zeta_1, \ldots, \zeta_n$. Suppose that either the 
total degree of $f$ equals $n$ or that $C$ is convex (or both). 
Then there exists at least one point $\zeta \in C$ such that 
$$
f(\zeta_1, \ldots, \zeta_n)=f(\zeta, \ldots, \zeta).
$$
\end{theorem}

From the Grace-Walsh-Szeg\"o coincidence theorem we immediately deduce:

\begin{corollary}\label{polarizeit}
Let $f \in \CC[z_1,\ldots, z_n]$ be of degree at most  $d$ in $z_1$ and 
consider the expansion of $f$ in powers of $z_1$, 
$$
f(z_1,\ldots,z_n)= \sum_{k=0}^dQ_k(z_2,\ldots, z_n)z_1^k,\quad 
Q_k\in\bC[z_2,\ldots,z_n],\, 0\le k\le d. 
$$
Then $f$ is stable if and only if the polynomial 
$$
\sum_{k=0}^d Q_k(z_2,\ldots,z_n)\frac {e_k(x_1,\ldots, x_d)}{\binom d k}
$$
is stable in the variables $z_2, \ldots, z_n, x_1, \ldots, x_d$, where 
$e_k(x_1, \ldots, x_d)$, 
$0 \leq k \leq d$, are the elementary symmetric functions in the variables 
$x_1, \ldots, x_d$ given 
by $e_0=1$ and 
$e_k = \sum_{1 \leq j_1 < j_2 < \cdots < j_k \leq d} x_{j_1}\cdots x_{j_k}$ 
for 
$1 \leq k \leq d$. 
\end{corollary}

\begin{lemma}\label{extension}
Let $T: \CC_n[z_1] \rightarrow \CC[z_1]$ be a linear operator such that 
$T[(z_1+w)^n] \in \HH_2(\CC)$. If $f \in \HH_m(\CC)$ is of degree at most $n$ 
in $z_1$ then 
$T(f) \in \HH_m(\CC)\cup\{0\}$, where $T$ is extended to a linear operator on
$\bC[z_1,\ldots,z_m]$ by setting 
$
T(z_1^{\alpha_1}\cdots  z_m^{\alpha_m}) 
= T(z_1^{\alpha_1})z_2^{\alpha_2} \cdots z_m^{\alpha_m}
$ for all $\alpha \in \NN^m$ with $\alpha_1 \leq n$ (compare with 
Notation~\ref{not1}).
\end{lemma}

\begin{proof}
Let $f \in \HH_m(\CC)$ be of degree $n$ in $z_1$. For $\epsilon >0$ set 
$$
f_\epsilon(z_1, \ldots, z_m) = 
f(z_1+\epsilon i, z_2,\ldots,z_m).
$$ 
Fixing $\zeta_2, \ldots, \zeta_m$ in the open upper half-plane  
we may write $f_\epsilon(z_1, \zeta_2, \ldots, \zeta_m)$ as
$$
f_\epsilon(z_1, \zeta_2, \ldots, \zeta_m)
= C(z_1-\xi_1)(z_1-\xi_2)\cdots (z_1-\xi_n) = 
C \sum_{k=0}^n(-1)^k e_k(\xi_1,\ldots, \xi_n)z_1^{n-k}, 
$$
where $C \neq 0$ and $\Im(\xi_j)<0$, $1\le j\le n$. 
 Note that $z_1\mapsto f_\epsilon(z_1, \zeta_2, \ldots, \zeta_m)$ is indeed a 
polynomial of degree $n$ in $z_1$. This is because 
$$f_\epsilon(z_1, z_2, \ldots, z_m)= z_1^nQ_n(z_2, \ldots, z_m)
+\mbox{terms of lower degree in $z_1$}$$
and $Q_n(z_2, \ldots, z_n) := 
\lim_{r \rightarrow \infty}r^{-n}f(r,z_2,\ldots,z_m)$ is stable by 
Hurwitz' theorem hence $Q_n(\zeta_2,\ldots,\zeta_n)\neq 0$.
Let us now write $T[(z_1+w)^n]$ as 
$$
T[(z_1+w)^n] = \sum_{k=0}^n \binom n k T\left(z_1^{n-k}\right)w^k \in
 \HH_2(\CC).
$$
By Corollary \ref{polarizeit} we know that 
$$
 \sum_{k=0}^n T\left(z_1^{n-k}\right)e_k(w_1,\ldots, w_n) \in \HH_{n+1}(\CC).
$$ 
But then 
$$
T(f_\epsilon)(z_1, \zeta_2, \ldots, \zeta_m)=  C\sum_{k=0}^n 
T\left(z_1^{n-k}\right)e_k(-\xi_1,\ldots, -\xi_n) \in \HH_{1}(\CC), 
$$ 
which gives $T(f_\epsilon) \in \HH_m(\CC)$. Letting $\epsilon \rightarrow 0$ 
we have $T(f) \in \HH_m(\CC)\cup\{0\}$. 
If $f \in \HH_m(\CC)$ is of degree less than $n$ in $z_1$ we may consider 
$f^\epsilon=(1-\epsilon i z_1)^{n-\deg f} f \in \HH_m(\CC)$.  Then by the 
above  
one has $T(f^\epsilon) \in  \HH_n(\CC)\cup\{0\}$ for all $\epsilon>0$. The 
lemma now follows from Hurwitz' theorem by letting $\epsilon \rightarrow 0$. 
\end{proof} 


We are now ready to prove Theorem \ref{finitestab}. 
\begin{proof}[Proof of Theorem \ref{finitestab}]
If $T[(z+w)^n] \in \HH_2(\CC)$ then by applying Lemma \ref{extension} with 
$m=1$ it follows that $T$ is stability 
preserving.

Suppose now that $T$ preserves stability. Assume first that there exists 
$w_0\in\bC$ with $\Im(w_0)>0$ such that $(z+w_0)^n$ is in the kernel of $T$. 
Since $(z+w_0)^n$ is strictly stable it follows from  Lemma \ref{degenerate} 
and Lemma \ref{spaces}  that 
$\dim_{\bC} T(\CC_n[z]) \leq 1$. Hence $T$ is given by $T(f) = \alpha(f)P$, 
where $P$ is a fixed stable 
polynomial and $\alpha : \CC_n[z]  \rightarrow \CC$ is a linear functional. 
Otherwise we may assume that  $T[(z+w_0)^n] \in \HH_1(\CC)$ for all 
$w_0 \in \CC$ with 
$\Im(w_0) >0$ and conclude that $T[(z+w)^n] \in \HH_2(\CC)$. 
\end{proof}

The proof of Theorem \ref{finitehyp} now follows easily. 

\begin{proof}[Proof of Theorem \ref{finitehyp}]
Recall Notation~\ref{not4} and note that by Lemma \ref{trichotomy} we may 
assume that $\dim_{\bR} T(\RR_n[z]) > 2$,  so that 
$T$ is either stability reversing or stability preserving. By 
Theorem \ref{finitestab} $T$ is 
stability reversing or stability preserving if and only if 
$T[(z+w)^n] \in \HH_2(\CC)$ or 
$T[(z-w)^n] \in \HH_2(\CC)$, respectively, which proves the theorem. 
\end{proof}

\begin{proof}[Proof of Theorem \ref{finitehypC}]
By Theorem \ref{finitehyp} it suffices to prove that if a linear operator  
$T : \CC_n[z] \rightarrow \CC[z]$ 
satisfies $T : \pi_n(\RR) \rightarrow \pi(\RR)$ then either 
\begin{itemize}
\item[(a)] There exists $\theta \in \RR$ such that $T=e^{i\theta}\tilde{T}$, 
where $\tilde{T}: \RR_n[z] \rightarrow \RR[z]$ is 
a hyperbolicity preserver when restricted to $\RR_n[z]$, or 
\item[(b)] $T$ is given by $T(f) = \alpha(f)P$, where 
$\alpha : \CC_n[z] \rightarrow \CC$ is a linear functional and $P$ is a 
hyperbolic polynomial. 
\end{itemize}
We prove this using induction on $n \in \NN$.  
If $n=0$ there is nothing to prove so we may assume that $n$ is a positive 
integer. Note that $T$ restricts to 
a linear operator $T' : \pi_{n-1}(\RR) \rightarrow \pi(\RR)$ and that by 
induction $T'$ must be of the form (a) or (b) above. Suppose that 
$T'=e^{i\theta}\tilde{T}'$, where $\tilde{T}'$ is a hyperbolicity preserver 
up to degree $n-1$. If $T(z^n)=e^{i\theta}f_n$, where $f_n \in \RR[z]$ 
(actually, $f_n\in\HH_1(\bR)\cup\{0\}$), then $T$ is of the form (a). Hence 
we may assume that $T(z^n)= e^{i\gamma}f_n$, where 
$0 \leq \gamma < 2\pi$, $\gamma- \theta$ is not an integer multiple of 
$\pi$ and 
$f_n$ is a hyperbolic polynomial. Suppose that there is an integer $k < n$ 
such that $T(z^k)$ is not a 
constant multiple of $f_n$. Let $M$ be the largest such $k$ and set 
$R(z)=e^{-i\theta}T(z^M)$. Then 
$$
e^{-i\theta}T\!\left[z^M(1+z)^{n-M}\right] 
= R(z)+ \left(r+e^{i(\gamma-\theta)}\right)f_n(z)
$$
for some  $r \in \RR$. But this polynomial is supposed to be a complex 
constant multiple of 
a hyperbolic polynomial, which can only happen if $R$ and thus 
$T\left(z^M\right)$ is a constant multiple of $f_n$.
This contradiction means that $T$ must be as in (b) above with $P=f_n$. 

Assume now that $T'$ is as in (b). 
If $T(z^n)$ is a constant multiple of $P$ there is nothing to prove, so we 
may assume that $T(z^n)=e^{i\theta}f_n$, where $0 \leq \theta < 2\pi$ and 
$f_n$ is a hyperbolic polynomial which is not a constant multiple of $P$. 
Suppose that there is an integer $k <n$ such 
that $\alpha(z^k)e^{-i\theta} \notin \RR$ and let $M$ be the largest such 
integer. Then 
$$
e^{-i\theta}T\!\left[z^M(1+z)^{n-M}\right]
= \left(\alpha\!\left(z^M\right)e^{-i\theta}+r\right)P(z) + f_n(z)
$$
for some $r \in \RR$. However, the latter polynomial should be a complex 
constant multiple of 
a hyperbolic polynomial and this can happen only if  
$\alpha(z^M)e^{-i\theta} \in \RR$, which 
contradicts the above assumption. This means that $T$ must be as in (a). 
\end{proof}

\begin{proof}[Proof of Corollary~\ref{cor-alghyp}]
Note first that if $T:\bR[z]\to \bR[z]$ is as in (a), (b) or (c) of 
Corollary \ref{cor-alghyp} then by Theorem~\ref{finitehyp} we have that $T$ 
preserves hyperbolicity up to any degree $n\in\bN$. Conversely, if 
$T:\bR[z]\to \bR[z]$ preserves hyperbolicity then for any $n\in\bN$ the 
restriction $T:\bR_n[z]\to \bR[z]$
preservers hyperbolicity (up to degree $n$). The case when 
$\dim_{\RR} T(\RR[z])\le 2$ is clear. Suppose now that 
$\dim_{\RR} T(\RR[z])>2$ and that 
$T[(z+w)^n] \in \HH_2(\RR)$ for some $n\in\bN$. Then by 
Lemma \ref{extension} we have that 
$T[(z+w)^m] \in \HH_2(\CC)\cup\{0\}$ for all $m \leq n$ and since the latter 
polynomial has real coefficients we get $T[(z+w)^m] \in \HH_2(\RR)\cup\{0\}$ 
for all $m \leq n$. Similarly, if $T[(z-w)^n] \in \HH_2(\RR)$ then 
$T[(z-w)^m] \in \HH_2(\RR)\cup\{0\}$ for all $m \leq n$. It follows that if 
$\dim_{\RR} T(\RR[z])>2$ then 
either  $T[(z+w)^n] \in \HH_2(\RR)\cup\{0\}$ for all $n \in \NN$ or 
$T[(z-w)^n] \in \HH_2(\RR)\cup\{0\}$ for all $n \in \NN$.
\end{proof}

By appropriately modifying the arguments in the proof of 
Corollary~\ref{cor-alghyp} one can easily check that 
Corollary~\ref{cor-algstab} follows readily from Theorem~\ref{finitestab}.
