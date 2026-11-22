---
doc_id: arxiv-math-0108046v3
doc_title: "arXiv:math/0108046v3 [math.RT] 3 May 2002"
section_id: page-031
section_title: "Page 31"
section_number: null
pages: 31-31
source_pdf: 0108046v3.pdf
source_sha256: f47c1bd39c671cf3
toc_source: undetermined
doc_brief: "Presenting Schur algebras — Motivated by work of R.M. Green, we obtain a pre- sentation of Schur algebras (both the classical and quantized ver- sions) in terms of generators and relations."
---
PRESENTING SCHUR ALGEBRAS
31
We shall also need the relation
X(a)
γ X(b)
γ
=

a + b
a

X(a+b)
γ
(γ ∈Φ).
(8.6)
which follows immediately from the deﬁnitions.
Proposition 8.7. The sets Y+ and Y−span the algebra TA.
Proof. We just prove the statement for Y+. As in the classical case,
the algebra TA is spanned by the set of all “special” monomials of the
form
M = X(ψ1)
γ1
· · · X(ψm)
γm
1µ
(8.8)
for m ∈N, γ ∈Φm, ψ ∈Nm. By (8.6) we may assume that γi̸ = γi+1
for all i ≤m −1. Set χ = χR(M) and deﬁne the deviation of M by
δ = P
χi>µi(χi −µi). We claim that the set of all special monomials
of deviation 0 lie within the A-span of Y+.
However, the proof of
this claim is diﬀerent in the present case. By (8.5) we can express the
product X(ψ1)
γ1
· · ·X(ψm)
γm
(which lies in the subalgebra U(sln)) in terms
of an A-linear combination of terms of the form EAKδ,BFC. In this
expression, each of the terms has right content not exceeding that of
M, because commutation does not increase degree or right content. We
express each Kδ,B in terms of an A-linear combination of idempotents
1λ, and use Proposition 7.9 to commute the idempotents all the way
to the right. Upon right multiplication of the resulting expression by
1µ we obtain an equality of the form
M =
X
A,C
aA,C EAFC1µ
(aA,C ∈A)
in which the right content of each term on the right-hand-side is no
greater than that of M. It follows that each term in the right-hand-
side of the above equality has deviation 0, and thus lies in Y+. This
proves the claim.
Now we proceed by induction on deviation, with the above claim
forming the base step in the induction. Let M be a special monomial
of the form (8.8) of deviation δ = δ(M) > 0. Set χ = χR(M). Since
χ̸ ⪯µ, there is an index j for which χj > µj. Fixing this index j, we
call β ∈Φ bad if β = εi −εj for some i̸ = j and call β good otherwise.
We extend this terminology to the factors X(ψγ)
γ
of M. We deﬁne the
defect D of the monomial M by the equality D(M) = P ψα where
the sum is over the set {X(ψα)
α
} of good factors in M appearing to the
right of some bad factor. The defect of M is 0 if and only if all the bad
