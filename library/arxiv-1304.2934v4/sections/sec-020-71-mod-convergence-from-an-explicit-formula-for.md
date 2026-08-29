---
doc_id: arxiv-1304.2934v4
doc_title: "MOD-φ CONVERGENCE, I:"
section_id: sec-020-71-mod-convergence-from-an-explicit-formula-for
section_title: "Mod-convergence from an explicit formula for the Laplace transform"
section_number: 7.1
pages: 48-50
source_pdf: 1304.2934v4.pdf
source_sha256: b7ed2a9e85264568
doc_brief: "MOD-φ CONVERGENCE, I: — In this paper, we use the framework of mod- φ convergence to prove pre- cise large or moderate deviations for quite general sequences of real valued random variables (Xn)n∈N"
---
where mod-convergence is proved using an explicit formula for the Laplace transform
were already given in Section 2.1. We provide here two additional examples of mod-
Gaussian convergence that can be obtained by this method.
Example 7.1. Let f (z) = ∑∞
n=0 an zn be a random analytic function, where the coefﬁ-
cients an are independent standard complex Gaussian variables. The random func-
tion f has almost surely its radius of convergence equal to 1, and its set of zeroes
Z ( f ) = {z ∈ D(0,1)| f (z) = 0} is a determinantal point process on the unit disk,
with kernel
K(w, z) = 1
π(1− wz)2 = 1
π
∞
∑
k=1
k(wz)k−1.
We refer to [HKPV09] for precisions on these results. It follows then from the gen-
eral theory of determinantal point processes, and the radial invariance of the kernel,
MOD-φ CONVERGENCE, I 49
that the number Nr of points of Z ( f )∩ B(0,r) can be represented in law as a sum of
independent Bernoulli variables of parameters{r2k}k≥1:
Nr = card{z∈Z ( f )|| z|≤ r} =law
∞
∑
k=1
B(r2k).
This representation as a sum of independent variables allows one to estimate the mo-
ment generating function of Nr under various renormalizations. Let us introduce the
hyperbolic area
h = 4π r2
1− r2
ofD(0,r), and denote Nr = Nh; we are interested in the asymptotic behavior of Nh as h
goes to inﬁnity, or equivalently as r goes to 1. Since E[ezNr ] = ∏∞
k=1(1 + r2k(ez− 1)),
one has
log
(
E
[
e
zNh
h1/3
])
=
∞
∑
k=1
log
(
1 + r2k
(
e
z
h1/3− 1
))
= h2/3z
4π + h1/3z2
16π + z3
144π + o(1)
with a remainder that is uniform when z stays in a compact domain of C. Therefore,
Nh− h
4π
h1/3 converges mod-Gaussian with
{
parameters th = h1/3
8π ,
limiting function ψ(z) = exp
(
z3
144π
)
.
Again, the limiting function is the exponential of a simple monomial. By Proposition
4.14,
Xh = Nh− h
4π√
h
8π
converges as h→ ∞ to a Gaussian law, with normality zone o(h1/6). Moreover, by
Theorem 4.3, at the edge of this normality zone,
P
[
Nh− h
4π≥ h2/3
4π x
]
= e− h1/3 x2
4π
h1/6 x exp
( x3
18π
)
(1 + o(1))
for any x > 0.
Example 7.2. Consider the Ising model on the discrete torus Z/nZ. Thus, we give to
each spin conﬁguration σ : Z/nZ→{± 1} a probability proportional to the factor
exp(−β ∑i∼j 1 σ(i)⁄=σ(j)), the sum running over neighbors in the circular graph Z/nZ.
The technique of the transfer matrix (see [Bax82, Chapter 2]) ensures that if Mn =
∑n
i=1 σ(i) is the total magnetization of the model, then
E[ezMn] = tr (T(z))n
tr (T(0))n , where T(z) =
(
e−z ez−β
e−z−β ez
)
.
The two eigenvalues ofT(z) are coshz±
√
(sinh z)2 + e−2β, and their Taylor expansion
shows that
log
(
E
[
e
zMn
n1/4
])
= eβ n1/2 z2
2 − (3e3β− eβ) z4
24 + o(1).
50 VALENTIN FÉRAY, PIERRE-LOÏC MÉLIOT, AND ASHKAN NIKEGHBALI
So, one has mod-Gaussian convergence for n−1/4 Mn, and the estimates
P[Mn≥ n3/4x] = e− n1/2 eβ x2
2
x
√
2πn1/2
exp
(
− (3e3β− eβ) x4
24
)
(1 + o(1)).
In particular, Mn
n1/2 eβ/2 satisﬁes a central limit theorem with normality zone o(n1/4).
Remark 7.3. If instead of Z/nZ we consider the graph 1 ↔ 2↔···↔ n (i.e., one
removes the link n ↔ 1), then one can realize the spins σ(i) of the Ising model as
the n ﬁrst states of a Markov chain with space of states {±1}. The magnetization Mn
appears then as a linear functional of the empirical measure of this Markov chain. More
generally, if Sn = ∑n
i=1 f (Xi) is a linear functional of a Markov chain on a ﬁnite space,
then under mild hypotheses this sum satisﬁes the Markov chain central limit theorem
(cf. for instance [Cog72]). In [FMN15a], we shall use arguments of the perturbation
theory of operators in order to prove that one also has mod-Gaussian convergence for
such linear functionals of Markov chains.
