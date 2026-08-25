---
doc_id: arxiv-2007.10190v2
doc_title: "THE RESURGENT STRUCTURE OF QUANTUM KNOT INVARIANTS"
section_id: sec-005-43-the-state-integral-and-its-descendants
section_title: "The state integral and its descendants"
section_number: 4.3
pages: 9-11
source_pdf: 2007.10190v2.pdf
source_sha256: 37bcbd3a343bb21a
doc_brief: "THE RESURGENT STRUCTURE OF QUANTUM KNOT INVARIANTS — The asymptotic expansion of quantum knot invariants in complex Chern-Simons theory gives rise to factorially divergent formal power series."
---
of state integrals and some of their basic properties. State integrals are multidimensional
integrals whose integrand is a product of Faddeev’s quantum dilogarithm function Φb (whose
deﬁnition we will not need and may be found in [Fad95, FK94]) times an exponential of a
quadratic and linear form. Here τ = b2∈ C ′ := C \ (−∞, 0], thus even if the integrand
contains no free variables, a state integral is always a holomorphic function of τ.
State integrals have two key properties:
(a) they deﬁne holomorphic functions in the complex cut plane C ′.
(b) they can be expressed bilinearly in the upper and in the lower half-plane in terms of
products of q-series and ˜q-series.
For a detailed discussion of state integrals and numerous example, see for instance [BDP14]
and also [AK14] and [GK17].
In this section we introduce a descendant version of the one dimensional state integrals
of [GK17] that satisﬁes the above properties. In this section we will use the notation
from [GK17]. Consider the state integral
IA,B,λ,µ(b) =
∫
R +iϵ
Φb(x)Be−Aπix2+2π(λb−µb−1)xdx, (λ,µ∈ Z ) (39)
where A and B are integers and B > A >0. Under these assumptions, it follows that the
integrand is exponentially decaying at inﬁnity and the integral is absolutely convergent and
deﬁnes a holomorphic function of τ = b2∈ C ′. Below, we will use the notation φ(w,δ•),
˜φ(w, ˜δ•) and
⟨F (q,x )⟩ =F (q, 1) (40)
from [GK17].
Theorem 3. Fix integers A and B with B > A >0 and integers λ and µ. For all τ with
ℑ(τ)> 0, we have:
IA,B,λ,µ(b) = (−1)λ−µq
λ
2 ˜q
µ
2
( ˜q
q
)B−3A
24
eπiB+2(A+1)
4 ⟨PA,B,λ,µ
(
FA,B,λ(q,x )~FA,B,µ(˜q, ˜x)
)
⟩ (41)
where the operator PA,B,λ,µ is given by
PA,B,λ,µ = Resw=0
(
e
w2
4πi +w(b(δ+1/2+λ/A)+b−1(˜δ+1/2−µ/A)))A
(
φ(bw,δ•)˜φ(b−1w, ˜δ•)
b(1− eb−1w)
)B
. (42)
In particular, the right hand side of Equation (41) is a bilinear combination ofq and ˜q-series
extend to the cut plane C ′. A similar formula can be given when τ is in the lower half-plane,
and what is more, the state integral satisﬁes the symmetry IA,B,λ,µ(b) =IA,B,λ,µ(b−1) which
is a consequence of the symmetry Φ b−1(x) = Φb(x) of the quantum dilogarithm.
Proof. We follow the derivation in [GK17] closely. The idea is to sum up residues at all
singularities in the upper half-plane. The factor Φ b(x) has poles at
xm,n = ib(m + 1/2) + ib−1(n + 1/2), m,n ∈ N . (43)
10 STA VROS GAROUF ALIDIS, JIE GU, AND MARCOS MARI ˜NO
We notice that
e2π(λb−µb−1)(x+xm,n) = ew(λb−µb−1)qλ(m+1/2)˜qµ(n+1/2)(−1)λ−µ (44)
where we have made the change of variables w = 2πx and used the notation
q = e2πib2
, ˜q = e−2πib−2
. (45)
Now by modifying Eqn.(27) of [GK17], we ﬁnd
IA,B,λ,µ(b) = (−1)λ−µq
λ
2 ˜q
µ
2
( ˜q
q
)B−3A
24
eπiB+2(A+1)
4 ×
∞∑
m,n=0
(Resw=0FA,B,m,n,λ,µ(w))qλmtm(q)A
(q;q)B
m
˜qµn˜tn(˜q)A
(˜q−1; ˜q−1)B
n
, (46)
where
FA,B,m,n,λ,µ(w) =
(
e
w2
4πi +w(b(m+1/2+λ/A)+b−1(n+1/2−µ/A)))A
(
φm(bw)˜φn(b−1w)
b(1−eb−1w)
)B
. (47)
Using the operator formalism in [GK17], this concludes the proof of Equation (41). □
The reader may ﬁnd in [GK17] the expressions of the operators φ(w,δ•), ˜φ(w, ˜δ•). Note
that el(˜q) in the paper are simply E(0)
l (˜q). In addition,
FA,B,λ(q,x ) =
∞∑
n=0
(−1)AnqAn(n+1)
2 +nλ
(q;q)B
n
xn, (48)
~FA,B,µ(˜q, ˜x) =
∞∑
n=0
(−1)(B−A)n ˜q(B−A)n(n+1)
2 +nµ
(˜q; ˜q)B
n
˜xn. (49)
They can be related by
FA,B,λ(q−1,x ) = ~FA,B,−λ(q,x ). (50)
Example 4. In this example we illustrate theorem 3 with the state integral I1,2,λ,µ(b) asso-
ciated to the 4 1 knot [AK14]. As we will see, this reproduces the q-series G0
m(q) and G1
m(q)
of (13a) and (13b).
Using
Fλ(q,x ) =F1,2,λ(q,x ) = ~F1,2,λ(q,x ) =
∞∑
n=0
(−1)nq
n(n+1)
2 +nλ
(q;q)2
n
xn. (51)
we ﬁnd that
P1,2,λ,µ = b
2(1 + 2δ− 4δ1 + 2λ)− b−1
2 (1 + 2˜δ− 4˜δ1 + 2µ). (52)
It then follows that (τ = b2)
I1,2,λ,µ(b) = (−1)λ−µ+1iq
λ
2 ˜q
µ
2
(q
˜q
) 1
24
(τ 1/2
2 G1
λ(q)G0
µ(˜q)− τ−1/2
2 G0
λ(q)G1
µ(˜q)
)
, (53)
THE RESURGENT STRUCTURE OF QUANTUM KNOT INV ARIANTS 11
where we have used that
⟨Fλ(q,x )⟩ =G0
λ(q), ⟨(1 + 2λ + 2δ− 4δ1)Fλ(q,x )⟩ =G1
λ(q). (54)
In appendix A, we give the details for the state integral I2,3,λ,µ(b) of the 5 2 knot.
