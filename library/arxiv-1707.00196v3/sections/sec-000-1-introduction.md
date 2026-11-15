---
doc_id: arxiv-1707.00196v3
doc_title: "Yang-Baxter representations of the inﬁnite symmetric group"
section_id: sec-000-1-introduction
section_title: "Introduction"
section_number: 1
pages: 1-5
source_pdf: 1707.00196v3.pdf
source_sha256: 9908b71521275b17
toc_source: outline
doc_brief: "Yang-Baxter representations of the inﬁnite symmetric group — Every unitary involutive solution of the quantum Yang-Baxter equation (R- matrix) deﬁnes an extremal character and a representation of the"
---
Introduction
March 22, 2018
Abstract
Every unitary involutive solution of the quantum Yang-Baxter equation (R-
matrix) deﬁnes an extremal character and a representation of the inﬁnite sym-
metric group S∞.
We give a complete classiﬁcation of all such Yang-Baxter
characters and determine which extremal characters of S∞are of Yang-Baxter
form.
Calling two involutive R-matrices equivalent if they have the same character
and the same dimension, we show that equivalence classes can be parameterized
by pairs of Young diagrams, and construct an explicit normal form R-matrix for
each class. Using operator-algebraic techniques (subfactors), we prove that two
R-matrices are equivalent if and only if they have similar partial traces.
Furthermore, we describe the algebraic structure of the set of equivalence
classes of all involutive R-matrices, and discuss several families of examples.
These include unitary Yang-Baxter representations of the Temperley-Lieb alge-
bra at loop parameter δ = 2, which can be completely classiﬁed in terms of their
trace and dimension.
The Yang-Baxter equation is an algebraic equation that plays a striking role in a
remarkable number of seemingly disparate ﬁelds: Statistical mechanics [3], quantum
mechanics [4], braid groups, knot theory [5, 6], integrable quantum ﬁeld theory [7],
quasitriangular Hopf algebras [8], and von Neumann algebras [9], to name but a few.
In its most basic form, the (quantum) Yang-Baxter equation is an equation for an
endomorphism R ∈End(V ⊗V ) on the tensor square of a vector space V , namely
(R ⊗idV )(idV ⊗R)(R ⊗idV ) = (idV ⊗R)(R ⊗idV )(idV ⊗R)
(1.1)
as an equation in End(V ⊗V ⊗V ). Several variations of this equation exist (see, for
example, [8, 10, 11]), but we shall only consider the form (1.1).
As a nonlinear system of (dim V )6 equations for (dim V )4 unknowns, the Yang-
Baxter equation is notoriously hard to solve in general. One rich source of solutions
to (1.1) is the theory of quantum groups, pioneered by Drinfeld [12] and Jimbo [13],
which connects the Yang-Baxter equation to the representation theory of Lie algebras.
A complete understanding or classiﬁcation of all solutions of the Yang-Baxter equation
has, however, not been reached.
1
A completely diﬀerent approach to solving the Yang-Baxter equation has been
put forward by Hietarinta. Emphasizing the point that an interesting structure of the
set of solutions of the Yang-Baxter equation can only be expected after dividing by
an appropriate equivalence relation, he succeeded in ﬁnding all solutions of (1.1) for
dim V = 2 up to a certain equivalence relation, with the help of computer algebra [14].
But already for dim V = 3, this program was only partially successful [15].
In this article, we develop a new approach to the Yang-Baxter equation in any
dimension by considering a more natural equivalence relation, based on representation
theory, on its set of solutions. Up to this equivalence, we give a complete classiﬁcation
of the special class of all unitary involutive R-matrices.
Here and hereafter, we consider (1.1) over a ﬁnite dimensional vector space V , and
agree to write d = dim V throughout1. We ﬁx a scalar product on V (and hence its
tensor powers), denote the set of all unitary solutions of (1.1) by R(V ), and write
R for the union of R(V ) over all ﬁnite dimensional vector spaces V . As usual, the
elements of R are referred to as R-matrices.
Given some R ∈R(V ), we refer to
d = dim V as the dimension of R – although R is an endomorphism of a space of
dimension d2 – and to V as the base space of R.
As is well known, any R ∈R(V ) generates (unitary) representations ρ(n)
R , n ∈N, of
the braid groups Bn on V ⊗n, by representing the elementary braid2 bk, k ∈{1, . . . , n−
1}, as
ρ(n)
R (bk) := id⊗(k−1)
V
⊗R ⊗id⊗(n−k−1)
V
∈End V ⊗n .
(1.2)
We set ρ(1)
R = idV . The representations (1.2) are used to deﬁne our equivalence relation
on R below. This relation is also suggested by applications in integrable quantum ﬁeld
theory [17]. In a particular context, the same relation was considered in [1], and a
more restrictive version of it was essential in the computation of all solutions of the
Yang-Baxter equation for d = 2 [14].
Deﬁnition 1.1. Two R-matrices R, S ∈R are deﬁned to be equivalent, denoted
R ∼S, if and only if for each n ∈N, the representations ρ(n)
R
and ρ(n)
S
are equivalent.
It is easy to check that two R-matrices are equivalent if and only if they have the
same dimension and the same normalized character, introduced in Sect. 2. Also note
that R ∼S implies similarity of these endomorphisms, R ∼= S, because ρ(2)
R (B2) is
generated by R.
Simple examples of equivalent R-matrices can be produced as follows: Let A ∈
GL(V ) be unitary and F ∈End(V ⊗V ) be the tensor ﬂip, deﬁned by F(v⊗w) = w⊗v.
Then, for any R ∈R(V ),
R ∼(A ⊗A)R(A−1 ⊗A−1),
R ∼FRF.
(1.3)
In particular, (A ⊗A)R(A−1 ⊗A−1) and FRF are elements of R(V ). But in general,
the two transformations (1.3) do not generate the full equivalence class of R.
1The Yang-Baxter equation (1.1) is of course also well deﬁned for inﬁnite dimensional Hilbert
spaces V , and in fact many interesting inﬁnite dimensional solutions exist: In particular, a solution
of the Yang-Baxter equation with spectral parameter can be rewritten as one without, but on an
inﬁnite dimensional base space (see, for example, [16, Lemma 2.2]).
2Recall that a presentation of the braid group Bn on n strands is given by Bn = ⟨b1, . . . , bn−1 :
bibi+1bi = bi+1bibi+1, bibj = bjbi for |i −j| > 1⟩.
2
In this paper, we focus on the important special case in which the representations
ρ(n)
R
factor through the surjective group homomorphism Bn →Sn onto the symmetric
group Sn of n letters. This happens if and only if R is involutive, R2 = 1.
Such involutive R-matrices play a prominent role in various ﬁelds, ranging from
symmetries of categories of vector spaces [18] over scattering operators in integrable
quantum ﬁeld theory (with a spectral parameter) [7] to representations of Thompson’s
group V [19] and recent constructions of non-commutative spaces [20].
They also
form the starting point for investigating q-deformed R-matrices with general quadratic
minimal polynomial.
We write R0(V ) ⊂R(V ), R0 ⊂R for the subset of involutive R-matrices.
In the involutive case, ρ(2)
R
∼= ρ(2)
S
is equivalent to R and S having the same
dimension and trace because the only possible eigenvalues are ±1. There is an old
conjecture by Gurevich to the eﬀect that equivalence classes of involutive R-matrices
R are even uniquely characterized by these two numbers, the dimension and the trace
of R [1, p. 760]. Gurevich gave a proof of his conjecture in the case that one of the
eigenvalues of R has multiplicity 1.
However, our ﬁndings in this article imply that this conjecture is false in general:
The full equivalence R ∼S is a much stronger condition than having the same dimen-
sion and trace, which is reﬂected in the rich structure of R0/∼that we ﬁnd. We shall
prove:
Theorem I. R0/∼is in one to one correspondence with pairs of Young diagrams.
Classes of R-matrices of dimension d correspond to pairs of Young diagrams with d
boxes in total.
Our analysis uses the fact that the Sn-representations ρ(n)
R , R ∈R0(V ), deﬁne a
representation ρR of the inﬁnite symmetric group S∞(the group of all bijections of
N that move only ﬁnitely many points) inside the inﬁnite (algebraic) tensor product
S
n End(V )⊗n. As any inﬁnite discrete group having no normal abelian subgroup of
ﬁnite index, S∞admits unitary representations which are not of type I [21], meaning
that its irreducible representations are not classiﬁable in a reasonable manner [22].
However, an explicit parameterization of its (normalized) extremal characters, corre-
sponding to ﬁnite factor representations, is known from the work of Thoma [23]. This
parameterization depends on countably many continuous variables 0 ≤αi, βi ≤1,
i ∈N. These Thoma parameters are subject to two simple conditions deﬁning a sim-
plex T which we recall in Sect. 2. For background information on the representation
theory of S∞, we refer readers to the recent monograph [24] and the literature cited
therein.
The upshot of our approach is that any involutive R-matrix R ∈R0 deﬁnes an
extremal character χR of S∞, and R, S ∈R0 are equivalent if and only if they have the
same character and the same dimension. Such Yang-Baxter characters (Sect. 2.1) can
therefore be parameterized by a subset TYB of Thoma’s simplex T, or, equivalently, in
terms of the Hilbert-Poincaré series of ρR [25, 2]. By a faithfulness consideration and
a theorem of Wassermann [26], it is straightforward to show that TYB̸ = T (Sect. 2.2).
Despite the ﬁnite dimensional appearance of the Yang-Baxter equation, a full
understanding of the subset TYB ⊂T and the equivalence relation ∼seems to require
tools from inﬁnite dimensional analysis and operator algebras. In Sect. 3, we propose
an approach based on subfactors arising from the subgroup {σ ∈S∞: σ(1) = 1} ⊂
S∞in Yang-Baxter representations ρR. Independent of the Yang-Baxter equation,
3
similar subfactors have been considered before, by Gohm and Köstler in a setting of
noncommutative probability theory in [27, 28], and by Yamashita in [29].
We will show that any R ∈R0, R̸ = ± idV ⊗V , deﬁnes an inclusion of II1 fac-
tors.
The trace-preserving conditional expectation of this subfactor can be com-
puted, and we show that it is closely related to the partial trace of R, ptr R =
(idEnd V ⊗TrV )(R) ∈End V . The partial trace turns out to be a complete invariant
of ∼:
Theorem II. Two R-matrices R, S ∈R0 are equivalent if and only if they have
similar partial traces, ptr R ∼= ptr S.
Our subfactor approach also completes the characterization of TYB as a subset of
T. Using the standard notation for Thoma parameters (recalled in Thm. 2.3), we ﬁnd
the following result.
Theorem III. An extremal character of S∞is a Yang-Baxter character if and only
if its Thoma parameters {αi}i, {βj}j satisfy
i) Only ﬁnitely many αi, βj are non-zero.
ii) P
i αi + P
j βj = 1.
iii) All αi, βj are rational.
The Thoma parameters of an R-matrix of dimension d satisfy dαi, dβi ∈N.
It is interesting to note that although the Yang-Baxter representations (1.2) have a
quite special form, their Thoma parameters form a dense subset of T. Several diﬀerent
approaches to characters and representations of S∞exist in the literature, of which
we mention here in particular the asymptotic character theory of Kerov and Vershik
[30, 31], and the works of Olshanski and Okounkov on spherical representations [32, 33],
partly in parallel with Wassermann [26].
One half of the proof of Thm. III relies on the operator-algebraic techniques men-
tioned above, and the other half (showing that any set of Thoma parameters {αi}i,
{βj}j satisfying the conditions i)-iii) is realized by some Yang-Baxter character χR)
is based on a constructive procedure for generating R-matrices which we develop in
Sect. 4.1. The main idea of this construction is to ﬁnd a good replacement for taking
direct sums of R-matrices/representations which respects the Yang-Baxter equation
(1.1). We deﬁne a suitable binary operation ⊞on R which enables us to construct
an explicit normal form R-matrix for each equivalence class in R0/∼. Together with
a suitably deﬁned tensor product of R-matrices and a compatible λ-operation, the
quotient R0/∼has the structure of a λ-semi ring.
Because of the rationality and ﬁniteness properties of TYB spelled out in Thm. III,
it is useful to switch to a parameterization in terms of the integer rescaled Thoma
parameters ai := dαi, bi := dβi. The two integer partitions deﬁned by the ai and
bi lie at the root of our classiﬁcation result in Thm. I. We also recast this structure
in terms of spectral data, reminiscent of previous work on the representation theory
of S∞(see, in particular, Okounkov [33] and Kerov, Olshanski, and Vershik [22]):
The eigenvalues of the partial trace ptr R of R ∈R0 uniquely determine the rescaled
Thoma parameters (see Thm. 4.8 ii) for details).
In addition to these main results summarized in the Theorems I–III, we also inves-
tigate the C∗-algebraic and combinatorial properties of Yang-Baxter representations.
4
In Sect. 5, we use K-theory to characterize the equivalence R ∼S in terms of ap-
proximate unitary equivalence of the homomorphisms ρR, ρS (Thm. 5.3) and recover
a result of Kerov and Vershik [34] in our Yang-Baxter setting. As K0(C∗S∞) is iso-
morphic to a quotient of the ring of symmetric functions [34], this also enables us
to give an explicit formula for the decomposition of the Yang-Baxter representations
ρ(n)
R
into irreducibles in terms of symmetric functions (Prop. 5.7), and to compute the
Hilbert-Poincaré series of ρR.
Our ﬁnal Sect. 6 is devoted to a discussion of examples, including in particular
Yang-Baxter representations of the Temperley-Lieb algebra [35] at loop parameter
δ = 2. Our results allow us to classify such representations completely in terms of the
dimension and trace of the underlying R-matrix (Prop. 6.3), thereby complementing
results of Gurevich and Bytsko [2, 48].
While it is clear that Theorems I–III do not hold verbatim for general R-matrices
(dropping the involutivity assumption), we do expect that many aspects of our tech-
niques and results can be generalized to other families of R-matrices, such as those
underlying knot polynomials, for which ρR factors through a Hecke algebra [5, 6, 36].
