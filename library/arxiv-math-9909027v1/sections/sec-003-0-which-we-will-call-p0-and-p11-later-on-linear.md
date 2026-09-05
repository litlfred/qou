---
doc_id: arxiv-math-9909027v1
doc_title: "Planar Algebras, I V. F. R. Jones ∗ Department of Mathematics University of California"
section_id: sec-003-0-which-we-will-call-p0-and-p11-later-on-linear
section_title: "(which we will call P0 and P1,1 later on). Linear maps between tensor"
section_number: 0
pages: 4-6
source_pdf: 9909027v1.pdf
source_sha256: e6cd544cdc141d3b
doc_brief: "Planar Algebras, I V. F. R. Jones ∗ Department of Mathematics University of California — We introduce a notion of planar algebra, the simplest exampl e of which is a vector space of tensors, closed"
---
powers of these vector spaces form a coloured operad Hom in th e obvious
way under composition of maps and the planar algebra structu re on the V ’s
is given by a morphism of coloured operads from P to Hom. In practice this
means that, to a k-tangle T in P there is a linear map Z(T ) : ⨂ n
i=1 Vki → Vk
such that Z(T ◦i S) = Z(T ) ◦i Z(S) where the ◦i on the right-hand side is
composition of linear maps in Hom .
Note that the vector spaces V white
0 and V black
0 may be diﬀerent. This is
the case for the “spin models” of §3. Both these V0’s become commutative
associative algebras using the tangles
D2
D1
and
D2
D1
4
To handle tangles with no internal discs we decree that the te nsor product
over the empty set be the ﬁeld K and identify Hom( K, Vk) with Vk so that
each Vk will contain a privileged subset which is Z({k-tangles with no internal
discs}). This is the “unital” structure (see [Ma]).
One may want to impose various conditions such as dim( Vk) < ∞ for all
k. The condition dim( V white
0 ) = 1 =dim( V black
0 ) is signiﬁcant and we impose
it in our formal deﬁnition of planar algebra (as opposed to ge neral planar
algebra) later on. It implies that there is a unique way to ide ntify each
V0 with K as algebras, and Z(© ) = 1 = Z( ). There are thus also two
scalars associated to a planar algebra, δ1 = Z( ) and δ2 = Z( ) (the inner
circles are strings, not discs!). It follows that Z is multiplicative on connected
components, i.e., if a part of a tangle T can be surrounded by a disc so that
T = T ′ ◦i S for a tangle T ′ and a 0-tangle S, then Z(T ) = Z(S)Z(T ′) where
Z(S) is a multilinear map into the ﬁeld K.
Two simple examples serve as the keys to understanding the no tion of a
planar algebra. The ﬁrst is the Temperley-Lieb algebra T L, some vestige of
which is present in every planar algebra. The vector spaces T Lk are:
T Lblack
0 ≃ T Lwhite
0 ≃ K
and T Lk is the vector space whose basis is the set of diﬀeomorphism cl asses of
connected planar k-tangles with no internal discs, of which there are 1
k+1
( 2k
k
)
.
The action of a planar k-tangle on T L is almost obvious — when one ﬁlls the
internal discs of a tangle with basis elements of T L one obtains another basis
element, except for some simple closed curves. Each closed c urve counts a
multiplicative factor of δ and then is removed. It is easily veriﬁed that this
deﬁnes an action of P on T L. As we have observed, any planar algebra
contains elements corresponding to the T L basis. They are not necessarily
linearly independent. See [GHJ] and §2.1.
The second key example of a planar algebra is given by tensors . We
think of a tensor as an object which yields a number each time i ts indices
are speciﬁed. Let Vk be the vector space of tensors with 2 k indices. An
element of P gives a scheme for contracting tensors, once a tensor is assi gned
to each internal disc. The indices lie on the strings and are l ocally constant
thereon. The boundary indices are ﬁxed and are the indices of the output
5
tensor. All indices on strings not touching D are summed over and one
contracts by taking, for a given set of indices, the product o f the values of
the tensors in the internal discs. One recognizes the partit ion function of
a statistical mechanical model ([Ba]), the boundary index v alues being the
boundary conditions and the tensor values being the Boltzma nn weights.
This diagrammatic contraction calculus for tensors is well known ([Pe]) but
here we are only considering planar contraction systems. If the whole planar
algebra of all tensors were the only example this subject wou ld be of no
interest, but in fact there is a huge family of planar subalge bras — vector
spaces of tensors closed under planar contractions — rich en ough to contain
the theory of ﬁnitely generated groups and their Cayley grap hs. See §2.7.
The deﬁnition of planar algebra we give in §1 is not the operadic one.
When the planar algebra structure ﬁrst revealed itself, the Vk’s already had an
associative algebra structure coming from the von Neumann a lgebra context.
Thus our deﬁnition will be in terms of a universal planar alge bra on some set
of generators (labels) which can be combined in arbitrary pl anar fashion. The
discs we have used above become boxes in section one, reﬂecti ng the speciﬁc
algebra structure we began with. The equivalence of the two d eﬁnitions is
completed in Proposition 1.20. The main ingredient of the eq uivalence is
that the planar operad P is generated by the Temperley-Lieb algebra and
tangles of two kinds:
