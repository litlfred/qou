---
doc_id: li-braid-closures
doc_title: "Knot polynomials on braid closures Eddy Li"
section_id: sec-006-split-links
section_title: "Split Links"
section_number: null
pages: 9-13
source_pdf: Li-braid-closures.pdf
source_sha256: f7410e7be5bc187e
---
From from Proposition 1.3 we haveV L(−1) = ∆L(−1) = 0 for all split links. We show that
this condition is not sufficient.
Corollary 3.3.Letα∈B 3. ThenV ˆα(−1) = ∆ˆα(−1) = 0if and only iftrϕ(α) = 2.
Proof.Immediate by Proposition 3.2.
The following result is due to Serre [8].
Proposition 3.4([8, Theorem 2.1.4]).The groupSL 2(Z)has presentation
SL2(Z)∼=⟨s,t|s 4 = 1,(st) 3 =s 2⟩
where the correspondence of matrices is given from(s,t)to
(S,T) =
 0 1
−1 0

,
1 0
1 1

.
Now we claim the following.
Lemma 3.5.The following statements are true.
(a) The matricesM 1 andM 2 generate the groupSL 2(Z).
(b) The groupSL 2(Z)admits the presentation
SL2(Z)∼=⟨m1,m 2|(m 1m2m1)4 =m 1m2m1m−1
2 m−1
1 m−1
2 = 1⟩.
Proof.Retain the notation as in Proposition 3.4. Check that (S,T) = (M 1M2M1,M−1
1 ) and
(M1,M 2) = (T−1,TST), so that any word in the alphabet{s,s −1,t,t−1}can be translated
to one in the alphabet{m 1,m−1
1 ,m 2,m−1
2 }and vice versa. This proves part (a) of the
desired result.
Now, we can simply make the substitution (s,t) = (m1m2m1,m−1
1 ), which has the inverse
substitution (m1,m 2) = (t−1,tst), as follows from the above matrix transformations. Hence
SL2(Z)∼=⟨s,t|s 4 = 1,(st) 3 =s 2⟩
∼=⟨m1,m 2|(m 1m2m1)4 = 1,(m 1m2)3 = (m1m2m1)2⟩
∼=⟨m1,m 2|(m 1m2m1)4 =m 1m2m1m−1
2 m−1
1 m−1
2 = 1⟩,
which proves part (b).
Following Garside [9], define ∆ 3 =σ 1σ2σ1∈B 3.
Proposition 3.6.The mapϕinduces an isomorphism between the groupsB 3/⟨∆4
3⟩and
SL2(Z).
9
Proof.From [9] we have thatZ(B 3) =⟨∆ 2
3⟩. In particular, quotienting by⟨∆ 4
3⟩simply
introduces a corresponding relation, so by Lemma 3.5 we have
⟨σ1,σ 2|σ 1σ2σ1σ−1
2 σ−1
1 σ−1
2 = 1⟩/⟨∆4
3⟩∼=⟨m1,m 2|(m 1m2m1)4 =m 1m2m1m−1
2 m−1
1 m−1
2 = 1⟩
with an isomorphism sendingσ i tom i.
Sinceϕ(∆ 4
3) acts as the identity,ϕis constant over all elements within any coset of⟨∆ 4
3⟩
as embedded inB 3, so the above isomorphism is well-defined.
We can thus reduce our original task of finding 3-braids whose braid closures have Jones
polynomial with root−1 with the task of finding conjugacy classes in SL 2(Z).
Proposition 3.7.Letα∈B 3 satisfyϕ(α) = 2. Then there exists someα 0∈B 3 andk∈Z
such thatϕ(α 0) =M k
2 andˆα= ˆα0.
Proof.It suffices to show that, given some matrixA∈SL 2(Z) such that trA= 2, there
exists someB∈SL 2(Z) such thatBAB −1 =M k
2 for somek∈Z. Indeed, letA=ϕ(α).
By Lemma 3.5, theM i generate SL2(Z), so there exists someβ∈B 3 such thatB=ϕ(β).
Defineα 0∈B 3 to beα 0 =βαβ −1. Thenϕ(α 0) =BAB −1 =M k
2 and ˆα0 = ˆαas we can
simply rotate the braid closure ofα 0 such that the components corresponding toβandβ −1
cancel out.
We now give an explicit construction of our above claim. Let
A=
a b
c d

.
Since trA= 2 and detA= 1, the eigenvalue ofAis 1 with multiplicity 2. Thus, there exists
some (x,y,z,w)∈Z 4 such that gcd(x,y) = 1,xw−yz= 1, andA(xe 1 +ye 2) =xe 1 +ye 2.
Then define the matrix
B=
x z
y w
−1
=
w−z
−y x

,
which is an element of SL 2(Z) by construction. Letting{e 1,e 2}be the canonical basis for
Z2, we can now check that
BAB−1e1 =BA(xe 1 +ye 2) =B(xe 1 +ye 2) =e 1
and
(BAB−1e2)·e 2 =w(dx−by) +z(cx−ay) = detB(trA−1) = 1.
Hence, for somek∈Z,
BAB−1 =
1k
0 1

=M k
2,
as desired.
Now we introduce the main results of this subsection.
10
Theorem 3.8.Letα∈B 3 satisfyV ˆα(−1) = ∆ˆα(−1) = 0. Then there exist integersmand
kfor whichˆαis equivalent to the braid closure ofσ k
2∆4m
3 .
Proof.By Corollary 3.3 and Proposition 3.7, there exists someα 0∈B 3 andk∈Zsatis-
fyingϕ(α 0) =M k
2 and ˆα= ˆα0. Thusσ −k
2 α0 is sent byϕto the identity, from which by
Proposition 3.6 it follows thatσ−k
2 α0∈⟨∆ 4
3⟩. Thenα 0 is of the formσ k
2∆4m
3 for somem.
Theorem 3.9.Form,k∈Z, letγ m,k denote the braidσ k
2∆4m
3 , so thatˆγ m,k denotes its
oriented link closure.
(a) The linkˆγm,k is split if and only ifm= 0.
(b) Form 1,m 2,k 1,k 2∈Z, the linksˆγm1,k1 andˆγm2,k2 are equivalent iff(m 1,k 1) = (m2,k 2).
Proof.First, suppose that 2|k. Consider the homomorphismψ:B 3→S 3 withψ(σ i) =
(i i+ 1). Then ˆγ m,k has three circles asψ(γ m,k) = (2 3) k((1 2)(2 3)(1 2)) 4m = 1. By
inspection, one can check that removing the strand unaffected byσ 2 fromγ m,k results in
the braidσ 4m+k
1 ∈B 2, while if any other strand is removed, the resulting braid isσ 4m
1 ∈B 2.
For part (a), if ˆγm,k is split, then at least two out of the three elements in the multiset
{4m,4m,4m+k}are equal to zero, forcingm= 0. For part (b), if ˆγ m1,k1 and ˆγm2,k2 are
equivalent for evenk i, then the multisets{4m 1,4m 1,4m 1 +k 1}and{4m 2,4m 2,4m 2 +k 2}
are equal, implying that (m 1,k 1) = (m2,k 2).
Otherwise, if 2∤k, then ˆγm,k is a link of two circles asψ(γm,k) = (2 3)k = (2 3). Then the
two strands affected byσ 2 form aT(2,4m+k) torus link. LetWbe the bounding torus of
this link. Then the third strand is an unknot that wraps 2mtimes around a cross-sectional
disk ofW. Hence, for part (a), if ˆγm,k is split, then the third strand cannot wrap around the
bounding torus at all, again forcingm= 0. For part (b), if ˆγ m1,k1 and ˆγm2,k2 are equivalent
for oddn i, then (2m 1,4m 1 +k 1) = (2m2,4m 2 +k 2), and the desired conclusion follows.
Note for part (b) that counting circles givesk 1≡k 2 (mod 2), as subsumed above.
Thus we have an infinite family of distinct links with no splitting whose Jones and
Alexander polynomials vanish att=−1. It turns out that certain pairs of links fail to be
detected by the HOMFLYPT polynomial.
Theorem 3.10.If6|k, thenX ˆγm,k(q,Λ) =X ˆγm+k
6,−k
(q,Λ).
Proof.We first computeχ (2,1)(γm,k). The Burau representation letsσ i act as−L i, where
(L1,L 2) =
−q0
−1 1

,
1−q
0−q

.
One can check that (L1L2L1)4 acts as scalar multiplication byq 6. Also note thatL k
2e1 =
e1 ase 1 is an eigenvector and (Lk
2e2)·e 2 =−q(L k−1
2 (e1 +e 2))·e 2 =−q(e 1 +Lk−1
2 e2)·e 2 =
11
−q(Lk−1
2 e2)·e 2.Thus (L k
2e2)·e 2 = (−q)k by induction, so it follows that tr(Lk
2) = 1+(−q) k.
We thus have
χ(2,1)(γm,k) = (−1)e(γm,k) tr(Lk
2(L1L2L1)4m) = (−1)e(γm,k)q6m(1 + (−q)k).
Sincee(γ m,k) =e(γ m+k
6,−k) = 12m+k, one checks thatχ (2,1)(γm,k) =χ (2,1)(γm+k
6,−k).
In addition, it is clear thatχ(1,1,1)(γm,k) =χ (1,1,1)(γm+k
6,−k) andχ (3)(γm,k) =χ (3)(γm+k
6,−k).
The desired result then follows by Definition 2.18.
We finish this subsection by constructing the Jones and Alexander polynomials of ˆγm,k.
Proposition 3.11.The Jones and Alexander polynomials ofˆγ m,k are
Vˆγm,k(t) = (−
√
t)12m+k

t6m((−t)k + 1) + 1
t +t

and
∆ˆγm,k(t) = (−t)12m+k−t 6m((−t)k + 1) + 1
(−
√
t)12m+k−2(t2 +t+ 1) .
Proof.From Theorem 3.10, we have thatχ (2,1)(γm,k) = (−1)kq6m(1 + (−q)k) ande(γ m,k) =
12m+k. It follows from Examples 2.19 and 2.20 that
Vˆγm,k(t) = (
√
t)e(γm,k)−2((t2 + 1)χ(1,1,1)(γm,k) +tχ (2,1)(γm,k))
= (−
√
t)12m+k

t6m((−t)k + 1) +t+ 1
t

and
∆ˆγm,k(t) = χ(1,1,1)(γm,k)−χ (2,1)(γm,k) +χ (3)(γm,k)
(
√
t)e(γm,k)−2(t2 +t+ 1)
= (−t)12m+k−t 6m((−t)k + 1) + 1
(−
√
t)12m+k−2(t2 +t+ 1) .
In both cases, we have substitutedtforq.
Remark.For evenk, Proposition 3.11 simplifies to
Vˆγm,k(t) =t 6m+k
2−1 +t 6m+k
2 +1 +t 12m+k
2 +t 12m+ 3k
2
and
∆ˆγm,k(t) = t6m+k
2 +1−t
k
2 +1−t−k
2 +1 +t−6m−k
2 +1
t2 +t+ 1 .
12
