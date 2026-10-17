---
doc_id: arxiv-1406.7337v4
doc_title: "Semi-Adequate Closed Braids and Volume"
section_id: sec-004-23-a-lemma-for-closed-braids
section_title: "A lemma for closed braids"
section_number: 2.3
pages: 5-9
source_pdf: 1406.7337v4.pdf
source_sha256: 5bae8237742733b9
toc_source: outline
text_source: latex
latex_prose_ratio: 0.972
latex_coverage_ratio: 0.996
doc_brief: "Semi-Adequate Closed Braids and Volume — In this paper, we show that the volumes for a family of A-adequate closed braids can be bounded above and below in terms of the twist number, the number of"
---
The main goal of this section is to produce a family of closed $n$-braids that satisfies the hypotheses of Theorem~\ref{Cor}. We will work within this family of braids throughout the rest of this paper. We begin with necessary definitions.  

\begin{definition}
Call two induced subwords $\gamma_{1}$ and $\gamma_{2}$ of a braid word $\beta \in B_{n}$ \emph{disjoint} if the subwords share no common letters when they are viewed as part of $\beta$. As an example, given the braid word
$$\beta=\sigma_{1}^{3}\sigma_{2}^{-3}\sigma_{1}^{2}\sigma_{3}^{-2}\sigma_{2}\sigma_{3}=\sigma_{1}^{2}(\sigma_{1}\sigma_{2}^{-3}\sigma_{1})\sigma_{1}(\sigma_{3}^{-2}\sigma_{2})\sigma_{3},$$ 
\noindent the subwords $\gamma_{1}=\sigma_{1}\sigma_{2}^{-3}\sigma_{1}$ and $\gamma_{2}=\sigma_{3}^{-2}\sigma_{2}$ are disjoint induced subwords of $\beta$. 
\end{definition}

\begin{definition}
Call a subword $\gamma$ of a braid word $\beta \in B_{n}$ \emph{complete} if it contains, at some point, each of the generators $\sigma_{1}, \ldots, \sigma_{n-1}$ of $B_{n}$. It is important to note that the generators $\sigma_{1}, \ldots, \sigma_{n-1}$ need not occur in any particular order and that repetition of some or all of these generators is allowed.
\end{definition}

Because the majority of the braids considered in this paper will satisfy the same set of assumptions, we make the following definition. 

\begin{definition}
Call a braid $\beta \in B_{n}$ \emph{nice} if $\beta$ is cyclically reduced into syllables and $\beta$ contains two disjoint induced complete subwords.
\end{definition}

Note that, in the case when $n=3$, the condition that the 3-braid $\beta=\sigma_{i}^{r_{1}}\sigma_{j}^{r_{2}}\cdots\sigma_{i}^{r_{2l-1}}\sigma_{j}^{r_{2l}} \in B_{3}$ is nice is equivalent to the condition that $\sigma_{1}$ and $\sigma_{2}$ each occur at least twice nontrivially in the braid word $\beta$ (which is equivalent to the condition that $l \geq 2$). 

We now define, in the following Main Lemma, the family of closed $n$-braids that we will consider for the remainder of this paper. 

\begin{lemma}[The Main Lemma] 
\label{setup}
Let $D(K)=\widehat{\beta}$ denote the closure of a nice $n$-braid $\beta=\sigma_{m_{1}}^{r_{1}}\cdots\sigma_{m_{l}}^{r_{l}} \in B_{n}$. View $D(K)$ as lying in an annular region of the plane and assume that $\beta$ satisfies the conditions
\begin{enumerate}   
\item[(1)] all negative exponents $r_{i}<0$ in $\beta$ satisfy the stronger requirement that $r_{i}\leq-3$;
\item[(2a)] when $r_{i}>0$ and $m_{i}=1$, we have that $r_{i-1} \leq -3$, that $r_{i+1} \leq -3$, and that $m_{i-1}=m_{i+1}=2$; 
\item[(2b)] when $r_{i}>0$ and $2 \leq m_{i} \leq n-2$, we have that $r_{i-2} \leq -3$, that $r_{i-1} \leq -3$, that $r_{i+1} \leq -3$, that $r_{i+2} \leq -3$, and that $\{m_{i-2}, m_{i-1}\}=\{m_{i+1}, m_{i+2}\}=\{m_{i}-1, m_{i}+1\}$; and
\item[(2c)] when $r_{i}>0$ and $m_{i}=n-1$, we have that $r_{i-1} \leq -3$, that $r_{i+1} \leq -3$, and that $m_{i-1}=m_{i+1}=n-2$. 
\end{enumerate}
Then we may categorize the all-A circles of $H_{A}$ into the following types:
\begin{itemize}
\item \emph{small inner circles} that arise from negative exponents $r_{i}\leq-3$ in the braid word $\beta$
\item \emph{medium inner circles} that arise from cyclically isolated positive syllables in the braid word $\beta$ 
\item \emph{essential wandering circles} that are essential in the annulus and have wandering that arises from adjacent negative syllables in adjacent generators in the braid word $\beta$ 
\item \emph{non-essential wandering circles} that are non-essential (contractible) in the annulus and have wandering that arises from adjacent negative syllables in adjacent generators in the braid word $\beta$  
\item \emph{nonwandering circles} that arise from the case when all syllables in the generator $\sigma_{1}$ are positive or the case when all syllables in the generator $\sigma_{n-1}$ are positive.
\end{itemize}
\noindent Furthermore, we have that $K$ is a hyperbolic link and that $D(K)$ is a connected, prime, A-adequate link diagram that satisfies the TELC and contains $t(D)~\geq~2(n-1)$ twist regions.    
\end{lemma}

\begin{remark} \label{cond}
Condition~(2a) of the above theorem requires that positive syllables in the generator $\sigma_{1}$ are cyclically neighbored on both sides by negative syllables in the generator $\sigma_{2}$. Similarly, Condition~(2c) of the above theorem requires that positive syllables in the generator $\sigma_{n-1}$ are cyclically neighbored on both sides by negative syllables in the generator $\sigma_{n-2}$. Condition~(2b) of the above theorem requires that positive syllables in the generator $\sigma_{i}$, where $2 \leq i \leq n-2$, are cyclically neighbored on both sides by a pair of negative syllables in the far commuting generators $\sigma_{i-1}$ and $\sigma_{i+1}$.
\end{remark}

Note that Condition~(2a), Condition~(2b), and Condition~(2c) are in a spirit similar to the condition that positive syllables are cyclically neighbored on both sides by negative syllables in Stoimenow's classification of A-adequate closed 3-braid diagrams (Proposition~\ref{adeq3braid}). 

\begin{figure}
	\centering
		\includegraphics[width=3in]{loopb.pdf}
	\caption{An example of an isolated positive syllable $\sigma_{1}^{r_{i}}$ corresponding to a single medium inner circle (left), an example of an isolated positive syllable $\sigma_{m_{i}}^{r_{i}}$, where $2 \leq m_{i} \leq n-2$, corresponding to two medium inner circles (center), and an example of a wandering circle portion coming from a negative subword $\sigma_{m_{i}}^{r_{i}}\sigma_{m_{i+1}}^{r_{i+1}}=\sigma_{{m_i}}^{r_{i}+1}(\sigma_{m_{i}}^{-1}\sigma_{m_{i+1}}^{-1})\sigma_{m_{i+1}}^{r_{i+1}+1}$ (right).}
	\label{loop}
\end{figure}

We will prove Lemma~\ref{setup} through a series of sublemmas. 

\begin{sublemma} \label{sublemma1} Let $D(K)=\widehat{\beta}$ satisfy the assumptions of Lemma~\ref{setup}. Then, as described in the statement of Lemma~\ref{setup}, we may categorize the all-A circles of $H_{A}$ into small inner circles, medium inner circles, essential wandering circles, non-essential wandering circles, and nonwandering circles.  
\end{sublemma}

\begin{proof} First, note that Condition (2a), Condition (2b), and Condition (2c) of Lemma~\ref{setup} imply that $\beta$ cannot be positive. Because positive syllables of $\beta$ are cyclically neighbored by negative syllables, we may decompose $\beta$ as $\beta=N_{1}$ (in the case that $\beta$ is a negative braid) or as $\beta=P_{1}N_{1} \cdots P_{t}N_{t}$, where $P_{i}$ denotes a positive syllable of $\beta$ and $N_{i}$ denotes a maximal length negative induced subword of $\beta$. 

\bigskip

\noindent \underline{Small Inner Circles}: Let $\sigma_{m_{i}}^{r_{i}}$, where $r_{i} \leq -3$, denote a negative syllable. Then, except for the additional $n-2$ surrounding vertical line segments, the A-resolution of this syllable will look like the left side of Figure~\ref{longshort}. In particular, having $r_{i} \leq -3$ implies the existence of at least two small inner circles. 

\bigskip

\noindent \underline{Wandering Circles}: Let $\sigma_{m_{i}}^{r_{i}}\sigma_{m_{i+1}}^{r_{i+1}}=\sigma_{{m_i}}^{r_{i}+1}(\sigma_{m_{i}}^{-1}\sigma_{m_{i+1}}^{-1})\sigma_{m_{i+1}}^{r_{i+1}+1}$, where $r_{i} \leq -3$ and $r_{i+1} \leq -3$, denote a pair of adjacent negative syllables.

\bigskip

\underline{Case 1}: Suppose $m_{i+1}=m_{i}-1$ or $m_{i+1}=m_{i}+1$. Then the pair of adjacent negative syllables involve adjacent generators of $B_{n}$. Consequently, the corresponding portion of $H_{A}$ will resemble (up to reflection and except for the additional surrounding vertical line segments) the right side of Figure~\ref{loop}. The key feature of this figure is the fact that we see a portion of a wandering circle, where the wandering behavior corresponds to the existence of the $\sigma_{m_{i}}^{-1}\sigma_{m_{i+1}}^{-1}$ induced subword. 

\bigskip

\underline{Case 2}: Suppose $\left|m_{i+1}-m_{i}\right| \geq 2$. In this case, the pair of adjacent negative syllables involve far commuting generators of $B_{n}$. Then, except for the additional $n-4$ surrounding vertical line segments, we get that the A-resolution will look like two copies of the left side of Figure~\ref{longshort}. Thus, we return to the case of small inner circles. 

\bigskip

\noindent \underline{Medium Inner Circles and Nonwandering Circles}: Let $\sigma_{m_{i}}^{r_{i}}$, where $r_{i}>0$, denote a positive syllable of $\beta$ that is cyclically neighbored on both sides by negative syllables as in Remark~\ref{cond}. Then the A-resolution of the induced subword will resemble either the left side (up to reflection and except for the additional surrounding vertical line segments) or the center (except for the additional surrounding vertical line segments) of Figure~\ref{loop}. In particular, the existence of an isolated positive syllable corresponds to the existence of one or two medium inner circles, one in the case of Condition~(2a) and Condition~(2c) and two in the case of Condition~(2b). Furthermore, a nonwandering circle will occur in $H_{A}$ precisely when all syllables in the generator $\sigma_{1}$ are positive (see the left side of Figure~\ref{loop}) or when all syllables in the generator $\sigma_{n-1}$ are positive (which would give a reflection of the left side of Figure~\ref{loop}).
 
\bigskip

Note that we may classify the wandering circles in the annulus into essential and non-essential circles. Since the A-resolutions of all portions of the closure of $\beta=N_{1}$ and $\beta=P_{1}N_{1} \cdots P_{t}N_{t}$ have been considered locally and since gluing such portions together joins wandering and potential nonwandering circle portions together to form wandering and nonwandering circles, then we have the desired classification of all-A circles.  
\end{proof}

\begin{sublemma} \label{sublemma2} Let $D(K)=\widehat{\beta}$ satisfy the assumptions of Lemma~\ref{setup}. Then $D(K)$ is connected, prime, and contains $t(D) \geq 2(n-1)$ twist regions.    
\end{sublemma}

\begin{proof} Recall that $D(K)$ is connected if and only if the projection graph of $D(K)$ is path-connected. Since $\beta \in B_{n}$ contains a complete subword, then each generator of $B_{n}$ (each of which corresponds to a crossing of $D(K)$ between adjacent braid string portions) must occur at least once. This fact implies that the closed $n$-braid diagram $D(K)$ must be connected. 

Since $\beta$ contains two disjoint complete subwords, then it must be that each of the generators $\sigma_{1}, \ldots, \sigma_{n-1}$ of $B_{n}$ must occur at least twice in (two distinct syllables of) the braid word. Since the syllables of the cyclically reduced braid word $\beta$ correspond to the twist regions of $D(K)$, then we have that $t(D) \geq 2(n-1)$. 

Let $C$ be a simple closed curve that intersects $D(K)=\widehat{\beta}$ exactly twice (away from the crossings) and contains crossings on both sides. To show that $D(K)$ is prime, we need to show that such a curve $C$ cannot exist. Recall that $D(K)$ lies in an annular region of the plane. 




	
	  
		  
	
	


\bigskip

\noindent \underline{Case 1}: Suppose $C$ contains a point $p$ outside of this annular region. Since $C$ only intersects $D(K)$ twice and must start and end at $p$, then $C$ must intersect $D(K)$ twice in braid string position $1$ or twice in braid string position $n$. This cannot happen because the crossings corresponding to the occurrences of $\sigma_{1}$ and $\sigma_{n-1}$ prevent $C$ from being able to close up in a way that will contain crossings on both sides. 

\bigskip

\noindent \underline{Case 2}: Suppose $C$ contains a point $p$ between braid string positions $i$ and $i+1$ for some $1 \leq i \leq n-1$. See Figure~\ref{primeclose}. Since $C$ only intersects $D(K)$ twice and must start and end at $p$, then $C$ must intersect $D(K)$ twice in braid string position $i$ or twice in braid string position $i+1$. Suppose, as in Figure~\ref{primeclose}, that $C$ intersects $D(K)$ twice in braid string position $i$. The case for braid string position $i+1$ is very similar. If $i=1$, then $C$ contains a point outside of the annular region and we return to Case 1. Suppose $2 \leq i  \leq n-1$. Since $\beta$ contains two disjoint induced complete subwords, then the generator $\sigma_{i-1}$ and the generator $\sigma_{i}$ must each occur at least twice, once above $p$ and once below $p$. These occurrences prevent $C$ from being able to close up in a way that will contain crossings on both sides. Thus, this case cannot occur. 
\end{proof}

\begin{figure}
	\centering
	  \def\svgwidth{1.5in}
		  
	\caption{A simple closed curve $C$ intersecting $D(K)$ twice and containing a point $p$ between braid string positions $i$ and $i+1$. Each box in the figure represents the eventual occurrence of the generator $\sigma_{i}$, the generator $\sigma_{i-1}$ (if it exists), and the generator $\sigma_{i+1}$ (if it exists).}
	\label{primeclose}
\end{figure}



\begin{sublemma} \label{sublemma3} Let $D(K)=\widehat{\beta}$ satisfy the assumptions of Lemma~\ref{setup}. Then $D(K)$ is A-adequate.  
\end{sublemma}

\begin{proof} To prove that $D(K)$ is A-adequate, we need to show that no A-segment of the all-A state $H_{A}$ joins an all-A circle to itself. Note that positive syllables in $\beta$ (which include the short twist regions of $D(K)$) A-resolve to give horizontal A-segments and that negative syllables in $\beta$ (which include the long twist regions of $D(K)$) A-resolve to give vertical A-segments. Suppose, for a contradiction, that an A-segment joins an all-A circle to itself. 

\bigskip

\noindent \underline{Case 1}: Suppose the A-segment is a vertical segment. Condition (1) (that negative exponents are at least three in absolute value) implies that it is impossible for a vertical A-segment to join an all-A circle to itself. This is because all vertical A-segments either join distinct small inner circles or join a small inner circle to a medium inner circle or a wandering circle. (See the left side of Figure~\ref{longshort}.)

\bigskip  

\noindent \underline{Case 2}: Suppose the A-segment is a horizontal segment. By Remark~\ref{cond} and Figure~\ref{loop}, it can be seen that it is impossible for a horizontal A-segment to join an all-A circle to itself. This is because all horizontal A-segments join a medium inner circle either to another medium inner circle, to a wandering circle, or to a nonwandering circle. 
\end{proof}

\begin{sublemma} \label{sublemma4} Let $D(K)=\widehat{\beta}$ satisfy the assumptions of Lemma~\ref{setup}. Then $D(K)$ satisfies the TELC.
\end{sublemma}

\begin{proof} Let $C_{1}$ and $C_{2}$ be two distinct all-A circles that share a pair of distinct A-segments, call them $s_{1}$ and $s_{2}$. To prove that $D(K)$ satisfies the TELC, we need to show that these A-segments correspond to crossings from the same short twist region of $D(K)$.

\bigskip

\noindent \underline{Case 1}: Suppose one of $s_{1}$ and $s_{2}$ is a horizontal segment (that must come from a cyclically isolated positive syllable of $\beta$). Then it is impossible for the other segment to be a vertical segment. This is because one of $C_{1}$ and $C_{2}$, say $C_{1}$, must be a medium inner circle. This circle is adjacent, via horizontal A-segments, to the second circle $C_{2}$, which will either be another medium inner circle, a wandering circle, or a nonwandering circle. By Condition~(1), the circle $C_{1}$ is also adjacent to small inner circles above and below. Consequently, the second segment cannot be vertical. Thus, if one of the segments $s_{1}$ and $s_{2}$ is horizontal, then the other segment must also be horizontal. Since the horizontal segments incident to the medium inner circle $C_{1}$ necessarily belong to the same resolution of a short twist region of $D(K)$, then the TELC is satisfied. (See the left side and center of of Figure~\ref{loop}.) 

\bigskip

\noindent \underline{Case 2}: Suppose both $s_{1}$ and $s_{2}$ are vertical segments. Since all vertical A-segments either join distinct small inner circles or join a small inner circle to a medium inner circle or a wandering circle, then one of $C_{1}$ and $C_{2}$ must be a small inner circle. By Condition~(1), it is impossible for a small inner circle to share more than one A-segment with another all-A circle. (See the left side of Figure~\ref{longshort}.) Therefore, this case cannot occur.
\end{proof}

We now combine all of the necessary ingredients in order to prove the Main Lemma. 

\begin{proof}[Proof of Lemma~\ref{setup} (The Main Lemma)] By applying Sublemma~\ref{sublemma1}, Sublemma~\ref{sublemma2}, Sublemma~\ref{sublemma3}, and Sublemma~\ref{sublemma4}, we get every conclusion of Lemma~\ref{setup} except the hyperbolicity of $K$, which follows from Theorem~\ref{Cor}. 
\end{proof}
