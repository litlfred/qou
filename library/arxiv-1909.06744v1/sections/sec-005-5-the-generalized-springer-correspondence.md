---
doc_id: arxiv-1909.06744v1
doc_title: "Springer correspondence for symmetric spaces"
section_id: sec-005-5-the-generalized-springer-correspondence
section_title: "§5. The generalized Springer correspondence"
section_number: null
pages: 5-7
source_pdf: 1909.06744v1.pdf
source_sha256: 82e3980da78c07da
toc_source: inferred
doc_brief: "Springer correspondence for symmetric spaces — This is a survey on the Springer correspondence for symmetric spaces."
---
The map W ∧֒ →NG is not necessarily surjective. It is an interesting problem to
understand the pair (O, E ) which is not contained in the image of W ∧(for example,
the unique missing pair (O, E ) in the case of type G2, F4 or E8 in Remarks 3.3).
As an analogue of the Harish-Chandra theory of the representations of reductive
groups, Lusztig extended this map to a bijection to NG. His ingredients are as
follows;
• The notion of a cuspidal pair for (O, E ) ∈NG,
• The notion of an induction indG
P for a parabolic subgroup P of G and its
Levi subgroup L,
indG
P : { L-equiv. perverse sheaves on L } →{ semisimple complexes on G }.
Note that K is called a semisimple complex if it is a direct sum of various A[i],
where A[i] is a degree shift of a semisimple perverse sheaf A. The induction functor
indG
P is deﬁned as follows. We consider the diagram
L
α
←−−−b
XP
ψ
−−−→e
XP
π
−−−→G,
where
b
XP = {(x, g) ∈G × G | g−1xg ∈P},
e
XP = {(x, gP) ∈G × G/P | g−1xg ∈P},
and the maps are deﬁned by
α : (x, g) 7→ηP(g−1xg),
ψ : (x, g) 7→(x, gP),
π : (x, gP) 7→x.
(η : P →L ≃P/UP is the natural projection.) Here α is a smooth morphism with
connected ﬁbre, and ψ is a principal P-bundle. Let K be an L-equivariant perverse
sheaf on L. Then α∗K[a] is a P-equivariant perverse sheaf on b
X (a is the dimension
of the ﬁbre of α), and there exists a unique perverse sheaf eK on e
X such that
α∗K[a] ≃ψ∗eK[b]
6
with b = dim P. Since e
XP is smooth, irreducible, and π is proper, π∗eK is a semisim-
ple complex on G by the decomposition theorem of Deligne-Gabber.
We deﬁne
indG
P K = π∗eK. Note that unless P = B, the map e
XP →L is not deﬁned directly,
so we need to consider b
XP for deﬁning eK.
Let SG be the set of triples (L, O1, E1), up to the natural action of G, where L
is a Levi subgroup of a parabolic subgroup of G, and (O, E ) ∈NL is a cuspidal pair.
Put WL = NG(L)/L. In general, WL is not a Coxeter group, but in a very special
situation that NL has a cuspidal pair, it turns out that WL is a Coxeter group. For
ξ = (L, O1, E1) ∈SG, put Kξ = IC(O1, E1)[dim O1]. Then Kξ is an L-equivariant
perverse sheaf on L, and one can consider the complex indG
P Kξ on G. The following
result was proved by Lusztig.
Theorem 5.1 (Lusztig [L3]).
(i) For ξ = (L, O1, E1) ∈SG, Kξ is a semisimple
perverse sheaf on G, equipped with WL-action, and is decomposed as
indG
P Kξ ≃
M
(O,E )∈NG
V ξ
(O,E ) ⊗IC(O, E )[dim O],
where V ξ
(O,E ) is an irreducible WL-module if it is non-zero.
(ii) For any ξ ∈SG, we have a bijection
N (ξ)
G
:= {(O, E ) ∈NG | V ξ
(O,E )̸ = 0} ∼
−→W ∧
L .
(iii) We have a partition NG = `
ξ∈SG N (ξ)
G . In particular, there exists a natural
bijection
NG ∼
−→
a
ξ∈SG
W ∧
L ,
which is called the generalized Springer correspondence.
Remarks 5.2.
(i) In general, cuspidal pairs occur very rarely. Let G = SpN or
SON, and δN the number of cuspidal pairs in G. Then we have
• G = SpN : δN =
(
1
if N = d(d −1) for some d ∈Z ,
0
otherwise.
• G = SON : δN =
(
1
if N = d2 for some d ∈Z ,
0
otherwise.
For example, the occurrence of the cuspidal pairs are given as
N = 2, 6, 12, 20, 30, . . .
(G : SpN),
N = 1, 4, 9, 16, 25, . . .
(G : SON).
(ii)
If ξ0 = (L, O1, E1), where L = T is a maximal torus, O1 = {1} is the
identity class, and E1 is the constant sheaf ¯Ql, then indG
P Kξ0 gives the original
Springer correspondence in Theorem 3.2 and Theorem 4.1. In this case,
• 1W ↔IC(O1, ¯Ql) : O1 : the regular unipotent class in Guni.
• εW ↔IC(O0, ¯Ql) : O0 = {1} ; the identity class.
