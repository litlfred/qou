---
doc_id: arxiv-1402.4615v3
doc_title: "GAUSSIAN FLUCTUATIONS OF YOUNG DIAGRAMS AND STRUCTURE CONSTANTS OF JACK CHARACTERS"
section_id: sec-017-41-structure-constants-are-polynomials-in
section_title: "Structure constants are polynomials in"
section_number: 4.1
pages: 31-32
source_pdf: 1402.4615v3.pdf
source_sha256: b6e7c795cd1a7cd2
doc_brief: "GAUSSIAN FLUCTUATIONS OF YOUNG DIAGRAMS AND STRUCTURE CONSTANTS OF JACK CHARACTERS — In this paper, we consider a deformation of Plancherel meas ure linked to Jack polynomials."
---
to prove our main result for the structure constants of the al gebra Λ (α)
⋆ of α-
polynomial functions which was stated as Theorem 1.4.
Proof of Theorem 1.4: First observe that for each i ∈ {1, 2, 3} one has:
ni(µ) = deg i(Chµ),
hence our bound on the degree of structure constants can be eq uivalently formu-
lated using three gradations introduced in Section 3.
Let us consider the bound involvingdeg1 (the case of deg3 is similar). We know
by Proposition 3.7 that
Chµ =
∑
ρ
aµ
ρ Mρ,
where each aµ
ρ is a polynomial in γ of degree deg1(Chµ) − deg1(Mρ). Hence, we
have
Chµ · Chν =
∑
ρ
bµ,ν
ρ Mρ,
where each bµ,ν
ρ is a polynomial inγ of degree deg1(Chµ)+deg1(Chν)−deg1(Mρ).
In particular Chµ · Chν has degree at most deg1(Chµ) + deg 1(Chν) and hence,
thanks to the remark of Section 3.8, gµ,ν;π = 0 whenever
n1(µ) + n1(ν) < n 1(π).
The structure constants are obtained by solving the linear system:
(S)
∑
τ
aτ
ρgµ,ν;τ = bµ,ν
ρ .
In this system, µ and ν are ﬁxed, there is one equation for each partition ρ without
parts equal to 1. In each equation, the sum runs over partitionsτ such that n1(τ ) ≤
n1(µ) + n1(ν). Finally, the unknown are gµ,ν;τ , for τ as above.
We will prove our statement by induction over
deg1(Chµ) + deg1(Chν) − deg1(Chπ).
Fix some partitions µ,ν and π. If the quantity above is negative, the coefﬁcient
gµ,ν;π is equal to 0 and the statement is true. Otherwise we suppose that for all
partitions τ bigger than π (in the sense that deg1(Chτ ) > deg1(Chπ)), the degree
of gµ,ν;τ is bounded from above by deg1(Chµ) + deg1(Chν) − deg1(Chτ ).
Note that aτ
ρ vanishes as soon as deg1(Chτ ) < deg1(Mρ). Then from (S) we
extract a subsystem
(S′)
∑
τ,
deg1(Chτ )=deg1(Chπ)
aτ
ρgµ,ν;τ = bµ,ν
ρ −
∑
τ,
deg1(Chτ )>deg1(Chπ)
aτ
ρgµ,ν;τ ,
where ρ runs over partitions such that deg1(Mρ) = deg 1(Chπ). The variables
are gµ,ν;τ for τ with deg1(Chτ ) = deg 1(Chπ). This system is invertible (because
(Chπ) is a basis of Λ (α)
⋆ ) and the coefﬁcients on the left-hand side of ( S′) are
32 M. DOŁ ˛ EGA AND V . FÉRAY
rational numbers (by Proposition 3.7). Besides, all terms on the right-hand side are
polynomials in γ of degree at most deg1(Chµ) + deg1(Chν) − deg1(Chπ) which
ﬁnishes the proof.
The proof of the parity follows in the same way.
The bound involving deg2 is obtained in a slightly different way. First note that
if µ and ν do not have any parts equal to 1, this bound is weaker that the one with
deg3. Hence, it holds in this case. Then the general case follows, using the fact
that Chµ∪(1) = (|λ| − |µ|) Chµ. □
