---
doc_id: arxiv-1409.2849v1
doc_title: "MOD-GAUSSIAN CONVERGENCE AND ITS APPLICATIONS FOR MODELS OF STATISTICAL MECHANICS"
section_id: sec-006-33-application-to-the-curie-weiss-model
section_title: "Application to the Curie-Weiss model"
section_number: 3.3
pages: 15-17
source_pdf: 1409.2849v1.pdf
source_sha256: 7bf9646716fbb247
doc_brief: "MOD-GAUSSIAN CONVERGENCE AND ITS APPLICATIONS FOR MODELS OF STATISTICAL MECHANICS — In this paper we complete our understanding of the role played by the lim- iting (or residue) function in the"
---
ables (σ(i))i≥1 with P[σ(i) = 1] = 1− P[σ(i) = −1] = eα
2 cosh α for some α ∈ R.
We set Un = ∑n
i=1 σ(i), so that
E[ezUn] =
(cosh(z + α)
cosh α
)n
= (cosh z + sinh z tanh α)n
E
[
ez Un−n tanh α
n1/3
]
=
(
cosh(zn−1/3) + sinh(zn−1/3) tanh α
ezn−1/3 tanh α
)n
log E
[
ez Un−n tanh α
n1/3
]
= n1/3
2 cosh2 α
z2− sinh α
3 cosh3 α
z3 + o(1)
so one has complex mod-Gaussian convergence of Un−n tanh α
n1/3 with parameters n1/3
cosh2 α
and limiting function exp(− sinh α
3 cosh3 α z3).
If α = 0, then the term of order 3 disappears in the Taylor expansion of the charac-
teristic function, and one obtains instead
log E
[
ez Un
n1/4
]
= n1/2 z2
2 − z4
12 + o(1),
hence a complex mod-Gaussian convergence of Xn = Un
n1/4 with parameters n1/2 and
limiting function exp (−z4/12). Since this function restricted to R is integrable, this
leads us to the following result, which originally appeared in [EN78] (without the mod-
Gaussian interpretation):
Theorem 8. Let Xn = n−1/4 ∑n
i=1 σ(i) be a rescaled sum of centred±1 independent Bernoulli
random variables. It converges in the L1-mod-Gaussian sense, with parameters n1/2 and limit-
ing function exp(− z4
12 ). As a consequence, if Y n = n−1/4Mn is the rescaled magnetization of
16 PIERRE-LOÏC MÉLIOT AND ASHKAN NIKEGHBALI
a Curie-Weiss model CW0,1 of parameters α = 0 and β = 1, then Yn/n1/2 converges in law
to the distribution
exp(− x4
12 ) dx
∫
R exp(− x4
12 ) dx
.
Proof. The function ψn(t) is in our case
ψn(t) = e− t2n1/2
2
(
cosh t
n1/4
)n
,
and we have seen that it converges locally uniformly to ψ(t) = exp(− t4
12 ). By Scheffe’s
lemma, to obtain the L1-mod-convergence, it is sufﬁcient to prove that
∫
R ψn(t) dt con-
verges to
∫
R exp(− t4
12 ) dt. This is a simple application of Laplace’s method:
∫
R
ψn(t) dt =
∫
R
e− t2n1/2
2
(
cosh t
n1/4
)n
dt = n1/4
∫
R
(
e− u2
2 cosh u
)n
du
and the function u↦→ e− u2
2 cosh u attains its global maximum at u = 0, with a Taylor
expansion 1− u4
12 + o(u4), see Figure 2.
-4 -2 2 4
0.5
1
1.5
FIGURE 2. The function f (u) = e− u2
2 cosh u.
Then, the exponential change of measure (9) gives a probability measure on spin con-
ﬁgurations proportional to
exp
( (Yn)2
2n1/2
)
= exp
( 1
2n (Mn)2
)
,
so it is indeed the Curie-Weiss model CW0,1. □
MOD-GAUSSIAN CONVERGENCE AND APPLICATIONS FOR MODELS OF STATISTICAL MECHANICS17
It is easily seen that the proof adapts readily to the case where Bernoulli variables
are replaced by so-called pure measures, so we recover all the limit theorems stated in
[EN78, ENR80]. However, by choosing the setting of mod-Gaussian convergence, we
also obtain new limit theorems for models that do not fall in the Curie-Weiss setting.
The following result explains how it would work to replace the Bernoulli distribution
by more general ones; cf. [KNN13, Proposition 2.2].
Proposition 9. Let k≥ 2 be an integer, and let(Bn)n≥1 be a sequence of i.i.d random variables
in Lr for some r > k + 1, such that the ﬁrst k moments of B1 are the same as the corresponding
moments of the Standard Gaussian distribution. Then the sequence of random variables
(
1
n1/(k+1)
n
∑
k=1
Bk
)
n≥1
converges in the mod-Gaussian sense with parameters
tn = n(k−1)/(k+1),
and limiting function
θ(t) = e(it)k+1 ck+1
(k+1)! ,
where ck+1 denotes the (k + 1)-th cumulant of B1.
When the random variables Bn have an entire moment generating function, then one
can replace t with−it to obtain mod-Gaussian convergence with the Laplace trans-
forms. If B1 is symmetric, then k is necessarily an odd number of the form 2 s− 1 and
hence
ψ(t) = e(−1)st2s c2s
(2s)! .
In the case of the Bernoulli random variables, s = 2 and c4 =−1/12. In order to have
our theorem of L1-mod-Gaussian convergence to hold, we need to ﬁnd conditions on
the distribution of B1 such that c2s is negative and that
∫
R ψn converges to
∫
R ψ. The
conditions in [EN78] and [ENR80] precisely imply these. But within our more general
framework, following the discussion in Section 1.2, we could well imagine a situation
which fulﬁls the assumptions of Theorem 6 but where the initial symmetric random
variables are not necessarily i.i.d but simply independent or even weakly dependent.
The following paragraph yields an example of such a setting.
