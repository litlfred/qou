---
doc_id: arxiv-1608.07308v1
doc_title: "FLAG HILBERT SCHEMES, COLORED PROJECTORS AND KHOV ANOV-ROZANSKY HOMOLOGY"
section_id: sec-026-39-geometric-markov-invariance
section_title: "Geometric Markov invariance"
section_number: 3.9
pages: 27-30
source_pdf: 1608.07308v1.pdf
source_sha256: bcc3b6f1a91a55c6
doc_brief: "FLAG HILBERT SCHEMES, COLORED PROJECTORS AND KHOV ANOV-ROZANSKY HOMOLOGY — We construct a categoriﬁcation of the maximal commutative subalgebra of the type A Hecke algebra."
---
governs the behavior of objects under Markov moves:
(3.32) α↝i(α), α ↝i(α)·σn, α ↝i(α)·σ−1
n
wherei is the operation of adding an extra strand to a braidα onn strands. We will now study
how the complexes of sheavesB(α) = ι∗(α)∈ Db(CohC∗×C∗(FHilbdg
n (C)) behave under the
same moves. Throughout this Subsection, we write FHilbdg
n = FHilbdg
n (C) and:
π : FHilbdg
n+1→ FHilbdg
n × C
for the standard projection. The following Corollary is an easy consequence of Conjecture 3.9,
as we will show in Subsection 4.8.
Corollary 3.11. For any braidα onn strands, we have:
(3.33) B(i(α)) =π∗(B(α)).
28 EUGENE GORSKY, ANDREI NEGUT , , AND JACOB RASMUSSEN
To tackle the second and third Markov moves of (3.32), we consider the dg subscheme:
(3.34) Zn⊂ FHilbdg
n+1
OZn :=
[
...
yn,n+1
− −−− →q2tLn
Ln+1
xn−xn+1
−−−−−→qtLn
Ln+1
yn,n+1
− −−− →qO
xn−xn+1
−−−−−→O
]
,
whereyn,n+1 denotes the last subdiagonal entry of the matrixY of (2.14), regarded as an endo-
morphismtLn→L n+1 on FHilbdg
n+1. The fact thatOZn is a complex follows from:
0 = [X,Y ]n,n+1 =xnyn,n+1−yn,n+1xn+1
Conjecture 3.12. For any braidα onn strands, we have:
(3.35) B(i(α)·σn) =π∗(B(α))⊗OZn.
Corollary 3.13. Conjecture 3.12 implies that for any braidα onn strands:
(3.36) B(i(α)·σ−1
n ) =π∗(B(α))⊗OZn⊗ Ln
Ln+1
.
Proof. Note the following the equation in the braid group:
Ln+1 =σn·Ln·σn⇒σ−1
n =L−1
n+1·σn·Ln⇒
i(α)·σ−1
n =i(α)·L−1
n+1·σn·Ln =L−1
n+1·i(α)·σn·Ln.
sinceLn+1 commutes with the image ofi. ApplyingB(−) to the above equation implies:
B(i(α)·σ−1
n ) =ι∗(i(α)⊗σ−1
n ) =ι∗(L−1
n+1⊗i(α)⊗σn⊗Ln))
As in Conjecture 1.1, we haveLk =ι∗(Lk) for allk, and therefore (3.17) implies (3.36).
□
Equations (3.33)–(3.36) are compatible with the stabilization invariance ofHHH at the level
of equivariant Euler characteristic.
Proposition 3.14. For any braidα onn strands, we have:
(3.37) χ
(
B(i(α))⊗∧•T∨
n+1
)
= 1−a
1−qχ (B(α)⊗∧•T∨
n )
Assuming Conjecture 3.12, we further have:
(3.38) χ
(
B(i(α)·σn)⊗∧•T∨
n+1
)
= χ (B(α)⊗∧•T∨
n )
(3.39) χ
(
B(i(α)·σ−1
n )⊗∧•T∨
n+1
)
= a
qtχ (B(α)⊗∧•T∨
n )
Proof. We replace the sheaves in (3.37)–(3.39) by theirK–theory classes and write:
[Tn+1] =π∗ ([Tn]) + [Ln+1]
and:
(3.40) [OZn] = (1−q)
(
1− qt[Ln]
[Ln+1]
)−1
Since
∫
is just pushforward to a point, it can be decomposed along the projection map π :
FHilbdg
n+1→ FHilbdg
n × C. In other words, for all sheavesA one has:
∫
FHilbdg
n+1
A =
∫
FHilbdg
n×C
π∗A
FLAG HILBERT SCHEMES, COLORED PROJECTORS AND KHOV ANOV-ROZANSKY HOMOLOGY 29
We will apply this equality for theK–theory class:
[A] = [B(i(α))]·∧•[T∨
n+1] =π∗ ([B(α)]·∧•[T∨
n ])·
(
1− a
[Ln+1]
)
where in the second equality we have used (3.33). Then we may prove (3.37) by noting that:
χ
(
[B(i(α))]·∧•[T∨
n+1]
)
=χ
(
π∗
[
π∗ ([B(α)]·∧•[T∨
n ])·
(
1− a
[Ln+1]
)])
=
(3.41) =χ
(
[B(α)]·∧•[T∨
n ]·π∗
(
1− a
[Ln+1]
))
= (1−a)χ ([B(α)]·∧•[T∨
n ])
(the additional factor of 1−q in the right hand side of (3.37) comes from integrating over C).
To establish the last equality in (3.41), we note that it holds at the categoriﬁed level:
(3.42) π∗
(
OFHilbdg
n+1
)
=OFHilbdg
n×C =π∗
(
OFHilbdg
n+1
⊗L−1
n+1
)
where the ﬁrst equality is a consequence of the fact thatπ is the projectivization ofE∨
n , and the
second equality follows from the ﬁrst and (2.40) forA =O. Similarly, if we assume formula
(3.35) (which would also imply (3.36), according to Corollary 3.13), then relations (3.38) and
(3.39) follow from:
(3.43) π∗(OZn) =
[
qO
xn−xn+1
−−−−−→O
]
, π ∗
(
OZn⊗ 1
Ln+1
)
= 0
(3.44) π∗
(
OZn⊗ 1
L2
n+1
)
=
[ 1
tLn
xn−xn+1
−−−−−→1
qtLn
]
[1]
We will only prove these equalities at the level ofK–theory, by using (3.40). Indeed, since the
mapπ is PE∨
n , the push-forwards of the powers ofLn+1 =O(1) are encoded by:
(3.45) π∗
(
δ
(Ln+1
z
))
=S∗
z∼∞[En]−S∗
z∼0[En] =
= ∧∗
z∼∞[qtTn]∧∗
z∼∞ [Tn]
(1−z−1)∧∗
z∼∞ [qTn]∧∗
z∼∞ [tTn]− ∧∗
z∼0[qtTn]∧∗
z∼0 [Tn]
(1−z−1)∧∗
z∼0 [qTn]∧∗
z∼0 [tTn]
where theδ function isδ(z) =∑∞
k=−∞zk. In the right hand side, we write:
S∗
z[V] =
∞∑
k=0
(−z)−k·SkV, ∧∗
z[V] =
∞∑
k=0
(−z)−k·∧kV
and the notationsS∗
z∼0,∧∗
z∼0 andS∗
z∼∞,∧∗
z∼∞ refer to expanding the rational functions S∗
z,∧∗
z
in the domainsz∼ 0 andz∼∞ , respectively. Applying (3.40), we obtain:
π∗
(
[OZn]·δ
(Ln+1
z
))
=π∗
(
1−q
1− qt[Ln]
[Ln+1]
·δ
(Ln+1
z
))
= 1−q
1− qt[Ln]
z
·π∗
(
δ
(Ln+1
z
))
and we can compute the right hand side using (3.45). To obtain (3.43) and (3.44), we must
extract the coefﬁcients ofz0,z1,z2 in the right hand side of the above equality, and it is easy to
see that one obtains 1−q, 0 and q−1
qt[Ln], respectively. □
30 EUGENE GORSKY, ANDREI NEGUT , , AND JACOB RASMUSSEN
