---
doc_id: arxiv-0707.2340v2
doc_title: "NEGATIVE DEPENDENCE AND THE GEOMETRY OF POLYNOMIALS"
section_id: sec-002-21-negative-dependence-concepts
section_title: "Negative Dependence Concepts"
section_number: 2.1
pages: 4-9
source_pdf: 0707.2340v2.pdf
source_sha256: bf0f91277a5874ff
toc_source: outline
text_source: latex
latex_prose_ratio: 0.972
latex_coverage_ratio: 0.975
doc_brief: "NEGATIVE DEPENDENCE AND THE GEOMETRY OF POLYNOMIALS — We introduce the class of strongly Rayleigh probability measures by means of geometric properties of their generating polynomials that amount to"
---
\label{s21}

Recall that a (real or complex) multivariate polynomial is said to be 
{\em multi-affine} 
if it has degree at most one in each variable. 
Denote by $\fP_n$, $n\in\NN$, the set of all 
probability measures on the Boolean algebra
$2^{[n]}$. (In the finite case we will always assume that the 
$\sigma$-algebra is the full algebra.) For $i\in [n]$ the $i$-th coordinate 
function on $2^{[n]}$ 
is an atomic (binary) random variable given by $X_i(S)=1$ if 
$i\in S$ and $0$ otherwise, where $S\subseteq [n]$, while the 
characteristic function $\chi_S$ of $S$ is defined by $\chi_S(T)=1$ if 
$T= S$ and $0$ otherwise.
Using the inclusion-exclusion principle one can show that any such 
characteristic function may be written as a multi-affine polynomial in 
$X_1,\ldots,X_n$. Any scalar function 
$F=\sum_{S\subseteq [n]}F(S)\chi_S$ on $2^{[n]}$ may therefore 
be viewed as a multi-affine polynomial in 
$X_1,\ldots,X_n$. By abuse of notation the latter is written as 
$F(X_1,\ldots,X_n)$ and then $\mu(F)=\int Fd\mu$. However, in what follows
the $X_i$'s always stand for (probabilistic) random variables and we will 
use other variables (such as $x,y,z,w$) when working with arbitrary 
functions/polynomials.

Let $\PP_n$ be the set of all multi-affine polynomials
in $n$ variables $f(z_1,\ldots,z_n)$ with non-negative coefficients such that
$f(\ben)=1$, where $\ben=(1,\ldots,1)\in\RR^n$ denotes the 
``all ones vector''. There is a 1-1 
correspondence between $\fP_n$ and $\PP_n$:
if $\mu\in\fP_n$ we may form its generating polynomial, namely 
$$
g_\mu(z) = \int z^{S} d\mu(S) = \sum_{S \subseteq [n]} \mu(S) z^S, \quad
z=(z_1,\ldots, z_n), \quad z^S:= \prod_{i \in S}z_i,
$$
and if 
\begin{equation}\label{coeff}
f(z)=\sum_{S\subseteq [n]}a_Sz^S\in\PP_n
\end{equation}
we define a measure $\mu_f$ on $2^{[n]}$ by setting $\mu_f(S)=a_S$, 
$S\subseteq [n]$. It is clear that $g_\nu\in\PP_n$, $\mu_f\in\fP_n$, 
$g_{\mu_f}=f$, and $\mu_{g_\nu}=\nu$ for any $\nu\in\fP_n$, $f\in\PP_n$. 
For convenience, we will sometimes use the symbol $\pa_i$ for $\pa/\pa z_i$
$1\le i\le n$, and the multi-index notation 
$\pa^S=\prod_{i\in S}\pa_i$, $S\subseteq [n]$. 

The NLC property for measures in $\fP_n$ 
translates into the corresponding property -- again called the 
{\em negative lattice condition} and denoted by NLC -- for polynomials in 
$\PP_n$: a polynomial $f\in\PP_n$ satisfies NLC if and only if its 
corresponding measure $\mu_f\in\fP_n$ does. This amounts to saying that
\begin{equation*}
\pa^S f(0,\ldots,0)\,\pa^T f(0,\ldots,0)\ge \pa^{S\cup T} 
f(0,\ldots,0)\,\pa^{S\cap T} f(0,\ldots,0), \tag*{(NLC)}
\end{equation*}
which in notation \eqref{coeff} becomes  
$a_Sa_T\ge a_{S\cup T}a_{S\cap T}$ for all $S,T\subseteq [n]$.

The so-called {\em ``closure'' operations}
discussed in e.g.~\cite[II.A]{P} may also be reformulated in terms of 
generating polynomials:

\begin{itemize}
\item[(i)] 
{\em Products.} If $\mu_1\in\fP_{n_1}$ has generating
polynomial $g_{\mu_1}(z_1,\ldots,z_{n_1})\in\PP_{n_1}$ and 
$\mu_2\in\fP_{n_2}$ has generating
polynomial $g_{\mu_2}(z_1,\ldots,z_{n_2})\in\PP_{n_2}$ then the product
$\mu_1\times \mu_2$ is the measure $\mu\in\fP_{[n_1+n_2]}$ with generating
polynomial
$g_\mu(z_1,\ldots,z_{n_1+n_2})
=g_{\mu_1}(z_1,\ldots,z_{n_1})g_{\mu_2}(z_{n_1+1},\ldots,z_{n_1+n_2})
\in\PP_{n_1+n_2}$.
\item[(ii)]
{\em Projections.} Given $S\subseteq [n]$ and $\mu\in\fP_n$ the 
projection of
$\mu$ onto $2^S$ is the measure $\mu'\in\fP_{|S|}$ with generating polynomial
$$g_\mu(z_1,\ldots,z_n)\big|_{z_i=1,\,i\in [n]\setminus S}\in\PP_{|S|}.$$
Note that in order for this definition 
to make sense we should also relabel the variables using indices in $[|S|]$. 
However, we allow ourselves this abuse of notation here and in what follows. 
\item[(iii)]
{\em Conditioning.} Let $\mu\in\fP_n$ with generating polynomial
$g_\mu(z_1,\ldots,z_n)\in\PP_n$ and fix some $i\in [n]$. The measure 
obtained from $\mu$ by conditioning the $i$-th random variable $X_i$ 
to be $0$ is the measure on $2^{[n]\setminus\{i\}}$ with generating polynomial
$$\frac{g_\mu(z_1,\ldots,z_n)\big|_{z_i=0}}
{g_\mu(z_1,\ldots,z_n)\big|_{z_i=0,\,z_j=1,\,j\neq i}}\in\PP_{n-1}$$
while the measure obtained from $\mu$ by conditioning $X_i$ 
to be $1$ is the measure on $2^{[n]\setminus\{i\}}$ with generating polynomial
$$\lim_{z_i\to\infty}\frac{g_\mu(z_1,\ldots,z_n)}
{g_\mu(z_1,\ldots,z_n)\big|_{z_j=1,\,j\neq i}}
=\frac{\pa_i g_\mu(z_1,\ldots,z_n)}
{\pa_i g_\mu(1,\ldots,1)}\in\PP_{n-1}.$$
Note that these conditional probability measures are well defined provided 
that the denominators appearing in the above expressions are non-zero.
\item[(iv)]
{\em External fields} (as pointed out in \cite[II.A]{P}, this name is 
borrowed 
from the Ising model). If  $\mu\in\fP_n$ has generating polynomial
$g_\mu(z_1,\ldots,z_n)\in\PP_n$ and $a_i$, $1\le i\le n$, are non-negative real
numbers then the measure obtained from $\mu$ by imposing the external field
$(a_1,\ldots,a_n)$ is the measure in $\fP_n$ with generating polynomial
$$\frac{g_\mu(a_1z_1,\ldots,a_nz_n)}{g_\mu(a_1,\ldots,a_n)}\in\PP_n,$$
which is well defined provided that $g_\mu(a_1,\ldots,a_n)\neq 0$.
\item[(v)]
{\em Symmetrization.} Denote the symmetric group on $n$ 
elements by $\mathfrak{S}_n$. For $\sigma\in \mathfrak{S}_n$ and 
$S\subseteq [n]$ let
$\sigma(S)=\{\sigma(s): s \in S\}$. Given $\mu\in\fP_n$ define a measure
$\sigma(\mu)\in\fP_n$ by setting $\sigma(\mu)(S)=\mu(\sigma(S))$, 
$S\subseteq [n]$. The (full or complete) symmetrization of 
$\mu$ is the measure 
$$\mu_s=\frac{1}{n!}\sum_{\sigma\in\mathfrak{S}_n}\sigma(\mu)\in \fP_n.$$ 
Note that the generating polynomial of $\mu_s$ is
\begin{equation}\label{sym}
\begin{split}
g_{\mu_s}(z)=\frac{1}{n!}\sum_{\sigma\in\mathfrak{S}_n}
g_{\sigma(\mu)}(z)
&=\frac{1}{n!}\sum_{\sigma\in\mathfrak{S}_n}\sum_{S\subseteq [n]}
a_{\sigma(S)}z^S\\
&=\sum_{k=0}^{n}\frac{\sum_{|S|=k}a_S}{\binom{n}{k}}
e_k(z_1,\ldots,z_n)\in\PP_n,
\end{split}
\end{equation}
where $\sum_{S\subseteq [n]}a_{S}z^S=g_{\mu}(z)$ and $e_k$, $0\le k\le n$, 
is the $k$-th elementary symmetric function (see \cite[\S 3.4]{W} for a proof
of the last identity). 
\item[(vi)]
{\em Partial symmetrization.} Let $\mu\in\fP_n$, $0\leq \theta \leq 1$, 
$1\leq i<j \leq n$, and $\tau=(ij)\in\mathfrak{S}_n$ be the transposition that 
permutes $i$ and $j$. The partial symmetrization of $\mu$ with respect to
$\tau$ and $\theta$ is the measure 
\begin{equation}\label{t-theta}
\mu^{\tau,\theta}
=\theta\mu+(1-\theta)\tau(\mu)\in\fP_n
\end{equation}
whose generating polynomial is obviously 
$g_{\mu^{\tau,\theta}}=\theta g_{\mu}+(1-\theta)g_{\tau(\mu)}\in\PP_n$.
\end{itemize}

\begin{remark}\label{r-complex}
All these ``closure'' operations are in fact well defined for arbitrary 
complex measures on $2^{[n]}$ if one drops the normalization factors 
appearing in the denominators of the
above expressions (these were used just to make sure that the resulting 
measures are again probability measures). 
In \S \ref{s-stable} we will actually use the partial symmetrization 
procedure \eqref{t-theta} for complex measures on $2^{[n]}$.
\end{remark}

The corresponding ``closure'' operations for generating polynomials -- i.e., 
{\em products}, 
{\em projections}, {\em conditioning}, {\em external fields}, 
{\em symmetrization}, {\em partial symmetrization} and {\em truncations} 
(cf.~Definition \ref{d-trunc} in \S \ref{s24})-- 
are defined simply by considering the resulting 
polynomials for each of the operations discussed above for measures.

\begin{definition}\label{d-exc}
A complex measure $\mu$ on $2^{[n]}$ is called {\em symmetric} or
{\em exchangeable} if $\sigma(\mu)=\mu$ for any $\sigma\in \mathfrak{S}_n$,
or equivalently, its generating polynomial $g_\mu$ is symmetric in all $n$
variables. We say that $\mu$ is {\em almost symmetric} or {\em almost
exchangeable} if $g_\mu$ is symmetric in all but possibly one variable. 
\end{definition}

\begin{definition}\label{d-inc-ev}
If $\mathcal{A}$ is a collection of subsets of $[n]$ we let 
$\chi_{\mathcal{A}} : 2^{[n]} \rightarrow \RR$ be the characteristic function 
of $\mathcal{A}$ defined by 
$\chi_{\mathcal{A}}(S) = 1$ if $S \in \mathcal{A}$ and 
$\chi_{\mathcal{A}}(S) = 0$ if $S \notin \mathcal{A}$.
An {\em increasing event} $\mathcal{A}$ on $2^{[n]}$ is a collection of 
subsets of $[n]$ that is closed upwards under containment, i.e., if 
$A \in \mathcal{A}$ and $A \subseteq B \subseteq [n]$ then 
$B \in \mathcal{A}$. Such an event {\em depends} only on the set
$\cI(\cA):=I_1\cup\cdots\cup I_m$ (that is, on the variables/coordinate 
functions $X_i$ with 
$i\in\cI(\cA)$), where $I_1,\ldots,I_m$ are the minimal sets of $\cA$ 
with respect to inclusion. Any (non-identically zero) non-negative increasing
function $f$ on $2^{[n]}$ may be written as $f=\sum_{i=1}^{k}a_i\chi_{\cA_i}$ 
for some increasing events $\cA_i$ on $2^{[n]}$ and $a_i>0$, $1\le i\le k$.
Clearly, $f$ depends on the set $\cI(f):=\cI(\cA_1)\cup\cdots\cup\cI(\cA_k)$.
\end{definition}

The weakest negative dependence property is the following 
(see, e.g., \cite{P}).

\begin{definition}\label{d-pnc}
A measure $\in\fP_n$ is said to be {\em pairwise
negatively correlated} or p-NC for short 
if $\mu(X_i)\mu(X_j)\ge \mu(X_iX_j)$ whenever 
$1\le i\neq j\le n$. In terms of the generating polynomial $g_\mu$ this 
translates into the inequalities
$$\pa_i g_\mu(\ben)\pa_j g_\mu(\ben)\ge \pa_i \pa_j g_\mu(\ben),
\quad 1\le i\neq j\le n,$$
where $\ben\in\RR^n$ is as before the ``all ones vector''. We say
that a polynomial $f\in\PP_n$ is p-NC (pairwise negatively correlated) if it
satisfies the above inequalities. 
\end{definition}

As shown by the following example, NLC does not necessarily imply p-NC.

\begin{example}\label{ex1}
The measure $\mu\in\fP_4$ with generating polynomial
$$g_\mu(z_1,z_2,z_3,z_4)=\frac{1}{2}(z_1z_2+z_3z_4)$$
trivially satisfies NLC but $\mu(X_1X_2)=\frac{1}{2}$ while 
$\mu(X_1)\mu(X_2)=\frac{1}{4}$, so $\mu$ is not p-NC. 
\end{example}

\begin{definition}[Definition 2.4 in \cite{P}]\label{h-nlc}
A measure $\mu\in\fP_n$ or a polynomial $f\in\PP_n$ 
satisfies the {\em hereditary negative lattice condition} or $\hNLC$ 
if every projection satisfies $\NLC$. One further says that $\mu$ 
(respectively, 
$f$) satisfies the {\em strong  hereditary negative lattice 
condition} or $\hNLC+$ if every measure (respectively, polynomial) obtained 
from $\mu$ (respectively, $f$) by imposing an external field satisfies
h-NLC.
\end{definition}

\begin{definition}\label{d1}
A polynomial $f\in\PP_n$ is called a {\em Rayleigh polynomial} if
\begin{equation}\label{ral-ineq}
\frac {\partial f} {\partial z_i}(x) \frac {\partial f} {\partial z_j}(x)
\geq \frac {\partial^2 f} {\partial z_i \partial z_j}(x) f(x)
\end{equation}
for all $x=(x_1,\ldots,x_n)\in \RR_+^n$ and $1\leq i,j \leq n$, where as 
usual $\RR_+=(0,\infty)$. More 
generally, a multi-affine 
polynomial in $\RR[z_1, \ldots, z_n]$ with non-negative coefficients is 
called a {\em Rayleigh polynomial} if it satisfies the above condition. 
A measure $\mu\in\fP_n$ is said to be a {\em Rayleigh measure} if its
generating polynomial $g_\mu$ is Rayleigh.
\end{definition}

 
The notion of Rayleigh polynomial was introduced in \cite[\S 3.1]{W}, the 
terminology being motivated by its similarity with the Rayleigh monotonicity 
property of 
the (Kirchhoff) effective conductance of linear resistive electrical networks,  
see \cite{CW,W2}. It was first considered for uniform measures on the set of bases of a matroid \cite{CW} as a strengthening of weaker notions studied in \cite{feder,seymour-welsh}. 
The following properties of
Rayleigh polynomials are consequences of Definition~\ref{d1}.
\begin{proposition}\label{p-proper}
If $f(z_1,\ldots,z_n)$ is Rayleigh then so are the following polynomials:
\begin{enumerate}
\item $\pa^S f(z_1,\ldots,z_n)$ for any $S\subseteq [n]$;
\item $f(z_1+\al_1,\ldots,z_n+\al_n)$ whenever $\al_i\ge 0$, $i\in [n]$;
\item $f(z_1,\ldots,z_n)|_{z_i=\al_i}$ for any $\al_i\ge 0$, $1\le i\le n$; 
\item $f(a_1z_1,\ldots,a_nz_n)$ for all $a_i\ge 0$, $i\in [n]$;
\item the ``inversion'' of $f$, i.e., the polynomial 
$z_1\cdots z_nf(z_1^{-1},\ldots,z_n^{-1})$;
\item the polynomial in $nk$ variables 
$f\!\left(k^{-1}\sum_{i=1}^k z_{1i},\ldots,k^{-1}\sum_{i=1}^k z_{ni}\right)$.
\end{enumerate}
\end{proposition}

To prove (1) note that by induction it is enough to do it for $S=\{i\}$ and
arbitrary $i\in [n]$. This follows by first writing 
$$f(z_1,\ldots,z_n)=z_i\pa_i f(z_1,\ldots,z_n)+f(z_1,\ldots,z_n)|_{z_i=0}$$
and then letting $z_i\to\infty$ in the Rayleigh inequalities \eqref{ral-ineq}
for $f$ corresponding to pairs of 
variables indexed by distinct $j,k\in [n]\setminus \{i\}$.

\begin{proposition}\label{p-r-h}
A measure in $\fP_n$ or a polynomial in $\PP_n$ is Rayleigh
if and only if it is h-NLC+.
\end{proposition}

\begin{proof}
In \cite[Theorem~4.4]{W} it was proved that if $f\in\PP_n$ is Rayleigh then 
$f$ satisfies NLC, which combined with Proposition~\ref{p-proper} shows that
$f$ is h-NLC+. To prove the converse statement, let $i,j\in [n]$ with $i\neq j$
and set 
$$g(z_i,z_j)=f(z_1,\ldots,z_n)|_{z_k=1,\,k\in [n]\setminus \{i,j\}}.$$
If $f$ is h-NLC+ then $g$ satisfies NLC (which in this case implies that
$g(z_i,z_j)$ is in fact a real stable polynomial, see 
Definition~\ref{d-rs-pol} in \S \ref{s23} and Theorem~\ref{stable-Rayleigh}
in \S \ref{s-stable}). In particular, we deduce that 
$\pa_i \pa_j f(\ben)\le \pa_i f(\ben)\pa_j f(\ben)$, 
where $\ben$ stands for the ``all ones vector'' as in Definition~\ref{d-pnc}.
Using the external field condition given in Definition~\ref{h-nlc}
wee see that the aforementioned inequality also holds for the polynomial
$f(x_1z_1,\ldots,x_nz_n)$ whenever $x_i\ge 0$, $i\in [n]$, which by 
Definition~\ref{d1} amounts to saying that $f$ is Rayleigh.
\end{proof}

\begin{remark}\label{r-hnlc}
It is interesting to note that one actually has the following analog of 
Proposition \ref{p-r-h}
for the h-NLC property: a measure $\mu\in\fP_n$ -- or its generating polynomial
$g_\mu\in\PP_n$ -- is h-NLC if and only if $g_\mu$ satisfies the Rayleigh 
inequalities
\eqref{ral-ineq} for all $x=(x_1,\ldots,x_n)$ with $x_i\in\{0,1,\infty\}$,
$i\in [n]$.
\end{remark}

\begin{definition}\label{phr}
A {\em homogeneous Rayleigh measure} is one whose generating polynomial
is homogeneous and Rayleigh. The set of all measures that are projections of 
homogeneous Rayleigh measures is denoted by PHR.
\end{definition}

Let us now recall the key concept of negative association. For probability 
measures this notion is usually defined as follows (cf., e.g., \cite{L2,P,W}).

\begin{definition}\label{d-na}
A measure $\mu\in\fP_n$ is called {\em negatively associated} or $\NA$ 
if
$$\int F d\mu \int G d\mu\ge \int FG d\mu$$
for any increasing functions $F,G$ on $2^\cN$ that depend on 
disjoint sets of coordinates (cf.~Definition~\ref{d-inc-ev}). One says that 
$\mu$ is {\em conditionally negatively associated}
or $\CNA$ if each measure obtained from $\mu$ by conditioning on some (or none)
of the values of the variables is $\NA$. Finally, $\mu$ is called {\em strongly
conditionally negatively associated} or $\CNA+$ if each measure obtained from 
$\mu$ by imposing external fields and projections is $\CNA$.
\end{definition}

\begin{remark}\label{r-pair}
It is clear from the definitions
that each of the five properties h-NLC, Rayleigh/h-NLC+, NA, CNA, CNA+ implies 
p-NC.
\end{remark}

\begin{remark}\label{r-cn-hn}
As explained in \cite{P}, one has the following subordination relations: 
CNA $\Rightarrow$ h-NLC and CNA+ $\Rightarrow$ Rayleigh/h-NLC+. In 
\S \ref{s-sna} and \S \ref{s-countex} below we show that PHR 
$\Rightarrow$ CNA+ and that this implication is strict.
\end{remark}

We note that NA can fail to imply NLC even for symmetric measures:

\begin{example}\label{ex2}
Let as before $e_k$, $0\le k\le n$, be the $k$-th elementary symmetric function
in $n$ variables and consider the measure $\mu\in\fP_3$ with 
generating polynomial
$$
g_\mu(z_1,z_2,z_3)=\frac{1}{15}\left[3+2e_1(z_1,z_2,z_3)+2e_2(z_1,z_2,z_3)
\right].
$$
It is not difficult to check that $\mu$ is NA but not NLC.
\end{example}

\begin{definition}\label{d-ulc}
The {\em diagonal 
specialization} of a polynomial $f\in\CC[z_1,\ldots,z_n]$ is the univariate 
polynomial 
$$t\mapsto\De(f)(t):=f(t,\ldots,t).$$
A real sequence $\{a_k\}_{k=0}^n$ is {\em log-concave} 
if $a_k^2 \geq a_{k-1}a_{k+1}$, $1\leq k \leq n-1$, and it is said to have
{\em no internal zeros} if the indices of its non-zero terms form an interval
(of non-negative integers). 
We say that a 
{\em non-negative} sequence $\{a_k\}_{k=0}^n$ is
\begin{itemize}
\item $\LC$ if it is log-concave with no internal zeros; 
\item $\SLC$ (strongly log-concave) if the sequence 
$\{k!a_k\}_{k=0}^{n}$ is $\LC$;
\item $\ULC$ (ultra log-concave) if the sequence
$\left\{a_k/\binom{n}{k}\right\}_{k=0}^{n}$ is $\LC$. 
\end{itemize}
Clearly, $\ULC\Rightarrow \SLC\Rightarrow 
\LC$. If $\mu\in\fP_n$ the sequence 
$$\left\{\mu\left(\sum_{i=1}^{n}X_i=k\right)\right\}_{k=0}^{n}
=\left\{\frac{\De(g_\mu)^{(k)}(0)}{k!}\right\}_{k=0}^{n}$$
is called the {\em rank sequence} of $\mu$ as well as of its generating 
polynomial $g_\mu\in\PP_n$. A measure in $\fP_n$ is then said to be $\ULC$,
$\SLC$ or $\LC$ if its rank sequence is $\ULC$,
$\SLC$ or $\LC$, respectively. 
\end{definition}
