---
doc_id: erlijman-wenzl-pjm-231-2
doc_title: "Subfactors from braided C* tensor categories"
section_id: sec-001-2-categories
section_title: "Categories"
section_number: 2
pages: 9-13
source_pdf: erlijman-wenzl-pjm-231-2.pdf
source_sha256: 1ee590e6f087b681
toc_source: inferred
doc_brief: "Subfactors from braided C* tensor categories — 10 sections: Front matter; Bimodules; Categories"
---
367
(b) Assume that the A–B-bimodule H decomposes as H = L mi Hi, with Hi
irreducible A–B-bimodules, and let l = dim(EndA,B(H)) = P
i m2
i . Then we
have P
i ind(Hi)≥ind(H)/l, with equality only if dimA(Hi)=mi dimA(H)/l
for all i.
Proof. It is well-known that the inclusion of higher relative commutants M′ ∩
Mk ⊂N′ ∩Mk deﬁnes periodic commuting squares which generate in the limit
a subfactor of index [M : N]. Hence we can use the results of [Wenzl 1988],
Theorem 1.5(iii). It follows that the index is equal to the quotient of the l2-norms
of the weight vectors of M′ ∩Mk and N′ ∩Mk for k sufﬁciently large. Let pλ and
pµ be minimal idempotents in M′ ∩Mk and N′ ∩Mk respectively. Then we have
ind(pνMk) = tr(pν)2[M : N]k and ind(pλMk) = tr(pλ)2[M : N]k+1. Solving for
tr(pλ)2 and tr(pν)2, we obtain
[M : N] =
P
ν ind(pνMk)/[M : N]k
P
λ ind(pλMk)/[M : N]k+1 .
The claimed formula follows from this in the case that our system of bimodules la-
bels the vertices of the principal graph. One obtains the claim for the dual principal
graph by the same proof applied to the inclusion M ⊂M1.
Part (b) is proved using Lagrange multipliers as follows: Let xi = dimA(Hi) and
let d = dimA H. Then the minimum of the function f (x1, . . . , xr) = P x2
i subject
to the condition P mixi = d is obtained for 2xi = λmi, and we deduce from the
constraint that d = λ
2
P m2
i = lλ/2. Hence xi = mid/l and
X
i
(dimA Hi)2 ≥d2
l2
X
i
m2
i = d2/l.
(∗)
Now observe that if pi is the projection onto the submodule Hi ⊂H, we have
tr(pi) = dimA(Hi)/ dimA(H) and ind(Hi) = tr(pi)2ind(H) (again see [Wenzl
1988], Theorem 1.5(iii)). The claim follows from this after multiplying (∗) by
ind(H)/d2.
□
2. Categories
In this section we deal with categories which can be considered as generalizations
of the representation categories of ﬁnite groups. This allows us to deal simulta-
neously with categories of bimodules of von Neumann factors, fusion categories
(which can be constructed using quantum groups or loop groups) and categories ob-
tained from unitary braid representations. For more details, we refer to [Mac Lane
1998], [Freyd 1964] for general categorical notions, and to [Kassel 1995], [Turaev
1994] for tensor categories; our treatment of traces also uses results from [Longo
and Roberts 1997].
368
JULIANA ERLIJMAN AND HANS WENZL
2A. General deﬁnitions. We recall some basic deﬁnitions and set up notations.
In the following, C will always denote a strict monoidal complex tensor category
with unit 1. This means that C is a category with a functor ⊗: C×C→C called the
tensor product which satisﬁes certain associativity conditions such as the Pentagon
Axiom. There are similar axioms involving the morphisms lX : 1 ⊗X →X and
rX : X ⊗1 →X called the left and right unit constraints. Moreover, C being a
complex category just means that the homomorphisms Hom(X, Y) form a complex
vector space for any objects X and Y in C.
The complex tensor category C is called a ∗tensor category if there exists a
contragredient complex conjugate functor ∗: C →C which is compatible with ⊗.
This means in detail that:
– if f ∈Hom(X, Y), then f ∗∈Hom(Y, X),
– (αf )∗= ¯α f ∗for all α ∈C and f ∈Hom(X, Y),
– ( f g)∗= g∗f ∗for f ∈Hom(X, Y) and g ∈Hom(U, X),
– ( f ⊗g)∗= f ∗⊗g∗for f ∈Hom(X, Y) and g ∈Hom(U, V ),
– 1∗
X = 1X for the identity morphism 1X for any object X in C.
2B. Duality and Frobenius reciprocity. An object X in a strict monoidal category
C is called left rigid if there exists an object ¯X ∈C and a pair of morphisms
iX :1→X⊗¯X and dX : ¯X⊗X →1 such that the maps (1X ⊗dX)(iX ⊗1X): X →X
and (dX ⊗1 ¯X)(1X ⊗i ¯X) : ¯X →¯X are 1X and 1 ¯X. An object X is called right rigid
if we can ﬁnd an object ¯X′ and morphisms i′
X : 1 →¯X′ ⊗X and d′
X : X ⊗¯X′ →1
satisfying analogous identities. It is easy to check that in a ∗category any left rigid
object is also right rigid, with ¯X′ = ¯X, i′
X = d∗
X and d′
X = i∗
X. Hence we will in the
following only talk about rigid objects. A category C is called rigid if every object
of C is rigid.
With this notion of duality, we also have the usual Frobenius reciprocity iso-
morphism between Hom(V, W ⊗¯X) and Hom(V ⊗X, W) for any objects V, W
in C. One checks easily that these isomorphisms are given by the maps
a 7→(1W ⊗dX) ◦(a ⊗1X)
and
b 7→(b ⊗1Y) ◦(1V ⊗iX)
for a ∈Hom(V, W ⊗X) and b ∈Hom(V ⊗Y, W). In particular, one obtains as a
special case that dim Hom(1, X ⊗¯X) = dim End(X) = 1 if X is a simple object.
Hence the morphisms iX and dX are unique up to scalar multiples for X simple. We
shall say that the rigidity morphisms iX and dX are normalized if i∗
XiX = dXd∗
X∗.
2C. Dimension, trace and conditional expectation. In the following we always
assume the rigidity morphisms iX and dX to be normalized for any object X. If X is
simple, this can always be assumed after some rescaling in view of the discussion
SUBFACTORS FROM BRAIDED C∗TENSOR CATEGORIES
369
in the last section. For normalized rigidity morphisms, we can now deﬁne the
dimension of a simple object X to be equal to the scalar
dim(X) = i∗
XiX = dXd∗
X.
Of course, we would like the dimension to be additive with respect to a decomposi-
tion X = L Wi, with the Wi being simple objects. To do so, we deﬁne morphisms
φi : Wi →X such that φ∗
i φ j = δi j1Wi and P
i φiφ∗
i = 1X, and we deﬁne
(2-1)
iX =
X
(φi ⊗¯φi)iWi,
dX =
X
dWi( ¯φ∗
i ⊗φ∗
i ),
where the ¯φi are the analogous morphisms for the decomposition of the dual ¯X =
P L
i ¯Wi. Then it is easy to check that these morphisms satisfy the rigidity axiom,
and they are normalized if the φi are so. Moreover, one also checks that these
morphisms yield the desired additivity property of the dimension function.
Additionally, the dimension function should be multiplicative with respect to
the tensor product. If X ⊗Y is a tensor product of simple objects X and Y, we
obtain normalized rigidity morphisms
iX⊗Y = (1X ⊗iY ⊗1 ¯X)iX,
dX⊗Y = dY(1 ¯X ⊗dX ⊗1X).
It can be shown that these rigidity morphisms deﬁne the same dimension as the one
we obtain from the decomposition X⊗Y ∼=L
i Wi, with Wi simple and with rigidity
morphisms as deﬁned in the last paragraph. It will be convenient to represent the
rigidity morphisms iX and dX, by the following pictures:
1
dX
X
¯X
1
X
¯X
iX
Figure 1. Rigidity morphisms.
In a ∗tensor category we deﬁne the categorical trace of an endomorphism f ∈
End(X) by
(2-2)
TrX( f ) = i∗
X ◦( f ⊗1 ¯X) ◦iX ∈End(1).
If Z = L mi Xi, where Xi is a simple object, and mi is the multiplicity of Xi in Z,
we can write an element f ∈End(Z) in the form f = L fi, where fi ∈End(mi Xi)
can be viewed as an mi × mi matrix. Deﬁning rigidity morphisms iZ, dZ with
respect to this decomposition, and using (2-1), one checks easily that
TrZ( f ) =
X
dim(Xi) Tr( fi),
370
JULIANA ERLIJMAN AND HANS WENZL
where Tr( fi) is the usual trace of a matrix. This shows that we obtain a well-
deﬁned trace for End(Z) for any object Z, and that TrZ( f g) = TrZ(g f ) for any
f, g ∈End(Z). Moreover, using this formula, one shows as well that we can deﬁne
the trace also by
TrX( f ) = i∗
¯X ◦(1 ¯X ⊗f ) ◦i ¯X ∈End(1).
This shows that ∗-categories satisfy the axioms of a spherical category (see [Barrett
and Westbury 1999]).
The normalized trace trX on End(X) is deﬁned by trX( f ) = TrX( f )/(dim X).
In the following we will often just write Tr, tr for the trace or normalized trace
when it is clear for which object it is deﬁned.
Conditional expectations can also be very naturally deﬁned using our categorical
deﬁnitions. Let X be an object. Let A = End(X) ∼= A ⊗1V ⊂B = End(X ⊗V ).
We deﬁne the map E A from B onto A by
E A(b) =
1
dim V (1X ⊗i∗
V )(b ⊗1 ¯V )(1X ⊗iV );
in the tangle picture, E A(b) is obtained from b by closing up the tangle with color
V and renormalizing by 1/ dim V .
b
X
V
EX(b) =
1
dim V
Figure 2. Conditional expectation.
It is known and easy to check that this deﬁnition of conditional expectation coin-
cides with the usual deﬁnition of conditional expectation in operator algebras (see
[Orellana and Wenzl 2002, Proposition 1.4], for instance). Actually, one can show
more: Let X1, X2, X3 be objects in our ∗tensor category C. Deﬁne the algebras
A =End(X2), B =End(X1⊗X2), C =End(X2⊗X3) and D =End(X1⊗X2⊗X3).
We can consider all these algebras as subalgebras of D, say by identifying A with
1X1 ⊗End(X2) ⊗1X3. The next proposition now follows immediately from the
graphical description of the conditional expectations.
Proposition 2.1. The algebras A, B, C, D form a commuting square; that is,
EB EC = E A = EC EB.
2D. Braided tensor categories. A strict monoidal category C is called braided if,
for any objects X, Y in C, there exists a natural isomorphism cX,Y : X ⊗Y →Y ⊗X
called the braiding such that:
cX,Y⊗Z = (1Y ⊗cX,Z)(cX,Y ⊗1Z)
SUBFACTORS FROM BRAIDED C∗TENSOR CATEGORIES
371
and
cX⊗Y,Z = (cX,Z ⊗1Y)(1X ⊗cY,Z).
Naturality means that for any morphisms f : X →X′ and g : Y →Y ′
(g ⊗f ) ◦cX,Y = cX′,Y ′ ◦( f ⊗g).
Finally, we also require that c1,X = 1X = cX,1 under the isomorphisms 1 ⊗X ∼=
X ∼= X ⊗1.
2E. C∗tensor categories. We call a complex ∗tensor category a C∗tensor cate-
gory if
(a) for any objects X, Y in C the space Hom(X, Y) is a Hilbert space with inner
product (a, b) = Tr(b∗a) for a, b ∈Hom(X, Y),
(b) for any objects X, Y in C the algebra End(Y) is a C∗-algebra acting on the
Hilbert space Hom(X, Y).
Observe that these deﬁnitions imply that the dimensions of all objects are posi-
tive. A braided C∗tensor category is a C∗tensor category with a braiding for
which all its braiding morphisms are unitary operators. For examples of C∗-tensor
categories, see Section 6A.
