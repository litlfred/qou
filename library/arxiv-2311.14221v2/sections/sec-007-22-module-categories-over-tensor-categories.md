---
doc_id: arxiv-2311.14221v2
doc_title: "FIBRE FUNCTORS AND RECONSTRUCTION OF HOPF ALGEBRAS"
section_id: sec-007-22-module-categories-over-tensor-categories
section_title: "Module categories over tensor categories"
section_number: 2.2
pages: 7-9
source_pdf: 2311.14221v2.pdf
source_sha256: 5aa4126bbb6df6eb
doc_brief: "FIBRE FUNCTORS AND RECONSTRUCTION OF HOPF ALGEBRAS — The main objective of the present paper is to present a ver- sion of the Tannaka-Krein type reconstruction Theorems: If F : B → C is an exact"
---
overC is a category M together with a k-bilinear bifunctor ⊲ :C×M→
M, exact in each variable, endowed with natural associativit y and unit
isomorphisms
mX,Y,M : (X⊗Y )⊲M →X⊲ (Y ⊲M ), ℓ M : 1⊲M →M.
These isomorphisms are subject to the following conditions :
(2.10)
(X⊗ (Y⊗Z))⊲M
((X⊗Y )⊗Z)⊲M (X⊗Y )⊲ (Z⊲M )
X⊲ (Y ⊲(Z⊲M ))
X⊲ ((Y⊗Z)⊲M )
∼
mX⊗Y,Z,M
mX,Y,Z⊲M
mX,Y ⊗Z,M idX ⊲mY,Z,M
for any X,Y,Z ∈C ,M ∈M , as well as
(2.11) (id X⊲ℓ M )mX,1,M = id.
Sometimes we shall also say that M is a C-module category or a represen-
tation ofC.
8 LENTNER AND MOMBELLI
LetM andM′ be a pair of C-module categories. A module functor
is a pair ( F,c ), where F :M→M ′ is a functor equipped with natural
isomorphisms
cX,M :F (X⊲M )→X⊲F (M ),
for X∈C , M∈M , such that
(2.12)
F ((X⊗Y )⊲M )
F (X⊲ (Y ⊲M )) X⊲F (Y ⊲M )
X⊲ (Y ⊲F (M ))
(X⊗Y )⊲F (M )
F (mX,Y,M )
cX,Y ⊲M
idX ⊲cY,M
cX⊗Y,M mX,Y,F (M )
for any X,Y ∈C , M∈M , as well as
ℓF (M )c1,M =F (ℓM ).(2.13)
Module functors are composable, if M′′ is a C-module category and
(G,d ) :M′→M ′′ is another module functor then the composition
(2.14) ( G◦F,e ) :M→M ′′, e X,M =dX,F (M )◦G(cX,M ),
is also a module functor.
A natural module transformation , between module functors ( F,c ) and
(G,d ), is a natural transformation θ :F→G such that
dX,MθX⊲M = (id X ⊲θ M )cX,M,(2.15)
for anyX∈C ,M∈M . The vector space of natural module transformations
will be denoted by Nat m(F,G ). Two module functors F,G are equivalent
if there exists a natural module isomorphism θ : F → G. We denote by
FunC(M,M′) the category whose objects are module functors ( F,c ) from
M toM′ and arrows module natural transformations.
TwoC-modulesM andM′ are equivalent if there exist module functors
F :M→M ′, G :M′→M , and natural module isomorphisms Id M′→
F◦G, Id M→G◦F .
A module category will be called strict if isomorphisms m andl are iden-
tities. Any module category is equivalent to a strict one. We will often
assume that the module category is strict without further me ntion.
FIBRE FUNCTORS AND RECONSTRUCTION OF HOPF ALGEBRAS 9
A right module category overC is a category M equipped with an exact
bifunctor ⊳ :M×C→M and natural isomorphisms
~mM,X,Y :M ⊳(X⊗Y )→ (M ⊳X)⊳Y, r M :M ⊳1→M
such that
(2.16)
M ⊳((X⊗Y )⊗Z)
M ⊳(X⊗ (Y⊗Z)) ( M ⊳X)⊳ (Y⊗Z)
((M ⊳X)⊳Y )⊳Z )
(M ⊳(X⊗Y ))⊳Z
∼
~mM,X,Y ⊗Z
~mM ⊳X,Y,Z
~mM,X ⊗Y,Z ~mM,X,Y ⊳idZ
as well as
(2.17) ( rM ⊳ id X) ~mM,1,X = id.
IfM,M′ are rightC-modules, a module functor from M toM′ is a pair
(T,d ) where T :M→M ′ is a functor and dM,X :T (M ⊳X)→T (M )⊳X
are natural isomorphisms such that for any X,Y ∈C , M∈M :
(2.18)
T (M ⊳(X⊗Y ))
T ((M ⊳X)⊳Y ) T (M ⊳X)⊳Y
(T (M )⊳X )⊳Y
T (M )⊳ (X⊗Y ))
T ( ˜mM,X,Y )
dM ⊳X,Y
dM,X ⊳id Y
dM,X ⊗Y ˜mT (M ),X,Y
as well as
rT (M )dM,1 =T (rM ).(2.19)
