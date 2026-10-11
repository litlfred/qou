---
doc_id: arxiv-0906.1500v4
doc_title: "Twisted Alexander invariant and non-abelian Reidemeister torsion for hyperbolic three-manifolds"
section_id: sec-034-822-computation-of-ϕadρ
section_title: "Computation of ∆ ϕ⊗Ad◦ρ"
section_number: 8.2.2
pages: 24-25
source_pdf: 0906.1500v4.pdf
source_sha256: 9a586f6d134ca47f
doc_brief: "Twisted Alexander invariant and non-abelian Reidemeister torsion for hyperbolic three-manifolds — W e study a computational method of the hyperbolic Reidemeister torsion (also called in the"
text_source: latex
latex_prose_ratio: 0.837
latex_coverage_ratio: 1.0
---
By using the Multiplicativity Lemma, we have 
\[
\PolyTors{\cup_{\ell=1}^b T^2_\ell}{\otAd{\varphi}{\rho}}(t) 
= (-1)^{b-1}
\PolyTors{T^2_b}{\otAd{\varphi}{\rho}}(t)
\cdot
\PolyTors{\cup_{\ell=1}^{b-1} T^2_\ell}{\otAd{\varphi}{\rho}}(t).
\]
Hence we have
$$

  \PolyTors{\bord M}{\otAd{\varphi}{\rho}}(t) = 
  (-1)^{b(b-1)/2}
  \prod_{\ell=1}^b
  \PolyTors{T^2_\ell}{\otAd{\varphi}{\rho}}(t).
$$
Furthermore a direct computation provides the following lemma:
\begin{lemma}\label{lemma:Torus}
  The torsion $\PolyTors{T^2_\ell}{\otAd{\varphi}{\rho}}(t)$ of the
  $\ell$-th component of $\bord M$ with the homology orientation given by
  the ordered basis $\{\bbrack{T^2_\ell}, \bbrack{\lambda_\ell},
  \bbrack{\mu_\ell},\bbrack{p_\ell}\}$ is equal to $+1$.
\end{lemma}

As a consequence, the twisted Alexander invariant of $\partial M$ is given by:
\begin{equation}\label{Eq:torsionbound}
\PolyTors{\bord M}{\otAd{\varphi}{\rho}}(t) = (-1)^{b(b-1)/2}.
\end{equation}


\subsubsection{Computation of $\PolyTors{(M, \bord M)}{\otAd{\varphi}{\rho}}(t)$.}
Here we use the duality properties of torsion proved by M. Farber and
V. Turaev in ~\cite{FarberTuraev:PR_metric}. We write the torsion
$\PolyTors{(M, \bord M)}{\otAd{\varphi}{\rho}}(t)$ in the right hand
side of Equation~$(\ref{eqn:1st_step_duality})$ as the torsion in the left
hand side with a sign term. Let $(M', \bord M')$ denotes the dual cell
decomposition of $(M, \bord M)$. Using the invariance of the Reidemeister torsion under
subdivisions of CW--pairs we obtain :
\[
\PolyTors{(M, \bord M)}{\otAd{\varphi}{\rho}}(t) = \PolyTors{(M',
  \bord M')}{\otAd{\varphi}{\rho}}(t).
\]
Let ${\rho}^{\star}\colon \pi_1(M) \to \SL$ be the following
representation
\[
{\rho}^{\star} = \left(
  \begin{smallmatrix}
    0 & 1\\
    -1& 0
  \end{smallmatrix}
\right)\rho \left(
  \begin{smallmatrix}
    0 & 1\\
    -1& 0
  \end{smallmatrix}
\right)^{-1}.
\]
Using the invariance of the Reidemeister torsion under conjugation of representations
we thus have
\[
  \PolyTors{(M, \bord M)}{\otAd{\varphi}{\rho}}(t)
  = \PolyTors{(M', \bord M')}{\otAd{\varphi}{\rho}}(t) 
  = \PolyTors{(M', \bord
    M')}{\otAd{\varphi}{{\rho}^{\star}}}(t).
\]

Observe that the pair $(M', \bord M')$ and the representation
$\otAd{\varphi}{{\rho}^{\star}}$ give the dual chain complex
of $M$ twisted by the representation $\otAd{\overline{\varphi}}{\rho}$, \ie, the
$\sllt_{{\rho}^{\star}}$-twisted chain complex $C_*(M', \bord
M';\sllt_{{\rho}^{\star}})$ can be identified with the dual chain complex of
$C_*(M;\msllrho{\overline{t}})$.  By using this identification and the
duality of torsion in~\cite{FarberTuraev:PR_metric}, the torsion
$\PolyTors{(M, \bord M)}{\otAd{\varphi}{\rho}}(t)$ is expressed as
\begin{align}\label{eqn:dualtorsion}
  \PolyTors{(M, \bord M)}{\otAd{\varphi}{\rho}}(t) &=
  \PolyTors{(M', \bord M')}{\otAd{\varphi}{{\rho}^{\star}}}(t) \nonumber \\
  &=
  (-1)^{s(H_*(M;\IR))+s(C_*(M;\IR))}\cdot(-1)^{s(C_*(M;\sllrhot))}\cdot
  \PolyTors{M}{\otAd{\overline{\varphi}}{\rho}}(t).
\end{align}
Here $s(C_*) = \sum_{q=1}^m \alpha_{q-1}(C_*)\alpha_q(C_*)$ for a chain
complex $C_*=C_m\oplus \cdots \oplus C_0$, with
$\alpha_q(C_*)=\sum_{j=0}^q\dim C_j$.  Further observe the sign term
difference between Farber--Turaev's formula and
Equation~(\ref{eqn:dualtorsion}): here the sign term
$\sum_{q=0}^{(m-1)/2}\alpha_{2q}(C_*)$ used
in~\cite{FarberTuraev:PR_metric} is omitted from $s(C_*)$ because we use
the complex $C_*(M', \bord M';\sllrhot)$ instead of the dual complex
of $C_*(M;\sllrhot)$.

The first sign $(-1)^{s(H_*(M;\IR))+s(C_*(M;\IR))}$
in~Equation~(\ref{eqn:dualtorsion}) comes from the duality of the sign
terms $\tau_0$ in $\PolyTors{(M, \bord M)}{\otAd{\varphi}{\rho}}(t)$
and the second one $(-1)^{s(C_*(M;\sllrhot))}$
in~Equation~(\ref{eqn:dualtorsion}) comes from the duality of torsions for
$C_*(M; \sllrhot)$.  Since $s(C_*(M;\IR))$ and $s(C_*(M;\sllrhot))$
are equal in $\ZZ/2\ZZ$, it turns out that
\begin{equation}\label{eqn:duality_torsion}
  \PolyTors{(M, \bord M)}{\otAd{\varphi}{\rho}}(t)
  =
  (-1)^{s(H_*(M;\IR))}
  \PolyTors{M}{\otAd{\overline{\varphi}}{\rho}}(t).
\end{equation}


\subsubsection{Conclusion}
Substituting $\nu =1$, $s(H_*(M;\IR)) = b+1$ and
Equation~(\ref{eqn:duality_torsion}) into
Equation~$(\ref{eqn:1st_step_duality})$ we obtain that
\begin{equation}\label{eqn:2nd_step_duality}
  \PolyTors{M}{\otAd{\varphi}{\rho}}(t)
  =\epsilon (-1)^{b}
  \PolyTors{\bord M}{\otAd{\varphi}{\rho}}(t)
  \PolyTors{M}{\otAd{\overline{\varphi}}{\rho}}(t).
\end{equation}
Finally, using

Equation~(\ref{Eq:torsionbound}),
we can see that Equation~(\ref{eqn:2nd_step_duality}) turns into
$$
\PolyTors{M}{\otAd{\varphi}{\rho}}(t)
=\epsilon (-1)^{b+b(b-1)/2}
\PolyTors{M}{\otAd{\overline{\varphi}}{\rho}}(t)
=\epsilon (-1)^{b(b+1)/2}
\PolyTors{M}{\otAd{\overline{\varphi}}{\rho}}(t)
$$
which achieves the proof of Theorem~\ref{theorem:symmetry_torsion}.
\qed
