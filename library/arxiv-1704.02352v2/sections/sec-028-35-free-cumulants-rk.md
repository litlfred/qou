---
doc_id: arxiv-1704.02352v2
doc_title: "GAUSSIAN FLUCTUATIONS OF JACK-DEFORMED RANDOM YOUNG DIAGRAMS"
section_id: sec-028-35-free-cumulants-rk
section_title: "Free cumulants Rk"
section_number: 3.5
pages: 23-26
source_pdf: 1704.02352v2.pdf
source_sha256: 9a14dd6ee33248d3
toc_source: outline
text_source: latex
latex_prose_ratio: 0.911
latex_coverage_ratio: 0.988
doc_brief: "GAUSSIAN FLUCTUATIONS OF JACK-DEFORMED RANDOM YOUNG DIAGRAMS — We introduce a large class of random Young diagrams which can be regarded as a natural one-parameter deformation of some classi- cal"
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
