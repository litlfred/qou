---
doc_id: arxiv-math-0508291v1
doc_title: "Stein’s Method and Random Character Ratios Running head: Stein’s Method and Random Character Ratios Version of 8/13/05"
section_id: sec-009-43-example-the-hypercube
section_title: "Example: The Hypercube"
section_number: 4.3
pages: 23-25
source_pdf: 0508291v1.pdf
source_sha256: d2d541426aaec742
toc_source: outline
text_source: latex
latex_prose_ratio: 0.948
latex_coverage_ratio: 0.993
doc_brief: "Stein’s Method and Random Character Ratios Running head: Stein’s Method and Random Character Ratios Version of 8/13/05 — Stein’s method is used to prove limit theorems for random character ratios."
---
\label{hypercube}

	The $n$ dimensional hypercube $\zz_2^n$ consists of $n$-tuples
        of 0's and 1's. Random walk on it proceeds by picking a random
        coordinate and changing it. The spectrum of this random walk
        is well known; for each $0 \leq i \leq n$ there is an
        eigenvalue $1-\frac{2i}{n}$ occurring with multiplicity ${n
        \choose i}$ (see for instance page 28 of \cite{Di}). Thus by
        the usual central limit theorem for the binomial distribution, the
        spectrum of the hypercube is asymptotically normal with an
        error term $O(n^{-1/2})$. The purpose of this subsection is to
        revisit this classical result from the viewpoint of Gelfand
        pairs, illustrating the construction of Subsection
        \ref{gelfandCLT}.

	To begin, note from the remarks on page 58 of \cite{Di}, that
        the hypercube can be viewed as $G/K$ for a certain Gelfand
        pair $(G,K)$. Namely $G$ is the semidirect product of $\zz_2^n$
        with $S_n$, where the group multiplication is
        $(x,\pi)(y,\tau)=(x+\pi(y),\pi \tau)$, where $\tau(x)$
        permutes the coordinates of $x$. $K$ is the subgroup
        $\{(0,\pi):\pi \in S_n \}$. The induced module $1_K^G$
        decomposes as $\oplus_{r=0}^n V_r$ where $d_r={n \choose
        r}$. Thus the Plancherel measure chooses $i \in
        \{0,\cdots,n\}$ with probability $\frac{{n \choose
        i}}{2^n}$. For $0 \leq r \leq n$, the double coset $K_r$ in
        $G$ consists of elements $(x,\pi)$ where $x$ has r coordinates
        equal to 1. Thus $|K_r| = {n \choose r} n!$, and as usual let
        $g_r$ denote some element of $K_r$. The spherical
        function $\omega_i$ ($0 \leq i \leq n$) is given by \[
        \omega_i(g_r) = \frac{1}{{n \choose i}} \sum_{m=0}^i (-1)^m {r
        \choose m} {n-r \choose i-m},\] which is a Krawtchouk
        polynomial if one overlooks the ${n \choose i}$ in the
        denominator.

	The following result emerges from Theorem \ref{main2}. Since
	$\omega_i(g_1)=1-\frac{2i}{n}$ (or by Lemma
	\ref{specgelfand}), it can be seen as a central limit theorem
	for the spectrum of random walk on the hypercube.

\begin{theorem} \label{hypbound1} Let $W=\sqrt{n}
 \omega_i(g_1)$ where $i$ is chosen from Plancherel measure. Then for
 all real $x_0$, \[ \left| \pp(W \leq x_0) - \frac{1}{\sqrt{2 \pi}}
 \int_{-\infty}^{x_0} e^{-\frac{x^2}{2}} dx \right| \leq \left(
 \frac{8}{\pi n} \right)^{1/4} .\] \end{theorem}

\begin{proof} Apply
 Theorem \ref{main2} with $u=1$ and $t=1$. Then $a=\frac{2}{n}$. One
 computes that $p_2(K_0)=\frac{1}{n}$, $p_2(K_2)=1-\frac{1}{n}$, and
 that $p_2(K_r)=0$ for all $r \neq 0,2$. Since
 $\omega_1(g_2)=1-\frac{4}{n}$, one has that
 $\omega_1(g_2)+2a-1=0$. Thus the first error term in Theorem
 \ref{main2} is 0. The second error term in Theorem \ref{main2} is
 computed to be $\left( \frac{8}{\pi n} \right)^{1/4}$, implying the
 result. \end{proof}

	To get $O(n^{-1/2})$ bounds by Stein's method, it will be
	shown that $|W'-W|$ is bounded, so that one can use the
	version of Stein's method in Theorem \ref{rinrot} instead of
	that in Theorem \ref{steinbound}. The boundedness of $|W'-W|$
	will follow from Lemma \ref{birth}, which proves that $L_1$ is
	in fact a birth-death chain.

\begin{lemma} \label{birth} The chain $L_1$ on the set $\{0,\cdots,n\}$ is a birth-death chain with transition probabilities \[ L_1(i,j) = \left\{ \begin{array}{ll} \frac{i}{n} & \mbox{if $j=i-1$}\\
1-\frac{i}{n} & \mbox{if $j=i+1$} \end{array} \right.\] \end{lemma}

\begin{proof} From the three term recurrence for Krawtchouk polynomials on page 152 of \cite{MS}, it follows that
\[ (i+1){n \choose i+1} \omega_{i+1}(g_r) = (n-2r) {n \choose i}  \omega_i(g_r)- (n-i+1) {n \choose i-1}  \omega_{i-1}(g_r).\] Since $n-2r = n \omega_1(g_r)$, one obtains that \[ n {n \choose i} \omega_1(g_r) \omega_i(g_r) = (i+1) {n \choose
 i+1} \omega_{i+1}(g_r) + (n-i+1) {n \choose i-1} \omega_{i-1}(g_r).\]
 Simplifying one obtains the relation
\[ \omega_1(g_r) \omega_i(g_r) = \left( 1- \frac{i}{n} \right) \omega_{i+1}(g_r) + \left( \frac{i}{n} \right) \omega_{i-1}(g_r).\] The result now follows from Lemma \ref{orthog1} and the definition of $L_1$. \end{proof}

	Now an $O(n^{-1/2})$ error term is established.

\begin{theorem}
 \label{hypbound2} Let $W=\sqrt{n} \omega_i(g_1)$ where $i$ is chosen
 from Plancherel measure. Then for
 all real $x_0$, \[ \left| \pp(W \leq x_0) - \frac{1}{\sqrt{2 \pi}}
 \int_{-\infty}^{x_0} e^{-\frac{x^2}{2}} dx \right| \leq 5 n^{-1/2}
 .\] \end{theorem}

\begin{proof} Apply the variation of Theorem \ref{main2} which would arise from using Theorem \ref{rinrot}
 instead of Theorem \ref{steinbound}. Recall that
 $a=\frac{2}{n}$. Also $|W'-W| \leq A$ with $A=\frac{2}{\sqrt{n}}$
 since $L_1$ is a birth-death chain. As explained in the proof of
 Theorem \ref{hypbound1}, $Var(\ee[(W'-W)^2|W])=0$. The result
 follows. \end{proof}

	A a final remark, Lemma \ref{birth} shows that $L_1$ is
closely related to the birth-death chain used by Stein \cite{Stn} in
proving a central limit theorem for $X_1+...+X_n$, where the $X's$ are
independent and each equal to 0 or 1 with probability 1/2. To form an
exchangeable pair Stein chose a random $l \in \{1,\cdots,n\}$ and then
replaced $X_l$ by a new random variable which is also 0 or 1 with
probability 1/2 and independent of all of the $X's$. The chain $L_1$
would arise by picking a random index $l$ and switching the value of
$X_l$.
