---
doc_id: arxiv-1409.2849v1
doc_title: "MOD-GAUSSIAN CONVERGENCE AND ITS APPLICATIONS FOR MODELS OF STATISTICAL MECHANICS"
section_id: sec-008-35-sub-critical-changes-of-measures
section_title: "Sub-critical changes of measures"
section_number: 3.5
pages: 19-20
source_pdf: 1409.2849v1.pdf
source_sha256: 7bf9646716fbb247
doc_brief: "MOD-GAUSSIAN CONVERGENCE AND ITS APPLICATIONS FOR MODELS OF STATISTICAL MECHANICS — In this paper we complete our understanding of the role played by the lim- iting (or residue) function in the"
---
may ask what happens if instead of β and 1
e2β one puts arbitrary coefﬁcients for the
local and the global interaction. More generally, given a sequence (Xn)n∈N that con-
verges in the L1-mod-Gaussian sense with parameters tn and limiting function ψ, one
can look at the change of measure
Q(γ)
n [dx] = e
γx2
2tn
E
[
e
γ(Xn)2
2tn
] Pn[dx]
with γ∈ (0, 1) (for γ > 1, the change of measure is not necessarily well-deﬁned, since
the hypotheses (A) and (B) do not ensure that E[eγ(Xn)2/2tn] < +∞). These subcritical
changes of measures do not modify the order of magnitude of the ﬂuctuations of Xn,
and more precisely:
Theorem 10. Suppose that (Xn)n∈N converges in the L1-mod-Gaussian sense with parame-
ters tn and limiting function ψ. Then, if (X(γ)
n )n∈N is a sequence of random variables under
the new probability measuresQ(γ)
n , it converges in theL1-mod-Gaussian sense with parameters
(1− γ)tn and limit ψ.
Example. Consider a random conﬁguration of spins σ on [ [1, n] ]with probability pro-
portional to
exp

β
(
n−1
∑
i=1
σ(i)σ(i + 1)
)
+ γ
2n
(
n
∑
i=1
σ(i)
)2
 ,
with γ < e−2β. The total magnetization of the system has order of magnitude n1/2,
and more precisely, one has the central limit theorem
Mn
n1/2 ⇀n→∞N (0, (1− γe2β)e2β),
and in fact a L1-mod-Gaussian convergence of Mn
n1/4 , with a limiting function
ψ(x) = exp(−(3e6β− e2β) x4/24)
that does not depend on γ.
Proof of Theorem 10. We denote as before (Yn)n∈N a sequence of random variables un-
der the laws Qn = Q(1)
n . We ﬁrst compute the asymptotics of Z(γ)
n = E[eγ(Xn)2/2tn]:
Z(γ)
n = Zn E[e−(1−γ)(Yn)2/2tn]
20 PIERRE-LOÏC MÉLIOT AND ASHKAN NIKEGHBALI
=
√
tn
2π
(∫
R
ψ(x) dx
)
E
[
e− tn(1−γ)
2 ( Yn
tn )2
]
(1 + o(1))
=
√
tn
2π
(∫
R
ψ(x) dx
)
E
[
e− tn(1−γ)
2 (Wn)2
]
(1 + o(1))
=
√
1
1− γ (1 + o(1))
by using on the third line the same argument as in the proof of Proposition 7 to replace
Yn
tn by Wn; and by using the Laplace method on the fourth line in order to compute∫
R e−tn(1−γ)x2/2 ψn(x) dx. The same computations give the asymptotics of
E[etXn+γ(Xn)2/2tn] = Zn E[etYn−(1−γ)(Yn)2/2tn]
=
√
tn
2π
(∫
R
ψ(x) dx
)
E
[
etnt ( Yn
tn )− tn(1−γ)
2 ( Yn
tn )2
]
(1 + o(1))
=
√
tn
2π
(∫
R
ψ(x) dx
)
E
[
etnt Wn− tn(1−γ)
2 (Wn)2
]
(1 + o(1))
= e− tnt2
2(1−γ)
√
1
1− γ ψ(t) (1 + o(1))
with again a Laplace method on the fourth line. Since
E[etX (γ)
n ] = E[etXn+γ(Xn)2/2tn]
Z(γ)
n
,
this shows the hypotheses (A) and (B) for the sequence(X(γ)
n )n∈N. Then, since ( Yn
tn )n∈N
converges in law, by using the implication (ii) ⇒ (iii) in Theorem 6 for the sequence
(X(γ)
n )n∈N, we see that the mod-Gaussian convergence of Laplace transforms neces-
sarily happens in L1(R). □
