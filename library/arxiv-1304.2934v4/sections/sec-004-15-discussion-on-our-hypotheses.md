---
doc_id: arxiv-1304.2934v4
doc_title: "MOD-φ CONVERGENCE, I: NORMALITY ZONES AND PRECISE DEVIATIONS"
section_id: sec-004-15-discussion-on-our-hypotheses
section_title: "Discussion on our hypotheses"
section_number: 1.5
pages: 8-9
source_pdf: 1304.2934v4.pdf
source_sha256: b7ed2a9e85264568
toc_source: outline
text_source: latex
latex_prose_ratio: 0.91
latex_coverage_ratio: 1.0
doc_brief: "MOD-φ CONVERGENCE, I: NORMALITY ZONES AND PRECISE DEVIATIONS — In this paper, we use the framework of mod-φ convergence to prove pre- cise large or moderate deviations for quite general sequences of"
---
\label{subsec:discussion_hypotheses}
The following remarks explain the role of each hypothesis of Definition~\ref{def:modphi}. As we shall see later, some assumptions can be removed in some of our results (\emph{e.g.}, the infinite-divisibility of the reference law), but Definition \ref{def:modphi} provides a coherent setting where all the techniques presented in the paper do apply without further verification. 

\begin{remark}[Analyticity]
The existence of the relevant moment generating function on a strip is crucial in our proof, as we consider in Section \ref{sec:nonlattice} the Fourier transform of $\widetilde{X_n}$, obtained from $X_n$ by an exponential change of measure. We also use respectively the existence of continuous derivatives up to order $3$ for $\eta$ and $\psi$ on the strip $\mathcal{S}_{(c,d)}$, and the local uniform convergence of $\psi_n$ and its first derivatives (say, up to order $3$) toward those of $\psi$. By Cauchy's formula, the local uniform convergence of analytic functions imply those of their derivatives, so it provides a natural framework where convergence of derivatives are automatically verified.
\medskip

Let us mention however that these assumptions of analyticity are a bit restrictive, as they imply that the $X_{n}$'s and $\phi$ have moments of all order; in particular, $\phi$ cannot be any infinitely divisible distribution (for instance the Cauchy distribution is excluded). That explains that the theory of mod-$\phi$ convergence was initially developed with characteristic functions on the real line  rather than moment generating functions in a complex domain. With this somehow weaker hypothesis, one can find many examples for instance of mod-Cauchy convergence (see \emph{e.g.} \cite{DKN11,KNN13}), while the concept of mod-Cauchy convergence does not even make sense in the sense of Definition~\ref{def:modphi}. We are unfortunately not able to give precise deviation results  in this framework.
\end{remark}\medskip

\begin{remark}[Infinite divisibility and non-vanishing of the terms of mod-$\phi$ convergence]
The non-vanishing of $\psi$ is a natural hypothesis since evaluations of $\psi$ appear in many estimates of non-zero probabilities, and also in denominators in fractions, see for instance Lemma \ref{lem:exponchange}. 
The assumption that $\phi$ is an infinitely divisible distribution 
will be discussed in Section \ref{subsect:OnInfDiv}.
\end{remark}
\bigskip
