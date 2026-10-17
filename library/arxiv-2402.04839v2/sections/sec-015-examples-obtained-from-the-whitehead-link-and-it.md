---
doc_id: arxiv-2402.04839v2
doc_title: "On a volume invariant of 3-manifolds"
section_id: sec-015-examples-obtained-from-the-whitehead-link-and-it
section_title: "Examples obtained from the Whitehead link and its sister"
section_number: null
pages: 17-18
source_pdf: 2402.04839v2.pdf
source_sha256: daf09811c350a2ad
toc_source: outline
text_source: latex
latex_prose_ratio: 0.964
latex_coverage_ratio: 0.929
doc_brief: "On a volume invariant of 3-manifolds (Kegel, Ray, Spreer, Thompson, Tillmann) — defines topological volume vol_t(M), the smallest volume of a hyperbolic-link complement in M; bounds and a…"
---
\label{sec:WandP}

Let $W$ denote the complement of the right-handed Whitehead link with Seifert framing. This is $m129$ and $L5a1$ in the census, where the latter denotes the left-handed Whitehead link. We also let $P$ denote the $(-2,3,8)$ pretzel link complement, again, with Seifert framing. This is often called the \emph{sister manifold} of $W$ and appears as $m125$ and L13n5885 in the census of manifolds and links respectively. In the following, we use $W$ and $P$ to denote the complements of Whitehead link and sister manifold with the Seifert framing, and $m129$ and $m125$ for the Snappy census manifolds with geometric framing. 

\begin{figure}[htb]
	\centering
	\includegraphics[width=13cm]{Whitehead_and_sister}
	\caption{The Whitehead link $L5a1$ (left) and its sister link $L13n5885$ (right). The unknotted blue component is the first cusp (which we fill).}
	\label{fig:W_and_P}
\end{figure}

In SnapPy \cite{snappy}, the framing change (under filling the first cusp) is as follows:
\begin{align*}
    L5a1(p,q)(0,0)&\cong m129(p+2q,-q)(0,0)\\
    L13n5885(p,q)(0,0)&\cong m125(p-4q,p-3q)(0,0)
\end{align*}

In this section we show that, for $p^2 + q^2$ sufficiently large, $L(p,q)$ has as minimiser a filling of the Whitehead or its sister link, cf.\thinspace \Cref{prop:lens-space-limit}. 

Our computation of the smallest volume lens spaces given in \Cref{tab:complete} shows that the minimisers of all lens spaces of topological volume at most 3.07---with $p^2 + q^2$ quite small---also arise as fillings of the Whitehead or its sister link.
However, there are lens spaces for which the minimiser is not realised as a filling on either of these. One example is $L(4,1)$ (see \Cref{cor:L4-is-special}). A surgery diagram of $m034$ that displays this manifold as a knot complement of a knot in $L(4,1)$ is shown in \Cref{fig:m034}. 

\begin{question}
What is the complete list of all lens spaces that do not have minimiser a filling of the Whitehead or its sister link?
\end{question}

\begin{figure}[htb]
	\centering
	\includegraphics[width=9cm]{m034_new}
	\caption{A surgery diagram of $m034$}
	\label{fig:m034}
\end{figure}
