---
doc_id: arxiv-1403.4021v2
doc_title: "MARKOV TRACES ON THE BIRMAN-WENZL-MURAKAMI ALGEBRAS"
section_id: sec-008-52-restrictions-to-3-strands-and-the-ocneanu-tra
section_title: "Restrictions to 3 strands, and the Ocneanu trace"
section_number: 5.2
pages: 21-24
source_pdf: 1403.4021v2.pdf
source_sha256: 046d02411e0dc086
doc_brief: "MARKOV TRACES ON THE BIRMAN-WENZL-MURAKAMI ALGEBRAS — We classify the Markov traces factoring through the Birman-Wenzl-Murakami (BMW) algebras."
---
MT 3(M) was deﬁned in section 2. We note that
tH
3 (1) =
(y + 1
x
)2
tH
3 (s1) = y + 1
x tH
3 (s1s2) = 1
and deﬁne additional elements tS
3 , tK
3 of MT 3(M) by
tS
3 (1) =a3, t S
3 (s1) =tS
3 (s1s2) = 0, t S
3 ((s1s−1
2 )2) =x2(2a +x),
tK
3 (1) =δ2
K, t K
3 (s1) =δK, t K
3 (s1s2) = 1, δ K = y2−ax +y
xy ,
tK
3 ((s1s−1
2 )2) =x3y(y + 1) +x2(y2 + 2a + a
y )−x(1 +y)− (y +a + a
y ).
Proposition 5.5. Lett∈MT 3(M) factorizing through ~BMW 3.
(i) The trace t is uniquely determined by t(1), t(s1) =t(s2) and t(s1s2).
(ii) If x(a2−y2) is invertible in M then t is uniquely determined by t(1) and t(s1s2).
(iii) If x2(a2−y) is invertible in M then t is uniquely determined by t(s1) and t(s1s2).
(iv) If x(a2−y2) and x2(a2−y) are invertible in M then t is uniquely determined by
t(s1s2).
Proof. Lett∈MT 3(M) factorizing though ~BMW 3. With the notations of proposition 2.5 we
writet =αe∗
1 +βe∗
2 +γe∗
3 +δe∗
4. By direct calculation, we check that the equation t(R1s1) = 0
means
0 =−x2(
a2 +ax +y
)
α + x
(
2 (y + 1)a3 + 2x (y + 1)a2 +a
(
x2 +y (y + 1)
)
+yx
)
a β
+− (y + 1)2a3−x (y + 1)2a2 +a
(
−x2− 2x2y +y
(
y2 +y + 1
))
−yx (y + 1)
a γ +y2δ
and, since y is invertible, this proves that t is determined by α,β and γ, meaning that t
is uniquely determined by t(1), t(s1) and t(s1s2), which proves (i). Similarly, we get that
t(s−1
1 R1) = 0 reads
(a2−y2) (xt(s1)− (y + 1)t(s1s2)) = 0
and t(R1) = 0 means
x2(a2−y)t(1) = (a2−y)(y + 1)−x(y− 1)a
a (xt(s1)− (y + 1)t(s1s2)) +x
a(y + 1)(a2−y)t(s1)
which easily implies (ii)-(iv). □
Corollary 5.6. Let (tn) be a Markov trace factoring through ( ~BMW n) with values in M. If
x(a2−y2) and x2(a2−y) are invertible in M then (tn) is a multiple of (tH
n ) composed with
some morphism R→M.
Proof. Immediate consequence of (iv) together with proposition 5.2. □
Recall that S† =S/(a2−y) =R[x−1]/(a2−y) and BMW†
n = ~BMW n⊗RS†.
Proposition 5.7. Let t′
n be the composite of tn with M → M⊗R S†[(y− 1)−1]. Then
(t′
n) is a scalar multiple of the composite of tH
n with some morphism R → M and with
M→M⊗RS†[(y− 1)−1].
22 Ivan Marin & Emmanuel Wagner
Proof. Inside S†[(y− 1)−1] we have a2−y2 = y(1−y), hence by proposition 5.5 (ii) we
have that t′
3 is uniquely determined by t′
3(1) and t′
3(s1s2), and more precisely the equation
t′
3(s−1
1 R1) = 0 means t′(s1) = y+1
x t′(s1s2). Let t◦
n =t′
n−t′
3(s1s2)tH
n . Then t◦
3(s1s2) = 0 hence
t◦
3(s1) = 0 and therefore t◦
3 =a−3t◦
3(1)tS
3 . Let τ =t◦
4◦ι3, where ι3 : ~BMW 3→ ~BMW 4 is the
natural map. Again by 5.5 (ii) we know that τ is uniquely determined by τ(1) and τ(s1s2).
Moreover τ(s1s2) = t◦
4(s1s2) = t◦
4(s2s3) = t◦
3(s2) = tS
3 (s2) = 0. It follows that τ(s1) = 0,
since τ(s1) = y+1
x τ(s1s2). But τ(s1) = t◦
4(s1) = t◦
4(s3) = t◦
3(1), hence t3(1) = 0 and t◦
3 = 0.
We prove by induction on n that t◦
n(1) = 0. Assume we know that t◦
r(1) = 0 for all r≤ n,
and consider the composite τ of t◦
n+1 with the natural map ~BMW 3→ ~BMW n+1. We have
τ(s1s2) =t◦
n+1(s1s2) =t◦
n+1(sn−1sn) =t◦
n−1(1) = 0. It follows as before that τ(s1) = 0, hence
t0
n(1) = t0
n+1(sn) = t0
n+1(s1) = τ(s1) = 0. It follows that t◦
n(1) = 0, and the claim follows by
induction because of proposition 5.1. □
5.3. The Kauﬀman trace. Recall that we deﬁned in§3 two Markov tracest±
n :BMW±
n →
S±. Using the Chinese Remainder Theorem isomorphism S≃S+⊕S− they can be patched
together into a Markov trace BMW n⊗R S → S, which extends to a Markov trace tK
n :
~BMW n→S.
BMW n⊗RS+ //BMW +
n
t+
n //S+

BMW n⊗RS
66
((
tK
n //S
BMW n⊗RS− //BMW−
n t−
n
//S−
@@
Note that the value of tK
3 ((s1s−1
2 )2) deﬁne before indeed matches this new deﬁnition, be-
cause of the computation of the Kauﬀman invariant of the ﬁgure-eight knot we did in section
3.
Proposition 5.8. Lett′
n be the composite of tn with M→M⊗RS[(a2−y)−1]. Then (t′
n) is
a linear combination of the composites of tH
n and tK
n with some morphism S→M⊗RS[(a2−
y)−1].
Proof. By proposition 5.2 we know that t′
n is uniquely determined by t′
1(1) = t′
3(s1s2) and
t′
2(1) =t′
3(s1). It is thus suﬃcient to show that tH
3 and tK
3 induce a basis of (S[(a2−y)−1])2
under t′
3↦→ (t′
3(s1s2),t′
3(s1)). The corresponding 2 × 2 matrix has for determinant
⏐⏐⏐⏐
δH 1
δK 1
⏐⏐⏐⏐ =δH−δK = a
y∈ (S[(a2−y)−1])×
with δH = y+1
x , and this concludes the proof. □
Remark 5.9. It is well-known that both the Kauﬀman polynomial and the HOMFLYPT
polynomial both specialize to the Jones polynomial (see e.g. [13] p. 180). It could have been
expected that this coincidence would have appeared in the previous proposition. It clearly does
not, since any specialized value of the invariants deﬁned by our traces tH
n and tK
n cannot
MARKOV TRACES ON THE BMW-ALGEBRAS 23
coincide on the 2-components unlink (we always have δH ⁄= δK). What happens is that,
according to [13] proposition 16.6, the tracetK
n provides the Jones polynomial when specialized
toα =−t
−3
4 ,q =t
1
4 , that is a =q−6,b =−q−2 =−t
−1
2 ,c =−q−4 =−t−1 while, according to
[13] proposition 16.5,tH
n provides the Jones polynomial when{b,c} is specialized to{−t
1
2,t
3
2},
and the only value of t for which these two parametrizations coincide is t
1
2 =−1, in which
case we get b +c = 0, which is forbidden here.
5.4. An additional trace when y =a2 = 1. Let S†† =S/(a2− 1,y− 1) =S†/(a2−y2) =
S/(a2−y), and BMW††
n = ~BMW n⊗RS††.
We ﬁrst deal with the very special case x =−2a.
Proposition 5.10. Let (xn)n≥1 denote a sequence with values in some S††-module satisfying
(x + 2a)M = 0. Then there exists a Markov trace (tX
n ) on ( ~BMW n) with values in M such
that, for every braid g, tX
n (g) = x#ˆg, where ˆg denotes the closure of the braid g and #L
denotes the number of components of the link L. Moreover, every Markov trace on ( ~BMW n)
with values in M is of that form.
Proof. We ﬁrst note that the relations ( si−a)(s2
i + 2asi + 1) = (si−a)(si +a)2 = (s2
i−
1)(si +a) = 0 hold true in M. Therefore, the action of BMW††
n on M factors through
the group algebra Q [a]/(a2− 1)Sn of the symmetric group. Moreover, the natural map
Hn⊗S††/(x + 2a)→ Q [a]/(a2− 1)Sn, where Hn is the cubic Hecke algebra deﬁned by
(s2
i− 1)(si +a) = 0, is clearly surjective, and R1 is easily checked to map to 0. Therefore,
the map ~BMW n⊗S††/(x + 2a)→ Q [a]/(a2− 1)Sn is surjective.
We show that there exists a Markov trace ( tX
n ) on (( Q [a]/(a2− 1))Sn) fulﬁlling the con-
ditions of the statement. Since the formula tX
n (g) =x#ˆg clearly deﬁnes an invariant of links,
and therefore a Markov trace on the tower of algebras of the braid groups, it is suﬃcient to
prove that tX
n vanishes on the deﬁning ideal of Q [a]/(a2− 1)Sn for any given n. This ideal
is the linear span of the As2
iB−AB for A,B two arbitrary braids on n strands. Since the
closures of As2
iB and AB have the same number of components, we indeed get that ( tX
n ) is
a well-deﬁned Markov trace on ( ~BMW n). Since tX
n (1) =xn, the fact that all Markov traces
are obtained this way is a consequence of proposition 5.1.
□
We can now state a general statement.
Proposition 5.11.
(i) There exists a Markov trace (t††
n ) on ~BMW n with values in S††, given by t††
n (β) =
anψn(β), where ψn : ~BMW n→S†† is an algebra morphism deﬁned by si↦→a.
(ii) Let t′
3 be the composite of t3 with M → M⊗R S††[(a−x)−1, (2a−x)−1]. Then
(t′
3) is a linear combination of the composites of tH
3 , tK
3 , t††
3 with coeﬃcients inside
M⊗RS††[(a−x)−1, (2a−x)−1].
Proof. We ﬁrst check that the R-algebra morphism ψn : Hn→ S†† deﬁned by si↦→ a in-
deed factorizes through ~BMW n, namely that ψn(R1) = 0, by direct calculation. Then
t††
n (x) =anψn(x) clearly deﬁnes a trace for every n, and we need to check the Markov prop-
erty, namely that t††
n+1(xs±1
n ) = t††
n (x) for all x∈ ~BMW n. This holds because t††
n+1(xs±1
n ) =
an+1ψn+1(xs±1
n ) =an+1ψn+1(x)a±1 =an+1ψn(x)a±1 =an+1ψn(x)a =an+2ψn(x) =anψn(x) =
24 Ivan Marin & Emmanuel Wagner
t††
n (x). This proves (i). Note that t††
3 (1) = a3, t††
3 (s1) = a2 = 1, t††
3 (s1s2) = a, We know that
t′
3 is uniquely determined by its value on 1 ,s 1,s 1s2. It has to be a linear combination of tH
3 ,
tK
3 and t††
3 if and only if
∆ =
⏐⏐⏐⏐⏐⏐
a3 a2 a
δ2
H δH 1
δ2
K δK 1
⏐⏐⏐⏐⏐⏐
=a
⏐⏐⏐⏐⏐⏐
a2 a 1
δ2
H δH 1
δ2
K δK 1
⏐⏐⏐⏐⏐⏐
is invertible. Since δH = (y + 1)/x = 2/x, δK = 2
x−a, we get
∆ = 2
x2 (2a−x)(a−x)
whence the conclusion of (ii).
□
We will show below (see corollary 6.12) that part (ii) actually holds true for every n,
provided that x + 2a is also assumed to be invertible.
We note that, when specialized to a ﬁeld, x = a,y = 1,a 2 = 1 imply x∈{− 1, 1}, hence
{b,c} ={−j,−j2} with j = exp( 2iπ
3 ) if a = 1, and {b,c} ={j,j 2} if a =−1 ; likewise,
x = 2a,y = 1,a 2 = 1 imply x∈ {−2, 2}, hence b = c, and b,c ∈ {−1, 1}, hence either
a = b = c = 1 or a = b = c =−1. In these four cases, we have a =±bc, and a possible
additional trace on ~BMW n cannot factorize through BMW±
n , as is immediately checked on
the 12-terms relation (note that, by substracting a linear combination of the two ordinary
traces, we can assume in the ﬁrst two cases that this trace satisﬁes t3(1) = t3(s1) = 0,
t3(s1s2) = 1, while in the latter cases we can assume t3(1) = 1, t3(s1) =t3(s1s2) = 0).
