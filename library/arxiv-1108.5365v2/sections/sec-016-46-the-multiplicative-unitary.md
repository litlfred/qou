---
doc_id: arxiv-1108.5365v2
doc_title: "Representation of the Quantum Plane, its Quantum Double and Harmonic Analysis on GL+_q(2,R)"
section_id: sec-016-46-the-multiplicative-unitary
section_title: "The multiplicative unitary"
section_number: 4.6
pages: 34-39
source_pdf: 1108.5365v2.pdf
source_sha256: 000961ede2234231
toc_source: outline
doc_brief: "Representation of the Quantum Plane, its Quantum Double and Harmonic Analysis on GL+_q(2,R) — We give complete detail of the description of the GNS representation of the quantum plane A and its dual"
---
The multiplicative unitary
In this section we will describe the multiplicative unitary W explicitly. Recall (cf.
(2.30)) that it is deﬁned as a unitary operator on H ⊗H by
W ∗(Λ(a) ⊗Λ(b)) = (Λ ⊗Λ)(∆(b)(a ⊗1)).
(4.56)
We will use extensively the following variants of Lemma 3.7:
Corollary 4.18. For AB = q2BA, ˆA ˆB = q−2 ˆB ˆA, using Lemma 2.24 we have
gb(B ⊗q ˆB ˆA−1)
=
Z
R+i0
Bib−1τ ⊗ˆA−ib−1τ ˆBib−1τ
Gb(Q + iτ)
dτ,
(4.57)
gb(q−1BA−1 ⊗ˆB)
=
Z
R+i0
Bib−1τA−ib−1τ ⊗ˆBib−1τ
Gb(Q + iτ)
dτ,
(4.58)
g∗
b(B ⊗q ˆB ˆA−1)
=
Z
R+i0
Bib−1τ ⊗ˆBib−1τ ˆA−ib−1τGb(−iτ)dτ,
(4.59)
g∗
b(q−1BA−1 ⊗ˆB)
=
Z
R+i0
A−ib−1τBib−1τ ⊗ˆBib−1τGb(−iτ)dτ.
(4.60)
Note that the arguments inside gb are all essentially self-adjoint, hence the expres-
sion is well-deﬁned.
34
Proposition 4.19. The multiplicative unitary W ∈B(H ⊗H) is given by
W
=
e
i
2πb2 log A−1⊗log ˆ
Agb(B ⊗q ˆB ˆA−1)
(4.61)
=
gb(q−1BA−1 ⊗ˆB)e
i
2πb2 log A−1⊗log ˆ
A,
(4.62)
W ∗
=
e
i
2πb2 log A⊗log ˆ
Ag∗
b(q−1BA−1 ⊗ˆB)
(4.63)
=
g∗
b(B ⊗q ˆB ˆA−1)e
i
2πb2 log A⊗log ˆ
A,
(4.64)
where
A = e−2πbps,
B = e2πbse−2πbpt
(4.65)
as before, and
ˆA = e2πbs,
ˆB = Gb(−it) ◦e2πbpt−2πbps ◦Gb(−it)−1.
(4.66)
Remark 4.20. Note that we actually have W ∈M(A ⊗B(H)).
Moreover, in
the next section, we will see that the hat operators are precisely the dual space
elements, hence indeed W ∈M(A ⊗ˆ
A). Furthermore, the multiplicative unitary
will be invariant under the exchange b −→b−1 and Aq −→Aeq.
Proof. First of all notice that ˆA and ˆB are positive operators on the subspace W
(with the measure shifted in t by iQ
2 ) since Gb( Q
2 −it) is unitary. Furthermore we
have ˆA ˆB = q−2 ˆB ˆA. Moreover, both q−1BA−1 and q ˆB ˆA−1 are positive operators,
hence the expressions are well-deﬁned.
The formula for W follows from W ∗by conjugation, and using the relations
(2.46), (2.47). For simplicity, we compute W ∗formally using the deﬁnition:
W ∗(f ⊗g)
=
∆(g)(f ⊗1)
=

g(s1, t1 + t2)Gb(−it1)Gb(−it2)
Gb(−i(t1 + t2)) δ(s2, s1 + t1)

· f(s1, t1)
=
Z
C
Z
R
g(s1 −s′
1, t1 + t2 −t′
1)Gb(it′
1 −it1)Gb(−it2)
Gb(−i(t1 + t2 −t′
1))
δ(s2, s1 + t1 −t′
1 −s′
1)f(s′
1, t′
1)e2πis′
1(t−t′
1)ds′
1dt′
1,
where C goes below t′
1 = t1. Replacing s′
1 = s1 + t1 −s2 −t′
1, we get
=
Z
C
f(s1 + t1 −s2 −t′
1, t′
1)g(t′
1 −t1 + s2, t1 + t2 −t′
1)
e2πi(s1+t1−s2−t′
1)(t−t′
1) Gb(it′
1 −it1)Gb(−it2)
Gb(−i(t1 + t2 −t′
1)) dt′
1.
35
Renaming t′
1 = τ and do a shift τ 7→t1 −τ we get
W ∗(f ⊗g)
=
Z
R+i0
f(s1 −s2 + τ, t1 −τ)g(s2 −τ, t2 + τ)e2πi(s1−s2+τ)τ Gb(−iτ)Gb(−it2)
Gb(−iτ −it2)
dτ,
where the contour of τ now goes above τ = 0.
On the other hand, using Corollary 4.18, the formula we desired is
e
i
2πb2 log A⊗log ˆ
Ag∗
b(q−1BA−1 ⊗ˆB)(f ⊗g)
=
e
i
2πb2 log A⊗log ˆ
A
Z
R+i0
A−ib−1τBib−1τ ⊗ˆBib−1τGb(−iτ)dτ

(f ⊗g)
=
e−2πips1s2
Z
R+i0
f(s1 + τ, t1 −τ)g(s2 −τ, t2 + τ)e2πi(s1+τ)τ Gb(−it2)Gb(−iτ)
Gb(−it2 −iτ)
dτ

=
Z
R+i0
f(s1 −s2 + τ, t1 −τ)g(s2 −τ, t2 + τ)e2πi(s1−s2+τ)τ Gb(−iτ)Gb(−it2)
Gb(−iτ −it2)
dτ.
For completeness, let us note that the action of W is given by
W(f ⊗g) =
Z
R+i0
Gb(−it2)e2πiτs1
Gb(−it2 −iτ)Gb(Q + iτ)f(s1 + s2, t1 −τ)g(s2 −τ, t2 + τ)dτ.
(4.67)
In [46], it is commented that manageability of the multiplicative unitary is the
property that distinguish quantum groups from quantum semigroups. However, we
obtain the following:
Theorem 4.21. W deﬁned above is manageable.
Proof. We need to look for the positive operator Q and the unitary f
W in Deﬁnition
2.21. It is known (e.g. see [40, 24]) that Q can be expressed in terms of the scaling
constant and the scaling group:
Q = P 1/2,
P itΛ(x) = ν1/2Λ(τt(a)).
(4.68)
From the expressions derived in the previous sections, we obtain
Q · f(s, t) = e−πQ(t−iQ
2 )f(s, t).
(4.69)
Note that in fact Q is positive, under the inner product of H (with a shift in
t 7→t + iQ
2 ).
Then we see that Q ⊗Q commutes with A ⊗1, 1 ⊗ˆA and B ⊗ˆB. Therefore
from the formula (4.61) we conclude that Q ⊗Q commutes with W.
36
Next we will express f
W from deﬁnition, and show that it is a unitary operator.
First of all, let us note that restricting to holomorphic functions, when a shift in
contour is involved, the inner product actually reads
⟨f, g⟩H =
Z
R
Z
R
f(s, t + iQ
2 )g(s, t + iQ
2 )dsdt,
(4.70)
see the derivation in the proof of Theorem 4.9.
By deﬁnition we have
⟨f ′ ⊗g′, W(f ⊗g)⟩H⊗H = ⟨f ⊗Qg′, f
W(f
′ ⊗Q−1g)⟩H⊗H,
where f := f(z) = f(z) ∈H, and the inner product is given by
⟨f, g⟩H
:=
⟨g, f⟩H
=
Z
R
Z
R
f(s, t −iQ
2 )g(s, t + iQ
2 )dsdt
=
Z
R
Z
R
f(s, t −iQ
2 )g(s, t −iQ
2 )dsdt.
(4.71)
Now using the action of W given by (4.67), we have
LHS
=
ZZ ZZ
ds1dt1ds2dt2f ′(s1, t1 + iQ
2 )g′(s2, t2 + iQ
2 ) ·
Z
R+i0
Gb( Q
2 −it2)e2πiτs1
Gb( Q
2 −it2 −iτ)Gb(Q + iτ)
f(s1 + s2, t1 −τ + iQ
2 )g(s2 −τ, t2 + τ + iQ
2 )dτ
=
ZZ ZZ Z
R+i0
dτds1dt1ds2dt2f ′(s1, t1 + iQ
2 )g′(s2, t2 + iQ
2 )e−2πiτs1 ·
Gb( Q
2 −it2 −iτ)Gb(iτ)
Gb( Q
2 −it2)
f(s1 + s2, t1 −τ −iQ
2 )g(s2 −τ, t2 + τ −iQ
2 )
=
ZZ ZZ Z
R+i0
dτds1dt1ds2dt2f(s1, t1 −iQ
2 )g′(s2, t2 + iQ
2 )e−2πiτ(s1−s2) ·
Gb( Q
2 −it2 −iτ)Gb(iτ)
Gb( Q
2 −it2)
f ′(s1 −s2, t1 + τ + iQ
2 )g(s2 −τ, t2 + τ −iQ
2 )
RHS
=
ZZ ZZ
ds1dt1ds2dt2f(s1, t1 −iQ
2 g′(s2, t2 + iQ
2 )e−πQt2
f
W(f
′ ⊗Q−1g)(s1, t1 −iQ
2 , s2, t2 + iQ
2 ).
37
Comparing, we get
f
W(f
′ ⊗Q−1g)(s1, t1 −iQ
2 , s2, t2 + iQ
2 )
=
Z
R+i0
eπQt2e−2πiτ(s1−s2) Gb( Q
2 −it2 −iτ)Gb(iτ)
Gb( Q
2 −it2)
f ′(s1 −s2, t1 + τ + iQ
2 )g(s2 −τ, t2 + τ −iQ
2 )dτ
f
W(f
′ ⊗Q−1g)(s1, t1 −iQ
2 , s2, t2 + iQ
2 )
=
Z
R+i0
eπQt2e2πiτ(s1−s2)
Gb( Q
2 −it2)
Gb( Q
2 −it2 −iτ)Gb(Q + iτ)
f ′(s1 −s2, t1 + τ −iQ
2 )g(s2 −τ, t2 + τ + iQ
2 )dτ
so that
f
W(f
′⊗Q−1g)(s1, t1, s2, t2) =
Z
R+i0
eπQ(t2−iQ
2 )e2πiτ(s1−s2)Gb(−it2)
Gb(−it2 −iτ)Gb(Q + iτ)
f
′(s1−s2, t1+τ)g(s2−τ, t2+τ)dτ.
Now renaming G = Q−1g, i.e. G(s2, t2) = eπQ(t2−iQ
2 )g(s2, t2), we have
g(s2 −τ, t2 + τ) = G(s2 −τ, t2 + τ)e−πQ(t2+τ−iQ
2 ),
hence the action of f
W becomes
f
W(f ⊗g)
=
Z
R+i0
e−πQτe2πiτ(s1−s2)Gb(−it2)
Gb(−it2 −iτ)Gb(Q + iτ) f(s1 −s2, t1 + τ)g(s2 −τ, t2 + τ)dτ
=
Z
R+i0
f(s1 −s2, t1 + τ)g(s2 −τ, t2 + τ)e2πiτ(s1−s2+t2+τ−iQ
2 )
Gb(Q + it2 + iτ)Gb(−iτ)
Gb(Q + it2)
dτ.
Hence we can conclude that
f
W
=
e−2πis2ps1
Z
R+i0
(B#)ib−1τ ⊗( ˆB#)ib−1τ( ˆA#)ib−1τGb(−iτ)dτ
=
e
i
2πb2 log A−1⊗log ˆ
Ag∗
b(B# ⊗q ˆB# ˆA#),
where
B# = e2πb(s+pt),
ˆA# = e2πb(t−iQ
2 ),
ˆB# = Gb(Q + it)−1e2πb(pt−ps) ◦Gb(Q + it),
are all positive operators with respect to the measure in H ⊗H, and we used an
analogue of (4.59) with ˆA# ˆB# = q2 ˆB# ˆA#. Hence f
W is a unitary operator.
38
Remark 4.22. This is a rather curious and striking result since our quantum
plane has been restricted to B > 0 so that all the operators involved are positive
essentially self-adjoint and nicely deﬁned. In fact, the key diﬀerence is that in [46],
the multiplicative unitary W lies in A ⊗A, while our W lies in A ⊗ˆ
A, and the
Hilbert space H ≃L2(R×R) is “twice” larger than the canonical space L2(R) for the
action of A only. For example, we see that the operator ˆA# = e2πb(t−iQ
2 ) does not
lie in the action spanned by A itself, which only contains actions on the variable s
and the shifting operator e2πbpt. Therefore it is worth studying a deeper meaning of
manageability of W in this wider context of quantum semigroups. The diﬀerence in
the deﬁnition of W mentioned above in fact produces a new transformation formula
for Gb, see Section 9 for further detail.
