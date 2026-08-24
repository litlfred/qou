---
doc_id: arxiv-math-9806163v1
doc_title: "Weights of Markov traces on Hecke algebras"
section_id: sec-021-20-r-c-orellana
section_title: "R. C. Orellana"
section_number: 20
pages: 20-21
source_pdf: 9806163v1.pdf
source_sha256: dba44975f29cb017
doc_brief: "Weights of Markov traces on Hecke algebras — We compute the weights, i.e. the values at the minimal idempo tents, for the Markov trace on the Hecke algebra of type Bn and type Dn."
---
sends gi to gi+n for all i. In particular, this tensor product allows us to multiply minimal
idempotents using the generalized Littlewood-Richardson rule in [GW]. Denote by 1 n the
identity in Hn(q).
Lemma 5.4 A Markov trace on the Hecke Algebra of type A induces a Markov trace on
the Hecke algebra of type B, which satisﬁes the condition tha t tr(t′
nx) = ytr(x), where x ∈
Hn(q, Q). In particular, this implies that yk = yk for all k ∈ N.
Proof: Let tr be a Markov trace for Hn+f (q) and trptλ be the Markov trace corresponding
to the reduced algebra. We have shown that the weights for the re duced algebra deﬁne a
Markov trace for Hn(q, −qr1+m).
Assume that EHn+f −1(q) : Hn+f (q) → Hn+f −1(q) is the unique conditional expectation
with respect to the Markov trace deﬁned by the weight function. T hus, EHn+f −1(q)(˜gn+f h) =
zh for all h ∈ Hn+f −1(q) and z = qr (1−q)
(1−qr).
We denote the image of t′
n under the homomorphism ρn+f by ptλ τn+f . Consider the ele-
ment ptλ τn+f h where h ∈ Hn+f −1(q). We would like to compute the conditional expectation
of ptλ τn+f h. Observe that
EHn+f −1(q)(ptλ τn+f h) = EHn+f −1(q)(ptλ τn+f )h.
Therefore it suﬃces to compute the conditional expectation for ptλ τn+f . Consider the fol-
lowing
(ptλ ⊗ 1n−1 ⊗ p[1r])(τn+f ⊗ 1r−1)(ptλ ⊗ 1n−1 ⊗ p[1r])(h ⊗ 1r)
The above expresion is equal to the left hand side of the following equ ation (see ﬁgure 7).
[((p[1r] ⊗ ptλ )(1r−1 ⊗ τn+f )(p[1r] ⊗ ptλ )) ⊗ 1n−1](1r ⊗ h) = ( const)(p[1r] ⊗ ptλ ⊗ 1n−1)(1r ⊗ h)
Since we are restricted to r rows we have by the generalization of the Littlewood-Richardson
rule, see [GW], that p[1r] ⊗ ptλ is a minimal idempotent. But Theorem 5.3 (c) implies that
(const)ptλ = EHn+f −1(q)(τn+f ptλ ). Thus,
trptλ (τn+f h) = ( const)trptλ (h).
This implies that we have a Markov trace with the property tr(t′
nh) = ( const)tr(h) for all
h ∈ Hn+f −1(q). But this trace is also a trace for Hn(q, −qr1+m). Since the above property
holds for all Q = −qr1+m, then it must hold for all Q. Thus our assertion is proved. □
Theorem 5.5 If tr is a Markov trace on the Hecke algebra of type B, with parameter z =
qr(1 − q)/(1 − qr1+r2), such that tr(t′
0t′
1 . . . , t′
k−1) = yk for k ≥ 1. Then the weights are given
by W(α,β )(q, Q) as deﬁned in equation (12) with y = (qr2Q + 1)(1 − qr1)/(1 − qr) − 1.
Weights of Markov Traces on Hecke Algebras 21
Proof: The fact that the weights deﬁne a Markov trace follows from Lemma s 5.1, 5.2
and 5.4. It remains to show that the weight formula is indeed given by t his values of
y = ( Qqr2 + 1)(1 − qr1)/(1 − qr1+r2) − 1. By Lemma 5.1 it suﬃces to compute tr(t) in
H1(q). This is a straight forward computation, we have W([1], ∅)(q, Q) = (1−qr1 )(1+Qqr2 )
(1−qr )(1+Q) and
W(∅, [1])(q, Q) = qr1 (1−qr1 )(1+Qq−r1 )
(1−qr )(1+Q) . Also χ([1], ∅)(t) = Q and χ(∅, [1])(t) = −1. Using these values
we compute
tr(t) = QW([1], ∅)(q, Q) − W(∅, [1])(q, Q) = (Qqr2 + 1)(1 − qr1)
(1 − qr) − 1. □
