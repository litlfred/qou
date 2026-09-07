---
doc_id: arxiv-2305.07425v1
doc_title: "LARGEST HYPERBOLIC ACTIONS OF 3–MANIFOLD GROUPS"
section_id: sec-010-43-theorem-11
section_title: "Theorem 1.1"
section_number: 4.3
pages: 16-18
source_pdf: 2305.07425v1.pdf
source_sha256: 2f7d2ac5818b6af4
doc_brief: "LARGEST HYPERBOLIC ACTIONS OF 3–MANIFOLD GROUPS — The set of equivalence classes of cobounded actions of a grou p G on diﬀerent hyperbolic metric spaces carries a natural partial order."
---
whose statement we recall for the convenience of the reader.
Theorem 1.1. LetM be a non-geometric 3-manifold with empty or toroidal bounda ry. If the
torus decomposition of M contains any of the following, then π1(M ) is H–inaccessible:
(1) a hyperbolic piece which contains a boundary torus of M ;
(2) two hyperbolic pieces glued along a torus;
(3) an isolated non-elementary Seifert ﬁbered piece; or
(4) a non-elementary maximal graph manifold component.
LARGEST HYPERBOLIC ACTIONS OF 3–MANIFOLD GROUPS 17
Proof. LetM1,...,M k be the maximal graph manifold components and isolated Seife rt ﬁbered
pieces of the torus decomposition of M . Let S1,...,S ℓ be the tori in the boundary of M that
bound a hyperbolic piece, and let T1,...,T m be the tori in the torus decomposition of M that
separate two hyperbolic components of the torus decomposit ion. By Lemma 4.2, π1(M ) is
hyperbolic relative to
P = {π1(Mp)}k
p=1 ∪ {π1(Sq)}ℓ
q=1 ∪ {π1(Tr)}m
r=1.
In all of the cases (1)–(4), the collection P is non-empty.
In case (1), the collection {S1,...,S ℓ} ⁄= ∅, while in case (2), {T1,...,T m} ⁄= ∅. Both of
these collections consist of tori. Note that Z2 is H–inaccessible: the projections of Z2 onto
each factor yield two actions on lines to which Lemma 2.3 appl ies. Thus, if {π1(Sq)}∪{π1(Tr)}
is nonempty, then π1(M ) is H–inaccessible by Lemma 4.3, proving the theorem in cases (1)
and (2).
Next suppose that (3) holds, so that there is an isolated non- elementary Seifert ﬁbered piece
Mp. By the proof of Corollary 4.6 we see that π1(Mp) has two actions to which Lemma 2.3
applies. By Lemma 4.3, π1(M ) is H–inaccessible.
Finally, suppose that (4) holds, so that there is a non-eleme ntary maximal graph manifold
component Mp. By the proof of Proposition 4.8, there are two commuting ele ments a,b ∈
π1(Mp) and two actions on hyperbolic spaces (in fact, quasi-trees )π1(Mp) ↷ X andπ1(Mp) ↷
Y such that a and b are elliptic and loxodromic, respectively, in π1(Mp) ↷ X and a is
loxodromic inπ1(Mp) ↷ Y . Applying Lemma 4.3 to P =π1(Mp), we conclude that H(π1(M ))
contains no largest element. □
4.4. H–accessibility of ﬁnitely generated 3-manifold groups. In this section, we ex-
plain how one might reduce the study of H–accessibility of all ﬁnitely generated 3–manifold
groups to the case of compact, orientable, irreducible, ∂–irreducible 3–manifold groups. In
particular, we show that for any hyperbolic 3-manifold M without rank-1 cusps, if π1(M ) is
ﬁnitely generated then it is H-accessible.
Let M be an orientable 3-manifold with ﬁnitely generated fundame ntal group. It follows
from Scott’s Core Theorem that M contains a compact codimension zero submanifold whose
inclusion map is a homotopy equivalence [Sco73], and thus al so an isomorphism on funda-
mental groups. We thus can assume our 3-manifolds are compac t.
The sphere-disk decomposition provides a decomposition of a compact, orientable 3-manifold
M into irreducible, ∂–irreducible pieces M1,...,M k. In particular, π1(M ) is a free product
π1(M1) ∗π1(M2) ∗ · · · ∗π1(Mk). Let Gi :=π1(Mi). Note that π1(M ) is hyperbolic relative to
the collection P = {G1,...,G k}. In light of Lemma 4.3, the H–inaccessibility ofπ1(M ) follows
whenever some Gi satisﬁes the conditions of Lemma 2.3. Hence, it suﬃces to inv estigate the
H–accessibility of the groups Gi.
If M has empty or toroidal boundary, then H–accessibility of π1(M ) is understood, ex-
cept for a few sporadic cases, by Theorem 1.1. The following p roposition addresses certain
manifolds with higher genus boundary.
Proposition 4.10. Let M be a compact, orientable, irreducible, ∂–irreducible 3-manifold
which has at least one boundary component of genus at least 2. Then π1(M ) is H–inaccessible
under either of the following hypotheses:
(1) M has trivial torus decomposition and at least one torus bound ary component; or
(2) M has non-trivial torus decomposition.
On the other hand, if M has trivial torus decomposition and all boundary component s have
genus at least 2, then π1(M ) is H–accessible.
LARGEST HYPERBOLIC ACTIONS OF 3–MANIFOLD GROUPS 18
Proof. As in [Sun20, Section 6.3], we can paste compact hyperbolic 3 -manifolds with totally
geodesic boundaries to the higher genus boundary component s of M to obtain a ﬁnite volume
hyperbolic manifold N (in case M has trivial torus decomposition) or a mixed 3-manifold (in
case M has non-trivial torus decomposition).
If (1) holds, then the manifold N has toroidal boundary, and, by assumption, there is a
boundary torus T for N which is also a boundary torus of M .
The subgroup P := π1(T ) ≃ Z2 satisﬁes Lemma 2.3 and is a peripheral subgroup in the
relatively hyperbolic structure on π1(N ). The proof of Lemma 4.3 shows that there are
commuting elements a,b ∈ P and hyperbolic actions π1(N ) ↷ ZX and π1(N ) ↷ ZY such
thata and b act loxodromically and elliptically, respectively, in the action π1(N ) ↷ ZX , and
b acts loxodromically in the action G ↷ ZY . As π1(M ) is a subgroup of π1(N ), we obtain
induced actions π1(M ) ↷ ZX and π1(M ) ↷ ZY . Since a,b ∈ π1(M ), we see that π1(M ) is
H–inaccessible by Lemma 2.3.
If (2) holds, then N has either empty or toroidal boundary and has the following p roperties:
(i) M is a submanifold of N with incompressible toroidal boundary;
(ii) cutting N along the tori in the torus decomposition of M yields the torus decomposition
of N ; and
(iii) each piece of M with a boundary component of genus at least 2 is contained in a hyper-
bolic piece of N .
In particular, it follows from (ii) and (iii) that N is a mixed 3-manifold, and hence π1(N ) is
H–inaccessible by Theorem 1.1.
In the proof of Theorem 1.1, we prove the H–inaccessibility of π1(N ) by showing there are
two commuting elements a,b ∈π1(T ) for some torus T in the torus decomposition of N and
isometric actions π1(N ) ↷ ZX and π1(N ) ↷ ZY on hyperbolic spaces, and then applying
Lemma 2.3.
By (ii), T is also a torus in the torus decomposition of M . Thus the induced actions
π1(M ) ↷ ZX and π1(M ) ↷ ZY satisfy the hypotheses of Lemma 2.3, and so π1(M ) is
H–inaccessible.
We now turn our attention to the ﬁnal statement of the theorem . In this case, the manifold
N is closed. A ﬁnitely generated subgroup H ofN is a virtual surface ﬁber subgroup ifN admits
a ﬁnite cover N ′ →N such thatH is a subgroup of π1(N ′) andH is a surface ﬁber subgroup of
π1(N ′). Any ﬁnitely generated subgroup H of π1(N ) is either a geometrically ﬁnite Kleinian
group or a virtual surface ﬁber subgroup in π1(N ) by the Covering Theorem (see [Can96])
and the Subgroup Tameness Theorem (see [Agol04, CG06] or [AF W15, Theorem 4.1.2] for a
statement). In particular, π1(M ) is either a virtual surface ﬁber subgroup, in which case it i s
hyperbolic, or it is geometrically ﬁnite in π1(N ). In the latter case, π1(M ) is undistorted
in π1(N ) [Hru10, Corollary 1.6], and we again conclude that π1(M ) is hyperbolic, since
undistorted subgroups of hyperbolic groups are hyperbolic . As a result, in either case, π1(M )
is H–accessible. □
