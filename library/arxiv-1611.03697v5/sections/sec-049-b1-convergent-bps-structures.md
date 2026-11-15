---
doc_id: arxiv-1611.03697v5
doc_title: "RIEMANN-HILBERT PROBLEMS FROM DONALDSON-THOMAS THEORY"
section_id: sec-049-b1-convergent-bps-structures
section_title: "B.1. Convergent BPS structures"
section_number: null
pages: 43-44
source_pdf: 1611.03697v5.pdf
source_sha256: 3d7e5a14a079c8c5
toc_source: outline
text_source: latex
latex_prose_ratio: 0.817
latex_coverage_ratio: 1.0
doc_brief: "RIEMANN-HILBERT PROBLEMS FROM DONALDSON-THOMAS THEORY — We study a class of Riemann-Hilbert problems arising naturally in Donaldson-Thomas theory."
---
\label{converge}


 The aim of this section is to prove the claims made in Section \ref{ref} that enable one to view the BPS automorphisms of a convergent BPS structure as being partially-defined automorphisms of the twisted torus. 


\subsection{Convergent BPS structures}

 
Recall  from Section \ref{defns} that a BPS structure $(\Gamma,Z,\Omega)$ is called convergent if there exists $R>0$ such that 
\begin{equation}
\label{blockhead}\sum_{\gamma\in \Gamma} |\Omega(\gamma)| \cdot e^{-R |Z(\gamma)|}<\infty.\end{equation}
Let us fix an arbitrary norm
$\|\cdot\|$  on the finite-dimensional vector space $\Gamma\tensor_\bZ \bR$. Then we can find $k_1<k_2$ such that for any active class $\gamma\in \Gamma$  there are inequalities
\begin{equation}\label{ein}k_1\cdot \|\gamma\| < |Z(\gamma)|< k_2\cdot \|\gamma\|.\end{equation}
The first inequality is the support property and requires the assumption that $\gamma\in \Gamma$ is active, whereas the second is just the fact that the linear map $Z\colon \Gamma\tensor_\bZ \bR\to \bC$ has bounded norm. It follows that in  expressions such as  \eqref{blockhead}, which are sums over active classes, we can equally well use $\|\gamma\|$ or $|Z(\gamma)|$ in the exponential factor.


\begin{lemma}
\label{sven}
Let $(\Gamma,Z,\Omega)$  be a convergent BPS structure and choose a norm $\|\cdot\|$  as above.   Then for any $\epsilon>0$ there is an $R>0$ such that
\begin{equation}\label{andrew}\sum_{\gamma\in \Gamma} \|\gamma\|^p \cdot |\DT(\gamma)|\cdot e^{-R  \|\gamma\|}<\epsilon,\end{equation}
for each integer $p\in \{0,1,2\}$. 
\end{lemma}

\begin{proof}
 Clearly it is enough to prove the result for each $p\in \{0,1,2\}$ separately, so we can consider $p$ fixed. For  $x\gg 0$ there is an inequality
\[\frac{x^p}{e^{2x}-1}<e^{-x}.\]
By the discussion above, we can take $S>0$ so that the inequality \eqref{blockhead} holds with $R=S$ and $|Z(\gamma)|$ replaced with $\|\gamma\|$ in the exponential factor.
The   numbers $\|\gamma\|$  are bounded below so increasing $S$ if necessary we can  assume that
\[S^p\|\gamma\|^p \cdot (e^{2S\|\gamma\|}-1)^{-1}< e^{-S\|\gamma\|}<1,\]
for all  classes $\gamma\in \Gamma$.
Taking $R=2S$ and using the definition of DT invariants \eqref{bps} gives
\[\sum_{\gamma\in \Gamma}\|\gamma\|^p \cdot |\DT(\gamma)|\cdot e^{-R \|\gamma\|}=\sum_{\gamma\in \Gamma} \sum_{n\geq 1}  \frac{1}{n^2}\cdot \|n\gamma\|^p \cdot |\Omega(\gamma)|\cdot e^{-2nS\|\gamma\|}\]\[
\leq \sum_{\gamma\in \Gamma}  \|\gamma\|^p\cdot |\Omega(\gamma)|\cdot \frac{e^{-2S\|\gamma\|}}{1-e^{-2S\|\gamma\|}}<S^{-p}\cdot \sum_{\gamma\in \Gamma} |\Omega(\gamma)| \cdot e^{-S \|\gamma\|} <\infty.\]
Since the numbers $\|\gamma\|$ appearing in the exponential factor are bounded below, by increasing $R$ we can  ensure that this sum is smaller than any given $\epsilon>0$. 
\end{proof}
