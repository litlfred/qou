---
doc_id: arxiv-0908.4305v3
doc_title: "Higher Dimensional Algebra VII: Groupoidification"
section_id: sec-010-a-review-of-groupoids
section_title: "A Review of Groupoids"
section_number: null
pages: 58-67
source_pdf: 0908.4305v3.pdf
source_sha256: ab8d2b335b026a36
doc_brief: "Higher Dimensional Algebra VII: Groupoidification — Groupoidiﬁcation is a form of categoriﬁcation in which vect or spaces are replaced by groupoids and linear operators are replaced by spans of"
---
Deﬁnition 50. A groupoid is a category in which all morphisms are invertible.
Deﬁnition 51. We denote the set of objects in a groupoid X by Ob(X) and
the set of morphisms by Mor(X).
Deﬁnition 52. A functor F :X →Y between categories is a pair of functions
F : Ob(X) → Ob(Y ) and F : Mor(X) → Mor(Y ) such that F (1x) = 1 F (x) for
x ∈ Ob(X) and F (gh) = F (g)F (h) for g,h ∈ Mor(X).
58
Deﬁnition 53. A natural transformationα :F ⇒G between functorsF,G : X →
Y consists of a morphism αx : F (x) → G(x) in Mor(Y ) for each x ∈ Ob(X)
such that for each morphism h : x → x′ in Mor(X) the following naturality
square commutes:
F (x)
α x /d47/d47
F (h)
/d15/d15
G(x)
G(h)
/d15/d15
F (x′) α x′
/d47/d47G(x′)
Deﬁnition 54. A natural isomorphism is a natural transformation α :F ⇒
G between functors F,G : X →Y such that for each x ∈ X, the morphism αx
is invertible.
Note that a natural transformation between functors between groupoids is nec-
essarily a natural isomorphism.
In what follows, and throughout the paper, we write x ∈ X as shorthand
for x ∈ Ob(X). Also, several places throughout this paper we have used the
notationα ·F orF ·α to denote operations combining a functor F and a natural
transformation α. These operations are called ‘whiskering’:
Deﬁnition 55. Given groupoids X, Y and Z, functors F : X →Y , G : Y →Z
and H : Y → Z, and a natural transformation α : G ⇒ H, there is a natural
transformationα ·F : GF ⇒HF called the right whiskering of α by F . This
assigns to any object x ∈ X the morphism αF (x) : G(F (x)) → H(F (x)) in Z,
which we denote as (α ·F )x. Similarly, given a groupoid W and a functor
J : Z → W , there is a natural transformation J · α : JG ⇒ JH called the
left whiskering of α by J. This assigns to any object y ∈ Y the morphism
J(αy) :JG(y) →JH (y) in W , which we denote as (J ·α)y.
Deﬁnition 56. A functor F : X → Y between groupoids is called an equiva-
lence if there exists a functor G : Y →X, called the weak inverse of F , and
natural isomorphisms η : GF ⇒ 1X and ρ : FG ⇒ 1Y . In this case we say X
and Y are equivalent.
Deﬁnition 57. A functor F : X → Y between groupoids is called faithful if
for each pair of objects x,y ∈X the function F : hom(x,y ) → hom(F (x),F (y))
is injective.
Deﬁnition 58. A functor F : X → Y between groupoids is called full if for
each pair of objects x,y ∈X, the function F : hom(x,y ) → hom(F (x),F (y)) is
surjective.
Deﬁnition 59. A functor F : X → Y between groupoids is called essentially
surjective if for each object y ∈Y , there exists an object x ∈X and a morphism
f :F (x) →y in Y .
A functor has all three of the above properties if and only if the fun ctor is an
equivalence. It is often convenient to prove two groupoids are equ ivalent by
exhibiting a functor which is full, faithful and essentially surjective.
59
Deﬁnition 60. A map from the span of groupoids
S
q
/d127/d127/d127/d127/d127/d127/d127/d127/d127 p
/d31/d31/d64/d64/d64/d64/d64/d64/d64
Y X
to the span of groupoids
S′
q′
/d126/d126/d126 /d126 /d126/d126 /d126 /d126/d126 p′
/d32/d32/d65/d65/d65/d65/d65/d65/d65
Y X
is a functor F : S → S′ together with natural transformations α : p ⇒ p′F ,
β :q ⇒q′F .
Deﬁnition 61. An equivalence of spans of groupoids
S
q
/d127/d127/d127/d127/d127/d127/d127/d127/d127 p
/d31/d31/d64/d64/d64/d64/d64/d64/d64 S′
q′
/d126/d126/d126/d126 /d126 /d126/d126 /d126 /d126 p′
/d32/d32/d65/d65/d65/d65/d65/d65/d65
Y X Y X
is a map of spans (F,α,β ) fromS toS′ together with a map of spans (G,α ′,β ′)
fromS′ to S and natural isomorphisms γ : GF ⇒ 1 and γ′ : FG ⇒ 1 such that
the following equations hold:
1p = (p ·γ)(α′ ·F )α 1q = (q ·γ)(β′ ·F )β
1p′ = (p′ ·γ′)(α ·G)α′ 1q′ = (q′ ·γ′)(β ·G)β′.
Lemma 62. Given equivalent groupoids X and Y , |X| = |Y |.
Proof. From a functor F : X →Y between groupoids, we can obtain a function
F : X →Y . If F is an equivalence, F is a bijection. Since these are the indexing
sets for the sum in the deﬁnition of groupoid cardinality, we just nee d to check
that for a pair of elements [ x] ∈X and [y] ∈Y such that F ([x]) = [y], we have
|Aut(x)| = |Aut(y)|. This follows from F being full and faithful, and that the
cardinality of automorphism groups is an invariant of an isomorphism c lass of
objects in a groupoid. Thus,
|X| =
∑
x∈X
1
|Aut(x)| =
∑
y∈Y
1
|Aut(y)| = |Y |.
Lemma 63. Given a diagram of groupoids
S
B
T
p
/d31/d31/d63/d63/d63/d63/d63/d63/d63/d63/d63/d63/d63/d63/d63/d63
q
/d127/d127/d127/d127/d127/d127/d127/d127/d127/d127/d127/d127/d127/d127/d127/d127
F /d47/d47
α
/d59/d67/d127/d127/d127 /d127/d127/d127
60
where F is an equivalence of groupoids, the restriction of F to the full inverse
image p−1(b)
F |p−1(b) :p−1(b) →q−1(b)
is an equivalence of groupoids, for any object b ∈B.
Proof. It is suﬃcient to check that F |p−1(b) is a full, faithful, and essentially
surjective functor from p−1(b) to q−1(b). First we check that the image of
F |p−1(b) indeed lies in q−1(b). Given b ∈B andx ∈p−1(b), there is a morphism
αx : p(x) → qF (x) in B. Since p(x) ∈ [b], then qF (x) ∈ [b]. It follows that
F (x) ∈ q−1(b). Next we check that F |p−1(b) is full and faithful. This follows
from the fact that full inverse images are full subgroupoids. It is c lear that a
full and faithful functor restricted to a full subgroupoid will again be full and
faithful. We are left to check only that F |p−1(b) is essentially surjective. Let
y ∈q−1(b). Then, since F is essentially surjective, there exists x ∈S such that
F (x) ∈ [y]. Since qF (x) ∈ [b] and there is an isomorphism αx : p(x) →qF (x), it
follows thatx ∈q−1(b). So F |p−1(b) is essentially surjective. We have shown that
F |p−1(b) is full, faithful, and essentially surjective, and, thus, is an equivalen ce
of groupoids.
The data needed to construct a weak pullback of groupoids is a ‘cosp an’:
Deﬁnition 64. Given groupoidsX andY , a cospan fromX toY is a diagram
Y
g
/d31/d31/d64/d64/d64/d64/d64/d64/d64 X
f/d126/d126/d126 /d126/d126 /d126/d126 /d126/d126
Z
whereZ is groupoid and f : X →Z and g :Y →Z are functors.
We next prove a lemma stating that the weak pullbacks of equivalent c ospans are
equivalent. Weak pullbacks, also called iso-comma objects, are part of a much
larger family of limits called ﬂexible limits . To read more about ﬂexible limits,
see the work of Street [40] and Bird [8]. A vastly more general theo rem than
the one we intend to prove holds in this class of limits. Namely: for any p air of
parallel functors F,G from an indexing category to Cat with a pseudonatural
equivalence η : F ⇒ G, the pseudo-limits of F and G are equivalent. But to
make the paper self-contained, we strip this theorem down and give a hands-on
proof of the case we need.
To show that equivalent cospans of groupoids have equivalent weak pull-
backs, we need to say what it means for a pair of cospans to be equiv alent. As
stated above, this means that they are given by a pair of parallel fu nctors F,G
from the category consisting of a three-element set of objects {1, 2, 3} and two
morphisms a : 1 → 3 and b : 2 → 3. Further there is a pseudonatural equiv-
alence η : F → G. In simpler terms, this means that we have equivalences
61
ηi : F (i) → G(i) for i = 1, 2, 3, and squares commuting up to natural isomor-
phism:
F (1)
F (3)
G(1)
G(3)
F (1)
F (3)
G(1)
G(3)
η 1
/d15/d15
F (a) /d47/d47
η 3
/d15/d15
G(a)
/d47/d47
η 2
/d15/d15
F (b) /d47/d47
η 3
/d15/d15
G(b)
/d47/d47
v /d59/d67/d127/d127/d127/d127/d127
/d127/d127/d127/d127/d127
w /d59/d67/d127/d127/d127/d127/d127
/d127/d127/d127/d127/d127
For ease of notation we will consider the equivalent cospans:
Y
g
/d30/d30/d62/d62/d62/d62/d62/d62/d62/d62 X
f/d127/d127/d0/d0/d0/d0/d0/d0/d0/d0 ˆY
ˆg /d30/d30/d62/d62/d62/d62/d62/d62/d62 ˆX
ˆf/d127/d127/d0/d0/d0/d0/d0/d0/d0
Z ˆZ
with equivalences ˆx : X → ˆX, ˆy : Y → ˆY , and ˆz : Z → ˆZ and natural isomor-
phisms v : ˆzf ⇒ ˆf ˆx and w : ˆzg ⇒ ˆg ˆy.
Lemma 65. Given equivalent cospans of groupoids as described above, t he weak
pullback of the cospan
Y
g
/d31/d31/d64/d64/d64/d64/d64/d64/d64 X
f/d126/d126/d126 /d126/d126 /d126/d126 /d126/d126
Z
is equivalent to the weak pullback of the cospan
ˆY
ˆg /d30/d30/d62/d62/d62/d62/d62/d62/d62 ˆX
ˆf/d127/d127/d0/d0/d0/d0/d0/d0/d0
ˆZ
Proof. We construct a functor F between the weak pullbacks XY and ˆX ˆY and
show that this functor is an equivalence of groupoids, i.e., that it is fu ll, faithful
and essentially surjective. We recall that an object in the weak pullb ack XY
is a triple ( r,s,α ) with r ∈ X, s ∈ Y and α : f (r) → g(s). A morphism in
ρ : (r,s,α ) → (r′,s ′,α ′) in XY is given by a pair of morphisms j : r →r′ in X
and k : s →s′ in Y such that g(k)α =α′f (j). We deﬁne
F : XY → ˆX ˆY
on objects by
(r,s,α ) ↦→(ˆx(r), ˆy(s),w −1
s ˆz(α)vr)
62
and on a morphism ρ by sending j to ˆx(j) and k to ˆy(k). To check that this
functor is well-deﬁned we consider the following diagram:
ˆf ˆx(r)
vr /d47/d47
ˆf ˆx(j)
/d15/d15
ˆzf (r)
ˆz(α ) /d47/d47
ˆzf (j)
/d15/d15
ˆzg(s)
w−1
s /d47/d47
ˆzg(k)
/d15/d15
ˆg ˆy(s)
ˆg ˆy(k)
/d15/d15
ˆf ˆx(r′) vr′
/d47/d47 ˆzf (r′)
ˆz(α ′)
/d47/d47 ˆzg(s′)
w−1
s′
/d47/d47 ˆg ˆy(s′)
The inner square commutes by the assumption that ρ is a morphism in XY .
The outer squares commute by the naturality of v and w. Showing that F
respects identities and composition is straightforward.
We ﬁrst check thatF is faithful. Let ρ,σ : (r,s,α ) → (r′,s ′,α ′) be morphisms
in XY such that F (ρ) = F (σ). Assume ρ consists of morphisms j : r → r′,
k : s →s′ and σ consists of morphisms l :r →r′ andm : s →s′. It follows that
ˆx(j) = ˆx(l) and ˆy(k) = ˆy(m). Since ˆx and ˆy are faithful we have that j =l and
k =m. Thus, we have shown that ρ =σ and F is faithful.
To show that F is full, we assume ( r,s,α ) and (r′,s ′,α ′) are objects in XY
and ρ : (ˆx(r), ˆy(s), ˆz(α)) → (ˆx(r′), ˆy(s′), ˆz(α′)) is a morphism in ˆX ˆY consisting
of morphisms j : ˆx(r) → ˆx(r′) and k : ˆy(s) → ˆy(s′). Since ˆx and ˆy are full, there
exist morphisms ˜j : r →r′ and ˜k : s →s′ such that ˆx(˜j) = j and ˆy(˜k) = k. We
consider the following diagram:
ˆz(f (r))
v−1
r /d47/d47
ˆz(f (˜j))
/d15/d15
ˆf ˆx(r)
ˆz(α ) /d47/d47
ˆf ˆx(˜j)
/d15/d15
ˆg ˆy(s)
ws /d47/d47
ˆg ˆy(˜k)
/d15/d15
ˆz(g(s))
ˆz(g(˜k))
/d15/d15
ˆz(f (r′))
v−1
r′
/d47/d47 ˆf ˆx(r′) ˆz(α ′)
/d47/d47 ˆg ˆy(s′) ws
/d47/d47 ˆz(g(s′))
The center square commutes by the assumption that ρ is a morphism in ˆX ˆY , and
the outer squares commute by naturality of v andw. Since ˆz is full, there exists
morphisms ¯α : f (r) → g(s) and ¯α′ : f (r′) → g(s′) such that ˆz(¯α) = ws ˆz(α)v−1
r
and ˆz( ¯α′) = ws′ ˆz(α′)v−1
r′ . Now since ˆz is faithful, we have that
f (r) ¯α /d47/d47
f (˜j)
/d15/d15
g(s)
g(˜k)
/d15/d15
f (r′) ¯α ′
/d47/d47g(s′)
commutes. Hence, F is full.
To showF is essentially surjective we let (r,s,α ) be an object in ˆX ˆY . Since ˆx
and ˆy are essentially surjective, there exist ˜r ∈X and ˜s ∈Y with isomorphisms
β : ˆx(˜r) →r and γ : ˆy(˜s) →s. We thus have the isomorphism:
ˆz(f (˜r))
v˜r−1
− → ˆf (ˆx(˜r))
ˆf (β )
− → ˆf (r)
α
− →ˆg(s)
ˆg(γ −1)
− → ˆg(ˆy(˜s))
w˜s
− →ˆz(g(˜s))
63
Since ˆz is full, there exists an isomorphism µ : f (˜r) → g(˜s) such that ˆz(µ) =
wsˆg(γ−1)α ˆf (β)v−1
r . We have constructed an object (˜r, ˜s,µ ) in XY and we need
to ﬁnd an isomorphism from F ((˜r, ˜s,µ ) = (ˆx(˜r), ˆy(˜s),w −1
s ˆz(µ)vr) to ( r,s,α ).
This morphism consists of β : ˆx(˜r) → r and γ : ˆy(˜s) → s. That this is an
isomorphism follows fromβ,γ being isomorphisms and the following calculation:
ˆg(γ)w−1
s ˆz(µ)vr = ˆg(γ)w−1
˜s w˜sˆg(γ−1)α ˆf (β)v−1
˜r v˜r
= α ˆf (β)
We have now shown that F is essentially surjective, and thus an equivalence of
groupoids.
References
[1] M. Aguiar and S. Mahajan, Monoidal functors, species and Hopf algebras,
available at ⟨http:/!/www.math.tamu.edu/∼maguiar/a.pdf⟩.
[2] J. Baez, Groupoidiﬁcation. Available at
⟨http:/ /math.ucr.edu/home/baez/groupoidiﬁcation/⟩.
[3] J. Dolan and J. Baez, Categoriﬁcation, in Higher Category Theory, eds.
E. Getzler and M. Kapranov, Contemp. Math. 230, American Mathe mat-
ical Society, Providence, Rhode Island, 1998, pp. 1–36. Also availa ble as
arXiv:math/9802029.
[4] J. Baez and J. Dolan, From ﬁnite sets to Feynman diagrams, in Math-
ematics Unlimited—2001 and Beyond , eds. B. Engquist and W. Schmid,
Springer, Berlin, 2001, pp. 29–50. Also available as arXiv:math/0004 133.
[5] K. Behrend, The Lefschetz trace formula for algebraic stacks , Invent. Math.
112 (1993), 127–149.
[6] F. Bergeron, G. Labelle, and P. Leroux, Combinatorial Species and Tree-
Like Structures , Cambridge U. Press, Cambridge, 1998.
[7] J. Bernstein, I. Frenkel and M. Khovanov, A categoriﬁcation o f the
Temperley–Lieb algebra and Schur quotients of U (2) via projective and
Zuckerman functors, Selecta Math. (N. S.) 5 (1999), 199–241. Also avail-
able as arXiv:math/0002087.
[8] G. Bird, G. Kelly, A. Power, and R. Street, Flexible limits for 2-cate gories,
J. Pure Appl. Algebra 61 (1989), 1–27.
[9] A. Borel, Linear Algebraic Groups , Springer, Berlin, 1991.
[10] K. Brown, Buildings, Springer, Berlin, 1989.
[11] L. Crane and I. Frenkel, Four-dimensional topological quantu m ﬁeld theory,
Hopf categories, and the canonical bases, Jour. Math. Phys. 35 (1994),
5136–5154. Also available as arXiv:hep-th/9405183
64
[12] B. Elias and M. Khovanov, Diagrammatics for Soergel categorie s. Available
as arXiv:0902.4700.
[13] M. Fiore and T. Leinster, Objects of categories as complex num bers, Adv.
Math. 190 (2005), 264–277. Also available as arXiv:math/0212377.
[14] P. Gabriel, Unzerlebare Darstellungen I, Manuscr. Math. 6 (1972), 71–103.
[15] P. Garrett, Buildings and Classical Groups , CRC Press, New York, 1997.
Preliminary version available at
⟨http:/ /www.math.umn.edu/∼garrett/m/buildings/⟩.
[16] P. G. Goerss and J. F. Jardine, Simplicial Homotopy Theory, Birk ¨ auser,
Basel, 1999.
[17] M. Guta and H. Maassen, Symmetric Hilbert spaces arising from
species of structures, Math. Zeit. 239 (2002), 477–513. Also available as
arXiv:math-ph/0007005.
[18] A. E. Hoﬀnung, The Hecke bicategory. Available as arXiv:1007.19 31.
[19] A. W. Hubery, Ringel–Hall algebras, lecture notes available at
⟨http:/ /www.maths.leeds.ac.uk/ ahubery/RHAlgs.html⟩.
[20] J. Humphreys, Reﬂection Groups and Coxeter Groups , Cambridge U.
Press, Cambridge, 1992.
[21] V. Jones, Hecke algebra representations of braid groups and link polyno-
mials, Ann. Math. 126 (1987), 335–388.
[22] A. Joyal, Une th´ eorie combinatoire des s´ eries formelles, Adv. Math. 42
(1981), 1–82.
[23] A. Joyal, Foncteurs analytiques et esp` eces des structures , in Springer Lec-
ture Notes in Mathematics 1234, Springer, Berlin, 1986, pp. 126–159.
[24] D. Kazhdan and G. Lusztig, Representations of Coxeter grou ps and Hecke
algebras, Invent. Math. 53 (1979), 165–184.
[25] M. Khovanov, A categoriﬁcation of the Jones polynomial, Duke Math. J.
101 (2000), 359–426. Also available as arXiv:math/9908171.
[26] M. Khovanov, Categoriﬁcations from planar diagrammatics. Av ailable as
arXiv:1008.5084.
[27] M. Khovanov and A. D. Lauda, A diagrammatic approach to cate goriﬁ-
cation of quantum groups I, Represent. Theory 13 (2009), 309–347. Also
available as arXiv:0803.4121.
A diagrammatic approach to categoriﬁcation of quantum groups II . Also
available as arXiv:0804.2080.
A diagrammatic approach to categoriﬁcation of quantum groups II I. Also
available as arXiv:0807.3250.
65
[28] M. Kim, A Lefschetz trace formula for equivariant cohomology, Ann.
Sci. ´Ecole Norm. Sup. (4) 28 (1995), no. 6, 669–688. Also available at
⟨http:/ /www.numdam.org⟩.
[29] T. Leinster, The Euler characteristic of a category, Doc. Math. 13 (2008),
21–49. Also available as arXiv:math/0610260.
[30] S. Mac Lane, Categories for the Working Mathematician , Springer, Berlin,
1998.
[31] A. Mathas, Iwahori-Hecke Algebras and Schur Algebras of the Symmetric
Ggroup, American Mathematical Society, Providence, Rhode Island, 1999 .
[32] Paddy McCrudden, Balanced coalgebroids, Th. Appl. Cat. 7 (2000), 71–
147. Available at
⟨http:/ /www.tac.mta.ca/tac/volumes/7/n6/7-06abs.html⟩.
[33] J. Morton, Categoriﬁed algebra and quantum mechanics, Theory Appl.
Categ.16, (2006), 785-854. Also available as arXiv:math/0601458.
[34] C. Ringel, Hall algebras and quantum groups, Invent. Math. 101 (1990),
583–591.
[35] C. Ringel, Hall algebras revisited, Israel Math. Conf. Proc. 7 (1993), 171–
176. Also available at
⟨http:/ /www.mathematik.uni-bielefeld.de/∼ringel/opus/hall-rev.pdf⟩.
[36] R. Rouquier, Categoriﬁcation of the braid groups. Available as
arXiv:math/0409593.
[37] R. Rouquier, 2-Kac–Moody algebras. Available as arXiv:0812.502 3.
[38] C. Stroppel, Categoriﬁcation of the Temperley–Lieb category , tangles and
cobordisms via projective functors, Duke Math. J. 126 (2005), 547–596.
[39] U. Schreiber, Span trace, nLab article available at
⟨http:/ /ncatlab.org/nlab/show/span+trace⟩.
[40] R. Street, Fibrations in bicategories, Cahiers Top. G´ eom. Diﬀ. 21 (1980),
111–160.
[41] O. Schiﬀman, Lectures on Hall algebras, available as arXiv:math/ 0611617.
[42] W. Soergel, The combinatorics of Harish-Chandra bimodules, J. Reine
Angew. Math. 429, (1992) 49–74.
[43] M. Szczesny, Representations of quivers over F1. Available as
arXiv:1006.0912.
[44] B. Webster and G. Williamson, A geometric model for Hochschild ho mology
of Soergel bimodules, Geom. Top. 12 (2008), 1243–1263. Also available as
arXiv:0707.2003.
66
[45] A. Weinstein, The volume of a diﬀerentiable stack, to appear in th e proceed-
ings of Poisson 2008 (Lausanne, July 2008). Available as arXiv:0809.2 130.
[46] H. Wilf, Generatingfunctionology, Academic Press, Boston, 1994. Also
available at ⟨http:/ /www.cis.upenn.edu/∼wilf/⟩.
67
