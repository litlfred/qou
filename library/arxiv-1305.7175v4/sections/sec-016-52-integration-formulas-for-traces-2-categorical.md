---
doc_id: arxiv-1305.7175v4
doc_title: "NONLINEAR TRACES"
section_id: sec-016-52-integration-formulas-for-traces-2-categorical
section_title: "Integration formulas for traces: 2-categorical consequences"
section_number: 5.2
pages: 31-36
source_pdf: 1305.7175v4.pdf
source_sha256: 5a09955f4fb6a57e
doc_brief: "NONLINEAR TRACES — W e combine the theory of traces in homotopical algebra with s heaf theory in de- rived algebraic geometry to deduce general ﬁxed point and ch aracter formulas."
---
functoriality of dimensions and traces. For this we require the 2-ca tegorical enhanced version
S of a sheaf theory, so as to take advantage of the resulting funct orial adjunction
S(X)
f∗ /d47/d47S(Y )
f !
/d111/d111
for f :X→Y proper. In particular, applying the functor S on two-morphisms we ﬁnd that
6One can also check directly that the cyclic structure on the c yclic bar construction of the dg category S(X)
is induced by the cyclic structure of the loop space LX under the identiﬁcation ω (LX) ≃ dim(S(X)).
32 DA VID BEN-ZVI AND DA VID NADLER
• A proper map f :Z→W of correspondences
Z
pZ
/d126/d126⑥⑥⑥⑥⑥⑥⑥⑥
f
/d15/d15
qZ
/d32/d32❆❆❆❆❆❆❆❆
X Y
W
pW
/d96/d96❇❇❇❇❇❇❇❇ qW
/d62/d62⑥⑥⑥⑥⑥⑥⑥⑥
induces a canonical integration morphism of integral transforms
∫
f :qZ∗p!
Z /d47/d47qW ∗p!
W
• In particular, when X =Y =pt, it induces a map of global volume forms
∫
f :ω(Z) /d47/d47ω(W )
• There is a canonical composition identity
∫
g◦
∫
f≃
∫
g◦f
Proposition 5.4. Forf :X→Y proper, the unit and counit of the (f∗,f !) adjunction are given
respectively by integration along the proper maps of self-c orrespondences ∆ /Y :X→X×Y X
of X and f/Y :X→Y of Y :
X
/d122/d122✉✉✉✉✉✉✉✉✉✉
∆ f
/d15/d15
/d36/d36■■■■■■■■■■ X
f
/d126/d126⑦⑦⑦⑦⑦⑦⑦⑦
f
/d15/d15
f
/d32/d32❅❅❅❅❅❅❅❅
X X Y Y
X×Y X
p1
/d100/d100❍❍❍❍❍❍❍❍❍ p2
/d58/d58✈✈✈✈✈✈✈✈✈
Y
/d95/d95❅❅❅❅❅❅❅❅
/d63/d63⑦⑦⑦⑦⑦⑦⑦⑦
Proof. The assertion follows immediately from the geometric description of t he unit and counit
in the correspondence category, Proposition 4.3, upon applying th e functorS. □
Proposition 5.5. For any proper map f :X→Y , the induced map on dimensions
dim(f∗) : dim(S(X)) /d47/d47 dim(S(Y ))
is identiﬁed ( S1-equivariantly) with integration along the loop map
dim(f∗)≃
∫
Lf :ω(LX) /d47/d47ω(LY )
Proof. According to Deﬁnition 3.19, we must calculate the composition
dim(f∗) : Tr(id S(X))
Tr(ηf )/d47/d47 Tr(f !f∗) ∼ /d47/d47 Tr(f∗f !)
Tr(ǫf )/d47/d47 Tr(idS(Y ))
The equivalence of the middle arrow is given by the canonical identiﬁca tions
Tr(f !f∗)≃ω((X×Y X)×X×XX)≃ω(X×Y ×Y Y )≃ Tr(f∗f !)
By Proposition 5.4, the unit ηf : id S(X)→f !f∗ is given by the integration morphism
∫
∆ f
: ∆ f ∗ωX /d47/d47ωX×YX
NONLINEAR TRACES 33
and hence its trace Tr( ηf ) : Tr(id S(X))→ Tr(f !f∗) is given by the induced integration map
∫
∆ f
:ω(LX) /d47/d47ω((X×Y X)×X×XX)
Likewise, the counit ǫf :f∗f !→ idS(Y ) is given by by the integration morphism
∫
f :f∗ωX /d47/d47ωY
and hence its trace Tr( ǫf ) : Tr(f∗f !)→Tr (idS(Y )) is given by the induced integration map
∫
f :ω(X×Y ×Y Y ) /d47/d47ω(LY )
Finally, by functoriality, their composition is given by the integration m ap
∫
Lf :ω(LX) /d47/d47ω(LY )
□
Finally, we have the functoriality of traces in parallel with the previou s theorem on the
functoriality of dimensions. Let us recall the relevant setup. Cons ider a proper morphism
f : X→ Y and endomorphisms FZ : X→ X and FW : Y → Y in Corrk given by respective
self-correspondences X←Z→X and Y ←W→Y .
By an f -morphism from the pair ( X,FZ ) to the pair ( Y,FW ), we mean an identiﬁcation
s :Z ∼ /d47/d47X×Y W
of correspondences from X toY . This in turn induces an identiﬁcation of what might be called
relative traces
Z×Y ×Y Y ∼ /d47/d47X×Y ×Y W
generalizing the relative loop space LXY from the case of the identity correspondences Z =X,
W =Y . We thus obtain a map of traces
τ (f,s ) : Z|∆ X =Z×X×XX /d47/d47Z×Y ×Y Y ∼ /d47/d47X×Y ×Y W /d47/d47Y×Y ×Y W =W|∆ Y
Proposition 5.6. With the preceding setup, the trace map Tr(f∗,s ) : Tr(FX∗)→ Tr(FY ∗) is
canonically identiﬁed with the integration map
∫
τ (f,s) :ω(Z|∆ X ) /d47/d47ω(W|∆ Y )
Proof. The argument is parallel to the proof of Proposition 5.5. One calculat es Tr(f∗,α ) from
Deﬁnition 3.24 using Proposition 4.8 and the compatibility of Proposition 5.2 and the integra-
tion morphism for integral transforms from Section 2.3.2. □
5.3. Ind-coherent sheaves andD-modules. We now apply the results of Gaitsgory-Rozenblyum [GR2]
and Drinfeld-Gaitsgory [DG] establishing functoriality properties of categories of ind-coherent
sheaves andD-modules.
We ﬁrst state a fundamental result of Gaitsgory-Rozenblyum [GR2 ]:
Theorem 5.7. [GR2, Theorem III.3.5.4.3, III.3.6.3] There is a uniquely deﬁned right-lax
symmetric monoidal functorQ! from the (∞, 2)-category whose objects are laft (locally almost of
ﬁnite type) prestacks, morphisms are correspondences with vertical arrow ind-inf-schematic, and
2-morphisms are ind-proper and ind-inf-schematic, to the (∞, 2) categorydgCatk of k-linear
presentable dg categories with continuous morphisms. The f unctorQ! is strictly symmetric
monoidal on the full subcategory of laft ind-inf-schemes.
34 DA VID BEN-ZVI AND DA VID NADLER
The theorem encodes a tremendous amount of structure in great generality. Let us highlight
some salient features useful in practice. The theorem assigns a sy mmetric monoidal dg category
Q!(X) to any stack satisfying a reasonable ﬁnite type assumption. The s ymmetric monoidal
structure, the !-tensor product, is induced by !-pullback along diag onal maps. For an arbitrary
morphism p :X→Y there is a continuous symmetric monoidal pullback functor f ! :Q!(Y )→
Q!(X), while for f schematic (or ind-schematic) there is a continuous pushforward f∗ :Q!(X)→
Q!(Y ), which satisﬁes base change with respect to !-pullbacks. Moreove r for f proper (or ind-
proper), (f∗,f !) form an adjoint pair.
The theorem goes much further through the powerful formalism o f inf-schemes: prototypical
inf-schemes are quotients of schemes by inﬁnitesimal equivalence r elation. Thus one can treat
on an equal footing ind-coherent sheaves that are equivariant fo r any formal groupoid. The
most important example is the de Rham space XdR of a scheme, and one recovers D-modules
on X as ind-coherent sheaves on the de Rham functor of X,D(X) =Q!(XdR). Thus by ﬁrst
applying the functor (−)dR the theorem encodes the theory of D-modules, as a functor out of
the correspondence 2-category of stacks (or laft prestacks) with pullbacks for arbitrary maps
and pushforward for (ind-)schematic maps.
Corollary 5.8. The functorsQ! andD deﬁne sheaf theories on laft ind-inf-schemes, i.e., deﬁne
symmetric monoidal functors
Q!,D :Corr (ind−inf−Schk)ind−prop−→dgCatk.
Thus the conclusions of Theorem 1.4 apply in this setting (in particular the Grothendieck-
Riemann-Roch theorem for ind-proper maps of ind-inf-schem es).
5.3.1. The QCA setting. We are mostly interested in applications of sheaf theory on stacks,
e.g. in an equivariant setting. That requires two features of the th eoriesQ! andD that are not
encoded in Theorem 5.7.
Theorem 5.7 produces in general a right-lax symmetric monoidal functor – in other words,
we have the natural map
Q!(X)⊗Q !(Y )−→Q !(X×Y )
satisfying the expected coherences, but it is not an equivalence in g eneral (though it is for
schemes).
Also, while the theorem encodes arbitrary pullbacks, it does not enc ode a continuous push-
forward functor p∗ :Q!(X)→Q !(Y ) for non-schematic morphisms (though a generalization to
include QCA morphisms has been announced by the authors). This pr ecludes an immediate
application of our formalism to traces on stacks.
However, since the full structure of a sheaf theory is far strong er than is needed for the
“local” statements we discuss in this paper, we can get around this is sue, by taking advantage
of the following compilation of results of Drinfeld and Gaitsgory (spec iﬁcally, see Section 3.6.1,
Corollarys 3.7.14, 4.2.3, and 4.4.7, Proposition 4.4.11, Corollarys 8.3.4 an d 8.4.3, Deﬁnition
9.3.2 and Proposition 9.3.12).
Theorem 5.9. [DG]
(1) For a QCA stack X, the categories Q!(X) andD(X) are dualizable and canonically
self-dual.
(2) The canonical functors deﬁne equivalences
Q!(X)⊗Q !(Y )≃Q !(X×Y ), D(X)⊗D (Y )≃D (X×Y )
NONLINEAR TRACES 35
(3) For a morphism f :X→Y of QCA stack, the “renormalized pushforwards” 7
f• :Q!(X)→Q !(Y ), f • :D(X)→D (Y )
deﬁned as the transpose of f ! (by the self-duality of (1)) are continuous functors satis-
fying base-change and the projection formula with respect t o pullback.
Let us now brieﬂy indicate how the results of the previous two sectio ns carry over to QCA
stacks in the absence of a fully ﬂedged sheaf theory, where we use the renormalized pushforward
functorsf• provided by Theorem 5.9 to carry out non-representable pushfor wards. In particular,
for X a general QCA stack, so that piX : X→ pt is not representable, this means that the
notation ω(X) has to be taken in a renormalized fashion,
ω(X) := πX,•π!
Xk =πX,•ωX.
For the theory of ind-coherent sheaves this produces the usual notion of derived global sections
of the dualizing complex, but for the theory of D-modules this will diﬀer in general from the
nonrenormalized version, namely Borel-Moore chains on X:
ω(X)non−renorm =RΓdR(ωX ) = CBM
∗ (X).
In Proposition 5.2, the self-duality in assertion (1) for QCA stacks is the content of Theo-
rem 5.9(1), and f• is deﬁned so as to make it the transpose of f !. Assertion (2) follows from the
sheaf theory construction (i.e. is independent of non-represent able morphisms), the projection
formula is asserted in item (3) of the theorem and the last two asser tions are deduced from the
ﬁrst three. Proposition 5.3 is also deduced directly from Proposition 5.2.
The general trace construction
∫
f discussed in Section 5.2 depends only on the functoriality
of proper adjunction (which is part of the [GR2] formalism) and the d eﬁnition of pullback and
(renormalized) pushforward. The identities needed to verify Prop ositions 5.4, 5.5 and 5.6 only
depend on base change, which is guaranteed by Theorem 5.9. We the refore get as a payoﬀ that
the conclusions of Theorem 1.4 hold for QCA stacks, in particular:
Theorem 5.10. LetS =Q! orS =D denote either ind-coherent sheaves or D-modules. Let
f :X→Y denote a proper morphism of QCA stacks.
• For any compact object M∈S (X) (coherent sheaf or safe coherent D-module) with char-
acter [M ]∈HH ∗(S(X))≃ω(LX), there is a canonical identiﬁcation
[f∗M]≃
∫
Lf
[M ]∈HH ∗(S(Y ))≃ω(LY )
• Assume Y =BG for an aﬃne group and X =Z/G for Z a proper QCA stack. Then for
any compact object M∈S (Z/G) (G-equivariant coherent sheaf or safely equivariant coheren t
D-module on X), and element g∈G, there is a canonical identiﬁcation
[f∗M ]|g≃
∫
Lf
[M ]|X g
• For a map f : (X,Z )→ (Y,W ) of QCA stacks with self-correspondences, the induced map
Tr (S(Z))→Tr (S(W )) is given by integration along ﬁxed points Z|∆ X→W∆ Y .
7W e note that for Q! the “renormalized” pushforward is the standard pushforwar d functor, while for D it
diﬀers for non-safe objects from the more familiar, but disc ontinuous, de Rham pushforward.
36 DA VID BEN-ZVI AND DA VID NADLER
