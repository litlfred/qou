---
doc_id: arxiv-1408.3518v3
doc_title: "On Augmentation Algorithms for Linear and Integer-Linear Programming:"
section_id: sec-002-2-proofs
section_title: "Proofs"
section_number: 2
pages: 8-13
source_pdf: 1408.3518v3.pdf
source_sha256: cf18585b886587c7
doc_brief: "On Augmentation Algorithms for Linear and Integer-Linear Programming: — 4 sections: Introduction.; Our Contributions; Proofs"
---
following lemma (a slight variation from Theorem 3.1 in [ 1]) which establishes the bounds we claim
once we can guarantee suﬃcient improvement at each iteratio n:
Lemma 3. Let ǫ > 0 be given. Moreover, let H denote the diﬀerence between maximum and
minimum objective-function values of the LP/ILP problem in n variables. Suppose that f k = c⊺xk
is the objective-function value of the solution xk at the k-th iteration of an algorithm and that
f ∗ = c⊺xmin is the minimum objective-function value. Furthermore, sup pose that the algorithm
guarantees that for every augmentation k,
(f k − f k+1) ≥ β(f k − f ∗)
(i.e., the improvement at augmentation k + 1 is at least β times the maximum possible improve-
ment). Then the algorithm reaches a solution with f k − f ∗ < ǫ in no more than 2 log (H/ǫ)/β
augmentations.
Proof: Without loss of generality, we assume that c is an integer vector. (Thus for the ILP
version the values f k are decreasing successive integer values.) The biggest nec essary change of
value of the objective function occurs when we start the augm entation at an maximum point xmax
and end with some minimum optimal point xmin. Thus, we have H = f max − f min.
If we had at every augmentation an improvement of at least β(f max − f min)/2, then in no more
than 2 /β augmentations we would have reached the optimum. But if this improvement is not
achieved at each augmentation, say at the q-th augmentation we have f q − f q+1 ≤ β(f max − f min)/2
then, together with the hypothesis ( f q − f q+1) ≥ β(f q − f min), we get that
f q − f min ≤ (f max − f min)/2 = H/2.
In other words, the overall improvement reached so far is at l east half of the maximum possible
improvement H. In conclusion, after 2 /β augmentations, we have either reached the optimum or
have at least divided the possible gap by 2. Therefore in no mo re than 2/β log2 (H/ǫ) augmentations
we reach a solution with f k − f ∗ < ǫ. □
It is important to note that in the ILP case f k is integer, and we can apply Lemma 3 with ǫ = 1
and conclude that we can reach the optimum in O(log (H)/β) augmentations. In the LP case, let δ
denote the least common multiple of all subdeterminants of A. Observe that once we ﬁnd a feasible
solution xk with objective value f k satisfying f k − f ∗ < ǫ = 1/δ, then any vertex with an objective
value of at most f k must be optimal. As explained above (right before the statem ent of Theorem
1), such a vertex can be found from xk in at most n additional augmentations. This leads to extra
factors of n and of log( δ) in the bounds for the LP cases compared to the ILP cases.
2.1. Proof of Lemma 1 and Theorem 1 Let us assume that xk is a non-optimal feasible
solution, and let xmin be an optimal solution to the ILP. Then there exists a (sign-c ompatible)
representation
xmin − xk =
∑
αigi,
with αi > 0, αi ∈ Z and with αigi ⊑ xmin − xk. Moreover, due to Seb¨ o’s result [34], at most 2 n − 2
summands are needed.
De Loera, Hemmecke and Lee: Augmentation in Linear and Integer Linear Programming
9
Note that sign-compatibility of the representation xmin − xk = ∑ αigi implies that for all i the
vectors xk + αigi and xmin − αigi are all feasible solutions, since their components lie betw een
the components of xk and of xmin. Moreover, we can observe that for all such sign-compatible
representations xmin − xk = ∑ αigi we must have c⊺gi ≤ 0 for all i, as otherwise xmin − αigi would
be a feasible solution with c⊺(xmin − αigi) = c⊺xmin − αic⊺gi < c⊺xmin, contradicting the minimality
of xmin.
Next, we analyze what happens for each choice of augmentatio n rule:
2.1.1. Proof of Lemma 1: Discrete deepest descent. We observe that
0 > c⊺(xmin − xk) = c⊺
∑
αigi =
∑
αic⊺gi ≥ −(2n − 2)∆
where ∆ > 0 is the largest value of −αc⊺z over all z ∈ G(A) and integer α > 0 for which xk + αz is
feasible. Rewriting this, we get
∆ ≥ c⊺(xk − xmin)
2n − 2 .
Now let αz be the discrete deepest-descent augmentation applied to xk, leading to xk+1 := xk + αz.
Then we get ∆ = −αc⊺z and
c⊺(xk − xk+1) = −αc⊺z = ∆ ≥ c⊺(xk − xmin)
2n − 2 .
Thus, we have a factor of β = 1/(2n − 2) of objective-function decrease at each augmentation,
leading to the desired polynomial number of augmentations v ia Lemma 3 taking ǫ = 1. In this case,
we get the number of augmentations bounded by (4 n − 4) log( c⊺(x0 − xmin))).
2.1.2. Proof of part (a) of Theorem 1: Discrete Dantzig descent. We observe that
0 > c⊺(xmin − xk) = c⊺
∑
αigi =
∑
αic⊺gi ≥ −∆ 0
∑
αi ≥ −(2n − 2)∆ 0αmax,
where this time ∆ 0 > 0 denotes the greatest value of −c⊺z over all z ∈ G(A) for which xk + z is still
feasible and where αmax = max { αi }. Rewriting this, we get
∆ 0 ≥ c⊺(xk − xmin)
(2n − 2)αmax
.
Now let αz be the discrete Dantzig-descent augmentation applied to xk, leading to xk+1 := xk + αz.
Then we get
c⊺(xk − xk+1) = −αc⊺z = α∆ 0 ≥ ∆ 0 ≥ c⊺(xk − xmin)
(2n − 2)αmax
≥ c⊺(x0 − xmin)
(2n − 2)γ ,
where γ is the maximum entry in any feasible integer solution (or, eq uivalently, in any vertex of PI).
Thus, we have a factor of β = 1/((2n − 2)γ) of objective-function decrease at each augmentation
leading to the desired polynomial number of augmentations v ia Lemma 3 taking ǫ = 1. In this case
we get the number of augmentations bounded by (4 n − 4) γ log(c⊺(x0 − xmin)))
2.1.3. Proof of part (b) of of Theorem 1: Discrete steepest descent. We begin with
a series of lemmas. Note that the proof for the LP case follows exactly the same lines, since we do
not use integrality of the components in our arguments.
Lemma 4. Let xk be a feasible solution, and let z be an associated steepest descent direction.
Then there is some augmentation direction g ∈ G(A) from xk, with −c⊺g/‖g‖1 ≥ −c⊺z/‖z‖1.
De Loera, Hemmecke and Lee: Augmentation in Linear and Integer Linear Programming
10
Proof. There is a sign-compatible representation z = ∑ αigi via elements gi ∈ G (A). Observe
that due to the sign-compatible representation, xk + αigi is also feasible for all i. (The components
of xk + αigi lie between those of xk and xk + z, implying that 0 ≤ xk + αigi ≤ u.) In other words,
all αigi are applicable augmentations at xk.
It remains for us to show that there exists some index i with −c⊺gi/‖gi‖1 ≥ −c⊺z/‖z‖1. Assume
to the contrary that we have −c⊺gi/‖gi‖1 < −c⊺z/‖z‖1 for all i. This yields
−c⊺z = −
∑
αic⊺gi
=
∑
αi‖gi‖1
−c⊺gi
‖gi‖1
<
∑
αi‖gi‖1
−c⊺z
‖z‖1
= −c⊺z
‖z‖1
∑
αi‖gi‖1
= −c⊺z
‖z‖1
‖z‖1
= −c⊺z,
a contradiction. □
Lemma 4 states that among all steepest-descent directions applica ble at a feasible solution xk,
there is always one in G(A). Or in other words, the discrete steepest-descent rule is a steepest
descent rule as claimed in Theorems 1 and 2, parts(c).
Lemma 5. Let xk be a feasible solution, let αs be a steepest-descent augmentation relative to
xk, and let xk+1 := xk + αs. Let βt be a steepest-descent augmentation relative to xk+1. Then we
have −c⊺s/‖s‖1 ≥ −c⊺t/‖t‖1.
Proof. Suppose on the contrary that −c⊺s/‖s‖1 < −c⊺t/‖t‖1. First observe that αs + βt is an
applicable augmentation at xk. Moreover, we have
−c⊺(αs + βt) = α‖s‖1
−c⊺s
‖s‖1
+ β‖t‖1
−c⊺t
‖t‖1
> α ‖s‖1
−c⊺s
‖s‖1
+ β‖t‖1
−c⊺s
‖s‖1
= ( α‖s‖1 + β‖t‖1) −c⊺s
‖s‖1
,
≥ (‖αs + βt‖1) −c⊺s
‖s‖1
,
and therefore
−c⊺(αs + βt)
‖αs + βt‖1
> −c⊺s
‖s‖1
.
This contradicts the fact that s was a steepest descent direction for xk. □
Lemma 5 states that the steepness of steepest-descent augmentatio ns never increases.
Lemma 6. Let xk be a feasible solution and let α1z1, . . . , αjzj be the following steepest-descent
augmentations applied to xk. If z1 and zj do not have the same sign-pattern from { ≤ 0, ≥ 0 }
n
,
then we have −c⊺z1/‖z1‖1 > −c⊺zj/‖zj‖1.
De Loera, Hemmecke and Lee: Augmentation in Linear and Integer Linear Programming
11
Proof. Assume on the contrary that −c⊺z1/‖z1‖1 ≤ −c⊺zj/‖zj‖1. By monotonicity, Lemma 5,
we must have −c⊺z1
‖z1‖1
= −c⊺z2
‖z2‖1
= · · ·=
−c⊺zj
‖zj ‖1
. We conclude that
−c⊺
( ∑ j
i=1 αizi
)
= ∑ j
i=1 αi‖zi‖1
−c⊺zi
‖zi‖1
= ∑ j
i=1 αi‖zi‖1
−c⊺z1
‖z1‖1
=
( ∑ j
i=1 αi‖zi‖1
)
−c⊺z1
‖z1‖1
>
‖‖‖∑ j
i=1 αizi
‖‖‖
1
−c⊺z1
‖z1‖1
,
since z1 and zj do not have the same sign-pattern. This implies that
−c⊺
( ∑ j
i=1 αizi
)
‖ ∑ j
i=1 αizi‖1
> −c⊺z1
‖z1‖1
.
As by assumption ∑ j
i=1 αizi is an applicable augmentation at xk. This contradicts the fact that z1
was a steepest-descent augmentation for xk. □
Lemma 6 states that once the sign pattern of a steepest-descent augm entation strictly changes,
the steepness must decrease. This lemma has a surprising con sequence if we only apply steepest-
descent directions from G(A):
Corollary 7. For discrete steepest descent, no direction from G(A) is chosen twice as an
augmenting direction. Therefore, the number of steepest-d escent augmentations needed to reach an
optimal solution is bounded by |G(A)| and thus is independent of b, c and the initial solution z0.
Proof. Let xk be a feasible solution and let α1z1, . . . , αjzj, with z1, . . . ,zj ∈ G(A), be the following
steepest-descent augmentations applied to xk with αi chosen maximally in each augmentation.
Moreover assume that zj = z1. Then, by Lemma 6, all intermediate augmentations must have the
same sign-pattern as z1, as otherwise the steepness of the augmentations would have dropped.
As all vectors α1z1, . . . , αjzj have the same sign-pattern, the components of xk + α1z1 + αjzj lie
between the components of xk and xk + ∑ j
i=1 αizi and therefore also between 0 and u. Thus,
xk + α1z1 + αkzj = xk + (α1 + αj)z1 is a feasible solution. This contradicts the fact that α1 was
chosen maximally. □
2.2. Proof of Lemma 2 and Theorem 2 Let us assume that xk is a non-optimal feasible
solution, and let xmin be an optimal solution to the LP. Then there exists a (sign-co mpatible)
representation
xmin − xk =
∑
αigi,
with αi > 0 and with αigi ⊑ xmin − xk. Moreover, due to Carath´ eodory theorem, at most n sum-
mands are needed in such a representation. Again, sign-comp atibility of the representation xmin −
xk = ∑ αigi implies that for all i the vectors xk + αigi and xmin − αigi are all feasible solutions.
Let us now analyze what happens for each choice of augmentati on rule:
2.2.1. Proof of Lemma 2 for Discrete deepest descent. We observe that
0 > c⊺(xmin − xk) = c⊺
∑
αigi =
∑
αic⊺gi ≥ −n∆
where ∆ > 0 is the largest value of −αc⊺z over all z ∈ C(A) and α > 0 for which xk + αz is feasible.
Rewriting this, we get
∆ ≥ c⊺(xk − xmin)
n .
De Loera, Hemmecke and Lee: Augmentation in Linear and Integer Linear Programming
12
Now let αz be the discrete deepest-descent augmentation applied to xk, leading to xk+1 := xk + αz.
Then we get ∆ = −αc⊺z and
c⊺(xk − xk+1) = −αc⊺z = ∆ ≥ c⊺(xk − xmin)
n .
Thus, we have a factor of β = 1/n of objective-function value decrease at each augmentation . Apply-
ing Lemma 3 with ǫ = 1/δ then yields a solution ¯x with |c⊺(¯x − xmin)| < 1/δ within 2n log(δ c⊺(x0 −
xmin))) many augmentations. Due to the deﬁnition of δ as the least common multiple of all subde-
terminants of A, any vertex with an objective value of at most c⊺ ¯x must be optimal. As explained
right before the statement of Theorem 1, such a vertex can be found from ¯x in at most n additional
augmentations. Finally, note that once the discrete deepes t-descent augmentation makes progress
in objective value less than ǫ/(2n − 2), we have
|c⊺(xk − xmin)| =
∑
|αic⊺gi| < (2n − 2) · ǫ/(2n − 2) = ǫ.
Hence, we can decide eﬀectively when we should stop making di screte deepest-descent augmenta-
tions and should rather ﬁnd a nearby vertex.
2.2.2. Proof of part (a) of Theorem 2: Discrete Dantzig descent. In order to avoid
zig-zagging (see example in Section 4 of [ 19] and the details of how to avoid this), we must augment
to a vertex with lower objective-function value after each d iscrete Dantzig-descent augmentation.
For this, we need at most n discrete Dantzig-descent augmentations within smaller an d smaller
faces of P . Let xk be a vertex of the given polyhedron. Again we observe that
0 > c⊺(xmin − xk) = c⊺
∑
αigi =
∑
αic⊺gi ≥ −∆ 0
∑
αi ≥ −n∆ αmax,
where ∆ 0 > 0 is the greatest value of −c⊺z over all z ∈ C (A) for which xk + λz is feasible for
suﬃciently small λ > 0 and where αmax = max { αi }. Rewriting this, we get
∆ 0 ≥ c⊺(xk − xmin)
nαmax
.
Now, let αz be the discrete Dantzig-descent augmentation applied to xk, leading to xk+1 := xk + αz.
As xk is a vertex and z an edge direction, we have xk, z ∈ 1
δ Zn. As xk+1 is lies on the intersection
of the half-line { x = xk + λz : λ ≥ 0 } with some facet of the polyhedron, we get that xk+1 ∈ 1
δ2 Zn.
Consequently, α ≥ 1/δ.
Thus, we get
c⊺(xk − xk+1) = −αc⊺z = α∆ 0 ≥ 1
δ ∆ 0 ≥ c⊺(xk − xmin)
nδαmax
≥ c⊺(x0 − xmin)
nδγ ,
where γ is the maximum entry in any feasible solution (or, equivalen tly, in any vertex). Thus, we
have a factor of β = 1/(nδγ) of objective-function decrease at each augmentation. App lying Lemma
3 with ǫ = 1/δ then yields the desired bound on the number of augmentations 2n2δγ log(δ c⊺(x0 −
xmin))) to reach a vertex ¯x with |c⊺(¯x − xmin)| < 1/δ. This vertex must be optimal.
2.2.3. Proof of part (b) of Theorem 2: Discrete steepest descent. The proof here
follows exactly the same lines of the proof to Theorem 1, part (c).
De Loera, Hemmecke and Lee: Augmentation in Linear and Integer Linear Programming
13
2.3. Proof of Theorem 3. If we keep A and B ﬁxed and let N vary, the binary encoding
lengths of the Graver bases of [ A, B](N ) are bounded by a polynomial in N , see [ 14]. More precisely,
there is a constant g(A, B), the so-called Graver complexity of A and B (see [ 22, 30, 3]), given by
max { ‖g‖1 : g ∈ G(BG(A)) } ,
such that ⏐⏐G
( [A, B](N )) ⏐⏐≤
( N
g(A, B)
) ⏐⏐G
( [A, B](g(A,B ))) ⏐⏐∈ O ( N g(A,B )) .
This means that we can ﬁnd a steepest-descent direction in G
(
[A, B](N ))
in time polynomial in N
and by Theorems 1 and 2, parts (c), the number of steepest-descent augmentations t o pass from any
feasible solution x0 to an optimal solution is bounded polynomially in N . As the input of an N -fold
LP/ILP contains Θ( N ) integer numbers (to encode b and c), we can augment x0 to optimality in
strongly polynomial-time. It remains for us to show how we ca n ﬁnd such a feasible solution x0
in strongly polynomial-time. Note that by a shift of coordin ates, we may assume without loss of
generality that l = 0.
To ﬁnd such a feasible solution x0, consider the extended N -fold LP/ILP with problem matrix


B O O I dB −IdB B O O I dB −IdB · · · B O O I dB −IdB
A I dA −IdA O O
A I dA −IdA O O
. . .
A I dA −IdA O O


.
This is an N -fold matrix composed using the matrices ¯A =
( A I dA −IdA O O )
and ¯B =( B O O I dB −IdB
)
. As the right-hand side of our LP/ILP, we choose the same righ t-hand side vec-
tor b, and as objective vector we use a 0 /1-vector with zeros in the original components and with
ones in the auxiliary components. All variables get lower bo unds of 0, and the original variables
get upper bounds speciﬁed by u. Due to the special form of the matrix, we can immediately wri te
down a feasible solution to this problem. (Simply assign zer os to the original variables and set the
auxiliary slack variables according to the positive and neg ative parts of the right-hand side values.)
Optimizing this special linear objective function can now b e done in strongly polynomial-time,
since ¯A and ¯B are constant the running time of this auxiliary N -fold LP/ILP is bounded polynomi-
ally in N , but does not depend on the right-hand side or the objective v ector. If the optimal value
of this auxiliary LP/ILP is 0, a feasible solution to our orig inal problem has been found (simply
drop the auxiliary components). If the optimal value is posi tive, our original problem is infeasible.
□
