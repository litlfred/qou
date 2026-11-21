---
doc_id: 0309214v3
doc_title: "The colored Jones function is q –holonomic"
section_id: sec-038-741-r-is-q--holonomic
section_title: "r is q--holonomic"
section_number: 7.4.1
pages: 33-33
source_pdf: 0309214v3.pdf
source_sha256: 53967ef30b0aedb9
toc_source: outline
doc_brief: "The colored Jones function is q –holonomic — A function of several variables is called holonomic if, roughly speaking, it is determined from ﬁnitely many of its values via ﬁnitely many linear"
---
We will need the linear maps rα, r′
α : U± →U±, as deﬁned in [17, Chapter 6].
Their restriction to U−is uniquely characterized by the properties:
rα(xy) = rα(x) y + v(α,|x|) x rα(y)
r′
α(xy) = x r′
α(y) + v(α,|x|) r′
α(x) y
(5)
and for any two fundamental roots α, β, (see [17, Eqn.(6.15.4)]) and
rα(F n
β ) = r′
α(F n
β ) = δα,β
1 −v2n
α
1 −v2α
F n−1
α
,
(6)
where vα := v(α,α)/2; see [17, Eqn.(8.26.2)].
Lemma 7.9 For a ﬁxed α ∈{α1, . . . , αℓ}, the matrix entries of the operators
(rα)k, (r′
α)k : U−→U−are q–holonomic with respect to k and the coordinates
of the matrix entry. Similarly, (rα)k, (r′
α)k : U+ →U+ are q–holonomic.
Proof We give a proof for rk
α : U−→U−. The other case is similar.
There is a reduced word w′ = si1 . . . sit representing the longest element ω0
of W such that αi1 = α.
Then w = si2 . . . sits¯α is another reduced word
representing ω0, where ¯α := −ω0(α).
For the PBW basis of U−associated with w it’s known that γt = α, and thus
ft = Fα. According to [17, 8.26.5], for every x in the algebra U−[t −1, 1], one
has
rα(x) = 0.
Using Equations (5) and (6) and induction, one can easily show that for every
x ∈U−[t −1, 1],
(rα)k(f nt
t x) =
k
Y
i=1
1 −v2nt−2i+2
α
1 −v2α
f nt−k
t
x,
This formula, applied to x = f nt−1
t−1 . . . f n1
1 , proves the statement.
7.4.2
