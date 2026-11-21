---
doc_id: arxiv-2505.02719v2
doc_title: "On the Palais-Smale condition in geometric knot theory"
section_id: sec-004-outline-of-the-paper
section_title: "Outline of the paper"
section_number: null
pages: 7-8
source_pdf: 2505.02719v2.pdf
source_sha256: 1803d10aa55c18cf
toc_source: outline
text_source: latex
latex_prose_ratio: 0.94
latex_coverage_ratio: 0.962
doc_brief: "On the Palais-Smale condition in geometric knot theory — We prove that various families of energies relevant in geometric knot theory satisfy the Palais–Smale condition (PS) on submanifolds of"
---
In \Cref{sec:PS-abstract} we develop sufficient criteria for the  validity of the (PS)-condition
in the abstract setting of general submanifolds of Hilbert spaces, not only
for a single energy as in \Cref{thm:PS-abstract} but also for total energies with a leading order term and
some additional energy of lower order; see \Cref{cor:PS-total-energy}. Moreover, with
\Cref{thm:gradflow_subconvergence} we
provide a long-time existence result for the gradient flow and subconvergence
to critical points  for energies of class $C^{1,1}_\loc$. 
That this flow preserves symmetry is shown in 
\Cref{prop:symmetry-preserving-grad-flow}. Then we
deduce as simple
consequences the existence of minimizing (PS)-sequences and energy minimizers;
see \cref{koro:critpoint_lowerenergy,koro:minimizer_existence}, as well as \cref{cor:critical+minimizers}
 for an alternative proof 
that works for energies that are only $C^1$. \Cref{sec:arclength} contains the proofs
that the sets $\AL^{1+s}$ and $\AL^{1+s}_\bz$ defined in \cref{eq:ALs}
and \cref{eq:ALsz} are actually smooth submanifolds of the Hilbert space
$H^{1+s}(\R/\Z,\R^n)$ for any $s\in (\frac{1}{2},1]$ and
$\bz\in\R^n$ 
(\Cref{thm:arclength-manifold} and \Cref{thm:arclength-manifold-point}).
We also define suitable projections onto the respective tangent spaces that are needed
in the abstract \Cref{thm:PS-abstract}. Then we prove in \Cref{sec:AL-toplogy} that the open set
of regular knots strongly deformation retracts onto the arclength submanifolds (see \Cref{thm:strong-deformation-ALs}), 
and that connected components
of the arclength submanifolds correspond to 
different knot classes (\Cref{thm:components-knot-classes}). 
In \Cref{sec:AL-critical} we prove that
arclength constrained critical knots are also critical under the more
relaxed fixed-length constraint, still in the abstract general setting; see \Cref{thm:critical-points} and \Cref{cor:critical-points}. 


\Cref{sec:PS-bending+knot-energies} is dedicated to the proofs of
our main results on the Palais--Smale condition. We start in  \Cref{sec:PS-bending}, however,
 with the pure bending energy $\BendingEnergy$
as a prototype example, both for the verification of the (PS)-condition (\Cref{cor:PS_elastic}) and its consequences (arclength-constrained $\BendingEnergy$-critical 
points via minimization
or gradient flows, see \Cref{cor:elastic_crit_gradient-flow}). \Cref{sec:PS-bending} is meant as a
comprehensible blueprint for the more complicated proofs involving non-local terms
in the following \cref{sec:PS-elastic-knot} on total energies, and in
\cref{sec:tanpoint} on the pure tangent-point energies. 
\Cref{thm:bending-knot-energy,thm:bending-moebius-energy} are shown in \cref{sec:PS-elastic-knot}, whereas \Cref{thm:PS-TP} is proven in \cref{sec:tanpoint}.

Finally, \cref{sec:Smoothness} is devoted to the proof of \cref{thm:smoothness}. 
This regularity theorem follows from the combination of the smoothness result for critical points of the pure bending energy $ \BendingEnergy $ (\cref{thm:elastic-smoothness-new}) with those for critical knots of total energies where $ \BendingEnergy $ is the leading order term (\cref{thm:smoothness-T-critical-new}) and of the pure tangent-point energies $ \TPp $ (\cref{thm:smoothness-TP-new}). 

For notational convenience, we use combinations of the indices $\inj,\reg,\mathrm{a}$ to denote \underline{i}njective,
\underline{r}egular, or \underline{a}rclength parametrized
curves in a function space 
$\mathscr{F}$, e.g., $\FS_\inj,$ $\FS_\reg,$ $\FS_\injreg, $
or $\FS_\injunitspeed$.
Furthermore, we denote by $ L(V,W) $ the space of bounded linear maps between normed spaces, abbreviating $ L(V,V)=L(V) $. Unless otherwise specified, $ \left\langle \cdot,\cdot \right\rangle  $ and $ \left|\cdot \right| $, refer to the Euclidean inner product and its induced Euclidean norm, respectively.
