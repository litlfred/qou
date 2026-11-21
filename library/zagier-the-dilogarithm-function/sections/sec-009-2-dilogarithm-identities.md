---
doc_id: zagier-the-dilogarithm-function
doc_title: "The Dilogarithm Function"
section_id: sec-009-2-dilogarithm-identities
section_title: "Dilogarithm identities"
section_number: 2
pages: 31-39
source_pdf: zagier-the-dilogarithm-function.pdf
source_sha256: 05079cf525c6ba0f
toc_source: inferred
doc_brief: "The Dilogarithm Function — 14 sections: Front matter; The dilogarithm function in geomet; Special values"
---
In Chapter I of this paper we discussed both functional equations of the dilog-
arithm function and numerical identities involving the values of dilogarithms
at algebraic arguments. Here we discuss both topics in more detail. In subsec-
tion A we give the algebraic characterization of arbitrary functional equations
of the dilogarithm and prove Wojtkowiak’s theorem that all functional equa-
tions whose arguments are rational functions of one variable are consequences
of the ﬁve-term functional equation. In subsections B and C we discuss speciﬁc
examples of identities of the form 
 D(αi) = 0 or 
 L(αi) ∈Q π2, where the
αi are complex or real algebraic numbers, respectively, and describe a general
method for producing such examples.
A key role in all these considerations is played by the ﬁve-term relation.
We recall its statement from Chapter I. A sequence of {xi}i∈Z of real or com-
plex numbers such that 1 −xi = xi−1xi+1 for all i automatically satisﬁes
xi+5 = xi . By a 5-cycle we mean any (cyclically ordered) 5-tuple of numbers
obtained in this way. Equivalently, a 5-cycle can be deﬁned as the set of cross-
ratios of the ﬁve (appropriately ordered) sub-4-tuples of a set of 5 distinct
points in the projective line, or—in a diﬀerent ordering—simply as any set of
the form

x, y, 1 −x
1 −xy , 1 −xy, 1 −y
1 −xy

with x, y̸ ∈{0, 1, ∞}, xy̸ = 1. The
ﬁve-term equation in its various guises says that the sum of the values of the
Bloch-Wigner dilogarithm D at arguments belonging to a 5-cycle of complex
numbers, or of the Rogers dilogarithm L (mod π2/2) at the numbers of a real
5-cycle, vanishes. This fact and related algebraic properties of 5-cycles turn
up in a surprising number of contexts in quite diﬀerent parts of mathemat-
ics: in the theory of webs (Bol’s counterexample and correction to a theorem
of Blaschke, later generalized by Chern and Griﬃths [9]), in the study of
the torsion in the group of birational transformations (Cremona transforma-
tions) of P2(C) [1], in the study of the 1-dimensional Schr¨odinger equation for
34
Don Zagier
the potential |x|3
[39], and in the study of the symmetry properties of the
Ap´ery-Beukers-type integrals leading to the best currently known irrational-
ity measures for π2 [34]. However, we will not discuss these connections here,
restricting ourselves only to the aspects directly related to the dilogarithm.
A. Functional equations of the dilogarithm. By a “functional equation
of the dilogarithm” we mean any collection of integers ni and rational or al-
gebraic functions xi(t) of one or several variables such that 
 niLi2(xi(t)) is
a ﬁnite combination of products of two logarithms, or such that 
 niD(xi(t))
(resp. 
 niL(xi(t)) if all the xi(t) are real) is constant (resp. locally constant).
A number of examples were given in Section 2 of Chapter I, with only the
statement “All of the functional equations of Li2 are easily proved by diﬀer-
entiation” by way of proof. That is a true, but somewhat ad hoc, statement,
since it does not give an algebraic way to recognize or characterize functional
equations of the dilogarithm. It is, however, easy to give such a criterion ([45],
Prop. 1 of §7): it is necessary and suﬃcient that 
 ni(xi(t)) ∧(1 −xi(t)) be
independent of t, i.e., that the element ξ = 
 ni[xi(t)] of the group ring of
the function ﬁeld in which the xi lie be in the kernel of the boundary map
∂: [x] →(x) ∧(1 −x) used to deﬁne the Bloch group (cf. §4 of Chapter I or
§4 below). For convenience, we ignore 2-torsion.
Let us check this criterion for each of the functional equations given in
§2 of Chapter I. For the one-variable functional equations corresponding to
ξ = [x] + [1 −x] or ξ = [x] + [1/x] the statement ∂(ξ) = 0 is trivial. For the
ﬁve-term equation we can either verify directly that the 5-term expression
V (x, y) = [x] + [y] +

 1 −x
1 −xy

+ [1 −xy] +

 1 −y
1 −xy

(17)
is annihilated by ∂or else use the more symmetric description of the ﬁve-term
relation as ξ = 
i (mod 5)[xi] with 1 −xi = xi−1xi+1 and then calculate
∂(ξ) =

i
(xi) ∧(xi−1xi+1) =

i

(xi) ∧(xi−1) −(xi+1) ∧(xi)

= 0 .
Similarly, the six-term relation of Kummer and Newman corresponds to
ξ = 2

i
[xi] −

i
[−xi−1xi+1/xi] ,
where {xi}i∈Z/3Z is a cyclically numbered triple of numbers with 
 x−1
i
= 1,
and here we ﬁnd
∂(ξ) =

i

2 (xi) ∧(1 −xi) −(−xi−1xi+1/xi) ∧((1 −xi−1)(1 −xi+1))

=

j

2(xj) −(−xjxj−1/xj+1) −(−xj+1xj/xj−1)

∧(1 −xj) = 0 .
The Dilogarithm Function
35
Finally, the “strange many-variable equation” given in eq. (1) of Chapter I
corresponds to the expression
ξ = [z] −
n

i=1
n

j=1
[xi/aj] ,
where x1, . . . , xn and a1, . . . , an are the roots (counted with multiplicity) of
f(x) = z and f(a) = 1, respectively, for some polynomial f of degree n
without constant term. Then from the two identities C 
i(t −xi) = f(t) −z
and C 
j(t −aj) = f(t) −1, where C̸ = 0 is the coeﬃcient of tn in f(t), we
ﬁnd (modulo 2-torsion)
∂(ξ) = (z) ∧(1 −z) −
n

i=1
(xi) ∧
 n
	
j=1
aj −xi
aj

+
n

j=1
(aj) ∧
 n
	
i=1
(aj −xi)

= (z) ∧(1 −z) −
n

i=1
(xi) ∧(1 −z) +
n

j=1
(aj) ∧
1 −z
C

= (z) ∧(1 −z) −
(−1)n−1z
C

∧(1 −z) +
(−1)n−1
C

∧
1 −z
C

= 0 .
The corresponding calculation for the yet more general functional equation
given in the ﬁrst line after equation (6) of Chapter I is left to the reader.
As already mentioned, the criterion 
 ni

xi(t)

∧

1 −xi(t)

= 0 for a
functional equation of the dilogarithm can be reformulated as saying that
the element ξ = 
 ni[xi(t)] belongs to the Bloch group of the corresponding
function ﬁeld. It is then reasonable to ask whether it in fact must be zero
in this Bloch group, i.e., whether ξ is necessarily equal (modulo Z[C]) to a
linear combination of ﬁve-term relations. This is conjectured, but not known
to be true, when the xi(t) are allowed to be algebraic functions or rational
functions of more than one variable. But in the case of rational functions of
one variable, an elementary proof was found by Wojtkowiak. We reproduce
his argument here in a slightly modiﬁed form.
Proposition 4 [40]. (i) Any rational function of one variable is equivalent
modulo the ﬁve-term relation to a linear combination of linear functions.
(ii) Any functional equation of the dilogarithm with rational functions of one
variable as arguments is a consequence of the ﬁve-term relation.
(Part (ii) is to be interpreted up to constants, i.e. the ﬁve-term relation suﬃces
to give all relations 
i D(xi(t)) = C but not necessarily to determine C.)
Proof. (i) Let f(t) be an element of the ﬁeld C(t) of rational functions in one
variable. We want to show that the element [f] ∈Z[C(t)] is equivalent modulo
ﬁve-term relations to a Z-linear combination of elements of the form [ait+bi].
We do this by induction on the degree. Write f(t) as A(t)/B(t), where A(t) and
36
Don Zagier
B(t) are polynomials of degree ≤n, not both constant. Since we are working
modulo the ﬁve-term relation, we can replace f by 1/f or 1/(1−f) if necessary
to ensure that both A(t) and C(t) := B(t) −A(t) are non-constant. Choose
a root a of A(t) and a root c of C(t) and set g(t) = c −a
t −a , A∗(t) = g(t)A(t)
and D(t) = B(t)−A∗(t), so that deg(A∗) ≤n−1, deg(D) ≤n, and D(c) = 0.
Then modulo the ﬁve-term relation, we have
[f] ≡−[g] + [fg] −

 1 −f
1 −fg

+

1 −1 −g
1 −fg

≡−
c −a
t −a

+
A∗(t)
B(t)

−
 C(t)/(t −c)
D(t)/(t −c)

+
(c −a)C(t)/(t −c)
(t −a)D(t)/(t −c)

.
Here each rational function appearing on the right has a numerator of degree
≤n −1 and a denominator of degree ≤n. Moreover, if B has degree ≤n −1,
then all terms on the right have both numerator and denominator of degree
≤n−1. Therefore we have reduced any rational function with numerator and
denominator of degrees ≤(n, n) to a combination of rational functions with
numerator and denominator of degrees ≤(n−1, n), and any rational function
with numerator and denominator of degrees ≤(n −1, n) to a combination of
rational functions with numerator and denominator of degrees ≤(n−1, n−1).
Iterating this procedure, we can keep reducing the degrees until we get to (0,1),
i.e. (after inversion), until only linear functions appear. (Note that the number
of applications of the ﬁve-term relation needed to reduce a rational function
to a linear combination of linear ones grows exponentially with the degree n;
more precisely, it is at most (1 +
√
2)2n/4.)
(ii) By what we have just proved, any element ξ = ξ(t) ∈Z[C(t)] can be
written modulo the 5-term relation as ξ0+
 ni[ℓi(t)], where ξ0 ∈Z[C], ni ∈Z
and the ℓi are non-constant linear functions of t. We can write each ℓi(t) as
(t −ci)/(c′
i −ci) with ci, c′
i ∈C distinct and (since we may replace [ℓi(t)] by
−[1−ℓi(t)] modulo the ﬁve-term relation) 0 ≤arg(c′
i−ci) < π. The derivative
of D(ℓi(t)) is proportional to (t −ci)−1 log |t −c′
i| −(t −c′
i)−1 log |t −ci|, and
since these functions are linearly dependent for diﬀerent i (as one sees by
looking at their singularities), we deduce that D(ξ(t)) is constant if and only
if ni = 0 for all i, i.e., if ξ(t) ≡ξ0 modulo the ﬁve-term relation, as claimed.
This proof also shows that every element of Z[C(t)]/(5-term relation) has a
unique representative of the form ξ0 + 
 ni[ait + bi] with 0 ≤arg(ai) < π.
B. Relations among special values of the dilogarithm. Relations among
values of D(α), or among values of L(α) modulo π2, correspond to torsion in
the Bloch group. (More precisely, an element of B[Q] is torsion if and only if
its Bloch-Wigner dilogarithm in all complex embeddings vanishes, in which
case its Rogers dilogarithm in all real embeddings is a rational multiple of π2.)
Such relations are of interest in various contexts in combinatorics (asymptotics
of certain q-hypergeometric series, like mock theta functions at roots of unity)
[24], [49] and mathematical physics (models in rational conformal ﬁeld theory,
The Dilogarithm Function
37
where the value of the Rogers dilogarithm divided by π2 corresponds to the
central charge) [17], [30]. If one has found a conjectural relation of this sort
(which can be done empirically, e.g. by computing lots of values of the Bloch-
Wigner or Rogers dilogarithm at algebraic arguments and searching for Z-
relations among them by the LLL algorithm), then one can always verify its
correctness by ﬁnding an explicit expression of some multiple of it as a linear
combination of ﬁve-term relations. We will describe a few examples and a
general construction.
(a) Recall that the ﬁve-term relation is 
[xi], where {xi} is a cyclically
ordered 5-tuple of numbers satisfying 1−xi = xi−1xi+1. The simplest example
is when xi = α for all i, where α is one of the two roots of the quadratic
equation 1 −α = α2, i.e., α = (−1 ±
√
5)/2. It follows that the element [α]
of Z[Q(
√
5)] is killed by 5 in the Bloch group for each of these two numbers.
That they are really 5-torsion and not trivial follows from the fact that the
corresponding values L((−1 ±
√
5)/2) = ±π2/10 of the Rogers dilogarithm
have the denominator 5 when divided by π2/6.
(b) We give a less trivial example which will be used in §3 in connection
with Nahm’s conjecture. Set ε = √α, with α = (−1+
√
5)/2 the inverse golden
ratio as in Example (a). The ﬁeld F = Q(ε) has two real and two (conjugate)
complex embeddings. Deﬁne ξ ∈Z[F] by
Q1 = ε ,
Q2 =
1
1 + ε ,
ξ = [Q1] + [Q2] .
(18)
From the identities
1 −Q1 = Q4
1 Q2 ,
1 −Q2 = Q1 Q2
(19)
we obtain
∂(ξ) = (Q1) ∧(4(Q1) + (Q2)) + (Q2) ∧((Q1) + (Q2)) = 0 ,
(20)
so ξ belongs to the Bloch group of F. To see that it is torsion, we use the
relation (17) with x = y = ε :
V (ε, ε) = 2 [ε] + 2

 1 −ε
1 −ε2

+

1 −ε2
= 2 ξ + [1 −α] ,
(21)
and since we have already seen in (a) that [α] and hence [1 −α] are 5-torsion
elements, this shows that 10 ξ = 0 in the Bloch group. To see that it really
has this denominator, we calculate that L(ξ)/L(1) = 13/10 (numerically, but
then exactly since we have just shown that 10 L(ξ)/L(1) must be an integer).
(c) In example (a), the torsion element in the Bloch group had the form
[x] for a single number x = (−1 ±
√
5)/2. Another such example, even more
obvious, is given by x = 1/2, for which x ∧(1 −x) = x ∧x = 0 and L(x) =
π2/12. We claim that the only torsion elements of the Bloch group of C of the
38
Don Zagier
form [x] with x ∈C ∖{0, 1} are these examples and the ones deduced from
them using [1/x] ≡−[x] and [1 −x] ≡−[x], i.e., the nine numbers x = 1/2,
−1, 2, (±1±
√
5)/2 and (3±
√
5)/2. (Compare this list with the special values
of the dilogarithm given in §1 of Chapter I.) Indeed, for the element [x] to
belong to the Bloch group of C after tensoring with Q), we must have that
x ∧(1 −x) = 0 up to torsion, i.e. x = αtp, 1 −x = βtq for some non-zero
complex number t, integers p and q, and roots of unity α and β. Moreover, x
must be totally real if [x] is to be torsion in BC, since this condition implies
that D(xσ) = 0 for all conjugates xσ and D is non-zero for non-real arguments
(cf. the picture in §3 of Chapter I), so we must in fact have x = ±t, 1−x = ±tq
with t totally real. Replacing x by one of the six numbers x, 1−x, 1/x, 1−1/x,
1/(1 −x) or x/(x −1), we may assume that 0 < 1 −x ≤x < 1 and hence
that x = tp, 1 −x = tq with 0 < t < 1 and q ≥p ≥1. But it is easily checked
that the only equations of the form tp + tq = 1 with q ≥p ≥1 which have
only real roots are t + t = 1 and t + t2 = 1, corresponding to x = 1/2 and
x = (
√
5 −1)/2, as claimed.
Remark about torsion. In examples (a) and (b), we showed that the
elements ξ under consideration were torsion in the Bloch group by writing
some multiple of them as a combination of ﬁve-term relations, and that they
were non-trivial by computing the Rogers dilogarithm L(ξ) and checking that
L(ξ)/L(1) had a non-trivial denominator. This method would not work if ξ
belonged to a number ﬁeld F having no real embeddings, but in that case we
could use instead the enhanced dilogarithm of §1B (with respect to a ﬁxed
embedding of F into C) and check numerically that its value was torsion
but not zero. This would also work, of course, for a ﬁeld having both real
and non-real embeddings , e.g. for example (b) and the embedding given
by ε =

(−1 −
√
5)/2. Note, however, that in contrast to the real case,
the statement that a torsion element of the Bloch group is non-trivial is not
absolute, but depends on the number ﬁeld, because it can happen that an
element which is non-trivial torsion in the Bloch group of one number ﬁeld
becomes trivial in the Bloch group of a larger ﬁeld containing more roots
of unity. A simple example where this happens is given by ξ = [−1] ∈BQ,
which is non-trivial in BR because the number L(−1)/L(1) = −1/2 is non-
integral, but which is trivial in BQ(i) because applying the duplication relation
[x2] ≡2[x] + 2[−x] (an easy consequence of the ﬁve-term relation) to x = i
gives [−1] ≡2[i]+2[1/i] ≡0. As a less trivial example, we saw in example (a)
that the inverse golden ratio α is 10-torsion in BF for F = Q(
√
5), but if we
pass to the ﬁeld F = Q(ζ), where ζ is a 5th root of unity, then it becomes
zero because modulo the relations [x] ≡−[1 −x] and [x] ≡−[x/(x −1)] we
have
V (−ζ, 1+ζ) = [−ζ] + [1+ζ] + [−ζ2] + [−ζ2/(−ζ2−1)] + [ζ3+ζ2+1] ≡[1/α] .
In fact, a theorem of Merkur’ev and Suslin [27] implies that this phenom-
enon always happens: every torsion element in the Bloch group of a number
The Dilogarithm Function
39
ﬁeld becomes trivial in the Bloch group of a larger number ﬁeld containing
suﬃciently many roots of unity.
C. Dilogarithm identities from triangulated 3-manifolds. Finally, we
describe a simple method for producing examples of torsion elements in Bloch
groups, using combinatorial triangulated 3-manifolds. (See also [18].) For this
purpose, it is convenient to think of L or D as functions of real or complex
oriented 3-simplices. By an oriented n-simplex in P1(C) we mean an (n + 1)-
tuple of points in P1(C) together with an ordering up to even permutations;
more precisely, such a simplex has the form [x0, . . . , xn] with xj ∈P1(C)
and with the convention that [xπ(0), . . . , xπ(n)] = sgn(π) [x0, . . . , xn] for π ∈
Sn+1 . Let Cn denote the free abelian group on oriented n-simplices. There are
boundary maps ∂: Cn →Cn−1 deﬁned by the usual formula ∂([x0, . . . , xn]) =

n
i=0(−1)i[x0, . . . , xi, . . . , xn], and the sequence (with ε([x]) = 1)
· · · −→C4
∂
−→C3
∂
−→C2
∂
−→C1
∂
−→C0
ε
−→Z −→0
(22)
is exact. The function D : C →R deﬁnes a function D : C3 →R which
associates to a 3-simplex in P1(C) the value of D on the cross-ratio of its
vertices, D([a, b, c, d]) = D
 a−d
a−c
b−c
b−d

, as in Chapter I. This is well-deﬁned (i.e.,
transforms under the action of π ∈S4 by sgn(π)) and is 0 on ∂(C4) by the ﬁve-
term relation, since the element V (x, y) in (17) is simply the boundary of the
4-simplex [∞, 0, x, 1, y−1] and any 4-simplex is equivalent to such a one under
the action of PGL2(C) on C3. (Notice that D is invariant under the action
of PGL2(C) on C3, since the cross-ratio is.) Because of the exactness of (22),
we can say equivalently that D vanishes on Ker(C3
∂→C2) or that it factors
through ∂: if we deﬁne a map
≈
D : C2 →R by
≈
D([a, b, c]) = −D([a, b, c, ∞])
(here “∞” could be replaced by any other ﬁxed base-point x0 ∈P1(C)), then
for every oriented 3-simplex [a, b, c, d] ∈C3 we have
≈
D

∂([a, b, c, d])

=
≈
D

−[a, b, c] + [a, b, d] −[a, c, d] + [b, c, d]

= D

[a, b, c, ∞] −[a, b, d, ∞] + [a, c, d, ∞] −[b, c, d, ∞]

= D

[a, b, c, d] −∂([a, b, c, d, ∞])

= D([a, b, c, d])
and hence D =
≈
D ◦∂.
We can think of an element ξ of Ker(C3
∂→C2) as a closed, triangulated,
oriented near-3-manifold M, smooth except possibly at its vertices (it is a
union of oriented tetrahedra glued to each other along their faces, and is
hence automatically smooth on the interior of its 3-, 2- or 1-simplices, while
at a vertex its topology is that of a cone on some compact oriented surface),
together with a map φ from the vertices of M to P1(C). Any such element ξ =
40
Don Zagier

[σi] gives an identity D(M, φ) := 
 D(σi) = 0 among values of the Bloch-
Wigner dilogarithm. This identity can be written explicitly as a combination
of ﬁve-term equations by the calculation above (just replace each simplex
σ = [a, b, c, d] of M by [σ, ∞] := [a, b, c, d, ∞]). We can also perform the same
construction over R, starting from a triangulated near-3-manifold M and a
map φ from its 0-skeleton to P1(R) ; then the element L(M, φ) deﬁned as the
sum over the 3-simplices σ of M of the value of L at the cross-ratio of the
images of the vertices of σ under φ will be an integral multiple of π2/2 by
virtue of the functional equation of the Rogers dilogarithm.
Here is an example. Let M be the join of an m-gon and an n-gon,
where m and n are two positive integers. If we write these two polygons
as {xj}j (mod m) and {yk}k (mod n), then this means that M is the union of
3-simplices [xj, xj+1, yk, yk+1] (j ∈Z/mZ, k ∈Z/nZ). Then
∂(M) =

j, k

[xj+1, yk, yk+1]−[xj, yk, yk+1]+[xj, xj+1, yk+1]−[xj, xj+1, yk]

vanishes because the ﬁrst two terms in the parentheses cancel when we sum
over all j with k ﬁxed and the last two when we sum over all k with j ﬁxed. If
we map the m+n vertices of M to points xj, yk ∈C (which we simply denote
by the same letters, omitting the map φ), then we get a functional equation

j (mod m), k (mod n)
D
yk −yk+1
yk −xj
xj −xj+1
yk+1 −xj+1

= 0 ,
valid for any complex numbers xj, yk. Specializing to xj = e2iXj, yk = e2iYk
with Xj, Yk ∈R gives real cross-ratios and a Rogers dilogarithm identity
2
π2

j (mod m), k (mod n)
L
sin(Yk −Yk+1)
sin(Yk −Xj)
sin(Xj −Xj+1)
sin(Yk+1 −Xj+1)

∈Z ,
where the value of the resulting integer depends on the ordering of the points
Xj and Yk on the circle R/πZ. In particular, if they are equally spaced we
ﬁnd
1
π2

j (mod m)
k (mod n)
L

sin
π
n

sin
 π
m

sin
kπ
n −jπ
m + t

sin
(k + 1)π
n
−(j + 1)π
m
+ t


= min(m, n) −1.
If also m = n, then each term occurs n times, so the equation reduces to
1
π2

k (mod n)
L

sin2π
n

sin2kπ
n + t


= 1 −1
n
(n ∈N, t ∈R) .
The Dilogarithm Function
41
Finally, specializing a fourth time to t = 0 and using L(+∞) = π2/3 = 2L(1),
we ﬁnd
L(1)−1

0<k<n
L
 sin2(π/n)
sin2(kπ/n)

= 4 −6
n ,
an equation well known in the physics literature.
