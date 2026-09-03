---
doc_id: arxiv-1712.08953v1
doc_title: "REPRESENTATIONS OF THE ORIENTED SKEIN CATEGORY"
section_id: sec-023-20-j-brundan
section_title: "J. BRUNDAN"
section_number: 20
pages: 20-21
source_pdf: 1712.08953v1.pdf
source_sha256: 005e0b1ad63c173e
doc_brief: "REPRESENTATIONS OF THE ORIENTED SKEIN CATEGORY — The oriented skein category OS(z, t ) is a ribbon category which un- derpins the deﬁnition of the HOMFLY-PT invariant of an orien ted link, in the"
---
the deﬁnition ofOS (z,t ) that ır, hence, ˜ır is surjective. We deduce that the right hand
˜Ψ is an isomorphism, hence, the left hand one is too. This shows that I is indeed the
kernel of Ψ. □
Remark 3.3. Let notation be as in Theorem 1.3, taking ε = +. If a, b∈⟨↑,↓⟩ are
objects such that x (resp. x′) letters of a and y (resp. y′) letters of b are equal to ↓
(resp.↑), and r :=x′ +y =x+y′ satisﬁesr≤n, then Ψ is injective on Hom OS (z,t)(a, b)
and
dimk HomOS(z,t)(a, b) = dimHr =r!. (3.14)
These assertions follow from the proof just explained: when r≤ n the map r is an
isomorphism so all of the vertical maps in (3.13) are isomorphisms too . (Theorem 1.2
implies that the formula (3.14) holds without the restriction r≤n, but we will use this
special case in its proof.)
Proof of Theorem 1.2. In this proof, we are going to allow k to vary, so may add an ad-
ditional subscript, denoting OS (z,t ) and ˆOS (z,t ) instead by OS (z,t )k andˆOS (z,t )k ,
respectively. We ﬁrst establish the result for the morphism spaces of OS . Take
a, b∈⟨↑,↓⟩ such that x (resp. x′) letters of a and y (resp. y′) letters of b are equal
to↓ (resp. ↑), and r := x′ +y = x +y′. Let B(a, b) be some set of reduced lifts of
the ( a, b)-matchings, so that |B(a, b)| = r!. It is straightforward to see for any k ,z
and t that B(a, b) spans Hom OS (z,t)k (a, b). We need to show that it is also linearly
independent.
Consider ﬁrst the case that k = Z[z,z−1,t,t−1]. Take a linear relation
∑
b∈B(a,b)
cb(z,t )b = 0
for cb(z,t )∈ Z[z,z−1,t,t−1]. For any n≥ r, we can consider the obvious strict Z-
linear monoidal functor ω :OS (z,t )Z[z,z −1,t,t−1]→OS (q−q−1,qn)Q(q) sending z↦→
q−q−1,t↦→qn, and generating morphisms to the generating morphisms with the sa me
names. This functor maps B(a, b) to a spanning set for Hom OS (q−q−1,qn)Q(q) (a, b).
Since|B(a, b)| =r!, we deduce from (3.14) that ω(B(a, b)) is linearly independent too.
Hence, cb(q−q−1,qn) = 0 for each b∈ B(a, b). Since this is true for inﬁnitely many
values of n, it follows that each cb(z,t ) = 0.
Now take an arbitrary commutative ground ring k and parameters ¯z, ¯t∈ k ×. View-
ing k as a Z[z,z−1,t,t−1]-module so z and t act via ¯z and ¯t, there is an obvious strict
k -linear monoidal functorOS(¯z, ¯t)k →OS (z,t )Z[z,z −1,t,t−1]⊗Z[z,z −1,t,t−1] k sending gen-
erating morphisms to the generating morphisms with the same name t ensored with 1 k .
This functor sends B(a, b) to a set of morphisms which we already know is linearly inde-
pendent thanks to the previous paragraph. Hence B(a, b) itself is linearly independent.
This completes the proof for OS.
It remains to treat the extended category ˆOS . Again, it is clear that the morphisms
from the statement of Theorem 1.2 span, so we just need to estab lish linear indepen-
dence. For all but the case a = b = ∅ , this follows immediately since we have already
established linear independence in the quotient category OS(z,t )k . Thus, we are left
with showing that 1 ∅ and are linearly independent in Hom ˆOS(z,t)k
(∅, ∅ ). By the
same arguments as in the previous two paragraphs, this follows if we can check it in
HomˆOS(q−q−1,qn)Q(q)
(∅, ∅ ) for inﬁnitely many values of n. This is done in the ﬁnal
paragraph of the proof.
So assume that k = Q(q), z = q−q−1 and t = qn for n∈ N. We deﬁne a new
strict k -linear monoidal category C. Its objects are as in OS (z,t ) with the same tensor
ORIENTED SKEIN CATEGORY 21
product, and its morphisms are deﬁned from
HomC(a, b) :=
{ HomOS(z,t)(a, b) if a⁄= ∅ or b⁄= ∅ ,
HomOS(z,t)(∅, ∅ )⊕ k if a = b = ∅ .
So HomC(∅, ∅ ) is two-dimensional with basis (1 ∅, 0) and (0, 1k ). Horizontal and ver-
tical composition of most of the morphisms in C is induced by the compositions in
OS (z,t ) in the obvious way; the horizontal and vertical composition of (0 , 1k ) with
any morphism in Hom C(a, b) is zero if a⁄= ∅ or b⁄= ∅ ; the horizontal and vertical
composition of (0, 1k ) with (a1∅,b 1k ) is (0,b 1k ). Now the point is that there is a strict
k -linear monoidal functor ˆOS (z,t )→ Csending objects and generating morphisms
to their images under the quotient functor to OS (z,t ) embedded (non-unitally) into
