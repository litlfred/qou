---
doc_id: arxiv-2011.12932v2
doc_title: "MODULAR CATEGORIES AND TQFTS BEYOND SEMISIMPLICITY"
section_id: sec-003-appendix-a-ends
section_title: "Appendix A. Ends"
section_number: null
pages: 20-24
source_pdf: 2011.12932v2.pdf
source_sha256: 23709542c5652a29
doc_brief: "MODULAR CATEGORIES AND TQFTS BEYOND SEMISIMPLICITY — Vladimir Turaev discovered in the early years of quantum topol- ogythatthenotionofmodularcategorywasanappropriatestructureforbuild- ing"
---
Let us consider the functorK : C× Cop→ C determined by(X,Y )↦→X⊗Y∗.
A dinatural transformation of targetK is given by an objectU∈ C equipped with
a family{dX :U→X⊗X∗}X∈C of morphisms ofC satisfying
(f⊗ idX∗)◦dX = (idY⊗f∗)◦dY
for every morphismf : X → Y of C, see [47, Sec. IX.4]. The end of K is the
universal dinatural transformation of targetK, which means it is an objectE∈ C
with a dinatural family of structure morphismsjX : E→ X⊗X∗ satisfying the
following condition: for every dinatural transformationU of target K there exists
a unique morphismeU :U→ E such that the diagram
Y⊗X∗
X⊗X∗
Y⊗Y∗
E
U
f⊗ idX∗
jX
idY⊗f∗
jY
dX
dY
eU
(8)
commutes for every morphismf :X→Y of C.
Proposition A.1. If C is a rigid fusion category andΓ (C) ={Vi|i∈I} is a set
of representatives of isomorphism classes of simple objects ofC, then
E∼=
⨁
i∈I
Vi⊗V∗
i ,
and for everyX∈ C the structure morphismjX : E→X⊗X∗ is given by
jX =


n(X,i)∑
a=1
ιa⊗ (πa)∗


i∈I
where{ιa∈ C(Vi,X )| 1⩽ a⩽ n(X,i )} and{πa∈ C(X,Vi)| 1⩽ a⩽ n(X,i )}
are dual bases with respect to composition. Furthermore, ifU∈ C is a dinatural
transformation of targetK with structure morphismsdX :U→X⊗X∗, then the
unique morphismeU :U→ E making (8) into a commutative diagram is given by
eU := (dVi)i∈I.
MODULAR CATEGORIES AND TQFTS BEYOND SEMISIMPLICITY 21
Proof. The fact thatjX is well-deﬁned is a direct consequence of a standard linear
algebra argument. Indeed, for any other pair of dual bases
{κa∈ C(Vi,X )| 1⩽a⩽n(X,i )}, {ρa∈ C(X,Vi)| 1⩽a⩽n(X,i )}
there exist scalarsma
b∈ k for 1⩽a,b⩽n(X,i ) satisfying
κb =
n(X,i)∑
a=1
ma
bιa, π a =
n(X,i)∑
b=1
ma
bρb,
which means
n(X,i)∑
b=1
κb⊗ (ρb)∗ =
n(X,i)∑
a,b=1
ma
bιa⊗ (ρb)∗ =
n(X,i)∑
a=1
ιa⊗ (πa)∗.
Next, we claim that
(f⊗ idX∗)◦jX = (idY⊗f∗)◦jY
for every morphismf :X→Y. Indeed, if
{ιa∈ C(Vi,X )| 1⩽a⩽n(X,i )}, {πa∈ C(X,Vi)| 1⩽a⩽n(X,i )},
{κa∈ C(Vi,Y )| 1⩽a⩽n(Y,i )}, {ρa∈ C(Y,Vi)| 1⩽a⩽n(Y,i )}
are dual bases for every fori∈I, there exist scalars(fi)a
b∈ k for all1⩽a⩽n(Y,i )
and 1⩽b⩽n(X,i ) satisfying
f =
∑
i∈I
fi, f i =
n(Y,i)∑
a=1
n(X,i)∑
b=1
(fi)a
bκa◦πb.
Then, if (jX)i : Vi⊗V∗
i → X⊗X∗ denotes the ith component ofjX for every
X∈ C and i∈I, we have
(f⊗ idX∗)◦ (jX)i = (fi⊗ idX∗)◦ (jX)i =
n(X,i)∑
a=1
((f◦ιa)⊗ (πa)∗)
=
n(X,i)∑
a=1
n(Y,i)∑
b=1
n(X,i)∑
c=1
(fi)b
c ((κb◦πc◦ιa)⊗ (πa)∗)
=
n(Y,i)∑
b=1
n(X,i)∑
c=1
(fi)b
c (κb⊗ (πc)∗)
=
n(Y,i)∑
a=1
n(Y,i)∑
b=1
n(X,i)∑
c=1
(fi)b
c (κa⊗ ((πc)∗◦κ∗
b◦ (ρa)∗))
=
n(Y,i)∑
a=1
(κa⊗ (f∗
i ◦ (ρa)∗)) = (idY⊗f∗
i )◦ (jY )i
= (idY⊗f∗)◦ (jY )i.
Next, we claim that
jX◦eU =dX
for every objectX∈ C. Indeed, we have
jX◦eU =
∑
i∈I
xi∑
a=1
(ιa⊗ (πa)∗)◦dVi =
∑
i∈I
xi∑
a=1
((ιa◦πa)⊗ idX∗)◦dX =dX,
where the second equality follows from the fact that{dX :U→X⊗X∗}X∈C is a
dinatural family.
22 C. BLANCHET AND M. DE RENZI
Finally, we claim thateU is unique. Indeed, consider morphismsfi :U→Vi⊗V∗
i
for i∈I satisfying ∑
i∈I
(jX)i◦fi =dX
for every objectX∈ C. Since (jVi0 )i =δi,i0idVi0⊗V∗
i0
for any ﬁxedi0∈I, we have
fi0 =
∑
i∈I
(jVi0 )i◦fi =dVi0. □
Proposition A.2. If C = H-mod is the category of ﬁnite-dimensional represen-
tations of a ﬁnite-dimensional Hopf algebraH, then
E∼= ad,
and for everyX∈ C the structure morphismjX : ad→X⊗X∗ is given by
jX(x) =
n∑
a=1
(x·va)⊗ϕa,
where{va∈X|1⩽a⩽n} and{ϕa∈X∗|1⩽a⩽n} are dual bases. Furthermore,
if U∈ C is a dinatural transformation of targetK with structure morphismsdX :
U→X⊗X∗, then the uniqueH-module morphismeU :U→ E making (8) into a
commutative diagram is given by
eU := (idH⊗η∗)◦dH,
whereH denotes the regular representation andη : k→H denotes the unit ofH.
Proof. The fact thatjX is well-deﬁned is a direct consequence of a standard linear
algebra argument. Indeed, for any other pair of dual bases
{wa∈X|1⩽a⩽n}, {ψa∈X∗|1⩽a⩽n}
there exist scalarsma
b∈ k for 1⩽a,b⩽n satisfying
wb =
n∑
a=1
ma
bva, ϕ a =
n∑
b=1
ma
bψb,
which means
n∑
b=1
(x·wb)⊗ψb =
n∑
a,b=1
ma
b(x·va)⊗ψb =
n∑
a=1
(x·va)⊗ϕa
for everyx∈H.
The fact thatjX is an intertwiner follows from
jX(adx(y)) =
n∑
a=1
(x(1)yS(x(2))·va)⊗ϕa =
n∑
a=1
(x(1)y·va)⊗ (x(2)·ϕa) =x·jX(y)
for allx,y∈H, where the second equality follows from the fact that
(x·ϕ)(v) =ϕ(S(x)·v)
for allx∈H, v∈X, andϕ∈X∗.
Next, we claim that
(f⊗ idX∗)◦jX = (idY⊗f∗)◦jY
for everyH-module morphismf :X→Y. Indeed, for everyx∈H we have
(f⊗ idX∗)(jX(x)) =
n∑
a=1
f(x·va)⊗ϕa =
n∑
a=1
x·f(va)⊗ϕa =
n∑
a=1
x·va⊗f∗(ϕa)
= (idX⊗f∗)(jX(x)).
MODULAR CATEGORIES AND TQFTS BEYOND SEMISIMPLICITY 23
Next, we claim thateU is an intertwiner. Indeed, if for everyu∈ U we adopt
the notation
dH(u) =
k∑
a=1
dH(u)a⊗dH(u)a
with dH(u)a∈H and dH(u)a∈H∗ for every 1⩽a⩽k, then
eU(u) =
k∑
a=1
dH(u)a(1)dH(u)a.
This means
eU(x·u) =
k∑
a=1
dH(x·u)a(1)dH(x·u)a =
k∑
a=1
dH(u)a(S(x(2))1)x(1)dH(u)a
=
k∑
a=1
dH(u)a(1S(x(2)))x(1)dH(u)a =
k∑
a=1
dH(u)a(1)x(1)dH(u)aS(x(2))
=
k∑
a=1
dH(u)a(1)adx(dH(u)a) = adx(eU(u))
for every x∈ H, where the second equality follows from the fact thatdH is an
intertwiner, and where the fourth equality follows from the fact that it is dinatural.
Next, we claim that
jX◦eU =dX
for everyH-module X. Indeed, if for everyu∈U we adopt the notation
dX(u) =
𝓁∑
a=1
dX(u)a⊗dX(u)a
with dX(u)a∈X and dX(u)a∈X∗ for every 1⩽a⩽𝓁, then
jX(eU(u)) =
k∑
a=1
n∑
b=1
dH(u)a(1)(dH(u)a·vb)⊗ϕb
=
𝓁∑
a=1
n∑
b=1
dX(u)a(1·vb)dX(u)a⊗ϕb =
𝓁∑
a=1
n∑
b=1
dX(u)a(vb)dX(u)a⊗ϕb
=
𝓁∑
a=1
dX(u)a⊗dX(u)a =dX(u),
where the second equality follows from the fact that{dX :U→X⊗X∗}X∈C is a
dinatural family, and thatx↦→x·v deﬁnes anH-module morphism fromH to X
for everyv∈X.
Finally, we claim thateU is unique. Indeed, consider anH-module morphism
f :U→ ad satisfying
jX◦f =dX
for everyH-module X. If we ﬁxX =H then, since
x =
n∑
a=1
ϕa(x)va =
n∑
a=1
ϕa(x· 1)va =
n∑
a=1
ϕa(1)x·va = (idH⊗η∗)(jH(x))
for everyx∈H, we have
f(x) = (idH⊗η∗)(jH(f(x))) = (idH⊗η∗)(dH(x)) =eU(x) □
24 C. BLANCHET AND M. DE RENZI
Just like the coendL, the endE admits the structure of a braided Hopf algebra
in C. When C = H-mod is the category of ﬁnite-dimensional representations of
a ﬁnite-dimensional ribbon Hopf algebraH, this can be expressed in terms of the
structure morphisms
µ :H⊗H→H, η : k→H,
∆ :H→H⊗H, ε :H→ k,
S :H→H,
and of the R-matrixR = R′⊗R′′∈ H⊗H, which determines the Drinfeld ele-
ment u = S(R′′)R′∈ H. This was ﬁrst explicitly spelled out by Majid [45], who
referred to the resulting braided Hopf algebra as thetransmutation of H, denoted
¯H. Thanks to Prop. A.2, as an object ¯H is given by the adjoint representation.
The braided Hopf algebra structure on¯H is given, for allx,y∈ ¯H, by
¯µ(x⊗y) =µ(x⊗y) =xy, ¯η(1) = 1,
¯∆(x) = adR′′(x(2))⊗R′x(1) ¯ε(x) =ε(x),
=x(1)S(R′′)⊗ adR′(x(2)),
¯S(x) =R′′u−1S(x)S(R′)
=u−1S(R′′)S(x)R′,
compare with [41, Sec. 3.4].
