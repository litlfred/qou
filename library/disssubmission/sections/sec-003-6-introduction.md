---
doc_id: disssubmission
doc_title: "Tannakian categories of perverse sheaves on abelian varieties"
section_id: sec-003-6-introduction
section_title: "Introduction"
section_number: 6
pages: 14-17
source_pdf: DissSubmission.pdf
source_sha256: 207fd5e3dc0d278d
doc_brief: "Tannakian categories of perverse sheaves on abelian varieties — 121 sections: Acknowledgements; Introduction; Introduction"
---
that this alternating resp. symmetric convolution square is irreducible up to
a skyscraper sheaf and negligible terms.
So for x varying in a Zariski-open dense subset ofX(C), the variable
part of the cohomology ofY+x deﬁnes a variation of Hodge structures whose
underlying local system is irreducible. The main topic of chapter 5 is a study
of this variation in the case whereg = 4. In this case we are dealing with
a family of smooth surfaces of general type with a surprisingly explicit and
beautiful geometry. On the level of integral cohomology, we will determine
the N´eron-Severi lattices
H2(Yx,Z) and H2(Y+
x ,Z)
of the respective surfaces and deduce that the local system underlying the
considered variation of Hodge structures essentially has the monodromy
groupW(E6), see theorem 5.1. We will also see that the appearance of this
Weyl group in the present context is closely related to the ubiquitous 27
lines on a cubic surface — the link is provided by the Prym-embedded
curves onYx which have been studied by E. Izadi in [61] and appear here as
glue vectors for the above N´eron-Severi lattices.
In view of this example, it remains an intriguing question to ask for the
general relationship between the Tannaka groupG(P) attached to a perverse
sheaf P∈ Perv(X,C) and the monodromy groups deﬁned by the simple
perverse sheaves in the corresponding Tannakian category. At present this
relationship remains mysterious even for Brill-Noether sheaves on Jacobian
varieties. As a ﬁrst step in this direction, we conclude this dissertation with
a recursive formula for the generic rank of Brill-Noether sheaves — in the
hope that this formula may be given a representation-theoretic and more
conceptual interpretation at some future time.
Some commonly used notations
Dbc (X,Λ) derived category of bounded constructible sheaf complexes
on X as deﬁned in [10], in the analytic sense ifΛ = C and in
the l-adic sense ifΛ is an extension ofQl
Perv(X,Λ) the abelian subcategory of perverse sheaves inDbc (X,Λ)
Hi(X,K) ith hypercohomology group ofK∈ Dbc (X,Λ)
Hic(X,K) ith compactly supported hypercohomology group ofK
H i(K) ith cohomology sheaf ofK
pHi(K) ith perverse cohomology sheaf ofK
χ(K) Euler characteristic∑i∈Z(−1)i dimHi(X,K) of K
Supp(K) support ofK
D(K) Verdier dual ofK
K(i) i-fold Tate twist ofK
δY = ICY[d] perverse intersection cohomology sheaf attached to a closed
subvarietyY ↪→X of dimensiond
ΛY constant sheaf with coefﬁcients in the ﬁeldΛ and support on
a closed subvarietyY ↪→X
Π(X) group of all charactersχ : π1(X,0)−→Λ∗ of the topological
fundamental group, resp. of all continuous characters of the
tame ´etale fundamental group in thel-adic setting
Π(X)l maximal pro-l-subgroup ofΠ(X)
Lχ local system attached to a characterχ∈ Π(X)
Kχ = K⊗Λ Lχ twist of a complexK∈ Dbc (X,Λ) by a characterχ∈ Π(X)
S (P) spectrum ofP∈ Perv(X,Λ) as deﬁned in section 1.5
Ψ, Ψ1 functor of nearby cycles resp. its unipotent part
sp specialization functor as deﬁned in section 4.3
G(P) Tannaka group attached toP∈ Perv(X,Λ) in corollary 3.10
An, Sn alternating resp. symmetric group of degreen
7
CHAPTER 1
Vanishing theorems on abelian varieties
As we mentioned in the introduction, our construction of Tannakian
categories will be closely intertwined with a vanishing theorem for perverse
sheaves on abelian varieties. In the ﬁrst two chapters of this dissertation
which are based on joint work with R. Weissauer [68], we discuss various
incarnations of this vanishing theorem and explain how it may be proved in
an abstract Tannakian framework.
