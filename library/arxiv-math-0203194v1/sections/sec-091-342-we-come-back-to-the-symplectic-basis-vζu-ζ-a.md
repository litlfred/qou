---
doc_id: arxiv-math-0203194v1
doc_title: "Period mappings and diﬀerential equations. From C to Cp Tˆohoku-Hokkaidˆo lectures in Arithmetic Geometry Yves Andr´ e (with appendices by F. Kato and N. Tsuzuki)"
section_id: sec-091-342-we-come-back-to-the-symplectic-basis-vζu-ζ-a
section_title: "We come back to the symplectic basis vζ,u ζ and write 1√−1Fζ"
section_number: 3.4.2
pages: 43-47
source_pdf: 0203194v1.pdf
source_sha256: 6f35e530f07116dc
doc_brief: "Period mappings and differential equations. From C to Cp Tôhoku-Hokkaidô lectures in Arithmetic Geometry Yves André (with appendices by F. Kato and N. Tsuzuki) — 580 sections: INTRODUCTION; INTRODUCTI"
---
ω in
the form vζ +τu ζ, where
τ =−
⟨ω,v ζ⟩
⟨ω,u ζ⟩∈ (z−ζcan)ˆQur
p [[z−ζcan]].
This deﬁnes an unbounded element of O(DCp(ζcan, 1−)) (notice that another
choice of u
ζ multipliesτ by an element of Z×
p ).
40 I. ANALYTIC ASPECTS OF p-ADIC PERIODS.
Applying∇(d/dz) to 1√−1Fζ
ω =vζ +τu ζ and using
⟨
ω,∇( d
dz )(ω)
⟩
= 2
z(z−1) ,
one derives:
dτ
dz = 2
z(1−z)F 2
ζ
.
The exponential of τ is called the Dwork-Serre-Tate parameter. We shall
recall later its meaning as a parameter for p-divisible groups. It satisﬁes the
following remarkable integrality property [ Dw69, Th.4], [ Ka73]
q =eτ∈ 1 + (z−ζcan)ˆ
Zur
p [[z−ζcan]].
This suggests the following question: does q arise from an element of ˆRet
ord ?
The answer is no. This may be seen by considering q (mod p): the for-
mula for dτ/dz = dlog(q) shows that q (mod p) is non-constant (dlog( q)≡
2(hp)2/p −1
z(z−1) (mod p)). If q comes from an element of ˆRet
ord which specializes to
1 at every canonical modulus ζcan, one has q≡ 1 (mod p), a contradiction.
3.5. Complex counterpart: the supersingular locus.
Let us now revert things and try to understand the complex sit uation
from the p-adic viewpoint!
Let D+ and D− be the (complex-conjugate) connected components of
D( 1
2, 3
2
−)\
(
D(−1
4 , 3
4
+)∪ D( 5
4, 3
4
+)
)
. Let S be the complement of D+∪
D− in the complex plane. Note that S is closed and arcwise connected,
and that πtop
1 (S) is a free group with two generators γ+,γ− (see ﬁgure 8).
Its interior S◦ has three connected (simply-connected) components D0 =
D(−1
4 , 3
4
−), D1 = D( 5
4, 3
4
−) and D∞.
D+
D−
D∞D0 D1
−1 0
.
1/2 1
.
2
γ+
γ−
Figure 8
3. THE TALE OF F ( 1
2 , 1
2 , 1; z). 41
LetO(S) denote the ring of continuous functions on S analytic in S◦.
According to Mergelyan’s theorem [ Mer54], they are uniform limits of ra-
tional functions on every compact K⊂ S such that π0(C\K, 0) is ﬁnite.
This ring is however not stable under diﬀerentiation, and we consider its
diﬀerential closure R inO(S◦). We also consider the integral closure Ret
ofR inO(S◦). Every element of Ret deﬁnes a multivalued locally analytic
function on S, i.e. an analytic germ which may be analytically continued
along any path of S not ending at −1, 1
2, 2, in such a way that the germ at
the other extremity is analytic.
For instance, F ( 1
2, 1
2, 1;z) may be viewed as an element of Ret: in fact,
F ( 1
2, 1
2, 1;z)4∈O (S). An explicit continuous extension of F ( 1
2, 1
2, 1;z)4 from
D0 toS is given by F ( 1
2, 1
2, 1; 1−z)4 in D1, 1
z2F ( 1
2, 1
2, 1; 1
z )4 in D∞, and the
values Γ(1 /4)8
64π6 , Γ(1 /4)8
16π6 , Γ(1 /4)8
64π6 at−1, 1
2, 2 respectively [ Car61, p.189]. On
the other hand, note that dlog F ( 1
2, 1
2, 1;z) is in R but not in O(S).
The de Rham cohomology of the Legendre elliptic pencil gives rise to an
R[1/z(1−z)]-module with connection (H,∇). It admits a unique non-zero
horizontal submoduleU which extends to S; we use the same symbol for the
extension. It can be described along the following lines:
• For anyu∈ (U⊗RRet)∇, “the” image of u inO(Dj)(j = 0, 1, or∞),
is a bounded solution of the diﬀerential operator L 1
2 , 1
2 ,1.
•U⊗ RRet[ 1
z(1−z) ] =
(
H⊗R[ 1
z(1−z) ]Ret[ 1
z(1−z) ]
)∇⊗CRet[ 1
z(1−z) ].
•
(
H⊗R[ 1
z(1−z) ]Ret[ 1
z(1−z) ]
)∇ has a canonical Z[i]-submodule (i =√−1)
which can be locally identiﬁed with the part H 1(X an
z , Z[i])isotriv of
H1(X an
z , Z[i]) where πtop
1 (S,z ) acts through a ﬁnite group.
•U| ∇
D 0 has a canonical Z-submodule, which can be identiﬁed with the
part of H 1(X an
z , Z[i])isotriv invariant under complex conjugation. One
of the two generators u satisﬁes
⟨
ω, u
2iπ
⟩
=iF
(1
2, 1
2, 1;z
)
in O(D0).
Similarly,U|∇
D 1 has a canonical Z-submodule, and for one of the two
generators u, one has
⟨
ω, u
2iπ
⟩
=iF
(1
2, 1
2, 1; 1−z
)
in O(D1).
Note the occurrence of 2 iπ in these formulas.
• The local monodromy γ+ around D+ maps onto
Aut H1(Xs, Z[i])isotriv≃ Z/4Z.
Same for γ−. The local monodromy at ∞ acts as±1.
• In D+ and in D−, there is no non-zero bounded analytic solution of
L 1
2 , 1
2 ,1.
42 I. ANALYTIC ASPECTS OF p-ADIC PERIODS.
This is quite similar to §§3.2,§§3.3, D+∪ D− playing the role of the
supersingular locus. This picture is assuredly very diﬀerent from the tradi-
tional view of monodromy for F ( 1
2, 1
2, 1;z), and may shed some light upon
the divergences between the topological and algebraic appr oaches to analytic
continuation in the p-adic case (here of course, the coexistence of the two
pictures is explained by the fact that the principle of uniqu e continuation
(Deﬁnition 1.1.1) fails for the sheaf of germs of continuous functions on S,
analytic on S◦).
The tale of F ( 1
2, 1
2, 1;z) is not ﬁnished: we have not yet explored the
islands of supersingularity. We shall reach them in §§5.2.
4. ABELIAN PERIODS AS ALGEBRAIC INTEGRALS. 43
4. Abelian periods as algebraic integrals.
Abstract: We discuss periods of abelian varieties. Their p-adic counterparts
live naturally in Fontaine’s ring BdR. We present Colmez’ construction of abelian
p-adic periods, which relies on p-adic integration and reﬂects as closely as possible
the complex picture. We also deal with the concrete evaluati on of elliptic p-adic
periods.
4.1. Over C.
Let A be an abelian variety over C of dimension g, and ω1,... ,ω g a
basis of invariant diﬀerential forms. Let Λ be the image of th e map
ι : H 1(A(C), Z)→ Cg ; γ↦→
(∫
γ
ωi
)
i
.
One has a canonical isomorphism
Cg/Λ ∼−→A(C).
Let us denote the projection Cg→ A(C) by pr. For any diﬀerential one-
formω of the second kind, one can consider a primitive function fω of pr∗ω;
it is meromorphic (univalued) on Cg, because all residues of ω are 0 by
deﬁnition, and it is unique up to addition of an arbitrary con stant. Then
fω(z1 +z2 +z3)−fω(z1 +z2)−fω(z1 +z3) +fω(z1) deﬁnes a periodic function
on (Cg)3, hence induces a meromorphic function on A(C)3, which we denote
by F 3
ω. Note that the function F 3
ω can also be deﬁned purely algebraically
by the following conditions:
• F 3
ω (z1, 0,z 3) = F 3
ω (z1,z 2, 0) = 0.
• dF 3
ω =m∗
123ω−m∗
12ω−m∗
13ω +m∗
1ω,
where m123 is the addition A3→A sending (z1,z 2,z 3) to z1 +z2 +z3, etc.
For γ ∈ H1(A(C), Z) the value fω
(
i(γ) + a
)
−fω(a) does not depend on
a∈ Cg (a being chosen so that i(γ) +a anda are not poles of fω), and one
has the equality
fω
(
i(γ) +a
)
−fω(a) =
∫
γ
ω,
which describes the period pairing
H1
dR(A)× H1(A(C), Z)−→ C
(or equivalently, the isomorphism H 1
dR(A)⊗ C ∼→ H1
B(A(C), Z)⊗ C.) Here
H1
dR(A) denotes the ﬁrst algebraic de Rham cohomology group of A, which
coincides with the group of diﬀerential forms of the second k ind modulo
exact forms.
