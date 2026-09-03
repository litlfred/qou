---
doc_id: arxiv-1712.08953v1
doc_title: "REPRESENTATIONS OF THE ORIENTED SKEIN CATEGORY"
section_id: sec-022-18-j-brundan
section_title: "J. BRUNDAN"
section_number: 18
pages: 18-20
source_pdf: 1712.08953v1.pdf
source_sha256: 005e0b1ad63c173e
doc_brief: "REPRESENTATIONS OF THE ORIENTED SKEIN CATEGORY — The oriented skein category OS(z, t ) is a ribbon category which un- derpins the deﬁnition of the HOMFLY-PT invariant of an orien ted link, in the"
---
Remark 3.2. Pre-composing the functor Ψ with one or both of the isomorphisms
# and π from (2.11)–(2.12) gives three more such functors with t = qn replaced by
q−n,−qn or−q−n. The arguments above actually show that these four functors co nsti-
tute essentially all possible k -linear monoidal functors OS (z,t )→ RepUq(gln) taking
↑↦→V + and↓↦→V−. Each of the four choices for this functor corresponds to a ribbo n
structure on the monoidal category Rep Uq(gln). The standard ribbon structure on
RepUq(gln) is the one coming from Ψ itself, i.e., t = qn, and we will only use this
from now it. Taking Ψ ◦ #, i.e., t = q−n, gives a non-standard ribbon structure on
RepUq(gln) with positive upward crossing −R−1, rightward cap and cup being ev and
coev, and leftward cap and cup being ev ′ and coev′ with ε =−1; this is the ribbon
category denoted Rep Uq(gl−n) in the introduction.
In order to prove Theorems 1.2 and 1.3 from the introduction, we als o need the
Iwahori-Hecke algebraHr associated to the symmetric group Sr. This is the associative
k -algebra with generators S1,...,S r−1 subject to the relations
(Si−q)(Si +q−1) = 0, S iSj =SjSi if|i−j|> 1, SiSi+1Si =Si+1SiSi+1. (3.6)
As is well known, Hr has dimension r!, with basis {Sw|w∈ Sr} deﬁned as usual by
lettingSw be the word in the generators Si arising from any reduced expression for w.
It is obvious from the deﬁning relations that there is a homomorphism
ır :Hr→ EndOS (z,t)(↑r) (3.7)
sending Si to the positive crossing of the ith and ( i + 1)th strands, numbering
strands in increasing order from right to left. Also for λ⊢r we let
xλ :=
∑
w∈Sλ
qℓ(w)Sw, y λ :=
∑
w∈Sλ
(−q)−ℓ(w)Sw, (3.8)
where Sλ denotes the usual parabolic subgroup Sλ1× Sλ2×··· of Sr. Assuming q is
not a root of unity, there is a unique (up to sign) idempotent
eλ∈yλtHrxλ. (3.9)
This is the Young symmetrizer. For example,
e(n) = q− 1
2n(n−1)
[n]!q
∑
w∈Sn
qℓ(w)hw, e (1n) = q
1
2n(n−1)
[n]!q
∑
w∈Sn
(−q)−ℓ(w)hw, (3.10)
which correspond to the trivial and the sign representations of Hr, respectively. The
algebra involution
# : Hr→Hr, S i↦→−S−1
i (3.11)
interchanges e(n) and e(1n). Given an Hr-module M , the Hr-module M # obtained
from M by twisting the action by # gives the q-analog of “tensoring with sign.”
Proof of Theorem 1.3. Since we can compose with #, which switches t = qn with
t = q−n and e(n) with e(1n), we are reduced just to proving the theorem in the case
that ε = +. Then the appropriate monoidal functor Ψ is the one construct ed in
Lemma 3.1.
In this paragraph, we show that Ψ is full. Take a, b∈ ⟨↑,↓⟩ such that x (resp.
x′) letters of a and y (resp. y′) letters of b are equal to ↓ (resp. ↑). The space
HomOS(z,t)(a, b) is zero unless r :=x′ +y =x +y′, so we may assume that is the case.
Let a :↑x′
→ a↑x be the unique morphism that consists of x nested rightward cups
on top of x′ vertical upward strands. Let b :↑yb→↑y′
be the unique morphism that
consists of y nested rightward caps on top of y′ vertical strands. The linear map
θ : HomOS (z,t)(a, b)→ HomOS (z,t)(↑r,↑r), (3.12)
ORIENTED SKEIN CATEGORY 19
f↦→(b⊗ 1↑x)◦ (1↑y⊗f⊗ 1↑x)◦ (1↑y⊗a)
has an obvious two-sided inverse, hence, it is a vector space isomor phism. For example,
taking a =↓↑↓↑ and b =↑↓, the map θ sends
↦→ .
Since Ψ is a monoidal functor, there is an isomorphism
φ : HomUq(gln)(Ψ( a), Ψ( b))
∼
→ HomUq (gln)((V +)⊗r, (V +)⊗r),
g↦→(Ψ(b)⊗ 1⊗x
V + )◦ (1⊗y
V +⊗g⊗ 1⊗x
V + )◦ (1⊗y
V +⊗ Ψ(a))
making the following diagram commute:
HomOS (z,t)(a, b)
∼
−−−−→
θ
HomOS (z,t)(↑r,↑r)
ır
←−−−−Hr
Ψ
↓
↓ Ψ
HomUq(gln)(Ψ( a), Ψ( b))
∼
−−−−→
φ
HomUq (gln)((V +)⊗r, (V +)⊗r).
(3.13)
The composition r : Hr→ EndUq (gln)((V +)⊗r) of ır and the right hand Ψ is a ho-
momorphism studied in [J] in the context of “quantized Schur-Weyl r eciprocity.” It is
shown there that r is surjective. Hence, the right hand Ψ is surjective. The commu-
tativity of the diagram then implies the analogous statement for the left hand Ψ.
As Rep Uq(gln) is additive Karoubian, the functor Ψ extends to a full functor
˙Ψ : ˙OS(z,t ) → RepUq(gln). Let N be the tensor ideal of ˙OS (z,t ) of negligible
morphisms. Since Rep Uq(gln) is absolutely semisimple, ˙Ψ induces a fully faithful func-
tor ¯Ψ : ˙OS (z,t )/N→ RepUq(gln) by the argument from the proof of [De, Th´ eor` eme
6.2]. This functor is also dense since every object of Rep Uq(gln) is a summand of some
tensor product of the modules V + and V−. So it is a monoidal equivalence.
To complete the proof, we need to show that N is generated as an additive k -linear
tensor ideal of ˙OS (z,t ) by the morphism ın+1(e(1n+1)). It suﬃces to show that the
kernel1 of the original functor Ψ is the k -linear tensor ideal I ofOS (z,t ) generated
byın+1(e(1n+1)). Jimbo’s results show that the homomorphism r introduced above is
injective when r≤n, and that ker r is the ideal of Hr generated by e(1n+1) (viewed as
an element of Hr via the natural embedding Hn+1֒→Hr) when r >n. In particular,
takingr =n + 1, this shows that Ψ( ın+1(e1n+1)) = 0, so Ψ induces a monoidal functor
˜Ψ : OS (q,qn)/I→ RepUq(gln). The commuting diagram (3.13) becomes
HomOS (z,t)/I(a, b)
∼
−−−−→
˜θ
HomOS (z,t)/I(↑r,↑r)
˜ır
←−−−−Hr/Ir
˜Ψ
↓
↓ ˜Ψ
HomUq(gln)(Ψ( a), Ψ( b))
∼
−−−−→
φ
HomUq(gln)((V +)⊗r, (V +)⊗r),
where Ir :={0} if r≤ n and Ir :=⟨e(1n+1)⟩ if r > n. The isomorphism ˜θ in this
diagram is deﬁned in the same way as θ, indeed, it is induced by θ in an obvious way.
Also when r>n the map ır takese(1n+1)∈Hr to↑r−n−1ın+1(e(1n+1)). This morphism
lies inI, showing that ır induces the homomorphism ˜ır indicated in the diagram. Now
the composition of ˜ır and the right hand ˜Ψ is an isomorphism. Also it is obvious from
1W e mean the tensor ideal of OS(z, t ) deﬁned by the kernels of the maps Ψ : Hom OS (z,t )(a, b)։
HomUq(gln)(Ψ( a), Ψ( b)) for all a, b ∈ ⟨↑, ↓⟩.
