---
doc_id: arxiv-1406.7337v4
doc_title: "Semi-Adequate Closed Braids and Volume"
section_id: sec-003-22-braids-and-a-adequacy
section_title: "Braids and A-adequacy"
section_number: 2.2
pages: 3-5
source_pdf: 1406.7337v4.pdf
source_sha256: 5bae8237742733b9
toc_source: outline
text_source: latex
latex_prose_ratio: 0.978
latex_coverage_ratio: 0.989
doc_brief: "Semi-Adequate Closed Braids and Volume — In this paper, we show that the volumes for a family of A-adequate closed braids can be bounded above and below in terms of the twist number, the number of"
---
Recall that the \emph{n-braid group} has Artin presentation

$$\displaystyle B_{n} = \left\langle \sigma_{1}, \cdots, \sigma_{n-1}\ |\ \sigma_{i}\sigma_{j}=\sigma_{j}\sigma_{i}\ \mathrm{and}\ \sigma_{i}\sigma_{i+1}\sigma_{i} = \sigma_{i+1}\sigma_{i}\sigma_{i+1}\right\rangle,$$ 

\noindent where the generators $\sigma_{i}$ are depicted in Figure~\ref{braidgen}, where $\left|i-j\right|\geq2$ and $1 \leq i < j \leq n-1$ in the first relation (sometimes called \emph{far commutativity}), and where $1\leq i\leq n-2$ in the second relation. As a special case, the \emph{3-braid group} has Artin presentation

$$B_{3}=\left\langle \sigma_{1}, \sigma_{2}\ |\ \sigma_{1}\sigma_{2}\sigma_{1}=\sigma_{2}\sigma_{1}\sigma_{2}\right\rangle.$$ 

\begin{figure}
	\centering
	\def\svgwidth{3in}
		
	\caption{The braid group generators $\sigma_{i}$ and $\sigma_{i}^{-1}$ of $B_{n}$, where $1 \leq i \leq n-1$.}
	\label{braidgen}
\end{figure}

\begin{definition}
Call a subword $\gamma$ of a braid word $\beta \in B_{n}$ \emph{(cyclically) induced} if the letters of $\gamma$ are all (cyclically) adjacent and appear in the same order as in the full braid word $\beta$. As an example, given the braid word 

$$\beta=\sigma_{1}^{3}\sigma_{2}^{-3}\sigma_{1}^{2}\sigma_{3}^{-2}\sigma_{2}\sigma_{3}=\sigma_{1}^{3}\sigma_{2}^{-1}(\sigma_{2}^{-2}\sigma_{1}^{2}\sigma_{3}^{-1})\sigma_{3}^{-1}\sigma_{2}\sigma_{3},$$ 

\noindent the subword $\gamma=\sigma_{2}^{-2}\sigma_{1}^{2}\sigma_{3}^{-1}$ is an induced subword of $\beta$. 
\end{definition} 

Because conjugate braids have isotopic braid closures, we will usually work within conjugacy classes of braids. Furthermore, note that cyclic permutation is a special case of conjugation.

\begin{definition} A braid $\beta=\sigma_{m_{1}}^{r_{1}}\cdots\sigma_{m_{l}}^{r_{l}} \in B_{n}$ is called \emph{cyclically reduced into syllables} if the following hold:

\begin{enumerate}
\item[(1)] $r_{i}\neq 0$ for all $i$. 
\item[(2)] there are no occurrences of induced subwords of the form $\sigma_{i}\sigma_{i}^{-1}$ or $\sigma_{i}^{-1}\sigma_{i}$ for any $i$ (looking up to cyclic permutation).
\item[(3)] $m_{i}\neq m_{i+1}$ for all $i$ (modulo $l$). 
\end{enumerate}
\end{definition}

Recall that a braid $\beta=\sigma_{m_{1}}^{r_{1}}\cdots\sigma_{m_{l}}^{r_{l}} \in B_{n}$ is called \emph{positive} if all of the exponents $r_{i}$ are positive and \emph{negative} if all of the exponents $r_{i}$ are negative. We define a syllable $\sigma_{m_{i}}^{r_{i}}$ of the braid word to be \emph{positive} if $r_{i}>0$ and \emph{negative} if $r_{i}<0$. We now present Stoimenow's (\cite{Stoimenow}) classification of A-adequate closed 3-braid diagrams. 

\begin{proposition}[\cite{Stoimenow}, Lemma 6.1] 

Let $D(K)=\widehat{\beta}$ denote the closure of a 3-braid 

$$\beta=\sigma_{i}^{r_{1}}\sigma_{j}^{r_{2}}\cdots\sigma_{i}^{r_{2l-1}}\sigma_{j}^{r_{2l}} \in B_{3},$$ 

\noindent where $\left\{i,j\right\}=\left\{1,2\right\}$, where $l \geq 2$, and where $\beta$ has been cyclically reduced into syllables. Then $D(K)$ is A-adequate if and only if either 
\begin{enumerate}\label{adeq3braid}
\item[(1)] $\beta$ is positive, or
\item[(2)] $\beta$ does not contain $\sigma_{1}^{-1}\sigma_{2}^{-1}\sigma_{1}^{-1}=\sigma_{2}^{-1}\sigma_{1}^{-1}\sigma_{2}^{-1}$ as a cyclically induced subword and $\beta$ also has the property that all positive syllables in the braid word are cyclically neighbored on both sides by negative syllables.   
\end{enumerate}
\end{proposition}
