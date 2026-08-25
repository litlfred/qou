---
doc_id: 13116841v1
doc_title: "Observables in Loop Quantum Gravity with a cosmological constant"
section_id: sec-001-contents
section_title: "Contents"
section_number: null
pages: 1-8
source_pdf: 1311.6841v1.pdf
source_sha256: ca65879d80b1e1c3
doc_brief: "Observables in Loop Quantum Gravity with a cosmological constant — 5 sections: Introduction; Contents; Scalar product"
---
Introduction 2
I.Uq(su(2)) in a nutshell 4
A. Deﬁnition of Uq(su(2)) 4
B. q-harmonic oscillators and the Schwinger-Jordan trick 7
II. Tensor operators for Uq(su(2)) 7
A. Deﬁnition and Wigner-Eckart theorem 7
B. Product of tensor operators: scalar product, vector product and triple product 8
1. Scalar product 9
2. Vector product 10
C. Tensor products of tensor operators 10
III. Realization of tensor operators of rank 1/2 and 1 forUq(su(2)) 11
A. Rank 1/2 tensor operators 11
B. Rank 1 tensor operators 13
IV. Observables for the intertwiner space 16
A. General construction and properties of intertwiner observables 16
B.Uq(u(n)) formalism for LQG deﬁned over Uq(su(2)) 18
V. Geometric interpretation of some observables in the LQG context 20
Outlook 24
A. Hyperbolic cosine law 25
B. Useful formulae 25
References 27
∗Electronic address: maite.dupuis@gravity.fau.de
†Electronic address: fgirelli@uwaterloo.ca
2
Introduction
Background: There are diﬀerent proposals to understand the nature of the cosmological constant Λ. It can be
interpreted as encoding some type of vacuum energy (see [1–3] and references therein) or as a coupling constant just
like the Newton’s constantG. The loop quantum gravity and spinfoam frameworks use the latter interpretation which
is motivated by the seminal works of Witten [4], and later of Fock and Rosly [5], and Alekseev, Grosse, Schomerus
[6, 7]. Indeed, in a 3d space-time, one can rewrite General Relativity with a (possibly zero) cosmological constant as
a Chern-Simons gauge theory 1. The general phase space structure of the theory for any metric signature and sign of
Λ can be treated in a nice uniﬁed way [8], using Poisson-Lie groups [9], the classical counterparts of quantum groups.
The quantization procedure leads explicitly to a quantum group structure. The full construction, from phase space
to quantum group is usually called combinatorial quantization [5–7].
We can also quantize 3d gravity using the spinfoam approach. In this approach, 3d gravity is formulated as a
BF theory. When Λ = 0, this is the well-known Ponzano-Regge model (both Euclidian or Lorentzian), based on
the irreducible unitary representations of the relevant gauge group. When Λ ⁄= 0, the quantum group structure is
introduced by hand. The Ponzano-Regge model is deformed, using irreducible unitary representations of the relevant
quantum deformation of the gauge group. This is then called the Turaev-Viro model [10]. The argument consolidating
the incorporation of the cosmological constant into a spinfoam model through a quantum group comes from the semi-
classical limit. Indeed, the asymptotics of the deformed {6j}q symbol, entering into the deﬁnition of the Turaev-Viro
model, goes to the Regge action with a cosmological constant in the regime 𝓁p≪𝓁≪R.
The third approach to quantize gravity is the canonical approach, i.e. the loop quantum gravity approach (LQG). In
this case, performing the classical hamiltonian analysis to General Relativity, the cosmological constant only appears
in the Hamiltonian constraint. This means that the kinematical space is the same whether Λ = 0 or not. In particular
this kinematical space (where the Gauss constraint has been solved) is based on the classical relevant gauge group.
Therefore at this stage, quantum groups naturally appear only in the combinatorial quantization of Chern-Simons.
Diﬀerent quantum groups are revealed according to the metric signature and the sign of the cosmological constant.
When Λ⁄= 0, we obtain q-deformed version of the gauge group Uq(g), where g is the Lie algebra of the gauge group
G = SL(2, R) in the Lorentzian case, SU(2) in the Euclidean case, with q function of the Planck scale and the
cosmological radius R =
√
|Λ|. The deformation parameter q can be real or complex. A nice way to recall what is q
according to the sign of Λ and the signature is to consider q =exp
(
− ℏG
√
Λ√
c2
)
and posingc2 > 0 in the Lorentzian case
andc2 < 0 in the Euclidian case [15]. Note that this trick givesq orq−1. The full relevant quantum group arising from
the combinatorial quantization is D(Uq(g)), the Drinfeld double of Uq(g). When Λ = 0, we get the Drinfeld double
D(U(g)) with a non-commutative parameter given by κ = 𝓁p in units ℏ = 1 = c. A list of the diﬀerent quantum
groups relevant for 3d gravity is given in the ﬁrst table below.
Since classically, the Chern-Simons formulation and the standard formulation of General Relativity are equivalent
(modulo the degenerated metrics), we can wonder whether the Chern-Simons combinatorial quantization formalism,
LQG and the spinfoam framework are related in some ways. It can be shown explicitly in the Euclidian case, with
Λ > 0, that the Chern-Simons quantum model and the Turaev-Viro model are related, more precisely, the Turaev
Viro amplitude is the square of the Chern-Simons amplitude [11]. On the other hand, it seems diﬃcult to relate the
LQG formalism, when Λ⁄= 0, to a spin foam model based on a quantum group if we assume that the LQG kinematical
space is based on a classical group such as SU(2).
When Λ = 0, it is also possible to relate the Chern-Simons amplitude and the Ponzano Regge amplitude [12], which
allows to identify a hidden symmetry given by the Drinfeld double D(U(g)) in the Ponzano-Regge model. Still when
Λ = 0, explicit links between LQG and the spinfoam framework [16] or between the Chern Simons combinatorial
quantization and LQG [14] have been identiﬁed. Note also that we can identify a hidden quantum group structure
(the Drinfeld double) in LQG when Λ = 0 [12–14], which is consistent with the other approaches. The diﬀerent cases
for 3d gravity are summarized in the ﬁrst table. For more details, we refer to the excellent review [15].
1 This is actually an extension of General Relativity since degenerated metrics are allowed.
3
Signature Λ Quantum group QG models
Euclidian
Lorentzian
Λ> 0
Λ = 0
Λ< 0
Λ> 0
Λ = 0
Λ< 0
D(Uq(su(2))), q =ei
𝓁p
R
D(U(su(2))), κ =𝓁p
D(Uq(su(2))), q =e
𝓁p
R
D(Uq(sl(2, R))), q =e−
𝓁p
R
D(U(sl(2, R))), κ =𝓁p
D(Uq(sl(2, R))), q =e−i
𝓁p
R
Chern-Simons
[11]
↔ Turaev-Viro
?
↔ LQG
Chern-Simons
[12]
↔ Ponzano-Regge
[16]
↔ LQG
[14]
↔ Chern-Simons
Chern-Simons
?
↔ Turaev-Viro
?
↔ LQG
Chern-Simons
?
↔ Turaev-Viro
?
↔ LQG
Chern-Simons
[12]
↔ Ponzano-Regge
[16]
↔ LQG
[14]
↔ Chern-Simons
Chern-Simons
?
↔ Turaev-Viro
?
↔ LQG
When dealing with 4d space-time, there is no Chern-Simons theory to guide us. Hence, it is postulated that the
cosmological constant should also be introduced through a quantum group structure. From the spinfoam approach,
one then considers the model one prefers (Barrett-Crane (BC) or EPRL-FK) when Λ = 0, based on the irreducible
unitary representations of the gauge group and one deforms it [17–20]. To argue a posteriori, that this is the right
thing to do, we can look at the asymptotic of the spinfoam amplitude and check we recover the Regge action with a
cosmological constant [21]. It is quite interesting that the current ”physical” EPRL spinfoam model deﬁned in the
Lorentzian case, with Λ > 0 leads to a ﬁnite amplitude [19, 20].
In 4d, we are not able to connect the Hamiltonian constraint arising in LQG to a spinfoam model, even when Λ = 0.
Just as in 3d, it is not clear at all why a quantum group structure should appear in the LQG framework. There exist
few arguments to justify this postulate [22]. We include now a table summarizing the diﬀerent quantum group models
appearing in 4d quantum gravity.
Signature Λ Quantum group QG models
Euclidian
Lorentzian
Λ> 0
Λ = 0
Λ< 0
Λ> 0
Λ = 0
Λ< 0
Uq(so(4)), q =ei2π𝓁2
pΛ
?
Uq(so(4)), q =ei2π
𝓁2
p
Λ
Uq(so(3, 1)), q =e𝓁2
pΛ
?
Uq(so(3, 1)), q =e
𝓁2
p
Λ
BC or EPRL-FK
?
⇔ LQG
BC or EPRL-FK
?
⇔ LQG
BC or EPRL-FK
?
⇔ LQG
BC or EPRL-FK
?
⇔ LQG
BC or EPRL-FK
?
⇔ LQG
BC or EPRL-FK
?
⇔ LQG
Several remarks can be made at this stage. The partition function of the Plebanski action is invariant under the
transformation Λ →− Λ [23], which explains why we have the same quantum group for the diﬀerent signs of the
cosmological constant. This change of sign for Λ is equivalent to q→q−1.
In the ”physical” case (Lorentzian, Λ > 0) in the EPRL-FK model, spin networks encoding the quantum state of
space are deﬁned in terms of Uq(su(2)), with q real [19, 20].
We also emphasize en passant, that the quantum deformation of the Lorentz group (in 3d or 4d) for q complex are
not understood.
Motivations: A common feature of the 3d and 4d quantum gravity is that it is hard to understand why a q-
deformation of the gauge group would appear from the LQG perspective. Since we do not know how to solve the
Hamiltonian constraint (for Λ⁄= 0) and since we would like to compare the LQG approach with the well-known models
coming from combinatorial quantization formalism and spinfoam, we would like to deﬁne LQG with a q-deformed
group and see what the consequences are. We hope then to identify some hints pointing to the quantum group
apparition in this context. In particular, if LQG deﬁned in terms of a quantum group describes well quantum curved
geometries, then this is a good sign that this could be a useful theory to consider.
To this aim, we need to understand the structure of the observables associated to spin networks deﬁned using the
representations of a quantum group. Not much work has been done in this context: LQG with a quantum group has
only been explored using the loop variables by Major and Smolin [24–26].
When Λ = 0, the structure of the observables for a spin network (or an intertwinner) is well understood, thanks
to the spinor approach to LQG [27–29]. In particular it is possible to construct a closed algebra (a u(n) Lie algebra,
wheren is the number of intertwinner legs) that generates all the observables acting on an intertwinner. This approach
not only gives some information about the observable structure but it has been applied to diﬀerent contexts, with
many interesting results [27–29]. This formalism has helped to understand that spin networks can be seen as the
quantization of classical discrete geometries, the so called twisted geometries [30, 31]. It allowed the construction of
a new Hamiltonian constraint in 3d Euclidian gravity [54], such that the kernel of this constraint is given by the 6 j
symbol, i.e. the Ponzano-Regge amplitude. It has provided the tools to implemented in a rigorous way the simplicity
constraints, using the Gupta-Bleuler method, to build a spinfoam model for Euclidian gravity (Λ = 0) [32].
4
Generalizing the spinor formalism to the quantum group case will help to better understand the quantum gravity
regime with a nonzero cosmological constant. Indeed, within this formalism, we should be able to construct an
Hamiltonian constraint relating Turaev-Viro and LQG [55], and we should be able to understand what is the relevant
phase space for LQG, the space of curved twisted geometries [49].
Main results: This generalization of the spinor formalism to the quantum group case is the main result of this
paper. We have focused on the quantum group Uq(su(2)) with q real, which is therefore relevant for 3d Euclidian
gravity with Λ < 0 and the physical case, i.e. 4d Lorentzian gravity with Λ > 0.
The key idea for this generalization is the use of tensor operators. These are well-known in the quantum mechanical
case for SU(2) [33]. Essentially, they are sets of operators that transform well under SU(2), i.e. as a representation.
They are known in LQG under the name of grasping operators. However they have not been studied intensively in this
context. We show that considering these operators seriously naturally leads to the spinor approach to LQG. These
tensor operators can be generalized to the quantum group case (more exactly they are deﬁned for any quasi-triangular
Hopf algebra) [34].
Given anUq(su(2)) intertwinner with n legs, we have identiﬁed some sets of operators that transform well under
Uq(su(2)). Due to the quantum group structure, they are much more complicated than their classical counterparts.
In particular their commutation relations are pretty complicated. We have clariﬁed the construction of Uq(su(2))
intertwinner observables. We show how there exists a fundamental algebra generating all observables, which is a
deformation of the u(n) algebra. We also discuss the geometric interpretation of some observables for 3d Euclidian
LQG with Λ < 0, pinpointing the fact that the quantum group structure encodes as expected the notion of curved
discrete geometry. Some of these results were already announced in [35].
Outline of the paper: The paper is organized as follow. In section I, we recall the main features ofUq(su(2)), the
q-deformed universal enveloping algebra of SU(2), with q real. We recall as well the notion of q-harmonic oscillators
which are used to build some tensor operators explicit realizations.
Section II is a review about tensor operators for Uq(su(2)), the essential tools of our construction. Due to the
nonlinearity of the quantum group structure, Uq(su(2)) tensor operators are more complicated than the standard
SU(2) case. In particular, due to the nontrivial nature of the quantum group action, the tensor product of tensor
operators is highly nontrivial, which will make the construction of tensor operators acting on diﬀerent legs of an
intertwiner quite cumbersome, but necessary.
Diﬀerent explicit realizations of tensor operators for Uq(su(2)) are given in section III. We recalled the results of
Quesnes [36] regarding spinor operators: their deﬁnition in terms of q-harmonic oscillators and their commutation
relations for spinor operators acting on diﬀerent legs. We have extended this analysis to vector operators, which will
be relevant for the construction of the standard geometric operators.
The main results of this paper are presented in section IV and V. We discuss the general construction of observables
for a Uq(su(2)) intertwiner. We construct a new realization of Uq(u(n)) in terms of tensor operators, which is also
invariant under the action of Uq(su(2)). We have identiﬁed the non-linear map relating our invariant operators to
the standard Uq(u(n)) Weyl-Cartan generators. We construct diﬀerent geometric operators which we interpret in
the context of 3d Euclidian LQG with Λ < 0. We show how we get a quantization of the hyperbolic cosine law,
a quantization of the length and of the area of a triangle. We pinpoint also how the presence of the cosmological
constant allows for a notion of minimum angle.
In the concluding section, we discuss the possible follow-ups of this tensor operator approach to LQG.
We have also included some appendices to recall the deﬁnition of the hyperbolic cosine law as well as some relevant
formulae regarding theUq(su(2)) recoupling coeﬃcients.
I. Uq(su(2)) IN A NUTSHELL
A. Deﬁnition of Uq(su(2))
In this section, we review the salient features of Uq(su(2)), which we shall extensively use, to ﬁx the notations. We
considerUq(su(2)), the q-deformation of the universal algebra of SU(2), with q real, generated by Jz, J+, J−. We
have the commutation relations
[Jz,J±] =±J±, [J+,J−] = [2Jz], with [Jz] = qJz/2−q−Jz/2
q1/2−q−1/2 . (1)
Forq→ 1 the right-hand side of the second equation of (1) approaches 2 Jz and we thus recover the usual Lie algebra
su(2).Uq(su(2)) is equipped with a structure of quasitriangular Hopf algebra (∆ ,ϵ,S, R) [9, 39, 40].
5
• The coproduct ∆ : Uq(su(2))→U q(su(2))⊗U q(su(2)) encodes physically the total angular momentum of a
2-particle system.
∆Jz =Jz⊗ 1 + 1⊗Jz, ∆J± =J±⊗qJz/2 +q−Jz/2⊗J±. (2)
Considering the un-deformed case, we have
(∆Jσ)|j1m1,j 2m2⟩ = (Jσ⊗ 1 + 1⊗Jσ)|j1m1j2m2⟩ = (J(1)
σ +J(2)
σ )|j1m1j2m2⟩, where σ = +,−, z. (3)
In the deformed case, the addition of angular momenta (2) is non-commutative, hence the addition of q-angular
momenta depends on the order we set our particles. As we shall see, the braiding constructed using theR-matrix
will allow to relate diﬀerent orderings.
• The counit ϵ :Uq(su(2))→U q(su(2)) is deﬁned such that ϵ(I) = 1, ϵ(Jσ) = 0 for σ = +,−, z.
• The antipode S :Uq(su(2))→U q(su(2)) encodes in some sense the notion of inverse angular momentum.
SJz =−Jz, SJ ± =−q±1/2J±. (4)
• TheR-matrix encodes the ”amount” of non-commutativity of the coproduct, i.e. of the addition of angular
momenta. Indeed, if we note ψ :Uq(su(2))⊗Uq(su(2))→U q(su(2))⊗Uq(su(2)), the permutation, then we have
that
(ψ◦ ∆)X =R(∆X)R−1. (5)
In terms of the Uq(su(2))-generators, theR-matrix can be written as
R =
∑
R1⊗R 2 =qJz⊗Jz
∞∑
n=0
(1−q−1)n
[n]! qn(n−1)/4(qJz/2J+)n⊗ (q−Jz/2J−)n, (6)
where [n] denotes the q-number [n]≡ q
n
2−q−n
2
q
1
2−q− 1
2
. A co-commutative product would simply mean that R = 1⊗ 1,
which is obtained when q→ 1 in (6). Further properties of the R-matrix are given in the Appendix B, in
particular its expression in terms of Clebsch-Gordan coeﬃcients.
The non-co-commutativity of the coproduct implies that we have a ”non-commutative” tensor product. Essen-
tially, we would get a symmetric 2-particle system if the permutation of the particles states does not aﬀect the
total observable, that is the permutation leaves invariant the coproduct, ψ◦ ∆ = ∆.
If it is non-co-commutative, as in the Uq(su(2)) case, we can still deﬁne a deformed permutation ψR – thanks
to the existence of the R-matrix [34, 40].
ψR :V⊗W → W⊗V
v⊗w → ψR(|v,w⟩)≡ψ(R|v,w⟩) =
∑
ψ(|R1v,R2w⟩) =
∑
|R2w,R1v⟩. (7)
Using the key property (ψ◦ ∆)X =R(∆X)R−1, we have that
ψR(X(|v,w⟩)) =ψ(RX(|v,w⟩)) =ψ(R(∆X)|v,w⟩) =ψ((ψ◦ ∆X)R|v,w⟩) = (∆X)ψ(R|v,w⟩) =X(ψR(|v,w⟩)).
Hence, the tensor product is only symmetric under this deformed notion of permutation. From now on, we shall
always consider this deformed permutationψR which is the natural notion of permutation in this quasi-triangular
context.
The representation theory of Uq(su(2)) with q real is very similar to the one of su(2) [37]. A representation Vj is
generated by the vectors|j,m⟩ withj∈ N/2 andm∈{−j,..,j}. The key-diﬀerence is that the action of the generators
on these vectors generates q-numbers.
Jz|jm⟩ =m|jm⟩, (8)
J±|jm⟩ =
√
[j∓m][j±m + 1]|jm± 1⟩. (9)
A Casimir operator can be deﬁned as
C =J+J− + [Jz][Jz− 1] =J−J+ + [Jz][Jz + 1]. (10)
6
The tensor product of vectors|j1m1,j 2m2⟩ can be decomposed into a linear combination of vectors using theq-Clebsh-
Gordon (CG) coeﬃcients qC j1 j2 j
m1m2m .
|j1m1,j 2m2⟩ =
∑
j,m
qC j1 j2 j
m1m2m|jm⟩, j =|j1−j2|,..,j 1 +j2. (11)
Conversely, given a representation Vj ofUq(su(2)) we can decompose it along two representations Vj1 and Vj2 of
Uq(su(2)) (with|j1−j2|≤ j≤j1 +j2 )
|jm⟩ =
∑
m1,m2
qC j1 j2 j
m1m2m|j1m1,j 2m2⟩. (12)
Acting with a generator Jσ (σ = +,−,z ) on the righthand side of (11) and with its coproduct on the lefthand side of
(11) we obtain a recursion relation for the CG coeﬃcients [37]. Such recursion relations can be taken as deﬁning the
CG coeﬃcients.
Jz ⊿|j1m1,j 2m2⟩ =
∑
j,m
qC j1 j2 j
m1m2mJz ⊿|jm⟩⇔ ∆Jz|j1m1,j 2m2⟩ =
∑
j,m
qC j1 j2 j
m1m2mJz|jm⟩
⇒ m1 +m2 =m
J± ⊿|j1m1,j 2m2⟩ =
∑
j,m
qC j1 j2 j
m1m2mJ± ⊿|jm⟩⇔ ∆J±|j1m1,j 2m2⟩ =
∑
j,m
qC j1 j2 j
m1m2mJ±|jm⟩
⇒ q−m1
2 ([j2±m2][j2∓m2 + 1])
1
2
qC j1 j2 j
m1m2∓ 1m +q
m2
2 ([j1±m1][j1∓m1 + 1])
1
2
qC j1 j2 j
m1∓ 1m2m
= ([j∓m][j±m + 1])
1
2
qC j1 j2 j
m1m2m± 1. (13)
We refer to the Appendix B for further CG coeﬃcients relevant properties.
Let us now introduce the notion of intertwiner forUq(su(2)) which is a fundamental object in LQG. An intertwinner
is a vector|ιj1..jN⟩ =∑
micm1..mN|j1m1,..,j NmN⟩∈ Vj1⊗..⊗VjN which is invariant under the action ofUq(su(2)).
Jα⊿|ιj1..jN⟩ = [(1⊗..1⊗ ∆)◦..◦ (1⊗ ∆)◦ ∆] (Jα)|ιj1..jN⟩ = 0, α=±,z. (14)
Note that since the coproduct is co-associative, we have no issue on how to compose the coproducts. In the case of
N = 3, (14) is equivalent to the recursion relations which deﬁne the CG coeﬃcients. A normalized 3-valent intertwiner
is then uniquely deﬁned by
|ιj1j2j3⟩ =
∑
mi
(−1)j3−m3q−m3
2
[2j3 + 1]
1
2
qC j1 j2 j3
m1m2−m3
|j1m1,j 2m2,j 3m3⟩.
Another ingredient which we shall use extensively in the following sections, is the adjoint action of Uq(su(2)) on an
operatorO. It diﬀers from the usual adjoint action of su(2) given by a commutator. The Uq(su(2)) adjoint action of
the generators Jσ is explicitly given by
Jz⊿O = [Jz,O], J ±⊿O =J±Oq−Jz/2−q± 1
2q−Jz/2OJ±. (15)
The following lemma is useful to relate quantities which are invariant under the adjoint action and the diﬀerent
Casimir one can construct. This is especially relevant in our case since the commutator and the adjoint action are
not coinciding.
Lemma I.1. LetC∈U q(su(2)) invariant under the adjoint action, then C commutes with the generators Jσ, σ =
+,−,z . Conversely, if C∈U q(su(2)) commutes with Jσ, then it is invariant under the adjoint action.
7
B. q-harmonic oscillators and the Schwinger-Jordan trick
To account for the deformation, we consider a pair of q-harmonic oscillators, comprising annihilation operators
αi = a,b , creation operators α†
i = a†,b† and number operators Nαi = Na,Nb, to construct representations of
Uq(su(2)). There are deﬁned as follows,
[αi,αj] = [αi,α†
j] = 0, with i⁄=j, [αi,α†
i]q± 1
2
=q
∓Nαi
2 , [Nαi,α†
j] =δijα†
i, [Nαi,αj] =−δijαi, (16)
where [A,B ]qn≡AB−qnBA. Let us point out that the operator α†
iαi is not the number operator Nαi but rather is
equal to [Nαi]. From (16), we have also that
qNαi/2α†
i =q1/2α†
iqNαi/2, q Nαi/2αi =q−1/2αiqNαi/2, α †
iαi = [Nαi], α iα†
i = [Nαi + 1]. (17)
The harmonic oscillator αi, α†
i, Nαi acts on the Fock space Fi ={∑
nicni|ni⟩} with vacuum|0⟩.
αi|0⟩ = 0, α i|ni⟩ =
√
[ni]|ni− 1⟩, with ni≥ 1, and α†
i|ni⟩ =
√
[ni + 1]|ni + 1⟩. (18)
The generators of Uq(su(2)) can be realized in terms of the pair of q-harmonic oscillators (a,b ), their adjoint and
their number operator [42, 43].
Jz = 1
2(Na−Nb), J + =a†b, J − =b†a, C = [1
2(Na +Nb)][1
2(Na +Nb) + 1]. (19)
Using this representation together with (16), we can recover the commutation relations (1). We can also use the Fock
spaceF∼Fa⊗Fb ={∑cnanb|na,nb⟩, cnanb∈ R} of this pair ofq-harmonic oscillators to generate the representations
ofUq(su(2)) by setting
j = 1
2(na +nb), m = 1
2(na−nb). (20)
The states|jm⟩ are then homogenous polynomials in the operators αi, α†
i.
|jm⟩ =
(
a†)j+m(
b†)j−m
√
[j +m]![j−m]!
|0, 0⟩. (21)
II. TENSOR OPERATORS FOR Uq(su(2))
We now introduce the concept of tensor operators. The general deﬁnition of tensor operators for a general quasitri-
angular Hopf algebra has been given in [34]. We use their formalism in the speciﬁc case of Uq(su(2)). These objects
are the building blocks of our construction of observables for LQG deﬁned with Uq(su(2)) as gauge group. We show
in section IV that the use of tensor operators allows us to build any observables associated to an intertwiner (of a
quantum or a classical group) in a straightforward manner.
A. Deﬁnition and Wigner-Eckart theorem
Deﬁnition II.1. Tensor operators [34].
LetV andW be two representations ofUq(su(2)), not necessarily irreducible, and L(W ) the set of linear maps on W .
A tensor operator t is deﬁned as the intertwinning linear map
t :V → L(W )
x → t(x) (22)
If we take V ≡ Vj the irreducible representation of rank j spanned by vectors |j,m⟩, then we note t(|j,m⟩)≡ tj
m.
tj =
(
tj
m
)
m=−j..j is called a tensor operator of rank j.
8
A tensor operator being an intertwining map for the action of Uq(su(2)) means that tj
m transforms at the same
time as an operator under the adjoint action of Uq(su(2)) and as a vector |jm⟩. This is encoded in the equivariance
property2
Jz⊿ tj
m = [Jz, tj
m] =m tj
m (23)
J±⊿ tj
m = J± tj
m q−Jz
2 −q± 1
2q−Jz
2 tj
m J± =
√
[j∓m][j±m + 1] tj
m±1.
This equivariance property has a very important consequence regarding the matrix elements of tj
m.
Theorem II.2. Wigner-Eckart theorem [34]:
The matrix elements⟨j1,m 1|tj
m|j2,m 2⟩ are proportional to the CG coeﬃcients. The constant of proportionality Nj
j1j2
is a function of j1, j2 and j only.
⟨j1,m 1|tj
m|j2,m 2⟩ =Nj
j1j2 qC j j2 j1
mm2m1
. (24)
The proof of the theorem follows from the constraints (23) written for the matrix elements of the tensor operator.
These constraints essentially implement the recurrence relations which deﬁne the CG coeﬃcients, as given in (13).
In order to have at least a non-zero matrix element, the j’s in the CG coeﬃcients must satisfy the triangular
condition. This means in particular that the tensor operator does not have to be realized as a square matrix. Let us
consider the cases j = 0, 1
2, 1.
• The scalar operator t0 has matrix elements given in terms of qC 0j2 j1
0m2m1
. As a consequence, we must have
j1 =j2 and the scalar operator must be encoded in a square matrix (2 j1 + 1)× (2j1 + 1).
• The spinor operator t
1
2 matrix elements are given in terms of qC
1
2 j2 j1
mm2m1
. We must have j2 + 1
2 = j1 or
j2− 1
2 =j1. The spinor operator cannot be realized by a square matrix. It has to be represented in terms of a
rectangular matrix of either of the type (2 j2 + 2)× (2j2 + 1), (2j2)× (2j2 + 1) or a direct sum of the two.
• In a similar way, the vector operator t1 has matrix elements given by qC 1 j2 j1
mm2m1
. Hence it must be realized
as a matrix of the either of the types (2 j2− 1)× (2j2 + 1), (2j2 + 1)× (2j2 + 1), (2j2 + 3)× (2j2 + 1) or a direct
sum of some/all of them.
