---
doc_id: disssubmission
doc_title: "Tannakian categories of perverse sheaves on abelian varieties"
section_id: sec-002-4-introduction
section_title: "Introduction"
section_number: 4
pages: 12-14
source_pdf: DissSubmission.pdf
source_sha256: 207fd5e3dc0d278d
doc_brief: "Tannakian categories of perverse sheaves on abelian varieties — 121 sections: Acknowledgements; Introduction; Introduction"
---
direct summandδn is a perverse sheaf. Let us say that a perverse sheaf is
a Brill-Noether sheaf if it is a subquotient ofδn for somen∈ N. Then for
a suitable normalization of the Abel-Jacobi morphism, it has been shown
in theorem 14 of loc. cit. that the category of all Brill-Noether sheaves is
equivalent to the category of algebraic representations of the group
G(δC) =
{
Sp2g−2(C) if C is hyperelliptic,
Sl2g−2(C) otherwise,
and that the tensor product of representations is induced by the convolution
product of perverse sheaves. This Tannakian description reduces classical
geometric problems to simple computations in representation theory. For
example, ifg denotes the genus ofC, then the perverse sheafδΘ attached
to the theta divisorΘ = Wg−1⊂ X corresponds via the above equivalence
to the g−1st fundamental representation ofG(δC). Using this one may
decompose the convolutionδΘ∗δΘ into its irreducible constituents, which
leads to a new proof of Torelli’s theorem [111].
Alongside our proof of the vanishing theorem and still based on [68], in
chapter 2 we generalize the Tannakian constructions from above to the case
of semisimple sheaf complexes on arbitrary complex abelian varietiesX. In
particular, we show that every convolution of semisimple perverse sheaves
is a direct sum of a semisimple perverse sheaf and a further sheaf complex
which is negligible in a suitable sense (for example, on a simple abelian
variety a complex is negligible iff all its cohomology sheaves are locally
constant). To any semisimple perverse sheafP∈ Perv(X,C) we then attach
a reductive algebraic groupG(P) whose representation theory governs the
decomposition of the convolution powersP∗n = P∗···∗ P up to negligible
direct summands, see corollary 2.14.
We remark that for algebraic tori in place of abelian varieties, similar
results have been obtained by Gabber and Loeser in [41]. However, in their
case the essential problem is to deﬁne the correct notion of convolution in
the non-proper case, and once this has been done, the required properties
follow from Artin’s vanishing theorem for afﬁne morphisms. By way of
contrast, in the case of abelian varieties the main point of the construction
is to ﬁnd a proper analog of Artin’s theorem, which will be precisely the
vanishing theorem that we stated earlier.
The Tannaka groupsG(P) attached to perverse sheavesP∈ Perv(X,C)
as above form an interesting family of new invariants which contain much
information about the geometry and the moduli of the underlying abelian
variety. So far the most efﬁcient method to determine such Tannaka groups
has been to study degenerations of the abelian variety (an example for this
can be found in chapter 4). Even if one is only interested in semisimple
5
perverse sheaves on abelian varieties, such degenerations naturally lead to
non-semisimple perverse sheaves on semiabelian varieties. In chapter 3 we
extend our Tannakian constructions to this more general case, combining
the results of Gabber and Loeser for tori with our vanishing theorem for
abelian varieties. We also give a Tannakian description for the functor of
nearby cycles for a family of abelian varieties which degenerates into a
semiabelian variety. Even though in the non-proper case the functor of
nearby cycles does not preserve the Euler characteristic, we will show that
the degenerate Tannaka group is a subgroup of the generic one whenever
one can possibly expect this to hold (see theorem 3.15).
In the remaining chapters we study in more detail the case whereP = δΘ
is the perverse intersection cohomology sheaf associated with a symmetric
theta divisor of a principally polarized abelian varietyX. In chapter 4 we
use a degeneration argument to show that for a general principally polarized
abelian variety (ppav) of dimensiong one has
G(δΘ) =
{
SOg!(C) if g is odd,
Spg!(C) if g is even,
and thatδΘ corresponds to the standard representation of this group, a result
that was conjectured in [67]. As an application we deduce that forg =4 the
invariantG(δΘ) solves the Schottky problem in the sense that it detects the
locus of Jacobian varieties inside the moduli spaceA4 of ppav’s.
Once we know the Tannaka groupG(δΘ), we can use representation
theory to decompose arbitrary convolution powers of the perverse sheafδΘ
into their simple constituents. This produces a plethora of interesting simple
perverse sheaves which describe the Hodge theory of various subvarieties
of X. For example, consider the translateΘx = Θ+x of the theta divisor by
a pointx∈ X(C). The geometry of the intersections
Yx = Θ∩Θx
is closely connected with the moduli of the underlying ppav and has been
studied classically in relation with Torelli’s theorem [25], with the Schottky
problem [27] and with the Prym map [61]. The involutionσ =−idX acts
on these intersections, and if the theta divisor is smooth, then for a general
pointx∈ X(C) the quotient variety
Y+
x = Yx/σ
will be smooth as well. We will see in chapter 5 that for varyingx, the
variable part of the cohomologyH•(Y+x ,Q) can be identiﬁed naturally with
the stalk cohomology of the alternating resp. symmetric convolution square
of the perverse sheafδΘ, depending on whether the dimensiong = dim(X)
is even or odd. For a general ppav the Tannakian result of chapter 4 implies
