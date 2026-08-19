---
doc_id: arxiv-math-0405508v1
doc_title: "Markov traces and knot invariants related to Iwahori-Hecke algebras of type B"
section_id: sec-020-44-in-the-course-of-the-above-proof-we-have-show
section_title: "In the course of the above proof, we have shown the following r emark-"
section_number: 4.4
pages: 18-19
source_pdf: 0405508v1.pdf
source_sha256: ef2e41cf67f3a411
doc_brief: "Markov traces and knot invariants related to Iwahori-Hecke algebras of type B — 30 sections: Introductory remarks on knots, bra; Geck–Lambropoulou; Geck–Lambropoulou"
---
able property of a Markov trace τ.
Let h ∈ Hn and d∗
n+1 ∈ D ′
n+1, 0, . . . , d ∗
n+m ∈ D ′
n+m, 0 for some m ≥ 1. Then
τ(hd∗
n+1 · · · d∗
n+m) = τ(hdn+1 · · · dn+m),
where, as before, di is the element in D′
i corresponding to d∗
i .
For h ∈ Hn let I(h) be the corresponding set given by Proposition 3.4. For
each i = (r, d ∗
1, . . . , d ∗
n) ∈ I(h) we write r(i) = r, a(i) = a(d1 · · · dn) and b(i) =
b(d1 · · · dn). Then the above property in combination with Proposition 3.4 and
Lemma 4.2 yields the following rule for computing τ(h).
τ(h) =
∑
i∈I(h)
r(i)za(i)yb(i).
Note that an algorithm for computing I(h) is given by the inductive proof of
Proposition 3.4.
Markov traces and knot invariants 19
Proposition 4.5 Let z, y ∈ A and τ : H → A be a Markov trace with param-
eter z and such that τ(t′
0t′
1 · · ·t′
k−1) = yk for all k ≥ 1. Then
τ(ht′
n, 0) = yτ(h) for all n ≥ 0 and h ∈ Hn.
Proof. Following the steps in the proof of Theorem 4.3 we see that it is suﬃcien t
to consider the case where h = d∗
1 · · · d∗
n with d∗
i ∈ D ′
i, 0 for all i. The result in
this case follows from Lemma 4.2. ✷
Remarks 4.6 (a) Given elements z, y ∈ A, the existence of a Markov trace
τ = τz,y as in the previous Proposition can also be proved along the lines of
the approach followed by Jones [5], §5, in the proof of Ocneanu’s Theorem for
Iwahori-Hecke algebras of type An. Such a proof is sketched in [7] (see also
[6], §3.3). It is based on the observation that, for all n ≥ 0, the map
Cn : Hn ⊕ Hn ⊕ Hn ⊗Hn−1 Hn − →Hn+1, a + b + c ⊗ d ↦→a + bt′
n + cgnd
deﬁnes an isomorphism of ( Hn, H n)-bimodules. Analogously to the proof of
[5], (5.1), we can now deﬁne an A-linear map τ inductively on H =⋃
n Hn by
the rules: τ(1) = 1, τ(bt′
n) = yτ(b) and τ(cgnd) = zτ(cd) where b, c, d ∈ Hn
and n ≥ 0. It follows easily that this map satisﬁes conditions (2) and (3)
of Deﬁnition 4.1, and the problem then is to show that (1) holds, that is, to
show that τ is a trace function. This veriﬁcation is a lengthy and tedious
calculation that we do not want to reproduce here. We do not see, h owever,
how this method could be modiﬁed so as to give an alternative proof of our
more general Theorem 4.3, too. Yet another construction of the trace in [7]
was given by T. tom Dieck in [9] using Turaev’s R–matrix approach (see [11]).
It would be interesting to ﬁnd such an R–matrix interpretation of our more
general traces in Theorem 4.3, too.
(b) For the deﬁnition of Markov traces it doesn’t matter whether w e use the
elements ti or t′
i in the signed block form of elements. From Theorem 4.3
we see that this only plays a role in the formulation of the initial conditions
determining the trace, and it would not be clear how to do this in terms of the
elements ti. This gives an explanation for using t′
i rather than ti.
