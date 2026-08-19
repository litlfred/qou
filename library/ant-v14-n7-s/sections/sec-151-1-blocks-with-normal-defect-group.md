---
doc_id: ant-v14-n7-s
doc_title: "Algebra & Number Theory Volume 14 No. 7 msp"
section_id: sec-151-1-blocks-with-normal-defect-group
section_title: "Blocks with normal defect group"
section_number: 1
pages: 289-294
source_pdf: ant-v14-n7-s.pdf
source_sha256: ab695eddd565addf
---
The aim of this section is to prove that Conjecture B follows from the Alperin–McKay–Navarro conjecture,
stated below.
For a ﬁxed prime p, consider the set Bl(G) of Brauer ( p-)blocks of G as in [Navarro 1998], so that
Bl(G) is a partition of Irr(G)∪ IBr(G) (recall that p-Brauer characters are deﬁned on p-regular elements
of G). Write Irr(B)= B∩ Irr(G) and IBr(B)= B∩ IBr(G) for any B∈ Bl(G). Every block B has
associated a uniquely deﬁned conjugacy class of p-subgroups of G, namely its defect groups. Given a
block B of G with defect group D, we write B∈ Bl(G| D) and we let b∈ Bl(NG(D)| D) denote its
Brauer ﬁrst main correspondent. Finally, χ∈ Irr(B) has height zero in B ifχ(1)p=| G: D|p, and we
write Irr0(B) to denote the subset of height zero characters in Irr(B).
Assuming the notation of the introduction, we have that the group G acts on{Irr(B)| B∈ Bl(G)}
by [Navarro 1998, Theorem 3.19]. The group H further acts on the set Bl(G) by [Navarro 2004,
Theorem 2.1]. While the action of G on characters is not natural enough in global-local contexts, Navarro
[2004] conjectured the following.
Conjecture (Alperin–McKay–Navarro conjecture). Let B∈ Bl(G| D) and let b∈ Bl(NG(D)| D) be its
Brauer ﬁrst main correspondent. Ifσ∈ H, then
|Irr0(B)σ|=| Irr0(b)σ|.
Here we are only concerned with the action of a speciﬁc element of H, namelyσ1. Recall that σ1∈ H
ﬁxes p′-roots of unity and sends any root of unity of order a power of p to its(p+1)-st power. If G is a
ﬁnite group of order dividing some integer n andξn is a primitive n-th root of unity, then by elementary
number theory, the restrictionω ofσ1 to the n-th cyclotomic ﬁeld Q(ξn) has order a power of p, andω
acts asσ1 on the ordinary characters of every subgroup of G. Abusing notation, we will also write σ1
for any such restriction. In particular, σ1 ﬁxes the elements of IBr(G), and hence acts trivially on Bl(G).
(Note that in general G does not act on IBr(G), but H does by Theorem 2.1 of [Navarro 2004].)
In order to prove that Conjecture B follows from the Alperin–McKay–Navarro conjecture, we need to
study blocks with a normal defect group. We follow the notation in Chapter 9 of [Navarro 1998]. Let
B∈ Bl(G| D) and assume that D◁ G. Write C= CG(D). We will denote by b∈ Bl(CD| D) a root
of B, and we will let θ∈ Irr(b) be the canonical character associated with B, which is unique up to
G-conjugacy (see [Navarro 1998, Theorem 9.12] and the subsequent discussion). Recall that D⊆ kerθ
andθ has p-defect zero when viewed as a character of CD/D (that is,θ(1)p=| CD: D|p), the stabilizer
1956 Noelia Rizo, A. A. Schaeﬀer Fry and Carolina Vallejo
of the block b is Gb= Gθ, and the inertial index |Gθ: CD| is not divisible by p. In this situation,
Irr(b)={θλ|λ∈ Irr(D)}, where the irreducible charactersθλ∈ Irr(CD) are deﬁned for x∈ CD as follows:
θλ(x)=λ(x p)θ( x p′) if x p∈ D andθλ(x)= 0 otherwise. One can see that
Gθλ= Gθ∩ Gλ.
Let c∈ Bl(Gb| D) be the Fong–Reynolds correspondent of b and B as in [Navarro 1998, Theorem 9.14].
Then the induction map Irr(c)→ Irr(B) deﬁnes a height-preserving bijection. By [loc. cit., Theorems 9.21
and 9.22] c= bGb is the only block of Gb that covers b and
Irr(B)=
⋃
λ∈Irr(D)
Irr(G|θλ). (1)
It is not difﬁcult to see that height zero characters of B further lie over characters parametrized by linear
characters of D, so that
Irr0(B)=
⋃
λ∈Irr(D/D′)
Irr(G|θλ). (2)
In order to explicitly describe the set Irr 0(B)σ1 when the defect group of B is normal we will use the
following technical lemma.
Lemma 1.1. Let G be a ﬁnite group and let p be a prime. Suppose that B is a block of G with normal
defect group D. Let b be a root of B with canonical characterθ. Write A=⟨σ1⟩≤ Gal(Q(ξ|G|)/Q). Ifλ
is a linear character of D, then let Gθ A
λ
={ g∈ G|(θλ)g=(θλ)a for some a∈ A}. With this deﬁnition
Gθ A
λ
= Gθλ= Gθ∩ Gλ.
Proof. Write C= CG(D). Recall that b is a block of CD of defect D andθ∈ Irr(CD) has defect zero
as a character of CD/D. Note that θ is A-ﬁxed since ba= b for every a∈ A. Let g∈ Gθ A
λ
. We start by
proving that g∈ Gθ. Since θ is A-ﬁxed, by the deﬁnition of θλ we have(θλ)g=(θλ)a=θλa for some
a∈ A. Evaluating on D we see that
θ(1)λa(x)=θλa(x)=θ g
λ(x)=θ(1)λg(x),
for every x∈ D. Hence λg=λa. Let x∈ CD be such that x D∈(CD/D)0, the set of p-regular elements
of CD/D, and notice that x p∈ D. (Otherwise θ( x)= 0.) Then
λg(x p)θ g(x p′)=θ g
λ(x)=θ a
λ(x)=λa(x p)θ( x′
p)=λg(x p)θ( x′
p).
This impliesθ g(x p′)=θ( x p′). Since x D= x p′ D, thenθ g=θ and g∈ Gθ.
Next we prove that g∈ Gλ. We know thatλg=λa for some a∈ A, and that g∈ Gθ. Since Gθ/CD is
a p′-group, thenλgm
=λ for some integer m relatively prime to p. In particular,λam
=λ and the order
of a as an element of Gal(Q(λ)/Q)= Gal(Q(ξo(λ))/Q) divides m, which forces a= 1 andλg=λ, as
wanted. □
Galois action on the principal block and cyclic Sylow subgroups 1957
Lemma 1.2. Let G be a ﬁnite group and let p be a prime. Suppose that B is a block of G with a normal
defect group D. Let b be a root of B with canonical character θ. Then
Irr0(B)σ1=
⋃
λ∈Irr(D/8( D))
Irr(G|θλ),
where8(D) is the Frattini subgroup of D. Moreover, if c∈ Bl(Gb| D) is the Fong–Reynolds correspon-
dent of B , then
|Irr0(B)σ1|=| Irr0(c)σ1|.
Proof. First notice that as a p-group, D has a unique block, the principal one, and Irr0(B0(D))=
Irrp′(D)= Irr(D/D′). Then Irrp′(D)σ1= Irr(D/8( D)). Since D/8( D) is p-elementary abelian, one
inclusion is straight-forward. To see that Irrp′(D)σ1⊆ Irr(D/8( D)) notice that if λ∈ Irr(D/D′) is
σ1-ﬁxed, thenλσ1=λp+1=λ, and hence|D/ kerλ|≤ p, implying8(D)⊆ kerλ.
Write A=⟨σ1⟩ and let Gθ A
λ
be as in Lemma 1.1. By (2), we know that
Irr0(B)=
⋃
λ∈Irr(D/D′)
Irr(G|θλ).
Ifχ∈ Irr0(B)σ1 lies overθλ, then(θλ)σ1=(θλ)g, for some g∈ G. In particular, g∈ Gθ A
λ
= Gθλ= Gθ∩Gλ
by Lemma 1.1. Then λσ1=λg=λ. Hence 8(D)⊆ kerλ andλ∈ Irr(D/8( D)).
Conversely, letχ∈ Irr(G|θλ), whereλ∈ Irr(D/8( D)). Then λσ1=λ. As bσ1= b, we seeσ1 ﬁxesθ
too. Then (θλ)σ1=θλ. Let ψ∈ Irr(Gθλ) be the Clifford correspondent of χ overθλ. Since Gθλ⊆ Gθ,
we know that p does not divide the order of Gθλ/CD. By [Navarro and Tiep 2019, Lemma 5.1], ψ is
σ1-invariant and so isχ.
To prove the last part of the statement, recall that the Fong–Reynolds correspondence states that the
induction mapψ↦→ψ G provides a bijection Irr0(c)→ Irr0(B). In particular,|Irr0(c)σ1|≤| Irr0(B)σ1|.
Now let χ∈ Irr0(B)σ1 lie over θλ, for some λ∈ Irr(D/8( D)) by the ﬁrst part of this proof. Then
(θλ)σ1=(θλ)g for some g∈ G. In particular, g∈ Gθ A
λ
. Since Gθ A
λ
= Gθλ by Lemma 1.1,θλ isσ1-ﬁxed.
Letξ∈ Irr(Gθλ|θλ) be the Clifford correspondent of χ. Since both χ andθλ areσ1-ﬁxed then so is ξ.
We have thatξ Gb is the Fong–Reynolds correspondent ofχ by the transitivity of block induction (see
[Navarro 1998, Problem 4.2]), which isσ1-ﬁxed. □
The Alperin–McKay–Navarro conjecture holds for blocks with cyclic defect groups by [Navarro 2004,
Theorem 3.4]. We obtain the following as a consequence of this fact.
Lemma 1.3. Let G be a ﬁnite group and let B be a block of G with cyclic defect group D. Then
1≤| Irr0(B)σ1|≤ p.
The set Irr0(B)σ1 has minimal size 1 if , and only if , D is trivial. Furthermore , if p∈{ 2, 3} and D is
nontrivial, then
|Irr0(B)σ1|= p.
1958 Noelia Rizo, A. A. Schaeﬀer Fry and Carolina Vallejo
Proof. By [Navarro 2004, Theorem 3.4], we may assume that D◁ G. Write C= CG(D)⊇ D. Let
b∈ Bl(C| D) be a root of B with canonical character θ. By Lemma 1.2, we may assume that θ is
G-invariant (in particular, G/C is a p′-group) and
Irr0(B)σ1=
⋃
λ∈Irr(D/8( D))
Irr(G|θλ)⊆ Irr(G/8( D)).
Write G= G/8( D) and use the bar convention. Let F= CG(D), where 8(D)⊆ F≤ G. We claim
that F= C. Clearly C⊆ F. Note that F acts trivially on D and coprimely on D. By [Isaacs 2008,
Theorem 3.29] we have that F acts trivially on D as well. Thus F= C as claimed.
Notice that since D is cyclic and G/C is a p′-group, then G/C is isomorphic to a subgroup of Cp−1.
Say|G/C|= m and let{λi}t
i=1 be a complete set of representatives of the G/C-orbits on Irr(D)\{ 1D},
where here we view Irr(D)⊆ Irr(D), and with this identiﬁcation Irr(D) are exactly the elements of Irr(D)
with order dividing p. Note that kerλi=8(D) for all 1≤ i≤ t, hence Gλi= C for every 1≤ i≤ t, and all
the orbits of the action of G/C on Irr(D)\{1D} have the same size m. In particular, t=(p−1)/m. Since
θ is G-invariant, for every 1≤ i≤ t we have that Gθλi= Gλi= C, and by the Clifford correspondence,
|Irr(G|θλi)|=| Irr(C|θλi)|= 1. Also, since G/C is cyclic,θ extends to G and therefore by Gallagher
theory|Irr(G|θ)|= m. Then
|Irr0(B)σ1|=| Irr(G|θ)|+
t∑
i=1
|Irr(G|θλi)|= m+ t= m+ p− 1
m ≤ p.
Note that if p= 2, 3 then m+(p−1)/m= p, whenever m divides p−1. Also notice that|Irr0(B)σ1|= 1
if, and only if, D= 1. □
The upper bound in Lemma 1.3 is not generally attained if p> 3, as shown by the dihedral group D2p,
which satisﬁes|Irr(B0(D2p))σ1|< p. We care to remark that the numerical condition|Irr0(B)σ1|≤ p does
not generally imply that a defect group D of B is cyclic. For instance, for p= 11, the semidirect product
H= F2
11 ⋊ SL2(5) satisﬁes|Irr11′(B0(H))σ1|=| Irr(H)|= 10. (We would like to thank Gabriel Navarro
for providing us with this example.)
We will need the following divisibility result, which we obtain by adapting the proof of [Gow 1979,
Theorem 5.2].
Lemma 1.4. Let G be a ﬁnite group , let p∈{ 2, 3}, and let B be a block of G with nontrivial defect
group D. Then p divides|Irr0(B)σ1|.
Proof. Write
ψ=
∑
χ∈Irr(B)
χ(1)χ, (3)
and notice thatψ is a character of G that vanishes on p-singular elements by the weak block orthogonality
relation (see [Navarro 1998, Corollary 3.7]). In particular, ψP= fρP for some natural number f , where
ρP denotes the regular character of P.
Galois action on the principal block and cyclic Sylow subgroups 1959
Let Irr(B)={χ1,...,χ t} and write χi(1)= pa−d+hi bi, where|P|= pa,|D|= pd, hi≥ 0 is the
height ofχi and p does not divide bi, for 1≤ i≤ t. Arrange the elements in Irr(B) in such a way that
Irr0(B)={χ1,...,χ k}, so that h j≥ 1 for all k+ 1≤ j≤ t. By [Navarro 1998, Theorem 3.28] we have
thatψ(1)= p2a−dc, where c is a nonnegative integer relatively prime to p. Thus, evaluating (3) at 1∈ G
we obtain
pdc=
k∑
i=1
b2
i+
t∑
j=k+1
p2h j b2
j.
As d≥ 1, we get∑k
i=1 b2
i≡ 0 mod p. Since p∈{ 2, 3}, we have that b2
i≡ 1 mod p for every 1≤ i≤ k,
and hence k is divisible by p.
Recall that the group A=⟨σ1⟩ acts on Irr0(B), and as such, we may view A as having order a power
of p. Since|Irr0(B)σ1|=| Irr0(B)A|, we obtain that p divides|Irr0(B)σ1| by the class equation for group
actions. □
The conclusion of the result above does not hold if p> 3, as the dihedral group D2p provides a
counterexample. Indeed, D2p has a unique p-block and every irreducible character has p′-degree and is
σ1-ﬁxed. Hence|Irrp′(B0(D2p))σ1|=| Irr(D2p)|= 2+(p− 1)/2< p.
Finally, we prove the main result of this section.
Theorem 1.5. Let p∈{ 2, 3}. Let G be a ﬁnite group and let B be a p-block of G with a nontrivial normal
defect group D. Then
|Irr0(B)σ1|= p if, and only if, D is cyclic.
In particular, Conjecture B follows from the Alperin–McKay–Navarro conjecture.
Proof. By Lemma 1.3 we know that the “if” implication holds. We now assume that|Irr0(B)σ1|= p and
we work to show that D is cyclic.
Write C= CG(D) and let θ∈ Irr(CD) be the canonical character of B. Let{λi}t
i=1 be a complete
set of representatives of the G/CD-orbits on Irr(D/8( D))\{ 1D}. By Lemma 1.2 we may assume that
Gθ= G and
Irr0(B)σ1=
t⋃
i=1
Irr(G|θλi)
is a disjoint union. If p= 2, then
2=| Irr0(B)σ1|=| Irr(G|θ)|+
t∑
i=1
|Irr(G|θλi)|.
Since D is nontrivial by hypothesis, we have that t≥ 1. Thus t= 1 and the charactersθ andθλ1 are fully
ramiﬁed with respect to their inertia subgroups. In particular, there are positive integers e and e1 such that
|G: C|= e2 and|Gθλ1: C|= e2
1. Suppose that|D|= 2n. Since G/CD acts transitively on the nontrivial
elements of D/8( D), we have that 2n− 1=| G: Gλ1|= (e/e1)2= f 2. The equality f 2+ 1= 2n forces
1960 Noelia Rizo, A. A. Schaeﬀer Fry and Carolina Vallejo
f to be odd, then f 2≡ 1 mod 8, and so f 2+ 1≡ 2 mod 8 leaves as the only possibility n= 1= f , that
is, D= C2, as wanted. These techniques do not totally sufﬁce to prove the case where p= 3. We ﬁrst
need to show that we may assume 8(D)= 1. Indeed, write G= G/8( D), D= D/8( D) and let B be a
block of G contained in B such that D is the defect group of B by [Navarro 1998, Theorem 9.9]. Then
Irr0(B)σ1⊆ Irr0(B)σ1. By Lemma 1.2 we have that Irr0(B)σ1= Irr(B) is nonempty. Hence by Lemma 1.4,
we have that p divides|Irr0(B)σ1|≤| Irr0(B)σ1|= p, that forces|Irr0(B)σ1|= p. If 8(D)⁄= 1 we can
apply induction to obtain that D is cyclic, and thus D is cyclic. Hence we may assume that 8(D)= 1.
Since D is p-elementary abelian, then Irr0(B)σ1= Irr(B) by the description of these sets in (1) and
Lemma 1.2. By [Sambale 2014, Proposition 15.2], if p= 3 then|Irr(B)|= p implies|D|= p and the
proof is ﬁnished. □
