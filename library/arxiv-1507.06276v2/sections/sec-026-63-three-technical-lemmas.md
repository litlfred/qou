---
doc_id: arxiv-1507.06276v2
doc_title: "UNIVERSAL K-MATRIX FOR QUANTUM SYMMETRIC PAIRS"
section_id: sec-026-63-three-technical-lemmas
section_title: "Three technical lemmas"
section_number: 6.3
pages: 31-33
source_pdf: 1507.06276v2.pdf
source_sha256: f552aa5de7125b23
toc_source: outline
doc_brief: "UNIVERSAL K-MATRIX FOR QUANTUM SYMMETRIC PAIRS — Let g be a symmetrizable Kac-Moody algebra and let Uq(g) de- note the corresponding quantized enveloping algebra."
---
inductively construct Xµ by solving the system of equations given by (6.2), (6.3)
for all i ∈ I. To simplify the proof that the right hand sides of equations (6.2),
(6.3) satisfy the conditions from Proposition 6.3.(2), we provide sev eral technical
lemmas. These results are auxiliary and will only be used in the proof of Lemma
6.8.
Lemma 6.4. Leti ⁄=j ∈I andµ = (1 −aij)αi +αj. If Θ(µ) = −µ theni,j ∈I \X
and one of the following two cases holds:
(1) Θ( αi) = −αj and aij = 0.
(2) Θ( αi) = −αi and Θ(αj) = −αj.
Proof. Assume that i ∈ X. Then Θ( αi) = αi which together with Θ( µ) = −µ
implies that
wX (ατ (j)) = −Θ(αj) = −Θ(µ − (1 −aij)αi) = αj + 2(1 −aij)αi.
Henceτ (j) = j andσi(αj) = wX (αj) and −aij = 2(1 −aij). This would mean that
aij = 2 which is impossible.
Assume that j ∈X. Then
wX (ατ (i)) = −Θ(αi) = −1
(1 −aij) Θ(µ −αj ) = αi + 2
(1 −aij)αj.
Hence τ (i) = i and σj(αi) = wX (αi) and aji = − 2
(1−aij ) . This is only possible if
aji =aij = −1. But then
αi(ρ∨
X ) = 1
2αi(hj) = −1
2 /∈ Z
which contradicts condition (3) in Deﬁnition 5.1 of an admissible pair.
Hence i,j ∈I \X. As ( wX − id)(αk) ∈QX for any k ∈I, it follows that
(1 −aij)(αi −ατ (i)) + (αj −ατ (j)) = −Θ(µ) −τ (µ) = (wX − id)(τ (µ))
lies in QX. Using i,j ∈I \X, it follows that (1 −aij)(αi −ατ (i)) + (αj −ατ (j)) = 0.
So, there are two possibilities: either (1) τ (i) = j and aij = 0, or (2) τ (i) = i and
τ (j) = j. □
Lemma 6.5. Letµ ∈Q+ and let j ∈I \X with sj = 0 . Assume that a collection
(Xµ′ )µ′≤µ with Xµ′ ∈U +
µ′ satisﬁes condition (6.2) for all µ′ ≤µ and for all i ∈I.
If Xµ ⁄= 0, then µ ∈ spanN0{αj − Θ(αj)} ⊕ spanN0 {αk|k ⁄=j}.
32 MARTINA BALAGOVI ´C AND STEF AN KOLB
Proof. We prove this by induction on ht( µ). If µ >0 and Xµ ⁄= 0 then by (2.18)
there exists some i such thatri(Xµ) ⁄= 0. Relation (6.2) implies that Xµ+Θ( αi)−αi ⁄=
0 or siXµ−αi ⁄= 0. If i ⁄= j then the induction hypothesis on µ + Θ( αi) −αi and
µ −αi implies the claim. If i =j then the induction hypothesis on µ + Θ(αi) −αi
implies the claim. □
Recall thatσ denotes the involutive antiautomorphism ofUq(g) deﬁned by (2.21).
Lemma 6.6. Let ν ∈Q+, and let (Xµ)µ<ν∈Q+ be a collection with Xµ ∈U +
µ and
X0 = 1 . For all µ < νassume that Xµ satisﬁes (6.2) and (6.3) for all i ∈ I. Let
j,k ∈I \X be such that Θ(αj) = −αj and Θ(αk) = −αk. Assume that n ≥ 0, and
that x ∈U −
nαk+αj satisﬁes σ(x) = −x. Then
⟨x, Xµ⟩ = 0(6.10)
for all µ<ν .
Proof. The space U −
nαk+αj is spanned by elements of the form Fa
kFjFb
k witha +b =
n. As the antiautomorphism σ is involutive it is enough to verify Equation (6.10)
for elements of the form x =Fa
kFjFb
k −σ(Fa
kFjFb
k ) = Fa
kFjFb
k −Fb
kFjFa
k. We will
prove that
⟨
Fa
kFjFb
k −Fb
kFjFa
k, Xµ
⟩
= 0(6.11)
for all µ < νand a,b ≥ 0 by induction on n = a +b. It holds for n = 0. Let
a +b =n> 0, and assume that (6.11) holds for all a′,b ′ witha′ +b′<n . Without
loss of generality assume that b >0. Using the assumption that Xµ satisﬁes (6.2)
and (6.3), we get that
⟨
Fa
kFjFb
k −Fb
kFjFa
k, Xµ
⟩
= −1
qk −q−1
k
(⟨
Fa
kFjFb−1
k ,rk(Xµ)
⟩
−
⟨
Fb−1
k FjFa
k,kr(Xµ)
⟩)
=
⟨
Fa
kFjFb−1
k , Xµ−2αkckXk +skXµ−αk
⟩
−
⟨
Fb−1
k FjFa
k,q (αk,αk)ckXkXµ−2αk +skXµ−αk
⟩
.
The assumption Θ( αk) = −αk implies that Xk = −Ek and by (5.17) and (5.16)
one has ck =q(αk,αk)ck and sk =sk. Hence the above equation turns into
⟨
Fa
kFjFb
k −Fb
kFjFa
k, Xµ
⟩
=sk
⟨
Fa
kFjFb−1
k −Fb−1
k FjFa
k, Xµ−αk
⟩
−ck
(⟨
Fa
kFjFb−1
k , Xµ−2αkEk
⟩
−
⟨
Fb−1
k FjFa
k,EkXµ−2αk
⟩)
By the induction hypothesis one has
⟨
Fa
kFjFb−1
k −Fb−1
k FjFa
k, Xµ−αk
⟩
= 0. Hence,
⟨
Fa
kFjFb
k −Fb
kFjFa
k, Xµ
⟩
= ck
qk−q−1
k
⟨
rk(Fa
kFjFb−1
k )−kr(Fb−1
k FjFa
k ), Xµ−2αk
⟩
.
As
σ(rk(Fa
kFjFb−1
k ) −kr(Fb−1
k FjFa
k ))
(2.22)
= kr(σ(Fa
kFjFb−1
k )) −rk(σ(Fb−1
k FjFa
k ))
= −(rk(Fa
kFjFb−1
k ) −kr(Fb−1
k FjFa
k )),
Equation (6.11) follows from the induction hypothesis. □
UNIVERSAL K-MATRIX FOR QUANTUM SYMMETRIC PAIRS 33
