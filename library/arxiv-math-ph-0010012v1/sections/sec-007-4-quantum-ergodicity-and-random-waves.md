---
doc_id: arxiv-math-ph-0010012v1
doc_title: "From random polynomials to symplectic geometry Steve Zelditch"
section_id: sec-007-4-quantum-ergodicity-and-random-waves
section_title: "Quantum ergodicity and random waves"
section_number: 4
pages: 6-7
source_pdf: 0010012v1.pdf
source_sha256: cd6eca5ccb81ff90
doc_brief: "From random polynomials to symplectic geometry Steve Zelditch — We review some recent results on random polynomials and their generalizations in complex and symplectic geometry."
---
We end with a brief discussion of the connection between random polynomials and quantum chaos.
The intutitive idea that quantum chaotic eigenfunctions should resemble ‘Gaussian random waves’ seems to
have been ﬁrst suggested by M. V. Berry [B]. A precise formulation of this random wave model and some
numerical results are given in [ABST] [HR].
Random spherical harmonics on Sm, or random combinations of eigenfunctions of Laplacians on gen-
eral compact Riemannian manifolds as described above, provide a rather diﬀerent random wave model for
quantum chaotic eigenfunctions. To motivate the model, we recall that the diagonal sums of squares
Sp(λ) =
X
j:λj≤λ
|(Aϕj, ϕj) −¯
σA|p,
(with
¯
σA =
Z
S∗M
σAdµ),
(3)
and their oﬀ-diagonal analogues, are used to characterize eigenfunctions as quantum ergodic, quantum mixing
and so on. Here, A is an observable (zeroth order pseudodiﬀerential operator), σA is its principal symbol.
For quantizations of ergodic systems, Sp(λ) →0 as λ →∞, and it is of some interest to measure the rate
and to relate it to the classical dynamics. In the random spherical harmonics model one has the following
rate (for similar results see [Ze2, ShZe]):
Theorem 4.1. ([Ze1], Lemma (2.15)) Let {ϕNj} be a random orthonormal basis of spherical harmonics
of S2. Then: E(S2(N)) = 1
N [
1
vol(S∗S2)
R
S∗S2 |σave
A (ζ) −¯
σA|2dµ(ζ)] + O(1/N 2).
The optimist may conjecture a similar rate for quantum chaotic eigenfunctions. In [Ze1] it is further
proved that almost all orthonormal bases of spherical harmonics are quantum ergodic, and this was improved
to quantum unique ergodicity by VanderKam [V].
On the level of quantum mixing, however, random
spherical harmonics do not provide a good model, but random combinations of Laplace eigefunctions on
generic Riemannian manifolds do; that was the motivation for studying the model in [Ze2].
Quantum
mixing systems involve oﬀ-diagonal sums like (3) with constant gaps between eigenvalues. Conversely, if the
eigenfunctions satisfy (3) and the analogous oﬀ-diagonal estimates for all gaps, then the system is classically
FROM RANDOM POLYNOMIALS TO SYMPLECTIC
7
mixing. Hence the random wave model is not a good model for ergodic systems which fail to be mixing (cf.
[HKZ]).
A further relation between Gaussian random waves and quantum chaotic eigenfunctions does not seem to
have been explored, even numerically. Let {ϕλ} be eigenfunctions of a quantum chaotic system, and consider
the local rescaling ϕλ(x0 + u
λ). The rescaled eigenfunction is an eigenfunction of the rescaled operator, which
is asymptotically Euclidean. Hence ϕλ(x0 + u
λ) can be expanded asymptotically in terms of plane waves,
and one might ask how the frequencies are distributed.
