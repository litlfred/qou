---
doc_id: arxiv-math-0508291v1
doc_title: "Stein’s Method and Random Character Ratios Running head: Stein’s Method and Random Character Ratios Version of 8/13/05"
section_id: sec-014-53-central-limit-theorem-for-shifted-plancherel
section_title: "Central limit theorem for shifted Plancherel measure"
section_number: 5.3
pages: 34-42
source_pdf: 0508291v1.pdf
source_sha256: d2d541426aaec742
toc_source: outline
text_source: latex
latex_prose_ratio: 0.911
latex_coverage_ratio: 0.904
doc_brief: "Stein’s Method and Random Character Ratios Running head: Stein’s Method and Random Character Ratios Version of 8/13/05 — Stein’s method is used to prove limit theorems for random character ratios."
---
\label{twCLT}

	This subsection studies the statistic $W=\sqrt{
	\frac{n!}{z_{\mu} 2^{n-l(\mu)}}}
	\frac{X^{\lambda}_{\mu}}{g_{\lambda}}$, where $\mu \in OP(n)$
	is fixed and $\lambda \in DP(n)$ is chosen from shifted
	Plancherel measure. The main goal is a proof of Theorem
	\ref{projerror}.

	Using $L$, one constructs an exchangeable pair $(W,W')$ as
	follows. Choose $\lambda$ from the shifted Plancherel measure on
	partitions of size $n$. Then choose $\rho$ with probability
	$L(\lambda,\rho)$ and let $(W,W')=(W(\lambda),W(\rho))$. Using
	$J_{\tau}$, one constructs an ``exchangeable pair'' $(W,W^*)$
	as follows. Choose $\lambda$ from the shifted Plancherel measure
	on partitions of size $n$. Then choose $\rho$ with ``probability''
	$J_{\tau}(\lambda,\rho)$ and let
	$(W,W^*)=(W(\lambda),W(\rho))$. The pair $(W,W')$ is a valid
	candidate for Stein's method, but the pair $(W,W^*)$ is much
	easier to work with, and by Proposition \ref{2chains}, when
	$\tau=(n-1,1)$, this gives insight into the genuine
	exchangeable pair $(W,W')$. Even though the transition
	probabilities of $J_{\tau}$ can be negative, for convenience
	the usual language of probability theory (expected value,
	variance, etc.) will be used when working with them.

\begin{lemma} \label{tsteinsat2}
\begin{enumerate}
\item $\ee(W^*|W) = \left( \frac{X^{\tau}_{\mu}}{g_{\tau}} \right)W$.
\item $\ee(W'|W) = \frac{m_1(\mu)}{n} W$.
\end{enumerate}
\end{lemma}

\begin{proof} For the first assertion, the definition of $J_{(n-1,1)}$ and Lemma \ref{torthog2} imply
that \begin{eqnarray*} \ee(W^*|\lambda) & = & \sqrt{\frac{n!}{z_{\mu}
2^{n-l(\mu)}}} \sum_{\rho \in DP(n)} \frac{g_{\rho}}{2^{l(\rho)}
g_{\lambda} g_{\tau}} \sum_{\nu \in OP(n)} \frac{2^{l(\nu)}
X^{\lambda}_{\nu} X^{\rho}_{\nu} X^{\tau}_{\nu}}{z_{\nu}}
\frac{X^{\rho}_{\mu}}{g_{\rho}}\\ & = & \sqrt{\frac{n!}{z_{\mu}
2^{n-l(\mu)}}} \frac{1}{g_{\lambda} g_{\tau}} \sum_{\nu \in OP(n)}
\frac{2^{l(\nu)} X^{\lambda}_{\nu} X^{\tau}_{\nu}}{z_{\nu}} \sum_{\rho
\in DP(n)} \frac{ X^{\rho}_{\nu} X^{\rho}_{\mu} }{2^{l(\rho)}} \\ & =
& \sqrt{\frac{n!}{z_{\mu} 2^{n-l(\mu)}}} \frac{X^{\lambda}_{\mu}}{g_{\lambda}}
\frac{X^{\tau}_{\mu}}{g_{\tau}}\\ & = & \left( \frac{X^{\tau}_{\mu}}{g_{\tau}}
\right) W(\lambda). \end{eqnarray*} The first assertion follows since this depends on $\lambda$ only through $W$.

	For the second assertion, observe that by Proposition
\ref{2chains}, \begin{eqnarray*} \ee(W'-W|\lambda) & = & \sum_{\rho} L(\lambda,\rho) \left(W(\rho)-W(\lambda) \right)\\ & = &
\frac{n-2}{n} \sum_{\rho} J_{(n-1,1)}(\lambda,\rho)
\left( W(\rho) - W(\lambda) \right)\\ & = & - \left( \frac{n-2}{n}
\right) W(\lambda) + \frac{n-2}{n} \sum_{\rho} J_{(n-1,1)}(\lambda,\rho)
W(\rho). \end{eqnarray*} By the first assertion and Lemma
\ref{valtwist}, this is \[ -\left(\frac{n-2}{n} \right) W(\lambda) +
\frac{n-2}{n} \frac{m_1(\mu)-2}{n-2} W(\lambda) = \left( \frac{m_1(\mu)}{n} -1
\right) W(\lambda), \] which implies the result.  \end{proof}

	Corollary \ref{diago} will not be needed but is worth recording.

\begin{cor} \label{diago} The eigenvalues of $J_{\tau}$ are $\frac{X^{\tau}_{\mu}}{g_{\tau}}$ as $\mu$ ranges over $OP(n)$. The functions $\psi_{\mu}(\lambda) = \sqrt{\frac{n!}{z_{\mu} 2^{n-l(\mu)}}} \frac{X^{\lambda}_{\mu}}{g_{\lambda}}$ are a basis of eigenvectors of $J_{\tau}$, orthonormal with respect to the inner product \[ \langle f_1,f_2 \rangle = \sum_{\lambda \in DP(n)} f_1(\lambda) \overline{f_2(\lambda)} \frac{2^{n-l(\lambda)} g_{\lambda}^2}{n!}.\]
\end{cor}

\begin{proof} The proof of part 1 of Lemma \ref{tsteinsat2} shows that $\psi_{\mu}$ is an eigenvector of $J_{\tau}$ with eigenvalue $\frac{X^{\tau}_{\mu}}{g_{\tau}}$. The orthonormality assertion follows from Lemma \ref{torthog2} and the fact from \cite{Mac} that all $X^{\lambda}_{\mu}$ are real valued. The basis assertion follows since $|DP(n)|=|OP(n)|$. \end{proof}

\begin{lemma} \label{timmcor2} $\ee(W^*-W)^2 = 2 \left(1- \frac{X^{\tau}_{\mu}}{g_{\tau}} \right)$. \end{lemma}

\begin{proof} This follows from the proof of Lemma \ref{var} (which does not require non-negative transition probabilities) and part 1 of Lemma \ref{tsteinsat2}. 
\end{proof}

	For the remainder of this subsection, $p_m(\tilde{K}_{\nu})$
	will denote the coefficient of $\tilde{K}_{\nu}$ in
	$(\tilde{K}_{\mu})^m$. When $m=0$ this is to be interpreted
	through Lemma \ref{tcountsol}, so that
	$p_0(\tilde{K}_{(1^n)})=1$ and $p_0(\tilde{K}_{\nu}) = 0$ for
	$\nu \neq (1^n)$. Due to the signs in the definition of
	$\tilde{K}_{\nu}$, these numbers are not probabilities so care
	must be taken in working with them. For instance it is not
	true that $\sum_{\nu \in OP(n)} p_m(\tilde{K}_{\nu})
	=1$. However the following three relations will be useful.

\begin{lemma} \label{sumneq1} $\sum_{\nu \in OP(n)}  p_2(\tilde{K}_{\nu}) 2^{l(\nu)-n} = 2^{2[l(\mu)-n]}$. \end{lemma}

\begin{proof} Using Lemma \ref{tcountsol},
 one has that, \[ \sum_{\nu \in OP(n)} p_2(\tilde{K}_{\nu})
 2^{l(\nu)} = 2^{2l(\mu)-n} \sum_{\rho \in DP(n)} 2^{-l(\rho)}
 \frac{(X^{\rho}_{\mu})^2}{g_{\rho}} \sum_{\nu \in OP(n)}
 \frac{2^{l(\nu)}}{z_{\nu}} X^{\rho}_{\nu} .\] By page 248 of
 \cite{Mac}, $X^{n}_{\nu}=1$, so that Lemma \ref{torthog1} implies
 that \[ \sum_{\nu \in OP(n)} \frac{2^{l(\nu)}}{z_{\nu}} X^{\rho}_{\nu}
 X^{n}_{\nu} = 2 \delta_{\rho,n}.\] The result
 follows. \end{proof}


\begin{lemma} \label{4step} $\ee \left( \frac{X^{\lambda}_{\mu}}{g_{\lambda}} \right)^4 = (2^{n-l(\mu)})^4 \sum_{\nu \in OP(n)} p_2(\tilde{K}_{\nu})^2 \frac{2^{l(\nu)} z_{\nu}}{2^n n!}$.
 \end{lemma}

\begin{proof} Consider
 the coefficient of $\tilde{K}_{(1^n)}$ in $(\tilde{K}_{\mu})^4$. On
 one hand, by Lemma \ref{tcountsol} it is equal to $(2^{l(\mu)-n})^4
 \ee \left(\frac{X^{\lambda}_{\mu}}{g_{\lambda}} \right)^4$. On the
 other hand, \[ (\tilde{K}_{\mu})^4 = (\tilde{K}_{\mu})^2
 (\tilde{K}_{\mu})^2 = \left[ \sum_{\nu \in OP(n)} p_2(\tilde{K}_{\nu})
 \tilde{K}_{\nu} \right]^2.\] From Lemmas \ref{tcountsol} and Lemma
 \ref{torthog2}, it follows that the coefficient of
 $\tilde{K}_{(1^n)}$ in $\tilde{K}_{\nu_1} \tilde{K}_{\nu_2}$ is 0 if
 $\nu_1 \neq \nu_2$, and that the coefficient of $\tilde{K}_{(1^n)}$ in
 $(\tilde{K}_{\nu})^2$ is $\frac{2^{l(\nu)-n} z_{\nu}}{n!}$. Thus the
 coefficient of $\tilde{K}_{(1^n)}$ in $(\tilde{K}_{\mu})^4$ is equal
 to \[ \sum_{\nu \in OP(n)} p_2(\tilde{K}_{\nu})^2 \frac{2^{l(\nu)-n}
 z_{\nu}}{n!}.\] Comparing the two expressions for the coefficient of
 $\tilde{K}_{(1^n)}$ in $(\tilde{K}_{\mu})^4$ proves the
 result. \end{proof}

\begin{lemma} \label{3step} $p_3(\tilde{K}_{\mu}) = \frac{2^{n-l(\mu)}} {z_{\mu}} \sum_{\nu \in OP(n)} p_2(\tilde{K}_{\nu})^2 2^{l(\nu)-n} z_{\nu}$.
\end{lemma}

\begin{proof} By Lemma \ref{tcountsol}, \[ p_3(\tilde{K}_{\mu})=\frac{n! (2^{l(\mu)-n})^3}{z_{\mu}} \ee \left( \frac{X^{\lambda}_{\mu}}{g_{\lambda}}
 \right)^4.\] Now use Lemma \ref{4step}. \end{proof}


	The next lemmas are crucial.

\begin{lemma} \label{tpreGP} $\ee((W^*)^2|\lambda) = \frac{n!}{z_{\mu} 2^{l(\mu)} } \sum_{\nu \in OP(n)} \frac{X^{\lambda}_{\nu}}{g_{\lambda}} \frac{X^{\tau}_{\nu}}{g_{\tau}} 2^{l(\nu)} p_2(\tilde{K}_{\nu})$.
\end{lemma}

\begin{proof} It follows from the definitions that $
\ee((W^*)^2|\lambda)$ is equal to
\begin{eqnarray*} &  & \frac{n!}{z_{\mu} 2^{n-l(\mu)}} \sum_{\rho
\in DP(n)} \frac{g_{\rho}}{2^{l(\rho)} g_{\lambda} g_{\tau}} \sum_{\nu
\in OP(n)} \frac{2^{l(\nu)} X^{\lambda}_{\nu} X^{\rho}_{\nu}
X^{\tau}_{\nu}}{z_{\nu}} \left( \frac{X^{\rho}_{\mu}}{g_{\rho}} \right)^2\\ & = &
\frac{n!}{z_{\mu} 2^{n-l(\mu)}} \sum_{\nu \in OP(n)}
\frac{X^{\lambda}_{\nu}}{g_{\lambda}}
\frac{X^{\lambda}_{\tau}}{g_{\tau}} 2^{l(\nu)} \left(
\frac{1}{z_{\nu}} \sum_{\rho \in DP(n)} \frac{g_{\rho}^2}{2^{l(\rho)}}
\frac{X^{\rho}_{\nu}}{g_{\rho}} \left( \frac{X^{\rho}_{\mu}}{g_{\rho}}
\right)^2 \right). \end{eqnarray*} The result now follows from Lemma
\ref{tcountsol}.
\end{proof}

\begin{lemma}
 \label{tbig1GP} \[ Var(\ee[(W^*-W)^2|\lambda]) = \frac{n!
 2^n}{z_{\mu}^2 2^{2 l(\mu)}} \sum_{\nu \in OP(n) \atop \nu \neq
 (1^n)} 2^{l(\nu)} p_2(\tilde{K}_{\nu})^2 z_{\nu} \left(
 \frac{X^{\tau}_{\nu}}{g_{\tau}}+1-\frac{2 X^{\tau}_{\mu}}{g_{\tau}}
 \right)^2\]
\end{lemma}

\begin{proof} By Lemmas \ref{tpreGP}, \ref{timmcor2}, and \ref{tsteinsat2}, $Var(\ee[(W^*-W)^2|\lambda])$ is equal to
\begin{eqnarray*}
 &  & \ee(\ee((W^*-W)^2|\lambda)^2) - 4
\left(1-\frac{X^{\tau}_{\mu}}{g_{\tau}} \right)^2\\ & = & \ee \left[
\frac{n!}{z_{\mu} 2^{l(\mu)}} \sum_{\nu \in OP(n)}
\frac{X^{\lambda}_{\nu}}{g_{\lambda}} \frac{X^{\tau}_{\nu}}{g_{\tau}}
2^{l(\nu)} p_2(\tilde{K}_{\nu}) + \left(1 - \frac{2
X^{\tau}_{\mu}}{g_{\tau}} \right) W^2 \right]^2\\ & & - 4
\left(1-\frac{X^{\tau}_{\mu}}{g_{\tau}} \right)^2\\ & = & T_1 + T_2 +
T_3 - 4 \left(1-\frac{X^{\tau}_{\mu}}{g_{\tau}} \right)^2\\
\end{eqnarray*} where

\[ T_1 = \left( \frac{n!}{z_{\mu} 2^{l(\mu)}} \right)^2 \ee \left( \sum_{\nu \in OP(n)} p_2(\tilde{K}_{\nu}) \frac{X^{\lambda}_{\nu}}{g_{\lambda}} \frac{X^{\tau}_{\nu}}{g_{\tau}} 2^{l(\nu)} \right)^2 \]

\[ T_2 = 2 \left( 1-\frac{2 X^{\tau}_{\mu}}{g_{\tau}} \right) \frac{(n!)^2}{z_{\mu}^2} \sum_{\nu \in OP(n)} \frac{X^{\tau}_{\nu} p_2(\tilde{K}_{\nu})}{g_{\tau} 2^{n-l(\nu)}} \ee \left( \frac{X^{\lambda}_{\nu} (X^{\lambda}_{\mu})^2}{(g_{\lambda})^3} \right) \]

\[ T_3 = \left( 1-\frac{2 X^{\tau}_{\mu}}{g_{\tau}} \right)^2 \left( \frac{n!}{2^{n-l(\mu)} z_{\mu}} \right)^2 \ee \left( \frac{X^{\lambda}_{\mu}}{g_{\lambda}} \right)^4. \]

	These expressions for $T_1,T_2,T_3$ can be simplified. Lemma
	\ref{torthog2} implies that \[ T_1 = \frac{n!
	2^n}{(z_{\mu})^2 2^{2 l(\mu)}} \sum_{\nu \in OP(n)} p_2(\tilde{K}_{\nu})^2
	2^{l(\nu)} z_{\nu} \left( \frac{X^{\tau}_{\nu}}{g_{\tau}}
	\right)^2.\] From Lemma \ref{tcountsol} it follows that \[ T_2
	= 2 \left( 1-\frac{2 X^{\tau}_{\mu}}{g_{\tau}} \right) \frac{n!
	2^n}{(z_{\mu})^2 2^{2 l(\mu)}} \sum_{\nu \in OP(n)} p_2(\tilde{K}_{\nu})^2
	2^{l(\nu)} z_{\nu} \frac{X^{\tau}_{\nu}}{g_{\tau}}.\] By
	Corollary \ref{4step}, \[ T_3 = \frac{n! 2^n}{2^{2 l(\mu)}
	(z_{\mu})^2} \left( 1-\frac{2 X^{\tau}_{\mu}}{g_{\tau}} \right)^2
	\sum_{\nu \in OP(n)} p_2(\tilde{K}_{\nu})^2 2^{l(\nu)} z_{\nu}.\] Hence, one can
	write \[ T_1+T_2+T_3 = \frac{n! 2^n}{(z_{\mu})^2 2^{2 l(\mu)}}
	\sum_{\nu \in OP(n)} 2^{l(\nu)} z_{\nu} p_2(\tilde{K}_{\nu})^2 \left(
	\frac{X^{\tau}_{\nu}}{g_{\tau}} + 1 - 
	\frac{2 X^{\tau}_{\mu}}{g_{\tau}} \right)^2 \] and the result
	follows since by Lemmas \ref{tcountsol} and \ref{torthog2},
	the $\nu=(1^n)$ term in the above sum is $4 \left(1 -
	\frac{X^{\tau}_{\mu}}{g_{\tau}} \right)^2$. \end{proof}

	Lemma \ref{tmom1GP} will also be helpful.

\begin{lemma} \label{tmom1GP} Let $k$ be a positive integer.
\begin{enumerate}
\item $\ee(W^*-W)^k$ is equal to \[ \left( \frac{n!
2^{n-l(\mu)}}{z_{\mu}} \right)^{k/2}  \sum_{m=0}^k
(-1)^{k-m} {k \choose m} \sum_{\nu \in OP(n)} \frac{X^{\tau}_{\nu}
z_{\nu}}{g_{\tau} n! 2^{n-l(\nu)}} p_m(\tilde{K}_{\nu}) p_{k-m}(\tilde{K}_{\nu}).\]
\item $ \ee(W^*-W)^4$ is equal to \[ \left( \frac{n!
2^{n-l(\mu)}}{z_{\mu}} \right)^2 \left[ \sum_{\nu \in OP(n)} \left( 8
\left( 1-\frac{X^{\tau}_{\mu}}{g_{\tau}} \right)-6 \left(
1-\frac{X^{\tau}_{\nu}}{g_{\tau}} \right) \right) \frac{z_{\nu}
p_2(\tilde{K}_{\nu})^2}{n! 2^{n-l(\nu)}} \right].\]
\end{enumerate}
\end{lemma}

\begin{proof} To prove the first assertion, observe that
\begin{eqnarray*}
& & \ee((W^*-W)^k|\lambda)\\ & = & \left(
\frac{n!}{z_{\mu} 2^{n-l(\mu)}} \right)^{k/2} \sum_{\rho \in DP(n)}
\frac{g_{\rho}}{2^{l(\rho)} g_{\lambda} g_{\tau}} \sum_{\nu \in OP(n)}
\frac{2^{l(\nu)} X^{\lambda}_{\nu} X^{\rho}_{\nu}
X^{\tau}_{\nu}}{z_{\nu}}\\ & & \cdot \sum_{m=0}^k (-1)^{k-m} {k
\choose m} \left(\frac{X^{\rho}_{\mu}}{g_{\rho}} \right)^m
\left(\frac{X^{\lambda}_{\mu}}{g_{\lambda}} \right)^{k-m}\\ & = &
\left( \frac{n!}{z_{\mu} 2^{n-l(\mu)}} \right)^{k/2}
\frac{1}{g_{\lambda} g_{\tau}} \sum_{m=0}^k (-1)^{k-m} {k \choose m}
\left(\frac{X^{\lambda}_{\mu}}{g_{\lambda}} \right)^{k-m}\\ & & \cdot
\sum_{\nu \in OP(n)} \frac{2^{l(\nu)} X^{\lambda}_{\nu}
X^{\tau}_{\nu}}{z_{\nu}} \sum_{\rho \in DP(n)}
\frac{g_{\rho}^2}{2^{l(\rho)}} \frac{X^{\rho}_{\nu}}{g_{\rho}} \left(
\frac{X^{\rho}_{\mu}}{g_{\rho}} \right)^m \\ & = & \left(
\frac{n!}{z_{\mu} 2^{n-l(\mu)}} \right)^{k/2} \frac{1}{2^n g_{\lambda}
g_{\tau}} \sum_{m=0}^k (-1)^{k-m} {k
\choose m}  (2^{n-l(\mu)})^m \left(\frac{X^{\lambda}_{\mu}}{g_{\lambda}} \right)^{k-m}\\
& & \cdot \sum_{\nu \in OP(n)} 2^{l(\nu)} X^{\lambda}_{\nu}
X^{\tau}_{\nu} p_m(\tilde{K}_{\nu}),
\end{eqnarray*} where the last equation is Lemma \ref{tcountsol}. Hence $\ee(W^*-W)^k$ is equal to 
\begin{eqnarray*}
& & \ee(\ee((W^*-W)^k|\lambda))\\
 & = & \left( \frac{n!}{z_{\mu}
2^{n-l(\mu)}} \right)^{k/2} \frac{(2^{n-l(\mu)})^k}{2^n} \sum_{m=0}^k
(-1)^{k-m} {k \choose m}\\ & & \cdot \sum_{\nu \in OP(n)} 2^{l(\nu)} \frac{
X^{\tau}_{\nu}}{g_{\tau}} \frac{ p_m(\tilde{K}_{\nu}) }{(2^{n-l(\mu)})^{k-m}} \ee \left[
\frac{X^{\lambda}_{\nu}}{g_{\lambda}} \left(
\frac{X^{\lambda}_{\mu}}{g_{\lambda}} \right)^{k-m}
\right]. \end{eqnarray*} The first assertion now follows from Lemma
\ref{tcountsol}.

	For the second assertion, the first assertion gives
 that $\ee(W^*-W)^4$ is equal to \[ \left(\frac{n!
 2^{n-l(\mu)}}{z_{\mu}} \right)^2 \sum_{m=0}^4 (-1)^{m} {4 \choose m}
 \sum_{\nu \in OP(n)} \frac{z_{\nu}}{2^{n-l(\nu)} n!}
 \frac{X^{\tau}_{\nu}}{g_{\tau}} p_m(\tilde{K}_{\nu})
 p_{4-m}(\tilde{K}_{\nu}) .\] The special case $\tau=(n)$ gives that
 \[ 0 = \left(\frac{n!  2^{n-l(\mu)}}{z_{\mu}} \right)^2 \sum_{m=0}^4
 (-1)^{m} {4 \choose m} \sum_{\nu \in OP(n)}
 \frac{z_{\nu}}{2^{n-l(\nu)} n!}  p_m(\tilde{K}_{\nu})
 p_{4-m}(\tilde{K}_{\nu}).\] Thus in general, $\ee(W^*-W)^4$ is equal
 to \[ - \left(\frac{n!  2^{n-l(\mu)}}{z_{\mu}} \right)^2 \sum_{m=0}^4
 (-1)^{m} {4 \choose m} \sum_{\nu \in OP(n)}
 \left(1-\frac{X^{\tau}_{\nu}}{g_{\tau}} \right) \frac{z_{\nu}
 p_m(\tilde{K}_{\nu}) p_{4-m}(\tilde{K}_{\nu})}{2^{n-l(\nu)} n!}  .\]
 The $m=0,4$ terms vanish since only $\nu=(1^n)$ could contribute, but
 it contributes 0. The $m=2$ term contributes \[ -6 \left(\frac{n!
 2^{n-l(\mu)} }{z_{\mu}} \right)^2 \sum_{\nu \in OP(n)} \left(
 1-\frac{X^{\tau}_{\nu}}{g_{\tau}} \right) \frac{z_{\nu}
 p_2(\tilde{K}_{\nu})^2}{n!  2^{n-l(\nu)}}.\] The $m=1,3$ terms are
 equal and together contribute \[ 8 \left(\frac{n!
 2^{n-l(\mu)}}{z_{\mu}} \right) \left(
 1-\frac{X^{\tau}_{\mu}}{g_{\tau}} \right) p_3(\tilde{K}_{\mu}).\] By
 Lemma \ref{3step}, this is \[ 8 \left( \frac{n!
 2^{n-l(\mu)}}{z_{\mu}} \right)^2 \left( 1 -
 \frac{X^{\tau}_{\mu}}{g_{\tau}} \right) \sum_{\nu \in OP(n)}
 \frac{z_{\nu} p_2(\tilde{K}_{\nu})^2}{n! 2^{n-l(\nu)}} .\] Adding the
 terms together proves the second assertion.  \end{proof}

	The final combinatorial ingredient for the proof of Theorem
	\ref{projerror} is an upper bound for
	$p_2(\tilde{K}_{\nu})$. Lemma \ref{reduce} reduces this to a
	result obtained earlier in the section on Gelfand pairs.

\begin{lemma}
 \label{reduce} Let $p_2(\tilde{K}_{\nu})$ be as in this subsection and
 let $p_2(K_{\nu})$ be as in Subsection \ref{matching}. Then
 $p_2(\tilde{K}_{\nu}) \leq p_2(K_{\nu})$ for all $\nu \in OP(n)$.
\end{lemma}

\begin{proof}
 Clearly $p_2(K_{\nu})$ is equal to $|B_n \omega_{\nu} B_n|$
 multiplied by the coefficient of $\omega_{\nu}$ in \[ \left(
 \frac{1}{|B_n|^2} \sum_{x_1,x_2 \in B_n} x_1 \omega_{\mu} x_2
 \right)^2.\] Next consider $p_2(\tilde{K}_{\nu})$. By definition it
 is the coefficient of $\tilde{K}_{\nu}$ in
 $(\tilde{K}_{\mu})^2$. Corollary 3.2 of \cite{Stem} gives that the
 coefficient of $\omega_{\nu}$ in $\tilde{K}_{\nu}$ is $\frac{1}{|B_n
 \omega_{\nu} B_n|}$. Hence $p_2(\tilde{K}_{\nu})$ is $|B_n
 \omega_{\nu} B_n|$ multiplied by the coefficient of $\omega_{\nu}$ in
 \[ \left( \frac{1}{|B_n|^2} \sum_{x_1,x_2 \in B_n} \phi(x_1 x_2) x_1
 \omega_{\mu} x_2 \right)^2,\] where $\phi$ is the linear character of
 $B_n$ described in Subsection \ref{rtgelfand}. Since $\phi(x_1
 x_2)$ is always $\pm 1$, the result follows. \end{proof}

	Finally, we prove Theorem \ref{projerror}.

\begin{proof}
 (Of Theorem \ref{projerror}) One can assume that $n \geq 2(2i+1)$. In
 the $O$ notation throughout the proof, $i$ is fixed and $n$ is
 growing.

	 One applies Theorem \ref{steinbound} to the pair $(W,W')$,
 where $\mu=(2i+1,1^{n-2i-1})$. Then $a=1-\frac{m_1(\mu)}{n}$ by part
 2 of Lemma \ref{tsteinsat2}. Proposition \ref{2chains} implies that
 \[ \ee((W'-W)^2|\lambda) = \frac{n-2}{n} \ee((W^*-W)^2|\lambda)\] for
 all $\lambda$. Thus \[ Var(\ee[(W'-W)^2|\lambda]) = \left(
 \frac{n-2}{n} \right)^2 Var(\ee[(W^*-W)^2|\lambda]).\] Lemmas
 \ref{tbig1GP} and \ref{valtwist} give that the first error term in
 applying Theorem \ref{steinbound} to the pair $(W,W')$ is at most \[
 \frac{n-2}{n} \frac{n! 2^{n-l(\mu)}}{\left(
 1-\frac{m_1(\mu)}{n} \right) z_{\mu}} \sqrt{ \sum_{\nu \in OP(n) \atop \nu \neq (1^n)}
 \frac{z_{\nu} p_2(\tilde{K}_{\nu})^2}{n!  2^{n-l(\nu)}} \left(
 \frac{n+m_1(\nu)-2m_1(\mu)}{n-2} \right)^2}.\] Observe that
 $\frac{n-2}{n} \frac{n! 2^{n-l(\mu)}}{\left(
 1-\frac{m_1(\mu)}{n} \right) z_{\mu}}$ is $O(n^{2i+2})$. In the sum
 over $\nu \neq (1^n)$, the term coming from
 $\nu=(2i+1,2i+1,1^{n-4i-2})$ contributes 0. Since $n \geq 2(2i+1)$,
 Lemmas \ref{reduce} and \ref{term1GP} imply that $\frac{z_{\nu}
 p_2(\tilde{K}_{\nu})^2}{n! 2^{n-l(\nu)}} = O(n^{-4i-3})$ for all
 other $\nu$ in the sum, and the number of such $\nu$ is bounded by a
 constant depending on $i$ but not $n$. Moreover if
 $p_2(\widetilde{K}_{\nu}) \neq 0$, then $p_2(K_{\nu}) \neq 0$,
 implying by Lemma \ref{con} that $m_1(\nu) \geq n-4i-2$ and thus that
 $ \frac{n+m_1(\nu)-2m_1(\mu)}{n-2}=O(n^{-1})$. Combining these
 observations gives that the first term in the upper bound of Theorem
 \ref{steinbound} is $O(n^{-1/2})$.

	By the Cauchy-Schwarz inequality, \[ \ee|W'-W|^3 \leq \sqrt{
	\ee(W'-W)^2 \ee(W'-W)^4} .\] Proposition \ref{2chains} implies
	that $\ee(W'-W)^k = \frac{n-2}{n} \ee(W^*-W)^k$ for all
	$k$. Hence Lemmas \ref{timmcor2} and \ref{valtwist} imply that
	the second error term in Theorem \ref{steinbound} is at most
	\[ \left[ \frac{(n-2)}{\pi n}
	\frac{\ee(W^*-W)^4}{(1-\frac{m_1(\mu)}{n})} \right]^{1/4} .\]
	By part 2 of Lemma \ref{tmom1GP} and Lemma \ref{valtwist},
	this can be written as \[ \left[ \frac{1}{\pi} \frac{(n!
	2^{n-l(\mu)})^2}{(1-\frac{m_1(\mu)}{n}) (z_{\mu})^2} \sum_{\nu
	\in OP(n)} \left( 2 - \frac{8m_1(\mu)}{n} + \frac{6
	m_1(\nu)}{n} \right) \frac{z_{\nu} p_2(\tilde{K}_{\nu})^2}{n!
	2^{n-l(\nu)}} \right]^{1/4}. \] The quantity $\frac{(n!
	2^{n-l(\mu)})^2}{(1-\frac{m_1(\mu)}{n}) (z_{\mu})^2}$ is
	$O(n^{4i+3})$. The contribution from $\nu=(1^n)$ to the sum is
	$\frac{8(2i+1)}{n} p_2(\tilde{K}_{(1^n)})^2$, which by Lemmas
	\ref{tcountsol} and \ref{torthog2} is $\frac{8
	(2i+1)^3}{2^{4i}} n^{-4i-3} + O(n^{-4i-4})$. By Lemmas
	\ref{reduce} and \ref{term1GP}, the contribution to the sum
	from $\nu$ not equal to either $(1^n)$ or
	$(2i+1,2i+1,1^{n-4i-2})$ is $O(n^{-4i-4})$. The contribution
	from $\nu=(2i+1,2i+1,1^{n-4i-2})$ is $-\frac{4(2i+1)}{n}
	\frac{z_{\nu} p_2(\tilde{K}_{\nu})^2}{n! 2^{n-l(\nu)}}$. Lemma
	\ref{sumneq1} implies that
	$p_2(\tilde{K}_{(2i+1,2i+1,1^{n-4i-2})})= 1+O(n^{-1})$, since
	$p_2(\tilde{K}_{\nu}) = O(n^{-1})$ for $\nu \neq
	(2i+1,2i+1,1^{n-4i-2})$ by Lemma \ref{reduce}. Thus the
	contribution from $\nu=(2i+1,2i+1,1^{n-4i-2})$ is
	$-\frac{8(2i+1)^3}{2^{4i}} n^{-4i-3} + O(n^{-4i-4})$. Hence
	there is useful cancellation and \[ \sum_{\nu \in OP(n)}
	\left( 2 - \frac{8m_1(\mu)}{n} + \frac{6 m_1(\nu)}{n} \right)
	\frac{z_{\nu} p_2(\tilde{K}_{\nu})^2}{n!  2^{n-l(\nu)}} =
	O(n^{-4i-4}). \] It follows that the second term in the upper
	bound of Theorem \ref{steinbound} is $O(n^{-1/4})$, completing
	the proof. \end{proof}
