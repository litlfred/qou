---
doc_id: arxiv-0906.1500v4
doc_title: "Twisted Alexander invariant and non-abelian Reidemeister torsion for hyperbolic three-manifolds"
section_id: sec-025-81-reciprocality-properties
section_title: "Reciprocality properties"
section_number: 8.1
pages: 23-23
source_pdf: 0906.1500v4.pdf
source_sha256: 9a586f6d134ca47f
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.614
latex_coverage_ratio: 1.0
doc_brief: "Twisted Alexander invariant and non-abelian Reidemeister torsion for hyperbolic three-manifolds — We study a computational method of the hyperbolic Reidemeister torsion (also called in the literature"
---
The Alexander polynomial $\Delta_K(t)$ of a knot $K \subset S^3$ is
known to be reciprocal in the sense that $\Delta_K(t^{-1}) = \pm t^s
\Delta_K(t)$ from a long time. This property was first observed by
Seifert~\cite{Seifert:1934} and is a consequence of
Poincar\'e duality. Milnor~\cite{Milnor:1962} proved
it again using the interpretation of the Alexander polynomial as an
abelian Reidemeister torsion. Kitano~\cite{Kitano}, Kirk and
Livingston~\cite{KL} observe that Milnor's argument work fine in the
context of twisted Alexander polynomial. Hillman, Silver and
Williams~\cite{HSW:09} give a more general discussion on reciprocality
of twisted Alexander invariants for representations into
$\mathrm{SL}_n(\CC)$. All the known reciprocality formulas are
sign--less. In our situation Milnor's argument also work, and using
the fact that the torsion of $\partial M = \bigcup_{\ell = 1}^b
T_\ell^2$ is trivial, we have the following result, in which the sign
is analyzed in details (\cf~\cite[Theorem 2]{Milnor:1962} and
\cite[Theorem 5.1]{KL}).
We also refer to \cite{FriedlKimKitayama_Poincare}
for duality formulas for the polynomial torsion in more general situations.


\begin{theorem}\label{theorem:symmetry_torsion}
  Let $\bar{\cdot} \colon \ZZ \to \ZZ$ be the involution defined by
  $\bar{t} = t^{-1}$.  If we consider a homomorphism 
  $\varphi \colon \pi_1(M) \to \ZZ$ and its composition $\bar{\varphi}$ 
  with the involution $\bar{\cdot}$, 
  then the polynomial torsion satisfies the following identity 
  up to a factor $t^k\, (k \in \ZZ)$:
  \[
  \PolyTors{M}{\otAd{\varphi}{\rho}}(t^{-1}) = 
  \PolyTors{M}{\otAd{\bar{\varphi}}{\rho}}(t) = 
  \epsilon (-1)^{b(b+1)/2} \PolyTors{M}{\otAd{\varphi}{\rho}}(t).
  \]
  Here $\epsilon$ is the sign of the Reidemeister torsion of the long
  exact sequence in homology associated to the pair $(M, \bord M)$
  with the basis given by the bases of $H_*(\bord M;\IR)$, $H_*(M;\IR)$
  and the Poincar\'e dual bases of $H_*(M;\IR)$ in $H_*(M, \bord
  M;\IR)$ as in Equation~$(\ref{eqn:bases_the_pair})$.
\end{theorem}

\begin{remark}[A duality property for link exteriors]
  As a special case, if $M$ is a link exterior $E_L =S^3 \setminus N(L)$,
  then we can explicitly compute the sign--term in
  Theorem~\ref{theorem:symmetry_torsion}. 
  Proposition~\ref{prop:sign_pair_link_exterior} in Appendix
  gives us the sign $\epsilon = (-1)^{b(b-1)/2}$, where $b$ is the number of boundary components of $M$. Using naturality of
  the polynomial torsion (see Section~\ref{section:naturality}) then the
  following duality for the polynomial torsion
  $\PolyTors{E_L}{\otAd{\varphi}{\rho}}$ holds:
  \begin{align}
    \PolyTors{E_L}{\otAd{\varphi}{\rho}}(t^{-1}) 
      &=(-1)^{b(b-1)/2} \cdot (-1)^{b(b+1)/2} \PolyTors{E_L}{\otAd{\varphi}{\rho}}(t) \nonumber\\
      &=(-1)^b \PolyTors{E_L}{\otAd{\varphi}{\rho}}(t) \label{eqn:symmLink}.
  \end{align}
  In particular, if $L$ is a knot $K$ in $S^3$, then the
  following duality holds:
  \begin{equation}\label{eqn:symmKnot}
    \PolyTors{E_K}{\otAd{\varphi}{\rho}}(t^{-1}) =  
     - \PolyTors{E_K}{\otAd{\varphi}{\rho}}(t).
  \end{equation}
  Equation~(\ref{eqn:symmKnot}), and more generally
  Equation~(\ref{eqn:symmLink}), can be considered as a sign--refined
  version of Milnor's duality Theorem~\cite{Milnor:1962} for
  Reidemeister torsion.
\end{remark}

Our attention is restricted to the composition of an
$\SL$-rerpesentation and the adjoint action.  We refer
to~\cite{FriedlKim:06, FriedlVidussi:survey,
  HSW:09} for reciprocality formulas for other types
of representations.



\subsection{Proof of Theorem~\ref{theorem:symmetry_torsion}}

The proof is essentially based on the Multiplicativity Lemma for
torsions (with sign).  We apply the Multiplicativity Lemma in
Section~\ref{subsection:multiplicativitylemma} for short exact
sequences with the coefficient $\IR$ and $\sllt$ to observe
the relation between the signed torsion of the original chain complex
and that of the dual chain complex.  
With the fact that
$\alpha(C', C'')$ for the coefficients in $\IR$ are same as $\alpha(C',
C'')$ for the coefficients in $\sllt$ in mind, 
the Multiplicativity Lemma for the pair $(M, \bord M)$ yields the following equation for 
the sign--refined torsions:
\begin{equation}\label{eqn:1st_step_duality}
  \PolyTors{M}{\otAd{\varphi}{\rho}}(t)
  =\epsilon(-1)^{\nu}\cdot
  \PolyTors{\bord M}{\otAd{\varphi}{\rho}}(t) \cdot
  \PolyTors{(M, \bord M)}{\otAd{\varphi}{\rho}}(t).
\end{equation}
Here $\nu \in \ZZ/2\ZZ$ is the sign given by the sum
$\nu = 
\sum_{i=0}^3 (\beta_i+1)(\beta'_i+\beta^{''}_i)+\beta'_{i-1}\beta^{''}_i 
\in \ZZ/2\ZZ$ where
$$\beta_i = 
\sum_{r=0}^i \dim_{\IR}H_r(M;\IR), \;\beta'_i = \sum_{r=0}^i
\dim_{\IR}H_r(\bord M;\IR) \text{ and } \beta^{''}_i = \sum_{r=0}^i
\dim_{\IR}H_r(M, \bord M;\IR).
$$

We compute each terms appearing in Equation~(\ref{eqn:1st_step_duality}).


\subsubsection{Computation of the sign $\nu$.}

By our assumption on $M$ and $\bord M$, we observe that $\nu = 1$
in $\ZZ/2\ZZ$.


\subsubsection{Computation of $\PolyTors{\bord M}{\otAd{\varphi}{\rho}}(t)$.}

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
