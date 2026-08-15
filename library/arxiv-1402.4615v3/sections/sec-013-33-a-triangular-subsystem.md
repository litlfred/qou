---
doc_id: arxiv-1402.4615v3
doc_title: "GAUSSIAN FLUCTUATIONS OF YOUNG DIAGRAMS AND STRUCTURE CONSTANTS OF JACK CHARACTERS"
section_id: sec-013-33-a-triangular-subsystem
section_title: "A triangular subsystem"
section_number: 3.3
pages: 22-26
source_pdf: 1402.4615v3.pdf
source_sha256: b6e7c795cd1a7cd2
doc_brief: "GAUSSIAN FLUCTUATIONS OF YOUNG DIAGRAMS AND STRUCTURE CONSTANTS OF JACK CHARACTERS — In this paper, we consider a deformation of Plancherel meas ure linked to Jack polynomials."
---
mine the coefﬁcients aµ
ρ (where ρ runs over partitions without parts equal to 1) of
Lµ as the solution of an overdetermined linear system of equations. In this section,
we extract from this system a triangular subsystem.
We will need an order on all partitions: let us deﬁne <1 as follows:
ρ < 1 ρ′ ⇐ ⇒





|ρ| < |ρ′|;
or |ρ| = |ρ′| and ℓ(ρ) > ℓ(ρ′);
or |ρ| = |ρ′|, ℓ (ρ) = ℓ(ρ′) and min(ρ) > min(ρ′).
We say that an equation involves a variable if its coefﬁcientis non-zero.
Lemma 3.4. Let ρ be a partition and q = min(ρ) its smallest part.
• If q = 2, set τ = ρ \ (2). Then Equation (Aτ ) involves the variable aµ
ρ and
involves some of the variables aµ
ρ′ for ρ′ >1 ρ (and no other variables aµ
ρ′).
• If q > 2, set τ = ρ↓q. Then Equation (Bτ ) involves the variable aµ
ρ and
some of the variables aµ
ρ′ for ρ′ >1 ρ (and no other variables aµ
ρ′).
Proof. We can reﬁne Corollary 3.2 as follows: for any partition ρ, any diagram λ
and any inner corner i of λ,
(15) Mρ(λ(i)) = Mρ(λ) +
∑
j≤ℓ(ρ)
Mρ\ρj




∑
g,t≥0,
g=ρj −2−t
(ρj − t − 1)Mt(λ)zg
i




+
∑
π,g
|π|+g<|ρ|−2
bρ
g,π (γ)Mπ(λ)zg
i .
LARGE DIAGRAMS AND STRUCTURE CONSTANTS 23
Indeed, it is true for ρ = (k) and follows directly for any ρ by multiplication. The
right-hand side is a linear combination of Mπzg
i with
|π| + g ≤ |ρ| − 2.
Moreover equality occurs only if π ∪ (g) is obtained from ρ by choosing a part,
removing 2 to this part and splitting it in two (possibly empty) parts.
Let us consider the ﬁrst statement of the lemma. Fix a partition ρ with a smallest
part equal to 2, that is ρ = τ ∪ (2) for some partition τ. Let us determine which
variables aµ
ρ′ appear in the left-hand side of Equation(Aτ ). In other terms, we want
to determine for which ρ′, the difference Mρ′(λ(i)) − Mρ′(λ) contains some term
Mπzg
i , for which τ = π ∪ (g). As explained above, a necessary condition is the
inequality |τ | = |π| + g ≤ |ρ′| − 2, i.e. |ρ′| ≥ | τ | + 2. Moreover, if |ρ′| = |τ | + 2,
then τ must be obtained from ρ′ by removing 2 from some part and splitting it into
two. In particular, ρ′ cannot be longer than τ, unless both new parts are empty.
This happens only if the split part of ρ′ was 2, that is if ρ′ = τ ∪ (2). We have
proved that (Aτ ) can involve aµ
ρ′ only if ρ′ = ρ or ρ′ >1 ρ (either ρ′ has a bigger
size than ρ, or it has a smaller length). It is easy to check that the coefﬁ cient of aµ
ρ
is equal to m2(ρ) (and thus, non-zero), which ﬁnishes the proof of the ﬁrst point.
The proof of the second point is quite similar. Fix a partitio n ρ, denote q its
smallest part (assume q > 2) and τ = ρ↓q. The same argument than above tells us
that the variable aµ
ρ′ can appear in the equation (Bτ ) only if |τ | = |π| + g + 1 ≤
|ρ′| − 1, i.e. |ρ′| ≥ | τ | + 1. Moreover, if there is equality, τ must be obtained from
ρ′ by removing 1 from some part and splitting it into two. One of the two new parts
is always non-empty (as ρ′ has no parts equal to 1), thus ρ′ is at most as long as τ.
If they have the same length, it means that τ is obtained from ρ′ by shortening a
part. If this part is equal to q, then ρ′ = ρ. Otherwise ρ′ contains a part q − 1 and
thus ρ′ >1 ρ (they have same size and same length). Finally, we have prove d that
(Bτ ) can involve aµ
ρ′ only if ρ′ >1 ρ. Once again, the coefﬁcient of aµ
ρ in (Bτ ) is
easy to compute: it is equal to (q − 1)mq(ρ) and, hence, non-zero. □
The ﬁrst interesting consequence is the following.
Corollary 3.5. The coefﬁcient aµ
ρ is a polynomial in γ with rational coefﬁcients.
The same is true for the coefﬁcients of Kerov’s polynomialsKµ.
Proof. We proceed by induction over |µ|. The quantities aµ
ρ are the solution of a
triangular linear system, whose right-hand side is a vector of aµ′
τ with |µ′| < |µ|.
By induction hypothesis, the right-hand side belongs to Q[γ]. The coefﬁcients
bρ
g,π(γ) of the system also belong to Q[γ]. Moreover, the diagonal coefﬁcients of
the system (given in the proof above) are invertible in Q[γ], hence the solution is
also in Q[γ].
For the second statement, it is enough to say that eachMk is a polynomial in the
Rk’s with integer coefﬁcients. □
Remark. Lemma 3.4 does not hold for Lassalle’s system of equation [Las09, Equa-
tions (9.1) and (9.2)], which computes recursively Kµ.
24 M. DOŁ ˛ EGA AND V . FÉRAY
3.4. A ﬁrst bound on the degree. Recall that (Mk)k≥2 is an algebraic basis of
the ring Λ (α)
⋆ of α-polynomial functions on Young diagrams. Hence, we can deﬁne
a gradation on Λ (α)
⋆ by choosing arbitrarily the degree of each of the generators
Mk. In this section, we do the following natural choice:
deg1(Mk) = k for k ≥ 2.
Our goal is to obtain a bound on the degree of the polynomial aµ
ρ ∈ Q[γ]. We
begin by the following lemma concerning the polynomials bρ
g,π (γ).
Notational convention. To emphasize the difference with gradations on Λ (α)
⋆ ,
we denote throughout the paper degrees of polynomials in γ by degγ.
Lemma 3.6. Let ρ and π be two partitions and g ≥ 0 be an integer. One has
degγ(bρ
g,π (γ)) ≤ deg1(Mρ) − deg1(Mπ∪(g)) − 2.
Moreover, if the right-hand side is an even (odd, respectively) number, then bρ
g,π (γ)
is an even (odd, respectively) polynomial.
Proof. By Proposition 3.1, Mk(λ(i)) can be written as a linear combination of
terms of the form b(γ) Mπ zg
i , where b is some polynomial. We deﬁne the pre-
degree (with respect to deg1) of such a term to be the quantity degγ(b) + |π| + g.
This degree is multiplicative. Then,
Mk(λ(i)) = Mk(λ) + terms of degree smaller or equal to k − 2.
By multiplying this kind of expressions we obtain that
Mρ(λ(i)) = Mρ(λ) + terms of degree smaller or equal to |ρ| − 2,
which corresponds to our bound on the degree. The parity alsofollows immediately
from the one-part case by multiplication. □
This yields the following result.
Proposition 3.7. The coefﬁcient aµ
ρ of Mρ in Jack character polynomial Lµ is a
polynomial in γ of degree smaller or equal to|µ| + ℓ(µ) − |ρ|. Moreover, it has the
same parity as the integer |µ| + ℓ(µ) − |ρ|.
The same is true for Kµ.
Proof. We proceed by induction over (µ, ρ). The base case µ = (1) is trivial as
L(1) = M2. Fix two partitions µ and ρ. We assume that our result holds for any
pair (µ′, ρ′) with |µ′| < |µ| or |µ′| = |µ| and ρ′ >1 ρ.
It may seem strange to assume that the result holds for ρ′ >1 ρ. We are indeed
doing some kind of descending induction. This is possible because, for a given µ,
the number of partitions ρ we shall consider is ﬁnite: indeed, aµ
ρ = 0 as soon as
|ρ| ≥ | µ| + ℓ(µ) [Las09, Proposition 9.2 (ii)]. The same remark holds for mos t
proofs in this section.
LARGE DIAGRAMS AND STRUCTURE CONSTANTS 25
Let us ﬁrst consider the case when ρ = τ ∪ (2) contains a part equal to 2. By
Lemma 3.4, Equation (Aτ ) can be written as:
m2(ρ) · aµ
ρ = m1(µ)aµ\1
τ −
∑
π,g,
π∪(g)=τ
∑
ρ′>1ρ
bρ′
g,π (γ)aµ
ρ′.
The ﬁrst term on the right-hand-side is by convention equal t o 0 if µ does not
contain any part equal to 1. If µ contains a part equal to 1, as |µ \ 1| is smaller than
|µ|, by induction hypothesis aµ\1
τ is a polynomial of degree at most
|µ \ 1| + ℓ(µ \ 1) − |τ | = |µ| − 1 + ℓ(µ) − 1 − (|ρ| − 2) = |µ| + ℓ(µ) − |ρ|.
As ρ′ >1 ρ, we can also apply the induction hypothesis to each summand o f the
second term: aµ
ρ′ is polynomial of degree at most |µ| + ℓ(µ) − | ρ′|. But using
Lemma 3.6, bρ′
g,π (γ) has degree at most |ρ′| − |π ∪ (g)| − 2. Hence the degree of
the product is bounded by
|µ| + ℓ(µ) − (|π ∪ (g)| + 2) = |µ| + ℓ(µ) − |ρ|.
The last equality comes from the fact that π ∪ (g) = τ = ρ \ 2.
The proof of the case when the smallest part q of ρ is greater than 2 is similar.
We use Equation (Bτ ) for τ = ρ↓q, which takes the form:
(q − 1)mq(ρ) · aµ
ρ =
∑
r≥2
r · mr(µ)aµ↓r
τ −
∑
π,g,
π∪(g+1)=τ
∑
ρ′>1ρ
bρ′
g,π (γ)aµ
ρ′.
Note that |µ↓r| < |µ|, therefore by induction hypothesis aµ↓r
τ is a polynomial in γ
of degree at most
|µ↓r| + ℓ(µ↓r) − |τ | = |µ| − 1 + ℓ(µ) − (|ρ| − 1) = |µ| + ℓ(µ) − |ρ|.
For the second summand, the argument is the same as before, ex cept that here
the equality |π ∪ (g)| + 2 = |ρ| comes from the fact that |τ | = |ρ| − 1 and
|τ | = |π ∪ (g + 1)| = |π ∪ (g)| + 1.
The parity is obtained the same way. □
Corollary 3.8. For any partition µ one has:
deg1(Chµ) = |µ| + ℓ(µ).
Moreover
Chµ =
∏
i
Rµi+1 + lower degree terms with respect to deg1.
Proof. By Proposition 3.7, Chµ has at most degree |µ| + ℓ(µ) (this has also been
proved by Lassalle [Las09, Proposition 9.2 (ii)]) and its component of degree |µ| +
ℓ(µ) does not depend on α. Hence the result follows as this dominant term is
known in the case α = 1 (see for example [´Sni06, Theorem 4.9]). □
26 M. DOŁ ˛ EGA AND V . FÉRAY
