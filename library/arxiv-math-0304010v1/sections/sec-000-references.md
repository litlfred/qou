---
doc_id: arxiv-math-0304010v1
doc_title: "KEROV’S CENTRAL LIMIT THEOREM FOR THE PLANCHEREL MEASURE ON YOUNG DIAGRAMS"
section_id: sec-000-references
section_title: "References"
section_number: null
pages: 1-9
source_pdf: 0304010v1.pdf
source_sha256: fc2296c027b3feb0
doc_brief: "KEROV’S CENTRAL LIMIT THEOREM FOR THE PLANCHEREL MEASURE ON YOUNG DIAGRAMS — Consider random Young diagrams with ﬁxed number n of boxes, dis- tributed according to the Plancherel measure Mn."
---
In: S. Fomin, editor. Symmetric Functions 2001: Surveys of Deve lopments and Perspectives
(NATO Science Series II. Mathematics, Physics and Chemistry. Vol. 74), Kluwer, 2002, pp.
93–151.
Vladimir Ivanov: Chair of Higher Algebra, Department of Mathe matics and Mechanics, Moscow
State University, Vorob’evy Gory, GZ, Moscow 119992, GSP-2, Russia. E-mail: vivanov@mccme.ru
Grigori Olshanski: Dobrushin Mathematics Laboratory, Institut e for Information Transmission
Problems, Bolshoy Karetny 19, Moscow 101447, GSP-4, Russia. E -mail: olsh@online.ru
Typeset by AMS-TEX
1
§0. Introduction
Main result. Let Yn denote the set of partitions of n (n = 1, 2, . . .). We identify
partitions and Young diagrams, so that elements of Yn become Young diagrams
with n boxes. We view each λ∈ Yn as a plane shape, of area n, inside the ﬁrst
quadrant R2
+, with coordinates r, s (the row and column coordinates). In new
coordinates x = s− r, y = r + s, the boundary ∂λ of the shape λ⊂ R2
+ may be
viewed as the graph of a continuous piece–wise linear functi on, which we denote as
y = λ(x). Note that λ′(x) =±1, and λ(x) coincides with |x| for suﬃciently large
values of|x|. The area of the shape |x|≤ y≤ λ(x) equals 2 n.
Further, we equip the ﬁnite set Yn with a probability measure Mn called the
Plancherel measure. The measure Mn has important representation theoretic and
combinatorial interpretations. By deﬁnition, the weight Mn(λ) assigned to a di-
agram λ∈ Yn equals dim 2 λ/n!, where dim λ is the dimension of the irreducible
representation (of the symmetric group Sn) indexed by λ. Equivalently, dim λ is
the number of standard tableaux of shape λ.
Viewing λ’s as points of the probability space ( Yn , Mn), we view λ(· )’s as
random functions, and we aim to describe their asymptotics as n→∞ . Informally,
the main result can be stated as follows:
1
√n λ(√n x) ∼ Ω( x) + 2√n ∆( x), n →∞ , (0.1)
where Ω( x) is a certain ﬁxed curve and ∆( x) is a generalized Gaussian process on
the interval [−2, 2] (Ω and ∆ are speciﬁed below).
The left–hand side (denoted as ¯λ(x) in the sequel) is a rescaled version of the
function y = λ(x). The graph of ¯λ(· ) is obtained from that of λ(· ) by shrinking
both the x–axis and the y–axis in √n times. The purpose of this procedure is to
put the random ensembles with diﬀerent n’s on the same scale (note that the area
of the shape |x|≤ y≤ ¯λ(x) equals 2 for any n).
The ﬁrst term in the right–hand side of (0.1) corresponds to t he law of large
numbers. It follows from (0.1) that in the large n limit, the random scaled polygonal
lines y = ¯λ(x) concentrate near the ﬁxed curve y = Ω( x). In the initial scale, this
means that, for large n, the “typical” functions y = λ(x) look like the function
y =√n Ω( 1√n x).
The second term in the right–hand side of (0.1) governs the ﬂuctuations of the
random functions ¯λ around the curve Ω, which corresponds to the central limit
theorem. We see that the ﬂuctuations of the scaled functions are of ord er 1√n .
That is, in the initial picture for the shape λ⊂ R2
+, the random ﬂuctuations of the
boundary line ∂λ need no scaling along the main diagonal , as n→∞ .
Description of Ω and ∆ . The function Ω( x) is given by two diﬀerent expressions
depending on whether x is in the interval [−2, 2]:
Ω( x) =
{ 2
π (x arcsin x
2 +
√
4− x2), |x|≤ 2,
|x|, |x|≥ 2. (0.2)
Note that Ω ′(x) = 2
π arcsin x
2 inside [−2, 2]. The critical points ±2 have an im-
portant meaning: for “typical” (with respect to the Planche rel measure) diagrams
λ∈ Yn, the length of the ﬁrst row and of the ﬁrst column is approxima tely 2√n.
2
This claim, which seems plausible from (0.1) and (0.2) can be substantially reﬁned,
see [BDJ], [AD].
The Gaussian process ∆( x) can be deﬁned by a random trigonometric series.
Let ξ2, ξ3, . . . be independent standard real Gaussian random variables (ea ch ξk
has mean 0 and variance 1), and set x = 2 cos θ, where 0 ≤ θ≤ π. Then
∆( x) = ∆(2 cos θ) = 1
π
∞∑
k=2
ξk√
k
sin(kθ). (0.3)
For any smooth test function ϕ on R, the smoothed series
1
π
∞∑
k=2
ξk
√
k
∫ 2
−2
sin(kθ)ϕ(x)dx, θ = arccos(x/2) (0.4)
converges and is a Gaussian random variable. In this way we ge t a Gaussian measure
on the space of distributions with support on [ −2, 2], or a generalized Gaussian
process. Its trajectories are not ordinary functions but ge neralized functions.
History of the result. The law of large numbers (the concentration near the
curve Ω) was independently obtained by Logan and Shepp [LoS] and by Vershik
and Kerov [VeK1]. Their papers appeared in 1977. Later, in 19 85, Vershik and
Kerov published a detailed version of their work, [VeK3], co ntaining stronger re-
sults. In [LoS] and [VeK3], the question about the second ter m of the asymptotics,
corresponding to the central limit theorem, was posed.
Such a theorem was obtained by Kerov and announced in his shor t note [Ke1],
1993. There Kerov also outlined the scheme of the proof. The n ote [Ke1] contained
a number of fruitful ideas, one of which (introduction of “go od” coordinates in
the set of Young diagrams) was largely developed in the joint note by Kerov and
Olshanski [KO], 1994.
For an intermediate result of [Ke1], which is of independent interest, an elegant
proof was suggested by Hora [Ho], 1998. Note that Hora’s appr oach diﬀers from
that of Kerov.
A few years ago we started to persuade Kerov to write a detaile d exposition of his
central limit theorem. Our discussions resulted ﬁrst in the joint paper by Ivanov
and Kerov [IK], 1999, which clariﬁed and developed one of the steps of Kerov’s
proof.1
Then Kerov found a simpler derivation of the theorem, which a lso made apparent
that the subject is connected with the concept of free cumula nts and a theorem due
to Biane [Bi1]. In the end of 1999 Kerov sent us two short work n otes with a
description of the new approach. About the same time he gave a talk on this
subject at Vershik’s seminar in St. Petersburg. He also star ted writing a detailed
paper on this subject but had time only to ﬁnish the prelimina ry section.
In the present paper we give a detailed exposition of Kerov’s central limit the-
orem. Our aim was to reconstruct from his notes the “new appro ach” of 1999. 2
This was not easy: for a long time we could not understand the m eaning of some
1It concerns the stable structure constants for convolution of c onjugacy classes in symmetric
groups. This topic was also discussed in [KO].
2It should be pointed out that the “old approach” of 1993 is also correct: we were able to
directly check all the claims of [Ke1].
3
claims stated too brieﬂy, but ﬁnally the picture became clea r. However, we cannot
be sure that we succeeded to completely fathom Kerov’s inten tion, and there is no
doubt that his own exposition would be quite diﬀerent.
Links with random matrices. Recently it was discovered that the limit dis-
tribution of a ﬁnitely many (properly scaled) ﬁrst rows of th e random Plancherel
Young diagram λ∈ Yn, as n→∞ , coincides with the limit distribution of the same
number of (properly scaled) largest eigenvalues of the rand om Hermitian N× N
matrix taken from the Gaussian Unitary Ensemble, as N →∞ . See [BDJ] and
subsequent papers [Ok], [BOO], [Jo3], [Jo4], [BDR]. It turn s out that the striking
similarity between these two random ensembles holds not onl y “at the edge” (as
is shown in these works) but also on the level of global ﬂuctua tions, which is the
subject of the present paper. For spectra of random matrices , the limit behavior
of global ﬂuctuations was ﬁrst studied in [DS], where a centr al limit theorem was
obtained. Further results in this direction were obtained i n [Jo1], [Jo2], [DE]. The
generalized Gaussian processes that emerge in these works a re very close to our
process, we discuss this topic in §9.
T echniques. Although the main result is stated in probabilistic terms, t he tech-
niques of the paper are essentially algebraic and combinato rial, the probabilistic
part being reduced to a few elementary facts. The work is base d on the choice of
convenient “coordinate systems” for Young diagrams (there are several ones) and
on the choice of an appropriate algebra A of “observables”. Elements of A are
functions on the set Y of all Young diagrams. They are given by polynomial ex-
pressions in each of the “coordinate systems”. For this reas on we call A the algebra
of polynomial functions on Y. We examine several diﬀerent bases in A. One of
them (denoted as {p#
ρ}) is related to the character table of the symmetric groups;
this basis is well adapted to evaluating expectations with r espect to the Plancherel
measures Mn. Another basis has geometric signiﬁcance; this basis is for med by
monomials in ~p2,~p3, . . ., a system of generators of A, which are essentially the mo-
ments of λ(x). One more basis (formed by monomials in generators p1, p2, . . .∈ A)
plays an intermediate role. A major part of our work consists in studying the
transitions between various bases. This ﬁnally makes it pos sible to isolate a good
system of generators in A that directly describe the Gaussian ﬂuctuations.
Organization of the paper. In§1, we introduce the algebra A and a system
p1, p2, . . . of its generators. We show that elements of A are both shifted symmet-
ric functions in the row coordinates λ1, λ2, . . . of a Young diagram λ∈ Y, and
supersymmetric functions in the (modiﬁed) Frobenius coord inates of λ. This fact
was ﬁrst pointed out in [KO].
In§2, we introduce the necessary geometric setting for visuali zing ﬂuctuations
of Young diagrams. We embed Yn into the larger set D0 of “continual diagrams”.
We introduce the generators ~p2,~p3, . . .∈ A and the “weight grading” of the algebra
A, which is well adapted to the operation of rescaling diagram s.
In§3, we examine one more system of generators in A, denoted as p#
1 , p#
2 , . . . .
These are character values on cycles in symmetric groups. We study the transitions
between all three systems of generators. Here our tools are a suitably elaborated
classical formula (due to Frobenius) for the value of a symme tric group character
on the k-cycle, and Lagrange’s inversion formula.
In§4, we introduce the basis {p#
ρ} in A and study a family of ﬁltrations in
A, which are deﬁned in terms of this basis. Here we follow the pa per [IK]. We
4
essentially need two diﬀerent ﬁltrations. Their purpose is to single out main terms
of asymptotics in diﬀerent regimes. One ﬁltration is respon sible for the “law of
large numbers” while another serves the “central limit theo rem”.
In§5, we start the study of the Plancherel measures Mn. We introduce the
sequence of expectation functionals ⟨·⟩n on A that corresponds to the sequence
{Mn}, and we remark that ⟨·⟩n becomes very simple in the basis {p#
ρ}. Then we
prove the main result of the section — the law of large numbers , or convergence
to the curve Ω. Although the central limit theorem, establis hed in§7, contains the
law of large numbers, we prefer to prove it independently, be cause this can be done
in a rather simple way. It is interesting to compare our simpl e algebraic argument
with the analytic approach of the pioneer works [LoS], [VeK1 ], [VeK3].
In§6, we examine the random variables p#
2
(n)
, p#
3
(n)
, . . ., where p#
k
(n)
stands
for the restriction of the function p#
k ∈ A to the ﬁnite probability space ( Yn, Mn).
We show that, as n→∞ , the variables p#
k
(n)
, suitably scaled, are asymptotically
independent Gaussians. This result is the ﬁrst version of th e central limit theorem.
Its proof relies on the method of [IK]. A diﬀerent proof has be en given by Hora
[Ho].
In§7, we obtain our main result: a description of the Gaussian ﬂu ctuations
around the limit curve Ω. It is derived from the central limit theorem for the gen-
erators p#
k mentioned above. The proof is based on a formula that gives th e highest
term of the polynomial expressing p#
k through the (centered and scaled versions of)
the generators ~pj. Here “highest term” refers to an appropriate ﬁltration of t he
algebra A, which we call Kerov’s ﬁltration.
In§8, we get one more version of the central limit theorem. Accor ding to Vershik–
Kerov’s theory, to any Young diagram λ we attach a probability measure on R
(say, µλ), supported by a ﬁnite set. Viewing λ∈ Yn as the random element of the
probability space ( Yn, Mn), we turn µλ into a random measure. For these random
measures we prove an asymptotic formula similar to (0.1), wh ere, instead of the
limit curve Ω, we have the semi–circle distribution, and ∆( x) is replaced by another
generalized Gaussian process. We do not know if Kerov was awa re of this result.
However, it perfectly ﬁts in the philosophy of his works.
In§9, we give comments to the results of §§7–8 and compare them with the
central limit theorem for random matrices.
In§10, we show that the highest terms of the elements p#
ρ in the “weight grading”
are closely related to the free cumulants. As an application , we get a simple proof
of Biane’s asymptotic formula for character values of large symmetric groups, [Bi1].
Acknowledgment. One of the authors (G. O.) is deeply grateful to Persi Diaconi s
for discussions and an important critical remark, which was taken into account in
the ﬁnal version of the paper.
§1. The algebra of polynomial
functions on the set of Young diagrams
Recall ﬁrst the basic deﬁnitions and notation related to par titions and Young
diagrams, see [Ma].
A partition is an inﬁnite sequence λ = (λ1, λ2, . . .) of nonnegative integers such
that λ1≥ λ2≥ . . . and the number of nonzero λi’s is ﬁnite. The sum λ1 + λ2 + . . .
is denoted by |λ|, and usually we set |λ| = n.
5
As in [Ma], we assign to a partition a Young diagram, which is d enoted by the
same symbol. We identify partitions and Young diagrams, and we denote by Y the
set of all Young diagrams. The conjugation involution of Y (transposition of rows
and columns of a diagram) is denoted as λ↦→λ′.
There is another presentation of Young diagrams, the Frobenius notation. We
shall use its modiﬁcation due to Vershik and Kerov [VeK2]:
λ = (a1, . . . , ad| b1, . . . , bd).
Here d = d(λ) is the length of the main diagonal in λ,
d(λ) ={i| λi≥ i} ={j| λ′
j≥ j},
and
ai = λi− i + 1
2 , b i = λ′
i− i + 1
2 , i = 1, . . . , d(λ). (1.1)
The numbers ai, bi are called the modiﬁed Frobenius coordinates of λ. Both
a1, . . . , ad and b1, . . . , bd are strictly decreasing positive proper half–integers, i. e.,
numbers from { 1
2 , 3
2 , 5
2 , . . .}, such that ∑ (ai + bi) = |λ|. Note that the Vershik–
Kerov deﬁnition (1.1) diﬀers from the classical deﬁnition o f the Frobenius coordi-
nates, which does not involve one–halves (see [Ma, p. 3]). Ho wever, these one–
halves play an important role in what follows.
Note that the conjugation involution λ↦→λ′ has a very simple description in
terms of the Frobenius coordinates:
(a1, . . . , ad| b1, . . . , bd)′ = (b1, . . . , bd| a1, . . . , ad). (1.2)
One more useful presentation of Young diagrams, due to Kerov , will be given in
§2.
Set
Z′ = Z + 1
2 ={. . . ,− 3
2 ,− 1
2 , 1
2 , 3
2 , . . .}, Z′
+ ={ 1
2 , 3
2 , . . .}, Z′
− ={. . . ,− 3
2 ,− 1
2}.
Given λ∈ Y, set
li = λi− i + 1
2∈ Z′, i = 1, 2, . . . ,
and note that l1 > l 2 > . . . . We assign to λ the inﬁnite subset L(λ) ={l1, l2, . . .}⊂
Z′.
The following claim is a version of the classical Frobenius l emma, see [Ma, ch.
I, (1.7) and Example 1.15 (a)].
Proposition 1.1. Let λ∈ Y be arbitrary.
(i) We have Z′ = L(λ)⊔ (−L(λ′)). I.e., L(λ)∩ (−L(λ′)) = ∅ andL(λ)∪
(−L(λ′)) = Z′.
(ii) In the notation (1.1),
L(λ)∩ Z′
+ ={a1, . . . , ad}, Z′
−\L (λ) =−(L(λ′)∩ Z′
+) ={−b1, . . . ,−bd}).
Proof. (i) We represent λ as a plane shape in the quarter plane R2
+. Let ( r, s) be
the coordinates in R2
+. Here the rows of λ are counted along the ﬁrst coordinate r,
6
directed downwards, while the columns are counted along the second coordinate s,
directed to the right. Denote by ∂λ the doubly inﬁnite polygonal line which ﬁrst
goes upwards along the r-axis, next goes along the boundary line separating λ from
its complement in R2
+, and then goes to the right along the s–axis. For any a∈ Z′,
the diagonal line s−r = a intersects ∂λ at the midpoint of a certain segment, which
is either vertical or horizontal. According to these two pos sibilities a is either in
L(λ) or in −L(λ′). This proves (i).
(ii) By the very deﬁnition (1.1), the numbers a∈ Z′
+ such that the diagonal
s− r = a meets a vertical boundary segment are exactly the numbers a1, . . . , ad.
Likewise, the numbers−b∈ Z′
− such that the diagonal s−r =−b meets a horizontal
boundary segment are exactly the numbers −b1, . . . ,−bd. This proves (ii). □
For any λ∈ Y we set
Φ( z; λ) =
∞∏
i=1
z + i− 1
2
z− λi + i− 1
2
, z ∈ C.
The product is actually ﬁnite, because λi = 0 when i is large enough. Therefore,
Φ( z; λ) is a rational function in z. We view it as a generating function of λ.
Proposition 1.2. In the notation (1.1), we have
Φ( z; λ) =
d∏
i=1
z + bi
z− ai
, (1.3)
which is the presentation of Φ( z; λ) as an incontractible fraction.
Proof. The equality (1.3) follows from Proposition 1.1. This is an i ncontractible
fraction, because the numbers a1, . . . , ad,−b1, . . . ,−bd are pairwise distinct. □
Another proof of the equality (1.3) is given in [OR V], it foll ows an idea from
[KO].
As the ﬁrst corollary of (1.3) note the relation
Φ( z; λ′) = 1 /Φ(−z; λ).
Remark that Φ( z; λ) = 1 + O( 1
z ) near z =∞, hence both Φ( z; λ) and ln Φ( z; λ)
can be expanded in a power series in z−1, z−2, . . . about z =∞.
Deﬁnition 1.3. The algebra of polynomial functions on the set Y, denoted as
A, is generated over R by the coeﬃcients of the above expansion of Φ( z; λ) or,
equivalently, of ln Φ( z; λ). We also assume that A contains 1.
Proposition 1.4. We have
ln Φ( z; λ) =
∞∑
k=1
pk(λ)
k z−k ,
where
pk(λ) =
∞∑
i=1
[(λi− i + 1
2 )k− (−i + 1
2 )k] (1.4)
=
d(λ)∑
i=1
[ak
i− (−bi)k]. (1.5)
7
Proof. Immediate from Proposition 1.2. □
Thus, A is generated by the functions pk(λ), k = 1, 2, . . ..
Recall [Ma] that the algebra of symmetric functions, denoted as Λ, is the graded
algebra deﬁned as the projective limit (in the category of gr aded algebras) lim←−Λ( n),
where Λ( n) denotes the algebra of symmetric polynomials in n variables. As the
base ﬁeld we take R. The morphism Λ( n)→ Λ( n− 1), which is employed in the
projective limit transition, is deﬁned as specializing the nth variable to 0. Let
{hk}k=1,2,... and{pk}k=1,2,... denote the complete homogeneous symmetric func-
tions and the Newton power sums, respectively. Each of these two families is a sys-
tem of homogeneous, algebraically independent generators of Λ, deg hk = deg pk =
k. Recall the basic relation:
1 +
∞∑
k=1
hktk = exp
∞∑
k=1
pk
k tk .
Proposition 1.5. The generators pk∈ A are algebraically independent, so that A
is isomorphic to R[p1, p2, . . .].
Proof. Fix an arbitrary N = 1 , 2, . . .. Assume that f is a polynomial in N vari-
ables such that f (p1, . . . , pN ) = 0, and show that f = 0. Let ¯f denote the top
homogeneous component of f counted with the understanding that the degree of
the ith variable equals i; it suﬃces to show that ¯f = 0.
Let λ range over the set of partitions of length ≤ N . Fix an arbitrary vec-
tor x∈ RN with nonnegative weakly decreasing coordinates and set λ = λ(A) =
([Ax]i)i=1,...,N , where A is a large integer. Letting A → ∞ in the equality
f (p1(λ(A)), . . . , pN (λ(A))) = 0 we get ¯f (p1(x), . . . ,pN (x)) = 0. Since the ﬁrst
N Newton power sums specialized in N variables are algebraically independent, we
conclude that ¯f = 0. □
Deﬁnition 1.6. Setting Λ ∋ pk↦→pk∈ A and taking into account Proposition
1.5 we get an algebra isomorphism Λ → A. We call it the canonical isomorphism.
We call the grading in A, inherited from that of Λ, the canonical grading of A.
Later on, in Deﬁnition 2.9, we shall deﬁne quite a diﬀerent gr ading in A.
In terms of generating series, the canonical isomorphism Λ → A takes the form
H(t) := 1 +
∞∑
k=1
hktk ↦→Φ( t−1;· ).
Formula (1.5) means that the functions pk(λ) are super power sums in ai’s
and bi’s, see [Ma, Example I.3.23], [VeK2], [KO], [OR V]. Thus, one can say that
under the canonical isomorphism of Deﬁnition 1.6, the algeb ra A is identiﬁed with
the algebra of supersymmetric functions in the modiﬁed Frobeni us coordinates of a
Young diagram.
Next, we shall give a similar interpretation of formula (1.4 ). Recall [OO] that the
algebra of shifted symmetric functions, denoted as Λ ∗, is the ﬁltered algebra deﬁned
as the projective limit (in the category of ﬁltered algebras ) lim←−Λ ∗(n), where Λ( n)∗
consists of those polynomials in n variables x1, . . . , xn, which become symmetric
in new variables yi = xi− i + const (the choice of the constant here is irrelevant).
The base ﬁeld is again R, the ﬁltration is taken with respect to the total degree
8
of a polynomial, and the morphism Λ ∗(n)→ Λ ∗(n− 1) is deﬁned as above, i.e.,
as specializing xn = 0. The graded algebra associated to the ﬁltered algebra Λ ∗
is canonically isomorphic to Λ. The algebra Λ ∗ is generated by the algebraically
independent system{p∗
k}k=1,2,..., where
p∗
k(x1, x2, . . .) =
∞∑
k=1
[(xi− i + 1
2 )k− (−i + 1
2 )k], k = 1, 2, . . . ,
are certain shifted analogs of the Newton power sums. See [OO ] for more detail
(note that the above deﬁnition of the elements p∗
k slightly diﬀers from that given
in [OO]). See also [EO].
By analogy with Deﬁnition 1.6, we deﬁne an algebra isomorphi sm Λ ∗→ A by
setting p∗
k↦→pk, k = 1 , 2, . . .. Note that it preserves the ﬁltration. Then formula
(1.4) makes it possible to say that the algebra A coincides with the algebra of shifted
symmetric functions in the row coordinates λ1, λ2, . . . of a Young diagram λ.
Deﬁnition 1.7. Deﬁne an involutive algebra automorphism inv : A→ A by
(inv(f ))(λ) = f (λ′), f ∈ A, λ ∈ Y. (1.6)
By virtue of (1.2) and (1.5),
inv(pk) = (−1)k−1pk , k = 1, 2, . . . . (1.7)
Hence the involution of A is compatible with the canonical involution of the algebra
Λ with respect to the isomorphism Λ → A introduced in Deﬁnition 1.6.
§2. Continual diagrams and their moments
Deﬁnition 2.1. A continual diagram is a function ω(x) on R such that:
(i)|ω(x1)− ω(x2)|≤| x1− x2| for any x1, x2∈ R (the Lipschitz condition).
(ii) There exists a point x0∈ R, called the center of ω, such that ω(x) =|x− x0|
when|x| is large enough.
The set of all continual diagrams is denoted by D, and the subset of diagrams
with center 0 is denoted by D0.
This deﬁnition is due to Kerov (see his papers [Ke2], [Ke3], [ Ke4]). We shall
mainly deal with the set D0.
To any ω∈D we assign a function σ(x):
σ(x) = 1
