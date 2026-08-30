---
doc_id: arxiv-math-0611941v3
doc_title: "HECKE ALGEBRAS OF FINITE TYPE ARE CELLULAR MEINOLF GECK"
section_id: sec-006-4-examples-and-applications-to-modular-represent
section_title: "Examples and applications to modular representations"
section_number: 4
pages: 11-15
source_pdf: 0611941v3.pdf
source_sha256: bf6f2d55c7adee51
doc_brief: "HECKE ALGEBRAS OF FINITE TYPE ARE CELLULAR MEINOLF GECK — Let H be the one-parameter Hecke algebra associated to a ﬁnite Weyl gr oup W , deﬁned over a ground ring in which “bad” primes for W are"
---
Throughout this section, we assume that Lusztig’s conjectures o n Hecke algebras with
unequal parameters hold; see §2.4. (Recall that this is the case, for example, if the weight
function L is a positive multiple of the length function.) We now discuss examples an d
applications of Theorem 3.1.
Example 4.1. Assume that L(s) > 0 for all s ∈ S and that λ ∈ Λ is such that dim Eλ =
dλ = 1. Then there exists a group homomorphism η : W → {± 1} and a weight function
m : W → Z such that Tw acts on Eλ
v via the A-algebra homomorphism
µ λ : H → A, T w ↦→η(w)vm(w).
By [25, Prop. 20.6], the corresponding representation of J is given by
tw ↦→
{ (−1)l(w) ˆnw ˆnw−1 η(w) if aλ + m(w) = 0 ,
0 otherwise .
(Note that a factor ˆnw ˆnw−1 should be inserted into the formula in [25, 20.6].) Clearly, we can
take Bλ = (1) in this case. Hence, the unique element of the cellular basis corr esponding to
λ is given by
C λ
1,1 =
∑
w∈W
aλ +m(w)=0
(−1)l(w) η(w) c†
w.
For example, if Eλ is the unit representation, we have η(w) = 1 and m(w) = L(w) for all
w ∈ W ; furthermore, aλ = 0 and so C λ
1,1 = c†
1 (since L(w) > 0 for all w ⁄= 1).
If Eλ is the sign representation, we have η(w) = ( −1)l(w) and m(w) = −L(w) for all
w ∈ W . Furthermore, aλ = L(w0) where w0 ∈ W is the longest element; see [25, 20.18].
Since L(w) < L(w0) for all w ⁄= w0, we obtain C λ
1,1 = c†
w0 in this case.
Example 4.2. Assume that there are no L-bad primes for W , that is, we have fλ = 1 for
all λ ∈ Λ. Then we claim that there are signs δw = ±1 ( w ∈ W ) such that
{δw c†
w | w ∈ W } is a cellular basis .
This is seen as follows. Let Γ be a left cell of W and [Γ] = ⟨tx | x ∈ Γ ⟩Q ⊆ JQ. Then [Γ] is a
simple left ideal of JQ; see [25, Chap. 21] and [8, Cor. 4.8]. Hence [Γ] aﬀords an irreducible
representation of JQ, and all irreducible representations arise in this way. So, for any λ ∈ Λ,
we can choose a left cell Γ λ such that [Γ λ] ∼
= Eλ
♠. Let us write
Γ λ = {xs | s ∈ M(λ)} for λ ∈ Λ .
12 MEINOLF GECK
Then {txs | s ∈ M(λ)} is a basis of [Γ λ] and the corresponding matrix coeﬃcients are
ρλ
st(tw) = γw,xt,x−1
s
for w ∈ W and s, t ∈ M(λ).
By (P7) in [25, 14.2] and [25, Prop. 13.9], we have
γw,xt,x−1
s
= γx−1
t ,w−1,xs = γw−1,xs,x−1
t
.
This implies that ρλ(tw−1) = ρλ(tw)tr for all w ∈ W . Thus, if we take for Bλ the identity
matrix of size dλ, then the conditions in Proposition 2.6 are satisﬁed. Furthermore, for ﬁxed
s, t ∈ M(λ), the Schur relations now read:
∑
y∈W
(
γy,xt,x−1
s
) 2
=
∑
y∈W
ρλ
st(ty) ρλ
ts(ty−1) = fλ = 1.
We deduce that there is a unique w = wλ(s, t) ∈ W such that γw,xt,x−1
s
⁄= 0; in fact, we have
γw,xt,x−1
s
= ±1. Now the formula in Theorem 3.1 reads
C λ
s,t =
∑
y∈W
ˆny ˆny−1 γy−1,xs,x−1
t
c†
y =
∑
y∈W
ˆny ˆny−1 γy,xt,x−1
s
c†
y
= ˆnw ˆnw−1 γw,xt,x−1
s
c†
w = δw c†
w,
where w = wλ(s, t) and δw = ±1. Thus, {δw c†
w | w ∈ W } is a cellular basis, as claimed.
The above assumptions are satisﬁed for W of type An where L is a positive multiple of the
length function; see [25, 22.4]. Thanks to a geometric interpretatio n of the basis {cw}, we
know that hx,y,z ∈ Z/greaterorequalslant0[v, v −1] for all x, y, z ∈ W ; see [25, Chap. 15] and the references there.
Hence we also have ˆnx /greaterorequalslant0 and γx,y,z /greaterorequalslant0 for all x, y, z ∈ W . So, in this case, {c†
w | w ∈ W }
is a cellular basis of H, as originally pointed out by Graham–Lehrer [16, Example 1.2]. Note
that another cellular structure in type An was constructed by Murphy [26], [27], using purely
combinatorial methods. The exact relation between the two cellular structures is determined
in [9].
Example 4.3. Let W be the Weyl group of type B2 where S = {s1, s 2} and ( s1s2)4 = 1.
Let L : W → Z be any weight function such that L(si) > 0 for i = 1 , 2. If L(s1) ⁄= L(s2),
then there are no L-bad primes for W . Furthermore, by [12], [10], Lusztig’s conjectures hold
in this case. (More generally, they hold for a certain class of weight f unctions in type Bn for
any n /greaterorequalslant2.) Hence, in this case, {δwc†
w | w ∈ W } is a cellular basis by Example 4.2. By [10,
Cor. 6.4], we actually have δw = 1 for all w ∈ W .
Now assume that L(s1) = L(s2) = 1 (“equal parameter case”). Then 2 is the only bad
prime. We have Irr( W ) = {1, ε 1, ε 2, ε, r } where 1 is the unit representation, ε is the sign
representation, ε1, ε2 have dimension one, and r has dimension two. The a-invariants are
HECKE ALGEBRAS OF FINITE TYPE ARE CELLULAR 13
a1 = 0, aε1 = aε2 = ar = 1 and aε = 4. A cellular basis as in Theorem 3.1 is given as follows:
C 1
1,1 = c†
1, C r
1,1 = c†
s1 + c†
s1s2s1,
C ε
1,1 = c†
w0, C r
1,2 = −2c†
s1s2,
C ε1
1,1 = c†
s2 − c†
s2s1s2, C r
2,1 = −2c†
s2s1,
C ε2
1,1 = c†
s1 − c†
s1s2s1, C r
2,2 = 2c†
s2 + 2c†
s2s1s2.
Indeed, by Example 4.1, we already know that c†
1 and c†
w0 belong to the cellular basis. Now
consider the two further one-dimensional representations. We ﬁ x the notation such that
ε1(Ts1) = ε2(Ts2) = v and ε1(Ts1) = ε2(Ts2) = −v−1. Using the formula in Example 4.1,
we obtain the above expressions for C ε1
1,1 and C ε2
1,1. Finally, consider the two-dimensional
representation r. We have to determine a corresponding representation of J such that the
conditions in Proposition 2.6 hold. Now, the basis elements {cw} are explicitly determined
in [25, Prop. 7.3]. From this, one easily deduces the left cells. They are given by
{1}, {s1, s 2s1, s 1s2s1}, {s2, s 1s2, s 2s1s2}, {w0 = s1s2s1s2};
see [25, 8.7]. Furthermore, one ﬁnds the following relations in J. We have t2
1 = t1 and
t1tx = 0 for x ⁄= 1; we have t2
w0 = tw0 and tw0tx = 0 for x ⁄= w0. Furthermore,
t2
s1 = ts1, t s1ts1s2 = ts1s2, t s1ts1s2s1 = ts1s2s1,
t2
s2 = ts2, t s2ts2s1 = ts2s1, t s2ts2s1s2 = ts2s1s2,
ts1s2ts2s1 = ts1 + ts1s2s1, t s1s2ts2s1s2 = ts1s2,
ts2s1ts1s2 = ts2 + ts2s1s2, t s2s1ts1s2s1 = ts2s1,
ts1s2s1ts1s2s1 = ts1, t s2s1s2ts2s1s2 = ts2.
All other products txty are either zero or can be deduced from the above list using the
formulas γx,y,z = γy−1,x−1,z−1 (see [25, Prop. 13.9]) and γx,y,z = γy,z,x (see (P7) in [25, 14.2]).
Note also that, by (P8) in [25, 14.2], we have γx,y,z = 0 unless x ∼L y−1, y ∼L z−1 and
z ∼L x−1. Now one readily checks that the following assignments deﬁne an irre ducible
two-dimensional representation of JQ:
t1 ↦→
[ 0 0
0 0
]
, t s1 ↦→
[ 1 0
0 0
]
, t s2s1 ↦→
[ 0 0
−1 0
]
, t s1s2s1 ↦→
[ 1 0
0 0
]
,
ts2 ↦→
[ 0 0
0 1
]
, t s1s2 ↦→
[ 0 −2
0 0
]
, t s2s1s2 ↦→
[ 0 0
0 1
]
, t w0 ↦→
[ 0 0
0 0
]
.
Finally, taking for Bλ the diagonal matrix with diagonal entries 1 and 2, we see that all the
conditions in Proposition 2.6 are satisﬁed. This yields the expressions for the basis elements
C r
s,t where 1 ⩽ s, t ⩽ 2.
14 MEINOLF GECK
Example 4.4. Following Graham–Lehrer [16], we deﬁne cell representations of H as follows.
Fix λ ∈ Λ and let W (λ) be a free A-module with basis {Cs | s ∈ M(λ)}. Then W (λ) is an
H-module with action given by
h.C s =
∑
s′∈M (λ)
rh(s′, s) Cs′ for h ∈ H and s ∈ M(λ).
There is a symmetric bilinear form gλ : W (λ) × W (λ) → A deﬁned by
gλ(Cs, C t) = rh(s, s) where s, t ∈ M(λ) and h = C λ
s,t;
see [16, Def. 2.3]. We have gλ(h.C s, C t) = gλ(Cs, h ∗.C t) for all s, t ∈ M(λ) and h ∈ H; see [16,
Prop. 2.4]. Using the formula for rh(s′, s) in the proof of Theorem 3.1, and a computation
analogous to that in the proof of [25, Prop. 20.6], it is straightforwa rd to check that
vaλ gλ(Cs, C t) ≡ fλ β λ
st mod vR[v].
In particular, we can see from this expression that the determinan t of the Gram matrix of
gλ is non-zero. (This fact also follows from the general theory of cellu lar algebras, since HK
is known to be split semisimple.)
Now let K be the ﬁeld of fractions of A; we write HK = K ⊗A H and WK(λ) = K ⊗A W (λ).
Since gλ induces a non-degenerate form on WK(λ) for each λ ∈ Λ, we have
Irr(HK) = {WK(λ) | λ ∈ Λ }; see [16, Theorem 3.8] .
In fact, by the formula for rh(s′, s) in the proof of Theorem 3.1, we see that the action of
H on W (λ) is obtained by pulling back the action of J on Eλ
♠ via Lusztig’s homomorphism
φ : H → JA. This shows that WK(λ) ∼= Eλ
v ; see [25, 20.2, 20.3].
Now let θ: A → k be any ring homomorphism where k is a ﬁeld. By extension of scalars,
we obtain a k-algebra Hk = k ⊗A H and cell representations Wk(λ) = k ⊗A W (λ) ( λ ∈ Λ),
which may no longer be irreducible. Denoting by gλ
k the induced bilinear form on Wk(λ), we
set Lλ = Wk(λ)/ rad(gλ
k ). Then, by [16, Theorem 3.4], each Lλ is either 0 or an absolutely
irreducible representation of Hk, and we have
Irr(Hk) = {Lµ | µ ∈ Λ ◦} where Λ ◦ = {λ ∈ Λ | Lλ ⁄= 0}.
Denote by [ Wk(λ) : Lµ] the multiplicity of Lµ as a composition factor of Wk(λ). Then
(∆)
{
[Wk(µ) : Lµ] = 1 for any µ ∈ Λ ◦,
[Wk(λ) : Lµ] = 0 unless λ ≼ µ (i.e., λ = µ or aµ < aλ);
see [16, Prop. 3.6]. Thus, the decomposition matrix
D =
(
[Wk(λ) : Lµ]
)
λ∈Λ ,µ∈Λ ◦
has a lower unitriangular shape, if the rows and columns are ordered according to increasing
a-value.
The relations (∆) show that the subset Λ ◦ ⊆ Λ deﬁnes a “canonical basic set” in the sense
of [11, Def. 4.13], which itself is an axiomatization of the results obtain ed earlier by Rouquier
HECKE ALGEBRAS OF FINITE TYPE ARE CELLULAR 15
and the author [7], [15]. Note that the deﬁnition of “canonical basic s ets” only requires the
invariants aλ (with respect to L) and the general set-up of Brauer’s theory of decomposition
numbers for associative algebras. Explicit descriptions of these “basic sets ” are now known
