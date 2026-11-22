---
doc_id: arxiv-math-0006111v2
doc_title: "Approximate factorization and concentration for characters of symmetric groups"
section_id: page-003
section_title: "Page 3"
section_number: null
pages: 3-3
source_pdf: 0006111v2.pdf
source_sha256: cd99f45d686eb6e2
toc_source: undetermined
doc_brief: "Approximate factorization and concentration for characters of symmetric groups — We prove a factorization-concentration result for characters of symmet- ric groups."
---
APPROXIMATE FACTORIZATION AND CONCENTRATION
3
continuous diagram. We shall denote them by
mn(ω) =
Z
R
xn mω(dx)
The measure corresponding to a diagram in CY has bounded support, it is centered
(i.e. m1 = 0), and its second moment is equal to half the area of the set
{(u, v) ∈R2| |u| ≤v ≤ω(u)}
Besides moments of measures we shall also consider their free cumulants. Recall
([B], [VDN]), that the free cumulants are deﬁned as the coeﬃcients Rn in the
expansion
K(z) = 1
z +
∞
X
n=1
Rnzn−1
where K(z) is the functional inverse of the Cauchy transform
G(z) =
Z
R
z −xmω(dx)
1.2 Positive deﬁnite functions. Let ψ be a normalized (i.e. ψ(e) = 1), central
positive deﬁnite function on Sq. By Fourier analysis on Sq, one can expand ψ as a
convex linear combination of normalized characters
ψ =
X
λ∈Yq
pλχλ
The weights pλ are non negative and sum to one, therefore they deﬁne a probability
measure Πψ on Yq, which puts a mass pλ on λ. Let V ⊂Yq and γ > 0, we say that
ψ is γ-supported on V if Πψ(V) > 1 −γ.
Let us deﬁne a probability measure on R associated with ψ by
mψ =
X
λ∈Yq
pλmλ
and denote its moments by
mn(ψ) =
X
λ∈Yq
pλmn(λ)
To this probability measure we can associate a diagram, by the correspondence
(1.1), which we call ωψ. By the GNS construction, there exists a ﬁnite dimensional
complex Hilbert space V , a unitary representation rψ : Sq →B(V ) (where B(V ) is
the space of bounded operators on V ), and a state τψ on B(V ), tracial on rψ(Sq)′′
such that
ψ(ρ) = τψ(rψ(ρ))
for all ρ ∈Sq. As in [B] for a unitary representation r of Sq in some B(H), we
deﬁne the selfadjoint element
Γ(r) =






1
1
. . .
1
1
1
r(1 2)
r(1 3)
. . .
r(1 q −1)
r(1 q)
1
r(1 2)
0
r(2 3)
. . .
r(2 q −1)
r(2 q)
...
...
...
...
...
...
...
1
(
0






