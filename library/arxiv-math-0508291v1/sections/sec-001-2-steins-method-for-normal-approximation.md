---
doc_id: arxiv-math-0508291v1
doc_title: "Stein’s Method and Random Character Ratios Running head: Stein’s Method and Random Character Ratios Version of 8/13/05"
section_id: sec-001-2-steins-method-for-normal-approximation
section_title: "Stein's Method for Normal Approximation"
section_number: 2
pages: 5-6
source_pdf: 0508291v1.pdf
source_sha256: d2d541426aaec742
toc_source: outline
text_source: latex
latex_prose_ratio: 0.983
latex_coverage_ratio: 0.989
doc_brief: "Stein’s Method and Random Character Ratios Running head: Stein’s Method and Random Character Ratios Version of 8/13/05 — Stein’s method is used to prove limit theorems for random character ratios."
---
\label{stein}

	In this section we briefly review Stein's method for normal
	approximation, using the method of exchangeable pairs
	\cite{Stn}. One can also use couplings to prove normal
	approximations by Stein's method (see \cite{Re} for a survey),
	but the exchangeable pairs approach is effective for our
	purposes. For a survey discussing both exchangeable pairs and
	couplings, the paper \cite{RR2} can be consulted.

	Two random variables $W,W'$ on a state space $X$ are called
	exchangeable if for all $w_1,w_2$, $\pp(W=w_1,W'=w_2)$ is
	equal to $\pp(W=w_2,W'=w_1)$. As is typical in probability
	theory, let $\ee(A|B)$ denote the expected value of $A$
	given $B$. The following result of Stein uses an exchangeable
	pair $(W,W')$ to prove a central limit theorem for $W$.

\begin{theorem} \label{steinbound} (\cite{Stn}) Let $(W,W')$ be an
 exchangeable pair of real random variables such that $\ee(W'|W) =
(1-a)W$ with $0< a <1$. Then for all real $x_0$, \begin{eqnarray*} & &
\left| \pp(W \leq x_0) - \frac{1}{\sqrt{2 \pi}} \int_{-\infty}^{x_0}
e^{-\frac{x^2}{2}} dx \right|\\ & \leq &
\frac{\sqrt{Var(\ee[(W'-W)^2|W])}}{a} + (2 \pi)^{- \frac{1}{4}}
\sqrt{\frac{1}{a} \ee|W'-W|^3}. \end{eqnarray*}
\end{theorem}

	In order to apply Theorem \ref{steinbound} to study a
	statistic $W$, one needs an exchangeable pair $(W,W')$. The
	usual way of doing this is to use Markov chain theory. A
	Markov chain $K$ (with chance of going from $x$ to $y$ denoted
	by $K(x,y)$) on a finite set $X$ is called reversible with
	respect to a probability distribution $\pi$ if $\pi(x) K(x,y)
	= \pi(y) K(y,x)$ for all $x,y$. This condition implies that
	$\pi$ is a stationary distribution for $K$. It is
	straightforward to check that if $K$ is reversible with
	respect to $\pi$, then one obtains an exchangeable pair
	$(W,W')$ as follows: choose $x \in X$ from $\pi$, then obtain
	$x'$ by taking one step from $x$ according to $K$, and set
	$(W,W')=(W(x),W(x'))$.

	To apply Theorem \ref{steinbound}, one needs the exchangeable
	pair arising from $K$ to satisfy $\ee(W'|W) = (1-a)W$, and
	also one must obtain useful bounds on $Var(\ee[(W'-W)^2|W])$
	and $\ee|W-W'|^3$. A main contribution of this paper is to
	provide a number of algebraically natural examples where this
	can be done. As the reader will see, the construction of $K$
	in our examples can be subtle.

	A drawback with Theorem \ref{steinbound} is that in many
	problems of interest, it gives a convergence rate of
	$O(n^{-1/4})$ rather than $O(n^{-1/2})$. When $|W'-W|$ is bounded,
	the following variation often gives the correct rate. A
	similar result is in \cite{RR}.

\begin{theorem} \label{rinrot} (\cite{SS}) Let $(W,W')$ be an
 exchangeable pair of real random variables such that $\ee(W'|W) =
(1-a)W$ with $0<a<1$. Suppose that $|W'-W| \leq A$ for some
constant $A$. Then for all real $x_0$, \begin{eqnarray*} & & \left|
\pp(W \leq x_0) - \frac{1}{\sqrt{2 \pi}} \int_{-\infty}^{x_0}
e^{-\frac{x^2}{2}} dx \right|\\ & \leq &
\frac{\sqrt{Var(\ee[(W'-W)^2|W])}}{a} + .41 \frac{A^3}{a} + 1.5
A. \end{eqnarray*}
\end{theorem} In many of our examples, $|W'-W|$ is unbounded. Thus as
	mentioned in the introduction, significantly more work may be
	needed to go beyond the $O(n^{-1/4})$ rate.

	The following general lemmas are helpful in working with the
	error bounds in either Theorem \ref{steinbound} or Theorem
	\ref{rinrot}.

\begin{lemma} \label{var} Let $(W,W')$ be an exchangeable pair of random variables such that $\ee(W'|W) = (1-a) W$ and $\ee(W^2)=1$. Then $\ee(W'-W)^2 = 2a$. 
\end{lemma}

\begin{proof} Since $W$ and $W'$ have the same distribution, \begin{eqnarray*}
 \ee(W'-W)^2 & = & \ee(\ee(W'-W)^2|W)\\ & = & \ee((W')^2) + \ee(W^2) -
2 \ee(W \ee(W'|W))\\ & = & 2 \ee(W^2) - 2 \ee(W \ee(W'|W))\\ & = & 2
 \ee(W^2) - 2(1-a) \ee(W^2)\\ & = & 2a. \end{eqnarray*} \end{proof}

	Lemma \ref{majorize} is a well known inequality (already used
	in the monograph \cite{Stn}) and useful because often the
	right hand side is easier to compute or bound than the left
	hand side. To make this paper as self-contained as possible,
	we include a proof. Here $x$ is an element of the state space
	$X$.

\begin{lemma} \label{majorize} \[ Var(\ee[(W'-W)^2|W]) \leq Var (\ee[(W'-W)^2|x]).\] \end{lemma}	

\begin{proof} Jensen's
 inequality states that if $g$ is a convex function, and $Z$ a random
 variable, then $g(\ee(Z)) \leq \ee(g(Z))$. There is also a
 conditional version of Jensen's inequality (Section 4.1 of \cite{Du})
 which states that for any $\sigma$ subalgebra ${\it F}$ of the
 $\sigma$-algebra of all subsets of $X$, \[ \ee(g(\ee(Z|{\it F})))
 \leq \ee(g(Z)).\] The lemma follows by setting $g(t)=t^2$,
 $Z=\ee((W'-W)^2|x)$, and letting ${\it F}$ be the $\sigma$-algebra
 generated by the level sets of $W$. \end{proof}
