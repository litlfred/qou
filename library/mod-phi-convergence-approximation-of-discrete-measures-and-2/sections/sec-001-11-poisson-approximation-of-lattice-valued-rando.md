---
doc_id: mod-phi-convergence-approximation-of-discrete-measures-and-2
doc_title: "ANNALES DE L’INSTITUT FOURIER Université Grenoble Alpes Les Annales de l’institut Fourier sont membres du Centre Mersenne pour l’édition scientifique ouverte www.centre-mersenne.or"
section_id: sec-001-11-poisson-approximation-of-lattice-valued-rando
section_title: "Poisson approximation of lattice-valued random variables"
section_number: 1.1
pages: 3-84
source_pdf: mod-phi-convergence-approximation-of-discrete-measures-and-20yc5c6q3n.pdf
source_sha256: c563cc999000e75d
doc_brief: "ANNALES DE L’INSTITUT FOURIER Université Grenoble Alpes Les Annales de l’institut Fourier sont membres du Centre Mersenne pour l’édition scientifique ouverte www.centre-mersenne.org — 2 sections: Intr"
---
Consider a sequence (Bi)i/greaterorequalslant1 of independent Bernoulli random variables,
with P[Bi = 1] = pi and P[Bi = 0] = 1 −pi. We set
Xn =
n∑
i=1
Bi.
The Poisson approximation ensures that if the pi’s are small but their sum
λn =∑ n
i=1pi is large, then the distribution of Xn is close to the distribution
of a Poisson random variable with parameter λn =∑ n
i=1pi. To make this
result quantitative, one can introduce the total variation distance between
two probability measures µ and ν on Z. Let us set
dTV(µ,ν ) =
∑
k∈Z
|µ({k}) −ν({k})| ;
this deﬁnition diﬀers by a multiplicative factor 2 from the usual conven-
tions, but otherwise we would have to keep track of a factor 1
2 in all our
estimates. A ﬁrst quantitative result regarding the Poisson approximation is
due to Prohorov and Kerstan (see [40, 49]): if pi = λ
n for all i ∈ [ [1,n ] ], then
dTV(Xn, P(λ)) =
∑
k∈N
⏐
⏐
⏐
⏐P[Xn =k] − e−λ λk
k!
⏐
⏐
⏐
⏐ ⩽ 2λ
n .
More generally, with parameters pi that can be distinct and with λn =∑ n
i=1pi, Le Cam showed that
∑
k∈N
⏐
⏐
⏐
⏐P[Xn =k] − e−λn (λn)k
k!
⏐
⏐
⏐
⏐ ⩽ 2
n∑
i=1
(pi)2.
This is an immediate consequence of the inequality on total variation dis-
tances
dTV(µ1 ∗µ2,ν 1 ∗ν2) ⩽ dTV(µ1,ν 1) +dTV(µ2,ν 2)
which holds for any probability measures µ1,µ 2,ν 1,ν 2 on Z (cf. [14]). By
using arguments derived from Stein’s method for the Gaussian approxi-
mation, Chen and later Barbour and Eagleson improved versions of this
inequality, e.g.,
∑
k∈N
⏐
⏐
⏐
⏐P[Xn =k] − e−λn (λn)k
k!
⏐
⏐
⏐
⏐ ⩽ 2 (1 − e−
∑ n
i=1pi)
∑ n
i=1(pi)2
∑ n
i=1pi
,
ANNALES DE L’INSTITUT FOURIER
APPROXIMATION OF DISCRETE MEASURES 1117
see [5, 19, 54]. We also refer to [20] for an extension to possibly depen-
dent Bernoulli random variables, to [2] for results regarding the Poisson
processes, and to [6] for a survey of the theory of Poisson approximations.
More generally, consider random variables Xn/greaterorequalslant1 whose distributions are
supported by the lattice Zd ⊂ Rd, and which stem from a common proba-
bilistic model. In many cases, the scaling properties of the model imply that
when n is large, Xn can be approximated by a discrete inﬁnitely divisible
lawνn, the Lévy exponents of these reference laws being all proportional:
ˆνn(ξ) :=
∑
k∈Zd
νn(k) ei⟨ξ |k⟩ = eλnφ(ξ), λ n → +∞.
To go beyond the classical Poisson approximation, one can try in this set-
ting to write bounds on the total variation distance dTV(Xn,νn), or on an-
other metric which measures the convergence in law (the local distance, the
Kolmogorov distance, the Wasserstein metric, etc.). A convenient frame-
work for this program is the notion of mod-φ convergence developed by Bar-
bour, Kowalski and Nikeghbali in [7], see also the papers [23, 26, 27, 35, 41].
The main idea is that, given a sequence of random variables (Xn)n∈N with
values in a lattice Zd, and a reference inﬁnitely divisible law φ on the same
lattice, if one has suﬃciently good estimates on the Fourier transform of
the law µn of Xn and on the ratio
ˆµn(ξ)
ˆνn(ξ) = E[eiξXn] e−λnφ(ξ),
then one can deduce from these estimates the asymptotics of the distribu-
tion of Xn: central limit Theorems [7, 35], local limit Theorems [23, 41],
large deviations [26], speed of convergence [27], etc. In this paper, we shall
use the framework of mod- φ convergence to compute the precise asymp-
totics of the distance between the law of Xn and the reference inﬁnitely
divisible law, for various distances.
When approximating lattice-distributed random variables, another ob-
jective that one can pursue consists in ﬁnding better approximations than
the one given by an inﬁnitely divisible law. A general principle is that,
if one allows signed measures instead of positive probability measures,
then simple deformations of the inﬁnitely divisible reference law can be
used to get smaller distances, i.e. faster convergences. In the setting of
the classical Poisson approximation of sums of independent integer-valued
random variables, this idea was used in [4, Theorem 5.1]. We also refer
to [8, 13, 16, 17, 18, 36, 42, 48] for other applications of the signed compound
Poisson approximation (SCP). For mod-Poisson convergent random vari-
ables (Xn)n∈N, an unconditional upper bound on the distance between the
TOME 70 (2020), F ASCICULE 3
1118 R. CHHAIBI, F. DELBAEN, P.-L. MÉLIOT & A. NIKEGHBALI
law of Xn and a signed measure νn deﬁned by means of Poisson–Charlier
polynomials was proven in [7, Theorem 3.1]. A more general upper bound
with an arbitrary reference law also appears in [7, Theorem 5.1]. In our
paper, we shall set up a general approximation scheme for sequences of
lattice-valued random variables, which will allow us:
• to obtain signed measure approximations whose distances to the
laws of the variables Xn are arbitrary negative powers of the pa-
rameter λn;
• to compute the asymptotics of these distances (instead of an un-
conditional upper bound).
Thus, this paper can be regarded as a complement to [7], with an alternative
approach and an alternative goal (namely, obtaining the exact asymptotics
of the distances). In [26, Proposition 4.1.1], we also used signed measures in
order to approximate mod-φ convergent random variables, but with respect
to a continuous inﬁnitely divisible distribution φ, and using a ﬁrst-order
deformation of the Gaussian distribution.
In the remainder of this introductory section, we recall the main deﬁni-
tions from the theory of mod- φ convergence, and we explain the general
approximation scheme. In subsequent sections, this approximation scheme
will yield the main hypotheses of our Theorems (Sections 2 and 3), and we
shall apply it to various one-dimensional and multi-dimensional examples
coming from probability, analytic number theory, combinatorics, etc. (Sec-
tions 4 and 5). We also present in this introduction the main tool that we
shall use in this paper, namely, harmonic analysis in the Wiener algebra.
1.2. Inﬁnitely divisible distributions and distances between
probability measures
Let us start by presenting the reference inﬁnitely divisible laws and the
distances between probability distributions that we shall work with. Fix a
dimension d /greaterorequalslant1. If X is a random variable with values in Zd, we denote
µX its probability law
µX (k1,k 2,...,k d) = P[X = (k1,k 2,...,k d)],
andˆµX its Fourier transform, which is deﬁned on the torus Td = (R/2πZ)d:
ˆµX (ξ) = E[ei⟨ξ |X⟩ ] =
∑
k1,...,k d∈Z
µX (k1,...,k d) exp

i
d∑
j=1
kjξj

.
ANNALES DE L’INSTITUT FOURIER
APPROXIMATION OF DISCRETE MEASURES 1119
Assume that the law of X is inﬁnitely divisible. Then the Fourier transform
of X can be written uniquely as
ˆµX (ξ) = eφ(ξ),
where φ is a function that is (2πZ)d-periodic:
∀ (n1,...,n d) ∈ Zd, φ(ξ1 + 2πn1,...,ξ d + 2πnd) = φ(ξ1,...,ξ d).
Moreover, the law µX is supported on Zd and none of its sublattices if and
only if the Lévy–Khintchine exponent φ is periodic with respect to (2πZ)d
and none of its sublattices. We refer to [53] and [55, Chapter 2] for details
on lattice-distributed inﬁnitely divisible laws (in the case d = 1 ); see also
the discussion of [26, Section 3.1]. Throughout this paper, we make the
following assumptions on a reference inﬁnitely divisible law µX :
• µX has moments of order 2;
• and µX is not supported on any sublattice of Zd.
Then, the corresponding Lévy–Khintchine exponent φ is twice continuously
diﬀerentiable and one has the Taylor expansion around zero
φ(ξ) = i ⟨m |ξ⟩ − ξtΣ ξ
2 +o(|ξ|2),
where m = E[X], ξt is the transpose of the column vector ξ, and Σ is
the covariance matrix of X, which is non-degenerate. Moreover, Re(φ(ξ))
admits a unique non-degenerate global maximum on [0, 2π]d at ξ = 0.
Remark 1.1. — Let (γ ∈ Rd,A ∈ M(d ×d, R), Π) be the triplet of the
Lévy–Khintchine representation of the Fourier transform of an inﬁnitely
divisible random variable X (cf. [53, Theorem 8.1]). Then, X is supported
on Zd and has a moment of order 2 if and only if:
(1) A = 0 and γ ∈ Zd;
(2) the Lévy measure Π is supported on Zd and has a second moment.
Example 1.2. — Withd = 1, suppose that X follows a Poisson distribu-
tion P(λ) with parameter λ. In this case,
φ(ξ) = λ
(
eiξ − 1
)
= iλξ −λξ2
2 +o(ξ2).
Example 1.3. — More generally, ﬁx a random variable Z with values in
Z, and consider the compound Poisson distribution X =∑ P(λ )
i=1 Zi, where
the Zi’s are independent copies of Z, and P(λ) is an independent Poisson
variable. One obtains a new inﬁnitely divisible law with values on the lattice
TOME 70 (2020), F ASCICULE 3
1120 R. CHHAIBI, F. DELBAEN, P.-L. MÉLIOT & A. NIKEGHBALI
Z, and the corresponding Lévy–Khintchine exponent is
φ(ξ) = λ
(
E[eiξZ ] − 1
)
= iλ E[Z]ξ −λ E[Z 2]ξ2
2 +o(ξ2).
Example 1.4. — The previous example is generic if one restricts oneself
to inﬁnitely divisible random variables with values in N = {0, 1, 2, 3,... };
see [38, 52]. Thus, a random variable X with values in N is inﬁnitely divis-
ible if and only it admits a representation
X =
P(λ )∑
i=1
Zi
as a compound Poisson distribution. In this representation, the Zi’s are
independent copies of a random variable Z with law
P[Z =j] = λj
λ for all j >0;
and P(λ) is an independent Poisson variable with parameter λ =∑ ∞
j=1λj.
Then, another representation of X is X =∑ ∞
j=1jUj, where the Uj’s are
independent Poisson variables with parameters λj. These parameters λj
are the solutions of the system of equations
k P[X =k] =
k∑
j=1
λjj P[X =k −j],
and this system provides a numerical criterion of inﬁnite divisibility: X is
inﬁnitely divisible if and only if the solutions λj are all non-negative.
Given a random variable X on Zd, the general question that we want to
tackle is: how close is the law µ = µX of X to an inﬁnitely divisible law
ν with exponent φ? For that purpose, one can choose diﬀerent distances
between probability measures, the typical ones being:
• the local distance :
dL(µ,ν ) := sup
k∈Zd
|µ({k}) −ν({k})|.
• the total variation distance :
dTV(µ,ν ) := 2 sup
A⊂Zd
|µ(A) −ν(A)| =
∑
k∈Zd
|µ({k}) −ν({k})|.
• and in dimension 1, the Kolmogorov distance :
dK(µ,ν ) := sup
k∈Z
|µ([ [−∞,k ] ])−ν([ [−∞,k ] ])|
= sup
k∈Z
|µ([ [k, +∞] ])−ν([ [k, +∞] ])|,
ANNALES DE L’INSTITUT FOURIER
APPROXIMATION OF DISCRETE MEASURES 1121
where [ [a,b ] ] ={a,a + 1,a + 2,...,b } denotes an integer interval.
It is well known and immediate to check that
dL(µ,ν ) ⩽ 2dK(µ,ν ) ⩽ dTV(µ,ν )
for any pair of signed measures (µ,ν ). The hardest distance to estimate
is usually the total variation distance. Note that all the previous quan-
tities metrize the convergence of signed measures on Zd with respect to
the weak or strong topology. As recalled before in the Poisson case, many
approaches for the estimation of dL, dK and dTV can be found in the lit-
erature, the most popular ones being Stein’s method, coupling methods
and semi-group methods, see [22, 54]. The use of characteristic functions
has long been considered not so eﬀective, until the remarkable series of
papers of Hwang [32, 33, 34] (see also [30, Section IX.2]). In [34], Hwang
explained how an eﬀective Poisson approximation can be achieved assum-
ing the analyticity of characteristic functions. In a similar spirit, but with
much weaker hypotheses, [7] explored this question by using the notion
of mod-φ convergence. Our paper revisits this notion, with the purpose of
showing that the phenomenons at stake ﬁnd their source in the harmonic
analysis of the torus. While [7] was devoted to the proof of unconditional
upper bounds on the distances dL, dK, dTV, here we shall be interested in
the asymptotics of these distances.
1.3. Mod- φ convergent sequences of random variables
We consider an inﬁnitely divisible law ν of exponent φ on Zd, and a
sequence of random variables (Xn)n∈N on Zd. Following [23, 26, 35], we say
that (Xn)n∈N converges mod-φ with parameters λn → +∞ and limiting
function ψ if
E
[
ei⟨ξ |Xn⟩
]
= eλnφ(ξ)ψn(ξ)
with
lim
n→∞
ψn(ξ) = ψ(ξ).
The precise hypotheses on the convergence ψn → ψ will be made explicit
when needed; typically, we shall assume it to occur in some space Cr(Td)
endowed with the norm
‖f ‖ C r = sup
|α|⩽ r
sup
ξ∈Td
|(∂αf )(ξ)|.
Let us provide a few examples which should enhance the understanding of
this notion, as well as show its large scope of applications.
TOME 70 (2020), F ASCICULE 3
1122 R. CHHAIBI, F. DELBAEN, P.-L. MÉLIOT & A. NIKEGHBALI
Example 1.5. — Consider as in Section 1.1 a sum of independent random
variables
Xn =
n∑
i=1
Bi,
withBi following a law B(pi): P[Bi = 1] = 1 −P[Bi = 0] = pi. Let us assume
that ∑ ∞
i=1pi = + ∞ and ∑ ∞
i=1(pi)2 < +∞. Then, setting λn = ∑ n
i=1pi
and µn =µXn,
ˆµn(ξ) =
n∏
i=1
(
1 +pi(eiξ − 1)
)
= eλn(eiξ −1)
n∏
i=1
(
1 +pi(eiξ − 1)
)
e−pi(eiξ −1)
= eλn(eiξ −1)
n∏
i=1
(
1 − (pi(eiξ − 1))2
2 (1 +o(1))
)
= eλn(eiξ −1)ψn(ξ)
with ψn(ξ) →ψ(ξ) =∏ ∞
i=1
(
1 +pi(eiξ − 1)
)
e−pi(eiξ −1). This inﬁnite prod-
uct converges uniformly on the circle because of the hypothesis ∑ ∞
i=1(pi)2 <
∞. So, one has mod-Poisson convergence with parameters λn.
The following two examples will later be generalized to the multidimen-
sional setting.
Example 1.6. — Ifσ is a permutation of the integers in [ [1,n ] ], denoteℓ(σ)
its number of disjoint cycles, including the ﬁxed points. We then set ℓn =
ℓ(σn), where σn is taken at random uniformly among the n! permutations
of Sn. Using Feller’s coupling (cf. [1]), one can show that ℓn admits the
following representation in law:
ℓn =
n∑
i=1
B
(1
i
)
,
where the Bernoulli random variables are independent. This representation
will also be made clear by the discussion of Section 5.3 in the present paper.
By the discussion of the previous example, (ℓn)n∈N converges mod-Poisson
with parameters Hn =∑ n
i=1
1
i and limiting function
∞∏
i=1
(
1 + eiξ − 1
i
)
e− eiξ −1
i = 1
Γ(e iξ) eγ (eiξ −1),
whereγ is the Euler–Mascheroni constant γ = limn→∞(Hn − logn) (see [3]
for this inﬁnite product representation of the Γ -function, due to Weier-
strass). Thus, one can also say that (ℓn)n∈N converges mod-Poisson with
parameters λn = logn and limiting function
ψ(ξ) = 1
Γ(e iξ).
ANNALES DE L’INSTITUT FOURIER
APPROXIMATION OF DISCRETE MEASURES 1123
Example 1.7. — As pointed out in [35, 41], mod- φ convergence is a com-
mon phenomenon in probabilistic number theory. For instance, denote ω(k)
the number of distinct prime divisors of an integer k /greaterorequalslant1, and ω(Nn) the
number of distinct prime divisors of a random integer Nn smaller than n,
taken according to the uniform law. Then, it can be shown by using the
Selberg–Delange method (cf. [57, Section II.5]) that
E[ezω(Nn)] = 1
n
n∑
k=1
ezω(k) = e (log logn)(ez−1)
(
Ψ(e z) +O
( 1
logn
))
with
Ψ( z) = 1
Γ( z)
∏
p prime
(
1 + z − 1
p
)
e− z−1
p ,
and where the remainder O( 1
logn ) is uniform for z in a compact subset of C.
Therefore, one has mod-Poisson convergence at speed λn = log logn, and
with limiting function ψ(ξ) = Ψ(e iξ). This limiting function involves two
factors: the limiting function 1
Γ(e iξ ) of the number of cycles of a random
permutation (“geometric” factor), and an additional “arithmetic” factor
∏
p∈P(1 + eiξ −1
p ) exp( − eiξ −1
p ). This appearance of two limiting factors is a
common phenomenon in number theory [35, 41].
Let (Xn)n∈N be a sequence of random variables that converges mod-
φ with parameters λn. Informally, ψn(ξ) = E[ei⟨ξ |Xn⟩ ] e−λnφ(ξ) measures
a deconvolution residue, and mod- φ convergence means that this residue
stabilizes, allowing the computation of equivalents of d(µn,νn), where
µn = law of Xn;
νn = law of the inﬁnitely divisible law with exponent λnφ
andd is one of the distances introduced in the previous paragraph. This set-
ting will be called the basic approximation scheme for a mod- φ convergent
sequence.
1.4. The Wiener algebra and the general scheme of
approximation
As explained before, we shall be interested in more general approximation
schemes, with signed measures νn that are closer to µn than the basic
scheme. When d = 1 , the appearance of signed measures is natural in
the setting of the Wiener algebra of absolutely convergent Fourier series
(see [37, 39]):
TOME 70 (2020), F ASCICULE 3
1124 R. CHHAIBI, F. DELBAEN, P.-L. MÉLIOT & A. NIKEGHBALI
Definition 1.8. — The Wiener algebra A = A (T) is the algebra of
continuous functions on the circle whose Fourier series converges absolutely.
It is a Banach algebra for the pointwise product and the norm
‖f ‖ A :=
∑
n∈Z
|cn(f )|,
where cn(f ) denotes the Fourier coeﬃcient
∫ 2π
0 f (eiθ) e−inθ dθ
2π .
Note that the characteristic function of any signed measure µ on Z be-
longs to the Wiener algebra, with
‖ˆµ‖ A =
∑
n∈Z
|cn(ˆµ)| =
∑
n∈Z
|µ(n)| = ‖µ‖ TV
equal to the total variation norm of the measure. Thus, A is the right
functional space in order to use harmonic analysis tools when dealing with
(signed) measures. To the best of our knowledge, this interpretation of the
total variation distance as the norm of A has not been used before. On the
other hand, another important property of the Wiener algebra is:
Proposition 1.9 (Wiener’s 1
f theorem). — Let f ∈ A . Then f never
vanishes on the circle if and only if 1
f ∈ A .
We refer to [45] for a short proof of the Wiener theorem. As a conse-
quence, ifXn is a Z-valued random variable and if ν is an inﬁnitely divisible
distribution with exponent φ, then the deconvolution residue
ψn(ξ) = E[eiξXn] e−λnφ(ξ)
belongs to A , so it is a convergent Fourier series ψn(ξ) =∑ ∞
k=−∞ak,n eikξ.
The idea is then to replace this residue ψn by a simpler residue χn ∈ A ,
which after reconvolution by eλnφ(ξ) yields a signed measure approximating
the law of Xn. We are thus led to:
Definition 1.10. — Let (Xn)n∈N be a sequence of random variables
in Zd that is mod- φ convergent with parameters (λn)n∈N. A general ap-
proximation scheme for (Xn)n∈N is given by a sequence of discrete signed
measures (νn)n∈N on Zd, such that
ˆµn(ξ) = E[ei⟨ξ |Xn⟩ ] = eλnφ(ξ)ψn(ξ);
ˆνn(ξ) = eλnφ(ξ)χn(ξ),
with limn→+∞ψn(ξ) = ψ(ξ) and limn→+∞χn(ξ) = χ(ξ). Here, the residues
ψn, ψ, χn and χ are functions on the torus Td = ( R/2πZ)d that have ab-
solutely convergent Fourier series, and with χn(0) = χ(0) = 1 (hence,
ANNALES DE L’INSTITUT FOURIER
APPROXIMATION OF DISCRETE MEASURES 1125
νn(Zd) = 1 ). The convergence of the residues ψn → ψ and χn → χ is as-
sumed to be at least uniform on the torus, that is in the space of continuous
functions C 0(T).
The basic approximation scheme is the case when χn(ξ) = χ(ξ) = 1 .
The residues χn and χ will typically be trigonometric polynomials, and
they will enable us to enhance considerably the quality of our discrete
approximations.
Example 1.11. — An important case of approximation scheme in the
sense of Deﬁnition 1.10 is the approximation scheme of orderr /greaterorequalslant1. Suppose
thatd = 1 and that the functions ψn(ξ) can be represented on the torus as
absolutely convergent series
ψn(ξ) = 1 +
∞∑
k=1
bk,n (eiξ − 1)k +
n∑
k=1
ck,n (e−iξ − 1)k.
The coeﬃcients ak,n of ψn(ξ) = ∑ ∞
k=−∞ak,n eikξ are related to the coeﬃ-
cientsbk,n and ck,n by the equations
bk,n =
∑
l/greaterorequalslantk
(l
k
)
al,n ; ck,n =
∑
l/greaterorequalslantk
(l
k
)
a−l,n
for all k /greaterorequalslant1. Set then
χ(r)
n (ξ) = P (r)
n (eiξ) = 1 +
r∑
k=1
bk,n (eiξ − 1)k +
r∑
k=1
ck,n (e−iξ − 1)k.
The χ(r)
n (ξ) are the Laurent polynomials of degree r that approximate the
residues ψn around 0 at order r /greaterorequalslant1. Then, if Xn is a random variable
with law µn with characteristic function ˆµn(ξ) = e λnφ(ξ)ψn(ξ), the ap-
proximation scheme of order r of µn is given by the signed measures ν(r)
n ,
with
ˆν(r)
n (ξ) = eλnφ(ξ)χ(r)
n (ξ).
We shall prove in Section 3 that dL(µn,ν (r)
n ),dK(µn,ν (r)
n ) anddTV(µn,ν (r)
n )
get smaller when r increases; in particular, ν(r/greaterorequalslant1)
n is asymptotically a better
approximation of µn than the basic scheme ν(0)
n .
One can give a functional interpretation to the approximation schemes of
orderr /greaterorequalslant1. Denote as before P (r)
n the Laurent approximation of order r of
ψn, and introduce the shift operator S on functions f : Z → C, deﬁned by
(Sf )(k) = f (k + 1).
TOME 70 (2020), F ASCICULE 3
1126 R. CHHAIBI, F. DELBAEN, P.-L. MÉLIOT & A. NIKEGHBALI
If ν(r)
n is the signed measure with Fourier transform given by
ˆν(r)
n (ξ) = eλnφ(ξ)P (r)
n (eiξ),
then for any square-integrable functionf : Z → C, if ˆf (ξ) =∑
k∈Zf (k) eikξ,
then
ν(r)
n (f ) =
∑
k∈Z
ν(r)
n ({k})f (k) = 1
2π
∫ 2π
0
ˆν(r)
n (ξ)ˆf (ξ) dξ
= 1
2π
∫ 2π
0
ˆν(0)
n (ξ)P (r)
n (eiξ)ˆf (ξ) dξ
= 1
2π
∫ 2π
0
ˆν(0)
n (ξ) ˆ(P (r)
n (S)f )(ξ) dξ
=ν(0)
n (P (r)
n (S)f ).
Moreover, the operatorP (r)
n (S) is a linear combination of discrete diﬀerence
operators:
P (r)
n (S) = id +
r∑
k=1
bk,n (∆ +)k +
r∑
k=1
ck,n (∆ −)k
with
(∆ k
+(f ))(j) =
k∑
l=0
(−1)k−l
(k
l
)
f (j +l);
(∆ k
−(f ))(j) =
k∑
l=0
(−1)k−l
(k
l
)
f (j −l).
Therefore:
Proposition 1.12. — In the previous setting, if (ν(r)
n )n∈N is the
approximation scheme of order r /greaterorequalslant1 of a sequence of probability
measures (µn)n∈N that is mod-φ convergent, then for any square-integrable
function f ,
ν(r)
n (f ) = E[(P (r)
n (S)(f ))(Yn)],
where Yn follows an inﬁnitely divisible law with exponent λnφ. Thus, to
estimate at order r the expectation µn(f ) = E[f (Xn)]:
(1) one replaces Xn by an inﬁnitely divisible random variable Yn;
(2) and one also replaces the function f byP (r)
n (S)(f ), which is better
suited for discrete approximations.
ANNALES DE L’INSTITUT FOURIER
APPROXIMATION OF DISCRETE MEASURES 1127
Remark 1.13. — Our notion of approximation scheme should be com-
pared to the one of [34], which is the particular case where the reference
inﬁnitely divisible law is Poissonian, and the residues χn are constant equal
to one. One of the main interest of our approach is that we are able to con-
struct better schemes of approximation, by allowing quite general residues
χn in the Fourier transform of the laws νn that approximate the ran-
dom variables Xn. On the other hand, we consider only three distances
among those studied in [34], but there should be no diﬃculty in adapting
our results to the other distances, such as the Wasserstein metric and the
Hellinger/Matusita metric.
Remark 1.14. — The approximation scheme of order r /greaterorequalslant1 can be con-
sidered as a discrete analogue of the Edgeworth expansion in the central
limit theorem, which is with respect to the Gaussian approximation, and
thus gives results for a diﬀerent scale of ﬂuctuations [47, Chapter VI].
1.5. Outline of the paper
Placing ourselves in the setting of a general approximation scheme, one
basic idea in order to evaluate the distances between the distributions µn
and νn is to relate them to the distances between the two residues ψn(ξ)
and χn(ξ) in the Wiener algebra A (Td). In Section 2, we prove various
concentration inequalities in this algebra, and we explain how to use them
in order to compute distances between distributions. In Section 3, we apply
these results to obtain asymptotic estimates for the distances in the general
approximation scheme (see our main Theorems 3.3, 3.6 and 3.11). In these
two sections, we shall restrict ourselves to the one-dimensional setting,
postponing the more involved computations of the higher dimensions d /greaterorequalslant2
to Section 5.
In Section 4, we apply our theorem to various one-dimensional examples
of mod-Poisson convergent sequences:
• In Section 4.1, we explain how to use the general theory with the
toy-model of sums of independent Bernoulli random variables (clas-
sical Poisson approximation). The combinatorics of the approxima-
tion schemes of order r /greaterorequalslant1 can be encoded in the algebra of sym-
metric functions, and we explain this encoding in Section 4.2, by
using the theory of formal alphabets. The formal alphabets provide
a simple description of the approximation schemes for all the exam-
ples hereafter, although none of them (except the toy-model) come
from independent Bernoulli variables.
TOME 70 (2020), F ASCICULE 3
1128 R. CHHAIBI, F. DELBAEN, P.-L. MÉLIOT & A. NIKEGHBALI
• In Section 4.3, we study the number of disjoint cycles in a model of
random permutations which generalises the uniform and the Ewens
measure (Example 1.6). The mod-Poisson convergence of this model
was proven in [46], and we compute here the approximation schemes
of this model.
• In Section 4.4, we show more generally how to use generating series
with algebraico-logarithmic singularities to construct general ap-
proximation schemes of statistics of random combinatorial objects.
We study with this method the number of irreducible factors of a
random monic polynomial over the ﬁnite ﬁeld Fq (counted with or
without multiplicity), and the number of connected components of
a random functional graph.
• In Section 4.5, we consider the number of distinct prime divisors of
a random integer (Example 1.7). We explain how to use the form of
the residue ψ(ξ) of mod-Poisson convergence to construct explicit
approximation schemes of the corresponding probability measures,
using again the formalism of symmetric functions.
Our approach also allows us to measure the gain of the Poissonian ap-
proximation in comparison to the Gaussian approximation, when one has
a sequence of random integers that behaves asymptotically like a Poisson
random variable with a large parameter λn. In Section 5, we extend our re-
sults to the multi-dimensional setting. One of the advantages of the Fourier
approach to approximation of probability measures is that it allows one to
deal with higher dimensions with the exact same techniques, although the
computations are more involved. There is however an important diﬀerence
from the one-dimensional setting: the dependence between the coordinates
of a mod- φ convergent sequence (Xn)n∈N in Zd has an inﬂuence over the
asymptotics of the distances between the laws of the random variables and
their approximation schemes. Note that this happens even when the ref-
erence inﬁnitely divisible distribution corresponds to independent coordi-
nates. We provide two examples of this phenomenon, stemming respectively
from the combinatorics of the wreath products Sn ≀ (Z/dZ) and from the
number theory of residue classes of prime numbers.
2. Concentration inequalities in the Wiener algebra
For convenience, until Section 5, we shall focus on the one-dimensional
case (d = 1) and the corresponding torus T = R/2πZ, which we view as the
ANNALES DE L’INSTITUT FOURIER
APPROXIMATION OF DISCRETE MEASURES 1129
set of complex numbers of modulus 1. Thus, a function on T will be a func-
tion of eiξ with ξ ∈ [0, 2π). For p ∈ [1, +∞), the space of complex-valued
functions on T whose p-powers are Lebesgue integrable will be denoted
Lp = Lp(T); it is a Banach space for the norm
‖f ‖p :=
(∫ 2π
0
|f (eiξ)|p dt
2π
) 1
p
.
Forp = +∞, L ∞(T) is the space of essentially bounded functions on the
torus, with Banach space norm
‖f ‖ ∞ := ess-supξ∈[0,2π]
⏐
⏐f (eiξ)
⏐
⏐.
In the sequel, we abbreviate sometimes the Haar integral
∫ 2π
0 f (eiξ) dξ
2π by∫
Tf (eiξ), or simply
∫
Tf .
2.1. Deconvolution residues in the Wiener algebra
Recall that the Wiener algebra A (T) is the complex algebra of absolutely
convergent Fourier series, endowed with the norm ‖f ‖ A =∑
n∈Z |cn(f )|.
We shall use the following property of A (T), which is akin to Poincaré’s
inequality for Sobolev spaces (see [39, Section 6.2]):
Proposition 2.1. — There is a constant CH = π√
3 = 1. 814... such
that
‖f ‖ A ⩽ |c0(f )| +CH ‖f ′‖ L 2
for all f ∈ A .
Proof. — Combining the Cauchy–Schwarz inequality and the Parseval
identity, we obtain
‖f ‖ A = |c0(f )| +
∑
n⁄=0
1
n |ncn(f )|
⩽ |c0(f )| +
√ ∑
n⁄=0
1
n2
√ ∑
n⁄=0
|ncn(f )|2
⩽ |c0(f )| +
√
π2
3 ‖f ′‖ L 2.
Note that the inequality is sharp, and it implies that the Sobolev space
W 1,2(T) of L 2 functions on T with weak derivative in L 2 is topologically
included in the Wiener algebra. □
TOME 70 (2020), F ASCICULE 3
1130 R. CHHAIBI, F. DELBAEN, P.-L. MÉLIOT & A. NIKEGHBALI
Another important tool for the computation of total variation distances
is the following Lemma 2.2. Call deconvolution residue of a signed measure
µ on Z by another signed measure ν on Z the function
δ(ξ) := ˆµ(ξ) (ˆν(ξ))−1.
By Wiener’s theorem, if ˆν never vanishes, which is for instance the
case when it is the Fourier transform of an inﬁnitely divisible law ν [53,
Lemma 7.5], then ˆν−1 ∈ A and the previous deconvolution happens in the
Wiener algebra: δ ∈ A . Now, in order to measure the distance between
the law µ ofX and a reference law ν, one can adopt the following point of
view, which is common in signal processing. For the deconvolution residue
to be considered as a small noise, δ has to be close to the constant function
1 (the Fourier transform of the Dirac distribution at zero). In particular,
suppose that we are given a general scheme of approximation of a sequence
of random variables (Xn)n∈N by a sequence of laws (νn)n∈N. Then, with the
notation of Deﬁnition 1.10, one has a sequence of deconvolution residues
δn(ξ) = ˆµn(ξ)
ˆνn(ξ),
and the quality of our scheme of approximation will be related to the speed
of convergence of (δn)n∈N towards the constant function 1. More precisely:
Lemma 2.2 (Fundamental inequality for deconvolution residues) .
Letµ andν be two signed measures on Z andδ =ˆµ
ˆν be the deconvolution
residue (we assume that ˆν does not vanish on T). For any c ∈ A ,
dTV(µ,ν ) ⩽ ‖c(δ − 1)ˆν‖ A + ‖δ − 1‖ A ‖ (1 −c)ˆν‖ A .
Proof.
dTV(µ,ν ) = ‖ˆµ −ˆν‖ A = ‖ (δ − 1)ˆν‖ A
⩽ ‖c(δ − 1)ˆν‖ A + ‖ (1 −c)(δ − 1)ˆν‖ A
⩽ ‖c(δ − 1)ˆν‖ A + ‖δ − 1‖ A ‖ (1 −c)ˆν‖ A . □
In practice, c ∈ A will be a carefully chosen cut function concentrated
on regions where ˆν is large. So, informally, ν is a good approximation of µ
if the deconvolution residue δ:
• is close to 1 whereˆν is large;
• has a reasonable norm in the Wiener algebra.
Note that the fundamental inequality does rely on the algebra norm of
A (T). We now quantify this idea.
ANNALES DE L’INSTITUT FOURIER
APPROXIMATION OF DISCRETE MEASURES 1131
2.2. Estimates of norms in the Wiener algebra
In this paragraph, we ﬁx two discrete measures µ andν on Z, both being
convolutions of an inﬁnitely divisible law with exponent λφ by residues ψ
and χ:
ˆµ(ξ) = eλφ(ξ)ψ(ξ);
ˆν(ξ) = eλφ(ξ)χ(ξ).
In Section 3, we shall recover the setting of a general approximation scheme
by adding indices n to this situation. We denote m and σ2 the ﬁrst two
coeﬃcients of the Taylor expansion of φ around 0:
φ(ξ) = miξ − σ2ξ2
2 +o(ξ2).
We then ﬁx an integer r /greaterorequalslant0 such that:
(1) the residues ψ and χ are assumed to be (r + 1) times continuously
diﬀerentiable on [−ε,ε ] for a certain ε> 0;
(2) their Taylor expansion coincides at 0 up to the r-th order:
∀s ∈ [ [0,r ] ], (ψ −χ)(s) (0) = 0.
In this setting, we deﬁne the non-negative quantities
βr+1(ε) = sup
ξ∈[−ε,ε]
⏐
⏐
⏐(ψ −χ)(r+1)(ξ)
⏐
⏐
⏐ ;
γ(ε) = sup
ξ∈[−ε,ε]
⏐
⏐φ′′(ξ) +σ2⏐
⏐ ;
M = − sup
ξ∈[−π,π]
(Re(φ(ξ))
ξ2
)
.
For instance, if φ(ξ) = e iξ − 1 is the exponent of the standard Poisson law,
thenγ(ε) = 2 sin( ε
2 ) andM = 2
π2 . The strict positivity of M as soon as φ is
not the constant distribution concentrated at 0 is proven in [26, Section 3].
Note that for any ξ ∈ [−ε,ε ], one has
Re(φ(ξ)) =
∫ ξ
θ=0
(ξ −θ) Re(φ′′(θ)) dθ
= −σ2ξ2
2 +
∫ ξ
θ=0
(ξ −θ) Re(φ′′(θ) +σ2) dθ ⩽ (γ(ε) −σ2)ξ2
2 .
On the other hand, outside the interval [−ε,ε ], one can use the inequality
Re(φ(ξ)) ⩽ −Mξ 2.
TOME 70 (2020), F ASCICULE 3
1132 R. CHHAIBI, F. DELBAEN, P.-L. MÉLIOT & A. NIKEGHBALI
Theorem 2.3 (Norm estimate) . — Takeε small enough so that γ(ε) ⩽
σ2
2 , and suppose that λ is large enough so that λ /greaterorequalslant2
σ2 . Then:
‖ˆµ −ˆν‖ A ⩽ ‖ψ −χ‖ A
(
1 +CH
(√
2
πε +λ‖φ′‖ ∞
))
e− λM ε 2
4
+ Cr+1βr+1(ε) (ε−1 +
√
5(r + 1))
(σ2
2 λ)
r
2 + 1
4
,
where Cr+1 is a constant depending only on r:
Cr+1 = 1
(r + 1)!
√
2π
3 Γ
(
r + 3
2
)
.
In order to prove this theorem, we introduce the cut function ξ ∈ T ↦→
c(ξ) that is piecewise linear, vanishes outside of [−ε,ε ], and is equal to 1
on [−ε
2, ε
2 ], see Figure 2.1.
−ε
2
ε
2ε ε
ξ
c(ξ)
Figure 2.1. The cut-function c(ξ).
Lemma 2.4. — Under the assumptions of Theorem 2.3,
‖
‖ (1 −c) eλφ‖
‖
A ⩽
(
1 +CH
(√
2
πε +λ‖φ′‖ ∞
))
e− λM ε 2
4 .
Proof. — Note that |(1 −c(ξ)) eλφ(ξ)| vanishes on [−ε
2, ε
2 ], and is smaller
than e−λMξ 2
⩽ e− λM ε 2
4 everywhere else. We then use Proposition 2.1:
‖
‖ (1 −c) eλφ‖
‖
A ⩽
∫
T
|1 −c| eλ Re(φ) +CH
‖
‖ −c′eλφ + (1 −c)λφ′ eλφ‖
‖
L 2
⩽ e− λM ε 2
4 +CH
‖
‖c′eλφ‖
‖
L 2 +CHλ‖φ′‖ ∞
‖
‖ (1 −c) eλφ‖
‖
L 2
ANNALES DE L’INSTITUT FOURIER
APPROXIMATION OF DISCRETE MEASURES 1133
⩽ e− λM ε 2
4 +CH ‖c′‖ L 2 e− λM ε 2
4 +CHλ‖φ′‖ ∞ e− λM ε 2
4
⩽
(
1 +CH
(√
2
πε +λ‖φ′‖ ∞
))
e− λM ε 2
4 . □
Lemma 2.5. — Under the assumptions of Theorem 2.3, we have:
‖
‖c (ψ −χ) eλφ‖
‖
A ⩽ Cr+1βr+1(ε) (ε−1 +
√
5(r + 1))
(σ2
2 λ)
r
2 + 1
4
.
Proof. — Note that the norm ‖ · ‖ A is invariant after multiplication by
eikξ,k ∈ Z. In particular,
‖
‖c (ψ −χ) eλφ‖
‖
A =
‖
‖
‖c(ξ) (ψ(ξ) −χ(ξ)) eλφ(ξ)−iξ⌊λm⌋
‖
‖
‖
A
,
where ⌊ · ⌋ denotes the integer part of a real number. Using again Proposi-
tion 2.1, we obtain
‖
‖c (ψ −χ) eλφ‖
‖
A
⩽
∫
T
|c (ψ −χ) eλφ| +CH
‖
‖
‖
‖
(
c(ξ) (ψ(ξ) −χ(ξ)) eλφ(ξ)−iξ⌊λm⌋
) ′‖
‖
‖
‖
L 2
⩽
∫
T
|c (ψ −χ) eλφ| +CH
‖
‖c′ (ψ −χ) eλφ‖
‖
L 2
+CH
‖
‖c (ψ −χ)′ eλφ‖
‖
L 2 +CH
‖
‖c (ψ −χ) (λφ′ −i⌊λm⌋) eλφ‖
‖
L 2
⩽ A +B +C +D.
Let us bound separately each term. Recall that
∫ ∞
−∞ |t|re−t2
dt = Γ
(r+1
2
)
for r /greaterorequalslant0.
(A) For ξ ∈ [−ε,ε ],
|ψ(ξ) −χ(ξ)| ⩽ βr+1(ε) |ξ|r+1
(r + 1)! ;
eλ Re(φ(ξ)) ⩽ e− λ (σ 2−γ (δ )) ξ 2
2 ⩽ e− λσ 2 ξ 2
4
the last inequality following from the assumptions on ε. Conse-
quently,
A ⩽ βr+1(ε)
2π (r + 1)!
∫ ε
−ε
e− λσ 2 ξ 2
4 |ξ|r+1 dt = βr+1(ε)
2π (r + 1)! (λ σ2
4 )
r
2 +1 Γ
(r
2 + 1
)
⩽ βr+1(ε)
2π (r + 1)! (λ σ2
4 )
r
2 +1
√
Γ
(r
2 + 3
4
)
Γ
(r
2 + 5
4
)
TOME 70 (2020), F ASCICULE 3
1134 R. CHHAIBI, F. DELBAEN, P.-L. MÉLIOT & A. NIKEGHBALI
⩽ βr+1(ε)
(r + 1)! (λ σ2
2 )
r
2 +1
( 2
π
) 1
4
√
1
2π Γ
(
r + 3
2
)
.
by using the log-convexity of the Gamma function, and the dupli-
cation formula Γ(2 z) = 22z−1
√π Γ( z) Γ(z + 1
2 ).
(B) Since |c′(ξ)| ⩽ 2
ε on [−ε,ε ] and vanishes outside [−ε,ε ], one obtains
B ⩽ 2CHβr+1(ε)
ε (r + 1)!
( 1
2π
∫ ∞
−∞
e− λσ 2ξ 2
2 |ξ|2r+2 dξ
) 1
2
⩽ βr+1(ε)
(r + 1)! (λ σ2
2 )
r
2 + 3
4
2CH
ε
√
1
2π Γ
(
r + 3
2
)
.
(C) For ξ ∈ [−ε,ε ],
|(ψ −χ)′(ξ)| ⩽ βr+1(ε) |ξ|r
r! ,
so as before,
C ⩽ CHβr+1(ε)
r!
( 1
2π
∫ ∞
−∞
e− λσ 2ξ 2
2 |ξ|2r dξ
) 1
2
⩽ CHβr+1(ε)
r! (λ σ2
2 )
r
2 + 1
4
√
1
2π Γ
(
r + 1
2
)
⩽ βr+1(ε)
(r + 1)! (λ σ2
2 )
r
2 + 1
4
CH (r + 1)√
r + 1
2
√
1
2π Γ
(
r + 3
2
)
.
(D) Last, for ξ ∈ [−ε,ε ], |φ′(ξ) − iµ| ⩽ γ(δ) |ξ| ⩽ σ2|ξ|
2 , and then,
|(λφ′(ξ) − i⌊λµ⌋)| ⩽ λσ2 |ξ|
2 + |λµ − ⌊λµ⌋| ⩽ λσ2 |ξ|
2 + 1.
Therefore,
D ⩽ CHβr+1(ε)√
2π (r + 1)!
(√ ∫
R
e− λσ 2ξ 2
2 |ξ|2r+2 dξ +λσ 2
2
√ ∫
R
e− λσ 2ξ 2
2 |ξ|2r+4 dξ
)
⩽ CHβr+1(ε)√
2π (r + 1)!
(
1
(λ σ2
2 )
r
2 + 3
4
√
Γ
(
r + 3
2
)
+ 1
(λ σ2
2 )
r
2 + 1
4
√
Γ
(
r + 5
2
) )
.
ANNALES DE L’INSTITUT FOURIER
APPROXIMATION OF DISCRETE MEASURES 1135
To conclude, notice that since λ σ2
2 /greaterorequalslant1, one can take in each denominator
the smallest power of this quantity, namely, (λ σ2
2 )
r
2 + 1
4 . One thus obtains:
A +B +C +D ⩽ βr+1(ε)
(r + 1)! (λ σ2
2 )
r
2 + 1
4
√
1
2π Γ
(
r + 3
2
)
×


( 2
π
) 1
4
+CH

 2
ε + r + 1√
r + 1
2
+ 1 +
√
r + 3
2




⩽ βr+1(ε)
(r + 1)! (λ σ2
2 )
r
2 + 1
4
√
2π
3 Γ
(
r + 3
2
)( 1
ε +
√
5(r + 1)
)
by using on the last line CH = π√
3 and
2
√
5(r + 1) /greaterorequalslantr + 1√
r + 1
2
+
√
r + 3
2 + 1 +
√
3
π
( 2
π
) 1
4
. □
Proof of Theorem 2.3. — We have
‖ˆµ −ˆν‖ A ⩽ ‖ψ −χ‖ A
‖
‖ (1 −c) eλφ‖
‖
A +
‖
‖c (ψ −χ) eλφ‖
‖
A ,
and Lemmas 2.4 and 2.5 allow us to control these two terms. □
Note that if ε is ﬁxed and λ goes to inﬁnity, then the dominant term
in the norm inequality is the second one, because the ﬁrst one decreases
exponentially fast. In this case,
dTV(µ,ν ) = ‖ˆµ −ˆν‖ A =O
( 1
λ
r
2 + 1
4
)
.
The constant hidden in the O( · ) depends only on φ,r, ‖ψ −χ‖ A and the
parameterβr+1(ε) introduced before. In particular, if φ is ﬁxed and we look
at families of residues (ψn)n∈N and (χn)n∈N such that the corresponding
quantities ‖ψn −χn‖ A and βr+1,n(ε) stay bounded, then one can take a
uniform constant in the O( · ).
Remark 2.6. — One can broaden slightly the scope of Theorem 2.3, if
one notes that regarding the residues ψ and χ, one only used the bounds
|ψ(ξ) −χ(ξ)| ⩽ βr+1(ε) |ξ|r+1
(r + 1)!
and |ψ′(ξ) −χ′(ξ)| ⩽ βr+1(ε) |ξ|r
r!
TOME 70 (2020), F ASCICULE 3
1136 R. CHHAIBI, F. DELBAEN, P.-L. MÉLIOT & A. NIKEGHBALI
for any ξ ∈ [−ε,ε ]. In particular, if one assumes that ψ and χ belong to
C 1(T) and that
ψ′(ξ) −χ′(ξ) = βr+1ξr (1 +oξ(1))
r!
in a neighborhood [−ε,ε ] of 0, then the previous bounds are satisﬁed and
the conclusions of Theorem 2.3 hold. We shall use this important remark
in Section 3.3.
3. Asymptotics of distances for a general scheme of
approximation
We now consider a general scheme of approximation of a sequence of
Z-valued random variables (Xn)n∈N by a sequence of laws (νn)n∈N, with
ˆµn(ξ) = E[eiξXn] = eλnφ(ξ)ψn(ξ),
ˆνn(ξ) = eλnφ(ξ)χn(ξ),
limn→∞ψn(ξ) = ψ(ξ) and limn→∞χn(ξ) = χ(ξ) as in Deﬁnition 1.10. We
can immediately deduce from Theorem 2.3:
Proposition 3.1. — Consider a general scheme of approximation such
that the convergences ψn →ψ andχn →χ occur in C 1(T). Then, one has
dTV(µn,νn) → 0, and as well for dL(µn,νn) and dK(µn,νn).
Proof. — Takingr = 0 in Theorem 2.3, we have
dTV(µn,νn) = ‖µn −νn‖ A =O
( 1
(λn)
1
4
)
,
where the constant in the O( · ) depends on ‖ψn −χn‖ A and ‖ψn −χn‖ C 1.
By Proposition 2.1, both quantities are bounded by a function of ‖ψn −
χn‖ C 1, which is itself bounded since ψn −χn → ψ −χ in C 1(T). For the
other distances, we use the inequality dL ⩽ 2dK ⩽ dTV. □
If we want to improve on the rate of convergence of the distances to 0,
then we need an additional assumption similar to the hypothesis of Theo-
rem 2.3, namely:
(H1)
∀n ∈ N, ψn(ξ) −χn(ξ) = βn (iξ)r+1 (1 +oξ(1))
and ψ(ξ) −χ(ξ) = β (iξ)r+1 (1 +oξ(1))
with limn→∞βn = β, and the oξ(1) that converges to 0 as ξ goes to 0,
uniformly in n. We denote this condition by (H1). It is satisﬁed if, for in-
stance, the convergences ψn → ψ and χn → χ occur in Cr+1(T), and if
ANNALES DE L’INSTITUT FOURIER
APPROXIMATION OF DISCRETE MEASURES 1137
the scheme of approximation is the scheme of order r as deﬁned in Exam-
ple 1.11. However, this new condition (H1) is a bit more general, as we do
not assume that the residues χn and χ are Laurent polynomials of degree
r in eiξ.
In Section 3.1, Section 3.2 and Section 3.3, we shall consider the setting
described above, and we shall establish some exact asymptotic formulas
fordL(µn,νn),dK(µn,νn) anddTV(µn,νn). These formulas generally follow
from an application of the Laplace method to an integral representation of
the distance, but we shall also use Theorem 2.3 in order to get rid of certain
non dominant terms in the asymptotics. In Section 3.4, we introduce the
notion of derived approximation schemes which involve simpler residues,
and under appropriate assumptions, we extend the results of Sections 3.1-
3.3 to these approximation schemes.
3.1. The local distance
Until the end of this section, (Xn)n∈N denotes a sequence that is mod- φ
convergent with parameters (λn)n∈N, and (νn)n∈N is a scheme of approx-
imation of it, which satisﬁes the hypothesis (H1). The main tool in the
computation of the local distance dL(µn,νn) is:
Proposition 3.2. — The error term being uniform in k ∈ Z, one has
µn({k}) −νn({k})
= (−1)r+1β
√
2π (σ2λn)
r
2 +1
∂r+1
∂αr+1
(
e− α 2
2
) ⏐
⏐
⏐
⏐
α= k−λ nm
σ
√
λ n
+o
( 1
(λn)
r
2 +1
)
.
Proof. — The computations hereafter are very similar to those of [26,
Section 3], but they are performed at a diﬀerent scale for k. We combine
the Fourier inversion formula
µn({k}) −νn({k}) =
∫
T
(ψn(ξ) −χn(ξ)) eλnφ(ξ) e−ikξ dξ
2π
with the Laplace method. Note that (H1) implies that ψn −χn is bounded
on the whole torus T by some constant C. As a consequence, for any ε> 0,
TOME 70 (2020), F ASCICULE 3
1138 R. CHHAIBI, F. DELBAEN, P.-L. MÉLIOT & A. NIKEGHBALI
since Re(φ(ξ)) ⩽ −Mξ 2 with M >0, one has
1
2π
⏐
⏐
⏐
⏐
⏐
∫
(−π,π)\ (−ε,ε)
(ψn(ξ) −χn(ξ)) eλnφ(ξ) e−ikξ dξ
⏐
⏐
⏐
⏐
⏐
⩽ C exp
(
λn sup
ξ∈(−π,π)\ (−δ,δ)
Re(φ(ξ))
)
⩽ C exp(−λnMε 2)
=o
( 1
(λn)
r
2 +1
)
,
this being uniform in k. Then, for ε> 0 small enough, one has the estimate:
∫ ε
−ε
(ψn(ξ) −χn(ξ)) eλnφ(ξ) e−ikξ dξ
=βn (1 +oε(1))
∫ ε
−ε
(iξ)r+1 eλnφ(ξ)−ikξ dξ
=β (1 +oε(1))
∫ ε
−ε
(iξ)r+1 eλn(φ(ξ)−imξ) e−i(k−λnm)ξ dξ
= β (1 +oε(1))
(σ2λn)
r
2 +1
∫ εσ√λn
−εσ√λn
(it)r+1 e
λn
(
φ( t
σ
√
λ n
)− φ ′ (0) t
σ
√
λ n
)
e
−it k−λ nm
σ
√
λ n dt
= β (1 +oε(1))
(σ2λn)
r
2 +1
∫ ∞
−∞
(it)r+1 e− t2
2 e
−it k−λ nm
σ
√
λ n dt.
The last step uses the dominated convergence theorem. Indeed, we have
the pointwise convergence:
λn
(
φ
( t
σ√λn
)
− φ′(0)t
σ√λn
)
− →n→∞ −t2
2
and if ε is small enough so that Re(φ′′(ξ))< −σ2
2 for all ξ ∈ [−ε,ε ], then
for every t ∈ [−εσ √λn,εσ √λn]:
⏐
⏐
⏐
⏐e
λn
(
φ
(
t
σ
√
λ n
)
− φ ′ (0) t
σ
√
λ n
) ⏐
⏐
⏐
⏐ = e
λn Re
(
φ
(
t
σ
√
λ n
)
− φ ′ (0) t
σ
√
λ n
)
⩽ e(supξ ∈[−ε,ε ]Re(φ′′(ξ))) t2
2σ 2 ⩽ e− t2
4 .
The integrand is therefore dominated by e− t2
4 |t|r+1. Hence,
µn({k}) −νn({k})
= β
2π(σ2λn)
r
2 +1
(∫ ∞
−∞
(it)r+1 e− t2
2 e
−it k−λ nm
σ
√
λ n dt
)
+o
( 1
(λn)
r
2 +1
)
,
ANNALES DE L’INSTITUT FOURIER
APPROXIMATION OF DISCRETE MEASURES 1139
with a remainder uniform in k ∈ Z. Last, we use the fact that
∫ ∞
−∞
e− t2
2 e−itα dt√
2π = e − α 2
2 ,
is the Fourier transform of the standard Gaussian distribution evaluated at
ξ = −α, and by taking the (r + 1)-th derivative with respect to α, we get:
∫ ∞
−∞
(it)r+1 e− t2
2 e−itα dt√
2π = (−1)r+1 ∂r
∂αr+1
(
e− α 2
2
)
,
hence the claimed result. □
The computation of the local distance amounts then to ﬁnd the maximum
ink ∈ Z of the previous quantity. Recall that the r-th Hermite polynomial
Hr(α) is deﬁned by
Gr(α) = ∂r
∂αr
(
e− α 2
2
)
= (−1)rHr(α) e− α 2
2 .
The local extremas of Gr correspond to the zeros of Hr+1, since G′
r(α) =
(−1)r (H ′
r(α) −αHr(α)) e− α 2
2 = ( −1)r+1Hr+1(α) e− α 2
2 = Gr+1(α). De-
note zr+1 the smallest absolute value of a zero of Hr+1; it is 0 when r is
even, and it can be shown that in any case it corresponds to the global
extrema of |Gr|; see [56, Chapter 6], and Figure 3.1 for an illustration.zr+1
α
Gr(α)
Figure 3.1. The Hermite function G9; it attains its global extremas at
the smallest zeroes of H10.
TOME 70 (2020), F ASCICULE 3
1140 R. CHHAIBI, F. DELBAEN, P.-L. MÉLIOT & A. NIKEGHBALI
Theorem 3.3. — Under the assumptions stated at the beginning of this
section (general scheme of approximation with condition (H1)), one has
dL(µn,νn) = |β| |Gr+1(zr+2)|√
2π (σ2λn)
r
2 +1 +o
( 1
(λn)
r
2 +1
)
.
Proof. — DenoteZn = {k−λnm
σ√λn
, k ∈ Z}. The previous discussion shows
that
dL(µn,νn) = |β|√
2π (σ2λn)
r
2 +1 sup
α∈Zn
|Gr+1(α)| +o
( 1
(λn)
r
2 +1
)
.
As n goes to inﬁnity, the set Zn becomes dense in R, and since Gr+1 is a
Lipschitz function, we have in fact
dL(µn,νn) = |β|√
2π (σ2λn)
r
2 +1 sup
α∈R
|Gr+1(α)| +o
( 1
(λn)
r
2 +1
)
= |β| |Gr+1(zr+2)|√
2π (σ2λn)
r
2 +1 +o
( 1
(λn)
r
2 +1
)
. □
Remark 3.4. — The ﬁrst values of Mr = |Gr(zr+1)| are
M0 = |G0(0)| = 1;
M1 = |G1(1)| = e − 1
2 = 0. 60653... ;
M2 = |G2(0)| = 1;
M3 =
⏐
⏐
⏐
⏐G3
(√
3 −
√
6
) ⏐
⏐
⏐
⏐ = e − 3−
√
6
2
(
3
√
6 − 6
)
= 1. 38012... ;
M4 = |G4(0)| = 3.
In particular, M2r = (2r − 1)!! = (2r)!
2rr! .
3.2. The Kolmogorov distance
To evaluate the Kolmogorov distance between µn and νn, we use the
classical integral formula
µn([ [k, +∞] ])−νn([ [k, +∞] ]) =
∫
T
(ψn(ξ) −χn(ξ)) eλnφ(ξ) e−ikξ
1 − e−iξ
dξ
2π.
Indeed, for any l /greaterorequalslantk, one has
µn([ [k,l ] ])−νn([ [k,l ] ]) =
l∑
j=k
∫
T
(ψn(ξ) −χn(ξ)) eλnφ(ξ) e−ijξ dξ
2π
=
∫
T
(ψn(ξ) −χn(ξ)) eλnφ(ξ) e−ikξ − e−i(l+1)ξ
1 − e−iξ
dξ
2π.
ANNALES DE L’INSTITUT FOURIER
APPROXIMATION OF DISCRETE MEASURES 1141
Since ψn(ξ) −χn(ξ) = βn (iξ)r+1 (1 + o(1)), the quotient ψn(ξ)−χn(ξ)
1−eiξ is
actually a continuous function on the torus, hence bounded. The same
holds for eλnφ(ξ) = E[eiξYn], where Yn is an inﬁnitely divisible random
variable with exponent λnφ. Thus,
f (ξ) = ψn(ξ) −χn(ξ)
1 − eiξ eλnφ(ξ)
is a bounded continuous function, hence in L 1(T), and by the Riemann–
Lebesgue lemma, one concludes that
lim
l→+∞
∫
T
f (ξ) e−i(l+1)ξ dξ
2π = 0.
Since liml→+∞µn([ [k,l ] ])−νn([ [k,l ] ]) = µn([ [k, +∞] ])−νn([ [k, +∞] ]), the
integral formula is indeed shown. It leads to the analogue of Proposition 3.2
for probabilities of half-lines of integers [ [k, +∞] ]:
Proposition 3.5. — The error term being uniform in k ∈ Z, one has
µn([ [k, +∞] ])−νn([ [k, +∞] ])
= (−1)rβ
√
2π (σ2λn)
r+1
2
∂r
∂αr
(
e− α 2
2
) ⏐
⏐
⏐
⏐
α= k−λ nm
σ
√
λ n
+o
(
1
(λn)
r+1
2
)
.
Proof. — One has the Taylor expansion
ψn(ξ) −χn(ξ)
1 − e−iξ = βn(iξ)r+1
iξ (1 +oξ(1)) = βn(iξ)r (1 +oξ(1)).
Combined with the aforementioned integral formula and with the same
Laplace method as in Proposition 3.2, it yields
µn([ [k, +∞] ])−νn([ [k, +∞] ]) =β (1 +o(1))
(σ2λn)
r+1
2
∫ ∞
−∞
(it)r e− t2
2 e
−it k−λ nm
σ
√
λ n dt.
Therefore, one has the same asymptotics as in Proposition 3.2, but with r
replacing r + 1. □
The same argument as in Section 3.1 gives:
Theorem 3.6. — Under the assumptions stated at the beginning of this
section (general scheme of approximation with condition (H1)), one has
dK(µn,νn) = |β| |Gr(zr+1)|
√
2π (σ2λn)
r+1
2
+o
(
1
(λn)
r+1
2
)
.
Example 3.7. — Consider the basic scheme of approximation of a mod- φ
convergent sequence of random variables (Xn)n∈N:
ˆνn(ξ) = eλnφ(ξ).
TOME 70 (2020), F ASCICULE 3
1142 R. CHHAIBI, F. DELBAEN, P.-L. MÉLIOT & A. NIKEGHBALI
Hence,νn is the law of an inﬁnitely divisible random variable Yn with Lévy–
Khintchine exponentλnφ. Then, ifˆµn(ξ) = eλnφ(ξ)ψn(ξ) andψn(ξ) →ψ(ξ)
in C 1(T), the hypothesis (H1) is satisﬁed with r = 0 and βn →β =ψ′(0).
Therefore, in this setting,
dL(Xn,Yn) = |ψ′(0)| e− 1
2
√
2πσ 2λn
+o
( 1
λn
)
;
dK(Xn,Yn) = |ψ′(0)|√2πσ 2λn
+o
( 1√λn
)
.
The second result should be compared with a computation in [26, Chap-
ter 4], which ensures that
dK(Xn,Yn) = |ψ′(0)|
√2πλn
+o
( 1√λn
)
if (Xn)n∈N is a sequence of random real numbers that converges mod-
Gaussian with parameters λn, and if (Yn)n∈N is a sequence of random
Gaussian variables with means 0 and variances λn.
3.3. The total variation distance
Before we estimate the total variation distance between the laws µn and
νn, let us make some observations with Proposition 3.2. Assume again that
one has a general scheme of approximation which satisﬁes the hypothe-
sis (H1). For any ﬁxed interval I = [a,b ], one can write
dTV(µn,νn) =
∑
k∈Z
|µn({k}) −νn({k})|
/greaterorequalslant
⌊λnm+bσ √
λn⌋∑
k=⌊λnm+aσ √λn⌋
|µn({k}) −νn({k})|
/greaterorequalslant|βn|√
2π (σ2λn)
r
2 +1


⌊λnm+b σ√
λn⌋∑
k= ⌊λnm+a σ√λn⌋
⏐
⏐
⏐
⏐
⏐
(
Hr+1(α) e− α 2
2
)
α= k−λ nm
σ
√
λ n
⏐
⏐
⏐
⏐
⏐


+o
(
(b −a)
(σ2λn)
r+1
2
)
/greaterorequalslant|βn|√
2π (σ2λn)
r+1
2
∫ b
a
⏐
⏐
⏐Hr+1(α) e− α 2
2
⏐
⏐
⏐ dα +o
(
(b −a)
(σ2λn)
r+1
2
)
,(RS)
ANNALES DE L’INSTITUT FOURIER
APPROXIMATION OF DISCRETE MEASURES 1143
by identifying a Riemann sum in (RS). Since this is true for any a and b,
and since Hr+1(α) e− α 2
2 is integrable, we conclude that in general, one has
lim inf
n→∞
(
dTV(µn,νn) (σ2λn)
r+1
2
)
/greaterorequalslant|β|
∫
R
|Hr+1(α)| e− α 2
2
dα√
2π.
The goal of this paragraph is to show that, under a slightly stronger hy-
pothesis than (H1), this inequality is in fact an identity, and that the liminf
above is actually a limit. To this purpose, it is convenient to introduce a
third sequence (ρn)n∈N of signed measures, deﬁned by their Fourier trans-
forms
ˆρn(ξ) = eλnφ(ξ)(
ψn(ξ) −βn (eiξ − 1)r+1)
.
These signed measures have their values given by:
Lemma 3.8. — Denote ν(0)
n the inﬁnitely divisible discrete law on Z
with exponent λnφ. The signed measure ρn whose Fourier transform is
ˆρn(ξ) = eλnφ(ξ) (ψn(ξ) −βn (eiξ − 1)r+1) is given by
ρn({k}) = µn({k}) −βn
r+1∑
l=0
(−1)r+1−l
(r + 1
l
)
ν(0)
n ({k −l}).
Proof. — One expands the Fourier transform ˆ(µn −ρn)(ξ) in powers
of eiξ:
ˆ(µn −ρn)(ξ) = βn
(
eiξ − 1
) r+1
∞∑
m=−∞
ν(0)
n ({m}) eimξ
=βn
r+1∑
l=0
∞∑
m=−∞
(−1)r+1−l
(r + 1
l
)
ν(0)
n ({m}) ei(l+m)ξ
=
∞∑
k=−∞
eikξ
(
βn
r+1∑
l=0
(−1)r+1−l
(r + 1
l
)
ν(0)
n ({k −l})
)
=
∞∑
k=−∞
eikξ (µn({k}) −ρn({k})).
The result follows by identiﬁcation of the Fourier coeﬃcients. □
TOME 70 (2020), F ASCICULE 3
1144 R. CHHAIBI, F. DELBAEN, P.-L. MÉLIOT & A. NIKEGHBALI
Remark 3.9. — Suppose in particular that φ(ξ) = e iξ − 1 is the exponent
of the Poisson law P(1). We then have
µn({k}) −ρn({k}) = βn
(r+1)∧k∑
l=0
(−1)r+1−l
(r + 1
l
) (λn)k−l e−λn
(k −l)!
=βnν(0)
n ({k})
(r+1)∧k∑
l=0
(−1)r+1−l
(r + 1
l
) (λn)−lk!
(k −l)!
=βnν(0)
n ({k})c(r + 1,k,λ n),
wherec(r+1,k,λ n) is a Poisson–Charlier polynomial, see [56, Section 2.8.1].
We now assume until the end of this paragraph that all the residues ψn,
ψ, χn and χ are in C 1(T), and that
(H2)
∀n ∈ N, ψ′
n(ξ) −χ′
n(ξ) = i(r +1)βn (iξ)r + i(r + 2)γn (iξ)r+1 (1 +oξ(1))
and ψ′(ξ) −χ′(ξ) = i(r +1)β (iξ)r + i(r + 2)γ (iξ)r+1 (1 +oξ(1))
with limn→∞βn =β and limn→∞γn =γ. As in Equation (H1), the oξ(1)
tend to 0 asξ → 0, uniformly in n. We denote this new condition by (H2).
Since ψn(0) = χn(0) = ψ(0) = χ(0) = 1 , it implies by integration that
∀n ∈ N, ψn(ξ) −χn(ξ) = βn (iξ)r+1 +γn (iξ)r+2 (1 +oξ(1))
and ψ(ξ) −χ(ξ) = β (iξ)r+1 +γ (iξ)r+2 (1 +oξ(1))
so in particular (H2) is stronger than (H1). On the other hand, the hy-
pothesis (H2) is satisﬁed for instance if the convergences ψn → ψ and
χn →χ occur in Cr+2(T), and if the scheme of approximation (νn)n∈N is
the scheme of order r as deﬁned in Example 1.11.
Lemma 3.10. — Let (νn)n∈N be a general approximation scheme of a
mod-φ convergent sequence (Xn)n∈N, with the new hypothesis (H2) satis-
ﬁed. Then, with ρn deﬁned as in Lemma 3.8,
dTV(ρn,νn) = o
(
1
(λn)
r+1
2
)
.
Moreover, (ρn)n∈N is a new general approximation scheme of (Xn)n∈N, with
the hypothesis (H2) again satisﬁed, with the same parameter r /greaterorequalslant0 and
the same sequence (βn)n∈N.
ANNALES DE L’INSTITUT FOURIER
APPROXIMATION OF DISCRETE MEASURES 1145
Proof. — Denote ~ψn(ξ) = ψn(ξ) − βn (eiξ − 1)r+1, so that ˆρn(ξ) =
eλnφ(ξ)~ψn(ξ). On the one hand, one has
(~ψn −χn)′(ξ) = (ψ′
n(ξ) −χ′
n(ξ)) − i(r + 1)βn eiξ(eiξ − 1)r
= i(r + 2)
(
γn − βn(r + 1)
2
)
(iξ)r+1 (1 +oξ(1))
by using the Taylor expansion (eiξ − 1)r = (iξ)r +r(iξ)r+1
2 +o(ξr+1). By the
remark following the proof of Theorem 2.3, this is a suﬃcient condition in
order to use the norm inequality of Section 2, but with parameter r + 1
instead of r. Moreover, the sequence
(
γn − βn(r + 1)
2
)
n∈N
is convergent under the hypothesis (H2), hence bounded. As a consequence,
the sequence (~ψn −χn)n∈N is bounded in C 1(T), and therefore in A by
Proposition 2.1. For the same reason, one has a uniform bound on the
parameters
βr+2,n(ε) = sup
ξ∈[−ε,ε]
⏐
⏐
⏐(~ψn −χn)′(ξ)
⏐
⏐
⏐
|ξ|r+1 .
According to the discussion after Theorem 2.3, we can conclude that
dTV(ρn,νn) = O
(
1
(λn)
r+1
2 + 1
4
)
=o
(
1
(λn)
r+1
2
)
.
This ends the proof of the ﬁrst part of the lemma, and for the second part,
we can write
ψ′
n(ξ) −~ψn
′
(ξ) = i(r + 1)βn eiξ(eiξ − 1)r
= i(r + 1)βn (iξ)r + i(r + 2)βn(r + 1)
2 (iξ)r+1 (1 +oξ(1)),
hence the hypothesis (H2) is satisﬁed. □
The previous Lemma shows that, if under the hypothesis (H2) one wants
to obtain an estimate of dTV(µn,νn) which is a O((λn)− r+1
2 ), then one can
assume without loss of generality that
ψn(ξ) −χn(ξ) = βn (eiξ − 1)r+1,
with limn→∞βn = β (in other words, νn = ρn is given exactly by the
formula of Lemma 3.8). This is now of course much easier, and one obtains:
TOME 70 (2020), F ASCICULE 3
1146 R. CHHAIBI, F. DELBAEN, P.-L. MÉLIOT & A. NIKEGHBALI
Theorem 3.11. — Consider a general scheme of approximation (νn)n∈N
of a mod-φ convergent sequence of random variables (Xn)n∈N. We also as-
sume that the reference law φ has a third moment, so that in the neigh-
borhood of 0, φ(ξ) = −σ2ξ2
2 +O(|ξ|3). If the hypothesis (H2) is satisﬁed,
then
dTV(µn,νn) = |β|√
2π (σ2λn)
r+1
2
(∫
R
|Gr+1(α)| dα
)
+o
(
1
(λn)
r+1
2
)
.
Proof. — According to the previous discussion, we have to compute the
asymptotics of
dTV(µn,νn) = ‖ˆµn −ˆνn‖ A =βn
‖
‖
‖ eλnφ(ξ) (eiξ − 1)r+1
‖
‖
‖
A
=βn
∑
k∈Z
⏐
⏐
⏐
⏐
∫
T
eλnφ(ξ) (eiξ − 1)r+1 e−ikξ dξ
2π
⏐
⏐
⏐
⏐.
We can here follow the arguments of [34, Proposition 1], but in the general
case of a discrete reference measure with Lévy exponent φ (instead of a
Poisson distribution).
Step 1. — We remove all the terms k outside the range of the central
limit theorem Yn−λnm
σ√λn
⇀ NR(0, 1), where Yn follows the inﬁnitely divisible
law with exponent λnφ. We claim that the terms k outside the interval
I =I
(
(λn)
1
7
)
=
[[
⌊λnm −σ(λn)
1
7 + 1
2 ⌋, ⌊λnm +σ(λn)
1
7 + 1
2 ⌋
]]
give an exponentially small contribution to the sum. Indeed, note that
∑
k∈Z
|µn({k}) −νn({k})| =βn
∑
k∈Z
⏐
⏐
⏐
⏐
⏐
r+1∑
l=0
(−1)r+1−l
(r + 1
l
)
ν(0)
n ({k −l})
⏐
⏐
⏐
⏐
⏐
=
∑
k∈Z
⏐
⏐
⏐
(
(∆ −1)◦(r+1)ν(0)
n
)
({k})
⏐
⏐
⏐
= sup
f :Z→[−1,1]
(∑
k∈Z
(
(∆ −1)◦(r+1)ν(0)
n
)
({k}) f (k)
)
= sup
f :Z→[−1,1]
(∑
k∈Z
ν(0)
n ({k})
{
(∆ 1)◦(r+1)f
}
(k)
)
with the notations ∆ j of discrete derivatives introduced at the end of Sec-
tion 1.4. Indeed, ∆ 1 and ∆ −1 are adjoint operators on ℓ2(Z). By the central
limit theorem, for every f : Z → [−1, 1], the sum over terms k outside the
ANNALES DE L’INSTITUT FOURIER
APPROXIMATION OF DISCRETE MEASURES 1147
intervalI is now bounded by
2r+1 P
[ ⏐
⏐
⏐
⏐
Yn −λnm
σ√λn
⏐
⏐
⏐
⏐ /greaterorequalslant(λn)
1
7
]
=o
( 1
(λn)p
)
for every exponent p,
so it will not contribute in the asymptotics. Therefore,
dTV(µn,νn)
= |βn|
∑
k∈I((λn)
1
7 )
⏐
⏐
⏐
⏐
∫
T
eλnφ(ξ) (eiξ − 1)r+1 e−ikξ dξ
2π
⏐
⏐
⏐
⏐ +o
(
1
(λn)
r+1
2
)
.
Step 2. — We now estimate the terms with k ∈I((λn)1/7) with a more
careful application of the Laplace method than in Proposition 3.2. Namely,
outside the interval (−(λn)
1
7 − 1
2, (λn)
1
7 − 1
2 ), one can bound (eiξ − 1)r+1 by
|ξ|r+1 and eλnφ(ξ) by e−λnMξ 2
, whence
⏐
⏐
⏐
⏐
⏐
∫
(−π,π)\ (−(λn)
1
7 − 1
2,(λn)
1
7 − 1
2 )
eλnφ(ξ) (eiξ − 1)r+1 e−ikξ dξ
⏐
⏐
⏐
⏐
⏐
⩽
∫
(−π,π)\ (−(λn)
1
7 − 1
2,(λn)
1
7 − 1
2 )
e−λnMξ 2
|ξ|r+1 dξ
⩽ 2
(λn)
r+1
2
∫ ∞
(λn)
1
7
e−Mu 2
ur+1 du.
This upper bound is exponentially small and will not contribute to the
asymptotics, even after multiplication by the number of terms of the inter-
valI, which is a O((λn)
1
2 + 1
7 ). On the other hand, if k = λnm +xσ √λn,
then
1
2π
∫ (λn)
1
7 − 1
2
−(λn)
1
7 − 1
2
eλnφ(ξ) (eiξ − 1)r+1 e−ikξ dξ
= 1
2π
∫ (λn)
1
7 − 1
2
−(λn)
1
7 − 1
2
e−i(k−λnm)ξ−λn σ 2
2 ξ2
(iξ)r+1
(
1 +O((λn)
3
7 − 1
2 )
)
dξ
= (1 +o(1))
2π (σ2λn)
r
2 +1
∫ σ(λn)
1
7
−σ(λn)
1
7
e−ixu− u2
2 (iu)r+1 du
= (1 +o(1))√
2π (σ2λn)
r
2 +1 (−1)r+1Hr+1(x) e− x2
2 ,
theo(1) being uniform in k ∈I((λn)1/7). Note that we used the hypothesis
of third moment of the reference law φ in order to get the multiplicative
error term 1 +O((λn)
3
7 − 1
2 ).
TOME 70 (2020), F ASCICULE 3
1148 R. CHHAIBI, F. DELBAEN, P.-L. MÉLIOT & A. NIKEGHBALI
The proof can now be completed by using the same argument of
Riemann sums as in the beginning of this paragraph, and the convergence
βn →β. □
Remark 3.12. — The ﬁrst values of Vr =
∫
R |Gr+1(α)| dα are:
V0 = 2;
V1 = 4 e− 1
2 ;
V2 = 2 (1 + 4 e− 3
2 ).
Example 3.13. — For the basic scheme of approximation ( χn =χ = 1 ),
assume that the residues ψn converge in C 2(T), which implies hypothe-
sis (H2) with r = 0 and |β| = |ψ′(0)|. We get the following estimate for
the total variation distance between Xn and an inﬁnitely divisible random
variableYn with exponent λnφ:
dTV(Xn,Yn) = 2 |ψ′(0)|√2πσ 2λn
+o
( 1√λn
)
.
Note that this is twice the asymptotic formula for the Kolmogorov distance.
3.4. Derived scheme of approximation with constant residue
To conclude this section, let us simplify a bit the general setting of ap-
proximation of discrete measures presented in Deﬁnition 1.10. Until now,
we have worked with measures νn such that
ˆνn(ξ) = eλnφ(ξ)χn(ξ),
where the residues χn(ξ) converge to a residue χ(ξ), and on the other
hand approximate the residues ψn(ξ) associated to the random variables
Xn. For instance, χn(ξ) can be the Laurent polynomial of degree r in eiξ
derived fromψn(ξ) (scheme of approximation of orderr). In this setting, the
residuesχn(ξ) are usually very good approximations of the residues ψn(ξ),
but on the other hand they vary with n, which is quite a complication
for explicit computations. Hence, for applications, it is simpler to work
with a constant residue χ(ξ) that does not depend on n. This leads to the
following deﬁnition:
ANNALES DE L’INSTITUT FOURIER
APPROXIMATION OF DISCRETE MEASURES 1149
Definition 3.14. — Let (νn)n∈N be a general scheme of approximation
of a sequence of random variables (Xn)n∈N that converges mod- φ with
parametersλn. The derived scheme of approximation with constant residue
is the new scheme (σn)n∈N, deﬁned by the Fourier transforms
ˆσn(ξ) = eλnφ(ξ)χ(ξ),
whereχ(ξ) = limn→∞χn(ξ) is the limit of the residues of the law νn (with
the notations of Deﬁnition 1.10).
Example 3.15. — Suppose that νn =ν(r)
n is the scheme of approximation
of orderr of (Xn)n∈N (see Example 1.11), and that the convergence ψn →ψ
occurs in Cr(T). Then, the derived scheme with constant residue (σn)n∈N
is deﬁned by the Fourier transforms
ˆσn(ξ) = eλnφ(ξ)P (r)(eiξ),
whereP (r)(eiξ) is the Laurent polynomial of degree r associated to the limit
ψ of the mod-φ convergence. Thus, to compute σn(f ) withf : Z → C, one
can take a random variableYn with law of exponentλnφ, and then calculate
E[(P (r)(S)f )(Yn)]
where T =P (r)(S) is a ﬁxed linear operator, which is a ﬁnite linear com-
bination of discrete diﬀerence operators. This is clearly convenient for con-
crete applications.
Informally, if the derived scheme with constant residue (σn)n∈N is suﬃ-
ciently close to the initial scheme (νn)n∈N, then the conclusions of Theo-
rems 3.3, 3.6 and 3.11 hold also for (σn)n∈N (under the appropriate con-
dition (H1) or (H2) for (νn)n∈N). Practically, this happens as soon as the
size of χn −χ is negligible in comparison to negative powers of λn. More
precisely, we have:
Theorem 3.16. — Let (νn)n∈N be a general scheme of approximation
of a sequence (Xn)n∈N that is mod- φ convergent. We denote (σn)n∈N the
derived scheme with constant residue.
(1) Suppose that (νn)n∈N satisﬁes the hypothesis (H1). If ‖χn −χ‖ ∞ =
o
(
1
(λn)
r
2 +1
)
, then
dL(µn,σn) = |β| |Gr+1(zr+2)|√
2π (σ2λn)
r
2 +1 +o
( 1
(λn)
r
2 +1
)
.
TOME 70 (2020), F ASCICULE 3
1150 R. CHHAIBI, F. DELBAEN, P.-L. MÉLIOT & A. NIKEGHBALI
(2) Suppose that (νn)n∈N satisﬁes the hypothesis (H1). If ‖χ′
n −χ′‖ ∞ =
o
(
1
(λn)
r+1
2
)
, then
dK(µn,σn) = |β| |Gr(zr+1)|√
2π (σ2λn)
r+1
2
+o
(
1
(λn)
r+1
2
)
.
(3) Suppose that (νn)n∈N satisﬁes the hypothesis (H2). If ‖χ′
n −χ′‖ ∞ =
o
(
1
(λn)
r
2 + 5
4
)
, then
dTV(µn,σn) = |β|√
2π (σ2λn)
r+1
2
(∫
R
|Gr+1(α)| dα
)
+o
(
1
(λn)
r+1
2
)
.
Proof. — In each case, we have to bound the distance between νn and
the derived scheme σn. For the local distance, one has
dL(νn,σn) = sup
k∈Z
⏐
⏐
⏐
⏐
∫
T
(χn(ξ) −χ(ξ)) eλnφ(ξ) e−ikξ dξ
2π
⏐
⏐
⏐
⏐
⩽ ‖χn −χ‖ ∞ =o
( 1
(λn)
r
2 +1
)
,
hence the estimate on dL(µn,σn). For the Kolmogorov distance, notice that
⏐
⏐
⏐
⏐
χn(ξ) −χ(ξ)
1 − e−iξ
⏐
⏐
⏐
⏐ ⩽ ‖χ′
n −χ′‖ ∞
⏐
⏐
⏐
⏐
ξ
1 − e−iξ
⏐
⏐
⏐
⏐ ⩽ π ‖χ′
n −χ′‖ ∞
for any ξ ∈ (−π,π ). Therefore,
dK(νn,σn) = sup
k∈Z
⏐
⏐
⏐
⏐
∫
T
χn(ξ) −χ(ξ)
1 − e−iξ eλnφ(ξ) e−ikξ dξ
2π
⏐
⏐
⏐
⏐
⩽ π‖χ′
n −χ′‖ ∞ =o
(
1
(λn)
r+1
2
)
,
hence the estimate on dK(µn,σn). Last, for the total variation distance, we
use Proposition 2.1:
dTV(νn,σn) =
‖
‖
‖ (χn −χ)(ξ) eλnφ(ξ)
‖
‖
‖
A
⩽ ‖χn −χ‖ ∞ +CH ‖ ((χn −χ)′(ξ) +λnφ′(ξ) (χn −χ)(ξ)) eλnφ(ξ)‖ L 2
⩽ π‖χ′
n −χ′‖ ∞ +CH (‖χ′
n −χ′‖ ∞ +λn ‖φ′‖ ∞ ‖χn −χ‖ ∞) ‖ eλnφ(ξ)‖ L 2
⩽ ‖χ′
n −χ′‖ ∞
(
π +CH (1 +πλn ‖φ′‖ ∞) ‖ eλnφ(ξ)‖ L 2
)
.
ANNALES DE L’INSTITUT FOURIER
APPROXIMATION OF DISCRETE MEASURES 1151
Since |eφ(ξ)| ⩽ e−Mξ 2
, we have the estimate ‖ eλnφ(ξ)‖ L 2 = O( 1
(λn)1/ 4 ), so
in the end
dTV(νn,σn) = O
(
‖χ′
n −χ′‖ ∞ (λn)
3
4
)
=o
(
1
(λn)
r+1
2
)
,
whence the estimate on dTV(µn,σn). □
4. One-dimensional applications
In this section, we apply our main Theorems 3.3, 3.6 and 3.11 to vari-
ous one-dimensional examples, most of them coming from number theory
or combinatorics. In each case, we compute the exact asymptotics of the
distances for the basic approximation scheme, and for some better approx-
imation schemes, which are derived from the approximation schemes of
order r /greaterorequalslant1.
4.1. Poisson approximation of a sum of independent Bernoulli
variables
As in Example 1.5, we consider a sum Xn =∑ n
j=1 B(pj) of independent
Bernoulli random variables, with ∑ ∞
j=1pj = + ∞ and∑ ∞
j=1(pj)2 < +∞.
The corresponding Fourier transforms are:
ˆµn(ξ) = eλn(eiξ −1)ψn(ξ) with ψn(ξ) =
n∏
j=1
(1 +pj(eiξ − 1)) e−pj (eiξ −1).
It is convenient to have an exact formula for the expansion in Laurent series
of the deconvolution residues ψn. Denote
p1,n = 0 and pk/greaterorequalslant2,n =
n∑
j=1
(pj)k.
One has
ψn(ξ) =


n∏
j=1
(1 +pj(eiξ − 1))

 e
−
∑ n
j=1pj (eiξ −1)
= exp


n∑
j=1
log(1 +pj(eiξ − 1)) −pj(eiξ − 1)


TOME 70 (2020), F ASCICULE 3
1152 R. CHHAIBI, F. DELBAEN, P.-L. MÉLIOT & A. NIKEGHBALI
= exp


n∑
j=1
∞∑
k=2
(−1)k−1
k (pj(eiξ − 1))k


= exp
( ∞∑
k=1
(−1)k−1
k pk,n (eiξ − 1)k
)
.
Denote P the set of integer partitions, that is to say ﬁnite non-increasing
sequences of positive integers
L = (L1 /greaterorequalslantL2 /greaterorequalslant· · · /greaterorequalslantLr > 0).
If L is an integer partition, we denote |L| =∑ r
i=1Li; ℓ(L) = r; mk(L) the
number of parts of L of size k; and zL =∏
k/greaterorequalslant1kmk(L)mk(L)!, which is the
size of the centralizer of a permutation of cycle-type L in the symmetric
group S|L|. The previous power series in eiξ − 1 expands then as
ψn(ξ) =
∑
L∈P
(−1)|L|−ℓ(L)
zL
pL,n (eiξ − 1)|L|,
where pL,n =∏ ℓ(L)
i=1 pLi,n. Since pn,1 = 0, the sum actually runs over integer
partitions without part equal to 1. In particular, one has
ψn(ξ) = 1 − p2,n
2 (eiξ − 1)2 + p3,n
3 (eiξ − 1)3 +o(|ξ|3).
Consider then the basic approximation scheme (ν(0)
n )n∈N of the sequence of
random variables (Xn)n∈N, which is mod-Poisson convergent with param-
eters λn =∑ n
j=1pj and limit ψ(ξ) = ∏ ∞
j=1(1 +pj(eiξ − 1)) e−pj (eiξ −1). It
satisﬁes the hypothesis (H1) with r = 1 and
βn = − 1
2 p2,n ; β = − 1
2 p2 = − 1
2
∞∑
j=1
(pj)2.
By Theorems 3.3 and 3.6, if (Yn)n∈N is a sequence of Poisson random
variables with parameters λn, then
dL(Xn,Yn) = p2
2
√
2π(λn)
3
2
+o
( 1
(λn)
3
2
)
;
dK(Xn,Yn) = p2
2
√
2π eλn
+o
( 1
λn
)
.
The sequence of inﬁnitely divisible laws (ν(0)
n )n∈N also satisﬁes the hypoth-
esis (H2), since the expansion of ψn(ξ) given before is exact and can be
derived term by term. So, one can apply Theorem 3.11, and
dTV(Xn,Yn) = 2 p2√
2π eλn
+o
( 1
λn
)
.
ANNALES DE L’INSTITUT FOURIER
APPROXIMATION OF DISCRETE MEASURES 1153
This last estimate should be compared with the unconditional bound
dTV(Xn,Yn) ⩽ 2 p2,n
λn
= 2
∑ n
j=1(pj)2
∑ n
j=1pj
stemming from the Chen–Stein method. On the other hand, we recover the
asymptotic formula for dTV(Xn,Yn) established by Deheuvels and Pfeifer
in [22], using only tools from harmonic analysis (instead of the semi-group
method developed in loc. cit. ).
We now look at a higher order approximation scheme, namely, the ap-
proximation scheme (ν(2)
n )n∈N of order r = 2 . It is deﬁned by the Fourier
transforms
ˆν(2)
n (ξ) = eλn(eiξ −1)
(
1 − p2,n
2 (eiξ − 1)2
)
.
Again, the hypotheses (H1) and (H2) are satisﬁed, this time with r = 2
and
βn = 1
3 p3,n ; β = 1
3 p3 = 1
3
∞∑
j=1
(pj)3.
So, applying the main theorems of Section 3, we obtain
dL(Xn,ν (2)
n ) = (
√
6 − 2) p3√
2π e3−
√
6 (λn)2
+o
( 1
(λn)2
)
;
dK(Xn,ν (2)
n ) = p3
3
√
2π (λn)
3
2
+o
( 1
(λn)
3
2
)
;
dTV(Xn,ν (2)
n ) = 2(1 + 4e− 3
2 ) p3
3
√
2π (λn)
3
2
+o
( 1
(λn)
3
2
)
.
Thus, (ν(2)
n )n∈N is asymptotically a better approximation scheme than the
simple Poisson approximation (ν(0)
n )n∈N. Moreover, if
+∞∑
j=n+1
(pj)2 =o
(
(λn)− 9
4
)
=o





n∑
j=1
pj


− 9
4


,
then all the results of Theorem 3.16 apply, and in the previous estimates
one can replace ν(2)
n byσ(2)
n , deﬁned by the Fourier transform
ˆσ(2)
n (ξ) = eλn(eiξ −1)
(
1 −
∑ ∞
j=1(pj)2
2 (eiξ − 1)2
)
.
with ﬁxed residue.
TOME 70 (2020), F ASCICULE 3
1154 R. CHHAIBI, F. DELBAEN, P.-L. MÉLIOT & A. NIKEGHBALI
Remark 4.1. — Performing the same computations as in Lemma 3.8, one
can give an exact formula for ν(2)
n ({k}):
ν(2)
n ({k}) = e −λn (λn)k
k!
(
1 +β
(
1 − 2k
λn
+ k(k − 1)
(λn)2
))
,
here with β = − p2,n
2 . At ﬁrst sight this might look like an important
deformation of the Poisson measure with parameter λn, but note that in
the range k =λn(1 +o(1)) where the Poisson law ν(0)
n = P(λn) has its mass
concentrated, one has
1 − 2k
λn
+ k(k − 1)
(λn)2 = 1 − 2(1 +o(1)) + (1 +o(1)) = o(1).
More generally, assume that the remainder of the series ∑ +∞
j=n+1(pj)2 is
asymptotically smaller than any negative power of λn. If
ˆσ(r)
n (ξ) = eλn(eiξ −1)
( r∑
k=0
ek (eiξ − 1)k
)
,
with
ek =
∑
L partition of size k
without part of size 1
(−1)|L|−ℓ(L)
zL
pL ; pk/greaterorequalslant2 =
∞∑
j=1
(pj)k,
then the sequence of signed measures (σ(r)
n )n∈N forms a scheme of approx-
imation of (Xn)n∈N, with
dL(Xn,σ (r)
n ) = |er+1Gr+1(zr+2)|√
2π (λn)
r
2 +1 +o
( 1
(λn)
r
2 +1
)
;
dK(Xn,σ (r)
n ) = |er+1Gr(zr+1)|√
2π (λn)
r+1
2
+o
(
1
(λn)
r+1
2
)
;
dTV(Xn,σ (r)
n ) =
∫
R |er+1Gr+1(α)| dα√
2π (λn)
r+1
2
+o
(
1
(λn)
r+1
2
)
.
Thus, one can in this setting approximate the law of Xn up to any order
(negative power of λn).
4.2. Poisson approximation schemes and formal alphabets
The description of the approximation schemes and of the asymptotic es-
timates for the distances by means of the parameters pk and ek is actually
possible for many other examples of discrete random variables. Thus, the
ANNALES DE L’INSTITUT FOURIER
APPROXIMATION OF DISCRETE MEASURES 1155
combinatorics of approximation schemes can be encoded in the algebra of
symmetric functions Sym. From an algebraic point of view, the language
of λ-rings and formal alphabets make this description even more striking.
Denote Sym the algebra of symmetric functions, that is to say symmet-
ric polynomials in an inﬁnity of variables {x1,x 2,x 3,... }; we refer to [43,
Chapter 1] or [44, Chapter 2] for the whole discussion of this paragraph.
The algebra Sym admits for algebraic basis over C the power sums
pk/greaterorequalslant1 =
∑
i
(xi)k
and the elementary functions
ek/greaterorequalslant1 =
∑
i1<i2<···<ik
xi1xi2 · · ·xik ;
thus, Sym = C[p1, p2,... ] = C[e1, e2,... ]. The two bases are related by the
identity of formal series
1 =
(∏
i
(1 −txi)
)
exp
(∑
i
log 1
1 −txi
)
=
(
1 +
∞∑
k=1
ektk
)
exp
( ∞∑
k=1
pk
k tk
)
,
which leads to the formula
ek =
∑
L∈Pk
(−1)|L|−ℓ(L)
zL
pL
where Pk is the set of integer partitions of size k, and pL =∏ ℓ(L)
i=1 pLi. This
is a particular case of the Frobenius–Schur formula for Schur functions [44,
Theorem 2.32].
A formal alphabet, or specialisation is a morphism of algebras ψ : Sym →
C. In particular, if A = {a1,a 2,... } is a set of complex numbers with∑
i |ai|< +∞, then the map
pk ↦→pk(A) =
∑
i
(ai)k
can be extended to a morphism of algebras Sym → C, hence a specialisation
of Sym (in this case one can speak of a “true” alphabet for A). Beware
that some specialisations are not of this form: indeed, a formal alphabet
can send the power sums pk to an arbitrary set of values in C. Still, we
can agree to use the notation f ↦→f (A) for any specialisation f ↦→ψ(f )
of the algebra Sym. In particular, suppose that A = {a1,a 2,... } is a set of
TOME 70 (2020), F ASCICULE 3
1156 R. CHHAIBI, F. DELBAEN, P.-L. MÉLIOT & A. NIKEGHBALI
complex numbers, but this time with ∑
i |ai| = + ∞ and∑
i |ai|2 < +∞.
We then denote f ↦→f (A) the specialisation
p1(A) = 0 ; pk/greaterorequalslant2(A) =
∑
i
(ai)k.
This deﬁnition extends indeed to a unique morphism of algebras Sym → C,
although there is a priori no underlying “true” alphabet. Given two formal
alphabets A andB, one can deﬁne new formal alphabets ε(A) andA +B,
as follows:
pk(ε(A)) = ( −1)k−1 pk(A) ; pk(A +B) = pk(A) + pk(B).
As before, these deﬁnitions extend uniquely to new morphisms of algebras
Sym → C. If A andB were true alphabets, then A +B is the true alphabet
which is the disjoint union of A and B. On the other hand, ε is related to
a certain involution of the Hopf algebra of symmetric functions.
Let us now relate the theory of symmetric functions to the approximation
schemes of discrete distributions. Consider a sequence of random integer-
valued variables (Xn)n∈N, whose Fourier transforms write as:
E[eiξXn] = eλn(eiξ −1) exp
( ∞∑
k=2
ck,n
k! (eiξ − 1)k
)
.
The coeﬃcients λn =c1,n and ck/greaterorequalslant2,n are called the factorial cumulants of
Xn, and the Poisson random variables are characterized by the vanishing of
their factorial cumulants of order k /greaterorequalslant2 (see [21, Section 5.2]). We associate
to these coeﬃcients the following specialisation of Sym:
p1(An) = 0 ; pk/greaterorequalslant2(An) = (−1)k−1ck,n
(k − 1)! .
Then, the deconvolution residue ψn(ξ) = E[eiξXn] e−λn(eiξ −1) admits the
expansion:
ψn(ξ) =
∞∑
k=0
ek(An) (eiξ − 1)k,
with e0(An) = 1 and e1(An) = 0 . The approximation scheme of order r /greaterorequalslant1
is given by the residue
χ(r)
n (ξ) =
r∑
k=0
ek(An) (eiξ − 1)k.
ANNALES DE L’INSTITUT FOURIER
APPROXIMATION OF DISCRETE MEASURES 1157
The reason why this formalism is convenient is that, for all the examples
that we shall look at in this section, the limiting residue
ψ(ξ) =
∞∑
k=0
ek(A) (eiξ − 1)k,
corresponds to a formal alphabet A which is explicit and which expresses
in terms of “natural” parameters of the random model. These formal al-
phabets are given by Table 4.1.
Table 4.1. Formal alphabets associated to the mod-Poisson convergent
sequences.
Xn formal alphabet A
sum of independent Bernoulli {p1,p 2,p 3... }variables with parameters pj (Section 4.1)
number of cycles of a random N∗−1
uniform permutation (Section 4.3)
number of cycles of a random Ewens Θpermutation with parameter θ (Section 4.3)
number of connected components (2N + 1)−1
of a uniform random map (Section 4.4)
number of distinct irreducible factors N∗−1 + (qdeg I)−1
of a random monic polynomial (Section 4.4)
number of irreducible factors of a N∗−1 +ε((qdeg I − 1)−1)random monic polynomial (Section 4.4)
number of distinct prime divisors N∗−1 + P−1
of a random integer (Section 4.5)
In this table we denote A−1 = { 1
a, a ∈A} if A is a true alphabet, and
Θ =
{
1, θ
θ + 1, θ
θ + 2,...
}
;
qdeg I =
{
qdegP, P ∈ I
}
;
(qdeg I − 1) =
{
qdegP − 1, P ∈ I
}
where I is the set of irreducible polynomials over the ﬁnite ﬁeld Fq. There-
fore, the asymptotic behavior of a sequence (Xn)n∈N in Table 4.1 is entirely
encoded in:
• a sequence of parameters (λn)n∈N,
• and a formal alphabet A which in some sense captures the geometric
and arithmetic properties of the model.
TOME 70 (2020), F ASCICULE 3
1158 R. CHHAIBI, F. DELBAEN, P.-L. MÉLIOT & A. NIKEGHBALI
In particular, the reader should notice the appearance of two contributions
to the formal alphabet as soon as one studies the problem of factorization
of a random element in a factorial ring.
4.3. Number of disjoint cycles of a random permutation
In this section, we study the number ℓn of disjoint cycles of a random
permutationσn ∈ Sn. If the permutation σn is chosen according to the uni-
form probability measure (Example 1.6), then the discussion of Section 4.1
applies, with the parameters pj taken equal to 1
j , and
λn =
n∑
j=1
1
j =Hn ≃ logn;
+∞∑
j=n+1
(pj)2 ≃ 1
n =o
( 1
(λn)r
)
for every r /greaterorequalslant0.
Therefore, if one looks for instance at the derived scheme with constant
residue from the approximation scheme of order r = 2:
ˆσ(2)
n (ξ) = eHn(eiξ −1)
(
1 − π2
12 (eiξ − 1)2
)
then
dL(ℓn,σ (2)
n ) = (
√
6 − 2)ζ(3)√
2π e3−
√
6 (logn)2
+o
( 1
(logn)2
)
,
and one has similar estimates for the Kolmogorov distance and for the total
variation distance.
One can extend this result to more general models of random permuta-
tions, namely, random permutations σn ∈ Sn under the so-called general-
ized weighted measures
PΘ ,n[σn] = 1
n!hn(Θ)
n∏
k=1
(θk)mk(σn),
where Θ = ( θk)k/greaterorequalslant1 is a sequence of non-negative parameters, mk(σ) is the
number of cycles of length k inσ ∈ Sn, andhn(Θ) is the normalization con-
stant so that each PΘ ,n is a probability measure on Sn. If Θ = ( θ,θ,... ) is
a constant sequence, then one recovers the Ewens measures of parameter θ:
Pn[σn] = θℓ(σn)
θ(θ + 1) · · ·(θ +n − 1).
ANNALES DE L’INSTITUT FOURIER
APPROXIMATION OF DISCRETE MEASURES 1159
The generalized weighted measures have been studied previously in [10,
11, 12, 24, 46], and they are related to the quantum Bose gas of statistical
mechanics. Denote as before ℓn = ℓ(σn) = ∑ n
k=1mk(σn) the number of
disjoint cycles of a random permutation under the measure PΘ ,n. We also
introduce the generating series of the parameter Θ :
gΘ (z) =
∞∑
k=1
θk
k zk.
Note that exp(gΘ (z)) =∑ ∞
n=0hn(Θ) zn is the generating series of the par-
tition functions of the models.
If Θ is the constant sequence equal to θ, then gΘ (z) = θ log( 1
1−z ). On the
other hand, in this setting, one can represent ℓn as a sum of independent
Bernoulli variables (Feller coupling):
ℓn =
n∑
j=1
B
( θ
θ +j − 1
)
.
We can then use the discussion of Section 4.1, and the mod-Poisson conver-
gence of (ℓn)n∈N with parameters λn =∑ n
j=1
θ
θ+j−1 ≃θ logn and limiting
residue
ψ(ξ) =
∞∏
j=1
(
1 + θ
θ +j − 1 (eiξ − 1)
)
e− θ
θ +j−1 (eiξ −1) = eγθ(eiξ −1) Γ( θ)
Γ( θeiξ).
The last formula relies on the inﬁnite product representation 1
Γ( z+1) =
eγz ∏ ∞
k=1(1 + z
k ) e− z
k .
More generally, the article [46] shows that if one has a good understand-
ing of the analytic properties of the generating series gΘ (z), then one can
establish the mod-Poisson convergence of (ℓn)n∈N, with a limiting residue
ψ(ξ) similar to the previous expressions. Thus:
Theorem 4.2 ([46, Lemma 4.1]) . — Assume that gΘ (z) is holomorphic
on a domain
∆ 0(r,R,φ ) = {z ∈ C, |z|<R, z ⁄=r, |arg(z −r)|>φ }
with 0<r<R and φ ∈ (0, π
2 ), see Figure 4.1.
Suppose moreover that the singularity of gΘ at z =r is logarithmic:
gΘ (z) = θ log
( 1
1 − z
r
)
+K +O(|z −r|).
Then, one has the asymptotics
EΘ ,n
[
ezℓn
]
= e (θ logn+K)(ez−1)
( Γ( θ)
Γ( θez) +O
( 1
n
))
,
TOME 70 (2020), F ASCICULE 3
1160 R. CHHAIBI, F. DELBAEN, P.-L. MÉLIOT & A. NIKEGHBALI
R
0 r
φ
Figure 4.1. Domain of analyticity of the generating series gΘ (z).
with a uniform remainder on compact subsets of C. Hence, (ℓn)n∈N con-
verges mod-Poisson with parameters λn =θ logn +K and limit
ψ(ξ) = Γ( θ)
Γ( θeiξ).
Moreover, the convergence of residues ψn →ψ happens in every space Cr,
with a norm ‖ψn −ψ‖ C r which is each time O( 1
n ).
Note that the last part of the theorem (convergence in every space Cr)
is an immediate consequence of the estimate of EΘ ,n[ezℓn], and of the ana-
lyticity of all terms in
EΘ ,n[eiξℓn] e−(θ logn+K)(eiξ −1) =ψn(ξ).
On the other hand, in the case of the Ewens measure, one has K = 0 and
r = 1, and in the case of the uniform measure, one has moreover θ = 1.
Because of the inﬁnite product representation of Γ( θ)
Γ( θeiξ ) , one can restate
Theorem 4.2 as follows. If one looks at a generalized weighted measure with
a generating series gΘ (z) that satisﬁes the hypotheses of Theorem 4.2, then
E[eiξℓn]
= e (θ(logn+γ)+K)(eiξ −1)


∞∏
j=1
(
1 + θ(eiξ − 1)
θ +j − 1
)
e− θ (eiξ −1)
θ +j−1 +O
( 1
n
) 
.
Therefore, in this setting, one can deal with the asymptotics of (ℓn)n∈N in
the same way as in Section 4.1, but with parameters λn =θHn +K, and
(Θ ) p1(Θ) = 0 ; pk/greaterorequalslant2(Θ) =
∞∑
j=1
( θ
θ +j − 1
) k
.
ANNALES DE L’INSTITUT FOURIER
APPROXIMATION OF DISCRETE MEASURES 1161
Thus, one has the following:
Theorem 4.3. — We consider a generalized weighted measure PΘ ,n,
with a generating series gΘ (z) which satisﬁes the hypotheses of Theo-
rem 4.2. For anyr /greaterorequalslant1, we introduce the scheme of approximation (σ(r)
n )n∈N,
deﬁned by the Fourier transforms
ˆσ(r)
n (ξ) = e (θHn+K)(eiξ −1)
( r∑
k=0
ek(Θ) (e iξ − 1)k
)
,
where Θ is the specialisation of Sym speciﬁed by Equation (Θ ). Note that
the residue is equal to 1 for r = 1 (basic scheme of approximation). One
has the asymptotics:
dL(ℓn,σ (r)
n ) = |er+1(Θ) Gr+1(zr+2)|√
2π (θ logn)
r
2 +1 +o
( 1
(logn)
r
2 +1
)
;
dK(ℓn,σ (r)
n ) = |er+1(Θ) Gr(zr+1)|√
2π (θ logn)
r+1
2
+o
(
1
(logn)
r+1
2
)
;
dTV(ℓn,σ (r)
n ) =
∫
R |er+1(Θ) Gr+1(α)| dα√
2π (θ logn)
r+1
2
+o
(
1
(logn)
r+1
2
)
.
4.4. Mod-Poisson convergence and algebraico-logarithmic
singularities
The discussion of Section 4.3 can be extended to any statistic of a random
combinatorial object, whose double generating series admits a certain form
of singularity. Suppose given a combinatorial class, that is to say a sequence
C = (Cn)n∈N of ﬁnite sets. We write card Cn = |Cn|. In this paragraph, we
shall in particular study the following two examples, cf. [32, Section 5,
Example 2] and [30, p. 449 and p. 671]:
(1) Fn = F([ [1,n ] ], [ [1,n ] ])is the set of maps from the ﬁnite set [ [1,n ] ]to
itself. It has cardinality nn.
(2) Pn = ( Fq[t])n is the set of monic polynomials of degree n with
coeﬃcients in the ﬁnite ﬁeld Fq, where q =pe is some prime power.
It has cardinality qn.
This is mainly to ﬁx the ideas, and the techniques hereafter can be applied
to many other examples from the aforementioned sources. We consider
a statistic X :⨆
n∈N Cn → N, and we denote by Xn the random variable
TOME 70 (2020), F ASCICULE 3
1162 R. CHHAIBI, F. DELBAEN, P.-L. MÉLIOT & A. NIKEGHBALI
obtained by evaluatingX on an element of Cn chosen uniformly at random.
We introduce the bivariate generating function
F (z,w ) =
∞∑
n=0
zn
n!
∑
c∈Cn
wX(c) =
∞∑
n=0
zn (card Cn)
n! E[wXn]
or F (z,w ) =
∞∑
n=0
zn ∑
c∈Cn
wX(c) =
∞∑
n=0
zn (card Cn) E[wXn].
Suppose that for any w,F (z,w ) is a complex analytic function on a domain
∆ 0(r(w),R (w),φ ), and admits an algebraico-logarithmic singularity atz =
r(w), that writes as
F (z,w ) = K(w)
(
1
1 − z
r(w)
) α(w)(
log 1
1 − z
r(w)
) β(w)
(1 +o(1)).
Then, the coeﬃcient cn(w) of zn in F (z,w ) has for asymptotics:
cn(w) = K(w)
Γ( α(w)) (r(w))−nnα(w)−1(logn)β(w)
(
1 +O
( 1
logn
))
,
see [29]. Moreover, the O( 1
logn ) is actually a O( 1
n ) ifβ(w) = 0 , or if α(w) =
0 and β(w) = 1 ; cf. [33]. If w stays in a suﬃciently small compact subset
of C, then one can take a uniform constant in the O( · ), which leads to an
asymptotic formula for the expectations E[wXn]:
E[wXn] = cn(w)
cn(1)
= K(w)
K(1)
Γ( α(1))
Γ( α(w))
(r(1)
r(w)
) n
nα(w)−α(1) (logn)β(w)−β(1)
(
1 +O
( 1
logn
))
,
again with a smaller remainder O( 1
n ) if β(w) = 0 for all w. In this para-
graph, we shall concentrate on this particular case; the case β(w) ⁄= 0
is more commonly observed in probabilistic number theory, see our next
paragraph 4.5.
Example 4.4. — If f ∈ Fn = F([ [1,n ] ], [ [1,n ] ]), the functional graph cor-
responding to f is the directed graph G(f ) with vertex set [ [1,n ] ], and with
edges (k,f (k)), k ∈ [ [1,n ] ]. Since f is a map, G(f ) is a disjoint union of
cycles on which trees are grafted, see [28] and Figure 4.2. We denote X(f )
the number of connected components of the functional graph G(f ). This
generalizes the notion of cycle of a permutation. If T = (Tn)n∈N is the com-
binatorial class of unordered rooted labeled trees, recall that its generating
function T (z) = ∑ ∞
n=1
zn
n! |Tn| is the solution of T (z) = zeT (z), because a
ANNALES DE L’INSTITUT FOURIER
APPROXIMATION OF DISCRETE MEASURES 1163
rooted tree is constructed recursively by taking a node and connecting to
it a set of trees (also, Cayley’s theorem gives card Tn =nn−1).
1
3 4
7
5
8 6
2
Figure 4.2. The functional graph associated to the function f :
[ [1, 8] ]→ [ [1, 8] ]with word 38471814, here with one connected compo-
nent.
The class C = (Cn)n∈N of cycles on such trees has generating series
C(z) =
∞∑
n=0
zn
n! |Cn|
=
∞∑
n=0
∑
k1+···+kr=n
|Tk1| |Tk2| · · · |Tkr |
rn !
( n
k1,...,k r
)
zn
=
∞∑
r=1
1
r
∑
k1,...,k r/greaterorequalslant1
|Tk1| · · · |Tkr |
(k1)! · · ·(kr)! zk1+···+kr
=
∞∑
r=1
(T (z))r
r = log
( 1
1 −T (z)
)
.
On the second line of this computation, the multinomial coeﬃcient comes
from the choice of the distribution of the integers of [ [1,n ] ]into the r dif-
ferent trees, and the factor 1
r comes from the fact that r distinct cyclic
permutations of the choices yield the same cycle of trees. Finally, a func-
tional graph is a set of cycles of trees, so,
F (z) =
∞∑
n=0
zn
n! |Fn| = exp(C(z)) = 1
1 −T (z).
TOME 70 (2020), F ASCICULE 3
1164 R. CHHAIBI, F. DELBAEN, P.-L. MÉLIOT & A. NIKEGHBALI
Moreover, counting connected components of functional graphs amounts to
count a factor w for each cycle, hence,
F (z,w ) =
∞∑
n=0
zn
n!
∑
f ∈Fn
wX(f ) = exp(wC(z)) =
( 1
1 −T (z)
) w
.
The generating series of rooted trees is classically known to have radius
of convergence 1
e , and a square-root type singularity at z = 1
e , see [28,
Formula (11)]:
T (z) = 1 −
√
2(1 − ez) +O(1 − ez).
Therefore,
F (z,w ) = 2 − w
2
( 1
1 − ez
) w
2
(1 +o(1)),
and the previous discussion applies with K(w) = 2 − w
2 , α(w) = w
2 and
β(w) = 0 . Consequently,
E[wXn] = e
1
2 log n
2 (w−1) Γ( 1
2 )
Γ( w
2 )
(
1 +O
( 1
n
))
,
with a remainder that is uniform if w remains on the unit circle. We shall
next interpret this result as a mod-Poisson convergence, and deduce from
it the construction of approximation schemes.
Example 4.5. — IfP ∈ Pn = (Fq[t])n, then it writes uniquely as a prod-
uct of monic irreducible polynomials, each of these monic irreducible poly-
nomials appearing with a certain multiplicity. In terms of generating series,
introducing the combinatorial class I = (In)n∈N of monic irreducibles, this
can be rewritten as:
P (z) =
∑
P ∈P
zdegP =
∏
P ∈I
(1 +zdegP +z2 degP + · · ·) =
∏
P ∈I
1
1 −zdegP
= exp
(∑
P ∈I
log
( 1
1 −zdegP
) )
= exp
( ∞∑
k=1
∑
P ∈I
zk degP
k
)
= exp
( ∞∑
k=1
I(zk)
k
)
,
where P (z) = ∑
n/greaterorequalslant0 |Pn|zn and I(z) = ∑
n/greaterorequalslant1 |In|zn. Similarly, if Y (P )
and Z(P ) are respectively the number of distinct irreducible factors and
ANNALES DE L’INSTITUT FOURIER
APPROXIMATION OF DISCRETE MEASURES 1165
the number of irreducible factors counted with multiplicity for P , then
PY (z,w ) =
∑
P ∈P
wY (P )zdegP =
∏
P ∈I
1 + (w − 1)zdegP
1 −zdegP
= exp
( ∞∑
k=1
∑
P ∈I
zk degP
k − ((1 −w)zdegP )k
k
)
= exp
( ∞∑
k=1
I(zk) (1 − (1 −w)k)
k
)
and
PZ(z,w ) =
∑
P ∈P
wZ(P )zdegP =
∏
P ∈I
1
1 −wz degP
= exp
( ∞∑
k=1
∑
P ∈I
wkzk degP
k
)
= exp
( ∞∑
k=1
wkI(zk)
k
)
.
Note that P (z) is simply equal to ∑ ∞
n=0qnzn = 1
1−qz . On the other hand,
the number |In| of irreducible monic polynomials of degree n is given by
Gauss’ formula
|In| = 1
n
∑
d|n
µ
(n
d
)
qd,
as can be seen by gathering the elements of Fqn according to their irre-
ducible polynomials over Fq (here, µ is the arithmetic Möbius function).
Consequently,
I(z) =
∑
n/greaterorequalslant1
|In|zn =
∑
k/greaterorequalslant1
∑
d/greaterorequalslant1
µ(k)qdzdk
dk =
∑
k/greaterorequalslant1
µ(k)
k log
( 1
1 −qzk
)
.
We split I(z) into two parts: the ﬁrst term k = 1 and the remainder
R(z) =
∑
k/greaterorequalslant2
µ(k)
k log
( 1
1 −qzk
)
.
The remainder R(z) is an analytic function in z on the open disk of radius
q−1/2, whereas the ﬁrst term log 1
1−qz is analytic on the smaller open disk
TOME 70 (2020), F ASCICULE 3
1166 R. CHHAIBI, F. DELBAEN, P.-L. MÉLIOT & A. NIKEGHBALI
of radius q−1. It follows that
PY (z,w ) =
( 1
1 −qz
) w
exp

wR(q−1) +
∑
k/greaterorequalslant2
I(q−k) (1 − (1 −w)k)
k +o(1)


PZ(z,w ) =
( 1
1 −qz
) w
exp

wR(q−1) +
∑
k/greaterorequalslant2
I(q−k)wk
k +o(1)


in the neighborhood of the singularity z =q−1. These algebraic singularities
with exponents α(w) = w and β(w) = 0 lead to the asymptotic formulas
E[wYn] = e(logn+R(q−1))(w−1)
Γ( w) exp

∑
k/greaterorequalslant2
(−1)k−1I(q−k)
k (w − 1)k +O
( 1
n
) 

E[wZn] = e(logn+R(q−1))(w−1)
Γ( w) exp

∑
k/greaterorequalslant2
I(q−k)
k (wk − 1) +O
( 1
n
) 
.
Thus, if a statistic X of a random combinatorial object has a double
generating series that admits an algebraico-logarithmic singularity, then
in many cases one can deduce from it the mod-Poisson convergence of
(Xn)n∈N. We restate hereafter the previous computations in this frame-
work. We note ϕ(D) the Euler function (number of integers in [ [1,D ] ]that
are coprime withD), which satisﬁes the identityϕ(D) =∑
m|Dµ(m) D
m ; and
S(z) =
∑
k/greaterorequalslant2
ϕ(k)
k log
( 1
1 −qzk
)
,
which is analytic on the open disk of radius q−1/2.
Theorem 4.6. — Let Xn be the number of components of a random
map in F([ [1,n ] ], [ [1,n ] ]), and Yn and Zn be the numbers of irreducible
factors of a random monic polynomial in (Fq[t])n∈N, counted respectively
without and with multiplicity. The sequences of random variables (Xn)n∈N,
(Yn)n∈N and (Zn)n∈N converge mod-Poisson with parameters
λX
n = 1
2 (log 2n +γ) ;
λY
n = logn +R(q−1) +γ;
λZ
n = logn +S(q−1) +γ.
ANNALES DE L’INSTITUT FOURIER
APPROXIMATION OF DISCRETE MEASURES 1167
and limiting functions ψX/Y/Z (ξ) = ∑ ∞
k=0 ek(X/Y/Z ) (eiξ − 1)k, where the
parameters ek(X), ek(Y ) and ek(Z) correspond to the specialisations of Sym:
pk/greaterorequalslant2(X) =
∑
n/greaterorequalslant1
1
(2n − 1)k ; p1(X) = 0 ;
pk/greaterorequalslant2(Y ) = ζ(k) +I(q−k) ; p1(Y ) = 0 ;
pk/greaterorequalslant2(Z) = ζ(k) + (−1)k−1 ∑
n/greaterorequalslant1
|In|
(qn − 1)k ; p1(Z) = 0.
Moreover, in each case, one has ψn(ξ) −ψ(ξ) = O( 1
n ) uniformly on the
cycle.
Proof. — Each time we set w = e iξ in the previous calculations, and we
also rewrite the residue so that it does not involve a power of w − 1 equal
to 1.
(1) Number of connected components of a random map. One can write
the inﬁnite products
Γ( 1
2 )
Γ( w
2 ) = e
γ
2 (w−1)
∞∏
n=1
1 +
w
2 −1
n
1 − 1
2n
e− w−1
2n
= e
γ
2 (w−1)
∞∏
n=1
(
1 + w − 1
2n − 1
)
e− w−1
2n
= e ( γ
2 +log 2) (w−1)
∞∏
n=1
(
1 + w − 1
2n − 1
)
e− w−1
2n−1
by using the identity ∑ ∞
n=1
1
2n−1 − 1
2n = log 2 . In the last inﬁnite
product, one recognizes the same form as in Section 4.1, with pa-
rameters pj = 1
2j−1 .
(2) Number of distinct irreducible factors of a random monic polyno-
mial. One rewrites the asymptotic formula for E[wYn]:
e(logn+R(q−1)+γ)(w−1)
( ∞∏
n=1
(
1 + w − 1
n
)
e− w−1
n
)
×

∏
k/greaterorequalslant2
(−1)k−1I(q−k)
k (w − 1)k


= e (logn+R(q−1)+γ)(w−1)

∏
k/greaterorequalslant2
(−1)k−1 (w − 1)k
k
( ∞∑
n=1
1
nk +I(q−k)
) 
.
TOME 70 (2020), F ASCICULE 3
1168 R. CHHAIBI, F. DELBAEN, P.-L. MÉLIOT & A. NIKEGHBALI
Again we recognize the formula
exp
( ∞∑
k=1
(−1)k−1(w − 1)k
k pk
)
=
∞∑
k=0
ek (w − 1)k.
(3) Number of irreducible factors of a random monic polynomial, count-
ed with multiplicity. The factor Γ( w)−1 is dealt with exactly as in
the previous case. Therefore, we only have to deal with the term
exp(∑
k/greaterorequalslant2
I(q−k)
k (wk − 1)). However,
∑
k/greaterorequalslant2
I(q−k)
k (wk − 1)
=
∑
k/greaterorequalslant2
k∑
l=1
I(q−k)
k
(k
l
)
(w − 1)l
=

∑
k/greaterorequalslant2
I(q−k)

 (w − 1) +
∞∑
l=2

∑
k/greaterorequalslantl
(k
l
) I(q−k)
k

 (w − 1)l.
The coeﬃcient of (w − 1) can be rewritten as follows:
∑
k/greaterorequalslant2
I(q−k) =
∑
k/greaterorequalslant2
m/greaterorequalslant1
µ(m)
m log
( 1
1 −q1−km
)
=
∑
D=km/greaterorequalslant2
log
( 1
1 −q1−D
) ∑
m|D
m⁄=D
µ(m)
m
=
∑
D/greaterorequalslant2
ϕ(D) −µ(D)
D log
( 1
1 −q1−D
)
=S(q−1) −R(q−1).
On the other hand, if l /greaterorequalslant2, then the coeﬃcient of (w − 1)l rewrites
as
∑
k/greaterorequalslantl
(k
l
) I(q−k)
k = 1
l
∑
k/greaterorequalslantl
∑
m/greaterorequalslant1
µ(m)
m
(k − 1
l − 1
)
log
( 1
1 −q1−km
)
= 1
l
∑
m,n/greaterorequalslant1
µ(m)
nm qn∑
k/greaterorequalslantl
(k − 1
l − 1
)
q−k(mn)
= 1
l
∑
D/greaterorequalslant1
|ID|
(qD − 1)l
ANNALES DE L’INSTITUT FOURIER
APPROXIMATION OF DISCRETE MEASURES 1169
by setting D = nm on the last line. We conclude that the Fourier
transform E[wZn] has asymptotics
e(logn+S(q−1)+γ)(w−1)
× exp


∞∑
l=2

(−1)l−1ζ(l) +
∑
D/greaterorequalslant1
|ID|
(qD − 1)l

 (w − 1)l
l

,
and the term of degree 1 in (w − 1) is separated from the other
terms. □
From Theorem 4.6, one can easily construct approximation schemes of
the sequences (Xn)n∈N, (Yn)n∈N and (Zn)n∈N, which yield distances that
are arbitrary large negative powers of logn. For instance, suppose that
one wants to approximate the law of Yn by a signed measure νn, such
that dTV(µn,νn) = O( 1
(logn)2 ). By Theorem 3.11, we can take the derived
scheme of the approximation scheme of order r = 3 , that is to say the
sequence of measures (σn)n∈N with Fourier transforms
ˆσn(ξ) = e (logn+R(q−1)+γ)(eiξ −1)
×
(
1 − ζ(2) +I(q−2)
2 (eiξ − 1)2 + ζ(3) +I(q−3)
3 (eiξ − 1)3
)
.
One has in this situation
dTV(Xn,σn)
≃ 1
(logn)2
((ζ(2) +I(q−2))2
8 + ζ(4) +I(q−4)
4
)( ∫
R
|G4(α)| dα√
2π
)
.
Remark 4.7. — A central limit theorem for the random variables Yn has
been proved by Rhoades in [51]. Our results immediately yield the speed
of convergence of this analogue on function ﬁelds of the Erdős–Kac central
limit theorem.
4.5. Number of distinct prime divisors of a random integer
As pointed out in the introduction, number theory provides another area
where the phenomenon of mod-Poisson convergence is prominent; see in
particular the discussion of [26, Section 7.2]. Consider as in Example 1.7
the number ω(Nn) of distinct prime divisors of a random integer chosen
TOME 70 (2020), F ASCICULE 3
1170 R. CHHAIBI, F. DELBAEN, P.-L. MÉLIOT & A. NIKEGHBALI
uniformly in [ [1,n ] ]. This quantity satisﬁes the celebrated Erdős–Kac central
limit theorem:
ω(Nn) − log logn√log logn ⇀ NR(0, 1),
where NR(0, 1) denotes a standard one-dimensional Gaussian distribution
of mean 0 and variance 1 (cf. [25]). This Gaussian approximation actually
comes from a more precise Poissonian approximation, which can be stated
in the framework of mod-Poisson convergence:
Theorem 4.8 (Rényi–Turán). — Locally uniformly in z ∈ C,
E[ezω(Nn)] = e (log logn+γ)(ez−1)
×

∏
n∈N
(
1 + ez − 1
n
)
e− ez −1
n
∏
p∈P
(
1 + ez − 1
p
)
e− ez −1
p +O
( 1
logn
) 
.
This formula ﬁrst appeared in [50], and it can be obtained by an appli-
cation of the Selberg–Delange method, see [57, Chapter II.5]. It is actually
stronger than the prime number theorem, as it requires a larger zero-free re-
gion of the Riemann zeta function than the line Re(s) = 1 . The problem of
the rate of convergence in the Erdős–Kac central limit theorem was already
studied by Harper in [31] for the Kolmogorov distance to the Gaussian ap-
proximation; and by Barbour, Kowalski and Nikeghbali in [7] for the three
distances to the Poissonian (or signed measure) approximation.
Note that the residue
ψ(ξ) =
∏
n∈N∗
(
1 + eiξ − 1
n
)
e− eiξ −1
n
∏
p∈P
(
1 + eiξ − 1
p
)
e− eiξ −1
p
can be rewritten as
exp

∑
k/greaterorequalslant2
(−1)k−1 pk(N∗−1 + P−1)
k (eiξ − 1)k

,
where pk(N∗−1 + P−1) =∑ ∞
n=1
1
nk +∑
p∈P
1
pk . Therefore:
Theorem 4.9. — For any r /greaterorequalslant1, we introduce the scheme of approxi-
mation (σ(r)
n )n∈N, deﬁned by the Fourier transforms
ˆσ(r)
n (ξ) = e (log logn+γ)(eiξ −1)
( r∑
k=0
ek(N∗−1 + P−1) (eiξ − 1)k
)
,
ANNALES DE L’INSTITUT FOURIER
APPROXIMATION OF DISCRETE MEASURES 1171
where the parameters ek(N∗−1 + P−1) correspond to the specialisation of
Sym:
p1(N∗−1 + P−1) = 0 ; pk/greaterorequalslant2(N∗−1 + P−1) = ζ(k) +
∑
p∈P
1
pk.
With log2n := log logn, one has the asymptotic formulas:
dL(ω(Nn),σ (r)
n ) = |er+1(N∗−1 + P−1)Gr+1(zr+2)|√
2π (log2n)
r
2 +1 +o
( 1
(log2n)
r
2 +1
)
;
dK(ω(Nn),σ (r)
n ) = |er+1(N∗−1 + P−1)Gr(zr+1)|√
2π (log2n)
r+1
2
+o
(
1
(log2n)
r+1
2
)
;
dTV(ω(Nn),σ (r)
n ) =
∫
R |er+1(N∗−1 +P−1)Gr+1(α)| dα√
2π (log2n)
r+1
2
+o
(
1
(log2n)
r+1
2
)
.
This theorem allows one to quantify how much better the Poisson ap-
proximation is in comparison to the Gaussian approximation (Erdős–Kac
theorem). Indeed, since the case r = 1 of Theorem 4.9 is the basic scheme
of approximation of ω(Nn) by a Poisson random variable Yn of parameter
λn = log 2n +γ, one has:
dK
(
ω(Nn) − log2n −γ
√
log2n +γ , P(log2n+γ) − log2n −γ√
log2n +γ
)
=dK(ω(Nn), P(log2n+γ)) = O
( 1
log2n
)
.
On the other hand, the classical Berry–Esseen estimate for sums of identi-
cally distributed random variables ensures that
dK
(
P(log2n+γ) − log2n −γ
√
log2n +γ , NR(0, 1)
)
=O
(
1√
log2n
)
.
Thus, in terms of Kolmogorov distance, the Poisson approximation of the
sequence (ω(Nn))n∈N is at distance O( 1
log2n ), whereas the Gaussian ap-
proximation is at distance O( 1√
log2n ). Similar remarks can be made for
the statistics of random combinatorial objects previously studied.
5. The multi-dimensional case
In this last section, we extend the theoretical results of Sections 2 and 3 to
the multi-dimensional case, that is to say that we are going to approximate
TOME 70 (2020), F ASCICULE 3
1172 R. CHHAIBI, F. DELBAEN, P.-L. MÉLIOT & A. NIKEGHBALI
the laws of random variables with values in Zd/greaterorequalslant2. Thus, we consider a
sequence of random variables (Xn)n∈N in Zd that converges mod- φ with
parametersλn, where φ is an inﬁnitely divisible distribution with minimal
lattice Zd:
µn(ξ) = E
[
ei
∑ d
i=1ξiXn,i
]
= eλnφ(ξ)ψn(ξ1,...,ξ d),
with limn→∞ψn =ψ uniformly on the torus. In all the examples that we
shall look at, the law with exponent φ enjoys the factorization property:
φ(ξ) = φ(ξ1,...,ξ d) =
d∑
i=1
φi(ξi),
where the φj’s are inﬁnitely divisible laws on Z. In other words, if Y is a
reference random variable with law on Zd with Lévy–Khintchine exponent
φ, then its coordinates are independent random variables on the lattice
Z. This assumption will also simplify a bit our calculations; more general
distributionsφ could be treated with the same techniques but more cumber-
some computations. Note that the factorization property for the reference
distribution φ does not mean at all that the Xn’s will have independent
coordinates. Hence, though we shall see independence of coordinates by
looking at the ﬁrst order asymptotics of Xn (captured by the inﬁnitely
divisible law φ), the higher order asymptotics will shed light on the non-
independence of the coordinates (this being captured by the limiting residue
ψ(ξ), which does not factorize in general).
As in Section 3, we consider a general approximation scheme (νn)n∈N of
(Xn)n∈N with Fourier transforms
ˆνn(ξ) = eλnφ(ξ)χn(ξ1,...,ξ d),
and limn→∞χn =χ. The goal will be to compute the asymptotics of
dL(µn,νn) = sup
k∈Zd
|µn({k}) −νn({k})|;
dTV(µn,νn) =
∑
k∈Zd
|µn({k}) −νn({k})|.
Note that in dimension d /greaterorequalslant2, there is no interesting analogue of the
Kolmogorov distance for discrete measures. In Section 5.1, we study the
multi-dimensional Wiener algebra A (Td), and we establish an estimate of
norms that is similar to our Theorem 2.3 (see Theorem 5.3). In Section 5.2,
we deduce from this theorem the multi-dimensional analogue of the results
of Section 3. Finally, in Section 5.3 and Section 5.4, we study two examples
which generalize the ones of Section 4, and stem respectively from the
ANNALES DE L’INSTITUT FOURIER
APPROXIMATION OF DISCRETE MEASURES 1173
combinatorics of coloured permutations, and from arithmetic progressions
in number theory.
Let us ﬁx some standard notation relative to the multi-dimensional set-
ting. The coordinates of a parameter ξ ∈ Td = ( R/2πZ)d (respectively,
k ∈ Zd) will be denoted (ξ1,...,ξ d) (resp., (k1,...,k d)). If α ∈ Nd is a
multi-index, we denote |α| =∑ d
i=1αi and
∂αf = ∂|α|f (ξ1,...,ξ d)
∂ξα1
1 · · ·∂ξαd
d
.
In the same setting, if n = |α|, then the multinomial coeﬃcient
(n
α
)
is
n!
(α1)!···(αd)! . On the other hand, if α and β are two d-tuples, we write
⟨α |β⟩ =
d∑
i=1
αiβi.
We also write α ⩽ β if αi ⩽ βi for all i ∈ [ [1,d ] ].
5.1. The multi-dimensional Wiener algebra
Definition 5.1. — The multi-dimensional Wiener algebra A = A (Td)
is the algebra of continuous functions on the d-torus whose Fourier series
converges absolutely. It is a Banach algebra for the norm
‖f ‖ A :=
∑
n∈Zd
|cn(f )|,
where cn(f ) denotes the Fourier coeﬃcient
cn(f ) =
∫ 2π
θ1=0
· · ·
∫ 2π
θd=0
f (eiθ1,..., eiθd) e−i
∑ d
i=1niθi dθ
(2π)d,
where n = (n1,...,n d).
As in the case d = 1 , if µ is a (signed) measure on Zd, then its total
variation norm is equal to ‖µ‖ TV = ‖ˆµ‖ A . On the other hand, one has the
analogue of Proposition 2.1:
Proposition 5.2. — There is a constant CH,d such that, for any f ∈
A (Td),
‖f ‖ A ⩽ CH,d sup
|α|⩽ Kd
‖∂αf ‖ L 2,
TOME 70 (2020), F ASCICULE 3
1174 R. CHHAIBI, F. DELBAEN, P.-L. MÉLIOT & A. NIKEGHBALI
where K = Kd = ⌊d
2 ⌋ + 1 , and L 2 = L 2(Td) is the space of square-
integrable functions on the torus, endowed with the norm
‖f ‖ L 2 =
√ ∫ 2π
θ1=0
· · ·
∫ 2π
θd=0
|f (eiθ1,..., eiθd)|2 dθ
(2π)d.
Proof. — Note that Kd /greaterorequalslantd+1
2 for any d /greaterorequalslant1. We use again the Cauchy–
Schwarz inequality and the Parseval identity:
‖f ‖ A =
∑
n∈Zd
|cn(f )| =
∑
n∈Zd
(
1 +∑ d
i=1(ni)2
1 +∑ d
i=1(ni)2
) Kd
2
|cn(f )|
⩽
/radicaltp
/radicalvertex
/radicalvertex
√
∑
n∈Zd
(
1
1 +∑ d
i=1(ni)2
) Kd
/radicaltp
/radicalvertex
/radicalvertex
/radicalvertex
√
∑
n∈Zd
(
1 +
d∑
i=1
(ni)2
) Kd
|cn(f )|2
⩽
/radicaltp
/radicalvertex
/radicalvertex
/radicalvertex
√
∑
n∈Zd
(
1
1 +∑ d
i=1(ni)2
) d+1
2
×
/radicaltp
/radicalvertex
/radicalvertex
√
∑
α0+···+αd=Kd
( Kd
α0,...,α d
) ∑
n∈Zd
|cn(∂(α1,...,α d)f )|2
⩽
/radicaltp
/radicalvertex
/radicalvertex
/radicalvertex
√
(d + 1)Kd
∑
n∈Zd
(
1
1 +∑ d
i=1(ni)2
) d+1
2
sup
|α|⩽ Kd
‖∂αf ‖ L 2,
hence the result since the series (CH,d)2 under the square root sign is
ﬁnite. □
This inequality leads to the analogue of Theorem 2.3 in a multi-dimensio-
nal setting. We consider two measures µ and ν on Zd with Fourier trans-
forms
ˆµ(ξ) = eλφ(ξ)ψ(ξ);
ˆν(ξ) = eλφ(ξ)χ(ξ)
where φ(ξ) = ∑ d
i=1φi(ξi). We assume φ to have moments at least up to
order Kd, and denote
φi(ξi) = imiξi − σ2
i ξ2
i
2 +o(ξ2
i )
the Taylor expansion around 0 of each law on Z with Lévy exponent φi.
We ﬁx an integer r /greaterorequalslant⌊d
2 ⌋ such that
ANNALES DE L’INSTITUT FOURIER
APPROXIMATION OF DISCRETE MEASURES 1175
(1) the residues ψ and χ are (r + 1) times continuously diﬀerentiable
on Td;
(2) their Taylor expansions at 0 coincide up to order r:
∀ |α| ⩽ r, (∂α(ψ −χ)) (0) = 0.
A parameter ε ∈ (0, 1) being ﬁxed, we also introduce the non-negative
quantities
βr+1(ε) = sup
|α|=r+1
sup
ξ∈[−ε,ε]d
|∂α(ψ −χ)(ε)|;
γ(ε) = sup
i∈[ [1,d] ]
sup
θ∈[−ε,ε]
|φ′′
i (θ) +σ2
i |;
M = − sup
i∈[ [1,d] ]
sup
θ∈[−π,π]
(Re(φi(θ))
θ2
)
.
The quantityβr+1(ε) allows one to bound any derivative up to order (r +1)
ofψ −χ on [−ε,ε ]d. Indeed, this is obvious for exponents α with |α| =r +1,
and otherwise,
|∂α(ψ −χ)(ξ)| =
⏐
⏐
⏐
⏐
∫ 1
t=0
d
dt (∂α(ψ −χ)(tξ)) dt
⏐
⏐
⏐
⏐
⩽
d∑
i=1
|ξi|
⏐
⏐
⏐
⏐
∫ 1
t=0
∂
∂αi
(∂α(ψ −χ)(tξ)) dt
⏐
⏐
⏐
⏐,
which leads by descending induction on |α| to the bound
|∂α(ψ −χ)(ξ)| ⩽
( d∑
i=1
|ξi|
) r+1−|α|
βr+1(ε) ⩽ (dε)r+1−|α|βr+1(ε)
for any ξ ∈ [−ε,ε ]d.
Theorem 5.3. — Fix ε ∈ (0, 1) such that γ(ε) ⩽ mini∈[ [1,d] ]
σ2
i
2 . There
exist some positive constants C1(d,c,φ ) and C2(d,c,φ ), that depend only
on d, the cut function c and the reference distribution φ, such that
‖ˆµ −ˆν‖ A ⩽ C1(d,c,φ )
(
1 + C2(d,c,φ )√
λ
)
×
(
‖ψ −χ‖ A
λK e− λM ε 2
4
ε + εr+1βr+1(ε)
λ
d
4
(√
λ + 1
ε
) K)
for any ε ∈ (0, 1) and any λ> 0.
TOME 70 (2020), F ASCICULE 3
1176 R. CHHAIBI, F. DELBAEN, P.-L. MÉLIOT & A. NIKEGHBALI
Since Proposition 5.2 involves higher order derivatives than Proposi-
tion 2.1, in order to prove Theorem 5.3, we shall use a smoother cut-
function than in the proof of Theorem 2.3. Thus, in the following, cd,ε(ξ) =∏ d
i=1c(ξi
ε ), wherec(x) is a function of one variable with values in [0, 1], that
is of class CKd on R, with c(x) = 0 outside [−1, 1] andc(x) = 1 on [− 1
2, 1
2 ].
In particular,cd,ε (respectively, 1−cd,ε) vanishes on [−π,π ]d\ [−ε,ε ]d (resp.,
on [−ε
2, ε
2 ]d).
Lemma 5.4. — Under the assumptions of Theorem 5.3, there exists a
constantC(d,c,φ ) such that
‖
‖ (1 −cd,ε) eλφ‖
‖
A ⩽ C(d,c,φ )λK
ε e− λM ε 2
4
(
1 +O
(1
λ
))
,
where the constant hidden in the O( · ) also depends only on d, c and φ.
Proof. — We combine Proposition 5.2 with the rules of diﬀerentiation of
functions of several variables:
‖
‖ (1 −cd,ε) eλφ‖
‖
A
CH,d
⩽ sup
|α|⩽ Kd
‖∂α((1 −cd,ε) eλφ)‖ L 2([−π,π]d\ [− ε
2, ε
2 ]d)
⩽ sup
|α|⩽ Kd
∑
β⩽ α
d∏
i=1
(αi
βi
)
‖∂α−β(1 −cd,ε)‖ L 2 ‖∂β(eλφ)‖ L ∞([−π,π]d\ [− ε
2, ε
2 ]d)
⩽ 2Kd
(
sup
|γ|⩽ Kd
‖∂γ(1 −cd,ε)‖ L 2
)(
sup
|β|⩽ Kd
‖∂β(eλφ)‖ L ∞([−π,π]d\ [− ε
2, ε
2 ]d)
)
.
Since the Lévy–Khintchine exponent φ is assumed to have the factorization
property, for any multi-index β,
∂β(eλφ) =
d∏
i=1
∂βieλφi(ξi)
∂ξβi
i
,
and
∂neλφi(θ)
∂θn = e λφi(θ)
n∑
k=1
Bn,k(λφ′
i(θ),λφ ′′
i (θ),...,λφ (n−k+1)
i (θ)),
ANNALES DE L’INSTITUT FOURIER
APPROXIMATION OF DISCRETE MEASURES 1177
where Bn,k(x1,...,x n+k−1) is the incomplete Bell polynomial of parame-
ters n and k, see [9]. More precisely,
Bn,k(x1,...,x n+k−1)
=
∑
m1+m2+···+mn−k+1=k
m1+2m2+···+(n−k+1)mn−k+1=n
n!
∏ n−k+1
i=1 (i!mimi!)
(x1)m1 · · ·(xn−k+1)mn−k+1
and
|Bn,k(x1,...,x n+k−1)| ⩽
(
sup
i∈[ [1,n+k−1] ]
|xi|
) k
S(n,k )
whereS(n,k ) = Bn,k(1, 1,..., 1) is the Stirling number of the second kind.
As a consequence,
⏐
⏐
⏐
⏐
∂neλφi(θ)
∂θn
⏐
⏐
⏐
⏐ ⩽ |eλφi(θ)|Tn(λ‖φi‖ C n(T)) ⩽ |eλφi(θ)|Tn(λ‖φ‖ C n(Td)),
where Tn(x) = ∑ n
k=1S(n,k )xk is the n-th Touchard polynomial, with
leading term S(n,n )xn =xn. Thus,
|∂βeλφ| ⩽ |eλφ|
d∏
i=1
⏐
⏐Tβi(λ‖φ‖ C β i (Td))
⏐
⏐
⩽ |eλφ| (λ‖φ‖ C K (Td))|β|
(
1 +O
( 1
λ‖φ‖ C K (Td)
))
if |β| ⩽ Kd. Now, ifξ /∈ [−ε
2, ε
2 ]d, then one of the coordinates ξi has modulus
larger than ε
2 , so |eφ(ξ)| ⩽ e− M ε 2
4 . We conclude that
‖
‖ (1 −cd) eλφ‖
‖
A
⩽ 2KdCH,d
(
sup
|γ|⩽ Kd
‖∂γ(1 −cd,ε)‖ L 2
)
(λ ‖φ‖ C K (Td))K e− λ M ε 2
4 +O( 1
λ ),
where the constant in the O( · ) only depends on d and the exponent φ.
Finally, as soon as γ ⁄= 0, ∂γ(1 −cd,ε) = − 1
ε|γ | (∂γcd,1)(ξ
ε ), so,
‖∂γ(1 −cd,ε)‖ L 2 = 1
ε|γ|
√ ∫
[−ε,ε]d
⏐
⏐
⏐
⏐(∂γcd,1)
(ξ
ε
) ⏐
⏐
⏐
⏐
2 dξ
(2π)d
= 1
ε|γ|− d
2
√ ∫
[−1,1]d
|(∂γcd,1)(θ)|2 dθ
(2π)d
=O
( 1
ε|γ|− d
2
)
.
TOME 70 (2020), F ASCICULE 3
1178 R. CHHAIBI, F. DELBAEN, P.-L. MÉLIOT & A. NIKEGHBALI
We conclude by taking the maximal possible value |γ| = Kd, which gives
Kd − d
2 = 1 if d is even, and 1
2 if d is odd. □
Lemma 5.5. — Under the assumptions of Theorem 5.3, there exists an-
other constant C(d,c,φ ) such that
‖
‖cd,ε (ψ −χ) eλφ‖
‖
A
⩽ C(d,c,φ )εr+1βr+1(ε)
λ
d
4
(√
λ + 1
ε
) K(
1 +O
( 1√
λ
))
.
Again, the constant hidden in the O( · ) depends only on d, c and φ.
Proof. — The hypothesis on γ(ε) ensures that, for any index i ∈ [ [1,d ] ]
and any θ ∈ [−ε,ε ], Re(φ′′
i (θ)) ⩽ −σ2
i/2 and |φ′′
i (θ)| ⩽ 2σ2
i . On the other
hand, as in the case d = 1 dealt with by Lemma 2.5, we can shift phases
byS(ξ) = i∑ d
i=1ξi⌊λmi⌋:
‖
‖cd,ε (ψ −χ) eλφ‖
‖
A
=
‖
‖cd,ε (ψ −χ) eλφ−S‖
‖
A
⩽ CH,d sup
|α|⩽ Kd
‖∂α(cd,ε (ψ −χ) eλφ−S)‖ L 2([−ε,ε]d)
⩽ CH,d sup
|α|⩽ Kd

 ∑
β+γ+δ=α
d∏
i=1
( αi
βi,γi,δi
)
‖∂βcd,ε∂γ(ψ −χ)‖ L ∞([−ε,ε]d)
× ‖∂δeλφ−S‖ L 2([−ε,ε]d)

.
On the last line, we can bound ‖∂βcd,ε‖ L ∞([−ε,ε]d) by C(d,c )ε−|β|, and
‖∂γ(ψ −χ)‖ L ∞([−ε,ε]d) by βr+1(ε) (dε)r+1−|γ|. Thus,
‖
‖cd,ε (ψ −χ) eλφ‖
‖
A
is smaller than
C(d,c )εr+1βr+1(ε)
× sup
|α|⩽ Kd

 ∑
ρ+δ=α
d∏
i=1
( αi
ρi,δi
)
ε−|ρ| ‖∂δeλφ−S‖ L 2([−ε,ε]d)


where C(d,c ) is some positive constant depending only on d and the cut
function c.
ANNALES DE L’INSTITUT FOURIER
APPROXIMATION OF DISCRETE MEASURES 1179
To bound the norms ‖∂δeλφ−S‖ L 2([−ε,ε]d), we use the same combinatorics
of Bell polynomials as in the previous lemma. Speciﬁcally, we have
⏐
⏐
⏐
⏐
∂n(eλφi(θ)−i⌊λmi⌋θ)
∂θn
⏐
⏐
⏐
⏐
⩽
⏐
⏐
⏐eλφi(θ)
⏐
⏐
⏐
⏐
⏐
⏐
⏐
⏐
n∑
k=1
Bn,k(λφ′
i(θ) − i⌊λmi⌋,λφ ′′
i (θ),...,λφ (n−k+1)
i (θ))
⏐
⏐
⏐
⏐
⏐,
and the variables of the incomplete Bell polynomials that appear above are
bounded as follows:
|λφ′
i(θ) − i⌊λmi⌋| ⩽ λ|φ′
i(θ) −φ′
i(0)| + |λmi − ⌊λmi⌋|
⩽ λ ‖φ′′
i ‖ L ∞([−ε,ε]) |θ| + 1 ⩽ 2λσ 2
i |θ| + 1;
|λφ(r/greaterorequalslant2)
i (θ)| ⩽ λ ‖φ(r)
i ‖ ∞ ⩽ λ ‖φ‖ C n(Td),
Rewriting the complete Bell polynomial Bn = ∑ n
k=1Bn,k as a sum over
integer partitions of size n, we thus obtain
⏐
⏐
⏐
⏐
∂n(eλφi(θ)−i⌊λmi⌋θ)
∂θn
⏐
⏐
⏐
⏐ e
λσ 2
i θ 2
4
⩽
∑
L partition
of size n
Bn,L
(
2λσ 2
i |θ| + 1
) m1(L)(
λ ‖φ‖ C n(Td)
) ℓ(L)−m1(L)
.
where Bn,L = n!∏
i/greaterorequalslant1((i!)mi(L)mi(L)!) is the number of set partitions of [ [1,n ] ]
whose parts have their sizes prescribed by the integer partition L. Conse-
quently,
√ ∫ ε
−ε
⏐
⏐
⏐
⏐
∂n(eλφi(θ)−i⌊λmi⌋θ)
∂θn
⏐
⏐
⏐
⏐
2
dθ
2π
⩽
∑
L partition
of size n
Bn,L (λ ‖φ‖ )ℓ(L)−m1(L)
√ ∫ ε
−ε
e−
λσ 2
i θ 2
2 (2λσ 2
i |θ| + 1)2m1(L) dθ
2π,
and each integral under the square root sign is equal to
/radicaltp
/radicalvertex
/radicalvertex
√
1√
2πλσ 2
i
2m1(L)∑
k=0
(2m1(L)
k
)
(2
√
λσi)k
∫
R
e− x2
2 |x|k dx√
2π
= 2m1(L)√
(2m1(L) − 1)!!
(2π)1/4 (λσ 2
i )
m1(L)
2 − 1
4
(
1 +O
( 1√
λ
))
.
TOME 70 (2020), F ASCICULE 3
1180 R. CHHAIBI, F. DELBAEN, P.-L. MÉLIOT & A. NIKEGHBALI
Thus, the term corresponding to an integer partition L in the previous
bound on the norm ‖
‖
‖
‖
∂n(eλφi(θ)−i⌊λmi⌋θ)
∂θn
‖
‖
‖
‖
L 2([−ε,ε])
is of order O(λℓ(L)− m1(L)
2 − 1
4 ), where the constant in the O( · ) can depend
only on n andφ. The integer partitions that maximise the exponent ℓ(L) −
m1(L)
2 among those of ﬁxed size n are those with parts 1 or 2, of the form
L = ( 2 , 2,..., 2/bracehtipupleft/bracehtipdownright/bracehtipdownleft/bracehtipupright
j parts of size 2
, 1, 1,..., 1/bracehtipupleft/bracehtipdownright/bracehtipdownleft/bracehtipupright
n−2j parts of size 1
).
Therefore,
‖
‖
‖
‖
∂n(eλφi(θ)−i⌊λmi⌋θ)
∂θn
‖
‖
‖
‖
L 2([−ε,ε])
≲ 1
(2πλσ 2
i )
1
4
⌊ n
2 ⌋∑
j=0
n! (λ ‖φ‖ C n(Td))j
2jj! (n − 2j)! 2n−2j√
(2n − 4j − 1)!! (λσ 2
i )
n
2 −j
≲ C(n,φ )λ
n
2 − 1
4,
where the symbol ≲ means that the inequality holds up to a multiplicative
factor 1 + O( 1√
λ ). The constant C(n,φ ) and the constant hidden in the
O( · ) depend only on n and φ. Finally,
‖
‖cd,ε (ψ −χ) eλφ‖
‖
A
⩽ C(d,c,φ )εr+1βr+1(ε)
λ
d
4
(
1 +O
( 1√
λ
)) (
sup
|α|⩽ Kd
(√
λ + 1
ε
) |α|)
⩽ C(d,c,φ )εr+1βr+1(ε)
λ
d
4
(√
λ + 1
ε
) Kd(
1 +O
( 1√
λ
))
. □
Proof of Theorem 5.3. — As in the one dimensional case, it suﬃces now
to write
‖ˆµ −ˆν‖ A ⩽ ‖ψ −χ‖ A
‖
‖ (1 −cd,ε) eλφ‖
‖
A +
‖
‖cd,ε (ψ −χ) eλφ‖
‖
A ,
and to use the two previous lemmas. □
Corollary 5.6. — With the assumptions of Theorem 5.3, for any r /greaterorequalslant
⌊d
2 ⌋, there exists a positive constant C3(r,d,c,φ ) such that, if ε> 0 is ﬁxed
and λ /greaterorequalslant2 is suﬃciently large (chosen according to ε), then
‖ˆµ −ˆν‖ A ⩽ C3(r,d,c,φ ) (‖ψ −χ‖ A +βr+1(ε)) (logλ)r+1
λ
r
2 + 1
4
.
ANNALES DE L’INSTITUT FOURIER
APPROXIMATION OF DISCRETE MEASURES 1181
Proof. — Setε = t logλ√
λ witht> 0. We then have, up to a multiplicative
remainder (1 +o(1)), a bound on the norm ‖ˆµ −ˆν‖ A equal to the sum of
the two terms:
C1(d,c,φ ) ‖ψ −χ‖ A
λK+ 1
2 − tM
4
t logλ
and C1(d,c,φ )βr+1(ε) (t logλ)r+1λ
K
2 − r+1
2 − d
4.
We set t = 1
M (d + 2r + 2K + 4), so that the two powers of λ agree. Note
that
Kd
2 − r + 1
2 − d
4 =
d
2 + 1
2 − r + 1
2 − d
4 =
{
−r
2 if d is even,
−r
2 − 1
4 if d is odd.
So,
‖ˆµ −ˆν‖ A ⩽



C3(r,d,c,φ ) (‖ψ −χ‖ A +βr+1(ε)) (logλ)r+1
λ
r
2
if d is even,
C3(r,d,c,φ ) (‖ψ −χ‖ A +βr+1(ε)) (logλ)r+1
λ
r
2 + 1
4
if d is odd.
If d is odd, the claim is proven. Otherwise, notice that if µ and ν are two
measures satisfying the hypotheses of Theorem 5.3 in even dimension d,
then
µ+(k1,...,k d,kd+1) = µ(k1,...,k d) e−λλkd+1
(kd+1)! ;
ν+(k1,...,k d,kd+1) = ν(k1,...,k d) e−λλkd+1
(kd+1)!
are signed measures on Zd+1 that again satisfy the hypotheses of Theo-
rem 5.3:
ˆµ+(ξ1,...,ξ d+1) = ˆµ(ξ1,...,ξ d+1) eλ(eiξ d+1 −1)
= eλΦ( x1,...,x d+1)ψ(ξ1,...,ξ d);
ˆν+(ξ1,...,ξ d+1) =ˆν(ξ1,...,ξ d+1) eλ(eiξ d+1 −1)
= eλΦ( x1,...,x d+1)χ(ξ1,...,ξ d),
where Φ( ξ1,...,ξ d+1) = φ(ξ1,...,ξ d) + eλ(eiξ d+1 −1). Since
‖
‖
‖ ˆµ+ −ˆν+
‖
‖
‖
A
= ‖ˆµ −ˆν‖ A ,
we can apply our result in dimension d + 1, assuming r /greaterorequalslant⌊d+1
2 ⌋:
‖ˆµ −ˆν‖ A ⩽ C3(r,d + 1,c,φ ) (‖ψ −χ‖ A +βr+1(ε)) (logλ)r+1
λ
r
2 + 1
4
.
TOME 70 (2020), F ASCICULE 3
1182 R. CHHAIBI, F. DELBAEN, P.-L. MÉLIOT & A. NIKEGHBALI
However, for d even, ⌊d+1
2 ⌋ = ⌊d
2 ⌋, so the minimum r that one can take is
again ⌊d
2 ⌋. □
In comparison to the one dimensional case, we lost a logarithmic factor
(logλ)r+1 in our estimate of norms (cf. Theorem 2.3). This will not be a
problem for the calculation of asymptotics of distances.
5.2. Asymptotics of distances in the multi-dimensional setting
As in the one-dimensional case, a combination of the Laplace method
and of the norm estimates given by Corollary 5.6 yields under appropri-
ate hypotheses the asymptotics of dL(µn,νn) and of dTV(µn,νn), where
(νn)n∈N is a general scheme of approximation of the laws µn of the mod-φ
convergent random variables Xn in Zd. The only diﬀerence is that, for the
computation of the total variation distance, we shall need to assume the
order of approximation r to be larger than some minimal value ⌊d
2 ⌋.
Until the end of this paragraph, (Xn)n∈N is a sequence of random vari-
ables with values in Zd, which converges mod- φ with parameters λn → ∞
and limit residue ψ(ξ1,...,ξ d). In the sequel, we shall write (νn)n∈N a se-
quence of signed measures on Zd such that ˆνn(ξ) = eλnφ(ξ)χn(ξ1,...,ξ d),
with limn→∞χn(ξ1,...,ξ d) = χ(ξ1,...,ξ d). The multi-dimensional ana-
logue of the hypothesis (H1) is:
(H1d)
ψn(ξ)−χn(ξ) =
∑
α1+···+αd=r+1
β(α1,...,α d)
n (iξ1)α1 · · ·(iξd)αd (1+oξ(1));
ψ(ξ)−χ(ξ) =
∑
α1+···+αd=r+1
β(α1,...,α d) (iξ1)α1 · · ·(iξd)αd (1+oξ(1))
with limn→∞βα
n =βα for any choice of index α = (α1,...,α d) with |α| =
r + 1. On the other hand, we write in the following ‖x‖ 2 = ∑ d
i=1(xi)2,
Hα(x) =∏ d
i=1Hαi(xi), σα =∏ d
i=1(σi)αi, and ﬁnally
k −λnm
√λnσ =
(ki −λnmi√λnσi
)
i∈[ [1,d] ]
if k ∈ Zd.
ANNALES DE L’INSTITUT FOURIER
APPROXIMATION OF DISCRETE MEASURES 1183
Proposition 5.7. — Under the assumption (H1d) with any r /greaterorequalslant0, one
has
(λn)
r+d+1
2 (µn(k1,...,k d) −νn(k1,...,k d))
=

 ∑
|α|=r+1
βα
σα
1
∏ d
i=1(
√
2πσi)
e
− 1
2
‖
‖
‖
k−λ nm
√
λ nσ
‖
‖
‖
2
Hα
(k −λnm
√λnσ
) 
 +o(1)
with a remainder that is uniform over Zd.
Proof. — The same arguments as in dimension 1 (d-dimensional Fourier
inversion formula and Laplace method) yield
µn(k1,...,k d) −νn(k1,...,k d)
≃
∑
|α|=r+1
βα
n
(2π)d
∫
[−ε,ε]d
( d∏
i=1
(iξi)αi eλn(φi(iξi)−imiξi) e−i (k−λnmi)ξi
)
dξ
(2π)d
≃
∑
|α|=r+1
βα
n
(2π)
d
2
d∏
i=1
(
1
(√λnσi)αi+1
∫
R
(ix)αi e− x2
2 e
−i
(
ki−λ nmi√
λ n σ i
)
x dx√
2π
)
,
where the symbol ≃ means that the two sides diﬀer by a o((λn)− r+d+1
2 )
which does not depend on k1,...,k d. We now observe that the same Her-
mite polynomials as in Proposition 3.2 appear. □
We now use the same argument as in the proof of Theorem 3.3. The
sequence of lattices {k−λnm√λnσ , k ∈ Zd} becomes dense, therefore:
Theorem 5.8. — Under the hypothesis (H1d), one has
dL(µn,νn)
= sup
x∈Rd

e− ‖ x‖ 2
2
⏐
⏐
⏐
⏐
⏐
⏐
∑
|α|=r+1
βαHα(x)
σα
⏐
⏐
⏐
⏐
⏐
⏐

 × 1 +o(1)
(∏ d
i=1
√
2πσi) (λn)
r+d+1
2
.
The proof of the multi-dimensional analogue of Theorem 3.11 is a bit
more involved, but the main diﬃculty was lying in the proof of the norm
estimate (Corollary 5.6). In the following we ﬁx r /greaterorequalslant⌊d
2 ⌋; then, r + 1 /greaterorequalslantKd.
The multi-dimensional version of the hypothesis (H2) is the following. We
assume the residues ψ, ψn, χ and χn to be of class CKd on Td, with
∂δ(ψn −χn)(0) = ∂δ(ψ −χ)(0) = 0 for any |δ|<K d. We also assume that
there exist families of coeﬃcients (βα
n )|α|=r+1,n∈N and (γα
n )|α|=r+2,n∈N, such
TOME 70 (2020), F ASCICULE 3
1184 R. CHHAIBI, F. DELBAEN, P.-L. MÉLIOT & A. NIKEGHBALI
that for any multi-index δ with |δ| =Kd,
(H2d)
∂δ(ψn −χn)(ξ) = i |δ|

 ∑
|ρ|=r+1−|δ|
βρ+δ
n
(ρ +δ)!
ρ! (iξ)ρ
+
∑
|ρ|=r+2−|δ|
γρ+δ
n
(ρ +δ)!
ρ! (iξ)ρ(1 +oξ(1))

;
∂δ(ψ −χ)(ξ) = i |δ|

 ∑
|ρ|=r+1−|δ|
βρ+δ (ρ +δ)!
ρ! (iξ)ρ
+
∑
|ρ|=r+2−|δ|
γρ+δ (ρ +δ)!
ρ! (iξ)ρ(1 +oξ(1))


with limn→∞βα
n =βα and limn→∞γα
n =γα. Here, given a multi-index α,
we write α! = ∏
i=1(αi)! and (iξ)α = ∏ d
i=1(iξi)αi. These hypotheses are
satisﬁed e.g. if the convergences ψn →ψ and χn →χ occur in Cr+2(Td),
and if (νn)n∈N is the scheme of approximation of order r of the sequence
of random variables (Xn)n∈N (its deﬁnition in dimension d /greaterorequalslant2 is similar
to the deﬁnition in dimension 1 given in Example 1.11, see also the two
worked examples hereafter).
Under the hypothesis (H2d), if one wants to prove a bound on dTV(µn,νn)
of order O((λn)− r+1
2 ), then one can replace νn with the measure ρn deﬁned
by the Fourier transform
ˆρn(ξ) = eλnφ(ξ)

ψn(ξ) −
∑
|α|=r+1
βα
n
d∏
i=1
(eiξi − 1)αi

.
Indeed, denoting ~ψn(ξ) the residue associated to ρn, the hypothesis (H2d)
implies that, for any |δ| ⩽ Kd,
⏐
⏐
⏐∂δ(~ψn −χn)(ξ)
⏐
⏐
⏐ ⩽ C |ξ|r+2−|δ|
with a constant C that is uniform, and also valid for the partial derivatives
|∂δ(~ψ−χ)(ξ)|. This bound is the only one useful in the proof of Theorem 5.3
and its Corollary 5.6, and therefore, one can apply Corollary 5.6 with a
parameter r + 1 instead of r. We thus get
dTV(ρn,νn) = O
(
(logλn)r+2
(λn)
r+1
2 + 1
4
)
=o
(
1
(λn)
r+1
2
)
.
ANNALES DE L’INSTITUT FOURIER
APPROXIMATION OF DISCRETE MEASURES 1185
From there, the proofs are essentially identical to the one dimensional case
(Theorem 3.11), and one obtains:
Theorem 5.9. — Consider a general approximation scheme (νn)n∈N of
a mod-φ convergent sequence (Xn)n∈N in Zd. We assume that r /greaterorequalslant⌊d
2 ⌋ and
that the hypothesis (H2d) is satisﬁed. Then,
dTV(µn,νn) = 1 +o(1)
(2π)
d
2 (λn)
r+1
2


∫
Rd
e− ‖ x‖ 2
2
⏐
⏐
⏐
⏐
⏐
⏐
∑
|α|=r+1
βαHα(x)
σα
⏐
⏐
⏐
⏐
⏐
⏐
dx

.
Last, the discussion of Section 3.4 holds mutatis mutandis in the multi-
dimensional setting, and if ‖χn −χ‖ C Kd is asymptotically smaller than any
negative power of λn, then one can replace (νn)n∈N by the derived scheme
(σn)n∈N with constant residue and keep the conclusions of Theorems 5.8
and 5.9.
5.3. Cycle-type of random coloured permutations
In this section, we study random elements of the group of d-coloured
permutations:
Gn = Sn ≀ (Z/dZ) = Sn ⋉ (Z/dZ)n.
It can be viewed as the group of complex matrices of size n times n, with
one non-zero coeﬃcient on each row and each column, and these non-
zero coeﬃcients belonging to the group of d-th roots of unity Z/dZ =
{1,ω,ω 2,...,ω d−1}, with ω = e
2iπ
d . Another alternative deﬁnition is the
following: if we identify Snd with S(Z/nZ × Z/dZ), then
Gn = {σ ∈ Snd | ∀ (a,b ) ∈ Z/nZ × Z/dZ, σ(a,b + 1) = σ(a,b ) + (0, 1)}.
From this deﬁnition, it appears that a d-coloured permutation is entirely
determined by the images of the elements (a, 0) with a ∈ Z/nZ:
σ(a, 0) = (ρ(a),k (a)) with ρ ∈ Sn = S(Z/nZ).
One then has σ(a,b ) = (ρ(a),k (a) +b). In particular, cardGn =n!dn, the
factor n! coming from the choice of ρ ∈ Sn, and the factor dn from the
choice of the elements k(a).
Let us identify the conjugacy classes of elements of Gn (we refer to [15,
Section 2.3]). Suppose that σ2 = τσ 1τ −1 in Gn, with σi associated to
the pair (ρi,ki) ∈ Sn × (Z/dZ)n, and τ associated to the pair (ν,l ). Note
TOME 70 (2020), F ASCICULE 3
1186 R. CHHAIBI, F. DELBAEN, P.-L. MÉLIOT & A. NIKEGHBALI
that τ −1 = (ν−1, −l ◦ν−1), this identity coming from the product rule
(ρ1,k 1)(ρ2,k 2) = (ρ1ρ2,k 1 ◦ρ2 +k2). Then,
(ρ2,k 2) = (ν,l )(ρ1,k 1)(ν−1, −l ◦ν−1)
= (ν,l )(ρ1ν−1, (k1 −l) ◦ν−1)
= (νρ1ν−1, (k1 +l ◦ρ1 −l) ◦ν−1),
so in particular ρ1 and ρ2 are conjugated in Sn, so they have the same
cycle-type (an integer partition L of size |L| =n). Then, to determine the
conjugacy class of (ρ1,k 1), taking the conjugate of (ρ2,k 2) by (ν−1, 0), we
can assume that ρ1 =ρ2 =ρ, in which case
σ1 = (ρ,k 1) ; σ2 = (ρ,k 2 =k1 + (l ◦ρ −l)),
that is to say that k2 and k1 diﬀer by a cocycle l ◦ρ −l. This is possible
if and only if, for every cycle c = (a = ρr(a),ρ (a),ρ 2(a),...,ρ r−1(a)) of
ρ ∈ Sn, one has
k1(a) +k1(ρ(a)) + · · · +k1(ρr−1(a)) = k2(a) +k2(ρ(a)) + · · · +k2(ρr−1(a)).
Indeed, one has
r−1∑
j=0
(l ◦ρ −l)(ρj(a)) = l(ρr(a)) −l(a) = l(a) −l(a) = 0.
In the previous setting, denote Σ(c,k ) = ∑ r−1
j=0k(ρj(a)), which is an ele-
ment of Z/dZ. This quantity depends only on the cycle c, and not on the
choice of a representative a of the corresponding orbit; it allows to one to
“color” each cycle of ρ. Then (cf. [15, Theorem 2.3.5], applied to the abelian
case):
Theorem 5.10. — Two coloured permutations σ1 = (ρ1,k 1) and σ2 =
(ρ2,k 2) are conjugated in Gn = Sn ≀ (Z/dZ) if and only if:
(1) the permutationsρ1 andρ2 have the same lengths of cycles (encoded
by an integer partition L of size n);
(2) and there is a size-preserving bijection c ↦→ψ(c) between the cycles
of ρ1 and ρ2, such that the colors are also preserved:
Σ(c,k 1) = Σ(ψ(c),k 2).
Consequently, the conjugacy classes of Gn are labelled by the d-uples of
integer partitions L = (L(1),L (2),...,L (d)), such that ∑ d
i=1 |L(i)| = n. If
σ ∈Gn is of type L, then the parts of L(i) are the sizes of the cycles of σ
with color i ∈ Z/dZ.
ANNALES DE L’INSTITUT FOURIER
APPROXIMATION OF DISCRETE MEASURES 1187
Example 5.11. — Consider the following 2-coloured permutation in the
group G8 = S8 ≀ Z/2Z:
σ =
(
38762415, 11010001
)
,
where the ﬁrst part is the word ρ(1)ρ(2)...ρ (8) of the permutation ρ of
size 8 underlyingσ, and the second part is the word k(1)k(2)...k (8). The
three disjoint cycles of ρ are (1, 3, 7), (2, 8, 5) and (4, 6), and the associated
colors are 1 + 0 + 0 = 1 , 1 + 1 + 0 = 0 and 1 + 0 = 1 . Therefore, the
cycle-type of σ is
L(1) = (3, 2),L (2) = (3)
since the sizes of the cycles of color 1 are 3 and 2, and the size of the unique
cycle of color 0 is 3. We leave the reader check that the other 2-coloured
permutation
σ′ =
(
73864512, 10011100
)
has the same cycle-type ((3, 2), (3)). Therefore, σ and σ′ are conjugated
in Gn.
In the following, we denote σn a random uniform element of the wreath
product Gn, and ℓn = (ℓ(1)
n ,ℓ (2)
n ,...,ℓ (d)
n ) the random d-uple of integers
that consists in the lengths of the partitions L(1),...,L (d) of the cycle-type
of σn. Our goal is to apply the results of the previous paragraph to these
random vectors. To this purpose, it is convenient to construct a coupling of
all the random permutations (σn)n∈N, which generalizes the Feller coupling
in the case d = 1 of the Feller coupling. Algebraically, this amounts to the
following:
Lemma 5.12. — We consider Gn as a subgroup of Gn+1, by sending a
pair
(ρ ∈ Sn, (k1,...,k n) ∈ (Z/dZ)n)
to the pair
(ρ ∈ Sn+1, (k1,...,k n, 0) ∈ (Z/dZ)n+1).
Let σn+1 be an element of Gn+1. There exists a unique element σn ∈Gn,
and a unique coloured transposition
τn = ((j,n + 1), (0,..., 0,α, 0,..., 0, −α)) with j ∈ [ [1,n + 1] ],
and the α ∈ Z/dZ at position j, such that σn+1 = τnσn. Here we agree
that the trivial transposition (n + 1,n + 1) is the identity permutation; in
this case we put α in position n + 1, and there is no term −α.
TOME 70 (2020), F ASCICULE 3
1188 R. CHHAIBI, F. DELBAEN, P.-L. MÉLIOT & A. NIKEGHBALI
Proof. — Denote σn+1 = (ρn+1, (k1,...,k n+1)). If
ρn =ρn+1 ◦ (j =ρ−1
n+1(n + 1),n + 1),
then ρn sends n + 1 to n + 1, so it can be considered as a permutation in
Sn. We then have ρn+1 =ρn ◦ (j,n + 1). Set
σn = (ρn, (k1,...,k j−1,kj +kn+1,kj+1,...,k n)) ∈Gn.
We then have
σnτn
= (ρn, (k1,...,k j +kn+1,...,k n, 0))((j,n + 1), (0,...,k j,..., −kj))
= (ρn ◦ (j,n + 1), (k1,..., 0,...,k n,kj +kn+1) + (0,...,k j,..., 0, −kj))
= (ρn+1, (k1,...,k n+1)) = σn+1.
The unicity of τn comes from a cardinality argument: cardGn+1
cardGn
= (n + 1)d,
and this is the number of d-coloured transpositions
((j,n + 1), (0,..., 0,α, 0,..., 0, −α)). □
We denote T (j,α ) the coloured transposition of the previous lemma.
Then, in order to construct a random coloured permutation σn ∈Gn, it suf-
ﬁces to take random independent positive integers j1 ⩽ 1,j 2 ⩽ 2,...,j n ⩽
n, and random independent elements α1,...,α n ∈ Z/dZ, and to consider
the product
σn =T (j1,α 1) ◦T (j2,α 2) ◦ · · · ◦T (jn,αn).
We also denote (Fn)n∈N the ﬁltration of probability spaces associated to
the sequence of random coloured permutations (σn)n∈N. The interest of our
construction is that one can easily follow the evolution of the cycle type
of σn. More precisely, if jn =n, then to construct σn, one adds a cycle of
length 1 to σn−1, with color αn. Thus, for every color i ∈ Z/dZ, there is a
probability 1
nd to increase the length ℓ(i) by one unit:
∀i ∈ [ [1,d ] ], P[ℓn =ℓn−1 + (0,..., 0, 1i, 0,..., 0)|Fn−1] = 1
nd.
On the other hand, if jn ⁄=n, then the multiplication by T (jn,αn) increases
by 1 the size of the cycle containing jn in σn−1, but it does not change its
color, because of the terms αn and −αn that compensate one another. So,
P[ℓn =ℓn−1|Fn−1] = 1 − 1
n.
ANNALES DE L’INSTITUT FOURIER
APPROXIMATION OF DISCRETE MEASURES 1189
We have therefore proven that ℓn is a sum of independent increments in
Zd, with
P[ℓn −ℓn−1 = 0] = 1 − 1
n ; P[ℓn −ℓn−1 =ei] = 1
nd,
where (ei)i∈[ [1,d] ] is the canonical basis of the lattice Zd.
As an immediate consequence of the previous discussion, we have:
Theorem 5.13. — The sequence of random vectors (ℓn)n∈N converges
modulo a d-dimensional Poisson law of exponent φ(ξ) = 1
d
∑ d
i=1 (eiξi − 1),
with parameters Hn and limiting function
ψ(ξ) =
∞∏
n=1
(
1 + 1
nd
d∑
i=1
(eiξi − 1)
)
e− 1
nd
∑ d
i=1(eiξ j −1)
= eγφ (ξ) 1
Γ
(
1
d
∑ d
i=1 eiξi
) .
Proof. — Since the increments of ℓn are independent,
E[ei⟨ξ |ℓn⟩ ] =
n∏
j=1
(
1 + 1
jd
d∑
i=1
(eiξi − 1)
)
= eHnφ(ξ)ψn(ξ)
where ψn(ξ) is the partial product over indices in [ [1,n ] ]coming from the
inﬁnite product ψ(ξ). □
In particular, since the Fourier transform of ℓn does not factorize over
the coordinates ξi, the coordinates of ℓn are not independent, though in the
asymptoticsn → ∞ and at ﬁrst order, ℓn looks like a d-uple of independent
Poisson variables of parameters Hn
d . In the following, in order to simplify
a bit the discussion, we assume d = 2 , which already contains all the
subtleties of the general case. We denote (x,y ) the coordinates in R2, and
(ξ,ζ ) the coordinates in the Fourier space. We can then write:
ψn(ξ,ζ ) =
n∏
j=1
(
1 + 1
j
(eiξ + eiζ
2 − 1
))
e
− 1
j
(
eiξ +eiζ
2 −1
)
=
∞∑
k=0
ek,n
(eiξ + eiζ
2 − 1
) k
= 1 − p2,n
2
(eiξ + eiζ
2 − 1
) 2
+o(‖ (ξ,ζ )‖ 2)
TOME 70 (2020), F ASCICULE 3
1190 R. CHHAIBI, F. DELBAEN, P.-L. MÉLIOT & A. NIKEGHBALI
where the ek,n’s are obtained from the parameters
p1,n = 0 ; pk/greaterorequalslant2,n =
n∑
j=1
1
jk
by the same recipe as in Section 4. The scheme of approximation of (ℓn)n∈N
of order r = 1 is the Poissonian approximation
ˆνn(ξ,ζ ) = e
Hn
(
eiξ +eiζ
2 −1
)
; νn(k,l ) = e −Hn (Hn)k+l
2k+lk!l!.
It satisﬁes the hypotheses (H1d) and (H2d), with β(2,0)
n = β(0,2)
n = − p2,n
8
and β(1,1)
n = − p2,n
4 . Since H(2,0)(x,y ) = x2 − 1, H(1,1)(x,y ) = xy and
H(0,2)(x,y ) = y2 − 1, Theorems 5.8 and 5.9 ensure that
dL(µn,νn) = π
6 (logn)2 sup
(x,y)∈R2
⏐
⏐
⏐
⏐e− x2+y2
2 (2 − (x +y)2)
⏐
⏐
⏐
⏐ +o
( 1
(logn)2
)
;
dTV(µn,νn) = π
24 logn
(∫
R2
e− x2+y2
2 |2 − (x +y)2| dx dy
)
+o
( 1
logn
)
since∑
|α|=2
βα Hα (x)
σα = − p2
2 ((x +y)2 − 2) = π2
12 (2 − (x +y)2).
0 0. 5 1 − 2
0
2
0
1
2
x
y
Figure 5.1. The function e− x2+y2
2 |2 − (x +y)2|.
For the local distance, one checks at once that the maximum of the
function f (x,y ) = e − x2+y2
2 |2 − (x +y)2| is obtained when x =y = 0, so
dL(µn,νn) = π
3 (logn)2 (1 +o(1)),
see Figure 5.1. For the total variation distance, a computer algebra system
(SageMath) yields the approximate value 12. 162... for the integral. As
in the one-dimensional case (Example 1.6 and Section 4.3), one can on
ANNALES DE L’INSTITUT FOURIER
APPROXIMATION OF DISCRETE MEASURES 1191
the other hand construct better schemes of approximations, which yield
distances smaller than any arbitrary negative power of logn. It is important
to notice that the dependence between the diﬀerent coordinates of ℓn is
directly involved in these asymptotics of distances.
5.4. Distinct prime divisors counted according to their residue
classes
Similar to the generalisation of Section 4.3 by the study of random
coloured permutations, there is a natural generalisation of the discussion of
Section 4.5 on distinct prime divisors of a random integer, which involves
residue classes of prime numbers.
Fix an integer a /greaterorequalslant2, and denote d =ϕ(a) the cardinality of the multi-
plicative group (Z/aZ)∗. This quantity is the usual Euler ϕ-function, and
it is equal to the number of integers in [ [1,a ] ]that are coprime to a. We
label the elements of (Z/aZ)∗ as b1,b 2,...,b d. If n ∈ N and i ∈ [ [1,d ] ], we
denote ωi(n) the number of distinct prime divisors of n that have residue
class bi modulo a:
ωi(n) = card {p ∈ P, p |n and p ≡bi moda}.
One then has
∑
i∈(Z/aZ)∗
ωi(n) = ω(n) − card{p ∈ P, p |a and p |n}.
We are interested in the random vector Ω( Nn) = ( ω1(Nn),...,ω d(Nn)),
where Nn is a random integer chosen uniformly in [ [1,n ] ]. In view of the
theory developed in the previous sections, the asymptotics of these vectors
are encoded in the multiple generating series
1
n
n∑
i=1
(z1)ω1(i)(z2)ω2(i) · · ·(zd)ωd(i).
In number theory, the asymptotics of such quantities are classically related
to the behavior of the Dirichlet series
F (z,s ) =
∞∑
n=1
(z1)ω1(n)(z2)ω2(n) · · ·(zd)ωd(n)
ns .
In a moment we shall precise these relations, which amount to the so-called
Selberg–Delange method, see [57, Chapter II.5]. Note that, though we want
to study a random vector in Zd/greaterorequalslant2, the Dirichlet series written above is not
a multiple Dirichlet series.
TOME 70 (2020), F ASCICULE 3
1192 R. CHHAIBI, F. DELBAEN, P.-L. MÉLIOT & A. NIKEGHBALI
The main algebraic tool that is required in order to use Selberg–Delange
method is the theory of Dirichlet characters and their L-series, see for
instance [57, Chapter II.8]. In the following we recall the basics of this
theory. The space of functions (Z/aZ)∗ → C is endowed with a Hilbert
structure
⟨f |g⟩ = 1
ϕ(a)
∑
i∈(Z/aZ)∗
f (i)g(i),
and a Hilbert basis consists of the Dirichlet characters χa,1,...,χ a,d, which
are the morphisms of (multiplicative) groups χ : ( Z/aZ)∗ → C∗. In par-
ticular, there are as many Dirichlet characters as elements of the group
(Z/aZ)∗, i.e., d distinct characters. In the following, we denote χa,1 the
trivial character: χa,1(i) = 1 for all i ∈ (Z/aZ)∗.
If χ is a character of (Z/aZ)∗, introduce its L-function
L(χ,s ) =
∞∑
n=1
χ(n)
ns ,
where the function χ is extended to Z by
χ(n) =
{
χ(m) if (n,a ) = 1 and m ≡n moda,
0 if (n,a )> 1.
These functions admit an Euler product representation:
L(χ,s ) =
∏
p∈Pa
(
1 − χ(p)
ps
) −1
,
where Pa is the set of prime numbers that do not divide a. In particular,
L(χa,1,s ) is almost the same as Riemann’s ζ-function:
L(χa,1,s ) =
∏
p∈Pa
(
1 − 1
ps
) −1
=ζ(s)
∏
p|a
(
1 − 1
ps
)
.
Therefore, the L-function associated to the trivial character has abscissa
of convergence 1, and can be extended to a meromorphic function on the
half-plane Re(s) > 0, with a single pole at s = 1 . On the other hand, for
the other characters χa,2,...,χ a,d, the corresponding L-functions converge
simply towards holomorphic functions on the same half-plane Re(s)> 0.
We now form the Dirichlet series
F (z,s ) =
∑
n/greaterorequalslant1
(z1)ω1(n) · · ·(zd)ωd(n)
ns .
ANNALES DE L’INSTITUT FOURIER
APPROXIMATION OF DISCRETE MEASURES 1193
For any choice of parameters z1,...,z d ∈ C, the series F (z,s ) converges
absolutely on the half-plane Re(s)> 1, as can be seen from the inequality
∑
n/greaterorequalslant1
⏐
⏐
⏐
⏐
(z1)ω1(n) · · ·(zd)ωd(n)
ns
⏐
⏐
⏐
⏐ ⩽
∏
p∈Pa
(
1 + maxi∈[ [1,d] ]|zi|
ps − 1
)
.
Given parameters y1,...,y d, we set
Gχ(z,s ) = F (z,s )
d∏
j=1
L(χa,j,s )−yi.
Let us choose the parameters y1,...,y d so that the series Gχ(z,s ) is an
holomorphic function on Re(s) > 1
2 . If Re(s) > 1, we can write without
ambiguity
F (z,s ) =
d∏
i=1
∏
p≡bi moda
(
1 + zi
ps − 1
)
;
Gχ(z,s ) =
d∏
i=1
∏
p≡bi moda
(
1 + zi
ps − 1
) d∏
j=1
(
1 − χa,j(p)
ps
) yj
=
∏
p∈Pa


(
1 + zi(p)
ps − 1
) d∏
j=1
(
1 − χa,j(bi(p))
ps
) yj


where i(p) is the unique i ∈ [ [1,d ] ]such that p ≡ bi moda. The Taylor
expansion of the term corresponding to p ∈ Pa is the previous product is
1 + 1
ps

zi(p) −
d∑
j=1
yjχa,j(bi(p))

 +O
( 1
p2s
)
.
Set yj = 1
d
∑ d
k=1zk
χa,j(bk). Then, by orthogonality of the Dirichlet char-
acters, one has:
d∑
j=1
yjχa,j(bi) = 1
d
d∑
j,k=1
zkχa,j(bk)χa,j(bi)
=d
d∑
j=1
⟨ d∑
k=1
zkbk
⏐
⏐
⏐
⏐
⏐χa,j
⟩
⟨χa,j |bi⟩
=d
⟨ d∑
k=1
zkbk
⏐
⏐
⏐
⏐
⏐bi
⟩
=zi.
Hence, for this choice of parameters, Gχ(z,s ) = ∏
p∈Pa
(
1 +O(p−2s)
)
, so
Gχ(z,d ) is an holomorphic function on Re(s)> 1
2 . Note thaty1 = z1+···+zd
d .
TOME 70 (2020), F ASCICULE 3
1194 R. CHHAIBI, F. DELBAEN, P.-L. MÉLIOT & A. NIKEGHBALI
Now, by the previous discussion on L-series, one can remultiply Gχ(z,s )
by∏
j⁄=1L(χa,j,s )yj , hence:
Proposition 5.14. — For any choice of complex parameters z1,...,z d,
the series
G(z,s ) = F (z,s ) (ζ(s))−
z1+···+zd
d
has an holomorphic extension on the half-plane Re(s)> 1
2 .
Proof. — If L(χa,1,s ) = ζa(s) is the partial ζ-function associated to the
integer a, then we shown that F (z,s ) (ζa(s))−
z1+···+zd
d is an holomorphic
function on Re(s)> 1
2 . It suﬃces then to multiply by the missing terms
∏
p|a
(
1 − 1
ps
) z1+···+zd
d
. □
We can now apply Theorem 3 in [57, Chapter II.5]:
Theorem 5.15. — When n goes to inﬁnity,
1
n
n∑
i=1
(z1)ω1(n) · · ·(zd)ωd(n)
= (logn)
z1+···+zd
d −1 G((z1,...,z d), 1)
Γ
(z1+···+zd
d
)
(
1 +O
( 1
logn
))
,
with a remainder that is locally uniform in the parameters z1,...,z d.
As a corollary, the random vectors (Ω( Nn))n∈N of numbers of distinct
prime divisors in each residue class of (Z/aZ)∗ converge mod-φ, where
φ(ξ) = 1
d
∑ d
j=1(eiξj − 1). The parameters of this mod- φ convergence are
λn = log logn, and the limiting residue is
ψ(ξ) = G((eiξ1,..., eiξd), 1)
Γ
(
eiξ 1 +···+eiξ d
d
) .
Moreover, the convergence happens at speed O( 1
logn ). As a consequence,
one can construct explicit schemes of approximations of the laws of the
vectors (Ω( Nn))n∈N, which yield distances that are O((log logn)− p
2 ) with
p /greaterorequalslant1 arbitrary (see Theorems 5.8 and 5.9). The ﬁrst of these schemes is
the Poisson approximation:
ˆνn(ξ) = e (log logn) 1
d
∑ d
i=1(eiξ i −1).
Unfortunately, it is then diﬃcult to calculate the constants involved in
these asymptotics of distances. Indeed, there are no simple expression for
the values of G((eiξ1,..., eiξd), 1) and its partial derivatives around ξ = 0.
ANNALES DE L’INSTITUT FOURIER
APPROXIMATION OF DISCRETE MEASURES 1195
BIBLIOGRAPHY
[1] R. Arratia, A. D. Barbour & S. Tavaré, Logarithmic Combinatorial Structures:
a Probabilistic Approach , EMS Monographs in Mathematics, European Mathemat-
ical Society, 2003.
[2] R. Arratia, L. Goldstein & L. Gordon , “Two moments suﬃce for Poisson ap-
proximations: the Chen-–Stein method”, Ann. Probab. 17 (1989), no. 1, p. 9-25.
[3] E. Artin , The gamma function , Athena Series. Selected Topics in Mathematics,
Holt, Rinehart and Winston, 1964.
[4] A. D. Barbour & V. Čekanavičius , “Total variation asymptotics for sums of
independent integer random variables”, Ann. Probab. 30 (2002), no. 2, p. 509-545.
[5] A. D. Barbour & G. K. Eagleson , “Poisson approximation for some statistics
based on exchangeable trials”, Adv. Appl. Probab. 15 (1983), no. 3, p. 585-600.
[6] A. D. Barbour, L. Holst & S. Janson , Poisson approximation, Oxford University
Press, 1992.
[7] A. D. Barbour, E. Kowalski & A. Nikeghbali , “Mod-discrete expansions”,
Probab. Theory Relat. Fields 158 (2014), no. 3-4, p. 859-893.
[8] A. D. Barbour & A. Xia, “Poisson perturbations”, ESAIM, Probab. Stat. 3 (1999),
p. 131-150.
[9] E. T. Bell , “Partition polynomials”, Ann. Math. 29 (1927), p. 38-46.
[10] V. Betz & D. Ueltschi, “Spatial random permutations and inﬁnite cycles”, Com-
mun. Math. Phys. 285 (2009), no. 2, p. 469-501.
[11] ——— , “Spatial random permutations with small cycle weights”, Probab. Theory
Relat. Fields 149 (2011), no. 1-2, p. 191-222.
[12] V. Betz, D. Ueltschi & Y. Velenik , “Random permutations with cycle weights”,
Ann. Appl. Probab. 21 (2011), no. 1, p. 312-331.
[13] K. A. Borovkov & D. Pfeifer , “On improvements of the order of approximation
in the Poisson limit theorem”, J. Appl. Probab. 33 (1996), no. 1, p. 146-155.
[14] L. Le Cam , “An approximation theorem for the Poisson binomial distribution”,
Pac. J. Math. 10 (1960), no. 4, p. 1181-1197.
[15] T. Ceccherini-Silberstein, F. Scarabotti & F. Tolli , Representation theory
and harmonic analysis of wreath products of ﬁnite groups , London Mathematical
Society Lecture Note Series, vol. 410, London Mathematical Society, 2014.
[16] V. Čekanavičius , “Asymptotic expansions in the exponent: a compound Poisson
approach”, Adv. Appl. Probab. 29 (1997), no. 2, p. 374-387.
[17] ——— , “Poisson approximations for sequences of random variables”, Stat. Probab.
Lett. 39 (1998), no. 2, p. 101-107.
[18] V. Čekanavičius & M. Mikalauskas, “Signed Poisson approximations for Markov
chains”, Stochastic Processes Appl. 82 (1999), no. 2, p. 205-227.
[19] L. H. Y. Chen , “On the convergence of Poisson binomial to Poisson distributions”,
Ann. Probab. 2 (1974), no. 1, p. 178-180.
[20] ——— , “Poisson approximation for dependent trials”, Ann. Probab. 3 (1975), no. 3,
p. 534-545.
[21] D. J. Daley & D. Vere-Jones , An introduction to the theory of point processes.
Vol. I: Elementary theory and methods , 2nd ed., Probability and Its Applications,
Springer, 2002.
[22] P. Deheuvels & D. Pfeifer , “A semigroup approach to Poisson approximation”,
Ann. Probab. 14 (1986), no. 2, p. 663-676.
[23] F. Delbaen, E. Kowalski & A. Nikeghbali , “Mod- φ convergence”, Int. Math.
Res. Not. 11 (2015), p. 3445-3485.
TOME 70 (2020), F ASCICULE 3
1196 R. CHHAIBI, F. DELBAEN, P.-L. MÉLIOT & A. NIKEGHBALI
[24] N. M. Ercolani & D. Ueltschi , “Cycle structure of random permutations with
cycle weights”, Random Struct. Algorithms 44 (2012), no. 1, p. 109-133.
[25] P. Erdős & M. Kac , “The Gaussian law of errors in the theory of additive number
theoretic functions”, Am. J. Math. 62 (1940), p. 738-742.
[26] V. Féray, P.-L. Méliot & A. Nikeghbali , Mod-φ convergence. Normality zones
and precise deviations , SpringerBriefs in Probability and Mathematical Statistics,
Springer, 2016.
[27] ——— , “Mod- φ convergence, II: Estimates on the speed of convergence”, in Sémi-
naire de Probabilités L , Lecture Notes in Mathematics, vol. 2252, Springer, 2019.
[28] P. Flajolet & A. M. Odlyzko , “Random mapping statistics”, in Advances in
Cryptology - EUROCRYPT 1989 , Lecture Notes in Computer Science, vol. 434,
Springer, 1990, p. 329-354.
[29] ——— , “Singularity analysis of generating functions”, SIAM J. Discrete Math. 3
(1990), no. 2, p. 216-240.
[30] P. Flajolet & R. Sedgewick , Analytic Combinatorics , Cambridge University
Press, 2009.
[31] A. J. Harper , “Two new proofs of the Erdős–Kac theorem, with bound on the rate
of convergence, by Stein’s method for distributional approximations”, Proc. Camb.
Philos. Soc. 147 (2009), no. 1, p. 95-114.
[32] H.-K. Hwang , “Large deviations for combinatorial distributions. I. Central limit
theorems”, Ann. Appl. Probab. 6 (1996), no. 1, p. 297-319.
[33] ——— , “On convergence rates in the central limit theorems for combinatorial struc-
tures”, Eur. J. Comb. 19 (1998), no. 3, p. 329-343.
[34] ——— , “Asymptotics of Poisson approximation to random discrete distributions:
an analytic approach”, Adv. Appl. Probab. 31 (1999), no. 2, p. 448-491.
[35] J. Jacod, E. Kowalski & A. Nikeghbali , “Mod-Gaussian convergence: new limit
theorems in probability and number theory”, Forum Math. 23 (2011), no. 4, p. 835-
873.
[36] Y. Jiao, N. El Karoui & D. Kurtz , “Gauss and Poisson approximations: appli-
cation to CDOs pricing”, J. Comput. Finance 12 (2008), no. 2, p. 31-58.
[37] J.-P. Kahane , Séries de Fourier absolument convergentes , Ergebnisse der Mathe-
matik und ihrer Grenzgebiete, vol. 50, Springer, 1970.
[38] S. K. Katti , “Inﬁnite divisibility of integer-valued random variables”, Ann. Math.
Stat. 38 (1967), p. 1306-1308.
[39] Y. Katznelson , An introduction to harmonic analysis , Cambridge Mathematical
Library, Cambridge University Press, 2004.
[40] J. Kerstan , “Verallgemeinerung eines Satzes von Prochorow und Le Cam”, Z.
Wahrscheinlichkeitstheor. Verw. Geb. 2 (1964), p. 173-179.
[41] E. Kowalski & A. Nikeghbali, “Mod-Poisson convergence in probability and num-
ber theory”, Int. Math. Res. Not. 18 (2010), p. 3549-3587.
[42] J. Kruopis , “Precision of approximations of the generalized binomial distribution
by convolutions of Poisson measures”, Lith. Math. J. 26 (1986), no. 1, p. 37-49.
[43] I. G. Macdonald , Symmetric functions and Hall polynomials , Oxford Mathemat-
ical Monographs, Clarendon Press, 1995.
[44] P.-L. Méliot , Representation theory of symmetric groups , Discrete Mathematics
and its Applications, CRC Press, 2017.
[45] D. J. Newman , “A simple proof of Wiener’s 1/f theorem”, Proc. Am. Math. Soc.
48 (1975), no. 1, p. 264-265.
[46] A. Nikeghbali & D. Zeindler , “The generalized weighted probability measure on
the symmetric group and the asymptotic behavior of the cycles”, Ann. Inst. Henri
Poincaré, Probab. Stat. 49 (2013), no. 4, p. 961-981.
ANNALES DE L’INSTITUT FOURIER
APPROXIMATION OF DISCRETE MEASURES 1197
[47] V. V. Petrov , Sums of independent random variables , Ergebnisse der Mathematik
und ihrer Grenzgebiete, vol. 82, Springer, 1975.
[48] E. L. Presman , “Approximation of binomial distributions by inﬁnitely divisible
ones”, Theory Probab. Appl. 28 (1983), no. 2, p. 393-403.
[49] Y. V. Prokhorov , “Asymptotic behavior of the binomial distribution”, Usp. Mat.
Nauk 8 (1953), no. 3, p. 135-142.
[50] A. Rényi & P. Turán , “On a theorem of Erdős–Kac”, Acta Arith. 4 (1958), p. 71-
84.
[51] R. C. Rhoades , “Statistics of prime divisors in function ﬁelds”, Int. J. Number
Theory 5 (2009), no. 1, p. 141-152.
[52] S. M. Samuels , “Positive-integer-valued inﬁnitely divisible distributions”, Purdue
University Technical Report, Department of Statistics, Division of Mathematical
Sciences, Mimeograph Series 406, 1975.
[53] K.-I. Sato, Lévy processes and inﬁnitely divisible Ddstributions , Cambridge Studies
in Advanced Mathematics, vol. 68, Cambridge University Press, 1999.
[54] J. M. Steele , “Le Cam’s inequality and Poisson approximations”, Am. Math. Mon.
101 (1994), no. 1, p. 48-54.
[55] F. W. Steutel & K. V an Harn, Inﬁnite divisibility of probability distributions on
the real line , Pure and Applied Mathematics, vol. 259, Marcel Dekker, 2004.
[56] G. Szegö , Orthogonal polynomials , Colloquium Publications, vol. 23, American
Mathematical Society, 1939.
[57] G. Tenenbaum , Introduction to analytic and probabilistic number theory , Cam-
bridge Studies in Advanced Mathematics, vol. 46, Cambridge University Press, 1995.
Manuscrit reçu le 19 mars 2018,
révisé le 18 mars 2019,
accepté le 18 septembre 2019.
Reda CHHAIBI
Institut de Mathématiques de Toulouse
Université Paul Sabatier
118, route de Narbonne
31062 Toulouse cedex 9 (France)
reda.chhaibi@math.univ-toulouse.fr
Freddy DELBAEN
ETH Zürich, Department of Mathematics and
Universität Zürich, Institut für Mathematik
Winterthurerstrasse 190
CH-8057 Zürich (Switzerland)
delbaen@math.ethz.ch
Pierre-Loïc MÉLIOT
Laboratoire de Mathématiques, Bâtiment 307
Faculté des sciences d’Orsay
Université Paris-Sud
91400 Orsay (France)
pierre-loic.meliot@math.u-psud.fr
Ashkan NIKEGHBALI
ETH Zürich, Department of Mathematics and
Universität Zürich, Institut für Mathematik
Winterthurerstrasse 190
CH-8057 Zürich (Switzerland)
ashkan.nikeghbali@math.uzh.ch
TOME 70 (2020), F ASCICULE 3
