---
doc_id: disssubmission
doc_title: "Tannakian categories of perverse sheaves on abelian varieties"
section_id: sec-057-43-local-monodromy-75
section_title: "Local monodromy 75"
section_number: 4.3
pages: 83-85
source_pdf: DissSubmission.pdf
source_sha256: 207fd5e3dc0d278d
doc_brief: "Tannakian categories of perverse sheaves on abelian varieties — 121 sections: Acknowledgements; Introduction; Introduction"
---
of all prime numbers other thanp, including our ﬁxed primel. In what
follows we will always assume that the nearby cyclesΨ(δ) are tame in the
sense thatP acts trivially on them (in the application in proposition 4.12
we only work in characteristicp = 0 anyway). The perverse sheafΨ(δ)
is then equipped with a natural action of quotientZl(1) of the tame inertia
group, and we denote byT : Ψ(δ)−→Ψ(δ) the endomorphism induced by
a topological generator 2πi of Zl(1). In the abelian category Perv(Ys,Λ) we
have as in [85, lemma 1.1] a Jordan decomposition
Ψ(δ) = Ψ1(δ)⊕Ψ⁄=1(δ) with Ψ⁄=1(δ) =
⨁
α⁄=1
Ψα(δ),
where for eachα∈ Λ the perverse subsheafΨα(δ) is stable under the action
of T and killed by a power ofT−α·id. We are particularly interested in
the case of the perverse intersection cohomology sheafδ = δYη.
REMARK 4.7. Suppose that the nearby cyclesΨ(δYη) are tame. If
the morphism f : Y→ S is proper and if the geometric generic ﬁbre Yη
is smooth, then after replacing f by its base change under some ﬁnite
branched covering of S we can assume that
H•(Ys,Ψ⁄=1(δYη)) = 0.
Proof. Let S′→ S be the normalization ofS in a ﬁnite extension of
the residue ﬁeld ofη with generic pointη′↦→ η, and denote byS→ S the
normalization in the residue ﬁeld ofη. For the base changesY′ =Y×S S′
andY =Y×S S we then have a commutative diagram
Ys // Y

Yηoo

Y′s // Y′

Y′
η′oo

Ys // Y Yηoo
where the vertical identiﬁcations on the left hand side come from the fact
that we are working over a strictly Henselian base. In particular, as an
object of Perv(Ys,Λ) =Perv(Y′s,Λ) the nearby cyclesΨ(δYη) do not change
if we replace our original familyY→S by the base changeY′→S′, though
of course the local monodromy operation and hence in the tame case the
Jordan decomposition is modiﬁed under this replacement. This being said,
our claim can be checked as follows.
76 Chapter 4 – The Tannaka group of the theta divisor
For eachα∈ Λsome power of the endomorphismT−α·id acts trivially
on the perverse sheafΨα(δYη) and hence also on its hypercohomology. In
particular, the Jordan decomposition
H•(Ys,Ψ(δYη)) =
⨁
α
H•(Ys,Ψα(δYη))
shows thatH•(Ys,Ψ⁄=1(δYη)) = 0 iff the action ofT on H•(Ys,Ψ(δYη)) is
unipotent. But this latter condition can be achieved after a ﬁnite branched
base changeS′→S as above: Indeed we have
H•(Ys,Ψ(δYη)) = H•(Yη,δYη)
by proper base change, and if the geometric generic ﬁbreYη is smooth, then
Grothendieck’s local monodromy theorem [60, th. 1.4] implies that on this
cohomology group the generatorT acts quasi-unipotently. □
Returning to an arbitrary perverse sheafδ∈ P(Yη) with tame nearby
cycles, to get hold onΨ1(δ) we consider the nilpotent operator
N = 1
2πi log(T) : Ψ1(δ)−→ Ψ1(δ)(−1).
Here 1
2πi∈ Zl(−1) denotes the dual of our chosen generator 2πi∈ Zl(1)
so that the morphismN is well-deﬁned and equivariant under the Galois
action. By [28, sect. 1.6] there is a unique ﬁnite increasing ﬁltrationF• of
the perverse sheafΨ1(δ) such that
N(Fi(Ψ1(δ)))⊆ Fi−2(Ψ1(δ))(−1)
and such that for eachi≥ 0 the i-fold iterateNi : Ψ1(δ)−→Ψ1(δ)(−i)
induces an isomorphism
Gri(Ψ1(δ))
∼=−→ Gr−i(Ψ1(δ))(−i)
of the graded pieces with respect to the ﬁltration. Furthermore, if fori≥ 0
we denote byP−i(δ) the kernel ofN : Gr−i(Ψ1(δ))→Gr−i−2(Ψ1(δ))(−1),
then by loc. cit. we have a decomposition
Gr−i(Ψ1(δ)) ∼=
⨁
k≥0
P−i−2k(−k).
We can represent this situation by a diagram of the following shape, where
each horizontal line of the triangle contains the composition factors of the
corresponding graded piece shown on the left (for the arrows labelledN one
must of course ignore the Tate twists in the diagram, which have only been
