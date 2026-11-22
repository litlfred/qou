---
doc_id: ant-v14-n7-s-p10
doc_title: "Abelian extensions in dynamical Galois theory"
section_id: sec-000-1-introduction
section_title: "Introduction"
section_number: 1
pages: 1-4
source_pdf: ant-v14-n7-s-p10.pdf
source_sha256: 8d3e47aa779ad9c7
toc_source: inferred
doc_brief: "Abelian extensions in dynamical Galois theory — 11 sections: Front matter; Introduction; Some algebraic lemmas"
---
Let K be a number ﬁeld with algebraic closure K. Let φ(x) ∈K[x] be a polynomial of degree d ≥2, and
denote by φn = φ ◦· · · ◦φ the n-fold composition of φ with itself. Let α ∈K be a nonexceptional point
for φ; that is, assume that the backward orbit {β ∈K | φn(β) = α for some n ≥0} of α is an inﬁnite set.
For each n ≥1, deﬁne the n-th inverse image set of the pair (φ, α) by
φ−n(α) = {β ∈K | φn(β) = α},
and let Kn = Kn(φ, α) be the ﬁeld generated over K by φ−n(α). Since the generators of Kn are φ-images
of generators of Kn+1, we obtain a tower K = K0 ⊆K1 ⊆K2 ⊆· · · of Galois extensions of K. Set
K∞= S
n≥0 Kn.
As described for example in [Jones 2013], Gal(Kn/K) acts faithfully on the n-th preimage tree
Tn = Tn(φ, α) associated to the pair (φ, α), which can be described as follows. For each 0 ≤m ≤n, the
level-m vertices of Tn are indexed by the elements of φ−m(α), and edge relations on Tn are determined
by φ-evaluation. In the limit as n →+∞, Gal(K∞/K) acts faithfully on T∞= S Tn, and we obtain the
arboreal Galois representations
ρn : Gal(Kn/K) ,→Aut(Tn)
ρ : Gal(K∞/K) ,→Aut(T∞).
(1)
The study of the representations (1) goes back to Odoni [1985a; 1985b; 1988; 1997] and Stoll [1992],
and has found renewed interest due to a series of papers by Boston [2000], Boston and Jones [2007; 2009]
and Jones [2005; 2007; 2008; 2013]. Much of the current research in this area focuses on identifying
MSC2010: primary 11R32; secondary 11G50, 11R18, 37P30.
Keywords: arithmetic dynamics, dynamical Galois theory, arboreal representations, Weil height, small points, Arakelov–Zhang
pairing.
1982
Jesse Andrews and Clayton Petsche
cases in which Gal(K∞/K) is large in the sense that the arboreal Galois representation ρ is surjective, or
has image with ﬁnite index in Aut(T∞).
Assume for now that the pair (φ, α) is stable, that is that the Gal(Kn/K)-action on φ−n(α) is transitive
for each n ≥1; this is equivalent to the irreducibility of φn(x) −α for all n ≥1. In this case, each Tn is
the complete d-ary rooted tree of level n, so using transitivity and comparing with the size of Aut(Tn), it
follows from the injectivity of (1) that
dn ≤|Gal(Kn/K)| ≤d!(dn−1)/(d−1)
(2)
for all n. Examples in which the upper bound in (2) is achieved for all n ≥1 have been identiﬁed by
Odoni [1985b] and Stoll [1992] in degree d = 2, by Looper [2019] in every prime degree, and by Specter
[2018] in arbitrary degree.
In the opposite direction, let us say that a pair (φ, α) is minimally stable if it is stable, and the lower
bound in (2) is achieved for all n ≥1. For example, let K = Q, φ(x) = x2, and α = −1. This pair (φ, α)
is stable, indeed φn(x) −α = x2n + 1 is the 2n+1-th cyclotomic polynomial and hence is irreducible
over Q, and |Gal(Kn/Q)| = [Kn : Q] = 2n. Since K∞/Q is cyclotomic, Gal(K∞/Q) is abelian. (In fact
Gal(K∞/Q) ≃Z×
2 ≃{±} × Z2.)
More generally, an elementary argument shows that if the pair (φ, α) is stable and Gal(K∞/K) is
abelian, then (φ, α) is minimally stable; see Lemma 2. We do not know whether the converse is true;
i.e., whether the only minimally stable pairs (φ, α) are those for which Gal(K∞/K) is abelian. We do
not directly address this question here. Instead, in this paper we consider the following question: for
precisely which pairs (φ, α) is Gal(K∞/K) abelian? In the stable case, this is closely related to the
question of characterizing minimally stable pairs (φ, α), but the question makes sense even in the absence
of a stability hypothesis. We conjecture that in general, Gal(K∞/K) is abelian only in cases related to
the powering map example described above, or to similar examples arising from Chebyshev polynomials.
Given a ﬁeld extension L/K, we say the pair (φ, α) is conjugate over L to the pair (ψ, β) if there
exists an afﬁne transformation γ (x) = ax + b deﬁned over L such that ψ = γ ◦φ ◦γ −1 and β = γ (α).
It is not hard to see that if (φ, α) and (ψ, β) are conjugate over K, then K∞(φ, α) = K∞(ψ, β). But
for us, the more important fact is that whether or not Gal(K∞(φ, α)/K) is abelian is an invariant of
the K ab-conjugacy class of the pair (φ, α), where K ab is the maximal abelian extension of K in K; see
Proposition 11.
Conjecture. Let K be a number ﬁeld, let φ(x) ∈K[x] be a polynomial of degree d ≥2, let α ∈K, and
assume that α is not an exceptional point for φ. Then K∞(φ, α)/K is an abelian extension if and only
if the pair (φ, α) is K ab-conjugate to the pair (ψ, β) occurring in one of the following two families of
examples:
(i) ψ(x) = xd and β = ζ, a root of unity in K.
(ii) ψ(x) = Td(x) is the d-th Chebyshev polynomial and β = ζ + ζ −1, where ζ is a root of unity in K.
Abelian extensions in dynamical Galois theory
1983
As a special case, when K = Q and d =2, we recall the well-known fact that every quadratic polynomial
over Q is Q-conjugate to x2 + c for a unique c ∈Q, and moreover any such Q-conjugacy is actually
deﬁned over Q. Thus the Conjecture asserts in this case that for a pair (φ, α) deﬁned over Q with
deg(φ) = 2, the extension K∞(φ, α)/Q is abelian if and only if (φ, α) is Q-conjugate to (x2, ±1) or
(x2 −2, β) for β = 0, ±1, ±2.
We prove partial results toward the Conjecture which can be divided into three main categories. First,
we prove the Conjecture in the quadratic, stable, postcritically inﬁnite case (Theorem 8). (Recall that a
quadratic polynomial φ(x) is said to be postcritically ﬁnite if its critical point is φ-preperiodic; otherwise
it is postcritically inﬁnite.) The main ideas in this proof are algebraic, and culminate in showing under the
above hypotheses that if K∞/K were abelian, then no primes of K with odd residue characteristic would
ramify in K∞, in contradiction with a result of Bridy et al. [2017] on arbitrary postcritically inﬁnite maps.
Next, we prove the Conjecture for polynomials φ which are K-conjugate to either a powering map or
a Chebyshev map (Theorems 12 and 13). These proofs use the theory of heights together with a result of
Amoroso and Zannier [2000] (generalizing a result of Amoroso and Dvornicich [2000]), giving a lower
bound on the heights of elements in abelian extensions of number ﬁelds. Notably, the results on powering
and Chebyshev maps do not require a stability hypothesis.
Finally, we treat the particular postcritically ﬁnite map φ(x) = x2 −1. Using a combination of the
ramiﬁcation techniques of Theorem 8 with the height techniques of Theorems 12 and 13 (and in particular
a lower bound on the height in certain cyclotomic extensions due to Amoroso and Dvornicich [2000]),
we prove the Conjecture for stable pairs (x2 −1, α) over Q. We point out that the proof of this result is
computer-assisted, in the sense that the key step in the proof is to numerically calculate the Arakelov–
Zhang pairing ⟨x2 −1, x2⟩with enough precision to show that it is less than the Bogomolov constant
of the maximal abelian extension of Q unramiﬁed at all odd primes. In particular, we use SageMath to
calculate a sum of elementary approximations to local height functions evaluated at roots of unity.
Combining these results, and using the well known fact that every quadratic polynomial over Q is
either postcritically inﬁnite or else Q-conjugate to either the squaring map x2, the Chebyshev map x2 −2,
or x2 −1, we obtain the following.
Theorem 1. The Conjecture is true for all quadratic stable pairs (φ, α) over Q.
It is well-known that any iterate of an Eisenstein polynomial in Z[x] is again Eisenstein, so the pair
(φ(x), 0) is stable whenever φ(x) ∈Z[x] is Eisenstein. Using this observation, we can give the following
simple examples to show that in each of the cases described above, stable pairs (x2 + c, α) exist over Q
and hence Theorem 1 is nonvacuous in each case:
(i) For any prime p, the (postcritically inﬁnite) pair (x2 + p, 0) is stable.
(ii) If α ∈Z and α ≡2 or 3 (mod 4), then the squaring pair (x2, α) is stable, since it is conjugate to
(x2 + 2αx + α2 −α, 0), which is 2-Eisenstein. Note that this family includes both abelian examples,
such as (x2, −1), and nonabelian examples, such as (x2, 3).
1984
Jesse Andrews and Clayton Petsche
(iii) If α ∈Z and α ≡0 or 1 (mod 4), then the Chebyshev pair (x2 −2, α) is stable, since it is conjugate
to (x2 + 2αx + α2 −α −2, 0), which is 2-Eisenstein. Note that this family includes both abelian
examples, such as (x2 −2, 0), and nonabelian examples, such as (x2 −2, 4).
(iv) This example was shown to us by Chifan Leung. If α ∈Z and α ≡1 or 2 (mod 4), then the
pair (x2 −1, α) is stable. It sufﬁces to show that (φ2, α) is stable, where φ(x) = x2 −1 and
φ2(x) = x4 −2x2, since the irreducibility of φ2n(x) −α implies the irreducibility of φ2n−1(x) −α.
The stability of (φ2, α) follows from the fact that it is conjugate to (φ2(x + α) −α, 0), which is
easily checked to be 2-Eisenstein. (See also [Ahmad et al. 2019] for a study of large-image results
for arboreal Galois representations associated to φ(x) = x2 −1.)
While this paper was under review, A. Ferraguti and C. Pagano [2020] informed us that they have used
an entirely different approach to give a complete proof of the K = Q, d = 2 case of the Conjecture (not
requiring any stability assumption).
The plan of this paper is as follows. In Section 2 we prove some preliminary algebraic lemmas, and in
Section 3 we prove the Conjecture in the quadratic, stable, postcritically inﬁnite case. In Section 4 we
review the absolute Weil height function deﬁned on algebraic extensions of Q, we recall the concept of
the Bogomolov constant associated to such ﬁelds, and we describe related results of Amoroso and Zannier
[2000] and Amoroso and Dvornicich [2000]. In Section 5 we prove the Conjecture for powering maps and
Chebyshev maps. In Section 6 we review the deﬁnition and basic facts about the Arakelov–Zhang pairing,
and in Sections 7 and 8 we treat the particular polynomial φ(x) = x2 −1, calculate the Arakelov–Zhang
pairing ⟨x2 −1, x2⟩, and prove the Conjecture for stable pairs (x2 −1, α) over Q.
