---
doc_id: arxiv-2502.02662v1
doc_title: "The String Dual to Two-dimensional Yang-Mills Theory Revisited"
section_id: sec-003-the-extended-hurwitz-theory
section_title: "The Extended Hurwitz Theory"
section_number: null
pages: 4-6
source_pdf: 2502.02662v1.pdf
source_sha256: 3f87983ce379a8d6
doc_brief: "The String Dual to Two-dimensional Yang-Mills Theory Revisited — We propose that chiral two-dimensional Yang-Mills theory on a Riemann surface X is dual to a deformed stationary subsector of the"
---
In the context of the string description of two-dimensional Yang-Mills theory, one needs to sum
over covering maps of all degrees d [2, 3]. This motivates the introduction of an overarching
grand canonical version of the Hurwitz theories with gauge groups Sd that takes into account
1Alternatively, it is the topological symmetric orbifold of a trivial theory, which contains only the identity
operator.
3
coverings of all degrees simultaneously [9, 10, 15]. 2 In the process, we move from a two-
dimensional Dijkgraaf-Witten theory with a finite gauge group to a topological quantum field
theory defined by a Frobenius algebra only. To treat all degreesd simultaneously, we introduce
an operator algebra which is the algebra of orbits of partial permutations A∞ of an infinite
set [10, 15]. We provide a brief review of partial permutations here and refer the reader
to [10,15] for more details.
A partial permutation is a pair ( d,ρ ), where d is a subset of N and ρ is a permutation of
elements in d. We refer to d as the support of the partial permutation. 3 An element σ of the
symmetric group S∞ acts on partial permutations as
σ· (d,ρ ) = (σ(d),σρσ−1). (2.5)
The orbits Ar of the algebra of partial permutations A∞ under this action are of the form
Ar =
X
(d,ρ)∈[r]
(d,ρ ), (2.6)
where [r] denotes an orbit of partial permutations that is indexed by partitions of integers. The
product of partial permutations is defined by concatenating their supports and multiplying
their permutations
(d1,ρ 1)· (d2,ρ 2) = (d1∪d2,ρ 1ρ2). (2.7)
The product of orbits is defined accordingly. Once the algebra is fixed, we only further need to
define the one-point functions on the algebra of partial permutations A∞ to fix all correlation
functions. To that end, we first introduce a fixed-degree one-point function on a Riemann
surface of genus G:
⟨Ar⟩d,G :=
m1(ρ)
m1(r)

⟨Cρ⟩d,G, (2.8)
where ρ denotes the permutation obtained by trivially completing the partial permutation
r and m1(r) (respectively m1(ρ)) is the number of inert entries of the partial permutation
(respectively permutation). Note that m1(ρ)−m1(r) =d−|dr|, where dr is the support of a
partial permutation in the orbit Ar. The definition (2.8) is valid for |dr|<d . For|dr|>d , we
set⟨Ar⟩d,G = 0. We now define the physical one-point function as
⟨Ar⟩G =
X
d
pd⟨Ar⟩d,G. (2.9)
Importantly, our grand canonical formulation of a Hurwitz theory allows for the introduction
of a chemical potentialp which explicitly keeps track of the degree of the maps that contribute
to a given correlator. The sum over degrees can be traded for a sum over the genus of the
covering surface by using the Riemann-Hurwitz formula. Let us study this for the example
of partial permutations r that consist of a single cycle k. The correlation functions of the
2This is a first essential supplementary tool that will distinguish our treatment of two-dimensional Yang-
Mills theory from those in the literature.
3For a given cover, the set d labels the sheets of the cover. The permutation codes a reshuffling of sheets
due to ramification. Some sheets may not be shuffled.
4
grand canonical symmetric orbifold theory on a Riemann surface of genus G are then shown
to exhibit the structure of string correlators
⟨Ak1··· Akn⟩G =
X
g
g2g−2
s ⟨g−k1+1
s Ak1··· g−kn+1
s Akn⟩g,G (2.10)
provided that we make the identification p = g2G−2
s and that we define normalized partial
permutations A′
r := g|dr|
s Ar.4 This observation is consistent with the behavior of a general
symmetric orbifold theory on the sphere [16]. With this normalization, the generic correlation
function becomes
⟨A′
r1··· A′
rn⟩ =
X
g
g2g−2
s ⟨gℓ(r1)
s Ar1··· gℓ(rn)
s Arn⟩g, (2.11)
where the length l(r) of a partial permutation r counts the number of parts in the partition
[r] of|dr|.
