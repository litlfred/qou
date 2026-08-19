---
doc_id: arxiv-1203.2182v1
doc_title: "Volume Conjecture: Reﬁned and Categoriﬁed"
section_id: sec-025-1-kaqt
section_title: "(K;a,q,t )"
section_number: 1
pages: 28-31
source_pdf: 1203.2182v1.pdf
source_sha256: 2fe21af194f65227
doc_brief: "Volume Conjecture: Refined and Categorified — The generalized volume conjecture relates asymptotic behavior of the colored Jones polynomials to objects naturally deﬁned on an algebra ic curve, the"
---
= arsq−r2st0 + (1 +a−1qrt−1)Qr(K;a,q,t ). (3.81)
5The slice genus of a knot K in S3 (sometimes also known as the Murasugi genus or four-ball gen us) is the
least integer g∗, such that K is the boundary of a connected, orientable surface of genus g∗ embedded in the
4-ball B4 bounded by S3. The slice genus is also a lower bound for the unknotting numb er of the knot K, i.e.
the least number of times that the string must be allowed to pa ss through itself in order to “untie” the knot.
– 27 –
It is easy to verify that all our results indeed have this rema rkable structure. Indeed, using
(3.79) for K = T 2,2p+1 and specializing to a = −q−1t−3 and a = −qrt−1 in (3.65) we ﬁnd
that, respectively, only ℓ =r and ℓ = 0 contributions survive.
For completeness, let us describe how the same structure looks in the “DGR conventions”
(3.68) and (3.69). The grading of the canceling diﬀerentials d1 and d−r for R = Sr can be
read oﬀ directly from (3.54):
degDGR (d1) = (−2, 2, −1) and deg DGR (d−r) = (−2, −2r, −2r − 1), (3.82)
and, similarly, the gradings of the canceling diﬀerentials d−1 and dr for R = Λr are
degDGR (d−1) = (−2, −2, −3) and deg DGR (dr) = (−2, 2r, −1). (3.83)
Substituting these values of ( a,q,t )-degrees (α,β,γ ) in the general formula (3.9), we arrive
to the following structure of the colored superpolynomials in the grading conventions of [27]:
P Sr
DGR(K;a,q,t ) = a2rsq−2rst0 + (1 +a−2q−2t−1)QDGR
1 (K;a,q,t )
= a2rsq2r2st2r2s + (1 +a−2q−2rt−2r−1)QDGR
−r (K;a,q,t ), (3.84)
P Λ r
DGR(K;a,q,t ) = a2rsq2rst2rs + (1 +a−2q−2t−3)QDGR
−1 (K;a,q,t )
= a2rsq−2r2st0 + (1 +a−2q2rt−1)QDGR
r (K;a,q,t ). (3.85)
Using s =p for K =T 2,2p+1, it easy to verify that our results (3.68) and (3.69) exhibit this
structure, ensuring the validity of some of the steps in sect ion 3.1.1.
While the above discussion hopefully makes it fairly convincing how powerful and elegant
the structure of diﬀerentials is, it is just the tip of an icebe rg! Indeed, besides the canceling
diﬀerentials that we discussed in detail and that, in many cas es, alone suﬃce for deducing
the superpolynomials from the colored HOMFLY polynomials, there is yet another class of
“universal” diﬀerentials found in [44]. These diﬀerentials a re called “colored” because they
relate homology theories associated with diﬀerent represen tations. The simplest example of
a colored diﬀerential discussed in [44] is a diﬀerential that, when acting on the S2-colored
HOMFLY homology, leaves behind the ordinary, S-colored HOMFLY homology, modulo a
simple re-grading: (
HS2
(K),d colored
)
2i,k+2j,2k
∼
= H□
i,j,k(K). (3.86)
As in our discussion of (3.75) and (3.77), we can take Poincar ´ e polynomials of both sides to
learn the following structure of the S2-colored superpolynomial,
P S2
(K;a,q,t ) = P(K;a2,q 2,qt 2) + (1 +q)Q(a,q,t ), (3.87)
which corresponds to the ﬁrst colored diﬀerential on our list (3.54). Similarly, the second
colored diﬀerential in (3.54) acts a little diﬀerently and lea ds to a similar, but diﬀerent
relation:
P S2
(K;a,q,t ) = asP(K;a,q 2,t ) + (1 +a−1t−1)Q(a,q,t ). (3.88)
– 28 –
Both superpolynomials P S2
(K;a,q,t ) and P(K;a,q,t ) that participate in these relations can
be easily determined from the corresponding HOMFLY polynom ials by using the structure
of either d2 or canceling diﬀerentials. Indeed, as a yet another illustra tion of this method, let
us explain how it works for the torus knots we are interested i n.
In the case of torus knots, the starting point of this constru ction – namely, the colored
HOMFLY polynomial – is available e.g. from [55]. In fact, for R =S, the explicit expression
for the (uncolored) HOMFLY polynomial of an arbitrary torus knot was written already by
Jones [58]. In our conventions, the answer for (2 , 2p + 1) torus knots reads
P (T 2,2p+1;a,q ) = −ap+1
p∑
i=1
q2i−p−1 +ap
p∑
i=0
q2i−p. (3.89)
The corresponding (uncolored) superpolynomials of torus k nots have the same structure [27].
In fact, for T 2,2p+1 torus knots, all of the terms in the superpolynomial P(T 2,2p+1;a,q,t )
are “visible” in the HOMFLY polynomial (3.89) and, therefor e, can be determined from the
structure (3.77) associated with two canceling diﬀerentialsd1 andd−1. In our grading conven-
tions (3.76), these canceling diﬀerentials for r = 1 have degree ( −1, 1, −1) and ( −1, −1, −3),
respectively. Hence, restoring the powers of t in (3.89) consistent with d1 and d−1 we get
P(T 2,2p+1;a,q,t ) = ap+1
p∑
i=1
q2i−p−1t2i+1 +ap
p∑
i=0
q2i−pt2i
= apqpt2paq−1t(1 −q−2pt−2p) + 1 −q−2p−2t−2p−2
1 −q−2t−2 .
Similarly, starting with the S2-colored HOMFLY polynomial (see e.g. [55]), one can derive
the S2-colored superpolynomial for all (2, 2p + 1) torus knots,
P S2
(T 2,2p+1;a,q,t ) = q4t4(aq2t2)2p(1 +at)(q +at)
1 −q2(1 +q)t2 +q5t4 (3.90)
− q2t2(1 +q)(aqt)2p(q +at)(1 +aq2t3)
1 −q2(1 +q2)t2 +q6t4 + (aq−1)2p(1 +aq2t3)(1 +aq3t3)
1 −q3(1 +q)t2 +q7t4
which, of course, is consistent with our earlier result (3.6 1). Substituting these colored su-
perpolynomials into relations (3.87) and (3.88), it is easyto verify that they work like a charm.
Finally, after an exciting discussion of colored and cancel ing diﬀerentials that have a
universal nature, let us consider a somewhat more rudimentary diﬀerentiald2 that, according
to (3.53), controls specialization to thesl(2) knot homology, see also Figure 2. This diﬀerential
is actually very important for the subject of our paper since it accompanies the specialization
toa =q2 and, hence, the deﬁnition of the invariantPn(q,t ) that appears in the reﬁned volume
conjectures (2.1) and (2.6). This invariant is deﬁned as a sp ecialization (3.11):
Pn=r+1(K;q,t ) := P Sr
(K;a =q2,q,t ) (3.91)
– 29 –
and, contrary to (3.8), for (2 , 2p + 1) torus knots appears to coincide with the Poincar´ e
polynomial of then-coloredsl(2) knot homology Hsl(2),Vn(K). Indeed, as one can see directly
from (3.90), for the trefoil knotT 2,3 = 31 theS2-colored HOMFLY homology simply contains
no terms that can be killed byd2. For the next torus knotT 2,5 = 51, there are such terms, but
according to our discussion around (3.74), none of them are c anceled by d2, i.e. Qsl(2),S2
= 0
in (3.9), etc.
The fact that Pn(T 2,2p+1;q,t ) deﬁned in (3.91) appears to coincide with the Poincar´ e
polynomial P sl(2),Vn(T 2,2p+1;q,t ) of the n-colored sl(2) knot homology has an important
implication: it suggests that the homological volume conje ctures (2.1) and (2.6) can be for-
mulated directly in terms of the sl(2) knot homology, as in (2.2), rather than in terms of the
specialization of the colored superpolynomial (3.11). For example, such homological version
of the generalized volume conjecture (2.6) has a nice form
∑
i,j
qitj dim Hsl(2),Vn
i,j (K) ≃ exp
(
1
ℏS0(u,t ) +
∞∑
k=0
Sk+1(u,t ) ℏk
)
(3.92)
and describes the asymptotic growth of the dimensions of then-coloredsl(2) homology groups
in the limit (2.5):
q =eℏ → 1, t = ﬁxed, x ≡eu =qn = ﬁxed. (3.93)
Similarly, the homological version of the quantum volume co njecture (2.1) presumably can
be formulated in the form of an exact sequence
0 − → C n − →an
C n+1 − →an+1
C n+2 − →an+2
... C n+d − → 0 (3.94)
where
C n(K) =
⨁
i,j∈Z
Hsl(2),Vn
i,j (K) (3.95)
and the maps aj are determined by the coeﬃcients of the quantum operator
ˆAref(ˆx,ˆy;q,t ) =
d∑
j=0
aj(ˆx;q,t )ˆyj. (3.96)
Although we believe that both volume conjectures (2.1) and ( 2.6) work equally well for the
sl(2) homological knot invariants (2.2) as well as for the spec ialization of the colored super-
polynomial (3.11), we leave this question to a future work. 6
In what follows we simply adopt (3.11) as a deﬁnition of Pn(q,t ). Then, from (3.61) we
have
Pn(T 2,2p+1;q,t ) =
n−1∑
ℓ=0
(−1)n−1
[
(−1)ℓq
(n−1)(n+1)−ℓ(ℓ+1)
2 t
3
