---
doc_id: arxiv-1111.2828v2
doc_title: "THE COMPLEX VOLUME OF SL(n, C)-REPRESENTATIONS OF 3-MANIFOLDS"
section_id: sec-011-31-the-regulator
section_title: "The regulator"
section_number: 3.1
pages: 12-13
source_pdf: 1111.2828v2.pdf
source_sha256: 90e2f5a9b978d403
toc_source: outline
text_source: latex
latex_prose_ratio: 0.824
latex_coverage_ratio: 0.917
doc_brief: "THE COMPLEX VOLUME OF SL(n, C)-REPRESENTATIONS OF 3-MANIFOLDS — For a compact 3-manifold M with arbitrary (possibly empty) boundary, we give a parametrization of the set of conjugacy classes of"
---
\lbl{sub.regulator}

By fixing a branch of logarithm, we may write a flattening with cross-ratio $z$ as $[z;p,q]=\big(\log(z)+p\pi i,\log(1-z)+q\pi i\big)$, where $p,q\in\Z$ are \emph{even} integers. There is a well defined \emph{regulator map}
\begin{equation}
\lbl{regulator}
\begin{gathered}
R\colon\widehat\Pre(\C)\to\C/4\pi^2\Z,\\
{[z;p,q]}\mapsto \Li_2(z)+\frac{1}{2}(\log(z)+p\pi i)(\log(1-z)-q\pi i)-\pi^2/6.
\end{gathered}
\end{equation}



\subsection{The $\PSL(2,\C)$-variant of the extended Bloch group}
\lbl{sub.vbloch}

There is another variant of the extended Bloch group using flattenings 
$[z;p,q]$, where $p$ and $q$ are allowed to be odd. This group is defined 
as above using the set
\begin{equation}
\widehat{\C}_{\odd}=\left\{(e,f)\in\C^2 \bigm\vert \pm\exp(e)\pm\exp(f)=1\right\},
\end{equation}
and fits in a diagram similar to~\eqref{bigdiagram}. We use a subscript 
$\PSL$ to denote the variant allowing odd flattenings. We have an exact 
sequence
\begin{equation}
\xymatrix{0\ar[r]&{\Z/4\Z}\ar[r]&{\widehat\B(\C)}\ar[r]&
{\widehat\B(\C)_{\PSL}}\ar[r]&0.}
\end{equation}
For odd flattenings, the regulator~\eqref{regulator} is well defined modulo 
$\pi^2\Z$.

\begin{theorem}
[Neumann~\cite{Neumann}, Goette-Zickert~\cite{GoetteZickert}] 
There are natural isomorphisms
\begin{equation}
H_3(\PSL(2,\C))\cong\widehat\B(\C)_{\PSL},\quad H_3(\SL(2,\C))\cong\widehat\B(\C)
\end{equation}
such that the Cheeger-Chern-Simons classes agree with the regulators.\qed
\end{theorem}


The following result is needed in Section~\ref{decorationsection}. The 
first part is proved in Zickert \cite[Lemma~3.16]{ZickertAlgK}, and 
the second has a similar proof, which we leave to the reader.
\begin{lemma}
\lbl{chipqlemma} 
For $(e,f)\in\widehat\C$ and $p,q\in\Z$, we have
\setlength{\belowdisplayskip}{0pt}
\setlength{\belowdisplayshortskip}{0pt}
\setlength{\parskip}{0pt}
\begin{align}
(e+2\pi ip,f+2\pi iq)-(e,f)&=\chi(qe-pf+2pq\pi i)\in\widehat\Pre(\C),\\
(e+\pi ip,f+\pi iq)-(e,f)&=\chi(qe-pf+pq\pi i)\in\widehat\Pre(\C)_{\PSL}.
\end{align}

\nopagebreak
\vspace{-\baselineskip}
\nopagebreak
\qed
\end{lemma}
