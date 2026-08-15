---
doc_id: arxiv-1402.4615v3
doc_title: "GAUSSIAN FLUCTUATIONS OF YOUNG DIAGRAMS AND STRUCTURE CONSTANTS OF JACK CHARACTERS"
section_id: sec-012-32-how-to-compute-jack-character-polynomials
section_title: "How to compute Jack character polynomials?"
section_number: 3.2
pages: 19-22
source_pdf: 1402.4615v3.pdf
source_sha256: b6e7c795cd1a7cd2
doc_brief: "GAUSSIAN FLUCTUATIONS OF YOUNG DIAGRAMS AND STRUCTURE CONSTANTS OF JACK CHARACTERS — In this paper, we consider a deformation of Plancherel meas ure linked to Jack polynomials."
---
given above to prove the existence of Lµ and Kµ is not effective. M. Lassalle
[Las09] gave an algorithm for computing Kµ by induction over µ. In this section
20 M. DOŁ ˛ EGA AND V . FÉRAY
we present a slightly simpler version of this algorithm which allows to compute Lµ
instead of Kµ.
One of the base ingredients is the following formula, which c orresponds to
[Las09, Proposition 8.3].
Proposition 3.1. Let k ≥ 2, λ be a Young diagram and i = (x, y) an inner corner
of λ.
Mk(λ(i)) − Mk(λ) =
∑
r≥1,s,t≥0,
2r+s+t≤k
zk−2r−s−t
i
( k − t − 1
2r + s − 1
)( r + s − 1
s
)
(−γ)s Mt(λ),
where zi = √
αx − √α−1y is the content of the corner corresponding to i in the
α-anisotropic diagram Aα(λ).
Proof. As mentioned above, this is exactly [Las09, Proposition 8.3 ]. To help the
reader, we compare our notations to Lassalle’s ones (we use boldface to refer to his
notations):
Mk(λ(i)) = αk/2Mk(λ (i));
Mt(λ) = αt/2Mt(λ );
zi = √α · xi;
γ = √α−1 − √α. □
For any partition ρ we deﬁne Mρ(λ) := ∏
i Mρi(λ) by multiplicativity. The
above proposition implies immediately the following corollary:
Corollary 3.2. For any partition ρ, any diagram λ and any inner corner i of λ,
Mρ(λ(i)) = Mρ(λ) +
∑
g,h≥0,
π⊢h
bρ
g,π (γ) zg
i Mπ(λ),
where bρ
g,π (γ) is a polynomial in γ.
Proof. The case when ρ consists of only one part is a direct consequence of Propo-
sition 3.1 (one even has an explicit expression forbρ
g,π (γ) in this case). The general
case follows by multiplication. □
This corollary is an analogue of Equation (8.1) in [Las09].
Let µ be a partition. By deﬁnition of Lµ, there exist some numbers aµ
ρ (depend-
ing on α) such that, for any Young diagram λ,
Chµ(λ) =
∑
ρ
aµ
ρ Mρ(λ).
LARGE DIAGRAMS AND STRUCTURE CONSTANTS 21
Using Corollary 3.2 we can compute
(11) Chµ(λ(i)) =
∑
ρ
aµ
ρ Mρ(λ(i))
= Ch µ(λ) +
∑
ρ
aµ
ρ



∑
g,h≥0,
π⊢h
bρ
g,π (γ) zg
i Mπ(λ)


 .
The second ingredient of Lassalle’s algorithm is a linear id entity between the
values of Jack character evaluated on different diagrams. W e denote by ci(λ) the
probability of the corner i in the transition measure µAα(λ), so that
(12) Mk(λ) =
∑
i
ci(λ)zk
i .
In particular,
∑
i
ci(λ) = 1 ,(13)
∑
i
ci(λ)zi = 0.(14)
Then we have [Las09, Equation (3.6)] the following proposition.
Proposition 3.3. For any (continuous) Young diagramλ and any partition µ
∑
i∈Iλ
ci(λ) Chµ(λ(i)) = m1(µ) Chµ\1(λ) + Chµ(λ),
∑
i∈Iλ
ci(λ)zi Chµ(λ(i)) =
∑
r≥2
rmr(µ) Chµ↓r (λ).
Proof. It is an exercise to adapt Equations (3.6) of [Las09] to our notations. □
Using Equations (11), (12), (13) and (14) together with Prop osition 3.3, we
obtain the following equalities between functions on the set of (continuous) Young
diagrams: for any partition µ,
∑
ρ
aµ
ρ



∑
g,h≥0,
π⊢h
bρ
g,π (γ) Mπ Mg


 = m1(µ) Chµ\1,(A)
∑
ρ
aµ
ρ



∑
g,h≥0,
π⊢h
bρ
g,π (γ) Mπ Mg+1


 =
∑
r≥2
r · mr(µ) Chµ↓r .(B)
Fix some partition τ. We can identify the coefﬁcient of a given monomial Mτ in
the above equations. This gives us two linear equations whic h will be denoted by
22 M. DOŁ ˛ EGA AND V . FÉRAY
(Aτ ) and (Bτ ):
∑
ρ
aµ
ρ




∑
g,h≥0, π ⊢h
π∪(g)=τ
bρ
g,π (γ)



 = m1(µ) aµ\1
τ ,(Aτ )
∑
ρ
aµ
ρ




∑
g,h≥0, π ⊢h
π∪(g+1)=τ
bρ
g,π (γ)



 =
∑
r≥2
r · mr(µ) aµ↓r
τ .(Bτ )
Now, assume that, for some partition µ, we can compute Lν for all partitions ν
of size smaller than |µ|. Then the equations ( Aτ ) and (Bτ ) can be interpreted as a
linear system, where the variables are the coefﬁcients aµ
ρ.
This is a ﬁnite system of linear equations (indeed, aµ
ρ = 0 as soon as |ρ| ≥
|µ| + ℓ(µ) [Las09, Proposition 9.2 (ii)]). As explained by M. Lassalle , the system
obtained that way has a unique solution (we shall see another explanation of that
in the next paragraph) and thus, one can compute the coefﬁcie nts aµ
ρ by induction
over |µ|.
