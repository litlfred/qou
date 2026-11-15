---
doc_id: arxiv-0707.2340v2
doc_title: "NEGATIVE DEPENDENCE AND THE GEOMETRY OF POLYNOMIALS"
section_id: sec-020-7-negative-results-on-negative-dependence
section_title: "Negative Results on Negative Dependence"
section_number: 7
pages: 41-45
source_pdf: 0707.2340v2.pdf
source_sha256: bf0f91277a5874ff
toc_source: outline
text_source: latex
latex_prose_ratio: 0.977
latex_coverage_ratio: 0.952
doc_brief: "NEGATIVE DEPENDENCE AND THE GEOMETRY OF POLYNOMIALS — We introduce the class of strongly Rayleigh probability measures by means of geometric properties of their generating polynomials that amount to"
---
\label{s-countex}

We will now use the results from the previous 
sections, in particular those of \S \ref{Almost}, to construct
counterexamples to the general cases of Pemantle's and Wagner's conjectures
on ULC rank sequences (Conjectures~\ref{c-p}--\ref{cna-ulc}) and   
Pemantle's conjecture
on stochastic domination and truncations 
(Conjecture~\ref{st}). We also answer in the negative  
some related problems as well as Problem~\ref{prob-phr-cna} and 
\cite[Problem 6]{BBCV}.
 
\begin{proof}[Counterexample 1]
Suppose that $\mu$ is a probability measure on $2^{[n+1]}$ whose 
generating polynomial 
$$
f(z_1,\ldots, z_{n+1})= 
z_{n+1}\sum_{k=0}^{n}a_ke_k(z_1,\ldots, z_n)+
\sum_{k=0}^{n}b_ke_k(z_1,\ldots, z_n)
$$
is symmetric in its first $n$ variables. Clearly, 
$$
\De(f)(t)=\sum_{k=0}^{n+1}\binom {n+1} k c_kt^k
=\sum_{k=0}^{n+1}\!\left[\binom n {k-1} a_{k-1}+\binom n k b_k\right]\!t^k, 
$$
where
$$
c_k = \frac{ka_{k-1}+(n+1-k)b_k}{n+1}.
$$
In light of Proposition \ref{RAS} and Corollary \ref{RandC},  
Conjectures~\ref{big} and \ref{cna-ulc} reduce to the following problem in 
the almost exchangeable case.  

\begin{problem}\label{p1}
Let $\{a_k\}_{k=0}^m$, $\{b_k\}_{k=0}^m$ be two non-negative sequences  
satisfying 
\begin{enumerate}
\item $\{\theta a_k+(1-\theta) b_k\}_{k=0}^m$ is LC 
for all $0\leq \theta \leq 1$, and 
\item $a_kb_{k+1} \geq a_{k+1}b_k$ for $0 \leq k \leq m-1$.
\end{enumerate}
Is it true that the sequence 
$$
\left\{ka_{k-1}+(m+1-k)b_k\right\}_{k=0}^{m+1},\,\text{ where }
a_{-1}=b_{m+1}=0, 
$$
is LC? 
\end{problem}

A related problem is the following.

\begin{problem}\label{p2}
Let $\{a_k\}_{k=0}^n$, $\{b_k\}_{k=0}^n$ be two non-negative sequences  
satisfying 
\begin{enumerate}
\item $\{\theta a_k+(1-\theta) b_k\}_{k=0}^n$ is LC 
for all $0\leq \theta \leq 1$, and 
\item $a_kb_{k+1} \geq a_{k+1}b_k$ for $0 \leq k \leq n-1$.
\end{enumerate}
Is it true that the sequence 
$$
\left\{ka_{k-1}+b_k\right\}_{k=0}^{n+1},\,\text{ where }\, a_{-1}=b_{n+1}=0, 
$$
is LC?
\end{problem}

Note that a counterexample $\{a_k\}_{k=0}^n$, $\{b_k\}_{k=0}^n$ to 
the latter problem would actually give a counterexample  to 
the former as well. This is
 because for some large integer $m\geq n$  the sequence $\{d_k\}_{k=0}^m$ 
defined by 
\begin{equation}\label{count-m}
d_k= ka_{k-1}+\frac {m+1-k} m b_k,\,\text{ where }\,     
d_k=0 \mbox{ if } k >n+1,
\end{equation}
will fail to be LC and the sequences  $\{a_k\}_{k=0}^m$ and 
$\{b_k/m\}_{k=0}^m$ 
will therefore constitute a counterexample to Problem~\ref{p1}. 

It remains to find negative solutions to Problems~\ref{p1} and \ref{p2}.   
Set 
$$a_0=2t^2,\quad a_1=2t,\quad a_2=\frac{4}{9}-t,\quad a_3=\frac{2}{3},\quad 
a_4=1,\quad a_5=\frac{2}{3}t,$$
$$b_0=9t^3,\quad b_1=9t^2,\quad b_2=3t,\quad b_3=1,\quad b_4=3,\quad b_5=9-t.$$
For $t$ sufficiently small and positive this is seen to be a negative 
solution to Problem~\ref{p2}. Indeed, 
\begin{equation*}
\begin{split}
&\lambda a_0+b_0=t^2(2\lambda+9t),\,\,\, \lambda a_1+b_1=t(2\lambda+9t),
\,\,\, \lambda a_2+b_2
=\left(\frac{4}{9}-t\right)\lambda+3t,\\
&\lambda a_3+b_3=\frac{2}{3}\lambda +1,\,\,\, \lambda a_4+b_4=\lambda+3,
\,\,\, \lambda a_5+b_5
=\frac{2}{3}t\lambda+9-t,
\end{split}
\end{equation*}
hence
$$(\lambda a_1+b_1)^2-(\lambda a_0+b_0)(\lambda a_2+b_2)
=t^2(2\lambda+9t)\left[\left(\frac{14}{9}+
t\right)\lambda+6t\right]\ge 0,$$
$$(\lambda a_2+b_2)^2-(\lambda a_1+b_1)(\lambda a_3+b_3)
=\lambda^2\left[\left(\frac{4}{9}-t\right)^2
-\frac{4}{9}t\right]+2t\lambda \left(\frac{1}{3}-6t\right)\ge 0,$$
$$(\lambda a_3+b_3)^2-(\lambda a_2+b_2)(\lambda a_4+b_4)
=t\lambda^2+(1-9t)\ge 0,$$
$$(\lambda a_4+b_4)^2-(\lambda a_3+b_3)(\lambda a_5+b_5)
=\left(1-\frac{4}{9}t\right)\lambda^2
+t\ge 0$$
for any $\lambda \ge 0$ if e.g.~$0<t\le \frac{1}{20}$. Moreover,
$$a_0b_1-a_1b_0=0,\quad a_1b_2-a_2b_1=t^2(2+9t)\ge 0,\quad a_2b_3-a_3b_2=
\frac{4}{9}-3t\ge 0,$$
$$a_3b_4-a_4b_3=1,\quad a_4b_5-a_5b_4=9-3t\ge 0$$
for $0<t\le\frac{4}{27}$. However, 
$$
(b_4+4a_3)^2-(b_3+3a_2)(b_5+5a_4)= -\frac{5}{9}+\frac{133}{3}t-3t^2<0 
$$
for $0<t \leq \frac{1}{80}$. Thus, if $0<t\le \frac{1}{80}$ then both 
sequences $\{a_k\}_{k=0}^5$ and $\{b_k\}_{k=0}^5$ are positive  and satisfy 
conditions (1) and (2) in 
Problems~\ref{p1} and \ref{p2}. By taking e.g.~$t=10^{-4}$ one can then 
check that the corresponding sequences $\{a_k\}_{k=0}^m$ and 
$\{b_k/m\}_{k=0}^m$ constructed in \eqref{count-m} produce a 
counterexample to Problem~\ref{p1} for any integer $m\ge 19$. Therefore, 
both Conjecture~\ref{big} and Conjecture~\ref{cna-ulc} fail whenever the 
(total) number 
of variables satisfies $n+1\ge 20$. 

We note that our construction disproves slightly more than 
Conjecture~\ref{big} and Conjecture~\ref{cna-ulc}. Indeed, 
the rank sequence of the measures obtained in this fashion 
(i.e., measures  
on $2^{[m+1]}$ with a generating polynomial of the form 
$$
z_{m+1}\sum_{k=0}^{m}a_ke_k(z_1,\ldots,z_m)+
\sum_{k=0}^{m}\frac{b_k}{m}e_k(z_1,\ldots,z_m),
$$
where $m\ge 19$ and $\{a_k\}_{k=0}^{m}$, $\{b_k\}_{k=0}^{m}$ are 
the sequences constructed above with $t=10^{-4}$)  
is not even SLC, which is weaker than ULC (Definition~\ref{d-ulc}). 

In \cite[Problem 6]{BBCV} it was 
asked whether Conjecture~\ref{big} would hold under the additional assumption
that the Rayleigh measure $\mu$ is decreasing on $2^{[n+1]}$, i.e., 
the coefficients of its generating polynomial $\sum a_Sz^S$ satisfy the
monotonicity condition $a_S\ge a_T$ whenever $S\subseteq T\subseteq [n+1]$. 
This fails as well, since if $f$ is as in the above construction with
$n+1\ge 20$, then the polynomial $f(\lambda z_1,\ldots,\lambda z_{n+1})$ is 
still Rayleigh and  
satisfies the additional monotonicity assumption stated above for all 
sufficiently small $\lambda\in\RR_+$, but its
rank sequence $\{\lambda^{k}r_k\}_{k=0}^{n+1}$ is not ULC.
\end{proof}

\begin{remark}\label{r-other-w}
In \cite{W} it was shown that Conjectures 3.11 and 3.4 in 
{\em loc.~cit.~}are equivalent and would follow from either Conjecture 3.13 or
Conjecture 3.14 in that same paper. Counterexample 1 above shows that all these
conjectures fail.
\end{remark}

Next we show that the above construction actually yields a counterexample to 
Conjecture~\ref{st} as well. 

\begin{proof}[Counterexample 2]
Let $$f(z_1,\ldots,z_{n+1})
= z_{n+1}\sum_{j=0}^n a_je_j(z_1,\ldots, z_n) + 
\sum_{j=0}^n b_je_j(z_1,\ldots, z_n)$$ 
be the $n+1=20$ variable polynomial in the previous counterexample 
and let $\mu$ be the 
corresponding probability measure in $\fP_{n+1}$, so that $\mu$ is CNA+. 
For $\AS=\{ S  \in 2^{[n+1]} : n+1 \in S \}$ we have 
$$
\mu_k(\AS) = \frac {a_{k-1} \binom n {k-1}}{a_{k-1}\binom n {k-1}
+b_k\binom n {k}}, \quad \quad 
\mu_{k+1}(\AS) = \frac {a_{k} \binom n {k}}{a_{k}\binom n {k}
+b_{k+1}\binom n {k+1}}.
$$
Hence, 
$$\mu_k(\AS) \leq \mu_{k+1}(\AS) \quad \Longleftrightarrow \quad a_{k-1} 
\binom n {k-1}b_{k+1}\binom n {k+1} \leq a_{k} \binom n {k}b_k\binom n {k} .$$
This fails for $k=3$ and $0<t<\frac{1}{18}$. 
\end{proof}

As we noted in \S \ref{s24}, a positive answer to Problem~\ref{prob-phr-cna}
would imply Conjecture~\ref{con-cna-R}. However, the answer to 
Problem~\ref{prob-phr-cna} is negative, which we will now prove. 

\begin{proof}[Counterexample 3]
We claim that if $\mu\in\fP_m$ satisfies 
\begin{enumerate}
\item $\mu$ is Rayleigh, 
\item $\mu=\theta \mu_k +(1-\theta)\mu_{k+1}$ for some $0<\theta<1$, 
\item $\mu_k \not \pc \mu_{k+1}$, 
\end{enumerate}
where $\mu_k,\mu_{k+1}$ are the truncations of $\mu$ as in 
Definition~\ref{d-trunc}, then $\mu$ is not PHR (projection of a 
Rayleigh measure with homogeneous generating polynomial, 
cf.~Definition~\ref{phr}). 
To prove this claim, let $g_k$ and $g_{k+1}$ be the generating 
polynomials for $\mu_k$ and $\mu_{k+1}$, respectively, and suppose that 
$$
f(z_1,\ldots,z_\ell)=h_{1}(z_{m+1},\ldots, z_\ell)g_k(z_1,\ldots,z_m)
+h_2(z_{m+1},\ldots, z_\ell)g_{k+1}(z_1,\ldots,z_m),
$$
is a homogeneous Rayleigh polynomial that projects to 
$\theta g_k +(1-\theta)g_{k+1}$ and has a minimal number of 
variables $\ell\ge m+1$. If the same variable, say $z_j$, appears in both 
$h_{1}(z_{m+1},\ldots, z_\ell)$ and $h_2(z_{m+1},\ldots, z_\ell)$, 
then we can differentiate $f$ with respect to $z_j$ and get a new 
homogeneous polynomial in fewer variables that still projects to 
$\theta g_k +(1-\theta)g_{k+1}$. Moreover, if either 
$h_{1}(z_{m+1},\ldots, z_\ell)$ or  
$h_2(z_{m+1},\ldots, z_\ell)$ is the positive sum of several monomials we 
could set a variable equal to zero and again get a polynomial in fewer 
variables with the desired properties. Hence, both  
$h_{1}(z_{m+1},\ldots, z_\ell)$ and $h_2(z_{m+1},\ldots, z_\ell)$ are 
monomials and by the minimality of $\ell$ we have that $\ell=m+1$ and
$$
f(z_1,\ldots,z_{m+1})= \theta z_{m+1}g_k(z_1,\ldots,z_m)
+(1-\theta)g_{k+1}(z_1,\ldots,z_m). 
$$
Since $f$ is a homogeneous Rayleigh polynomial, by Theorem \ref{PHR-NA} 
the corresponding measure $\mu_f\in\fP_{m+1}$ is (strongly) negatively 
associated. As in the proof of Proposition~\ref{stdom} we then deduce that 
$\mu_k  \pc \mu_{k+1}$, which contradicts assumption (3) above. 

It remains to find a measure $\mu$ satisfying properties (1)--(3) above.
If we let $\mu$ have generating polynomial a constant multiple of 
$$
z_{n+1}(a_2e_2(z_1,\ldots, z_n) + a_3e_3(z_1,\ldots, z_n))+ 
b_3e_3(z_1,\ldots, z_n) + b_4e_4(z_1,\ldots, z_n),
$$
where $m=n+1$ and $a_2,a_3, b_3, b_4$ are as in Counterexample 1, we see that 
$\mu$ satisfies all these three properties. 
Clearly, this counterexample fails to have a ULC rank sequence. Therefore, 
we conclude that not even the PHR property implies ULC. 
\end{proof}

\begin{remark}\label{r-strong-NA}
We note that to disprove just the strongest version of 
Pemantle's conjecture on ULC rank sequences (Conjecture~\ref{c-p}) we can 
simply invoke Example~\ref{ex2} in \S \ref{s21}, which combined with
Theorem~\ref{pro-w} shows that
Conjecture~\ref{c-p} actually fails even for symmetric measures. To give yet 
another
counterexample to Conjecture~\ref{c-p} we can 
also employ a construction used in \cite{L2}. Indeed, the measure in  
$\fP_4$ considered in \cite[Theorem 3.5]{L2} is seen to be NA but not ULC. 






























Note though that both examples mentioned 
above fail to be NLC (hence also CNA+, CNA, h-NLC+, h-NLC), so they do 
not provide counterexamples to the weaker conjectures (Conjectures~\ref{big}
and \ref{cna-ulc}). 




\end{remark}

\medskip

\noindent
{\bf Acknowledgements.} We would like to thank David Wagner for 
discussions pertaining to this project and the anonymous referee for useful 
comments and suggestions. The first author is 
partially supported by Swedish Research 
Council Grant 621-2005-870. The third author is supported by 
NSF Grant DMS-0301795.
