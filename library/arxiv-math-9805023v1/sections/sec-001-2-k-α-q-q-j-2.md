---
doc_id: arxiv-math-9805023v1
doc_title: "q-LAGUERRE POL YNOMIALS AND BIG q-BESSEL"
section_id: sec-001-2-k-α-q-q-j-2
section_title: "(k− α )(q; q)∞ J (2)"
section_number: 2
pages: 5-7
source_pdf: 9805023v1.pdf
source_sha256: ea8758b2a2bf9d85
doc_brief: "q-LAGUERRE POLYNOMIALS AND BIG q-BESSEL — The q-Laguerre polynomials correspond to an indetermined moment probl em."
---
α (2√c q
1
2 k; q)
and a similar expression for V q− 1
2 α
k (0). We recall the deﬁnition of Jackson’s q-Bessel
function, see [8]:
(2.9) J (2)
α (x; q) := (qα +1; q)∞
(q; q)∞
( x
2
)α
0ϕ1
( −
qα +1 ; q, −qα +1 x2
4
)
.
Remark. It follows from Lemma 2.2(i) that L has deﬁciency indices (1 , 1) for q
1
2 < |t| <
q− 1
2 , t ⁄= ±1, and that the deﬁciency space N± i = {u ∈ ℓ2(Z) | Lu = ±i u} is spanned by
U (±i).
The Wronskian for two sequences ( uk)k∈ Z and ( vk)k∈ Z is given by
(2.10) [ u, v]k := ak
(
uk+1vk − ukvk+1
)
.
It is independent of k if u and v are two solutions to Lu = x u, so that we may denote it
by [ u, v].
5
Lemma 2.3. We have the following Wronskians:
[V t(x), V t− 1
(x)] =
√c
t (t2, qt− 2 − 1/c, −cq; q)∞ ,
[U (x), V t(x)] = ct− 1 (x)
−t√c .
Proof. The ﬁrst Wronskian follows by combining (2.10) with Lemma 2. 2(ii) and letting
k → ∞ using (2.7). The second Wronskian follows from the ﬁrst and ( 2.4) for ±t /∈ {q
1
2 m |
m ∈ Z}. Next use analytic continuation with respect to t. □
So we ﬁnd that for x ∈ C\R the solution U (x) and V t− 1
(x) of Lu = x u are linearly
independent for x ∈ C\R. Moreover, U (x) is ℓ2 for k → −∞ and this determines U (x)
up to a constant by the considerations in the ﬁrst paragraph o f this section. Furthermore
V t− 1
(x) is ℓ2 for k → ∞ for |t| > q
1
2 , and for |t| ≥ q− 1
2 this condition determines V t− 1
(x)
up to a constant.
3. Spectral resolution.
In case |t| > q
1
2 we see V t− 1
(x) is ℓ2 for k → ∞ by Lemma 2.2(ii). From now on
we assume that |t| > q
1
2 . In case |t| ≥ q− 1
2 we moreover have that L is self-adjoint. The
domain of L is given by {u ∈ ℓ2(Z) | Lu ∈ ℓ2(Z)}. In case, q
1
2 < |t| < q − 1
2 , t ⁄= ±1, the
deﬁciency indices of L are (1 , 1), so that all extensions of L to a self-adjoint operator are
parametrised by U (1) = T. In this case, we ﬁx the self-adjoint extension such that V t− 1
is
contained in the domain, which is always possible since Ni = N− i because of ak, bk ∈ R.
See Dunford and Schwartz [6, Ch. XII] for more information.
Deﬁne the Green function for x ∈ C\R by
Gx(m, n) :=









Un(x)V t− 1
m (x)
[U (x), V t− 1
(x)] , for n ≤ m,
Um(x)V t− 1
n (x)
[U (x), V t− 1
(x)] , for n > m ,
so that
(
(x − L)− 1f
)
m = ∑ ∞
n=−∞ Gx(m, n) fn. For the resolution of the identity E for L,
i.e. L =
∫
R t dE(t), we now have, see [6, Ch. XII],
⟨E
(
(a, b)
)
v, w⟩ = lim
δ↓0
lim
ε↓0
1
2πi
∫ b− δ
a+δ
⟨(s − iε − L)− 1v, w⟩ − ⟨(s + iε − L)− 1v, w⟩ds.
Now observe that
⟨(s ± iε − L)− 1v, w⟩ =
∑
n≤ m
Un(s ± iε)V t− 1
m (s ± iε)
[U (s ± iε), V t− 1
(s ± iε)]
vn ¯wm + vm ¯wn
2 .
Since V t− 1
m (x) is an entire function of x, and Un(x) is analytic in C\{0} we see that
the measure ⟨E
(
(a, b)
)
v, w⟩ has only discrete mass points at the zeros of the Wronskian
6
[U (x), V t− 1
(x)]. By Lemma 2.3 this corresponds to the zeros of ct(x) which are the points
ηp = −√cqp/t, p ∈ Z≥ 0, and ξp = tqp/√c, p ∈ Z. So the spectrum of L is {ηp | p ∈
Z≥ 0} ∪ {ξp | p ∈ Z} ∪ {0}, and it remains to show that 0 is not in the point spectrum of
