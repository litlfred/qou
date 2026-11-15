---
doc_id: arxiv-math-0508291v1
doc_title: "Stein’s Method and Random Character Ratios Running head: Stein’s Method and Random Character Ratios Version of 8/13/05"
section_id: sec-013-52-markov-chains-on-strict-partitions
section_title: "Markov chains on strict partitions"
section_number: 5.2
pages: 32-34
source_pdf: 0508291v1.pdf
source_sha256: d2d541426aaec742
toc_source: outline
text_source: latex
latex_prose_ratio: 0.939
latex_coverage_ratio: 1.0
doc_brief: "Stein’s Method and Random Character Ratios Running head: Stein’s Method and Random Character Ratios Version of 8/13/05 — Stein’s method is used to prove limit theorems for random character ratios."
---
\label{exchange}

	This subsection discusses a Markov chain on $DP(n)$ to be used
	in defining an exchangeable pair for the proof of Theorem
	\ref{projerror}. 

	Motivated by constructions in the group and Gelfand pair
	cases, it would be natural, for $\tau$ a fixed element of
	$DP(n)$, to define a ``Markov chain'' $J_{\tau}$ on $DP(n)$
	with transition ``probabilities'' \[ J_{\tau}(\lambda,\rho) :=
	\frac{g_{\rho}}{2^{l(\rho)} g_{\lambda} g_{\tau}} \sum_{\nu
	\in OP(n)} \frac{2^{l(\nu)} X^{\lambda}_{\nu} X^{\rho}_{\nu}
	X^{\tau}_{\nu}}{z_{\nu}} .\] Using Lemma \ref{torthog2}, one
	can see that $\sum_{\rho} J_{\tau}(\lambda,\rho) = 1$ for all
	$\lambda$, and that $J_{\tau}$ satisfies the reversibility
	condition \[ \frac{2^{n-l(\lambda)} g_{\lambda}^2}{n!} J_{\tau}(\lambda,\rho) = \frac{2^{n-l(\rho)} g_{\rho}^2}{n!}
	J_{\tau}(\rho,\lambda) \] for all $\lambda,\rho \in
	DP(n)$. Unfortunately, the quantity $J_{\tau}(\lambda,\rho)$
	can be negative. For instance one can check from Lemma
	\ref{valtwist} that $J_{(2,1)}((2,1),(2,1))=-1$.

	To deal with the complication raised in the previous
	paragraph, it is helpful to introduce a genuine Markov chain
	$L$ on $DP(n)$, with transition probabilities \[ L(\lambda,
	\rho) = \frac{2g_{\rho}}{n g_{\lambda}} \sum_{\eta \in DP(n-1)
	\atop \eta \nearrow \lambda, \eta \nearrow \rho} 2^{l(\eta)-l(\rho)}.\] Here
	$\eta \nearrow \lambda$ means that $\eta$ is obtained from
	$\lambda$ by decreasing the size of some part by exactly one.

	Lemma \ref{ischain} proves that $L$ is a Markov chain which is
	reversible with respect to shifted Plancherel measure. As is
	mentioned in the proof, the definition of $L$ was motivated by
	the theory of harmonic functions on Bratteli diagrams.

\begin{lemma} \label{ischain} The transition
 probabilities of $L$ are real and non-negative and sum to 1. Moreover
 the chain $L$ is reversible with respect to shifted Plancherel
 measure.
\end{lemma}

\begin{proof}
 This is a special case of a construction in Section 2 of
 \cite{F1}. To see this, one takes the underlying Bratteli diagram to
 be the Schur graph, the properties of which are discussed in Section 5 of
 \cite{BO2}. The vertices of the Schur graph are all partitions of all
 non-negative integers with distinct parts, and the edge multiplicity
 between $\eta \in DP(n-1)$ and $\lambda \in DP(n)$ is 1 if $\eta
 \nearrow \lambda$, and is 0 otherwise. The combinatorial dimension of
 a shape $\lambda$ is $g_{\lambda}$, and if $\pi$ denotes shifted
 Plancherel measure, the function $\frac{\pi(\lambda)}{g_{\lambda}}$
 is harmonic on the Schur graph. \end{proof}

	Proposition \ref{2chains} will establish a fundamental
	relation between the Markov chain $L$ and the ``Markov chain''
	$J_{(n-1,1)}$. The argument involves symmetric function
	theory, and first a lemma is needed about properties of a
	certain subring $\Gamma$ of the ring of symmetric functions,
	defined on page 252 of \cite{Mac}.

	Recall from page 255 of \cite{Mac} that there is an inner
	product on $\Gamma$ which satisfies the properties \begin{enumerate} \item $\langle p_{\lambda},p_{\mu} \rangle = 2^{-l(\lambda)} z_{\lambda}
	\delta_{\lambda,\mu}$ if $\lambda,\mu \in OP(n)$.
\item $\langle P_{\lambda},P_{\mu} \rangle= 2^{-l(\lambda)}
\delta_{\lambda,\mu}$ if $\lambda,\mu \in DP(n)$. \end{enumerate} Here
$p_{\lambda}$ is a power sum symmetric function and $P_{\lambda}$ is a
Hall-Littlewood polynomial with the parameter $t=-1$. It is also
helpful to recall, from page 247 of \cite{Mac}, that for $\lambda
\in DP(n)$, \[ P_{\lambda} = 2^{-l(\lambda)} \sum_{\nu \in OP(n)}
\frac{2^{l(\nu)}}{z_{\nu}} X^{\lambda}_{\nu} p_{\nu}.\]

\begin{lemma} \label{symlem} Let $p_1^{\perp}$ be the adjoint in $\Gamma$ of multiplication by $p_1$.
\begin{enumerate}
\item (\cite{Mac}, page 265) $p_1^{\perp} = \frac{1}{2}
\frac{\partial}{\partial p_1}$.
\item $p_1^{\perp} P_{\lambda} = \sum_{\eta \in DP(n-1) \atop \eta
\nearrow \lambda} 2^{l(\eta)-l(\lambda)} P_{\eta}$.
\end{enumerate}
\end{lemma}

\begin{proof} Only
 the second assertion needs to be proved. Consider the coefficient of
 $P_{\eta}$ in $p_1^{\perp} P_{\lambda}$.  It is \[ \frac{ \langle p_1^{\perp}
 P_{\lambda}, P_{\eta} \rangle}{\langle P_{\eta},P_{\eta} \rangle} = \frac{\langle  P_{\lambda},
 p_1 P_{\eta} \rangle}{\langle P_{\eta},P_{\eta} \rangle} = 2^{l(\eta)} \langle P_{\lambda}, p_1
 P_{\eta} \rangle.\] From Section 3.8 of \cite{Mac}, \[ p_1 P_{\eta} =
 \sum_{\lambda \in DP(n) \atop \eta \nearrow \lambda} P_{\lambda},\]
 which implies the result. \end{proof}

	Proposition \ref{2chains} can now be proved.

\begin{prop} \label{2chains} Suppose that $n \geq 3$, so that $(n-1,1)$ is a strict partition. Then \[ L(\lambda,\rho) = \frac{n-2}{n} J_{(n-1,1)}(\lambda,\rho)\] for $\lambda,\rho \in DP(n)$ such that $\lambda \neq \rho$. 
\end{prop}

\begin{proof} By Lemma \ref{valtwist}, \[ J_{(n-1,1)}(\lambda,\rho) = 	\frac{g_{\rho}}{2^{l(\rho)} g_{\lambda} (n-2)} \sum_{\nu
	\in OP(n)} \frac{2^{l(\nu)} X^{\lambda}_{\nu} X^{\rho}_{\nu}
	(m_1(\nu)-2)}{z_{\nu}}.\] Since $\lambda \neq \rho$, Lemma
	\ref{torthog1} and part 1 of Lemma \ref{symlem} imply that
	this is equal to \begin{eqnarray*} & &
	\frac{g_{\rho}}{2^{l(\rho)} g_{\lambda} (n-2)} \sum_{\nu \in
	OP(n)} \frac{2^{l(\nu)} X^{\lambda}_{\nu} X^{\rho}_{\nu}
	m_1(\nu)}{z_{\nu}}\\ & = & \frac{g_{\rho}}{2^{l(\rho)}
	g_{\lambda} (n-2)} \left \langle \sum_{\nu \in OP(n)} m_1(\nu)
	\frac{2^{l(\nu)}}{z_{\nu}} X^{\lambda}_{\nu} p_{\nu},
	\sum_{\nu \in OP(n)} \frac{2^{l(\nu)}}{z_{\nu}} X^{\rho}_{\nu}
	p_{\nu} \right \rangle\\ & = & \frac{2^{l(\lambda)}
	g_{\rho}}{g_{\lambda} (n-2)} \langle 2 p_1 p_1^{\perp}
	P_{\lambda},P_{\rho} \rangle\\ & = & \frac{2^{l(\lambda)+1}
	g_{\rho}}{g_{\lambda} (n-2)} \langle p_1^{\perp} P_{\lambda},
	p_1^{\perp} P_{\rho} \rangle. \end{eqnarray*}

	By part 2 of Lemma \ref{symlem}, this is \begin{eqnarray*} & &
	\frac{2^{l(\lambda)+1} g_{\rho}}{g_{\lambda} (n-2)} \left
	\langle \sum_{\eta \in DP(n-1) \atop \eta \nearrow \lambda}
	2^{l(\eta)-l(\lambda)} P_{\eta} , \sum_{\eta \in DP(n-1) \atop
	\eta \nearrow \rho} 2^{l(\eta)-l(\rho)} P_{\eta} \right
	\rangle \\ & = & \frac{2g_{\rho}}{g_{\lambda} (n-2)}
	\sum_{\eta \in DP(n-1) \atop \eta \nearrow \lambda, \eta
	\nearrow \rho} 2^{l(\eta)-l(\rho)} \\ & = & \frac{n}{n-2}
	L(\lambda,\rho). \end{eqnarray*}
\end{proof}
