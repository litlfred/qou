---
doc_id: arxiv-0911.4494v2
doc_title: "The geometry of Markov traces Ben Webster Geordie Williamson"
section_id: sec-005-6-character-sheaves-and-molien-series
section_title: "Character sheaves and Molien series"
section_number: 6
pages: 11-13
source_pdf: 0911.4494v2.pdf
source_sha256: 1ba1c79686b12d98
doc_brief: "The geometry of Markov traces Ben Webster Geordie Williamson — We give a geometric interpretation of the Jones-Ocneanu tra ce on the Hecke algebra, using the equivariant cohomology of shea ves on"
---
need only sum over the sheaves that appear as summands of K1, since the trivial local
system is the only unipotent character sheaf onT. Let us give a more careful description
of these sheaves.
Consider the variety ~G = G∆×B∆ B and let c : G∆×B∆ B→ G be the map induced
by ( g, t)↦→gtg−1. A unipotent character sheaf is induced from T if and only if it is a
summand of K1 = c∗
/CZ
~G.
It is known that the map ~G→ G is small, and so the sheaf K1 is the intermediate
extension of a local system on the regular semi-simple locus Greg, since ~Greg → Greg
is a Galois covering with Galois group W. Because intermediate extension preserves
endomorphism rings,
End(K1) = End
/CZ W(/CZ W) = /CZ W.
Thus, the isomorphism types of simple summands which appear are in canonical
bijection with simple representations of W. Given an irreducible character ν∈ ˆW recall
that we denote byVν the corresponding unipotent character sheaf.
Set t∗ = X(T)⊗Z
/CZ , where X(T) denotes the lattice of characters of T. Note that t∗ is a
W-module in a natural way , and set E = Sym•(t∗)⊗∧•t∗, which we may view as a W-
module with the tensor product action. We have a canonical id entiﬁcation E /simequalH∗
T∆
(T).
11
The geometry of Markov traces
The geometric realization of this algebra equips it with a bi grading by degree and
weight as in Section 4. Given an irreducible character ν∈ ˆW the graded dimension
Mν(q, t) =
∑
i, j
qi/2t j−i dim HomW(Vν, E)i, j
is called the Molien series of ν.
Proposition 12. H•
G∆
(Vν) = HomW(Vν, E).
Proof. Because K1 = c∗
/CZ
~G we have canonical isomorphisms
(6) H•
G∆
(K1) /simequalH•
G(~G) /simequalH•
B∆
(B) /simequalH•
T(pt)⊗ H•(T) /simequalE.
The W-action on K1 induces a W-action on E such that with this induced action
H•
G∆
(Vν, E) = HomW(Vν, E).
Thus, we need only check that the induced W-action on E via the the isomorphisms (6)
is the natural action. Since W acts by algebra homomorphisms, it su ﬃces to check this
on H1 and on pure classes in H2. To this end, note that the restriction map
(7) H•
G(~G)→ H•
G(~Greg)
is W-equivariant, where the W-action on HG(~Greg) is induced by the deck transforma-
tions of the covering ~Greg→ Greg. We claim that the restriction map (7) is an injection
on H1 and an isomorphism on the subspace of pure classes.
We may identify ~Greg = G/T× Treg. Under this identiﬁcation the W-action by deck
transformations is given by w· (gT, t) = (g ˙w−1T, ˙wt ˙w−1). Furthermore the G-action on
Treg is trivial and hence
(8) H•
G(~Greg) = H•
G(G/T)⊗ H•(Treg) /simequalH•
T(pt)⊗ H•(Treg).
It is straightforward to check that under the isomorphisms ( 6) and (8) the restriction
map (7) is the tensor product of the identity on H•
T(pt) and the restriction map H•(T)→
H•(Treg) on ordinary cohomology .
Now Treg is obtained from the smooth variety T by removing a divisor, and so
H•(T)→ H•(Treg) is injective on H1 and there are no pure classes in positive degree in
either group. Hence the pure classes in both (6) and (8) consi sts of the image of H•
T(pt).
It follows that (7) is injective on H1 and an isomorphism on pure classes as claimed.
Finally , given the above description of the action ofW on G/T×Treg one may conclude
that the induced action of W on (8) is the tensor product of the natural action of W on
HT(pt) = Sym•(t∗) and action induced by conjugation on H•(Treg). The proposition then
follows. □
This geometric realization of the Molien series allows us toarrive at the main theorem
of [Gom06] by a very di ﬀerent route.
12
Ben Webster & Geordie Williamson
Corollary 13. For all characters ν∈ ˆW, we have M ν(q, t) = PVν(q, t). In particular, by
Proposition 8, it follows that
Tr(x) =
∑
χ∈ ˆW
χq(x)·{ χ, ν}· Mν(q, t).
Remark 2. The above identiﬁcation of the cohomology of a character she af with a
multiplicity space reﬂects a deeper fact about the structur e of G∆-equivariant sheaves
on G: by an extension of the arguments above, one can construct a natural isomorphism
Ext•
G∆(K1) /simequal
/CZ [W]#E as bigraded algebras. This provides an equivariant version of a
theorem of Ginzburg [Gin93, Theorem 8.1].
