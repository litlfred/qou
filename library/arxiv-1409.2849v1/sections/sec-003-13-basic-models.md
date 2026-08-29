---
doc_id: arxiv-1409.2849v1
doc_title: "MOD-GAUSSIAN CONVERGENCE AND ITS APPLICATIONS FOR MODELS OF STATISTICAL MECHANICS"
section_id: sec-003-13-basic-models
section_title: "Basic models"
section_number: 1.3
pages: 7-11
source_pdf: 1409.2849v1.pdf
source_sha256: 7bf9646716fbb247
doc_brief: "MOD-GAUSSIAN CONVERGENCE AND ITS APPLICATIONS FOR MODELS OF STATISTICAL MECHANICS — In this paper we complete our understanding of the role played by the lim- iting (or residue) function in the"
---
nomenon of mod-Gaussian convergence for probabilistic models stemming from sta-
tistical mechanics; this extends the already long list of models for which we were able
to establish this asymptotic behavior of the Fourier or Laplace transforms ([JKN11,
KN12, FMN13]). More precisely, we shall focus on one-dimensional spin conﬁgura-
tions, which already yield an interesting illustration of the theory and technics of mod-
Gaussian convergence. Given two parameters α∈ R and β∈ R+, we recall that the
Curie-Weiss model and the one-dimensional Ising model are the probability laws on
spin conﬁgurations σ : [ [1, n] ]→{± 1} given by
CWα,β(σ) = 1
Zn(CW, α, β) exp

α
n
∑
i=1
σ(i) + β
2n
(
n
∑
i=1
σ(i)
)2
 ; (7)
Iα,β(σ) = 1
Zn(I, α, β) exp
(
α
n
∑
i=1
σ(i) + β
(
n−1
∑
i=1
σ(i) σ(i + 1)
))
. (8)
The coefﬁcient α measures the strength and direction of the exterior magnetic ﬁeld,
whereas β measures the strength of the interaction between spins, which tend to align
in the same direction. This interaction is local for the Ising model, and global for the
Curie-Weiss model. Set Mn = ∑n
i=1 σ(i): this is the total magnetization of the system,
and a random variable under the probabilities CWα,β and Iα,β.
In Section 2, we quickly establish the mod-Gaussian convergence of the magnetiza-
tion for the Ising model, using the explicit form of the Laplace transform of the mag-
netization, which is given by the transfer matrix method. Alternatively, when α = 0,
in the appendix, we apply the cumulant method and give an explicit formula for each
elementary cumulant of spins (see Section 5). This allows us to prove the analogue
for joint cumulants of the well-known fact that covariances between spins decrease
exponentially with distance in the 1D-Ising model. This second method is much less
direct than the transfer matrix method, but we consider the Ising model to be a very
good illustration of the method of joint cumulants. Moreover it illustrates the fact that
one does not necessarily need to be able to compute precisely the moment generating
function of the random variables.
In Section 3, we focus on the Curie-Weiss model, and we interpret the magnetiza-
tion as a change of measure on a sum of i.i.d. random variables. Since these sums
converge in the mod-Gaussian sense, it leads us to study the effect of a change of
measure on a mod-Gaussian convergent sequence. We prove that in the setting of
8 PIERRE-LOÏC MÉLIOT AND ASHKAN NIKEGHBALI
L1-mod-Gaussian convergence, such changes of measures either conserve the mod-
Gaussian convergence (with different parameters), or lead to a convergence in law,
with a limiting distribution that involves the residue ψ. We thus recover the results
of [EN78, ENR80], and extend them to the setting of L 1-mod-Gaussian convergence.
In Section 4, using Fourier analytic arguments, we quickly recover the optimal rate
of convergence of the Ellis-Newman limit theorem for the Curie-Weiss model which
was recently obtained in [EL10] using Stein’s method, and then we establish a local
limit theorem, thus completing the existing limit theorems for the Curie-Weiss model
at critical temperature CW0,1.
2. M OD-GAUSSIAN CONVERGENCE FOR THE ISING MODEL :
THE TRANSFER MATRIX METHOD
In this section, (σ(i))i∈[ [1,n] ]is a random conﬁguration of spins under the Ising mea-
sure (8), and Mn = ∑n
i=1 σ(i) is its magnetization. The mod-Gaussian convergence of
Mn after appropriate rescaling can be obtained by two different methods: the transfer
matrix method, which yields an explicit formula for E[ezMn]; and the cumulant method,
which gives an explicit combinatorial formula for the coefﬁcients of the power series
log E[ezMn]. We use here the transfer matrix method, and refer to the appendix (Section
5) for the cumulant method.
1
FIGURE 1. Two conﬁgurations of spins under the Ising measures of pa-
rameters (α = 0, β = 0.3) and (α = 0, β = 1).
The Laplace transform E[ezMn] of the magnetization of the one-dimensional Ising
model is well-known to be computable by the following transfert matrix method, see
[Bax82, Chapter 2]. Introduce the matrix
T =
(
eα+β e−α−β
eα−β e−α+β
)
,
and the two vectors V = ( eα, e−α) and W = ( 1
1 ). If the rows and columns of T cor-
respond to the two signs +1 and−1, then any conﬁguration of spins σ = ( σ(i))i∈[ [1,n] ]
has under the Ising measure Iα,β a probability proportional to
Vσ(1)Tσ(1),σ(2)Tσ(2),σ(3)··· Tσ(n−1),σ(n).
Therefore, the partition function Zn(I, α, β) is given by
∑
σ(1),...,σ(n)
Vσ(1)Tσ(1),σ(2)Tσ(2),σ(3)··· Tσ(n−1),σ(n) = V(T)n−1W
= a+(λ+)n−1 + a−(λ−)n−1,
MOD-GAUSSIAN CONVERGENCE AND APPLICATIONS FOR MODELS OF STATISTICAL MECHANICS 9
where
a+ = cosh α + eβ sinh2 α + e−β
√
e2β sinh2 α + e−2β
; a− = cosh α− eβ sinh2 α + e−β
√
e2β sinh2 α + e−2β
λ+ = eβ cosh α +
√
e2β sinh2 α + e−2β ; λ− = eβ cosh α−
√
e2β sinh2 α + e−2β.
Indeed, λ± are the two eigenvalues of T, and a+ and a− are obtained by identiﬁcation
of coefﬁcients in the two formulas
Z1(I, α, β) = eα + e−α
Z2(I, α, β) = e2α+β + e−2α+β + 2e−β.
Then, the Laplace transform of Mn is given by
Eα,β[ezMn] = Zn(I, α + z, β)
Zn(I, α, β) .
In particular,
Eα,β[Mn] = ∂E[ezMn]
∂z
⏐⏐⏐⏐
z=0
= ∂
∂α log Zn(I, α, β) = n eβ sinh α√
e2β sinh2 α + e−2β
+ O(1).
whence a formula for the (asymptotic) mean magnetization by spin:
m = eβ sinh α√
e2β sinh2 α + e−2β
.
A more precise Taylor expansion of Zn(I, α + z, β) leads to the following:
Theorem 3. Under the Ising measure Iα,β, Mn−nm
n1/3 converges in the complex mod-Gaussian
sense with parameters
tn = n1/3 e−β cosh α
(e2β sinh2 α + e−2β)3/2
and limiting function
ψ(z) = exp
(
−2eβ sinh3 α + (3eβ− e−3β) sinh α
6(e2β sinh2 α + e−2β)5/2 z3
)
.
Proof. In the following, we are dealing with square roots and logarithms of complex
numbers, but each time in a neighborhood ofR∗+, so there is no ambiguity in the choice
of the branches of these functions. That said, it is easier to work with log-Laplace
10 PIERRE-LOÏC MÉLIOT AND ASHKAN NIKEGHBALI
transforms:
log E
[
ez Mn−nm
n1/3
]
= log Zn
(
I, α + z
n1/3 , β
)
− log Zn(I, α, β)− zn2/3m
log Zn(I, α, β) = log a+(α, β) + (n− 1) log λ+(α, β) + o(1)
log Zn
(
I, α + z
n1/3 , β
)
= log a+
(
α + z
n1/3 , β
)
+ (n− 1) log λ+
(
α + z
n1/3 , β
)
+ o(1)
= log a+(α, β) + (n− 1) log λ+(α, β) + zn2/3 ∂
∂α (log λ+(α, β))
+ z2n1/3
2
∂2
∂α2 (log λ+(α, β)) + z3
6
∂3
∂α3 (log λ+(α, β)) + o(1).
Thus, it sufﬁces to compute the ﬁrst derivatives of log λ+(α, β) with respect to α:
log λ+(α, β) = log
(
eβ cosh α +
√
e2β sinh2 α + e−2β
)
∂
∂α (log λ+(α, β)) = eβ sinh α√
e2β sinh2 α + e−2β
= m
∂2
∂α2 (log λ+(α, β)) = e−β cosh α
(e2β sinh2 α + e−2β)3/2 = σ2
∂3
∂α3 (log λ+(α, β)) =−2eβ sinh3 α + (3eβ− e−3β) sinh α
(e2β sinh2 α + e−2β)5/2 = K3.
We therefore get
log E
[
ez Mn−nm
n1/3
]
= n1/3 σ2 z2
2 + K3 z3
6 + o(1).
□
By using Formula 2, this result leads to new estimates of moderate deviations for the
probability Pα,β[Mn≥ nm + n1/3x]. In the special case when α = 0, the limiting func-
tion ψ(z) of Theorem 3 is equal to 1, and one has to push the expansion of logZn(I, 0, β)
to order 4 to get a meaningful mod-Gaussian convergence (the same phenomenon will
occur in the case of the Curie-Weiss model):
Theorem 4. Under the Ising measure I0,β, Mn
n1/4 converges in the complex mod-Gaussian sense
with parameters tn = n1/2 e2β and limiting function
ψ(z) = exp
(
−3e6β− e2β
24 z4
)
.
MOD-GAUSSIAN CONVERGENCE AND APPLICATIONS FOR MODELS OF STATISTICAL MECHANICS11
3. M OD-GAUSSIAN CONVERGENCE IN L1 AND THE CURIE -WEISS MODEL
In this Section, (Xn)n∈N is a sequence of random variables with entire moment gen-
erating series E[ezXn], and we assume the following:
(A) One has mod-Gaussian convergence of the Laplace transforms, i.e., there is a se-
quence tn→ +∞ and a function ψ continuous on R such that
ψn(t) = E[etXn] e− tn t2
2
converges locally uniformly on R to ψ(t).
(B) Each function ψn, and their limit ψ are in L1(R).
We denote Pn the law of Xn,
Qn[dx] = e
x2
2tn
E
[
e
(Xn)2
2tn
] Pn[dx], (9)
and Yn a random variable under the new lawQn. Note that hypothesis (B) implies that
Zn = E[e(Xn)2/2tn] is ﬁnite for all n∈ N. Indeed,
∫
R
ψn(t) dt = E
[∫
R
etXn− tn t2
2 dt
]
= E
[
e
(Xn)2
2tn
(∫
R
e− (Xn−tnt)2
2tn dt
)]
=
√
2π
tn
E
[
e
(Xn)2
2tn
]
.
Therefore the new probability measures Qn are well deﬁned. The goal of this section
is to study the asymptotics of the new sequence (Yn)n∈N. As we shall see in §3.3,
the Curie-Weiss model deﬁned by Equation (7) is one of the main examples in this
framework. However, it is more convenient to look at the general problem, and we
shall introduce later other models concerned by our general results.
