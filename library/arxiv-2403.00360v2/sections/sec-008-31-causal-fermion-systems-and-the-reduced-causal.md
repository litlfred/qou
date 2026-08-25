---
doc_id: arxiv-2403.00360v2
doc_title: "CAUSAL FERMION SYSTEMS AND OCTONIONS"
section_id: sec-008-31-causal-fermion-systems-and-the-reduced-causal
section_title: "Causal Fermion Systems and the Reduced Causal Action Principle"
section_number: 3.1
pages: 10-11
source_pdf: 2403.00360v2.pdf
source_sha256: b0764ca18a83a84f
doc_brief: "CAUSAL FERMION SYSTEMS AND OCTONIONS — We compare the structures and methods in the theory of causal fermion systems with approaches to fundamental physics based on division algebras, in par- ticular"
---
begin with the general definition of a causal fermion system.
Definition 3.1. (causal fermion systems) Given a separable complex Hilbert space H
with scalar product ⟨.|.⟩H and a parameter n∈ N (the “spin dimension”), we let F⊂
L(H) be the set of all symmetric operators on H of finite rank, which (counting
multiplicities) have at most n positive and at most n negative eigenvalues. On F we
are given a positive measure ρ (defined on a σ-algebra of subsets of F). We refer
to (H, F,ρ ) as a causal fermion system .
A causal fermion system describes a spacetime together with all structures and
objects therein. In order to single out the physically admissible causal fermion systems,
one must formulate physical equations. To this end, we impose that the measure ρ
should be a minimizer of the causal action principle, which we now introduce. For
brevity of the presentation, we only consider the reduced causal action principle where
the so-called boundedness constraint has been incorporated by a Lagrange multiplier
term. This simplification is no loss of generality, because the resulting Euler-Lagrange
(EL) equations are the same as for the non-reduced action principle as introduced for
example in [39, Section §1.1.1].
For any x,y ∈ F, the product xy is an operator of rank at most 2 n. However,
in general it is no longer a symmetric operator because ( xy)∗ = yx, and this is dif-
ferent from xy unless x and y commute. As a consequence, the eigenvalues of the
operator xy are in general complex. We denote the rank of xy by k≤ 2n. Counting
algebraic multiplicities, we chooseλxy
1 ,...,λ xy
k ∈ C as all the non-zero eigenvalues and
set λxy
k+1,...,λ xy
2n = 0. Given a parameter κ> 0 (which will be kept fixed throughout
this paper), we introduce the κ-Lagrangian and the causal action by
κ-Lagrangian: L(x,y ) = 1
4n
2nX
i,j=1


λxy
i

−

λxy
j

2
+κ
 2nX
j=1

λxy
j

2
(3.1)
causal action: S(ρ) =
ZZ
F×F
L(x,y )dρ(x)dρ(y). (3.2)
The reduced causal action principle is to minimizeS by varying the measure ρ under
the following constraints,
volume constraint: ρ(F) = 1 (3.3)
trace constraint:
Z
F
tr(x)dρ(x) = 1. (3.4)
This variational principle is mathematically well-posed if H is finite-dimensional. For
a review of the existence theory and the analysis of general properties of minimizing
measures we refer to [52, Chapter 12].
CAUSAL FERMION SYSTEMS AND OCTONIONS 11
