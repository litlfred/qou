---
doc_id: arxiv-1408.3518v3
doc_title: "On Augmentation Algorithms for Linear and Integer-Linear Programming:"
section_id: sec-000-1-introduction
section_title: "Introduction."
section_number: 1
pages: 1-4
source_pdf: 1408.3518v3.pdf
source_sha256: cf18585b886587c7
doc_brief: "On Augmentation Algorithms for Linear and Integer-Linear Programming: — 4 sections: Introduction.; Our Contributions; Proofs"
---
integer-linear programs (ILPs) of the form
min { c⊺x : Ax = b, 0 ≤ x ≤ u, x ∈ X } , (1)
1
De Loera, Hemmecke and Lee: Augmentation in Linear and Integer Linear Programming
2
where A ∈ Zd×n, b ∈ Zd, c ∈ Zn, and where X = Rn (LP) or X = Zn (ILP). We focus on solution
algorithms that are based on an augmentation procedure. At each iteration, we have a current
feasible point xk. An augmentation direction z has xk + αz feasible for some α > 0 (which implies
that z is in the kernel of A) and has c⊺z < 0. Together, the augmentation is αz, and we pass to
the next feasible solution xk+1 := xk + αz. We note the trivial fact that c⊺xk+1 < c⊺xk. In this way,
an augmentation procedure produces a sequence of feasible s olutions x1, x2, . . . that are successive
improvements on the value of the objective function, until a n optimal solution is reached. Finally,
an augmentation αz is maximal if, considering xk and z to be ﬁxed, α is the largest value of t > 0
for which xk+1 := xk + tz is feasible. If the augmentation is maximal, xk+1 is the best point on the
intersection of the feasible region with the half-line {xk + tz : t > 0}. In what follows, we give
upper bounds on the number of maximal augmentations require d to reached an optimum, for both
the LP and ILP cases.
Of course, augmentation algorithms are nothing new, and one of the best-known in the family
is the classical simplex algorithm. For the case of LP, the si mplex method is indeed an augmen-
tation algorithm, where we start at a vertex of the polyhedro n that is the feasible region, and
the augmentation used at each iteration corresponds to an av ailable edge direction at the current
vertex. Of course, in the degenerate case, there can be consi derable work to calculate an improving
edge direction. Nonetheless, by limiting augmentation dir ections to available edge directions at
the current vertex, and always choosing maximal augmentati ons, we insure that the next feasible
solution is also a vertex, and so the simplex algorithm can co ntinue. Similarly, the idea of aug-
mentation has played a very important historical role in the algorithmic theory of network ﬂows;
in particular, there is the seminal and very well-known work of Edmonds and Karp (see [ 15]).
They showed that for maximum-ﬂow (essentially the same prob lem as maximizing the ﬂow on a
single arc of a ﬂow-conservative network, subject to simple bounds on the other arcs), the num-
ber of augmentations (taken by the classic Ford-Fulkerson a ugmentation algorithm) is bounded
by the number of arcs times the number of vertices, or slightl y more crudely by the number of
arcs squared, when augmentations are always chosen to have the fewest numb er of arcs, and the
augmentation is maximal. In unpublished work, R. Bland ([ 6]) extended this, rather elegantly, to
general LPs. Besides not being published by Bland in the 1970 ’s, it is not well known even today.
The result was implicitly alluded to in print in 1987 (see [ 4]), and mentioned more concretely in J.
Lee’s 1986 dissertation [ 25] (see Proposition 3.1 in the follow-on publication [ 26]). Bland himself
made a concrete statement of it (still without proof) in 1992 (see [ 7]):
“It was prompted by another result in the same Edmonds-Karp p aper [ 15], that if one always
augments on a shortest augmenting path, the number of augmen tations in the Ford-Fulkerson
maximum ﬂow algorithm is less than the product of the numbers of nodes and edges. Fulkerson
[17] had investigated the extent to which fundamental properti es of networks generalize to
broader classes of linear programming problems, where elem entary vectors in the appropriate
subspaces play the roles of circuits and cocircuits (minima l cutsets). Bland’s dissertation [ 5]
carried this further, and in later work he showed how the Edmo nds-Karp result generalizes to
arbitrary linear programming problems of the form
maximize x0
subject to Ax = 0, (2)
l ≤ x ≤ u.
Here the bound on the number of augmentations is the number of variables times the number
of diﬀerent lengths of normalized elementary vectors; in pa rticular if A is totally unimodu-
lar the bound is the product of the dimensions of A, as in the max ﬂow result of Edmonds
and Karp, where A is the (totally unimodular) node-edge matrix of a directed g raph. This
seemed to be amusing, but without any obvious use, until late in 1978 when Paul Seymour [ 35]
De Loera, Hemmecke and Lee: Augmentation in Linear and Integer Linear Programming
3
proved his remarkable decomposition theorem for unimodula r matroids. Bland and Edmonds
[8] used Seymour’s theorem to show how shortest augmentations could be computed in polyno-
mial time when the constraint matrix A is totally unimodular. Cost scaling was used to extend
the approach to a polynomial-time primal algorithm for tota lly unimodular linear programming
problems
maximize a⊺x
subject to Ax = b,
l ≤ x ≤ u.
which are solved as a sequence of subproblems of the form ( 2). More recently Tardos [ 36] has
given strongly polynomial algorithms for totally unimodul ar linear programming problems, and
still more general classes of combinatorial optimization p roblems, using cost scaling in a far
more clever way.”
Today, progress on the augmentation approach to LP continue s: new families of augmentation
algorithms for LP include those proposed in [ 12] (and rediscovered in [ 2]). Very recently, the work
of Kern, Faigle, and Peis [ 23] rekindled our interest in Bland’s result as they, among oth er things,
rediscovered it. Additionally, Kitahara and Mizuno [ 24] gave an upper bound for the number of
diﬀerent basic-feasible solutions generated by the simple x method. Their results are direct gener-
alizations of Y. Ye’s work [ 37].
On the other hand, the study of augmentation algorithms for I LPs goes back at least to the
1970’s and was part of the study of “test sets” (see [ 18, 31, 32] and the references therein). More
recently there have been important developments. In [ 33] the authors show that one can solve
every integer-linear programming problem in polynomial ti me provided one can eﬃciently solve a
special directed-augmentation problem (the directed-augmentation problem diﬀers from the ordi-
nary augmentation problem by splitting each direction into its positive and negative parts and
considering linear objectives on each of these parts). Thes e authors showed that if one can solve the
directed-augmentation problem in polynomial time, then th e original problem can be solved by a
polynomial-time algorithm. Their main application is to sp eciﬁc combinatorial-optimization prob-
lems, such as the min-cost ﬂow problem. Later [ 21] showed that if a “best-improving” augmentation
z in the “Graver basis” of the constraint matrix is chosen (the authors of [ 21] called this augmenta-
tion rule “greedy improvement”; here we will call this “deep est descent”), only polynomially-many
augmentations (in the binary encoding length of the input da ta) must be performed in order to
reach the optimal value. The paper [ 21] shows how to eﬃciently use an augmentation algorithm
for separable convex objective functions and implicitly pr ovided bounds like those presented here.
The set of possible augmentation directions we use depends o n the type of problem: for the
LP case, we use as the set of possible augmentation direction s the circuits of A. C(A) consists
of the normalized elementary vectors (or circuits) associated with ker( A) \ { 0 } (see [ 29]) — that
is, the vectors having (set-wise) minimal support in ker( A) \ { 0 }. The set of elementary vectors
of ker( A) \ { 0 } is a ﬁnite set of lines through the origin, with the origin exc luded. Usually, it is
convenient to normalize in an arbitrary manner, so that C(A) comprises a single point and its
negative from each such line. In our context, Bland’s normal ization uses the objective function so
that c⊺z = −1 for every augmentation direction — in his terms, such a z is unit augmenting . For
the vectors in C(A), we choose on each line the (nonzero) integer point closest to the origin and its
negative as the normalized representatives.
For the IP case, the set of possible augmentation directions is the Graver basis of A, denoted
by G(A). We obtain Graver’s original ﬁnite set of ⊑-minimal elements in ker( A) ∩ Zn \ {0 }, where
u ⊑ v if and only if u(i)v(i) ≥ 0 and |u(i)| ≤ | v(i)| (see [ 18]). In general, G(A) has a nice sign-
compatible representation property: every (integer vecto r) z ∈ ker(A) can be written as z = ∑ αigi,
with gi ∈ G(A), αi > 0, αi ∈ Z, and αigi ⊑ z, for all i, and the sum involves at most 2 n − 2 terms.
De Loera, Hemmecke and Lee: Augmentation in Linear and Integer Linear Programming
4
In fact, G(A) is an inclusion-minimal set with this property. It should b e noted that due to the
sign-compatible representation we have
‖z‖1 =
∑
αi‖gi‖1,
where ‖ · ‖1 is the usual 1-norm.
We remark that the all circuits are members of the Graver basi s. But they also provide an elegant
sign-compatible representation over the reals for all non-zero elements of ker( A). Speciﬁcally, every
vector z ∈ ker(A) can be written as z = ∑ αigi, with gi ∈ C(A), αi ≥ 0, αi ∈ R, and the sum involves
at most n terms. Note that the (worst-case) number of summands is smal ler than in the general
Graver decomposition. It is worth remarking that Graver bas es can also be deﬁned for the general
mixed-integer case (see [ 19, Section 3.3]) — but in the mixed-integer setting, the Grave r basis is
not generally ﬁnite, in sharp contrast to the LP and ILP cases ; so we do not consider that situation
here as, unlike the LP and ILP cases, it requires the existenc e of some kind of specialized oracle
to generate the augmentations one by one. For an introductio n to Graver bases and the latest on
augmentation algorithms for integer programming see the bo oks [ 13] and [ 27].
