---
doc_id: arxiv-0711.4229v2
doc_title: "MODIFIED QUANTUM DIMENSIONS AND RE-NORMALIZED LINK INVARIANTS"
section_id: sec-003-4-the-quasi-functor-f
section_title: "The quasi-functor F'"
section_number: 4
pages: 5-8
source_pdf: 0711.4229v2.pdf
source_sha256: 2e6cc61069016627
toc_source: outline
doc_brief: "MODIFIED QUANTUM DIMENSIONS AND RE-NORMALIZED LINK INVARIANTS — In this paper we give a re-normalization of the Reshetikhin-Turaev quantum invariants of links, by modiﬁed quantum dimensions."
---
In this section we extend the invariant F ′ to C-colored ribbon graphs with endpoints. This
leads us to a notion of a quasi-functor which we brieﬂy discuss in a more general setting. This
section is essentially independent from the rest of the paper.
Let E be a category. Given a map M : Ob(E)×Ob(E) →Sets we will use the notation m ∈M
to mean that there exist two objects X and Y of E such that m ∈M(X, Y ).
Deﬁnition 4. A E-bimodule is a map M : Ob(E)×Ob(E) →Sets endowed with two operations:
⊲: HomE(Y, Z) × M(X, Y ) →M(X, Z)
⊳: M(Y, Z) × HomE(X, Y ) →M(X, Z)
where X, Y and Z are any objects of E. Given morphisms f and g of E and m ∈M we require
that
(1) (f ◦g) ⊲m = f ⊲(g ⊲m).
(2) m ⊳(f ◦g) = (m ⊳f) ⊳g.
(3) (f ⊲m) ⊳g = f ⊲(m ⊳g).
whenever the operations in these equalities make sense.
Remark that if one has Id ⊲m = m ⊳Id = m for all m ∈M these Axioms mean that M is a
bifunctor contravariant in the ﬁrst place and covariant in the second place with M(X, f)(m) =
f ⊲m and M(f, Z)(m) = m ⊳f.
Example 5. The functor HomE is a E-bimodule with ⊳= ⊲= ◦.
Example 6. Let K be an integral domain and suppose that (M, ⊲, ⊳) is a E-bimodule with
values in K-modules. If Γ is a K-module then we deﬁne an E-bimodule HE by HE(X, Y ) =
HomK(M(Y, X), Γ) with operations ⊲and ⊳deﬁned as follows. Let f : Y →Z and f ′ : Z →X
be morphisms of E and let φ be an element of HE(X, Y ) then
(f ⊲φ)(m) = φ(m ⊳f)
and
(φ ⊳f ′)(m′) = φ(f ′ ⊲m′)
where m ∈M(Z, X) and m′ ∈M(Y, Z).
Suppose now that E is a tensor Ab-category and that M is a E-bimodule which takes values
in abelian groups. We assume that the operations ⊲and ⊳are bilinear.
6
NATHAN GEER, BERTRAND PATUREAU-MIRAND, AND VLADIMIR TURAEV
Deﬁnition 7. We call M a monoidal E-bimodule if it is endowed with two bilinear operations:
: HomE(X, Y ) × M(X′, Y ′) →M(X ⊗X′, Y ⊗Y ′)
: M(X, Y ) × HomE(X′, Y ′) →M(X ⊗X′, Y ⊗Y ′)
such that for any morphisms f, g and h in E and any m ∈M,
(1) (f ⊗g)
m = f
(g
m).
(2) m
(f ⊗g) = (m
f)
g.
(3) f
(m
g) = (f
m)
g.
(4) (f ◦g)
(h ⊲m) = (f ⊗h) ⊲(g
m).
(5) (h ⊲m)
(f ◦g) = (h ⊗f) ⊲(m
g).
(6) (f ◦g)
(m ⊳h) = (f
m) ⊳(g ⊗h).
(7) (m ⊳h)
(f ◦g) = (m
f) ⊳(f ⊗g).
whenever the operations in these equalities make sense.
Deﬁnition 7 can be illustrated by pictures. For example, Axiom (4) is given by
f
◦
g
h
∇
m
=
f ⊗h
∇
g
m
where the composition operations should be read from the top to the bottom and tensor oper-
ations from left to right.
Example 8. The functor HomE is a monoidal E-bimodule with ⊳= ⊲= ◦and
=
= ⊗.
Suppose that G : D →E is a monoidal functor between two tensor Ab-categories. Let M be
a monoidal E-bimodule and M′ be a monoidal D-bimodule.
Deﬁnition 9. A G-bilinear monoidal quasi-functor G′ : M′ →M is a family of maps G′ :
M′(X, Y ) →M(G(X), G(Y )) indexed by the objects X and Y of E, such that for every m ∈
M′(X, Y ) and every morphism f of D one has:
(1) G′(f ⊲m) = G(f) ⊲G′(m).
(2) G′(m ⊳f) = G′(m) ⊳G(f).
(3) G′(f
m) = G(f)
G′(m).
(4) G′(m
f) = G′(m)
G(f).
whenever the operations in these equalities make sense.
Let us now go back to the situation of Section 3. Deﬁne a C-bimodule structure on HC =
HomK(HomC, F) as in Example 6. In particular, for any objects U, V of C we have
HC(U, V ) = HomK(HomC(V, U), F)
and if f and g are morphisms of C and φ ∈HC then
(f ⊲φ)(g) = φ(g ◦f) and (φ ⊳f)(g) = φ(f ◦g)
when these operations make sense.
To give HC a monoidal structure, let us recall the partial traces in C: if f ∈HomC(X ⊗Z, Y ⊗
Z) set trR(f) = (IdX ⊗d′
Z)◦(f⊗IdZ∗)◦(IdX ⊗bZ) ∈HomC(X, Y ) and if f ∈HomC(X⊗Y, X⊗Z)
set trL(f) = (dX ⊗IdZ) ◦(IdX∗⊗f) ◦(b′
X ⊗IdY ) ∈HomC(Y, Z).
Then
: HomC(U, V ) × HC(U ′, V ′) →HC(U ⊗U ′, V ⊗V ′)
: HC(U, V ) × HomC(U ′, V ′) →HC(U ⊗U ′, V ⊗V ′)
are deﬁned as follows.
MODIFIED QUANTUM DIMENSIONS AND RE-NORMALIZED LINK INVARIANTS
7
(1) If f ∈HomC(U, V ) and φ ∈HC(U ′, V ′) then f
φ ∈HC(U ⊗U ′, V ⊗V ′) is given by
(f
φ)(g) = φ(trL(g ◦(f ⊗IdV ′))).
where g is any element of HomC(V ⊗V ′, U ⊗U ′). This operation can be represented by
the following diagram:
❄❄
g
V
V ′
U
U′
7→φ








❄
❄
f
g








(2) If f ∈HomC(U ′, V ′) and φ ∈HC(U, V ) then φ
f ∈HC(U ⊗U ′, V ⊗V ′) is given by
(φ
f)(g) = φ(trR(g ◦(IdU′ ⊗f)))
where g is any element of HomC(V ⊗V ′, U⊗U ′). Again this operation can be represented
by the following diagram:
❄❄
g
V
V ′
U
U′
7→φ








❄
❄
f
g








One can check that these maps make HC a monoidal C-bilinear module.
Fix now a simple ambidextrous object J in C and a non-zero element d0 of F. Set A = A(J).
Let RibA be the monoidal RibC-bimodule deﬁned as follows. The operations of RibA are the
composition and tensor product of RibC, i.e. ⊳= ⊲= ◦and
=
= ⊗. Let V and W be
objects of RibC then RibA(V, W) is the set of C-colored ribbon graphs in HomC(V, W) with at
least one color in A. In particular, RibA(∅, ∅) = LA.
Theorem 10. The invariant F ′ : LA →F extends naturally to a F-bilinear monoidal quasi-
functor F ′ : RibA →HC by the formula
F ′(T )(g) = F ′(trRibC(T ◦cg))
where T ∈RibA(V, W), g ∈HomC(F(W), F(V )) and where cg is a coupon labeled by g. This
expresion can be represented by the following diagram:
F ′(T ) : g 7→F ′




T
g




Proof. Let T and T ′ be morphisms of RibC and RibA, respectively. Suppose that T ◦T ′ is
deﬁned. Let T ′′ be the trace in RibC of T ◦T ′ and let C be a coupon labeled by F(T ′). The
proof follows from the fact that
F ′(T ′′) = F ′(trRibC(T ◦C)) = F ′(T )(F(T ′)).
For example, we will now check (1) of Deﬁntion 9. Let T and T ′ be as above. Let g be a
morphism of C and let cg is a coupon labeled by g. Suppose that g is a morphism such that
8
NATHAN GEER, BERTRAND PATUREAU-MIRAND, AND VLADIMIR TURAEV
F ′(T ⊲T ′)(g) is deﬁned. If cg is a coupon labeled by g then we have
F ′(T ⊲T ′)(g)
= F ′(trRibC(T ◦T ′ ◦cg)) = F ′(T ′)(F(cg ◦T ))
= F ′(T ′)(g ◦F(T )) = (F(T ) ⊲F ′(T ′))(g).
Checking (2)-(4) of Deﬁntion 9 are similar.
□
