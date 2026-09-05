---
doc_id: arxiv-1608.07308v1
doc_title: "FLAG HILBERT SCHEMES, COLORED PROJECTORS AND KHOV ANOV-ROZANSKY HOMOLOGY"
section_id: sec-018-31-the-hecke-algebra
section_title: "The Hecke algebra"
section_number: 3.1
pages: 19-20
source_pdf: 1608.07308v1.pdf
source_sha256: bcc3b6f1a91a55c6
doc_brief: "FLAG HILBERT SCHEMES, COLORED PROJECTORS AND KHOV ANOV-ROZANSKY HOMOLOGY — We construct a categoriﬁcation of the maximal commutative subalgebra of the type A Hecke algebra."
---
Hn = C(q)⟨σ1,...,σ n−1⟩
modulo relations:
(3.1)
(
σi−q
1
2
)(
σi +q− 1
2
)
= 0 ∀i∈{ 1,...,n − 1}
(3.2) σiσi+1σi =σi+1σiσi+1 ∀i∈{ 1,...,n − 2}
(3.3) σiσj =σjσi ∀|i−j|> 1.
The algebra Hn is a q-deformation of the group algebra of the symmetric group C[Sn]. The
irreducible representations Vλ ofHn at generic parameter q are labeled by partitions of n, or,
equivalently, by Young diagrams of size n. The multiplicity of Vλ in the regular representa-
tion is equal to its dimension, which is itself equal to the number of standard Young tableaux
(henceforth abbreviated SYT) of shape λ. Therefore, the regular representation of Hn splits
into a direct sum of irreducible representations labeled by standard tableaux. For each such
20 EUGENE GORSKY, ANDREI NEGUT , , AND JACOB RASMUSSEN
tableauT , let PT denote the projector onto the irreducible summand in Hn labeled by T . By
construction, these projectors have the following properties:
(3.4) PTPT′ =δT
T′PT,
∑
T
PT = 1.
The projectors PT can be written very explicitly in terms of the generators σi, see [4, 33] for
details. They satisfy the following branching rule:
(3.5) i(PT ) =
∑
□
PT +□,
wherei :Hn→Hn+1 is the natural inclusion and the summation in the right hand side is over
all possible SYT obtained fromT by adding a single box labeled byn + 1.
The renormalized Markov traceχ :Hn→ C(a,q ) satisﬁes the relations:
(3.6) χ(σσ′) =χ(σ′σ), χ (i(σ)) =χ(σ)· 1−a
q
1
2−q− 1
2
, χ (i(σ)σn) =χ(σ).
There is a natural pairing ⟨·,·⟩ : Hn×Hn→ C(a,q ) given by⟨σ,τ⟩ = χ(στ†), where σ†
is the “Hermitian conjugate” of σ (this is the C-antilinear map determined by the relations
q† = q−1, σ†
i = σ−1
i , and (στ )† = τ†σ†). With respect to this pairing, the adjoint of the
inclusioni :Hn→Hn+1 is the partial Markov trace:
Tr :Hn+1→Hn⊗ C[a].
It follows easily from the deﬁnitions that for allσ∈Hn, we haveχ(σ) = Trn(σ).
The Markov trace of a projectorPT only depends on the underlying Young diagramλ of the
SYTT , and is equal to theλ-colored HOMFLY-PT polynomial of the unknot. Speciﬁcally, we
have the following result:
Proposition 3.1. (e.g. [3]) The Markov trace ofPT equals:
Trn(PT ) =
∏
□∈λ
1−aqc(□)
1−qh(□) ,
wherec(□) andh(□) respectively denote the content and the hook length of a square□ inλ.
