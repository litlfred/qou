---
doc_id: arxiv-1608.07308v1
doc_title: "FLAG HILBERT SCHEMES, COLORED PROJECTORS AND KHOV ANOV-ROZANSKY HOMOLOGY"
section_id: sec-040-55-sheaves-for-two-strand-braids
section_title: "Sheaves for two-strand braids"
section_number: 5.5
pages: 47-49
source_pdf: 1608.07308v1.pdf
source_sha256: bcc3b6f1a91a55c6
doc_brief: "FLAG HILBERT SCHEMES, COLORED PROJECTORS AND KHOV ANOV-ROZANSKY HOMOLOGY — We construct a categoriﬁcation of the maximal commutative subalgebra of the type A Hecke algebra."
---
one needs to consider the moduleHom(1,M⊗FT
•
) over the graded algebraA = Hom(1, FT
•
).
In the previous subsection, we have studied the caseM = FT
k
for positive integersk, and we
found thatι∗(M) =O(k). The computation for negativek is more interesting:
FT
−k∼=

t−kR→q− 1
2t
1
2−kB→q− 1
2t1−kB→q−1t
3
2−kB→···→ q
1
2−kt− 1
2B→q
1
2−kB| {z }
2k


for anyk≥ 0, where the maps alternate between x⊗1+1⊗x
2 and x⊗1−1⊗x
2 . Therefore, we have:
Hom(1, FT
−k
)∼=

t−kR
1
− →t
1
2−kR
0
− →t1−kR
x
− →q−1t
3
2−kR
0
− →...
x
− →q1−kt− 1
2R
0
− →q1−kR| {z }
2k


(5.20) =⇒ Hom(1, FT
−k
)∼=t
1
2H1(
FHilb2,O(−k)
)
according to (5.9). The case of general a follows by analogy with the previous subsection, so
we conclude the following formula that extends (5.16) to negative integers:
(5.21) RHom•
SBim2(1, FT
−k
)∼=RΓ
(
FHilb2,O(−k)⊗∧•O(−1)
)
Remark 5.3. Let us observe the fact that the derived functors in the two sides of the above
equation are very different. In the left hand side, we have the derived Hochschild homology
functor, whose degree is measured by a. In the right hand side, we have derived direct image
of sheaves, whose degree is measured byt
1
2 , and thea grading comes from∧•O(−1).
To complete the discussion for n = 2 , let us compute B(σ) := ι∗(σ) where σ denotes a
single positive crossing. Together with the projection formula (4.5), this implies that:
B(σ2k+1) :=ι∗(σ2k+1) =ι∗(σ⊗ FT
k
) =ι∗(σ)⊗O (k) =B(σ)⊗O (k)
for all integersk. In fact, we have:
Hom(1,σ 2k+1)∼=

qk+ 1
2R
x
− →···
0
− →q2tk−1R
x
− →qtk− 1
2R
0
− →qtkR| {z }
2k+1
x
− →tk+ 1
2R


and therefore:
⨁
k≥0
Hom(1,σ⊗ FTk) =
⨁
k≥0
Hom(1,σ 2k+1) =t1/2 C[x,z,w ]
x
48 EUGENE GORSKY, ANDREI NEGUT , , AND JACOB RASMUSSEN
where recall that z and w are the maps of (5.12). We conclude that B(σ) is the structure
sheaf of the subscheme {x = 0}⊂ FHilb2, which is nothing but the connected component
Z2 = FHilb2(point)∼= P1 of (5.6). The periodic resolution (3.49) takes the form:
B(σ)∼=OP1
q.i.s.
∼=
[
...
w
−→q2tO(−1)
x
→qtO(−1)
w
−→qO(−1)
x
→O
]
whereO denotes the structure sheaf of FHilb2. In the non-reduced category, one needs to
replacex byx1−x2 everywhere. Finally, let us computeι∗(B), where recall thatB =R⊗RsR.
Sincez⊗ IdB is an isomorphism betweenB and FT2⊗B, we have:
⨁
k≥0
Hom(1,B· FTk) =
⨁
k≥0
zk Hom(1,B ) = C[x1,x 2,z ].
Thereforeι∗(B) is the structure sheaf of the irreducible componentZ1⊂ FHilb2 cut out by the
equationw = 0 (see (5.5)), which is isomorphic to C2 with coordinatesx1 andx2.
6. E XAMPLE : THE CASE OF THREE STRANDS
6.1. The geometry ofFHilb3. We will now study the varietyFHilb3 = FHilb3(C) and formu-
late a precise conjecture about the sheafι∗(ﬁgure eight knot). Recall the matrix presentation:
FHilb3 =


X =


x1 0 0
a x 2 0
α1 α2 x3

, Y =


0 0 0
b 0 0
β1 β2 0

, [X,Y ] = 0,
(6.1) v =


1
0
0

 cyclic



/
conjugation byg =


1 0 0
0 c 0
0 t d


Note that in the presentation above, we ﬁxed the vectorv (and this ﬁxes the ﬁrst column of the
conjugating matrix) to eliminate certain coordinates. Note that the map FHilb3→ FHilb2 is
given by only retaining the top 2× 2 corners of the matrices in question. If one is given the
eigenvaluesx1,x 2,x 3 and the point [a :b]∈ P1, then the datum one needs to construct a point
in FHilb3 is the vector:
(6.2) (α1,α 2,β 1,β 2)∈T ∨
2 ⊕T ∨
2
To ensure that the equation [X,Y ] = 0 is satisﬁed, we need to ensure that:
(x1−x3)β1 =α2b−β2a and (x2−x3)β2 = 0
Moreover, the fact that we quotient out by conjugation matrices implies that we must identify:
(α1,α 2,β 1,β 2)∼ (α1+ta,α 2+t(x2−x3),β 1+tb,β 2) and (α1,α 2,β 1,β 2)∼d(α1,α 2,β 1,β 2)
for t∈ C and d∈ C∗. Unwinding these facts, one sees that the datum (6.2) corresponds
to a vector in H0(E∨
2 ), whereE2 is the complex in (2.25) when ∗ = C. It is elementary to
prove thatE2 andE∨
2 are quasi-isomorphic to their zero-th cohomology, so we conclude that
FHilb3 = FHilbdg
3 . The irreducible components of the ﬂag Hilbert scheme FHilb3 are:
FHilb3(C) =Z1∪Z2∪Z3∪Z4∪Z5
whereZ1,...,Z 5 are determined by which eigenvaluesx1,x 2,x 3 are equal to each other:
Z1 ={x1⁄=x2⁄=x3⁄=x2}, Z 2 ={x1 =x2 =x3}
Z3 ={x1 =x2⁄=x3}, Z4 ={x3 =x1⁄=x2}, Z5 ={x2 =x3⁄=x1}
FLAG HILBERT SCHEMES, COLORED PROJECTORS AND KHOV ANOV-ROZANSKY HOMOLOGY 49
OnZ1, because the eigenvalues are generically distinct, the commutation relation [X,Y ] = 0
forces Y = 0 . Then the cyclicity of the vector v implies a,α ⁄= 0 , and so conjugation by g
allows one to seta =α = 1 ande = 0. We conclude that:
(6.3) Z1 = C3
As forZ2, note that one can always subtract a constant matrix fromX without changing any of
the other properties of (6.1). By (2.29), we see that:
(6.4) Z2 = FHilb2(point)× C = PP1
(O(1)
qt ⊕O (−2)
)
× C
