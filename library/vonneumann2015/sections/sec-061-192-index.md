---
doc_id: vonneumann2015
doc_title: "Von Neumann Algebras"
section_id: sec-061-192-index
section_title: "Index."
section_number: 19.2
pages: 141-146
source_pdf: vonNeumann2015.pdf
source_sha256: 781c6912b7d7b9a4
toc_source: inferred
doc_brief: "Von Neumann Algebras — 70 sections: Front matter; Hilbert Space; The Spectral Theorem"
---
Index.
Inspired by the above and 10.2.2 we make the following:
Deﬁnition 19.2.1. If N ⊆M are II1 factors, the index [M : N] of N in M
is the real number dimN L2(M).
Exercise 19.2.2. Show that [M : N] = 1 implies N = M.
Proposition 19.2.3. (i) If M acts on H so that dimN H < ∞then
[M : N] = dimN H
dimM H.
(ii) If [M : N] < ∞and p is a projection in N ′ ∩M then set [M : N]p =
[pMp : pN], then
[M : N]p = trN′(p)trM(p)[M : N].
(for any action of M on H for which N ′is a type II1 factor.) (iii) If {p} is
a partition of unity in N ′ ∩M then
[M : N] =
X
p
[M : N]p
tr(p)
.
(iv) If N ⊆P ⊆M are type II1 factors then
[M : N] = [M : P][P : Q].
(v) If M acts on H such that dimN H < ∞then
[M : N] = [N ′ : M ′]
141
Proof. (i) Certainly M ′ (on H) is a type II1 factor since N ′ is and taking the
direct sum of ﬁnitely many copies of H will not change the ratio dimN H
dimM H. So
we may assume dimM H ≥1 which means there is a projection p in M ′ with
pH ∼= L2(M) as an M module. But the trace of this p in N ′ is the same as
the trace in M ′ by uniqueness of the trace. Hence by the properties of the
coupling constant, dimN H
dimM H does not change under reduction by this p.
(ii) This follows immediately from (i) and properties of the coupling constant.
(iii) Just sum [M:N]p
trM(p) over p.
(iv) The only case of interest is when [M : N] < ∞. Then the result follows
immediately from (i).
(v) Immediate from (i).
Corollary 19.2.4. If N ′ ∩M̸ = Cid then [M : N] ≥4.
Deﬁnition 19.2.5. We call a subfactor irreducible if N ′ ∩M = Cid.
Deﬁnition 19.2.6. A subfactor N ⊆M is called locally trivial
if [M : N]p = 1 for any minimal projection in N ′ ∩M.
Exercise 19.2.7. Show that dim(N ′ ∩M) ≤[M : N].
Here is a list of what might be called the "classical" subfactors- ones
whose existence owes nothing to the dedicated development of subfactor the-
ory.
Example 19.2.8. The trivial subfactors.
If M is a type II1 factor, so is M ⊗Mk(C) for any integer k > 0. We can
embed M in M ⊗Mk(C) by x 7→x ⊗1. It is clear that L2(M ⊗Mk(C)) is
the direct sum of k2 copies of L2(M) so [M ⊗Mk(C) : M] = k2.
Example 19.2.9. Continuously varying index.
Choose a projection of trace d in the hyperﬁnite type II1 factor R. Then
pRp and (1 −p)R(1 −p) are isomorphic by hyperﬁniteness so choose a von
Neumann algebra isomorphism θ : pRp →(1 −p)R(1 −p). Let M be R and
N be the subalgebra {x + θ(x)|x ∈pRp}. It is clear that pMp = Np and
(1 −p)M(1 −p) so by lemma 19.2.3,
[M : N] = 1
d +
1
1 −d.
As d varies between 0 and 1, this index takes all real values ≥4.
Observe though that N ′∩M contains p so the subfactor is reducible. The
set of index values for irreducible subfactors of R is not understood though
for other type II1 factors it may be the interval [4, ∞]
142
Example 19.2.10. Group-subgroup subfactors.
If G is a discrete group acting by outer automorphisms on the type II1 factor
M, and H is a subgroup of G, it is clear that M ⊗H is a subfactor of M ⊗G
of index [G : H].
If G is ﬁnite we may consider M G ⊆M H which also has index [G : H]
by 19.1.2 and 19.2.3
Example 19.2.11. Making the trivial non-trivial.
Deﬁnition 19.2.12. An action of a compact group on a factor M is called
minimal if (M G)′ ∩M = Cid.
If G has a minimal action α on M and ρ is an irreducible unitary repre-
sentation of G on Ck we may take the action α ⊗Adρ on M ⊗Mk(C). One
then deﬁnes the "Wassermann subfactor"
(M ⊗1)G ⊆(M ⊗Mk(C))G.
The point is that the commutant of (M ⊗1)G in M ⊗Mk(C) is already just
Mk(C) by minimality of the action. So the ﬁxed points are indeed factors
and the Wassermann subfactor is irreducible.
Already for ﬁnite groups this provides lots of examples. If G is inﬁnite
there is a simple way to construct minimal actions. Just take a ﬁnite dimen-
sional unitary representation ρ and consider ⊗∞
1 Adρ on R. The group S∞is
contained in the ﬁxed points via its (inner) action permuting the tensor prod-
uct factors. Moreover if we choose an orthonormal basis {xi|i = 1, 2, ...k2} for
Mk(C) with x1 = 1, an orthonormal basis of R is formed by tensors ⊗∞
j=1xi(j)
indexed by functions i : N →{1, 2, · · · , k2} with i(j) = 1 for suﬃciently
large j. The action of S∞on this basis has only one ﬁnite orbit-that of the
identity. So the only ﬁxed points on in L2(R) are the scalar multiplies of the
identity.
Example 19.2.13. Finitely generated discrete groups.
This example shows that ﬁnite index subfactors can be inﬁnite objects in
disguise. Let Γ = ⟨γ1, γ2 · · · γk⟩be a ﬁnitely generated discrete group. We
have seen that Γ can act in lots of ways, in particular outer, on type II1
factors. Choose any action on M and for each x in M deﬁne the matrix
d(x) = xi,j over M by
xi,j =
(
0
if i̸ = j
γi(x)
if i = j
143
Then consider the subfactor
D(M) = {d(x)|x ∈M} ⊆M ⊗Mk(C).
This subfactor is locally trivial so its index is k2 and one may think of it as
a "twisted" version of the trivial subfactor of index k2.
Exercise 19.2.14. Show that dim(D(M)′ ∩M ⊗Mk(C)) = k iﬀγ−1
i γj is
outer whenever i̸ = j.
In fact one may easily extract the image of Γ modulo inner automorphisms
from the subfactor D(M).
We now want to consider an entirely arbitrary subfactor. For this the fol-
lowing "basic construction" is important. We have already seen its usefulness
for ﬁnite group actions.
Proposition 19.2.15. Let N ⊆M be a type II1 factors acting on L2(M)
and let eN be the extension to L2 of the trace-preserving conditional EN
expectation onto N. Then
JN ′J = (JNJ)′ = {M, eN}”.
Proof. Already done in 19.1.4.
Deﬁnition 19.2.16. The von Neumann algebra ⟨M, eN⟩= {M, eN}” of the
previous result is said to be the "basic construction" for N ⊆M.
Here are the most important facts about the basic construction. It will
be convenient from now on to use τ for [M : N]−1. Since ⟨M, eN⟩is a type
II1 factor its trace is unique and its restriction to M is the trace of M. So
we just use tr for it.
Proposition 19.2.17.
(i) For x ∈M, [x, eN] = 0 iﬀx ∈N.
(ii) eNxeN = EN(x)eN for x ∈M.
(iii) [M : N] < ∞iﬀ⟨M, eN⟩is a type II1 factor, in which case
[⟨M, eN⟩: M] = [M : N].
(iv) M + MeNM is a weakly dense *-subalgebra of ⟨M, eN⟩.
(v) eN⟨M, eN⟩eN = NeN
(vi) tr(eN) = [M : N]−1
(vii) For x ∈M, tr(eNx) = τtr(x)
144
Proof. (i) was done in 19.1.4.
(ii) is a consequence of the bimodule property of EN on the dense subspace
M of L2(M).
(iii) is immediate from proposition 19.2.15.
(iv) Closure of M +MeNM under multiplication follows from (ii). It contains
M and eN hence is dense.
(v) Follows immediately from (ii) and (iv).
(vi) Follows from (v) and the behaviour of the coupling constant under re-
duction by projections-note that eN(L2(M)) = L2(N).
(vii) tr(xeN) = tr(eNxeN) = tr(eNxeN) = tr(EN(x)eN) = τ(EN(x) where
we deduce the last equality from uniqueness of the trace on the type II1 factor
N. Since the conditional expectation preserves the trace, we are done.
From now on we will use τ for [M : N]−1.
Corollary 19.2.18. There is no subfactor N ⊆M with 1 < [M : N] < 2.
Proof. By the uniqueness of the trace we see that trN′(eN) = τ. Thus trN′(1−
eN) = 1 −τ. Hence [(1 −eN)⟨M, eN⟩(1 −eN) : N(1 −eN)] = (1 −τ)2(1/τ)2
which is less than 1 if 1/2 < τ < 1.
If we suppose [M : N] < ∞we see we may do the basic construction
for M ⊆⟨M, eN⟩.
In the type II1 factor ⟨⟨M, eN⟩, eM⟩we have the two
projections eM and eN.
Proposition 19.2.19.
eMeNeM = τeM and eNeMeN = τeN
.
Proof. For the ﬁrst relation we must show that EM(eN) = τid. But this is
just another way of saying (vii) of 19.2.17.
To prove the second relation, by (iv) of 19.2.17 it suﬃces to apply each side
to elements of the form x + yeNz ∈L2(⟨M, eN⟩) for x, y, z ∈M. To do this
note that eN acts by left multiplication.
Corollary 19.2.20. If [M : N]̸ = 1 then
eM ∨eN =
1
1 −τ (eN + eM −eMeN −eNeM)
Proof. The relations show that eN and eM generate a 4-dimensional non-
commutative algebra. By our analysis of two projections its identity must
be a multiple of (eM −eN)2. The normalisation constant can be obtained by
evaluating the trace.
145
Note that the special case eN ∨eM = 1 (which is equivalent to τ = 1/2
or index 2) means that eN and eM satisfy an algebraic relation.
Exercise 19.2.21. Use this relation to prove that, in index two, ⟨⟨M, eN⟩, eM⟩
is the crossed product of ⟨M, eN⟩by an outer action of Z/2Z. Use duality
to deduce Goldman’s theorem ([]): a subfactor of index 2 is the ﬁxed point
algebra for an outer Z/2Z action.
Let φ be the golden ratio 1+
√
5
2
.
Corollary 19.2.22. There is no subfactor N ⊆M with 2 < [M : N] < φ2.
Proof. We see that eN and eM are equivalent in the algebra they generate
so their traces are equal wherever they are.
Thus tr⟨⟨M,eN⟩,eM⟩(eN∨M) =
trN′(eN∨M) = 2τ and
[(1 −eN ∨eM)⟨⟨M, eN⟩, eM⟩(1 −eN ∨eM) : (1 −eN ∨eM)N] = (1 −2τ)2τ −3
This is less than 1 if φ−2 < τ < 1/2.
If we did yet another basic construction in the same way and calculated
the trace of the supremum of the three conditional expectations we would
conclude that there is no subfactor with index between φ2 and 3. But it is
high time to systematise the process.
