---
doc_id: bn
doc_title: "Braid groups and Hodge theory Curtis T. McMullen 25 April, 2009"
section_id: sec-015-2-dz-dz
section_title: "(dz −dz),"
section_number: 2
pages: 20-22
source_pdf: bn.pdf
source_sha256: 95ed0908ceb54a1c
doc_brief: "Braid groups and Hodge theory Curtis T. McMullen 25 April, 2009 — This paper gives an account of the unitary representations of the braid group that arise via the Hodge theory of cyclic branched cove"
---
19
we ﬁnd the action of the braid group on
H 1(X)q =H 1(X) = C[dz] ⊕ C[dz]
is given by
~τ ∗
i (x) = x −
√−1
2 ⟨x,e i⟩ei,
wheree1 =dz −dz andei+1 = (R−i)∗e1. Since Cei is the unique eigenspace
for~τ ∗
i |H 1(X), it must coincide with H 1
c (Xi). With these normalizations, we
have ⟨ei,e i⟩ = 0 and
⟨e1,e 2⟩ = ⟨ei,e i+1⟩ =
√
−1 ⟨dz −dz,dz +dz⟩ = 2
√
−1
for all i.
Proof of Theorem 4.1. We can assume X is deﬁned by yd =xn − 1 and
the disks Di are chosen symmetrically with respect to rotation, as in Fig ure
4; then R(Xi) = Xi+1. Using Theorem 4.4, we can choose ei ∈H 1(X)q such
that
H 1
c (Xi)q = Cei, ⟨ei,e i⟩ = 2 Imq and R∗(ei+1) = ei.
Then ⟨ei,e j⟩ = 0 if |i −j|> 1, since Xi and Xj are disjoint up to isotopy.
If q = −1, then ⟨ei,e i⟩ = 0 as well, and ei can be normalized so that
⟨ei,e i+1⟩ = 2 √−1 and ~τ ∗
i acts by (4.1), by comparison with the case y2 =
x4 − 1 above. If q = 1 then H 1(X)q = 0 and the theorem also holds.
Now suppose q ⁄= −1 (and q ⁄= 1, as usual). Since the value of A =
⟨ei,e i+1⟩ = ⟨e1,e 2⟩ is independent of n, to compute it we may assume n =d.
Then by Theorem 3.1, 1 and q−1 do not occur as eigenvalues of R|H 1(X)q,
and thus ∑ n
1ei =∑ n
1q−iei = 0. Pairing these vectors with e1, we ﬁnd
A + 2 Imq +
A =qA + 2 Imq +qA = 0,
which gives A = √−1(1 −q).
Once the inner product is known, we can also compute that
⟨ n∑
i=1
ζ −ji
d ei,e 1
⟩
=ζ j
dA + 2 Imq +ζ −j
d A ⁄= 0
whenever ζ j
d ⁄= 1 or q−1; thus the eigenspaces of R|H 1(X)q that do occur
are all contained in the span of ( ei)n
1 . It follows that ( ei)n
1 spans H 1(X)q.
The intersection form on H 1
c (Xi) is nondegenerate, so we have an or-
thogonal splitting
H 1(X)q =H 1
c (Xi)q ⊕H 1
c (Xi)⊥
q ∼
=H 1
c (Xi)q ⊕H 1(Yi)q
20
preserved by~τ ∗
i . Since ~τ ∗
i acts by −q on the ﬁrst factor by the identity on the
second (cf. (2.8)), its action on H 1(X)q is given by the complex reﬂection
formula (4.2).
Remark: The cases q = ± 1. Whenq = 1 we have H 1(X)q = 0, and the
formulas in Theorem 4.1 give ⟨ei,e j⟩ = 0. On the other hand, if we rescale
by (Imq)−1 asq → 1 in S1, then the inner product converges to the Coxeter
matrix
⟨ei,e j⟩′ =









2 −1 −1
−1 2 −1
−1 2 −1
· · · − 1
−1 −1 2









for the aﬃne diagram ~An, and the action of Bn onH 1(X)q converges to the
action of Sn as a reﬂection group.
As q → − 1 in S1, no rescaling is necessary: we have ( q + 1)/⟨ei,e i⟩ →√
−1/2, and thus the transvection (4.1) arises as a limit of the com plex
reﬂections (4.2). In the case q = −1 we can also express the action of Bn by
τ ∗
i (x) = x + [x,e i]ei,
where [ei,e i+1] = 1 and [ ei,e j ] = 0 for |i −j|> 1. This alternating form is
a positive multiple of the usual intersection pairing on H 1(X, R).
