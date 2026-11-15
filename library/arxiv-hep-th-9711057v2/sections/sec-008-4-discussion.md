---
doc_id: arxiv-hep-th-9711057v2
doc_title: "arXiv:hep-th/9711057v2 30 Apr 1998"
section_id: sec-008-4-discussion
section_title: "Discussion"
section_number: 4
pages: 9-10
source_pdf: 9711057v2.pdf
source_sha256: acf5cdd7fe848f43
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.976
latex_coverage_ratio: 1.0
doc_brief: "arXiv:hep-th/9711057v2 30 Apr 1998 — 11 sections: Front matter; Introduction; Random-matrix theory for finite qu"
---
\label{sec4}

We have computed the microscopic spectrum of the massive QCD Dirac
operator, including the microscopic spectral density and the
distribution of the smallest eigenvalue, for an arbitrary number of
flavors, arbitrary quark masses, and arbitrary topological charge.
Our results generalize the previously known results for the
microscopic correlations in the chiral limit \cite{Verb93}.  The
distribution of the smallest eigenvalue was previously known only in
the quenched approximation.  Wherever there is an overlap, our results
agree with those obtained in the recent preprint by Damgaard and
Nishigaki \cite{Damg97}.  It would be very interesting to obtain the
result (\ref{darmnij}) using the supersymmetry method as in
Refs.~\cite{Guhr97a,Jack97a}.  Work in this direction is in progress.

The quantities we have computed in this paper are conjectured to be
universal, i.e., identical to those of QCD, for quark masses of the
order of $1/V$.  This conjecture can be verified straightforwardly in
lattice calculations.  One computes the eigenvalues of the Dirac
matrix and constructs the microscopic spectral density and the
distribution of the smallest eigenvalue by averaging over a sufficient
number of independent gauge field configurations.  The lattice data
can then be compared to the analytical predictions of RMT.  For pure
SU(2) gauge theory without dynamical quarks, this was already done in
Ref.~\cite{Berb97a}, and the agreement was excellent.

Our present calculation applies to full QCD with 3 colors in the
continuum limit.  In the context of lattice QCD, it applies to SU(3)
with dynamical staggered fermions.  The necessary lattice algorithms
are available, e.g., the hybrid Monte-Carlo algorithm for generating
unquenched configurations and the Lanczos algorithm for computing
eigenvalues of large sparse matrices.  Therefore, we are confident
that the results obtained in this paper will be verified in the very
near future.

Given that the analytical results obtained in this paper really
describe QCD, one may ask what their relevance is in practice.  We
list here a few possible applications.  (i) The parameter which
appears in the microscopic quantities contains the absolute value of
the chiral condensate, $\Sigma$.  As we have already seen in quenched
SU(2) \cite{Berb97b}, the analytical information available from RMT
can be used to determine $\Sigma$ and to extract its thermodynamic
limit from very small lattices.  Since otherwise one would have to
perform an extrapolation, this seems to offer an interesting
technological advantage.  (ii) Lattice simulations with light
dynamical quarks are very expensive, and extrapolations to the chiral
limit are difficult.  In RMT, we have computed exact analytical
expressions which apply for very small quark masses, and the chiral
limit can be taken analytically.  One would, therefore, hope that
lattice practitioners can use the analytical information in their
extrapolations to the chiral limit for those quantities that depend on
the small eigenvalues.  (iii) A very interesting issue is topology.
As one approaches the continuum limit on the lattice, one expects zero
modes to appear which give rise to non-zero topological charge $\nu$.
The microscopic quantities we consider are sensitive to topology, and
we have computed them for arbitrary $\nu$.  Hence, one can analyze
lattice results in different sectors of topological charge.  Whether
or not topology is seen on present-day lattices is still a somewhat
controversial issue, and for quenched SU(2) the lattice results of
Ref.~\cite{Berb97a} were consistent with $\nu=0$.  We hope that our
results will prove useful in future analyses of topology.  (iv) The
performance of many lattice algorithms depends on the magnitude of the
smallest eigenvalue.  While RMT cannot predict this magnitude, it
predicts the distribution of $\lambda_{\rm min}$ over the ensemble of
gauge field configurations.  It would be interesting to see if experts
in algorithm development can make use of the analytical information
available from RMT.
