---
doc_id: arxiv-math-0405508v1
doc_title: "Markov traces and knot invariants related to Iwahori-Hecke algebras of type B"
section_id: sec-009-8-gecklambropoulou
section_title: "Geck–Lambropoulou"
section_number: 8
pages: 8-9
source_pdf: 0405508v1.pdf
source_sha256: ef2e41cf67f3a411
doc_brief: "Markov traces and knot invariants related to Iwahori-Hecke algebras of type B — 30 sections: Introductory remarks on knots, bra; Geck–Lambropoulou; Geck–Lambropoulou"
---
(a) In [3], Proposition 2.4(a), it is shown that the equation wy = vy holds
in Wn and that the expressions on both sides are reduced. Hence the lef t hand
side can be transformed to the right hand side by a ﬁnite sequence o f braid
relations. It follows that the equation wy = vy also holds in the braid group.
(b) We write y = (si+m+1 · · ·si+1)y′. Then
y−1t′
i+m+1y = y−1si+m+1 · · · si+1t′
is−1
i+1 · · · s−1
i+m+1y = y′−1t′
iy′ = t′
i.
For the last equality, note that y′ is a product of generators sj with j > i + 1
and that all of these commute with t′
i.
Now ( si+1 · · · si+m) commutes with t′
i+m+1. So we can write w = t′
i+m+1wa
and v = t′
iva where wa and va are as in part (a) of the Lemma. Hence we
deduce, using (a), that
y−1wy = (y−1t′
i+m+1y)(y−1way) = t′
iva = v.
(c) We rearrange the given reduced expression for y as
y = (si+m+1 · · ·si+m+k+1)(si+m · · · si+m+k) · · ·(si+1 · · · si+k+1)
and write y = y′(si+1 · · · si+k+1). Now note that y′ is a product of generators
sj with j > i + 1 and that all of these commute with t′
i. Then we compute
that
y−1t′
iy = ( s−1
i+k+1 · · ·s−1
i+1)y′−1t′
iy′(si+1 · · · si+k+1)
= s−1
i+k+1 · · ·s−1
i+1t′
isi+1 · · · si+k+1
=: t′′
i+k+1,i .
We can write w = t′
iwb where wb is as in part (b). Thus, we deduce, using (b),
that
y−1wy = (y−1t′
iy)(y−1wby) = ( t′′
i+k+1,i t′
isi+1 · · · si+k)(si+k+2 · · ·si+k+m+1).
Using Lemma 2.3(b), we compute that t′′
i+k+1,i t′
i = t′
it′′
i+k+1,i +1 where the in-
verses in t′′
i+k+1,i +1 at all indices bigger than i + 1 are on the left hand side of
t. A ﬁnal calculation then shows that
t′′
i+k+1,i +1(si+1 · · · si+k) = ( si+1 · · · si+k)(si+k+1s−1
i+k · · · s−1
i+1t′
isi+1 · · ·si+ks−1
i+k+1).
If we denote the second factor on the right hand by t′
i+k+1,i then y−1wy = v
as required. The proof is complete. ✷
Markov traces and knot invariants 9
Remarks 2.6 (a) One can also show that, if the conjugation in (b), (c) of the
above Lemma is performed step by step (one generator of y at a time) then
this sequence of conjugations can be arranged in such a way that t he length
of the elements does not increase at each step (cf. [3], Proposition 2.4(b,c)).
(b) Consider the elements
w = (s1)(s−1
2 s1ts−1
1 s2) and v = ts2 (in ˜W3).
If all the inverses in w were on the right hand side of t then this element
would be conjugate to v in ˜W3, by part (b) of the above Lemma (with m = 1,
k = i = 0). However, one can show that w and v are not conjugate in ˜Wn,
and not even in the associated Iwahori-Hecke algebra. This example indicates
that the statements in the above Lemma are as strong as possible, and that
we cannot distribute the inverses in some arbitrary order around t when we
want to conjugate elements in block form.
Note, however, that the oriented links obtained by closing the braid s cor-
responding to the above elements are isotopic (see (5.4) below). In particular,
the knot invariants constructed in Deﬁnition 5.3 must have the same value on
them.
