---
doc_id: arxiv-math-9806163v1
doc_title: "Weights of Markov traces on Hecke algebras"
section_id: sec-010-8-r-c-orellana
section_title: "R. C. Orellana"
section_number: 8
pages: 8-9
source_pdf: 9806163v1.pdf
source_sha256: dba44975f29cb017
doc_brief: "Weights of Markov traces on Hecke algebras — We compute the weights, i.e. the values at the minimal idempo tents, for the Markov trace on the Hecke algebra of type Bn and type Dn."
---
(H6) tgi = git for i ≥ 2.
Note that for q = 1 and Q = 1, (H3) and (H4) become g2
i = 1 and t2 = 1, respectively. In
this case the generators satisfy exactly the same relations as a se t of simple reﬂections of the
hyperoctahedral group, Hn. It is known that Hn(q, Q) ∼= CHn (the group algebra of Hn) if
q is not a root of unity and Q ⁄= −qs for −n < s < n . CHn is semisimple since it is a ﬁnite
complex group algebra. This implies that Hn(q, Q) is semisimple for generic values of q and
Q. Furthermore the simple modules are in 1-1 correspondence with do uble partitions. Their
decomposition rule and their dimensions are the same as for Hn. [See Bourbarki, Groups et
algebres de Lie IV, V, VI]
Hoefsmit, in [H], has written down explicit irreducible representations of Hn(q, Q) for
each pair of Young diagrams. This demonstrates that dimension ove r C(q, Q) of Hn(q, Q) is
2nn!. Let V(α,β ) be an Hn(q, Q) module then we have the following restriction rule:
V(α,β )
⏐
⏐
⏐
Hn−1(q,Q )
∼=
⨁
(α,β )′⊂(α,β )
V(α,β )′, (8)
where ( α, β)′ is the double partition obtained from ( α, β) by subtracting one from one
of the parts. This isomorphism follows from the bijection t(α,β ) → t(α,β )′
of T(α,β ) and⋃
(α,β )′⊂(α,β ) T(α,β )′, where t(α,β )′
is the pair of standard tableaux obtained by removing the
box containing n. Moreover, π(n) = ⨁
(α,β )⊢n π(α,β ) is a faithful representation of Hn(q, Q).
Note that (H1) and (H2) are the deﬁning relations for the braid gro up Bn(A). So repre-
sentations of Hn(q, Q) also yield in particular representations of Bn(A). Obviously we also
obtain representations of the braid group of type B.
The Hecke algebras satisﬁes the following embedding of algebras H0 ⊂ H1 ⊂ H2 ⊂ · · ·
We shall denote
H∞(q, Q) :=
⋃
n≥0
Hn(q, Q)
Observe that (H3) and (H4) imply that t and gi have at most 2 eigenvalues each, hence
also at most 2 projections corresponding to these eigenvalues.
Right and Double Coset Representatives
The fact that q is invertible in C(q, Q) implies that the generators gi are also invertible
in Hn(q, Q). In fact, the inverse of the generators is given by
g−1
i = q−1gi + (q−1 − 1)1 ∈ Hn(q, Q)
This implies that the following element is well-deﬁned in Hn(q, Q): t
′
i = gi · · · g1tg−1
1 · · · g−1
i .
We use this elements to deﬁne the set Dn as a subset of Hn(q, Q). If n = 1, we let D1 := {1, t}.
For n ≥ 2 we have
Dn := {1, gn−1, t
′
n−1}.
Weights of Markov Traces on Hecke Algebras 9
Also the set of right coset representatives of Hn−1(q, Q) in Hn(q, Q) is given as follows:
Rn := {1, t ′
n−1, g n−1gn−2 . . . gn−k, g n−1gn−2 . . . gn−kt′
n−k−1 (1 ≤ k ≤ n − 1)}.
Note that R1 = {1, t}. The elements {r1r2 . . . rn|ri ∈ R i} form a C(q, Q)-basis of Hn(q, Q),
see [GL].
