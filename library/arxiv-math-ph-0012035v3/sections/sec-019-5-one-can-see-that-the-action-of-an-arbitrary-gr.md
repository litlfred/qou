---
doc_id: arxiv-math-ph-0012035v3
doc_title: "Non-Abelian Stokes theorem in action"
section_id: sec-019-5-one-can-see-that-the-action-of-an-arbitrary-gr
section_title: "One can see that the action of an arbitrary group element g ∈ G on |R⟩"
section_number: 5
pages: 18-21
source_pdf: 0012035v3.pdf
source_sha256: 06a4c8096c8ebb10
doc_brief: "Non-Abelian Stokes theorem in action — In this short review main issues related to the non-Abelian S tokes theorem have been addressed."
---
is given by
g |R⟩ = ξh |R⟩ = ξ |R⟩eiφ(h).
The combination
|ξ, R⟩
def
= ξ |R⟩
is the general group deﬁnition of the coherent states. For simplicit y, we
will denote the coherent states as |g, R⟩.
The coherent states |g, R⟩are generally non-orthogonal but normalized to unity,
⟨g, R |g, R⟩ = 1.
Furthermore, for an appropriately normalized measure dµ(g), we have a very
important for our furher analysis identity the, so-called, resolutio n of unity
∫
|g, R⟩dµ(g) ⟨g, R| = I. (19)
18
Path integral Our ﬁrst aim is to calculate the “transition amplitude” between
the two coherent states |g′, R⟩ and |g′′, R⟩
⟨
g′′, R
⏐
⏐
⏐
⏐
⏐P exp
[
i
∫ t′′
t′
A(t) dt
] ⏐
⏐
⏐
⏐
⏐g′, R
⟩
= lim
N →∞
∫
. . .
∫
⟨gN , R |(1 + iǫAN)| gN −1, R⟩dµ(gN −1)
⟨gN −1, R |(1 + iǫAN −1)| gN −2, R⟩dµ(gN −2)
. . . dµ(g1) ⟨g1, R |(1 + iǫA1)| g0, R⟩, (20)
where we have used 16 and 19. To continue, one should evaluate a sin gle am-
plitude (i.e. the amplitude for an inﬁnitesimal “time” ǫ), i.e.
⟨gn, R |(1 + iǫAn)| gn−1, R⟩
= ⟨gn, R|gn−1, R⟩+ i ⟨gn, R |An| gn−1, R⟩ǫ.
Now
⟨gn, R|gn−1, R⟩ = ⟨g(tn), R|g(tn−1), R⟩
=
⟨
R
⏐
⏐g†(tn)g(tn−1)
⏐
⏐R
⟩
=
⟨
R
⏐
⏐g†(tn)g(tn − ǫ)
⏐
⏐R
⟩
=
⟨
R
⏐
⏐g†(tn)
[
g(tn) − ˙g(tn)ǫ + O
(
ǫ2)]⏐
⏐R
⟩
=
⟨
R
⏐
⏐g†(tn)g(tn)
⏐
⏐R
⟩
−
⟨
R
⏐
⏐g†(tn) ˙g(tn)
⏐
⏐R
⟩
ǫ + O
(
ǫ2)
= 1 −
⟨
R
⏐
⏐g†(tn) ˙g(tn)
⏐
⏐R
⟩
ǫ + O
(
ǫ2)
,
whereas
i ⟨gn, R |An| gn−1, R⟩ǫ = i ⟨g(tn), R |A(tn)| g(tn−1), R⟩ǫ
= i
⟨
R
⏐
⏐g†(tn)A(tn)g(tn − ǫ)
⏐
⏐R
⟩
ǫ
= i
⟨
R
⏐
⏐g†(tn)A(tn)g(tn)
⏐
⏐R
⟩
ǫ + O
(
ǫ2)
.
Then
⟨gn, R |(1 + iǫAn)| gn−1, R⟩
= 1 −
⟨
R
⏐
⏐g†(tn) ˙g(tn)
⏐
⏐R
⟩
ǫ + i
⟨
R
⏐
⏐g†(tn)A(tn)g(tn)
⏐
⏐R
⟩
ǫ + O
(
ǫ2)
= exp
[⟨
R
⏐
⏐−g†(tn) ˙g(tn) + ig†(tn)A(tn)g(tn)
⏐
⏐R
⟩
ǫ + O
(
ǫ2)]
.
19
Returning to 20
⟨
g′′, R
⏐
⏐
⏐
⏐
⏐P exp
[
i
∫ t′′
t′
A(t) dt
] ⏐
⏐
⏐
⏐
⏐g′, R
⟩
=
∫
[Dµ(g)] exp
(
i
∫ t′′
t′
L dt
)
,
where the “lagrangian” appearing in the path integral is deﬁned as
L =
⟨
R
⏐
⏐[
ig†(t) ˙g(t) + g†(t)A(t)g(t)
] ⏐
⏐R
⟩ def
= ⟨R |Ag(t)| R⟩, (21)
and
[Dµ(g)] =
∏
t′<t<t′′
dµ[g(t)].
According to [HU00], wee can transform L in Eq.21 to the form originally
proposed by [DP89]. Namely, for any Lie-algebra element K we have in the
Cartan basis 18
⟨R |K| R⟩ =
⟨
R
⏐
⏐
⏐
⏐
⏐
∑
i
λiHi + . . .
⏐
⏐
⏐
⏐
⏐R
⟩
=
∑
i
λi ⟨R |Hi| R⟩,
where dots mean E∓α generators vanishing between |R⟩’s. Since
Hi |R⟩ = mi |R⟩,
then
∑
i
λi ⟨R |Hi| R⟩ =
∑
i
λi ⟨R |Ri| R⟩ =
∑
i
λimi
= 1
κ
∑
i
miTr(HiK) = 1
κTr(m · H K),
where the normalization
Tr(HiHj) = κδij
has been assumed. Thus,
L = ⟨R |Ag(t)| R⟩
= 1
κ
∑
i
Tr [miHiAg(t)]
= 1
κTr
{
m · H
[
ig†(t) ˙g(t) + g†(t)A(t)g(t)
]}
. (22)
20
Non-Abelian Stokes theorem Finally, the LHS of the non-Abelian Stokes
theorem reads ∫
Dµ(g) exp
(
i
∮ t′′
t′
L dt
)
,
where
Dµ(g) =
∏
t′≤t<t′′
dµ[g(t)],
and g(t′) = g(t′′). Or, in the language of diﬀerential forms
∫
Dµ(g) exp
(
i
∮
C
L
)
,
where now
Dµ(g) =
∏
x∈C
dµ[g(x)],
and
L = 1
κ
∑
i
Tr [m · HAg
i (x)] dxi def
= Bi dxi
with
Ag
i (x) = ig†(x)∂ig(x) + g†(x)Ai(x)g(x),
Ag(t) = Ag
i [x(t)] dxi(t)
dt .
Here Bi is an Abelian diﬀerential form, so obviously
∫
Dµ(g) exp
(
i
∮
C=∂S
B
)
=
∫
Dµ(g) exp
(
i
∫
S
dB
)
.
