---
doc_id: arxiv-2104.07437v4
doc_title: "Peacock patterns and new integer invariants in topological string theory"
section_id: sec-011-333-second-spectral-trace-and-its-factorisation
section_title: "Second spectral trace and its factorisation"
section_number: 3.3.3
pages: 34-38
source_pdf: 2104.07437v4.pdf
source_sha256: a0f28a6b61618467
---
The TS/ST correspondence allows us to write down an integral representation of the second
trace. In principle the second bosonic trace Tr ρ2
P2 involves a double integral of a product of the
integral kernel (3.109), but it was shown in [59] that it can be converted into a one-dimensional
integral. Using the result of the ﬁrst trace (3.113), this translates into the following integral
representation of the normalised second trace
Tr′ρ2
P2 =
√
3bΦb(− ib
6− ib−1
2 )2
Φb( ib
6 + ib−1
2 )2
∫
R
sinh(2πhx)
sinh(πbx)
Φb(x− ib
3 +cb)2
Φb(x + ib
3−cb)2 e2πx( 1
3 b+b−1)dx. (3.141)
In order to perform the large b expansion of the integral (3.141), one can ﬁrst do the scaling
x→ b−1x and then use the formula of semi-classical expansion of the quantum dilogarithm (A.16)
for large b (or equivalently (A.15) for small bD = 1/b). After evaluating convergent integrals
∫
R
sinh( 1
3πx)
sinh(πx) x2ndx = 2(−1)n−1
2n + 1 B2n+1( 1
3)32n+1/2, n = 0, 1, 2,..., (3.142)
one ﬁnds that
Tr′ρ2
P2∼ Φ0;2(gs) = 1 + 8π2
9
√
3gs + 16π4
81 g2
s +..., g s =− 3
2π b−2→ 0, (3.143)
justifying the prediction (3.121) of the TS/ST correspondence. Using the technique explained
in Appendix B, we are able to compute 700 terms of this series, which allows us to perform in
detail the resurgence analysis.
The integral form (3.141) of the normalised second trace can be evaluated explicitly by closing
the contour of integral from above and summing up residues of poles. Following the exercise in
Section 3.2.2, it is helpful to introduce artiﬁcially a “mass” deformation of the integral so that
the integrand only has simple poles, and then turn oﬀ the mass deformation.
We consider the following integral
I(ξ, b) =
∫
R
sinh(2πhx)
sinh(πbx)
Φb(x + ξb
2π− 2ia +cb)Φb(x− ξb
2π− 2ia +cb)
Φb(x + ξb
2π + 2ia−cb)Φb(x− ξb
2π + 2ia−cb)
e2πx( 1
3 b+b−1)dx. (3.144)
– 33 –
We only consider the case ξ is small and Im b2 > 0. Since Re b> 0, the poles in the upper half
plane are
ib−1k, ±ξb
2π + 2ia + irb + isb−1, k = 1, 2, 3,..., r,s = 0, 1, 2, 3,... (3.145)
After summing up the residues at these poles, by using (A.6), we arrive at
I(ξ, b) =ib−1h0(x,q )˜h0(˜x, ˜q)
+ibw−1
a
(
h+
1 (x,q )˜h+
1 (˜x, ˜q)−h+
2 (x,q )˜h+
2 (˜x, ˜q)
+h−
1 (x,q )˜h−
1 (˜x, ˜q)−h−
2 (x,q )˜h−
2 (˜x, ˜q)
)
, (3.146)
where we deﬁned
x := eξb2
, ˜x := eξ. (3.147)
The holomorphic blocks are
h0(x,q ) =(q2/3x;q)∞(q2/3x−1;q)∞
(q1/3x;q)∞(q1/3x−1;q)∞
, (3.148a)
h+
1 (x,q ) =q1/3x (q;q)∞
(q2/3;q)∞
(qx2;q)∞(q4/3x;q)∞
(q2/3x2;q)∞(q1/3x;q)∞
3φ2
(q2/3,q 2/3x2,q 1/3x
qx2,q 4/3x ;q,q
)
, (3.148b)
h+
2 (x,q ) =q2/9x2/3 (q;q)∞
(q2/3;q)∞
(qx2;q)∞(q4/3x;q)∞
(q2/3x2;q)∞(q1/3x;q)∞
3φ2
(q2/3,q 2/3x2,q 1/3x
qx2,q 4/3x ;q,q 2/3
)
, (3.148c)
as well as
h−
1 (x,q ) =h+
1 (x−1,q ), h −
2 (x,q ) =h+
2 (x−1,q ). (3.149)
The anti-holomorphic blocks are
˜h0(˜x, ˜q) =(˜qw−1
a ˜x; ˜q)∞(˜qw−1
a ˜x−1; ˜q)∞
(wa˜x; ˜q)∞(wa˜x−1; ˜q)∞
×
(
3φ2
( ˜q,wa˜x,wa˜x−1
˜qw−1
a ˜x, ˜qw−1
a ˜x−1; ˜q, ˜qw−1
a
)
− 3φ2
( ˜q,wa˜x,wa˜x−1
˜qw−1
a ˜x, ˜qw−1
a ˜x−1; ˜q, ˜q
))
, (3.150a)
˜h+
1 (˜x, ˜q) =˜x(˜qwa; ˜q)∞
(˜q; ˜q)∞
(˜qwa˜x2; ˜q)∞
(˜x2; ˜q)∞
2φ1
(w−1
a ,w−1
a ˜x−2
˜q˜x−2 ; ˜q, ˜qw−1
a
)
, (3.150b)
˜h+
2 (˜x, ˜q) =˜x(˜qwa; ˜q)∞
(˜q; ˜q)∞
(˜qwa˜x2; ˜q)∞
(˜x2; ˜q)∞
2φ1
(w−1
a ,w−1
a ˜x−2
˜q˜x−2 ; ˜q, ˜q
)
, (3.150c)
as well as
˜h−
1 (˜x, ˜q) = ˜h+
1 (˜x−1, ˜q), ˜h−
2 (˜x, ˜q) = ˜h+
2 (˜x−1, ˜q). (3.151)
In the equations above,
wa = e−4πia/b = e−2πi/3. (3.152)
The factorisation formula (3.146) can be further simpliﬁed. The holomorphic blocks h+
1 (x,q )
and h+
2 (x,q ) can also be expressed in terms of q-Appell functions, deﬁned in (A.24),
h+
1 (x,q ) =q1/3x(q5/3;q)∞
(q2/3;q)∞
Φ(1)(q;q1/3,q ;q5/3;q;q2/3x2,q 1/3x), (3.153a)
h+
2 (x,q ) =q2/9x2/3 (q;q)∞(q4/3;q)∞
(q2/3;q)2∞
Φ(1)(q2/3;q1/3,q ;q4/3;q;q2/3x2,q 1/3x). (3.153b)
– 34 –
The summand of a q-Appell function Φ (1)(a;b,b′;c;q;x,y ) is q-holonomic. By using Takayama’s
algorithm [88, 89] of creative telescoping, implemented in the HolonomicFunctions package of
Koutschan [90, 91], we ﬁnd thath+
1 (x,q ),h+
2 (x,q ), together with the remaining three holomorphic
blocks, satisfy a third order linear diﬀerence equation
C3(x;q)h(q3x;q) +C2(x;q)h(q2x;q) +C1(x;q)h(qx;q) +C0(x;q)h(x;q) = 0, (3.154)
where
C3(x;q) =(1−qx)(1 +qx)(1−q5/3x)(1−q8/3x)2(1 +q8/3x)(1−qx2)(1−q13/3x2),
C2(x;q) =−q1/3(1−q5/3x)(1−q2x)(1 +q2x)(1−qx2)
(
1 +q1/3 +q2/3−q4/3(1−q1/3 +q2/3 + 2q)x
− (1 +q1/3)q2(1 +q−q4/3 + 2q2− 3q7/3 + 2q8/3 +q10/3)x2
+ (1 +q1/3)q4(1 + 2q2/3− 3q + 2q4/3−q2 +q7/3 +q10/3)x3
+q22/3(2 +q1/3−q2/3 +q)x4− (1 +q1/3 +q2/3)q9x5
)
,
C1(x;q) =q(1−qx)(1 +qx)(1−q4/3x)(1−q5x2)
(
1 +q1/3 +q2/3−q4/3(2 +q1/3−q2/3 +q)x
− (1 +q1/3)q(1 + 2q2/3− 3q + 2q4/3−q2 +q7/3 +q10/3)x2
+ (1 +q1/3)q2(1 +q−q4/3 + 2q2− 3q7/3 + 2q8/3 +q10/3)x3
+q13/3(1−q1/3 +q2/3 + 2q)x4− (1 +q1/3 +q2/3)q6x5
)
,
C0(x;q) =−q2(1−q1/3x)2(1 +q1/3x)(1−q4/3x)(1−q2x)(1 +q2x)(1−q5/3x2)(1−q5x2).
(3.155)
Therefore there are only three linearly independent holomorphic blocks. By making the ansatz
that
hi0(x,q ) =f1(x,q )hi1(x,q ) +f2(x,q )hi2(x,q ) +f3(x,q )hi3(x,q ), (3.156)
where hi0(x,q ),hi1(x,q ),hi2(x,q ),hi3(x,q ) are any four holomorphic blocks and the coeﬃcients
fj(x,q ) are elliptic functions satsifying fj(qx,q ) =fj(x,q ), we ﬁnd
h+
2 (x,q ) =− q2/9(q;q)2
∞θ(−q−1/2x;q)
x1/3θ(−q−1/6;q)∞θ(−q−1/6x;q)h0(x,q )
− x2/3θ(−q−1/6x2;q)
q1/9θ(−q−1/2x2;q) (h+
1 (x,q )−h−
1 (x,q )), (3.157a)
h−
2 (x,q ) =− q2/9x1/3(q;q)2
∞θ(−q−1/2/x;q)
θ(−q−1/6;q)θ(−q−1/6/x;q) h0(x,q )
+ θ(−q−1/6/x2;q)
q1/9x2/3θ(−q−1/2/x2;q)(h+
1 (x,q )−h−
1 (x,q )), (3.157b)
– 35 –
where we have used the notation
θ(x;q) = (−q1/2x;q)∞(−q1/2/x;q)∞. (3.158)
Notice thath+
1 (x,q ) andh−
1 (x,q ) always appear in these relations by the combination h+
1 (x,q )−
h−
1 (x,q ), which is also true in the factorisation (3.146) once we take into account the fact that
˜h−
1 (˜x, ˜q) =−˜h+
1 (˜x, ˜q). We can therefore write down a simpliﬁed factorisation of I(ξ, b) by using
only two reduced (anti-)holomorphic blocks
I(ξ, b) = ib−1h0(x,q )~hred
0 (˜x, ˜q) + ibw−1
a hred
1 (x,q )~hred
1 (˜x, ˜q), (3.159)
where
hred
1 (x,q ) =h+
1 (x,q )−h−
1 (x,q ), (3.160)
and
~hred
0 (˜x, ˜q) =~h0(˜x, ˜q) +w−1
a
(˜q; ˜q)2
∞θ(−˜q1/2˜x; ˜q)
θ(−˜q1/2wa; ˜q)θ(−˜q1/2w−1a ˜x; ˜q)
~h+
2 (˜x, ˜q)
+w−1
a
(˜q; ˜q)2
∞θ(−˜q1/2˜x−1; ˜q)
θ(−˜q1/2wa; ˜q)θ(−˜q1/2w−1a ˜x−1; ˜q)
~h−
2 (˜x, ˜q), (3.161a)
~hred
1 (˜x, ˜q) =~h+
1 (˜x, ˜q)−wa
θ(−˜q1/2w−1
a ˜x2; ˜q)
θ(−˜q1/2˜x2;tq)
~h+
2 (˜x, ˜q)
+wa
θ(−˜q1/2w−1
a ˜x−2; ˜q)
θ(−˜q1/2˜x−2;tq)
~h−
2 (˜x, ˜q). (3.161b)
Finally, taking the massless limit ξ→ 0 and using the relation
Tr′ρ2
P2 =
√
3bΦb(− ib
6− ib−1
2 )2
Φb( ib
6 + ib−1
2 )2 I(0, b), (3.162)
we ﬁnd the following elegant factorisation formula for the normalised second trace
Tr′ρ2
P2 = i
√
3
(
~H0(˜q) + 3b4H1(q)~H1(˜q)
)
, (3.163)
where the only non-trivial massless holomorphic block is
H1(q) =q1/3 (q;q)4
∞(q1/3;q)2
∞
(q2/3;q)5∞(q4/3;q)∞
3φ2
(q1/3,q 2/3,q 2/3
q,q 4/3 ;q,q 2/3
)
, (3.164)
and the massless anti-holomorphic blocks are
~H0(˜q) =3φ2
( wa,wa, ˜q
w−1
a ˜q,w−1
a ˜q; ˜q,w−1
a ˜q
)
− 3φ2
( wa,wa, ˜q
w−1
a ˜q,w−1
a ˜q; ˜q, ˜q
)
+ (˜q; ˜q)2
∞(˜qwa; ˜q)2
∞
(˜qw−1a ; ˜q)4∞
2φ1
(w−1
a ,w−1
a
˜q ; ˜q, ˜q
)
, (3.165a)
~H1(˜q) = 2(˜qwa; ˜q)6
(˜q; ˜q)3(˜qw−1a ; ˜q)3. (3.165b)
The simple factorisation formula (3.163) enables us to rapidly and accurately calculate the
value of the normalised second trace for gs in the upper half plane. Through a high precision
numerical calculation we ﬁnd the following relationship between the normalised second trace and
the Borel resummation of Φ 0;2(gs), Φ1;2(gs).
– 36 –
• Forgs in sector II
Tr′ρ2
P2 =sII (Φ0;2)(gs), (3.166)
thus Tr′ρ2
P2(b) furnishes a holomorphic lift of sII (Φ0;2)(gs).
• Forgs in sector I
Tr′ρ2
P2 =sI(Φ0;2)(gs) +sI(Φ1;2)(gs)K2(q), (3.167)
where
K2(q) =q1/6(1− 3q1/3 + 10q2/3 +... ). (3.168)
By comparing these two identities we conclude immediately
S+
01;2(q) =K2(q). (3.169)
We comment that the two relations (3.166), (3.167) also justify the claim (3.143). When gs is
in the second quadrant, (3.166) clearly implies (3.143). When gs is in the ﬁrst quadrant, (3.167)
indicates that in the leading order
Tr′ρ2
P2(b)∼ Φ0;2(gs) + e−(3VP2+ i
2 )/gs(... ) (3.170)
and the series Φ 0;2(gs) clearly dominates.
In the next subsection we consider the radial asymptotic analysis of the anti-holomorphic
blocks, which is a more eﬃcient way to compute the q-series S+
01;2.
