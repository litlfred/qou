---
doc_id: disssubmission
doc_title: "INAUGURAL-DISSERTATION Erlangung der Doktorwürde an der Naturwissenschaftlich-Mathematischen Gesamtfakultät der Ruprecht-Karls-Universität Heidelberg TANNAKIAN CATEGORIES OF PERVER"
section_id: sec-051-37-variation-of-tannaka-groups-in-families-65
section_title: "Variation of Tannaka groups in families 65"
section_number: 3.7
pages: 73-75
source_pdf: DissSubmission.pdf
source_sha256: 207fd5e3dc0d278d
doc_brief: "INAUGURAL-DISSERTATION Erlangung der Doktorwürde an der Naturwissenschaftlich-Mathematischen Gesamtfakultät der Ruprecht-Karls-Universität Heidelberg TANNAKIAN CATEGORIES OF PERVERSE SHEAVES — 121 sec"
---
is a constructible sheaf onS which is concentrated in degree zero
and has geometric stalks
Ws = H0(Xs,Qs) = ω(Ps⊕P∨
s ),
(c) for eachr≤r0 a constructible subsheaf ofW⊗r whose stalks at any
geometric points coincide under the above identiﬁcation with the
cohomology of the direct sum of all skyscraper summands1 = δ0
in the convolutionQ∗rs = Qs∗···∗ Qs.
In general this is too much to expect. However, since the groupsGs =G(Ps)
only depend on the geometric ﬁbres of our abelian scheme and since for
the proof of constructibility we can argue by Noetherian induction on the
dimension dim(S), it will do no harm if we replace our original abelian
scheme by the base change
X′ = X×S S′−→S′
under a quasi-ﬁnite´etale morphismS′−→S and also replaceP∈ D(X)
by its pull-backP′∈ D(X′). In particular, for the proof of the proposition
we are free to replace our base schemeS by arbitrary Zariski-open dense
subsets ofS and also by ﬁnite´etale covers of such subsets.
With this extra freedom, property(a) can be obtained from the general
fact [64, prop. 1.1.7] that for any morphismp : X→ S of varieties with
smooth target varietyS and any P∈ D(X), there is a Zariski-open dense
subsetS′ ↪→S such that the formation of the relative dual
DX/S(P) = RHom(P, p!ΛS)
commutes with every base change that factors overS′ ↪→S. Property(b)will
be obtained in lemma 3.21 after a base change to a ﬁnite´etale cover of some
Zariski-open dense subset ofS, which is needed to make sure that there are
sufﬁciently many characters available. For part(c) consider the relative
convolution powerQ∗r =Ra∗(Q⊠S···⊠SQ) wherea : X×S···× SX−→X
is the group law. We have a relative K¨unneth isomorphism
Rp∗(Q∗r)
∼=−→ (Rp∗(Q))⊗r = W⊗r
as in the absolute case. LetZ⊂X be the zero section of our abelian scheme,
and consider the morphism
ϕ : Rp∗(RHom(ΛZ,Q∗r))−→RHom(ΛS,W⊗r)∼= W⊗r
which corresponds by adjunction to the composite morphismψ given by
the following diagram (where the diagonal arrow on the left comes from
66 Chapter 3 – Perverse sheaves on semiabelian varieties
the adjoint of the relative K¨unneth isomorphism).
RHom(ΛZ,Q∗r)
ψ //
((QQQQQQQQQQQQQ p!(RHom(ΛS,W⊗r))
RHom(p∗(ΛS), p!(W⊗r))
∼=
55kkkkkkkkkkkkkk
As a candidate for the constructible subsheaf in part(c)we take the image of
the induced morphismH 0(ϕ) on the stalk cohomology sheaves in degree
zero. After shrinkingS we can by loc. cit. assume that the occuringRHom
commute with base change. If we put
K = (Ps⊕P∨
s )∗r
and denote byχs the restriction of the characterχ to the geometric ﬁbreXs,
then on stalks we obtain a commutative diagram
H0(Xs,RHom(δ0,Kχs))
H 0(ϕ)s // H0(Xs,Kχs)
⨁
i∈ZExti(δ0, pH−i(K)χs) // Hom(δ0, pH0(K)χs)
OO
where theExt andHomin the lower row refer to the abelian categoryP(Xs)
and where the vertical identiﬁcations come from Gabber’s decomposition
theorem by whichKχs
∼=⨁
i∈Z pHi(K)χs[−i]. The fact thatH 0(ϕ)s factors
over the projection in the lower row follows from the observation that by
part (b) we haveH•(Xs, pH−i(K)χs) = 0 for alli⁄= 0. Hence(c) follows as
well, and we are done. □
In the above proof we have used that after a suitable quasi-ﬁnite´etale
base change there exist enough charactersχ∈ Π(X) so that we can apply
the vanishing theorem from section 3.1 ﬁbre by ﬁbre. More precisely we
have the following result.
LEMMA 3.21. Let P∈ D(X) be a complex which restricts to a perverse
sheaf on each geometric ﬁbre of the abelian scheme X→ S, and suppose
that S is irreducible. Then there exists
• a quasi-ﬁnite´etale morphism f: S′→S,
• a characterχ∈ Π(X′) for the abelian scheme X′ = X×S S′,
such that the direct image of P′ = (idX, f )∗(P)∈ D(X′) under the structure
morphism p: X′→S′ satisﬁes
H i(Rp∗(P′⊗ΛLχ)) = 0 for all i ⁄= 0.
