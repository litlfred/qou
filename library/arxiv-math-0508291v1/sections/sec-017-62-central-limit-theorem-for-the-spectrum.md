---
doc_id: arxiv-math-0508291v1
doc_title: "Stein’s Method and Random Character Ratios Running head: Stein’s Method and Random Character Ratios Version of 8/13/05"
section_id: sec-017-62-central-limit-theorem-for-the-spectrum
section_title: "Central limit theorem for the spectrum"
section_number: 6.2
pages: 44-49
source_pdf: 0508291v1.pdf
source_sha256: d2d541426aaec742
toc_source: outline
text_source: latex
latex_prose_ratio: 0.88
latex_coverage_ratio: 0.992
doc_brief: "Stein’s Method and Random Character Ratios Running head: Stein’s Method and Random Character Ratios Version of 8/13/05 — Stein’s method is used to prove limit theorems for random character ratios."
---
\label{assocCLT}

	Recall that the goal is to study Plancherel measure of
	association schemes, which chooses $i \in \{0,\cdots,n\}$ with
	probability $\frac{\mu_i}{|X|}$. More precisely, for $s$
	fixed, a central limit theorem is proved for the random
	variable $W$ whose value at $i \in \{0,\cdots,n \}$ is
	$\frac{\phi_s(i)}{\sqrt{v_s}}$.

 	Given $t \in \{0,\cdots,n\}$, we define a Markov chain $L_t$ on
	the set $\{0,\cdots,n \}$ which moves from $i$ to $j$ with
	probability \[ L_t(i,j) := \frac{\mu_j}{|X|} \sum_{r=0}^n
	\frac{\phi_r(i) \phi_r(t) \phi_r(j)}{(v_r)^2} .\]

\begin{lemma} \label{asniceprop} The transition probabilities of $L_t$ are real and non-negative and sum to 1. Moreover the chain $L_t$ is reversible with respect to Plancherel measure.
\end{lemma}

\begin{proof} By Theorems 3.6 and 3.8 of \cite{BI}, the $L_t(i,j)$ are non-negative real numbers. Next, observe that \[ \sum_{j=0}^n L_t(i,j)
 = \frac{1}{|X|} \sum_{r=0}^n \frac{\phi_r(i) \phi_r(t)}{(v_r)^2}
 \sum_{j=0}^n \mu_j \phi_r(j).\] Since $\phi_0(j)=1$ for all $j$,
 Lemma \ref{asorthog2} implies that \[ \sum_{j=0}^n L_t(i,j) = v_0
 \sum_{r=0}^n \frac{\phi_r(i) \phi_r(t)}{(v_r)^2} \delta_{r,0} = 1.\]
 For the reversibility assertion, it is clear from the definition of
 $L_t$ that \[ \frac{\mu_i}{|X|} L_t(i,j) = \frac{\mu_j}{|X|} L_t(j,i)
 \] for all $i,j$. \end{proof}
	
	One uses the chain $L_t$ to construct an exchangeable pair
	$(W,W')$ in the usual way. First choose $i$ from Plancherel
	measure, then choose $j$ with probability $L_t(i,j)$, and
	finally let $(W,W') = (W(i),W(j))$.

\begin{lemma} \label{assteinsat} $\ee(W'|W) = \left( \frac{\phi_s(t)}{v_s} \right) W$.
\end{lemma}

\begin{proof} By the definitions and Lemma \ref{asorthog2}, one has that \begin{eqnarray*} \ee(W'|i) & = & \frac{1}{\sqrt{v_s}} \sum_{j=0}^n
L_t(i,j) \phi_s(j)\\ & = & \frac{1}{\sqrt{v_s}} \frac{1}{|X|}
\sum_{r=0}^n \frac{\phi_r(i) \phi_r(t)}{(v_r)^2} \sum_{j=0}^n \mu_j
\phi_s(j) \phi_r(j)\\ & = & \left( \frac{\phi_s(t)}{v_s} \right)
W(i). \end{eqnarray*} The result follows since this depends on
$i$ only through $W$. \end{proof}

	Corollary \ref{eiglast} will not be used but is worth recording.

\begin{cor} \label{eiglast} The eigenvalues of $L_t$ are $\frac{\phi_s(t)}{v_s}$ for $0 \leq s \leq n$. The functions $\psi_s(i) = \frac{\phi_s(i)}{\sqrt{v_s}}$ are a basis of eigenvectors of $L_t$, orthonormal with respect to the inner product \[ \langle f_1,f_2 \rangle = \sum_{i=0}^n f_1(i) \overline{f_2(i)} \frac{\mu_i}{|X|}.\]
\end{cor}

\begin{proof} The proof of Lemma \ref{assteinsat} shows that $\psi_s$ is an eigenvector of $L_t$ with eigenvalue  $\frac{\phi_s(t)}{v_s}$. The orthonormality assertion follows from Lemma \ref{asorthog2}, and the basis assertion follows since there are $n+1$ eigenvectors. \end{proof}

\begin{lemma} \label{asimmcor} $\ee(W'-W)^2 = 2 \left( 1-\frac{\phi_s(t)}{v_s} \right)$. \end{lemma}

\begin{proof} This is immediate from Lemmas \ref{var} and \ref{assteinsat}.
\end{proof}

\begin{lemma} \label{aspre2} $\ee((W')^2|i) = v_s \sum_{r=0}^n \frac{\phi_r(i)\phi_r(t)}{(v_r)^2} p_2(r)$.
\end{lemma}

\begin{proof} It follows from the definitions that \begin{eqnarray*}
\ee((W')^2|i) & = & \frac{1}{v_s} \sum_{j=0}^n \frac{\mu_j}{|X|}
\sum_{r=0}^n \frac{\phi_r(i) \phi_r(t) \phi_r(j)}{(v_r)^2}
\phi_s(j)^2\\ & = & \frac{1}{v_s} \sum_{r=0}^n \frac{\phi_r(i)
\phi_r(t)}{(v_r)^2} \sum_{j=0}^n \frac{\mu_j}{|X|} \phi_s(j)^2
\phi_r(j). \end{eqnarray*} The result now follows from Lemma
\ref{ascountsol}. \end{proof}

	Note that in the next lemma, the sum is over non-zero $r$. 

\begin{lemma} \label{asbig1} \[ Var(\ee[(W'-W)^2|i]) = (v_s)^2 \sum_{r=1}^n \frac{p_2(r)^2}{v_r} \left( \frac{\phi_r(t)}{v_r} + 1 - \frac{2 \phi_s(t)}{v_s} \right)^2.\]
\end{lemma}

\begin{proof} By Lemmas \ref{assteinsat}, \ref{asimmcor}, and \ref{aspre2}, $Var(\ee[(W'-W)^2|i])$ is equal to 
\begin{eqnarray*}
& & \ee(\ee((W'-W)^2|i)^2) - 4 \left(1 - \frac{\phi_s(t)}{v_s} \right)^2\\
& = & \ee \left[ v_s \sum_{r=0}^n \frac{\phi_r(i) \phi_r(t)}{(v_r)^2} p_2(r) + \left( 1 - \frac{2 \phi_s(t)}{v_s} \right) W^2 \right]^2\\
& &  - 4 \left(1 - \frac{\phi_s(t)}{v_s} \right)^2\\
& = & T_1 + T_2 + T_3 - 4 \left(1 - \frac{\phi_s(t)}{v_s} \right)^2,
\end{eqnarray*} where 
\[ T_1 = (v_s)^2 \ee \left( \sum_{r=0}^n \frac{\phi_r(i) \phi_r(t)}{(v_r)^2} p_2(r) \right)^2 \]
\[ T_2 = 2 \left(1-\frac{2 \phi_s(t)}{v_s} \right) \sum_{r=0}^n
 \frac{\phi_r(t)}{(v_r)^2} p_2(r) \ee \left( \phi_r(i)
 \phi_s(i)^2  \right) \]
\[ T_3 = \left( 1 - \frac{2 \phi_s(t)}{v_s} \right)^2 \ee \left( \frac{\phi_s(i)^4}{(v_s)^2} \right).\]

	Next we simplify these terms. By Lemma \ref{asorthog2}, \[ T_1
	= (v_s)^2 \sum_{r=0}^n \frac{\phi_r(t)^2}{(v_r)^3} p_2(r)^2.\]
	Lemma \ref{ascountsol} implies that \[ T_2 = 2 (v_s)^2 \left(1
	- \frac{2 \phi_s(t)}{v_s} \right) \sum_{r=0}^n
	\frac{\phi_r(t)}{(v_r)^2} p_2(r)^2.\] Lemma \ref{ascountsol}
	and part 1 of Lemma \ref{asrel} imply that \[ T_3
	= (v_s)^2 \left( 1-\frac{2 \phi_s(t)}{v_s} \right)^2 p_4(0) =
	(v_s)^2 \left( 1-\frac{2 \phi_s(t)}{v_s} \right)^2
	\sum_{r=0}^n \frac{p_2(r)^2}{v_r} .\] Thus \[ T_1+T_2+T_3 =
	(v_s)^2 \sum_{r=0}^n \frac{p_2(r)^2}{v_r}
	\left(\frac{\phi_r(t)}{v_r} + 1 - \frac{2 \phi_s(t)}{v_s}
	\right)^2.\] Since $p_2(0)=\frac{1}{v_s}$, the $r=0$ term of
	$T_1+T_2+T_3$ is equal to $4 \left(1 - \frac{\phi_s(t)}{v_s}
	\right)^2$, proving the result. \end{proof}

\begin{lemma} \label{asmom1} Let $k$ be a positive integer.
\begin{enumerate}
\item $\ee(W'-W)^k = (v_s)^{k/2} \sum_{m=0}^k (-1)^{k-m} {k \choose m} \sum_{r=0}^n \frac{\phi_r(t)}{v_r} \frac{p_m(r) p_{k-m}(r)}{v_r}$.
\item $\ee(W'-W)^4 =  v_s^2 \left[ \sum_{r=0}^n \left(8 \left(
1-\frac{\phi_s(t)}{v_s} \right) - 6  \left(1 - \frac{\phi_r(t)}{v_r} \right) \right) \frac{p_2(r)^2}{v_r} \right]$.
\end{enumerate}
\end{lemma}

\begin{proof} For the first assertion, note that
\begin{eqnarray*}
& & \ee((W'-W)^k|i)\\ & = & \frac{1}{(v_s)^{k/2}} \sum_{j=0}^n
\frac{\mu_j}{|X|} \sum_{r=0}^n \frac{\phi_r(i) \phi_r(t)
\phi_r(j)}{(v_r)^2} (\phi_s(j)-\phi_s(i))^k\\ & = &
\frac{1}{(v_s)^{k/2}} \sum_{m=0}^k (-1)^{k-m} {k \choose m}
\phi_s(i)^{k-m} \sum_{r=0}^n \frac{\phi_r(i) \phi_r(t)}{(v_r)^2}\\ & &
\cdot \sum_{j=0}^n \frac{\mu_j}{|X|} \phi_s(j)^m \phi_r(j)\\ & = &
\frac{1}{(v_s)^{k/2}} \sum_{m=0}^k (-1)^{k-m} {k \choose m}
\phi_s(i)^{k-m} (v_s)^m \sum_{r=0}^n \frac{\phi_r(i) \phi_r(t)
p_m(r)}{(v_r)^2}, \end{eqnarray*} where the last equality is Lemma
\ref{ascountsol}. Consequently, \begin{eqnarray*} \ee((W'-W)^k) & = &
\ee (\ee((W'-W)^k|i))\\ & = & (v_s)^{k/2} \sum_{m=0}^k (-1)^{k-m} {k
\choose m}\\ & & \cdot \sum_{r=0}^n \frac{\phi_r(t)}{(v_r)^2} p_m(r)
\sum_{i=0}^n \frac{\mu_i}{|X|} \frac{\phi_s(i)^{k-m}
\phi_r(i)}{(v_s)^{k-m}}. \end{eqnarray*} The first assertion now
follows from Lemma \ref{ascountsol}.

	For the second part, the first assertion gives that \[
\ee(W'-W)^4 = (v_s)^2 \sum_{m=0}^4 (-1)^{m} {4 \choose m} \sum_{r=0}^n
\frac{\phi_r(t)}{v_r} \frac{p_m(r) p_{4-m}(r)}{v_r}.\]
By page 654 of \cite{MS}, $\phi_r(0)=v_r$ for all $r$. Thus
specializing to $t=0$ shows that \[ 0 = (v_s)^2 \sum_{m=0}^4 (-1)^{m}
{4 \choose m} \sum_{r=0}^n \frac{p_m(r) p_{4-m}(r)}{v_r}.\] So for
general $t$, one has that \[ \ee(W'-W)^4 = -(v_s)^2 \sum_{m=0}^4
(-1)^{m} {4 \choose m} \sum_{r=0}^n \left( 1 -\frac{\phi_r(t)}{v_r}
\right) \frac{p_m(r) p_{4-m}(r)}{v_r}.\] The contribution from the
$m=0,4$ terms is 0, since $p_0(r) =0$ if $r \neq 0$. The contribution
from the $m=2$ term is \[ - 6 (v_s)^2 \sum_{r=0}^n \left(1 -
\frac{\phi_r(t)}{v_r} \right) \frac{p_2(r)^2}{v_r}.\] The $m=1,3$
terms are equal and together contribute \begin{eqnarray*} 8 (v_s)^2
\sum_{r=0}^n \left( 1 - \frac{\phi_r(t)}{v_r} \right) \frac{p_1(r)
p_3(r)}{v_r} & = & 8 (v_s)^2 \left( 1 - \frac{\phi_s(t)}{v_s} \right)
\frac{p_3(s)}{v_s}\\ & = & 8 (v_s)^2 \left(1 - \frac{\phi_s(t)}{v_s}
\right) \sum_{r=0}^n \frac{p_2(r)^2}{v_r}, \end{eqnarray*} where the
final equality is part 2 of Lemma \ref{asrel}. Adding the terms
completes the proof of the second assertion. \end{proof}

	Arguing as in the proof of Theorem \ref{main1}, and using the
	above lemmas, one obtains the following result.

\begin{theorem} \label{asmains} Fix $s \in \{0,\cdots,n\}$, and let $W = \frac{\phi_s(i)}{\sqrt{v_s}}$ where $i$ is chosen from the Plancherel measure of the association scheme. Fix $t \in \{1, \cdots, n\}$. Then for all real $x_0$,
\begin{eqnarray*}
& & \left| \pp(W \leq x_0) - \frac{1}{\sqrt{2 \pi}}
\int_{-\infty}^{x_0} e^{-\frac{x^2}{2}} dx \right|\\ & \leq &
\frac{v_s}{a} \sqrt{ \sum_{r=1}^n \frac{p_2(r)^2}{v_r} \left(
\frac{\phi_r(t)}{v_r}+1 - \frac{2 \phi_s(t)}{v_s} \right)^2}\\
 & & +
\frac{\sqrt{v_s}}{(\pi)^{1/4}} \left[ \sum_{r=0}^n \left( 8
-\frac{6}{a} \left(1-\frac{\phi_r(t)}{v_r} \right) \right)
\frac{p_2(r)^2}{v_r} \right]^{1/4}, \end{eqnarray*} where $a=1
-\frac{\phi_s(t)}{v_s}$.
\end{theorem}
