---
doc_id: arxiv-hep-th-9310070v1
doc_title: "September, 1993 Quantum Dilogarithm"
section_id: sec-001-1-introduction
section_title: "Introduction"
section_number: 1
pages: 2-3
source_pdf: 9310070v1.pdf
source_sha256: b979ebf2f47a4653
doc_brief: "September, 1993 Quantum Dilogarithm — A quantum generalization of Rogers’ ﬁve term, or “pentagon” dilogarithm identity is suggested. It is shown that the classical limit gives usua l Rogers’ identity."
---
Recently, the dilogarithm function appeared in the study of the two dimensional quantum
conformal ﬁeld theory (CFT)[1] and solvable lattice models both in two [2] and three
dimensions [3]. Particularly, the eﬀective central charge s of some rational CFT can be
expressed as ﬁnite sums of Rogers’ dilogarithm function wit h the arguments being solutions
for certain algebraic relations (e. g. thermodynamical Bet he anzats relations).
People use the dilogarithm function in two forms, L2(x) and L(x), introduced by
Euler and Rogers, respectively. Euler’s dilogarithm for an y complex x can be deﬁned by
the following integral:
L2(x) = −
∫ x
0
log(1 − z)
z dz, (1.1)
while Rogers’ diﬀers by the addition of an elementary functi on
L(x) = L2(x) + log(1 − x) log(x)/2. (1.2)
Among the various properties of these functions the most pro found one is (probably) the
ﬁve term or “pentagon” identity for L(x), proved by Rogers [4]:
L(x) + L(y) − L(xy) = L( x − xy
1 − xy ) + L( y − xy
1 − xy ), (1.3a)
which in terms of Euler’s dilogarithm looks like
L2(x) + L2(y) − L2(xy) = L2( x − xy
1 − xy ) + L2( y − xy
1 − xy ) + log( 1 − x
1 − xy ) log( 1 − y
1 − xy ). (1.3b)
On the other hand, in the context of integrable lattice quant um ﬁeld theory models
and quantum groups the problem of constructing of the Viraso ro algebra on the lattice has
been suggested and partially solved [5], [6]. The following transcendental function plays
the signiﬁcant role in the latter:
Ψ( x) =
∞∏
n=1
(1 − xθn), |θ| < 1, (1.4)
where x is any complex variable and θ, a ﬁxed complex parameter, lies within a unit
disk⋆. Considering θ as a quantization parameter, the function Ψ( x) can be interpreted as
a “quantum” Euler’s dilogarithm in the following sense. Let θ = exp(ǫ) for Re( ǫ) < 0 and
perform the limit ǫ → 0. Then, it is easy to see that
Ψ( x) = 1√1 − x exp(L2(x)/ǫ)(1 + O(ǫ)). (1.5)
⋆ In [6] this function has been deﬁned using a slightly diﬀeren t argument and denoted
as S(x), with θ being q2 of [6]. In fact, the precise relation between the two deﬁniti ons is
Ψ( x) = S(−θ1/2x).
1
Motivated by relation (1.5) we address the following proble m: What is the proper general-
ization of Rogers’ “pentagon” identity (1.3) in terms of Ψ( x)? The purpose of this paper
is to answer this question.
In Section 2 a quantized “pentagon” identity is suggested an d it is shown that in the
classical limit it is reduced to (1.3). In Section 3 the case w here θ is a root of unity is
considered. The quantum dilogarithm for such a θ is a function on Fermat curve, while
the classical limit of the “pentagon” identity again gives ( 1.3). In the summary the main
formulae are enumerated with a little discussion.
