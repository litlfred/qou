---
doc_id: arxiv-math-0508291v1
doc_title: "Stein’s Method and Random Character Ratios Running head: Stein’s Method and Random Character Ratios Version of 8/13/05"
section_id: sec-018-63-example-hamming-scheme
section_title: "Example: Hamming Scheme"
section_number: 6.3
pages: 49-50
source_pdf: 0508291v1.pdf
source_sha256: d2d541426aaec742
toc_source: outline
text_source: latex
latex_prose_ratio: 0.957
latex_coverage_ratio: 0.985
doc_brief: "Stein’s Method and Random Character Ratios Running head: Stein’s Method and Random Character Ratios Version of 8/13/05 — Stein’s method is used to prove limit theorems for random character ratios."
---
\label{Hamming}

	This subsection illustrates the theory of Subsection
	\ref{assocCLT} for the Hamming scheme $H(d,q)$, where $d,q$
	are positive integers and $q \geq 2$.

	To begin we recall the definition of $H(d,q)$ and its basic
	properties, referring the reader to Chapter 3 of \cite{BI} for
	more details. The elements $X$ of $H(d,q)$ are d-tuples of
	numbers chosen from $\{1,\cdots,q\}$; clearly $|X|=q^d$. A
	pair $(x,y)$ is in $R_i$ if $x$ and $y$ differ in exactly i
	coordinates. For $0 \leq i \leq d$, one has that $v_i=(q-1)^i
	{d \choose i}$ and $\mu_i=(q-1)^i {d \choose i}$. Thus the
	Plancherel measure on $\{0,\cdots, d\}$ chooses $i$ with
	probability $\frac{(q-1)^i {d \choose i}}{q^d}$. The numbers
	$\phi_s(i)$ are equal to \[ \sum_{j=0}^s (-1)^j (q-1)^{s-j} {i
	\choose j} {d-i \choose s-j}.\] The polynomial $\phi_s$ in the
	variable $i$ is known as a q-Krawtchouk polynomial.

	In what follows $W=\frac{\phi_1(i)}{\sqrt{v_1}}$, where $i$ is
 chosen from Plancherel measure of the Hamming scheme $H(d,q)$. The
 Hamming graph has vertex set $X$ and an edge between two vertices if
 they differ in one coordinate. Thus the eigenvalues of the adjacency
 matrix of the Hamming graph are $\phi_1(i)$ with multiplicity
 $\mu_i$, which motivates the study of $W$. Hora \cite{Ho2} shows
 that if $d \rightarrow \infty$ and $q/d \rightarrow 0$, then $W$
 converges in distribution to a normal random variable with mean 0 and
 variance 1.
	
	In fact since $W(i)=\frac{(q-1)d-qi}{\sqrt{(q-1)d}}$ and
	$\frac{\mu_i}{|X|} = \frac{(q-1)^i {d \choose i}}{q^d}$, it is straightforward
	that $W$ has the same distribution as \[
	\frac{Y_1+\cdots+Y_d}{\sqrt{(q-1)d}}, \] where the $Y$'s are
	independent random variables, each equal to $q-1$ with
	probability $\frac{1}{q}$ and to $-1$ with probability $1-\frac{1}{q}$. Hence
	the Berry-Esseen theorem \cite{Du} shows that $W$ satisfies a
	central limit theorem with the error term $C
	\sqrt{\frac{q}{d}}$ where $C$ is a small explicit constant.

	For comparison, let us study $W$ using Theorem \ref{asmains}
	with $s=1$ and $t=1$. Then $a=\frac{q}{(q-1)d}$ and one
	computes that $p_2(0)=\frac{1}{(q-1)d}$, $p_2(1) =
	\frac{(q-2)}{(q-1)d}$, and $p_2(2)=1-\frac{1}{d}$. The first
	term in the error term of Theorem \ref{asmains} is then
	computed to equal $\sqrt{\frac{(q-2)^2}{(q-1)d}}$, which is
	less than $\sqrt{\frac{q}{d}}$. The second term in the error
	term of Theorem \ref{asmains} is computed to equal $\left(
	\frac{2q^2}{\pi (q-1)d} \right)^{1/4}$, which is at most
	$\left( \frac{2q}{d} \right)^{1/4}$. Thus one obtains a
	central limit theorem for $W$ with error term
	$\sqrt{\frac{q}{d}} +\left( \frac{2q}{d} \right)^{1/4}$.

	To close this section, it is shown how our exchangeable pair
	can be used to give $O(d^{-1/2})$ bounds for $q$ fixed. The
	key is Lemma \ref{bdeath}, which shows that the Markov chain
	$L_1$ is actually a birth-chain and computes its transition
	probabilities.

\begin{lemma} \label{bdeath} The Markov chain $L_1$ on the set $\{0,\cdots,d\}$ is a birth-death chain with transition probabilities \[ L_1(i,j) = \left\{ \begin{array}{ll} 
\frac{i}{d(q-1)} & \mbox{if $j=i-1$}\\
\frac{i}{d} \left(1-\frac{1}{q-1} \right) & \mbox{if $j=i$}\\
1-\frac{i}{d} & \mbox{if $j=i+1$} \end{array} \right. \]
\end{lemma}	

\begin{proof} Recall that $L_1(i,j) = \frac{\mu_j}{|X|} \sum_{r=0}^n \frac{\phi_r(i) \phi_r(1) \phi_r(j)}{(v_r)^2}$. From the formula for $\phi_r(l)$ one sees that \[ \phi_r(l) =  (q-1)^{r-l} \frac{{d \choose r}}{{d \choose l}} \phi_l(r)  \] for any $0 \leq r,l \leq d$. Thus \[ L_1(i,j) = \frac{\mu_j}{|X| d {d \choose i} {d \choose j} (q-1)^{i+j+1}} \sum_{r=0}^n {d \choose r} (q-1)^r \phi_1(r) \phi_i(r) \phi_j(r).\] From page 152 of \cite{MS}, there is a recurrence relation \[
	(i+1) \phi_{i+1}(r) = [(d-i)(q-1)+i-qr] \phi_i(r) -
	(q-1)(d-i+1) \phi_{i-1}(r) .\] Since $\phi_1(r)= d(q-1)-qr$,
	the recurrence is equivalent to \[ \phi_1(r) \phi_i(r) =
	i(q-2) \phi_i(r) + (i+1) \phi_{i+1}(r) + (q-1)(d-i+1)
	\phi_{i-1}(r).\] Applying this to expression for $L_1(i,j)$ at
	the end of the previous paragraph, the result follows from
	Lemma \ref{asorthog2}. \end{proof}

	Lemma \ref{bdeath} implies that $|W'-W| \leq A$ with
$A=\frac{q}{\sqrt{(q-1)d}}$. Thus one can apply the version of Theorem
\ref{asmains} which would arise by using Theorem \ref{rinrot} instead
of Theorem \ref{steinbound}. Recalling that $a=\frac{q}{(q-1)d}$, one
obtains an error term of $\sqrt{\frac{q}{d}} + \frac{.41q^2 + 1.5
q}{\sqrt{(q-1)d}}$. For $q$ fixed this goes as $d^{-1/2}$.
