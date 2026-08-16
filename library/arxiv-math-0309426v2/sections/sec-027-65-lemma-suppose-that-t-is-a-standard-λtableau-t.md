---
doc_id: arxiv-math-0309426v2
doc_title: "ELEMENTARY DIVISORS OF SPECHT MODULES"
section_id: sec-027-65-lemma-suppose-that-t-is-a-standard-λtableau-t
section_title: "Lemma. Suppose that t is a standard λ–tableau. Then"
section_number: 6.5
pages: 12-14
source_pdf: 0309426v2.pdf
source_sha256: f2aa01164d9f243c
doc_brief: "ELEMENTARY DIVISORS OF SPECHT MODULES — 46 sections: MATTHIAS K ¨UNZER AND ANDREW MATHA; Introduction and statement of main; The Hecke algebra and permutation"
---
v′
t =
∑
(a|b)≺t
(−1)k+1−It(a|b)qℓ(d(t′))−ℓ(d(a|b))x(a|b).
Proof. First consider vtλ . Looking at the deﬁnitions we see that
v′
tλ =x(k|n−k)y′
k+1 =xt(k|n−k)
(
1 −q−1Tk +q−2Tk,k−1 − · · · + (−q)−kTk,1
)
=
∑
(a|b)≺tλ
(−q)−ℓ(d(a|b))x(a|b).
As ℓ(d(tλ)′) = ℓ(d(tλ′
)) = 0 and ℓ(d(a|b)) = k + 1 −Itλ (a|b), when ( a|b) ≺ tλ, the
Lemma follows in this case.
Now suppose that t is an arbitrary standard λ–tableaux. If t ⁄= tλ then we can
ﬁnd another standard λ–tableau s and an integer i in the ﬁrst column of s such
that t = sri and ℓ(d(t)) = ℓ(d(s)) − 1. (That is, t ⊵ s where ⊵ is the dominance
order on tableaux; see, for example, [ 10].) Therefore, by induction,
v′
t =v′
sTi =
∑
(a|b)≺s
(−1)k+1−Is(a|b)qℓ(d(s′))−ℓ(d(a|b))x(a|b)Ti.
Since s and t are standard, i is in the ﬁrst column of s and the ﬁrst row of t andi+1
is in the ﬁrst row of s and the ﬁrst column of t. Therefore, if ( a|b) ≺ s then the
entries in the ﬁrst component of ( a|b)ri are still in increasing order and the entries
in the second component are in increasing order unless i andi + 1 both appear in b.
So, ℓ(d(a|b)ri) = ℓ(d(a|b)) + 1 and by Lemma 6.4(ii) we have
x(a|b)Ti =
{
qx(a|b), if i and i + 1 both appear in b,
x(a|b)ri, otherwise.
In the ﬁrst case, when i and i + 1 both appear in b, we have that ( a|b) ≺ t. Also,
thatℓ(d(t′)) −ℓ(d(a|b)) = ℓ(d(s′)) −ℓ(d(a|b)) + 1 andIt(a|b) = Is(a|b) so x(a|b) has
the required coeﬃcient in v′
t.
ELEMENTARY DIVISORS OF SPECHT MODULES 13
In the second case, i appears in a andi+1 appears in b, so ( ari|bri) = ( a|b)ri ≺ t,
It(ari|bri) = Is(a|b) and ℓ(d(t′)) −ℓ(d(a|b)) = ℓ(d(s′)) −ℓ(d(a|b)) + 1. Hence, once
again, x(a|b)ri has the predicted coeﬃcient in v′
t.
As there are exactly k standard (k|n −k)–tableaux ( a|b) satisfying ( a|b) ≺ t,
this completes the proof. □
In order to compute the elementary divisors of S(λ) we need a second basis
of S′(λ). Let
xn−k = 1 +T1 + · · · +T1,n−k−1 =
n−k−1∑
j=0
T1,j.
(Note that r1,0 = 1.) As with y′
k+1, we have x(n−k,1k) =x(1,n−k−1,1k−1)xn−k. Now,
for any standard ( n −k, 1k)–tableau t we deﬁne
w′
t =
{
v′
t(1,n), if n appears in row 1 of t,
v′
tλxn−kTd(t), otherwise.
We remark that it is not obvious that the set of elements {w′
t | t ∈ Std(λ) } is a
basis of S′(λ). We will prove this below.
Lemma 6.5 gives an explicit description of the basis {v′
t}. We need to do the
same for the basis {w′
t}, and for this we need some more notation. If t is a standard
λ–tableau let t∗ = t(1,n ). If ( a|b) is a (k|n −k)–tableau write ( a|b) ≺n t if (a|b) ≺ t
and n is contained in b. Finally, if n appears in the ﬁrst row of t then we deﬁne
(a∗
t |b∗
t ) to be the unique standard ( k|n −k)–tableau such that
(
a∗
t |b∗
t ) ≺ t∗ and n
appears in b∗
t . So
(
a∗
t |b∗
t ) ≺ t∗ and
(
a∗
t |b∗
t ) ≺ t.
6.6. Lemma. Suppose that t is a standard λ–tableau and that n appears in the ﬁrst
row of t. Then
w′
t = (−1)kq2n−2k−3x(a∗
t |b∗
t ) +
∑
(a|b)≺nt∗
rabx(a|b),
for some scalars rab ∈ Z[q,q −1].
Proof. We now argue by downwards induction on t beginning with t = tλ, this is
an unpleasant calculation. Now,
w′
tλ =x(k|n−k)y′
k+1T1,n−1Tn−2,1 = (−1)kx(k|n−k)y′
k+1Tk+1,n−1Tn−2,1
since x(k|n−k)y′
k+1 = x(1k,n−k)y(k+1,1n−k−1). Therefore, using the deﬁnitions to-
gether with the braid relations,
w′
tλ = (−1)kx(k|n−k)y′
k+1Tn−1...T k+2Tk+1,n−1Tk,1
= (−1)kx(k|n−k)Tn−1...T k+2y′
k+1Tk+1,n−1Tk,1
= (−1)kqn−k−2x(k|n−k)y′
k+1Tk+1,n−1Tk,1
