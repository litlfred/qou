---
doc_id: arxiv-1111.2828v2
doc_title: "THE COMPLEX VOLUME OF SL(n, C)-REPRESENTATIONS OF 3-MANIFOLDS"
section_id: sec-011-31-the-regulator
section_title: "The regulator"
section_number: 3.1
pages: 12-13
source_pdf: 1111.2828v2.pdf
source_sha256: 90e2f5a9b978d403
doc_brief: "THE COMPLEX VOLUME OF SL(n, C)-REPRESENTATIONS OF 3-MANIFOLDS — For a compact 3-manifold M with arbitrary (possibly empty) boundary, we give a parametrization of the set of conjugacy classes of"
text_source: latex
latex_prose_ratio: 0.86
latex_coverage_ratio: 0.944
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



\subsection{Arbitrary fields}
\lbl{sub.allfields}

In Zickert~\cite{ZickertAlgK}, extended Bloch groups $\widehat\B_E(F)$ and 
$\widehat\B_E(F)_{\PSL}$ are defined for an arbitrary field $F$ and a primitive extension $E$ of $F^*$ by $\Z$. The definitions 
are as above using the sets
\begin{equation}
\widehat E_F=\left\{(e,f)\in E^2\bigm\vert \pi(e)+\pi(f)=1\right\},
\quad (\widehat E_F)_{\odd}=\left\{(e,f)\in E^2\bigm\vert 
\pm\pi(e)\pm\pi(f)=1\right\}.
\end{equation}
If $F$ is a number field, the extended Bloch groups are up to canonical isomorphism 
independent of the choice of extension, so we may omit the subscript $E$. 

\begin{theorem} 
[{Zickert~\cite[Theorem~1.1]{ZickertAlgK}}]  
Let $F$ be a number field. There is a natural isomorphism
\begin{equation}
K_3^{\ind}(F)\cong\widehat\B(F)
\end{equation}
respecting Galois actions.\qed
\end{theorem}

\begin{corollary}
[{Zickert~\cite[Corollary~7.14]{ZickertAlgK}}]
\lbl{injectivity} 
For each embedding $\tau\colon F\to\C$, the induced map 
$\tau\colon\widehat\B(F)\to\widehat\B(\C)$ is injective.\qed
\end{corollary}

\begin{corollary}
[{Galois descent; Zickert~\cite[Corollary~7.15]{ZickertAlgK}}]
\lbl{Galoisdescent}
Let $F_2:F_1$ be an extension of number fields. An element in $\widehat\B(F_2)$ is in 
$\widehat\B(F_1)$ if and only if it is invariant under all automorphisms of $F_2$ over $F_1$.\qed 
\end{corollary}
