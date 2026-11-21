---
doc_id: arxiv-1011.0679v2
doc_title: "A FORMULA OF ARTHUR AND AFFINE HECKE ALGEBRAS"
section_id: sec-008-4-algebras-of-invariants
section_title: "Algebras of invariants"
section_number: 4
pages: 17-20
source_pdf: 1011.0679v2.pdf
source_sha256: 6fa4bbcf4e908373
toc_source: outline
text_source: latex
latex_prose_ratio: 0.979
latex_coverage_ratio: 0.925
doc_brief: "A FORMULA OF ARTHUR AND AFFINE HECKE ALGEBRAS — Let π, π′ be tempered representations of an aﬃne Hecke algebra with positive parameters."
---
Let $U$ be a smooth manifold, possibly with corners, and let $G$ be a finite group
acting on $U$ by diffeomorphisms $\alpha_g$. Let $V$ be a finite dimensional complex
$G$-representation and endow the algebra $C^\infty (U) \otimes \mr{End}_\C (V)$
with the diagonal $G$-action. Algebras of the form
\[
\big( C^\infty (U) \otimes \mr{End}_\C (V) \big)^G
\]
were studied among others in \cite{Sol-Chern} and \cite[Section 2.5]{Sol-Thesis}.
In the proof of Theorem \ref{thm:ArthurFormula} we used some elementary results
on such algebras, which we prove here. Certainly a substantial part of this section is
already known, but the authors have not found a suitable reference.

\begin{thm}\label{thm:Moritaeq}
Let $V'$ be another finite dimensional $G$-representation and assume that, for every irreducible
$G$-representation $W, \; \mr{Hom}_G (W,V) = 0$ if and only if $\mr{Hom}_G (W,V') = 0$.
\enuma{
\item The algebras $\big( C^\infty (U) \otimes \mr{End}_\C (V) \big)^G$ and
$\big( C^\infty (U) \otimes \mr{End}_\C (V') \big)^G$ are Morita-equivalent.
\item For the regular representation $\C [G]$ of $G$ we have
\[
\big( C^\infty (U) \otimes \mr{End}_\C (\C [G]) \big)^G \cong C^\infty (U) \rtimes G .
\]
\item Denote the isotropy group of $u \in U$ by $G_u$. Let $\sigma$ be finite dimensional
representation $G_u$ and let $\sigma^*$ be the contragredient representation.
Under the isomorphism (b) the $C^\infty (U) \rtimes G$-representation
\[
\mr{Ind}_{C^\infty (U) \rtimes G_u}^{C^\infty (U) \rtimes G} (\C_u \otimes \sigma)
\]
corresponds to a $\big( C^\infty (U) \otimes \mr{End}_\C (\C [G]) \big)^G$-representation
$\pi (u,\sigma)$ with $C^\infty (U)^G$-character $G u$, such that
\[
\mr{Hom}_{\big( C^\infty (U) \otimes \mr{End}_\C (V) \big)^G}
(\pi (u,\sigma), \C_u \otimes V)) \cong \sigma^*,
\]
as $G_u$-representations.
}
\end{thm}
\noindent \emph{Proof.}
(a) Consider the bimodules
\[
\begin{array}{lll}
M_1 & = & C^\infty (U) \otimes \mr{Hom}_\C (V,V'), \\
M_2 & = & C^\infty (U) \otimes \mr{Hom}_\C (V',V).
\end{array}
\]
It is clear that
\begin{equation}\label{eq:13}
M_1 \otimes_{C^\infty (U) \otimes \mr{End}_\C (V)} M_2 \cong C^\infty (U) \otimes \mr{End}_\C (V') ,
\end{equation}
and similarly in the reversed order. We will show that \eqref{eq:13} remains valid if we take
$G$-invariants everywhere. In other words, we claim that the bimodules $M_1^G$ and $M_2^G$
implement the desired Morita-equivalence. Notice the multiplication yields a natural map
\begin{equation}\label{eq:14}
M_1^G  \otimes_{\big( C^\infty (U) \otimes \mr{End}_\C (V) \big)^G} M_2^G  \to
\big( C^\infty (U) \otimes \mr{End}_\C (V') \big)^G .
\end{equation}
Take any $u \in U$ and let $I \subset C^\infty (U)^G$ be the maximal ideal of functions
vanishing at $G u$. Dividing out \eqref{eq:14} by $I$, we obtain
\begin{equation}\label{eq:15}
\mr{Hom}_{G_u} (V,V') \otimes_{\mr{End}_{G_u} (V')} \mr{Hom}_{G_u} (V',V) \to
\mr{End}_{G_u} (V) .
\end{equation}
Decompose the $G_u$-representations $V$ and $V'$ as
\[
V \cong \bigoplus_{\rho \in \mr{Irr}(G)} \rho \otimes \C^{m_\rho} ,\qquad
V' \cong \bigoplus_{\rho \in \mr{Irr}(G)} \rho \otimes \C^{m'_\rho}
\]
The assumption of the Theorem says that $m_\rho = 0$ if and only if $m'_\rho = 0$. As
\[
\mr{End}_{G_u} (V') \cong
\bigoplus_{\rho \in \mr{Irr}(G)} \mr{End}_{G_u} (\rho) \otimes \mr{End}_\C (\C^{m'_\rho}) ,
\]
the left hand side of \eqref{eq:15} is isomorphic to
\begin{multline*}
\hspace{-5mm} \bigoplus_{\rho \in \mr{Irr}(G)} \!\! \mr{End}_{G_u} (\rho)
\otimes \mr{Hom}_\C (\C^{m_\rho}, \C^{m'_\rho}) \: \otimes_{\mr{End}_{G_u} (V')}
\bigoplus_{\rho \in \mr{Irr}(G)} \mr{End}_{G_u} (\rho) \otimes
\mr{Hom}_\C (\C^{m'_\rho}, \C^{m_\rho}) \\
\cong \bigoplus_{\rho \in \mr{Irr}(G)} \!\! \mr{End}_{G_u} (\rho) \otimes
\mr{End}_\C (\C^{m_\rho}) \cong \mr{End}_{G_u} (V) .
\end{multline*}
Hence \eqref{eq:15} is a bijection for all $u \in U$, which implies that \eqref{eq:14} is injective.
The image of \eqref{eq:14} is a two-sided ideal of $\big( C^\infty (U) \otimes \mr{End}_\C (V')
\big)^G$, which is dense in the sense that for every $u \in U$ the algebra and its ideal have the
same set of values at $u$. Consequently \eqref{eq:14} is bijective, and it is an isomorphism of
$\big( C^\infty (U) \otimes \mr{End}_\C (V') \big)^G$-bimodules.\\
(b) For use in part (c) we provide a proof of this folklore result.
We agree that the action of $G$ on $V = \C [G]$ is $\rho(g) (h) = h g^{-1}$.
For a decomposable tensor $f \otimes g \in C^\infty (U) \rtimes G$ we define
$L(f \otimes g) \in C^\infty (U) \otimes \mr{End}_\C (\C [G])$ by
\[
L(f \otimes g) (h) = \alpha_{h^{-1} g^{-1}} (f) \otimes gh \qquad h \in G .
\]
It is easily verified that $L(f \otimes g)$ is $G$-invariant and that $L$
extends to an algebra homomorphism
\[
L : C^\infty (U) \rtimes G \to \big( C^\infty (U) \otimes \mr{End}_\C (\C [G]) \big)^G .
\]
We claim that $L$ is invertible, with inverse
\[
L'(b) = \sum_{g \in G} b(g^{-1})_e \otimes g \text{, where }
b(g^{-1}) = \sum_{h \in G} b (g^{-1})_h \otimes h \in C^\infty (U) \otimes \C [G] .
\]
Clearly $L' (L (f \otimes g)) = f \otimes g$, while for any
$b \in \big( B \otimes \mr{End}(\mh C [G]) \big)^G$ and $h \in G$:
\begin{equation}
\begin{split}
L(L'b)(h) &= \sum_{g \in G} \alpha_{h^{-1} g^{-1}} (b(g^{-1})_e) \otimes gh \\
 &= \alpha_{h^{-1}} \big( (\alpha_{g^{-1}} b)(g^{-1}) \big)_e \otimes gh \\
 &= \sum_{g \in G} \alpha_{h^{-1}} \big( (\rho(g) b \rho (g^{-1}) ) (g^{-1}) \big)_e \otimes gh \\
 &= \sum_{g \in G} \alpha_{h^{-1}} \big( b(e) g^{-1} \big)_e \otimes gh \\
 &= \big( \alpha_{h^{-1}} b \big) (e) h \\
 &= \big( \rho(h^{-1}) \alpha_{h^{-1}}(b) \rho(h) \big) (h) \;=\; b(h) .
\end{split}
\end{equation}
Thus indeed $L'$ is the inverse of $L$.\\
(c) It suffices to show this when $\sigma$ is an irreducible $G_u$-representation.
The isomorphism from part (b) preserves the central characters, so the ideal $I$ of
$\big( C^\infty (U) \otimes \mr{End}_\C (V) \big)^G$ generated by
$\{ f \in C^\infty (U)^G | f(u) = 0 \}$ annihilates $\pi (u,\sigma)$. In other words, we
must describe $\pi (u,\sigma)$ as a representation of
\[
\big( C^\infty (U) \otimes \mr{End}_\C (V) \big)^G / I \cong
\big( \bigoplus\nolimits_{g \in G / G_u} \mr{End}_\C (\C [G]) \big)^G \cong \mr{End}_{G_u} (\C [G]) .
\]
As a $G_u$-representation $V = \C [G] \cong \C [G_u] \otimes \C^{[G:G_u]}$, so
\[
\mr{End}_{G_u} (\C [G]) \cong \mr{End}_{G_u} (\C [G_u]) \otimes \mr{End}_\C (\C^{[G:G_u]})
\cong \C [G_u] \otimes M_{[G:G_u]} (\C) .
\]
Unter these identifications $\pi (u,\sigma)$ corresponds to the representation
$\sigma \otimes \C^{[G:G_u]}$. Then
\[
\mr{Hom}_{\big( C^\infty (U) \otimes \mr{End}_\C (V) \big)^G} (\pi (u,\sigma), \C_u \otimes V)
\cong \mr{Hom}_{G_u} (\sigma, \C [G_u]) .
\]
As a $G_u \times G_u$-representation $\C [G_u] \cong \bigoplus_{\rho \in \mr{Irr}(G_u)}
\rho \otimes \rho^*$, so $\mr{Hom}_{G_u} (\sigma, \C [G_u]) \cong \sigma^*$
as $G_u$-representations. $\qquad \Box$
\vspace{4mm}
