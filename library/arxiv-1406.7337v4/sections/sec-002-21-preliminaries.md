---
doc_id: arxiv-1406.7337v4
doc_title: "Semi-Adequate Closed Braids and Volume"
section_id: sec-002-21-preliminaries
section_title: "Preliminaries"
section_number: 2.1
pages: 2-3
source_pdf: 1406.7337v4.pdf
source_sha256: 5bae8237742733b9
toc_source: outline
text_source: latex
latex_prose_ratio: 0.969
latex_coverage_ratio: 0.992
doc_brief: "Semi-Adequate Closed Braids and Volume — In this paper, we show that the volumes for a family of A-adequate closed braids can be bounded above and below in terms of the twist number, the number of"
---
\begin{figure}
	\centering
		\def\svgwidth{2.5in}
		
	\caption{A crossing neighborhood of a link diagram, along with its A-resolution and B-resolution.}
	\label{resolutions}
\end{figure}

Let $D(K) \subseteq S^2$ denote a diagram of a link $K \subseteq S^3$. To smooth a crossing of the link diagram $D(K)$, we may either \emph{A-resolve} or \emph{B-resolve} this crossing according to Figure~\ref{resolutions}. By A-resolving each crossing of $D(K)$ we form the \emph{all-A state} of $D(K)$, which is denoted by $H_{A}$ and consists of a disjoint collection of \emph{all-A circles} and a disjoint collection of dotted line segments, called \emph{A-segments}, that are used record the locations of crossing resolutions. We will adopt the convention throughout this paper that any unlabeled segments are assumed to be A-segments. We call a link diagram $D(K)$ \emph{A-adequate} if $H_{A}$ does not contain any A-segments that join an all-A circle to itself, and we call a link $K$ \emph{A-adequate} if it has a diagram that is A-adequate. While we will focus exclusively on A-adequate links, our results can easily be extended to semi-adequate links by reflecting the link diagram $D(K)$ and obtaining the corresponding results for B-adequate links. 

From $H_{A}$ we may form the \emph{all-A graph}, denoted $\mathbb{G}_{A}$, by contracting the all-A circles to vertices and reinterpreting the A-segments as edges. From this graph we can form the \emph{reduced all-A graph}, denoted $\mathbb{G}_{A}'$, by replacing parallel edges with a single edge. For an example of a diagram $D(K)$, its all-A resolution $H_{A}$, its all-A graph $\mathbb{G}_{A}$, and its reduced all-A graph $\mathbb{G}_{A}'$, see Figure~\ref{figure8}. Let $v(G)$ and $e(G)$ denote the number of vertices and edges, respectively, in a graph $G$. Let $-\chi(G)=e(G)-v(G)$ denote the negative Euler characteristic of $G$. 

\begin{figure}
	\centering
		\def\svgwidth{3.5in}
		
	\caption{A link diagram $D(K)$, its all-A resolution $H_{A}$, its all-A graph $\mathbb{G}_{A}$, and its reduced all-A graph $\mathbb{G}_{A}'$.}
	\label{figure8}
\end{figure}






\begin{figure}
	\centering
		\def\svgwidth{200pt}
		
	\caption{The long and short resolutions of a twist region of $D(K)$.}
	\label{longshort}
\end{figure}

\begin{definition} 
Define a \emph{twist region} of $D(K)$ to be a longest possible string of bigons in the projection graph of $D(K)$. Denote the number of twist regions in $D(K)$ by $t(D)$ and call $t(D)$ the \emph{twist number} of $D(K)$. Note that it is possible for a twist region to consist of a single crossing of $D(K)$. If a given twist region contains two or more crossings, then the A-resolution of a left-handed twist region will be called a \emph{long resolution} and the A-resolution of a right-handed twist region will be called a \emph{short resolution}. See Figure~\ref{longshort} for depictions of these resolutions. We will call a twist region \emph{long} if its A-resolution is long and \emph{short} if its A-resolution is short. 
\end{definition}

\begin{definition}
A link diagram $D(K)$ satisfies the \emph{two-edge loop condition (TELC)} if, whenever two all-A circles share a pair of A-segments, these segments correspond to crossings from the same short twist region of $D(K)$. (See the right side of Figure~\ref{longshort}.)
\end{definition}


















	
		
		
	
	


Recall that $v_{8}=3.6638\ldots$ denotes the volume of a regular ideal octahedron and $v_{3}=1.0149\ldots$ denotes the volume of a regular ideal tetrahedron. By combining results from \cite{New}, \cite{Guts}, and \cite{Lackenby}, we get the following key result.

\begin{theorem}[Corollary 1.4 of \cite{New}, Theorem from Appendix of \cite{Lackenby}]
Let $D(K)$ be a connected, prime, A-adequate link diagram that satisfies the TELC and contains $t(D) \geq 2$ twist regions. Then $K$ is hyperbolic and
\label{Cor}
\begin{equation*}
-v_{8}\cdot\chi(\mathbb{G}_{A}') \leq \mathrm{vol}(S^{3}\backslash K) < 10v_{3}\cdot(t(D)-1).
\end{equation*}
\end{theorem}
