---
doc_id: arxiv-2012.00062v3
doc_title: "PEACOCK PATTERNS AND RESURGENCE IN COMPLEX CHERN-SIMONS THEORY"
section_id: sec-008-2-borel-resummation-and-stokes-automorphisms
section_title: "Borel resummation and Stokes automorphisms"
section_number: 2
pages: 9-12
source_pdf: 2012.00062v3.pdf
source_sha256: 2aacb7fa43f5e0da
toc_source: outline
text_source: latex
latex_prose_ratio: 0.954
latex_coverage_ratio: 0.95
---
\label{sec.borel}


\subsection{Borel resummation}
\label{sub.borel}


In this section we briefly review the process of Borel resummation of
a factorially divergent series, its Laplace integral along rays and
the corresponding Stokes automorphism across a Stokes ray. The
material in this section is classical and well-known and is explained
in detail in the books~\cite{Costin:asymptotics,Miller:applied,msauzin},
and in the references therein. We will be following the physics convention
of Borel resummation as found for example in~\cite[Sec. 3.2]{mmbook}
and~\cite[Sec.42.5]{Zinn-Zustin:QFT}, which differs by a factor of
$\tau$ from the Borel resummation found in the math literature.

Borel resummation is a 2-step process to pass from a factorially
divergent series $F(\tau)$ to the analytic function $s(F)(\tau)$
defined in the right half-plane $\Re(\tau)>0$ summarized in the
following diagram
\begin{equation}
  \label{borel-sum}
  F(\tau) \leadsto 
  \wh{F}(\zeta) \leadsto 
  s(F)(\tau) \,.
\end{equation}
Here one starts with a Gevrey-1 a formal power series $F(\tau)$
\begin{equation}
  F(\tau) = \sum_{n=0}^\infty f_n \tau^{n} ,\quad f_n = O(C^n \, n!)
\end{equation}
and defines its Borel stransform $\wh{F}(\zeta)$ by
\begin{equation}
  \wh{F}(\zeta) = \sum_{n=0}^\infty \frac{f_n}{n!} \zeta^n \,.
\end{equation}
It follows that $\wh{F}$ is the germ of an analytic function at
$\zeta=0$. If it analytically continues to an $L^1$-analytic function
along the ray $\rho_\theta:=\re^{\ri\theta}\IR_+$ where
$\theta = \arg \tau$, we define its Laplace transform by 
\begin{equation}
  s_{\theta}(F)(\tau)=
  \int_0^\infty \wh{F}(\tau\zeta) \re^{-\zeta} \rd \zeta=
  \frac{1}{\tau} \int_{\rho_\theta}
  \wh{F}(\zeta)\re^{-\zeta/\tau} \rd \zeta
  \label{eq:brlsum}
\end{equation}






The function $s(F)(\tau)$ is often called the Borel resummation of the
formal power series $F$, and we often suppress the subscript $\theta=0$
when $\tau$ is real and positive.













If we vary $\theta = \arg \tau$ and we do not encounter singularities
of $\wh{F}$, the function $s_\th(F)(\tau)$ is locally analytic. Thus,
the problem is to understand the analytic continuation of $\wh{F}$ and
to analyze what happens to the Borel resummation $s_\theta(F)(\tau)$
when $\theta =\arg(\tau)$ crosses a Stokes ray, i.e., a ray in Borel
plane that contains one or more singularities of $\wh{F}$. This is
described by a Stokes automorphism.


\subsection{Stokes automorphism}
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
