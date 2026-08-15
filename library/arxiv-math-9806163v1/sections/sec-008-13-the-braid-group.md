---
doc_id: arxiv-math-9806163v1
doc_title: "Weights of Markov Traces on Hecke Algebras ∗ R.C. Orellana"
section_id: sec-008-13-the-braid-group
section_title: "The Braid Group"
section_number: 1.3
pages: 6-7
source_pdf: 9806163v1.pdf
source_sha256: dba44975f29cb017
doc_brief: "Weights of Markov Traces on Hecke Algebras ∗ R.C. Orellana — We compute the weights, i.e. the values at the minimal idempo tents, for the Markov trace on the Hecke algebra of type Bn and type Dn."
---
The braid group of type A, Bn(A), can be deﬁned algebraically by generators ˜σ1, ˜σ2, . . . , ˜σn−1
and relations
˜σi ˜σj = ˜σj ˜σi if |i − j| > 1, (4)
˜σi ˜σi+1˜σi = ˜σi+1˜σi ˜σi+1 if 1 ≤ i ≤ n − 2 (5)
Similarly we can deﬁne the braid group of type B, Bn(B), by generators t, σ1, σ2, . . . , σn−1
and deﬁning relations given by equations (4) and (5) and
σ1tσ1t = tσ1tσ1 (6)
tσi = tσi if i > 1. (7)
Below we illustrate the generator ˜ σi ∈ B n(A), the full-twist ∆ 2
3 ∈ B 3(A), and the gener-
ators t, σi ∈ B n(B).
1
q q q ❊
❊
❊
❊❊
❊
❊
❊❊
i
✆
✆
✆
✆
✆
✆
✆
✆
✆✆
i+1
q q q
n
˜σi
❉❉
1
❉❉
2
❉❉
3
✭✭✭
❉
❉❉
❉
❉❉
❉
❉❉
✭✭✭
❉❉❉❉❉
❉
✭✭✭
❉
❉❉
❉
❉❉
❉
❉❉
∆ 2
3
1
✘✘✘
❍ ❍
2
q q q
n
t
1
q q q ❊
❊
❊
❊❊
i
✆
✆
✆
✆
✆
✆
✆
✆
✆✆
i+1
❊
❊
❊❊
q q q
n
σi
Figure 3
In general, the full-twist ∆ 2
f in f strings, is an element in the center of Bf (A). Alge-
braically, ∆ 2
f = (˜σf −1 . . . ˜σ1)f . We now deﬁne a map from the generators of Bn(B) into
Bf +n(A). We call the map ˜ ρf,n , and we deﬁne the image of the generators of Bn(B) as
follows: ˜ρf,n (t) = ∆ −2
f ∆ 2
f +1 and ˜ρf,n (σi) = ˜σf +i for i = 1 , . . . , n. Pictorially, we have the
following:
q q q
✥✥✥✥✥✥
❍
q q q ❍
∆ −2
f ∆ 2
f +1
1 2 f f+1
q q q
q q q
f+2 f+n
✟✟✟
❍ ❍
q q q
q q q
1 2 n
✲˜ρf,n
t
q q q
❊
❊
❊❊
✆
✆
✆
✆
✆
✆
✆
✆✆
❊
❊
❊
❊❊
q q q ✲˜ρf,n
1 i i+1 n
σi
q q q
❊
❊
❊❊
✆
✆
✆
✆
✆
✆
✆
✆✆
❊
❊
❊
❊❊
q q q
f+n1 f+i+1f+i
˜σf +i
Figure 4
Weights of Markov Traces on Hecke Algebras 7
Proposition 1.1 Let n, f ∈ N and ˜ρf,n be as deﬁned above for the generators of Bn(B).
Then ˜ρf,n is a well-deﬁned group homomorphism.
Proof: It suﬃces to prove that ˜ ρf,n preserves the relations of Bn(B). It is convenient
to express ˜ρf,n (t) = ˜σf . . . ˜σ2˜σ2
1 ˜σ2 . . . ˜σf . Relations (4),(5) and (7) follow immediately from
the deﬁnition of ˜ ρf,n and the deﬁnition of Bn(A). To show that (6) holds we will use the
commuting property of the full-twist.
σf +1∆ 2
f +1∆ −2
f σf +1∆ 2
f +1∆ −2
f = ∆ 2
f +2∆ −2
f +1∆ 2
f +1∆ −2
f = ∆ 2
f +1∆ −2
f σf +1∆ 2
f +1∆ −2
f σf +1.
It might be easier to see that this relation holds from the picture, se e ﬁgure 5. This completes
the proof. □
q q q
✥✥✥✥✥✥
q q q❍
❍
✥✥✥✥✥
q q q
❍
❍
q q q
1 f f+1 f+2 f+3 f+n
˜σ f +1∆ −2
f ∆ 2
f +1 ˜σ f +1∆ −2
f ∆ 2
f +1
=
q q q
✥✥✥✥✥
q q q❍
❍
✥✥✥✥✥✥
q q q❍
❍
q q q
1 f f+1 f+2 f+3 f+n
∆ −2
f ∆ 2
f +1 ˜σ f +1∆ −2
f ∆ 2
f +1 ˜σ f +1
Figure 5
Corollary 1.2 The representations ρf,n can be extended in a natural way to representations
of the corresponding braid group algebras.
