---
doc_id: arxiv-1304.2934v4
doc_title: "MOD-φ CONVERGENCE, I: NORMALITY ZONES AND PRECISE DEVIATIONS"
section_id: sec-049-11-random-character-values-from-central-measures
section_title: "Random character values from central measures on partitions"
section_number: 11
pages: 88-91
source_pdf: 1304.2934v4.pdf
source_sha256: b7ed2a9e85264568
toc_source: outline
text_source: latex
latex_prose_ratio: 0.687
latex_coverage_ratio: 0.983
doc_brief: "MOD-φ CONVERGENCE, I: NORMALITY ZONES AND PRECISE DEVIATIONS — In this paper, we use the framework of mod-φ convergence to prove pre- cise large or moderate deviations for quite general sequences of"
---
\label{sec:central}
Our Theorem~\ref{thm:dependencygraphsrefined} can also be used to study certain models of random integer partitions. Recall that if $G$ is a finite group and if $\tau$ is a function $G \to \C$ with $\tau(e_{G})=1$ and $\tau(gh)=\tau(hg)$ (such a function is called a \emph{trace} on $G$), then $\tau$ can be expanded uniquely as a linear combination of normalized irreducible characters:
$$\tau=\sum_{\lambda \in \widehat{G}} \,\proba_{\tau}[\lambda]\,\widehat{\chi}^{\lambda},$$
where $\widehat{G}$ is the (finite) set of isomorphism classes of irreducible representations of $G$ and $\widehat{\chi}^{\lambda}$ the normalized ({\em i.e.} divided by the dimension of the space)
character of the irreducible representation associated to $\lambda$.
\begin{definition}
The map $\lambda \mapsto \proba_{\tau}[\lambda]$ is called the spectral measure of the trace $\tau$. It takes non-negative values if and only if, for every family $(g_1,\ldots,g_n)$ of elements of $G$, the matrix $(\tau(g_i(g_j)^{-1}))_{1 \leq i,j \leq n}$ is Hermitian non-negative definite. Then, the spectral measure is a probability measure on $\widehat{G}$.
\end{definition}
\bigskip

When $G=\sym(n)$ is the symmetric group of order $n$, the irreducible representations are indexed by \emph{integer partitions} of size $n$, that is non-increasing sequences of positive integers $\lambda=(\lambda_{1},\ldots,\lambda_{\ell})$ with $\sum_{i=1}^{\ell}\lambda_{i}=n$. In the following we denote $\pym(n)=\widehat{\sym}(n)$ the set of integer partitions of size $n$, and $\ell(\lambda)=\ell$ the length of a partition. We shall also consider the infinite symmetric group $\sym(\infty)=\bigcup_{n \ge 1} \sym(n)$, which is the group of permutations of the set of natural numbers that have a finite support.

\begin{definition}
A \emph{central measure} on partitions is a family $(\proba_{\tau,n})_{n \in \N}$ of spectral measures on the sets $\pym(n)$ that come from the same trace of the infinite symmetric group $\sym(\infty)$. In other words $(\proba_{\tau,n})_{n \in \N}$ is a central measure if there exists a trace $\tau : \sym(\infty) \to \C$ such that
$$\tau_{|\sym(n)}=\sum_{\lambda \in \pym(n)} \proba_{\tau,n}[\lambda]\,\widehat{\chi}^{\lambda}.$$
\end{definition}

\begin{example}
The regular trace $\tau(\sigma)=\mathbbm{1}_{\sigma=\mathrm{id}}$ corresponds to the Plancherel measures of the symmetric groups, given by the formula $\proba_{n}[\lambda]=(\dim V^\lambda)^{2}/n!$, where $V^{\lambda}$ is the $\sym(n)$-irreducible module of label $\lambda$. They have been extensively studied in connection with Ulam's problem of the longest increasing subsequence and with random matrix theory, see \emph{e.g.} \cite{BDJ99,BOO00,Oko00,IO02}.
\end{example}
\bigskip

A central measure $(\proba_{\tau,n})_{n \in \N}$ is non-negative if and only if $(\tau(\rho_{i}\rho_{j}^{-1}))_{1\leq i,j \leq n}$ is Hermitian non-negative definite for any finite family of permutations $\rho_{1},\ldots,\rho_{n}$. The set of non-negative central measures, \emph{i.e.}, coherent systems of probability measures on partitions has been identified in \cite{Tho64} and later studied in \cite{KV81}. Call extremal a non-negative trace on $\sym(\infty)$  that is not a positive linear combination of non-negative traces. Then, extremal central measures are indexed by the infinite-dimensional \emph{Thoma simplex}
$$\Omega=\bigg\{\omega=(\alpha,\beta)=\big((\alpha_{1}\geq \alpha_{2}\geq \cdots \geq 0),(\beta_{1}\geq \beta_{2}\geq \cdots \geq 0)\big)\,\,\bigg|\,\,\sum_{i=1}^{\infty}\alpha_{i}+\beta_{i}\leq 1\bigg\}.$$
The trace on the infinite symmetric group corresponding to a parameter $\omega$ is given by

\begin{equation}\label{eq:def_tau_omega}
\tau_{\omega}(\sigma)=\prod_{c \in C(\sigma)} p_{|c|}(\omega) \quad\text{with }p_{1}(\omega)=1,\,\,\,p_{k\geq 2}(\omega)=\sum_{i=1}^{\infty}(\alpha_{i})^{k}+(-1)^{k-1}(\beta_{i})^{k},
\end{equation}
$C(\sigma)$ denoting the set of cycles of $\sigma$. Kerov and Vershik have shown that if $\omega \in \Omega$ and $\rho \in \sym(\infty)$ are fixed, then the random character value $\widehat{\chi}^{\lambda}(\rho)$ with $\lambda$ chosen according to the central measure $\proba_{\omega,n}$ converges in probability towards the trace $\tau_{\omega}(\rho)$. Informally, central measures on partitions and extremal traces of $\sym(\infty)$ are {\em concentrated}. More recently, it was shown by F\'eray and M\'eliot that this concentration is Gaussian, see \cite{FM12,Mel12}. The aim of this section is to use the techniques of Sections \ref{sec:depgraph}-\ref{sec:erdosrenyi} in order to prove the following:

\begin{theorem}\label{thm:modgaussianrcv}
Fix a parameter $\omega \in \Omega$, and denote $\rho$ a $k$-cycle in $\sym(\infty)$ (for $k \ge 2$). Assume $p_{2k-1}(\omega)-(p_{k}(\omega))^{2}\neq 0$. Denote then $\RCV$ the random character value $\widehat{\chi}^{\lambda}(\rho)$, where:\vspace{2mm}
\begin{itemize}
\item $\lambda \in \pym(n)$ is picked randomly according to the central measure $\proba_{\omega,n}$, \vspace{2mm}
\item and $\widehat{\chi}^{\lambda}$ denotes the normalized irreducible character indexed by $\lambda$ of $\sym(n)$, that is 
$$\widehat{\chi}^{\lambda}(\rho)=\frac{\mathrm{tr}\, \Pi^{\lambda}(\rho)}{\dim V^{\lambda}}\qquad \text{ with }(V^{\lambda},\Pi^{\lambda}) \text{ irreducible representation of }\sym(n).$$
\end{itemize}
The rescaled random variable $n^{2/3}\,\big[\RCVk-p_{k}(\omega)\big]$ converges in the mod-Gaussian sense with parameters $t_{n}=n^{1/3}\,\sigma^{2}$ and limiting function $\psi(z)=\exp(L\,\frac{z^{3}}{6})$, where
\begin{align*}
\sigma^{2}&=k^{2}\,\big(p_{2k-1}(\omega)-p_{k}(\omega)^{2}\big);\\
L&= k^{3}\,\big((3k-2)\,p_{3k-2}(\omega)-(6k-3)\,p_{2k-1}(\omega)\,p_{k}(\omega)+(3k-1)\,p_{k}(\omega)^{3}\big).
\end{align*}
\end{theorem}

As in Section \ref{sec:erdosrenyi}, the mod-Gaussian convergence is proved by bounds on cumulants of type \eqref{eq:superbound}.
Furthermore, the hypothesis \eqref{eq:limitcumulant} on the third and second cumulant are ensured
by the polynomiality of joint cumulants --- Lemma \ref{lem:cumulantcharacterpoly}.
Therefore, we can apply Propositions \ref{prop:largedeviationscumulants} and \ref{prop:normalityzone}.
\begin{corollary}\label{cor:moderatedeviationcharacter}
Let $\SubGraph_{k}=\RCVk$ be the random character value on a $k$-cycle as defined above.
Then $n^{1/2}\, (\SubGraph_{k}-p_{k}(\omega))$ satisfies a central limit theorem with normality zone 
$o(n^{1/6})$.
Moreover, at the edge of this normality zone and at a slightly larger scale, the deviation probabilities are given by:
for any sequence $x$ of positive numbers bounded away from $0$ with $x_n=o\big( n^{1/12} \big)$,
one has
\begin{align*}
    \proba\left[n^{1/2} (\SubGraph_{k}-p_{k}(\omega))\geq n^{1/6} \sigma^2 x_n\right]&=
\frac{\E^{-\frac{(x_n)^2\, n^{1/3}\sigma^2}{2}}}{x_n\, n^{1/6}\sigma \sqrt{2\pi}}\,\E^{\frac{L(x_n)^3}{6}}\,(1+o(1)).\\
    \proba\left[n^{1/2} (\SubGraph_{k}-p_{k}(\omega))\leq - n^{1/6} \sigma^2 x_n\right]&=
\frac{\E^{-\frac{(x_n)^2\, n^{1/3}\sigma^2}{2}}}{x_n\, n^{1/6}\sigma \sqrt{2\pi}}\,\E^{\frac{-L(x_n)^3}{6}}\,(1+o(1)).
\end{align*}
where $\sigma^{2}$ and $L$ as in Theorem \ref{thm:modgaussianrcv}.
\end{corollary}\bigskip


\begin{remark}\label{rem:limitvarianceispositive}
The condition $\sigma^{2}>0$ is satisfied as soon as the sequence $\alpha \sqcup \beta$ associated to the Thoma parameter $\omega$ contains two different non-zero coordinates. Indeed, for any summable non-increasing non-negative sequence $\gamma=(\gamma_{1},\gamma_{2},\ldots)$ with $\gamma_{i}>\gamma_{i+1}$ for some $i$, one has
$$\left(\sum_{i=1}^{\infty} (\gamma_{i})^{k-\eps} \right)\left(\sum_{i=1}^{\infty} (\gamma_{i})^{k+\eps} \right) \geq \left(\sum_{i=1}^{\infty} (\gamma_{i})^{k} \right)^{2}$$
with equality if and only if $\eps=0$. Indeed, the derivative of the function of $\eps$ on the left-hand side is
$$\sum_{i<j} \left(\gamma_{i}\gamma_{j}\right)^{k}\,\log\!\left(\frac{\gamma_{i}}{\gamma_{j}}\right)\,\left(\left(\frac{\gamma_{i}}{\gamma_{j}}\right)^{\!\eps}-\left(\frac{\gamma_{j}}{\gamma_{i}}\right)^{\!\eps}\,\right).$$
Applying the result to $\gamma=\alpha \sqcup \beta$ and $\eps=k-1$, we obtain on the left-hand side
$$\left(\sum_{i=1}^{\infty} \gamma_{i} \right)\left(\sum_{i=1}^{\infty} (\gamma_{i})^{2k-1} \right) = \left(\sum_{i=1}^{\infty} \alpha_{i}+\beta_{i} \right)\,p_{2k-1}(\omega)\leq p_{2k-1}(\omega)$$
and on the right-hand side
$$\left(\sum_{i=1}^{\infty} (\gamma_{i})^{k}\right)^{2} \geq \left(\sum_{i=1}^{\infty} (\alpha_{i})^{k} + (-1)^{k-1}(\beta_{i})^{k}\right)^{2}=(p_{k}(\omega))^{2}.$$
This proof shows that the condition $\sigma^{2}>0$ is also satisfied if $0<\sum_{i=1}^{\infty} \alpha_{i}+\beta_{i}<1$.
\end{remark}


This Section is organized as follows. In Section \ref{subsec:prelim_chmu}, we present the necessary material. In Section \ref{subsec:boundcumulantchmu}, we then prove bounds on these cumulants similar to those of Proposition \ref{prop:boundcumulantsubgraph}, and we compute the limits of the second and third cumulants. This will allow us to use in Section \ref{subsec:asymptoticrcv} the framework of Section \ref{subsec:deviationscumulant} in order to prove the results stated above. We shall also detail some consequences of these results for the shapes of the random partitions $\lambda \sim \proba_{n,\omega}$ viewed as Young diagrams, in the spirit of \cite{FM12,Mel12}. \bigskip




\subsection{Preliminaries}\label{subsec:prelim_chmu}

\subsubsection{Non-commutative probability theory}
The originality of this section is that, although the problem is formulated in a classical probability space,
it is natural to work in the setting of non-commutative probability theory.
\begin{definition}
    A {\em non-commutative probability space} is a complex unital $\star$-algebra $\mathscr{A}$ 
    with some linear functional $\varphi:\mathscr{A} \to \C$ such that $\varphi(1)=1$ and,
    for any $a \in \mathscr{A}$, $\varphi(a^\star a) \ge 0$.
\end{definition}
This generalizes the notion of probability space: elements of $\mathscr{A}$ should be thought as random variables, while $\varphi$ should be thought as the expectation. The difference is that, unlike random variables in usual probability theory, elements of $\mathscr{A}$ are not assumed to commute. Usually one also assumes that $\varphi$ is tracial, \emph{i.e.}, $\varphi(ab)=\varphi(ba)$ for any $a,b\in\mathscr{A}$.\bigskip

There are five natural analogues of the notion of independence in non-commutative probability theory, see~\cite{Muraki03}. In our context, the relevant one is the following one, sometimes called {\em tensor independence} \cite[Definition 1.1]{HS10}.
\begin{definition}
    Two subalgebras $\mathscr{A}_1$ and $\mathscr{A}_2$ of $\mathscr{A}$ are {\em tensor independent} if and only if, for any sequence $a_1,\dots,a_r$ with, for each $i$, $a_i \in \mathscr{A}_1$ or $a_i \in \mathscr{A}_2$, one has
    \[\varphi(a_1 \dots a_r) = 
    \varphi \left(\prod_{\substack{1\le i \le r \\ a_i \in \mathscr{A}_1}}^{\rightarrow} a_i\right)
    \varphi \left(\prod_{\substack{1\le i \le r \\ a_i \in \mathscr{A}_2}}^{\rightarrow} a_i\right)
    .\]
    The arrow on the product sign means that the $a_i$ in the product appear in the same order as in $a_1,\dots,a_r$.
\end{definition}

With this definition of independence, the notion of dependency graph presented in Section \ref{subsec:dependencygraphs} is immediately extended to the non-commutative framework. One can also define joint cumulants as follows: if $a_1,\dots,a_r$ are elements in $\mathscr{A}$, we set
$$\kappa(a_1,\dots,a_r) = \sum_{\pi} \,\mu(\pi) \,\prod_{B \in \pi} \varphi \!\left( 
\prod^{\rightarrow}_{i \in B} a_i \right).$$
Note that, in the proof of Theorem~\ref{thm:dependencygraphsrefined}, independence is only used in equation~\eqref{eq:alsoinnoncommutative}. By definition of tensor independence, equation~\eqref{eq:alsoinnoncommutative} also holds in the non-commutative setting and hence, so does Theorem~\ref{thm:dependencygraphsrefined}.
\bigskip



\subsubsection{Two probability spaces}
From now on, we fix an element $\omega$ in the Thomas simplex $\Omega$. Denote $\C\sym(n)$  the group algebra of $\sym(n)$. The function $\tau_\omega$, defined by Equation \eqref{eq:def_tau_omega}, can be linearly extended to $\C\sym(n)$. Then $(\C\sym(n),\tau_{\omega})$ is a non-commutative probability space.
\bigskip

Note that we are now working with two probability spaces: the non-commutative probability space $(\C\sym(n),\tau_{\omega})$ and the usual probability space that we want to study (the set of Young diagrams of size $n$ with the probability measure $\proba_{\omega,n}$). They are related as follows. Consider an element $y$ in $\C\sym(n)$ and define the random variable (for the usual probability space) $X_y$ by $X_y(\lambda)=\widehat{\chi}(y)$.
Then one has
\[\esper_{\proba_{\omega,n}}(X_y) = \sum_{\lambda \vdash n} \proba_{\omega,n}(\lambda)
\widehat{\chi}(y) = \tau_\omega(y).\]
In other words, the {\em expectations} of $y$ (in the non-commutative probability space) and of $X_y$ (in the usual probability space) coincide (recall that the trace of a non-commutative probability space, here $\tau_\omega$, is considered as an expectation).
\bigskip

Besides, if we restrict to the {\em center} of $(\C\sym(n),\tau_{\omega})$, then the map $y \mapsto X_y$ is an {\em algebra morphism}, called {\em discrete Fourier transform}. As a consequence, if $y_1,\dots,y_r$ lie in the center of $(\C\sym(n),\tau_{\omega})$, their joint moments (and joint cumulants) are the same as those of $X_{y_1},\dots,X_{y_r}$.



\subsubsection{Renormalized conjugacy classes and polynomiality of cumulants}
Given a partition $\mu=(\mu_{1},\ldots,\mu_{\ell})$ of size $|\mu|=\sum_{i=1}^{\ell}\mu_{i}=k$, we denote 
$$\varSigma_{\mu,n}=\sum_{A} \rho_\mu(A) \text{ where } \rho_\mu(A)=(a_1,\ldots,a_{\mu_{1}})(a_{\mu_1+1},\ldots,a_{\mu_1+\mu_{2}})\cdots.$$
In the equation above, the formal sum is taken over arrangements in $\arr(n,k)$ and is considered as an element of the group algebra $\C\sym(n)$. It clearly lies in its center. Besides, $\varSigma_{\mu,n}$ is the sum of $n\fall{k}$ elements of cycle-type $\mu$, hence, if $\rho$ is a fixed permutation of type $\mu$, one has:
\[X_{\varSigma_{\mu,n}} = n\fall{k} X_\rho.\]
Note that considering these elements $\varSigma_{\mu,n}$ and their normalized characters is a classical trick in the study of central measures on Young diagrams; see \cite{IO02,Sni06b,FM12}.
\bigskip

Fix some permutations $\rho_1,\dots,\rho_r$ of respective size $k_1,\dots,k_r$. Denote $\mu^{1},\ldots,\mu^{r}$ their cycle-types.
\begin{align}
n\fall{k_{1}}\cdots n\fall{k_{r}}\,\,\kappa\!\left(\SubGraph_{\rho_{\mu^{1}}},\ldots,\SubGraph_{\rho_{\mu^{r}}}\right)&=\kappa(\varSigma_{\mu^{1}},\ldots,\varSigma_{\mu^{r}})\nonumber\\
&=\sum_{\substack{A^{1}\in \arr(n,k_{1}) \vspace{-1mm} \\ \vdots  \vspace{1mm}\\ A^{r} \in \arr(n,k_{r})}}
\kappa\left(\rho_{\mu^{1}}(A^{1}),\ldots,\rho_{\mu^{r}}(A^{r})\right).\label{eq:listequality}
\end{align}
As in the framework of subgraph count statistics,
the invariance of $\tau_\omega$ by conjugacy of its argument
implies that the joint cumulant $\kappa\left(\rho_{\mu^{1}}(A^{1}),\ldots,\rho_{\mu^{r}}(A^{r})\right)$
depends only on the graph $G_{\mathbb{A}}$ associated to the family of arrangement
$\mathbb{A}=(A^{1},\dots,A^{r})$.
Copying the proof of Corollary~\ref{cor:jointcumulantpoly},
we get:
\begin{lemma}\label{lem:cumulantcharacterpoly}
Fix some integer partitions  $\mu^1,\dots,\mu^r$. Then the rescaled joint cumulant 
$$\kappa(\varSigma_{\mu^{1}},\ldots,\varSigma_{\mu^{r}})=n\fall{k_{1}}\cdots n\fall{k_{r}}\,\,\kappa\!\left(\SubGraph_{\rho_{\mu^{1}}},\ldots,\SubGraph_{\rho_{\mu^{r}}}\right)
$$ 
is a polynomial in $n$.
\end{lemma}\bigskip
