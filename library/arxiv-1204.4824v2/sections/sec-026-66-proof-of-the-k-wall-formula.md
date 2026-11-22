---
doc_id: arxiv-1204.4824v2
doc_title: "Spectral networks"
section_id: sec-026-66-proof-of-the-k-wall-formula
section_title: "Proof of the K-wall formula"
section_number: 6.6
pages: 40-42
source_pdf: 1204.4824v2.pdf
source_sha256: bf01cbaa5a8712c8
toc_source: outline
text_source: latex
latex_prose_ratio: 0.921
latex_coverage_ratio: 0.99
doc_brief: "Spectral networks — We introduce new geometric objects called spectral networks. Spectral net- works are networks of trajectories on Riemann surfaces obeying certain local rules."
---
\label{sec:k-proof}

Here we provide the proofs omitted in \S\ref{sec:f-jump}.

First let us explain why $L(\gamma)$ as defined in \eqref{eq:def-L} is indeed a 1-cycle,
i.e. has no boundary.
For any two-way street $p$, the boundary of $p_\Sigma$ lies over the boundary of $p$.
More precisely, a boundary point of $p$ may be either a branch point or a joint;
$p_\Sigma$ has no boundary over a branch point, but does have a boundary over a joint.
So we need to check that $L(\gamma)$ has no boundary over a joint.
To establish this we consider Figure \ref{fig:six-way-junction}.
\insfig{six-way-junction}{A joint where two-way streets meet.  Each two-way street is shown
slightly ``resolved'', as explained at the end of \S\ref{sec:K-walls}.  The resolution here
is the ``American resolution,'' as appropriate since we are considering the limit
$\vartheta \to \vartheta_c^-$.}
Let $z$ denote the joint in the figure.
The coefficient of $z^{(i)}$ in $\partial L(\gamma)$ is
$\alpha_\gamma(p_1) + \alpha_\gamma(p_2) - \alpha_\gamma(p_3) - \alpha_\gamma(p_4)$, and
we would like to show that this vanishes.  Consider the open paths $\wp$ and $\wp'$.
The constraint of twisted homotopy invariance
says that $F(\wp, \vartheta_c^-) = F(\wp', \vartheta_c^-)$.
In particular, we can look at the pieces on both sides which involve paths which
both begin and end on sheet $i$:
\begin{equation}\label{eq:Fpm-equals}
F(\wp, \vartheta_c^-)_{ii} = F(\wp', \vartheta_c^-)_{ii}.
\end{equation}
Directly computing the two sides of \eqref{eq:Fpm-equals} we obtain
\begin{equation}
 Q(p_1) Q(p_2) = Q(p_3) Q(p_4).
\end{equation}
This amounts to
\begin{equation}
 \alpha_\gamma(p_1) + \alpha_\gamma(p_2) = \alpha_\gamma(p_3) + \alpha_\gamma(p_4),
\end{equation}
which is what we wanted to show.

Now let us explain why the jump formula \eqref{eq:k-jump} is true.
We will show that
the following hold both
for $\CF(\wp) = F(\wp, \vartheta_c^+)$ and $\CF(\wp) = \cK\left(F(\wp, \vartheta_c^-)\right)$:
\begin{description}
 \item[P1.] $\CF(\wp)$ is a twisted homotopy invariant of $\wp$ (in the sense explained
in \S\ref{sec:tricky-sign}).
 \item[P2.] If $\wp$ does not meet $\wnet_{\vartheta_c}$, then
\begin{equation}
 \CF(\wp) = \CD(\wp).
\end{equation}
 \item[P3.] If $\wp$ and $\wp'$ have endpoints off $\wnet_{\vartheta_c}$, $\CF$ obeys the composition law
\begin{equation}
 \CF(\wp) \CF(\wp') = \CF(\wp \wp').
\end{equation}
 \item[P4.] If $\wp$ crosses $\wnet_{\vartheta_c}$ exactly once at a point $z$ on a one-way street $p$, then $\CF(\wp)$ is of the form
\begin{equation} \label{eq:f-one-way}
 \CF(\wp) = \CD(\wp_+) \left(1 + \sum_{\bar a \in \Gamma_{ij}^s} \mu(a) X_{a_\tz}\right) \CD(\wp_-),
\end{equation}
for some $\mu(a) \in \Z$.
\item[P5.] If $\wp$ crosses $\wnet_{\vartheta_c}$ exactly once at a point $z$ on a two-way street $p$, and the intersection between $\wp$ and $p$
is positive (with respect to the orientation of $p$ as a $ji$ trajectory and the underlying orientation of $C$ as a complex curve),
then $\CF(\wp)$ is of the form
\begin{equation} \label{eq:f-two-way}
 \CF(\wp) = \CD(\wp_+) \left(1 + \sum_{\bar a \in \Gamma_{ji}^s} \mu(a) X_{a_\tz}\right) \left(1 + \sum_{\bar b \in \Gamma_{ij}^s} \mu(b) X_{b_\tz} \right) \CD(\wp_-)
\end{equation}
for some $\mu(a) \in \Z$ and $\mu(b) \in \Z$.
\end{description}

For $\CF(\wp) = F(\wp, \vartheta_c^+)$ these properties follow directly from what we have already said; the most nontrivial one is
P5, which is \eqref{eq:two-way-crossing-1}.  To prove them for
$\CF(\wp) = \CK(F(\wp, \vartheta_c^-))$ is slightly harder.
P1-3 are true of $F(\wp, \vartheta_c^-)$ and clearly preserved by $\CK$.
P4 is also true of $F(\wp, \vartheta_c^-)$, but we have to show it is preserved by $\CK$:
this follows simply from the fact that $\CK$ just multiplies each term by a function of the $X_{\tilde \gamma}$,
which indeed preserves the form \eqref{eq:f-one-way}.  P5 is the only really nontrivial one.  We begin with
the formula \eqref{eq:two-way-crossing-2} for $F(\wp, \vartheta_c^-)$, and need to show that the action of $\CK$
transforms it into the form \eqref{eq:f-two-way}.  Expanding out \eqref{eq:two-way-crossing-2} we find
various classes of terms:
\begin{align}
 F(\wp, \vartheta_c^-)_{ii} &= \wp_+^{(i)} \left( 1 + \sum_{\bar a, \bar b} \mu^-(a) \mu^-(b) X_b X_a \right) \wp_-^{(i)} = Q(p) \wp^{(i)}, \\
 F(\wp, \vartheta_c^-)_{ij} &= \wp_+^{(i)} \left( \sum_{\bar b} \mu^-(b) X_b \right) \wp_-^{(j)}, \\
 F(\wp, \vartheta_c^-)_{ji} &= \wp_+^{(j)} \left( \sum_{\bar a} \mu^-(a) X_a \right) \wp_-^{(i)}, \\
 F(\wp, \vartheta_c^-)_{jj} &= \wp^{(j)}, \\
 F(\wp, \vartheta_c^-)_{kk} &= \wp^{(k)} \quad \text{ for } k \notin \{i,j\}.
\end{align}
Within each class, the terms in the sum over $\bar a, \bar b$
differ only by multiplication by factors $X_{\tilde\gamma}$.  Since $L(\gamma)$ is a multiple of
$\gamma$, it follows that $\inprod{\gamma, L(\gamma)} = 0$.  Hence the action of $\CK$ on each class of terms is independent
of the particular term.  We consider them in turn.  For the $ii$ terms, $\CK$ acts by multiplication by
$\prod_{\gamma \in \Gamma_c} (1 + X_{\tilde\gamma})^{\inprod{\wp^{(i)}, L(\gamma)}}$, but using \eqref{eq:def-L}
we see that $\inprod{\wp^{(i)}, L(\gamma)} = -\alpha_\gamma(p)$
(since $p$ is the only edge of $\wnet$ crossed by $\wp$) and hence this reduces to
multiplication by $Q(p)^{-1}$.  On the $jj$ terms $\CK$ similarly acts by multiplication by $Q(p)$.
On the $ij$ terms the action of $\CK$ is more complicated:  it is multiplication by a new function $H = \prod_{\gamma \in \Gamma_c} (1 + X_{\tilde\gamma})^{\inprod{\wp_+^{(i)} + \bar b + \wp_-^{(j)}, L(\gamma)}}$.  But we have
$\inprod{\wp_+^{(i)} + \bar b + \wp_-^{(j)}, L(\gamma)} = - \inprod{\wp_+^{(j)} + \bar a + \wp_-^{(i)}, L(\gamma)}$ as one readily
sees using the facts that $\cl(\bar a+\bar b)$ is proportional to $L(\gamma)$ and
$\inprod{\wp^{(i)}, L(\gamma)} = - \inprod{\wp^{(j)}, L(\gamma)}$.
It follows that the action of $\CK$ on the $ji$ terms is multiplication by $H^{-1}$.
These facts together are sufficient to imply the desired P5.\footnote{Incidentally, they also imply
that $\CF(\wp)_{jj} = Q(p)$; this and the fact $\CF(\wp) = F(\wp, \vartheta_c^+)$ (which we are
in the process of showing) together prove our remark under \eqref{eq:def-Q}.}

Finally we must explain why these properties actually \ti{determine} $\CF(\wp)$.
As a warm-up, suppose that there are only one-way streets.  In that case we have shown in \S \ref{sec:F-basics}
and \S \ref{sec:wnet} above that the properties P1-P4 are sufficient to determine all of the $\mu(a)$,
and hence also to fix $\CF(\wp)$.
The same kind of argument can be made in the presence of two-way streets; the only new complication is that
the local structure around joints and branch points is more complicated.
Nevertheless, a direct computation
using only the fact that $\CF(\wp)$ obey P1-P5 determines the $\mu(a)$ appearing there
for all charges $a$ oriented out of a joint, in terms of the $\mu(a)$ for charges $a$
oriented into the same joint.
(The resulting explicit formulae are recorded in Appendix
\ref{app:joint-rules}, e.g. \eqref{eq:outgoing-2wayjoint}.)
Inductively we can thus determine the 2d-4d
degeneracies $\mu(a)$ everywhere on $\wnet_{\vartheta_c}$, just as we did in the (generic) case
with only one-way streets.
Having done so the $\CF(\wp)$ are also determined by P1-P5.  This completes the proof.
