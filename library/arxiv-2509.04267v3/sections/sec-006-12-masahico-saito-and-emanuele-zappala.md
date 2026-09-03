---
doc_id: arxiv-2509.04267v3
doc_title: "QUANTUM COCYCLE INVARIANTS OF KNOTS FROM YANG-BAXTER COHOMOLOGY"
section_id: sec-006-12-masahico-saito-and-emanuele-zappala
section_title: "MASAHICO SAITO AND EMANUELE ZAPPALA"
section_number: 12
pages: 12-14
source_pdf: 2509.04267v3.pdf
source_sha256: 9843b9dd71d1ec74
doc_brief: "QUANTUM COCYCLE INVARIANTS OF KNOTS FROM YANG-BAXTER COHOMOLOGY — Yang-Baxter operators (YBOs) have been employed to construct quantum knot invari- ants."
---
fappears on internal arcs. The only terms that are potentially nonzero in Ψ 1
ϕ(bm) are therefore
those in whichfappears on external arcs.
By adding canceling pairsσiσ−1
i if necessary, we may assume that all strings cross at least another
string of the braid. Further, observe that all instances wherefappears as a top arc have positive
sign, while all instances wherefappears on a bottom arc have negative sign. Therefore, we have
X
(i,j1,...,jm)∈Γm+1
Tr(Ψϕ(bm)(µj1⊗···⊗µ jm))
= Tr(Ψ 1
ϕ(bm)(µ0⊗···⊗µ 0)) +
X
(j1,...,jm)∈Γm
Tr(Ψ0
ϕ(bm)(µj1⊗···⊗µ jm))
=
mX
i=1
Tr[Ψ0
ϕ(bm)(µ⊗(i−1)
0 ⊗fµ 0⊗µ⊗(m−i−1)
0 )−(1 ⊗(i−1)⊗f⊗1 ⊗(m−i−1))Ψ0
ϕ(bm)(µ0⊗···⊗µ 0)]
+
mX
i=1
Tr(Ψ0
ϕ(bm)(µ⊗(i−1)
0 ⊗µ 1⊗µ⊗(m−i−1)
0 ))
(A)
=
mX
i=1
Tr[Ψ0
ϕ(bm)(µ⊗(i−1)
0 ⊗fµ 0⊗µ⊗(m−i−1)
0 )−Ψ 0
ϕ(bm)(µ⊗(i−1)
0 ⊗µ 0f⊗µ ⊗(m−i−1)
0 )]
+
mX
i=1
Tr(Ψ0
ϕ(bm)(µ⊗(i−1)
0 ⊗µ 1⊗µ⊗(m−i−1)
0 ))
=−
mX
i=1
Tr(Ψ0
ϕ(bm)(µ⊗(i−1)
0 ⊗µ 1⊗µ⊗(m−i−1)
0 )) +
mX
i=1
Tr(Ψ0
ϕ(bm)(µ⊗(i−1)
0 ⊗µ 1⊗µ⊗(m−i−1)
0 ))
= 0
where the equality (A) follows from the cyclic property of the partial trace.□
5.Examples via traces
In this section we provide examples that yield nontrivial values of the quantum cocycle invariant
defined in the preceding section via traces.
5.1.Invariants from deformations of the transposition.Let us consider a finite dimensional
vector spaceValong with the transposition mapR=τ:V⊗V→V⊗V, which is a YBO onV.
Lemma 5.1.ForR=τ, we haveH 2
YB(V,V) =C 2
YB(V,V) = Hom(V ⊗2,V ⊗2).
Proof.For a 2-cochainϕ, we use the structure constantsϕ(e i⊗ej) =ϕ kℓ
ijek⊗eℓ, where we employ
the usual Einstein notation for the sums of repeated indices, and we have denoted bye 1,...,e n a
basis forV. The first term in the 2-cocycle condition is
(R⊗1)(1⊗R)(ϕ⊗1)(e i⊗ej⊗ek) = (τ⊗1)(1⊗τ)(ϕ tr
ijet⊗er⊗ek)) =ϕ tr
ijek⊗et⊗er.
Similarly the 2-cocycle condition is computed as
δ2
YB(ϕ)(ei⊗ej⊗ek)
=ϕ tr
ijek⊗et⊗er +ϕtr
iket⊗ej⊗er +ϕtr
jket⊗er⊗ei
−ϕtr
jket⊗er⊗ei−ϕtr
iket⊗ej⊗er−ϕtr
ijek⊗et⊗er = 0,
QUANTUM COCYCLE INVARIANTS OF KNOTS FROM YANG-BAXTER COHOMOLOGY 13
which is satisfied. It follows that any 2-cochain is a 2-cocycle. Similarly, using the notation
f(ei) =f j
iej for a 1-cochainf:V→V, we find directly thatδ 1
YB(f) = 0. Hence we have
H2
YB(V,V) =C 2
YB(V,V).□
For the transpositionτ, Equations (1) and (2) can be checked to see thatS= (R,α,β,µ 0) =
(τ,1,1,1) is an EYBO. We consider the problem of finding enhanced 2-cocycles ofτ.
Lemma 5.2.LetV=R⟨e 0,e 1⟩be a 2-dimensional real vector space on basise 0,e 1. LetS=
(τ,1,1,1)be an EYBO as above. Let ˜S= ( ˜R,1,1,˜µ)where ˜R=τ+ℏϕand˜µ=1+ℏµ 1. Consider
the following choices forϕandµ 1:
ϕk0
i0 =−ϕ 0k
0i, ϕk1
i1 =−ϕ 1k
1i, ϕ10
01 andϕ 01
10 arbitrary,withµ 1 defined byµ k
i =−ϕ k0
i0−ϕk1
i1.(9)
Then we have that ˜S= (τ+ℏϕ,1,1,1+ℏµ 1)is an EYBO.
Proof.Let ˜µ=µ 0 +ℏµ 1 be a deformation ofµ 0, whereµ 0 =1, and writeµ 1(ei) =µ j
iej. We
need to obtain the constraints onϕandµ 1 in order to have Equation (5) to hold. The first term
in the left-hand side of Equation (5) for (0,0,1)∈Γ 2 isϕ 0(µ0⊗µ 1)(ei⊗e j), and substituting
ϕ0 =τ,µ 0 =1andµ 1(ej) =µ k
jek, we obtainµ k
jek⊗ei as the first term. Similar computations for
Equation (5) give
µk
jek⊗ei +µk
iej⊗ek +ϕkℓ
ijek⊗eℓ =ϕ kℓ
ijek⊗eℓ +µk
iej⊗ek +µk
jek⊗ei,
which once again holds identically.
For the deformation ˜S= ( ˜R,α,β,ϕ) = (τ+ℏϕ,1,1,µ 1) to give an EYBE, it is sufficient to verify
Equations (6) and (7). To evaluate Tr2, we calculate as follows. With basis{e i}, let an operatorA
defined via the tensor notationA(e i⊗ej) =P
klakl
ijek⊗el, and lete ∗
j be dual basis vectors. Then
the computation for Tr2(A) is performed as
ei7→
X
j
ei⊗ej⊗e∗
j7→
X
j
A(ei⊗ej)⊗e ∗
j7→
X
j
akl
ijek⊗el⊗e∗
j7→
X
j
akl
ijδjlek =
X
j
akj
ijek.
Hence the entryikof the matrix for Tr 2(A) isP
jakj
ij , or simplya kj
ij in Einstein convention.
We compute Tr 2τ(µ 0⊗µ 1)(ei) =µ k
iek =µ 1(ei), Tr 2τ(µ 1⊗µ 0)(ei) =µ j
iej =µ 1(ei), and
ˆϕ1 =−ϕ−1
0 ϕ1ϕ−1
0 as in Theorem 4.3. For Equations (6) we compute
Tr2τ(µ 0⊗µ 1)(ei) + Tr2τ(µ 1⊗µ 0)(ei) + Tr2ϕ(µ0⊗µ 0)(ei) =µ 1(ei),
hence we obtainϕ kj
ij =−µ k
i . Similarly for Equations (7) we obtainϕ jk
ji =µ k
i . Then it is checked
that the stated Solution (9) indeed satisfies these equations, due to the symmetryϕ iℓ
ik =−ϕ ℓi
ki,
which uniquely fixesµ 1, and the fact thatϕ 10
01 andϕ 01
10 do not appear in the equations for the
partial trace. □
Letσ 1 denote the standard generator of the 2-strand braid groupB 2, and letT n be the closure
ofσ n
1 for s positive integern. Forn= 2,3,T n is a Hopf link and trefoil knot, respectively.
Proposition 5.3.Consider the special case of Solution(9)in Lemma 5.2:
ϕ01
01 =−ϕ 10
10 =ϕ 11
01 =−ϕ 11
10 = 1, ϕ10
01 =ϕ 01
10 =q,
andϕ kℓ
ij = 0otherwise, whereqis an arbitrary real number, along withµ 0
0 =µ 1
0 =−µ 1
1 = 1,µ 0
1 = 0.
For the knots and linksT n and the YB 2-cocycleϕin this solution, we have the following values.
Φϕ(Tn) =
(
4 + 2nqℏn= 2k
2n= 2k+ 1
