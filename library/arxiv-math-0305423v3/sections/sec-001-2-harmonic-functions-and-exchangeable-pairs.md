---
doc_id: arxiv-math-0305423v3
doc_title: "Stein's method and Plancherel measure of the symmetric group"
section_id: sec-001-2-harmonic-functions-and-exchangeable-pairs
section_title: "Harmonic functions and exchangeable pairs"
section_number: 2
pages: 5-8
source_pdf: 0305423v3.pdf
source_sha256: e4554f9084ba4935
toc_source: outline
text_source: latex
latex_prose_ratio: 0.989
latex_coverage_ratio: 1.0
doc_brief: "Stein's method and Plancherel measure of the symmetric group — We initiate a Stein’s method approach to the study of the Plancherel measure of the symmetric group."
---
\label{harmonic} 

	To begin we recall the theory of harmonic functions on Bratelli diagrams. This is a beautiful subject with deep connections to probability theory and representation theory. Two excellent surveys are \cite{K2} and \cite{BO}.

	The basic set-up is as follows. One starts with a
Bratteli diagram; that is an oriented graded graph $\Gamma= \cup_{n \geq 0} \Gamma_n$ such that

\begin{enumerate}
\item $\Gamma_0$ is a single vertex $\emptyset$.
\item If the starting vertex of an edge is in $\Gamma_i$, then its end vertex is in $\Gamma_{i+1}$.
\item Every vertex has at least one outgoing edge.
\item All $\Gamma_i$ are finite.
\end{enumerate}

	For two vertices $\lambda, \Lambda \in \Gamma$, one writes $\lambda \nearrow \Lambda$ if there is an edge from $\lambda$ to
$\Lambda$. Part of the underlying data is a multiplicity function
$\kappa(\lambda,\Lambda)$. Letting the weight of a path in $\Gamma$ be
the product of the multiplicities of its edges, one defines the
dimension $dim(\Lambda)$ of a vertex $\Lambda$ to be the sum of the
weights over all maximal length paths from $\emptyset$ to $\Lambda$; $dim(\emptyset)$ is taken to be $1$. Given a Bratteli
diagram with a multiplicity function, one calls a function $\phi$ {\it
harmonic} if $\phi(\emptyset)=1$, $\phi(\lambda) \geq 0$ for all $\lambda \in
\Gamma$, and \[ \phi(\lambda) = \sum_{\Lambda: \lambda \nearrow
\Lambda} \kappa(\lambda,\Lambda) \phi(\Lambda).\] An equivalent
concept is that of coherent probability distributions. Namely a set
$\{M_n\}$ of probability distributions $M_n$ on $\Gamma_n$ is called
{\it coherent} if \[ M_{n}(\lambda) = \sum_{\Lambda: \lambda
\nearrow \Lambda} \frac{dim(\lambda)
\kappa(\lambda,\Lambda)}{dim(\Lambda)} M_{n+1}(\Lambda).\] The formula
allowing one to move between the definitions is $\phi(\lambda) =
\frac{M_n(\lambda)}{dim(\lambda)}$.

        One reason the set-up is interesting from the viewpoint of
probability theory is the fact that every harmonic function can be
written as a Poisson integral over the set of extreme harmonic
functions (i.e. the boundary). For the Pascal lattice (vertices of $\Gamma_n$ are pairs
$(k,n)$ with $k=0,1,\cdots,n$ and $(k,n)$ is connected to $(k,n+1)$
and $(k+1,n+1)$), this fact is the simplest instance of de Finetti's
theorem, which says that an infinite exchangeable sequence of $0-1$ random variables is a mixture of coin toss sequences for different
probabilities of heads. One of Kerov's insights in \cite{K2} is that one can prove Selberg type integral formulas by expressing interesting harmonic functions as integrals over the boundary. The paper \cite{BO} carries out this program in many cases.

	Before proceeding, let us indicate that Plancherel measure is
	a special case of this set-up. Here the lattice which one uses
	is the Young lattice, that is $\Gamma_n$ consists of all
	partitions of size $n$, and a partition of size $n$ is
	adjoined to a partition of size $n+1$ in $\Gamma_{n+1}$ if the
	partition of size $n+1$ can be obtained from the partition of
	size $n$ by adding a box. The multiplicity function
	$\kappa(\lambda,\Lambda)$ is equal to 1 on each edge. The
	dimension function $dim(\lambda)$ is simply
	$\frac{n!}{\prod_{x} h(x)}$, the dimension of the irreducible
	representation of the symmetric group parameterized by the
	partition $\lambda$. Then one can show that if $M_n$ is the
	Plancherel measure, the family of measures $\{M_n\}$ is
	coherent \cite{K2}. More generally it follows from Frobenius
	reciprocity that if $H$ is a subgroup of $G$, $M_H$ is
	Plancherel measure of $H$ and $M_G$ is Plancherel measure of
	$G$, and $\kappa(\lambda,\Lambda)$ is the multiplicity of
	$\lambda$ in the restriction of $\Lambda$ from $G$ to $H$,
	then \[ M_{H}(\lambda) = \sum_{\Lambda: \lambda \nearrow
	\Lambda} \frac{dim(\lambda)
	\kappa(\lambda,\Lambda)}{dim(\Lambda)} M_{G}(\Lambda).\]

	The relevance of these considerations is Proposition
	\ref{constructchain}. Parts 1 and 2 are implicit in
	\cite{K2}. Recall that a Markov chain $J$ on a finite set $X$
	is said to be reversible with respect to $\pi$ if $\pi(x)
	J(x,y) = \pi(y) J(y,x)$ for all $x,y$. It is easy to see that
	if $J$ is reversible with respect to $\pi$, then $\pi$ is
	stationary for $J$ (i.e. that $\pi(y) = \sum_{x \in X}
	\pi(x)J(x,y)$). Note that if $W$ is any statistic on $X$ and
	$W^*$ is obtained by evaluating the statistic after taking a
	step according to a Markov chain which is reversible with
	respect to $\pi$, then $(W,W^*)$ is an exchangeable pair under
	the probability measure $\pi$.

\begin{prop} \label{constructchain} Suppose that the family of measures $\{M_n\}$ is coherent for the Bratelli diagram. 
\begin{enumerate}
\item If $\lambda$ is chosen from the measure $M_n$, and one moves from $\lambda$ to $\Lambda$ with probability $\frac{dim(\lambda) M_{n+1}(\Lambda) \kappa(\lambda,\Lambda)}{dim(\Lambda) M_n(\lambda)}$, then $\Lambda$ is distributed according to the measure $M_{n+1}$.
\item If $\Lambda$ is chosen from the measure $M_{n+1}$, and one moves from $\Lambda$ to $\mu$ with probability $\frac{dim(\mu) \kappa(\mu,\Lambda)}{dim(\Lambda)}$, then $\mu$ is distributed according to the measure $M_n$.
\item The Markov chain $J$ on vertices in level $\Gamma_n$ of the Bratelli diagram given by moving from $\lambda$ to $\mu$ with probability \[ J(\lambda,\mu) = \frac{dim(\lambda) dim(\mu)}{M_n(\lambda)} \sum_{\Lambda \in \Gamma_{n+1}} \frac{M_{n+1}(\Lambda) \kappa(\lambda,\Lambda) \kappa(\mu,\Lambda)}{dim(\Lambda)^2}\] is reversible with stationary distribution $M_n$.
\item The Markov chain $J$ on vertices in level $\Gamma_n$ of the
Bratelli diagram given by moving from $\lambda$ to $\mu$ with
probability \[ J(\lambda,\mu) = \frac{M_n(\mu)}{dim(\lambda) dim(\mu)}
\sum_{\tau \in \Gamma_{n-1}} \frac{dim(\tau)^2 \kappa(\tau, \lambda)
\kappa(\tau,\mu)} { M_{n-1}(\tau)}\] is reversible with stationary
distribution $M_n$.
\end{enumerate}
\end{prop}

\begin{proof} For part 1, observe that \begin{eqnarray*} & & \sum_{\lambda \in \Gamma_n}
 M_n(\lambda) \frac{dim(\lambda) M_{n+1}(\Lambda)
 \kappa(\lambda,\Lambda)}{dim(\Lambda) M_n(\lambda)}\\ & = &
 \frac{M_{n+1}(\Lambda)}{dim(\Lambda)} \sum_{\lambda \in \Gamma_n} dim(\lambda) \kappa(\lambda,\Lambda)\\ & = &
 M_{n+1}(\Lambda).\end{eqnarray*} Note that the transition probabilities sum to 1 because the measures $\{M_n\}$ are coherent. Part 2 is similar and also uses the fact that $\{M_n\}$ is coherent. For part 3 reversibility is immediate from the definitions, provided that the transition probabilities for $J$ sum to 1. But $J$ is simply what one gets by moving up one level in the Bratelli diagram according to the transition
	mechanism of part 1, and then moving down according to the
	transition mechanism of part 2. Part 4 is similar; one first moves down the Bratelli diagram and then up. \end{proof}

	One can investigate more general Markov chains where one moves up or down by an amount $k$. This is done in Section \ref{decompose} where it is applied to tensor products. However in the application of Stein's method, we will only use the chain $J$ in part 3 of the proposition (the chain in part 4 would work as well). This chain simplifies in many cases of interest. We mention two of them. 

{\bf Example 1:} The first example is the Plancherel measure of $S_n$. We
already indicated how it fits in with harmonic functions on the Young
lattice. Let $parents(\lambda,\mu)$ denote the set of partitions above
both $\lambda,\mu$ in the Young lattice (this set has size $0$ or $1$
unless $\lambda=\mu$). Then
$J(\lambda,\mu)=\frac{dim(\mu)|parents(\lambda,\mu)|}{(n+1)dim(\lambda)}$. Lemma
\ref{parents} in the next section will use representation theory to
derive a more complicated (but useful) expression for $J(\lambda,\mu)$
as a sum over the symmetric group $S_n$.

{\bf Example 2:} The second example concerns cycles of random
permutations. As explained in \cite{K2}, the partitions of $n$ index
the conjugacy classes of the symmetric group and the probability
measure on partitions corresponding to the conjugacy class of a random
permutation is a coherent family of measures with respect to the
Kingman lattice. Here the underlying lattice is the same as the Young
lattice, but the multiplicity function $\kappa(\lambda,\Lambda)$ is
the number of rows of length $j$ in $\Lambda$, where $\lambda$ is
obtained from $\Lambda$ by removing a box from a row of length
$j$. Also $dim(\lambda)=\frac{n!}{\lambda_1 ! \cdots \lambda_l!}$
where $l$ is the number of rows of $\lambda$ and $\lambda_i$ is the
length of row $i$ of $\lambda$. So the Markov chain $J$ amounts to the
following. Letting $m_r(\lambda)$ denote the number of rows of length
$r$ in $\lambda$, first obtain $\Lambda$ by adding a box to a row of
length $r$ with chance $\frac{r m_r(\lambda)}{n+1}$, or to an empty
row with probability $\frac{1}{n+1}$. Then remove a box from a row of
$\Lambda$ of length $s$ with probability $\frac{s
m_s(\Lambda)}{n+1}$. The cycle structure of random permutations (and
more generally the Ewens sampling formula) is very well understood,
but still in future work we intend to revisit them by Stein's method
(using the exchangeable pairs in this section) and to study the
spectral properties of the Markov chains of Proposition
\ref{constructchain}.
