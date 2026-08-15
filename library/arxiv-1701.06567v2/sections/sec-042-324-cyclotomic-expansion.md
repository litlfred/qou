---
doc_id: arxiv-1701.06567v2
doc_title: "BPS spectra and 3-manifold invariants"
section_id: sec-042-324-cyclotomic-expansion
section_title: "Cyclotomic expansion"
section_number: 3.2.4
pages: 39-41
source_pdf: 1701.06567v2.pdf
source_sha256: c1610b50f5a7e22c
doc_brief: "BPS spectra and 3-manifold invariants — We provide a physical deﬁnition of new homological invariants Ha(M3) of 3- manifolds (possibly, with knots) labeled by abelian ﬂat connections."
---
In this secition we show how to obtain expression for ˆZa(1/q,t ) with |q| < 1 using what is
usually called the cyclotomic expansion.
Let us ﬁrst consider the general construction. Let F (q,t ) be some function of q and t,
and suppose we know its restrictions at t =qβ, with β∈ Z,
F (β)(q)≡F (q,qβ). (3.73)
Then, one can write the following formal cyclotomic-like expansion for F (q,t ):
F (q,t ) =
∞∑
m=0
~F (m)(q)· tm(1/t;q)m
(q;q)m
. (3.74)
The coeﬃcient of the cyclotomic expansion, ~F (m)(q), are related to F (m)(q) by a “triangular”
linear transform:
~F (0)(q) = F (0)(q)
~F (1)(q) = F (0)(q)−F (1)(q)
~F (2)(q) = F (0)(q)− (1 +q−1)F (1)(q) +q−1F (2)(q)
~F (3)(q) = F (0)(q)− (1 +q−1 +q−2)F (1)(q) + (q−1 +q−2 +q−3)F (2)(q)−q−4F (3)(q)
...
(3.75)
Note, that the denominators (q;q)m in (3.74) are introduced for convenience, so that
F (β)(q) ∈ Z[q,q−1] ⇐⇒ ~F (m)(q)∈ Z[q,q−1] (3.76)
but in principle they can be absorbed into the deﬁnition of cyclotomic coeﬃcients ~F (m)(q).
– 38 –
If the minimal degree of q in ~F (m)(q) grows with m, one can produce a q-expansion from
the cyclotomic expansion ( 3.74). However, such procedure is quite formal and in general
might not actually give the actual q-expansion that converges to F (q,t ) when|q| < 1. But
it can be done for homological blocks. In particular, from ( 3.59) one obtains the following
cyclotomic-like expansion:
ˆZa(q,t ) = 1
(qt;q)∞
∞∑
m=0
~ˆZ
(m)
a (q)· tm(1/t;q)m
(q;q)m
(3.77)
where the coeﬃcients
~ˆZ
(m)
a (q) ∈ Z[q] (3.78)
turn out to be polynomials in q (non-Laurent) with minimal power growing linearly in m.
Expanding each term in q then gives us a q-series of the following form:
ˆZa(q,t ) =
∞∑
n=0
Pn(t)qn, P n(t)∈ Z[t], (3.79)
which coincides with the q-series that can be produced directly from ( 3.33). On the other
hand, since Pm(t) contain only positive powers of t, one can produce ˆZ(β)(q) — or, equiva-
lently, the coeﬃcients of the cyclotomic expansion ~ˆZ
(β)
(q) — from (3.33) just by making the
substitution t =qβ and observing that the resulting q-series truncates.
Therefore, we assume that for anti-blocks one can write similarly:
ˆZa(1/q,t ) = (1/t;q)∞
∞∑
m=0
~ˆZ
(−m)
a (1/q)· tm(1/t;q)m
(q;q)m
(3.80)
where ~ˆZ
(−m)
a (1/q) are related to ˆZ(−β)
a (1/q)≡ (q−1t;q−1)∞ˆZa(q−1,t )|t=qβ in the same way
as ~F (m)(q) are related to F (β)(q) in (3.75).
For example, in the case p = 5, using expressions for ˆZ(−β)
a (q) calculated in Section 3.2.3
we have
2ˆZ0(1/q,t ) =
(
−t3 +t2−t + 1
)
+
(
t4− 3t3 + 5t2− 3t
)
q +
(
−t5 + 6t4− 11t3 + 11t2− 6t + 1
)
q2
+
(
t6− 6t5 + 17t4− 28t3 + 26t2− 12t + 2
)
q3 +O
(
q4)
,
ˆZ1(1/q,t ) = q−1/5
((
t2−t
)
+
(
t4− 3t3 + 3t2− 2t + 1
)
q +
(
−t5 + 4t4− 9t3 + 10t2− 5t + 1
)
q2
+
(
−4t5 + 15t4− 24t3 + 21t2− 10t + 2
)
q3 +O
(
q4))
,
ˆZ2(1/q,t ) = q1/5
((
−t3 + 2t2−t
)
+
(
2t4− 5t3 + 5t2− 3t + 1
)
q+
+
(
−2t5 + 7t4− 13t3 + 14t2− 7t + 1
)
q2 +O
(
q3))
.
(3.81)
– 39 –
Now we can check ( 3.35) and ( 3.55) directly. From ( 3.31), or equivalently from ( 3.77), we
have
ˆZ0(q,t ) = 1 +q + (2−t +t2)q2 + (3− 2t + 2t2)q3 +O(q4),
ˆZ1(q,t ) = q1/5(
−1 + (−2 +t)q + (−3 + 2t− 2t2)q2 + (−5 + 4t− 3t2 +t3)q3 +O(q4)
)
,
ˆZ2(q,t ) = q4/5(
(1−t)q + (1− 2t +t2)q2 +O(q3)
)
.
(3.82)
And from (3.31) we have:
I(q,t ) =
(
1− 1
t3
)
+
(
−1 + 1
t + 1
t2− 1
t3
)
q +
(
t2− 2 + 1
t− 1
t3 + 1
t4
)
q2+
+
(1
t− 1
t2− 1
t5 + 1
t6
)
q3 +O
(
q4)
. (3.83)
Then, one can check explicitly that indeed
I(q,t ) = ˆZ0(q,t )· 2ˆZ0(1/q, 1/t) +ˆZ1(q,t )ˆZ1(1/q, 1/t) +ˆZ2(q,t )ˆZ2(1/q, 1/t). (3.84)
Similarly, the topologically twisted index,
Itop(q,t ) = 1 −t3, (3.85)
can indeed be decomposed as
Itop(q,t ) = ˆZ0(q,t )· 2ˆZ0(1/q,t ) +ˆZ1(q,t )ˆZ1(1/q,t ) +ˆZ2(q,t )ˆZ2(1/q,t ). (3.86)
