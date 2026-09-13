---
doc_id: arxiv-2101.05931v3
doc_title: "CATEGORICAL BRAID GROUP ACTIONS"
section_id: sec-008-4-perverse-equivalences
section_title: "Perverse equivalences"
section_number: 4
pages: 10-11
source_pdf: 2101.05931v3.pdf
source_sha256: 41eaa81b97ede8e9
doc_brief: "CATEGORICAL BRAID GROUP ACTIONS — Let g be a semisimple simply-laced Lie algebra of ﬁnite type."
---
4.1. General deﬁnition. Let T be a triangulated category with shift functor [1] : T → T . In
the cases of most interest to us, T is a subcategory of a derived category, in which case [1] is th e
homological shift functor. Suppose T has a t-structure t = (T ≤0, T ≥0), with heart T ♥ = T ≤0 ∩T ≥0
[4]. Recall that a triangulated functor F : T → S between triangulated categories with t-structure
is t-exact if F (T ≤0) ⊆ S ≤0 and F (T ≥0) ⊆ S ≥0. We let F [p] : T → S denote the pre-composition
of F with the p-shift [p].
Now let S ⊂ T be a thick triangulated subcategory, and consider the quoti ent functor Q :
T → T /S. Following [15], we say that t is compatible with S if tT /S = (Q(T ≤0),Q (T ≥0)) is a t-
structure on T/S. By [15, Lemmas 3.3 & 3.9], if t is compatible with S then (T/S)♥ = T ♥/T ♥ ∩S ,
and tS = (S ∩ T ≤0, S ∩ T ≥0) is a t-structure on S such that S ♥ = T ♥ ∩ S .
Now suppose that T, T ′ are two triangulated categories with t-structures t,t ′. Suppose further
that we have ﬁltrations by thick triangulated subcategorie s:
0 ⊂ T 0 ⊂ T 1 ⊂ · · · ⊂ T r = T, 0 ⊂ T ′
0 ⊂ T ′
1 ⊂ · · · ⊂ T ′
r = T ′,
such that for everyi,t is compatible with Ti andt′ is compatible with T ′
i . By [15, Lemma 3.11], tTi is
also compatible with Ti−1, and hence Ti/Ti−1 inherits a natural t-structure. Let p : {0,...,r } → Z.
The data ( T•, T ′
•,p ) is termed a perversity triple .
Although Chuang and Rouquier didn’t formulate perverse equ ivalences for graded categories, it
is straightforward to extend their deﬁnitions to this setti ng.
Deﬁnition 4.1. A graded equivalence of graded triangulated categories F : T → T ′ is a (graded)
perverse equivalence with respect to ( T•, T ′
•,p ) if for every i,
(1) F(Ti) = T ′
i , and
(2) the induced equivalence F[−p(i)] : Ti/Ti−1 → T ′
i/T ′
i−1 is t-exact.
For brevity, we say F is perverse if it is a graded perverse equivalence with respect to some
perversity datum. Since we will be working exclusively in th e graded setting, a perverse equivalence
for us will always mean a graded perverse equivalence.
A perverse equivalence F : T → T ′ induces a bijection ϕF : Irr(T ♥) → Irr(T ′♥). Indeed, by (2)
F[−p(i)] induces a bijection Irr(T ♥
i ) \ Irr(T ♥
i−1) → Irr(T ′♥
i ) \ Irr(T ′♥
i−1), and these yield ϕF.
Although the construction of ϕF depends on a choice of perversity triple, the resulting bije ction
does not when T ♥, T ′♥ have ﬁnitely many simple objects. This follows from the foll owing lemma.
CATEGORICAL BRAID GROUP ACTIONS AND CACTUS GROUPS 11
Lemma 4.2 ([33], Lemma 2.4) . Suppose that T ♥, T ′♥ have ﬁnitely many simple objects, and for
i = 1, 2 let Fi : T → T ′ be a perverse equivalence with respect to the perversity dat um (Ti,•, T ′
i,•,p i).
If the induced maps [F1], [F2] : [ T ]Z → [T ′]Z coincide then ϕF1 =ϕF2 .
Corollary 4.3. Suppose that T ♥, T ′♥ have ﬁnitely many simple objects, and F : T → T ′ is
perverse. Then ϕF is independent of the choice of perversity triple.
Proof. Suppose F is a graded perverse equivalence with respect to two choices of perversity triples
(Ti,•, T ′
i,•,p i), i = 1, 2. Now apply the lemma. □
The proofs of the following lemmas are straightforward.
Lemma 4.4. Suppose F : T → T ′ is perverse. Then for any ℓ ∈ Z, F[ℓ] is also perverse and
ϕF[ℓ] =ϕF.
Lemma 4.5. Suppose F : T → T ′ is a perverse equivalence with respect to (T•, T ′
•,p ), and G : T ′ →
T ′′ is a perverse equivalence with respect to (T ′
•, T ′′
• ,q ). Then G ◦ F is a perverse equivalence with
respect to (T•, T ′′
• ,p +q), and ϕG◦F =ϕG ◦ϕF.
Lemma 4.6. Let T, T ′ be triangulated with t-structures t,t ′, and let S ⊂ T , S ′ ⊂ T ′ be thick
triangulated subcategories such that t is compatible with S and t′ is compatible with S ′. Suppose
further that F : T → T ′ is a perverse equivalence with respect to (T•, T ′
•,p ), and F(S) = S ′.
Deﬁne Si = S ∩ T i, S ′
i = S ′ ∩ T ′
i and (T/S)i = Q(Ti), (T ′/S ′)i = Q′(T ′
i ). Let G : S → S ′ and
H : T/S → T ′/S ′ be the induced equivalences. Then:
(1) G is a perverse equivalence with respect to (S•, S ′
•,p ), and ϕG =ϕF|IrrS ♥.
(2) H is a perverse equivalence with respect to ((T/S)•, (T ′/S ′)•,p ), and ϕH =ϕF|IrrT ♥\IrrS ♥.
Lemma 4.7 ([33], Lemma 2.4) . Suppose F : T → T ′ is perverse, and G (respectively G′) is an
autoequivalence of T (respectively T ′) which is t-exact up to shift. Then G′ ◦ F ◦ G is perverse, and
ϕG′◦F◦G =ϕG′ ◦ϕF ◦ϕG′.
Note that in [33, Lemma 2.4] is stated for functors which are t -exact. Our formulation for
functors which are t-exact up to shift follows by Lemma 4.4.
