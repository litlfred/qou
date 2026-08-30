---
doc_id: arxiv-math-0508291v1
doc_title: "Stein’s Method and Random Character Ratios"
section_id: sec-003-32-central-limit-theorems-for-character-ratios
section_title: "Central limit theorems for character ratios"
section_number: 3.2
pages: 9-14
source_pdf: 0508291v1.pdf
source_sha256: d2d541426aaec742
doc_brief: "Stein’s Method and Random Character Ratios — Stein’s method is used to prove limit theorems for random character ratios."
---
section is to prove a central limit theorem for the random var iableW deﬁned
byW (λ) = |C|1/ 2χ λ (C)
dim(λ ) , whereC is a ﬁxed conjugacy class such that C =C −1
and λ is random from the Plancherel measure of G.
For this purpose, it is useful to construct a Markov chain on t he set of
irreducible representations of G as follows. First, ﬁx a non-trivial irreducible
representationτ whose character is real valued. This gives a Markov chain
Lτ by deﬁning the probability of transitioning from λ to ρ as
Lτ (ρ,λ ) := dim(ρ)
dim(λ)dim(τ )
1
|G|
∑
g
χλ (g)χτ (g)χρ(g).
It is worth remarking that since Stein’s method is in the spir it of Taylor
approximation,τ should typically be chosen to be as close as possible to the
trivial representation.
Lemma 3.6 veriﬁes that Lτ is a Markov chain which is reversible with
respect to Plancherel measure.
Lemma 3.6. The transition probabilities of Lτ are real and non-negative
and sum to 1. Moreover the chain Lτ is reversible with respect to the
Plancherel measure of G.
Proof. The transition probabilities of Lτ are real and non-negative since
1
|G|
∑
g
χλ (g)χτ (g)χρ(g)
is the multiplicity of ρ in the tensor product of λ and τ . Letting id denote
the identity, it follows from Lemma 3.3 that
∑
ρ
Lτ (λ,ρ ) = 1
dim(λ)dim(τ )|G|
∑
g
χλ (g)χτ (g)
∑
ρ
χρ(id)χρ(g) = 1.
For the reversibility assertion, the fact that χτ and the transition probabil-
ities of Lτ are both real valued implies that
dim(λ)2
|G| Lτ (λ,ρ ) = dim(ρ)2
|G| Lτ (ρ,λ ).
□
An exchangeable pair ( W,W ′) is now constructed from the chain Lτ in
the standard way. First choose λ from the Plancherel measure of G, then
chooseρ with probability Lτ (λ,ρ ), and ﬁnally let ( W,W ′) = (W (λ),W (ρ)).
The remaining results in this subsection show that the excha ngeable pair
(W,W ′) has desirable properties.
Lemma 3.7. E(W ′|W ) =
(
χ τ (C)
dim(τ)
)
W .
10
Proof. From the deﬁnition of W ′,
E(W ′|λ) = |C|1/ 2∑
ρ
dim(ρ)
dim(λ)dim(τ )
1
|G|
∑
g
χλ (g)χτ (g)χρ(g)χρ(C)
dim(ρ)
= |C|1/ 2
|G|
∑
g
χλ (g)
dim(λ)
χτ (g)
dim(τ )
∑
ρ
χρ(C)χρ(g)
=
( χτ (C)
dim(τ )
)
W (λ),
where the last step is Lemma 3.3. The result follows since thi s depends on
λ only through W . □
Corollary 3.8 is not needed in what follows, but is worth reco rding.
Corollary 3.8. The eigenvalues of Lτ are χ τ (C)
dim(τ) asC ranges over conjugacy
classes of G. The functions ψC(λ) = |C|1/ 2χ λ (C)
dim(λ ) are a basis of eigenvectors
of Lτ , orthonormal with respect to the inner product
⟨f1,f 2⟩ =
∑
λ
f1(λ)f2(λ)dim(λ)2
|G| .
Proof. The proof of Lemma 3.7 shows that ψC is an eigenvector of Lτ with
eigenvalue χ τ (C)
dim(τ) . The orthonormality assertion follows from Lemma 3.3,
and the basis assertion follows since the number of conjugac y classes of G
is equal to the number of irreducible representations of G. □
Lemma 3.9. E(W ′ −W )2 = 2
(
1 − χ τ (C)
dim(τ)
)
.
Proof. This is immediate from Lemma 2.3 and 3.7. □
For the remainder of this subsection, if K is a conjugacy class of G,pm(K)
will denote the probability that the random walk generated b y C is in K
after m steps.
Lemma 3.10.
E((W ′)2|λ) = |C|
dim(λ)dim(τ )
∑
K
p2(K)χλ (K)χτ (K)
where the sum is over all conjugacy classes K of G.
Proof.
E((W ′)2|λ)
= 1
dim(λ)dim(τ )|G|
∑
ρ
dim(ρ)
∑
g
χλ (g)χτ (g)χρ(g)
(
|C|1/ 2χρ(C)
dim(ρ)
) 2
= |C|
dim(λ)dim(τ )|G|
∑
g
χλ (g)χτ (g)
∑
ρ
dim(ρ)χρ(g)
( χρ(C)
dim(ρ)
) 2
.
11
The result now follows from Lemma 3.4. □
Lemma 3.11 writes Var ([E(W ′ −W )2|λ]) as a sum of positive quantities.
Lemma 3.11.
Var ([E(W ′ −W )2|λ]) = |C|2 ∑
K⁄=id
p2(K)2
|K|
( χτ (K)
dim(τ ) + 1 − 2χτ (C)
dim(τ )
) 2
,
whereK ranges over all non-identity conjugacy classes of G.
Proof. By Lemmas 3.10, 3.9, and 3.7,
Var ([E(W ′ −W )2|λ])
= E
(
E((W ′ −W )2|λ)2)
− 4
(
1 − χτ (C)
dim(τ )
) 2
= |C|2E
[ ∑
Kp2(K)χλ (K)χτ (K)
dim(λ)dim(τ ) +
(
1 − 2χτ (C)
dim(τ )
)( χλ (C)
dim(λ)
) 2] 2
−4
(
1 − χτ (C)
dim(τ )
) 2
= T1 +T2 +T3 − 4
(
1 − χτ (C)
dim(τ )
) 2
where
T1 = |C|2
dim(τ )2 E
( ∑
K
p2(K)χλ (K)χτ (K)
dim(λ)
) 2
T2 = 2|C|2
dim(τ )
(
1 − 2χτ (C)
dim(τ )
) ∑
K
p2(K)χτ (K)E
[
χλ (K)
dim(λ)
( χλ (C)
dim(λ)
) 2]
.
T3 = |C|2
(
1 − 2χτ (C)
dim(τ )
) 2
E
( χλ (C)
dim(λ)
) 4
.
Fortunately, these terms can be simpliﬁed. By Lemma 3.10, th e expres-
sion inside parentheses in T1 is real. Since χτ is real valued, Lemma 3.3
implies that
T1 = |C|2∑
K
p2(K)2
|K|
χτ (K)2
dim(τ )2.
Since χλ (C) is real, Lemma 3.4 implies that
T2 = 2|C|2
(
1 − 2χτ (C)
dim(τ )
) ∑
K
p2(K)2
|K|
χτ (K)
dim(τ )
12
and since C =C −1,
T3 = |C|2
(
1 − 2χτ (C)
dim(τ )
) 2
p4(id)
= |C|2
(
1 − 2χτ (C)
dim(τ )
) 2∑
K
p2(K)2
|K| .
Thus one can write
T1 +T2 +T3 = |C|2∑
K
p2(K)2
|K|
( χτ (K)
dim(τ ) + 1 − 2χτ (C)
dim(τ )
) 2
and the result follows since p2(id) = 1
|K|. □
Lemma 3.12. Letk be a positive integer.
(1) E(W ′ −W )k = |C|k/ 2∑ k
m=0(−1)k−m( k
m
) ∑
K
χ τ (K)
dim(τ)
pm(K)pk−m(K)
|K| .
(2) E(W ′ −W )4 is equal to
|C|2∑
K
[
8
(
1 − χτ (C)
dim(τ )
)
− 6
(
1 − χτ (K)
dim(τ )
)] p2(K)2
|K| .
Proof. For the ﬁrst assertion, note that
E((W ′ −W )k|λ) = |C|k/ 2
dim(λ)dim(τ )
∑
ρ
dim(ρ)
|G|
∑
g
χλ (g)χτ (g)χρ(g)
·
k∑
m=0
(−1)k−m
( k
m
)( χρ(C)
dim(ρ)
) m( χλ (C)
dim(λ)
) k−m
= |C|k/ 2
dim(λ)dim(τ )
k∑
m=0
(−1)k−m
( k
m
)( χλ (C)
dim(λ)
) k−m
·
∑
g
χτ (g)χλ (g)
∑
ρ
dim(ρ)
|G|
( χρ(C)
dim(ρ)
) m
χρ(g)
= |C|k/ 2
dim(λ)dim(τ )
k∑
m=0
(−1)k−m
( k
m
)( χλ (C)
dim(λ)
) k−m
·
∑
K
χ τ (K)χλ (K)pm(K),
where the ﬁnal equality is by Lemma 3.4. Thus E((W ′ −W )k) is equal to
E(E((W ′ −W )k|λ))
= |C|k/ 2
dim(τ )
k∑
m=0
(−1)k−m
( k
m
)
·
∑
K
pm(K)χτ (K)
∑
λ
dim(λ)2
|G|
χλ (K)
dim(λ)
( χλ (C)
dim(λ)
) k−m
.
13
The ﬁrst assertion now follows from Lemma 3.4 and the fact tha t χλ (C) is
real for all λ.
For the second assertion, note by the ﬁrst assertion that
E(W ′ −W )4 = |C|2
4∑
m=0
(−1)m
( 4
m
) ∑
K
χτ (K)
dim(τ )
pm(K)p4−m(K)
|K| .
If τ is the trivial representation, then W ′ =W , which implies that
0 = |C|2
4∑
m=0
(−1)m
( 4
m
) ∑
K
pm(K)p4−m(K)
|K| .
Thus for general τ ,
E(W ′ −W )4 = −|C|2
4∑
m=0
(−1)m
( 4
m
) ∑
K
(
1 − χτ (K)
dim(τ )
) pm(K)p4−m(K)
|K| .
Observe that the m = 0, 4 terms in this sum vanish, since the only contri-
bution could come from the identity, which contributes 0. Th e m = 2 term
is
−6|C|2∑
K
(
1 − χτ (K)
dim(τ )
) p2(K)2
|K| .
Them = 1, 3 terms are equal and together contribute
8|C|2∑
K
(
1 − χτ (K)
dim(τ )
) p1(K)p3(K)
|K|
= 8 |C|
(
1 − χτ (C)
dim(τ )
)
p3(C)
= 8 |C|2
(
1 − χτ (C)
dim(τ )
)
p4(id)
= 8 |C|2
(
1 − χτ (C)
dim(τ )
) ∑
K
p2(K)2
|K| ,
whereid is the identity and the last two equalities can be seen either directly
or from Lemma 3.4. This completes the proof of the second asse rtion. □
Putting the pieces together, one obtains the following theo rem.
Theorem 3.13. LetC be a conjugacy class of a ﬁnite group G such thatC =
C −1 and ﬁx a nontrivial irreducible representation τ of G whose character
is real valued. Let λ be a random irreducible representation, chosen from the
14
Plancherel measure of G. Let W = |C|1/ 2χ λ (C)
dim(λ ) . Then for all real x0,
⏐
⏐
⏐
⏐P(W ≤x0) − 1
√
2π
∫ x0
−∞
e− x2
2 dx
⏐
⏐
⏐
⏐
≤ |C|
a
/radicaltp
/radicalvertex
/radicalvertex
√
∑
K⁄=id
p2(K)2
|K|
( χτ (K)
dim(τ ) + 2a − 1
) 2
+
[
|C|2
π
∑
K
(
8 − 6
a
(
1 − χτ (K)
dim(τ )
)) p2(K)2
|K|
] 1/ 4
,
wherea = 1 − χ τ (C)
dim(τ) .
Proof. One applies Theorem 2.1 to the exchangeable pair ( W,W ′) of this
subsection. By Lemmas 2.4 and 3.11, the ﬁrst term in Theorem 2 .1 gives
the ﬁrst term in the theorem. To upper bound the second term in Theorem
2.1, note by the Cauchy-Schwarz inequality that
E|W ′ −W |3 ≤
√
E(W ′ −W )2E(W ′ −W )4.
Now use Lemma 3.9 and part 2 of Lemma 3.12. □
