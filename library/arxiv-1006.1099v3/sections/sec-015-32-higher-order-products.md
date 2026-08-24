---
doc_id: arxiv-1006.1099v3
doc_title: "FLOER COHOMOLOGY AND PENCILS OF QUADRICS IV AN SMITH"
section_id: sec-015-32-higher-order-products
section_title: "Higher order products"
section_number: 3.2
pages: 19-21
source_pdf: 1006.1099v3.pdf
source_sha256: 76c1c4173cdee9d8
doc_brief: "FLOER COHOMOLOGY AND PENCILS OF QUADRICS — There is a classical relationship in algebraic geometry bet ween a hyperelliptic curve and an associated pencil of quadric hypersurfaces."
---
linear over C. By deﬁnition, F(M ) has:
• objects being monotone oriented Lagrangian submanifolds equippe d withSpin structures
and additional perturbation data 1;
• morphisms given by Floer cochain complexes CF (L,L ′); and
• higher order composition operations from counting pseudoholomor phic polygons.
The higher order operations of the A∞-structure comprise a collection of maps µd
F of degree d
(mod 2), for d≥ 1, with µ1
F being the diﬀerential and µ2
F the holomorphic triangle product
mentioned previously:
µd
F :CF (Ld−1,L d)⊗···⊗ CF (L0,L 1)→CF (L0,L d)[2−d]
The{µd
F} have matrix coeﬃcients which are deﬁned by counting holomorphic dis ks with (d + 1)-
boundary punctures, whose arcs map to the Lagrangian submanif olds (L0,...,L d) in cyclic order.
The construction of the operations µd
F is rather involved, and we defer to [92] for details. We
should emphasise that monotonicity enters crucially in ensuring that the only disk and sphere
bubbling in the zero- or one-dimensional moduli spaces of solutions w e wish to count comes
from bubbling of Maslov index 2 disks on the Lagrangian boundary con ditions, because the
other possible bubbles sweep out subsets of M or the Lj of suﬃciently high codimension to not
interact with holomorphic polygons of index at most 1. Monotonicity, together with Lemma
3.1, further ensures that the Maslov index 2 disks are multiples of ch ain-level representatives for
the units 1 Li in the complexes CF (Li,L i), which in turn means that their contributions to the
boundary strata of one-dimensional solution spaces cancel algeb raically.
Remark 3.4. The simplest construction of F(M ) uses Hamiltonian perturbations to to guarantee
that the Lagrangian submanifolds {Lj} which are boundary conditions for a given higher-order
product are pairwise transverse. In the sequel, we will encounter Lagrangians ﬁbred over arcs in
C (as matching cycles in Lefschetz ﬁbrations), and the Riemann mapp ing theorem will provide
1One can also equip the Lagrangians with ﬂat unitary line bund les; we will not need that reﬁnement in this paper,
though see Remark 3.22.
20 IV AN SMITH
a useful constraint on the µd
F. To take advantage of this systematically would preclude using
Hamiltonian perturbations. There is another approach to the Fuka ya category, based on counting
pearls – conﬁgurations of holomorphic polygons and gradient ﬂow trees – w hich is the open string
counterpart of work of Biran, Cornea and Lalonde. For closed cur ves in monotoneM the theory is
developed in [13], and for open curves the theory is described in [93, S ection 7] and [98, Section 4]
(in the balanced, or monotone, and exact settings respectively). The fact that a pearly deﬁnition
gives rise to a quasi-isomorphic category to that obtained through Hamiltonian perturbations is
addressed by a “mixed category” trick in [98, Section 4.8], cf. [92, Se ction 10a].
In general, pearly moduli spaces cannot be made transverse, and a complete deﬁnition of the
Fukaya category using only pearls relies on virtual perturbation te chniques. In this paper, the
A∞-structures are essentially always constrained by their formal alg ebraic properties, rather than
by explicit computations (or the computations involve rather benign non-transversal situations,
for instance a pair of Lagrangians meeting cleanly in a Morse-Bott int ersection). However, a
pearly model would be more natural in Section 5.5, even if not strictly required.
Suppose λ∈ K is not an eigenvalue of the quantum cup-product
∗c1(M ) : QH ∗(M ; K)→QH ∗(M ; K).
Then c1(M )−λ1M is invertible in QH ∗(M ); on the other hand, if L∈ F(M ;λ), then Lemma
3.1 implies that c1(M )−λ1M↦→0∈ HF ∗(L,L ), which implies that HF ∗(L,L ) = 0. Lemma
3.1 therefore implies that a monotone symplectic manifold M gives rise to a collection of mu-
tually orthogonal categories F(M ;λ), which are non-trivial only for λ an eigenvalue of ∗c1(M ) :
QH ∗(M )→ QH ∗(M ). The summand F(M ;λ) has as objects the Lagrangian submanifolds L
for which m0(L) = λ, i.e. for which the natural map of Z2-graded unital rings
QH ∗(M )→HF (L,L ) takes c1(M )↦→m0(L)· (unit). (3.4)
We will refer to the category F(M ; 0) as the nilpotent summand of the Fukaya category. We next
recall the deﬁnition of the Hochschild cohomology of an A∞-category, which is deﬁned by a bar
complex CC ∗(A) as follows. A degree r cochain is a sequence ( hd)d≥0 of collections of linear
maps
hd
(X1,...,Xd+1) :
1⨂
i=d
homA(Xi,X i+1)→homA(X1,X d+1)[r−d]
for each (X1,...,X d+1)∈Ob(A)d+1. The diﬀerential is deﬁned by the sum over concatenations
(∂h)d(ad,...,a 1) =
∑
i+j<d+1
(−1)(r+1)✠ iµd+1−j
A (ad,...,a i+j+1,h j(ai+j,...,a i+1),a i,...,a 1)
+
∑
i+j≤d+1
(−1)✠ i+r+1hd+1−j(ad,...,a i+j+1,µ j
A(ai+j,...,a i+1),a i,...,a 1).
(3.5)
It is a basic fact that HH ∗(A) = H(homf un(A,A)(id, id)) computes the morphisms in the A∞-
category of endofunctors of A from the identity functor to itself; moreover, the Hochschild coho -
mology of an A∞-category over a ﬁeld is invariant under passing to a split-closed tria ngulated
envelope [15, Theorem 4.12]. The maps of Equation 3.4 are the lowest o rder pieces of a natural
“open-closed string map”
QH ∗(M )−→HH ∗(F(M ))
from quantum cohomology to Hochschild cohomology, given by count ing holomorphic polygons
with one interior marked point, constrained to a cycle in M , and a collection of boundary
punctures, one of which is outgoing and the rest incoming. Equation 3.4 corresponds to the
case in which there are no boundary inputs. By construction, the o pen-closed string map is
FLOER COHOMOLOGY AND PENCILS OF QUADRICS 21
compatible with the decomposition of the Fukaya category into orth ogonal summands and with
the splitting of Equation 3.1, giving maps
QH ∗(M ;λ)−→HH ∗(F(M ;λ))
for each λ∈ Spec(∗c1(M )).
Remark 3.5. The monotone Fukaya category F(M ) is invariant, up to quasi-isomorphism, under
rescaling the symplectic form. Some care must be taken, however, when considering products of
monotone manifolds, since the factors cannot be scaled independe ntly preserving monotonicity.
