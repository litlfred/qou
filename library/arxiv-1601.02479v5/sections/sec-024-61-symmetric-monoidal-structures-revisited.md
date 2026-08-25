---
doc_id: arxiv-1601.02479v5
doc_title: "Cohomological Donaldson-Thomas theory of a quiver with potential and quantum enveloping algebras"
section_id: sec-024-61-symmetric-monoidal-structures-revisited
section_title: "Symmetric monoidal structures, revisited"
section_number: 6.1
pages: 50-53
source_pdf: 1601.02479v5.pdf
source_sha256: 52c2dcd4adf2e72b
doc_brief: "Cohomological Donaldson-Thomas theory of a quiver with potential and quantum enveloping algebras — This paper concerns the cohomological aspects of Donaldson – Thomas theory for Jacobi algebras and"
---
+ be a stability
condition, and let µ ∈ (−∞, ∞) be a slope. We assume that ζ is µ -generic. We
deﬁne Xζ -ss
d,N and Xζ -ss
d′,d′′,N as in (78) and (79) respectively. As throughout the
paper, we assume that we are given a Serre subcategory of the ca tegory of ﬁnite-
dimensional CQ-modules, and denote by
ωd,N : Xζ -ss,S
d,N → Xζ -ss
d,N ωd′,d′′,N : Xζ -ss,S
d′,d′′,N → Xζ -ss
d′,d′′,N
COHAS AND QUANTUM ENVELOPING ALGEBRAS 51
the inclusions of the reduced loci corresponding to CQ-modules in S. Consider
again the algebra from the end of Section 5.1
H
(
Aζ ,S
W,µ
)
= H c
(
Mζ -ss,S
µ , ICζ
W,µ
) ∨
∼
=
⨁
d∈Λ ζ
µ
lim
N ↦→∞
H
(
Dim∗ ω!
d,Nφ mon
Tr(W )ζ
d,N
L(d,d)/2
Xζ -ss
d,N
)
.
By [10, Thm.5.11] this algebra carries a localised bialgebra structure, in the sense
that for all decompositions d = d′ + d′′, with d′, d′′ ∈Λζ
µ , there are maps
H
(
Aζ ,S
W,d
)
→ H
(
Aζ ,S
W,d′
)
˜⊠
tw
+ H
(
Aζ ,S
W,d′′
)
(90)
where
H
(
Aζ ,S
W,d′
)
˜⊠
tw
+ H
(
Aζ ,S
W,d′′
)
:=
(
H
(
Aζ ,S
W,d′
)
⊠tw
+ H
(
Aζ ,S
W,d′′
))
(d,d′′)
:=
(
H
(
Aζ ,S
W,d′
)
⊠tw
+ H
(
Aζ ,S
W,d′′
))
[L−1
d′,d′′ ]
Ld′,d′′ :=
∏
i,j∈Q0
∏
1≤t′≤d′
i
∏
1≤t′′≤d′′
j
(yj,t′′ − xi,t′ )
∈ HGd′ (pt) ⊗ HGd′′ (pt)
=C[x1,1, . . . , x1,d′
1 , . . . , xn,1, . . . , xn,d′
n ]Symd′
⊗ C[y1,1, . . . , y1,d′′
1 , . . . , yn,1, . . . , yn,d′′
n ]Symd′′
with Q0 = {1, . . . , n}, satisfying some natural compatibility conditions with the
multiplication, see [10, Def.5.3]. We next describe the most important o f these
conditions, which is a localised variant of the condition that the multiplic ation and
comultiplication together endow H
(
Aζ ,S
W,µ
)
with a bialgebra structure.
Let d1, d2, d3, d4 ∈Λζ
µ . Set
d = d1 + d2 + d3 + d4
c1 = d1 + d2
c2 = d3 + d4
e1 = d1 + d3
e2 = d2 + d4 .
Let I• = H
(
Mζ -ss,S
• ,φ mon
Tr(W )ζ
•
QMζ -ss, S
•
)
. I.e. for now we do not impose our usual
system of (half) Tate twists. By the main result of [10] the following diagram
commutes
Ic1 ⊠+ Ic2
b
/d15/d15
a /d47/d47 (Id1 ⊠+ Id2 ⊠+ Id3 ⊠+ Id4 )(d1,d2),(d3,d4)
c
/d15/d15
Id
d /d47/d47 (Ie1 ⊠+ Ie2)(e1,e2)
where we have left out the (whole) Tate twists, and the subscripts indicate which
Euler class we localise with respect to. Here, a and d are given by the comultipli-
cation, while b is given by multiplication. The morphism c is given by ﬁrst further
localising, then swapping the second and third entries (observing th e Koszul sign
rule), multiplying by the scalar ( −1)χ (d2,d3), then the CoHA multiplication. The
reader is encouraged to consult [10] for the full details; our descr iption in this section
is mainly directed towards the limited aim of explaining required sign conv entions,
as we next explain.
52 BEN DA VISON AND SVEN MEINHARDT
We would like to have, instead, commutativity of the diagram
H
(
Aζ ,S
W,c1
)
⊠+ H
(
Aζ ,S
W,c2
)
a′
/d47/d47
b′
/d15/d15
(
H
(
Aζ ,S
W,d1
)
⊠+ H
(
Aζ ,S
W,d2
)
⊠+ H
(
Aζ ,S
W,d3
)
⊠+ H
(
Aζ ,S
W,d4
))
♥
c′
/d15/d15
H
(
Aζ ,S
W,d
)
d′
/d47/d47
(
H
(
Aζ ,S
W,e1
)
⊠ H
(
Aζ ,S
W,e2
))
♠
(91)
where now the map c′ is deﬁned to be the map swapping the second and third terms
via the symmetric monoidal structure in D≥,lf (MMHM(Λζ
µ )), and then applying
the multiplication. Here,
♥ =(d1, d2), (d3, d4)
♠ =(e1, e2)
as before. The relation between the two diagrams is as follows. The o bjects in
diagram (91) are tensor products of terms I• tensored on the left with half Tate
twists, which we may commute to the left. Then tensoring the morph isms a, b, c, d
on the left by an overall half Tate twist and commuting the required h alf Tate
twists into the tensor product, we obtain the maps a′, b′, c′, d′ respectively. In
order to arrange commutativity of (91), then, we deﬁne the sign o ccurring in the
symmetrizing morphism for D≥,lf (MMHM(Λζ
µ )) to be given by
τ sw(α ⊗β ) = ( −1)χ (d2,d2)χ (d3,d3)+χ (d2,d3)sw(α ⊗β )
where sw is the standard symmetrizing morphism. We pick the superscript τ
since the bilinear form (15) deﬁnes the deviation from the usual sign conven-
tion. The χ(d2, d3) term is as in the deﬁnition of the morphism c. We denote
byτ D≥,lf (MMHM(Λζ
µ )) the symmetric monoidal category obtained via this modi-
ﬁed sign convention.
Proposition 6.1. Let (B, ∗) be a free supercommutative algebra in the category
D(MMHM(Λζ
µ )), given the above symmetric monoidal structure. Then if we de ﬁne
ψ B by modifying the product as in (17), it is a free supercommuta tive algebra in
D(MMHM(Λζ
µ )) with its usual symmetric monoidal structure.
Explicitly, we deﬁne τ sw via the chain of isomorphisms
⨁
d′∈Λ ζ
µ
F ′
d′ ⊠+
⨁
d′′∈Λ ζ
µ
F ′′
d′′ ∼
=
⨁
d′,d′′∈Λ ζ
µ
L(χ (d′,d′)+χ (d′′,d′′))/2 ⊗
(
L−χ (d′,d′)/2 ⊗ F ′
d′
)
⊠+
(
L−χ (d′′,d′′)/2 ⊗ F ′′
d′′
)(92)
∼
=
⨁
d′,d′′∈Λ ζ
µ
L(χ (d′,d′)+χ (d′′,d′′))/2 ⊗
(
L−χ (d′′,d′′)/2 ⊗ F ′′
d′′
)
⊠+
(
L−χ (d′,d′)/2 ⊗ F ′
d′
)
∼
=
⨁
d′′∈Λ ζ
µ
F ′′
d′′ ⊠+
⨁
d′∈Λ ζ
µ
F ′
d′
where we have applied the usual symmetrizing natural isomorphism f or the ten-
sor product of the objects L−χ (d′,d′)/2 ⊗ F ′
d′ and L−χ (d′′,d′′)/2 ⊗ F ′′
d′′ . We deﬁne
the twisted symmetric monoidal structure on D≥,lf (MMHM(Mζ -ss
µ )) via the same
recipe as (92), with ⊠+ replaced with ⊠⊕. It then follows as before from [34] that
dim∗ : τ D≥,lf (MMHM(Mζ -ss
µ )) →τ D≥,lf (MMHM(Λζ
µ ))
is a symmetric monoidal functor.
COHAS AND QUANTUM ENVELOPING ALGEBRAS 53
The algebras H
(
Aζ ,S
W
)
and H(ψAζ ,S
W,µ ) diﬀer by the above type of sign twist. In
particular, their underlying graded monodromic mixed Hodge struct ures are the
same, and Theorem C implies that there is an isomorphism in D≥,lf (MMHM(Λζ
µ )):
τ Sym⊠+
(
H(BC*)vir ⊗ BPSζ ,S
W,µ
)
∼
= Sym⊠+
(
H(BC*)vir ⊗ BPSζ ,S
W,µ
)
.
The next proposition shows that this is a general phenomenon.
Proposition 6.2. Let F ∈ D ≥,lf (MMHM(Mζ -ss
µ \ Mζ -ss
0 )). Then there is an
isomorphism
τ Sym⊠+ (F ) ∼
= Sym⊠+ (F ).
Proof. Let F be represented by the complex ( G, d) of mixed Hodge modules on
Mζ -ss
µ × A1. Let ψ be as in (17). Let
T (G, d) :=

⨁
n≥0
Tn(G), d


Tn(G) :=
⨁
n≥0
G ⊠ . . . ⊠ G/bracehtipupleft
/bracehtipdownright/bracehtipdownleft/bracehtipupright
n times
be the algebra generated by G in the category
D≥,lf

MHM

∐
n≥0
(
(Mζ -ss
µ \ Mζ -ss
0 ) × A1
) ×n




along with its natural diﬀerential. Via the results of [34], as recalled in S ection 3.2,
Tn(G, d) carries an action of Sn, determined by morphisms for each π ∈ Sn and
a1, . . . , an ∈Λζ
µ
Ga1 ⊠ . . . ⊠ Gan
π #
a1,...,a n
− − − − − − →π ∗
(
Gπ (a1) ⊠ . . . ⊠ Gπ (an)
)
.
Setting
π #,τ
a1,...,an :=
∑
1≤i<j≤n|π (i)>π (j)
(−1)τ (ai,aj )π #
a1,...,an
we obtain the τ-twisted action. Then the morphisms
Ga1 ⊠ . . . ⊠ Gan
· ∑
1≤i<j≤n|π (i)>π (j) (−1)ψ (ai ,a j )
− − − − − − − − − − − − − − − − − − − − − − → Ga1 ⊠ . . . ⊠ Gan
commute with the diﬀerential, and intertwine the two Sn-actions. Passing to the
invariant subcomplexes, and taking the direct image along the iterat ed monoid
morphism
∐
n≥0
(
(Mζ -ss
µ \ Mζ -ss
0 ) × A1
) ×n
→ Mζ -ss
µ × A1
we deduce the result. □
