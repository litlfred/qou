---
doc_id: arxiv-math-9806163v1
doc_title: "Weights of Markov traces on Hecke algebras"
section_id: sec-013-10-r-c-orellana
section_title: "R. C. Orellana"
section_number: 10
pages: 10-10
source_pdf: 9806163v1.pdf
source_sha256: dba44975f29cb017
doc_brief: "Weights of Markov traces on Hecke algebras — We compute the weights, i.e. the values at the minimal idempo tents, for the Markov trace on the Hecke algebra of type Bn and type Dn."
---
Let d(tµ , i) = c(i + 1) − c(i) − r(i + 1) + r(i) where c(i) and r(i) denote respectively, the
column and row of the box containing the number i, and for d ∈ Z \ {0} let
ad(q) = qd(1 − q)
1 − qd and cd(q) =
√
(1 − qd+1)(1 − qd−1)
1 − qd .
Then one deﬁnes πµ on the vector space Vµ by
πµ (˜gi)vtµ = ad(q)vtµ + cd(q)v˜gi(tµ )
where d = d(tµ , i) and ˜gi(tµ ) is the tableau obtained by interchanging i and i + 1 in tµ . This
representation follows from the ones deﬁned in [W1] by setting πµ (˜gi) = ( q + 1)πµ (ei) − Id Vµ ,
where ei is the eigenprojection corresponding to the characteristic value q of ˜gi. More-
over πn = ⨁
µ ⊢n πµ is a faithful representation of Hn(q). Thus we have that Hn(q) ∼
=⨁
µ ⊢n πµ (Hn(q)), where πµ (Hn(q)) ∼= Mf µ and Mf µ is the ring of complex f µ × f µ matrices,
and f µ is the number of standard tableaux of shape µ.
If µ is a partition of n then denote by µ′ the partition obtained by decreasing one part
of µ by one; and µ′′ is obtained by decreasing one part of µ′ by one. Let tµ be a standard
tableau of shape µ, then tµ → (tµ )′ deﬁnes a bijection between Tµ and ⋃
µ ′⊂µ Tµ ′, where ( tµ )′
is the Young tableau obtained by removing the box containing n from tµ . This in turn yields
the following isomorphism of modules
Vµ
⏐
⏐
⏐
Hn−1(q)
∼
=
⨁
µ ′⊂µ
Vµ ′. (9)
A special element in Hf (q) is the full-twist deﬁned algebraically by ∆ 2
f := (˜gf −1 . . . ˜g1)f .
The full-twist is an element in the center of Hf (q). The action of ∆ 2
f on (πν , Vν) is described
in the following lemma, the proof of which appears in [W2], pg. 261.
Lemma 3.1 Let ν ⊢ f . Then the full-twist acts by a scalar αν on the irreducible represen-
tation (πν, Vν) of Hf (q) where
αν = qf (f −1)−∑
i<j (νi+1)νj .
