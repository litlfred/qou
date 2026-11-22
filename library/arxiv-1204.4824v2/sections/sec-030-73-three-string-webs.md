---
doc_id: arxiv-1204.4824v2
doc_title: "Spectral networks"
section_id: sec-030-73-three-string-webs
section_title: "Three-string webs"
section_number: 7.3
pages: 45-46
source_pdf: 1204.4824v2.pdf
source_sha256: bf01cbaa5a8712c8
toc_source: outline
text_source: latex
latex_prose_ratio: 0.982
latex_coverage_ratio: 0.991
doc_brief: "Spectral networks — We introduce new geometric objects called spectral networks. Spectral net- works are networks of trajectories on Riemann surfaces obeying certain local rules."
---
\label{sec:three-string}

\insfigscaled{three-pronged-network}{0.52}{A new way in which $\cS$-walls can collide, which appears only in
theories with $K > 2$.  The picture shows a patch of $C$ containing three branch points.  $\wnet_\vartheta$
involves both ``primary'' $\cS$-walls born from the branch points (supporting charges $a$, $b$, $c$) and ``secondary'' $\cS$-walls
born from intersections between primary
$\cS$-walls (supporting charges $a+b$, $b+c$, $a+c$.)
At the critical phase $\vartheta = \vartheta_c$, primary and secondary walls collide head-on, along a locus which forms
a three-string finite web.}

When we go beyond $K=2$, we encounter many new and varied phenomena.

The simplest new possibility is shown in Figure \ref{fig:three-pronged-network}.
Near the critical phase $\vartheta = \vartheta_c$, we see \ti{three} pairs of $\cS$-walls nearly colliding head-on.
Each pair consists of one ``primary'' $\cS$-wall, born at a branch point, and one ``secondary'' $\cS$-wall, born at the intersection
between two primary walls.  At the critical phase $\vartheta = \vartheta_c$ each such pair of walls collides along
a two-way street $p$.
Each of the three two-way streets $p$
supports a different pair of two 2d-4d charges, with
all three pairs summing to $\gamma = \cl(\bar a+\bar b+\bar c)$.

We would like to compute the 1-cycle $L(\gamma)$.
Let us focus attention on the two-way street $p$
supporting the 2d-4d charges $\bar a$ and $\bar b+\bar c$.
At $\vartheta < \vartheta_c$,
the $\cS$-wall supporting charge $\bar a$ is emerging directly from a branch point,
and thus has a natural lift $a$ with $\mu(a) = 1$.  The
$\cS$-wall supporting $\bar b+\bar c$, on the other hand, is emerging from a joint where walls supporting $\bar b$ and $\bar c$ intersect.  These two walls
in turn emerge from branch points, so at the joint $\mu^-(b) = 1$, $\mu^-(c) = 1$.
It follows from \eqref{eq:cv-wcf} that the emerging wall has
$\mu^-(b+c) = 1$.  Since these are the only two $\cS$-walls
which collide along $p$, all other $\mu^-(\cdot)$ vanish along $p$.
Plugging into \eqref{eq:def-Q} we obtain
\begin{equation}
 Q(p) = 1 + X_{\cl(a+b+c)}
\end{equation}
and hence, letting $\gamma = \cl(\bar a+\bar b+\bar c)$ with preferred lift $\tilde\gamma = \cl(a+b+c) + H$, for suitable $a,b,c$,
we find $\alpha_\gamma(p) = 1$.  The same result holds for the other two two-way streets $p^n$,
so $L(p)$ is the sum:
\begin{equation}
 L(\gamma) = p^1_\Sigma + p^2_\Sigma + p^3_\Sigma.
\end{equation}
In other words, letting $N$ denote the finite web made up of the three two-way streets $p^n$,
we have
\begin{equation}
 L(\gamma) = N_\Sigma.
\end{equation}
Moreover, $[N_\Sigma] = \gamma$, so the 4d BPS degeneracy here is
\begin{equation}
\Omega(\gamma) = 1.
\end{equation}
So we have found that the finite web $N$, made up of three strings which meet
at a junction, corresponds to a BPS hypermultiplet.
