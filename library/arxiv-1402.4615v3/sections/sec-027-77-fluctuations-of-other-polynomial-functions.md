---
doc_id: arxiv-1402.4615v3
doc_title: "GAUSSIAN FLUCTUATIONS OF YOUNG DIAGRAMS AND STRUCTURE CONSTANTS OF JACK CHARACTERS"
section_id: sec-027-77-fluctuations-of-other-polynomial-functions
section_title: "Fluctuations of other polynomial functions"
section_number: 7.7
pages: 53-54
source_pdf: 1402.4615v3.pdf
source_sha256: b6e7c795cd1a7cd2
doc_brief: "GAUSSIAN FLUCTUATIONS OF YOUNG DIAGRAMS AND STRUCTURE CONSTANTS OF JACK CHARACTERS — In this paper, we consider a deformation of Plancherel meas ure linked to Jack polynomials."
---
sis of polynomial functions, Theorem 1.2 implies that any po lynomial function F
converge, after proper normalization, towards a multivariate polynomial evaluated
in independent Gaussian variables.
However, the proper order of normalization and the actual po lynomial are not
easy to be expressed explicitly, as this relies on the expans ion of F in the Ch(k)
basis. In particular, we are not able to do it for Chµ, when µ is not a hook and
hence we can not describe the ﬂuctuations of these random variables as it was done
in the case α = 1; see [Hor98] and [IO02, Theorem 6.5].
8. J ACK MEASURE : CENTRAL LIMIT THEOREMS FOR YOUNG DIAGRAMS AND
TRANSITION MEASURES
In this section, we state formally and prove our ﬂuctuation r esults for Young
diagrams under Jack measure. We will also present a ﬂuctuati on result for the
transition measures of these diagrams.
Before we state our results, we need some preparations. We fo llow here nota-
tions from [IO02, Sections 7 and 8]. First, we deﬁne
uk(x) = Uk(x/2) =
∑
0≤j≤⌊k/2⌋
(−1)j
(k − j
j
)
xk−2j,
tk(x) = 2 Tk(x/2) =
∑
0≤j≤⌊k/2⌋
(−1)j k
k − j
(k − j
j
)
xk−2j,
where Tk and Uk are respectively Chebyshev polynomials of the ﬁrst and seco nd
kind. They can be alternatively deﬁned by the following equations:
uk(2 cos(θ)) = sin((k + 1)θ)
sin(θ) ;
tk(2 cos(θ)) = 2 cos( kθ).
It is known that (uk(x))k and (tk(x))k form a family of orthonormal polynomials
with respect to the measures
√
4−x2
2π dx and 1
2π
√
4−x2 dx, respectively, i. e.:
∫ 2
−2
uk(x)ul(x)
√
4 − x2
2π dx = δk,l;
∫ 2
−2
tk(x)tl(x) 1
2π
√
4 − x2 dx = δk,l.
The measure
√
4−x2
2π dx supported on the interval [−2, 2] is called the semi-circular
distribution and is denoted by the µS−C (see Subsection 1.1).
Recall from Theorem 1.1 that the limit shape of scaled Young diagrams
ω
(
D1/√n
(
Aα(λ(n))
) )
is given by Ω , where λ(n) is a random Young diagram with n boxes distributed
according to Jack measure. Hence, in order to study ﬂuctuati ons of the random
54 M. DOŁ ˛ EGA AND V . FÉRAY
Young diagrams around the limit shape, we introduce the foll owing application
from the set of Young diagrams to the space of functions from R to R:
∆ (α)(λ)(x) := √
n
ω
(
D1/√n
(
Aα(λ)
) )
(x) − Ω( x)
2 ,
where n is the number of boxes of λ.
Besides, tt was shown by Kerov [Ker93a] that the transition m easure (see Sub-
section 2.2) of the continuous Young diagram Ω is the semi-circular distribution
(see Subsection 1.1). Thus we deﬁne the following function o n the set of Young
diagrams with n boxes with values in the space of real signed measures:
ˆ∆ (α)(λ) := √n


µ(
D1/√
n
(
Aα(λ)
) ) − µS−C


 .
As above, n is the number of boxes of λ. This function describes the (scaled)
difference between the transition measure of the scaled You ng diagram and the
limiting semi-circular measure.
Now, we are ready to formulate the central limit theorem for t he Jack measure.
Here, we use the usual notation [condition] for the indicator function of the corre-
sponding condition.
Theorem 8.1. Choose a sequence (Ξ k)k=2,3,... of independent standard Gaussian
random variables and let λ(n) be a random Young diagram of size n distributed
according to Jack measure. As n → ∞, we have
(1) a central limit theorem for Young diagrams:
(
u(α)
k (λ(n))
)
k=1,2,...
d− →
( Ξ k+1
√
k + 1 − γ
k + 1 [k is odd]
)
k=1,2,...
,
where u(α)
k (λ) =
∫
R uk(x)∆ (α)(λ)(x) dx;
(2) and a central limit theorem for transition measures:
(
t(α)
k (λ(n))
)
k=3,4,...
d− →
(√
k − 1 Ξ k−1 − γ [k is odd]
)
k=3,4,...
,
where t(α)
k (λ) =
∫
R tk(x)ˆ∆ (α)(λ)(dx).
Remark. Notice that, for γ = 0 (i.e. α = 1 ), this theorem specializes to Kerov’s
central limit theorems for Plancherel measure [Ker93a, IO02].
