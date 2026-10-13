---
doc_id: arxiv-2104.07437v4
doc_title: "Peacock patterns and new integer invariants in topological string theory"
section_id: sec-002-21-perturbative-series-in-topological-string-the
section_title: "Perturbative series in topological string theory"
section_number: 2.1
pages: 5-7
source_pdf: 2104.07437v4.pdf
source_sha256: a0f28a6b61618467
toc_source: outline
text_source: latex
latex_prose_ratio: 0.981
latex_coverage_ratio: 0.996
doc_brief: "Peacock patterns and new integer invariants in topological string theory — Topological string theory near the conifold point of a Calabi–Yau threefold gives rise to factorially divergent power series"
---
In this section, $X$ will be a CY threefold, compact or non-compact. 
We will denote by $\boldsymbol{T}=(T_1, \cdots, T_r)$ its complexified K\"ahler moduli. In the case of toric CY threefolds, K\"ahler moduli can be of two types: ``true" moduli, denoted by $\bt$, or mass parameters $\bm=(m_1, \cdots, m_s)$ (see e.g. \cite{hkp}). In topological string theory, the basic 
objects are the genus $g$ free energies $F_g (\bT)$, which can be regarded as generating functions of 
Gromov--Witten invariants at genus $g$:

\be
\label{gw-series}
F_g(\bT)= \sum_{\bd} N_{g, \bd}\, \re^{-\bd \cdot \bT}. 
\ee

In this equation, $\bd=(d_1, \cdots, d_r)$ are non-negative integers representing a two-homology class (or vector of degrees), and 
$N_{g, \bd}$ is the Gromov--Witten invariant. 

From the point of view of the global picture of the moduli space provided by mirror symmetry, 
the series (\ref{gw-series}) is an expansion near the large radius
point.





The moduli space is covered by overlapping open patches, each of which
is parametrised by a different set of so-called flat coordinates,
related by electromagnetic duality transformations in
${\rm Sp}(2r, \IZ)$, or changes of frames.

In each frame we have different genus $g$ free energies, related among themselves by formal Fourier transforms \cite{abk}. 
In addition, there are preferred choices of frame associated 
to particular points in moduli space. We will be interested in particular in the free energies associated to a special point 
in the conifold locus of moduli space. When there is a single 
K\"ahler parameter, the conifold locus is a point. In the multi-parameter, toric case, 
it has been noted in \cite{cgm} that there exists a particular point in the conifold locus 
where its connected components cross transversally. We will call this point the {\it maximal conifold point}, 
as in \cite{cgm, cgum}\footnote{In the compact case there seem to exist analogues of the maximal 
conifold point in various examples, but points where components cross transversally might not be unique.}. There is a special 
choice of frame and flat coordinates $\blambda=(\lambda_1, \cdots, \lambda_r)$ such that the maximal conifold point is located at

\be
\blambda=0. 
\ee

The free energies in this frame will be denoted by $\CF_g(\blambda)$, and we will call them {\it conifold free energies}. 
These free energies are given by the sum of a singular part $\CF_g^{\rm s}(\blambda)$ with a universal structure \cite{gv-conifold}, and a 
regular part $\CF_g^{\rm r}(\blambda)$:

\be
\CF_g(\blambda)=\CF_g^{\rm s}(\blambda)+ \CF_g^{\rm r}(\blambda).
\ee

The singular part has a pole of order $2g-2$ at the maximal conifold point, for $g\ge 2$, and logarithmic singularities for 
$g=0,1$. More precisely, it has the structure

\be
\label{con-sr}
\CF_g^{\rm s}(\blambda)={B_{2 g} \over 2g(2g-2)} \sum_{i=1}^r \lambda_i^{2-2g}, \qquad g \ge 2. 
\ee

The regular part $\CF_g^{\rm r}(\blambda)$ is of the form 

\be
\label{cr-exp}
\CF_g^{\rm r}(\blambda)= \sum_{n_i \ge 0} c_{g; n_1, \cdots, n_r} \lambda_1^{n_1} \cdots \lambda_r^{n_r},
\ee

and it is an analytic function at the maximal conifold point. The
coefficients $c_{g;n_1, \cdots, n_r}$ (except for a finite number)
belong to an algebraic number field which depends on the geometry of
the CY threefold. For example, in the case of local $\IP^2$ (the
canonical bundle of $\IP^2$), which has a single modulus, the number
field is $\mathbb{Q}[{\sqrt{-3}}]$, and we have

\be
\label{f0ex}
\ba
\CF_0^{\rm r}(\lambda)&= -\frac{3 V}{4 \pi^2}\lambda  -\frac{\pi^2}{9 \sqrt{3}}\lambda^3+\frac{\pi^4}{486}\lambda^4+\frac{56\pi^6}{10 935 \sqrt{3}}\lambda^5-\frac{1058 \pi^8}{492075}\lambda^6+\CO(\lambda^7), 
\ea
\ee

where

\be
 \label{eight}
 V= 2 \, {\rm Im}\left( {\rm Li}_2 \left(\re^{\pi \ri \over 3} \right) \right).
 \ee
 

 The expansion of the free energy around the conifold point is
 probably one of the less explored aspects of topological string
 theory. The large radius expansion (\ref{gw-series}) is well
 understood and it can be reformulated in terms of BPS invariants, as
 first noted in \cite{gv}. The expansions around orbifold points also
 have an algebro-geometric interpretation in terms of orbifold
 Gromov--Witten invariants (see e.g.~\cite{abk}), but as far as we
 know, there is no direct geometric interpretation of the coefficients
 $c_{n_1, \cdots, n_r}$ appearing in (\ref{cr-exp}).  The conifold
 expansion should however play an important r\^ole in view of large
 $N$ dualities between string theory and gauge theory. In these
 dualities, string moduli are regarded as 't Hooft parameters in an
 underlying gauge theory, and perturbative gauge theory corresponds to
 the small radius, or tensionless limit of the string. In the case of
 the topological string, large $N$ dualities and the TS/ST
 correspondence suggest that the small radius regime corresponds to
 the conifold locus of moduli space.  In addition, we should regard
 the conifold flat coordinates as 't Hooft parameters,\footnote{Note
   that we choose a slightly unusual convention for $g_s$ with an
   additional minus sign, for reasons explained in footnote
   \ref{fn:gs}.}

\be
\label{quant-kahler}
\lambda_i = -N_i g_s, 
\ee

where $N_i$ are non-negative integers and $g_s$ is the string coupling
constant. The perturbative gauge theory regime corresponds to $N_i$
fixed and $g_s \rightarrow 0$, which means that we should consider the
conifold expansion around $\blambda=0$. If we consider the total free
energy, summed over all genera,

\be
\CF(\blambda, g_s)= \sum_{ g \ge 0} \CF_g(\blambda) (-g_s)^{2g-2},
\ee

we conclude that the analogue of a perturbative gauge theory expansion
is obtained by setting (\ref{quant-kahler}) in (\ref{con-sr}) and
(\ref{cr-exp}). This produces a series in $g_s$ for each choice of the
integers $\bN=(N_1, \cdots, N_d)$:

\be
\CF_{\bN} (g_s)=  \sum_{ g \ge 0} \CF_g(-\bN g_s) (-g_s)^{2g-2}.
\ee

For our purposes, the singular part of the conifold expansion is not
relevant, and we will often consider the partition function, or
exponential of the total free energies.  This defines a family of
formal power series in the string coupling constant

\be
\label{phiN}
\Phi_{\bN} (g_s)= \exp\left( \sum_{ g \ge 0} \CF^{\rm r}_g(-\bN g_s) (-g_s)^{2g-2} \right).
\ee


The series (\ref{phiN}) will be the basic object in this paper. It is
the simplest and more natural formal power series in one variable
obtained from topological string theory on a wide class of CY
manifolds. As we have suggested, it corresponds to a perturbative
gauge theory expansion in a conjectural large $N$ dual gauge theory.
In some cases, the large $N$ dual can be identified explicitly. For
example, if $X$ is the resolved conifold, the large $N$ dual is $U(N)$
Chern--Simons theory on $\IS^3$ \cite{gv-cs}, and the formal power series
(\ref{phiN}) is the perturbative expansion of its partition function
at fixed $N$.

We should note that, if we know the series $\Phi_{\bN} (g_s)$ for all
$r$-tuples of non-negative integers $\bN$, we can reconstruct the power
series $\CF_g(\blambda)$ for all $g \ge 0$. Therefore, the collection
of asymptotic series $\Phi_{\bN} (g_s)$ contain the all-genus
information of perturbative, topological string theory.

Another important motivation to consider the series (\ref{phiN}) is
the TS/ST correspondence formulated in \cite{ghm,cgm}. This
correspondence provides a spectral theory interpretation for
$\Phi_{\bN} (g_s)$, as well as a matrix model interpretation
\cite{mz,kmz}. This will be relevant in concrete calculations of the
integer invariants defined in this section.
