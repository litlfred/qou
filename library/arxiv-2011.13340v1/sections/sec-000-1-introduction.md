---
doc_id: arxiv-2011.13340v1
doc_title: "A Matrix Bernstein Inequality for Strong Rayleigh Distributions*"
section_id: sec-000-1-introduction
section_title: "Introduction"
section_number: 1
pages: 1-10
source_pdf: 2011.13340v1.pdf
source_sha256: e73876ed2c923608
---
Concentration inequalities bound tail probabilities of ge neral functions of random variables. Sev-
eral methods have been known to prove such inequalities, inc luding martingale methods, infor-
mation theoretic methods, Talagrand’s induction method as well as a variety of problem-speciﬁc
methods. Ledoux (see [ Led99] for a survey) developed a powerful framework known as the "e n-
tropy method" for proving concentration inequalities. Thi s framework is concerned with proving
functional inequalities (like Poincare and log-Sobolev in equalities) which bound some global di-
vergence of any function whose concentration properties ar e of interest to us by quantities which
measure "local variation" of this function under some di ﬀusion process whose stationary measure
is our measure of interest. This framework can be used to reco ver strong forms of concentration
results for scalar functions which seem to be inaccessible through many other strategies for proving
*This paper was submitted to STOC 2020, during the process of w hich another paper [ ABY19] appeared which
proves a slightly stronger result. This note is being releas ed in its unedited form.
concentration. One prominent example of this is concentrat ion of scalar Lipshitz functionals of
distributions which are the stationary measure of some rapi d mixing markov chain. We refer to
the excellent book [ BLM13] for details on this and other methods for proving scalar con centration
inequalities. The entropy method has also been immensely us eful in proving deep theorems in the
analysis of boolean functions and we refer the reader to [O’D14] for more details on this fascinating
topic.
The ﬁeld of Matrix valued concentration of measure is concerne d with the phenomenon of
matrix valued functions being close (usually in spectral no rm) to their expected value with high
probability . In comparison to scalar concentration inequa lities, results on Matrix concentration
are much more recent. However, they have already had tremend ous applications in the ﬁeld
of computer science, statistics and information theory . So me examples include applications to
spectral graph theory , statistical learning problems, dee p learning, sketching . While a large
class of applications can be handled using matrix concentra tion of sums of independent random
matrices, there are several applications where there is som e dependence structure in the sums of
random matrices. Some examples of such applications are sim plifying Laplacian linear equations
(cite), semi-streaming graph sparsiﬁcation among others.
Despite the recent ﬂurry of activity in proving and using mat rix concentration inequalities,
as pointed out by [ CT13], one frequently encounters random matrices that do not sub mit to
existing techniques and the study of matrix concentration i nequalities remains an active area of
investigation.
Negative dependence of random variables is an intuitive pro perty that suggests that it might
help with concentration of measure. A class of negatively dependent measures are strong Rayleigh
measures which were introduced and deeply studied in the wor k of [ BBL09]. Examples of such
distributions include determinantal measures and random s panning tree distributions. [ BBL09]
show that strong Rayleigh distributions satisfy the strong est form of negative dependence prop-
erties. These negative dependence properties were recentl y exploited to design approximation
algorithms (cite) They have also been used in numerical line ar algebra and algorithmic fairness
for selecting subsets of elements which maximize some notio n of diversity .
In this paper, we are interested in understanding matrix con centration of random matrices
whose distribution is coming from the stationary distribut ion of a Markov chain. While some
results in this line of work exist in the work of [ PMT16, MJC+14] which extends Chaterjee’s work
[Cha05] on proving scalar concentration inequalities via Stein’s method. The kind of markov
chains that this line of work can handle is fairly restricted as it requires a stringent condition
known as the Dobrushin condition which is not always to prove . Nevertheless, these results
imply strong matrix concentration results in a variety of sc enarios, most notably matrix Efron
Stein inequalities. Another line of work is the paper of Chen and Tropp [ CT13] where they are
interested in extending the entropy method to the matrix val ued case. However, their results are
fairly restrictive since they require rotational symmetry of the random matrices. The reason for the
rotational symmetry requirement is the need for a "Herbst ar gument" which requires building a
diﬀerential equation for the exponential moment generating fu nction. However, since [ CT13] can
only control trace of quantities similar to variance and Dir ichlet form (which we also study here).
Since they are only controlling the trace, they can only tran sform the trace of those functions into a
2
diﬀerential form assuming rotational symmetry of those matric es which lets them ignore any non-
commutative structure of the sums of those random matrices. We refer the reader to [ CT13] for a
more detailed discussion. Our main idea here is to construct matrix valued functional inequalities
and show how these can be used to derive matrix concentration inequalities without any rotational
symmetry assumption. While we cannot prove matrix valued (m odiﬁed) log-Sobolev inequalities
we do show that matrix concentration by establishing matrix valued Poincare inequalities (which
are far more common for various markov chains as opposed to mo diﬁed log-sobolev). While our
techniques seem to be fairly general, we illustrate it for de riving matrix concentration for strongly
Rayleigh measures.
We now formally deﬁne strong Rayleigh measures. Let µ : 2 [n] → R+ be a probability distri-
bution on the subsets of [ n] = {1, 2, . . . ,n}. In particular, we assume that µ(·) is nonnegative and∑
S⊆[n]
µ(S) = 1. We associate a multi-a ﬃne polynomial with variables z1, . . . ,zn to µ
/g1µ(z1, . . . ,zn) =
∑
S⊆[n]
µ(S)
∏
i∈S
zi
The polynomial /g1µ is known as the generating polynomial of µ. We say µ is k-homogenous if /g1µ
is a homegenous polynomial of degree k. A polynomial p(z1, . . . ,zn) ∈ C[z1, . . . ,zn] is said to be
stable if whenever Im( zi) > 0 for all i ∈ [n], p(z1, . . . ,zn) /nequal0. We say p is real stable is p is stable
and all its coe ﬃcients are real. Anari et al. [ AGR16] proved a mixing time bound by proving
a poincare constant for a bases exchange markov chain associ ated to strong Rayleigh measures.
Hermon and Salez[ HS19] gave a uniﬁed proof of a log-sobolev and Poincare inequality in the
scalar case. One of our main results is showing that one can e ﬀortlessly follow their exact proof
and make minor modiﬁcations(using operator convexity of cer tain functions) to prove a matrix
valued Poincare inequality (which has also been consideredin [CHT15, CH15, CH16]). Our second
main result implies that one can use matrix valued Poincare i nequalities to prove matrix Bernstein
like concentration inequalities. See [ Led99] for how to prove similar concentration inequalities for
scalar lipshitz valued functions using Poincare and log-so bolev inequalities. Combining our two
main theorems, we get the following result.
Theorem 1.1. Given a k-homogenous strong Rayleigh measure π supported on n elements and given a
L-Lipshitz matrix valued function F : {0, 1}n → Sd and let µ = Ex∼π[F(x)]. We have for all t > 0,
Prx∼π[‖F(x) − µ‖/greaterorequalslantt] ⩽ 2de−t2/32(kL2+t
√
kL)
A matrix valued function F : Ω → Sd is L-Lipshitz if for all x, y ∈ Ω
‖F(x) − F(y)‖⩽ L · d(x, y)
with respect to some distance function between states d(x, y). In this paper, we will use the
hamming distance. We remark that a matrix Cherno ﬀbound for strong Rayleigh measures was
proven by [ KS18] by martingale arguments inspired by the scalar concentrat ion case by [ PP14].
Their application was to prove that spanning trees can be use d to construct spectral sparsiﬁers.
While our concentration result can’t prove a similar statem ent, our result can be used in situations
theirs cant. We compare our result with theirs in Section 4.
3
We ﬁnally deﬁne some terminology we will require pertaining to Markov chains and refer the
reader to [ MT06, LPW09] for more details. Let the stationary distribution of a reve rsible Markov
chain with state space Ωbe µ
Eµ[F] =
∑
x∈Ω
µ(x)F(x)
V arµ[F] = Eµ[F2] − (E(F(x))2
Consider a generator for the Markov chain Q ∈ RΩ×Ω with non-negative oﬀ-diagonal entries with
each row summing up to 0 and satisfying the local balance equa tions
π(x)Q(x, y) = π(y)Q(y, x)
For normalized generators, one can associate a stochastic matrix P such that Q = P − I. In
such cases, P also satsiﬁes local balance. Finally , the Dirchlet form for s calar functions is
EQ[ f, /g1] = ∑
x∈Ω,y∈Ω π(x)Q(x, y)( f (x) − f (y))2. It is easy to see that EQ[ f, /g1] = EP[ f, /g1]. For ma-
trix valued functions F, G : Ω → Sd, the dirchlet form is deﬁned as EQ[F, G] = EP[F, G] =∑
x∈Ω,y∈Ω π(x)Q(x, y)(F(x) − F(y))2 where Sd is the space of symmetric matrices of size d × d.
2 Matrix V alued Poincare Inequality for Strong Rayleigh mea sures
In this section, we prove our matrix valued Poincare inequality for measures satisfying the stochas-
tic covering property (SCP). We ﬁrst need some notation in ord er to deﬁne SCP measures. Let
{ei}n
i=1 be the coordinate basis of Rn. For x, y ∈ { 0, 1}n, we write x ⊲ y if x can be obtained by y by
increasing at most one coordinate from 0 to 1, i.e.,
x = y or ∃i ∈ [n], x = y + ei
This covering relation can be lifted to measures on {0, 1}n by writing π ⊲ π ′ whenever there is a
coupling of π and π′ which is supported on the set {(x, y) : x ⊲ y}. We say that π has the SCP if for
any S ⊆ [n] and x, y ∈ {0, 1}S, we have
x ⊲ y =⇒ π(XSc = ·|XS = y) ⊲ π(XSc = ·|XS = x)
This property was proposed by Pemantle and Peres [PP14] and they proved that all strong Rayleigh
measures satisfy the SCP . However, there are examples of matroids for which the uniform distribu-
tion has the SCP but do not have the strong Rayleigh property . Hermon and Salez [HS19] consider
the following local dynamics :
x ∼ y ⇐ ⇒ x, y diﬀer by a ﬂip or a swap
where x, y diﬀer by a ﬂip if x = y ± ei for some i and by a swap if y = x + ej − ek for distinct j and k.
And then they say that Q is a ﬂip-swap walk Markov generator for π which is reversible under π
and we have
Qxy > 0 ⇐ ⇒ x ∼ y
4
If in addition, we have ∆(Q) = max{−Qxx : x ∈ Ω} ⩽ 1, we say that Q is normalized and Q may
hence be written as Q = P−I for some stochastic matrix P. [ HS19] proved that there is a normalized
ﬂip-swap walk for an SCP distribution has a modiﬁed log-Sobol ev and Poincare constant 1/2k. We
will prove using their proof strategy that this walk actually has it’s Matrix valued Poincare constant
also 1/2k.
Theorem 2.1. If π is a k-homogenous SCP measure, then there is a normalized ﬂip -swalk walk Q for π
such that for any matrix valued function f : Ω → Sd
λV ar[f] ≼ E(f, f)
with λ /greaterorequalslant1
2k . Furthermore, the conclusion remains valid without the homogeneity assumption, with k = n/2
The proof of the scalar equivalent of the above statement in [ HS19] follows the chain decom-
position framework of [ JSTV04] which we elaborate on next. Let Q be any reversible Markov
generator with respect to some probability distribution π on a ﬁnite set Ω. Consider any partition
of the state space :
Ω =
⋃
i∈I
Ωi
We deﬁne two chains using this partition. Let the projection chain induced by this partition be the
Markov chain whose state space is I and whose Markov generator ˆQ is deﬁned as follows: for any
i, j ∈ Ω,
ˆQ(i, j) = 1
ˆπ(i)
∑
x∈Ωi,y∈Ωj
π(x)Q(x, y) where ˆπ(i) =
∑
x∈Ωi
π(x)
Note that ˆπ is a probability distribution on I and that it is reversible under ˆQ,i.e.,
ˆπ(i)ˆQ(i, j) = ˆπ(j)ˆQ(j, i)
We also have, that for each i ∈ I, the restriction chain on Ωi is the Markov chain whose state space
is Ωi and whose Markov geneator Qi is deﬁned as: for any states x, y ∈ Ωi,
Qi(x, y) = Q(x, y)
with the diagonal entries being adjusted so that the rows of Qi sum to zero. Clearly , then we have
ˆπi(x) = π(x)
ˆπ(i)
which is reversible under Qi. Now suppose that for each ( i, j) ∈ I 2 with ˆQi j > 0, we are given a
coupling κi j : Ωi × Ωj → [0, 1] of the probability distribution πi and πj,i.e.,
∀x ∈ Ωi,
∑
y∈Ωj
κi j(x, y) = πi(x)
5
∀y ∈ Ωj,
∑
x∈Ωi
κi j(x, y) = πj(y)
We will also need the following measure of quality of the coup ling
χ = min
{ π(x)Q(x, y)
ˆπ(i)ˆQ(i, j)κi j(x, y)
}
where the minimum runs over all ( x, y, i, j) such that the denominator is positive.
The main idea of [ JSTV04] is to relate the Poincare and (modiﬁed) log-Sobolev constan ts of the
original chain to the projection and restriction chains. Gi ven the above setup, we would now like
to prove recursive functional inequalities over the restriction and projection chains. Inequalities of
this form are the workhorse of all applications of the induction/chain decomposition idea [JSTV04].
Our next lemma establishes that scalar recursive Poincare i nequalities can be lifted to matrix
Poincare inequalities, using operator convexity properti es of the square function. We ﬁrst need
the following proposition.
Proposition 2.2. The function f (X, Y) = (X − Y)2 is jointly operator convex.
Proof. For any t ∈ [0, 1], X1, X2, Y1, Y2, we have
(
(tX1 + (1 − t)X2) − (tY1 + (1 − t)Y2)
) 2
=
(
t(X1 − Y1) + (1 − t)(X2 − Y2)
) 2
≼t(X1 − Y1)2 + (1 − t)(X1 − Y1)2
where the last step follows from the operator convexity of th e square function applied to X1 − Y1
and X2 − Y2 □
Lemma 2.3. [Recursive Poincare inequalities] With the above notation, w e have
λ(Q) /greaterorequalslantmin
{
χλ(ˆQ), min
i∈I
λ(Qi)
}
where the λ(·) represent the constant in the matrix valued Poincare inequali ty for the associated generator.
Proof. Let F : Ω→ Sd. The Dirichlet form can be written as
E(F, F) = 1
2
∑
x,y∈Ω
π(x)Q(x, y)(F(x) − F(y))2
We can also deﬁne the projection of a function ˆF : I → Sd by ˆF(i) = Eπi [F]. Hence, we can also
decompose the variance and Dirichlet form of a matrix valued function as follows:
V arπ[F] =
∑
i∈I
ˆπ(i)V arπi[F] + V arˆπ[ˆF]
Eπ(F, F) =
∑
i∈I
ˆπ(i)Eπi (F, F) + 1
2
∑
i/nequalj
∑
x∈Ωi,y∈Ωj
π(x)Q(x, y)(F(x) − F(y))2
6
We would now like to make a term-by-term comparison between the right hand sides of the above
two equations. In order to do this, we would like to replace th e second term in the Dirichlet form
equation by the Dirichlet form for Eˆπ(ˆF,ˆF). This is where the coupling is useful. Consider any pair
(i, j) ∈ I such that ˆQ)i, j>0 . Since κi j is a coupling of πi and πj, we have
ˆF(i) =
∑
x∈Ωi,y∈Ωj
κi j(x, y)F(x)
ˆF(j) =
∑
x∈Ωi,y∈Ωj
κi j(x, y)F(y)
We can now use Lemma 2.2 and operator Jensen’s inequality (Lemma 3.2) to conclude that
∑
x∈Ωi,y∈Ωj
κi j(x, y)(F(x) − F(y))2 ≽(ˆF(i) − ˆF(j))
Multiplying the above equation by χˆπ(i)ˆQ(i, j) we have
∑
x∈Ωi,y∈Ωj
π(x)Q(x, y)(F(x) − F(y))2 ≽χˆπ(i)ˆQ(i, j)(ˆF(i) − ˆF(j))2
It is easy to see that the above equation also holds when ˆQ(i, j) = 0 rather than just when ˆQ(i, j) = 0.
Now, summing up over all distinct i, j ∈ I, we get that
1
2
∑
i/nequalj
∑
x∈Ωi,y∈Ωj
π(x)Q(x, y)(F(x) − F(y))2 ≽χEˆπ[ˆF,ˆF]
=⇒ E π[F, F] ≽
∑
i∈I
ˆπ(i)Eπi [F, F] + χEˆπ[ˆF,ˆF]
Comparing this with the Variance decomposition, we get

Eˆπ[ˆF,ˆF] ≽ˆκV arˆπ[ˆF]
Eπi[F, F] ≽κiV arπi [F]∀i ∈ I,
=⇒ E π[F] ≽min{χˆκ, min
i∈I
κi}V arπ[F]
Since we did not assume anything about our function F, we get the desired conclusion. □
We will also need the following estimate on the quality of the coupling. Since the proof does
not depend on the function (and hence there is no di ﬀerence in the scalar and matrix valued case),
we present the lemma without proof.
Lemma 2.4. [Crude lower-bound on χ, Lemma 2 in [ HS19]] We always have
π(x)Q(x, y)
ˆπ(i)ˆQ(i, j)κi j(x, y)
/greaterorequalslantmax
{Q(x, y)
ˆQ(i, j)
, Q(y, x)
ˆQ(j, i)
}
7
2.1 Proof of Theorem 2.1
To prove Theorem 2.1, we will ﬁrst need to use the inductive framework to prove some functional-
analytic estimates for SCP measures.
Lemma 2.5. Given a generator ˆQ for a two state ({0, 1}) chain. We have for any F : {0, 1} → Sd,
(a + b)V ar[F] ≼ EˆQ[F, F]
Proof. It is easy to prove that for a Markov chain with generator Q, the stationary distribution π
satisﬁes π(1) = a
a+b and π(0) = b
a+b . Now we can focus on understanding the Dirichlet form and
variance of any matrix valued function F .
E[F, F] = b
a + b · a(F(0) − F(1))2
V ar[F] = E[F2] − (E[F])2
= 1
a + b (bF(0)2 + aF(1)2) − 1
(a + b)2 (bF(0) + a[F](1))2
= ab
(a + b)2 (F(0) − F(1))2
which concludes that the Poincare constant is ( a + b) □
We will also need the following lemma which characterizes th e quality of the couplings for
SCP measures.
Lemma 2.6. [Exploiting the SCP , Lemma 4 in [HS19]] If π has the SCP , then there is a couplingκ of π0, π1
supported on
{(x, y) ∈ Ω0 × Ω1 : x ∼ y}
In particular, taking κ01 and κ10 to be κ and its transpose respectively, we obtain
χ /greaterorequalslantM(Q)
max{a, b}
where M(Q) = min
x,y∈Ω
x∼y
max{Q(x, y), Q(y, x)}
We will now prove theorem 2.1.
Proof. [of Theorem 2.1] The proof is unchanged from the proof in [ HS19]. We will induct on the
number of elementsn. We will change the normalization of the generator : For any distribution π on
{0, 1}n with the SCP , our goal is to prove the existence of a ﬂip-swap walk Q for π such that λ(Q) /greaterorequalslant1
and ∆(Q) ⩽

n always
2k if π is k-homogenous
Once we have established this, after dividing Q by ∆(Q),
we will be done. As before, take a coordinate ℓ ∈ [n] and deﬁne the sets Ω0 = {x ∈ Ω : xℓ = 0}
8
and Ω1 = {x ∈ Ω : xℓ = 1} are both non-empty . We now consider the projection and restr iction
chains. Let their stationary distributions be ˆπ, π0, π1 respectively . We can of course view π0, π1
as distributions on {0, 1}n−1 and both distributions are SCP . If π is k-homogenous, then π0 is also
k-homogenous while π1 is ( k − 1)-homogenous. Thus, using our induction hypothesis, we ca n
say that there exists a ﬂip-swap walk generator Qi for πi (for i =0,1) satisfying λ(Qi) /greaterorequalslant1 and
∆(Qi) ⩽

n − 1 always
2(k − i) if π is k-homogenous
We also have, from Lemma 2.6, a coupling κ of π0 and
π1 supported on {x ∈ Ω0, y ∈ Ω1 : x ∼ y}. □
Hermon and Salez [HS19] deﬁne the following ﬂip-swap walk Q for π as follows : for x /nequaly ∈ Ω,
Q(x, y) =

Q0(x, y) if ( x, y) ∈ Ω0 × Ω0
Q1(x, y) if ( x, y) ∈ Ω1 × Ω1
ˆπ(0)ˆπ(1)κ(x,y)
π(x) if (x, y) ∈ Ω0 × Ω1
ˆπ(0)ˆπ(1)κ(y,x)
π(y) if (x, y) ∈ Ω1 × Ω0
and the diagonal is adjusted to make the row sums 0.
We will now use Lemma 2.3 with Ω0, Ω1 as our partition and the couplings κ01 being κ and κ10
being transpose of κ. We also have that the projection generator ˆQ satisﬁes λ(ˆQ) /greaterorequalslantˆQ(0, 1) + ˆQ(1, 0)
from Lemma 2.5. We also have that for any x ∈ Ω0, y ∈ Ω1 with κ(x, y) > 0,
π(x)Q(x, y)
ˆπ(0)ˆQ(0, 1)κ01(x, y)
= ˆπ(1)
ˆQ(0, 1)
= ˆπ(0)
ˆQ(1, 0)
= π(y)Q(y, x)
ˆπ(1)ˆQ(1, 0)κ01(y, x)
where the second equality follows from reversibility . Hence, we get
χ = ˆπ(0)
ˆQ(1, 0)
= ˆπ(1)
ˆQ(0, 1)
Finally combining the two inequalities above, we get
χλ(ˆQ) /greaterorequalslantˆπ(0) + ˆπ(1) = 1
From our induction hypothesis, we had λ(Qi) /greaterorequalslant1, so we can use Lemma 2.3 to get that λ(Q) /greaterorequalslant1.
We just need to bound the diagonal of Q now. For x ∈ Ω0, we have by construction
−Q(x, x) =
∑
y∈Ω0/downslopex
Q0(x, y) + ˆπ(0)ˆπ(1)
π(x)
∑
y∈Ω1
κ(x, y)
Using the deﬁnition of ∆(Q0) and the fact that the ﬁrst marginal of κ is π0, we deduce that
−Q(x, x) ⩽ ∆(Q0) + ˆπ(1) = ∆(Q0) + Eπ[Xℓ]
Similarly , ifx ∈ Ω1, we have
−Q(x, x) ⩽ ∆(Q1) + ˆπ(0) ⩽ ∆(Q1) + xℓ
9
as xℓ = 1. So using the induction hypothesis on ∆(Qi), we get that for all x ∈ Ω,
∆(Q) ⩽

n always
2k + Eπ[Xℓ] − xℓ if π is k-homogenous
Finally to bound the second line by 2 k, we average over the coordinate ℓ. The generator will be
written as Q(ℓ) to denote the dependence on ℓ.For each ell ∈ [n], the construction of our generator
produces a ﬂip-swap walk Q(ℓ) for π which satisﬁes λ(Q(ℓ)) /greaterorequalslant1 and ∆(Q(ℓ)) ⩽ n. Now we crucially
notice that the matrix valued variance is unchanged under av eraging (because it doesnt depend
on the generator) and the Dirchlet form has a linear dependen ce on the generator Q(ℓ). Hence,
λ(Q) and ∆(Q) is preserved under convex combinations. So we can deﬁne an av erage generator
Q∗ = 1
n
n∑
ℓ=1
Q(ℓ) automatically satisﬁes λ(Q∗) /greaterorequalslant1 and ∆(Q∗) ⩽ n. If π is k-homogenous, then for
every x ∈ Ω, we get
−Q∗(x, x) = − 1
n
n∑
ℓ=1
Q(ℓ)(x, x) ⩽ 1
n
n∑
ℓ=1
(2k + E[Xℓ] − xℓ) = 2k
Thus Q∗ satisﬁes our desired properties and we are done.
