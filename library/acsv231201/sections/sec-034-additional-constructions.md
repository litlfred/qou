---
doc_id: acsv231201
doc_title: "Analytic Combinatorics in Several Variables Expanded Second Edition"
section_id: sec-034-additional-constructions
section_title: "Additional constructions"
section_number: null
pages: 180-187
source_pdf: ACSV231201.pdf
source_sha256: 1a664d0bf666041e
toc_source: outline
doc_brief: "Analytic Combinatorics in Several Variables Expanded Second Edition — 100 sections: Front matter; Preface to the second edition; Preface to the first edition"
---
We end this chapter by defining some additional constructions that will be
required in Chapters 10 and 11.

Definition 6.46. If f : C’ — C is analytic at w € C@ then the order of
vanishing of f at w is

deg(f, w) := sup {n EN: f(w + z) = O(z|") as |z| 3 o} >

and the homogeneous part hom(f,w) of f at w is the sum of all terms of
degree deg(f, w) in the power series for f(w + z) at z = 0, so

S(w + z) = hom(f, w)(z) + O (later!) :
The algebraic tangent cone of f at w is the set
algtan,,(f) = Vnom fw):

When w = 0 we omit w from the notation and write hom(f) = hom(f, 0).

Remark. The algebraic tangent cone is not always a cone. For instance, if
f(x,y) = xy then the algebraic tangent cone V,, is the union of the x and y
axes.

A more geometric definition of the algebraic tangent cone is that it consists
of lines through a that are the limits of secant lines through a. Thus, for a unit
vector u the line a + ru lies in the algebraic tangent cone if there are points
x, € Vy distinct from but converging to x for which (@, —2)/||&,—2x|| > +u.
Equivalence of the two definitions follows from our next result, which we state
after introducing some new terminology.
6.5 Additional constructions
163
Figure 6.8 The real parts of V and Vε with ε = 1/10.
Deﬁnition 6.47. If (X, d) is a metric space then the Hausdorﬀmetric ρ on
compact subsets of X is deﬁned stepwise by
d(x, Y) = inf
y∈Y d(x, y)
(x ∈X and Y ⊂X)
d(Z, Y) = sup
z∈Z
d(z, Y)
(Z, Y ⊂X)
ρ(Z, Y) = max{d(Z, Y), d(Y, Z)}
(Z, Y ⊂X).
Lemma 6.48 (algebraic tangent cone is the limiting secant cone). Let Q(z)
be a polynomial vanishing to degree m ≥1 at the origin. Deﬁne the m-
homogeneous part A(z) = hom(Q), the remainder
R(z) = Q(z) −A(z),
and, for ε > 0, the scaled polynomial Qε(z) = ε−mQ(εz). If Vε denotes the
intersection of the zero set of Qε with the unit sphere S 1 and V0 denotes the
intersection of the zero set of A with S 1 then Vε →V0 in the Hausdorﬀmetric
as ε →0.
Example 6.49. Let Q(x, y) = x3 −xy + y3, which vanishes to order m = 2. The
leading homogeneous part is A(x, y) = −xy, the remainder is R(x, y) = x3 + y3,
and Qε(x, y) = ε(x3 + y3) −xy. Figure 6.8 shows V and Vε for ε = 1/10,
illustrating that Vε is close to the union of the x and y axes V0 = VA.
◁
Proof
On any compact set, including S 1, the rescaled remainder ε−mR(εz)
goes to zero uniformly. If zn →z and zn ∈V1/n then, for each n,
|A (zn)| =

Q1/n (zn) −R1/n (zn)

 =

R1/n (zn)

 →0 ,
164
Laurent series, amoebas, and convex geometry
so A(z) = 0 by the continuity of A. Thus, any limit point of Vε as ε →0 lies
in V0.
Conversely, ﬁx a unit vector z ∈V0. The homogeneous polynomial A is not
identically zero, therefore there is a projective line along which A has a zero
of ﬁnite order k at z. Let γ : C →S 1 denote any analytic curve through z
along which A has a zero of ﬁnite order at z. The univariate analytic function
γ ◦Qε converges uniformly to γ ◦A, and Hurwitz’s Theorem [Con78b, p. 152]
implies that for ε suﬃciently small it has k zeros of Qε converging uniformly
to z as ε →0. In particular, z is a limit point of Vε as ε →0.
□
Exercise 6.12. Is it true that the algebraic tangent cone Vhom( f,z) is always
homeomorphic to V f within a suﬃciently small ball around z?
Finally, let A be a homogeneous polynomial with square-free part ˜A (equal
to the product of the distinct irreducible factors of A), so VA = V ˜A but VA is
locally a manifold near any point where the gradient of ˜A doesn’t vanish. Any
hyperplane Hn = {z ∈Cd : z ·n = 0} through the origin can be identiﬁed with
its normal n, viewed as an element in complex projective space CPd−1. We say
the hyperplane Hn is a tangent hyperplane to VA if n = (∇˜A)(w) for some
zero w of A in CPd−1. The closure of all normals n to tangent hyperplanes
of VA in CPd−1 is an algebraic variety V∨
A, called the projective dual variety
to A. In generic situations V∨
A is deﬁned by the vanishing of a homogeneous
polynomial A∗, called the algebraic dual polynomial to A.
Example 6.50. If A(x, y, z) = x2 + y2 + z2 then (X, Y, Z) ∈V∨
A if and only if
(X, Y, Z) = λ∇A(x, y, z) = λ(2x, 2y, 2z) and x2 + y2 + z2 = 0 for some (x, y, z) ∈
VA and λ , 0. Eliminating x, y, and z from these equations gives X2/4λ2 +
Y2/4λ2 + Z2/4λ2 = 0, so the algebraic dual of A(x, y, z) is A∗(X, Y, Z) = X2 +
Y2 + Z2.
◁
Exercise 6.13. Prove that if A is a nonsingular quadratic form A(z) = zT Mz
then A∗is the quadratic form A∗(Z) = ZT M−1Z.
Exercise 6.14. Find the algebraic dual to A(x, y, z) = xy.
Notes
Perhaps the earliest use of amoebas is the algebraic work of Bergman [Ber71],
although their application to the problems considered here, along with the
coinage of the term amoeba, is generally credited to Gelfand, Kapranov, and
Zelevinsky [GKZ08]. That seminal text on discriminants devotes much of its
6.5 Additional constructions
165
Chapter 6 to amoebas and Newton polytopes. The development of basic re-
sults on amoebas [GKZ08, Section 6.1] begins by quoting without proof some
basic facts about Laurent series akin to Theorem 6.4. The reference they give,
namely [Kra01], proves these only for ordinary power series, and the result-
ing wild-goose chase led us to write down a more complete development
(the ﬁrst author learned much of the material used in our proofs while sit-
ting in on a graduate course at the University of Pennsylvania given by L.
Matusevich in Fall 2004). Additional background material on amoebas can be
found in [FPT00; Mik00; The02; Mik04; dWol13; dWol17; Tim18; For+19].
As noted above, our treatment of the order map and connections between the
Newton polytope and amoeba complement components is heavily based on
Forsberg et al. [FPT00]. Exercise 6.16 is taken from Rudin [Rud69, Theo-
rem 4.6.2]. Our proof of Theorem 6.44(b) is inspired by Mikhalkin [Mik00;
Mik04].
A good part of the theory of amoebas of algebraic hypersurfaces goes through
for analytic hypersurfaces. This and its applications to statistical physics, for
example, make up the content of [PPT13]. Because the theory of amoebas of
analytic hypersurfaces is still being formed, we mostly avoid its use.
The Legendre transform (or convex dual) of a convex function f : Rd →R
is the function f ∗: (Rd)∗→R deﬁned by
f ∗(v) = sup
x∈Rd ⟨v, x⟩−f(x) ,
which satisﬁes the duality relation f ∗∗= f – see, e.g., [Roc66], where f ∗is also
called the convex conjugate of f. Legendre transforms are intimately connected
with exponential rates of growth and decay. For example, in probability theory
the large deviation rate function f(λ), deﬁned as the Legendre transform of
the logarithm of the moment generating function, gives the rate of exponential
decay of the probability of the mean of n IID variables to exceed λ. In our
setting, the dual rate β∗(r) = infx∈B −r · x from (6.5) is the negative of the
Legendre transform of the convex function that is 1 on B and ∞on Bc.
Additional exercises
Exercise 6.15. Give a simple necessary condition on f for amoeba( f) to fail
to be strictly convex (in other words, for amoeba( f) to be ﬂat by containing a
line segment in its boundary).
Exercise 6.16. If α, β : [0, 1] →C2
∗are curves with α(0) = α(1) = β(0) = β(1)
then the product loop α#β : [0, 1] →C2
∗obtained by following α and then β is
166
Laurent series, amoebas, and convex geometry
deﬁned by
(α#β)(t) =

α(2t)
: 0 ≤t ≤1/2
β(2t −1)
: 1/2 ≤t ≤1
.
If α(t) = (a1(t), a2(t)) and β(t) = (b1(t), b2(t)) then the Hadamard loop α ⊙β :
[0, 1] →C2
∗obtained by coordinatewise product is deﬁned by (α ⊙β)(t) =

a1(t)b1(t), a2(t)b2(t)

.
a) Prove that α⊙β is homotopic to [α#u]⊙[u#β], where u is the constant curve
u(t) = (1, 1).
b) Prove that [α#u] ⊙[u#β] = [α ⊙u]#[u ⊙β].
c) Fix a, b ∈Z and let p1, p2 : [0, 1] →C2
∗be the curves p1(t) = (ea2πit, 1) and
p2(t) = (1, eb2πit). Prove that the image of w = e2πit under the map (wa, wb)
is homotopic to p1#p2.
Exercise 6.17. Use Propositions 6.27 and 6.24 to prove Corollary 6.28.
Exercise 6.18. Let P be a d-dimensional polytope with integer vertices and let
f(z) = P
m∈P cmzm where cm = exp(−λ|m|2).
(a) Show that if λ > 0 is suﬃciently large then there is some x = x(m) ∈Rd
such that
cm exp(m · x) ≥
X
m′∈P
m′,m
cm′ exp(m′ · x) .
(b) Conclude that x(m) is not in amoeba( f).
(c) Show that each x(m) is in a separate component of amoeba( f)c as m
varies over P, establishing that for every polytope with integer coordinates
there is a polynomial whose amoeba complement has a component for
every integer point of the polytope.
Exercise 6.19. Prove that if λ is suﬃciently large in Exercise 6.18 then the
boundary ∂amoeba( f) equals the contour C( f). (Be warned this is diﬃcult.)
PART III
MULTIVARIATE ENUMERATION
