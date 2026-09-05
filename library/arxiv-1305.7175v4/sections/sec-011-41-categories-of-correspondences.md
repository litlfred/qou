---
doc_id: arxiv-1305.7175v4
doc_title: "NONLINEAR TRACES"
section_id: sec-011-41-categories-of-correspondences
section_title: "Categories of correspondences"
section_number: 4.1
pages: 24-27
source_pdf: 1305.7175v4.pdf
source_sha256: 5a09955f4fb6a57e
doc_brief: "NONLINEAR TRACES — W e combine the theory of traces in homotopical algebra with s heaf theory in de- rived algebraic geometry to deduce general ﬁxed point and ch aracter formulas."
---
work in the symmetric monoidal ( ∞, 1)-category Stacksk of derived stacks over Spec k. It is
worth pointing out that the constructions of this section apply in an y presentable∞-category
with the Cartesian symmetric monoidal structure.
LetCorrk denote the symmetric monoidal ∞-category of correspondences in Stacksk. Thus
morphisms are given by the classifying space of correspondences
X Z/d111/d111 /d47/d47Y
so all higher morphisms are isomorphisms. Composition of correspon dences is given by the
derived ﬁber product. The based loop category
ΩCorrk = EndCorr k(Speck)≃Stacksk
is again derived stacks, regarded as self-correspondences of th e point Spec k.
NONLINEAR TRACES 25
We will also enhance Corrk to the symmetric monoidal (∞, 2)-categoryCorrk where we now
allow noninvertible maps of correspondences
Z
/d126/d126⑥⑥⑥⑥⑥⑥⑥⑥
/d32/d32❆❆❆❆❆❆❆❆
/d15/d15
X Y
W
/d96/d96❇❇❇❇❇❇❇❇
/d62/d62⑥⑥⑥⑥⑥⑥⑥⑥
In other words, the morphisms Corrk(X,Y ) now form the ∞-category Stacks/X×Y of stacks
overX×Y with arbitrary morphisms rather than isomorphisms as in Corrk(X,Y ).
We will also have need to restrict the class of morphisms of correspo ndences to some sub-
category of Stacks/X×Y . In particular, we will consider the subcategory Corrprop
k in which we
only allow proper maps of correspondences.
4.2. T races of correspondences. Given a map Z → X, it is convenient to introduce the
symmetric presentation of the based loop space
LZX =Z×Z×XZ
Note the two natural identiﬁcation with the traditional based loop s pace
LX×X Z≃X×X×XZ Z ×Z×X Z∼/d111/d111 ∼ /d47/d47Z×X×XX≃Z×XLX
There is a natural rotational equivalence LX×X Z≃ Z×XLX that makes the above two
identiﬁcations coincide. (It does not preserve base points and is no t given by swapping the
factors). Thus we can unambiguously identify all of the above vers ions of the based loop space.
Proposition 4.1. (1) Any derived stack X is dualizable as an object of Corrk, with dual X ∨
identiﬁed with X itself, and dimension dim(X) identiﬁed with the loop space
LX =XS1
≃X×X×XX
regarded as a self-correspondence of pt = Speck.
(2) The transpose of any correspondence X← Z→ Y is identiﬁed with the reverse corre-
spondenceY ←Z→X. The trace of a self-correspondence X←Z→X is identiﬁed with the
based loop space
Tr(Z)≃Z|∆ X =Z×X×XX≃L ZX
regarded as a self-correspondence of pt = Speck.
In particular, the trace of the graph Γf→X×X of a self-map f :X→X is identiﬁed with
the ﬁxed point locus
Tr(f )≃ Γf|∆ X = Γf×X×XX≃Xf
Proof. The evaluation and coevaluation presenting the self-duality of X are both given by X
itself as a correspondence between pt = Speck andX×X via the diagonal map. The standard
identities follow from the calculation of the ﬁber product of the two d iagonal maps
X ∆ 12×X×X×X ∆ 23X≃X
26 DA VID BEN-ZVI AND DA VID NADLER
Thus the dimension of X is the loop space
LX
/d123/d123✇✇✇✇✇✇✇✇✇
/d35/d35●●●●●●●●●
X
/d127/d127⑦⑦⑦⑦⑦⑦⑦⑦
/d35/d35●●●●●●●●● X
/d123/d123✇✇✇✇✇✇✇✇✇
/d31/d31❅❅❅❅❅❅❅❅
pt X ×X pt
By deﬁnition, the transpose of a correspondence X←Z→Y is identiﬁed with Y←Z→X
by checking the deﬁnition
Z
/d118/d118♥♥♥♥♥♥♥♥♥♥♥♥♥
/d39/d39PPPPPPPPPPPPP
Y×Z
/d120/d120♣♣♣♣♣♣♣♣♣♣♣
/d39/d39PPPPPPPPPPPP Z×X
/d119/d119♥♥♥♥♥♥♥♥♥♥♥♥
/d38/d38◆◆◆◆◆◆◆◆◆◆◆
Y×X
/d123/d123①①①①①①①①①
/d38/d38◆◆◆◆◆◆◆◆◆◆◆ Y×Z×X
/d119/d119♥♥♥♥♥♥♥♥♥♥♥♥
/d39/d39PPPPPPPPPPPP Y×X
/d120/d120♣♣♣♣♣♣♣♣♣♣♣
/d35/d35●●●●●●●●●
Y Y ×X×X Y ×Y×X X
The trace of a self-correspondence X←Z→X is then calculated by the composition
Z×Z×X Z
/d120/d120qqqqqqqqqqq
/d38/d38▼▼▼▼▼▼▼▼▼▼▼
Z
/d123/d123✇✇✇✇✇✇✇✇✇
/d38/d38◆◆◆◆◆◆◆◆◆◆◆ Z
/d120/d120♣♣♣♣♣♣♣♣♣♣♣
/d35/d35●●●●●●●●●
X
/d127/d127⑦⑦⑦⑦⑦⑦⑦⑦
/d35/d35❋❋❋❋❋❋❋❋❋ Z×X
/d120/d120qqqqqqqqqqq
/d38/d38▼▼▼▼▼▼▼▼▼▼▼ X
/d123/d123①①①①①①①①①
/d31/d31❅❅❅❅❅❅❅❅
pt X ×X X ×X pt
Finally, the case of the graph Z = Γf of a self-map gives the ﬁxed point locus by deﬁnition.
□
Remark 4.2 (Cyclic version). The identiﬁcation dim(X)≃LX above is naturallyS1-equivariant
for the standard loop rotation on LX and the cyclic symmetry of dim( X) provided by the
cobordism hypothesis. To see this it is useful to consider X as anE∞-algebra object in Stacksop
k
via the diagonal map (or as an En-object for any n). In other words, for n = 1 we identify
stacks and correspondences with objects and morphisms in the Mo rita category Alg(Stacksop
k ).
It follows from the properties of topological chiral homology [L2, Th eorem 5.3.3.8] that for
a (constant) commutative algebra A its topological chiral homology over a manifold is given
by the tensoring of commutative algebras over simplicial sets
∫
MA = M⊗A. In particular
(passing back from the opposite category to stacks) we have
∫
S1X =XS1
=LX. Moreover this
identiﬁcation holds not just for a ﬁxed circle but over the moduli spa ce of circles BDiff (S1)∼
BS 1, i.e. equivariantly for rotation. We also know from [L2, Example 5.3.3.14 ] or [L3, Example
NONLINEAR TRACES 27
4.2.2] that the S1-action on the dimension of an associative algebra A (given classically by
the cyclic structure on the Hochschild chain complex) is given by the r otation S1-action on
the topological chiral homology
∫
S1A, i.e., the family of topological chiral homologies over the
moduli space of circles. In our case this recovers the rotation act ion on the loop space.
