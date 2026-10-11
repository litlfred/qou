---
doc_id: arxiv-0903.0853v3
doc_title: "Jean-Pierre Ramis"
section_id: sec-023-63-matricial-description
section_title: "Matricial description"
section_number: 6.3
pages: 32-38
source_pdf: 0903.0853v3.pdf
source_sha256: d4295d4b18b2f08f
toc_source: inferred
---
description, valid without any restriction on the slopes (number or integrity).
Details can be found in appendix A. From the theorem 2.2.4, we deduce that
each analytic q-diﬀerence module M with S(M) = {µ1, . . . , µk}, these slopes
being indexed in increasing order: µ1 < · · · < µk and having multiplicities
r1, . . . , rk ∈N∗, can be written M = (C({z})n, ΦA) with:
(2.2)
A = AU :=







B1
. . .
. . .
. . .
. . .
. . .
. . .
. . .
Ui,j
. . .
0
. . .
. . .
. . .
. . .
. . .
0
. . .
. . .
. . .
0
. . .
0
. . .
Bk







,
where, for 1 ≤i ≤k, Bi ∈GLri(C({z})) encodes a pure isoclinic mod-
ule Pi = (Kri, ΦBi) of slope µi and rank ri and where, for 1 ≤i <
j ≤k, Ui,j ∈Matri,rj(C({z})).
Here, U stands short for (Ui,j)1≤i<j≤k ∈
Q
1≤i<j≤k
Matri,rj(C({z})).
Call MU = M the module thus deﬁned:
it is
implicitly endowed with an isomorphism from grMU to M0 := P1 ⊕· · · ⊕Pk,
here identiﬁed with (Kn, ΦA0). If moreover the slopes are integral: S(M) ⊂Z,
then one may take, for 1 ≤i ≤k, Bi = zµiAi, where Ai ∈GLri(C).
Now, a morphism from MU to MV compatible with the graduation (as in
deﬁnition 2.3.1) is a matrix:
(2.3)
F :=







Ir1
. . .
. . .
. . .
. . .
. . .
. . .
. . .
Fi,j
. . .
0
. . .
. . .
. . .
. . .
. . .
0
. . .
. . .
. . .
0
. . .
0
. . .
Irk







, with (Fi,j)1≤i<j≤k ∈
Y
1≤i<j≤k
Matri,rj(C({z})),
such that (σqF)AU = BUF. The corresponding relations for the Fi,j, Ui,j, Vi,j
will be detailed in subsection 3.3.2. Here, we just note that the above form of
F characterizes a unipotent algebraic subgroup G of GLn, which is completely
determined by the Newton polygon of M0. The condition of equivalence of
MU and MV reads:
MU ∼MV ⇐⇒∃F ∈G(C({z})) : F[AU] = AV .
2.3. APPLICATION TO THE ANALYTIC ISOFORMAL CLASSIFICATION
27
The set of classes F(P1, . . . , Pk) may therefore be identiﬁed with the quotient
of
Q
1≤i<j≤k
Matri,rj(C({z})) by that equivalence relation, i.e. by the action of
G(C({z})).
For a more formal description, we introduce the block-diagonal part of A,
i.e. the matrix A0 corresponding to the pure module M0:
(2.4)
A0 :=







B1
. . .
. . .
. . .
. . .
. . .
. . .
. . .
0
. . .
0
. . .
. . .
. . .
. . .
. . .
0
. . .
. . .
. . .
0
. . .
0
. . .
Bk







,
along with the following set:
GA0(C((z))) := { ˆF ∈G(C((z))) | ˆF[A0] ∈GLn(C({z}))}.
If ˆF ∈GA0(C((z))) and F ∈G(C({z})), then (F ˆF)[A0] = F
 ˆF[A0]

∈
GLn(C({z})), so that F ˆF ∈GA0(C((z))): therefore, the group G(C({z}))
operates on the set GA0(C((z))).
Proposition 2.3.11. — The map ˆF 7→ˆF[A0] induces a one-to-one corre-
spondance:
GA0(C((z)))/G(C({z})) →F(P1, . . . , Pk).
Proof. — From the formal case in 2.2.3, it follows that, for any U
∈
Q
1≤i<j≤k
Matri,rj(C({z})) there exists a unique ˆF
∈G(C((z))) such that
ˆF[A0] = AU. The equivalence of ˆF[A0] with ˆF ′[A0] is then just the relation
ˆF ′ ˆF −1 ∈G(C({z})).
Remark 2.3.12. — Write ˆFU for the ˆF in the above proof. More generally,
for any U, V ∈
Q
1≤i<j≤k
Matri,rj(C({z})) there exists a unique ˆF ∈G(C((z)))
such that ˆF[AU] = AV ; write it ˆFU,V . Then ˆFU,V = ˆFV ˆF −1
U
and the condition
of equivalence of MU and MV reads:
MU ∼MV ⇐⇒ˆFU,V ∈G(C({z})).
Giving analyticity conditions for a formal object strongly hints towards a
resummation problem! (See chapters 4 and 5.)
CHAPTER 3
THE AFFINE SPACE OF ISOFORMAL
ANALYTIC CLASSES
3.1. Isoformal analytic classes of analytic q-diﬀerence modules
We shall now specialize the results of the appendix A, in particular its
section A.7, to the case of q-diﬀerence modules (1).
3.1.1. Extension classes of analytic q-diﬀerence modules. — From
here on, we consider only analytic q-diﬀerence modules and the base ﬁeld is
C({z}) (except for brief indications about the formal case).
Theorem 3.1.1. — Let M, N be pure modules of ranks r, s ∈N∗and slopes
µ < ν ∈Q. Then dimC F(M, N) = rs(ν −µ).
Proof. — Since F(M, N) ≃Ext1(N, M) ≃Γ1(N ∨⊗M) (proposition 2.1.3)
and since N ∨⊗M is pure isoclinic of rank rs and slope µ−ν < 0, the theorem
is an immediate consequence of the following lemma.
Lemma 3.1.2. — Let M be a pure module of ranks r and slope µ < 0. Then
dimC Γ1(M) = −rµ.
Proof. — We give four diﬀerent proofs, of which two require that µ ∈Z.
1) Write d := −rµ ∈N∗. If M = Dq/DqP, the module M∨is pure of
rank r and slope −µ, and can be written as Dq/DqP ∨for some dual P ∨=
a0 + · · · + arσr
q of P, such that v0(a0) = 0, v0(ar) = d and v0(ai) ≥id/r for
all i (lemma 2.2.3). We want to apply proposition 2.5 of [7], but the latter
assumes |q| < 1, so we consider L := P ∨σ−r
q
= b0 + · · · + brσr, where σ := σ−1
q
and bi := ar−i. After loc.cit, the operator L : C{z} →C{z} has index d.
1. Reading the appendix is not a prerequisite to reading that chapter, except for some
particular explicit references.
30
CHAPTER 3. THE AFFINE SPACE OF ISOFORMAL ANALYTIC CLASSES
More generally, for all m ∈N∗, the operator L : z−mC{z} →z−mC{z} is
conjugate to zmLz−m = P qimbiσi : C{z} →C{z}, which also has index d.
Hence L : C({z}) →C({z}) has index d, and so has P ∨. After corollary
A.7.5, this index is dimC Γ1(M) −dimC Γ(M). But, M being pure isoclinic of
non null slope, Γ(M) = 0, which ends the ﬁrst proof.
2) In the following proof, we assume µ ∈Z. From theorem 1.2.3 of [48], we
know that we may choose the dual operator such that:
P ∨= (z−µσq −c1)u1 · · · (z−µσq −cr)ur,
where c1, . . . , cr ∈C∗and u1, . . . , ur ∈C{z}, u1(0) = · · · = ur(0) = 1. We
are thus left to prove that each z−µσq −c1 has index −µ: the indexes add up
and the sum will be −rµ = d. Since the kernels are trivial, we must compute
the cokernel of an operator zmσq −c, m ∈N∗. But it follows from lemma
3.1.3 that the image of zmσq −c : C({z}) →C({z}) admits the supplementary
space C ⊕· · · ⊕Czm−1.
3) In the following proof, we assume again µ ∈Z. After lemma 2.2.3, we
can write M = (C({z})r, ΦzµA), A ∈GLr(C). After corollary A.7.3, we must
consider the cokernel of C({z})r ΦzµA−Id
−→
C({z})r. But, after lemma 3.1.3, the
image of ΦzµA −Id admits the supplementary space (C ⊕· · · ⊕Cz−µ−1)r.
4) A similar proof, but for arbitrary µ, can be deduced from [56]. It follows
indeed from this paper that each isoclinic module of slope µ can be obtained by
successive extensions of modules admitting a dual of the form Dq/Dq(zaσb
q−c),
where b/a = −µ and c ∈C∗.
Lemma 3.1.3. — Let d, r ∈N∗and A ∈GLr(C). Let D ⊂Z be any set of
representatives modulo d, for instance {a, a+1, . . . , a+d−1} for some a ∈Z.
Then, the image of the C-linear map F : X 7→zdAσqX −X from C({z})r to
itself admits as a supplementary
 P
i∈D
Czi
r
.
Proof. — For all i ∈Z, write Ki := ziC({zd}), so that C({z}) = L
i∈D Ki.
Each of the Kr
i is stable under F. We write w := zd, L := C({w}), ρ := qd
and deﬁne σ on L by σf(w) = f(ρw). Multiplication by zi sends Lr to Kr
i and
conjugates the restriction of F to Kr
i to the mapping Gi : Y 7→wqiAσY −Y
from Lr to itself. We are left to check that the image of Gi admits Cr as a
supplementary. But this is just the case d = 1, D = {0} of the lemma. So we
tackle this case under these assumptions with the notations of the lemma.
So write FA : X 7→zAσqX −X from C({z})r to itself.
Also write
X = P Xnzn and Y
= FA(X) = P Ynzn (all sums here have at most
3.1. ISOFORMAL ANALYTIC CLASSES OF ANALYTIC q-DIFFERENCE MODULES 31
a ﬁnite number of negative indices), so that Yn
= qn−1AXn−1 −Xn.
Putting
˜X
:=
P A−nXnzn and
˜Y
:=
P A−nYnzn, from the relation
A−nYn = qn−1A−(n−1)Xn−1 −A−nXn, we draw ˜Y
= zσq ˜X −X.
Of
course, X 7→˜X is an automorphism of C({z})r and we just saw that it con-
jugates FA to the map F : X 7→zσqX −X from C({z})r to itself. Moreover,
the same automorphism leaves invariant the subspace Cr ⊂C({z})r, so the
question boils down to prove that the image of F has supplementary Cr. And
this, in turn, splits into r times the same problem for r = 1.
So we are left with the case of the map Ψ : f 7→zσqf −f from C({z}) to
itself, which is the very heart of the theory ! (See for instance example 3.3.2
page 38 and section 7.1 of chapter 7.) This case has been studied in detail
in paragraph 2.3.1. We saw there that Ψ is injective and that its image is in
direct sum with C ⊂C({z}). More precisely, for any u ∈C({z}), the unique
u0 ∈C such that u −u0 ∈Im Ψ is u0 := Bq,1 u(1) (the q-Borel transform
Bq,1 u was deﬁned in paragraph 2.3.1). This achieves the proof.
Note that from the proof, one draws explicit projection maps from C({z})r
to the image of FA and its supplementary Cr: these are the maps Y 7→
Y −Bq,1Y (A−1) and Y 7→Bq,1Y (A−1), where:
Bq,1Y (A−1) :=
X
q−n(n−1)/2A−nYn.
3.1.2. The aﬃne scheme F(P1, . . . , Pk). — Now let P1, . . . , Pk be pure
isoclinic q-diﬀerence modules over C({z}), of ranks r1, . . . , rk ∈N∗and slopes
µ1 < · · · < µk. From section A.6 of the appendix A, we have a functor from
commutative C-algebras to sets:
C ❀F(C) := F(C ⊗C P1, . . . , C ⊗C Pk).
Here, the base change C ⊗C−means that we extend the scalars of q-diﬀerence
modules from C({z}) to C ⊗C C({z}).
Theorem 3.1.4. — The functor F is representable and the corresponding
aﬃne scheme is an aﬃne space over C with dimension:
dim F(P1, . . . , Pk) =
X
1≤i<j≤k
rirj(µj −µi).
Proof. — We apply theorem A.6.1. We need two check the assumptions:
∀i, j,
s.t. 1 ≤i < j ≤k , Hom(Pj, Pi) = 0 and
dimC Ext(Pj, Pi) = rirj(µj−µi).
32
CHAPTER 3. THE AFFINE SPACE OF ISOFORMAL ANALYTIC CLASSES
The ﬁrst fact comes from theorem 2.2.4 and the second fact from theorem
3.1.1; the fact that the extension modules are free is here obvious since C is a
ﬁeld.
Remark 3.1.5. — The use of base changes C ⊗C C({z}) is too restrictive to
consider this as a true space of moduli, as was done for diﬀerential equations
in [3, chap. III]: we would like to consider families of modules the coeﬃcients
of which are arbitrary analytic functions of some parameter. This will be done
in [52].
Now, to get coordinates on our aﬃne scheme, we just have to ﬁnd bases of
the extension modules Ext(Pj, Pi) for 1 ≤i < j ≤k: this follows indeed from
corollary A.6.5. An example will be given by corollary 3.3.7.
