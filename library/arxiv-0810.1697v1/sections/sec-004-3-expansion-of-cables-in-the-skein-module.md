---
doc_id: arxiv-0810.1697v1
doc_title: "ON THE CABLE EXPANSION FORMULA QIHOU LIU"
section_id: sec-004-3-expansion-of-cables-in-the-skein-module
section_title: "Expansion of cables in the skein module"
section_number: 3
pages: 5-8
source_pdf: 0810.1697v1.pdf
source_sha256: 1aef66179da3c154
doc_brief: "ON THE CABLE EXPANSION FORMULA QIHOU LIU — In this paper, a generalized version of Morton’s formula [8] is proved."
---
In this section, the framing convention is assumed.
Let M be the standard solid torus D × S1, the link L, which is to be considered,
consists of two components: K1 is given by
(ρ exp(iqθ), exp(ipθ))|0≤θ≤2π
where p, q are coprime integers, 0 < ρ < 1; K2 is the core of the solid torus
(0, exp(iθ))|0≤θ≤2π
Here D is identiﬁed with the unit disk in the complex plane and S1 with the unit
circle.
Fix the framing of K2 to be 0. The framing σ of K1 corresponds to some integer.
By abuse of notation, it is also denoted by σ. Denote the color of K1 by N . Denote
the color of K2 by s. Assume they are nonnegative. ⟨eN , es⟩L is some element of
S(D × S1). Denote it by T N
σ (p, q; s).
As an element of S(D × S1), T N
σ (p, q; s) can be expressed as a linear combination
of the basis elements {el}|l≥0. The coeﬃcients before el is denoted by gl
σ(p, q; s),
i.e.
T N
σ (p, q; s) =
∑
l≥0
gl
σ(p, q; s)el
Note the range of l is not restricted except that l ≥ 0. These coeﬃcients are all
0 but for ﬁnitely many l’s.
First some simple cases:
(1) If (p,q)=(0,1),then it follows from the second example in 2.1.2 that with
σ = 0
gl
σ(0, 1; s) = δls(−1)N [(N + 1)(s + 1)]
[s + 1]
.
(2) If (p,q)=(1,0), we have two parallel strings, one with color s, th e other with
color N. It’s clear from the multiplication formula of en’s that for framing
σ = 0, gl
σ(1, 0; s) = 1 if (l,s,N) is an admissible triple, and gl
σ(1, 0; s) = 0
otherwise. By introducing the δ-function, which is δ(0) = 1 and δ(m) = 0
for nonzero m, we can encode these phrases into a formula
gl
σ(1, 0; s) =
N∑
k=−N
k+N even
{δ(l − s − k) − δ(l + s + 2 + k)}
(3) If we change the framing σ of the cable, by the remark in 2.1.2, we just add
an overall phase factor to each of the g,s, i.e.
gl
σ+b(p, q; s) = ( −1)bN Ab(N 2+2N )gl
σ(p, q; s)
(4) Since (-p,-q) represents the same cable as (p,q) does, we shall always assume
p > 0.
The approach to calculate g,s for general (p,q) are quite straightforward. We
start from (1,0), then calculate the case(1,q), then (q,1), then ( q,1 + bq), then
(1 + bq,q)... Formally, we express q
p as a continued fraction
q
p = a0 + 1
a1
+
1
a2
+ ... +
1
aγ
6 QIHOU LIU
and then use induction on γ.
This is made possible by the following two lemmas.
Lemma 1.
gl
σ(p, q + p; s) = ( −1)l+sA−s2−2s+l2+2lgl
σ′ (p, q; s)
Proof. Since to get the (p,q+p)-cable from a (p,q)-cable, one simply apply De hn
twist once around the meridian. And it follows from the remark in 2.1.2. The phase
factor appear because twisting has changed the framing of the co re string of the
solid torus as well. □
Now how to make transition from (q,p) to (p,q)? We use a multi-linear br acket
associated to the following link in S3: L = K1 ∪ K2 ∪ K3
each component has 0 framing. Let H be the Hopf link. We have
⟨x1, x2, x3⟩L = ⟨x1 · x2, x3⟩H
where x1 · x2 is the multiplication in S(D × S1).
Let r be a positive integer, and
ωr =
r−1∑
t=0
(−1)t[t + 1]et
then for r > m > 0, we have
⟨em, ωr⟩H ≡ 0
and
⟨e0, ωr⟩H ≡ ⟨ωr⟩U
where U is the unknot with framing 0, equivalence means equal at A = exp
(
πi
2(r+1)
)
.
See Lemma 13.9 from Lickorish’s book [4].
Thus for r > 2l ≥ 0, r > 2k ≥ 0, we have
⟨el, ek, ωr⟩L = ⟨el · ek, ωr⟩H
=
∑
m
(k,l,m) admissible
⟨em, ωr⟩H
≡
∑
m
(k,l,m) admissible
δ(m)⟨ωr⟩U
CABLE EXPANSION 7
Thus we have
(*) ⟨el, ek, ωr⟩L ≡ δ(l − k)⟨ωr⟩U
Then
(**) ⟨el, T σ(p, q; s), ωr⟩L ≡ gl
σ(p, q; s)⟨ωr⟩U
Let L1 be the second example mentioned in 2.1.2, we have
⟨el, et⟩L1 = (−1)l [(l + 1)(t + 1)]
[t + 1] et
Map D × S1 to a tubular neighborhood of K3, we have
⟨el, T σ(p, q; s), ωr⟩L = ⟨Tσ(p, q; s), ⟨el, ωr⟩L1⟩H
= ⟨Tσ(p, q; s),
r−1∑
t=0
(−1)t[t + 1]⟨el, et⟩L1⟩H
= ⟨Tσ(p, q; s),
r−1∑
t=0
(−1)l+t[(t + 1)(l + 1)]et⟩H(***)
=
Now we can go on. We have a link Tσ(p, q; s) in the tubular neighborhood N (K2)
of the second component K2 of L, which consists of a string at the core of the solid
torus, surrounded by a (p,q)-cable. Let’s push this (p,q)-cable oﬀ to the boundary,
and push it a little further so that it slides into the world on the other s ide of the
boundary torus. Observe that S3 − N (K2) is still a solid torus, since K2 is the
unknot. The meridian of the N (K2) becomes a longitude when viewed from the
other side, and the longitude we chose becomes a meridian of S3 − N (K2). And
we push the cable further into N (K3), then the (p,q)-cable becomes (q,p)-cable in
N (K3).
So
(****)
⟨Tσ(p, q; s),
r−1∑
t=0
(−1)l+t[(t+1)(l+1)]et⟩H = ⟨es,
r−1∑
t=0
(−1)l+t[(t+1)(l+1)]Tσ(q, p; t)⟩H
Then we expand Tσ(q, p; t) on the right hand side, note that
⟨es, ek⟩H = (−1)s+k[(s + 1)(k + 1)]
in this way get a relation between gl
σ(p, q; s) and gk
σ(q, p; t).
We summarize (**),(***),(****) into the following lemma.
8 QIHOU LIU
Lemma 2.
(−1)l+sgl
σ(p, q; s)⟨ωr⟩
≡
r−1∑
t=0
∑
k≥0
(−1)k+tgk
σ(q, p; t)[(t + 1)(l + 1)][(s + 1)(k + 1)]
here equivalence means equal at A = exp
(
πi
2(r+1)
)
. Note that in this formula g(p, q)
and g(q, p) have the same framing.
Using the two lemmas and the formula for (p,q)=(1,0), we can now writ e down
the general formula for g,s.
Theorem 1. Assume p > 0,let ǫ, β, α be such that ǫ = [ q
p ], q = ǫp + β with
0 ≤ β < p , α = p · β.Then for framing σ = pq, we have
gl
σ(p, q; s) = ( −1)qN Aǫ(−s2−2s+l2+2l)
×
N∑
k=−N
k+N even
Aαk2+2βk(s+1){δ(l − s − pk) − δ(l + s + 2 + pk)}
It seems to be complicated. But note there’re at most two nonzero terms in this
summation. Since for each value of k, the summand is nonzero only if l − s − pk = 0
or l + s + 2 + pk = 0.
Theorem 2. Substitute the expression for g’s to the expansion of Tσ(p, q; s), we
have
Tσ(p, q; s) = ( −1)qN
N∑
k=−N
k+N even
Apqk2+2qk(s+1)epk+s
Proof of theorem 2. Substitute the expression for g’s, then change the order of sum-
mation. Also note that el = −e−l−2 and e−1 = 0. □
