---
doc_id: arxiv-math-9806163v1
doc_title: "Weights of Markov Traces on Hecke Algebras ∗ R.C. Orellana"
section_id: sec-015-12-r-c-orellana
section_title: "R. C. Orellana"
section_number: 12
pages: 12-14
source_pdf: 9806163v1.pdf
source_sha256: dba44975f29cb017
doc_brief: "Weights of Markov Traces on Hecke Algebras ∗ R.C. Orellana — We compute the weights, i.e. the values at the minimal idempo tents, for the Markov trace on the Hecke algebra of type Bn and type Dn."
---
In order to determine the constant − α β
α γ
we only need to substitute the partitions β =
[m + 1, mr1−1] and γ = [mr1, 1] in the formula given in lemma 3.1. Thus we obtain
−αβ
αγ
= −q− ∑
i<j (β i+1)β j +∑
i<j (γi+1)γj = −qr1+m.
This concludes this proof. □
The following ﬁgure gives a pictorial deﬁnition of the homomorphism ρf,n deﬁned in the
previous lemma.
✟✟✟
❍ ❍ q q q
1 2 n
✲ρf,n
ptλ
1
q q q
f
ptλ
✥✥✥✥✥
❍
❍
f+1 f+2
q q q
f+n 1
q q q
❊
❊
❊❊
❊
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
✆✆
i+1
q q q
n
✲ρf,n
ptλ
1
q q q
f
ptλ
f+1
q q q
❊
❊
❊❊
❊
❊
❊
❊❊
f+i
✆
✆
✆
✆
✆
✆
✆
✆✆
f+i+1
q q q
f+n
Figure 6
We have shown that ρf,n is a homomorphism. In the remainder of this section we will
show that it is onto. In particular, we will show that the irreducible re presentations of the
reduced algebra are also irreducible representations of Hn(q, −qr1+m).
Notice that for µ ⊢ n + f there is a 1-1 correspondence between standard skew tableaux
of shape µ/λ and tableaux tµ which contain tλ . For this reason we denote by Tµ/λ the set
of standard tableaux which contain tλ . Notice that the order of Tµ/λ is equal to the number
of standard skew tableaux of shape µ/λ. For our choice of m, i.e. m > n , we have that µ/λ
will consist of two parts which can be interpreted as a double partitio n, say ( δ, γ). In this
case, the order of Tµ/λ is
( n
|δ|
)
f δf γ , where f γ is the number of standard tableaux of shape γ;
this formula is given by Hoefsmit in [H].
Deﬁne Vµ/λ as the complex vector space with orthonormal basis {vtµ | tµ ∈ Tµ/λ }. Notice
that Vµ/λ is a subspace of Vµ and ptλ Vµ = Vµ/λ , where Vµ has basis indexed by standard
tableaux of shape µ.
Observation: Let µ ⊢ n + f and Vµ be an irreducible Hn+f (q) module. Then ptλ Vµ is an
irreducible ptλ Hn+f (q)ptλ module.
This observation implies that there is a set of irreducible representa tions of ptλ Hn+f (q)ptλ
indexed by Young diagrams with n + f boxes, which contain λ. It follows from equation (9)
that
ptλ Vµ
⏐
⏐
⏐
ptλ Hn+f −1(q)ptλ
∼=
⨁
λ ⊂µ ′⊂µ
Vµ ′/λ (10)
where µ′ has n + f − 1 boxes and ptλ Vµ ′ = Vµ ′/λ .
Weights of Markov Traces on Hecke Algebras 13
We let zµ denote the minimal central idempotents of Hn+f (q), and zµ/λ denote the min-
imal central idempotents of ptλ Hn+f (q)ptλ . Notice that zµ/λ has rank equal to the number
of skew standard tableaux of shape µ/λ.
Theorem 3.3 Let f, n be as in Lemma 3.2 and assume that q is not a root of unity. Then
ρf,n as deﬁned in Lemma 3.2 is an onto homomorphism.
Proof: In Lemma 3.2 we showed that ρf,n is a homomorphism. Thus it only remains to show
that it is onto. The proof is by induction on n. For n = 1, we have ρf, 1 : H1(q, −qr1+m) →
ptλ Hf +1(q)ptλ . Since λ ⊢ f is a rectangular diagram there are only two Young diagrams with
f + 1 boxes which contain λ, i.e. [ m + 1, mr1−1] and [ mr1, 1]. As we showed in Lemma 3.2 the
action of ρf, 1(t) on the representation indexed by [ m + 1, mr1−1] (resp. [ mr1, 1]) is −qr1+m
(resp. −1). And both representations are 1 dimensional.
The algebra H1(q, −qr1+m) has two irreducible representations indexed by ([1] , ∅) and
(∅, [1]). Both of these representations are 1 dimensional and t ∈ H1(q, −qr1+m) acts by a
scalar on these representations. The action of t on V([1], ∅) (resp. V(∅, [1])) is −qr1+m (resp. −1).
Since q is not a root of unity, these representations are irreducible and no nequivalent. This
shows that π([1], ∅) ∼= π[m+1,m r1−1] and π(∅, [1]) ∼= π[mr1 , 1].
Assume that for n > 1 we have ρf,n is onto. Then for all µ containing λ, Vµ/λ is an
irreducible Hn+1(q, −qr1+m), and Vµ/λ
⏐
⏐
⏐
Hn(q, −qr1+m)
∼= ⨁
λ ⊂µ ′⊂µ Vµ ′/λ , as in equation (10).
The remainder of this proof is similar to the proof of irreducibility of mo dules of the
Hecke algebra of type A in [W1], Theorem 2.2.
Let µ ⊢ n + f + 1 be as described above. By the induction assumption, Hn(q, −qr1+m)
is a semisimple algebra with minimal central idempotents zµ ′/λ . Let 0 ⁄= W ⊂ Vµ/λ be an
Hn+1(q, −qr1+m) module. But Vµ/λ decomposes as an Hn(q, −qr1+m) module into the direct
sum of irreducible modules Vµ ′/λ since ρf,n is onto ptλ Hn+f (q)ptλ . Thus, there exists a µ′ ⊢
n + f such that Vµ ′/λ ⊂ W . Let ˜ µ′ ⁄= µ′ be another Young diagram with n + f boxes
such that λ ⊂ ˜µ′ ⊂ µ. There is exactly one µ′′ ⊢ n + f − 1 contained in both µ′ and ˜µ′
such that µ′′ contains λ. Let tµ ∈ Tµ/λ be such that ( tµ )′ ∈ Tµ ′/λ and ( tµ )′′ ∈ Tµ ′′/λ . Then
(˜gn+f (tµ ))′ ∈ T˜µ ′/λ and therefore
πµ (z˜µ ′/λ )πµ (˜gn+f )vtµ = cdv˜gn+f (tµ ) ∈ V˜µ ′/λ
where d is the axial distance in tµ between n + f and n + f + 1. Since q is not a root of unity
then cd is well-deﬁned and nonzero. Hence the irreducible Hn(q, −qr1+m) module, V˜µ ′/λ , is
contained in W. But ˜µ′ was arbitrary, therefore W ⊃ ⨁
µ ′⊂µ Vµ ′.
Next we show that the Vµ/λ are mutually nonisomorphic Hn+1(q, −qr1+m) modules. As
we observed above this is true for n = 1. For n = 2 there are ﬁve irreducible modules; 4 are
one dimensional and 1 is two dimensional. We must check that the one d imensional modules
are nonequivalent. By the deﬁnition of the action of t and ˜gf +1 we have that t acts by
