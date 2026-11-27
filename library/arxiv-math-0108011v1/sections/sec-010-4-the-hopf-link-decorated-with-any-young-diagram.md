---
doc_id: arxiv-math-0108011v1
doc_title: "The Homfly polynomial of the decorated Hopf link"
section_id: sec-010-4-the-hopf-link-decorated-with-any-young-diagram
section_title: "The Hopf link decorated with any Young diagrams"
section_number: 4
pages: 13-21
source_pdf: 0108011v1.pdf
source_sha256: e4af4b5d3c5ff6cd
toc_source: inferred
doc_brief: "The Homfly polynomial of the decorated Hopf link — The main goal is to ﬁnd the Homﬂy polynomial of a link formed by decorating each component of the Hopf link with the closure of a directly oriented"
---
diagrams
We now in principle have a means of ﬁnding ⟨ck, λ⟩by calculating the Schur
function sλ(Eck(t)). This in turn gives the coeﬃcients for the series Eλ(t),
whose Schur function sµ ﬁnally gives ⟨λ, µ⟩. The aim of this section is to give a
simple formula for the series Eλ(t) = P⟨λ, ci⟩ti/ ⟨λ⟩as a product of the known
series E∅(t) =
P ⟨ci⟩ti and a rational function of t, in theorem 4.5. To do this
we specialise the coeﬃcients so that Eck(t) becomes a polynomial, and we can
apply the classical determinantal formulae for Schur functions. By comparing
the coeﬃcients in Eλ(t) with those of our proposed product formula, and
showing that they agree under suﬃciently many of the specialisations we are
able to deduce that they are identical.
The determinantal formulae which appear give us a very attractive ex-
pression for the specialised versions of the invariants ⟨λ, µ⟩, which we describe
in theorem 4.2.
4.1
The sl(N) substitution
We use the substitution v = s−N to deﬁne a ring homomorphism from our
coeﬃcient ring Λ to the ring of Laurent polynomials in s with denominators
sr −s−r. Denote the image of ⟨X, Y ⟩by ⟨X, Y ⟩N, and the image of ⟨X⟩by
⟨X⟩N.
The element tλ(Y ) for Y ∈C is an element of Λ. Applying the homo-
morphism to the equation ⟨λ⟩tλ(Y ) = ⟨λ, Y ⟩from lemma 1.1 shows that if
⟨λ⟩N = 0 then ⟨λ, Y ⟩N = 0 also, for any Y .
13
We make use of some results of Macdonald to help in our evaluations.
In exercise I.3.3 of [7] Macdonald observes that when a power series can be
expressed as
E(t) =
∞
Y
i=0
1 + aqit
1 + bqit
then its Schur function sλ is given in terms of the cells x ∈λ by the formula
sλ = qn(λ) Y
x∈λ
a −bqcn(x)
1 −qhl(x) ,
(9)
where cn(x) is the content of x, determined by its position, hl(x) is its hook
length, determined by its relation to other cells of λ and n(λ) is given by
2n(λ) =
X
x∈λ
1 + cn(x) −hl(x).
The coeﬃcients of the series ⟨P crtr⟩= P ⟨cr⟩tr were shown in chapter 4
of [1] to satisfy the simple recursive relation
⟨cr+1⟩= v−1s−r −vsr
sr+1 −s−r−1 ⟨cr⟩,
leading to the product formula
X
⟨cr⟩tr =
∞
Y
i=0
1 + vs2i+1t
1 + v−1s2i+1t.
(10)
Applying Macdonald’s formula (9) gives
⟨λ⟩= sλ
DX
crtrE
= qn(λ) Y
x∈λ
vs −v−1sqcn(x)
1 −qhl(x)
(11)
taking q = s2, a = vs and b = v−1s. This can be rewritten in the form
⟨λ⟩=
Y
x∈λ
v−1scn(x) −vs−cn(x)
shl(x) −s−hl(x)
,
(12)
which can equally be derived by skein theory for ⟨Qλ⟩from [10], without
assuming that Qλ can be expressed as a Schur function.
It is clear that the specialisation v = s−N gives
⟨λ⟩N = 0
⇐⇒
some cell x ∈λ has content −N
⇐⇒
λ has > N parts.
(13)
Consequently when N ≥l(λ) we can always write tλ(Y )N = ⟨λ, Y ⟩N
⟨λ⟩N
.
14
Lemma 4.1 Let λ be a Young diagram and let N ≥l(λ). Then the special-
isation EN
λ (t) is a polynomial in t of degree ≤N.
Proof :
We must show that tλ(cr)N = 0 for r > N. Since ⟨λ⟩N̸ = 0 it is
enough to show that ⟨λ, cr⟩N = 0 for r > N.
By (13) we know that ⟨cr⟩N = 0 for r > N, and so
⟨cr, λ⟩N = tcr(λ)N ⟨cr⟩N = 0.
The result follows since ⟨λ, cr⟩= ⟨cr, λ⟩.
✷
We now ﬁnd a factorisation of this polynomial EN
λ (t) into linear factors in
lemma 4.3, and use the Schur function sµ(EN
λ (t)) to derive a determinantal
formula for ⟨λ, µ⟩N in theorem 4.2.
Recall ﬁrst the determinantal description of the Schur function
sλ(x1, . . . , xN) = sλ
 N
Y
i=1
(1 + xit)
!
.
For ﬁxed N ≥l(λ) deﬁne the index set
Iλ = {λ1 + N −1, λ2 + N −2, . . . , λN}
consisting of N distinct integers ≥0.
Number the columns of the N × ∞matrix






1
x1
x2
1
· · ·
1
x2
x2
2
· · ·
...
...
...
...
1
xN
x2
N
· · ·






starting with 0, so that its (i, j) entry is xj
i.
Write P N
λ (x) for the N × N minor determined by the columns Iλ. The
leading minor is P N
∅(x), and the Schur function is given by
sλ(x1, . . . , xN) = P N
λ (x)/P N
∅(x).
(14)
The formula for ⟨λ, µ⟩N can be found in terms of a function of q = s2
deﬁned similarly by N × N minors of the inﬁnite Vandermonde matrix
V =











1
1
1
1
1
· · ·
1
q
q2
q3
q4
· · ·
1
q2
q4
q6
q8
· · ·
1
q3
q6
q9
q12
· · ·
1
q4
q8
q12
q16
· · ·
...
...
...
...
...
...











15
with (i, j) entry qij, numbering both rows and columns from 0.
Deﬁnition.
For partitions λ, µ with l(λ), l(µ) ≥N take index sets Iλ and
Iµ as above and deﬁne P N
(λ,µ) to be the N × N minor of V with rows indexed
by Iµ and columns by Iλ.
Theorem 4.2
⟨λ, µ⟩N = s(1−N)(|λ|+|µ|)P N
(λ,µ)/P N
(∅,∅).
Proof :
Using formula (14) for the Schur function, applied to the rows Iµ of
V , we can write
sλ

Y
i∈Iµ
(1 + qit)

= P N
(λ,µ)/P N
(∅,µ).
(15)
In particular
P N
(λ,∅)/P N
(∅,∅) = sλ
 N−1
Y
i=0
(1 + qit)
!
.
We ﬁrst derive a formula for the polynomial EN
λ (t) in the next lemma.
Lemma 4.3
Y
i∈Iλ
(1 + qit) = EN
λ (sN−1t),
giving
EN
λ (t) =
N
Y
j=1
(1 + sN+2λj−2j+1t).
To ﬁnish the proof of theorem 4.2 we use equation (15), lemma 4.3 and
lemma 2.1 to get
P N
(λ,µ)/P N
(∅,µ) = sλ

Y
i∈Iµ
(1 + qit)


=
sλ(EN
µ (sN−1t))
=
s(N−1)|λ|sλ(EN
µ (t))
=
s(N−1)|λ|⟨λ, µ⟩N/ ⟨µ⟩N
and
P N
(µ,∅)/P N
(∅,∅) = sµ(EN
∅(sN−1t) = s(N−1)|µ| ⟨µ⟩N .
Multiply the two expressions to get
P N
(λ,µ)/P N
(∅,∅) = s(N−1)(|λ|+|µ|)⟨λ, µ⟩N.
16
The formula claimed in theorem 4.2 for ⟨λ, µ⟩N in terms of the N × N
minors of the Vandermonde matrix follows at once.
✷
Proof of lemma 4.3:
We begin by establishing theorem 4.2 directly in the case µ = ck. The
index set Ick is
Ick = {N, N −1, . . . , N −k + 1, N −k −1, . . . , 2, 1, 0} = I∅∪{N} −{N −k}.
Recall that equation (11) gives
E∅(t) =
X
r≥0
⟨cr⟩tr =
∞
Y
i=0
1 + vs2i+1t
1 + v−1s2i+1t.
The substitution v = s−N reduces this to the ﬁnite product
EN
∅(t) =
N−1
Y
i=0
(1 + s−N+2i+1t).
Then
EN
∅(sN−1t) =
N−1
Y
i=0
(1 + s2it) =
Y
i∈I∅
(1 + qit).
(16)
Let k be an integer, k ≤N. By corollary 3.3 we have
Eck(t) =
1 + v−1st
1 + v−1s−2k+1tE∅(t).
Substituting v = s−N in the above equation gives
EN
ck(sN−1t)
=
1 + s2Nt
1 + s2N−2ktEN
∅(sN−1t)
=
Y
i∈Ick
(1 + qit).
(17)
Now sλ
Q
i∈Ick(1 + qit)

= P N
(λ,ck)/P N
(∅,ck), by (15). Consequently
P N
(λ,ck)/P N
(∅,ck) = sλ(EN
ck(sN−1t))
and
P N
(ck,∅)/P N
(∅,∅) = sck(EN
∅(sN−1t)).
17
Since sλ(EN
ck(t)) = ⟨λ, ck⟩N/ ⟨ck⟩N by lemma 2.1, we can multiply the two
expressions to get
P N
(λ,ck)/P N
(∅,∅)
=
sλ(EN
ck(sN−1t))sck(EN
∅(sN−1t))
=
s(N−1)|λ|⟨λ, ck⟩N
⟨ck⟩N
s(N−1)|ck| ⟨ck⟩N
=
s(N−1)(|λ|+|ck|)⟨λ, ck⟩N.
(18)
To complete the proof of lemma 4.3 it is enough to show that
sck

Y
i∈Iλ
(1 + qit)

= sck(EN
λ (sN−1t))
for all k ≤N, so as to compare the coeﬃcients of the two polynomials.
By (15) we have sck
Q
i∈Iλ(1 + qit)

= P N
(ck,λ)/P N
(∅,λ), while
sck(EN
λ (t))
=
⟨λ, ck⟩N/ ⟨λ⟩N
=
s(1−N)|ck|P N
(λ,ck)/P N
(λ,∅)
by (18).
Since P N
(ck,λ) = P N
(λ,ck) and sck(EN
λ (sN−1t)) = s(N−1)|ck|sck(EN
λ (t)) the re-
sult follows.
✷
We now deduce a formula for the power series Eλ(t) with coeﬃcients in
the two variables s and v from the formula for EN
λ (t) in lemma 4.3.
Theorem 4.4 We have
Eλ(t) =
l(λ)
Y
j=1
1 + v−1s2λj−2j+1t
1 + v−1s−2j+1t E∅(t)
for any Young diagram λ.
Proof :
For any integer N ≥l(λ) we have EN
λ (sN−1t) = Q
i∈Iλ(1 + qit) by
lemma 4.3. Now
Iλ = I∅∪l(λ)
j=1 {λj + N −j} −∪l(λ)
j=1{N −j}.
Hence
EN
λ (sN−1t) =
l(λ)
Y
j=1
1 + qλj+N−jt
1 + qN−jt EN
∅(sN−1t)
18
and so
EN
λ (t)
=
l(λ)
Y
j=1
1 + s2(λj+N−j)s1−Nt
1 + s2(N−j)s1−Nt EN
∅(t)
=
l(λ)
Y
j=1
1 + sN+2λj−2j+1t
1 + sN−2j+1t
EN
∅(t).
This means that the two power series Eλ(t) and
l(λ)
Y
j=1
1 + v−1s2λj−2j+1t
1 + v−1s−2j+1t E∅(t)
agree for every substitution v = s−N with N ≥l(λ). Since the coeﬃcients
are Laurent polynomials in v it follows that the two power series are equal
when v is treated as an indeterminate.
✷
When we apply theorem 4.4 to the case λ = ck and compare the result
with corollary 3.3 we note a number of cancellations in
l(λ)
Y
j=1
1 + v−1s2λj−2j+1t
1 + v−1s−2j+1t .
In our ﬁnal theorem we give a simpler expression for the rational function
Eλ(t)/E∅(t), in terms of the Frobenius notation λ = (a1, . . . , ad(λ)|b1, . . . , bd(λ))
for the partition λ. As in [7] recall that the Frobenius notation describes λ
in terms of the lengths {ai} of the ‘arms’ and {bi} of the ‘legs’ of its Young
diagram, counting right or down from the d(λ) cells on the main diagonal.
Thus ai = λi −i and bi = λ∨
i −i for i = 1, . . . , d(λ).
Theorem 4.5 We have
Eλ(t) =
d(λ)
Y
i=1
1 + v−1s2ai+1t
1 + v−1s−2bi−1tE∅(t)
for any Young diagram λ = (a1, . . . , ad(λ)|b1, . . . , bd(λ)) in Frobenius notation.
Proof :
The result follows from exactly the same argument as in theorem
4.4 once we observe that we can write the index set Iλ as
Iλ = I∅∪d(λ)
i=1 {N + ai} −∪d(λ)
j=1{N −bj −1}.
19
To conﬁrm this, write ai = λi −i, bj = λ∨
j −j for all i, j ≤N. Then
ai ≥0
⇐⇒
i ≤dλ,
bj ≥0
⇐⇒
j ≤dλ.
The integers ai, 1 ≤i ≤N are all distinct, and Iλ = {N + ai, i ≤N}. Since
N + ai ≥N ⇐⇒i ≤dλ there are exactly dλ numbers in Iλ which are not
in I∅, and hence dλ numbers in I∅which are not in Iλ. We can identify these
as {N −bj −1 : j ≤dλ} by showing that
N −bj −1̸ = N + ai, for any i, j ≤N.
Consider the cell in row i and column j, 1 ≤i, j ≤N, in relation to the
Young diagram λ. If the cell lies in λ then λi ≥j and λ∨
j ≥i. Add these to
get ai + bj ≥0 and so ai + bj̸ = −1. Otherwise λi ≤j −1 and λ∨
j ≤i −1,
giving ai + bj ≤−2 and again ai + bj̸ = −1.
This completes the proof; indeed the rational function
d(λ)
Y
i=1
1 + v−1s2ai+1t
1 + v−1s−2bi−1t = Eλ(t)/E∅(t)
admits no further cancellation, since the exponents of s in the numerator are
all positive, while those in the denominator are negative.
✷
Having used this result to get the power series for Eλ(t) with explicit
coeﬃcients in Λ, the general invariant ⟨λ, µ⟩is then found by calculating
Schur functions of the series, using the formula
⟨λ, µ⟩= sµ(Eλ(t)) ⟨λ⟩.
Remark.
The rational function above can be expressed in terms of the
content polynomial Cλ(t) deﬁned by
Cλ(t) =
Y
x∈λ
(1 + qcn(x)t).
It is easy to check, by decomposing λ as a disjoint union of simple hooks
based on the diagonal cells, that
d(λ)
Y
i=1
1 + v−1s2ai+1t
1 + v−1s−2bi−1t = Cλ(v−1st)/Cλ(v−1s−1t).
This leads to an alternative proof of theorem 4.5 using theorem 3.10 of [9],
once it is established that the product of the Gyoja-Aiston idempotent eλ,
with |λ| = n, and the polynomial EM(t), whose coeﬃcients are the ele-
mentary symmetric functions of the Murphy operators in Hn, satisﬁes the
equation
EM(t)eλ = Cλ(t)eλ.
20
