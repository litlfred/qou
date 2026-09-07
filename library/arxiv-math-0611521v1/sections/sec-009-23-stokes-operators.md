---
doc_id: arxiv-math-0611521v1
doc_title: "THE q-ANALOGUE OF THE WILD FUNDAMENTAL GROUP"
section_id: sec-009-23-stokes-operators
section_title: "Stokes operators"
section_number: 2.3
pages: 12-14
source_pdf: 0611521v1.pdf
source_sha256: 65fcd77b7b0a208e
doc_brief: "THE q-ANALOGUE OF THE WILD FUNDAMENTAL GROUP — We describe an explicit construction of galoisian Stokes op erators for irregular linear q-difference equations."
---
Algebraic summation. The following computations are extracted from [28]. We needthe following theta
function of Jacobi: θq(z) = ∑ n∈Z q−n(n+1)/2zn. It is holomorphic in C∗ with simple zeroes, all located on the
discrete q-spiral [−1;q]. It satisﬁes the functional equation: σqθq = zθq. We then deﬁne θq,c(z) = θq(z/c)
(for c∈ C∗); it is holomorphic in C∗ with simple zeroes, all located on the discrete q-spiral [−c;q] and
satisﬁes the functional equation: σqθq,c = z
c θq,c.
For a given formal class described byA0, µ1, . . . ,µk and r1, . . . ,rk as above, and for anyc∈ C∗, we introduce
the matrix Tc,A0∈ Matn(M (C∗)) which is block-diagonal with blocks θ−µi
c Iri. Moreover, we shall assume
the following normalisation due to Birkhoff and Guenther (see [21], [28]):
∀i < j , all coefﬁcients of Ui,j belong to ∑
µi≤d<µ j
Czd.
Then, putting A′
i = cµiAi∈ GLri (C) and U′
i,j = (z/c)−µiθ
µ j−µi
c Ui,j∈ Matri,r j (O(C∗)), we have:
A′
U′ =
de f
Tc,A0[AU ] =


A′
1 . . . . . . . . . . . .
. . . . . . . . .U′
i,j . . .
0 . . . . . . . . . . . .
. . . 0 . . . . . . . . .
0 . . . 0 . . . A′
k


.
Now, if the images in Eq of the spectra Sp(A′
i) are pairwise disjoint, there is a unique F′∈ G(O(C∗)) such
that F′[A′
0] = A′
U′. Its coefﬁcients are recursively deﬁned by the equations:
σqF′
i,jA′
j− A′
iF′
i,j = ∑
i<k< j
U′
i,kF′
k,j +U′
i,j.
The unique solution of this equation in O(C∗) is obtained by taking the Laurent series:
F′
i,j = ∑
p∈Z
Φ−1
qpA′
j,A′
i
(Vp)zp,
(
∑
p∈Z
Vp zp = ∑
i<k< j
U′
i,kF′
k,j +U′
i,j
)
,
where one writes Φ B,C(M) = MB−CM (that map is one to one if and only if Sp(B)∩ Sp(C) = /0). Note for
further use that the condition we have to impose on the spectra is the following:
(4) ∀i < j ,qZcµiSp(Ai)∩ qZcµ jSp(A j) = /0.
12
This is equivalent to requiring that c⁄∈ΣA0, where ΣA0 is some explicit ﬁnite subset of Eq.
¿From the equalities A′
U′ = Tc,A0[AU ], A′
0 = Tc,A0[A0] and F′[A′
0] = A′
U′, we get at last F[A0] = AU, where
F = T−1
c,A0F′Tc,A0 can be easily computed: it belongs to G(M (C∗)) and Fi,j = θ
µi−µ j
c F′
i,j. The condition that
the F′
i,j are holomorphic over C∗ is equivalent to the following condition:
(5) ∀i < j ,Fi,j has poles only on [−c;q], and with multiplicities≤ µ j− µi.
Then, we get the following conclusion: there is a unique F∈ G(M (C∗)) such that condition (5) holds and
F[A0] = AU. Note that the condition depends on c∈ Eq rather than c. To summarize the discussion:
Proposition 2.5 For every c∈ C∗ satisfying condition (4) (i.e., c⁄∈ΣA0), there is a unique F∈ G(M (C∗))
satisfying condition (5) and such that F [A0] = AU. We consider this F as obtained by summation of ˆFA in
the direction c∈ Eq and, accordingly, write it Sc ˆFA.
If we now choose two q-directions of summation c,d∈ Eq, the ambiguity of summation is expressed by:
(6) Sc,d ˆFA =
de f
(Sc ˆFA)−1Sd ˆFA.
This is a meromorphic automorphism of A0. As explained in [21] and [28], it is a Stokes operator.
Case of one level. For further use, we now specialize some of the previous resul ts to the case of two
(integral) slopes µ < ν, and only one “level” δ = ν− µ∈ N∗. For simplicity, we write our matrices:
(7) M0 =
(
zµA 0
0 zνB
)
and M =
(
zµA z µUB
0 zνB
)
,
where A∈ GLr(C), B∈ GLs(C) and U∈ Matr,s(Cδ−1[z]) (polynomials with degree < δ). It is clear that the
upper right block can indeed be written in such a way. Then the unique element of G(C((z))) which sends
M0 to M is the matrix
( Ir F
0 Is
)
, where F is the unique element of Matr,s(C((z))) such that:
(8) zδσqF− Λ(F) = U,
Here, we have writtenΛ(F) = AFB−1 (thus, an endomorphism of Matr,s(C) and similar spaces). The formal
solution F can be computed by identiﬁcation of coefﬁcients, i.e. by solving:
(9) ∀n∈ Z ,qn−δFn−δ− AFnB−1 = Un.
Similarly, the unique element ofG(M (C∗)) such that condition (5) holds which sendsM0 to M is the matrix( Ir F
0 Is
)
, where F is the unique of Mat r,s(M (C∗)) with poles only on [−c;q] and with multiplicities≤ d
which is solution of equation (8). This is solved by putting F = θ−δ
c G, so that G is a solution holomorphic
on C∗ of the following equation:
(10) cδσqG− Λ(G) = V, where G = θδ
cF and V = θδ
cU.
This can be solved by identiﬁcation of coefﬁcients of the corresponding Laurent series, i.e. by solving:
(11) ∀n∈ Z ,cδqnGn− AGnB−1 = Vn.
This is possible if cδqZ∩ Sp(A)/Sp(B) = /0, which is precisely condition (4) specialized to the presen t
setting. Then we can take Gn = (cδqnId− Λ)−1Vn.
13
