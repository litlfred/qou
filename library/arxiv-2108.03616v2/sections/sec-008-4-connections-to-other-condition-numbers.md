---
doc_id: arxiv-2108.03616v2
doc_title: "Circuit imbalance measures and linear programming ∗"
section_id: sec-008-4-connections-to-other-condition-numbers
section_title: "Connections to other condition numbers"
section_number: 4
pages: 15-18
source_pdf: 2108.03616v2.pdf
source_sha256: 63696ad045602440
doc_brief: "Circuit imbalance measures and linear programming ∗ — We study properties and applications of various circuit imbalance mea sures associated with linear spaces."
---
4.1 The condition number ¯χ and the lifting operator
For a full row rank matrix A∈ Rm×n, the condition number ¯χA can be deﬁned in the following
two equivalent ways:
¯χA = sup
{ ‖‖‖‖A⊤
(
ADA⊤
)−1
AD
‖‖‖‖ :D∈ Dn
}
= sup
{ ‖‖A⊤y
‖‖
‖p‖ :y minimizes
‖‖‖D1/2(A⊤y−p)
‖‖‖ for some 0 ⁄=p∈ Rn and D∈ Dn
}
.
(5)
This condition number was ﬁrst studied by Dikin [ Dik67], Stewart [ Ste89], and Todd [ Tod90].
There is an extensive literature on the properties and appli cations of ¯χA, as well as its relations
to other condition numbers. In particular, it plays a key rol e in layered-least-squares interior
point methods, see Section 7.2. We refer the reader to the papers [ HT02, MT03, VY96] for
further results and references.
It is important to note that—similarly to κA and ˙κA— ¯χA only depends on the subspace
W = ker(A). Hence, we can also write ¯χW for a subspace W⊆ Rn, deﬁned to be equal to ¯χA for
some matrixA∈ Rk×n withW = ker(A). We will use the notations ¯χA and ¯χW interchangeably.
The following characterization reveals the connection bet weenκA and ¯χA.
Proposition 4.1 ([TTY01]). For a full row rank matrix A∈ Rm×n,
¯χA = max{‖A−1
B A‖ :AB is a non-singular m×m-submatrix of A}.
Together with Proposition 3.1, this shows that the diﬀerence between ¯ χA andκA is in using
ℓ2 instead of ℓ∞ norm. This immediately implies the upper bound and a slightl y weaker lower
bound in the next theorem.
Theorem 4.2 ([DHNV20, DNV20]). For a matrix A∈ Rm×n we have
√
1 +κ2
A≤ ¯χA≤nκA.
Approximating the condition number ¯χA is known to be hard; by the same token, ¯ κA also
cannot be approximated by any polynomial factor. The proof r elies on the hardness of approx-
imating the minimum subdeterminant by Khachiyan [ Kha95].
Theorem 4.3 (Tun¸ cel [Tun99]). Approximating ¯χA up to a factor of 2poly(n) is NP-hard.
In connection with ¯χA, it is worth mentioning the lifting map, a key concept in the algorithms
presented in Section 7. The map LW
I : πI (W )→ W lifts back a vector from a coordinate
projection of W to a minimum-norm vector in W :
LW
I (p) = arg min{‖z‖ :zI =p,z∈W}.
Note that LW
I is the unique linear map from πI (W ) to W such that LW
I (p)I =p and LW
I (p) is
orthogonal toW∩Rn
[n]\I. The condition number ¯χW can be equivalently deﬁned as the maximum
norm of any lifting map for an index subset.
15
Proposition 4.4 ([DHNV20, O’L90, Ste89]). For a linear subspace W⊆ Rn,
¯χW = max
{
‖LW
I ‖ :I⊆ [n],I ⁄=∅
}
.
Even though LW
I is deﬁned with respect to the ℓ2-norm, it can also be used to characterize
κW .
Proposition 4.5 ([DNV20]). For a linear subspace W⊆ Rn,
κW = max
{‖LW
I (p)‖∞
‖p‖1
:I⊆ [n],I ⁄=∅,p∈πI (W )\{ 0}
}
.
Proof. We ﬁrst show that for any I⁄=∅, and p∈ πI(W )\{ 0},‖LW
I (p)‖∞≤ κW‖p‖1 holds.
Let z = LW
I (p), and take a conformal decomposition z = ∑ h
k=1gk as in Lemma 2.1. For each
k∈ [h], let Ck = supp(gk). We claim that all these circuits must intersect I. Indeed, assume for
a contradiction that one of them, say C1 is disjoint from I, and let z′ = ∑ h
k=2gk. Then, z′∈W
and z′
I = zI = p. Thus, z′ also lifts p to W , but ‖z′‖2 <‖z‖2, contradicting the deﬁnition of
z =LW
I (p) as the minimum-norm lift of p.
By the deﬁnition of κW , ‖gk‖∞ ≤ κW‖gk
I‖1 for each k ∈ [h]. The claim follows since
p =zI = ∑ h
k=1gk
I , moreover, conformity guarantees that ‖p‖1 = ∑ h
k=1‖gk
I‖1. Therefore,
‖z‖∞≤
h∑
k=1
‖gk‖∞≤κW
h∑
k=1
‖gk
I‖1 =κW‖p‖1.
We have thus shown that the maximum value in the statement is a t most κW . To show that
equality holds, let C∈C W be the circuit and gC∈W the corresponding elementary vector and
i,j∈C such that κW =|gC
j /gC
i|.
Let us set I = ([n]\C)∪{i}, and deﬁne pk = 0 if k∈ [n]\C andpi =gC
i . Then p∈πI (W ),
and the unique extension to W is gC ; thus, LW
I (p) = gC. We have ‖LW
I (p)‖∞ =|gC
j|. Noting
that‖p‖1 =|gC
i|, it follows that κW =‖LW
I (p)‖∞/‖p‖1.
4.2 The condition number δ and bounds on diameters of polyhedra
Another related condition number is δ, deﬁned as follows:
Deﬁnition 4.6. LetV⊆ Rn be a set of vectors. Then δV is the largest value such that for any
set of linearly independent vectors {vi : i∈I}⊆ V and λ∈ RI ,
‖‖‖‖‖
∑
i∈I
λivi
‖‖‖‖‖≥δV max
i∈I
|λi|·‖ vi‖.
For a matrix M∈ Rm×n, we let δM denote the value associated with the rows M 1,M 2,...,M m
of M .
This can be equivalently characterized as follows: for a sub set{vi : i∈I}⊆ V and vj∈V ,
vj /∈W = span({vi : i∈I}), the sine of the angle between the vector vj and the subspace W is
at least δV (see e.g. for the equivalence [ DVZar]).
A line of work studied this condition number in the context of the simplex algorithm and
diameter bounds. The diameter of a polyhedron P is the diameter of the vertex-edge graph
associated withP ; Hirsch’s famous conjecture from 1957 asserted that the dia meter of a polytope
(a bounded polyhedron) in n dimensions with m facets is at most m−n. This was disproved by
Santos in 2012 [ San12], but the polynomial Hirsch conjecture, i.e., a poly( n,m ) diameter bound
remains wide open.
16
Consider the LP in standard inequality form with n variables and m constraints as
max⟨c,x⟩ s.t.x∈P, P ={x∈ Rn : Ax≤b}, (6)
for A∈ Rm×n, b∈ Rm. Using a randomized dual simplex algorithm, Dyer and Frieze [DF94]
showed the polynomial Hirsch conjecture for TU matrices. Bo nifas et al. [ BDSE+14] strength-
ened and extended this to the bounded subdeterminant case, s howing a diameter bound of
O(n4∆ 2
A log(n∆ A)) for integer constraint matrices A∈ Zm×n. Note that this is independent of
the number of constraints m.
Brunsch and R¨ oglin [BR13] analyzed the shadow vertex simplex algorithm in terms of th e
condition number δA, noting that for integer matrices δA≥ 1/(n∆ 2
A). They gave a diameter
bound O(mn2/δ2
A). Eisenbrand and Vempala [ EV17] used a diﬀerent approach to derive a
bound poly(n, 1/δA) that is independent of m. Dadush and H¨ ahnle [ DH16] further improved
these bounds to O(n3 log(n/δA)/δA).
In recent work, Dadush et al. [ DVZar] considered ( 6) in the oracle model, where for each
point x∈ Rn, the oracle returns x∈ P or a violated inequality ⟨ai,x⟩≤ bi from the system
Ax≤ b. Their algorithm ﬁnds exact primal and dual solutions using O(n2 log(n/δM )) oracle
calls, where M =
(0 1
A b
)
; the running time is independent of the cost function c. They also
show the following relation between κ and δ:
Lemma 4.7 ([DVZar]). (i) Let A∈ Rm×n be a matrix with full row rank and m < n, with
‖ai‖ = 1 for all columns i∈ [n]. Then, κA≤ 1/δA⊤.
(ii) Let A∈ Rm×n be in basis form A = (Im|A′). Then, 1/δA⊤≤mκ2
A.
(iii) If B is the basis maximizing | det(AB)|, then for ¯A =A−1
B A, it holds that 1/δ ¯A⊤≤mκA.
Proof. Part (i): Let g ∈ F(A) be an elementary vector. Select an arbitrary i∈ supp(g),
and let J = supp(g)\{i}. Then, the columns {gi : i ∈ J} are linearly independent, and
−giai = ∑
j∈Jgjaj. Thus,
|gi|·‖ ai‖ =
‖‖‖‖‖‖
∑
j∈J
gjaj
‖‖‖‖‖‖
≥δA⊤ max
j∈J
|gj|·‖ aj‖,
and using that all columns have unit norm, we get |gj/gi|≤ 1/δA⊤ for all j∈ J. This shows
that κA≤ 1/δA⊤ .
Parts (ii) and (iii): Let A = (Im|A′) in basis form, and let α = maxi∈[n]‖Ai‖. Let us ﬁrst
show
1/δA⊤≤√mακA. (7)
Take any set{Ai : i∈I} of linearly independent columns of A, along with coeﬃcients λ∈ RI .
Without loss of generality, assume |I| = m, i.e., I is a basis, by allowing λi = 0 for some
coeﬃcients. Let z = ∑
i∈IλiAi. Then, λ =A−1
I z. Lemma 3.3 implies that every column of A−1
I
has 2-norm at most √mκA. Hence, |λi|≤ √mκA‖z‖ holds for all i∈I, implying ( 7).
Then, part (ii) follows since ‖Ai‖≤ √mκA by Proposition 3.1. For part (iii), let B be a
basis maximizing | det(AB)|. Then, ‖A−1
B A‖∞≤ 1. Indeed, if there is an entry |Aij|> 1, then
we can obtain a larger determinant by exchanging i for j. This implies α≤√m.
Using this correspondence between δ andκ, we can derive the following bound on the diam-
eter of polyhedra in standard form from [ DH16]. This veriﬁes the polynomial Hirsch-conjecture
wheneverκA is polynomially bounded.
17
Theorem 4.8. Consider a polyhedron in the standard equality form
P ={x∈ Rn : Ax =b,x≥ 0}
for A∈ Rm×n and b∈ Rm. Then, the diameter of P is at most O((n−m)3mκA log(κA +n)).
Proof. Without loss of generality, we can assume that A has full row rank. Changing to a
standard basis representation does neither change the geom etry (in particular, the diameter) of
P , nor the value of κA. Let B be the basis maximizing det( AB), and let us replace A byA−1
B A;
w.l.o.g. assume that B is the set of the last m columns. Hence, A = (A′|Im) for A′∈ Rm×(n−m).
According to Lemma 3.6, P has the same diameter as P ′ deﬁned as
P ′ ={x′∈ Rn−m : A′x′≤b,x ′≥ 0},
in other words, P ′ ={x′ ∈ Rn−m : Cx ′≤ d}, where C =
(−In−m
A′
)
and d =
(0
b
)
. There is
a one-to-one correspondence between the vertices and edges of P and P ′, and hence, the two
polyhedra have the same diameter. Thus, [ DH16] gives a bound O((n−m)3 log(n/δC )/δC ) on
the diameter of P ′. By the choice of B, from Lemma 4.7(iii), we obtain the diameter bound
O((n−m)3mκC⊤ log(κC⊤+n)). We claim that κC⊤ =κA. Indeed, the kernels of A = (A′|Im) and
C ⊤ = (−In−m|(A′)⊤) represent orthogonal complements, thus κC⊤ = κA by Proposition 3.14.
This completes the proof.
The diameter bound in [ DH16] is proved constructively, using the shadow simplex method .
However, in the proof we choose B maximizing| det(AB)|, a hard computational problem to
solve even approximately [ DSEFM14]. However, we do not actually require a (near) maximizing
subdeterminant. For the argument, we only need to ﬁnd a basis B⊆ [n] such that for ¯A =A−1
B A,
‖ ¯A‖∞≤µ for some constant µ> 1. Then, ( 7), gives 1/δ ¯A⊤≤mµκA.
Such a basis B corresponds to approximate local subdeterminant maximiza tion, and can
be found using the following simple algorithm proposed by Kn uth [ Knu85]. As long as there
is an entry |Aij| > µ, then swapping i for j increases| det(AB)| by a factor |Aij| > µ. Using
that| det(AB)| ≤( ˙κW )m by Proposition 3.19, the algorithm terminates in O(m log( ˙κW/µ))
iterations.
We also note that δA was also studied for lattice basis reduction by Seysen [ Sey93]. A
related quantity has been used to characterize Hoﬀman consta nts (introduced in Section 6), see
[GHR95, KT95, PVZ20].
