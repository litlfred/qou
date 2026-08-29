---
doc_id: arxiv-1705.10485v2
doc_title: "Mod-φ convergence, II: Estimates on the speed of convergence"
section_id: sec-042-41-cumulants-zone-of-control-and-kolmogorov-boun
section_title: "Cumulants, zone of control and Kolmogorov bound"
section_number: 4.1
pages: 28-30
source_pdf: 1705.10485v2.pdf
source_sha256: b33759def53c6a43
doc_brief: "Mod-φ convergence, II: Estimates on the speed of convergence — In this paper, we give estimates for the speed of convergence towards a limiting stable law in the recently introduced setting of mod-φ"
---
In this section, we will see that appropriate bounds on the cumulants of a sequence of random variables
(Sn)n∈N imply the existence of a large zone of control for a renormalized version ofSn. In this whole
section and in the next one, the reference stable law is thestandard Gaussian law.We also assume that
the random variablesSn are centered.
Let us ﬁrst recall the deﬁnition of cumulants. IfX is a real-valued random variable with exponential
generating function
E[ezX] =
∞∑
r=0
E[Xr]
r! zr
convergent in a neighborhood of 0, then its cumulants κ(1)(X),κ (2)(X),... are the coeﬃcients of the
series
log E[ezX] =
∞∑
r=1
κ(r)(X)
r! zr,
which is also well deﬁned forz in a neighborhood of0 (see for instance [LS59]). For example,κ(1)(X) =
E[X], κ(2)(X) = E[X2]− E[X]2 = Var(X), and
κ(3)(X) = E[X3]− 3 E[X2] E[X] + 2E[X]3.
We are interested in the case where cumulants can be bounded in an appropriate way.
Deﬁnition 28.Let (Sn)n∈N be a sequence of (centered) real-valued random variables. We say that
(Sn)n∈N admits uniform bounds on cumulantswith parameters (Dn,Nn,A ) if, for anyr≥ 2, we have
|κ(r)(Sn)|≤ Nnrr−2 (2Dn)r−1Ar.
In the following, it will be convenient to set(~σn)2 = Var(Sn)
NnDn
. The inequality of Deﬁnition 28 withr = 2
gives (~σn)2≤ 2A2.
Lemma 29.Let (Sn)n∈N be a sequence with uniform bounds on cumulants with parameters(Dn,Nn,A ).
Set
Xn = Sn
(Nn)1/3 (Dn)2/3 and tn = (~σn)2(Nn
Dn
)1/3 = Var(Xn).
Then, we have for(Xn)n∈N a zone of control[−Ktn, Ktn] of index (3, 3), with the following constants:
K = 1
(8 + 4e)A3, K 1 =K2 = (2 + e)A3.
Proof. From the deﬁnition of cumulants, sinceXn is centered and has variancetn, we can write
Mod-φ convergence, II: Estimates on the speed of convergence 29
θn(ξ) = E[eiξXn] exp
(tnξ2
2
)
= exp
(∞∑
r=3
κ(r)(Sn)
r!
(iξ)r
(Nn(Dn)2)r/3
)
= exp(z),
with
|z|≤ 1
2
Nn
Dn
∞∑
r=3
rr−2
err!
((Dn
Nn
)1/3
2eA|ξ|
)r
.
We sety = (Dn
Nn
)1/3 2eA|ξ| and suppose thaty≤ 1, that is to say thatξ∈ [−L (Nn
Dn
)1/3, L(Nn
Dn
)1/3] with
L = 1
2eA.
By Stirling’s bound, the seriesS(y) =∑∞
r=3
rr−2
r! er yr is convergent for anyy∈ [0, 1], and we have the
inequalityS(y)≤ y3
2e3 (1−y), which implies
|z|≤ 2 (A|ξ|)3
1−
(
Dn
Nn
)1/3
2eA|ξ|
.
We now consider the zone of control[−Ktn,Ktn] with K = 1
(4e+8)A3. Ifξ is in this zone, then we have
indeed
|ξ|≤ (~σn)2
4eA3
(Nn
Dn
)1/3
≤ 1
2eA
(Nn
Dn
)1/3
=L
(Nn
Dn
)1/3
by using the remark just before the lemma. Then,
|z|≤ 2A3
1− 2eA (~σn)2
(4e+8)A3
|ξ|3≤ 2A3
1− e
e+2
|ξ|3 = (2 + e)A3|ξ|3.
Thus, on the zone of control,|θn(ξ)− 1| =|ez− 1|≤| z| e|z|, whence a control of index(3, 3) and with
constants
K1 =K2 = (2 + e)A3.
We have chosenK so thatK = 1
4K2
, hence, the inequalities of Condition (Z2) are satisﬁed. ⊓ ⊔
Using the results of Section 2, we obtain:
Corollary 30.Let Sn be a sequence with a uniform bounds on cumulants with parameters(Dn,Nn,A )
and letYn = Sn√
Var(Sn)
. Then we have
dKol(Yn,NR(0, 1))≤ 76.36A3
(~σn)3
√
Dn
Nn
.
Proof. We can apply Theorem 20, choosingγ = 1, and λ = 0.193. It yields a constant smaller than
77.911. It is however possible to get the better constant given above by redoing some of the computations
in this speciﬁc setting. Withρ> 4, setK = 1
(4e+ρ)A3, andεn = 1
K (tn)3/2. On the zoneξ∈ [− 1
εn
, 1
εn
], we
have a bound|θn(ξ)− 1|≤ M|ξ|3 exp(M|ξ|3), this time withM = (2 + 8e
ρ )A3. Hence,
