---
doc_id: arxiv-1002.4860v2
doc_title: "A STATE-SUM FORMULA FOR THE ALEXANDER POLYNOMIAL"
section_id: sec-006-3-construction
section_title: "Construction"
section_number: 3
pages: 5-7
source_pdf: 1002.4860v2.pdf
source_sha256: a2cfe924f7a9f5a0
---
Begin with a word w ∈ Σ •
n in the braid generators σ1,...,σ n−1 and their inverses,
which we picture as a diagram drawn up the page as the word is read fr om right to
left.
σr = · · · /d127/d127/d127/d127/d63/d63
/d63/d63
r r +1
· · · σ−1
r = · · · /d127/d127
/d127/d127/d63/d63/d63/d63
r r +1
· · ·
Construct permutation diagrams from the braid diagram by replacing each crossing
by one of two resolutions:
/d127/d127/d127/d127/d127/d127/d127/d127/d127
/d63/d63/d63/d63
/d63/d63/d63/d63
↦− → or
/d127/d127/d127/d127/d127/d127/d127/d127/d127
/d63/d63/d63/d63/d63/d63/d63/d63/d63
/d127/d127/d127/d127
/d127/d127/d127/d127
/d63/d63/d63/d63/d63/d63/d63/d63/d63 ↦− → or
/d127/d127/d127/d127/d127/d127/d127/d127/d127
/d63/d63/d63/d63/d63/d63/d63/d63/d63
A permutation diagram x is admissible if
P1: the ﬁrst (leftmost) strand goes straight through without cross ing any other
strands, and
P2: the underlying permutation is the identity.
A state is a pair ( x,ε ), where x is an admissible permutation diagram and ε is an
assignment of a sign ± to each strand such that
S1: the ﬁrst (leftmost) sign is +, and
S2: no two strands of the same sign cross.
Let S(w) denote the set of states for w. To a state ( x,ε ) ∈ S (w), we associate a
weight M(w, x,ε ) ∈ C(v) deﬁned by multiplying together certain scalars, one for
each resolved crossing. The scalar associated to a positive crossin g of strands in
positions r and r + 1 is given in (11). For a negative crossing, replace v by v−1 in
each expression.
(11)
/d127/d127/d127/d127/d127/d127/d127/d127/d127
/d63/d63/d63/d63
/d63/d63/d63/d63
r r+1
↦− →



v
+ +
−v−1
− −
vr
[r]
− +
−v−r
[r]
+ −
[r + 1]
[r]
−
/d127/d127/d127/d127/d127/d127/d127/d127/d127
+
/d63/d63/d63/d63/d63/d63/d63/d63/d63
[r − 1]
[r]
+
/d127/d127/d127/d127/d127/d127/d127/d127/d127
−
/d63/d63/d63/d63/d63/d63/d63/d63/d63
A STATE-SUM FORMULA FOR THE ALEXANDER POLYNOMIAL 6
Deﬁne A(w) ∈ C(v) by
(12) A(w) = 1
[n]
∑
(x,ε)∈S(w)
⟨ε⟩M(w, x,ε )
where ⟨ε⟩ ∈ {±1} is the product of the signs ε1,...,ε n attached to the strands.
Theorem 3.1. Let L be an oriented link, and let w ∈ Σ •
n represent a braid in Bn
whose closure is L. Then, A(w) is a polynomial in v −v−1, and
A(w) = ∆( L),
where ∆(L) is the Conway-normalized Alexander polynomial.
Proof. To avoid confusion when switching between the generators Hr andTr =vHr of
Hn, let us write ϕ :Bn ։ H×
n for the group homomorphism given by ϕ(σr) = Hr and
ψ :Bn ։ H×
n for the one with ψ(σr) = Tr. Formula (7.2) in [7] gives the Alexander
polynomial for a link L as
(13) ∆( L) = ( −1)n−1
( 1
q
) (e−n+1)/2 1 −q
1 −qn
n−1∑
k=0
(−1)kχn−1−k
(
ψ(w)
)
where χℓ = tr ◦ρℓ is the character of Hn arising from the irreducible representation
ρℓ : Hn → End(S(λℓ)) indexed by the hook partition ( n −ℓ, 1ℓ), and e is the exponent
sum of w. Put q =v2 and Tr =vHr for each r, so that ψ(w) = veϕ(w). Reindex the
sum over ℓ =n − 1 −k to get
∆(L) = ( −1)n−1
( 1
v
) e−n+1 1 −v2
1 −v2n
n−1∑
ℓ=0
(−1)n−1−ℓχℓ
(
veϕ(w)
)
= 1
[n]
n−1∑
ℓ=0
(−1)ℓχℓ
(
ϕ(w)
)
.(14)
Now we compute χℓ by using the semi-normal form for S(λℓ). The action of the
generators Hr, H −1
r on xε from Theorem 2.7 are pictured in (15).
(15)
/d127/d127/d127/d127/d127/d127/d127/d127/d127
/d63/d63/d63/d63
/d63/d63/d63/d63
r r+1
↦− → ar(ε)
εr
εr
εr+1
εr+1
+ br(ε)
/d127/d127/d127/d127/d127/d127/d127/d127/d127
/d63/d63/d63/d63/d63/d63/d63/d63/d63
εr
εr
εr+1
εr+1
/d127/d127/d127/d127
/d127/d127/d127/d127
/d63/d63/d63/d63/d63/d63/d63/d63/d63
r r+1
↦− → ¯ar(ε)
εr
εr
εr+1
εr+1
+ br(ε)
/d127/d127/d127/d127/d127/d127/d127/d127/d127
/d63/d63/d63/d63/d63/d63/d63/d63/d63
εr
εr
εr+1
εr+1
A STATE-SUM FORMULA FOR THE ALEXANDER POLYNOMIAL 7
Moreover, if r = 1, the second term on the right hand side should be omitted.
Only diagonal entries of the matrix ρℓ(ϕ(w)) contribute to the trace. Hence, for
eachℓ we need only consider those permutation diagrams that represent the identity
permutation and whose ﬁrst strand goes straight through. The t heorem follows on
comparing formulas (7) and (8) with (11). □
