---
doc_id: arxiv-2509.04267v3
doc_title: "QUANTUM COCYCLE INVARIANTS OF KNOTS FROM YANG-BAXTER COHOMOLOGY"
section_id: sec-014-28-masahico-saito-and-emanuele-zappala
section_title: "MASAHICO SAITO AND EMANUELE ZAPPALA"
section_number: 28
pages: 28-30
source_pdf: 2509.04267v3.pdf
source_sha256: 9843b9dd71d1ec74
doc_brief: "QUANTUM COCYCLE INVARIANTS OF KNOTS FROM YANG-BAXTER COHOMOLOGY — Yang-Baxter operators (YBOs) have been employed to construct quantum knot invari- ants."
---
Next we show that ˜R(n) = Pn
i=0 ℏiϕi is invertible moduloℏ n for anyn. Let us set ˜R−1
(n) =
Pn
i=0 ℏi ˆϕi. The fact that ˜R−1
(n) is an inverse to ˜R(n) is equivalent to the following two systems.
ˆϕ0 =ϕ−1
0 , ..., ˆϕk =−ϕ−1
0
kX
i=1
ϕi ˆϕk−i, ..., ˆϕn =−ϕ−1
0
nX
i=1
ϕi ˆϕn−i(20)
and
ˆϕ0 =ϕ−1
0 , ..., ˆϕk =−
kX
i=1
ϕi ˆϕk−i·ϕ−1
0 , ..., ˆϕn =−
nX
i=1
ϕi ˆϕn−i·ϕ−1
0(21)
where (20) gives right-invertibility, and (21) corresponds to left invertiblity. Additionally, we need
to verify that the solutions obtained by the two systems coincide. Letϕ i1,...,ϕ ik be a list of
elements appearing in ˜ϕ, not necessarily mutually distinct. We define the symmetrized expression
(−1)nS(ϕi1|...|ϕ ik) =
X
σ∈Σk
1
q1!···q t!ϕ−1
0 ϕσ(i1)ϕ−1
0 ···ϕ −1
0 ϕσ(ik)ϕ−1
0 ,(22)
whereq 1,...,q t indicate the number of repeated indices among thei r. Then, we have for example
S(ϕ1|···|ϕ 1) =−ϕ−1
0 ϕ1ϕ−1
0 ···ϕ −1
0 ϕ1ϕ−1
0
whenϕ 1 is repeated 2n+ 1 times,
S(ϕ1|···|ϕ 1) =ϕ−1
0 ϕ1ϕ−1
0 ···ϕ −1
0 ϕ1ϕ−1
0
whenϕ 1 is repeated 2ntimes. Similarly, by a direct computation we have
S(ϕ1|ϕ1|ϕ2) =−ϕ−1
0 ϕ1ϕ−1
0 ϕ1ϕ−1
0 ϕ2ϕ−1
0 −ϕ−1
0 ϕ1ϕ−1
0 ϕ2ϕ−1
0 ϕ1ϕ−1
0 −ϕ−1
0 ϕ2ϕ−1
0 ϕ1ϕ−1
0 ϕ1ϕ−1
0
and so forth. We now show that the inverse of ˜ϕis given by
ˆϕn =
X
S(ϕi1|···|ϕ ik),(23)
where the sum is taken over all the possible choices of indicesi 1,...,i k such thati 1≤i 2≤···≤i k
and Pk
d=1id =n. We proceed by induction to show that ˆϕn chosen as in Equation (23) gives a
solution of the system of equations (21).
The casen= 0 is trivial, since ˆϕ0 =ϕ−1
0 , and casen= 1 was seen to produce ˆϕ1 =ϕ−1
0 ϕ1ϕ−1
0 ,
which coincides withS(ϕ 1), and therefore with Equation (23) since there is no sum.
Suppose now that the inverse for ˜R(n) has been determined when there arenterms, withn>1.
When we consider (21) for ˜R(n+1). The firstnequations are identical to the case of lengthn.
Therefore, they are given by Equation (23) by the inductive assumption. The (n+ 1) th equation is
given by
ˆϕn+1 =−ϕ−1
0
n+1X
i=1
ϕi ˆϕn+1−i =−ϕ−1
0
n+1X
i=1
ϕi
X
S(ϕi1|···|ϕ ik),
where the second sum is defined as in Equation (23). A direct inspection shows that the sum inˆϕn+1
gives all the possible product of terms of typeϕ −1
0 ϕi1ϕ−1
0 ···ϕ −1
0 ϕirϕ−1
0 where the indicesi 1,...,i r
add up ton+ 1. This completes the inductive step. The case of (20) is analogous. This procedure
also shows that both right and left inverses coincide, therefore implying that ˜ϕis invertible for any
n. This implies that the system of equations (19) is well posed.□
QUANTUM COCYCLE INVARIANTS OF KNOTS FROM YANG-BAXTER COHOMOLOGY 29
Definition 8.2.We say thatϕ 1 is an integrable enhanced deformation when the obstruction to
deforming ˜R(n) =R+ Pn
i=1 ℏiϕi to degreen+ 1, ˜R(n+1) =R+ Pn+1
i=1 ℏiϕi vanishes for alln. In
other words, if for alln= 1,2,...there existsϕ n+1 such that ˜R(n) =R+ Pn+1
i=1 ℏiϕi is an EYBO
over ˜V(n) =k[[ℏ]]/(ℏ n+1)⊗V. In this case, we formally write ˜R= P∞
i=0 ℏiϕi, where we setR=ϕ 0.
Theorem 8.3.Let a knotKbe given by a diagram that is in a closed braid form of anm-braid
bm. Suppose that ˜R(n) is an EYBO with inverse ˜R−1
(n) for alln= 1,...,N.
LetΨ ( ˜R(N), ˜R−1
(N))(bm)be the operator defined from deformed YBOs ˜R±
(n). Then we have that
Φ( ˜R(N), ˜R−1
(N))(bm) =
X
(i,j1,...,jm)∈Γmn
α−w(bm)β−m Tr(Ψ( ˜R(N), ˜R−1
(N))(bm)(µj1⊗···⊗µ jm))(24)
is invariant under Markov moves, and therefore defines a knot invariantΦ ϕ(K).
WriteΦ ( ˜R(N), ˜R−1
(N))(K) =Pn
i=0 ℏiΦi
( ˜R(N), ˜R−1
(N))(K), then we have
Φi
( ˜R(N), ˜R−1
(N))(K) =
X
(i,j1,...,jm)∈Γm+1
k
α−w(bm)β−m Tr(Ψi
( ˜R(N), ˜R−1
(N))(bm)(µj1⊗···⊗µ jm))(25)
Proof.We define the quantum invariant of Turaev [20] associated to the EYBO ˜ϕ. Since ˜ϕis
graded by the formal variableℏ, it follows that each coefficient of the monomials inℏin the
quantum invariant is invariant under Markov moves. Considering the degreencomponent inℏ
we find the term P
(i,j1,...,jm)∈Γm+1
k
α−w(bm)β−m Tr(Ψi
ϕ(bm)(µj1⊗···⊗µ jm)), which is therefore an
invariant of the knotK. This completes the proof.□
Although it is desirable to have cencrete examples of higher order invariants as defined above,
it is out of the scope of this paper, and the purpose of this section is to generalize this further to
Laurent polynomial deformation to give an interpretation of the Jones and Alexander polynomials
as such quantum cocycle invariant in the next section.
9.The Jones and Alexander polynomials as higher order invariants
In this section we discuss how to interpret the Jones and Alexander polynomials as quantum
cocycle invariants. We need a slight generalization of the framework considered up to now, before
proceeding with the main results of the section.
Note that YB cohomology used in this article does not depend on the invertibility of the YBO,
as opposed to that used in [6,7], for example. Therefore, it still makes sense to discuss YB cocycles
of pre-YB operators, i.e. operators that satisty the YBE, but are not necessarily invertible. While
we have assumed invertibility so far, in this section we will not make this assumption.
Definition 9.1.Let
˜R(n) =
nX
i=0
ℏiϕi∈ ˜V(n) =k[[ℏ]]/(ℏ n+1)⊗Vand ˜R−1
(n) =
nX
i=0
ˆℏi ˆϕi∈ ˆV(n) =k[[ ˆℏ]]/(ˆℏn+1)⊗V
be pre-YBOs for alln= 0,...,N. Regard ˜V(N) and ˆV(N) as submodules of
V=k[[ℏ, ˆℏ]]/(ℏˆℏ−1).
If ˜R(N) and ˜R−1
(N) satisfy the YBE inV, and are inverse to each other inV, then we say that
( ˜R(N), ˜R−1
(N)) is a YBO obtained byLaurent deformationof pre-YBOs (R,R −1) = (ϕ0, ˆϕ0), of order
N. We do not exclude the case whereN=∞, and ˜R(∞) =P∞
i=0 ℏϕi, ˜R−1
(∞) =P∞
i=0 ˆℏi ˆϕi.
