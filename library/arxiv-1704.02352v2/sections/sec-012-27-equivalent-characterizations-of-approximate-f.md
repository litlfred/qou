---
doc_id: arxiv-1704.02352v2
doc_title: "GAUSSIAN FLUCTUATIONS OF JACK-DEFORMED RANDOM YOUNG DIAGRAMS"
section_id: sec-012-27-equivalent-characterizations-of-approximate-f
section_title: "Equivalent characterizations of approximate factorization of characters"
section_number: 2.7
pages: 18-23
source_pdf: 1704.02352v2.pdf
source_sha256: 9a14dd6ee33248d3
doc_brief: "GAUSSIAN FLUCTUATIONS OF JACK-DEFORMED RANDOM YOUNG DIAGRAMS — We introduce a large class of random Y oung diagrams which can be regarded as a natural one-parameter deformation of so me classi- cal Y"
---
acters. The following result, Theorem 2.3, is the key tool for the pur poses
of the current paper. Its main content is part ( a); roughly speaking, it states
that each of the four families of numbers (2.6)–(2.9) can be t ransformed into
the others. Each of these four families describes some conve nient aspect of
the characters χn in the limit n → ∞. To be more speciﬁc:
• The family (2.8) (and its subset, the family (2.7)) has a dire ct prob-
abilistic meaning. It contains information about the cumul ants of
some random variables which might be handy while proving pro b-
abilistic statements such as Central Limit Theorem or Law of Large
Numbers.
• On the other hand, the cumulants appearing in the families (2 .6) and
(2.9) are purely algebraic and do not have any direct probabilistic
meaning. However, their merit lies in the fact that in many co n-
crete applications (such as the ones from [D ´S18]) it is much simpler
JACK-DEFORMED RANDOM YOUNG DIAGRAMS 19
to verify algebraic conditions ( A) and ( D) than their probabilistic
counterparts (B) and (C).
Theorem 2.3 (The key tool) . Assume that α = α(n) is such as in Sec-
tion 1.11. Assume also that for each integer n ≥ 1 we are given a reducible
Jack character χn : Pn → R.
(a) Equivalent characterization of approximate factorizatio n property.
Then the following four conditions are equivalent:
(A) for each integer ℓ ≥ 1 and all integers l1, . . . , lℓ ≥ 2 the limit
(2.6) lim
n→∞
kχn
ℓ (l1, . . . , lℓ) n
l1+···+lℓ+ℓ−2
2
exists and is ﬁnite;
(B) for each integer ℓ ≥ 1 and all x1, . . . , xℓ ∈ { Ch1, Ch2, . . .}
the limit
(2.7) lim
n→∞
κχn
ℓ (x1, . . . , xℓ) n− deg x1+···+deg xℓ−2(ℓ−1)
2
exists and is ﬁnite;
(C) for each integer ℓ ≥ 1 and all x1, . . . , xℓ ∈ P the limit
(2.8) lim
n→∞
κχn
ℓ (x1, . . . , xℓ) n− deg x1+···+deg xℓ−2(ℓ−1)
2
exists and is ﬁnite;
(D) for each integer ℓ ≥ 1 and all x1, . . . , xℓ ∈ P• the limit
(2.9) lim
n→∞
κχn
•ℓ (x1, . . . , xℓ) n− deg x1+···+deg xℓ−2(ℓ−1)
2
exists and is ﬁnite.
(b) Assume that the conditions from part ( a) hold true. Furthermore,
assume that for ℓ = 1 the rate of the convergence of any of the four
expressions under the limit symbol in (2.6)– (2.9) is of the form
(2.10) const1 + const2 +o(1)√n
in the limit n → ∞ and all choices of l1 (respectively, for all choices
of x1); the constants depend on the choice of l1 (respectively, x1).
Then for ℓ = 1 the rate of convergence of each of the four expres-
sions (2.6)– (2.9) is of the form (2.10).
20 MACIEJ DOŁ ˛ EGA AND PIOTR ´SNIADY
When α = 1, part (a) of the above result corresponds to [ ´Sni06, Theorem
and Deﬁnition 1]. The proof is postponed to Section 3.
3. P ROOF OF THEOREM 2.3
In the current section we shall prove the key tool, Theorem 2. 3.
Additionally, concerning part ( a) of Theorem 2.3 we shall discuss the
exact relationship between the limits of the quantities (2.6)–(2.9) in the case
ℓ ∈ {1, 2}. This relationship provides the information about the limi t shape
of random Y oung diagrams in Theorem 1.3 as well as about the co variance
of the limit Gaussian process describing the ﬂuctuations in Theorem 1.5.
Concerning part ( b) of Theorem 2.3 we shall discuss the exact relation-
ship between the constants which describe the ﬁne asymptoti cs (2.10) of
the quantities (2.6)–(2.9) in the case ℓ = 1 . This relationship provides the
information about the mean value E∆ ∞ of the limit Gaussian process from
Equation (1.19).
3.1. Approximate factorization property for α-polynomial functions.
Deﬁnition 3.1. Let A and B be ﬁltered, commutative, unital algebras and let
E : A → B be a unital map. We say that E has approximate factorization
property if for all choices of x1, . . . , xℓ ∈ A we have that
(3.1) degB κB
A(x1, . . . , xℓ) ≤ (degA x1) + · · · + (degA xℓ) − 2(ℓ − 1).
We consider the ﬁltered unital algebras P• and P from Section 2.5, and
as a conditional expectation between them we take the identi ty map:
(3.2) P• P.
id
We denote by κ• := κP
P• the conditional cumulants related to the condi-
tional expectation (3.2).
We are now ready to state the main auxiliary result, proved ve ry recently
by the second-named author, which will be necessary for the p roof of the
key tool, Theorem 2.3.
Theorem 3.2 ([ ´Sni18, Theorem 2.3]) . The identity map (3.2) has approxi-
mate factorization property.
3.2. Approximate factorization for α = 1. We denote by P (1) a version
of the ﬁltered algebra of α-polynomial functions P obtained by the spe-
cialization α := 1 , γ := 0 ; analogously we denote by P (1)
• the algebra
P (1) equipped with the multiplication given by the disjoint prod uct.
The following result has been proved earlier by the second-named author.
JACK-DEFORMED RANDOM YOUNG DIAGRAMS 21
Theorem 3.3 ([ ´Sni06, Theorem 15]) . The identity map
(3.3) P (1)
• P (1).id
has approximate factorization property.
Theorems 3.2 and 3.3 are of the same ﬂavor. There are two major dif-
ferences between them: ﬁrstly, the arrows in (3.2) and (3.3) point in the
opposite directions; secondly, the algebra P is more rich than its special-
ized version P (1), in particular the variable γ ∈ P is not treated like a
scalar since deg γ = 1 > 0.
3.3. Proof of Theorem 2.3, part ( a). This proof follows closely its coun-
terpart from the work of the second-named author [ ´Sni06, Theorem and
Deﬁnition 1] with the references to Theorem 3.3 replaced by T heorem 3.2
and, occasionally, the roles of P and P• reversed. We present the details
below.
3.3.1. Proof of the equivalence ( A) ⇐ ⇒ (D).. The quantities (2.6) and
(2.9) coincide with their counterparts from the work of the s econd-named
author [ ´Sni06, Eqs. (12) and (13)]. The equivalence of the condition s (A)
and (D) was proved in [ ´Sni06, Section 4.7].
3.3.2. Proof of the equivalence (B) ⇐ ⇒(C).. The implication (C) =⇒ (B)
is immediate since Ch1, Ch2, . . . ∈ P.
The following result was proved by the second-named author [ ´Sni06,
Corollary 19] (note that the original paper does not contain the assump-
tion (3.5) without which it is not true). The proof did not use any speciﬁc
properties of the ﬁltered algebra P and thus it remains valid also in our
context when the original algebra of polynomial functions is replaced by
the algebra of α-polynomial functions.
Lemma 3.4. Assume that X ⊆ P is a set with the property that each
z ∈ P can be expressed as a polynomial in the elements of X:
(3.4) z =
∑
1≤i≤n
zi,1 · · ·zi,li
for some n ≥ 0 and zi,j ∈ X in such a way that such that for each value of
1 ≤ i ≤ n
(3.5) deg z ≥ deg zi,1 + · · · + deg zi,li;
in other words the degree of each monomial should be bounded f rom above
by the degree of z.
Under the above assumption, if condition (B) holds true for all x1, . . . , xℓ ∈
X then more general condition (C) holds true for arbitrary x1, . . . , xℓ ∈ P.
22 MACIEJ DOŁ ˛ EGA AND PIOTR ´SNIADY
We claim that the set X = {γ, Ch1, Ch2, Ch3, . . .} generates the ﬁltered
algebra P in the way speciﬁed in Lemma 3.4. Indeed, by the way the
ﬁltration on P was deﬁned (cf. Deﬁnition 2.2) it is enough to check the
assumption of Lemma 3.4 for z = γk Chπ for integer k ≥ 0 and a partition
π = ( π1, . . . , πℓ); we will do it by induction over deg z = k + |π| + ℓ. We
write
z = γk Chπ1 · · · Chπℓ +
[
γk Chπ −γk Chπ1 · · ·Chπℓ
]
.
The ﬁrst summand on the right-hand side is of the form which is ﬁts the
framework given by the right-hand side of (3.4). By [DF16, Co rollary 2.5,
Corollary 3.8], the second summand on the right-hand side is of smaller
degree, thus the inductive hypothesis can be applied. This c oncludes the
proof.
We claim that (2.7) holds true for all x1, . . . , xℓ ∈ X. Indeed, in the
case when x1, . . . , xℓ ∈ { Ch1, Ch2, . . .} this is just the assumption ( C).
Consider now the remaining case when xj = γ for some index j. For ℓ = 1
the corresponding expression from (2.8) is equal to
κχn
1 (γ) n− 1
2 = γ√n
which by (1.9) converges to a ﬁnite limit, as required. For ℓ ≥ 2, the
corresponding cumulant
κχn
ℓ (. . . , γ, . . .) = 0
vanishes because it involves a deterministc random variabl e γ. It follows
immediately that the limit (2.8) exists.
In this way we veriﬁed that the assumptions of Lemma 3.4 are fu lﬁlled.
Condition (C) follows immediately.
3.3.3. Proof of the equivalence (C) ⇐ ⇒(D).. The proof will follow closely
the ideas from [ ´Sni06, Section 4.7] with the roles of the cumulants κχn and
κχn
• interchanged. The original proof was based on the observati on that the
conditional cumulants (denoted in the original work [ ´Sni06] by the symbol
kid = κP(1)
•
P(1)) related to the map (3.3) fulﬁll the degree bounds (3.1) give n
by the approximate factorization property. By changing the meaning of the
symbol kid and setting kid := κP
P• = κ• to be the conditional cumulants
related to the map (3.2) and by applying Theorem 3.2 we still h ave in our
more general context that the cumulants kid fulﬁll the degree bounds (3.1).
The reasoning from [ ´Sni06, Section 4.7] is still valid in our context.
JACK-DEFORMED RANDOM YOUNG DIAGRAMS 23
