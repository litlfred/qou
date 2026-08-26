---
doc_id: arxiv-math-0606435v2
doc_title: "PROPERTIES OF CLOSED 3-BRAIDS"
section_id: sec-030-43-q-polynomial-23
section_title: "Q polynomial 23"
section_number: 4.3
pages: 23-25
source_pdf: 0606435v2 (1).pdf
source_sha256: 6dddaf838a19f0f5
doc_brief: "PROPERTIES OF CLOSED 3-BRAIDS — We show that 3-braid links with given (non-zero) Alexander o r Jones polynomial are ﬁnitely many, and can be effectively determined."
---
Theorem 4.7 (J. Murakami) If L is a closure of a 3-braid β of exponent sum e, then
Q(L,x) = χ(β,
√
t)2 − 1 + 2(x2 + x − 1)
x2(x2 − 3) (ue + e−e) + −x4 − 2x3 + 3x2 + 4x − 4
x2(x2 − 3) χ(β,t) .(25)
Proof of theorem 4.3. We can w.l.o.g. (taking the mirror image) assume that e ≥ 0, and (excluding trivial to check
special cases) that χ ≤ 0. Clearing denominators and absolute terms in (25), we ﬁnd
Q1(L,x) := x2(x2 − 3)(Q(L,x) +1) =
[
ie(−t)−eV (t) + (−t)−e/ 2(−t − 1
t )
]
· (−x4 − 2x3 + 3x2 + 4x − 4)(26)
+
[
ie(−t)−e/ 2V (−
√
−t) + (−t)−e/ 4x
] 2 · x2(x2 − 3)
+2(x2 + x − 1)(
√
−t
e
+
√
−t
−e
) .
Rearranging, we need to show that the sum of the following 5 ex pressions, regarded as a polynomial in t±1/ 2, has
either arbitrarily small minimal degree or arbitrarily lar ge maximal degree. (Note that by (25) this sum must be
self-conjugate in t up to coefﬁcient signs, which is not at all evident directly.)
T ′
1 = ie(−t)−eV (t) · (−x4 − 2x3 + 3x2 + 4x − 4)
T ′
2 = t−e[
V (−
√
−t)
] 2 · x2(x2 − 3)
T ′
3 = 2ie(−t)−3e/ 4V (−
√
−t)x3(x2 − 3)
T ′
4 = ( −t)−e/ 2[
(x2 − 2)(−x4 − 2x3 + 3x2 + 4x − 4) +x4(x2 − 3) +2(x2 + x − 1)
]
T ′
5 = ( −t)e/ 2[
2(x2 + x − 1)
]
Switching −t → t to simplify the expressions, and regrouping terms, we have
T1 = iet−eV (−t) · (−1 − 2 − 1 − 2 [−4] − 2 − 1 − 2 − 1)
T2 = ( −t)−e[
V (−
√
t)
] 2 · (1 0 1 0 [0] 0 1 0 1)
T3 = 2iet−3e/ 4V (−
√
t) · (1 0 2 0 1 [0] 1 0 2 0 1)
T4 = t−e/ 2[
−2(x − 1)(x2 − 3)(x2 − 1)
]
T5 = te/ 2[
2(x2 + x − 1)
]
Now u = t1/ 2 and x = t1/ 2 + t−1/ 2. The last factors for T1,2,3 are given as a list of coefﬁcients, with the absolute term
put in brackets. Note that these are polynomials in √t, so for example, the ﬁrst two polynomials have degree 2 in t.
Since we are concerned with cancellations of the leading and trailing coefﬁcients of Tk, let us compile their minimal
mk = mindegt Tk and maximal degrees Mk = maxdegt Tk (note that by taking degrees w.r.t. t, and not √t, the mk, Mk
are only half-integers).
k mk Mk
1 mindeg V − e − 2 maxdeg V − e + 2
2 mindeg V − e − 2 maxdeg V − e + 2
3 − 3e
4 + mindeg V
2 − 5
2 − 3e
4 + maxdeg V
2 + 5
2
4 − e
2 − 5
2 − e
2 + 5
2
5 e
2 − 1 e
2 + 1
(Here again mindeg V = mindegt V (t) is a half-integer, and similarly maxdegV.)
Our aim will be to determine what of the Mk is the largest, and to show that the coefﬁcients of the contri buting Tk do
not cancel. An important case where we exclude (problematic) cancellation is
24 4 Polynomial invariants
Lemma 4.11 Assume that
M1 = M2 ≥ Mk + 3/ 2 and(27)
m1 = m2 ≤ mk − 3/ 2(28)
for k = 3,4,5. Then maxdeg t Q1(L,x) ≥ M1 − 1. (Here Q1(L,x) refers to (26).) If L the closure of a 3-braid which is
A-adequate resp. B-adequate then assuming (28) resp. (27) alone is sufﬁcient.
Proof. By theorem 4.5, L is the closure of a 3-braid β which is either A-adequate or B-adequate. We consider the
B-adequate case and show that M1 = M2 ≥ Mk + 3/ 2 implies maxdeg t Q1(L,x) ≥ M1 − 1. If β is A-adequate, we
obtain similarly mindegt Q1(L,x) ≤ m1 + 1, and the result follows by the (anti)symmetry of Q1.
Now if M1 = M2 ≥ Mk + 3/ 2, the last three coefﬁcients of M1,2 are not cancelled from other Mk (remember these
are polynomials in √t, and coefﬁcients are meant for such polynomials), so it is en ough to show that they do not
(completely) cancel among each other. Now a look at the formu las for T1,2 shows that if these three coefﬁcients are
all to cancel, then (apart from proper sign coincidences) we must have ¯V1 ¯V0 = −1 and ¯V2 = 0. (Take also into account
the switch −t → t.) However, this situation was ruled out by lemma 4.10. ✷
We assumed e ≥ 0; we also excluded the case e = 3 − χ of strongly quasi-positive braids. To apply the lemma, we
need to establish (28) and/or (27). For this we use now lemma 4.6.
Clearly, a strongly almost quasi-negative braid should not be considered for e ≥ 0; the almost quasi-positive braid
require a small extra argument, which is given below. Now
maxdeg V − e = 1 − χ
2 + 1 ≥ e
2 + 1 ,(29)
so M3 ≥ M4, and we can discard M4. Also from (29) we obtain
M1 − M5 − 1 = maxdeg V − 3e
2 ≥ 1 ,
so M1 > M5 + 1, and can neglect M5. Similarly, if β is not almost strongly quasi-positive, we have with (22) and
mindeg V < e/ 2 that
m3 < m4 < m5 ,(30)
so m4,5 are also irrelevant.
So we need to deal only with mk,Mk for k ≤ 3. Moreover, we see from (21) that M1 ≥ (1 − χ)/ 2 + 3. So whenever we
can apply lemma 4.11, we have for χ ≤ 0 that maxdeg Q1 ≥ M1 − 1 > 2, so maxdeg z Q > 0, and Q is not an unlink
polynomial. Moreover, we have for a sequence of links from χ → −∞ also maxdeg M1 → ∞, so maxdeg Q → ∞, and
a given (even just degree of a) Q polynomial occurs only ﬁnitely many times, as desired. A sim ilar argument applies
if we use (22).
To apply lemma 4.11, we need to checkM3 < M1 −1 and m3 > m1 +1. Note that if β is almost strongly quasi-positive,
then (22) may not hold. So may not be able to apply lemma 4.11 di rectly. However, we remedied this by showing in
lemma 4.9 that β is B-adequate. Then (21) holds, and it is enough to use M3 < M1 − 1 (the condition (30) becomes
also irrelevant).
Now using (21) and (22)
m1 − m3 + 1 = mindeg V − e − 2 + 3e
4 − mindeg V
2 + 5
2 + 1 = mindeg V
2 − e
4 + 3
2
= e
2 − 1 − χ
4 − 1
2 − e
4 + 3
2 = e
4 − 1 − χ
4 + 1 ,
M1 − M3 − 1 = maxdeg V
2 − e
4 − 3
2(31)
= e
2 + 1 − χ
4 + 1
2 − e
4 − 3
2 = 1 − χ
4 + e
4 − 1 .
