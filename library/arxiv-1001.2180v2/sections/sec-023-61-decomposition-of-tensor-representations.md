---
doc_id: arxiv-1001.2180v2
doc_title: "ASYMPTOTICS OF q-PLANCHEREL MEASURES"
section_id: sec-023-61-decomposition-of-tensor-representations
section_title: "Decomposition of tensor representations"
section_number: 6.1
pages: 23-24
source_pdf: 1001.2180v2.pdf
source_sha256: f4225d7b024940aa
doc_brief: "ASYMPTOTICS OF q-PLANCHEREL MEASURES — In this paper, we are interested in the asymptotic size of the rows and columns of a random Young diagram under a natural deformation of the Plancherel measure"
---
metric group: Sn acts on the space (
/BV
N )⊗n by commuting the vectors of the pure tensors. Its character i s
very easy to compute: χ(ρ) = N ℓ(ρ), where ℓ(ρ) is the number of parts of the partition ρ (or, equivalently,
the number of cycles of any permutation of type ρ).
This representation can be decomposed into irreducible rep resentations of Sn: let us denote mλ the
multiplicity of the irreducible module Sλ. We associate to this decomposition the following measure o n
partitions
/C8 [λ] = mλ · dim(Sλ)
N n .
In other words, /C8 [λ] is the dimension of the isotypic component of type λ divided by the total dimension
of the module (/BV
N )⊗n. Note that this is a very natural way to construct a measure on Young diagrams of
a given size: the same construction with the regular represe ntation gives rise to the Plancherel measure.
What is interesting with this kind of measure is that the expe ctation of rescaled character values is
proportional to the character of the representation. In the case we are looking at (the action of Sn on
(/BV
N )⊗n),
/BX [Σ ρ] = n↓|ρ| · χ(ρ1n−|ρ|)
N n
= n↓|ρ| · N ℓ(ρ)−|ρ|.
Let us ﬁnish this paragraph with a little remark. By Schur-We yl duality, one has the following isomor-
phism of Sn × GL(N, /BV )-modules
(/BV
N )⊗n ≃
⨁
λ⊢n,ℓ(λ)≤N
Vλ ⊗ Uλ,
where Uλ is an irreducible GL(N, /BV )-module. Moreover, the dimension of Uλ is the number of semi-
standard tableaux of shape λ with entries lower or equal than N . So,
/C8 [λ] =
⏐
⏐
⏐
⏐
{
standard tableaux
of shape λ
} ⏐
⏐
⏐
⏐·
⏐
⏐
⏐
⏐
{
semistandard tableaux
of shape λ (entries ≤ N )
} ⏐
⏐
⏐
⏐
N n .
This implies, as mentioned in paragraph 1.2.3, that this measure is in fact the image of the uniform
distribution on words of length n and letters from 1 to N by the RSK algorithm. On the other hand,
notice that the Schur-Weyl measure charges only the Young di agrams whose lengths are smaller than N .
24 V ALENTIN FÉRAY AND PIERRE-LOÏC MÉLIOT
