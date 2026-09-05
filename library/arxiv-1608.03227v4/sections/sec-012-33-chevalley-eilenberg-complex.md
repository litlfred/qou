---
doc_id: arxiv-1608.03227v4
doc_title: "January 30, 2018"
section_id: sec-012-33-chevalley-eilenberg-complex
section_title: "Chevalley-Eilenberg complex"
section_number: 3.3
pages: 14-15
source_pdf: 1608.03227v4.pdf
source_sha256: c71128e9a6c35343
doc_brief: "January 30, 2018 — For each braid β ∈ Brn we construct a 2-periodic complex Sβ of quasi-coherent C∗ × C∗ - equivariant sheaves on the non-commutative nested Hilbert scheme Hilb f ree 1,n ."
---
Suppose that h is a Lie algebra. Chevalley-Eilenberg complex CE h is the complex ( V•(h),d ) with Vp(h) =
U (h)⊗C Λ ph and diﬀerential dce =d1 +d2 where:
d1(u⊗x1∧···∧ xp) =
p∑
i=1
(−1)i+1uxi⊗x1∧···∧ ˆxi∧···∧ xp,
d2(u⊗x1∧···∧ xp) =
∑
i<j
(−1)i+ju⊗ [xi,x j]∧x1∧···∧ ˆxi∧···∧ ˆxj∧···∧ xp,
For h moduleV we deﬁne CE h(V ) := Hom U(h)(CEh,V ). The homology of this complex is called Chevalley-
Eilenberg cohomology of V : H ∗
Lie(h,V ). Consider a group H such that Lie(H) = h,Z is an aﬃne variety with
H-action and H-invariant function F . Suppose we are given F∈ MFh(Z,F ), that is, we have a Z2-graded
C[Z] module M with diﬀerential D such that D2 = F· Id and D(h·m) = h·D(m) for any h∈ H. The
complex Hom U(h)(CEh,M ) is a Z× Z2-graded module and we collapse the ﬁrst Z-grading to Z2-grading.
The map D +dce respects Z2-grading and the direct computation shows that D and dce anti-commute.
Hence (D +dce)2 =F and we deﬁne CE h(F ) := (Hom Uh(CEh,M ),D +dce). The diﬀerential dce commutes
with the elements of the ring invariants C[Z]h, thus the complex CE h(F )∈ MF(Z/H,F ) where Z/H =
Spec(C[Z]h).
14
Later on we will need an analog for the lemma 2.1 in the case of equivaria nt matrix factorizations. Our
proof the lemma 2.1 relies on the fact that every map from Hom <0(C+,C +) is homotopically trivial and
hence we can construct a homotopy that connects this map to 0. I t appears to us that the analog of this
statement does not hold in the equivariant setting: the homotopy c onnecting the map to 0 in general is
equivariant up to homotopy.
Thus to make our proof of lemma 2.1 work in equivariant setting one wo uld have to enlarge our category
of equivariant complexes to the category of L∞-complexes. That would make our theory extremely technical
and we postpone this development for subsequent publications. Be low we explain more elementary way to
get around this problem: we incorporate Eilenberg-Chevalley comple x in our deﬁnition of equivariant matrix
factorizations. We give details below and we start with some preliminar y material.
Let us deﬁne by ∆ the standard map h→ h⊗ h deﬁned by x↦→x⊗ 1 + 1⊗x. Suppose V and W
are modules over Lie algebra h then we use notation V⊗
∆
W for h-module which is isomorphic to V ⊗W
as vector space, the h-module structure being deﬁned by ∆. Respectively, for a given h-equivariant matrix
factorizationF = (M,D ) we denote by CE h⊗
∆
F the h-equivariant matrix factorization ( CEh⊗
∆
F,D +dce).
The h-equivariant structure on CE h⊗
∆
F originates from the left action of U (h) that commutes with right
action on U (h) used in the construction of CE h.
In more details, for a given h-moduleM the complex CE h⊗
∆
M has terms U (h)⊗ Λ i(h)⊗M with h-module
structure
x· (u⊗ω⊗m) = x·u⊗ω⊗m,
and the diﬀerential of the complex is dce =d1 +d2 where:
d1(u⊗x1∧···∧ xp⊗m) =
p∑
i=1
(−1)i+1 (uxi⊗mx1∧···∧ ˆxi∧···∧ xp⊗m+
x1∧···∧ ˆxi∧···∧ xp⊗xi·m),
d2(u⊗x1∧···∧ xp) =
∑
i<j
(−1)i+ju⊗ [xi,x j]∧x1∧···∧ ˆxi∧···∧ ˆxj∧···∧ xp.
A slight modiﬁcation of the standard fact that CE h is the resolution of the trivial module implies that
CEh⊗
∆
M is a free resolution of the h-module M .
