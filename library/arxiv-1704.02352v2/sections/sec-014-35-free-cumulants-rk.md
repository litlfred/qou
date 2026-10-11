---
doc_id: arxiv-1704.02352v2
doc_title: "GAUSSIAN FLUCTUATIONS OF JACK-DEFORMED RANDOM YOUNG DIAGRAMS"
section_id: sec-014-35-free-cumulants-rk
section_title: "Free cumulants Rk"
section_number: 3.5
pages: 23-29
source_pdf: 1704.02352v2.pdf
source_sha256: 9a14dd6ee33248d3
doc_brief: "GAUSSIAN FLUCTUATIONS OF JACK-DEFORMED RANDOM YOUNG DIAGRAMS — We introduce a large class of random Y oung diagrams which can be regarded as a natural one-parameter deformation of so me classi- cal Y"
text_source: latex
latex_prose_ratio: 0.914
latex_coverage_ratio: 0.989
---
\label{sub:FreeCumu}
In many calculations related to 
the asymptotic representation theory it is convenient to parametrize
the shape of the Young diagram~$\lambda$ by \emph{free cumulants}
$\Rfunct_k(\lambda)$ (which depend on the parameter $\alpha$ in our settings). In the context of the representation theory of the symmetric groups
these quantities have been introduced by Biane \cite{Biane1998}.

For the purposes of the current paper it is enough to know that
for a fixed Young diagram $\lambda$ its sequence of functionals of shape and its 
sequence of free cumulants are related to each other by the following simple systems of equations
\cite[Eqs.~(14) and (15)]{DolegaFeraySniady2008}:
\begin{align}
\label{eq:s-r}
\Sfunct_l &= \sum_{i\geq 1} \frac{1}{i!}  (l-1)^{\underline{i-1}} 
\sum_{\substack{k_1,\dots,k_i\geq 2 \\ k_1+\cdots+k_i=l }} \Rfunct_{k_1} \cdots
\Rfunct_{k_i}, \qquad l\geq 2,\\
\label{eq:r-s}
\Rfunct_{l} &=
\sum_{i\geq 1} \frac{1}{i!} (-l+1)^{i-1} \sum_{\substack{k_1,\dots,k_i\geq 2 \\
		k_1+\cdots+k_i=l }} \Sfunct_{k_1} \cdots \Sfunct_{k_i},\qquad  l\geq 2,
\end{align}
where we use a shorthand notation $\Sfunct_k=\Sfunct_k(\lambda)$,
$\Rfunct_k=\Rfunct_k(\lambda)$.
In fact, the above-cited papers \cite{Biane1998,DolegaFeraySniady2008}
concerned only the special isotropic case $\alpha=1$,
however the passage to the anisotropic case $\alpha\neq 1$ does not create any difficulties,
see the work of Lassalle \cite{Lassalle2009} (who used a different normalization constants)
as well as of the first-named author and F\'eray \cite{DolegaFeray2014} 
(whose normalization we use).


\subsection{The case $\alpha=1$.}
\label{sec:alpha-equal-1}
The main advantage of free cumulants lies in the combination of the following two facts.
\begin{itemize}
	\item Each free cumulant $\Rfunct_k$ of a given Young diagram $\lambda$ can be efficiently calculated
	\cite{Biane1998} and its dependence on the shape of $\lambda$ takes a particularly simple
	form (more specifically, ``$\Rfunct_k$ is a \emph{homogeneous} function'').
	
	\item The family $(\gamma,\Rfunct_2,\Rfunct_3,\dots)$ forms a convenient algebraic basis of the algebra $\Poly$
	with $\deg \gamma=1$ and $\deg \Rfunct_k=k$.
	In the special case $\alpha=1$
	(which corresponds to $\gamma=0$) the expansion of $\Ch_l$ in this basis 
	
	takes the following, particularly
	simple form:
	\begin{equation} 
	\label{eq:Kerov-polynomial-gamma0}
	\Ch_l=
	\Rfunct_{l+1} +
	(\text{terms of degree at most $l-1$}).
	\end{equation}
\end{itemize}

One of the consequences of \eqref{eq:Kerov-polynomial-gamma0} is that 
in the special case $\alpha=1$ the relationship announced in
\cref{def:approx-factorization-charactersB}\ref{item:equivalent-enhanced}
between the 
refined asymptotics of the four quantities \eqref{eq:AFPPartitions}--\eqref{eq:AFPDisjointCumulants} 
for $\ell=1$ takes the following, particularly
simple form. Assume that there exists some sequence $(a_l)$ with the property that
\begin{align}
\label{eq:quick-convergence-1}
\chi_n(l)              &= a_{l+1}\ n^{-\frac{l-1}{2}} + O\left(  n^{-\frac{l+1}{2}} \right) 
\qquad\text{for all $l\geq 1$}; \\
\intertext{note that it is a stronger version of \eqref{eq:nice-limit} with 
	$\operatorname{const}_2\equiv 0$; then}
\label{eq:quick-convergence-2}
\E_{\chi_n}(\Ch_l)     &= a_{l+1}\ n^{ \frac{l+1}{2}} + O\left(  n^{ \frac{l-1}{2}} \right)
\qquad\text{for all $l\geq 1$}; \\
\label{eq:quick-convergence-3}
\E_{\chi_n}(\Rfunct_{l+1})  &= a'_{l+1}\ n^{ \frac{l+1}{2}} + O\left(  n^{ \frac{l-1}{2}} \right)
\qquad\text{for all $l\geq 1$}, \\
\label{eq:quick-convergence-4}
\E_{\chi_n}(\Sfunct_{l})  &= a''_{l}\ n^{ \frac{l}{2}} + O\left(  n^{ \frac{l-2}{2}} \right)
\qquad \text{for each $l\geq 2$,}
\intertext{where}
\label{eq:what-is-prime}
a'_{l+1} &= a_{l+1} 
\intertext{and}
\label{eq:my-little-constants}
a''_l &= \sum_{i\geq 1} \frac{1}{i!}  (l-1)^{\underline{i-1}} 
\sum_{\substack{k_1,\dots,k_i\geq 2 \\ k_1+\cdots+k_i=l }} a'_{k_1} \cdots a'_{k_i},    
\end{align}
see \eqref{eq:s-r} for the last equality and \cite{Sniady2006c} for more details.


\subsection{Details of \cref{def:approx-factorization-charactersB} part \ref{item:afp2}  
	in the generic case $\alpha\neq 1$.}
\label{sec:co-sie-dzieje-alpha-neq-1}
The original proof of \cite[Theorem and Definition 1]{Sniady2006c}
was based on the idea of expressing various elements $F$ of the algebra
of $\alpha$-polynomial functions $\Poly^{(1)}$
(such as the characters $\Ch_\pi$ or the conditional
cumulants $\kumuDisjointPoint$ of such characters)
as polynomials in the basis $\Rfunct_2,\Rfunct_3,\dots$
of free cumulants and studying the top-degree of such polynomials, as we did in \cref{sec:alpha-equal-1}.
In our more general context of $\alpha\neq 1$ (or, in other words, $\gamma\neq 0$)
the corresponding polynomial for $F$
might have some \emph{extra terms} which depend additionally on the variable~$\gamma$. 
These \emph{extra terms} might influence the asymptotic behavior of random Young diagrams.
We shall discuss this issue in more detail in the remaining of this section
as well as in \cref{sec:extra-terms-evil}.


\subsubsection{The first-order asymptotics when $\alpha$ is constant}

The first-named author and F\'eray \cite[Proposition 3.7]{DolegaFeray2014}
proved that the degree of 
\begin{equation}
\label{eq:F1} 
F :=  \Ch_l    
\end{equation}
with respect to the filtration from \cref{sec:alpha-equal-1}
remains equal to $l+1$ even when we pass from $\Poly^{(1)}$ to $\Poly$
or, in other words, that the degree of the \emph{extra terms} is bounded from above by $l+1$.
In the asymptotics when $\alpha$ is a constant and does not depend on $n$
(or, more generally, when the constant $g$ from \eqref{eq:double-scaling-refined} fulfills $g=0$),
it follows that $\gamma=O(1) \ll O\left( n^{\frac{\degg \gamma}{2}}\right) $.
Since each extra term is divisible by the monomial $\gamma$, it follows 
that the contribution of the extra terms
is negligible when compared to the unique original top-degree term $\Rfunct_{l+1}$. 
It follows that in this asymptotics the relationships between the 
quantities $(a_l)$, $(a'_l)$ and $(a''_l)$ which provide the first-order asymptotics of, respectively,
the characters, the mean value of free cumulant, and the mean value of the functionals of shape, remain the same
as in \cref{sec:alpha-equal-1} for the case $\alpha=1$.

\medskip

From \cref{theo:factorization-of-characters} it follows that
an analogous result holds true for the conditional cumulant
(covariance)
\begin{equation}
\label{eq:F2} 
F:= \kumuDisjointPoint(\Ch_{l_1},\Ch_{l_2})
\end{equation}
and the degree of $F$ remains equal to $l_1+l_2$ 
when we pass from $\Poly^{(1)}$ to $\Poly$.
A reasoning similar to the one above implies that
not only the proof of \cite[Theorem and Definition 1]{Sniady2006c}
remains valid in our context for $\ell=2$, but 
\emph{also the relationships between the 
	quantities \eqref{eq:AFPPartitions}--\eqref{eq:AFPDisjointCumulants}
	which provide the first-order asymptotics of cumulants
	remain the same as in \cite[Theorem 3]{{Sniady2006c}}.}

Anticipating the proof of \cref{theo:clt},
the above considerations imply the following explicit description
of the covariance of the limiting Gaussian process $\Delta_\infty$.

\begin{corollary}
	The covariance of the Gaussian process
	$\Delta_\infty$
	describing the limit fluctuations of random Young diagrams from \cref{theo:clt}
	coincides with its counterpart 
	for $\alpha=1$ from
	\cite[Theorem 3]{Sniady2006c}.
\end{corollary}


\subsubsection{The first-order asymptotics in the double scaling limit}
\label{sec:first-order-for-g-neq0}

In the asymptotics when $\alpha=\alpha(n)$ depends on $n$ 
in a way described in \cref{sec:hypothesis-double-scaling} with $g\neq 0$, 
the \emph{extra terms} in both examples \eqref{eq:F1}, \eqref{eq:F2}  
considered above are of the same 
order as the original terms. It follows that 
the relationship between 
the quantities $(a_l)$, $(a'_l)$ and $(a''_l)$ is altered
and depends on the constant $\sconstant$ from \eqref{eq:double-scaling-refined}, see \cref{subsubsect:DoubleScaling} below.
Also the covariance of the Gaussian process
describing the fluctuations of random Young diagrams is altered;  finding an explicit form for this covariance
is currently beyond our reach because no closed formula 
for the top-degree part of
the conditional cumulant $\kumuDisjointPoint(\Ch_{l_1},\Ch_{l_2})$
(an analogue of the results of \cite[Section 1]{Sniady-AsymptoticsJack} for $\Ch_n$)
is available. 


\subsection{Refined asymptotics of characters}
\label{subsec:refinedasymptotics}
In order to find more subtle relationships between the asymptotics of various
quantities appearing in \cref{def:approx-factorization-charactersB}
we need an analogue of Equation \eqref{eq:Kerov-polynomial-gamma0}
between the character $\Ch_l$ and the free cumulants in the generic case $\alpha\neq 1$.
We present below two such formulas: the one from \cref{sec:rough-estimate}
is conceptually simpler and will be sufficient for 
the scaling when $\alpha$ is fixed;
in the case of the double scaling limit we will need a more involved
formula from \cref{sec:top-degree-by-Sniady}.


\subsubsection{The rough estimate}
\label{sec:rough-estimate}

We start with the formula expressing the top-degree part of the
normalized Jack character $\Ch_l$ modulo terms divisible by $\gamma^2$
which follows follows from 
\cite[Section 11]{Lassalle2009} 
combined with the degree bounds of the first-named author and F\'eray
\cite[Proposition 3.7]{DolegaFeray2014}
as well as from \cite[Theorem A.3]{Sniady-AsymptoticsJack}:
\begin{multline}
\label{eq:kerov-polynomial-subtle}
\Ch_l=
\bigg[ \Rfunct_{l+1}+ \\
+\gamma \sum_{i\geq 1} \sum_{k_1+\cdots+k_i=l}
\frac{l}{i} 
(k_1-1) \cdots (k_i-1) \Rfunct_{k_1} \cdots \Rfunct_{k_i}+ \\
{+ (\text{terms divisible by $\gamma^2$ })\bigg]+ }
\\
(\text{terms of degree at most $l-1$}).
\end{multline}


\subsubsection{Closed formula for top-degree part of Jack characters}
\label{sec:top-degree-by-Sniady}
Let us fix an integer $l\geq 1$.
We will view the symmetric group $\Sym{l}$ as the set of permutations of the set
$[l]:=\{1,\dots,l\}$ and its subgroup 
\[\Sym{l-1}:=\big\{ \sigma\in\Sym{l} : \sigma(l)=l \big\}\] 
as the set of permutations of the same set $[l]$ which have $l$ as a fixpoint.
Consider the set 
\begin{multline*}
\mathcal{X}_l= \big\{ (\sigma_1,\sigma_2) \in \Sym{l}\times \Sym{l} : \\
\text{the group generated by $\sigma_1,\sigma_2$ acts transitively on the set $[l]$}
\big\}.   
\end{multline*}
The group $\Sym{l-1}$ acts on $\mathcal{X}_l$ by coordinate-wise conjugation:
\[ \pi\cdot (\sigma_1,\sigma_2) := \big(\pi \sigma_1 \pi^{-1}, \pi \sigma_2 \pi^{-1}\big). \]
The orbits of this action define an equivalence relation $\sim$ on $\mathcal{X}_l$;
the corresponding equivalence classes have a natural combinatorial interpretation as
\emph{non-labeled, rooted, bicolored, oriented maps with $l$ edges} 
which is out of scope of the current paper
(see \cite[Section 1.4.3]{Sniady-AsymptoticsJack} for details).

\medskip

For a permutation $\pi$ we denote by $C(\pi)$ the set of its cycles.

We say that a triple $(\sigma_1,\sigma_2,q)$ is an \emph{`expander'}
\cite[Appendix A.1]{Sniady-AsymptoticsJack}, see also \cite{DolegaFeraySniady2008}, 
if $\sigma_1,\sigma_2\in\Sym{l}$ are permutations
and $q\colon C(\sigma_2)\to\{2,3,\dots\}$ is a function on the set of cycles of $\sigma_2$
with the following two properties:
\[ \sum_{c\in C(\sigma_2)} q(c) = |C(\sigma_1)|+|C(\sigma_2)|\]
and for every set $A\subset C(\sigma_2)$ such that $A\neq \emptyset$ and $A\neq C(\sigma_2)$
we have that
\begin{multline*}
\#\big\{ c\in C(\sigma_1): \text{$c$ intersects at least one of the cycles in $A$} \big\} > \\
\sum_{d\in A} \big[ q(d)-1  \big].
\end{multline*}

The following is a refined version of the formula
\eqref{eq:kerov-polynomial-subtle}.
\begin{lemma}[{\cite[Theorem A.3 and Theorem 1.6]{Sniady-AsymptoticsJack}}]
	\label{lem:top-degree-jack-character}
	For each integer $l\geq 1$ the expansion of the character
	$\Ch_l$ as a polynomial in the variables $\gamma,\Rfunct_2,\Rfunct_3,\dots$ is given by
	\begin{multline}
	\label{eq:Sniady-proved-this}
	\Ch_l= \\
	\sum_{[(\sigma_1,\sigma_2)]\in \mathcal{X}_l/\sim} \gamma^{l+1-|C(\sigma_1)|-|C(\sigma_2)|} 
	\sum_{\substack{q\colon C(\sigma_2)\to\{2,3,\dots\} \\
			\text{$(\sigma_1,\sigma_2,q)$ is an expander}}}
	\prod_{c\in C(\sigma_2)} \Rfunct_{q(c)} + \\
	+\text{(terms of degree at most $l-1$)}.
	\end{multline}
	where the first sum runs over the representatives of the equivalence clases.
\end{lemma}


\subsection{Proof of part \ref{item:equivalent-enhanced} of \cref{def:approx-factorization-charactersB}}
\label{sec:extra-terms-evil}


\subsubsection{The scaling when $\alpha$ is constant}
\label{sec:concrete-alpha-constant}

Part \ref{item:equivalent-enhanced} of \cref{def:approx-factorization-charactersB} concerns the trivial 
case $\ell=1$ which one can easily prove from scratch, based on \eqref{eq:kerov-polynomial-subtle}.
We shall present a detailed proof only for a specific case which will be useful in applications
(more specifically, for the proof of \cref{theo:clt} from \cref{sec:proof-of-CLTCLT}) and we shall 
assume that the refined asymptotics of characters specified in
part \ref{item:equivalent-enhanced} of \cref{def:approx-factorization-charactersB}
holds true for the quantity \eqref{eq:AFPPartitions}. The other implications are
analogous.

For a specific choice of the constants
\begin{align}
\label{eq:quick-convergence-1-B}
\chi_n(l)              &= a_{l+1}\ n^{-\frac{l-1}{2}} + b_{l+1} \ n^{-\frac{l}{2}} + o\left(  n^{-\frac{l}{2}} \right)
\qquad \text{for $l\geq 1$}\\
\intertext{for some sequences $(a_l)$ and $(b_l)$,
	it is a simple exercise to use \eqref{eq:what-is-jack-character-zmiana} and \eqref{eq:kerov-polynomial-subtle}
	in order to show that}
\label{eq:quick-convergence-2-B}
\E_{\chi_n}(\Ch_l)     &= a_{l+1}\ n^{ \frac{l+1}{2}} + b_{l+1}\ n^{\frac{l}{2}}+ o\left(  n^{ \frac{l}{2}} \right)
\qquad \text{for $l\geq 1$,}\\
\label{eq:quick-convergence-3-B}
\E_{\chi_n}(\Rfunct_{l+1})  &= a'_{l+1}\ n^{ \frac{l+1}{2}} + b'_{l+1} \ n^{\frac{l}{2}} + o\left(  n^{ \frac{l}{2}} \right)
\qquad \text{for $l\geq 1$,}
\end{align}
where $(a'_l)$ is given again by \eqref{eq:what-is-prime} and $(b'_l)$ is the unique sequence which fulfills
\begin{equation}
\label{eq:co-sie-dzieje-z-b}
b_{l+1}= b'_{l+1}+\gamma \sum_{i\geq 1} \sum_{k_1+\cdots+k_i=l}
\frac{l}{i} 
(k_1-1) \cdots (k_i-1) a_{k_1} \cdots a_{k_i}.
\end{equation}
In particular, \eqref{eq:quick-convergence-2-B} shows that the
refined asymptotics of characters specified in
part \ref{item:equivalent-enhanced} of \cref{def:approx-factorization-charactersB}
holds true for the quantity \eqref{eq:AFPCumulants-characters}.

\medskip

Consider now the quantity under the limit symbol in \eqref{eq:AFPCumulants}
for $\ell=1$ and for the specific choice of $x_1=\Sfunct_l$.
Equation \eqref{eq:s-r} implies that
the refined asymptotics of characters specified in
part \ref{item:equivalent-enhanced} of \cref{def:approx-factorization-charactersB}
holds true for the quantity \eqref{eq:AFPCumulants}:
\begin{equation}
\label{eq:quick-convergence-4-B}
\E_{\chi_n}(\Sfunct_{l})  = a''_{l}\ n^{ \frac{l}{2}} + b''_{l} \ n^{\frac{l-1}{2}} + o\left(  n^{ \frac{l-1}{2}} \right)
\qquad \text{for each $l\geq 2$,}
\end{equation}
with the constants given by \eqref{eq:my-little-constants} and
\begin{equation}
\label{eq:what-is-b-bis}
b''_l = \sum_{i\geq 1} \frac{1}{(i-1)!}  (l-1)^{\underline{i-1}} 
\sum_{\substack{k_1,\dots,k_i\geq 2 \\ k_1+\cdots+k_i=l }} b'_{k_1} a'_{k_2} \cdots a'_{k_i}.    
\end{equation}

We conclude the proof by pointing out that for $\ell=1$ the expression under the limit symbol in \eqref{eq:AFPCumulants}
coincides with its counterpart from \eqref{eq:AFPDisjointCumulants}.
\qed

\begin{remark}
	One can see that generically for $\alpha\neq 1$ and $\gamma\neq 0$
	(even if the initial characters $\chi_n(l)$ have small subleading terms which corresponds to
	$b_l\equiv 0$) the subleading terms in
	\eqref{eq:quick-convergence-4-B}
	are much bigger than their counterparts for $\alpha=1$ from \eqref{eq:quick-convergence-4},
	namely they are of order $\frac{1}{\sqrt{n}}$ times the leading asymptotic term.
	As we shall see in \cref{sec:proof-of-CLTCLT}, 
	
	
	this leads to non-centeredness of the limiting Gaussian process $\Delta_\infty$. 
\end{remark}


\subsubsection{The double scaling limit}
\label{subsubsect:DoubleScaling}

In the double scaling limit $\sconstant\neq 0$ considered in \cref{sec:hypothesis-double-scaling}
the reasoning presented in \cref{sec:concrete-alpha-constant} above remains valid
if one replaces all the references to \eqref{eq:kerov-polynomial-subtle}
by \cref{lem:top-degree-jack-character}.
Note, however, that the relationship \eqref{eq:what-is-prime}
in this new context takes the form
\begin{equation*}
a_{l+1}= \sum_{[(\sigma_1,\sigma_2)]\in \mathcal{X}_l/\sim} g^{l+1-|C(\sigma_1)|-|C(\sigma_2)|} 
\sum_{\substack{q\colon C(\sigma_2)\to\{2,3,\dots\} \\
		\text{$(\sigma_1,\sigma_2,q)$ is an expander}}}
\prod_{c\in C(\sigma_2)} a'_{q(c)},
\end{equation*}
while \eqref{eq:co-sie-dzieje-z-b} takes the form
\begin{multline*} 
b_{l+1}=
\\
\shoveleft{\sum_{[(\sigma_1,\sigma_2)]\in \mathcal{X}_l/\sim} 
	\big({l+1-|C(\sigma_1)|-|C(\sigma_2)|}\big) 
	\ \sconstant' \ \sconstant^{l-|C(\sigma_1)|-|C(\sigma_2)|} \times} 
\\ 
\shoveright{\times
	\sum_{\substack{q\colon C(\sigma_2)\to\{2,3,\dots\} \\
			\text{$(\sigma_1,\sigma_2,q)$ is an expander}}}
	\prod_{c\in C(\sigma_2)} a'_{q(c)}+} \\
\shoveleft{
	+\sum_{[(\sigma_1,\sigma_2)]\in \mathcal{X}_l/\sim} \sconstant^{l+1-|C(\sigma_1)|-|C(\sigma_2)|} 
	\times 
} 
\\ 
\times
\sum_{\substack{q\colon C(\sigma_2)\to\{2,3,\dots\} \\
		\text{$(\sigma_1,\sigma_2,q)$ is an expander}}}
\sum_{c \in C(\sigma_2)} b'_{q(c)}\prod_{c'\in
	C(\sigma_2)\setminus\{c\}} a'_{q(c')}.
\end{multline*}
