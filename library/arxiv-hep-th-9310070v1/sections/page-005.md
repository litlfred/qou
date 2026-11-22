---
doc_id: arxiv-hep-th-9310070v1
doc_title: "Quantum dilogarithm"
section_id: page-005
section_title: "Page 5"
section_number: null
pages: 5-5
source_pdf: 9310070v1.pdf
source_sha256: b979ebf2f47a4653
toc_source: undetermined
doc_brief: "Quantum dilogarithm — A quantum generalization of Rogers’ ﬁve term, or “pentagon” dilogarithm identity is suggested. It is shown that the classical limit gives usual Rogers’ identity."
---
3. Quantum Dilogarithm at θN = 1
When |θ| = 1, deﬁnition (1.4) of the quantum dilogarithm needs qualiﬁcation because the
inﬁnite product is not convergent. In this section we restrict ourselves to a particular case,
θN = 1, for some integer, N ≥2, and properly modify the formulae of Section 2.
Let θ = ω, where ω is a primitive N-th root of unity. We choose ω together with its
square root ω1/2 as
ω = exp(2πi/N),
ω1/2 = exp(πi/N).
(3.1)
In this case, operators, satisfying algebra (2.1), can be realized as N-by-N matrices, since
their N-th powers are the central elements. Let us ﬁx them equal to the minus identity
operator :
ˆU N = −1,
ˆV N = −1.
(3.2a)
As a consequence of this choice we have also
(−ˆU ˆV )N = −1.
(3.2b)
The spectrum of any operator, ˆA, whose N-th power is −1, is given by N distinct numbers
ωn−1/2,
n = 0, 1, . . ., N −1,
(3.3)
so, all operators ˆU, ˆV , and −ˆU ˆV have one and the same spectrum (3.3). Index n in (3.3)
can be considered
(mod N), i. e. as an element of ZN.
Before speciﬁcation of the quantum dilogarithm, following [8], for complex variables
a, b, c, constrained by Fermat equation
aN + bN = cN,
(3.4)
deﬁne the function
w(a, b, c|0) = 1,
w(a, b, c|n) =
n
Y
j=1
b/(c −aωj),
n ≥1,
(3.5)
which depends on n only
(mod N) due to relation (3.4):
w(a, b, c|n + N) = w(a, b, c|n).
(3.6)
Quantum dilogarithm Ψ( ˆA), depending on an operator argument, ˆA with spectrum (3.3),
can be deﬁned as an operator, commuting with ˆA, and with spectrum given by
Ψ(ωn−1/2) = Ψ(ω−1/2)w(a, b, c|n),
(3.7)
where Ψ(ω−1/2) is a non-zero complex factor to be speciﬁed later. Using deﬁnition (3.7),
it is easy to derive the “functional” relation on Ψ( ˆA):
Ψ(ω−1 ˆA)Ψ( ˆA)−1 = (c −ω1/2a ˆA)/b,
(3.8)
4
