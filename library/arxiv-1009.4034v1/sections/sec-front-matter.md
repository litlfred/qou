---
doc_id: arxiv-1009.4034v1
doc_title: "KEROV’S CENTRAL LIMIT THEOREM FOR SCHUR-WEYL MEASURES OF PARAMETER α = 1/2"
section_id: sec-front-matter
section_title: "Front matter"
section_number: null
pages: 1-5
source_pdf: 1009.4034v1.pdf
source_sha256: 8f8d6d786b60c279
toc_source: outline
---
KEROV’S CENTRAL LIMIT THEOREM FOR SCHUR-WEYL
MEASURES OF PARAMETER α = 1/2
PIERRE-LOÏC MÉLIOT
Abstract. In this article, we show that Kerov’s central limit theorem related to the ﬂuctuations of
Young diagrams under the Plancherel measure extends to the case of Schur-Weyl measures, which are
the probability measures on partitions associated to the representations of the symmetric groups Sn on
tensor products of vector spaces V ⊗n (see [Bia01]). The proof is inspired by the one given in [IO02] for
the Plancherel measure, and it relies on the combinatorics of the algebra of observables of diagrams; we
shall also use Śniady’s theory of cumulants of observables (cf. [Ś06]).
Given a ﬁnite group G and a ﬁnite-dimensional complex linear representation V of G, the decomposition
in irreducible components V = L
λ∈b
G mλ Vλ yields a probability measure on the set bG of isomorphism
classes of irreducible representations of G:
PV
h
λ ∈bG
i
= mλ dim Vλ
dim V
In particular, when G = Sn is the symmetric group of permutations of [[1, n]], a reducible representation of
Sn yields a probability measure on the set Pn = bSn of integer partitions of size n. When V = CSn is the
(left) regular representation, one obtains the so-called Plancherel measure, which has been extensively
studied in the n →∞asymptotic; see for instance [IO02].
In this paper, we focus on the Schur-
Weyl measures that correspond to the representations (CN)n ↶Sn, where Sn acts on the right by
permutation of the letters of the simple tensors:
(v1 ⊗v2 ⊗· · · ⊗vn) · σ = vσ(1) ⊗vσ(2) ⊗· · · ⊗vσ(n)
By Schur-Weyl reciprocity, the probability measure on partitions associated to this representation is
also a probability measure on irreducible representations of GL(N, C). The ﬁrst order asymptotic of
these measures when n1/2 ≃cN and n goes to inﬁnity has been determined by P. Biane in [Bia01]; we
shall recall this in §1, and by using the Robinson-Schensted-Knuth correspondence, we will also give a
“combinatorial model” for these probability measures.
The asymptotics of the Plancherel measures on partitions correspond to the case c = 0, and for
Plancherel measures, S. Kerov has shown that Young diagrams deviate from their limit shape by a
(generalized) gaussian process ([Ker93], [IO02]). Consequently, it was natural to ask whether such a
result extends to the case of Schur-Weyl measures with parameter c > 0. We have found out that it is
indeed the case, and that the central limit theorem for Schur-Weyl measures is up to a translation on
the x-axis the same as for Plancherel measures. This is the main result of this paper, see Theorem 14
in §6. Notice that our result is the “Schur-Weyl dual” of a result of Lytova and Pastur related to the
deviation of the empirical spectral measure of Wishart matrices from the Marčenko-Pastur distribution,
cf. [LP09]. In order to prove Theorem 14, we shall follow the approach of V. Ivanov and G. Olshanski
([IO02]), and we shall therefore use the algebra O of observables of diagrams. These objects are in
some sense “polynomial functions on partitions” (see [KO94]), and in the setting of random partitions,
their expectations play the same role as the moments for real or complex random variables. Moreover, P.
Śniady has developed in [Ś06] a theory of cumulants of observables of diagrams that allow to prove
results of gaussian concentration. These facts are recalled in §2 and §4, and we will also compute certain
observables of the limit shapes Ωc of the Young diagrams under Schur-Weyl measures with parameters
α = 1/2, c > 0, cf. §3.
1
arXiv:1009.4034v1  [math.RT]  21 Sep 2010
2
PIERRE-LOÏC MÉLIOT
The core of the proof of our central limit theorem is contained in §5, and it is shown that Chebyshev
polynomials of the second kind yield random variables related to the second order asymptotic of the
Schur-Weyl measures, and that are asymptotically centered independant gaussian variables. Our proof
is slightly diﬀerent from the one given in [IO02, §7] for Plancherel measures, because in the setting of
Schur-Weyl measures, one cannot use the so-called Kerov degree on observables.
Hence, one has to
use instead the weight ﬁltration on observables, and the arguments of Ivanov and Olshanski that relie
on Kerov’s degree will be replaced by a somewhat nasty trick, see Lemma 12. Thus, our calculations
present quite miraculous simpliﬁcations, and these simpliﬁcations can be summarized by the following
fact: Chebyshev polynomials of the second kind do play a hidden and nethertheless prominent role in the
combinatorics of observables of diagrams. We ought to say that we do not understand completely the
reasons of the universality of Kerov’s central limit theorem; in this paper, we only show that calculations
can be performed in a more general setting than previously known, but as for now we do not know why.
1. Schur-Weyl measures of parameter α = 1/2
In the following, we ﬁx two positive real numbers α and c. Recall that the irreducible representations
of the symmetric group Sn are labelled by partitions of size n, that is to say, non-increasing sequences
λ = (λ1, . . . , λr)
of positive integers that sum up to n; see for instance [Wey39, Chapter 4]. Such a sequence can be
represented by its Young diagram, which is an array of n boxes with λ1 boxes in the ﬁrst line, λ2 boxes
in the second line, etc.
Figure 1. The Young diagram of the partition λ = (7, 5, 2, 2, 1).
We denote by Pn the set of integer partitions of size n, and if λ = (λ1, . . . , λr) is in Pn, we set |λ| = n
and ℓ(λ) = r. We also denote by dim λ = dim Vλ the dimension of the irreducible representation of Sn of
label λ; this dimension can be computed by using the hook length formula, cf. [Mac95, Chapter 1, §7].
Alternatively, by using the branching rules for the irreducible representations of the symmetric groups
Sn, it is easy to show that
dim λ = card

standard tableaux of shape λ
	
.
Here, a standard tableau of shape λ is a numbering of the cases of the Young diagram of λ by the
integers 1, 2, . . . , n, such that each row and each column is strictly increasing.
Example. The ﬁve standard tableaux of shape (3, 2) are drawn in ﬁgure 2. Hence, dim(3, 2) = 5.
4 5
1 2 3
3 5
1 2 4
3 4
1 2 5
2 5
1 3 4
2 4
1 3 5
Figure 2. The standard tableaux of shape (3, 2).
KEROV’S CENTRAL LIMIT THEOREM FOR SCHUR-WEYL MEASURES
3
The Schur-Weyl measure of parameters α and c on partitions of size n is the probability measure
on Pn deﬁned by:
SWn,α,c[λ] = mλ dim λ
N n
where nα ≃cN and the multiplicities mλ are the one coming from the decomposition of the (right-side)
representation (CN)⊗n ↶Sn. Of course, these probability measures depend on the exact sizes N, but
for the asymptotic analysis, we shall see that the parameters α and c are suﬃcient.
The general linear group GL(N, C) acts on the left of the tensor product V = (CN)⊗n by
g · (v1 ⊗v2 ⊗· · · ⊗vn) = g(v1) ⊗g(v2) ⊗· · · ⊗g(vn),
and it is well-known that the algebras generated by the actions of GL(N, C) and Sn in End(V ) are full
mutual centralizers — this is the Schur-Weyl duality phenomenon, see [Wey39, Chapter 4]. Hence, V
can be decomposed as a direct sum of irreducible (GL(N, C), Sn)-bimodules:
GL(N,C)↷

(CN)⊗n	
↶Sn =
M
λ
GL(N,C)↷{Mλ} ⊗C {Vλ}↶Sn
The irreducible algebraic representations of GL(N, C) are labelled by the sequences λ = (λ1, . . . , λN) of
non-negative integers, and consequently, the Schur-Weyl measure charges only the partitions of length
ℓ(λ) ≤N; moreover, mλ = dim Mλ. These dimensions can be given a combinatorial interpretation similar
to the one for the dim Vλ’s, see [Mac95, Appendix A, §8]. Hence,
dim Mλ = card

semistandard tableaux of shape λ with entries in [[1, N]]
	
,
where a semistandard tableau of shape λ is a numbering of the cases of the Young diagram of λ that
is non-decreasing along the rows and strictly increasing along the columns.
Example. The two semistandard tableaux of shape (3, 2) and entries in [[1, 2]] are drawn in ﬁgure 3. As
a consequence, the dimension of the GL(2, C)-module M3,2 is 2.
2 2
1 1 1
2 2
1 1 2
Figure 3. The semistandard tableaux of shape (3, 2) and entries in [[1, 2]].
Given a word of length n over the alphabet [[1, N]], one can associate to it two tableaux of size n and
same shape by using the Robinson-Schensted-Knuth algorithm, see [Ful97]. For instance, when
n = 9 and N = 5, the word m = 233154243 is associated to the two tableaux
5
2 3 4
1 2 3 3 4
and
7
4 6 9
1 2 3 5 8 .
The ﬁrst tableau is semistandard with entries in [[1, N]], and can be obtained by applying the jeu de
taquin algorithm to the ribbon of the word m; the second tableau is always a standard tableau. Hence,
there is a bijection
RSK :

words of length n over [[1, N]]
	
→
G
λ∈Pn
ST (λ) × SST (λ, N),
and if one reminds only the shape RSKsh(m) of the tableaux associated to a word m by RSK, then the
Schur-Weyl measure is precisely the image of the uniform law on N n by the map RSKsh. Hence, one
obtains a combinatorial model for the measures SWn,α,c, and moreover, it can be shown that the size
of the ﬁrst part of RSKsh(m) is always equal to the length of a non-decreasing subsequence of maximal
4
PIERRE-LOÏC MÉLIOT
length in m; consequently, the study of Schur-Weyl measures is related to analogues of Ulam’s problem
([Ula61]).
If λ is a Young diagram, we turn it by 45 degrees and we consider the upper boundary of the new
drawing as a continuous function s 7→λ(s), with by convention λ(s) = |s| if s is too big (see ﬁgure 4).
y = λ(x)
Figure 4. Function s 7→λ(s) associated to the Young diagram λ = (5, 4, 4, 1).
This interpretation permits to rescale the Young diagrams, and in particular, we shall denote by λ∗
the Young diagram λ rescaled by a factor 1/
p
|λ| in both directions:
λ∗(s) = λ(s√n)/√n
Then, P. Biane has shown that under Schur-Weyl measures with parameter α ≥1/2, rescaled Young
diagrams admit a limit form (see Theorem 3 in [Bia01]):
c = 0
c = 1
c = 1/2
c = 2
Figure 5. Limit shapes of the rescaled Young diagrams under Schur-Weyl measures of
parameter α = 1/2.
Theorem 1 (First order asymptotics of Schur-Weyl measures of parameter α = 1/2). We ﬁx ε > 0, and
we suppose that α = 1/2. As n goes to inﬁnity,
SWn,α,c[∥λ∗−Ωc∥∞≥ε] →0,
KEROV’S CENTRAL LIMIT THEOREM FOR SCHUR-WEYL MEASURES
5
where Ωc is deﬁned by the following formulas:
Ω0(s) = Ω(s) =
(
2
π
 s arcsin( s
2) +
√
4 −s2
if |s| ≤2,
|s|
otherwise;
Ωc∈]0,1[(s) =



2
π

s arcsin(
s+c
2√1+sc) + 1
c arccos( 2+sc−c2
2√1+sc ) +
√
4−(s−c)2
2

if |s −c| ≤2,
|s|
otherwise;
Ω1(s) =
(
s+1
2
+ 1
π

(s −1) arcsin( s−1
2 ) +
p
4 −(s −1)2

if |s −1| ≤2,
|s|
otherwise;
Ωc>1(s) =







s + 2
c
if s ∈] −1
c , c −2[ ,
2
π

s arcsin(
s+c
2√1+sc) + 1
c arccos( 2+sc−c2
2√1+sc ) +
√
4−(s−c)2
2

if |s −c| ≤2,
|s|
otherwise.
The case when c = 0 corresponds to the limit shape of rescaled Young diagrams under Schur-Weyl measures
with parameter α > 1/2.
When α < 1/2, the “isotropic” scaling by a factor 1/√n in both directions is no more adequate, and
in fact, it can be shown that the order of magnitude of the parts of λ under Schur-Weyl measures with
parameter α < 1/2 is a O(n1−α), see [FM10, §6]. On the other hand, the function Ω0 is also the limit
shape of rescaled Young diagram under the so-called Plancherel measure, and in this case, a central limit
theorem for the ﬂuctuation
√n ∆λ(s) = √n (λ∗(s) −Ω0(s))
has been proved by S. Kerov, see [Ker93] and [IO02]. Our paper is concerned with the analogue of this
result for Schur-Weyl measures with parameters α = 1/2 and c > 0. In the next sections, we shall start
by presenting the tools commonly used for the asymptotic study of representations of symmetric groups.
