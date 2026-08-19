---
doc_id: arxiv-2404.03933v2
doc_title: "TENSOR POWERS OF VECTOR REPRESENTATION OF Uq(sl2) AT EVEN ROOTS OF UNITY"
section_id: sec-000-1-introduction
section_title: "Introduction"
section_number: 1
pages: 1-4
source_pdf: 2404.03933v2.pdf
source_sha256: 48aff6e97e1f1267
doc_brief: "TENSOR POWERS OF VECTOR REPRESENTATION OF Uq(sl2) AT EVEN ROOTS OF UNITY — We study the decomposition of tensor powers of two dimensional irreducible rep- resentations of quantum sl2 at even roots of"
---
2. Algebra Uq(sl2) and its representations 4
3. Decomposition of tensor powers of T (1) over Uq(sl2) 9
4. Restriction from Uq(sl2) to uq(sl2) 11
5. Recursive formulae for Uq(sl2) and uq(sl2) tensor products. 13
6. Multiplicities and lattice paths 14
7. Integral formula for multiplicities 18
8. Probabilistic measures on the tensor product decomposition 21
9. The asymptotic of the character and Plancherel measures for Uq(sl2) 23
10. The asymptotic of probability measures for uq(sl2) 28
Appendix A. Gaussian binomial coefficients 30
Appendix B. Proof of Theorem 6.3 31
Appendix C. Proof of Theorems 9.1, 9.2, 9.3 38
Appendix D. Proof of Theorem 9.4 41
Appendix E. Proof of Theorems 9.5 and 9.6 42
References 43
1. Introduction
1.1. A typical problem in asymptotical representation theory, the subject pioneered by A. M.
Vershik, is the study of infinite sequences of branching rules. For example, if An, n∈ Z>0 is a
1
arXiv:2404.03933v2  [math.RT]  29 Jul 2024
2 ANNA LACHOWSKA, OLGA POSTNOV A, NICOLAI RESHETIKHIN, AND DMITRY SOLOVYEV
sequence of associative algebras, Vn is a sequence of finite dimensional 1 representations of An
and Bn⊂An is a sequence of subalgebras, consider restrictions of Vn to Bn. We have:
Vn|Bn
∼=
M
j

V (j)
Bn
⊕mj (n)
where V (j)
Bn are indecomposable representations of Bn. Natural important problem related to
such a sequence is to find the asymptotic of mj(n) as n→∞ and to find the asymptotic of
the Plancherel measure
pj(n) = mj(n) dimV (j)
n
dimVn
.
For earlier references on the subject see [V], [LS], [K], [B], [TZ].
An important example of such type of problems is when H is a Hopf algebra, An = H⊗n,
Bn =H, ∆(n) :H→H⊗n and Vn =V⊗n where V is a representation of H. When H =U(g)
such problem was studied in [K] for g = sln and V = Cn. It was extended to all simple g with
any irreducible V in [B] [TZ]. The asymptotic of character measures, which is a deformation
family of Plancherel measures was studied in [PR1] [PR2]. In [CEO] a related problem of
finding the asymptotical behavior of bn = P
jm(j)
n in the context of tensor categories was
addressed.
1.2. In this paper we extend the study of statistics of irreducible components in tensor prod-
ucts of finite dimensional representations of simple Lie algebras [K, B, TZ, PR1] to a similar
question about tensor powers ofL(1), the two dimensional irreducible representation ofUq(sl2)
of type 1, whenq is a root of unity.2 In this case representation theory is not semisimple and we
study the statistics of indecomposable submodules in tensor powers of L(1). We consider two
versions of quantum sl2 at a root of unity, Uq(sl2) which is the quantized universal enveloping
of the sl2 with divided powers [Lus89] and its finite dimensional Hopf subalgebra uq(sl2).
The two dimensional irreducible representation ofUq(sl2) is a simplest indecomposable tilting
module. This is why we also use notationT (1) forL(1). Because the category of tilting modules
is a tensor subcategory of the category of finite dimensional representations of Uq(sl2), tensor
powers of T (1) decompose into direct sums of tilting modules. On indecomposable tilting
components of T (1)⊗N there is a natural probability measure, the character measure. It is a
one parametric family of probability measures with the Plancherel measure being a particular
case.
The multiplicities of tilting modules over Uq(sl2) in tensor powers of L(1) also give the
dimensions of simple modules for the corresponding Temperley-Lieb algebras, which can be
considered as endomorphism algebras of tensor powers of L(1) over Uq(sl2), see e.g. [AST],
[ILZ]. We provide a detailed derivation of the multiplicity formulas for the case of Uq(sl2) and
the small quantum group uq(sl2). In the case of the big quantum group Uq(sl2) our result
agrees with the formulas obtained earlier in [And17], where the case of U(sl2) over a field of
positive characteristics and the mixed case are also considered.
1Finite dimensionality is not necessary. For example in [F] similar problem was analyzed for tensor powers
of the fundamental representation of ˆsl2 where all representations are infinite dimensional.
2Throughout the paper we always imply a complex root of unity.
TENSOR POWERS 3
Forq =eiπm
l wherel is odd andm andl are mutually prime, indecomposable tilting modules
ofUq(sl2) of type 1 are parametrized by integers. For such tilting modules we write T (k) with
k =lk1 +k0, m1∈ Z≥0, 0≤k0≤l− 2. For details see Section 2.1. The multiplicities of T (k)
in the decomposition of the tensor power T (1)⊗N
T (1)⊗N =
M
n∈Z≥0
T (n)⊕M (l)
n (N )
are given in Theorem 3.1, see also [And17], Corollary 3.5 . They are also computed in [Sol]
in terms of lattice paths, and as an integral of characters and their duals in Section 7.3. The
character ofT (k) is determined by characters of the Weyl modules(see Section 2.1) and can be
explicitly computed (see Lemma 7.1)
chT (k1l+k0)(x) =



xk0+1−x−(k0+1)
x−x−1 , if 0≤k0≤l− 1 and k1 = 0,
x(k1+1)l−x−(k1+1)l
x−x−1 , if k0 =l− 1 and k1∈ Z>0,
(xk0+1 +x−(k0+1))xk1l−x−k1l
x−x−1 , if 0≤k0≤l− 2 and k1∈ Z>0.
Whenx> 0 all these characters are positive and we have the character probability measure on
indecomposable tilting components with the probability of module T (n) occurring in T (1)⊗N
being
(1) p(l)
N (k;x) = M (l)
k (N)chT (k)(x)
(chT (1)(x))N .
In Theorem 9.2 we prove the weak convergence of (1) to the tensor product p1(•;t)⊗p2(•;t),
where t = lnx, p2 is the Gaussian measure on R with the density
p2(α;t) =
r
l
2π cosh(t)e−α2l
2 (cosh(t))2
, α ∈ R
and p1 is the discrete probability measure on k0 = 0, 1,...,l − 1 with
p1(k0;t) =
( (et(k0+1)+e−t(k0+1))(et(l−1−k0)−e−t(l−1−k0))
l(etl−e−tl) , if k0 = 0,...,l − 2,
1
l, if k0 =l− 1.
Note that this tensor product of distributions is reminiscent to the tensor product formula for
tilting modules from Theorem 2.11. We use it indirectly in the proof of Theorem 7.1. We
expect a more direct use of Theorem 2.11 in the derivation of the weak limit of the character
measure based on Markov processes.
We also compute the intermediate scaling of the character measure(near Plancherel behavior
of the character measure), when N→∞ , t→ 0 such that t
√
N is finite. And we compute the
limit when N,t →∞ such that θ =Ne−2t is finite, which corresponds to the critical drift. In
the latter case the limit probability measure is geometric in the variable s = N−k
2 .
The character and, as a consequence, the Plancherel measure are special: they are given by
running certain Markov process N times. This Markov process is determined by the decompo-
sition of T (1)⊗T (k). This gives another way to compute the limit of the character measure.
We do this for the Plancherel measures for the small quantum sl2, for uq(sl2) in Section 10.2.
Markov process derivation of the limit of the character measure will be done in a separate
publication.
4 ANNA LACHOWSKA, OLGA POSTNOV A, NICOLAI RESHETIKHIN, AND DMITRY SOLOVYEV
In this paper we focused on Uq(sl2) and uq(sl2). The extension of these results to other
simple Lie algebras and superalgebras involves regular values of coefficients of Kazhdan-Lusztig
polynomials and will be done in a separate publication. Following the classical framework via a
suitable version of Schur-Weyl duality this study should have implications for the representation
theory of Hecke and Brauer algebras, as outlined in e.g. [AST].
1.3. The paper is organized as follows. In Section 2 we review basic facts about quantized
universal enveloping algebra Uq(sl2) at even roots of unity. In Section 3 we derive formula
for multiplicities of tilting modules in decomposition of T (1)⊗N overUq(sl2). In Section 4 we
do this for the small quantum group uq(sl2). In Section 5 we give recursive description of
the multiplicities. In Section 6 we describe multiplicity functions in terms of path counting
formulae for lattice path models, defined by the given recursive description. In Section 7 we
obtain formulae for multiplicities over Uq(sl2) by means of an integral of characters and their
duals.
In the remaining sections we study the asymptotic of multiplicities and asymptotic of dis-
tributions of tilting modules in T (1)⊗N in the N→∞ limit. In Section 8 we define proba-
bilistic measures on indecomposable components in tensor product decomposition of T (1)⊗N
overUq(sl2) and over uq(sl2). For the case Uq(sl2) we consider the character measure and the
Plancherel measure, for the caseuq(sl2) we consider the Plancherel and the quantum Plancherel
measures. In Section 9 we derive asymptotic of character and Plancherel measures for Uq(sl2).
We consider asymptotics in the bulk, the critical drift and the intermediate scaling. In Section
10 we use Markov processes associated with tensor products to derive asymptotic of Plancherel
and quantum Plancherel measures for uq(sl2). In Appendices B, C, D, E we give proofs of the
main statements.
1.4. Acknowledgements. The authors are grateful to V. Serganova, P. Shan and H. H. An-
dersen for inspiring discussions. At earlier stages of this work we enjoyed discussions with A.
M. Vershik. This work was supported by Leonhard Euler International Mathematical Insti-
tute (agreement no.075-15-2022-289 date 06/04/2022). The work of O.P., N.R. and D.S. was
supported by the the RSF grant 21-11-00141. The work of N.R. was also supported by the
Collaboration Grant ”Categorical Symmetries” from the Simons Foundation, by the grant, by
the grant BMSTC and ACZSP (Grant no. Z221100002722017) and by the Changjiang fund.
The work of D.S. was supported by the Xing Hua Scholarship program of Tsinghua University.
