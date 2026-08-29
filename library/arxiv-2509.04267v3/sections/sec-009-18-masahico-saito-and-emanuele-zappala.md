---
doc_id: arxiv-2509.04267v3
doc_title: "QUANTUM COCYCLE INVARIANTS OF KNOTS FROM YANG-BAXTER COHOMOLOGY"
section_id: sec-009-18-masahico-saito-and-emanuele-zappala
section_title: "MASAHICO SAITO AND EMANUELE ZAPPALA"
section_number: 18
pages: 18-20
source_pdf: 2509.04267v3.pdf
source_sha256: 9843b9dd71d1ec74
doc_brief: "QUANTUM COCYCLE INVARIANTS OF KNOTS FROM YANG-BAXTER COHOMOLOGY — Yang-Baxter operators (YBOs) have been employed to construct quantum knot invari- ants."
---
The difference to Φ 1
ϕ is that in the quandle invariant the Boltzmann weights associated to each
coloringCare multiplied together inA, and then the corresponding elements inZ[A] for each
coloring are summed together using the additive operation of the group ring; however, in the
quantum cocycle invariant the Boltzmann weights for each coloring are summed inZ[A] using the
additive operation of the group ring. If for each fixed coloring we multiply the elements ofZ[A],
we obtain the corresponding summand of the quandle cocycle invariant.
In the example that follows, the quantum cocycle invariant turns out to be stronger than the
quandle cocycle invariant. It is desirable to know more explicit and detailed relations between the
two. For example, the following questions arise: Are there examples of knots with the same quantum
invariant but distinct quandle cocycle invariant? If the quantum version is always stronger, can
we characterize the possible values of quantum cocycle invariants with a given quandle cocycle
invariant?
m−1
1 A2
A0
x
y
A AA
A
m m−1 mA
Figure 9
Example 5.11.We compare the values of quandle cocycle invariant and the corresponding quan-
tum cocycle invariant values for (2,m)-torus knotsT m with the quandleQ=Z 2[t]/(t2 +t+ 1). We
represent elements ofQby{0,1,t,1 +t}. In [5], it was shown that the following gives a non-trivial
2-cocycle with the coefficient groupZ 2:
ψ(x,y) =
X
(a,b)
χ(a,b),
whereχis Kronecker’s delta and the sum ranges over alla,b∈Qsuch thata̸=banda,b∈
{0,1,1 +t}. LetT m be a torus knot (or a link) withmcrossings that is the closure of the diagrams
depicted in Figure 9. The arcs are labeled byA i fori= 0,...,min the figure, and letu j be the
crossings from left to right of the figure. Although the cocycle invariant is known forT m with this
Q, we present computations here to observe the contrast of computations to the quantum cocycle
invariant.
Letx,ybe a pair of colors assigned to the left arcs labeled byA 0 andA m as indicated in the
figure. Then one computes that the colors are successively
C(A1) =tx+ (1 +t)y,C(A 2) =x,C(A 3) =y,C(A 4) =tx+ (1 +t)y,
and this pattern repeats with period 3. HenceT m is nontrivially colored if and only ifmis a
multiple of 3,m= 3ℓ. Ifmis not divisible by 3, then the quandle cocycle invariant is Φ Q
ψ (Tm) = 4.
A coloring ofT m form= 3ℓis trivial if and only ifx=y. We first examine the cocycle invariant
forT 3 (trefoil). For distinct (x,y), setz=tx+(1+t)y, which is the color ofA 2. The cocycle values
foru i fori= 1,2,3 areψ(x,y),ψ(y,z) andψ(z,x), respectively, and this pattern is repeated for
more crossings.
By direct computations for 12 pairs (x,y),x̸=y, for every ordered triple (x,y,z), the number
oft∈Qamong (x,y,z) is either 0 or 1. If the number oftamong{x,y,z}is 0, then from the
QUANTUM COCYCLE INVARIANTS OF KNOTS FROM YANG-BAXTER COHOMOLOGY 19
definitionψ(x,y) = P
(a,b)χ(a,b) summed overa,b∈{0,1,1 +t}, all ofψ(x,y),ψ(y,z), andψ(z,x)
take the value 1, hence
ψ(x,y) +ψ(y,z) +ψ(z,x) = 1∈Z 2
in additive notation. If the number oftis 1, then exactly one ofψ(x,y),ψ(y,z), andψ(z,x) is 1
and the other two take the value 0. Hence again we haveψ(x,y) +ψ(y,z) +ψ(z,x) = 1∈Z 2.
With a multiplicative generatorζofZ 2,ψ(x,y)ψ(y,z)ψ(z,x) =ζ, so that every nontrivial
coloring contributesζto Q
uψ(xu,yu)ϵ(u). Hence we obtain the cocycle invariant value Φ Q
ψ (T3) =
4 + 12ζ. Since the colorings and cocycle values repeat, we obtain
ΦQ
ψ (T3ℓ) = 4 + 12ζ
for all positive integerℓ.
Next we compute the corresponding quantum cocycle invariant. Letϕ(x⊗y) =ψ(x⊗y)R(x⊗y)
as in Lemma 5.4. In the above analysis of colorings, among the 12 pairs (x,y), there are two cases:
(Case 1)ψ(x,y) =ψ(y,z) =ψ(z,x) = 1,
(Case 2){ψ(x,y),ψ(y,z),ψ(z,x)}={0,0,1}.
where the numbers of colorings are 3 and 9, respectively. In (Case 1), the contribution to Φ 1
ϕ(T3) is
3ℏ, and in (Case 2), it isℏ. Hence in total the contribution toP
uϵ(u)ψ(xu,yu) is 3(3ℏ)+9(ℏ) = 18ℏ.
The trivial colorings give the contribution 4. Hence by Proposition 5.9 we obtain Φϕ(T3) = 4+18ℏ.
For generalm= 3ℓ, the contributions increase according to the number of crossings, and (Case
1) gives contribution 3ℓℏand (Case 2) givesℓℏ. In total we obtain 3(3ℓℏ) + 9(ℓℏ) = 18ℓℏand we
obtain
Φϕ(T3ℓ) = 4 + 18ℓℏ.
We note that for this particular example the quantum cocycle version gives a stronger invariant than
the quandle cocycle invariant. Further studies on relations between these invariants are desirable.
6.Quantum cocycle invariants via maxima/minima
In this section we describe a construction of quantum cocycle invariants by deforming maxima
and minima for knot diagrams with a height function specified. Throughout this section, a height
function is fixed on the plane where knot diagrams lie, and diagrams are in general position, so
that they have isolated maxima, minima, and double crossings. Diagrams are unoriented.
LetRbe a YBO onV. Let ˜R=ϕ 0 +ℏϕ 1, whereϕ 0 :=Randϕ 1 :=ϕ, be a deformed YBO.
Denote by ˜R−1 = ˆϕ0 +ℏ ˆϕ1 as before. Let ˜∪=∪ 0 +ℏ∪ 1, where∪ 0 :=∪and∪ 1 :V⊗V→Vis a
pairing. Similarly let ˜∩=∩ 0 +ℏ∩ 1, where∪ 0 :=∩and∩ 1 :V→V⊗Vis a copairing. Suppose
that∪and∩satisfy the switchback, passcup, and passcap properties. Below we use the notation
Γ = Γ2
1 from Definition 4.2.
