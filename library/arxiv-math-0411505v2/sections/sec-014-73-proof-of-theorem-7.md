---
doc_id: arxiv-math-0411505v2
doc_title: "A NON-COMMUTATIVE FORMULA FOR THE COLORED JONES FUNCTION"
section_id: sec-014-73-proof-of-theorem-7
section_title: "Proof of Theorem 7"
section_number: 7.3
pages: 14-15
source_pdf: 0411505v2.pdf
source_sha256: a38cec365e0a227e
toc_source: outline
doc_brief: "A NON-COMMUTATIVE FORMULA FOR THE COLORED JONES FUNCTION — The colored Jones function of a knot is a sequence of Laurent polynomials that encodes the Jones polynomial of a knot and its parallels."
---
Deﬁnition 7.8. Let e ∈Fr. We deﬁne set P(f, e) as follows: if e ∈F(e′), e1 ∈F(e′
1) then e1 ∈P(f, e) if
t(e′) = t(e′
1) = v and e′
1 <v e′, or e′ = e′
1 and e1 < e in our ﬁxed total order of F(e).
Deﬁnition 7.9. Let e ∈Fr. We deﬁne
• def1(C, v, e) = |{e′ ∈P(f, e) : ve′ < ve}|,
• def2(C, v, e) = |{e′ ∈Cd(e) : ve′ < ve}|, where d(e) is the biggest index such that d(e) ≥t(e) and
e̸ ∈Cd(e).
Recall that t(e) denotes the terminal vertex of e.
Proposition 7.10. Let P = (C, v) be an n-sorting of f. Then
exc(P) =
X
e∈Fr
δ1(e) + δ2(e),
where
δ1(e) =
(
|P(f, e)| −def1(C, v, e)
if e starts in a + vertex
−def1(C, v, e)
if e starts in a −vertex,
δ2(e) =
(
|Cd(e)| −def2(C, v, e)
if
sign(d(e)) = +
−def2(C, v, e)
if
sign(d(e)) = −.
Proof. Let e ∈Fr and ﬁrst assume sign(s(e)) = +. Then
δ1(e) = |P(f, e)| −def1(C, v, e) = |{e′ : e′ ∈P(f, e) ∩Fr, ve < ve′}| + |{e′ ∈Ct(e)−1 : ve < ve′}|.
This equals, by deﬁnition 6.6 of function X and by deﬁnition of bijection Φ in lemma 7.7,
sign(s(Φ(e)))
X
e′∈F
X(Φ(e), Φ(e′)).
We proceed analogously if sign(s(e)) = −. Hence
X
e∈Fr
δ1(e) =
X
e∈Fr
sign(s(Φ(e)))
X
e′∈F
X(Φ(e), Φ(e′)).
Next we denote, for e ∈Fr, by D(e)) the red edge of Φ(P) that starts at vertex ad(e)
v(e)+1. Note that D is a
bijection between Fr and the set of the red edges of Φ(P).
Now let sign(d(e)) = +. Then δ2(e) equals the number of e′ ∈Cd(e) such that ve < ve′. This equals
sign(d(e)) P
e′∈F Y (D(e), Φ(e′)). Again the case sign(d(e)) = −is analogous.
Hence we get
X
e∈Fr
δ2(e) =
X
e∈Fr
sign(d(e))
X
e′∈F
Y (D(e), Φ(e′)).
This ﬁnishes the proof by lemma 6.7.
□
Proof. (of Theorem 7)
We use Theorem 8, Lemma 7.7 and Proposition 7.10:
Jn(K)(t) = tδ(K,n)
X
f∈F(GK)
tδ(f)
X
P ∈AC(f,n)
texc(P )b(P) =
tδ(K,n)
X
f∈F(GK)
tδ(f)tn(f −
b −f +
b )(1 −t)f −
r (1 −t−1)f +
r
Y
e∈F +
r
t−(n−1−|P (f,e)|)
Y
e∈Fr,sign(d(e))=+
t|Cd(e)|
X
(C,v)∈AC(f,n)
Y
e∈Fr
tve−def1(C,v,e)−def2(C,v,e).
Let us recall that
mult(f)q =
r−2
Y
v=1
 f(v)
f(ebv)

qsign(v)
.
14
At this point, we will use Appendix C. By Theorem 9 and Theorem 10 we get
Jn(K)(t) = tδ(K,n)
X
f∈F(GK)
tδ(f)tn(f −
b −f +
b )(1 −t)f −
r (1 −t−1)f +
r t−(n−1)f +
r
Y
e∈F +
r
t|P (f,e)|
Y
e∈Fr,sign(d(e))=+
t|Cd(e)|
r
Y
v=1
 f(v)
f(ebv)

t−1
Y
e∈Fr
(n −|P(f, e)|)t =
tδ(K,n)
X
f∈F(GK)
tδ(f)
r
Y
v=1
 f(v)
f(ebv)

t−1
Y
v:sign(v)=+
tf(er
v)f(eb
v)
tn(f −
b −f +
b )(1 −t)f −
r (1 −t−1)f +
r t−(n−1)f +
r
Y
e∈F +
r
t|P (f,e)| Y
e∈Fr
(n −|P(f, e)|)t =
tδ(K,n)
X
f∈F(GK)
multt(f)tδ(f)tn(f −
b −f +
b )(1 −t)f −
r (1 −t−1)f +
r Y
e∈Fr
(n −|P(f, e)|)t−sign(s(e)) =
tδ(K,n)
X
f∈F(GK)
multt(f)tδ(f) Y
v∈VK
t−sign(v)nf(eb
v)
Y
ered;t(e)=v
f(e)−1
Y
j=0
(1 −t−sign(s(e))(n−j−P
e′<ve f(e))).
This ﬁnishes the proof.
□
