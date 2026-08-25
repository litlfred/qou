---
doc_id: zagier-the-dilogarithm-function-copy-b
doc_title: "The Dilogarithm Function Don Zagier"
section_id: sec-035-30-don-zagier
section_title: "Don Zagier"
section_number: 30
pages: 28-29
source_pdf: zagier-the-dilogarithm-function-copy-b.pdf
source_sha256: c584944a501ef0c5
doc_brief: "The dilogarithm function — 56 sections: Don Zagier; The dilogarithm function in geomet; The Bloch-Wigner function D(z) and"
duplicate_of: "zagier-the-dilogarithm-function"
---
Proof. All three of these identities can be proved in essentially the same way.
To emphasize this, we present the three proofs simultaneously. S ince ( x)∞ is
obviously a power series in x with constant term 1, we can write
(x)∞ =
∞∑
n=0
an xn , 1
(x)∞
=
∞∑
n=0
bn xn , − log(x)∞ =
∞∑
n=1
cn xn
for some coeﬃcients an, bn and cn depending on q, a0 = b0 = 1. Combining
each of these expansions with the functional equation ( x)∞ =( 1 − x)( qx)∞
and comparing the coeﬃcients of xn on both sides, we ﬁnd
(1 − qn) an = −qn−1 an−1 , (1 − qn) bn = bn−1 , (1 − qn) cn = 1
n ,
from which the desired formulas
an = (−1)n q(
n
2)
(q)n
,b n = 1
(q)n
cn = 1
n · 1
1 − qn (10)
follow immediately or by induction. Note that the third identity of th e propo-
sition can also be proved directly, without using the functional eq uation of
(x)∞, by the calculation
− log(x)∞ =
∞∑
i=0
− log(1 − qix)=
∞∑
i=0
∞∑
n=1
1
n qin xn =
∞∑
n=1
xn
n (1 − qn) ,
i.e., Li 2(x; q)= ∑ ∞
i=0 Li1(qix).
The second surprise is the discovery by Faddeev and Kashaev [15] that t he
q-dilogarithm satisﬁes a non-commutative 5-term functional equation whi ch
degenerates in the limit q → 1 to the classical 5-term functional equation
of the classical dilogarithm. We content ourselves with stating and pro ving
the ﬁrst statement only, referring the reader for the second statem ent (which
involves the use of the Baker-Campbell-Hausdorﬀ formula) to the original
paper, or to the more recent survey paper by Zudilin [48].
Proposition 3 ([38], [15], [22]). Let u and v be non-commuting variables
satisfying the commutation relation
uv = qvu. (11)
Then
(v)∞ (u)∞ =( u)∞ (−vu)∞ (v)∞ . (12)
Proof. Expanding each factor ( x)∞ in (12) by equation (7) and observing that
vnum = q−mnumvn and ( vu)s = q−(
s+1
2 )usvs, we ﬁnd that (12) is equivalent
to the generating series identity
The Dilogarithm Function 31
∑
m, n≥0
q−mn am an um vn =
∑
r, s, t≥0
(−1)sq−(
s+1
2 ) ar as at ur+s vs+t
with an as in (10) or, comparing coeﬃcients of like monomials, to the combi-
natorial identity
∑
r, s, t≥0
r+s=m, s+t=n
qrt
(q)r (q)s (q)t
= 1
(q)m (q)n
(m, n ≥ 0) . (13)
(Amusingly, if we write (12) in the equivalent form ( v)−1
∞ (−vu)−1
∞ (u)−1
∞ =
(u)−1
∞ (v)−1
∞ and expand each term ( x)−1
∞ using (8) instead of (7), then the
combinatorial identity to be proved turns out to exactly the same form ula
(13), but with q replaced by q−1.) Identity (13) can be proved either using
generating functions (now commutative!) by multiplying both side s by xmyn,
summing over m, n ≥ 0, and applying (8) and the easy identity∑ ∞
r=0
(y)r
(q)r
xr =
(xy)∞
(x)∞
, or else by using the standard recursion property
[ m+1
s
]
= qs[ m
s
]
+
[ m
s−1
]
of the q-binomial coeﬃcient
[ m
s
]
= (q)m
(q)s(q)m−s
to show that the numbers
Cm,n :=∑
s
[ m
s
]
q(m−s)(n−s) (q)n
(q)n−s
satisfy Cm+1,n = qnCm,n +( 1 − qn)Cm,n−1
and hence by induction Cm,n = 1 for all m, n ≥ 0.
E. The p-adic dilogarithm and the dianalog. The next dilogarithm
variant we mention is the p-adic dilogarithm, studied by R. Coleman and
other authors. We ﬁx a prime number p and deﬁne
Li(p)
