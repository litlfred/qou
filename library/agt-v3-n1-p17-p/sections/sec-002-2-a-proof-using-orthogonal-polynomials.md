---
doc_id: agt-v3-n1-p17-p
doc_title: "Skein-theoretical derivation of some formulas of Habiro"
section_id: sec-002-2-a-proof-using-orthogonal-polynomials
section_title: "A proof using orthogonal polynomials"
section_number: 2
pages: 5-9
source_pdf: agt-v3-n1-p17-p.pdf
source_sha256: df196f0a732ad6b9
toc_source: inferred
doc_brief: "Skein-theoretical derivation of some formulas of Habiro — We use skein theory to compute the coeﬃcients of certain power series considered by Habiro in his theory of sl2 invariants of integral homol"
---
A proof using orthogonal polynomials
Habiro’s proof of Theorem 1.1 uses the relationship with the quantum group
Uqsl2. Here is another proof, using the method of orthogonal polynomials as in
[BHMV1].
Testing with the Sn-basis, we see that (8) holds if and only if
cn,−= ⟨t−1Sn⟩
⟨Rn, Sn⟩.
Thus, it is clear that an ω−satisfying (8) exists, and to compute its coeﬃcients,
we just need to compute ⟨t−1Sn⟩.
As in [BHMV1], deﬁne another bilinear form ⟨, ⟩1 by
⟨x, y⟩1 = ⟨t(x), t(y)⟩.
Deﬁne polynomials
Rn and
Sn by
t(Rn) = µnRn,
t(Sn) = µ2nSn .
(The factors µn and µ2n are included so that
Rn and
Sn are monic, i.e. have
leading coeﬃcient equal to one.)
Again, the
Rn form a basis of B, and the
Sn form a basis of the even part Bev
of B, since the twist map t preserves Bev. We have ⟨Rn,
Sm⟩1 = 0 for n̸ = m,
and
⟨Rn,
Sn⟩1 = µnµ2n⟨Rn, Sn⟩.
(10)
Note that ⟨t−1Sn⟩= µ−1
2n ⟨Sn⟩. Thus, we just need to compute ⟨Sn⟩.
Proposition 2.1 The polynomials
Sn satisfy a four-term recursion formula
Sn+1 = (z2 −αn)Sn −βn−1
Sn−1 −γn−2
Sn−2
(11)
for certain αn, βn−1, γn−2 ∈Z[A±].
Algebraic & Geometric Topology, Volume 3 (2003)
542
Gregor Masbaum
Proof Since
Sn is monic of degree 2n, we have that z2
Sn −
Sn+1 is a linear
combination of the
Sk with k ≤n. The coeﬃcients can be computed by taking
the scalar product with
Rk. So we just need to show that ⟨z2
Sn,
Rk⟩1 = 0 if
k < n −2.
The point is that multiplication by z is a self-adjoint operator with respect to
the bilinear form ⟨, ⟩1. In other words, one has
⟨zx, y⟩1 = ⟨x, zy⟩1
for all x, y ∈B. (This is because ⟨x, y⟩1 = ⟨t(xy)⟩.) It follows that
⟨z2
Sn,
Rk⟩1 = ⟨Sn, z2
Rk⟩1 = 0 if k < n −2,
since
Rk has degree k, and
Sn annihilates all polynomials of degree < n.
Note that the coeﬃcients in the recursion formula (11) are given by
αn = ⟨z2
Sn,
Rn⟩1
⟨Sn,
Rn⟩1
, βn−1 = ⟨z2
Sn,
Rn−1⟩1
⟨Sn−1,
Rn−1⟩1
, γn−2 = ⟨z2
Sn,
Rn−2⟩1
⟨Sn−2,
Rn−2⟩1
.
(12)
By convention, if n < 0 then
Rn,
Sn, αn, βn, γn are all zero.
Proposition 2.2 One has
αn
=
2 + a6n+4[3] −a2n
(13)
βn−1
=
(a4n+1 + a8n+1[3]){2n}{2n + 1}
(14)
γn−2
=
a10n−4{2n −2}{2n −1}{2n}{2n + 1}
(15)
Proof The formula for γn−2 is the easiest. Let us use the notation o≤n for
terms of degree ≤n. Since z2
Rn−2 =
Rn + o≤n−1, we have
⟨z2
Sn,
Rn−2⟩1 = ⟨Sn, z2
Rn−2⟩1 = ⟨Sn,
Rn⟩1 ,
and hence formula (15) follows from (12), (10), and (5).
For βn−1, we need to compute
⟨z2
Sn,
Rn−1⟩1 = ⟨Sn, z2
Rn−1⟩1 = µ2nµn−1⟨Sn, tz2t−1Rn−1⟩.
(16)
This amounts to computing the coeﬃcient of Rn in the expression of tz2t−1Rn−1
in the Rk-basis. This coeﬃcient can be computed as follows.
For n ≥1, one has
zn = en + (n −1)en−2 + o≤n−4 .
Algebraic & Geometric Topology, Volume 3 (2003)
Skein-theoretical derivation of some formulas of Habiro
543
(This follows by induction from (2).) Thus, for ε = ±1, one has
tεzn = µε
nzn + (n −1)(µε
n−2 −µε
n)zn−2 + o≤n−4 .
It follows that
tz2t−1zn = µn+2
µn
zn+2 + (2 −(n + 1)µn+2
µn
+ (n −1) µn
µn−2
)zn + o≤n−2 .
(17)
Now write
Rn =
n−1
Y
i=0
(z −λ2i) = zn −xn−1zn−1 + o≤n−2 ,
where xn−1 = Pn−1
i=0 λ2i. Then (17) gives
tz2t−1Rn−1 = µn+1
µn−1
Rn+1 + (xn
µn+1
µn−1
−xn−2
µn
µn−2
)Rn + o≤n−1
(18)
and hence
⟨Sn, tz2t−1Rn−1⟩= (xn
µn+1
µn−1
−xn−2
µn
µn−2
)⟨Sn, Rn⟩.
Plugging this into (16), we have
⟨z2
Sn,
Rn−1⟩1 =µ2nµn−1⟨Sn, tz2t−1Rn−1⟩
=(xn
µn+1
µn
−xn−2
µn−1
µn−2
)⟨Sn,
Rn⟩1
=(A6n+1[3] + A−2n+1)⟨Sn,
Rn⟩1 .
Using (12), (10), and (5) as before, this implies formula (14) for βn−1.
Finally, for αn, let us compute
⟨z2
Sn,
Rn⟩1 = µ2nµn⟨tz2t−1Sn, Rn⟩.
(19)
This amounts to computing the coeﬃcient of Sn in the expression of tz2t−1Sn
in the Sk-basis.1
The computation is similar to the one above. We write
Sn =
n−1
Y
i=0
(z2 −λ2
i ) = z2n −yn−1z2n−2 + o≤2n−4 ,
1This is easier than computing ⟨Sn, tz2t−1Rn⟩by expanding tz2t−1Rn in the Rk-
basis, because the latter would require computing the ﬁrst three terms, and not just
the ﬁrst two terms as in (18) above and also in (20) below.
Algebraic & Geometric Topology, Volume 3 (2003)
544
Gregor Masbaum
where yn−1 = Pn−1
i=0 λ2
i . Then (17) gives
tz2t−1Sn =
(20)
µ2n+2
µ2n
Sn+1+

2 + (yn −2n −1)µ2n+2
µ2n
−(yn−1 −2n + 1) µ2n
µ2n−2

Sn + o≤2n−2
and hence
⟨tz2t−1Sn, Rn⟩=

2 + (yn −2n −1)µ2n+2
µ2n
−(yn−1 −2n + 1) µ2n
µ2n−2

⟨Sn, Rn⟩
= (2 + a6n+4[3] −a2n)⟨Sn, Rn⟩.
Plugging this into (19), we get
⟨z2
Sn,
Rn⟩1 = (2 + a6n+4[3] −a2n)⟨Sn,
Rn⟩1 ,
proving formula (13) for αn.
Proof of Habiro’s Theorem 1.1 As already observed, we have
cn,−= ⟨t−1Sn⟩
⟨Rn, Sn⟩= µ−1
2n
⟨Sn⟩
⟨Rn, Sn⟩.
But ⟨Sn⟩satisﬁes the recursion relation
⟨Sn+1⟩= (λ2
0 −αn)⟨Sn⟩−βn−1⟨Sn−1⟩−γn−2⟨Sn−2⟩
(21)
(since ⟨z⟩= λ0). It follows that
⟨Sn⟩= (−1)na(3n2+n)/2 {n + 1}{n + 2} · · · {2n + 1}
{1}
,
(22)
since one can check that (22) is true for n = 0, 1, 2 and that it solves the
recursion (21). This implies Habiro’s formula (9) for cn,−. Taking conjugates,
one then also obtains formula (7) for cn,+.
Remark 2.3 Although it might be hard to guess formula (22), once one knows
it the recursion relation (21) is easily checked. Observe that λ2
0 = a2 + a−2 −2.
Put q(n) = (3n2 + n)/2. Then (21) is equivalent to
(a2 + a−2 −a6n+4[3] + a2n)aq(n) + (a4n+1 + a8n+1[3]){n}aq(n−1)
−a10n−4{n −1}{n}aq(n−2) = −{2n + 2}{2n + 3}
{n + 1}
aq(n+1)
which is a straightforward computation.
Algebraic & Geometric Topology, Volume 3 (2003)
Skein-theoretical derivation of some formulas of Habiro
545
