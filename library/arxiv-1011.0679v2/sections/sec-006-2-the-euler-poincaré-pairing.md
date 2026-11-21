---
doc_id: arxiv-1011.0679v2
doc_title: "A FORMULA OF ARTHUR AND AFFINE HECKE ALGEBRAS"
section_id: sec-006-2-the-euler-poincaré-pairing
section_title: "The Euler-Poincaré pairing"
section_number: 2
pages: 12-14
source_pdf: 1011.0679v2.pdf
source_sha256: 6fa4bbcf4e908373
toc_source: outline
text_source: latex
latex_prose_ratio: 0.965
latex_coverage_ratio: 0.909
doc_brief: "A FORMULA OF ARTHUR AND AFFINE HECKE ALGEBRAS — Let π, π′ be tempered representations of an aﬃne Hecke algebra with positive parameters."
---
Let $\pi, \pi' \in \mr{Mod}_f (\mc H)$. Their Euler-Poincar\'e pairing is defined as
\begin{equation}\label{eq:4}
EP_{\mc H} (\pi,\pi') = \sum_{n \geq 0} (-1)^n \dim_\C \mr{Ext}_{\mc H}^n (\pi,\pi') .
\end{equation}
Since $\mc H$ is Noetherian and has finite cohomological dimension \cite[Proposition 2.4]{OpSo1},
this pairing is well-defined.

\begin{thm}\label{thm:EP}
\enuma{
\item For all $\pi,\pi' \in \mr{Mod}_f (\mc H)$ and $\ep \in [0,1] $:
\[
EP_{\mc H (\mc R, q^\ep)} (\tilde \sigma_\ep (\pi), \tilde \sigma_\ep (\pi')) = EP_{\mc H} (\pi,\pi') .
\]
\item The pairing $EP_{\mc H}$ is symmetric and positive semidefinite.
\item If $P \subset F_0$ and $\R P \neq \mf a^*$, then $\mr{Ind}_{\mc H^P}^{\mc H}(V)$
lies in the radical of $EP_{\mc H}$, for all $V \in \mr{Mod}_f (\mc H^P)$.
}
\end{thm}
\noindent \emph{Proof.}
See Proposition 3.4 and Theorem 3.5 of \cite{OpSo1}. We note that the symmetry
of $EP_{\mc H}$ is not automatic, it is proved via part (a) for $\ep = 0$ and a more detailed
study of $EP_{W^e} = EP_{\mc H (\mc R ,q^0)}$ \cite[Theorem 3.2]{OpSo1}.
$\qquad \Box$ \\[2mm]

The pairing $EP_{\mc H}$ extends naturally to a Hermitian form on $G_\C (\mc H)$, say complex
linear in the second argument. By Theorem \ref{thm:EP}.c it factors through the quotient
\[
\mr{Ell} (\mc H) := G_\C (\mc H) \Big/ \sum_{P \subset F_0, \R P \neq \mf a^*}
\mr{Ind}_{\mc H^P}^{\mc H} \big( G_\C (\mc H^P) \big)
\]
Following \cite{Opd-ICM} we call Ell$(\mc H)$ the space of elliptic characters of $\mc H$. Notice
that Ell$(\mc H) = 0$ and $EP_{\mc H} = 0$ if the root datum $\mc R$ is not semisimple.

\begin{lem}\label{lem:Elltemp}
The composite map $G_\C (\mc S) \to G_\C (\mc H) \to \mr{Ell} (\mc H)$ is surjective.
\end{lem}
\noindent \emph{Proof.} We may and will assume that $\mc R$ is semisimple.
We have to show that every irreducible $\mc H$-representation $\pi$ that does not vanish
in Ell$(\mc H)$, can be written as a linear combination of tempered representations and of
representations induced from proper parabolic subalgebras.
Recall \cite[Section 2.2]{Sol-Irr} that a Langlands datum is a triple $(P,\sigma,t)$ such that
\begin{itemize}
\item $P \subset F_0$ and $\sigma$ is an irreducible tempered $\mc H_P$-representation;
\item $t \in T^P$ and $|t| \in T^{P++}$.
\end{itemize}
The Langlands classification \cite[Theorem 2.2.4]{Sol-Irr} says that the $\mc H$-representation
$\pi (P,\sigma,t)$ has a unique irreducible quotient $L(P,\sigma,t)$ and that there is
(up to equivalence) a unique Langlands datum such that $L(P,\sigma,t) \cong \pi$.

If $P = F_0$, then $T^P = \{1\}$ because $\mc R$ is semisimple.
So $\mc H_P = \mc H^P = \mc H$ and $\pi \cong \sigma$, which by definition is tempered.

Therefore we may suppose that $P \neq F_0$. Since $\pi (P,\sigma,t)$ is induced from $\mc H^P$,
we have $\pi = L(P,\sigma,t) - \pi (P,\sigma,t)$ in Ell$(\mc H)$. By \cite[Lemma 2.2.6.b]{Sol-Irr}
\[
\pi (P,\sigma,t) - L (P,\sigma,t) \in G_\C (\mc H)
\]
is a sum of representations $L(Q,\tau,s)$ with $P \subset Q$ and
$\norm{cc_P (\sigma)} < \norm{cc_Q (\tau)}$, where $cc_P (\sigma)$ is as in
\eqref{eq:ccdelta}. Given the central character of $\pi$ (an element of $T/W_0$),
there are only finitely many possibilities for $cc_P (\sigma)$. Hence we can deal with
the representations $L(Q,\tau,s)$ via an inductive argument. $\qquad \Box$
\\[2mm]

From \cite[Lemma 4.2.3.a]{Sol-Irr} we know that $\tilde \sigma_0 : \mr{Mod}_f (\mc H) \to
\mr{Mod}_f (W^e)$ commutes with parabolic induction, so it induces a linear map
\begin{equation}
\sigma_{\mr{Ell}} : \mr{Ell}(\mc H) \to \mr{Ell}(W^e) = \mr{Ell} \big( \mc H (\mc R ,q^0) \big) .
\end{equation}
\begin{thm}\label{thm:sigmaEll}
The pairings $EP_{\mc H}$ and $EP_{W^e}$ induce Hermitian inner products on respectively
Ell$(\mc H)$ and Ell$(W^e)$, and the map $\sigma_{\mr{Ell}}$ is an isometric bijection.
\end{thm}
\noindent \emph{Proof.}
By Lemma \ref{lem:Elltemp} and \cite[(3.35)]{Sol-Irr}, $\sigma_{\mr{Ell}}$ is a linear bijection.
According to \cite[Theorem 3.2.b]{OpSo1} $EP_{W^e}$ induces a Hermitian inner product on
Ell$(W^e)$, and by Theorem \ref{thm:EP} $\sigma_{\mr{Ell}}$ is an isometry. Therefore the
sesquilinear form on Ell$(\mc H)$ induced by $EP_{\mc H}$ is also a Hermitian inner product.
$\qquad \Box$
\vspace{4mm}
