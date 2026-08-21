---
doc_id: aif-2009-59-1-347-0
doc_title: "On q-summation and confluence"
section_id: sec-012-32-q-integral-and-continuous-integral
section_title: "q-integral and continuous integral"
section_number: 3.2
pages: 31-34
source_pdf: AIF_2009__59_1_347_0.pdf
source_sha256: 35b8422990e24888
doc_brief: "On q-summation and confluence — 18 sections: Introduction; Part 1. Convergent q-Borel and q-L; Convergent q-Euler series"
---
Although both Eq(x) and E [λ]
q are solutions of the q-diﬀerence equation
x2dqy +y = x, they have a deeply diﬀerent nature. In fact, while Eq(x)
is meromorphic on the whole Riemann surface ~C∗ of the logarithme, the
function E [λ]
q is a uniform function: more precisely, it is analytic on C∗
minus a spiral of simple poles.
Let us consider the projection:
π : ]0 , +∞[×R ∼= ~C∗ − → C∗
(r,α ) ↦− → re2iπα
.
Of course, we can identify E [λ]
q to its pull back via π on ~C∗, i.e. to a mero-
morphic function on~C∗, and study the solution Eq(x)−E [λ]
q ofx2dqy+y = 0.
We have the following result (we identify all meromorphic function on C∗
to their pull back on ~C∗):
Proposition 3.6. — Let λ ∈ C∗ \ (−qZ). For any:
x ∈ ˜Ωλ :=π−1 (C∗ \ [−λ(1 −p);q]),
we have:
Eq(x) − E [λ]
q (x) = −2πiq − 1
lnq
(
L(−λ(1−p))∗,q∗ (x∗) −Cλ,q
)
eq(−q/x)−1,
ANNALES DE L’INSTITUT FOURIER
ON q-SUMMATION AND CONFLUENCE 377
where we have used the following notation:
x∗ =e−2πi log x
ln q , q ∗ =e4π2/ ln q,
La,q(x) = −x
a
θ′
p(− x
a )
θp(− x
a ) =𝓁p
(x
a
)
, C λ,q =L(−λ(1−p))∗,q∗ ((1 −p)∗).
Since La,q( x
a′ ) = Laa′,q(x) = 𝓁p( x
aa′ ) and (xx′)∗ = x∗(x′)∗, the theorem
above can be rephrased in the following statement:
Corollary 3.7. — Let p∗ = 1/q∗ =e−4π2/ ln q. Then
Eq(x) − E [λ]
q (x) =
− 2πiq − 1
lnq
[
𝓁p∗
((
− x
λ(1 −p)
)∗)
−𝓁p∗
((
− 1
λ
)∗)]
eq(−q/x)−1.
The proof of Proposition 3.6 is based on the following two lemmas:
Lemma 3.8. — Letλ ∈ C∗ \ (−pZ) and ˜Ωλ :=π−1(C∗ \ [−λ(1 −p);q]) ⊂
˜C∗. For any x ∈ ˜Ωλ we set:
Uλ(x) = ( Eq(x) − E [λ](x))eq(−q/x).
Then
Uλ(xe2πi) −Uλ(x) = −2πiq − 1
lnq
and
Uλ(qx) = Uλ(x).
Proof. — The proof follows from Lemma 3.4, taking into account the
functional equation of eq(−q/x):
eq(−q/x) =
(
1 − q − 1
x
)
eq(−1/x)
□
Lemma 3.9. — Let a ∈ C∗ and consider the function La,q deﬁned for
x ∈ C∗ \ [a;q] as above, i.e. :
La,q(x) = 𝓁p
(x
a
)
= −x
a
θ′
p(− x
a )
θp(− x
a ).
Then, up to an additive constant,La,q is the only solution of the q-diﬀerence
equationy(qx)−y(x) = 1 , which is analytic on C∗ \aqZ and has only simple
poles at aqZ.
TOME 59 (2009), F ASCICULE 1
378 Lucia DI VIZIO & Changgui ZHANG
Proof. — The functional equation for La,q is obtained deriving the equa-
tion − x
aθp(−p x
a ) = θp(− x
a ). The uniqueness (up to a constant) comes from
the remark that there are no non constant elliptic function having only a
simple pole in a fundamental domain. □
Proof of Proposition 3.6. — Let us consider the modular variable change:
q ↦− →q∗ =e4π2/ ln q, x ↦− →x∗ =e−2πi log x
ln q .
In the notation of Lemma 3.8 above let W (x∗) = Uλ(x). Then:
W (x∗q∗) −W (x∗) = −2πiq − 1
lnq , W (x∗e−2πi) = W (x∗).
Equivalently,x∗ ↦→ W (x∗) represents a uniform solution to a ﬁrst order
q∗-diﬀerence equation. By Lemma 3.9, there exists a constant C ∈ C such
that
W (x∗) = −2πiq − 1
lnq L(−λ(1−p))∗,q∗ (x∗) +C, x ∈ ˜Ωλ.
We calculate the constant C =Cλ,q settingx = 1 −p andx∗ =e−2πi ln(1−p)
ln q .
Since eq(−q/x) has a zero for x = 1 −p, we obtain the exact expression
for C. □
The main result of this section is:
Theorem 3.10. — For any x ∈ C∗\] − ∞, 0[ we have:
Eq(x) = 1
lnq
∫ q
1
E [λ]
q (x)dλ
λ .
The theorem follows from the combination of Corollary 3.7 and the fol-
lowing lemma:
Lemma 3.11. — Let p∗ = 1/q∗ = e− 4π2
ln q. For z close enough to 1, we
have: ∫ q
1
𝓁p∗
((
− z
λ
)∗)dλ
λ =
∫ q
1
𝓁p∗
((
− 1
λ
)∗)dλ
λ .
Proof. — Let µ = −λ−1. From the identity x∗ = e−2πi log x
ln q we deduce
that:
dλ
λ = −dµ
µ = − lnq
2πi
dµ∗
µ∗ .
Therefore for t =µ∗ we obtain:
∫ q
1
𝓁p∗
((
− z
λ
)∗)dλ
λ = lnq
2πi
∫
C(−z)∗
𝓁p∗ (t)dt
t ,
ANNALES DE L’INSTITUT FOURIER
