---
doc_id: ant-v14-n7-s
doc_title: "Algebra & Number Theory Volume 14 No. 7 msp"
section_id: sec-101-8b-algebraic-k-theory
section_title: "8B. Algebraic K-theory"
section_number: null
pages: 171-173
source_pdf: ant-v14-n7-s.pdf
source_sha256: ab695eddd565addf
---
Algebraic K-theory on SmB is represented by the motivic commutative ring spectrum KGL∈ SH(B); see
[V oevodsky 1998, §6.2]. Just as for HZ, the purity theorem
KGLa,b
Z (X)≃ KGLa−2c,b−c(Z)
for i: Z→ X a closed immersion of codimension d in SmB (a consequence of Quillen’s localization
sequence for algebraic K-theory [1973, §7, Proposition 3.2]) gives Thom class ϑKGL(V)∈ KGL2r,r
0V (V)
for V→ X a rank r vector bundle over X∈ SmB, and makes KGL a GL-oriented motivic spectrum.
Explicitly, KGL represents Quillen K-theory on SmB via KGLa,b≃ K2b−a and the Thom class for a
rank r vector bundle p: V→ X is represented by the Koszul complex KosV(p∗V∨, can). Here
can: p∗V∨→ OV
is the dual of the tautological section OV→ p∗V and KosV(p∗V∨, can) is the complex whose terms are
given by
KosV(p∗V∨, can)−r=3r p∗V∨
1838 Marc Levine and Arpon Raksit
and whose differential3r p∗V∨→3r−1 p∗V∨ is given with respect to a local framing of V∨ by
d(ei1∧···∧ eir)=
r∑
j=1
(−1) j−1can(ei j)· ei1∧···∧ ˆei j∧···∧ eir.
This complex is a locally free resolution ofs∗(OX), where s: X→ V is the zero-section. Thus, by the identi-
ﬁcation of KGL2r,r
0V (V) with the Grothendieck group of the triangulated category of perfect complexes onV
with support contained in 0V , KosV(p∗V∨, can) gives rise to a class[KosV(p∗V∨, can)]∈ KGL2r,r
0V (V)
which maps to 1X under the purity isomorphism KGL2r,r
0V (V)≃ KGL0,0(X), so that we indeed have
[KosV(p∗V∨, can)]= ϑKGL(V).
Just as for motivic cohomology, one has explicit pushforward maps in K-theory given by Quillen’s
localization and devissage theorems identifying, forX∈ SmB and Z⊆ X a closed subscheme, the K-theory
with support KZ(X) with the K-theory of the abelian category of coherent sheaves CohZ on Z, denoted
G(Z). For a projective morphism f: Y→ X, one has the pushforward map ˆf∗: G(Y)→ G(X) deﬁned
by using a suitable subcategory of Coh Y on which f∗ is exact. On K 0, this recovers the usual formula
ˆf∗([F])=
dim Y∑
j=0
(−1) j[R j f∗(F)]
for F∈ CohY . Via the isomorphisms KGLa,b
Z (X)≃ G2b−a(Z), this gives pushforward maps ˆf∗ for
KGL∗,∗, deﬁning a GL-oriented cohomology theory on Sm B.
For s: X→ V the zero-section of a vector bundle,ˆs∗ agrees with the pushforward s∗ using the Thom
isomorphism/localization theorem, hence by our comparison theorem (again really the theorem of Panin
and Smirnov), we have ˆf∗= f∗ for all projective f.
Theorem 8.3. LetπX: X→ B be a smooth projective morphism with B a regular separated scheme of
ﬁnite Krull dimension. Then
uKGL(χ( X/B))=
dimB X∑
j=0
dimB X∑
i=0
(−1)i+ j[R jπX∗i
X/B]∈ K0(B)= KGL0,0(B).
Proof. Let p: TX/B→ X denote the relative tangent bundle and let s: X→ TX/B denote the zero-section.
We have
eKGL(TX/B)= s∗(th(TX/B))= s∗(KosTX/B(p∗T∨
X/B, can)).
Since T∨
X/B=X/B, and s∗(can) is the zero-map, it follows that, in K 0(X),
s∗(KosTX/B(p∗T∨
X/B, can))=
dimB X∑
i=0
(−1)i[i
X/B],
and thus
πX∗(eKGL(TX/B))=
dimB X∑
j=0
dimB X∑
i=0
(−1)i+ j[R jπX∗i
X/B].
Motivic Gauss–Bonnet formulas 1839
We conclude by applying the motivic Gauss–Bonnet theorem. □
