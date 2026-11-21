---
doc_id: arxiv-2012.00062v3
doc_title: "PEACOCK PATTERNS AND RESURGENCE IN COMPLEX CHERN-SIMONS THEORY"
section_id: sec-009-22-stokes-automorphism
section_title: "Stokes automorphism"
section_number: 2.2
pages: 10-12
source_pdf: 2012.00062v3.pdf
source_sha256: 2aacb7fa43f5e0da
toc_source: outline
text_source: latex
latex_prose_ratio: 0.982
latex_coverage_ratio: 0.923
doc_brief: "PEACOCK PATTERNS AND RESURGENCE IN COMPLEX CHERN-SIMONS THEORY — The partition function of complex Chern-Simons theory on a 3-manifold with torus boundary reduces to a ﬁnite dimensional"
---
\label{sub.stokes}

We will specialize our discussion to the series of interest, namely to
the Borel transform $\wh{\Phi}(x;\zeta)$ of the vector of series
$\Phi(x;\tau)$. The singularities of $\Phi(x;\tau)$ are conjectured to
be in the set~\eqref{Phising} that generates a set of Stokes rays
whose complement is a countable union of open cones in Borel plane.
When $\th$ is in a fixed such cone $C$, the Laplace transform
$s_\th(\Phi)(x;\tau)$ depends on $C$ but not on $\th$.  To compare two
adjacent such cones, let $\iota_{\s,\s'}^{(\ell,k)}$ denote one of the
singularities of $\Phi_\s(x;\tau)$, $\theta$ denote its argument and
$\rho=\re^{\ri\theta}\BR_+$ denote the corresponding Stokes ray.  When
$x$ is generic, a Stokes ray contains a single singularity and the
Laplace integrals to the right and the left of $\rho$ are related by
\begin{equation}
  s_{\theta^+}(\Phi_\s)(x;\tau) =  s_{\theta^-}(\Phi_\s)(x;\tau) +
  \mc{S}_{\s,\s'}^{(\ell,k)}\tx^\ell \tq^k
  s_{\theta^-}(\Phi_{\s'})(x;\tau),
  \label{eq:Sauto}
\end{equation}
where $\mc{S}_{\s,\s'}^{(\ell,k)}$ is the Stokes constant. In matrix
form, the above formula reads
\begin{equation}
\label{lap2}
  s_{\theta^+}(\Phi)(x;\tau) =
  \mfS_{\theta}(\tx;\tq) s_{\theta^-}(\Phi)(x;\tau) 
\end{equation}
where
\begin{equation}
\label{Grho}
\mfS_\th(\tx;\tq)=
I + \mc{S}_{\s,\s'}^{(\ell,k)}\, \tx^\ell \, \tq^k \, E_{\s,\s'}
\end{equation}
where $E_{\s,\s'}$ is the elementary matrix with $(\s,\s')$-entry $1$
and all other entries zero.

More generally, consider two non-Stokes rays $\rho_{\th^+}$ and
$\rho_{\th^-}$ whose arguments satisfy $0 \leq \th^+-\th^- \leq
\pi$. Then, the Laplace integrals are related by
\begin{equation}
\label{lap3}
  s_{\theta^+}(\Phi)(x;\tau) =
  \mfS_{\theta^- \rightarrow \theta^+}(\tx;\tq) s_{\theta^-}(\Phi)(x;\tau) 
\end{equation}
where the Stokes matrices satisfy the factorization property
\begin{equation}
  \mfS_{\theta^- \rightarrow \theta^+ }(\tx,\tq) =
  \prod_{\th^- < \th < \th^+}^{\longleftarrow} \mfS_{\th}(\tx,\tq).
  \label{eq:SRR-fac}
\end{equation}
where the ordered product is taken over the Stokes rays in the cone
genarated by $\rho_{\th^-}$ and $\rho_{\th^+}$. This factorization is
well-known in the classical litetature on WKB (see for instance
Voros~\cite[p.228]{voros} who called it the ``radar method''  for
obvious visual reasons). In our case, there are four
special non-Stokes rays denoted by 
\begin{equation}
\label{4I}
I=\re^{\ri \epsilon}\BR_+,
\qquad II=\re^{\ri (\pi-\epsilon)}\BR_+,
\qquad III=\re^{\ri (\pi+\epsilon)}\BR_+,
\qquad IV=\re^{\ri (2\pi-\epsilon)}\BR_+
\end{equation}
(for $\epsilon>0$ and sufficently small) that belong to the four
distinguished cones (labeled $I,II,III,IV$) adjacent to the real axis
and free of Stokes lines. The corresponding Stokes matrices
\begin{equation}
  \label{SG}
  \ms{S}^+(\tx;\tq) =
  \mf{S}_{I\rightarrow II}(\tx;\tq)\, \mf{S}_{IV\rightarrow I}(\tx;\tq),
  \qquad
  \ms{S}^-(\tx;\tq) =
  \mf{S}_{III\rightarrow IV}(\tx;\tq)\, \mf{S}_{II\rightarrow III}(\tx;\tq)
\end{equation}
that swap two complementary and nearly horizontal half-planes
separated by a line $L$ are the ones that appear in
Conjecture~\ref{conj.asy}. They are related to the matrices
$M_\rho$ in the second part of that conjecture by
\begin{align}
  \mfS_{I\rightarrow II}(\tx;\tq)
  &= (M_{II}(\tx;\tq))^{-1}\cdot M_{I}(\tx;\tq),\quad |\tq|<1\nn
    \mfS_{III\rightarrow IV}(\tx;\tq)
  &= (M_{IV}(\tx;\tq^{-1}))^{-1}\cdot M_{III}(\tx;\tq^{-1}),\quad |\tq|<1\nn
    \mfS_{IV\rightarrow I}(\tx;\tq)
  &= (M_{I}(\tx;\tq))^{-1}\cdot M_{IV}(\tx;\tq),\nn
    \mfS_{II\rightarrow III}(\tx;\tq)
  &= (M_{III}(\tx;\tq))^{-1}\cdot M_{II}(\tx;\tq) \,.
    \label{4G}
\end{align}

We now come to an important feature of our resurgent series,
a unique factorization property for the Stokes matrices reminiscent
of the ``stability data'' description of DT-invariants in
Kontsevich-Soibelman~\cite{KS,KS:stability, KS:wall-crossing}), and
of the properties of BPS spectrum generators in
Gaiotto-Moore-Neitzke~\cite{gmn, gmn2, gmn3}. 

\begin{lemma}
  \label{lem.fac}
  $\ms{S}$
  uniquely determines $\mfS_{\th}$ for all $\th$. 
\end{lemma}

\begin{proof}
  Without loss of generality, we will show that $\ms{S}^+$ uniquely
  determines the Stokes matrices $\mfS_\th$ for all $\th$ such that
  $-\varepsilon < \th < \pi - \varepsilon$ for $\varepsilon>0$ and
  sufficiently small. We have
  \begin{equation}
    \label{SScal}
    \ms{S}^+(\tx;\tq) = \prod_{\s,\s',k,\ell}^{\longleftarrow}
    (I + \calS_{\s,\s'}^{(\ell,k)} \tx^\ell \, \tq^k E_{\s,\s'})
  \end{equation}
  where the product is over all the singularities above the line $L$.
  The entries of the above matrices are in the ring
  $\BZ[\tx^\pm][[\tq]]$.  For each fixed natural number $N$, there are
  only finitely many horizontal lines of singularities in Borel plane,
  of height at most $N$ and within those, there are finitely many
  $\tx$-dots. It follows by induction on $k$ that the finite
  collection $\{\calS_{\s,\s'}^{(\ell,k)}\}_\ell$ is uniquely
  determined from $\ms{S}^+(\tx;\tq)$.
\end{proof}

It follows that we can repackage the information of the Stokes
constants in two matrices $\calS^+$ and $\calS^-$ defined by

\begin{equation}
  \label{calS}
  \calS^\pm(\tx;\tq) = \sum_{\ell,k} \calS_{\s,\s'}^{(\ell,k)}
  \tx^\ell \, \tq^k E_{\s,\s'}
\end{equation}
where the sum in $\calS^+$ (resp. $\calS^-$) is over the singularities
above (resp., below) $L$. The matrices $\calS^\pm(\tx;\tq)$ appear to
have some positivity properties; see Sections~\ref{sub.41stokes}
and~\ref{sub.52stokes} below for the $\knot{4}_1$ and the $\knot{5}_2$
knots.
