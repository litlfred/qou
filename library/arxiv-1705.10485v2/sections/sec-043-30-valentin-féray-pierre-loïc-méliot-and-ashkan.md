---
doc_id: arxiv-1705.10485v2
doc_title: "Mod-φ convergence, II: Estimates on the speed of convergence"
section_id: sec-043-30-valentin-féray-pierre-loïc-méliot-and-ashkan
section_title: "Valentin Féray, Pierre-Loïc Méliot, and Ashkan Nikeghbali"
section_number: 30
pages: 30-31
source_pdf: 1705.10485v2.pdf
source_sha256: b33759def53c6a43
doc_brief: "Mod-φ convergence, II: Estimates on the speed of convergence — In this paper, we give estimates for the speed of convergence towards a limiting stable law in the recently introduced setting of mod-φ"
---
|E[fa,εn(Yn)]− E[fa,εn(Y )]|≤ M
2π (tn)3/2
∫ 1
εn
− 1
εn
|ξ|2 e
−ξ2
2 +M |ξ|3
(tn )3/2
dξ
≤ M
2π (tn)3/2
∫ 1
εn
1
εn
|ξ|2 e−ξ2( 1
2− 2
ρ)dξ
≤ M√
2π (tn)3/2 (1− 4
ρ)3/2 = 1√
2π
2
ρ(1− 4
ρ)3/2 εn.
By Theorem 19, we get for anyλ> 0:
dKol
(
Sn√
Var(Sn)
,NR(0, 1)
)
≤ (1 +λ)√
2π
(
2
ρ(1− 4
ρ)3/2 + 1
3√π
(
4
3
√
1 + 1
λ + 3
3√
3
))
εn.
The best constant is then obtained withρ = 6.79 and λ = 0.185. ⊓ ⊔
Remark 31.There is a trade-oﬀ in the bound of Corollary 30 between thea prioriupper bound on(~σn)2,
and the constantC that one obtains such that the Kolmogorov distance is smaller than
CA3
(~σn)3
√
Dn
Nn
.
This bound gets worse when(~σn)2 is small, but on the other hand, the knowledge of a bettera priori
upper bound (that is precisely when(~σn)2 is small) yields a better constantC. So, for instance, if one
knowns that(~σn)2≤A2 (instead of2A2), then one gets a constantC = 52.52. A general bound that one
can state and that takes into account this trade-oﬀ is:
dKol(Yn,NR(0, 1))≤ 27.55
((A
~σn
)3
+ A
~σn
)√
Dn
Nn
.
We are indebted to Martina Dal Borgo for having pointed out this phenomenon. In the sequel, we shall
freely use this small improvement of Corollary 30.
The above corollary ensures asymptotic normality with a bound on the speed of convergence when
( 1
(~σn)3
√
Dn
Nn
→ 0
)
⇐⇒
(
(~σn)2
(Nn
Dn
)1/3
→ +∞
)
.
Using a theorem of Janson, the asymptotic normality can be obtained under a less restrictive hypothesis,
but without bound on the speed of convergence. Even if the main topic of the paper is to ﬁnd bounds on
the speed of convergence, we will recall the result here for the sake of completeness.
Proposition 32.As above, letSn be a sequence with a uniform bounds on cumulants with parameters
(Dn,Nn,A ) and assume that
lim
n→∞
Var(Sn)
NnDn
(Nn
Dn
)ε
= lim
n→∞
(~σn)2
(Nn
Dn
)ε
= +∞
for some parameterε∈ (0, 1). Then,
Sn√
Var(Sn)
⇀NR(0, 1).
Mod-φ convergence, II: Estimates on the speed of convergence 31
Proof. Note that the bounds on cumulants can be rewritten as
|κ(r)(Yn)|≤ Cr
(
Var(Sn)
NnDn
(Nn
Dn
)1− 2
r
)−r
2
for some constantCr. Choosingr large enough so that1− 2
r≥ ε, we conclude thatκ(r)(Yn)→ 0 for r
large enough. This is a suﬃcient condition for the convergence in law towards a Gaussian distribution,
see [Jan88, Theorem 1] and [Gri92]. ⊓ ⊔
Remark 33.Up to a change of parameters, it would be equivalent to consider bounds of the kind
|κ(r)(Sn)|≤ (Cr)rαn(βn)r, or
⏐⏐⏐⏐κ(r)
(
Sn√
Var(Sn)
)⏐⏐⏐⏐≤ r!
∆r−2n
,
as done by Saulis and Statulevičius in [SS91] or by the authors of this paper in [FMN16]. In particular,
it was proved in [FMN16, Chapter 5], that under slight additional assumptions on the second and third
cumulants, we have the following: the sequence(Xn)n∈N deﬁned in Lemma 29 converges in the mod-
Gaussian sense with parameters(tn)n∈N.
