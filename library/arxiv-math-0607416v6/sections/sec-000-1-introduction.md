---
doc_id: arxiv-math-0607416v6
doc_title: "PÓLYA-SCHUR MASTER THEOREMS FOR CIRCULAR DOMAINS AND THEIR BOUNDARIES"
section_id: sec-000-1-introduction
section_title: "Introduction"
section_number: 1
pages: 1-3
source_pdf: 0607416v6.pdf
source_sha256: 0705075947ce4a3d
toc_source: outline
text_source: latex
latex_prose_ratio: 0.962
latex_coverage_ratio: 0.974
doc_brief: "PÓLYA-SCHUR MASTER THEOREMS FOR CIRCULAR DOMAINS AND THEIR BOUNDARIES — We characterize all linear operators on ﬁnite or inﬁnite-dimensio- nal polynomial spaces that preserve the property of having"
---
\label{s1}

Some of the main challenges in the theory of distribution of zeros of 
polynomials and transcendental entire functions concern the description of 
linear operators that preserve certain prescribed (``good'') properties.
Notwithstanding their fundamental character, most of these problems are 
in fact still open as they turn out to be surprisingly difficult in full
generality. Two outstanding questions among these are the following: let 
$\Om\subseteq\bC$ be an appropriate set of interest and denote by $\pi(\Om)$
the class of all (complex or real) univariate polynomials whose zeros lie in
$\Om$. 

\begin{problem}\label{pb1}
Characterize all linear transformations 
$T:\pi(\Om)\rightarrow \pi(\Om)\cup\{0\}$. 
\end{problem}

Let $\pi_n$ be the vector space (over $\bC$ or $\bR$) of all polynomials
of degree at most $n$ and denote by $\pi_n(\Om)$ the subclass of $\pi(\Om)$
consisting of polynomials of degree at most $n$. The finite degree analog
of Problem~\ref{pb1} is as follows.

\begin{problem}\label{pb2}
Describe all linear operators $T:\pi_n(\Om)\rightarrow \pi(\Om)\cup\{0\}$ for 
$n\in\bN$.
\end{problem}

These problems were stated in precisely this general form in 
\cite{CC1,cso} 
(see also \cite{BBCV}, \cite[pp.~182--183]{RS}) thereby encompassing 
essentially all
similar questions or variations thereof scattered throughout the literature.
Problems~\ref{pb1}--\ref{pb2} originate from the works of 
Laguerre \cite{lag} and P\'olya-Schur \cite{PS} and have been open for all but 
trivial
choices of $\Om$, including such important cases when $\Om=\bR$
or $\Om$ is a half-plane. In this paper we completely solve 
Problems~\ref{pb1}--\ref{pb2} in arguably the most relevant cases, 
namely all closed circular domains (iii)--(v) 
and their boundaries (i)--(ii):
\begin{itemize}
\item[(i)] $\Om$ is a line, 
\item[(ii)] $\Om$ is a circle, 
\item[(iii)] $\Om$ is a closed half-plane, 
\item[(iv)] $\Om$ is a closed disk, 
\item[(v)] $\Om$ is the complement of an open disk.
\end{itemize}

Despite their long history only relatively few results pertaining to
Problems~\ref{pb1}--\ref{pb2} are known. As we note in the following 
(very brief) survey, these deal almost 
exclusively with special
types of linear transformations satisfying the required properties. 

To prove the transcendental characterizations of linear preservers of 
polynomials whose zeros are located on a line or 
in a closed half-plane (Theorems~\ref{tranR} and~\ref{tranC}) we first 
establish a result
on uniform limits on compact sets of bivariate polynomials 
which are non-vanishing whenever  both variables are in the upper half-plane
(Theorem~\ref{genpol}). Entire functions which are 
uniform limits on compact sets 
of sequences of univariate polynomials with only positive zeros were first 
described 
by Laguerre \cite{lag}. In the process he showed that if $Q(z)$ is a real 
polynomial with all negative zeros then 
$T(\pi(\bR))\subseteq \pi(\bR)\cup\{0\}$, 
where $T:\bR[z]\rightarrow \bR[z]$ is the linear operator defined by 
$T(z^k)=Q(k)z^k$, $k\in \bN$. Laguerre also stated without proof 
the correct result  for uniform limits of polynomials with all real zeros.
The class of entire functions thus obtained -- the so-called 
Laguerre-P\'olya class -- was subsequently characterized by P\'olya \cite{pol}.
A more complete investigation of sequences of such polynomials was 
carried out in 
\cite{Lindwart-Polya}. This also led to the description of entire 
functions obtained as uniform limits on compact sets of sequences of 
univariate polynomials all whose zeros lie in a given closed 
half-plane \cite{Le,Ob0,szasz} as well as the description of entire 
functions in two variables obtained 
as limits, uniformly on compact sets, of sequences of bivariate polynomials 
which are non-vanishing when both variables are in a given open half-plane 
\cite{Le}.

The Laguerre-P\'olya class has ever since 
played a significant role in the theory of entire functions 
\cite{CCS,Le}. It was for instance a key ingredient in 
P\'olya and Schur's (transcendental) 
characterization of {\em multiplier sequences of the first kind}  \cite{PS}, 
see Theorem~\ref{ps} below. The latter are linear transformations $T$ on 
$\bR[z]$ that are 
diagonal in the standard monomial basis of $\bR[z]$ and satisfy 
$T(\pi(\bR))\subseteq \pi(\bR)\cup\{0\}$. P\'olya-Schur's seminal paper 
generated a vast literature on this topic and related subjects at the interface
between analysis, operator theory and algebra but a solution to 
Problem~\ref{pb1} in the case $\Om=\bR$ has so far remained elusive 
(cf.~\cite{CC1}). Among the most noticeable progress in this direction we 
should mention Theorem 17 of \cite[Chap.~IX]{Le}, where Levin describes a 
certain class of ``regular" linear operators acting on the closure 
of the set of polynomials in one variable which have all zeros in the closed 
upper half-plane. However, Levin's theorem 
actually uses rather restrictive assumptions and seems in fact to rely on 
additional (albeit not
explicitly stated) non-degeneracy conditions for the transformations involved. 
Indeed, one can easily produce counterexamples to Levin's result by 
considering linear operators such as the ones described in 
Corollary \ref{cor-algstab} (a) of this paper. In \cite{CC2} 
Craven and Csordas established
an analog of the P\'olya-Schur theorem for multiplier sequences in finite 
degree thus solving Problem~\ref{pb2} for $\Om=\bR$ in the special case of
diagonal operators. Unipotent upper triangular linear operators $T$ on 
$\bR[z]$ 
satisfying $T(\pi(\bR))\subseteq \pi(\bR)\cup\{0\}$ were described in 
\cite{CPP}. 
Quite recently, in \cite{BBS} the authors solved Problem~\ref{pb1} for 
$\Om=\bR$ and obtained
multivariate extensions for a large class of linear transformations, namely 
all finite order linear differential operators with polynomial coefficients.
Further partial progress towards a solution to Problem~\ref{pb1} for $\Om=\bR$
is preliminarily reported in \cite{fisk} although the same kind
of remarks as in the case of Levin's theorem apply here. Namely, the
results of {\em op.~cit.~}are valid only in the presence of extra 
non-degeneracy or continuity assumptions for the operators under 
consideration. Various other special cases of Problem~\ref{pb1} for 
$\Om=\bR$ have been 
considered in 
\cite{aleman,Br,brenti, iserles1,iserles2,iserles3}. Finally, we should 
mention that to the best of our 
knowledge  
Problems~\ref{pb1}--\ref{pb2} have so far been widely open in cases 
(ii)--(v).

To begin with, in \S \ref{ss21} and \S \ref{ss31}--\S \ref{ss32} we solve 
Problems~\ref{pb1}--\ref{pb2} for $\Om=\bR$ and 
$\Om=\{z \in \CC: \Im(z) \leq 0\}$ and thus obtain complete algebraic and
transcendental characterizations of linear operators that preserve
hyperbolicity and stability, respectively. In order to deal with 
Problems~\ref{pb1}--\ref{pb2} for {\em all} closed circular domains and their
boundaries we are naturally led to considering a third classification problem,
namely the following more general version of Problem~\ref{pb2}.

\begin{problem}\label{pb3}
Let $n\in\bN$ and $\Omega \subset \CC$. Describe all linear operators 
$$T:\pi_n(\Om)\setminus \pi_{n-1}(\Om) \rightarrow \pi(\Om)\cup\{0\}.$$  
\end{problem}

As we explain in \S \ref{ss22}, Problems~\ref{pb2} and~\ref{pb3} are 
equivalent for closed unbounded sets but for closed bounded sets the latter 
problem is more natural and actually turns out to be a crucial step in 
solving Problems~\ref{pb1}--\ref{pb2} for closed discs. 
In \S \ref{ss22} and \S \ref{ss33} we fully answer Problem~\ref{pb3} for 
any closed circular domain or the boundary of such a domain and as a 
consequence we get
complete solutions to Problems~\ref{pb1}--\ref{pb2} in all cases ((i)--(v))
listed above.

On the one hand, these results accomplish the classification program 
originating from the works of Laguerre and P\'olya-Schur that we briefly 
outlined 
in this introduction. On the other hand, they seem to have numerous 
applications ranging from entire function theory and operator theory to 
real algebraic geometry, matrix theory and combinatorics. Some of these 
will make the object of forthcoming publications.  
The paper concludes with several remarks
on related open problems and potential further developments (\S \ref{s4}).
