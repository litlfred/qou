---
doc_id: arxiv-0811.2435v1
doc_title: "Stability structures, motivic Donaldson-Thomas invariants and cluster transformations"
section_id: sec-032-d0-d6-bps-bound-states-an-example-related-to-the
section_title: "D0-D6 BPS bound states: an example related to the MacMahon function"
section_number: null
pages: 105-109
source_pdf: 0811.2435v1.pdf
source_sha256: 615b04eca83bcade
doc_brief: "Stability structures, motivic Donaldson-Thomas invariants and cluster transformations — 43 sections: Introduction; Counting problems for 3-dimensiona; Non-commutative varieties with pol"
---
the MacMahon function
LetX be a compact 3d Calabi-Yau manifold over k, such that H 1(X,OX) =
0. We denote by C(0,6) the ind-constructible triangulated category generated
by the structure sheaf OX and torsion sheaves Ox,x ∈ X.22 This category
has at-structure with the heart consisting of coherent sheaves on X which are
trivial vector bundles outside of a ﬁnite set. Then OX is the only spherical
object in C(0,6). We choose Γ = Zγ1⊕ Zγ2, which is the image of K0(C(0,6))
under the Chern class in the quotient of the Chow group by the n umerical
equivalence, where γ1 = cl k(Ox)) for any point x∈ X, and γ2 = cl k(OX).
We are going to consider a stability condition σ = (Z, (C(0,6))ss,... ) onC(0,6)
with the above t-structure and such that
z1 :=Z(γ1) =−1, z2 =Z(γ2) = i =
√
−1 .
Then σ-semistable objects in C(0,6) will be either pure torsion sheaves sup-
ported at ﬁnitely many points or torsion-free sheaves.
This corresponds to the following picture for Ω( γ).
22This category is related to the counting of D0-D6 BPS bound st ates, compare with
[13], formula (6.1).
105
✲
✻
r r r r r
r r r r r
r r r r r
r r r r r
−χ −χ
−χ χ2+5χ
2 −χ3+15χ2+20χ
6
?
?
?
?
?
1 0
0 0 0
0 0 0 0
Let us comment on the last ﬁgure.
a) The vertical line corresponds to the subcategory generat ed by the
spherical object OX, for which we know Ω( γ). Namely, Ω( γ2) = 1 and
Ω( nγ2) = 0,n /greaterorequalslant2.
b) Horizontal line z2−nz1,n /greaterorequalslant0 corresponds to sheaves of ideals of
0-dimensional subschemes. Then:
∑
n/greaterorequalslant0
Ω( γ2−nγ1)tn =M(−t)χ(X),
where χ(X) is the Euler characteristic of X and
M(x) :=
∏
n/greaterorequalslant1
(1−xn)−n∈ Z[[x]]
is the MacMahon function (see [47], [4] about this identity) .
c) The torsion sheavesOx,x∈X are Schur objects inC(0,6). Their moduli
space is canonically identiﬁed with X. By Behrend’s formula (see [2]) their
contribution to the virtual fundamental number of objects i s
Ω( γ1) = (−1)dimXχ(X) =−χ(X).
d) The numbers marked by “?” correspond to (possibly non-Sch ur) ob-
jects. Notice that there are no semistable objects with the c lass nγ2−mγ1
with 0 <m<n . They correspond to the sector ﬁlled by 0’s.
106
Let us now choose a path σz1(τ ),z2(τ ) in the space of the above stability
structures such that
z1(τ ) =− exp(iτ ), z2(τ ) = i,
whereτ∈ [0,π/ 2 +ε], i=√−1 and ε> 0 is suﬃciently small. The heart of
the t-structure for τ >0 consists of complexes of sheaves E such that there
exists an exact triangle E1→E→E2[−1], where E1 is a torsion-free sheaf
and E2 is a torsion sheaf (indeed, the new t-structure is obtained from the
initial one by the standard tilting procedure). This heart c oincides with the
categoryC(0,6)
V for any τ∈ (0,π/ 2 +ε] where
V ={z∈ C∗| 0≤ Arg(z)≤π/2 +ε}.
ObjectOX∈C (0,6)
V can not be represented as a non-trivial extension in C(0,6)
V ,
hence it is semistable for any τ∈ [0,π/ 2 +ε].
Let us now consider the case τ∈ (π/2,π/ 2 +ε]. Then object OX has the
minimal argument among all non-trivial objects in C(0,6)
V . Therefore, all other
indecomposable semistable objects E are strictly on the left of OX, and we
have
Ext0(E,OX) = 0 .
Taking the long exact sequence of Ext-groups to the object OX one easily
shows that in the decomposition E1→E→E2[−1] we have E1 = 0. Hence
in this new heart C(0,6)
V the left orthogonal to OX consists of objects F [−1],
whereF is a torsion sheaf. We conclude that for the stability condit ion with
τ ∈ (π/2,π/ 2 + ε] the only semistable objects have classes which belong
to Z⁄=0γ2⊔ Z⁄=0γ1. Therefore, all DT-invariants Ω τ (γ) for σz1(τ ),z2(τ ) with
τ > π/2 are completely determined by the numbers an = Ω τ (−nγ1),n /greaterorequalslant1
(and known invariants Ω τ (mγ2) = δm,1,m /greaterorequalslant1). Then the wall-crossing
formula determines all the invariants Ω( γ) = Ω 0(γ) for the initial stability
condition σz1(0),z2(0) in terms of the numbers an,n /greaterorequalslant1.
The wall-crossing formula implies that the following ident ity:
∏
n/greaterorequalslant1
Tan
−nγ1Tγ2 =
−→∏
m/greaterorequalslant1,n/greaterorequalslant0
T Ω(−nγ1+mγ2)
−nγ1+mγ2
∏
n/greaterorequalslant1
Tan
−nγ1 .
Using the known result for special values Ω( γ2−nγ1), n /greaterorequalslant1 (in terms of
the MacMahon function), one can deduce that all the numbers an = Ω( nγ1))
107
for n /greaterorequalslant1 are equal to −χ(X). We don’t know how to prove this identity
directly. We see that invariants Ω τ (γ) for τ >π/2 have a much simpler form
than Ω( γ) = Ω 0(γ). Moreover, it is now possible (in principle) to work out a
formula for Ω( −nγ1 +mγ2) for any given m /greaterorequalslant2.
Remark 23 One can try to generalize the above considerations to the cas e
of D0-D2-D6 bound states. Mathematically this means that we consider the
triangulated category generated by the sheaf OX and sheaves with at most 1-
dimensional support (cf. [47]). A problem arises here, sinc e for the natural
t-structure there is no central charge which gives a stabilit y condition on the
category. Presumably, in this case one can use the limit stab ility conditions
(see [1], [73]).
Remark 24 Let X be a 3d complex Calabi-Yau manifold, C≃ P1⊂ X a
rational curve with normal bundle isomorphic to O(−1)⊕O (−1) andC be an
ind-constructibleA∞-version of the category PerfC(X) of perfect complexes
supported on C. Then Γ := K0(C)≃ Z2 carries a trivial skew-symmetric
(Euler) form. The lattice Γ is generated by cl(Opt) and cl(OC). It follows
that there are no wall-crossings in this case, and hence our i nvariants Ω( γ) do
not change under continuous deformations of a stability con dition. In order
to use this idea for computations one can choose two stabilit y conditions by
specifying the corresponding t-structures and central charges:
a) choose the t-structure with the heart consisting of coherent sheaves on
X supported on C and the central charge Z such that
Z(cl(Opt))∈ R<0, ImZ(cl(OC))> 0 ;
b) choose the t-structure given by the category of ﬁnite-dimensional rep-
resentations of the quiver with two vertices and two double a rrows in each
direction and the potential
W =a1b1a2b2−a1b2a2b1 .
Then calculations from [66] give the following formulas for the invariants
Ω( γ):
Ω( n cl(Opt)) = −2,n⁄= 0 ;
Ω( n cl(Opt)± cl(OC)) = 1 ,n∈ Z .
In all other cases Ω( γ) = 0 .
For recent generalization of [66] see [49],[50],[51].
108
