---
doc_id: arxiv-2605.19310v1
doc_title: "A FOURIER-FREE DENSITY-INCREMENT PROOF OF ROTH’S THEOREM MARK LEWKO"
section_id: sec-002-6-mark-lewko
section_title: "MARK LEWKO"
section_number: 6
pages: 6-8
source_pdf: 2605.19310v1.pdf
source_sha256: 047d492babc63d2f
doc_brief: "A FOURIER-FREE DENSITY-INCREMENT PROOF OF ROTH’S THEOREM — We give an elementary, Fourier-free proof of Roth’s theorem."
---
Lemma 7(Dense modular progression).Assume E(f)≥βm 3, with0 <
β≲α 2, and choose an integerℓsatisfying
ℓ∼ βm
α2 ,1≤ℓ<m/2,
where the implicit constant is chosen small enough. Then there exist d∈Z ×
m
andx∈Z m such that
(5.4)S d(x) =
ℓ−1X
i=0
f(x+id)≳ β
αℓ.
Proof.SetM= max d∈Z×
m
Vd. By (5.3) and (5.2),
βℓ3m3≲
X
d∈Z×
m
V 2
d ≤M
X
d∈Zm
Vd≤Mαℓm 2.
Thus there is a nonzero stepdwith
(5.5)V d≳ β
αℓ2m.
We now extract a large positive value of Sd(x). Since|Sd(x)|≤ℓ for every
x∈Z m, the definition of Vd givesVd≤ℓ P
x∈Zm|Sd(x)|. Using (5.5), we get
X
x∈Zm
|Sd(x)|≳ β
αℓm.
AlsoP
x∈ZmSd(x) = ℓP
x∈Zmf(x) = 0. Therefore the total positive mass
of Sd is exactly half of P
x∈Zm|Sd(x)|, and hence some x∈Z m satisfies
(5.4).□
6.Finding a genuine integer progression
We now show how to pass from a density increment on a modular progres-
sion to one on a genuine integer progression.
Lemma 8(Finding a genuine integer progression).Suppose d∈Z ×
m and
x∈Z m satisfyPℓ−1
i=0f(x +id)≥ηℓ for some0 < η≤ 1. If ℓ≳η −2, then
there is an arithmetic progressionP⊂[N]such that
|P|≳η
√
ℓand |A∩P|
|P| ≥α+cη
for an absolute constantc>0.
Proof. We find a short subprogression of the original progression whose step
is represented by a small integer, then intersect it with [N].
Apply the pigeonhole principle to the⌊
√
ℓ⌋+1 elements 0,d, 2d,...,⌊
√
ℓ⌋d
in Zm: two of these have a difference represented by an integer of size
≲m/
√
ℓ. Hence there is an integer q, with 1 ≤q≤
√
ℓ, such that qd is
represented by an integer s with|s|≲m/
√
ℓ. Since m∼N , after enlarging
the absolute constant inℓ≳η −2, we may assume|s|<N.
A FOURIER-FREE DENSITY-INCREMENT PROOF OF ROTH’S THEOREM 7
Taking everyqth term of the original progression gives q subprogressions,
each with step represented by s. Divide each of these into consecutive
progressions of length K∼
√
ℓ, choosing the implicit constant in K small
enough that each subprogression has length at least K and every progression
travels distance<m/ 10 before reduction modulom. Merging any incomplete
final progression into its predecessor, we may assume every progression has
length∼
√
ℓ. These progressions still partition the original ℓ terms. Since
the original average offis at leastη, one block ePsatisfies
X
u∈ eP
f(u)≥η| eP|.
It remains to intersect eP with [N]. On the integer line, the copies of
[N] modulo m are separated by gaps of length m−N > 3m/4, while eP
travels distance < m/10. Thus eP cannot meet [N], leave [N], and later
meet [N] again. Hence the terms of eP lying in [N] form one consecutive
subprogression; call it P . Since f = 0 outside [ N], passing from eP to P
does not change the sum of f. As f≤ 1, we get|P|≥η| eP|≳η
√
ℓ, and the
average of f on P is at least η. Finally, P is an ordinary integer arithmetic
progression: all its terms lie in [ N], and its step is represented by the integer
swith|s|<N. Sincef=1 A−αon [N],
|A∩P|
|P| =α+ 1
|P|
X
u∈P
f(u)≥α+η.
This completes the proof.□
Combining this with Lemma 5 gives the following density increment.
Proposition 9(Density increment).Let A⊂ [N]have density α, and
suppose that A contains no nontrivial three-term arithmetic progression. If
N≳α −32, then there is an arithmetic progressionP⊂[N]such that
|P|≳α 16N 1/2 and |A∩P|
|P| ≥α+cα 11.
Proof. By Lemma 5,E(f)≳α 12m3. Put β∼α 12 and choose ℓ∼βm/α 2∼
α10m. The hypothesis N≳α −32 ensures that such an integer ℓ satisfies
1≤ℓ<m/ 2. Lemma 7 givesd∈Z ×
m andx∈Z m withPℓ−1
i=0f(x+id)≳α 11ℓ.
Set η∼α 11. Again using N≳α −32, we have ℓ≳η −2. Lemma 8 gives an
arithmetic progressionP⊂[N] with density increment≳α 11 and length
|P|≳η
√
ℓ≳α 11α5m1/2≳α 16N 1/2.
□
