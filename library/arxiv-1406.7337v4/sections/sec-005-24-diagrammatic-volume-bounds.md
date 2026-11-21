---
doc_id: arxiv-1406.7337v4
doc_title: "Semi-Adequate Closed Braids and Volume"
section_id: sec-005-24-diagrammatic-volume-bounds
section_title: "Diagrammatic volume bounds"
section_number: 2.4
pages: 9-11
source_pdf: 1406.7337v4.pdf
source_sha256: 5bae8237742733b9
toc_source: outline
text_source: latex
latex_prose_ratio: 0.966
latex_coverage_ratio: 1.0
doc_brief: "Semi-Adequate Closed Braids and Volume — In this paper, we show that the volumes for a family of A-adequate closed braids can be bounded above and below in terms of the twist number, the number of"
---
In this section, we apply Lemma~\ref{setup} and Theorem~\ref{Cor} to produce diagrammatic volume bounds for the complements of the closed $n$-braids considered in this paper. We now begin with a lemma for the case of 3-braids. 









\begin{lemma} Let $D(K)=\widehat{\beta}$ denote the closure of a nice 3-braid $\beta \in B_{3}$. Furthermore, assume that the positive syllables of $\beta$ are cyclically neighbored on both sides by negative syllables. Then the all-A state $H_{A}$ of $D(K)$ satisfies precisely one of the following conditions:
\label{mylemma2}
\begin{enumerate}
\item[(1)] $H_{A}$ contains exactly one nonwandering circle and no wandering circles.
\item[(2)] $H_{A}$ contains exactly one wandering circle and no nonwandering circles. 
\end{enumerate}
\end{lemma}

\begin{proof} A 3-braid $\beta \in B_{3}$ is either alternating or nonalternating. 

\bigskip

\noindent \underline{Case 1}: Suppose $\beta$ is alternating. Then one of the braid generators must always occur with positive exponents and the other generator must always occur with negative exponents. Hence, by the proof of Sublemma~\ref{sublemma1}, since a generator occurs with only positive exponents, then there will be a nonwandering circle. Since only one generator occurs with only positive exponents, then there is only one such nonwandering circle. Also, since adjacent negative syllables cannot occur in $\beta$, then wandering circles cannot occur in $H_{A}$. 

\bigskip

\noindent \underline{Case 2}: Suppose $\beta$ is nonalternating. Since positive syllables are cyclically neighbored on both sides by negative syllables, then the nonalternating behavior of $\beta$ must come from a pair of adjacent negative syllables. Hence, by the proof of Sublemma~\ref{sublemma1}, this implies the existence of a wandering circle in $H_{A}$ and prevents the existence of a nonwandering circle (since both generators occur once with negative exponent). Finally, since a wandering circle (which is always essential in the case that $n=3$) ``uses up'' a braid string from the braid closure and since a wandering circle must wander from braid string position 1 to braid string position 3 and back before closing up, then the existence of a second such wandering circle is impossible. 

\end{proof}

\begin{definition}
Let $D(K)=\widehat{\beta}$ be the closure of an $n$-braid $\beta \in B_{n}$. With the sign conventions for braid generators given in Figure~\ref{braidgen}, we call a twist region \emph{positive} if its crossings correspond to a positive syllable in the braid word $\beta$ and \emph{negative} if its crossings correspond to a negative syllable in the braid word $\beta$. Let $t^{+}(D)$ denote the number of positive twist regions in $D(K)$ and let $t^{-}(D)$ denote the number of negative twist regions in $D(K)$.
\end{definition}

The following theorem, which is the first main result of this paper, is a more precise version of Theorem~\ref{introthm} from the introduction. 

\begin{theorem} \label{mytheorem} Let $D(K)=\widehat{\beta}$, where $\beta \in B_{n}$ satisfies the assumptions of Lemma~\ref{setup}. Let $m$ denote the number of non-essential wandering circles in the all-A state $H_{A}$ of $D(K)$. In the case that $n=3$, we have that
$$-\chi(\mathbb{G}_{A}')=t^{-}(D)-1 \geq \frac{1}{2}\cdot (t(D)-2),$$
\noindent which gives the volume bounds
$$\frac{v_{8}}{2}\cdot(t(D)-2) \leq v_{8}\cdot(t^{-}(D)-1) \leq \mathrm{vol}(S^{3}\backslash K) < 10v_{3}\cdot(t(D)-1).$$
In the case that $n\geq4$ and that the only positive syllables of $\beta$ possibly occur in the generators $\sigma_{1}$ and $\sigma_{n-1}$, we have the volume bounds
$$\frac{v_{8}}{2}\cdot(t(D)-2(n+m-2)) \leq v_{8}\cdot(t^{-}(D)-(n+m-2)) \leq \mathrm{vol}(S^{3}\backslash K) < 10v_{3}\cdot(t(D)-1).$$
In the case that $n\geq4$ and that positive syllables of $\beta$ occur in a generator $\sigma_{i}$ for some $2 \leq i \leq n-2$, we have the volume bounds
$$v_{8}\cdot(t^{-}(D)-t^{+}(D)-(n+m-2)) \leq \mathrm{vol}(S^{3}\backslash K) < 10v_{3}\cdot(t(D)-1) = 10v_{3}\cdot(t^{-}(D)+t^{+}(D)-1).$$
\end{theorem}

It is worth noting that the lower bounds on volume in terms of $t(D)$ given above are sharper than the general lower bounds given in the Main Theorem (Theorem 1.1) of \cite{Me} when $t(D)$ is large compared to the sum $n+m$. Specifically, the lower bounds are sharper when $t(D)>4$ for the case when $n=3$ (in which $m=0$ and $t(D) \geq 4=2(n-1)$) and when $t(D)>6(n+m)-16$ for the case when $n \geq 4$.  

\begin{proof}[Proof of Theorem~\ref{mytheorem}] To begin, note that we may apply the many results of Lemma~\ref{setup}. Since $D(K)$ is connected, A-adequate, and satisfies the TELC, then Lemma~3.4 of \cite{Me} implies that $$-\chi(\mathbb{G}_{A}')=t(D)-\#\left\{\text{OCs}\right\},$$ where $\#\left\{\text{OCs}\right\}$ is the number of all-A circles in $H_{A}$, called \emph{other circles}, that are not small inner circles. Note that, by Sublemma~\ref{sublemma1}, the set of other circles consists of the medium inner circles, essential wandering circles, non-essential wandering circles, and nonwandering circles in $H_{A}$. By Remark~\ref{cond} and Figure~\ref{loop}, it can be seen that $$t^{+}(D) \leq \#\left\{\text{medium\ inner\ circles}\right\} \leq 2t^{+}(D),$$ which says that each positive twist region corresponds to either one or two medium inner circles. In particular, looking at the left side (up to reflection) of Figure~\ref{loop}, it can be seen that $$\#\left\{\text{medium\ inner\ circles}\right\} = t^{+}(D)$$ in the case that $n=3$ and in the case that $n \geq 4$ when the only positive syllables of $\beta$ possibly occur in the generators $\sigma_{1}$ and $\sigma_{n-1}$. Additionally, Condition (2a), Condition (2b), and Condition (2c) of Lemma~\ref{setup} imply that at least half of the twist regions in $D(K)$ must be negative twist regions. 

\bigskip

\noindent \underline{Case 1}: Suppose $n=3$. By Lemma~\ref{mylemma2}, we know that the total number of wandering circles and nonwandering circles is one. Therefore, using all of what was said above, we get
\begin{eqnarray*}-\chi(\mathbb{G}_{A}') & = & t(D)-\#\left\{\text{OCs}\right\}\\
\ & = & t(D)-\#\left\{\text{medium\ inner\ circles}\right\}-\#\left\{\text{wandering\ circles}\right\}\\
\ & \ & \hspace{2in} -\#\left\{\text{nonwandering\ circles}\right\}\\
\ & = & t(D)-t^{+}(D)-1\\
\ & = & t^{-}(D)-1\\
\ & \geq & \frac{t(D)}{2}-1\\
\ & = & \frac{1}{2}\cdot (t(D)-2).
\end{eqnarray*} 

\noindent \underline{Case 2}:  Suppose $n\geq4$. Note that both essential wandering circles and nonwandering circles ``use up'' a braid string from the braid closure. Also, note that Lemma~\ref{setup} implies that there can be at most two nonwandering circles in the all-A state $H_{A}$. These two facts imply that

\begin{equation}\label{EWC}
\#\left\{\text{essential\ wandering\ circles}\right\}+\#\left\{\text{nonwandering\ circles}\right\} \leq n-2.
\end{equation}

\bigskip

\noindent \underline{Subcase 1}: Suppose that the only positive syllables of $\beta$ possibly occur in the generators $\sigma_{1}$ and $\sigma_{n-1}$, in which case we have that $\#\left\{\text{medium\ inner\ circles}\right\} = t^{+}(D)$. Then, by using Inequality~\ref{EWC} and what was said in the beginning of the proof, we get
\begin{eqnarray*}-\chi(\mathbb{G}_{A}') & = & t(D)-\#\left\{\text{OCs}\right\}\\
\ & = & t(D)-\#\left\{\text{medium\ inner\ circles}\right\}-\#\left\{\text{non-essential\ wandering\ circles}\right\}\\
\ & \ & \hspace{.318in} -\#\left\{\text{essential\ wandering\ circles}\right\}-\#\left\{\text{nonwandering\ circles}\right\}\\
\ & \geq & t(D)-t^{+}(D)-m-(n-2)\\
\ & = & t^{-}(D)-(n+m-2)\\
\ & \geq & \frac{t(D)}{2}-(n+m-2)\\
\ & = & \frac{1}{2}\cdot (t(D)-2(n+m-2)).
\end{eqnarray*}

\noindent \underline{Subcase 2}: Suppose that positive syllables of $\beta$ occur in a generator $\sigma_{i}$ for some $2 \leq i \leq n-2$, in which case we have that $\#\left\{\text{medium\ inner\ circles}\right\} \leq 2t^{+}(D)$. Then, by using Inequality~\ref{EWC} and what was said in the beginning of the proof, we get
\begin{eqnarray*}-\chi(\mathbb{G}_{A}') & = & t(D)-\#\left\{\text{OCs}\right\}\\
\ & = & t(D)-\#\left\{\text{medium\ inner\ circles}\right\}-\#\left\{\text{non-essential\ wandering\ circles}\right\}\\
\ & \ & \hspace{.318in} -\#\left\{\text{essential\ wandering\ circles}\right\}-\#\left\{\text{nonwandering\ circles}\right\}\\
\ & \geq & t(D)-2t^{+}(D)-m-(n-2)\\
\ & = & t^{-}(D)-t^{+}(D)-(n+m-2).\\
\end{eqnarray*}

\noindent By applying the inequalities for $-\chi(\mathbb{G}_{A}')$ above to Theorem~\ref{Cor}, we get the desired volume bounds.

\end{proof}
