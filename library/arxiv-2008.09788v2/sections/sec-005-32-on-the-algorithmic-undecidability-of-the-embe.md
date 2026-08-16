---
doc_id: arxiv-2008.09788v2
doc_title: "NONSTANDARD ANALYSIS, DEFORMATION QUANTIZATION AND SOME LOGICAL ASPECTS OF (NON)COMMUTATIVE ALGEBRAIC GEOMETR Y"
section_id: sec-005-32-on-the-algorithmic-undecidability-of-the-embe
section_title: "On the algorithmic undecidability of the embeddability problem for algebraic varieties over a field of characteristic zero"
section_number: 3.2
pages: 25-28
source_pdf: 2008.09788v2.pdf
source_sha256: 460f4f5432cb1f0c
doc_brief: "NONSTANDARD ANALYSIS, DEFORMATION QUANTIZATION AND SOME LOGICAL ASPECTS OF (NON)COMMUTATIVE ALGEBRAIC GEOMETRY — This paper surveys results related to well-known works of B. Plotkin and V."
---
braic varieties over a ﬁeld of characteristic zero.
3.2.1. The Case of Real Numbers. By a Matiyasevich family of polynomials we mean
a family of polynomials
Q(σ 1, . . . , σ τ , x 1, . . . , x s)
for which the existence of a solution for a given set of parame ters of the polynomial is
undecidable. As was established in [65], such a polynomial e xists.
Consider the aﬃne space of dimension 5 d + 1. We denote coordinates in this space
by Xi, Y i, Z i, U i, W i, 1 ≤ i ≤ d, and T . Consider the variety B(d) given by the following
system of generators and relations:
{ X 2
i −
(
T 2 − 1
)
Y 2
i = 1,
Yi − (T − 1)Zi = Vi,
ViUi = 1,
⟨3.24⟩
where 1 ≤ i ≤ d. For ﬁxed i, the admissible values of the coordinates Xi, Y i, Z i, U i,
and Wi are determined by the same value of T . Consider the “short” subsystem
{ X 2 −
(
T 2 − 1
)
Y 2 = 1,
Y − (T − 1)Z = V,
V U = 1,
⟨3.25⟩
Lemma 3.3. The following assertions hold for every solution of system ( 3.25):
1) U and V are nonzero constants in F[t] (deg U = deg V = 0);
2) either T = ±1 and X = ±1 or
Y =
[N/ 2]∑
k=0
(
N2k + 1
) (
T 2 − 1
) k
T N−1−2k
for some integer N .
Let R denote a root of the equation R2 = T 2 − 1 such that R belongs to the algebraic
extension F[t]. Then the element ( T + R)n can be uniquely represented in the form
Xn + RYn, where Xn and Yn are polynomials in F[t]. All solutions of the equation
X 2 − (T 2 − 1)Y 2 = 1 ⟨3.26⟩
26 KANEL-BELOV, CHILIKOV, IV ANOV-POGODAEV, MALEV, PLOTKI N, YU, AND ZHANG
are of the form X = ±Xn, Y = ±Yn (see [16]).
The structure of this set depends on T . In the case T = ±1, the ﬁrst equation of
the system imposes no conditions at all on Y . In turn, the other equation implies Y =
(T − 1)Z + V . For every choice of V ∈ F \ {0} and Z ∈ F[t], the corresponding solution
exists and is unique.
Lemma 3.4. If deg T > 0, then V = Y mod(T − 1) = N for an integer N and Z =
(Y − N )/ (T − 1). If T = const ⁄= ±1, then Y and Z are constants in F[t].
Thus, the following three cases are possible:
(1) for deg T > 0, to every set of integers Ni there correspond polynomial solutions
Yi and Xi determined up to sign, as well as the constants Vi = Ni and Ui = 1/V i,
and Zi = (Yi − Vi)/ (T − 1);
(2) for deg T = 0 and T ⁄= ±1, there are constant solutions for Yi chosen from a given
sequence; the values Xi, Z i, V i and Ui are also constants, and they are determined
by the chosen values of Yi;
(3) for T = ±1, we obtain Xi = ±1; for arbitrarily chosen constants Vi and polyno-
mials Zi, we set U1 = 1/V i and Yi = (T − 1)Zi + Vi.
So far, these considerations are valid for an arbitrary grou nd ﬁeld F of characteristic
zero. In the case F = R, we introduce a new coordinate S by completing the main system
of equations by the equation
T = S2 + 2, ⟨3.27⟩
which ensures the impossibility of T = ±1. All common solutions of systems (3.24) and
(3.27) either are constants (if deg T = 0, T ⁄= ±1) or correspond to some set of integer
parameters ( N1, . . . , N d). We refer to solutions of the ﬁrst kind as “bad” and to those o f
the second kind as “good”.
Consider a Matiyasevich family of polynomials Q(σ 1, . . . , σ τ , x 1, . . . , x s). Let d ≤ s.
Then, adding the new equation Q(σ, V 1, . . . , V s) = 0 to systems (3.24) and (3.27), we
obtain a system deﬁning a new variety. We denote this variety by B′
(d),σ .
If Q = 0 has no integer solutions, then the original system has no g ood solutions. In
this case, the variety B′
(d),σ is zero-dimensional, and there are no embeddings of A in
B′
(d),σ .
Otherwise, for every solution N1, . . . , N s, we can explicitly construct functions
Yi(S), X i(S), and Zi(S) which are solutions. They deﬁne an embedding of the line in
the variety B′
(d),σ .
Since the existence of integer solutions for Q is undecidable, it follows that so is the
embeddability of A in B′
(d),σ (in particular, in B′
(s),σ ). Here the input data is the equations
deﬁning B′
(d),σ . We have proved the following theorem.
Theorem 3.5. The problem of the embeddability of the aﬃne line (and, there fore, the
general embedding problem for an arbitrary variety) over R in an arbitrary algebraic variety
B (deﬁned by generators and relations) is undecidable.
3.2.2. The Complex Case. In this case, the situation is more complicated: it is hard
to eliminate the case in which T = ±1 and Xi = ±1, since no constraints on Yi arise in
this case. Therefore, we consider the problem of the embedda bility of an aﬃne space Am
in a given variety B and construct a class of varieties such that it is impossible to decide
whether a desired embedding exists from the deﬁning relatio ns for representatives of this
class (for a certain suitable integer m). We deﬁne the coordinate ring of the variety B(d,e )
by the following system of generators and relations:





X 2
ij −
(
T 2
j − 1
)
Y 2
ij = 1,
Yij − (Tj − 1) Zij = Vij,
VijUij = 1,
Tj+1 =∏ j
k=1
((
T 2
k − 1
)
Wk
)
Wj+1,
⟨3.28⟩
SOME LOGICAL ASPECTS 27
where 1 ≤ i ≤ d and 1 ≤ j ≤ e. In fact, we compose a system of many “clones” of the
main system of the previous subsection and augment it by the “ linking” relations between
the parameters Tj . Let us study the solutions of the resulting system in C[t].
The relations for Xij, Y ij, Z ij, U ij, and Vij for each ﬁxed Tj are similar to those con-
sidered above. For a ﬁxed set of Tj, the set of solutions is the direct sum of the sets B(d),
which have already been studied above.
As above, for each j, the following cases can occur: Tj = ±1 and deg Tj = 0; Tj ⁄= ±1,
and deg Tj > 0.
The case most important from the point of view of “eliminatio n” is the case where
Tˆj = ±1 for some ˆj. In this case, T 2
ˆj − 1 = 0, and for all j < ˆj, we obtain
Tj =
j−1∏
k=1
((T 2
k − 1)Wk)Wj.
Lemma 3.6. If TN = CN ⁄= 0 for some N , then all Wk with k ≤ N and all Tk with
k ≤ N − 1 are constants.
By Lemma 3.6, we have Tj = Cj for j < ˆj. Here Cj ⁄= ±1 (otherwise Cj+1 = 0). Thus,
if Tˆj = ±1 for some ˆj, then the corresponding component has dimension d. However,
in this case, all other components are zero-dimensional, an d the total dimension of the
variety does not exceed d.
In the second case, we have Tˆj = Cˆj ⁄= ±1 for some ˆj. The corresponding component
of the variety has dimension 0. Moreover, Lemma 3.6 implies Tj = Cj for j < ˆj. The
corresponding ˆj − 1 components of the variety are zero-dimensional as well.
The case deg Tj > 0 was considered in Sec. 3.2.1. Each component of the variety is
parametrized by a set of integers N1j , . . . , N d j,for which the corresponding solutions for
Xij, Y ij, Z ij, U ij, and Vij are constructed explicitly. The corresponding component h as
dimension 1.
Consider a Matiyasevich family of polynomials Q(σ 1, . . . , σ τ , x 1, . . . , x s). The solvabil-
ity problem of the Diophantine equation Q(σ 1, . . . , σ τ , V 1j , . . . , V sj) = 0 is algorithmically
undecidable. Let d ≤ s. Adding the new equations Q(σ, V i1, . . . , V is) = 0 to system 3.28,
we obtain a system deﬁning a new variety. We denote it by B′
(d,e ),σ .
If Q = 0 has no integer solutions, then the original system has no s olutions for which
deg T0 > 0. In this case, the possible solutions correspond either to the case where Tj = ±1
for some j (and the set of solutions has dimension d) or to the case Tj = Cj ⁄= ±1. In the
latter case, assuming that j is the maximum index for which Tj = Cj ⁄= ±1, we see that
all the succeeding e − j components are one-dimensional and the total dimension of t he
set equals precisely e − j ≤ e − 1. Setting e = s and d = s − 1, we obtain
dim B′
(d,e ) ≤ max(e − 1, d ) = s − 1 < s.
Obviously, in this case, for m ≥ s, there is no embedding of A = Am in B′
(d,e ),σ =
B′
(s−1,s ),σ . In particular, As cannot be embedded in B′
(s−1,s ),σ .
If Q has integer solutions, then, for every such solution N1, . . . , N s, we can explicitly
construct functions Yij(T ), X ij(T ), and Zij(T ) which are solutions. These functions deﬁne
an embedding of A = As in the variety B′
(d,e ),σ .
Since the existence of integer solutions for Q is undecidable, it follows that the embed-
dability of As in B′
(s−1,s ),σ is undecidable as well (the input data is the equations deﬁni ng
B′
(s−1,s ),σ ). The proof is valid for any ﬁeld K of of characteristic zero. The following
theorem holds.
Theorem 3.7. There is a positive integer s for which the embeddability of a n aﬃne space
As over K in an arbitrary algebraic variety B (deﬁned by generators and relations) is
undecidable. Thus, the general embeddability problem for a n arbitrary algebraic variety is
undecidable as well.
28 KANEL-BELOV, CHILIKOV, IV ANOV-POGODAEV, MALEV, PLOTKI N, YU, AND ZHANG
