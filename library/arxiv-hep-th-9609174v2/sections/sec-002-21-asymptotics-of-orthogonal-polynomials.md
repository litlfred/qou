---
doc_id: arxiv-hep-th-9609174v2
doc_title: "arXiv:hep-th/9609174v2 23 Sep 1996"
section_id: sec-002-21-asymptotics-of-orthogonal-polynomials
section_title: "Asymptotics of orthogonal polynomials"
section_number: 2.1
pages: 5-8
source_pdf: 9609174v2.pdf
source_sha256: 87885f4d03661f26
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.984
latex_coverage_ratio: 0.97
doc_brief: "arXiv:hep-th/9609174v2 23 Sep 1996 — We prove the universality of correlation functions of chiral unitary and unitary ensembles of ran- dom matrices in the microscopic limit."
---
We shall prove the following theorem on the asymptotic behavior 
of these orthogonal polynomials:
\begin{quote}
{\bf Theorem 1}:\  
{\it
Let $\{P^{(\alpha)}_n(\lambda)\}_{n=0,1,\cdots}$ be 
the set of polynomials orthogonal 
with respect to the measure} 
\[
\d \lambda\, \lambda^\alpha\,\e^{-N\,V(\lambda)},\ \ \ 
V(\lambda)=\sum_{k\geq 1} \frac{g_k}{k}\,\lambda^k,\ \ \ 
\alpha=0,1,\cdots
\]
{\it over the range $[0,\infty)$, whose moments are all finite.
If the polynomials can be normalized according to 
$P^{(\alpha)}_n(0)=1$,
then, for fixed $x=N^2\lambda$ and $t=n/N$, 
the following limiting relation holds:}
\begin{equation}
\lim_{N\rightarrow\infty} \left.
P^{(\alpha)}_{n}( \frac{x}{N^2})\right|_{n=Nt}=
\alpha !\,
 \frac{J_\alpha\left(u(t)\sqrt{x}\right)}{\left(u(t)
\sqrt{x}/2\right)^\alpha} ,
\label{Jalpha}
\end{equation}
{\it where $u(t)$ is determined by}
\[
u(t)=\int_0^t \frac{\d t'}{\sqrt{r(t')}},\ \ \ \  
t= \sum_k \frac{g_k}{2} \left(2k \atop k \right) r(t)^k.
\]
\end{quote}
The proof of this theorem for $\alpha=0$ was recently given by one of
the authors \cite{Nis}, and is reproduced here for completeness. 
The central idea of how to prove it for arbitrary
$\alpha = 1, 2, \ldots$ is to use induction, starting with the case 
$\alpha = 0$. Tracing it back, this means that the Bessel-type behavior
of the polynomials is a consequence of the three-term
recursion relation for the orthogonal polynomials.
As $n, N \rightarrow \infty$ with
$t = n/N$ fixed, this yields a certain ``continuum limit'' reminiscent
of the derivation of string equations in the double-scaling limit. The
recursion relations thus become the defining second order differential
equations for Bessel (and Neumann) functions. 
It is the boundary conditions
that finally uniquely specify the Bessel solutions. 
However, for simplicity we shall here show the proof by induction.

\vspace{12pt}\noindent
We start with the case $\alpha = 0$.
The recursion relation for 
$P_n(\lambda) \equiv P^{(0)}_n(\lambda)$ takes the form
(with $h_n \equiv h^{(0)}_n$ and $p_n \equiv p^{(0)}_n$):
\begin{eqnarray}
\lambda\,P_n(\lambda)&=&
-r_{n}\left\{ P_{n+1}(\lambda)- P_n(\lambda)
-\frac{h_{n}}{r_n}\frac{r_{n-1}}{h_{n-1}} 
\left( P_{n}(\lambda)-P_{n-1}(\lambda) 
\right) \right\} \ \ \ \ 
\left( r_n\equiv-\frac{p_{n}}{p_{n+1}}\right)
\nonumber\\
&\equiv& \sum_m \hat{\lambda}_{nm}\,P_m(\lambda). 
\label{3t-recII}
\end{eqnarray}
This is the well-known three-term recursion relation
rewritten in our nonmonic normalization. 
The structure of the coefficients is dictated by a comparison of
$O(\lambda^0)$ and $O(\lambda^{n+1})$ terms on both sides.
The sets of unknowns $\{h_n\}$, $\{r_n\}$ can  
be determined iteratively by
\begin{eqnarray}
&&1=
-\int_0^\infty 
\d\lambda \frac{\d}{\d\lambda} \left\{ 
\e^{-N\,V(\lambda)}P_n(\lambda)\,P_{n}(\lambda) \right\}=
N\,V'(\hat{\lambda})_{nn}\, h_n ,
\label{vnn}\\
&&0=
-\int_0^\infty 
\d\lambda \frac{\d}{\d\lambda} \left\{ 
\e^{-N\,V(\lambda)}\lambda\,P_{n}(\lambda)\,
P_{n}(\lambda) \right\}=
\left( N (\hat{\lambda}V'(\hat{\lambda}))_{nn}
-2n-1 \right) h_{n}.
\label{vnn-1}
\end{eqnarray}

\vspace{12pt}\noindent
In the following we need to know 
the asymptotic behavior of 
$r_n$ and $h_n$ for 
\begin{equation}
n,\ N\rightarrow \infty\ \ ~~~  
\mbox{while}~~\ \ \frac{n}{N}=t\ ~~ \mbox{is kept fixed}.
\label{lim}
\end{equation}
Eqs.~(\ref{3t-recII}), (\ref{vnn}) and (\ref{vnn-1}) 
tell us that
they should behave as
\begin{equation}
r_n=r\left(\frac{n}{N}\right)
+ \mbox{~~higher orders in ~}\frac{1}{N} ~,~~~ \ \ \ 
h_n=\frac{1}{N}\, h\left(\frac{n}{N}\right)
+ \mbox{~~higher orders in ~}\frac{1}{N}. 
\end{equation}
Then the leading behavior of the matrix $\hat{\lambda}$
and its powers is
\begin{eqnarray}
&&\hat{\lambda}_{nm}= r(\frac{n}{N})
\left(
-\delta_{n\,m-1}+2\delta_{n m}-\delta_{n\,m+1}
\right), \nonumber\\
&&(\hat{\lambda}^k)_{nm}= r(\frac{n}{N})^k
\sum_{\ell=-k}^k (-)^\ell \left( {2k \atop k+\ell} \right)
\delta_{n\,m+\ell}
\end{eqnarray}
so that eqs.~(\ref{vnn}) and (\ref{vnn-1}) read
\begin{eqnarray}
\sum_{k} g_k \left({2k-2\atop k-1}\right) 
r(t)^{k-1}
&=&
\frac{1}{h(t)} ,
\label{vNN}\\
\frac12 \sum_{k} g_k \left({2k \atop k}\right) 
r(t)^{k} 
&=&t.
\label{qn}
\end{eqnarray}
Note that eqs.~(\ref{vNN}) and (\ref{qn}) 
imply a universal relationship
among total derivatives,
\begin{equation}
\d t=
2r\,\d\left( \frac1h \right) + \frac{1}{h} \d r
=\sqrt{r}\, \d \left( \frac{2\sqrt{r}}{h} \right).
\label{dt}
\end{equation}

\vspace{12pt}\noindent
Next we expand the right hand side of the recursion relation 
(\ref{3t-recII}) in terms of $1/N$ in the limit (\ref{lim}) to get
\begin{equation}
N^2 \lambda \, P(n,N,\lambda) =
-r(t)\left\{\frac{\d^2\,P}{\d t^2}+
\frac{h(t)}{r(t)}
 \left( \frac{\d}{\d t}  \frac{r(t)}{h(t)}\right) \frac{\d P}{\d t}
\right\}
=
-h(t) \frac{\d}{\d t}  \frac{r(t)}{h(t)} \frac{\d}{\d t}
 P(n,N,\lambda) ,
\label{diff-eq}
\end{equation}
where the argument $N$ in 
$P(n, N, \lambda)\equiv P_n(\lambda)$ is to indicate 
explicitly the dependency via the coefficient 
in front of the potential.
Only the leading terms up to $O(1/N)$ have been kept here.
Eq.~(\ref{diff-eq}) tells us that that the arguments of the polynomial
appear
only in the combinations $t=n/N$ and $x=N^2\lambda$
in the large-$N$ limit.
The rescaled eigenvalue coordinate $x$ is to be fixed finite hereafter,
and is regarded as a parameter 
in the ordinary differential equation in $t$.
Performing the change of variable
\begin{equation}
t \mapsto u(t)\equiv \frac{2\sqrt{r(t)}}{h(t)}=
\int_0^t \frac{\d t'}{\sqrt{r(t')}},
\end{equation}
using the relationship (\ref{dt}),
and neglecting higher order terms in $1/N$,
eq.~(\ref{diff-eq}) 
reduces to Bessel equation of zeroth order:
\begin{equation}
\left(
\frac1u \frac{\d}{\d u}  u \frac{\d}{\d u} +x
\right)
P(u,x)=0.
\end{equation}
The unique solution to this equation which satisfies
the following boundary condition at $t=n/N=0$ ($u(0)=0$),
\begin{equation}
P(0, x)=P_0(\lambda)=1 ,
\end{equation}
is
\begin{equation}
P(u,x)=J_0\left( u\sqrt{x} \right) .
\label{Bes0}
\end{equation}

\vspace{12pt}\noindent
We now proceed for a generic integer $\alpha$ by induction.
Given a set of polynomials $\{P^{(\alpha)}_n(\lambda)\}$
which are orthogonal with respect to the measure 
$\d\lambda \,\lambda^\alpha\,\e^{-NV(\lambda)}$
on $[0,\infty)$,
and are normalized by $P^{(\alpha)}_n(0)=1$ as in eq.~(\ref{normal}), 
we note that
\begin{equation}
\tilde{P}_n^{(\alpha+1)}(\lambda) \equiv 
\frac{P^{(\alpha)}_{n+1}(\lambda)-P^{(\alpha)}_n(\lambda)}{\lambda}
\label{Ptn+1}
\end{equation}
are polynomials of order $n$. They are orthogonal to
$\lambda^k$, 
$k=0,\cdots,n-1$
with respect to the measure 
$\d\lambda\,\lambda^{\alpha+1}\,\e^{-NV(\lambda)}$
\cite{Sze}:
\begin{eqnarray}
&&\int_0^\infty \d\lambda\,\lambda^{\alpha+1}\,\e^{-NV(\lambda)}
\tilde{P}_n^{(\alpha+1)}(\lambda) \,\lambda^k
\nonumber\\
&=&\int_0^\infty \d\lambda\,\lambda^{\alpha}\,\e^{-NV(\lambda)}
\left( P^{(\alpha)}_{n+1}(\lambda)-P^{(\alpha)}_n(\lambda) \right)
\lambda^k =0.
\end{eqnarray}
Under the assumption that $\tilde{P}_n^{(\alpha+1)}(0)\neq 0$,
the orthogonal polynomial normalized to ${P}_n^{(\alpha+1)}(0) =1$
is thus given by
\begin{equation}
P^{(\alpha+1)}_n(\lambda) =
\frac{\tilde{P}_n^{(\alpha+1)}(\lambda) }{\tilde{P}_n^{(\alpha+1)}(0)}.
\label{Pn+1}
\end{equation}
The microscopic limit of the contiguous relation (\ref{Ptn+1}) reads
\begin{equation}
\tilde{P}^{(\alpha+1)}_{Nt} (\frac{x}{N^2})=
\frac{N}{x}\frac{\partial}{\partial t} 
P^{(\alpha)}_{Nt} (\frac{x}{N^2})
+ \mbox{~~higher orders in ~}\frac{1}{N}.
\end{equation}
If we substitute eq.~(\ref{Jalpha}) 
for a given $\alpha$ into the above, we confirm that
\begin{eqnarray}
\tilde{P}^{(\alpha+1)}_{Nt} (\frac{x}{N^2})&=&
-N\, \frac{\alpha!}{\sqrt{r(t)}}
\frac{
J_{\alpha+1}\left(u(t)\sqrt{x}\right)}{\left(u(t)/2\right)^\alpha
(\sqrt{x})^{\alpha+1}},
\\
\tilde{P}^{(\alpha+1)}_{Nt} (0)&=&
-N\,\frac{u(t)/2}{(\alpha+1)\sqrt{r(t)}}.
\end{eqnarray}
Thus eq.~(\ref{Jalpha}) holds also for $\alpha+1$ 
after normalizing according to (\ref{Pn+1}).
Together with the result (\ref{Bes0}) for $\alpha=0$,
this completes the proof.

\vspace{12pt}\noindent
We have worked out 
an alternative proof of the same
theorem, which does not rely on induction. 
Rather, it is possible to convert the recursion relation for 
$P^{(\alpha)}_n(\lambda)$
directly into Bessel equation of order $\alpha$,
$\left( \frac{1}{u^{2\alpha+1}}\frac{\d}{\d u}
u^{2\alpha+1}\frac{\d}{\d u}
+x\right)P^{(\alpha)}(u,x)=0$.
Since it is lengthy, we do not reproduce it here.
