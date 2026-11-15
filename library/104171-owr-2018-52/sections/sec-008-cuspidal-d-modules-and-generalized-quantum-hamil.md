---
doc_id: 104171-owr-2018-52
doc_title: "Enveloping Algebras and Geometric Representation Theory (Oberwolfach Report No. 52/2018)"
section_id: sec-008-cuspidal-d-modules-and-generalized-quantum-hamil
section_title: "Cuspidal D-modules and generalized quantum Hamiltonian reduction"
section_number: null
pages: 24-27
source_pdf: 10.4171-owr-2018-52.pdf
source_sha256: b33ed36eaa470877
toc_source: inferred
doc_brief: "Enveloping Algebras and Geometric Representation Theory (Oberwolfach Report No. 52/2018) — The workshop brought together experts investigating algebraic Lie theory from the geometric and categorical"
---
Sam Gunningham
Let G be a connected complex reductive group acting on g = Lie(G) by the adjoint
action. We consider the abelian category Dmod(g)G of strongly G-equivariant D-
modules on g. In [Gun18] we proved the following generalized Springer theorem
for Dmod(g)G.
Theorem 1. There is an equivalence of abelian categories
Dmod(g)G ≃
⊥
M
(L,E)
Dmod (z(l))WG,L ,
where the (ﬁnite) sum is indexed by cuspidal data (L, E) in the sense of Lusztig
[Lus84].1 Here, L is a Levi subgroup of G, z(l) denotes the center of l = Lie(L)
and WG,L = NG(L)/L is the relative Weyl group.
Example 2. The block Dmod(g)G
Spr corresponding to the unique cuspidal datum
(T, E) for a maximal torus T is known as the Springer block.
The theorem in
particular gives an equivalence
Dmod(g)G
Spr ≃Dmod(t)W = Dt#W −mod
where W is the Weyl group of G (with respect to T ). In the case G = GLn (or
PGLn) the Springer block is the entire category. Thus there is an equivalence
Dmod(gln)GLn ≃Dmod(An)Sn ≃DAn#Sn −mod
Example 3. In the case G = SL2, there is a unique simple cuspidal D-module E
supported on the nilpotent cone of G. It may be characterized as the intersection
cohomology (IC) extension of the unique non-trivial local system on the regular
nilpotent orbit.2 In this case the generalized Springer decomposition has two blocks
- the Springer block and the cuspidal block:
Dmod(sl2)SL2 ≃Dmod(A1)Z/2Z ⊕⟨E⟩
The cuspidal block ⟨E⟩is a semisimple category with a single simple object E, thus
it is equivalent to the category of vector spaces.
1A cuspidal datum consists of a pair (L, E) of a Levi subgroup of G and a simple D-module
supported on the nilpotent cone for L which is cuspidal: it vanishes upon parabolic restriction
to every proper Levi subgroup of L. Considering the simple objects of the subcategory of equi-
variant D-modules supported on the nilpotent cone of G recovers Lusztig’s generalized Springer
correspondence.
2In fact the extension is clean, so the IC extension agrees with the star and shriek extensions.
Enveloping Algebras and Geometric Representation Theory
3105
The goal of this project is to understand the interaction of the generalized
Springer decomposition with the underlying G-representation on the global sec-
tions of the D-module.
To give a sense of of what such an understanding might look like, let us ﬁrst ex-
amine the Springer block. Consider the equivariant D-module P := Dg/Dgad(g),
which represents the functor of quantum Hamiltonian reduction (i.e. G-invariants
of the global sections of a strongly equivariant module). Combining the results of
Hotta-Kashiwara [HK84] with Theorem 1 one can show the following:
Theorem 4. The Hamiltonian reduction D-module P is a projective generator of
the Springer block; under the generalized Springer correspondence
Dmod(g)G
Spr ≃Dmod(t)W
it corresponds to the object Dt (with its canonical W-equivariant structure). In
particular the Springer block is characterized by the property that any non-zero
object has a G-invariant vector.
It is natural to ask: is the a similar characterization of the other generalized
Springer blocks?
Let us ﬁrst describe a natural generalization of the quantum Hamiltonian re-
duction D-module P. For each (ﬁnite dimensional) representation V of G, there
is a canonical strongly equivariant D-module
P(V ) := Dg ⊗Ug V
where the homomorphism ad : Ug →Dg is induced from the inﬁnitesimal adjoint
action. The modules P(V ) are compact and projective; they represent the functor
which assigns to each equivariant D-module its V -multiplicity space. The collec-
tion of all P(V ) as V ranges over ﬁnite dimensional representations of G forms a
set of compact projective generators of Dmod(g)G.
Now our question can be made more precise: how do the modules P(V ) under
the generalized Springer decomposition?
This question has a nice partial answer in the case G = SLn (though we shall see
that the situation is necessarily more complicated for other types). In general, the
component group π0Z(G) = Z(G)/Z◦(G) acts on the category Dmod(g)G, giving
an orthogonal decomposition indexed by the characters
\
π0Z(G). In the case G =
SLn, we may show that this decomposition agrees with the generalized Springer
decomposition, in the sense that for each character k ∈
\
π0Z(G) ≃Z/nZ there is
a corresponding cuspidal datum (Lk, Ek) such that the corresponding generalized
Springer block is characterized by the fact that π0(Z(G)) acts via the character k.
In particular, for an irreducible representation V , Z(G) acts on V via a character
k and the D-module P(V ) lies entirely in the corresponding generalized Springer
block. If the central character k of V is relatively prime to n then the D-module
P(V ) is a direct sum of a number of copies of the unique simple cuspidal object
with the same central character.
3106
Oberwolfach Report 52/2018
Example 5. If G = SL2 and Vn = Symn(C2) the irreducible representation of
dimension n + 1, P(Vn) is cuspidal exactly when n is odd. In that case P(Vn) ≃
E⊕mn for some non-negative integers mn. By the universal property of the objects
P(Vn), the multiplicities mn may also be interpreted as the multiplicity of the
representation Vn in the global sections of E.3 On the other hand, for even values
of n P(Vn) lies in the Springer block which is equivalent to Dmod(t)W . Under
this equivalence, P(Vn) corresponds to Dt (respectively Dt ⊗sgn) if n ≡0 mod 4
(respectively n ≡2 mod 4).
One can see that the situation for G = SLn cannot hold in general: there are
groups G of adjoint type (so Z(G) = 1) which admit non-trivial cuspidal data.
In those cases one can show that the D-module P(V ) always have a summand
which is contained in the Springer block (controlled by the zero weight space of
V together with its Weyl group representation). But for certain representations
there may be other summands which live in other generalized Springer blocks.
This naturally leads to the following set of problems, which the author hopes
to investigate in forthcoming work.
• Let us call a representation quasi-cuspidal if P(V ) admits a cuspidal sum-
mand (equivalently, submodule or quotient).
How to characterize the
quasi-cuspidal representations?
• Find a minimal set of irreducible representations V1, . . . Vn such that
P(V1), . . . , P(Vn) generate the category Dmod(g)G.
• For each cuspidal datum (L, E), characterize the corresponding block of
Dmod(g)G in terms of the irreducible representations of G appearing as a
summand of the global sections.
References
[CEE09] Damien Calaque, Benjamin Enriquez, and Pavel Etingof, Universal KZB equations:
the elliptic case, Algebra, arithmetic, and geometry: in honor of Yu. I. Manin. Vol. I,
Progr. Math., vol. 269, Birkh¨auser Boston, Inc., Boston, MA, 2009, pp. 165–266.
[Gun18] Sam Gunningham, Generalized Springer theory for D-modules on a reductive Lie al-
gebra, Selecta Mathematica, New Series (2018).
[HK84]
Ryoshi Hotta and Masaki Kashiwara, The invariant holonomic system on a semisimple
Lie algebra, Inventiones Mathematicae 75 (1984), no. 2, 327–358.
[Lus84]
G. Lusztig, Intersection cohomology complexes on a reductive group, Inventiones Math-
ematicae 75 (1984), no. 2, 205–272.
3Since giving the talk, the author has learned that these multiplicities (and corresponding
ones for G = SLn) have been computed by Calaques-Enriques-Etingof [CEE09] using a certain
Schur-Weyl duality functor with values in a rational Cherednik algebra: we have mn = n.
Enveloping Algebras and Geometric Representation Theory
3107
