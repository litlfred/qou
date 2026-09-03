---
doc_id: arxiv-1108.0687v3
doc_title: "Concentration of Lipschitz functionals of determinantal a nd other strong Rayleigh measures"
section_id: sec-003-2-strong-rayleigh-property-stochastic-covering-p
section_title: "Strong Rayleigh property, stochastic covering property, and other negative dependence conditions"
section_number: 2
pages: 4-6
source_pdf: 1108.0687v3.pdf
source_sha256: 66ba88e13a429a0a
doc_brief: "Concentration of Lipschitz functionals of determinantal a nd other strong Rayleigh measures — Let {X1,...,X n} be a collection of binary valued random variables and let f : {0, 1}n → R be a Lipschitz"
---
and other negative dependence conditions
Let [n] denote {1,...,n } and let Bn := {0, 1}n denote the Boolean lattice of rank n, with coordi-
natewise partial order. The function N : Bn → Z+ will be used throughout to denote the counting
3
function deﬁned by N (ω) := ∑ n
j=1ωj. A measure ν on Bn is said to be k-homogeneous if ν is
supported on the set of {ω :N (ω) = k}. The probability measure ν on Bn is said to be negatively
associated if
∫
fgdν ≤ (
∫
fdν )(
∫
gdν ) for every pair of nonnegative monotone functions f and g
such that for some set S ⊆ [n], the function f depends only on coordinates {ωj :j ∈S} while the
function g depends only on coordinates {ωj :j ∈Sc}.
The strong Rayleigh condition is said to hold for a measure P on Bn if the generating function
∑
ω∈Bn
P(ω)
n∏
j=1
zωj
j
has no roots ( z1,...,z n) all of whose coordinates lie in the (strict) upper half plane. This and
many consequences are given in [BBL09], including (implicitly) the stochastic covering property
(see Proposition 2.2), which was conjectured [Pem00, Conjecture 9] to follow from something a little
weaker. Some of the relevant implications are summarized in Figure 1 b elow.
The deﬁnition of the stochastic covering property requires a few p reliminary deﬁnitions. Recall
that a measure ν on a partially ordered set is said to stochastically dominate a measureρ, denoted
ν ≽ ρ, if ν(A) ≥ρ(A) for every upwardly closed set A. An equivalent condition is that there exists
a coupling, that is a measure Q on Bn × Bn with respective marginals ν and ρ, supported on the
set {(x,y ) : x ≥ y}. If P is a measure on Bn making the coordinate variables {Xi : 1 ≤ i ≤ n}
negatively associated, an immediate consequence of negative asso ciation is that the conditional
measure ( P |Xn = 0) on Bn−1 stochastically dominates the conditional measure ( P |Xn = 1).
Rayleigh
projected
homogeneous
Stochastic
Covering
Property
Negative
Association
Negative
Cylinder
Dependence
Rayleigh
Strong
Figure 1: relations among negative dependence properties
We say that the probability measure ν on Bn stochastically covers another probability measure
ρ if there is a measure on B2
n with ﬁrst marginal ν and second marginal ρ (in other words, a coupling)
supported on the set of pairs ( x,y ) for which x =y orx coversy in the coordinatewise partial order;
here x is said to cover y when x>y but there is no z such that x>z >y . We denote the covering
relation in Bn by x ·>y , and one measure covering another by ν⊲ρ . Stochastic covering is strictly
stronger than stochastic domination, and may be thought of as “s tochastic domination, but by at
most 1”.
Stochastic covering combines stochastic ordering with closeness in the so-calledL∞-transportation
metric, deﬁned on probability measures on a given metric space as fo llows: d∞(µ,ν ) is the least ρ
such that there is a coupling of µ andν supported on the set {(x,y ) : |x −y| ≤ ρ}. Thus µ⊲ν implies
4
d∞(µ,ν ) ≤ 1. This is useful because if ||f ||Lip denotes the Lipschitz norm on Lipschitz functions,
then ⏐⏐⏐⏐
∫
fdµ −
∫
fdν
⏐⏐⏐⏐ ≤ ||f ||Lip d∞(µ,ν ). (2.7)
Suppose that x ≥ y and we compare the conditional laws Px := ( P |Xj = xj,j ∈ S) and
Py := (P |Xj =yj,j ∈S) on the remaining coordinates, that is as laws on {0, 1}Sc
. If P and all its
conditionalizations are negatively associated, it follows that Px ≼ Py.
Deﬁnition 2.1 (stochastic covering property) . We say that a probability measure ν on Bn has the
stochastic covering property if for every S ⊆ {1,...,n } and for every x,y ∈ {0, 1}S with x ·>y , the
conditional law (ν |Xj =xj,j ∈S) is covered by the conditional law (ν |Xj =yj,j ∈S).
In [BBL09, Theorem 4.2] it was shown that strong Rayleigh property implies the projected
homogeneous Rayleigh property (PHR), meaning that the measure can be embedded as th e ﬁrst
n coordinates of a homogeneous measure ν′ on Bm, for some m ≥n, that has the ordinary Rayleigh
property; the ordinary Rayleigh property is that the partial deriv atives of the generating function
F (z1,...,z n) := E∏ n
j=1zXj
j satisfy FiFj ≥ FijF at any point with positive real coordinates. We
record two further consequences.
Proposition 2.2. PHR (and hence strong Rayleigh) implies the stochastic cove ring property.
Proof: PHR implies negative association of all conditionalizations (CNA) [BBL09 , Theorem 4.10];
the homogeneous extensionν′ witnessing the PHR property is also PHR hence also CNA. By negative
association, if x ·>y then (ν′ |Xj =yj,j ∈S) ≽ (ν′ |Xj =xj,j ∈S), when viewed as measures on
the coordinates in [ m] \S. Because ν′ is homogeneous, the coupling that witnesses this ≽ relation
in fact witnesses the relation ⊲. Restricting to [ n] \S we see that ( ν |Xj = yj,j ∈ S)⊲ (ν |Xj =
xj,j ∈S). □
Proposition 2.3 ([BBL09, Theorem 4.19]) . Let P be a strong Rayleigh measure on Bn. Let Pk
denote P conditioned onN =k. Then for every 0 ≤k ≤n − 1 such that P(N =k) and P(N =k + 1)
are both nonzero, we have the covering relation Pk+1⊲ Pk. □
