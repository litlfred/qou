---
doc_id: arxiv-1901.01312v1
doc_title: "Braided fermions from Hurwitz algebras"
section_id: sec-001-1-introduction
section_title: "Introduction"
section_number: 1
pages: 1-3
source_pdf: 1901.01312v1.pdf
source_sha256: a480da38283622d6
doc_brief: "Braided fermions from Hurwitz algebras — Some curious structural similarities between a recent braid- and Hurwitz algebraic description of the unbroken internal symmetries for a single generations of"
---
Leptons and quarks are identiﬁed with representations of the gauge group U(1)Y×SU (2)L×
SU (3)C in the Standard Model (SM) of particle physics. Despite its success in accurately
describing and predicting experimental observations, this gauge group lacks a theoretical basis.
Why has Nature chosen these gauge groups from an inﬁnite set of Lie groups, and why do only
some representations correspond to physical states? A second shortcoming of the SM is the lack
of gravity, or equivalently, its uniﬁcation with General Relativity (GR).
Preon models attempt do explain SM structure by proposing that leptons and quarks are not
truly fundamental, instead being composed of a smaller number of subparticles called preons.
The most famous of these is the 1979 Harari-Shupe preon model in which all SM leptons and
quarks are composites of two spin half fermions [1, 2]. This model is able to account for many
of the observed SM symmetries but not without introducing some problems. For one, the
preons must be conﬁned but via what mechanism is not known. Attempts to account for preon
conﬁnement via a QCD-like conﬁnement mechanism inevitably requires sacriﬁcing the original
model’s simplicity.
In 2006, Bilson-Thompson proposed representing a single generation of SM fermions in terms
of simple three stand ribbon braids [3]. Inspired by the model of Harari and Shupe, it duplicates
the success of that model while also avoiding some of its shortcomings 1. The binding of preons
1 Other schemes have also been able to reproduce the structure of the Harari and Shupe preon model. One
such example is a knot model by Finkelstein, in which the trefoil knots, understood as the j = 3/2 irreducible
representations of the quantum group SUq(2), form the basis of fermion states [4, 5]. In that scheme the Rishons
arXiv:1901.01312v1  [physics.gen-ph]  21 Dec 2018
is purely topological, and preons do not have their own independent existence. These braided
objects ﬁnd an embedding into Loop Quantum Gravity (LQG) when the cosmological constant
is not zero [10] 2. A braided description of matter therefore provides a potential means of
unifying the SM with GR, with both being emergent from a theory of quantum gravity based
on (q-deformed) spin networks.
Dixon has demonstrated that many of the SM symmetries can be seen to arise from tensor
products of Hurwitz algebras, in particular the algebra T = C⊗ H⊗ O [12, 13, 14]. Starting
from a split algebra basis in a tensor product of Hurwitz algebras, say C⊗ O, one can deﬁne
projection operators corresponding to primitive idempotents. These reduce C⊗ O spinors into
orthogonal subspaces, each of which transforms correctly as a generation of leptons and quarks
underSU (3)C⊗U(1)Y . In similar constructions by Furey and Stoica, the basis states of minimal
left ideals of the Cliﬀord algebraC𝓁(6) are shown to transform like a single generation of fermions
under the unbroken symmetries SU (3)C⊗U(1)EM [15, 16].
Unlike Lie and Cliﬀord algebras, of which there are inﬁnitely many, there are only four
normed division algebras. Speciﬁc Cliﬀord algebras are generated via the nested left actions
of these algebras (or tensor products of them) on themselves. The bivectors of these close
under commutation to give a representation of a speciﬁc Lie algebra. In this way, the Hurwitz
algebras are very generative. It is well known that the complex numbers generate U(1) and that
the quaternions H are isomorphic to SU (2). The automorphism group of the octonions is the
exceptional Lie groupG2, which contains the subgroupSU (3). The octonions have been studied
in relation to the structure of quarks since 1973 [17, 18]. These observations suggest that the
Hurwitz algebras may be the appropriate mathematical structures from which to derive the SM.
Several curious structural similarities between the braid and Hurwitz algebra descriptions
of SM fermions have recently been identiﬁed [19, 20]. The complex numbers and quaternions
contain representations of precisely the braid groups used to construct braided fermions in the
Helon model. Furthermore, the twist and permutation structure of the ribbon braids in the Helon
model coincides exactly with the states that span the minimal left ideals of C𝓁(6), generated
from the nested left action of C⊗ O on itself, indicating a relation between the braid spectrum
and octonion algebras. These unexpected connections provide the ﬁrst steps towards developing
a uniﬁed theory based on braid groups and Hurwitz algebras. This paper reviews these recent
results and comments of current research.
2. Hurwitz algebras
A Hurwitz algebra is a ﬁnite-dimensional unital (but not necessarily associative) algebra A
with a nondegenerate quadratic form Q satisfying Q(a)Q(b) =Q(ab). There exist two kinds of
Hurwitz algebras; normed division algebras, of which there are exactly four ( R, C, H, O), and
split algebras (split- C, H, O) 3. Generalizing from the real number R to the complex numbers
C, one gives up the ordered property of the reals. Generalizing in turn to the quaterions H one
furthermore loses commutatativity. The quaternions are spanned by 1 ,I,J,K with 1 being the
identity and I,J,K satisfying
I 2 =J 2 =K2 =IJK =−1. (1)
of the Harari-Shupe model may be identiﬁed with the fundamental representations [6, 7]. A second example is
the non-relativistic phase-space approach of ˙Zenczykowski [8, 9].
2 In such cases the underlying spin networks of LQG are q-deformed, giving a framing to its edges and requiring
that these edges be labelled by representations of the quantum group Uq(2) instead of its classical counterpart
[11].
3 A division algebra is an algebra over a ﬁeld where division is always possible, with the exception of division by
zero. In a split algebra on the other hand, there exists at least one x∈A such that Q2(x) =xx∗ = 0 where Q(x)
is the norm of A deﬁned in terms of a conjugation x↦→ x∗. For a division algebra, the multiplicative inverse of
an element x is given by x∗/Q2(x).
Figure 1. Quaternion multiplication I 2 =J 2 =K2 =IJK =−1, and octonion multiplication
represented using a Fano plane.
Finally, in moving to the octonions O one no longer has associativity. An excellent introduction
to the octonions is given by Baez [21]. The octonions are spanned by the identity 1 = e0 and
sevenei satisfying
eiej =−δije0 +ϵijkek, where eie0 =e0ei =ei, e2
0 =e0, (2)
andϵijk is a completely antisymmetric tensor with value +1 whenijk = 123, 145, 176, 246, 257,
347, 365. The multiplication of quaternions and octonions is shown in Figure 1.
