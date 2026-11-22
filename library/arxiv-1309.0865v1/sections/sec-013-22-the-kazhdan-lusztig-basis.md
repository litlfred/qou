---
doc_id: arxiv-1309.0865v1
doc_title: "SOERGEL CALCULUS"
section_id: sec-013-22-the-kazhdan-lusztig-basis
section_title: "The Kazhdan-Lusztig basis"
section_number: 2.2
pages: 14-15
source_pdf: 1309.0865v1.pdf
source_sha256: e610a4fa938a7cc9
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.933
latex_coverage_ratio: 0.971
doc_brief: "SOERGEL CALCULUS — The monoidal category of Soergel bimodules is an incarnation of the Hecke category, a fundamental object in representation theory."
---
\label{subsec-KLbasis}


The Hecke algebra is equipped with a $\Z$-linear \emph{bar involution}, denoted $h \mapsto \overline{h}$ and
uniquely specified as an algebra homomorphism by $v \mapsto v^{-1}$ and $H_s \mapsto H_s^{-1}$. A simple
calculation shows that $H_s + v = H_s^{-1}+v^{-1}$, so that the element $\un{H}_s = H_s+v$ is bar-invariant.

\begin{thm}(Kazhdan-Lusztig \cite{KaL1}) There exists a unique basis $\{\un{H}_w\}_{w \in W}$ of $\HB$ as a $\Zvv$-module, called the \emph{Kazhdan-Lusztig basis}, which satisfies:
\begin{itemize}
\item $\overline{\un{H}_w}=\un{H}_w$;
\item $\un{H}_w = H_w + \sum_{x < w} h_{x,w} H_x$ where $h_{x,w} \in v\ZM[v]$.\end{itemize}
\end{thm}

The polynomials $h_{x,w} \in \ZM[v]$ are \emph{Kazhdan-Lusztig polynomials}. 

\begin{remark} In this paper we follow the normalization of Soergel \cite{Soe4} rather than the original normalization of \cite{KaL1}. In particular, the Kazhdan-Lusztig polynomials $P_{x,w}$ in \cite{KaL1} are related to the Kazhdan-Lusztig polynomials above by the formula
\[
h_{x,w} = v^{2(\ell(w) - \ell(x))}P_{x,w}(v^{-2}).
\]
\end{remark}

Given $\un{w} = s_1s_2 \dots s_m$ we set $\un{H}_{\un{w}} \define \un{H}_{s_1} \dots \un{H}_{s_m}$. Note that $\un{H}_{\un{w}} \ne \un{H}_w$ in general, but equality does hold when $\ell(\un{w}) \le 2$ and $s_1 \ne s_2$.

An element $w \in W$ is called \emph{(rationally) smooth} if $\un{H}_w = \sum_{y \le w} v^{\ell(w) -\ell(y)}H_y$. The longest element of any finite parabolic subgroup is smooth. Any
element of a rank 2 parabolic subgroup is smooth.

We pause to present three conjectures of Kazhdan and Lusztig:

\begin{conj} The polynomials $h_{x,y}$ have positive coefficients, i.e. they lie in $\ZM_{\ge 0}[v]$. \end{conj}

\begin{conj} The structure coefficients of the Kazhdan-Lusztig basis $\HB$ are positive. In other words, $\un{H}_u \un{H}_v = \sum c^w_{u,v} \un{H}_w$ for some $c^w_{u,v} \in \Nvv$. \end{conj}

These first two conjectures are commonly referred to as the \emph{Kazhdan-Lusztig positivity conjectures}. The following conjecture is the \emph{Kazhdan-Lusztig conjecture}. It and its many generalizations account to a large extent for the interest in Kazhdan-Lusztig polynomials. (For a precise statement of the Kazhdan-Lusztig conjecture see \cite{KaL1}.)

\begin{conj} (The Kazhdan-Lusztig Conjecture) If $W$ is the Weyl group of a complex semi-simple Lie algebra, then the Kazhdan-Lusztig polynomials give the multiplicities of simple modules in Verma modules in the principal block of category $\OC$.\end{conj}

These three conjectures are themselves implications of the Soergel conjecture. We will discuss this in section \ref{subsec-SoergelCatfn}.
