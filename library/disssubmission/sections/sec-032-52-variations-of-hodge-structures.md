---
doc_id: disssubmission
doc_title: "Tannakian categories of perverse sheaves on abelian varieties"
section_id: sec-032-52-variations-of-hodge-structures
section_title: "Variations of Hodge structures"
section_number: 5.2
pages: 110-114
source_pdf: DissSubmission.pdf
source_sha256: 207fd5e3dc0d278d
toc_source: inferred
doc_brief: "Tannakian categories of perverse sheaves on abelian varieties — 52 sections: Front matter; Introduction; Some commonly used notations"
---
So far we have mostly ﬁxed a general point x ∈X(C). Now let us see
what happens when this point varies. For the moment the dimension g can
be arbitrary, but as before we always assume that the theta divisor Θ ⊂X is
smooth or has only isolated singularities. To begin with, we put the Hodge
structures V± from section 5.1 into a family as follows.
LEMMA 5.10. Over some Zariski-open dense subset U ⊂X there exists
for each integer n ≥0 a polarized variation of pure Hodge structures Hn
with stalks
Hn
x = Hn(Yx,Q),
and there are subvariations
V+ ⊂Hg−2
and
V−⊂Hg−2
whose stalks are precisely the subspaces V+ and V−deﬁned in section 5.1.
Proof. Consider the Zariski-open dense subset U ⊂X and the smooth
proper family fU : YU −→U from lemma 5.3 and corollary 5.4. We can
then deﬁne
Hn = Rn fU∗(QYU)
for
n ≥0
since for any smooth proper family of complex varieties the direct images
deﬁne variations of Hodge structures whose stalks are the cohomology of
the ﬁbres [103, chapt. III]. It remains to construct the subvariations V±. For
5.2. Variations of Hodge structures
103
this we consider the commutative diagram
YU  
i
/
fU
%J
J
J
J
J
J
J
J
J
J
J
J
U ×X
pU

U
where pU denotes the projection onto the ﬁrst factor and where the closed
immersion i is deﬁned by i(x,y) = (x + y,y), recalling that YU ⊂Θ × Θ by
construction. The adjunction morphism QU×X −→i∗(QYU) deﬁnes in each
degree n ≥0 a morphism
Hn(X,Q)⊗Q QU = RnpU∗(QU×X) −→Rn fU∗(QYU)
of polarized variations of pure Hodge structures, and this morphism induces
on each ﬁbre the restriction morphism that occurs in the weak Lefschetz
theorem. Furthermore, the involution
σ :
U ×X −→U ×X ,
(x,y) 7→(x,x−y)
preserves YU and restricts on each ﬁbre Yx to the involution σx. This being
said, we can perform the constructions from section 5.1 ﬁbre by ﬁbre to
obtain the subvariations V± ⊂Hg−2 with the desired property.
□
As we mentioned in the introduction, one of the principal goals of this
chapter will be the proof of theorem 5.1. We now explain how this will
follow from the results to be discussed in the next sections. Let us for
convenience ﬁrst recall the statement of the theorem.
THEOREM 5.1. For a general complex ppav X of dimension g = 4 the
monodromy group G of the local system V+ is either the Weyl group W(E6)
or its unique simple subgroup of index two which is the kernel of the sign
homomorphism sgn : W(E6) −→{±1}.
Plan of the proof. To begin with, in sections 5.3 and 5.4 we give a
detailed study of the integral cohomology and the N´eron-Severi lattices of
the smooth surfaces Yx = Θ∩Θx and Y +
x = Yx/σx for x ∈U(C). As a result
of the lattice computations it will in particular follow that if we view V+ as
a polarized variation of Z-Hodge structures, then its stalks can be identiﬁed
with the E6-lattice up to a rescaling of the bilinear form. Coming back to
the monodromy group G of the underlying local system, we then deduce in
proposition 5.18 that
G ≤W(E6)
is a subgroup of the Weyl group. Once we have this upper bound, we can
proceed as follows. If equality holds, then we are done. If not, then G must
be contained in some maximal proper subgroup M < W(E6). Now the table
104
Chapter 5 – A family of surfaces
of maximal subgroups in [23, p. 26] shows that any such subgroup M must
be conjugate to one of the following subgroups:
(a) the simple subgroup W +(E6) of index two which is the kernel of
the sign homomorphism sgn : W(E6) −→{±1},
(b) the stabilizer of a line through some minimal vector in the dual
lattice E∗
6 = {v ∈E6 ⊗Z Q | ⟨v,w⟩∈Z ∀w ∈E6},
(c) the stabilizer of a line through some root vector inside E6, with the
symmetric group S6 as a subgroup of index two,
(d) three other subgroups, two of order 24 ·34 and one of order 27 ·39.
Furthermore, any proper subgroup of the simple group in (a) is by the table
of loc. cit. also contained in some of the maximal subgroups described in
cases (b), (c) or (d). So for the proof of theorem 5.1 it will sufﬁce to show
that for a general ppav the monodromy group G cannot be contained in any
of the subgroups listed in (b), (c) and (d).
One tool for this will be the Tannakian formalism of convolution given
in chapters 2 and 3. Indeed, consider the perverse intersection cohomology
sheaf δΘ = CΘ[g −1] ∈Perv(X,C). Over the open dense subset U ⊂X it
turns out that the local system underlying V+ can be identiﬁed with a direct
summand of the convolution
δΘ ∗δΘ ∈Db
c (X,C),
as we will show in section 5.6. Since for a general ppav of dimension g = 4
we know the Tannaka group G(δΘ) = Sp24(C) from theorem 4.2, it will then
follow via the representation theory of the symplectic group that the local
system underlying V+ is irreducible — in other words, the monodromy
group G acts irreducibly on the stalks E6 ⊗Z C of this local system, see
proposition 5.23. Hence G cannot be contained in the stabilizer of a line as
described in the above cases (b) or (c).
The remaining cases cannot be excluded with the same argument, in fact
some of the subgroups in case (d) act irreducibly on E6 ⊗Z C. An example
is given in appendix C. However, a look at the group orders shows that the
maximal subgroups in case (d) do not contain the alternating group A6 as a
subgroup, so the proof of theorem 5.1 will be ﬁnished if we can show that
for a general ppav there exists an embedding
A6 ,→G.
For this we use a degeneration argument to ﬁll in the dotted lines in the
following Hasse diagram, where G(d2) is the Galois group of the difference
5.2. Variations of Hodge structures
105
morphism for a general curve as in theorem 5.2.
W(E6)
G








S6
???????
W +(E6)
G(d2)







A6
AAAAAAAA
More speciﬁcally, in lemma 5.28 we construct over some smooth complex
quasi-projective curve S a principally polarized abelian scheme XS −→S
with a relative theta divisor ΘS ⊂XS such that the following properties are
satisﬁed.
(1) For some point s0 ∈S(C) the ﬁbre Xs0 is the Jacobian variety of
a general curve of genus g = 4, but for all other points s̸ = s0 the
theta divisor Θs ⊂Xs is smooth.
(2) The relative addition morphism f : YS = ΘS ×S ΘS −→XS restricts
to a smooth proper morphism
fUS :
f −1(US) −→US
over some Zariski-open dense subset US ⊂XS that surjects onto S.
We remark that the statement in (2) is nothing but the relative version of
the Bertini-type lemma 5.3. The proof of lemma 5.10 carries over verbatim
to this relative setting, so over the Zariski-open dense subset US ⊂XS we
obtain two variations of Hodge structures
VS+
and
VS−
which on the ﬁbre over each point s ∈S(C) restrict to the variations V±
from lemma 5.10. If for each such point we denote by G(s) the monodromy
group of the local system
VS+|Us
on the ﬁbre
Us ⊂Xs,
then a general result about degenerating monodromy representations, to be
recalled in lemma 5.27 below, says that for general s ∈S(C) we have an
embedding
G(s0) ,→G(s).
So we will be ﬁnished if we can show that the monodromy group G(s0) for
the Jacobian variety Xs0 = JC of a general curve C of genus g = 4 contains
the group A6 as a subgroup. To achieve this we show in proposition 5.24
106
Chapter 5 – A family of surfaces
via the theory of Brill-Noether sheaves that G(s0) coincides with the Galois
group of the difference morphism
d2 :
C2 ×C2 −→Pic0(C),
(D,E) 7→[OC(D−E)]
whereC2 denotes the second symmetric product of the curve, identiﬁed with
the group of effective divisors of degree two. By theorem 5.2 (to be proven
in section 5.8 below) the Galois group G(d2) of this difference morphism
is either the alternating group A6 or the full symmetric group S6. This ﬁlls
in the dotted lines in the above Hasse diagram and thereby completes the
proof of theorem 5.1.
□
