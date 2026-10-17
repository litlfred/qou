---
doc_id: arxiv-1204.4824v2
doc_title: "Spectral networks"
section_id: sec-006-34-enhanced-degeneracies
section_title: "Enhanced degeneracies"
section_number: 3.4
pages: 16-17
source_pdf: 1204.4824v2.pdf
source_sha256: bf01cbaa5a8712c8
toc_source: outline
text_source: latex
latex_prose_ratio: 0.924
latex_coverage_ratio: 0.667
doc_brief: "Spectral networks — We introduce new geometric objects called spectral networks. Spectral net- works are networks of trajectories on Riemann surfaces obeying certain local rules."
---
\label{sec:enh-4d}

In the presence of a surface defect $\bS_z$ there is an important enhancement to the 4d BPS degeneracies $\Omega(\gamma)$ \cite{Gaiotto:2011tf}:  they are replaced by numbers
$\omega(\gamma, \bar a) \in \Z$ for any $\gamma \in \Gamma$
and $\bar a \in \Gamma(z_1,z_2)$.  $\omega$ is ``linear'' in its second argument, i.e. it obeys
\begin{equation}
 \omega(\gamma, \bar a + \bar b) = \omega(\gamma, \bar a) + \omega(\gamma, \bar b)
\end{equation}
when $\bar a+\bar b$ is defined (that is, when the end of $\bar a$ coincides with the
start of $\bar b$).  Moreover, $\omega$ obeys
\begin{equation} \label{eq:Omega-def}
\omega(\gamma, \bar a + \gamma') - \omega(\gamma, \bar a) = \Omega(\gamma) \inprod{\gamma, \gamma'}
\end{equation}
for $\gamma' \in \Gamma$.
In particular this equation is sufficient to determine $\Omega$ if we know $\omega$.
(More precisely, it determines $\Omega(\gamma)$ for all $\gamma$ not in the kernel
of $\inprod{\cdot, \cdot}$, i.e. all $\gamma$ which are not pure flavor charges.)

The $\omega(\gamma, \bar a)$ are a bit subtle to interpret directly in terms of
traces over Hilbert spaces.  In \cite{Gaiotto:2011tf} the most general interpretation we found
was in terms of a Hilbert space of ``halo states'' (analogues of the ones studied by Frederik
Denef\footnote{See \cite{Denef:2007vg,Gaiotto:2010be,Andriyash:2010yf,Andriyash:2010qv}
for a description of the halo approach to wall-crossing.}), which induce 2d-4d wallcrossing.
The individual states in this Hilbert space may be interpreted either as 4d particles carrying
charge $\gamma$ or as 2d particles living on the surface defect and
carrying the same charge.
This fact will become relevant in one of our concrete examples,
in \S\ref{sec:nine-hypers}.
