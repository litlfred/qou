---
doc_id: li-braid-closures
doc_title: "Knot polynomials on braid closures"
section_id: sec-007-split-links
section_title: "Split Links"
section_number: null
pages: 9-13
source_pdf: Li-braid-closures.pdf
source_sha256: f7410e7be5bc187e
toc_source: outline
doc_brief: "Knot polynomials on braid closures — We explore properties of the Jones and Alexander polynomials of braid closures of braids of index 3."
---
Split Links
From from Proposition 1.3 we have VL(−1) = ∆L(−1) = 0 for all split links. We show that
this condition is not sufficient.
Corollary 3.3. Let α ∈B3. Then Vˆα(−1) = ∆ˆα(−1) = 0 if and only if tr ϕ(α) = 2.
Proof. Immediate by Proposition 3.2.
The following result is due to Serre [8].
Proposition 3.4 ([8, Theorem 2.1.4]). The group SL2(Z) has presentation
SL2(Z) ∼= ⟨s, t | s4 = 1, (st)3 = s2⟩
where the correspondence of matrices is given from (s, t) to
(S, T) =
 0
1
−1
0

,
1
0
1
1

.
Now we claim the following.
Lemma 3.5. The following statements are true.
(a) The matrices M1 and M2 generate the group SL2(Z).
(b) The group SL2(Z) admits the presentation
SL2(Z) ∼= ⟨m1, m2 | (m1m2m1)4 = m1m2m1m−1
2 m−1
1 m−1
2
= 1⟩.
Proof. Retain the notation as in Proposition 3.4. Check that (S, T) = (M1M2M1, M −1
1 ) and
(M1, M2) = (T −1, TST), so that any word in the alphabet {s, s−1, t, t−1} can be translated
to one in the alphabet {m1, m−1
1 , m2, m−1
2 } and vice versa.
This proves part (a) of the
desired result.
Now, we can simply make the substitution (s, t) = (m1m2m1, m−1
1 ), which has the inverse
substitution (m1, m2) = (t−1, tst), as follows from the above matrix transformations. Hence
SL2(Z) ∼= ⟨s, t | s4 = 1, (st)3 = s2⟩
∼= ⟨m1, m2 | (m1m2m1)4 = 1, (m1m2)3 = (m1m2m1)2⟩
∼= ⟨m1, m2 | (m1m2m1)4 = m1m2m1m−1
2 m−1
1 m−1
2
= 1⟩,
which proves part (b).
Following Garside [9], define ∆3 = σ1σ2σ1 ∈B3.
Proposition 3.6. The map ϕ induces an isomorphism between the groups B3/⟨∆4
3⟩and
SL2(Z).
9
Proof. From [9] we have that Z(B3) = ⟨∆2
3⟩. In particular, quotienting by ⟨∆4
3⟩simply
introduces a corresponding relation, so by Lemma 3.5 we have
⟨σ1, σ2 | σ1σ2σ1σ−1
2 σ−1
1 σ−1
2
= 1⟩/⟨∆4
3⟩∼= ⟨m1, m2 | (m1m2m1)4 = m1m2m1m−1
2 m−1
1 m−1
2
= 1⟩
with an isomorphism sending σi to mi.
Since ϕ(∆4
3) acts as the identity, ϕ is constant over all elements within any coset of ⟨∆4
3⟩
as embedded in B3, so the above isomorphism is well-defined.
We can thus reduce our original task of finding 3-braids whose braid closures have Jones
polynomial with root −1 with the task of finding conjugacy classes in SL2(Z).
Proposition 3.7. Let α ∈B3 satisfy ϕ(α) = 2. Then there exists some α0 ∈B3 and k ∈Z
such that ϕ(α0) = M k
2 and ˆα = ˆα0.
Proof. It suffices to show that, given some matrix A ∈SL2(Z) such that tr A = 2, there
exists some B ∈SL2(Z) such that BAB−1 = M k
2 for some k ∈Z. Indeed, let A = ϕ(α).
By Lemma 3.5, the Mi generate SL2(Z), so there exists some β ∈B3 such that B = ϕ(β).
Define α0 ∈B3 to be α0 = βαβ−1. Then ϕ(α0) = BAB−1 = M k
2 and ˆα0 = ˆα as we can
simply rotate the braid closure of α0 such that the components corresponding to β and β−1
cancel out.
We now give an explicit construction of our above claim. Let
A =
a
b
c
d

.
Since tr A = 2 and det A = 1, the eigenvalue of A is 1 with multiplicity 2. Thus, there exists
some (x, y, z, w) ∈Z4 such that gcd(x, y) = 1, xw −yz = 1, and A(xe1 + ye2) = xe1 + ye2.
Then define the matrix
B =
x
z
y
w
−1
=
 w
−z
−y
x

,
which is an element of SL2(Z) by construction. Letting {e1, e2} be the canonical basis for
Z2, we can now check that
BAB−1e1 = BA(xe1 + ye2) = B(xe1 + ye2) = e1
and
(BAB−1e2) · e2 = w(dx −by) + z(cx −ay) = det B(tr A −1) = 1.
Hence, for some k ∈Z,
BAB−1 =
1
k
0
1

= M k
2 ,
as desired.
Now we introduce the main results of this subsection.
10
Theorem 3.8. Let α ∈B3 satisfy Vˆα(−1) = ∆ˆα(−1) = 0. Then there exist integers m and
k for which ˆα is equivalent to the braid closure of σk
2∆4m
3 .
Proof. By Corollary 3.3 and Proposition 3.7, there exists some α0 ∈B3 and k ∈Z satis-
fying ϕ(α0) = M k
2 and ˆα = ˆα0. Thus σ−k
2 α0 is sent by ϕ to the identity, from which by
Proposition 3.6 it follows that σ−k
2 α0 ∈⟨∆4
3⟩. Then α0 is of the form σk
2∆4m
3
for some m.
Theorem 3.9. For m, k ∈Z, let γm,k denote the braid σk
2∆4m
3 , so that ˆγm,k denotes its
oriented link closure.
(a) The link ˆγm,k is split if and only if m = 0.
(b) For m1, m2, k1, k2 ∈Z, the links ˆγm1,k1 and ˆγm2,k2 are equivalent iff (m1, k1) = (m2, k2).
Proof. First, suppose that 2 | k. Consider the homomorphism ψ: B3 →S3 with ψ(σi) =
(i i + 1). Then ˆγm,k has three circles as ψ(γm,k) = (2 3)k((1 2)(2 3)(1 2))4m = 1. By
inspection, one can check that removing the strand unaffected by σ2 from γm,k results in
the braid σ4m+k
1
∈B2, while if any other strand is removed, the resulting braid is σ4m
1
∈B2.
For part (a), if ˆγm,k is split, then at least two out of the three elements in the multiset
{4m, 4m, 4m + k} are equal to zero, forcing m = 0. For part (b), if ˆγm1,k1 and ˆγm2,k2 are
equivalent for even ki, then the multisets {4m1, 4m1, 4m1 + k1} and {4m2, 4m2, 4m2 + k2}
are equal, implying that (m1, k1) = (m2, k2).
Otherwise, if 2 ∤k, then ˆγm,k is a link of two circles as ψ(γm,k) = (2 3)k = (2 3). Then the
two strands affected by σ2 form a T(2, 4m + k) torus link. Let W be the bounding torus of
this link. Then the third strand is an unknot that wraps 2m times around a cross-sectional
disk of W. Hence, for part (a), if ˆγm,k is split, then the third strand cannot wrap around the
bounding torus at all, again forcing m = 0. For part (b), if ˆγm1,k1 and ˆγm2,k2 are equivalent
for odd ni, then (2m1, 4m1 + k1) = (2m2, 4m2 + k2), and the desired conclusion follows.
Note for part (b) that counting circles gives k1 ≡k2 (mod 2), as subsumed above.
Thus we have an infinite family of distinct links with no splitting whose Jones and
Alexander polynomials vanish at t = −1. It turns out that certain pairs of links fail to be
detected by the HOMFLYPT polynomial.
Theorem 3.10. If 6 | k, then Xˆγm,k(q, Λ) = Xˆγm+ k
6 ,−k(q, Λ).
Proof. We first compute χ(2,1)(γm,k). The Burau representation lets σi act as −Li, where
(L1, L2) =
−q
0
−1
1

,
1
−q
0
−q

.
One can check that (L1L2L1)4 acts as scalar multiplication by q6. Also note that Lk
2e1 =
e1 as e1 is an eigenvector and (Lk
2e2) · e2 = −q(Lk−1
2
(e1 + e2)) · e2 = −q(e1 + Lk−1
2
e2) · e2 =
11
−q(Lk−1
2
e2)·e2. Thus (Lk
2e2)·e2 = (−q)k by induction, so it follows that tr(Lk
2) = 1+(−q)k.
We thus have
χ(2,1)(γm,k) = (−1)e(γm,k) tr(Lk
2(L1L2L1)4m) = (−1)e(γm,k)q6m(1 + (−q)k).
Since e(γm,k) = e(γm+ k
6 ,−k) = 12m + k, one checks that χ(2,1)(γm,k) = χ(2,1)(γm+ k
6 ,−k).
In addition, it is clear that χ(1,1,1)(γm,k) = χ(1,1,1)(γm+ k
6 ,−k) and χ(3)(γm,k) = χ(3)(γm+ k
6 ,−k).
The desired result then follows by Definition 2.18.
We finish this subsection by constructing the Jones and Alexander polynomials of ˆγm,k.
Proposition 3.11. The Jones and Alexander polynomials of ˆγm,k are
Vˆγm,k(t) = (−
√
t)12m+k

t6m((−t)k + 1) + 1
t + t

and
∆ˆγm,k(t) = (−t)12m+k −t6m((−t)k + 1) + 1
(−
√
t)12m+k−2(t2 + t + 1)
.
Proof. From Theorem 3.10, we have that χ(2,1)(γm,k) = (−1)kq6m(1 + (−q)k) and e(γm,k) =
12m + k. It follows from Examples 2.19 and 2.20 that
Vˆγm,k(t) = (
√
t)e(γm,k)−2((t2 + 1)χ(1,1,1)(γm,k) + tχ(2,1)(γm,k))
= (−
√
t)12m+k

t6m((−t)k + 1) + t + 1
t

and
∆ˆγm,k(t) = χ(1,1,1)(γm,k) −χ(2,1)(γm,k) + χ(3)(γm,k)
(
√
t)e(γm,k)−2(t2 + t + 1)
= (−t)12m+k −t6m((−t)k + 1) + 1
(−
√
t)12m+k−2(t2 + t + 1)
.
In both cases, we have substituted t for q.
Remark. For even k, Proposition 3.11 simplifies to
Vˆγm,k(t) = t6m+ k
2 −1 + t6m+ k
2 +1 + t12m+ k
2 + t12m+ 3k
2
and
∆ˆγm,k(t) = t6m+ k
2 +1 −t
k
2 +1 −t−k
2 +1 + t−6m−k
2 +1
t2 + t + 1
.
12
