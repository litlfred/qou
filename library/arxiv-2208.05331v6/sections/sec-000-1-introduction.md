---
doc_id: arxiv-2208.05331v6
doc_title: "PURE BRAID GROUP ACTIONS ON CATEGORY O MODULES"
section_id: sec-000-1-introduction
section_title: "Introduction"
section_number: 1
pages: 1-7
source_pdf: 2208.05331v6.pdf
source_sha256: 54b4a400388dbf41
toc_source: outline
doc_brief: "PURE BRAID GROUP ACTIONS ON CATEGORY O MODULES — Let g be a symmetrisable Kac–Moody algebra and Uℏg its quan- tised enveloping algebra. Answering a question of P."
---
1
2.
Kac–Moody algebras and quantum groups
7
3.
Faithfulness of category O integrable modules
10
4.
Quantum Weyl group actions of pure braid groups
12
5.
The Casimir connection
14
6.
Braided Coxeter categories
18
7.
The equivariant monodromy theorem
24
8.
The monodromy theorem in category O∞
27
9.
Parabolic pure braid group actions
29
References
35
1. Introduction
1.1.
Let g be a symmetrisable Kac–Moody algebra, Uℏg its quantized enveloping
algebra and W their Weyl group. We denote by O the category of deformation
highest weight modules of g, by Oint ⊂O the full subcategory of integrable ones, and
by Oint
ℏ⊂Oℏthe corresponding categories for Uℏg. In [ATL15], we constructed an
equivalence Oint →Oint
ℏ
which intertwines the monodromy of the rational Casimir
connection of g and the quantum Weyl group action of the braid group BW of
g, respectively, thus extending the equivalence obtained in [TL02, TL08, TL16]
when g is ﬁnite–dimensional. P. Etingof asked whether this equivalence extends to
suitable categories of modules which are not necessarily integrable, while remaining
equivariant under the pure braid group PW of g.
2020 Mathematics Subject Classiﬁcation. Primary: 81R50. Secondary: 17B37, 20F36.
The ﬁrst author is partially supported by the Program FIL 2020 of the University of Parma
and co-sponsored by the Fondazione Cariparma. The second author is partially supported by the
NSF grant DMS–1802412.
2
A. APPEL AND V. TOLEDANO LAREDO
The goal of the present paper is to answer this question in the aﬀermative.
Speciﬁcally, we prove that the quantum Weyl group action of PW on category Oint
ℏ
modules can be extended to all category Oℏmodules.
We then show that this
action is equivalent to the restriction to PW of the equivariant monodromy of the
Casimir connection, which is deﬁned on any category O module. Our results hold
more generally for the category O∞of modules which are locally ﬁnite under the
action of the Borel subalgebra, though for simplicity we restrict to category O in
the Introduction.
1.2.
We turn now to a more detailed description of our results. Endow O with the
associativity and commutativity constraints arising from the KZ equations [Dri90].
In [EK96, EK98, EK08], Etingof–Kazhdan constructed a braided tensor equivalence
F : O →Oℏwhich is Tannakian, that is endowed with a natural isomorphism α
ﬁtting in the diagram
O
Oℏ
Vectℏ
F
f
fℏ
α
where Vectℏis the category of topologically free modules over C[[ℏ]], f, fℏare the
forgetful functors, and f is endowed with an appropriate tensor structure. The pair
(F, α) gives rise to an isomorphism Ψα : End(fℏ) →End(f) via the composition
End(fℏ) −→End(fℏ◦F) −→End(f)
where the ﬁrst isomorphism is induced by F, and the second is given by Ad(α). Note
that α is only unique up to an automorphism γ of f, and that Ψγ◦α = Ad(γ) ◦Ψα.
1.3.
Building on our earlier work [ATL18, ATL19a, ATL19b], we constructed in
[ATL15] an automorphism γ ∈Aut(f) such that Ψγ◦α is equivariant with respect to
the action of the braid group BW on integrable category O modules. Speciﬁcally, the
Etingof–Kazhdan functor F restricts to an equivalence Oint →Oint
ℏ
and therefore
leads to an isomorphism Ψint
α′ : End(fint
ℏ) →End(fint) for any α′ : fℏ◦F ⇒f.
Regard the quantum Weyl group action of BW on objects in Oint
ℏ
as a morphism
λ : BW →End(fint
ℏ), and the monodromy of the Casimir connection as a morphism
µ : BW →End(fint). Then, γ may be chosen so that the following is a commutative
triangle [ATL15]
BW
End(fint
ℏ)
End(fint)
λ
µ
Ψint
γ◦α
(1.1)
As a consequence, the monodromy of the Casimir connection on a module V ∈Oint
is equivalent to the quantum Weyl group action of BW on F(V ).
1.4.
P. Etingof asked us whether such an equivalence holds for a larger class of not
necessarily integrable modules, provided BW is replaced by the pure braid group
PW . The choice of the latter is suggested by the fact that BW does not act on all
category O modules for either g or Uℏg, while PW does on category O g–modules
via the monodromy of the Casimir connection.
PURE BRAID GROUP ACTIONS ON CATEGORY O MODULES
3
To the best of our knowledge, no action of PW on category Oℏmodules has been
previously constructed. The main result of the present paper is to construct such
an action, and then show the commutativity of the resulting diagram
PW
End(fℏ)
End(f)
λ
µ
Ψγ◦α
(1.2)
1.5.
To state our results in more detail, recall ﬁrst that the abelianisation P ab
W =
PW /[PW , PW ] of the pure braid group is isomorphic to the free abelian group with
a generator pα for each positive real root α [Tit66, Dig15]. Set ι = √−1, and deﬁne
the sign character to be the morphism
εℏ: P
ab
W →Aut(f
int
ℏ)
pα →exp(πιhα)
where exp(πιhα) acts as multiplication by exp(πιν(hα)) on the ν–weight space of
an integrable category Oℏmodule. The morphism εℏarises as the reduction mod
ℏof the quantum Weyl group action of PW on category Oint
ℏ.
As a subgroup of BW , PW is generated by the elements S2
w,i = SwS2
i S−1
w , where
Si is a generator of BW , w ∈W is such that wαi is a positive root, and Sw ∈BW is
the canonical lift of w [DG01]. Moreover, the quantum Weyl group action of Sw,i
on a module V ∈Oint
ℏis given by
λ(S2
w,i) = exp(πιhwαi)qKw,i = εℏ(Sw,i)qKw,i
where the second factor is the truncated quantum Casimir operator for the copy of
Uℏsl2 ⊂Uℏg corresponding to the pair (w, i) [Lus93], and q = exp(ℏ/2).
1.6.
To extend this action to an arbitrary category Oℏmodule, we lift the sign
character εℏto a morphism
P
ab
W →Aut(fℏ)
pα →exp(πιhα)
which we denote by the same symbol. We then prove that the quantum Casimirs
qKw,i ∈Uℏg give rise to a morphism K : PW →(Uℏg)h. It follows that
λ : PW →Aut(fℏ)
S2
w,i →exp(πιhwαi)qKw,i
(1.3)
is an extension of the quantum Weyl group action of PW to all category Oℏmodules.
1.7.
The fact that K is a morphism would follow at once if End(fℏ) acted faithfully
on fint
ℏ. This, however, is clearly false: if ϕ is any function on h∗which vanishes on
integral weights, then ϕ ∈End(fℏ), but ϕ maps to zero in End(fint
ℏ). To remedy this,
we rely on the fact that Uℏg acts faithfully on fint
ℏ, whose proof is due to Etingof.
This implies that any λ(p) ∈End(fint
ℏ), p ∈PW , arises from the action of a unique
element of Uℏg, thereby yielding the required action of PW on End(fℏ).1
A similar argument works for the quantum group Uqg, where q is either an
indeterminate, or not a root of unity. In that case, the quantum Casimirs qKw,i do
not lie in Uqg, but in a variant Dq of an algebra originally introduced by Drinfeld
[Dri92, Sect. 8], which consists of formal, inﬁnite series of the form P cXX, where
X runs over a weight basis of Uqn+ and cX ∈Uqb−. Etingof’s faithfulness result
also applies to Dq, and yields an action of PW on any category O module for Uqg.
1Note that this bypasses having to explicitly check that the quantum Casimirs satisfy the
relations of the generators Sw,i given in [DG01, Cor. 6].
4
A. APPEL AND V. TOLEDANO LAREDO
1.8.
Let now Y be the complexiﬁcation of the Tits cone of g, X ⊂Y its set of
regular points, and x0 ∈X a basepoint. By a theorem of van der Lek [vdL83], which
generalises Brieskorn’s [Bri71], the pure and full braid groups may be realised as
PW ∼= Π1(X; x0)
and
BW ∼= Π1(X/W; [x0])
The Casimir connection is the Ug–valued formal meromorphic connection on X
with logarithmic singularities on the root hyperplanes given by
∇K = d −h
X
α≻0
dα
α · K+
α
(1.4)
where K+
α = Pmα
i=1 e(i)
−αe(i)
α is the normally ordered truncated Casimir operator cor-
responding to the positive root α, and h = ℏ/2πι [MTL05, TL02, Pro96, FMTV00].
The sum (1.4) over α is locally ﬁnite on any (not necessarily integrable) category O
module V , and gives rise to a well–deﬁned ﬂat connection on the holomorphically
trivial vector bundle V on Y with ﬁbre V . Its monodromy therefore gives rise to a
morphism
P : Π1(X; x0) →End(f)
(1.5)
1.9.
The normal ordering in (1.4) breaks the equivariance of ∇K with respect to
the action of W on X and the subalgebra of h–invariants Ugh ⊂Ug, which contains
the Casimirs K+
α .
Nevertheless, it is possible to modify the monodromy of ∇K so that it gives
rise to a representation of the braid group BW on integrable category O modules
[ATL15, Sect. 4] (see also Section 5). This relies on the equivalence of groupoids
Ex0 : Π1(X/W; [x0]) →W ⋉Π1(X; Wx0)
(1.6)
where the right–hand side is the semi–direct product of W with the fundamental
groupoid of X based at the orbit Wx0, and Ex0 is given by the unique lifting of
loops through x0, and proceeds as follows.
• Extend the monodromy of ∇K to a morphism
P : Π1(X; Wx0) →End(f)
(1.7)
• Replace the target of P by a subalgebra Tg ⊂End(f) which, unlike End(f),
is acted upon by W.
Tg is the image of the holonomy algebra of the root
arrangement of g, and is a completion of the subalgebra of Ugh[[ℏ]] generated
by the Casimirs ℏK+
α and the Cartan subalgebra ℏh.
• The lack of equivariance of ∇K can then be measured by a 1–cocycle
A : W →Hom(Π1(X; Wx0), Tg)
deﬁned by Aw(γ) = P(γ)−1 · w−1P(wγ).
• We prove that A is abelian i.e., takes values in
M = Hom(Π1(X; Wx0), exp(ℏh))
and that it is the coboundary of an essentially unique cochain B ∈M i.e., that
Aw = B · (w−1B)−1 for any w ∈W.
• As a consequence, P can be modiﬁed to a W–equivariant morphism
PB : Π1(X; Wx0) →Tg
PB(γ) = P(γ) · B(γ)
• Composing PB with the morphism Ex0 (1.6) then yields an action of BW on
any W ⋉Tg–module.
PURE BRAID GROUP ACTIONS ON CATEGORY O MODULES
5
• It is well–known that W does not act on an integrable module V , but that the
triple exponentials
τi = exp(ei) · exp(−fi) · exp(ei)
(1.8)
are well–deﬁned on V , permute its weight spaces according to the W–action,
and give rise to a morphism τ : BW →Aut(fint).
• Finally, lifting Ex0 to eEx0 : Π1(X/W; [x0]) →BW ⋉Π1(X; Wx0), and composing
with τ ⊗PB yields a morphism
Pτ,B : BW →Aut(f
int)
γ →τ(γ) · P(γ) · B(γ)
which we term the equivariant monodromy of ∇K.
1.10.
By [ATL15], the equivariant monodromy of ∇K on an integrable module
V ∈Oint is canonically equivalent to the quantum Weyl group action of BW on the
Etingof–Kazhdan quantisation F(V ) ∈Oint
ℏ
i.e., the diagram (1.1) is commutative
for µ = Pτ,B. This can be used to give a monodromic description of the action λ
(1.3) of PW on category Oℏmodules as follows.
The restriction of the triple exponential map τ (1.8) to PW is the sign character
ε : P
ab
W →Aut(f
int)
pα →exp(πιhα)
Lifting it to ε : P ab
W →Aut(f) as in 1.6 therefore lifts the equivariant monodromy
action of PW to
Pε,B : PW →Aut(f)
γ →ε(γ) · P(γ) · B(γ)
i.e., extends the restriction of Pτ,B to PW to any category O module.
To relate Pε,B to λ, denote the restriction morphisms by
Res : End(f) →End(f
int)
and
Resℏ: End(f) →End(f
int)
The commutativity of (1.1) implies that, for any p ∈PW
Res ◦Ψγ◦α ◦λ(p) = Ψ
int
γ◦α ◦Resℏ◦λ(p) = Res ◦Pε,B(p)
and therefore that Res ◦Ψγ◦α ◦K (p) = Res ◦(P(p)B(p)), since ε = Ψγ◦α(εℏ). In
turn, this implies that Ψγ◦α ◦K (p) = P(p)B(p), so that Ψγ◦α intertwines λ and
Pε,B, since Ψγ◦α maps the Drinfeld algebra Dℏ⊃Uℏg to its classical analogue D,
the latter acts faithfully on f, and the algebra Tg ∋P(p), B(p) is contained in D.
1.11.
The above can also be used to give a description of the (non–equivariant)
monodromy P : PW →Aut(f) of the Casimir connection ∇K (1.5) in terms of
quantum Weyl group operators as follows.
We prove that the restriction to PW of the cochain B is the map P ab
W →exp(ℏh)
given by B(pα) = exp(ℏtα/2), where tα ∈h corresponds to α via the isomorphism
h∗→h induced by the chosen inner product on g. Deﬁne the morphism
λε,B : PW →Aut(fℏ)
p →εℏ(p)−1 · λ(p) · B(p)−1 = K (p) · B(p)−1
We refer to λε,B as the normally ordered quantum Weyl group action of PW on
category Oℏmodules. The terminology is motivated by the fact that, while λ(S2
i ) =
exp(πιhi) · qKℏ,i by (1.3), λε,B(S2
i ) = q2K+
ℏ,i, where the latter is a normally ordered
version of the quantum Casimir. The commutativity of (1.1) then implies that λε,B
computes the monodromy of ∇K, that is that Ψγ◦α ◦λε,B = P.
6
A. APPEL AND V. TOLEDANO LAREDO
1.12.
The above results can be generalised to the parabolic setting as follows. Let
J be a subset of nodes of the Dynkin diagram of g, gJ ⊆g the corresponding Lie
subalgebra, WJ ⊆W its Weyl group, and PBJ ⊆BW the parabolic pure braid
group given by the preimage of WJ.
We construct a quantum Weyl group action of PBJ on any category Oℏmodule
whose restriction to UℏgJ is integrable. This action is such that
• its restriction to the braid group BWJ is the quantum Weyl group action of
BWJ on integrable UℏgJ–modules
• its restriction to the pure braid group PW coincides with the quantum Weyl
group action (1.3) on category Oℏmodules
We also deﬁne a normally ordered version of this quantum Weyl group action, in
analogy with 1.11.
We then construct a monodromy action of PBJ on any category O module
whose restriction to gJ is integrable. We do so by relying on the fact that PBJ
is isomorphic to Π1(X/WJ; [x0]), and correcting the equivariance of the Casimir
connection, as outlined in 1.9, but only with respect to WJ. The resulting WJ–
equivariant monodromy action is such that
• its restriction to BWJ is the equivariant monodromy action of BWJ on inte-
grable category O gJ–modules
• its restriction to PW coincides with the monodromy action (1.7) on category
O modules (up to a simple correction on PWJ).
Finally, we show that the above quantum Weyl group and monodromic actions
of PBJ are equivalent by relying on the fact that PBJ is generated by BWJ and
PW , and using the equivalences (1.1) for BWJ and (1.2) for PW .
1.13. Outline of the paper. In Section 2, we review the deﬁnition of quantum
Weyl group operators. In Section 3, we introduce the Drinfeld algebra and prove
that it acts faithfully on Oint
ℏ. In Section 4, we construct the quantum Weyl group
action of PW on category O. Section 5 reviews the deﬁnition of the Casimir con-
nection, and the equivariant extension of its monodromy to a representation of the
braid group BW . Section 6 reviews the deﬁnition of a braided Coxeter category, and
Section 7 the main result of [ATL15]. In Section 8, we prove the stated equivalence.
We also point out that it continues to hold if F is replaced by the Etingof–Kazhdan
equivalence FΦ corresponding to an arbitrary Lie associator Φ rather than the one
arising from the KZ equations. Finally, in Section 9, we generalise these results to
parabolic pure braid groups.
1.14. Acknowledgments. We heartily thank Pavel Etingof for persistently asking
us about extending the main result of [TL08, TL16, ATL15] to pure braid groups,
and for his detailed comments on, and very careful reading of, an earlier version of
this paper.
PURE BRAID GROUP ACTIONS ON CATEGORY O MODULES
7
