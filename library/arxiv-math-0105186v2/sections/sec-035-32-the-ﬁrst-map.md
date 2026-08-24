---
doc_id: arxiv-math-0105186v2
doc_title: "Along exact sequence for symplectic Floer cohomology Paul Seidel"
section_id: sec-035-32-the-ﬁrst-map
section_title: "The ﬁrst map"
section_number: 3.2
pages: 55-57
source_pdf: 0105186v2.pdf
source_sha256: e1552ceb6c82c27c
doc_brief: "A long exact sequence for symplectic Floer cohomology — 45 sections: Introduction; Dehn twists, and all that; Exact symplectic geometry and ﬁbra"
---
Let S be the surface in Figure 3, which has three boundary componen ts ∂kS
and three strip-like ends (two positive and a negative one). Take the trivial
exact symplectic ﬁbration π : E = S×M→ S, with Ω ∈ Ω 2(E), Θ ∈ Ω 1(E)
pulled back from ω, θ. Equip this with the Lagrangian boundary condition
Q = (∂1S×τL(L0))∪ (∂2S×L)∪ (∂3S×L1);κQ is zero, and KQ(z,x ) is equal
to KτL(L0)(x), KL(x) or KL1(x), for z in the respective component ∂kS. This
gives rise to a relative invariant
Φ rel
0 (E,π,Q ) : HF (L,L 1)⊗HF (τL(L0),L )→HF (τL(L0),L 1).
The purpose of this section is to analyse this more closely, o n the cochain level.
Fix a complex structure j on S, trivial over the ends, and let U ⊂ S be the
open set shaded in Figure 3.
S2
S3
S1
Figure 3:
Lemma 3.3. (E,π,Q ) and U satisfy the conditions of Proposition 2.28(i).
Proof. The curvature of ( E,π ) is zero. A section u(z) = (z,σ (z)) is horizontal
iﬀ σ(z)≡x∈M is constant, and it further satisﬁes u(∂S )⊂Q iﬀ x∈τL(L0)∩
L∩L1. If W⊂S is a connected open subset which intersects all three bounda ry
components, the same description applies to partial horizo ntal sectionsw :W→
E|W withw(W∩∂S )⊂Q. As a consequence, any such section can be extended
to u∈ Mh. This is in particular true for W =U .
Fix somex∈τL(L0)∩L∩L1 and the corresponding constant section u∈ Mh.
By deﬁnition A(u) = 0, and it remains to prove that ind Du,J = 0. From the
description of the points x in Lemma 3.2(iii), together with the corresponding
local statement in Lemma 1.9, it follows that there is a sympl ectic isomorphism
TMx∼= Cn which takes the tangent spaces to τL(L0),L, andL1 to Rn,e2πi/3Rn,
andeπi/3Rn respectively. Since the index is independent of the almost c omplex
structure, we may choose J = j×JM to be the product of j and some ω-
compatible JM on M . We may also assume that the isomorphism TMx∼= Cn
takesJM
x to the standard complex structure. By deﬁnition, the domain ofDu,J
are sections of the vector bundle u∗(TEv,J|TEv)∼=S×TMx, with boundary
55
conditions given by the tangent spaces to τL(L0), L, L1. Its range are (0 , 1)-
forms with values in the same vector bundle. The preceding di scussion allows
us to identify
W1
u ={X∈W 1,p(S, Cn) : Xz∈ei(1−k)π/3Rn for z∈∂kS},
W0
u,J =Lp(Λ 0,1S⊗ Cn).
(3.8)
In (2.5) take ∇ =∇S×∇M to be the product of torsion-free connections on
S and on M . Then the second term ( ∇XJ)◦Du◦j in the formula vanishes,
because Du◦j takes values in TEh whereas∇XJ is nontrivial only on TEv;
and moreover, the pullback connection u∗∇ on u∗TEv is trivial. This shows
that Du,J is the standard ¯∂-operator for functions S → Cn, with boundary
conditions (3.8).
2z
z
z
z1
3
z0 4
z5
Figure 4:
There is a general index formula for such operators, but we pr efer to use an
ad hoc gluing trick instead. Consider the compact surface ¯S in Figure 4, which
is of genus one with one boundary component. Parametrize the boundary by
a closed path l : [0; 6]→ ∂ ¯S, such that l(t) = zt for t∈{ 0, 1, 2, 3, 4, 5} are the
marked points in Figure 4. Take a smooth nondecreasing funct ionλ : [0; 6]→ R
such that
λ(t) =



0 0 ≤t≤ 1,
1/3 2 ≤t≤ 3,
2/3 4 ≤t≤ 5.
1 t = 6.
56
Let ¯D be the ¯∂-operator on the trivial bundle ¯S× Cn → ¯S, with boundary
condition given by the family of Lagrangian subspaces Λ l(t) =eπiλ(t)Rn⊂ Cn.
As a loop in the Lagrangian Grassmannian, this represents n times the standard
generator of the fundamental group. Riemann-Roch for compa ct surfaces with
boundary therefore tells us that ind ¯D =nχ( ¯S)+n = 0. On the other hand, one
can divide ¯S into ﬁve pieces (two shaded and three unshaded ones) as indic ated
in Figure 4, and add strip-like ends to each piece; the standa rd gluing theory
for elliptic operators says that ind ¯D is the sum of the indices of the obvious
corresponding operators on those pieces. For each shaded pi ece, this yields a
copy of Du,J (in one of the two cases, the vector space Cn has been rotated
by eπi/3). The unshaded pieces give rise to operators of index zero. T his can
be derived from the index theorem of [20], or else by directly deforming the
operator to an invertible one. Consider for instance the two intervals of ∂ ¯S
which are contained in the leftmost unshaded piece. The Lagr angian subspaces
Λ z parametrized by the points z in one of these intervals are all equal to eπi/3Rn;
for the other interval, they are of the form eπisRn for 2/3≤ s≤ 1. Since
eπi/3Rn∩eπisRn = 0 for all such s, the Maslov index for paths [20] is zero. The
same holds for the other unshaded pieces, and one concludes t hat 0 = ind ¯D =
2 indDu,J .
At this point, ﬁx
J (1)∈ Jreg(M,τL(L0),L ),
J (2)∈ Jreg(M,L,L 1),
J (3)∈ Jreg(M,τL(L0),L 1).
Proposition 2.28(i) tells us that there is a J∈ J(E,π,j,J (1),J (2),J (3)) which
is both horizontal and regular. By part (ii) of the same resul t, the coeﬃcients
νJ (˜x0,x 1,x ) for ˜x0∈τL(L0)∩L,x1∈L∩L1,x∈τL(L0)∩L1, are zero whenever
χ(˜x0,x 1,x ) = aτL(L0),L1(x)−aτL(L0),L(˜x0)−aL,L1(x1) (3.9)
is < 0. Lemma 3.2(ii) shows that χ(˜x0,x 1,x ), if≥ 0, must be either in [0; ǫ) or
[3ǫ;∞), and that the ﬁrst case only happens for x = p(˜x0,x 1). Hence, if one
writes the relative invariant as
CΦ rel
