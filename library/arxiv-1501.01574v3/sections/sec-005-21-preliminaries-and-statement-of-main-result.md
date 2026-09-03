---
doc_id: arxiv-1501.01574v3
doc_title: "KNOT CABLING AND THE DEGREE OF THE COLORED JONES POLYNOMIAL"
section_id: sec-005-21-preliminaries-and-statement-of-main-result
section_title: "Preliminaries and statement of main result"
section_number: 2.1
pages: 4-6
source_pdf: 1501.01574v3.pdf
source_sha256: 8af5d6264a0ad5e0
doc_brief: "KNOT CABLING AND THE DEGREE OF THE COLORED JONES POLYNOMIAL — We study the behavior of the degree of the colored Jones polyn omial and the boundary slopes of knots under the operation of cabling."
---
solid torus in S3 and let V ′ ⊂ V a second standard solid torus that is concentric to V . On
∂V ′ we choose a pair of meridian and canonical longitude (which a lso determines such a
pair on ∂V ). For coprime integers p, q, let Tp,q ⊂ ∂V ′ be a simple closed curve of slope
p/q; that is a ( p, q)-torus knot.
Recall that for a knot K, n(K) denotes a neighborhood of K. Embed V in S3 by a
homeomorphism f : V − →n(K) that preserves the canonical longitudes. The ( p, q)-cable
of K is the image Kp,q := f (Tp,q ). The space Cp,q := f (V \ n(Tp,q )) is called a ( p, q)-
cable space. The complement of Kp,q , denoted by MKp,q, is obtained from the complement
of K by attaching Cp,q . The space Cp,q has two boundary components; the inner one
T− = f (∂n(Tp,q )) = ∂MKp,q and the outer one T+ = f (∂V ) = ∂MK .
Deﬁnition 2.1. For a knot K ⊂ S3, let ⟨µ, λ⟩ be the canonical meridian–longitude basis
of H1(∂n(K)). For a pair of integers (a, b), the ratio a/b ∈ Q ∪ {1/0} is called a boundary
slope of K if there is a properly embedded essential surface (S, ∂S) ⊂ (MK, ∂n(K)), such
that ∂S represents aµ + bλ ∈ H1(∂n(K)).
In Deﬁnition 2.1, a, b do not need to be coprime. In fact if d = gcd( a, b) then we have
a surface S as above with d boundary components. To stress this point sometimes we will
say that the total slope of ∂S is a/b. Recall that every knot K has ﬁnitely many boundary
slopes and that bsK denotes the set of boundary slopes of K. The rest of the section is
devoted to the proof of the following theorem.
5
Theorem 2.2. (a) Let K ⊂ S3 be a non-trivial knot and (p, q) coprime integers. If a/b
is a boundary slope of K, then q2a/b is a boundary slope of Kp,q .
(b) For every knot K ⊂ S3 and (p, q) coprime integers, we have
(
q2bsK ∪ {pq}
)
⊂ bsKp,q.
The reader is referred to [14, 16] for basic deﬁnitions and te rminology. Let ( p, q) be
coprime integers. The cable space Cp,q is a Seifert ﬁbered manifold over an annulus B,
with one singular ﬁber of multiplicity q. In Cp,q there is an essential annulus A, that is
vertical with respect to the ﬁbration, with ∂A ⊂ T− and with boundary slope equal to pq;
this annulus is the cabling annulus. There are two additional essential annuli in Cp,q . One
with both boundary components on T−, each with slope p/q. The other annulus A′ has
one component of ∂A′ on T− with slope pq, and the second component of ∂A′ on T+ with
slope p/q. See [13]. In particular, we have the following.
Lemma 2.3. For any cable knot Kp,q , s = pq is a boundary slope in MKp,q.
Recall that a properly embedded surface S in a 3-manifold M with boundary, is essential
if the map on π1 induced by inclusion is injective. If S is orientable this is equivalent to
saying that S is incompressible and ∂-incompressible in M . If S is non-orientable, then
S being essential is equivalent to saying that the surface ~S := ∂(S × I) is incompressible
and ∂-incompressible in M .
We need the following lemma, a proof of which is given, for exa mple, in [21, Proposition
1.1].
Lemma 2.4. Let M be a knot complement in S3 and let Σ be a properly embedded essential
surface in M . Suppose that a path α ⊂ Σ that has its endpoints on ∂Σ is homotopic relative
endpoints in M to a path in ∂M . Then α is homotopic relative endpoints in Σ to a path
in ∂Σ .
The complement MKp,q of the cable knot Kp,q is obtained by gluing Cp,q and the com-
plement of K along the torus T+. If K is a non-trivial knot, then the torus T+ is essential
in MKp,q; that is a companion of Kp,q .
We will use MKp,q\\T+ to denote the 3-manifold obtained by splitting MKp,q along T+.
Also given a properly embedded surface S in MKp,q we will use S\\T+ to denote the image
of S in MKp,q\\T+.
Lemma 2.5. Let K ⊂ S3 be a non-trivial knot and (p, q) coprime integers. Let S be a
properly embedded surface in MKp,q. Suppose that each component of S\\T+ is essential
in the component of MKp,q\\T+ it lies in. Then S is essential in MKp,q.
Proof. Since S may be non-orientable we will work with the orientable doubl e~S = ∂(S ×I).
By way of contradiction, suppose that ~S is not π1-injective. This means that ~S is either
compressible or ∂-compressible. Since ∂MKp,q consists of tori, incompressibility implies
∂-incompressibility [14]. Thus we may assume that there is a c ompression disk ( E, ∂E ) ⊂
(MKp,q,~S). Since each component of ~S\\T+ is incompressible, the intersection E ∩ T+
must be non-empty. Since T+ is essential (and thus incompressible in MKp,q) we may
eliminate the closed components of E ∩ T+. Thus we may assume that each component
6
of E ∩ T+ is an arc properly embedded in E. By further isotopy of E, during which ∂E
moves on ~S, we may assume that the intersection E ∩ T+ is minimal. Now let α be a
component of E ∩ T+ that is outermost on E: It cuts oﬀ a disc E′ ⊂ E whose interior
contains no further intersections with T+. Now ∂E ′ consists of α and an arc β that is
properly embedded on a component, say Σ, of ~S\\T+. We can use disk E′ to isotope β,
relatively ∂β , on T+; this isotopy takes place in MKp,q\\T+. Since Σ is essential in the
component of MKp,q\\T+ it lies in, we conclude that the arc β may be isotopied on Σ,
relatively ∂β , to an arc on ∂Σ. This follows from Lemma 2.4. But this isotopy will reduce
the components of the intersection E ∩ T+, contradicting our assumption of minimality.
Thus ~S must be incompressible and therefore, by above discussion, essential in MKp,q. □
