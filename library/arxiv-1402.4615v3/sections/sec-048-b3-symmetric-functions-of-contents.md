---
doc_id: arxiv-1402.4615v3
doc_title: "GAUSSIAN FLUCTUATIONS OF YOUNG DIAGRAMS AND STRUCTURE CONSTANTS OF JACK CHARACTERS"
section_id: sec-048-b3-symmetric-functions-of-contents
section_title: "B.3. Symmetric functions of contents"
section_number: null
pages: 65-68
source_pdf: 1402.4615v3.pdf
source_sha256: b6e7c795cd1a7cd2
toc_source: outline
doc_brief: "GAUSSIAN FLUCTUATIONS OF YOUNG DIAGRAMS AND STRUCTURE CONSTANTS OF JACK CHARACTERS — In this paper, we consider a deformation of Plancherel measure linked to Jack polynomials."
---
lated problem considered by Matsumoto in [Mat10, Section 8] in connection with
matrix integrals. Our results allow us to prove two conjectures stated in his paper.
For a box □= (i, j) of a Young diagram λ (i is the row-index, j is the column
index and j ≤λi), we deﬁne its (α-)content as c(□) = √α(j −1)−√α−1(i−1).
The alphabet of the contents of λ is the multiset Cλ = {c(□) : □∈λ}.
Matsumoto [Mat10, Equation (8.9)] (beware that in his paper the normalization
is different than ours) showed the following remarkable result: for any partition λ
(63)
ek(Cλ) =
X
µ:
|µ|−ℓ(µ)=k,
m1(µ)=0
Chµ(λ)
zµ
.
In particular, λ 7→ek(Cλ) is a shifted symmetric function. Therefore, for any
symmetric function F, the map λ 7→F(Cλ) is also a shifted symmetric function
66
M. DOŁ ˛EGA AND V. FÉRAY
and one may wonder how it can be expressed in the Ch basis. Explicitly, we are
interested in the coefﬁcients aµ(F) deﬁned by:
(64)
F(Cλ) =
X
µ partition
aµ(F) Chµ(λ).
Using the results of Section 4.1, one has the following result:
Proposition B.3. Let F be a symmetric function of degree d and let µ be a parti-
tion. The coefﬁcient aµ(F) is a polynomial in γ of degree at most
d −(|µ| −ℓ(µ) + m1(µ)).
Proof. From (63), the proposition is true for F = ek for any k ≥1. Besides, if
it is true for two symmetric functions F1 and F2, it is clearly true for any linear
combination of them. Using Theorem 1.4, it is also true for F1 · F2. Since the
elementary symmetric functions form a basis of symmetric functions, it follows
that the proposition is true for any symmetric function F.
□
From now on, we use the convention that the boldface quantities refer to the
notation of Matsumoto. The coefﬁcients aµ(F) are closely related to the quantities
A(α)
µ (F, n) introduced by S. Matsumoto [Mat10]. Namely, one has the following
lemma (which extends [Mat10, Lemma 8.5]):
Lemma B.4. Let µ be a partition. For n ≥|µ|+ℓ(µ), let π := µ+(1n−|µ|) be the
partition obtained from µ by adding 1 to every part and adding new parts equal to
1. Then, for any homogeneous symmetric function F of degree d, one has:
A(α)
µ (F, n) = α
d−(|π|−ℓ(π))
2

X
i≤m1(π)
a˜π1i(F) z˜π i!
n −|˜π|
i

,
where A(α)
µ (F, n) is the quantity deﬁned in [Mat10, Section 8.3].
Proof. If we ﬁx the integer n, one may rewrite Equation (64) using the deﬁnition
of Ch:
F(Cλ) =
X
ν,
|ν|≤n
aν(F)α
|ν|−ℓ(ν)
2
zν
n −|ν| + m1(ν)
m1(ν)

θν1n−|ν|(λ)
=
X
π⊢n
θπ(λ)

α
|π|−ℓ(π)
2
X
i≤m1(π)
a˜π1i(F)z˜πi!
n −|˜π|
i

.
The notations are the same as in Section 4.2. The second equality comes from
the fact that each partition ν of size at most n writes uniquely as ˜π1i where π is
a partition of n and i a non-negative integer smaller or equal to m1(π). Let Aπ
denotes the expression in the bracket in the equation above.
LARGE DIAGRAMS AND STRUCTURE CONSTANTS
67
As in the proof of Proposition B.1 we shall use the Jack deformation of Hall
scalar product on the space of symmetric functions.
X
λ⊢n
F(Cλ)
Jλ
⟨Jλ, Jλ⟩=
X
λ,π⊢n
Aπθπ(λ)
Jλ
⟨Jλ, Jλ⟩=
X
π⊢n
Aπ
pπ
⟨pπ, pπ⟩.
The last equality corresponds to (61). We deduce that
Aπ =
*X
λ⊢n
F(Cλ)
Jλ
⟨Jλ, Jλ⟩, pπ
+
=
X
λ⊢n
F(Cλ)θπ(λ) · ⟨pπ, pπ⟩
⟨Jλ, Jλ⟩
.
This formula coincides with the deﬁnition of A(α)
µ (F, n) in [Mat10, paragraph
8.3] up to a scalar multiplication, namely,
A(α)
µ (F, n) = αd/2Aπ.
The only difﬁculty is the difference of notations. To help the reader, we provide
the following dictionary. First recall that ⟨pπ, pπ⟩= zπ αℓ(π). Then our partition
π corresponds to µ + (1n−|µ|). In particular, one has |µ| = |π| −ℓ(π) and
zµ+(1n−|µ|) = zπ. Besides, F(Cλ) in our paper corresponds to αd/2 F (Aα
λ) in
[Mat10]. Finally, the probability P(α)
n (λ) is simply given by
n!αn
⟨Jλ,Jλ⟩.
□
Proposition B.3, when translated into Matsumoto’s notation by Lemma B.4, has
several interesting consequences. As above, we consider an homogeneous sym-
metric function F of degree d.
• If d = |µ|, the only term of the sum which can be non-zero corresponds to
i = 0 (by Proposition B.3). Moreover, it does not depend on α. Besides,
the exponent of α in the formula is equal to zero. Finally, A(α)
µ (F, n)
does not depend neither on α nor on n, which proves [Mat10, Conjecture
9.2].
• If d = |µ| + 1, there are only two terms (corresponding to i = 0, 1) which
can be non-zero in the sum. Besides, the coefﬁcient a˜π1 does not depend
on α because of Proposition B.3. But it is easy to prove that it is equal
to 0 in the case α = 1 (it comes from the combinatorial interpretation of
A(1)
µ (F, n), see [Mat10, Example 9.2]). Hence, a˜π1 = 0 and only the
term corresponding to i = 0 is non-zero. In particular, one can see that
A(α)
µ (F, n) does not depend on n, which proves [Mat10, Conjecture 9.3].
• In the general case, non-zero terms of the sum are indexed by values of i
smaller or equal to d −|µ| (by Proposition B.3). Hence A(α)
µ (F, n) is a
polynomial in n of degree at most d−|µ|. This result is not stronger that the
bound of Matsumoto on the degree of A(α)
µ (F, n) [Mat10, Theorem 8.8].
Nevertheless, it is better in some cases and we also have some control on
the dependence on α (as illustrated by the proofs of the conjectures above).
68
M. DOŁ ˛EGA AND V. FÉRAY
