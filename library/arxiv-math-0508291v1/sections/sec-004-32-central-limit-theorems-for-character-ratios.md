---
doc_id: arxiv-math-0508291v1
doc_title: "Stein’s Method and Random Character Ratios Running head: Stein’s Method and Random Character Ratios Version of 8/13/05"
section_id: sec-004-32-central-limit-theorems-for-character-ratios
section_title: "Central limit theorems for character ratios"
section_number: 3.2
pages: 9-14
source_pdf: 0508291v1.pdf
source_sha256: d2d541426aaec742
toc_source: outline
text_source: latex
latex_prose_ratio: 0.955
latex_coverage_ratio: 0.988
doc_brief: "Stein’s Method and Random Character Ratios Running head: Stein’s Method and Random Character Ratios Version of 8/13/05 — Stein’s method is used to prove limit theorems for random character ratios."
---
\label{groupCLT}
	
	The goal of this subsection is to prove a central limit
	theorem for the random variable $W$ defined by $W(\lambda) =
	\frac{|C|^{1/2} \chi^{\lambda}(C)}{dim(\lambda)}$, where $C$
	is a fixed conjugacy class such that $C=C^{-1}$ and $\lambda$
	is random from the Plancherel measure of $G$.

	For this purpose, it is useful to construct a Markov chain on
	the set of irreducible representations of $G$ as
	follows. First, fix a non-trivial irreducible representation
	$\tau$ whose character is real valued. This gives a Markov chain
	$L_{\tau}$ by defining the probability of transitioning from
	$\lambda$ to $\rho$ as \[ L_{\tau}(\rho,\lambda) :=
	\frac{dim(\rho)}{dim(\lambda) dim(\tau)} \frac{1}{|G|}
	\sum_{g} \chi^{\lambda}(g) \chi^{\tau}(g)
	\overline{\chi^{\rho}(g)}. \] It is worth remarking that since
	Stein's method is in the spirit of Taylor approximation,
	$\tau$ should typically be chosen to be as close as possible
	to the trivial representation.

	Lemma \ref{gchain} verifies that $L_{\tau}$ is a Markov chain
which is reversible with respect to Plancherel measure.

\begin{lemma} \label{gchain} The transition probabilities of $L_{\tau}$ are real and non-negative and sum to 1. Moreover the chain $L_{\tau}$ is reversible with respect to the Plancherel measure of $G$.
\end{lemma}

\begin{proof} The transition probabilities of $L_{\tau}$ are real and non-negative since \[  \frac{1}{|G|} \sum_{g} \chi^{\lambda}(g) \chi^{\tau}(g)
	\overline{\chi^{\rho}(g)} \] is the multiplicity of $\rho$ in
	the tensor product of $\lambda$ and $\tau$. Letting $id$
	denote the identity, it follows from Lemma \ref{orth1} that \[
	\sum_{\rho} L_{\tau}(\lambda,\rho) = \frac{1}{dim(\lambda)
	dim(\tau) |G|} \sum_g \chi^{\lambda}(g) \chi^{\tau}(g)
	\sum_{\rho} \chi^{\rho}(id) \overline{\chi^{\rho}(g)} = 1.\]
	For the reversibility assertion, the fact that $\chi^{\tau}$
	and the transition probabilities of $L_{\tau}$ are both real
	valued implies that \[ \frac{dim(\lambda)^2}{|G|}
	L_{\tau}(\lambda,\rho) = \frac{dim(\rho)^2}{|G|}
	L_{\tau}(\rho,\lambda). \] \end{proof}

	An exchangeable pair $(W,W')$ is now constructed from the
	chain $L_{\tau}$ in the standard way. First choose $\lambda$
	from the Plancherel measure of $G$, then choose $\rho$ with
	probability $L_{\tau}(\lambda,\rho)$, and finally let $(W,W')
	= (W(\lambda),W(\rho))$. The remaining results in this
	subsection show that the exchangeable pair $(W,W')$ has
	desirable properties.

\begin{lemma} \label{steinsat} $\ee(W'|W) = \left(  \frac{\chi^{\tau}(C)}{dim(\tau)} \right) W$. \end{lemma} 

\begin{proof} From the definition of $W'$,
\begin{eqnarray*}
\ee(W'|\lambda) & = & |C|^{1/2} \sum_{\rho} \frac{dim(\rho)}{dim(\lambda) dim(\tau)} \frac{1}{|G|} \sum_g \chi^{\lambda}(g) \chi^{\tau}(g) \overline{\chi^{\rho}(g)} \frac{\chi^{\rho}(C)}{dim(\rho)}\\
& = & \frac{|C|^{1/2}}{|G|} \sum_{g} \frac{\chi^{\lambda}(g)}{dim(\lambda)} \frac{\chi^{\tau}(g)}{dim(\tau)} \sum_{\rho} \chi^{\rho}(C) \overline{\chi^{\rho}(g)}\\
& = &  \left(  \frac{\chi^{\tau}(C)}{dim(\tau)} \right) W(\lambda), \end{eqnarray*} where the last step is Lemma \ref{orth1}. The result follows since this depends on $\lambda$ only through $W$. \end{proof}

	Corollary \ref{record} is not needed in what follows, but is
	worth recording.

\begin{cor}
 \label{record} The eigenvalues of $L_{\tau}$ are
 $\frac{\chi^{\tau}(C)}{dim(\tau)}$ as $C$ ranges over conjugacy
 classes of $G$. The functions $\psi_C(\lambda) = \frac{|C|^{1/2}
 \chi^{\lambda}(C)}{dim(\lambda)}$ are a basis of eigenvectors of
 $L_{\tau}$, orthonormal with respect to the inner product \[ \langle
 f_1,f_2 \rangle = \sum_{\lambda} f_1(\lambda) \overline{f_2(\lambda)}
 \frac{dim(\lambda)^2}{|G|}.\]
\end{cor}

\begin{proof} The proof of Lemma \ref{steinsat} shows that $\psi_C$ is an eigenvector of $L_{\tau}$ with eigenvalue $\frac{\chi^{\tau}(C)}{dim(\tau)}$. The orthonormality assertion follows from Lemma \ref{orth1}, and the basis assertion follows since the number of conjugacy classes of $G$ is equal to the number of irreducible representations of $G$. \end{proof} 

\begin{lemma} \label{immcor} $\ee(W'-W)^2 = 2 \left(1 - \frac{\chi^{\tau}(C)}{dim(\tau)} \right)$. \end{lemma}

\begin{proof} This is immediate from Lemma \ref{var} and \ref{steinsat}. \end{proof}

	For the remainder of this subsection, if $K$ is a conjugacy
	class of $G$, $p_m(K)$ will denote the probability that the
	random walk generated by $C$ is in $K$ after $m$ steps.

\begin{lemma} \label{pre2} \[ \ee((W')^2|\lambda) = \frac{|C|}{dim(\lambda) dim(\tau)} \sum_K p_2(K) \chi^{\lambda}(K) \chi^{\tau}(K) \] where the sum is over all conjugacy classes $K$ of $G$.     
\end{lemma}

\begin{proof} \begin{eqnarray*} & & \ee((W')^2|\lambda)\\ & = & \frac{1}{ dim(\lambda) dim(\tau) |G|} \sum_{\rho} dim(\rho) \sum_g \chi^{\lambda}(g) \chi^{\tau}(g) \overline{\chi^{\rho}(g)} \left(\frac{|C|^{1/2} \chi^{\rho}(C)}{dim(\rho)} \right)^2 \\
& = & \frac{|C|}{ dim(\lambda) dim(\tau) |G|} \sum_g \chi^{\lambda}(g)
\chi^{\tau}(g) \sum_{\rho} dim(\rho) \overline{\chi^{\rho}(g)} \left(
\frac{\chi^{\rho}(C)}{dim(\rho)} \right)^2. \end{eqnarray*} The result
now follows from Lemma \ref{countsol}. \end{proof}

	Lemma \ref{big1} writes $Var([\ee(W'-W)^2|\lambda])$ as a sum
	of positive quantities.

\begin{lemma} \label{big1} \[
 Var([\ee(W'-W)^2|\lambda]) = |C|^2 \sum_{ K \neq id}
 \frac{p_2(K)^2}{|K|} \left( \frac{\chi^{\tau}(K)}{dim(\tau)} + 1 -
 \frac{2 \chi^{\tau}(C)}{dim(\tau)} \right)^2  , \] where $K$
 ranges over all non-identity conjugacy classes of $G$. \end{lemma}

\begin{proof} By Lemmas \ref{pre2}, \ref{immcor}, and \ref{steinsat}, \begin{eqnarray*} & & Var([\ee(W'-W)^2|\lambda])\\ & = & \ee \left( \ee((W'-W)^2|\lambda)^2 \right) - 4 \left( 1 - \frac{\chi^{\tau}(C)}{dim(\tau)} \right)^2\\
& = & |C|^2 \ee \left[ \frac{ \sum_K p_2(K)
\chi^{\lambda}(K) \chi^{\tau}(K)   }{dim(\lambda) dim(\tau)}
 + \left(1 - \frac{2 \chi^{\tau}(C)}{dim(\tau)} \right) \left(\frac{\chi^{\lambda}(C)}{dim(\lambda)} \right)^2 \right]^2\\
& &  - 4  \left( 1 - \frac{\chi^{\tau}(C)}{dim(\tau)} \right)^2 \\ & = & T_1 + T_2 + T_3 - 4  \left( 1 - \frac{\chi^{\tau}(C)}{dim(\tau)} \right)^2 \end{eqnarray*} where
\[ T_1 = \frac{|C|^2}{ dim(\tau)^2} \ee \left( \sum_K \frac{p_2(K) \chi^{\lambda}(K) \chi^{\tau}(K)}{dim(\lambda)} \right)^2 \]

\[ T_2 = \frac{2 |C|^2}{ dim(\tau)}
 \left(1-\frac{2 \chi^{\tau}(C)}{dim(\tau)} \right) \sum_K p_2(K)
 \chi^{\tau}(K) \ee \left[ \frac{\chi^{\lambda}(K)}{dim(\lambda)}
\left( \frac{\chi^{\lambda}(C)}{dim(\lambda)} \right)^2 \right] .\]

\[ T_3 =  |C|^2 \left( 1-\frac{2 \chi^{\tau}(C)}{dim(\tau)} \right)^2 \ee \left( \frac{\chi^{\lambda}(C)}{dim(\lambda)} \right)^4 .\]

	Fortunately, these terms can be simplified. By Lemma
	\ref{pre2}, the expression inside parentheses in $T_1$ is
	real. Since $\chi^{\tau}$ is real valued, Lemma \ref{orth1}
	implies that \[ T_1 = |C|^2 \sum_K \frac{p_2(K)^2}{|K|}
	\frac{\chi^{\tau}(K)^2}{dim(\tau)^2}.\] Since
	$\chi^{\lambda}(C)$ is real, Lemma \ref{countsol} implies that
	\[ T_2 = 2 |C|^2 \left( 1-\frac{2 \chi^{\tau}(C)}{dim(\tau)}
	\right) \sum_K \frac{p_2(K)^2}{|K|} \frac{\chi^{\tau}(K)}
	{dim(\tau)} \] and since $C=C^{-1}$, \begin{eqnarray*} T_3 & =
	&  |C|^2 \left( 1-\frac{2 \chi^{\tau}(C)}{dim(\tau)} \right)^2 p_4(id)\\ & =
	&  |C|^2 \left( 1-\frac{2 \chi^{\tau}(C)}{dim(\tau)} \right)^2 \sum_K
	\frac{p_2(K)^2}{|K|}. \end{eqnarray*} Thus one can write \[
	T_1+T_2+T_3 = |C|^2 \sum_K \frac{p_2(K)^2}{|K|} \left(
	\frac{\chi^{\tau}(K)}{dim(\tau)} + 1 - 
	\frac{2 \chi^{\tau}(C)}{dim(\tau)} \right)^2 \] and the result
	follows since $p_2(id) = \frac{1}{|K|}$. \end{proof}

\begin{lemma} \label{mom1} Let $k$ be a positive integer.
\begin{enumerate}
\item $\ee(W'-W)^k= |C|^{k/2} \sum_{m=0}^k  (-1)^{k-m} {k \choose m} \sum_K \frac{\chi^{\tau}(K)}{dim(\tau)} \frac{p_m(K) p_{k-m}(K)}{|K|}$.
\item $\ee(W'-W)^4$ is equal to \[ |C|^2 
\sum_K \left[  8 \left(1 - \frac{\chi^{\tau}(C)}{dim(\tau)} \right) - 6 \left( 1-\frac{\chi^{\tau}(K)}{dim(\tau)} \right) \right] \frac{p_2(K)^2}{|K|}.\]
\end{enumerate}
\end{lemma}  

\begin{proof} For the first assertion, note that
\begin{eqnarray*}  \ee((W'-W)^k|\lambda)
 & = & \frac{|C|^{k/2}}{dim(\lambda) dim(\tau)}
\sum_{\rho} \frac{dim(\rho)}{|G|}
\sum_g \chi^{\lambda}(g) \chi^{\tau}(g) \overline{\chi^{\rho}(g)}\\ & & \cdot \sum_{m=0}^k
(-1)^{k-m} {k \choose m} \left(\frac{\chi^{\rho}(C)}{dim(\rho)}
\right)^m \left( \frac{\chi^{\lambda}(C)}{dim(\lambda)} \right)^{k-m}
\\ & = & \frac{|C|^{k/2}}{dim(\lambda) dim(\tau)} \sum_{m=0}^k
(-1)^{k-m} {k \choose m} \left( \frac{\chi^{\lambda}(C)}{dim(\lambda)}
\right)^{k-m}\\ & & \cdot \sum_g \chi^{\tau}(g) \chi^{\lambda}(g)
\sum_{\rho} \frac{dim(\rho)}{|G|} \left( \frac{\chi^{\rho}(C)}{dim(\rho)}
\right)^m \overline{\chi^{\rho}(g)} \\
& = & \frac{|C|^{k/2}}{dim(\lambda) dim(\tau)}
\sum_{m=0}^k (-1)^{k-m} {k \choose m} \left(
\frac{\chi^{\lambda}(C)}{dim(\lambda)} \right)^{k-m}\\ & & \cdot \sum_K \chi^{\
\tau}(K) \chi^{\lambda}(K) p_m(K), \end{eqnarray*} where the final equality is by Lemma \ref{countsol}. Thus $ \ee((W'-W)^k)$ is equal to   \begin{eqnarray*}
 &  & \ee(\ee((W'-W)^k|\lambda))\\
& = &  \frac{|C|^{k/2}}{dim(\tau)}
\sum_{m=0}^k (-1)^{k-m} {k \choose m} \\ & & 
\cdot \sum_K p_m(K) \chi^{\tau}(K) \sum_{\lambda} \frac{dim(\lambda)^2}{|G|} \frac{\chi^{\lambda}(K)}{dim(\lambda)} \left( \frac{\chi^{\lambda}(C)}{dim(\lambda)} \right)^{k-m}. \end{eqnarray*} The first assertion now follows from Lemma \ref{countsol} and the fact that $\chi^{\lambda}(C)$ is real for all $\lambda$.

	For the second assertion, note by the first assertion that \[
	\ee(W'-W)^4 = |C|^2 \sum_{m=0}^4 (-1)^{m} {4 \choose m} \sum_K
	\frac{\chi^{\tau}(K)}{dim(\tau)} \frac{p_m(K) p_{4-m}(K)}{|K|}
	.\] If $\tau$ is the trivial representation, then $W'=W$,
	which implies that \[ 0 = |C|^2 \sum_{m=0}^4 (-1)^{m} {4
	\choose m} \sum_K \frac{p_m(K) p_{4-m}(K)}{|K|}. \] Thus for
	general $\tau$, \[ \ee(W'-W)^4 = - |C|^2 \sum_{m=0}^4 (-1)^{m}
	{4 \choose m} \sum_K \left( 1 -
	\frac{\chi^{\tau}(K)}{dim(\tau)} \right) \frac{p_m(K)
	p_{4-m}(K)}{|K|}.\] Observe that the $m=0,4$ terms in this sum
	vanish, since the only contribution could come from the
	identity, which contributes 0. The $m=2$ term is \[ -6 |C|^2
	\sum_K \left( 1-\frac{\chi^{\tau}(K)}{dim(\tau)} \right)
	\frac{p_2(K)^2}{|K|} .\] The $m=1,3$ terms are equal and
	together contribute \begin{eqnarray*} & & 8 |C|^2 \sum_K \left(
	1-\frac{\chi^{\tau}(K)}{dim(\tau)} \right) \frac{p_1(K)
	p_3(K)}{|K|}\\ & = & 8 |C| \left(1 -
	\frac{\chi^{\tau}(C)}{dim(\tau)} \right) p_3(C)\\ & = & 8
	|C|^2 \left(1 - \frac{\chi^{\tau}(C)}{dim(\tau)} \right)
	p_4(id)\\ & = & 8 |C|^2 \left(1 -
	\frac{\chi^{\tau}(C)}{dim(\tau)} \right) \sum_K
	\frac{p_2(K)^2}{|K|}, \end{eqnarray*} where $id$ is the
	identity and the last two equalities can be seen either
	directly or from Lemma \ref{countsol}. This completes the
	proof of the second assertion. \end{proof}

	Putting the pieces together, one obtains the following theorem.

\begin{theorem} \label{main1} Let
 $C$ be a conjugacy class of a finite group $G$ such that $C=C^{-1}$
 and fix a nontrivial irreducible representation $\tau$ of $G$ whose character
 is real valued. Let $\lambda$ be a random irreducible representation,
 chosen from the Plancherel measure of $G$. Let $W=\frac{|C|^{1/2}
 \chi^{\lambda}(C)}{dim(\lambda)}$. Then for all real $x_0$,
 \begin{eqnarray*} && \left| \pp(W \leq x_0) - \frac{1}{\sqrt{2 \pi}}
 \int_{-\infty}^{x_0} e^{-\frac{x^2}{2}} dx \right|\\ & \leq &
 \frac{|C|}{a} \sqrt{\sum_{ K \neq id} \frac{p_2(K)^2}{|K|} \left(
 \frac{\chi^{\tau}(K)}{dim(\tau)} + 2a -1 \right)^2}\\ & & +
  \left[ \frac{|C|^2}{\pi} \sum_K \left(8 - \frac{6}{a} \left(
 1-\frac{\chi^{\tau}(K)}{dim(\tau)} \right) \right)
 \frac{p_2(K)^2}{|K|} \right]^{1/4} , \end{eqnarray*} where
 $a=1-\frac{\chi^{\tau}(C)}{dim(\tau)}$. \end{theorem}

\begin{proof}
 One applies Theorem \ref{steinbound} to the exchangeable pair
 $(W,W')$ of this subsection. By Lemmas \ref{majorize} and \ref{big1},
 the first term in Theorem \ref{steinbound} gives the first term in
 the theorem. To upper bound the second term in Theorem
 \ref{steinbound}, note by the Cauchy-Schwarz inequality that \[
 \ee|W'-W|^3 \leq \sqrt{ \ee(W'-W)^2 \ee(W'-W)^4}.\] Now use Lemma
 \ref{immcor} and part 2 of Lemma \ref{mom1}. \end{proof}
