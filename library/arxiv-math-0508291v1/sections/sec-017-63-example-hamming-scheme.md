---
doc_id: arxiv-math-0508291v1
doc_title: "Stein’s Method and Random Character Ratios"
section_id: sec-017-63-example-hamming-scheme
section_title: "Example: Hamming Scheme"
section_number: 6.3
pages: 49-50
source_pdf: 0508291v1.pdf
source_sha256: d2d541426aaec742
doc_brief: "Stein’s Method and Random Character Ratios — Stein’s method is used to prove limit theorems for random character ratios."
---
of Subsection 6.2 for the Hamming scheme H(d,q ), where d,q are positive
integers and q ≥ 2.
To begin we recall the deﬁnition of H(d,q ) and its basic properties, refer-
ring the reader to Chapter 3 of [BaI] for more details. The ele ments X of
H(d,q ) are d-tuples of numbers chosen from {1, · · ·,q }; clearly |X| =qd. A
pair (x,y ) is in Ri if x and y diﬀer in exactly i coordinates. For 0 ≤i ≤d,
one has that vi = (q − 1)i( d
i
)
and µi = (q − 1)i( d
i
)
. Thus the Plancherel
measure on {0, · · ·,d } chooses i with probability
(q−1)i(d
i)
qd . The numbers
φs(i) are equal to
s∑
j=0
(−1)j (q − 1)s−j
( i
j
)( d −i
s −j
)
.
The polynomial φs in the variable i is known as a q-Krawtchouk polynomial.
In what follows W = φ 1(i)√v1
, where i is chosen from Plancherel measure
of the Hamming scheme H(d,q ). The Hamming graph has vertex set X
and an edge between two vertices if they diﬀer in one coordinat e. Thus the
eigenvalues of the adjacency matrix of the Hamming graph are φ1(i) with
multiplicityµi, which motivates the study of W . Hora [Ho2] shows that if
d → ∞ andq/d → 0, then W converges in distribution to a normal random
variable with mean 0 and variance 1.
In fact since W (i) = (q−1)d−qi√
(q−1)d and µ i
|X| =
(q−1)i(d
i)
qd , it is straightforward
that W has the same distribution as
Y1 + · · · +Yd√
(q − 1)d
,
where the Y ’s are independent random variables, each equal to q − 1 with
probability 1
q and to −1 with probability 1 − 1
q . Hence the Berry-Esseen
theorem [Du] shows that W satisﬁes a central limit theorem with the error
term C
√
q
d where C is a small explicit constant.
For comparison, let us study W using Theorem 6.12 with s = 1 and t = 1.
Then a = q
(q−1)d and one computes that p2(0) = 1
(q−1)d , p2(1) = (q−2)
(q−1)d , and
p2(2) = 1 − 1
d . The ﬁrst term in the error term of Theorem 6.12 is then
computed to equal
√
(q−2)2
(q−1)d , which is less than
√
q
d . The second term in the
error term of Theorem 6.12 is computed to equal
(
2q2
π (q−1)d
) 1/ 4
, which is at
most
(
2q
d
) 1/ 4
. Thus one obtains a central limit theorem for W with error
term
√
q
d +
(
2q
d
) 1/ 4
.
To close this section, it is shown how our exchangeable pair c an be used to
giveO(d−1/ 2) bounds for q ﬁxed. The key is Lemma 6.13, which shows that
50
the Markov chain L1 is actually a birth-chain and computes its transition
probabilities.
Lemma 6.13. The Markov chain L1 on the set {0, · · ·,d } is a birth-death
chain with transition probabilities
L1(i,j ) =





i
d(q−1) if j =i − 1
i
d
(
1 − 1
q−1
)
if j =i
1 − i
d if j =i + 1
Proof. Recall that L1(i,j ) = µ j
|X|
∑ n
r=0
φ r(i)φ r(1)φ r (j)
(vr)2 . From the formula for
φr(l) one sees that
φr(l) = (q − 1)r−l
( d
r
)
( d
l
) φl(r)
for any 0 ≤r,l ≤d. Thus
L1(i,j ) = µj
|X|d
( d
i
)( d
j
)
(q − 1)i+j+1
n∑
r=0
( d
r
)
(q − 1)rφ1(r)φi(r)φj(r).
From page 152 of [MaSl], there is a recurrence relation
(i + 1)φi+1(r) = [(d −i)(q − 1) +i −qr]φi(r) − (q − 1)(d −i + 1)φi−1(r).
Since φ1(r) = d(q − 1) −qr, the recurrence is equivalent to
φ1(r)φi(r) = i(q − 2)φi(r) + (i + 1)φi+1(r) + (q − 1)(d −i + 1)φi−1(r).
Applying this to expression for L1(i,j ) at the end of the previous paragraph,
the result follows from Lemma 6.2. □
Lemma 6.13 implies that |W ′ −W | ≤ A with A = q√
(q−1)d . Thus one
can apply the version of Theorem 6.12 which would arise by usi ng Theorem
2.2 instead of Theorem 2.1. Recalling that a = q
(q−1)d , one obtains an error
term of
√
q
d + . 41q2+1. 5q√
(q−1)d . For q ﬁxed this goes as d−1/ 2.
