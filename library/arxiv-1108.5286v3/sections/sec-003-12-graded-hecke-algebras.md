---
doc_id: arxiv-1108.5286v3
doc_title: "Hochschild homology of affine Hecke algebras"
section_id: sec-003-12-graded-hecke-algebras
section_title: "Graded Hecke algebras"
section_number: 1.2
pages: 7-8
source_pdf: 1108.5286v3.pdf
source_sha256: 447d90883adce21e
toc_source: outline
text_source: latex
latex_prose_ratio: 0.972
latex_coverage_ratio: 1.0
doc_brief: "Hochschild homology of affine Hecke algebras — Let H = H(R, q) be an aﬃne Hecke algebra with complex, possibly unequal parameters q, which are not roots of unity."
---
Graded Hecke algebras are also known as degenerate (affine) Hecke algebras.
They were introduced by Lusztig in \cite{Lus-Gr}. We call 
\begin{equation}
\tilde{\mc R} = (\mf a^* ,R, \mf a, R^\vee, \Delta )
\end{equation}
a degenerate root datum. We pick complex numbers $k_\alpha$ for $\alpha \in \Delta$,
such that $k_\alpha = k_\beta$ if $\alpha$ and $\beta$ are in the same $W$-orbit.
The graded Hecke algebra associated to these data is the complex vector space
\[
\mh H = \mh H (\tilde{\mc R},k) = S( \mf t^*) \otimes \C [W] ,
\]
with multiplication defined by the following rules:
\begin{itemize}
\item $\mh C[W]$ and $S (\mf t^* )$ are canonically embedded as subalgebras;
\item for $x \in \mf t^*$ and $s_\alpha \in S$ we have the cross relation
\begin{equation}\label{eq:1.1}
x \cdot s_\alpha - s_\alpha \cdot s_\alpha (x) = 
k_\alpha \inp{x}{\alpha^\vee} .
\end{equation}
\end{itemize}
Multiplication with any $\ep \in \mh C^\times$ defines a bijection $m_\ep : \mf t^* \to \mf t^*$,
which clearly extends to an algebra automorphism of $S(\mf t^* )$. From the cross relation
\eqref{eq:1.1} we see that it extends even further, to an algebra isomorphism
\begin{equation}\label{eq:1.3}
m_\ep : \mh H (\tilde{\mc R},\ep k) \to \mh H (\tilde{\mc R}, k)
\end{equation}
which is the identity on $\mh C[W]$. For $\ep = 0$ this map is well-defined, but
obviously not bijective.

Let $\Gamma$ be a group of diagram automorphisms of $\mc R$, and assume that 
$k_{\gamma (\alpha)} = k_\alpha$ for all $\alpha \in R , \gamma \in \Gamma$.
Then $\Gamma$ acts on $\mh H$ by the algebra automorphisms
\begin{equation}
\begin{split}
& \psi_\gamma : \mh H \to \mh H \,, \\
& \psi_\gamma (x s_\alpha ) = \gamma (x) s_{\gamma (\alpha )} 
  \qquad x \in \mf t^* , \alpha \in \Pi \,.
\end{split}
\end{equation}
By \cite[Proposition 5.1.a]{SolHomGHA} the centre of the resulting crossed product algebra is
\begin{equation}\label{eq:1.4}
Z (\mh H \rtimes \Gamma) = S(\mf t^*)^{W \rtimes \Gamma} = 
\mc O (\mf t / (W \rtimes \Gamma)) .
\end{equation}
We say that the central character of an $\mh H \rtimes \Gamma$-representation is real 
if it lies in $\mf a / (W \rtimes \Gamma)$.
\vspace{2mm}
