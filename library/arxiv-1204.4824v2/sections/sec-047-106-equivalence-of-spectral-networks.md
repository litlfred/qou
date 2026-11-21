---
doc_id: arxiv-1204.4824v2
doc_title: "Spectral networks"
section_id: sec-047-106-equivalence-of-spectral-networks
section_title: "Equivalence of spectral networks"
section_number: 10.6
pages: 68-70
source_pdf: 1204.4824v2.pdf
source_sha256: bf01cbaa5a8712c8
toc_source: outline
text_source: latex
latex_prose_ratio: 0.956
latex_coverage_ratio: 0.946
doc_brief: "Spectral networks — We introduce new geometric objects called spectral networks. Spectral net- works are networks of trajectories on Riemann surfaces obeying certain local rules."
---
\label{subsubsec:EqivalentGSN}

Given a nondegenerate spectral network $\wnet$
we have constructed a corresponding nonabelianization map $\Psi_\wnet$.
It is natural to ask how this map depends on $\wnet$.

We can get some intuition by remembering previous results about the case $K=2$.  In that case, as already mentioned
in \S\ref{sec:k2-examples}, $\wnet$ determines
an ideal triangulation $T(\wnet)$ of $C$ up to isotopy.  $T(\wnet)$ does not change if we vary $\wnet$ by an isotopy (while holding $\Sigma$ fixed).
Moreover, the map $\Psi_\wnet$ in this case only depends on $T(\wnet)$.  So we find that $\Psi_\wnet$ is an isotopy invariant of $\wnet$.

We now extend this discussion to general $K$.  We begin by defining a notion of equivalence between
nondegenerate spectral networks.  Our experience from the case $K=2$ suggests that equivalence should at least include isotopy.
In fact, for $K > 2$ it will be natural to
allow even some moves which are \ti{not} isotopies.  Given two
nondegenerate spectral networks $\wnet$ and $\wnet'$, an
\ti{equivalence} between $\wnet$ and $\wnet'$ is a one-parameter family of path-lifting rules
$\bF(\cdot, t)$ to coverings $\Sigma(t)$, such that:

\begin{description}
\item[E1.] $\bF(\cdot, 0) = \bF(\cdot, \wnet)$ and $\bF(\cdot, 1) = \bF(\cdot, \wnet')$.

\item[E2.] For any point $\tz$ on $\tilde{C}$ and pair $0 \le t_1 \le t_2 \le 1$, there exists a formal sum of paths
$R(\tz, t_1, t_2)$, such that for any path $\wp$ from $\tz_1$ to $\tz_2$ we have
\begin{equation} \label{eq:equalpt}
 \bF(\wp, t_2) = R(\tz_1, t_1, t_2) \bF(\wp, t_1) R(\tz_2, t_1, t_2)^{-1}.
\end{equation}
\end{description}
The point of this definition is that if $\wnet$ and $\wnet'$ are connected by an equivalence then we have
\begin{equation} \label{eq:equalpsi}
\Psi_\wnet = \Psi_{\wnet'}.
\end{equation}
(The meaning of the equal signs in \eqref{eq:equalpt}, \eqref{eq:equalpsi} has
to be clarified in case the coverings $\Sigma(t)$ vary with $t$:  in this case
we identify the different coverings using the ``Gauss-Manin'' parallel transport induced by
the family $\{\Sigma(t)\}$.)

One natural way of getting an equivalence is to consider a 1-parameter family of nondegenerate spectral networks $\wnet(t)$
and take $\bF(\cdot, t) = \bF(\cdot, \wnet(t))$.  In this case $R(\tz, t_1, t_2)$ is a product,
with one factor of the form $(1 + \sum_{\nu \in \cS_c(t)} \bX_{\ba(\nu)})$ for each $t$ with $t_1 \le t \le t_2$
such that $z$ lies on an $\cS$-wall $p_c(t)$ in $\wnet(t)$.

Here are some examples of equivalences:
\begin{description}
\item[M1.] An \ti{isotopy}.  This is a one-parameter family of spectral networks $\wnet(t)$ subordinate to coverings
$\Sigma(t)$, such that the $\Sigma(t)$ vary continuously in the obvious sense (in particular the branch points move continuously),
each wall $p_c$ varies by isotopy, and the joints $z_\mu$ move continuously. The combinatorics of $\wnet(t)$ do not change during
an isotopy.

\insfig{infinity-crossing}{Crossing at a defect:  an equivalence which relates two non-isotopic spectral networks.}
\item[M2.] A \ti{crossing at a defect}.  This is a family $\wnet(t)$ which implements a
move as illustrated in Figure \ref{fig:infinity-crossing}.  Here the combinatorics of the network
do change at the critical value $t = t_c$.  Nevertheless the family gives an equivalence.

\insfig{bubble}{Bubble:  an equivalence which relates two non-isotopic spectral networks.}
\item[M3.] A \ti{bubble}.  This is a family $\wnet(t)$ which implements a
move as illustrated in Figure \ref{fig:bubble}.

\insfig{branch-point-traversal}{Branch point traversal:  an equivalence which relates two non-isotopic spectral networks.}
\item[M4.] A \ti{traversal of a branch point}.  This is a family $\wnet(t)$ which implements a
move as illustrated in Figure \ref{fig:branch-point-traversal}.  The member $\wnet(t_c)$ strictly speaking is not
quite a spectral network according to our definition, because of the extra $kj$ lines passing through the branch point;
nevertheless one can define $\bF(\cdot, t_c)$ by a straightforward extension of our rules, and after so doing,
E1, E2 above are obeyed.

\end{description}

All of these equivalences really occur in practice, e.g. in families $\wnet_\vartheta$ as $\vartheta$
varies.  We emphasize that these equivalences are \ti{not} the jumps of $\wnet_\vartheta$ which we studied in
\S\ref{sec:K-walls}:  those jumps generally connect spectral networks which are \ti{inequivalent} in our sense.
