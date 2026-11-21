---
doc_id: arxiv-math-0508291v1
doc_title: "Stein’s Method and Random Character Ratios Running head: Stein’s Method and Random Character Ratios Version of 8/13/05"
section_id: sec-008-42-central-limit-theorem-for-spherical-functions
section_title: "Central limit theorem for spherical functions"
section_number: 4.2
pages: 18-23
source_pdf: 0508291v1.pdf
source_sha256: d2d541426aaec742
toc_source: outline
text_source: latex
latex_prose_ratio: 0.934
latex_coverage_ratio: 0.986
doc_brief: "Stein’s Method and Random Character Ratios Running head: Stein’s Method and Random Character Ratios Version of 8/13/05 — Stein’s method is used to prove limit theorems for random character ratios."
---
\label{gelfandCLT}

	The aim of this subsection is to prove a central limit theorem
	for the random variable $W$ defined by
	$W(i)=\frac{|K_u|^{1/2}}{|K|^{1/2}} \omega_i(g_u)$. Here $g_u$
	is fixed satisfying $Kg_uK= K g_u^{-1}K$ and $i$ is random
	from the Plancherel measure of the Gelfand pair $(G,K)$. It is not
	assumed that the Gelfand pair $(G,K)$ is symmetric.

	To construct an exchangeable pair to be used for Stein's
	method, it is helpful to define a Markov chain on the set of
	spherical functions of $(G,K)$. To do this fix $t$ with $1
	\leq t \leq s$ such that the spherical function $\omega_t$ is
	real-valued. Let $L_t$ be the Markov chain on
	the set $\{\omega_0,\cdots,\omega_s\}$ which transitions from
	$\omega_i$ to $\omega_j$ with probability \[
	L_t(\omega_i,\omega_j) := \frac{d_j}{|G|} \sum_{r=0}^s |K_r|
	\omega_i(g_r) \omega_t(g_r) \overline{\omega_j(g_r)}.\] As in
	the group case, one typically wants to choose $\omega_t$ as
	close as possible to the trivial spherical function.

        Lemma \ref{niceprop} verifies that $L_t$ is a Markov chain
        which is reversible with respect to Plancherel measure.

\begin{lemma} \label{niceprop} Let $t$
 with $0 \leq t \leq s$ be such that the spherical function $\omega_t$
 is real-valued. Then the transition probabilities of $L_t$ are real
 and non-negative and sum to 1. Moreover the chain $L_t$ is reversible
 with respect to the Plancherel measure of the pair
 $(G,K)$. \end{lemma}

\begin{proof}  From page 396 of \cite{Mac}, if $a_{it}^k$ are defined by \[ \omega_i
 \omega_t = \sum_{k=0}^s a_{it}^k \omega_k \] (where the notation
 $\omega_i \omega_j$ denotes the pointwise product), then $a_{it}^k$
 are real and non-negative. Hence Lemma \ref{orthog1} implies that
 $L_t(\omega_i,\omega_j)$ is real and non-negative. Since
 $\omega_j(g_0)=1$ for all $j$, Lemma \ref{orthog2} gives that \[
 \sum_{j=0}^s L_t(\omega_i,\omega_j) = \sum_{r=0}^s |K_r|
 \omega_i(g_r) \omega_t(g_r) \frac{1}{|G|} \sum_{j=0}^s d_j
 \omega_j(g_0) \overline{\omega_j(g_r)} =1.\] Reversibility of $L_t$
 with respect to Plancherel measure is equivalent to showing that \[
 \frac{d_i d_j |K|}{|G|} \sum_{r=0}^s |K_r| \omega_i(g_r) \omega_t(g_r)
 \overline{\omega_j(r)} = \frac{d_i d_j |K|}{|G|} \sum_{r=0}^s |K_r|
 \omega_j(g_r) \omega_t(g_r) \overline{\omega_i(r)}.\] Both sides are
 real by the previous paragraph, so the result follows by the
 assumption that $\omega_t$ is real valued.  \end{proof}

	An exchangeable pair $(W,W')$ to be used in a Stein's method
        approach to studying $W$ can be constructed from the chain
        $L_t$ in the usual way. First choose $i$ from Plancherel measure,
        then choose $j$ with probability $L_t(\omega_i,\omega_j)$, and
        finally let $(W,W')=(W(\omega_i),W(\omega_j))$.

\begin{lemma} \label{steinsat2} $\ee(W'|W) = \omega_t(g_u) W$.
\end{lemma}

\begin{proof} From the definitions and Lemma \ref{orthog2},
\begin{eqnarray*}
\ee(W'|\omega_i) & = & \frac{|K_u|^{1/2}}{|K|^{1/2}} \sum_{j=0}^s \frac{d_j}{|G|} \sum_{r=0}^s |K_r| \omega_i(g_r) \omega_t(g_r) \overline{\omega_j(g_r)} \omega_j(g_u)\\
& = & \frac{|K_u|^{1/2}}{|K|^{1/2}} \sum_{r=0}^s |K_r| \omega_i(g_r) \omega_t(g_r) \sum_{j=0}^s \frac{d_j}{|G|} \omega_j(g_u) \overline{\omega_j(g_r)}\\
& = &  \omega_t(g_u) W(\omega_i). \end{eqnarray*} The result follows since this depends on $\omega_i$ only through $W$. \end{proof}

	Corollary \ref{record2} is not needed in the sequel but is
	interesting.

\begin{cor}
 \label{record2} The eigenvalues of $L_t$ are $\omega_t(g_r)$ for $0
 \leq r \leq s$. The functions $\psi_r(\omega_i) =
 \frac{|K_{g_r}|^{1/2}}{|K|^{1/2}} \omega_i(g_r)$ are a basis of
 eigenvectors of $L_{\tau}$, orthonormal with respect to the inner
 product \[ \langle f_1,f_2 \rangle = \sum_{i=0}^s f_1(\omega_i)
 \overline{f_2(\omega_i)} \frac{d_i |K|}{|G|}.\]
\end{cor}

\begin{proof} By the proof of Lemma \ref{steinsat2}, $\psi_r$ is an eigenvector of $L_{t}$ with
 eigenvalue $\omega_t(g_r)$. The orthonormality assertion follows from
 Lemma \ref{orthog2}, and the basis assertion follows since the number
 of spherical functions is equal to the number of $K$ double cosets of
 $G$. \end{proof}

\begin{lemma} \label{immcor2}
$\ee(W'-W)^2 = 2(1-\omega_t(g_u))$.
\end{lemma}

\begin{proof} This is immediate from Lemmas \ref{var} and \ref{steinsat2}.
\end{proof}

\begin{lemma} \label{preGP}
$\ee((W')^2|\omega_i) = \frac{|K_u|}{|K|} \sum_{r=0}^s \omega_i(g_r) \omega_t(g_r) p_2(K_r)$.
\end{lemma}

\begin{proof} From the definitions,
\begin{eqnarray*} \ee((W')^2|\omega_i)
& = & \frac{|K_u|}{|K|} \sum_{j=0}^s \frac{d_j}{|G|} \sum_{r=0}^s |K_r| \omega_i(g_r) \omega_t(g_r) \overline{\omega_j(g_r)} \omega_j(g_u)^2\\
& = & \frac{|K_u|}{|K|} \sum_{r=0}^s |K_r| \omega_i(g_r) \omega_t(g_r) \frac{1}{|G|} \sum_{j=0}^s d_j \omega_j(g_u)^2 \overline{\omega_j(g_r)}. \end{eqnarray*} The result follows from Lemma \ref{fourier}.
\end{proof}

	Note that the sum in Lemma \ref{big1GP} begins at $r=1$ and so
	excludes the $r=0$ term which corresponds to the trivial
	spherical function.

\begin{lemma} \label{big1GP}
\[ Var(\ee[(W'-W)^2|\omega_i]) = \frac{|K_u|^2}{|K|} \sum_{r=1}^s
\frac{p_2(K_r)^2}{|K_r|} \left( \omega_t(g_r)+ 1 - 2 \omega_t(g_u) \right)^2.\]
\end{lemma}

\begin{proof} It follows from Lemmas \ref{preGP}, \ref{immcor2}, and \ref{steinsat2} that
\begin{eqnarray*}
& & Var(\ee[(W'-W)^2|\omega_i])\\
& = & \ee(\ee((W'-W)^2|\omega_i)^2) - 4(1-\omega_t(g_u))^2\\
& = & \frac{|K_u|^2}{|K|^2} \ee \left[ \sum_{r=0}^s p_2(K_r) \omega_i(g_r) \omega_t(g_r) + (1-2 \omega_t(g_u)) \omega_i(g_u)^2 \right]^2 \\
& & - 4(1-\omega_t(g_u))^2\\
& = & T_1 + T_2 + T_3 - 4(1-\omega_t(g_u))^2
\end{eqnarray*} where
\[ T_1 = \frac{|K_u|^2}{|K|^2} \ee \left( \sum_{r=0}^s p_2(K_r) \omega_i(g_r) \omega_t(g_r) \right)^2 \]
\[ T_2 = \frac{|K_u|^2}{|K|^2} 2 (1-2 \omega_t(g_u)) \sum_{r=0}^s p_2(K_r)  \omega_t(g_r) \ee \left(\omega_i(g_r)  \omega_i(g_u)^2 \right) \]
\[ T_3 = \frac{|K_u|^2}{|K|^2} (1-2 \omega_t(g_u))^2 \ee ( \omega_i(g_u)^4).\]

	For reasons similar to the finite group case, there are useful
	simplifications.  Lemma \ref{orthog2} implies that \[ T_1 =
	\frac{|K_u|^2}{|K|} \sum_{r=0}^s \frac{p_2(K_r)^2
	\omega_t(g_r)^2}{|K_r|} .\] Lemma \ref{fourier} gives that \[
	T_2 = \frac{|K_u|^2}{|K|} 2 (1-2 \omega_t(g_u)) \sum_{r=0}^s
	\frac{p_2(K_r)^2 \omega_t(g_r)}{|K_r|} .\] Also, one can write
	\[ T_3 = \frac{|K_u|^2}{|K|^2} (1-2 \omega_t(g_u))^2 p_4(K_0) =
	\frac{|K_u|^2}{|K|} (1-2 \omega_t(g_u))^2 \sum_{r=0}^s
	\frac{p_2(K_r)^2}{|K_r|}.\] The first equality used Lemma
	\ref{fourier} and the second equality used the assumption that
	$Kg_uK = Kg_u^{-1}K$. Hence \[ T_1+T_2+T_3 =
	\frac{|K_u|^2}{|K|} \sum_{r=0}^s \frac{p_2(K_r)^2}{|K_r|}
	\left( \omega_t(g_r)+1-2 \omega_t(g_u) \right)^2,\] which
	implies the result since the $r=0$ term is
	$4(1-\omega_t(g_u))^2$. \end{proof}


\begin{lemma} \label{mom1GP} Let $k$ be a positive integer.
\begin{enumerate}
\item $\ee(W'-W)^k$ is equal to \[ \left( \frac{|K_u|}{|K|} \right)^{k/2} \sum_{m=0}^k (-1)^{k-m} {k \choose m} \sum_{r=0}^s \frac{|K|}{|K_r|} \omega_t(g_r) p_m(K_r) p_{k-m}(K_r).\]
\item $\ee(W'-W)^4 = \frac{|K_u|^2}{|K|} \sum_{r=0}^s \left[ 8 \left (1-\omega_t(g_u) \right) -6 \left( 1 - \omega_t(g_r) \right) \right] \frac{p_2(K_r)^2}{|K_r|}$.
\end{enumerate}
\end{lemma}

\begin{proof} For the first assertion, note that $\ee((W'-W)^k|\omega_i)$ is equal to \begin{eqnarray*}
& & \left( \frac{|K_u|}{|K|} \right)^{k/2} \sum_{j=0}^s \frac{d_j}{|G|} \sum_{r=0}^s |K_r| \omega_i(g_r) \omega_t(g_r) \overline{\omega_j(g_r)} \left( \omega_j(g_u)-\omega_i(g_u) \right)^k\\
& = & \left( \frac{|K_u|}{|K|} \right)^{k/2} \sum_{j=0}^s \frac{d_j}{|G|} \sum_{r=0}^s |K_r| \omega_i(g_r) \omega_t(g_r) \overline{\omega_j(g_r)}\\
& & \cdot \sum_{m=0}^k (-1)^{k-m} {k \choose m} \omega_j(g_u)^m \omega_i(g_u)^{k-m}\\
& = & \left( \frac{|K_u|}{|K|} \right)^{k/2} \sum_{m=0}^k (-1)^{k-m} {k \choose m} \omega_i(g_u)^{k-m} \\
& & \cdot \sum_{r=0}^s |K_r| \omega_i(g_r) \omega_t(g_r) \sum_{j=0}^s \frac{d_j}{|G|} \omega_j(g_u)^m \overline{\omega_j(g_r)}\\
& = &  \left( \frac{|K_u|}{|K|} \right)^{k/2} \sum_{m=0}^k (-1)^{k-m} {k \choose m} \omega_i(g_u)^{k-m} \sum_{r=0}^s \omega_i(g_r) \omega_t(g_r) p_m(K_r), \end{eqnarray*} where the last equality is Lemma \ref{fourier}. Hence \begin{eqnarray*} 
\ee(W'-W)^k & = & \ee(\ee((W'-W)^k|\omega_i))\\
& = & \left( \frac{|K_u|}{|K|} \right)^{k/2} \sum_{m=0}^k (-1)^{k-m} {k \choose m}\\
& & \cdot \sum_{r=0}^s \omega_t(g_r) p_m(K_r) \sum_{i=0}^s \frac{d_i |K|}{|G|} \omega_i(g_r) \omega_i(g_u)^{k-m}. \end{eqnarray*} The first assertion follows from Lemma \ref{fourier} and the fact that $\omega_i(g_u)$ is real.

	For the second assertion, one knows from the first assertion
	that \[ \ee(W'-W)^4 = \left( \frac{|K_u|}{|K|} \right)^{2}
	\sum_{m=0}^4 (-1)^{m} {4 \choose m} \sum_{r=0}^s
	\frac{|K|}{|K_r|} \omega_t(g_r) p_m(K_r) p_{4-m}(K_r).\] The
	special case $t=0$ gives the equation \[ 0 = \left(
	\frac{|K_u|}{|K|} \right)^{2} \sum_{m=0}^4 (-1)^{m} {4 \choose
	m} \sum_{r=0}^s \frac{|K|}{|K_r|} p_m(K_r) p_{4-m}(K_r).\]
	Hence in general, $\ee(W'-W)^4$ is equal to \[ -
	\frac{|K_u|^2}{|K|^2} \sum_{m=0}^4 (-1)^{m} {4 \choose m}
	\sum_{r=0}^s \frac{|K|}{|K_r|} (1-\omega_t(g_r)) p_m(K_r)
	p_{4-m}(K_r).\] The $m=0,4$ terms both vanish since
	$p_0(K_r)=0$ if $r \neq 0$. The $m=2$ term is equal to \[ -
	\frac{6 |K_u|^2}{|K|} \sum_{r=0}^s \frac{(1-\omega_t(g_r))
	p_2(K_r)^2}{|K_r|}.\] The $m=1,3$ terms are equal and together
	contribute \begin{eqnarray*} \frac{8 |K_u|^2}{|K|}
	\sum_{r=0}^s \frac{(1-\omega_t(g_r)) p_1(K_r) p_3(K_r)}{|K_r|}
	& = & \frac{ 8 |K_u|}{|K|} (1-\omega_t(g_u)) p_3(K_u)\\ & = &
	\frac{8 |K_u|^2}{|K|^2} (1-\omega_t(g_u)) p_4(K_0)\\ & = &
	\frac{8 |K_u|^2}{|K|} (1-\omega_t(g_u)) \sum_{r=0}^s
	\frac{p_2(K_r)^2}{|K_r|}. \end{eqnarray*} This completes the
	proof of the second assertion. \end{proof}

	Arguing as in the proof of Theorem \ref{main1}, and using the
	above lemmas, one obtains the following result.

\begin{theorem}
 \label{main2} Let $(G,K)$ be a Gelfand pair, and fix a double coset
 $K_u=Kg_uK$ of $G$ satisfying $Kg_uK=Kg_u^{-1}K$. Let $\omega_t$ be a
 nontrivial spherical function which is real valued. Choosing
 $\omega_i$ from the Plancherel measure of the pair $(G,K)$, let $W=
 \frac{|K_u|^{1/2}}{|K|^{1/2}} \omega_i(g_u)$.  Then for all real
 $x_0$, \begin{eqnarray*} && \left| \pp(W \leq x_0) - \frac{1}{\sqrt{2
 \pi}} \int_{-\infty}^{x_0} e^{-\frac{x^2}{2}} dx \right|\\ & \leq &
 \frac{|K_u|}{a |K|} \sqrt{ \sum_{r=1}^s \frac{|K|p_2(K_r)^2}{|K_r|}
 \left( \omega_t(g_r)+2a-1 \right)^2 }\\ & & + \frac{1}{(\pi)^{1/4}}
 \frac{|K_u|^{1/2}}{|K|^{1/2}} \left[ \sum_{r=0}^s \left( 8 -
 \frac{6(1-\omega_t(g_r))}{a} \right) \frac{|K| p_2(K_r)^2}{|K_r|}
 \right]^{1/4}, \end{eqnarray*} where
 $a=1-\omega_t(g_u)$. \end{theorem}
