---
doc_id: arxiv-math-9806163v1
doc_title: "Weights of Markov traces on Hecke algebras"
section_id: sec-014-32-a-homomorphism-of-hnq-qr1m-onto-a-reduced-alg
section_title: "A Homomorphism of Hn(q, −qr1+m) onto a reduced algebra of"
section_number: 3.2
pages: 10-12
source_pdf: 9806163v1.pdf
source_sha256: dba44975f29cb017
doc_brief: "Weights of Markov traces on Hecke algebras — We compute the weights, i.e. the values at the minimal idempo tents, for the Markov trace on the Hecke algebra of type Bn and type Dn."
---
Hn+f (q)
In ([W1], Cor. 2.3) Wenzl deﬁned a special set of minimal idempotents of Hf (q) indexed by
the standard tableaux. The sum of these idempotents is 1. These m inimal idempotents are
well-deﬁned whenever Hf (q) is semisimple.
Weights of Markov Traces on Hecke Algebras 11
If p ∈ Hf (q) is an idempotent then the reduced algebra of Hf (q) is pHf (q)p := {pap | a ∈
Hf (q)}. Let λ ⊢ f and tλ be a standard tableau of shape λ. Then ptλ is the minimal
idempotent indexed by tλ . Thus, the reduced algebra decomposes as follows:
ptλ Hn+f (q)ptλ ∼
=
⨁
λ ⊂µ,
µ ⊢n+f
πµ (ptλ )πµ (Hn+f (q))πµ (ptλ ).
Notice that if µ is a partition of n + f and µ does not contain λ then πµ (ptλ ) is the zero
matrix. In particular, if we choose λ to be rectangular, we have that the reduced algebra
ptλ Hf +1(q)ptλ has only two nonzero irreducible modules indexed by partitions [ m + 1, mr1−1]
and [ mr1, 1], since these are the only partitions of f + 1 which contain λ.
Recall that in Section 1 we showed that there is a homomorphism ˜ ρf,n from the braid
group Bn(B) into the braid group Bf +n(A). In what follows we will show that it is possible
to extend ˜ρf,n to a homomorphism of the corresponding Hecke algebras.
Lemma 3.2 For a ﬁxed integer n and m, r1 ∈ N, let m > n and r1 > n . Set f = mr1
and assume λ = [ mr1] and γ = [ mr1, 1]. Let αλ and αγ be as in Lemma 3.1. Choose a
minimal idempotent ptλ in Hf (q). We deﬁne a map ρf,n for the generators of Hn(q, −qr1+m)
as follows:
ρf,n (1) = ptλ , ρ f,n (t) = −αλ
αγ
ptλ ∆ −2
f ∆ 2
f +1 and ρf,n (gi) = ptλ ˜gi+f
for i = 1 , . . . , n − 1, (see Figure 6 for a pictorial deﬁnition). Then ρf,n extends to a well-
deﬁned homomorphism of algebras, ρf,n : Hn(q, −qr1+m) → ptλ Hn+f (q)ptλ .
Proof: It is enough to check that ρf,n preserves the relations of the Hecke algebra of type
B. First notice that since ptλ ∈ Hf (q), it commutes with all ˜ gj for all j > f . From this
observation and the deﬁning relations of Hn+f (q) it follows that we only need to check the
relations involving ρf,n (t). For relations (H5) and (H6), (see pg. 7), notice that ptλ commutes
with the full-twist ∆ 2
f +1, ∆ −2
f and with ˜gf +1. Thus these two relations will hold by the proof
of Prop. 1.2.
It remains to be shown that ρf,n (t) has two eigenvalues: −1 and Q = −qr1+m. In
particular, we want to show that ρf,n (t) acts by a scalar on two irreducible modules of
Hf +1(q) and by 0 on all others. Since λ is rectangular this means that there are only two
partitions of f + 1 containing it.
By lemma 3.1 we have that the full-twist, ∆ 2
f +1, acts by the scalar αβ (resp. αγ ) on the
irreducible module indexed by β (resp. γ). Also ∆ −2
f acts by α−1
λ on the irreducible modules
of Hf +1(q) which are indexed by Young diagrams which contain λ. Therefore, we have that
∆ −2
f ∆ 2
f +1 acts by αβ α−1
λ on the module Vβ and by αγ α−1
λ on the module Vγ . Therefore, we
have that − α λ
α γ
ptλ ∆ −2
f ∆ 2
f +1 acts by −1 on Vγ and by − α β
α γ
on Vβ , and by zero on all other
modules, since ptλ kills all modules which do not contain λ.
