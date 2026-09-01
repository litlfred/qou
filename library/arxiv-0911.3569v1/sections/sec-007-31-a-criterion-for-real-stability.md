---
doc_id: arxiv-0911.3569v1
doc_title: "MULTIVARIATE STABLE POLYNOMIALS: THEORY AND APPLICATIONS"
section_id: sec-007-31-a-criterion-for-real-stability
section_title: "A criterion for real stability."
section_number: 3.1
pages: 8-10
source_pdf: 0911.3569v1.pdf
source_sha256: 4e7c15c9724fb453
---
∆ijf =∂if·∂jf−f·∂i∂jf.
Notice that for f∈ C[x]MA,
∆ijf =fj
ifj−fjfij = Wi[fj,fj] =−Wi[fj,f j],
and
∆ijf =fj
ifi
j−fijfij.
Theorem 3.1 (Theorem 5.6 of [8] and Theorem 3 of [16]) . Let f ∈ R[x]MA be
multiaﬃne. The following are equivalent:
(a) f is real stable.
(b) For all{i,j}⊆ [m] and all a∈ Rm, ∆ijf(a)≥ 0.
(c) Either m = 1, or there exists {i,j}⊆ [m] such that fi, fi, fj and fj are real
stable, and ∆ijf(a)≥ 0 for all a∈ Rm.
MULTIVARIATE STABLE POLYNOMIALS 9
Proof. To see that (a) implies (b), ﬁx {i,j} ⊆[m]. Proposition 2.7(a) shows
that fj≪ fj, and from the calculation above and Corollary 2.10, it follows that
∆ijf(a) =−Wi[fj,f j](a)≥ 0 for all a∈ Rm.
We show that (b) implies (a) by induction on m, the base case m = 1 being
trivial. For the induction step let f be as in part (b), let a∈ R, and let g =
f|xm=a. For all {i,j}⊆ [m− 1] and a∈ Rm−1, ∆ijg(a) = ∆ ijf(a,a )≥ 0. By
induction, g = fm +afm is real stable for all a∈ R; it follows that afm +bfm∈
SR[x1,...,x m−1] for all a,b∈ R. Furthermore, for all j∈ [m− 1] and a∈ Rm−1,
Wj[fm,f m](a) = −∆jmf(a, 1)≤ 0. This veriﬁes condition (c) of Corollary 2.10
for the pair (fm,f m), and it follows that f =fm +xmfm∈ SR[x], completing the
induction.
It is clear that (a) and (b) imply (c) – we show that (c) implies (b) below. This
is clear if m≤ 2, so assume that m≥ 3. To begin with, let {h,i,j}⊆ [m] be
three distinct indices, and consider ∆ ijf as a polynomial in xh. That is, ∆ ijf =
Ahijx2
h +Bhijxh +Chij in which
Ahij = fj
hifi
hj−fij
h fhij = ∆ijfh,
Bhij = fj
hifhi
j −fij
h fh
ij +fhj
i fi
hj−fhijfhij, and
Chij = fhj
i fhi
j −fhijfh
ij = ∆ijfh.
If ∆ijf(a)≥ 0 for all a∈ Rm then this quadratic polynomial in xh:
∆ijf(a1,...,a h−1,xh,ah+1,...,a m)
has a nonpositive discriminant for all a∈ Rm. That is, Dhij =B2
hij− 4AhijChij is
such that Dhij(a)≤ 0 for all a∈ Rm.
It is a surprising fact that as a polynomial in {xk : k∈ [m] r{h,i,j}}, Dhij is
invariant under all six permutations of its indices, as is seen by direct calculation:
Dhij = ( fij
h fh
ij)2 + (fhj
i fi
hj)2 + (fhi
j fj
hi)2 + (fhijfhij)2
−2(fij
h fh
ijfhj
i fi
hj +fhj
i fi
hjfhi
j hj
hi +fhi
j fj
hifij
h fh
ij)
−2(fij
h fh
ij +fhj
i fi
hj +fhi
j fj
hi)fhijfhij
+4fh
ijfi
hjfj
hifhij + 4fij
h fhj
i fhi
j fhij.
Now for the proof that (c) implies (b) whenm≥ 3. Consider any h∈ [m]r{i,j}.
Then
∆hif =Ajhix2
j +Bjhixj +Cjhi
has discriminant Djhi =Dhij. Since fj and fj are real stable, we have Ajhi(a) =
∆hifj(a)≥ 0 and Cjhi(a) = ∆hifj(a)≥ 0 for all a∈ Rm. Since ∆ ijf(a)≥ 0 for
all a∈ Rm it follows that Djhi(a) = Dhij(a)≤ 0 for all a∈ Rm. It follows that
∆hif(a)≥ 0 for all a∈ Rm. (Note that if B2− 4AC≤ 0 and either A = 0 or
C = 0, then B = 0.) A similar argument using the fact that fi and fi are real
stable shows that ∆hjf(a)≥ 0 for all a∈ Rm.
It remains to show that ∆hkf(a)≥ 0 for all a∈ Rm when{h,k} is disjoint from
{i,j}. We have seen that ∆ hif(a)≥ 0 for all a∈ Rm, and we know that both fi
andfi are real stable. The argument above applies once more: ∆ hif(a)≥ 0 for all
a∈ Rm, so that Dihk(a) =Dkhi(a)≤ 0 for all a∈ Rm, and then since Aihk(a)≥ 0
and Cihk(a)≥ 0 for all a∈ Rm it follows that ∆hkf(a)≥ 0 for all a∈ Rm. Thus
(c) implies (b). □
10 DAVID G. WAGNER
