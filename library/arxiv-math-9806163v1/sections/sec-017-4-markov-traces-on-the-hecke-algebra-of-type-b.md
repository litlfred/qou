---
doc_id: arxiv-math-9806163v1
doc_title: "Weights of Markov Traces on Hecke Algebras ∗ R.C. Orellana"
section_id: sec-017-4-markov-traces-on-the-hecke-algebra-of-type-b
section_title: "Markov Traces on the Hecke Algebra of type B"
section_number: 4
pages: 14-16
source_pdf: 9806163v1.pdf
source_sha256: dba44975f29cb017
doc_brief: "Weights of Markov Traces on Hecke Algebras ∗ R.C. Orellana — We compute the weights, i.e. the values at the minimal idempo tents, for the Markov trace on the Hecke algebra of type Bn and type Dn."
---
In this section we give the necessary background on Markov trace s. We refer the reader to
[GL] or [G] for the details.
A trace function on H∞(q, Q) is a C(q, Q)-linear map φ : H∞(q, Q) − →C(q, Q) such that
φ(hh′) = φ(h′h) for all h, h′ ∈ H∞(q, Q). This deﬁnition is in fact valid for any associative
algebra over a commutative ground ring. In the case of the group a lgebra it is clear that
every trace function is constant on the conjugacy classes of the underlying group. Notice
Weights of Markov Traces on Hecke Algebras 15
that φ(hh′) − φ(h′h) = 0; this means that φ(hh′ − h′h) = φ([h, h′]) = 0, which implies that
the commutators are in the kernel of a trace function in an algebra .
The weights we are going to give in this paper correspond to a trace t hat satisﬁes the
following deﬁnition.
Deﬁnition: Let z ∈ C(q, Q) and tr : H∞(q, Q) − →C(q, Q) be an C(q, Q)-linear map.
Then tr is called a Markov trace (with parameter z) if the following conditions are satisﬁed:
(1) tr is a trace function on H∞(q, Q);
(2) tr(1) = 1 (normalization);
(3) tr(hgn) = ztr(h) for all n ≥ 1 and h ∈ Hn(q, Q).
The name of these traces comes from their invariance under the Ma rkov moves for closed
braids. Remember that the Hecke Algebra is a quotient of the braid g roup. We note that all
generators gi (for i = 1 , 2, . . .) are conjugate in H∞(q, Q). In particular, any trace function
on H∞(q, Q) must have the same value on these elements. This explains why the p arameter
z is independent of n in rule (3) of this deﬁnition.
Geck and Pfeiﬀer in [GP] showed that a trace function on the Hecke a lgebra is uniquely
determined by its value on basis elements corresponding to represe ntatives of minimal length
in the various conjugacy classes of the underlying Coxeter group. Also representatives of min-
imal length in the classes of Coxeter groups of classical types are o f the form d1 . . . dn, where
di is a distinguished double coset representative of the Hi(q, Q) with respect to Hi−1(q, Q).
Let tr be a Markov trace with parameter z, and let di ∈ D i for i = 1, . . . , n. Then
tr(d1 . . . dn) = zatr(t′
0t′
1 . . . t′
b−1)
where a is the number of factors d′
i which are equal to gi−1 and b is the number of factors
which are equal to t′
i−1. Thus, tr is uniquely determined by its parameter z and the values
on the elements in the set {t′
0t′
1 . . . t′
i−1 | i = 1, 2, . . .}.
Conversely, given z, y 1, y 2, . . . ∈ C(q, Q) then there exist a unique Markov trace on
H∞(q, Q) such that tr(t′
0t′
1 . . . t′
k−1) = yk for all k ≥ 1. For details on these results see [GL],
Theorem 4.3.
We are particularly interested in the special case when yi = yi for all i ∈ N, this is the case
when there is only two parameters. In this case, we have that if di is a distinguished double
coset representative then tr(dix) = ξtr(x) where ξ = y or z. The proof of the following
proposition is found in [GL].
Proposition 4.1 Let z, y ∈ C(q, Q) and tr : H∞(q, Q) − →C(q, Q) be a Markov trace with
parameter z such that tr(t
′
0t
′
1 . . . t
′
k−1) = yk for all k ≥ 1 then
tr(ht
′
n, 0) = ytr(h) for all n ≥ 0 and h ∈ Hn(q, Q)
where t′
n, 0 = gn . . . g1tg−1
1 . . . g−1
n or g−1
n . . . g−1
1 tg1 . . . gn.
We point out that the converse is also true. A proof of the existenc e of such traces for
every z ∈ C is given in [GL]. We will compute the weight vectors for this Markov trac e on
Hn(q, Q).
