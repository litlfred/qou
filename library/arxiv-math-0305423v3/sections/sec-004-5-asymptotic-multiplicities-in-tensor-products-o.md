---
doc_id: arxiv-math-0305423v3
doc_title: "Stein's method and Plancherel measure of the symmetric group"
section_id: sec-004-5-asymptotic-multiplicities-in-tensor-products-o
section_title: "Asymptotic multiplicities in tensor products of representations"
section_number: 5
pages: 14-18
source_pdf: 0305423v3.pdf
source_sha256: e4554f9084ba4935
toc_source: outline
text_source: latex
latex_prose_ratio: 0.976
latex_coverage_ratio: 0.965
doc_brief: "Stein's method and Plancherel measure of the symmetric group — We initiate a Stein’s method approach to the study of the Plancherel measure of the symmetric group."
---
\label{decompose}

	This section gives an intruiging method for understanding some
	asymptotic aspects of the decomposition of tensor products of
	certain representations of the symmetric group. A recent paper
	which investigates this topic from the viewpoint of free
	probability theory is \cite{Bi}. However the methods and
	results are completely different from those presented
	here. The main new idea of this section is to use spectral
	theory of Markov chains. This is further developed in
	\cite{F} (connections with card shuffling, generalization to
	other groups) and in \cite{Fu2} (generalizations to arbitrary
	representations of finite groups).

	Throughout this section $X$ is the set of partitions of size $n$, endowed with Plancherel measure $\pi$. We consider the space of real valued functions $\ell^2(\pi)$ with the norm \[ ||f||_2 = \left( \sum_x |f(x)|^2 \pi(x) \right)^{1/2}.\] If $J(x,y)$ is the transition rule for a Markov chain, the associated Markov operator (also denoted by $J$) on $\ell^2(\pi)$ is given by $Jf(x) = \sum_y J(x,y) f(y)$. Let $J^r(x,y)=J_x^r(y)$ denote the chance that the Markov chain started at $x$ is at $y$ after $r$ steps.

	If the Markov chain with transition rule $J(x,y)$ is reversible with respect to $\pi$ (i.e. $\pi(x) J(x,y) = \pi(y) J(y,x)$ for all $x,y$), then the operator $J$ is self adjoint with real eigenvalues \[ -1 \leq \beta_{min}=\beta_{|X|-1} \leq \cdots \leq \beta_1 \leq \beta_0=1.\] Let $\psi_i$ ($i=0,\cdots,|X|-1$) be an orthonormal basis of eigenfunctions such that $J\psi_i = \beta_i \psi_i$ and $\psi_0 \equiv 1$. Define $\beta = max \{|\beta_{min}|,\beta_1\}$.

	The total variation distance between the measures $J_x^r$ and $\pi$ is defined by $||J_x^r- \pi||_{TV} = \frac{1}{2} \sum_{y} |J_x^r(y)-\pi(y)|$. (The application to representation theory does not require total variation distance but this concept is useful for understanding the Markov chain $J$; see Theorem \ref{main2}).

	The following lemma is well-known; for a proof see \cite{DSa}. Part 1 is essentially Jensen's inequality. 

\begin{lemma} \label{classic}
\begin{enumerate}
\item $2 ||J_x^r - \pi||_{TV} \leq ||\frac{J_x^r}{\pi}-1||_2$.
\item $J^r(x,y) = \sum_{i=0}^{|X|-1} \beta_i^r \psi_i(x) \psi_i(y) \pi(y)$.
\item $||\frac{J_x^r}{\pi}-1||_2^2 = \sum_{i=1}^{|X|-1} \beta_i^{2r} |\psi_i(x)|^2 \leq \frac{1-\pi(x)}{\pi(x)} \beta^{2r}$.
\end{enumerate}
\end{lemma}

	Next we specify a class of Markov chains to which we will apply Lemma \ref{classic}. Recall from Proposition \ref{constructchain} that there is a natural transition mechanism for moving up one step in the Young lattice or down one step in the Young lattice. For $1 \leq k \leq n$, let $J(k)$ be the Markov chain which from a partition of $n$ first moves down $k$ steps in the Young lattice (one at a time according to part 2 of Proposition \ref{constructchain}), and then moves back up $k$ steps in the Young lattice (one at a time according to part 1 of Proposition \ref{constructchain}). Proposition \ref{diagonalize} finds the eigenvalues and eigenfunctions for the corresponding operators $J(k)$. The word Mult. stands for multiplicity.

\begin{prop} \label{diagonalize} The eigenvalues and eigenfunctions of the operator $J(k)$ on partitions of size $n$ are indexed by conjugacy classes $C$ of the symmetric group on $n$ symbols.
\begin{enumerate}
\item Letting $n_1(C)$ denote the number of fixed points of the class $C$, the eigenvalue parameterized by $C$ is $\frac{(n_1(C))(n_1(C)-1) \cdots (n_1(C)-k+1)}{n(n-1) \cdots (n-k+1)}$.
\item The orthonormal basis of eigenfunctions $\psi_C$ is defined by $\psi_C(\lambda)=|C|^{\frac{1}{2}} \frac{\chi^{\lambda}(C)}{dim(\lambda)}$.
\end{enumerate}
\end{prop}

\begin{proof} From Proposition \ref{constructchain}, the chance that the Markov
chain $J(k)$ moves from $\lambda$ to $\mu$ is easily seen to be \[ \frac{dim(\mu)}{ (n)(n-1) \cdots (n-k+1) dim(\lambda)} \sum_{\tau \atop |\tau|=n-k} dim(\lambda/\tau) dim(\mu/\tau).\] From the branching rules of irreducible representations of the symmetric group \cite{Sa}, this is   \[ \frac{dim(\mu)}{dim(\lambda)} \frac{Mult. \ \mu \
in \ Ind^{S_n}_{S_{n-k}} Res^{S_n}_{S_{n-k}} (\lambda)}{n(n-1)\cdots
(n-k+1)}.\] Now observe that the $\psi_C(\lambda)=|C|^{\frac{1}{2}}
\frac{\chi^{\lambda}(C)}{dim(\lambda)}$ is an eigenfunction with the asserted eigenvalue because
\begin{eqnarray*} & & \frac{|C|^{\frac{1}{2}}}{(n) \cdots (n-k+1) dim(\lambda)} \sum_{\mu} \chi^{\mu}(C) \cdot  Mult. \ \mu \ in \ Ind^{S_n}_{S_{n-k}}
Res^{S_n}_{S_{n-k}}(\lambda) \\ & = & \frac{|C|^{\frac{1}{2}}}{n (n-1) \cdots (n-k+1)
dim(\lambda)} Ind^{S_n}_{S_{n-k}} Res^{S_n}_{S_{n-k}}(\lambda) [C]\\ & = &
\frac{(n_1(C))(n_1(C)-1) \cdots (n_1(C)-k+1)}{n(n-1)\cdots (n-k+1)}
\frac{|C|^{\frac{1}{2}} \chi^{\lambda}(C)}{dim(\lambda)}. \end{eqnarray*} The last equality is Lemma \ref{induced}. The fact that
$\psi_C$ are orthonormal follows from Lemma \ref{orth1}. Being
linearly independent, they are a basis for $\ell ^2(\pi)$ since the
number of conjugacy classes of $S_n$ is equal to the number of partitions of
$n$. \end{proof}

Remarks:
\begin{enumerate}
\item A similar argument shows that the chain which moves up $k$ steps (one at a time) and then down $k$ steps (one at a time) has the $\psi_C$ as an orthonormal basis with eigenvalues $\frac{(n_1(C)+1)(n_1(C)+2) \cdots (n_1(C)+k)}{(n+1)(n+2) \cdots (n+k)}.$ The results in the remainder of this section could be applied to that Markov chain as well.

\item It is remarkable that the set of eigenvalues of the Markov chain
$J(1)$ is precisely the set of eigenvalues of the top to random
shuffle (see \cite{DFP} for background on top to random
shuffles). This is not coincidence; the paper \cite{F} explains this
and more general facts in terms of the Robinson-Schensted-Knuth
correspondence.
\end{enumerate}

	Theorem \ref{main2} studies the convergence properties of the Markov chains $J(k)$. Throughout all logs are taken base e, as usual.
	
\begin{theorem} \label{main2} Let $(n)$ denote
 the partition which consists of one part of size $n$ (corresponding
 to the trivial representation of $S_n$). Let $\beta=\frac{(n-k)(n-k-1)}{(n)(n-1)}$. Then for $n \geq 3, 1 \leq k < n$, \[
 2||J(k)_{(n)}^r-\pi||_{TV} \leq \left( \sum_{\lambda \atop
 |\lambda|=n} |\frac{J(k)^r((n),\lambda)}{\pi(\lambda)}-1|^2
 \pi(\lambda) \right)^{1/2} \leq \sqrt{n!} \left( \beta
 \right)^{r}.\] Thus for $r > \frac{n log(n) +
 2c}{2log(\frac{1}{\beta})}$, \[ ||J(k)_{(n)}^r-\pi||_{TV} \leq
 \frac{(2 \pi)^{\frac{1}{4}}}{2} e^{-c}.\]
\end{theorem}

\begin{proof} From parts 1 and 3 of Lemma \ref{classic}, to prove the first assertion it is enough to show that for the chain $J(k)$, $\beta=\frac{(n-k)(n-k-1)}{(n)(n-1)}$ and that $\frac{1-\pi((n))}{\pi((n))} \leq n!$. The value of $\beta$ follows from Proposition \ref{diagonalize} (note that a permutation on n symbols cannot have exactly n-1 fixed points) and the inequality holds since $\pi((n))=\frac{1}{n!}$. This proves the first assertion. 

	The second assertion follows from the Stirling formula bound
\cite{Fe} \[ n! \leq \sqrt{2 \pi}
e^{-n+\frac{1}{12n}+(n+\frac{1}{2})log(n)}, \] for then
\begin{eqnarray*} \sqrt{n!} \left( \beta \right)^{r} &
\leq & (2 \pi)^{\frac{1}{4}} e^{r
log(\beta)-\frac{n}{2}+\frac{1}{24n}+\frac{1}{2}(n+\frac{1}{2})log(n)}\\
& \leq & (2 \pi)^{\frac{1}{4}} e^{r log(\beta)+\frac{n
log(n)}{2}}. \end{eqnarray*} \end{proof}

	Now we give the application to representation theory. We remind the reader that $Ind_{S_{n-1}}^{S_n}(1)$ is the defining representation of the symmetric group (i.e. the n dimensional permutation representation on the symbols $1,\cdots,n$), and hence corresponds to the case $k=1$ below. As usual, $\pi(\lambda)=\frac{dim(\lambda)^2}{n!}$ denotes the Plancherel measure of the symmetric group, and the word Mult. is short for multiplicity. We let $\otimes^r$ denote the operation of taking the r-fold tensor product of a representation of a symmetric group $S_n$ (yielding the sum of various irreducible representations of $S_n$).

\begin{theorem} \label{main3} Let $\beta=\frac{(n-k)(n-k-1)}{(n)(n-1)}$. Then for $n \geq 3, 1 \leq k < n$, \[  \sum_{\lambda
 \atop |\lambda|=n} |\frac{n! [Mult. \ \lambda \ in \ \otimes^r
 Ind_{S_{n-k}}^{S_n} (1)]}{dim(\lambda) \left( (n)\cdots (n-k+1)
 \right)^r}-1|^2 \pi(\lambda) \leq n! \left(\beta \right)^{2r}.\] For
 $r> \frac{n log(n) + c}{2log(\frac{1}{\beta})}$, this is at most
 $\sqrt{2 \pi} e^{-c}$. \end{theorem}

\begin{proof}
 Let $(n)$ be the partition which consists of one row of size $n$, and
 let $n_1(C)$ denote the number of fixed points of a conjugacy class
 $C$. We now consider the quantity $||\frac{J(k)_{(n)}^r}{\pi}-1||_2^2$. One on
 hand, by part 2 of Lemma \ref{classic}, we know that \begin{eqnarray*} & & J(k)_{(n)}^r
 (\lambda)\\ & = & dim(\lambda) \sum_{C} \left( \frac{(n_1(C)) \cdots
 (n_1(C)-k+1)}{n \cdots (n-k+1)} \right) ^r \frac{|C| \chi^{\lambda}(C)}{n!}\\
& = & \frac{dim(\lambda)}{\left( n \cdots (n-k+1) \right) ^r} \frac{1}{n!} \sum_{g \in S_n} \left( n_1(g) \cdots
 (n_1(g)-k+1) \right)^r \chi^{\lambda}(g). \end{eqnarray*} By Lemmas \ref{mult} and \ref{induced}, and the
 fact that the character of a tensor product is the product of the
 characters, this is precisely \[ \frac{dim(\lambda)}{\left( n(n-1) \cdots
 (n-k+1) \right) ^r} [Mult. \ \lambda \ in \ \otimes^r
 Ind_{S_{n-k}}^{S_n} (1)].\] Thus \[ ||\frac{J(k)_{(n)}^r}{\pi}-1||_2^2 = 
 \sum_{\lambda \atop |\lambda|=n} |\frac{ n! [Mult. \ 
 \lambda \ in \ \otimes^r Ind_{S_{n-k}}^{S_n} (1)]}{dim(\lambda) \left((n)\cdots(
 n-k+1) \right)^r}-1|^2 \pi(\lambda).\] The result now follows
 by the upper bound on $||\frac{J(k)_{(n)}^r}{\pi}-1||_2^2$ in Theorem \ref{main2}. \end{proof}
