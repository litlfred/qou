---
doc_id: arxiv-1105.2919v1
doc_title: "Chiral eﬀective ﬁeld theory and nuclear forces"
section_id: sec-027-452-renormalization-beyond-leading-order
section_title: "Renormalization beyond leading order"
section_number: 4.5.2
pages: 37-38
source_pdf: 1105.2919v1.pdf
source_sha256: 6d94496f2093ddd0
toc_source: outline
text_source: latex
latex_prose_ratio: 1.0
latex_coverage_ratio: 1.0
doc_brief: "Chiral eﬀective ﬁeld theory and nuclear forces — We review how nuclear forces emerge from low-energy QCD via chiral eﬀective ﬁeld theory. The presentation is accessible to the non-specialist."
---
As shown below, for a quantitative chiral $NN$ potential one needs to advance all the way
to N$^3$LO. Thus, the renormalization issue needs to be discussed beyond LO.
Naively, the most perfect renormalization procedure is the one where the cutoff
parameter $\Lambda$ is carried to infinity while stable results are maintained.
This was done successfully at LO in the work by Nogga {\it et al.}~\cite{NTK05} described above.
At NNLO, the infinite-cutoff renormalization procedure has been investigated 
in~\cite{YEP07} for partial waves with total angular momentum $J\leq 1$ and
in~\cite{VA07} for all partial waves with $J\leq 5$. At N$^3$LO, an investigation
of the $^1S_0$ state exists~\cite{Ent08}.
From all of these works, it is evident that no counter term is effective in partial-waves with
short-range repulsion and only a single counter term can effectively be used in
partial-waves with short-range attraction. Thus, for the $\Lambda \rightarrow \infty$
renormalization prescription, even at N$^3$LO, we have either one or no counter term
per partial-wave state. This is inconsistent with any reasonable power-counting scheme
and, therefore, defies the principals of an EFT.

A possible way out of this dilemma was proposed already in~\cite{NTK05}
and reiterated in a recent paper by Long and van Kolck~\cite{LK08}. In the latter
reference, the authors examine the renormalization of an attractive $1/r^2$ potential
perturbed by a $1/r^4$ correction.
Generalizing their findings, they come to
the conclusion that, for any attractive $1/r^n$ potential (with $n\geq 2$),
partial waves with low angular momentum $L$ must be summed to all orders
and one contact term is needed for each $L$ to renormalize the LO
contribution. However, there exists
an angular momentum $L_p$ ($L_p\approx 3$ for the nuclear case, cf.\ Ref. ~\cite{NTK05}), 
above which the leading order can be calculated perturbatively. 
In short, naive dimensional analysis (NDA) does not apply at LO below $L_p$.
However, once this failure of NDA is corrected at LO, higher order corrections
can be added in perturbation theory using counterterm that follow NDA~\cite{LK08}.

Reference~\cite{LK08} used just a toy model and, therefore, a full investigation 
using the chiral expansion is needed to answer the question 
if this renormalization approach will work for the realistic nuclear force.
A first calculation of this kind for the $S$ waves was recently performed by
Valderrama~\cite{Val09}. The author renormalizes the LO interaction nonperturbatively
and then uses the LO
distorted wave to calculate the 2PE contributions at NLO and NNLO
perturbatively. It turns out that perturbative renormalizability requires the introduction
of three counterterms in $^1S_0$ and six in the coupled $^3S_1-^3D_1$
channels. 
Thus, the number of counterterms required in this scheme is larger than in the
Weinberg scheme, which reduces the predictive power. For a final evaluation
of this approach, also the results for $P$ and $D$ waves are needed, which
are not yet published.

However, even if such a project turns out to be successful for $NN$ scattering,
there is doubt if the interaction generated in this approach is of any use
for applications in nuclear few- and many-body problems.
In applications, one would first have to solve the many-body problem
with the renormalized LO interaction, and then add higher order corrections in
perturbation theory.
However, it was shown in a recent paper~\cite{Mac09} that the renormalized LO
interaction
is characterized by a very large tensor force from 1PE. This is no surprise since
LO is renormalized with $\Lambda \rightarrow \infty$ implying that the 1PE,
particularly its tensor force, is totally uncut.
As a consequence of this, the wound integral in nuclear matter, $\kappa$,
comes out to be about 40\%. The hole-line and coupled cluster expansions
are know to converge $\propto \kappa^{n-1}$
with $n$ the number of hole-lines or particles per cluster~\cite{Bra67,Day67,Bet71}.
For conventional nuclear forces, the wound integral is typically between 5 and 10\%
and the inclusion of three-body clusters (or three hole-lines) are needed to
obtain converged results in the many-body system~\cite{FOS04,Hag08,DW85}.
Thus, if the wound integral is 40\%, probably, up to six hole-lines need to be
included for approximate convergence. Such calculations are not feasible even with
the most powerful computers of today and will not be feasible any time soon.
Therefore, even if the renormalization procedure proposed in~\cite{LK08} will work
for $NN$ scattering, the interaction produced will be highly impractical (to say
the least) in applications in few- and many-body problems because of convergence problems
with the many-body energy and wave functions.
