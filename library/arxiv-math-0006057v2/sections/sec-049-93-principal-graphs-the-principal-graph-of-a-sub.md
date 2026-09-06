---
doc_id: arxiv-math-0006057v2
doc_title: "FINITE QUANTUM GROUPOIDS AND THEIR APPLICA TIONS"
section_id: sec-049-93-principal-graphs-the-principal-graph-of-a-sub
section_title: "Principal graphs. The principal graph of a subfactor N ⊂ M is deﬁned"
section_number: 9.3
pages: 41-42
source_pdf: 0006057v2.pdf
source_sha256: c881434fe9f4b04f
doc_brief: "FINITE QUANTUM GROUPOIDS AND THEIR APPLICA TIONS — W e give a survey of the theory of ﬁnite quantum groupoids (wea k Hopf algebras), including foundations of the theory and app lications to ﬁnite"
---
as follows ([JS], 4.2, [GHJ], 4.1). Let X = NL2(M )M and consider the following
sequence of N −N and N −M bimodules :
NL2(N )N, X, X⊗M X ∗, X ⊗M X ∗ ⊗N X,...
obtained by right tensoring with X ∗ and X. The vertex set of the principal graph
is indexed by the classes of simple bimodules appearing as summands in t he above
sequence. Let us connect vertices corresponding to bimodules NYN and NZM by
l edges if NYN is contained in the decomposition of NZN , the restriction of NZM ,
with multiplicity l.
We apply Theorem 9.2.6 to express the principal graph of a ﬁnite dept h subfactor
N ⊂M in terms of the quantum groupoid associated with it.
LetB andK be a quantum groupoid and its left coideal ∗-subalgebra such that
B acts on N and (N ⊂M ) ∼= (N ⊂N>⊳K). Then ˆK = NL2(M )M , where we view
K as a relative ( B,K ) Hopf module as in Example 9.2.3
By Theorem 9.2.6 we can identify irreducible N −N (resp. N −M ) bimodules
with simple B-comodules (resp. relative right ( B,K ) Hopf modules). Consider a
bipartite graph with vertex set given by the union of (classes of) sim pleB-comodules
and simple relative right (B,K ) Hopf modules and the number of edges between the
verticesU and V representingB-comodule and relative right ( B,K ) Hopf module
respectively being equal to the multiplicity of U in the decomposition of V (when
the latter is viewed as a B-comodule) :
simple B-comodules
· · · | · · · | · · ·
simple relative right ( B,K ) Hopf modules
The principal graph of N ⊂M is the connected part of the above graph containing
the trivial B-comodule.
It was shown in ([NV3], 3.3, 4.10) that:
(a) the map δ :I ↦→[g−1/2S(I)g1/2]′∩ ˆB ⊂ ˆB>⊳B deﬁnes a lattice anti-isomorphism
betweenℓ(B) and ℓ( ˆB);
(b) the triple δ(I) ⊂ ˆB ⊂ ˆB>⊳I is a basic construction.
42 DMITRI NIKSHYCH AND LEONID V AINERMAN
Proposition 9.3.1. If K is a coideal ∗-subalgebra of B then the principal graph
of the subfactor N ⊂ N>⊳K is given by the connected component of the Bratteli
diagram of the inclusion δ(K) ⊂ ˆB containing the trivial representation of ˆB.
Proof. First, let us show that there is a bijective correspondence betwee n right
relative (B,K ) Hopf modules and ( ˆB>⊳K)-modules. Indeed, every right ( B,K )
Hopf module V carries a right action of K. If we deﬁne a right action of ˆB by
v⊳x = ⟨v(1), x⟩v(2), v ∈V,x ∈ ˆB,
then we have
(v⊳k )⊳x = ⟨v(1)k(1), x⟩(v(2)⊳k (2)) = ⟨v(1), (k(1)⊲x ) ⟩(v(2)⊳k (2))
= ( v⊳ (k(1)⊲x ))⊳k (2),
for all x ∈ ˆB andk ∈K which shows that kx and (k(1)⊲x )k(2) act on V exactly in
the same way, therefore V is a right ( ˆB>⊳K)-module.
Conversely, given an action of ( ˆB>⊳K) onV , we automatically have aB-comodule
structure such that
⟨v(1)k(1),x ⟩(v(2)⊲k (2)) = ⟨v(1), x(1) ⟩⟨k(1), x(2) ⟩(v(2)⊳k (2))
= ( v⊳ (k(1)⊲x ))⊳k (2) = (v⊳k )⊳x
= ⟨x, (v⊳k )(1) ⟩(v⊳k )(2),
which shows that v(1)k(1) ⊗ (v(2)⊳k (2)) = (v⊳k )(1) ⊗ (v⊳k )(2), i.e., that V is a right
relative (B,K )-module.
Thus, we see that the principal graph is given by the connected com ponent the
Bratteli diagram of the inclusion ˆB ⊂ ˆB>⊳K containing the trivial representation
of ˆB. Since ˆB>⊳K is the basic construction for the inclusion δ(K) ⊂ ˆB, therefore
the Bratteli diagrams of the above two inclusions are the same.
Corollary 9.3.2. If N ⊂N>⊳B is a depth 2 inclusion corresponding to the quan-
tum groupoid B, then its principal graph is given by the Bratteli diagram of the
inclusion ˆBt ⊂ ˆB.
Proof. In this case K =B and inclusion ˆBt ⊂ ˆB is connected, so that δ(K) = ˆBt
(note that ˆB is biconnected).
