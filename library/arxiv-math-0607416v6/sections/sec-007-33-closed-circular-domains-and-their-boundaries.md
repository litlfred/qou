---
doc_id: arxiv-math-0607416v6
doc_title: "PÓLYA-SCHUR MASTER THEOREMS FOR CIRCULAR DOMAINS AND THEIR BOUNDARIES"
section_id: sec-007-33-closed-circular-domains-and-their-boundaries
section_title: "Closed Circular Domains and Their Boundaries"
section_number: 3.3
pages: 17-20
source_pdf: 0607416v6.pdf
source_sha256: 0705075947ce4a3d
---
and 4, Notation 4 and the linear operators φn introduced in Notation 5. In par-
ticular, an H-stable polynomial in the sense of Deﬁnition 4 is precisely a stable
polynomial in the sense of Deﬁnition 1.
Lemma 6. Let T : Cn[z] → Cm[z] be a linear operator and suppose m is minimal,
i.e., m = max{deg T (f ) : f ∈ Cn[z]}. Let further C = Φ −1(H) be an open circular
domain, where Φ is a M¨ obius transformation as in (2.2), and let S : Cn[z] → Cm[z]
be the linear operator deﬁned by S = φ−1
m T φn. The following are equivalent:
(i) T (f ) is C-stable or zero whenever f is of degree n and C-stable,
(ii) S(f ) is H-stable or zero whenever f is of degree n and H-stable,
(iii) S(f ) is H-stable or zero whenever f is of degree at most n and H-stable.
The following are also equivalent:
(iv) T (f ) is ∂C -stable or zero whenever f is of degree n and ∂C -stable,
(v) S(f ) is R-stable or zero whenever f is of degree n and R-stable,
(vi) S(f ) is R-stable or zero whenever f is of degree at most n and R-stable.
Proof. Note ﬁrst that the equivalences (ii) ⇔ (iii) and (v) ⇔ (vi) are simple conse-
quences of the density argument used in §2.2. Let us now show that (i) ⇔ (ii). This
is obvious if C is an open half-plane, i.e., if c = 0 (cf. (2.3)). Therefore we assume
that c ⁄= 0 and that the boundary of C is a circle. If C is an open disk then a/c
is in the open lower half-plane, so that −cz + a is H-stable. Moreover, −d/c ∈ ∂C
and thus cz + d is C-stable. Hence f is H-stable if and only if φn(f ) is C-stable so
the assertion follows in this case as well.
It remains to prove that (i) ⇔ (ii) in the case when C is the open complement
of a (closed) disk, which we proceed to do.
(i) ⇒ (ii). Clearly, we may assume that T is not the trivial (identically zero)
operator. Let p(z) = ∑ n
k=0 akzk be an H-stable polynomial of degree n and suppose
ﬁrst that ∑ n
k=0 akakcn−k ⁄= 0. Then φn(p) is a C-stable polynomial of degree n so
that by assumption T (φn(p)) is C-stable or zero. If S(p) ⁄= 0 it follows that that
we can express S(p) uniquely as S(p) = ( −cz + a)r(p)S0(p), where S0(p) is H-stable
and r(p) is a non-negative integer. By a continuity argument and an applicat ion
of Hurwitz’ theorem we have that a factorization as above holds fo r any H-stable
polynomial of degree n. Since the set of H-stable polynomials of degree n is dense
in πn(H ′) ∪ {0} – that is, the set of H-stable polynomials of degree at most n union
the zero polynomial – we deduce that such a factorization holds for the image under
S of any H-stable polynomial p of degree at most n, namely
S(p) = ( −cz + a)r(p)S0(p),
where S0(p) is H-stable or zero and r(p) is a non-negative integer.
Fix a basis {pj(z)}n
j=0 of Cn[z] consisting of strictly H-stable (that is, H-stable)
polynomials of degree n. We distinguish two cases:
Suppose ﬁrst that S(f ) ⁄= 0 for all strictly H-stable polynomials f of degree
n. Since the topological space of strictly stable polynomials of degree n is (path-)
connected we have by Hurwitz’ theorem that r(f ) is constant on the set of strictly
H-stable polynomials of degree n. Thus, by the minimality assumption on m and
the fact that φn is invertible we must have deg( T (φn(pk))) = m for some k. It
follows that r(pk) = 0 hence S(f ) = S0(f ) for any strictly H-stable polynomial f
18 J. BORCEA AND P. BR ¨AND ´EN
of degree n. Using again a standard density argument and Hurwitz’ theorem we
deduce that S preserves ( H-)stability up to degree n.
Suppose now that S(f ) = 0 for some strictly H-stable polynomial f of degree n
and let g ∈ Cn[z]. Clearly, f + ǫg is strictly H-stable for all ǫ > 0 small enough.
By the above we have that
S(g) = ǫ−1S(f + ǫg) = ( −cz + a)r(g)S0(g),
where S0(g) is H-stable or zero. It follows that V := S(Cn[z]) is a C-linear space
such that every non-zero polynomial in V is a ( −cz + a)r-multiple of an H-stable
polynomial. We know that r(pk) = 0 for the strictly H-stable polynomial pk above.
Assume that h ∈ Cn[z] is such that r(h) ⁄= 0. Since r(pk) = 0 and
S(h) + δS(pk) = S(h + δpk) = ( −cz + a)r(h+δpk)S0(h + δpk) ∈ V,
where S0(h + δpk) is H-stable or zero, we conclude that S(h) + δS(pk) is H-stable
or zero for all δ ⁄= 0. Letting δ → 0 we have by Hurwitz’ theorem that either
S(h) = 0 or S(h) is H-stable. However, this contradicts the fact that a/c ∈ H and
S(h)(a/c) = 0, which follows from the assumption that r(h) ⁄= 0. Hence all non-zero
polynomials in V are H-stable and thus we deduce that S preserves ( H-)stability
up to degree n in this case as well.
(ii) ⇒ (i). Since the set of H-stable polynomials of degree n is dense in the set
of H-stable polynomials of degree at most n it follows that S preserves H-stability
on the latter set (i.e., S preserves H-stability up to degree n). Let f be a C-stable
polynomial of degree n. Then φ−1
n (f ) is H-stable. Hence so is S(φ−1
n (f )) and thus
T (f ) = φm
(
S(φ−1
n (f ))
)
is a C-stable polynomial (note that −d/c ∈ ∂C ).
The equivalence (iv) ⇔ (v) follows just as above by replacing “strictly H-stable”
with “strictly hyperbolic”, that is, real- and simple-rooted. □
Notation 7. Given a polynomial f ∈ C[z, w] of degree at most m in z and at most
n in w and a M¨ obius transformation Φ as in (2.2) we let
φm,z(f )(z, w) = ( cz + d)mf (Φ( z), w), φ n,w(f )(z, w) = ( cw + d)nf (z, Φ( w)).
Lemma 7. Let f (z, w) ∈ C[z, w] be of degree at most m in z and at most n in w
and let Φ : C → H be a M¨ obius transformation as in (2.2). If either
(a) C is not the exterior of a disk, or
(b) C is the exterior of a disk and
(b1) the degree in z of φm,z(f )(z, w) is m, and
(b2) the degree in w of φn,wφm,z(f )(z, w) is n,
then f is H-stable if and only if φn,wφm,z(f ) is C-stable.
Proof. The equivalence is clear when C is a disk or a half-plane since in these cases
−cz + a is H-stable and cz + d is C-stable (cf. (2.3)). Hence we may assume that
C is the exterior of a disk. Note that if g(z) is a polynomial of degree k then a/c
is not a zero of φ−1
k (g)(z). In particular, if g(z) is a C-stable polynomial of degree
k then φ−1
k (g)(z) is an H-stable polynomial of degree k. Now since −d/c ∈ ∂C we
have that cz + d is C-stable and therefore φn,wφm,z(f ) is C-stable if f is H-stable,
which proves one of the implications.
Conversely, suppose that G(z, w) := φn,wφm,z(f )(z, w) = ∑ n
k=0 Qk(z)wk is C-
stable. Then so is λ−nG(z, ζ + λ(w − ζ)) whenever λ ≥ 1, where ζ is the center of
C′. Letting λ → ∞ we see by Hurwitz’ theorem that ( w − ζ)nQn(z) is C-stable.
P ´OLYA-SCHUR MASTER THEOREMS 19
Hence, so is Qn(z). For every z0 ∈ C the degree of G(z0, w) is n, from which it
follows that φ−1
n,w(G)(z, w) = φm,z(f )(z, w) ⁄= 0 whenever z ∈ C, w ∈ H. Similarly,
if φm,z(f )(z, w) = ∑ m
k=0 Pk(w)zk then Pm(w) is H-stable so that φm,z(f )(z, w0)
has degree m for every w0 ∈ H. We conclude that f (z, w) = φ−1
m,zφ−1
n,w(G)(z, w) is
H-stable, as claimed. □
The following lemma is a simple consequence of Hurwitz’ theorem since b ound-
edness prevents zeros from escaping to inﬁnity.
Lemma 8. Let Ω 1 be a path-connected subset of C and let Ω 2 be a bounded subset of
C. If T : Cn[z] → C[z] is a linear operator such that T : πn(Ω 1)\πn−1(Ω 1) → π(Ω 2)
then all polynomials in the image of πn(Ω 1) \ πn−1(Ω 1) have the same degree.
Note that in the hypothesis of Lemma 8 we do not allow the identically ze ro
polynomial to be in the image of πn(Ω 1) \ πn−1(Ω 1).
Proof of Theorem 7. Suppose that T : Cn[z] → Cm[z], where as before m is min-
imal in the sense that m = max {deg T (f ) : f ∈ Cn[z]}. By combining Lemma 6
with Hurwitz’ theorem we see that T : πn(C′) \ πn−1(C′) → π(C′) ∪ {0} if and
only if φ−1
m T φn : πn(H ′) → π(H ′) ∪ {0}. The case dim C T (Cn[z]) ≤ 1 is clear. If
dimC T (Cn[z]) > 1 then by Theorem 4 we have φ−1
m T φn : πn(H ′) → π(H ′) ∪ {0} if
and only if f (z, w) := φ−1
m T φn [(z + w)n] is H-stable. Now the polynomial in (b)
of Theorem 7 is precisely φn,wφm,z(f ). Moreover, by Lemma 7 (a) we may assume
that C is the exterior of a disk. Therefore, in order to complete the proof it only
remains to show that conditions (b1) and (b2) of Lemma 7 are satisﬁ ed.
If there were two diﬀerent C-stable polynomials of degree n that were mapped by
T on polynomials of diﬀerent degrees then by Lemma 8 there would be a C-stable
polynomial g of degree n in the kernel of T . However, since φ−1
n (g) is strictly H-
stable it would then follow from Lemmas 1 and 2 that φ−1
m T φn and hence also T has
range of dimension at most one, which is not the case. We infer that d eg T (h) = m
for any C-stable polynomial h of degree n.
Clearly, φm,z(f )(z, w) = T [φn,z
(
(z + w)n)
]. Let w0 ∈ H \ {−a/c}. The only zero
of the degree n polynomial
pw0(z) := φn,z
(
(z + w0)n)
=
(
(a + w0c)z + b + w0d
) n
is Φ −1(−w0) ∈ C
′
, so pw0(z) is C-stable. By the previous paragraph we then have
deg(φm,z(f )(z, w0)) = deg( T [pw0(z)]) = m,
which veriﬁes condition (b1) of Lemma 7.
Note next that coeﬃcient of wn in the polynomial deﬁned in (b) of Theorem 7
is T [(2acz + bc + ad)n]. We claim that the polynomial (2 acz + bc + ad)n is C-stable
and of degree n. Since the image of any C-stable polynomial of degree n is of degree
m this would verify condition (b2) of Lemma 7. To prove the claim note ﬁr st that
since C is the exterior of a disk we have that ac ⁄= 0 so deg(2 acz + bc + ad)n = n.
Let ζ = −b/a and η = −d/c. Since Φ( ζ) = 0 and Φ( η) = ∞ we have that ζ, η ∈ ∂C ,
which implies – again by the assumption that C is the exterior of a disk – that the
zero of (2 acz + bc + ad)n
− bc + ad
2ac = ζ + η
2 ,
is in C
′
. Thus (2 acz + bc + ad)n is C-stable and of degree n, as required. □
20 J. BORCEA AND P. BR ¨AND ´EN
Proof of Theorem 8. Let m = max {deg T (f ) : f ∈ Cn[z]}. By Lemma 6 we have
that T : πn(∂C ) → π(∂C ) ∪ { 0} if and only if φ−1
m T φn : πn(R) → π(R) ∪ { 0}.
Using this and Theorem 3 it is not diﬃcult to verify the theorem in the ca se
dimC T (Cn[z]) ≤ 2. Let f (z, w) = φ−1
m T φn[(z + w)n]. To settle the remaining cases
note ﬁrst that by Theorem 3 (c) and (d) we have that T : πn(∂C ) → π(∂C ) ∪ {0}
if and only if f (z, w) or f (z, −w) is a complex multiple of a real stable polynomial.
Now the condition that f (z, w) is a complex multiple of a real stable polynomial is
equivalent to saying that f (z, w) is both H-stable and H r-stable, see [3, Proposition
3] (note that H r = −H). By Theorem 7 we know that f (z, w) is H-stable if and
only if the polynomial in (c) of Theorem 8, that is, φn,wφm,z(f )(z, w), is C-stable.
On the other hand, since −cz + a is H r-stable and cz + d is Cr-stable (since Cr
is not the exterior of a disk) we also have that f (z, w) is H r-stable if and only if
φn,wφm,z(f ) is Cr-stable. The proof of the fact that condition (d) in Theorem 8 is
equivalent to saying that f (z, −w) is a complex multiple of a real stable polynomial
follows in similar fashion. This completes the proof of the theorem. □
Corollary 3 and Corollary 4 are immediate consequences of Theorem 7 and The-
orem 8, respectively.
