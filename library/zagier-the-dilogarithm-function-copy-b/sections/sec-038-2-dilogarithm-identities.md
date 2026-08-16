---
doc_id: zagier-the-dilogarithm-function-copy-b
doc_title: "The Dilogarithm Function Don Zagier"
section_id: sec-038-2-dilogarithm-identities
section_title: "Dilogarithm identities"
section_number: 2
pages: 31-35
source_pdf: zagier-the-dilogarithm-function-copy-b.pdf
source_sha256: c584944a501ef0c5
doc_brief: "The Dilogarithm Function Don Zagier — 56 sections: Don Zagier; The dilogarithm function in geomet; The Bloch-Wigner function D(z) and"
duplicate_of: "zagier-the-dilogarithm-function"
---
In Chapter I of this paper we discussed both functional equations of the dilog-
arithm function and numerical identities involving the values of di logarithms
at algebraic arguments. Here we discuss both topics in more detail. In sub sec-
tion A we give the algebraic characterization of arbitrary functional equations
of the dilogarithm and prove Wojtkowiak’s theorem that all functional eq ua-
tions whose arguments are rational functions of one variable are consequence s
of the ﬁve-term functional equation. In subsections B and C we discuss speciﬁc
examples of identities of the form ∑ D(αi)=0o r ∑ L(αi) ∈ Q π2, where the
αi are complex or real algebraic numbers, respectively, and describe a ge neral
method for producing such examples.
A key role in all these considerations is played by the ﬁve-term rel ation.
We recall its statement from Chapter I. A sequence of {xi}i∈Z of real or com-
plex numbers such that 1 − xi = xi−1xi+1 for all i automatically satisﬁes
xi+5 = xi .B ya 5-cycle we mean any (cyclically ordered) 5-tuple of numbers
obtained in this way. Equivalently, a 5-cycle can be deﬁned as the se t of cross-
ratios of the ﬁve (appropriately ordered) sub-4-tuples of a set of 5 dist inct
points in the projective line, or—in a diﬀerent ordering—simply as an y set of
the form
(
x, y, 1 − x
1 − xy , 1 − xy, 1 − y
1 − xy
)
with x, y ⁄∈{ 0, 1, ∞}, xy ⁄=1 .T h e
ﬁve-term equation in its various guises says that the sum of the values of the
Bloch-Wigner dilogarithm D at arguments belonging to a 5-cycle of complex
numbers, or of the Rogers dilogarithm L (mod π2/2) at the numbers of a real
5-cycle, vanishes. This fact and related algebraic properties of 5-cycl es turn
up in a surprising number of contexts in quite diﬀerent parts of mat hemat-
ics: in the theory of webs (Bol’s counterexample and correction to a th eorem
of Blaschke, later generalized by Chern and Griﬃths [9]), in the stud y of
the torsion in the group of birational transformations (Cremona transforma-
tions) of P2(C) [1], in the study of the 1-dimensional Schr¨ odinger equation for
34 Don Zagier
the potential |x|3 [39], and in the study of the symmetry properties of the
Ap´ery-Beukers-type integrals leading to the best currently know n irrational-
ity measures for π2 [34]. However, we will not discuss these connections here,
restricting ourselves only to the aspects directly related to th e dilogarithm.
A. F unctional equations of the dilogarithm. By a “functional equation
of the dilogarithm” we mean any collection of integers ni and rational or al-
gebraic functions xi(t) of one or several variables such that ∑ niLi2(xi(t)) is
a ﬁnite combination of products of two logarithms, or such that ∑ niD(xi(t))
(resp.∑ niL(xi(t)) if all the xi(t) are real) is constant (resp. locally constant).
A number of examples were given in Section 2 of Chapter I, with only the
statement “All of the functional equations of Li 2 are easily proved by diﬀer-
entiation” by way of proof. That is a true, but somewhat ad hoc, statemen t,
since it does not give an algebraic way to recognize or characterize funct ional
equations of the dilogarithm. It is, however, easy to give such a crite rion ([45],
P r o p .1o f§7): it is necessary and suﬃcient that ∑ ni(xi(t)) ∧ (1 − xi(t)) be
independent of t, i.e., that the element ξ =∑ ni[xi(t)] of the group ring of
the function ﬁeld in which the xi lie be in the kernel of the boundary map
∂ :[ x] ↦→(x) ∧ (1 − x) used to deﬁne the Bloch group (cf. §4 of Chapter I or
§4 below). For convenience, we ignore 2-torsion.
Let us check this criterion for each of the functional equations given in
§2 of Chapter I. For the one-variable functional equations corresponding t o
ξ =[ x]+[ 1 − x]o r ξ =[ x]+[ 1 /x] the statement ∂(ξ) = 0 is trivial. For the
ﬁve-term equation we can either verify directly that the 5-term ex pression
V (x, y)=[ x]+[ y]+
[ 1 − x
1 − xy
]
+[ 1 − xy]+
[ 1 − y
1 − xy
]
(17)
is annihilated by ∂ or else use the more symmetric description of the ﬁve-term
relation as ξ =∑
i (mod 5) [xi] with 1 − xi = xi−1xi+1 and then calculate
∂(ξ)=
∑
i
(xi) ∧ (xi−1xi+1)=
∑
i
(
(xi) ∧ (xi−1) − (xi+1) ∧ (xi)
)
=0 .
Similarly, the six-term relation of Kummer and Newman corresponds to
ξ =2
∑
i
[xi] −
∑
i
[−xi−1xi+1/xi] ,
where {xi}i∈Z/3Z is a cyclically numbered triple of numbers with ∑ x−1
i =1 ,
and here we ﬁnd
∂(ξ)=
∑
i
(
2( xi) ∧ (1 − xi) − (−xi−1xi+1/xi) ∧ ((1 − xi−1)(1 − xi+1))
)
=
∑
j
(
2(xj) − (−xjxj−1/xj+1) − (−xj+1xj/xj−1)
)
∧ (1 − xj)=0 .
The Dilogarithm Function 35
Finally, the “strange many-variable equation” given in eq. (1) of Chapter I
corresponds to the expression
ξ =[ z] −
n∑
i=1
n∑
j=1
[xi/aj] ,
where x1,... ,x n and a1,... ,a n are the roots (counted with multiplicity) of
f (x)= z and f (a) = 1, respectively, for some polynomial f of degree n
without constant term. Then from the two identities C∏
i(t − xi)= f (t) − z
and C∏
j(t − aj)= f (t) − 1, where C ⁄= 0 is the coeﬃcient of tn in f (t), we
ﬁnd (modulo 2-torsion)
∂(ξ)=( z) ∧ (1 − z) −
n∑
i=1
(xi) ∧
( n∏
j=1
aj − xi
aj
)
+
n∑
j=1
(aj) ∧
( n∏
i=1
(aj − xi)
)
=( z) ∧ (1 − z) −
n∑
i=1
(xi) ∧ (1 − z)+
n∑
j=1
(aj) ∧
( 1 − z
C
)
=( z) ∧ (1 − z) −
( (−1)n−1z
C
)
∧ (1 − z)+
( (−1)n−1
C
)
∧
( 1 − z
C
)
=0 .
The corresponding calculation for the yet more general functional equati on
given in the ﬁrst line after equation (6) of Chapter I is left to the read er.
As already mentioned, the criterion ∑ ni
(
xi(t)
)
∧
(
1 − xi(t)
)
=0f o ra
functional equation of the dilogarithm can be reformulated as saying that
the element ξ =∑ ni[xi(t)] belongs to the Bloch group of the corresponding
function ﬁeld. It is then reasonable to ask whether it in fact must be zero
in this Bloch group, i.e., whether ξ is necessarily equal (modulo Z[C]) to a
linear combination of ﬁve-term relations. This is conjectured, but n ot known
to be true, when the xi(t) are allowed to be algebraic functions or rational
functions of more than one variable. But in the case of rational functions of
one variable, an elementary proof was found by Wojtkowiak. We reproduc e
his argument here in a slightly modiﬁed form.
Proposition 4 [40]. (i) Any rational function of one variable is equivalent
modulo the ﬁve-term relation to a linear combination of linear fun ctions.
(ii) Any functional equation of the dilogarithm with rational f unctions of one
variable as arguments is a consequence of the ﬁve-term relation.
(Part (ii) is to be interpreted up to constants, i.e. the ﬁve-ter m relation suﬃces
to give all relations ∑
i D(xi(t)) = C but not necessarily to determine C.)
Proof. (i) Let f (t) be an element of the ﬁeld C(t) of rational functions in one
variable. We want to show that the element [ f ] ∈ Z[C(t)] is equivalent modulo
ﬁve-term relations to a Z-linear combination of elements of the form [ ait + bi].
We do this by induction on the degree. Write f (t)a s A(t)/B(t), where A(t)a n d
36 Don Zagier
B(t) are polynomials of degree ≤ n, not both constant. Since we are working
modulo the ﬁve-term relation, we can replace f by 1/f or 1/(1−f ) if necessary
to ensure that both A(t)a n d C(t): = B(t) − A(t) are non-constant. Choose
ar o o t a of A(t)a n dar o o t c of C(t) and set g(t)= c − a
t − a , A∗(t)= g(t)A(t)
and D(t)= B(t) − A∗(t), so that deg( A∗) ≤ n − 1, deg(D) ≤ n,a n d D(c)=0 .
Then modulo the ﬁve-term relation, we have
[f ] ≡− [g]+[ fg ] −
[ 1 − f
1 − fg
]
+
[
1 − 1 − g
1 − fg
]
≡−
[ c − a
t − a
]
+
[ A∗(t)
B(t)
]
−
[ C(t)/(t − c)
D(t)/(t − c)
]
+
[ (c − a)C(t)/(t − c)
(t − a)D(t)/(t − c)
]
.
Here each rational function appearing on the right has a numerator of degree
≤ n − 1 and a denominator of degree ≤ n. Moreover, if B has degree ≤ n − 1,
then all terms on the right have both numerator and denominator of degree
≤ n − 1. Therefore we have reduced any rational function with numerator and
denominator of degrees ≤ (n, n) to a combination of rational functions with
numerator and denominator of degrees ≤ (n − 1,n ), and any rational function
with numerator and denominator of degrees ≤ (n − 1,n ) to a combination of
rational functions with numerator and denominator of degrees ≤ (n−1,n −1).
Iterating this procedure, we can keep reducing the degrees unti l we get to (0,1),
i.e. (after inversion), until only linear functions appear. (Note that the number
of applications of the ﬁve-term relation needed to reduce a rational fun ction
to a linear combination of linear ones grows exponentially with the degre e n;
more precisely, it is at most (1 +
√
2)2n/4.)
(ii) By what we have just proved, any element ξ = ξ(t) ∈ Z[C(t)] can be
written modulo the 5-term relation as ξ0 +∑ ni[ℓi(t)], where ξ0 ∈ Z[C], ni ∈ Z
and the ℓi are non-constant linear functions of t. We can write each ℓi(t)a s
(t − ci)/(c′
i − ci) with ci,c ′
i ∈ C distinct and (since we may replace [ ℓi(t)] by
−[1−ℓi(t)] modulo the ﬁve-term relation) 0 ≤ arg(c′
i −ci) <π . The derivative
of D(ℓi(t)) is proportional to ( t − ci)−1 log |t − c′
i|− (t − c′
i)−1 log |t − ci|,a n d
since these functions are linearly dependent for diﬀerent i (as one sees by
looking at their singularities), we deduce that D(ξ(t)) is constant if and only
if ni = 0 for all i, i.e., if ξ(t) ≡ ξ0 modulo the ﬁve-term relation, as claimed.
This proof also shows that every element of Z[C(t)]/(5-term relation) has a
unique representative of the form ξ0 +∑ ni[ait + bi] with 0 ≤ arg(ai) <π .
B. Relations among special values of the dilogarithm. Relations among
values of D(α), or among values of L(α) modulo π2, correspond to torsion in
the Bloch group. (More precisely, an element of B[
Q] is torsion if and only if
its Bloch-Wigner dilogarithm in all complex embeddings vanishes, in which
case its Rogers dilogarithm in all real embeddings is a rational multiple of π2.)
Such relations are of interest in various contexts in combinatorics (asy mptotics
of certain q-hypergeometric series, like mock theta functions at roots of unit y)
[24], [49] and mathematical physics (models in rational conformal ﬁeld theor y,
The Dilogarithm Function 37
where the value of the Rogers dilogarithm divided by π2 corresponds to the
central charge) [17], [30]. If one has found a conjectural relation of this sort
(which can be done empirically, e.g. by computing lots of values of the B loch-
Wigner or Rogers dilogarithm at algebraic arguments and searching for Z-
relations among them by the LLL algorithm), then one can always verify its
correctness by ﬁnding an explicit expression of some multiple of it as a linear
combination of ﬁve-term relations. We will describe a few examples an d a
general construction.
(a) Recall that the ﬁve-term relation is ∑ [xi], where {xi} is a cyclically
ordered 5-tuple of numbers satisfying 1 −xi = xi−1xi+1. The simplest example
is when xi = α for all i, where α is one of the two roots of the quadratic
equation 1 − α = α2, i.e., α =( −1 ±
√
5)/2. It follows that the element [ α]
of Z[Q(
√
5)] is killed by 5 in the Bloch group for each of these two numbers.
That they are really 5-torsion and not trivial follows from the fact that the
corresponding values L((−1 ±
√
5)/2) = ±π2/10 of the Rogers dilogarithm
have the denominator 5 when divided by π2/6.
(b) We give a less trivial example which will be used in §3 in connection
with Nahm’s conjecture. Set ε = √α, with α =( −1+
√
5)/2 the inverse golden
ratio as in Example (a). The ﬁeld F = Q(ε) has two real and two (conjugate)
complex embeddings. Deﬁne ξ ∈ Z[F ]b y
Q1 = ε, Q 2 = 1
1+ ε ,ξ =[ Q1]+[ Q2] . (18)
From the identities
1 − Q1 = Q4
