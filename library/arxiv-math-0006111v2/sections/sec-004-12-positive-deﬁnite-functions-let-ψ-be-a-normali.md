---
doc_id: arxiv-math-0006111v2
doc_title: "Approximate factorization and concentration for characters of symmetric groups"
section_id: sec-004-12-positive-deﬁnite-functions-let-ψ-be-a-normali
section_title: "Positive deﬁnite functions. Let ψ be a normalized (i.e. ψ (e) = 1), central"
section_number: 1.2
pages: 3-4
source_pdf: 0006111v2.pdf
source_sha256: cd99f45d686eb6e2
doc_brief: "Approximate factorization and concentration for characters of symmetric groups — We prove a factorization-concentration result for characters of s ymmet- ric groups."
---
positive deﬁnite function on Sq. By Fourier analysis on Sq, one can expand ψ as a
convex linear combination of normalized characters
ψ =
∑
λ ∈Yq
pλχλ
The weightspλ are non negative and sum to one, therefore they deﬁne a probab ility
measure Π ψ on Yq, which puts a mass pλ onλ. Let V ⊂ Yq andγ >0, we say that
ψ is γ-supported on V if Π ψ (V)> 1 −γ.
Let us deﬁne a probability measure on R associated with ψ by
mψ =
∑
λ ∈Yq
pλ mλ
and denote its moments by
mn(ψ ) =
∑
λ ∈Yq
pλmn(λ)
To this probability measure we can associate a diagram, by th e correspondence
(1.1), which we call ωψ . By the GNS construction, there exists a ﬁnite dimensional
complex Hilbert space V , a unitary representation rψ :Sq → B (V ) (where B(V ) is
the space of bounded operators on V ), and a state τψ on B(V ), tracial on rψ (Sq)′′
such that
ψ (ρ) = τψ (rψ (ρ))
for all ρ ∈ Sq. As in [B] for a unitary representation r of Sq in some B(H), we
deﬁne the selfadjoint element
Γ(r) =






0 1 1 1 ... 1 1
1 0 r(1 2) r(1 3) ... r (1q − 1) r(1q)
1 r(1 2) 0 r(2 3) ... r (2q − 1) r(2q)
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
1 r(1q) r(2q) r(3q) ... r (q − 1q) 0






