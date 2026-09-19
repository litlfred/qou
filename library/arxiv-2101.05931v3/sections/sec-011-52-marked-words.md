---
doc_id: arxiv-2101.05931v3
doc_title: "CATEGORICAL BRAID GROUP ACTIONS"
section_id: sec-011-52-marked-words
section_title: "Marked words"
section_number: 5.2
pages: 13-17
source_pdf: 2101.05931v3.pdf
source_sha256: 41eaa81b97ede8e9
doc_brief: "CATEGORICAL BRAID GROUP ACTIONS — Let g be a semisimple simply-laced Lie algebra of ﬁnite type."
---
sition 5.9 below. A marked word is a word in the elements of I with one letter marked:
a = (i1,i 2,...,i ℓ,...,i n). From a we can deﬁne a functor and an element of W :
Φ( a) = Θ i1 · · ·Θ iℓ−1FiℓΘ iℓ1 · · ·Θ in
/BD
λ,
w(a) = si1 · · ·sin.
Note that unlike Φ( a), w(a) forgets the location of the marked letter. We say that a is reduced,
if the corresponding unmarked word is a reduced expression f or w(a).
We will apply braid relations to marked words. Away from the m arked letter these operate as
usual, and at the marked letter we have:
(...,k,ℓ ,... ) ↔ (...,ℓ ,k,... ), if (k,ℓ ) = 0 and, (5.4)
(...,ℓ,k,ℓ ,... ) ↔ (...,k ,ℓ,k,... ), if (k,ℓ ) = −1. (5.5)
For marked words a, b we write a ∼ b if they are related by a sequence of braid relations.
Lemma 5.6. Let a, b be marked words which diﬀer by a single braid relation. Then th ere exists
k ∈ {0, ±1} such that Φ( a) ∼= Φ( b)[k]⟨−k⟩.
Proof. If the relation doesn’t involve the marked letter then Φ( a) ∼= Φ( b) since Rickard complexes
satisfy the braid relations [11, Theorem 2.10]. Suppose the n that the relation does involve the
marked letter. If (j,ℓ ) = 0 the result follows from the fact that Θ jFℓ ∼= FℓΘ j. Otherwise (j,ℓ ) = −1.
Set µ =sℓsj(λ) −αj. Applying Lemma 5.3 (twice) we deduce that
/BD
µΘ ℓΘ jFℓ
/BD
λ = Θ ℓΘ jFℓ
/BD
λ ∼=
{
Θ ℓFjℓΘ j
/BD
λ, if λj ≥ 0,
Θ ℓFjℓΘ j
/BD
λ[1]⟨−1⟩, if λj < 0.
∼=



FjΘ ℓΘ j
/BD
λ[−1]⟨1⟩ if λj ≥ 0,µ ℓ > 0,
FjΘ ℓΘ j
/BD
λ[1]⟨−1⟩ if λj < 0,µ ℓ ≤ 0,
FjΘ ℓΘ j
/BD
λ otherwise.
Hence the result follows. □
Corollary 5.7. Let a, b be marked words such that a ∼ b. Then there exists an integer k such
that Φ( a) ∼= Φ( b)[k]⟨−k⟩.
Lemma 5.8. Let a = (i1,...,i n,ℓ ) and b = (ℓ′,i 1,...,i n) be reduced marked words such that w(a) =
w(b). Then a ∼ b.
14 IV A HALACHEV A, ANTHONY LICATA, IV AN LOSEV, AND ODED YACOB I
Proof. We prove the claim by induction on n. Since w(a) = w(b) there is a Matsumoto sequence
of length M relating the unmarked words a = (i1,...,i n,ℓ ) and b = (ℓ′,i 1,...,i n). Let a0 = a →
a1 → · · · → aM = b denote the resulting sequence of unmarked words, starting a t a and ending b.
Let ar+1 be the ﬁrst word in this sequence whose last entry is not ℓ. In other words, the ﬁrst r
steps in the sequence do not involve the last entry of a, but the ( r + 1)st step does.
We will now consider the same sequence of steps, but applied t o the marked words. We then
obtain a sequence of marked words a0 = a → a1 → · · · . Further, we know that ar = (j1,...,j n,ℓ )
for some j1,...,j n, and the next step involves the marked letter.
If the (r + 1)st step is an application of (5.5) then jn−1 =ℓ and the step is:
ar = (j1,...,j n−2,ℓ,j n,ℓ ) → ar+1 = (j1,...,j n−2,j n,ℓ,j n).
Let b′ := (ℓ′,j 1,...,j n−2,ℓ,j n), i.e. b′ is obtained from b by applying the ﬁrst r steps to its (last
n) entries as were used for the (ﬁrst n) entries of a. Note that ar+1 and b′ are reduced marked
words such that w(ar+1) = w(b′), and both end in ( ℓ,j n). Hence, if we delete these last two entries
we obtain two reduced marked words a′′ = (j1,...,j n−2,j n) and b′′ = (ℓ′,j 1,...,j n−2) such that
w(a′′) = w(b′′). By induction a′′ ∼ b′′ and therefore ar+1 ∼ b′. Since clearly b′ ∼ b, we have our
desired result:
a ∼ ar ∼ ar+1 ∼ b′ ∼ b.
If the (r + 1)st step is an application of (5.4) then the step is:
ar = (j1,...,j n−1,j n,ℓ ) → ar+1 = (j1,...,j n−1,ℓ,j n).
Note that ar+1 and b′ := (ℓ′,j 1,...,j n−1,j n) are reduced marked words such that w(ar+1) = w(b′),
and both end in jn. Hence we can delete this last entry and apply a similar analy sis as above.
□
5.3. The relation between Θ w0 and Chevalley functors. We now have the machinery in place
to prove our main relation.
Proposition 5.9. For any i ∈I,λ ∈X we have the following relations:
Θ w0Ei
/BD
λ ∼= Fτ (i)Θ w0
/BD
λ[1]⟨λi⟩,
Θ w0Fi
/BD
λ ∼= Eτ (i)Θ w0
/BD
λ[1]⟨−λi⟩.
Proof. We’ll prove the ﬁrst relation, the second being entirely ana logous. For two functors F, G we
write F ≡ G if there exist integers ℓ,k such that F ∼= G[ℓ]⟨k⟩.
We ﬁrst show that Θ w0Ei ≡ Fτ (i)Θ w0 by induction on the rank of g. The base case, when g = sl2,
follows from Lemma 5.1. For the inductive step let J ⊂ I be a strict subdiagram containing i.
Recall the bijection τJ : I →I induced by the longest element wJ
0 ∈ WJ . Let u =w0(wJ
0 )−1 and
let u =si1 · · ·sin be a reduced expression. Deﬁne two marked words:
a = (i1,...,i n,τ J (i)),
b = (τ (i),i 1,...,i n).
Note that w(a) = w(b). By the inductive hypothesis we have Θ wJ
0
Ei ≡ FτJ (i)Θ wJ
0
, and therefore
Θ w0Ei ≡ Θ uΘ wJ
0
Ei ≡ Θ uFτJ (i)Θ wJ
0
≡ Φ( a)Θ wJ
0
.
Note that a, b satisfy the hypothesis of Lemma 5.8, so by Lemmas 5.7 and 5.8 w e have that
Φ( a) ≡ Φ( b), and hence Θ w0Ei ≡ Φ( b)Θ wJ
0
≡ Fτ (i)Θ w0.
We now know there exist integers k,ℓ such that Θ w0Ei
/BD
λ ∼= Fτ (i)Θ w0
/BD
λ[ℓ]⟨k⟩, and it remains to
show that ℓ = 1,k =λi. Let u =w0si and let u =si1 · · ·sin be a reduced expression. Deﬁne two
CATEGORICAL BRAID GROUP ACTIONS AND CACTUS GROUPS 15
marked words:
a = (i1,...,i n,i ),
b = (τ (i),i 1,...,i n).
Note that a, b satisfy the hypothesis of Lemma 5.8, so by Lemmas 5.7 and 5.8 t here exists an
integerm such that Φ( a) ∼= Φ( b)[m]⟨−m⟩. Hence we have that
Θ w0Ei
/BD
λ ∼= Θ uΘ iEi
/BD
λ
∼= Θ uFiΘ i
/BD
λ[1]⟨λi⟩
∼= Fτ (i)Θ uΘ i
/BD
λ[m + 1]⟨−m +λi⟩
∼= Fτ (i)Θ w0
/BD
λ[m + 1]⟨−m +λi⟩
showing that ℓ +k = 1 +λi.
On the other hand, we can deduce k by inspecting the relation on the level of Grothendieck
groups. Namely, by [25, Lemma 5.4], we have that
tw0Ei1λ = −q−λiFτ (i)tw01λ,
showing that k =λi. □
6. On t-exactness and perversity of Θ w0
In this section we will state and prove the central results of the paper. We ﬁx throughout a
categorical representation C of Uq(g), and let w0 =si1si2 · · ·sin be a reduced expression.
6.1. Θ w0 on isotypic categoriﬁcations. In this section we prove that Θ w0 is t-exact on any
isotypic categoriﬁcation. Fix λ ∈X+. We write Θ = Θ w0,L =L(λ) and L = L(λ).
Lemma 6.1. Let k ∈ { 2,...,n } and set µ = sik · · ·sin(w0(λ)). The weight space L(λ)µ−αik−1
is
zero.
Proof. By [24, Proposition 21.3], it suﬃces to ﬁnd u ∈ W such that u(µ −αik−1) č w0(λ). Take
u =sik−1 and, noting that ( µ,α ik−1)< 0, the result follows. □
Recall that vλ and vlow
λ are the highest and lowest weight elements of the canonical b asis B(λ).
Lemma 6.2. [25, Comment 5.10] We have tw0(vlow
λ ) = vλ.
Proposition 6.3. The equivalence Θ /BD
w0(λ) : Db(Lw0(λ)) → Db(Lλ) satisﬁes /CZ
low ↦→/CZ
high, where
both are considered as complexes concentrated in degree zer o. In particular, under the equivalences
Lλ ∼= Lw0(λ) ∼=
/CZ −modZ, Θ /BD
w0(λ) is isomorphic to the identity autofunctor of Db(/CZ −modZ).
Proof. Consider ﬁrst the case g = sl2. On the minimal categoriﬁcation of highest weight m, we
have that Θ /BD
−m(/CZ
low) = /CZ
high⟨ℓ⟩ for some ℓ by [16, Theorem 6.6]. Since [Θ /BD
−m] = t11−m, by
Lemma 6.2 we conclude that ℓ = 0, and hence Θ /BD
−m(/CZ
low) = /CZ
high.
For general g, suppose X ∈ L ν is simple and FiX = 0 for some i ∈I. Consider L as a categorical
representation of sl2 by restriction to thei-th root subalgebra. Then for some m we have a morphism
of categorical sl2 representationsRX : L(m) → L, such that RX (/CZ
low) = X [16, Theorem 5.24].
The functor RX is equivariant for the categorical sl2 action on C determined by Ei, Fi (in fact it is
strongly equivariant in the sense of [34, Deﬁnition 3.1]), a nd hence commutes with Θ i
/BD
ν. Therefore
we have that
Θ i
/BD
ν(X) ∼= Θ i
/BD
ν(RX (/CZ
low))
∼=RX (Θ i
/BD
ν(/CZ
low))
∼=RX (/CZ
high) ∈ L,
16 IV A HALACHEV A, ANTHONY LICATA, IV AN LOSEV, AND ODED YACOB I
and so Θ i
/BD
ν(X) is in homological degree zero. It follows that in the case wh enX is not necessarily
simple (but still assume that FiX = 0), Θ i
/BD
ν(X) is still in homological degree zero. Indeed, by
induction on the length of a Jordan-H¨ older ﬁltration of X one deduces this since L ⊂ Db(L) is
extension closed.
Now we study Θ /BD
w0(λ) applied to /CZ
low. For k = 2,...,n , by Lemma 6.1,
Fik−1(Θ ik · · ·Θ in
/BD
w0(λ)(/CZ
low)) = 0.
By the previous paragraph, it follows that Θ ik−1 · · ·Θ in
/BD
w0(λ)(/CZ
low) is in homological degree zero,
and in particular, Θ /BD
w0(λ)(/CZ
low) is supported in homological degree zero. Since in addition
[Θ /BD
w0(λ)] = tw01w0(λ),
by Lemma 6.2 we conclude that Θ /BD
w0(λ)(/CZ
low) ∼=
/CZ
high. □
Theorem 6.4. Letλ ∈X+ and set L = L(λ). For any µ ∈X,
Θ /BD
µ[−n] : Db(Lµ) →Db(Lw0(µ))
is t-exact, where n =ht(µ −w0(λ)).
Proof. Consider P = Ei1 · · · Eiℓ(/CZ
low) ∈ L µ. We will ﬁrst prove by induction on n that there exists
an integer k such that
Θ(P )[−n] ∼= Fj1 · · ·Fjℓ(/CZ
high)⟨k⟩ ∈ Lw0(µ), (6.5)
where jr =τ (ir).
The base case when n = 0 follows by Proposition 6.3. For the inductive step write P = Ei1(Q).
Note that Q ∈ L µ−αi1 . By Proposition 5.9 we have that
Θ /BD
µ(P )[−n] = Θ Ei1
/BD
µ−αi1 (Q)[−n]
∼= Fτ (i1)Θ /BD
µ−αi1 (Q)[−n + 1]⟨(µ −αi1,α i1)⟩.
By hypothesis
Θ /BD
µ−αi1 (Q)[−n + 1] ∼= Fj2 · · ·Fjℓ(/CZ
high)⟨k⟩ ∈ Lw0(µ−αi1 )
for some k, and hence Equation (6.5) follows.
Since up to grading shift, any projective indecomposable ob ject in Lµ, respectively Lw0(µ), is a
summand of an object of the form Ei1 · · ·Eiℓ (/CZ
low) (respectively Fj1 · · · Fjℓ(/CZ
high)), it follows that
Θ /BD
µ[−n] takes projective objects in Lµ to projective objects in Lw0(µ). Since Θ /BD
µ[−n] is a derived
equivalence it follows that it is t-exact.
□
Remark 6.6. Theorem 6.4 is a generalisation of [16, Theorem 6.6], which c overs the sl2 case. Note
that [16, Theorem 6.6] is crucial in the work of Chuang and Rou quier, since it’s one of the main
technical results needed to prove that Rickard complexes ar e invertible. Our proof in the general
case follows a completely diﬀerent approach, but it does not g ive a new proof in the case of sl2.
Indeed we use [16, Theorem 6.6] explicitly in the proof of Pro position 6.3, and more generally we
use the fact the Θ i is invertible throughout.
Corollary 6.7. Suppose C is an isotypic categoriﬁcation of type λ, for some λ ∈ X+, and let
µ ∈X. Then Θ /BD
µ[−n] : Db(Cµ) →Db(Cw0(µ)) is a t-exact equivalence, where n =ht(µ −w0(λ)).
Proof. By Lemma 3.5, there exists an abelian /CZ -linear category A such that C ∼= L(λ) ⊗
/CZ
A as
categorical representations. We have that
Θ /BD
µ[−n](L(λ)µ ⊗
/CZ
A) ∼= Θ /BD
µ[−n](L(λ)µ) ⊗
/CZ
A ∼= L(λ)w0(µ) ⊗
/CZ
A,
proving that Θ /BD
µ[−n] : Db(Cµ) →Db(Cw0(µ)) is a t-exact equivalence. □
