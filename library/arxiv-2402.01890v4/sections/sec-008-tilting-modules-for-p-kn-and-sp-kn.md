---
doc_id: arxiv-2402.01890v4
doc_title: "On the spherical partition algebra"
section_id: sec-008-tilting-modules-for-p-kn-and-sp-kn
section_title: "Tilting modules for P k(n) and SP k(n)"
section_number: null
pages: 24-27
source_pdf: 2402.01890v4.pdf
source_sha256: e1eeb2865f0b53e1
toc_source: outline
doc_brief: "On the spherical partition algebra — For k ∈N we introduce an idempotent subalgebra, the spherical partition algebra SPk, of the partition algebra Pk, that we define using an embedding associated"
---
We already saw that Pk(n) are quasi-hereditary algebras when n̸ = 0 and therefore, in particular, they are endowed
with families of tilting modules, see the appendix to [15]. In this section we take the opportunity to describe the
structure of these tilting modules, using standard arguments from the theory of quasi-hereditary algebras. We
observe that the same arguments also provide us with a description of the tilting modules for SPk(n).
We assume n ∈{1, 2, . . . , 2k −2} in which case Pk(n), as we already saw, is non-semisimple quasi-hereditary on
the poset Λk defined in (7.4). Correspondingly, the category Pk(n)-mod of finite dimensional Pk(n)-modules is a
highest weight category where the standard modules {∆k(λ) | λ ∈Λk} are as described in the paragraphs between
(7.7) and (7.9) and the irreducible modules {Lk(λ) | λ ∈Λk} as described in c) of Theorem 18.
Pk(n)-mod is equipped with a duality M 7→M ∗via M ∗= HomC(M, C) where the Pk(n)-structure on M ∗is
given by
af(m) = f(a∗m) for a ∈Pk(n), f ∈M ∗, m ∈M
(9.1)
for a 7→a∗the anti-automorphism coming from the cellular structure on Pk(n). Note that the Lk(λ)’s are self dual
Lk(λ) = Lk(λ)∗via
Lk(λ) →Lk(λ)∗, v 7→⟨·, v⟩λ.
(9.2)
The costandard modules {∇k(λ) | λ ∈Λk} for Pk(n) are defined by ∇k(λ) = ∆k(λ)∗.
The following definitions and results are part of the general theory of quasi-hereditary algebras. Let Fk(∆) be
the subcategory of Pk(n)-modules whose objects have ∆-filtrations, in other words, a Pk(n)-module M belongs to
Fk(∆) if there is a filtration of Pk(n)-modules 0 ⊂M1 ⊂M2 ⊂. . . ⊂Mr = M such that for each i = 1, 2, . . . , r
there is a λi ∈Λk such that Mi/Mi−1 = ∆k(λi). We define Fk(∇) in a similar way, that is M ∈Fk(∇) if and only
if M ∗∈Fk(∆).
For λ ∈Λk we let Pk(λ) be the projective cover of Lk(λ) in Pk(n)-mod. Then Pk(λ) ∈Fk(∆) and for any
∆-filtration 0 ⊂M1 ⊂M2 ⊂. . . ⊂Mr−1 ⊂Mr = Pk(λ) with Mi/Mi−1 = ∆k(λi) we have λr = λ whereas λj ▷λ
for j < r. For M ∈Fk(∆) we define (M : ∆k(λ)) = dim HomPk(n)(M, ∇k(λ)) which is the number of times ∆k(λ)
occurs as a subfactor in a ∆-filtration of M. We then have the Brauer-Humphreys reciprocity formula
(Pk(λ) : ∆k(µ)) = [∆k(µ) : Lk(λ)] for λ, µ ∈Λk
(9.3)
where [∆k(µ) : Lk(λ)] denotes decomposition number multiplicity.
For λ ∈Λk we let Pk(n)-mod≤λ be the subcategory of Pk(n)-mod consisting of modules with composition
factors in {Lk(µ) | µ ⊴λ}. Then Pk(n)-mod≤λ is a highest weight category with standard modules {∆k(µ) | µ ⊴λ}
and costandard modules {∇k(µ) | µ ⊴λ} and so we deduce from the description of projective covers that ∆k(λ) is
the projective cover of Lk(λ) in Pk(n)-mod≤λ. If µ ◁λ we then get from b) of Theorem 18 and Proposition A3.3
in [15] that
dim Ext1
Pk(n)-mod(Lk(λ), Lk(µ)) = dim Ext1
Pk(n)-mod
≤λ(Lk(λ), Lk(µ)) =
 1
if (λ, µ) is an n-pair
0
otherwise
(9.4)
and if λ ◁µ we get
dim Ext1
Pk(n)-mod(Lk(λ), Lk(µ)) = dim Ext1
Pk(n)-mod(Lk(µ)∗, Lk(λ)∗) =

1
if (µ, λ) is an n-pair
0
otherwise
(9.5)
since Lk(µ)∗= Lk(µ) and Lk(λ)∗= Lk(λ).
We now fix a chain of partitions C = {λ1, λ2, . . . , λp} in Λk such that (λi, λi+1) is an n-pair for i = 1, 2, . . . , p−1.
Suppose furthermore that the chain is maximal in both directions, in other words there is no µ ∈Λk such that
(µ, λ1) is an n-pair or such that (λp, µ) is an n-pair. By Lemma 17, each λ ∈Λk belongs to a unique such maximal
chain C. Defining
Pk(n)-modC = {M ∈Pk(n)-mod | [M : Lk(λ)]̸ = 0 =⇒λ ∈C}
(9.6)
we get from (9.4) and (9.5) that Pk(n) = ⊕CPk(n)-modC is the block decomposition of Pk(n)-mod where C runs
over maximal chains in the above sense.
A Pk(n)-module T is called a tilting module if T ∈Fk(∆) ∩Fk(∇). For each λ ∈Λk there exists a unique
indecomposable tilting module Tk(λ) satisfying [Tk(λ) : Lk(λ)] = 1 and that [Tk(λ) : Lk(µ)]̸ = 0 =⇒µ ⊴λ. Each
tilting module T is a direct sum of such Tk(λ)’s.
Part a) of the following Theorem was obtained already in [33], but still we include it for completeness.
Theorem 21. With the above notation, we have the following results.
a) If j = 2, 3, . . . , p −1 then the Loewy structure for Pk(λj) is as follows
Pk(λj) = Lk(λj−1)
Lk(λj+1)
Lk(λj)
Lk(λj) .
(9.7)
b) If j = 1 then the Loewy structure for Pk(λ1) is as follows
Pk(λ1) =
∆k(λ1) =
Lk(λ1)
Lk(λ2) .
(9.8)
c) If j = p then the Loewy structure for Pk(λp) is as follows
Pk(λp)
=
Lk(λp)
Lk(λp−1)
Lk(λp) .
(9.9)
Proof:
To prove a) we first observe that b) of Theorem 18 together with (9.3) imply that (Pk(λj) : ∆k(λi)) = 1
for j = i or j = i + 1 and otherwise (Pk(λj) : ∆k(λi)) = 0.
Therefore there are two ∆-factors in the ∆-
filtration for Pk(λj), namely ∆k(λj) and ∆k(λj−1). On the other hand, defining Qk(λ) = ker(Pk(λ) →Lk(λ))
we get from (9.4) and (9.5) that dim HomPk(n)(Qk(λj), Lk(λi)) = 1 if i = j −1 or i = j + 1 and otherwise
dim HomPk(n)(Qk(λj), Lk(λi)) = 0. Hence the Loewy structure for Pk(λj) must be as indicated in a).
To prove b) we once again use Theorem 18 and (9.3), but this time we find that ∆k(λ1) is the only ∆-factor of
Pk(λ1), which shows b).
Finally, to show c) we first note that b) of Theorem 18 gives ∆k(λp) = Lk(λp). Since Pk(λp) has ∆-factors
∆k(λp) and ∆k(λp−1), as one sees from Theorem 18 and (9.3), the structure of Pk(λp) must be the one indicated
in c). This proves the Theorem.
□
We now get the following Theorem, describing the indecomposable tilting modules for Pk(n).
Theorem 22. The tilting module Tk(λi) for i = 1, 2, . . . , p are given by the following.
a) If j = 1, 2, . . . , p −1 then Tk(λj) = Pk(λj+1).
b) Tk(λp) = ∆k(λp).
Proof:
The modules in a) are described in a) and c) of Theorem 21. They are self-dual and therefore tilting
modules. The missing tilting module is Tk(λp) = ∆k(λp), given in b).
□
We finally mention that there are versions of Theorem 21 and Theorem 22 for SPk(n) instead of Pk(n). In view
of Theorem 20 the statements and proofs are here exactly the same as for Theorem 21 and Theorem 22.
References
[1] F. Aicardi, J. Juyumaya, Markov trace on the algebra of braids and ties, Mosc. Math. J. 16, No. 3, (2016),
397-431.
[2] D. Arcis, J. Espinoza, Tied-boxed algebras, arXiv:2312.04844.
[3] F. C. Auluck, On partitions of bipartite numbers, Proc. Cambridge Philos. Soc. 49, (1953), 72-83.
[4] A. C. Aitken, On induced permutation matrices and the symmetric group, Proc. Edinburgh Math. Soc. 5, No.
1, (1936), 1-13.
[5] E. Banjo, The generic representation theory of the Juyumaya algebra of braids and ties, Algebr. Represent.
Theory 16, No. 5, (2013), 1385-1395.
[6] G. Benkart, T. Halverson, Partition algebras Pk(n) with 2k > n and the fundamental theorems of invariant
theory for the symmetric group Sn, J. Lond. Math. Soc. 99(2), (2019), 194–224.
[7] G. Benkart, T. Halverson, N. Harman, Dimensions of irreducible modules for partition algebras and tensor
power multiplicities for symmetric and alternating groups, J. Algebr. Comb. 46, (2017), 77–108.
[8] C. Bowman, S. Doty, S. Martin, Integral Schur-Weyl duality for partition algebras, Algebr. Comb. 5, No. 2,
(2022), 371-399.
[9] C. Bowman, M. De Visscher, O. King, The blocks of the partition algebra in positive characteristic, Algebr.
Represent. Theory 18, No. 5, (2015), 1357-1388.
[10] C. Bowman, M. De Visscher, R. Orellana, The partition algebra and the Kronecker coefficients, Trans. Amer.
Math. Soc. 367 (2015), no. 5, 3647–3667.
[11] J. M. Campbell, Alternating submodules for partition algebras, rook algebras, and rook-Brauer algebras, J. Pure
Appl. Algebra 228, No. 1 (2024), 107452.
[12] T. Ceccherini-Silberstein, F. Scarabotti, F. Tolli, Representation theory of the symmetric groups: the Ok-
ounkov–Vershik approach, character formulas, and the partition algebras, Cambridge Studies in Advanced
Mathematics, 121, (2010).
[13] J. Comes, V. Ostrik, On blocks of Deligne’s category Rep(St), Adv. Math. 226, No. 2, (2011), 1331-1377.
[14] Z. Daugherty, R. Orellana, The quasi-partition algebra, J. Algebra 404, (2014), 124-151.
[15] S. Donkin, The q-Schur algebra, London Mathematical Society Lecture Note Series 253, Cambridge: Cambridge
University Press. x, (1998), 179 pages.
[16] S. Donkin, Cellularity of endomorphism algebras of Young permutation modules, J. Algebra 572, (2021), 36-59.
[17] S. Donkin, Double centralisers and annihilator ideals of Young permutation modules, J. Algebra 591, (2022),
249-288.
[18] W. F Doran IV, D. B. Wales, The partition algebra revisited, Journal of Algebra 231, (2000), 265-330.
[19] J. Espinoza, S. Ryom-Hansen, Cell structures for the Yokonuma-Hecke algebra and the algebra of braids and
ties, J. Pure Appl. Algebra 222, No. 11, (2018), 3675-3720.
[20] T. Halverson, A. Ram, Partition algebras, Eur. J. Comb. 26, No. 6, (2005), 869-921.
[21] V. F. R. Jones, The Potts model and the symmetric group, in Subfactors: Proceedings of the Taniguchi
symposium on operator algebras, (Kyuzeso, 1993), World Sci. Publishing, River Edge, NJ, (1994), 259–267.
[22] J. J. Graham, G. I. Lehrer, Cellular algebras, Inventiones Mathematicae 123, (1996), 1-34.
[23] A. M. Garsia, I. Gessel, Permutation statistics and partitions, Adv. in Math. 31(3), (1979), 288–305.
[24] M. Haiman, Combinatorics, symmetric functions, and Hilbert schemes, Jerison, David (ed.) et al., Current
developments in mathematics, 2002. Proceedings of the joint seminar by MIT and Harvard, Cambridge, MA,
2002. Somerville, MA: International Press, 39-111, (2003).
[25] N. Harman, Representations of monomial matrices and restriction from GLn to Sn, arXiv:1804.04702.
[26] G. D. James, The representation theory of the symmetric groups, Lecture Notes in Mathematics 682, Edited
by A. Dold and B. Eckman, Springer Verlag, Berlin Heidelberg New York, 1978.
[27] S. K¨onig, C. C. Xi, On the structure of cellular algebras, Proceedings of ICRA VIII, Canadian Mathematical
Society Conference Proceedings 24 (Canadian Mathematical Society, Ottawa, 1998), 365–385.
[28] S. K¨onig, C. C. Xi, When is a cellular algebra quasi-hereditary?, Mathematische Annalen 315, (1999), 281-293.
[29] S. Lang, Algebra, Graduate Texts in Mathematics 211, Springer-Verlag New York, 3rd ed., (2002), 934 pages.
[30] P. A. Macmahon, Combinatory analysis, Vol. 1. Cambridge Univ. Press, Cambridge, England, (1916).
[31] I. G. Macdonald, Symmetric functions and Hall polynomials, Oxford University Press, second edition, (1995),
475 pages.
[32] P. Martin, Potts models and related problems in statistical mechanics, Series on Advances in Statistical Me-
chanics, 5. Singapore etc.: World Scientific. xiii, (1991), 344 pages.
[33] P. Martin, The structure of the partition algebras, Journal of Algebra 183, (1996), 319-358.
[34] P. Martin, The partition algebra and the Potts model transfer matrix spectrum in high dimensions, J. Phys. A:
Math. Gen. 33, 3669, (2000).
[35] P. Martin, G. Rollet, The Potts model representation and a Robinson-Schensted correspondence for the partition
algebra, Compositio Math. 112, (1998), 237–254.
[36] P. Martin, D. Woodcock, The partition algebras and a new deformation of the Schur algebras, J. Algebra 203,
No. 1, (1998), 91-124.
[37] P. Martin, D. Woodcock, On central idempotents in the partition algebra, J. Algebra 217, No. 1, (1999),
156-169.
[38] A. Mathas, Hecke algebras and Schur algebras of the symmetric group, Univ. Lecture Notes 15, A.M.S., Prov-
idence, R.I., 1999.
[39] G. E. Murphy, The representations of Hecke algebras of type An, Journal of Algebra 173, (1995), 97-121.
[40] S. Narayanan, D. Paul, S. Srivastava, The multiset partition algebra, Isr. J. Math. 255, No. 1, (2023), 453-500.
[41] R. Orellana, M. Zabrocki, Symmetric group characters as symmetric functions, Adv. Math. 390, (2021), 34
pages.
[42] R. Orellana, M. Zabrocki, Howe duality of the symmetric group and a multiset partition algebra, Commun.
Algebra 51, No. 1, (2023), 393-413.
[43] R. Rouquier, Representations of rational Cherednik algebras, Berman, Stephen (ed.) et al., Infinite-dimensional
aspects of representation theory and applications. International conference on infinite-dimensional aspects of
representation theory and applications, Charlottesville, VA, USA, May 18–22, 2004. Providence, RI: American
Mathematical Society (AMS). Contemp. Math. 392, (2005), 103-131.
[44] I. Schur, ¨Uber die rationalen Darstellungen der allgeimeinen linearen Gruppe, (1927), Gesammelte Abhandlun-
gen, Band III (German), herausgegeben von Alfred Brauer und Hans Rohrbach, Springer-Verlag, Berlin/New
York, 1973.
[45] T. Scrimshaw, Cellular subalgebras of the partition algebra, J. Comb. Algebra, (2023), published online first.
[46] R. Stanley, Enumerate combinatorics, Volume 2, Cambridge University Press, (1999), pages 1-585.
[47] S. Ryom-Hansen, On the representation theory of an algebra of braids and ties, J. Algebr. Comb. 33, No. 1,
(2011), 57-79.
[48] S. Ryom-Hansen, On the annihilator ideal in the bt-algebra of tensor space, J. Pure Appl. Algebra 226, No. 8,
(2000), 24 pages.
[49] J-Y. Thibon, The inner plethysm of symmetric functions and some of its applications, Bayreuther Mathema-
tische Schriften 40, (1992), 177-201.
[50] A. Wilson, A diagram-like basis for the multiset partition algebra, arXiv:2307.01353.
[51] H. Weyl, The classical groups, their invariants and representations, Princeton Mathematical Series. No. 1.
Princeton: Princeton University Press, London, Humphrey Milford, Oxford: University Press. xii, (1939), 302
pages.
[52] C. Xi, Partition algebras are cellular, Compositio Math. 119, (1999), 99–109.
