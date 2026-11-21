---
doc_id: arxiv-1204.4824v2
doc_title: "Spectral networks"
section_id: sec-035-83-the-theory-of-9-free-hypermultiplets
section_title: "The theory of 9 free hypermultiplets"
section_number: 8.3
pages: 52-54
source_pdf: 1204.4824v2.pdf
source_sha256: bf01cbaa5a8712c8
toc_source: outline
text_source: latex
latex_prose_ratio: 0.981
latex_coverage_ratio: 0.876
doc_brief: "Spectral networks — We introduce new geometric objects called spectral networks. Spectral net- works are networks of trajectories on Riemann surfaces obeying certain local rules."
---
\label{sec:nine-hypers}

Next let us consider $K=3$ and $C = \IC\IP^1$, with three defects, two ``full'' (at $z = \pm 1$)
and one ``simple'' (at $z = 0$).  This means that at $z = \pm 1$ we impose the condition
that $\phi_2$ has a pole of order $2$ and $\phi_3$ one of order $3$, while
at $z = 0$ we require that the discriminant $\Delta = 27 \phi_3^2 - 4 \phi_2^3$ has a pole
of order $4$.
Concretely this means we take
\begin{equation}
 \phi_2 = \frac{- 3 m^2 + a z + b z^2}{z^2 (z+1)^2 (z-1)^2} \de z^{2}, \qquad \phi_3 = \frac{2 m^3 - a m z - c z^2 + d z^3}{z^3 (z+1)^3 (z-1)^3} \de z^{3}.
\end{equation}
Here $m, a, b, c, d$ are complex parameters, related to the flavor masses which will appear below.

According to \cite{Gaiotto:2009we}
the corresponding theory $S[A_2, C, D]$ is
a theory of $9$ free hypermultiplets, transforming in the $(\mathbf{3}, \mathbf{3}, +1)$ of an
$SU(3) \times SU(3) \times U(1)$ flavor symmetry.  The mass parameter for the $U(1)$ flavor symmetry is $m$, while
those for the two $SU(3)$ are the residues $r_1^{(i)}$, $r_{-1}^{(i)}$ of $\lambda^{(i)}$ at $1$, $-1$ respectively
(these are some functions of $m, a, b, c, d$).
As a test of this statement (and of our whole picture) one
can choose some arbitrary values for $a$, $b$, $c$, $d$, $m$ and study the BPS spectrum.
We should expect to find $9$ BPS multiplets,
corresponding to the quanta of the elementary hypermultiplet fields,
 carrying charges $\gamma(i,j)$ for $1 \le i,j \le 3$.
The expected central charges of these BPS multiplets are determined by the flavor mass parameters:
\begin{equation}
 Z_{\gamma(i,j)} = 2 \I (-m + r_1^{(i)} + r_{-1}^{(j)}).
\end{equation}

We found it simplest to study the spectrum in the regime where $\abs{m} \gg \abs{r_{\pm 1}^{(i)}}$.
In this regime the $4$ branch points coalesce into two pairs,
each pair sitting very close to one of the two full punctures.
For several chosen values of parameters in this regime,
we indeed found $9$ BPS multiplets with exactly the predicted central charges.
See Figure \ref{fig:nine-hypers} for an example.
\insfigscaled{nine-hypers}{0.28}{The cutoff spectral networks $\wnet_\vartheta[\Lambda]$ where $\Lambda e^{\I \vartheta}$ runs over the $9$ values $\half Z_{\gamma(i,j)}$, and we
have fixed parameters such that $\abs{m} \gg \abs{r_{\pm 1}^{(i)}}$.  In each network
we see a pair of $\cS$-walls meeting head-to-head, thus combining into a single path,
highlighted in red;
this corresponds to a BPS hypermultiplet with central charge $Z_{\gamma(i,j)}$.}

In addition we found $6$ extra BPS multiplets, $3$ associated to each of the $2$ full punctures,
with central charges
\begin{equation}
 Z_{\gamma_{\pm 1}(i,j)} = 2 \I (r_{\pm 1}^{(i)} - r_{\pm 1}^{(j)}) \qquad (i > j).
\end{equation}
(Taking $i < j$ in this formula gives the central charges for the corresponding antiparticles.)
In the regime we are considering, these multiplets are represented by small loops
around the punctures.
They might at first seem unexpected, but they have a natural explanation:
they do not represent 4d particles at all but rather 2d particles living on the surface defect
$\bS_z$.  Indeed,
as we emphasized in \cite{Gaiotto:2011tf}, the quantity $\omega(\gamma, a)$
in general must be interpreted as a sum of contributions from 4d particles carrying charge
$\gamma$ and 2d particles carrying the same charge. The phenomenon that a closed loop around
a puncture represents a 2d particle carrying flavor charge
also arose there, in the context of the $\IC\IP^1$ sigma model.
