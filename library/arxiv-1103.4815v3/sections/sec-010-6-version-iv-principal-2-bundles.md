---
doc_id: arxiv-1103.4815v3
doc_title: "Four Equivalent Versions of Non-Abelian Gerbes"
section_id: sec-010-6-version-iv-principal-2-bundles
section_title: "Version IV: Principal 2-Bundles"
section_number: 6
pages: 33-36
source_pdf: 1103.4815v3.pdf
source_sha256: 28647b02ea1441e3
doc_brief: "Four Equivalent Versions of Non-Abelian Gerbes — We recall and partially improve four versions of smooth, non -abelian gerbes: ˇCech cocycles, classifying maps, bundle gerbes, and principal"
---
The basic idea of a smooth 2-bundle is that it gives for every point x in the base manifold M a
Lie groupoid Px varying smoothly with x. Numerous diﬀerent versions have appeared so far in the
literature, e.g [Bar04, BS07, Woc11, SP11]. The main objective of our version of principal 2-bundles
is to make the deﬁnition of the objects (i.e. the 2-bundles) as simple as possible , while keeping
their isomorphism classes in bijection with non-abelian cohomology. Th us, our principal 2-bundles
will be deﬁned using strict actions of Lie 2-groups on Lie groupoids, and not using anafunctors.
The necessary “weakness” will be pushed into the deﬁnition of 1-mo rphisms.
6.1 Deﬁnition of Principal 2-Bundles
As an important prerequisite for principal 2-bundles we have to disc uss actions of Lie 2-groups on
Lie groupoids, and equivariant anafunctors.
Deﬁnition 6.1.1. Let P be a Lie groupoid, and let Γ be a Lie 2-group. A smooth right action of Γ
on P is a smooth functor R : P × Γ /d47/d47 P such that R(p, 1) = p and R(ρ, id1) = ρ for all p ∈ P 0
and ρ ∈ P 1, and such that the diagram
P × Γ × Γ
id ×m /d47/d47
R ×id
/d15/d15
P × Γ
R
/d15/d15
P × Γ m
/d47/d47 P
of smooth functors is commutative (strictly, on the nose).
For example, every Lie 2-group acts on itself via multiplication. Note t hat due to strict com-
mutativity, one has R(R(p,g ),g −1) = p andR(R(ρ,γ ),i (γ)) = ρ for all g ∈ Γ 0,p ∈ P 0,γ ∈ Γ 1 and
ρ ∈ P 1.
Remark 6.1.2. This deﬁnition could be weakened in two steps. First, one could allow a n atural
transformation in the above diagram instead of commutativity. Sec ondly, one could allow R to be
an anafunctor instead of an ordinary functor. It turns out that for our purposes the above deﬁnition
is suﬃcient.
– 33 –
Deﬁnition 6.1.3. Let X and Y be Lie groupoids with smooth actions (R1,ρ 1), (R2,ρ 2) of a Lie
2-group Γ . An equivariant structure on an anafunctor F : X /d47/d47 Y is a transformation
X × Γ
F ×id
/d15/d15
R1 /d47/d47 X
λ ③③③③③
③③③③③
/d120/d0 ③③③③③③③③ F
/d15/d15
Y × Γ R2
/d47/d47 Y
satisfying the following condition:
X × Γ × Γ
id ×m /d47/d47
R1 ×id
❑❑❑
/d37/d37❑❑
F ×id ×id
/d15/d15
X × Γ
R1
/d31/d31❃❃❃❃❃
X × Γ
λ ×idssssss
/d117/d125 ssss
R1 /d47/d47
F ×id
/d15/d15
X
λ
④④④④④④④
④④④④④④④
/d121/d1 ④④④④④
④④④④④ F
/d15/d15
Y × Γ × Γ
R2 ×id /d37/d37❑❑❑❑❑❑❑
Y × Γ R2
/d47/d47 Y
=
X × Γ × Γ
id ×m /d47/d47
F ×id ×id
/d15/d15
X × Γ
F ×id
/d15/d15
R1
/d31/d31❄❄❄❄❄
X
λ ⑧⑧⑧⑧⑧⑧
/d123/d3 ⑧⑧⑧⑧
F
/d15/d15
Y × Γ × Γ
R2 ×id /d37/d37❑❑❑❑❑❑❑ id ×m /d47/d47 Y × Γ
R2
❃❃
/d31/d31❃❃
Y × Γ R2
/d47/d47 Y
An anafunctor together with a Γ -equivariant structure is called Γ -equivariant anafunctor.
In Appendix A we translate this abstract (but evidently correct) d eﬁnition of equivariance into
more concrete terms involving a Γ 1-action on the total space of the anafunctor.
Deﬁnition 6.1.4. If (F,λ ) : X /d47/d47 Y and (G,γ ) : X /d47/d47 Y are Γ -equivariant anafunctors, a
transformationη :F /d43/d51 G is called Γ -equivariant, if the following equality of transformation holds:
X × Γ
G ×id
/d31/d31
F ×id
/d127/d127
η ×id/d107/d115
R1 /d47/d47 X
λ ssssssss
ssssssss
/d117/d125 ssssssss
F
/d15/d15
Y × Γ R2
/d47/d47 Y
=
X × Γ
G ×id
/d15/d15
R1 /d47/d47 X
γ ✉✉✉✉✉✉✉
✉✉✉✉✉✉✉
/d118/d126 ✉✉✉✉✉✉
✉✉✉✉✉✉ G
/d31/d31
F
/d95/d95
η/d107/d115
Y × Γ R2
/d47/d47 Y
It follows from abstract nonsense in the bicategory of Lie groupoid s, anafunctors and transfor-
mations that we have another bicategory with
• objects: Lie groupoids with smooth right Γ-actions.
• 1-morphisms: Γ-equivariant anafunctors.
• 2-morphisms: Γ-equivariant transformations.
– 34 –
We need three further notions for the deﬁnition of a principal 2-bu ndle. Let M be a smooth
manifold, and let P be a Lie groupoid. We say that a smooth functor π : P /d47/d47 Mdis is a surjective
submersion functor , if π : P0 /d47/d47 M is a surjective submersion. Let π : P /d47/d47 Mdis be a surjective
submersion functor, and let Q be a Lie groupoid with some smooth functor χ : Q /d47/d47 Mdis. Then,
the ﬁbre product P × M Q is deﬁned to be the full subcategory of P × Q over the submanifold
P0 ×M Q0 ⊂ P 0 × Q0.
Deﬁnition 6.1.5. LetM be a smooth manifold and let Γ be a Lie 2-group.
(a) A principal Γ -2-bundle over M is a Lie groupoid P, a surjective submersion functor π :
P /d47/d47 Mdis, and a smooth right action R of Γ on P that preserves π, such that the smooth
functor
τ := (pr 1,R ) : P × Γ /d47/d47 P ×M P
is a weak equivalence.
(b) A 1-morphism between principal Γ -2-bundles is a Γ -equivariant anafunctor
F : P1 /d47/d47 P2
that respects the surjective submersion functors to M .
(c) A 2-morphism between 1-morphisms is a Γ -equivariant transformation between these.
Remark 6.1.6.
(a) The condition in (a) that the action R preserves the surjective submersion functor π means
that the diagram of functors
P × Γ R /d47/d47
pr1
/d15/d15
P
π
/d15/d15
P π
/d47/d47Mdis
is commutative.
(b) The condition in (b) that the anafunctor F respects the surjective submersion functors means
in the ﬁrst place that there exists a transformation
P1
F /d47/d47
π 1
/d30/d30❂❂❂❂❂❂❂❂❂❂❂ P2
/d113/d121 ❦❦❦❦❦❦❦❦❦❦❦❦❦
❦❦❦❦❦❦❦❦❦❦❦❦❦
π 2
/d0/d0✁✁✁✁✁✁✁✁✁✁✁
Mdis.
– 35 –
However, since the target of the anafunctors π1 and π2 ◦F is the discrete groupoid Mdis, the
equivalence of Example 2.3.4 applies, and implies that if such a transfor mation exists, it is
unique. Indeed, it is easy to see that an anafunctor F : P /d47/d47 Q with anchors αl :F /d47/d47 P0
and αr :F /d47/d47 Q0 respects smooth functors π : P /d47/d47 Mdis and χ : Q /d47/d47 Mdis if and only
if π ◦αl =χ ◦αr.
Example 6.1.7. The trivial Γ -2-bundle overM is deﬁned by
P :=Mdis × Γ , π := pr 1 , R := idM ×m.
Here, the smooth functor τ even has a smooth inverse functor . In the following we denote the
trivial Γ-2-bundle by I.
Remark 6.1.8. The principal Γ-2-bundles of Deﬁnition 6.1.5 are very similar to those o f Bartels
[Bar04] and Wockel [Woc11], in the sense that their ﬁbres are group oids with a Γ-action. They only
diﬀer in the strictness assumptions for the action, and in the formu lation of principality. Opposed
to that, the principal 2-group bundles introduced in [GS] are quite diﬀerent: their ﬁbres are Lie
2-groupoids equipped with a certain Lie 2-groupoid morphism to BΓ.
