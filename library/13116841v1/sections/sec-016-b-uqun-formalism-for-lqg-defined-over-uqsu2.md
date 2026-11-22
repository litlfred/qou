---
doc_id: 13116841v1
doc_title: "Observables in Loop Quantum Gravity with a cosmological constant"
section_id: sec-016-b-uqun-formalism-for-lqg-defined-over-uqsu2
section_title: "B Uq(u(n)) formalism for LQG defined over Uq(su(2))"
section_number: null
pages: 18-20
source_pdf: 1311.6841v1.pdf
source_sha256: ca65879d80b1e1c3
toc_source: outline
doc_brief: "Observables in Loop Quantum Gravity with a cosmological constant — 22 sections: Front matter; Contents; Introduction"
---
We want to construct the ”smallest” observables. It is therefore natural to consider the observables built from
the scalar product of spinor operators (47). Since we have two types of spinor operators, we have diﬀerent possible
combinations.
Eαβ ≡−(α)T
1
2 ·(β) ˜T
1
2 ,
G†
αβ ≡−(α)T
1
2 ·(β) T
1
2
Fαβ ≡−(α) ˜T
1
2 ·(β) ˜T
1
2 .
(82)
Note that since the operators on diﬀerent legs do not commute, we could a priori choose a diﬀerent order of T and ˜T
in the deﬁnition of Eαβ. One can show however that choosing the order leads to the same operator modulo a constant
factor. This factor comes from the (deformed) symmetry of the scalar product as well as the commutation relations
between the spinor operators acting on diﬀerent legs.
Let us focus on the operators Eαβ. Consider ﬁrst the spinor operators which act on the same leg α = β = i.
Eii := −(i)T
1
2 · (i) ˜T
1
2 = −q
1
4 A†
i ˜
Ai + q−1
4 B†
i ˜Bi.
(83)
Having in mind Lemma II.5, we can forget about the tensor product, and the only relevant action is on the leg i so
Eii|ιj1...jN ⟩= [2ji]|ιj1...jN ⟩.
(84)
Consider now the spinor operators which act on diﬀerent legs i and j.
Eij = A†
iCj + B†
i Dj.
(85)
The action of E12 = A†
1C2 + B†
1D2 on a trivalent intertwiner is given by
E12|ιj1j2j3⟩= −˜N
1
2
j2N
1
2
j1(−1)j1+j2+j3−1q−3
4 j1p
[2j1 + 2][2j2]
(
j2 −1
2
1
2
j2
j1
j3 j1 + 1
2
)
|ij1+ 1
2 j2−1
2 j3⟩
(86)
with the normalization choice
N
1
2
j = [dj]
1
2 q
j
2 ,
˜N
1
2
j = [dj]
1
2 q
j
2 −1
4 .
The other operators Eij (i, j ∈{1, 2, 3}) can be constructed using the tricks described in the previous section. In a
similar way, we get
q
3
4 F12|ij1j2j3⟩= −˜N
1
2
j2 ˜N
1
2
j1(−1)j1+j2+j3q
1
2 (j2+1)p
[2j1][2j2]
(
j2 −1
2
1
2
j2
j1
j3 j1 −1
2
)
|ij1−1
2 j2−1
2 j3⟩
q
1
4 G†
12|ij1j2j3⟩= −N
1
2
j2N
1
2
j1(−1)j1+j2+j3q−1
2 (j1+ 3
4 )p
[2j1 + 2][2j2 + 2]
(
j2 + 1
2
1
2
j2
j1
j3 j1 + 1
2
)
|ij1+ 1
2 j2+ 1
2 j3⟩
(87)
When we perform the limit q →1, the operators A†
i, B†
i , Ci, Di become respectively a†
i, b†
i, ai and bi, that is
the standard harmonic oscillators operators. Hence in this limit, the operators Eij become a†
iaj + b†
ibj which are
the generators Eij of a u(n) Lie algebra, written using the Schwinger-Jordan representation. In a similar way, the
operators Fij, Gij become respectively Fij and F †
ij deﬁned as follows
G†
ij
q→1
→a†
ib†
j −b†
ia†
j =F †
ij,
Fij
q→1
→aibj −biaj =Fij.
(88)
We recognize the operators E, F, F † which are the basis of the U(N) formalism [27–29]. They appear very naturally
in our framework.
It is then natural to demand if the operators Eij are the generators Uq(u(n)). First, let us recall the deﬁnition of
Uq(u(n)) Cartan Weyl generators [37]. We have respectively the raising, diagonal, lowering operators Eii+1, Ei, Ei−1i,
with the following commutation relations
[Eii, Ejj] = 0,
[Eii, Ejj+1] = (δij −δij+1)Ejj+1,
[Eii, Ej−1j] = (δij+1 −δij)Ej−1j,
[Eii+1, Ej−1j] = δij(Ei −Ei+1).
The other generators are constructed by induction.
Eij = q
1
2 Ej−1 
Eij−1Ej−1j −q
1
2 Ej−1,jEij−1

,
j > i + 1
(89)
Eji = q−1
2 Ej−1 
Ejj−1Ej−1i −q−1
2 Ej−1,iEjj−1

,
j > i + 1.
(90)
Note that Eij is not necessarily the adjoint of Eji due to the presence of q. The coproduct is deﬁned as follows
∆Ei = Ei ⊗1 + 1 ⊗Ei,
∆Eii+1 = Eii+1 ⊗qEi+Ei+1 + qEi+Ei+1 ⊗Eii+1,
.
(91)
The coproduct for the other generators are obtained by induction.
The Schwinger-Jordan map allows to express these generators in terms of N q-harmonic oscillators ai.
Eij = aia†
j,
Ei = 1
2(Ni −Ni+1)
(92)
To have the representation of these generators in terms of N pairs of q-harmonic oscillators (ai, bi), we use the
coproduct:
Eii := Nai + Nbi,
(93)
Ei,i+p := a†
iai+p q
Nbi +2(Pp−1
l=1 Nbi+l )−Nbi+p
4
+ q
−Nai +2(Pp−1
l=1 Nai+l )+Nai+p
4
b†
ibi+p
+(q−1
4 −q
3
4 )
p−1
X
k=1
 
q
Nai+k +2(Pp−1
l=k+1 Nai+l )+Nai+p
4
a†
iai+k q
Nbi +2(Pk−1
l=1 Nbi+l )+Nbi+k
4
b†
i+kbi+p
!
,
(94)
Ei+p,i := aia†
i+p q
Nbi −2(Pp−1
l=1 Nbi+l )−Nbi+p
4
+ q
−Nai −2(Pp−1
l=1 Nai+l )+Nai+p
4
bib†
i+p
+(q
1
4 −q−3
4 )
p−1
X
k=1
 
q
−Nai −2(Pk−1
l=1 Nai+l )−Nai+k
4
a†
i+pai+k q
−Nbi+k −2(Pp−1
l=k+1 Nbi+l )−Nbi+p
4
b†
i+kbi
!
. (95)
Using the deﬁnition of the Eij in terms of the q-harmonic oscillators (ai, bi) deduced from the expression of the spinor
operators, we can identify a non linear relationship between these Eij and the Eij.
Eii = q−1
2 q
Eii
2 [Eii],
Ei,i+1 = q
Ei+1,i+1
4
Ei,i+1,
Ei+1,i = q
Eii
2 Ei+1,i q
Ei+1,i+1
4
,
Ei,i+p = q
−Pp−1
l=1 Ei+l,i+l+Ei+p,i+p
4
Ei,i+p,
Ei+p,i = q
2Eii+Pp−1
l=1 Ei+l,i+l
4
Ei+p,i q
Ei+p,i+p
4
.
(96)
To have a non-linear redeﬁnition of the generators is something common when dealing with quantum groups. For
example, there exists diﬀerent realizations of Uq(su(2)), all related with a non-linear redeﬁnition of the generators [45].
Biedenharn recalls also diﬀerent deﬁnitions of the generators of Uq(u(n)) related by nonlinear transformations in [37].
For some choice of generators, the commutation relation might take a simpler shape but the coproduct would be more
complicated, and vice-versa. The key point is here that we have found that the intertwiner carries a representation
of Uq(u(n)), and this generalizes the results of [27, 29].
In the classical case, when q = 1, it was shown that the intertwiner carries an irreducible u(n) representation [28].
We can wonder whether a similar result also holds here. The answer is positive. A cumbersome proof can probably
be obtained by looking at the Casimirs of Uq(u(n)). We do not want to follow this route. Instead we would like to
recall the seminal results by Jimbo, Rosso and Lustzig [46–48] which essentially state that all the ﬁnite dimensional
representations of the deformation Uq(g) of the enveloping algebra U(g), where g is any complex simple Lie algebra,
are completely reducible. The irreducible representations can be classiﬁed in terms of highest weights and in particular
they are deformations of the irreducible representations of U(g), when q is not root of unity. We can extend this
result to the semi-simple case and to Uq(u(n)) in particular (see Section 2.5 of [37] for example). Now we know
that when q = 1, the intertwiner is an irreducible representation of u(n), hence by deforming the enveloping algebra,
the representation of Uq(u(n)) carried by the Uq(su(2)) intertwiner must stay an irreducible representation. As a
consequence, the Uq(su(2)) intertwiner must carry an irreducible representation of Uq(u(n)), just as in the classical
case.
Finally, we can discuss the hermiticity property of the scalar operators we have constructed. Indeed, we expect an
observable to be self-adjoint. The operators Eij are not self-adjoint, but this should not come as a surprise. Indeed
the classical operators Eij are not hermitian either. However, the adjoint (Eij)† = Eji is still a generator. This means
that we can do a linear change of basis Eij →Eij + (Eij)† in the u(n) basis to construct self-adjoint generators.
This is actually how the formalism was initially introduced in [27]. The Cartan Weyl generators Eij when expressed
in terms of the harmonic oscillators satisfy a similar property, namely E†
ij = Eji [37]. As a consequence, from the
Eij, we can do a (non-linear) change of basis and construct the relevant hermitian Uq(u(n)) generators which will be
Uq(su(2)) invariant, using the maps (96).
V.
