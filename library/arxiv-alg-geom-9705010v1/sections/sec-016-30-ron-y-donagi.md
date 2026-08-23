---
doc_id: arxiv-alg-geom-9705010v1
doc_title: "Seiberg-Witten Integrable Systems"
section_id: sec-016-30-ron-y-donagi
section_title: "RON Y. DONAGI"
section_number: 30
pages: 30-41
source_pdf: 9705010v1.pdf
source_sha256: 30ab8d0cc2d8f1ae
doc_brief: "Seiberg-Witten Integrable Systems — 17 sections: RON Y. DONAGI; Introduction; References"
---
is the Jacobian of the spectral curve
det(˜t −ϕi),
where ϕi is the ni ×ni dimensional i-th block of ϕ. The claim is then that this
is one of the SU (ni) spectral curves, i.e. that the residue at ∞ of the i-th block
is conjugate to m · diag (1, 1,..., 1, 1 − ni). An equivalent condition is: rank
(ϕi −m) ≤ 1, and this condition is clearly inherited by any block in ϕ, as required.
Singularities
Much of the eﬀort in [ DW] was devoted to analyzing the discriminant, the
hypersurface D ⊂ B over which the spectral curves are singular. Physically, th at
is where all the interesting phenomena occur, and where many predictions can
be made. For instance, as τ → ∞ (“at weak coupling”), the limit of D should
be reducible: this is a classical limit, where the mass spect rum can be analyzed
directly from the classical Lagrangian. D is the locus where some mass vanishes.
This mass can belong to either of the two types (vector or hype r) of N = 2 SUSY
multiplets mentioned in section 1 (“Adding matter”), and th is gives rise to the two
components. In fact, one knows the explicit equations in B for these components.
A Maple assisted computation, using the explicit equations obtained above for
the spectral curves, conﬁrmed the reducibility and produce d the precise predicted
factors for SU (3).
For any τ (and any n), the most interesting locus in B is the (n − 1)-fold self-
intersection of D, a ﬁnite set. Physically, this corresponds to the massive va cua,
where the (low energy) gauge group is broken to its maximal to rus by monopole
condensation. A classiﬁcation result due to ’t Hooft predic ts that the possible
massive vacua should correspond to index n subgroups of Zn × Zn.
The corresponding result can be obtained directly from the i ntegrable system.
The general spectral curve has genus n, and we are imposing the maximal number,
n − 1, of nodes. The normalized spectral curve is then of genus 1, and must be an
unramiﬁed n-sheeted cover of the base E. These covers are of course classiﬁed by
the subgroups as above. Conversely, given any n-sheeted cover π :E′ →E and a
point ∞′ above ∞ ∈ E, there is a unique meromorphic 1-form on E′ with residue
m at π−1(∞)\∞′ and residue (1 −n)m at ∞′ (modulo the constant form π∗dz),
hence a unique map of E′ to the total space of ωE(∞) whose image is a spectral
curve, as required. (Changing the choice of ∞′ amounts to a deck transformation,
leaving the spectral curve unchanged).
We also analyzed, assisted with some massive and miraculous -looking Maple
computations, the locus of cusps in the SU (3) theory, again conﬁrming some rather
delicate predictions coming from the physics. It seems that there is some very beau-
tiful geometry still waiting to be understood in the structu re of the discriminant
for the SU (n) theories.
§4. Other integrable systems
Having studied in some detail the system which solves one par ticular family of
SYM theories, we proceed to consider what is known for some of the other families.
Our discussion will include,
• The pure N = 2 SYM for arbitrary gauge group G, and its relation to the
Toda systems.
• The situation when fundamental matter is added to the pure th eory.
SEIBERG-WITTEN INTEGRABLE SYSTEMS 31
• The theory with adjoint matter for arbitrary G, and its relation to the
elliptic Calogero-Moser system.
• A few words about the integrable systems arising in string th eory.
Pure N=2 SYM
The solutions by Seiberg and Witten of the pure N = 2 SYM theory [ SW1]
and the theories with fundamental or adjoint matter [ SW2] led rapidly to the
creation of a whole literature of solutions to speciﬁc SYM th eories. The general
pattern was: postulate the general form of a family of curves which builds-in some
of the expected symmetries of the theory, then adjust coeﬃci ents to enforce all
other available information: further symmetries, limitin g theories which were al-
ready known, internal consistencies. All cases which were w orked out this way, e.g.
[KL TY], [AF], [DS], [HO], [APS], [BL], [AS], [H], [AAG] and further references
therein, were based on postulating curves which are hyperel liptic or closely related
to hyperelliptics.
It was observed in [ GKMMM] that the curves obtained in [ KL TY], [ AF] for
the pure G =SU (n) theory are precisely the spectral curves of the periodic To da
system. The analogue for all semisimple groups was found in [ MW], which we
follow here.
The T oda system
A simple way to describe the Toda system is via the constructi on of Adler-
Kostant-Symes. Start with a decomposition g = a ⊕ b of a Lie algebra g as vector
space direct sum of two of its subalgebras a, b. This induces a dual decomposition
g∗ = a∗ ⊕ b∗, an injection i := b∗֒→g∗, and a projection π : g ։ b. Let Ox ⊂ b∗
denote the coadjoint orbit of some x ∈ b∗. The image i(Ox) ⊂ g∗ has, in general,
nothing to do with the coadjoint orbit Oi(x) of i(x) in g∗. So i∗ of a G-invariant
functionf on g∗ can be a complicated, non-constant function on Ox. The AKS claim
is that any two such, i∗f1 and i∗f2, Poisson commute with respect to the natural
(Kirillov-Kostant) symplectic structure σOx on Ox. Indeed, let vj ∈ g correspond
to the diﬀerential dfj|i(x) ∈ g∗∗ = g, so i∗dfj is given by π(vj ). G-invariance of fj
implies that vj is conormal to Oi(x), i.e. that
0 = ⟨i(x), [g,v j ]⟩.
We set aj :=vj −π(vj ) ∈ a, and compute:
{i∗f1,i ∗f2}Ox =σOx (πv1,πv 2)
= ⟨x, [π(v1),π (v2)]b⟩
= ⟨i(x), [π(v1),π (v2)]g⟩
= ⟨i(x), [v1,π (v2)]g⟩ − ⟨i(x), [a1,π (v2)]g⟩
= ⟨i(x), [v1,π (v2)]⟩ − ⟨i(x), [a1,v 2]⟩+ ⟨i(x), [a1,a 2]⟩.
We have just seen that the ﬁrst two terms vanish when f1,f 2 are G-invariant, and
the third term vanishes since it pairs i(x) ∈ b∗ = a⊥ with [a1,a 2] ∈ a. This proves
AKS.
A shifted version of AKS is very convenient in applications. Replace the in-
clusion i : b∗֒→g∗ by its shifted version ǫ +i, where ǫ is an element of g∗ which
annihilates [a, a] and [b, b]. The above argument goes through verbatim. For exam-
ple, take g = sl(n), a = strictly lower triangular matrices, b = upper triangulars,
32 RON Y. DONAGI
and (after identifying g with g∗, so that b∗ becomes the lower triangulars):
ǫ =






0 1
0
. . .
0 1
0






,x =






0
1 0
. . .
0
1 0






.
The orbit Ox ⊂ b∗ consists of all matrices of the form:





b1 0
a1
. . .
. . .
0 an−1bn





with aj ⁄= 0 and Σ bj = 0. The shifted orbit consists of tridiagonal matrices:





b1 1 0
a1 · ·
· · ·
· · 1
0 an−1 bn




.
This is a 2(n− 1)-dimensional symplectic manifold (X,σ ), isomorphic as symplectic
manifold to the cotangent bundle of the maximal torus T ≈ (C∗)n−1. The restric-
tion to it of the symmetric polynomials of SL(n) (= coeﬃcients of the characteristic
polynomial) givesn−1 independent, commuting Hamiltonians. This is the classic al
Toda system.
An equivalent system is obtained if ǫ is replaced by m ·ǫ with m ∈ C∗. When
m = 0, the Hamiltonians become the symmetric functions of the bi. We get the
cotangent bundle X of ( C∗)n−1, ﬁbered by its moment map over ( C)n−1. Another
variant is to take ǫ = 0, but replace a by the algebra so(n) of skew symmetric
matrices. Now b∗ sits in sl(n) as the symmetric matrices, and the orbit consists of
symmetric tridiagonal matrices






b1 c1
c1 b2
. . .
bn−1 cn−1
cn−1 bn






.
This is conjugate to the previous matrix with ai =c2
i , so we obtain a new version
( ˜X, ˜σ) of Toda which is just a 2 n−1-sheeted cover of the previous, basic version,
(X,σ ).
The Toda system for a semisimple Lie algebra g is obtained with b a Borel
subalgebra, a the nilpotent radical of the opposite Borel, x = Σ eα and ǫ = Σ e−α,
where the sums are over the simple roots α with respect to b, and the e±α are
normalized root vectors. The total space can again be identi ﬁed with the cotangent
bundle of the maximal torus, a typical element having the for m Σ
α simple
(bαhα +
aαeα +e−α) with respect to a standard basis hα,e ±α.
Periodic T oda
SEIBERG-WITTEN INTEGRABLE SYSTEMS 33
The periodic Toda systems are obtained when the semisimple a lgebra g is re-
placed by a loop algebra g(1). This has an extended Dynkin diagram consisting of
the simple roots α of g plus the aﬃne root α0, corresponding to the highest root of
g. The general element of the periodic Toda system can thus be w ritten as
Σ α(bαhα +aαeα +e−α) +zeα0 +z−1a0e−α0,
where z is the loop variable, and the product a0
∏
αaα = µ is a ﬁxed non-zero
constant. (For g = sl(n), this is:





b1 1 a0z−1
a1
. . . . . .
. . . . . . 1
z a n−1 bn




,
with∏ ai =µ, Σ bj = 0).
As in the case of Higgs bundles, the spectral curves Cρ,b depend on the choice
of a representation ρ of G. These Toda curves and their relationships were ﬁrst
studied in [ Ml] and [ MS], with some clariﬁcations added in [ MW1]. Each Cρ,b is
a branched cover of the z-line P1
z. The latter plays the role for periodic Toda which
the base curve E played for the meromorphic Higgs system in §2. The cameral
cover in this situation has a strikingly simple description . The classifying map
P1
z /axisshort/axisshort/arrowaxisrightt/W , which is usually only locally deﬁned, is now a morphism for z ⁄= 0, ∞.
It factors through the double cover
P1
z → P1
w
z ↦→w =z +µz−1
which maps P1
z\{0, ∞} to A1
w = P1
w\{∞}, followed by an aﬃne linear map
A1
w ↦→t/W
whose image in t/W is a straight line pointing in the direction of the invariant
polynomial of highest degree, which is equal to the Coxeter n umber hg of g. More
precisely, the algebra of polynomial functions on t/W is isomorphic to the algebra
of invariant polynomials on t, which is ﬁltered by the degree. The equations of the
image of A1
w are obtained by ﬁxing the values of all polynomials on t/W whose
pullback to t has degree <h g. The induced W -cover of P1
w then has r = rank( g)
branch points in A1
w, and one at w = ∞. The choice of a Borel labels the ﬁnite
branch points wα by the simple roots α in such a way that the monodromy at wα
is the reﬂection corresponding to α. The monodromy at ∞ is then the product of
these reﬂections, the Coxeter element. The Cameral cover is the pullback to P1
z. It
can be described as the W -cover obtained from the trivial cover W × P1
z by making
r + 1 cuts labelled by the extended set of roots {α} ∪ {α0}, each running from
a point zα to µz−1
α , and pasting across each cut according to the corresponding
element of W .
In addition to the loop algebras g(1), there are twisted versions g(k) where k
is the order of an automorphism of the Dynkin diagram of g, and each of these
also gives rise to a periodic Toda system. The basic observat ion of Martinec and
Warner [MW1] is that each of the known families of pure N = 2 SYM curves arises
as spectral curves for one of these twisted periodic Toda sys tems. The speciﬁc
34 RON Y. DONAGI
identiﬁcation involves Langlands duality (Olive-Montone n duality, to a physicist)
exchanging the direction of arrows in the extended diagram. The (untwisted) ex-
tended diagrams for types A,D,E are self-dual, yielding ordinary Toda systems.
The remaining cases yield twisted algebras and systems:
(B(1)
r )∨ =A(2)
2r−1, (C(1)
r )∨ =D(2)
r+1, (F (1)
4 )∨ =E(2)
6 , (G(1)
2 )∨ =D(3)
4 .
We will now describe explicitly the spectral curves for some of these systems.
The spectral curves
For the classical groups we can write the equation of the Toda spectral curves
CF,u for the fundamental representation F as
w =z +µz−1,x ǫw +p = 0
where
p =p(x) = xn+1 +u2xn−1 + · · · +un+1
for type An (G =SL(n + 1)), and
p =p(x2) = x2n +u2x2n−2+... +u2n
for types Bn,C n, and Dn, and the uℓ are coordinates on the base. Here ǫ = 0
for An,B n,C n and ǫ = 2 for Dn. In general, deg x(p) is the dimension of the
representation, while the w term modiﬁes the coeﬃcient uhg corresponding to the
invariant of highest degree. For An,B n,C n,D n, these Coxeter numbers are n +
1, 2n, 2n, 2n − 2. (The Bn case is slightly diﬀerent since 0 is a weight of F . So the
actual “spectral” curve has equation x(w +p(x)) = 0. We may safely ignore the x
factor, since the distinguished Prym lives in the Jacobian o f the other factor).
ForAn, the fundamental curve has genus n, so its Jacobian is the distinguished
Prym. It can be described geometrically as the ﬁber product o ver P1
w of the double
coverw =z +µz−1, branched at w = ±2√
µ, and the degree n+ 1 coverw = −p(x),
with total ramiﬁcation over w = ∞ and n simple branch points at the images of
the roots of p′(x) = 0. The substitution y = 2z +p(x)/2, 4µ = Λ 2(n+1) converts it
to
y2 =p2(x) − Λ 2(n+1),
the form obtained in [ AF] and [ KL TY]. (Here we have reinstated the scale param-
eter Λ of the asymptotically free theory. Previously this wa s set to 1).
The other spectral curves for An are easily obtained from the fundamental one.
The curve for ∧2F is of degree n(n+1)
2 over thez line, and of genusn(n−1)+1−[ n+1
2 ].
The obvious correspondence between it and CF,u produces a copy of J(CF,u) in
J(C∧2F,u). The A3 case is described in [ Ml], [ MS]: The tetragenal curve CF,u
of genus 3 gives rise via Recillas’ trigonal construction (c f. [ D3]) to the degree 6,
genus 5 curve C∧2F,u, together with an involution whose quotient is a trigonal cu rve
C′ of genus 2. The Jacobian of CF,u is isogenous to Prym( C∧2F,u/C ′). (Actually,
the degree 6 and 3 curves produced by the trigonal constructi on have genera 7 and
4 respectively, but each has 2 nodes, over z = 0 and z = ∞; the curves C∧2F,u
and C′, of genera 5 and 3, are their respective desingularizations ). A beautiful
picture of the g = 11 curve C∧2F,u for A4 is given in [ MW1]. In contrast to these
small curves, there is the gigantic cameral cover, of degree n! over P1
z and of genus
1 + n−1
2(n+1) (n + 2)!, whose Jacobian contains those of all (irreducible com ponents of)
spectral covers.
SEIBERG-WITTEN INTEGRABLE SYSTEMS 35
ForDn,C F,u has equation x2w +p(x2) = 0. This depends on n parameters,
but has genus 2 n − 1, too big. The quotient C′ by the involution x ↦→ −x is
hyperelliptic of genus n − 1; the n-dimensional piece is Prym ( CF,u/C ′), and it can
be realized as the Jacobian of a curve C′′, the quotient of CF,u by the involution
x ↦→ −x,z ↦→µz−1. The substitution y := x2(z −µz−1), 4µ = Λ 4(n−1) takes the
equation of CF,u to
y2 =p2(x2) − Λ 4(n−1)x4,
the form of the SO(2n) SYM curve obtained in [ BL]. In terms of s = xy,t = x2,
the quotient C′′ becomes:
s2 =tp2(t) − Λ 4(n−1)t3.
For typeCn, the fundamental Toda curve CF,u has equationw +p(x2) = 0,w =
z +µz−1. The substitution y = 2z +p(x2) changes this to
y2 =p2(x2) − 4µ.
Just as in the Dn case,CF,u has automorphism group Z2 × Z2 over the t =x2 line:
P I1 :(t)
=p  (x  )-4  )2 2 µ:(x,y)/(y2C F,u
C :(t,s)/(s  =t(p  (t)-4  ))22 µ P I1:(x)C :(t,y)/(y  -p  (t)-4  )2 2 µ
and the n-dimensional piece is J(C′′). But this is not the right abelian variety for
the SYM theory. Rather, we should consider the Toda curves fo r (C(1)
n )∨ =D(2)
n+1.
These have the form
w2 +p(x2) = 0, w =z +µz−1.
The coordinates on the three Z2 quotients by the involutions x ↦→ ±x,z ↦→ ±µz−1
are now:
(x,z)
(x,w) (x,z  )2 (x,w  )
(x,w  )2
36 RON Y. DONAGI
where w′ =w − 2µz−1 =z −µz−1. The corresponding genera are:
4n-3
n-1 2n-1 n-1
0
The middle curve has equation v + µ2
v +p(x2) − 2µ = 0, where v = z2. It fac-
tors further: in fact, it looks just like the Cn-Toda curve, with z,µ,p replaced by
v,µ 2,p − 2µ respectively. So its Jacobian has an n-dimensional piece, which is the
Jacobian of:
s2 =t((p(t) − 2µ)2 − 4µ2) = tp(t)(p(t) − 4µ).
This is essentially the Cn-curve obtained in [ AS].
For Bn the story is similar, but simpler. The dual Toda curve has equ ation
x(z +µz−1) +p(x2) = 0. The substitution y = 2xz +p(x2), 4µ = Λ 2(2n−1) converts
this to the form obtained in [ DS],
y2 =p2(x2) − Λ 2(2n−1)x2.
Again this is of genus 2 n − 1. The genus n quotient is
s2 =t(p2(t) − Λ 2(2n−1)t).
ForG2, we need Toda curves for ( G(1)
2 )∨ =D(3)
4 . These are given [ MW1] as:
3(z −µz−1)2 −x8 + 2u2x6 − [u2
2 + 6(z +µz−1)]x4 + [u4 + 2u2(z +µz−1)]x2 = 0.
The various quotients involve the functions:
w =z +µz−1
s =x2
u =x(z −µz−1)
v =x(w −s2 + u2
3 s).
Some quotient curves, indicated by the functions which gene rate their ﬁelds, are:
(x,z)
(s,u)
(s,w)
(x,w) (s,z)
(s) (w)
(z)(x) (s,v)
SEIBERG-WITTEN INTEGRABLE SYSTEMS 37
The corresponding genera are:
11
5 53
00
00 2 1
I have not checked whether the genus 2 curve with functions ( s,v ) is the one
corresponding to the G2 theory. An explicit family of genus 2 curves was proposed
in several works (see references in [ AAG]) for the G2 theory, but according to
[LPG] this family does not have good physical properties, and doe s not match the
Toda curves.
TheE6 curves were considered in [ L W], and turn out to involve some beautiful
geometry. The simplest curve is based on the 27-dimensional representation of E6.
The resulting 27-sheeted cover of the z line behaves like the lines on a 1-parameter
family of cubic surfaces. Each of the 6 simple roots correspo nds to an ordinary
double point acquired by the surface, so the local monodromy at each ﬁnite branch
point is the product of 6 disjoint transpositions. Lerche an d Warner study this
genus-34 spectral curve, and go on to relate it to an integrab le system coming from
a string theory compactiﬁcation on a Calabi-Yau threefold w hich degenerates to a
ﬁbration of the E6 ALE singularity by a family of cubic surfaces.
F undamental matter
The spectral curves for SYM with various gauge groups and num bers of par-
ticles (“quarks”) in the fundamental representation have b een determined by vari-
ous means. A very incomplete list includes [ HO], [ APS], [ AS], [ H], [ MN], [ KP],
[DKP1],[DKP2]. Each of these solutions is supported by substantial evide nce, and
yet the total picture seems far from complete. No really clea r unifying principle is
known, and there is no analogue of the Toda integrable system which is responsible
for the various curves. There is also a certain level of disag reement among compa-
rable solutions, see the discussion in [ MN] and [ DKP1]. (The curves involved in
those solutions are the same, but the parametrizations diﬀe r. An integrable system
would of course give a preferred parametrization).
Adjoint matter
As soon as [ MW] and [ DW] appeared, each with a class of integrable systems
which solves its respective version of SYM, the question aro se whether there was
a common generalization: an integrable system for SYM with a djoint matter and
arbitrary gauge group G, going to the periodic Toda system in the limit as m and
τ go together to ∞.
In [Mc], Martinec suggested that the elliptic Calogero-Moser sys tem (cf. [ OP])
may provide this common generalization. There is such a syst em for each semisim-
ple G, and the case G =SU (n) agrees exactly with the system in [ DW]. There is
also a direct computation [ I1] showing that the An andDn systems can degenerate
to the respective Toda systems, and there is a deformed famil y of integrable systems
depending on some additional parameters (the elliptic spin models, [ I2]). A way of
obtaining the An system by symplectic reduction is given in [ GN].
One way to try to understand the geometry of these systems is a s follows.
Fix an elliptic curve E, a semisimple group G, and its maximal torus T . Let
38 RON Y. DONAGI
M, M′ denote the moduli spaces of semistable bundles on E with structue groups
G,T respectively. A special feature of genus 1 is that the natura l map M′ → M
is surjective, in fact it is a Galois cover with group W . (It is not true that the
structure group of every semistable G-bundle on E can be reduced to T ; but every
S-equivalence class of semistable bundles contains one whos e structure group can
be reduced). Now let X be the moduli space of Higgs bundles on E with ﬁrst
order pole at ∞, and let X ′ be its ﬁnite cover induced by M′ → M. (A point of
X ′ is an equivalence class of pairs ( V,ϕ ) where V is a T -bundle on E and ϕ is a
meromorphic Higgs ﬁeld on V ⊗T G). There is a “moment map”
µ :X ′ → t⊥/T,
where t⊥ ⊂ g∗ is the annihilator of the Cartan t, and the T -action is coadjoint. Now
all the ﬁbers of µ are symplectic, of the minimal dimension 2 r (wherer = rank(g)),
and at least for some of them (but certainly not for all!), the restrictions of all
the X-Hamiltonians Poisson commute, giving a large family of sma ll integrable
systems. (Presumably, this involves an analogue of the AKS p roof of integrability
of the Toda system). As the elliptic curve degenerates to P1 with 0 glued to ∞,
this construction specializes to the periodic Toda.
The question remains, though: of all the possible T -orbits, which one corre-
sponds to SYM with adjoint matter? A necessary condition see ms to be that the
T orbit O needs to be W -invariant; otherwise the limit as m → 0 will not be the
Hitchin system T ∗M, but its ﬁnite cover T ∗M′. (Or something in-between, if O is
invariant under a subgroup of W .) For SU (n), there is a unique such class (up to
scalars), namely ∑
i⁄=jeij. The natural analogue for arbitrary g would be ∑
αeα,
the sum over all roots. Unfortunately, this is ill deﬁned: th e eα can be normalized
only up to sign, and diﬀerent signs give distinct T orbits. For the orthogonal groups,
there does not seem to be any W -invariantT orbit. David Lowe has pointed out
[L] that for Sp(n) there is an invariant orbit, namely the T orbit of the deﬁning
matrixJ. (It is a signed sum of the long root vectors). This does give a n integrable
system, but a rather boring one: it is the n-fold product of the SU (2) system, which
does not ﬂow to the pure N = 2 Cn spectral curves described earlier.
In sum, the elliptic Calogero-Moser systems (or their spin v ariants) seem to
be a promising general class of systems for realizing the SYM theory with adjoint
matter for arbitrary gauge group, but at the moment we lack a g ood geometric
understanding of these systems, e.g. via spectral curves, e xcept in the case of
SU (n).
Stringy integrable systems?
Quantum ﬁeld theory is a limit of string theory compactiﬁed o n a Calabi-
Yau threefold, and the SW duality can be realized as the limit ing form of various
string dualities. A series of recent papers, such as [ MW2], [ KLMVW], [ GHL1],
[GHL2], [L W], suggest that much of the QFT structure studied in this pape r - the
spectral curves, integrable systems, SW diﬀerentials and s o on - arises as limit of
corresponding stringy structures. A possible framework fo r studying the transition
from stringy integrable systems to the SW systems is propose d in [ F], where SW-
type integrable systems are shown to arise from rigid specia l geometry, while the
stringy type arises from local special geometry. From a pure ly mathematical point
of view, it should be interesting to understand the relation s between the SW-type
systems, whose basic input is an elliptic curve; the Mukai sy stem on a K3 surface,
SEIBERG-WITTEN INTEGRABLE SYSTEMS 39
which degenerates to Hitchin’s on a curve ([ DEL], [ DM1]); and the Calabi-Yau
systems constructed in [ DM2].
References
[AAG] M. R. Abolhasani, M. Alishahiha, A. M. Ghezelbash, hep -th 9606043.
[AHH] M. Adams, J. Harnad, J. Hurtubise, Isospectral Hamiltonian ﬂows in ﬁnite and inﬁ-
nite dimensions II: Integration of ﬂows , Commun. Math. Phys. (1990), 555-585.
[AM] M. Adler, P. van Moerbeke, Completely integrable systems, Euclidean Lie algebras,
and curves , Advances in Math. 38 (1980), 267-379.
[AF] P. C. Argyres, A. Faraggi, The vacuum Structure and Spectrum of N = 2 Supersym-
metric SU (N ) Gauge Theory , Phys. Rev. Lett. 74 (1995), hep-th 9411057.
[APS] P. C. Argyres, R. Plesser, A. D. Shapere,, The Coulomb phase of N = 2 supersym-
metric QCD , Phys. Rev. Lett. 75:1699-1702 (1995), no. e-Print Archive: hep-th
9505100.
[AS] P. C. Argyres, A. D. Shapere,, The vacuum structure of N = 2 super-QCD with
classical gauge groups , hep-th 9509175.
[B] A. Beauville,, Jacobiennes des courbes spectrales et systemes hamiltonie ns complete-
ment integrables, Acta Math. 164 (1990), 211-235.
[Be] J. Bernstein, Lectures on Supersymmetry, Lectures at IAS, Fall 1996 , Preprint avail-
able at http://www.math.ias.edu/drm/QFT.
[Bo] F. Bottacin, Symplectic geometry on moduli spaces of stable pairs , Orsay, 1992.
[BL] A. Brandhuber, K. Landsteiner, On the Monodromies of N = 2 Supersymmetric
Yang-Mills Theory with Gauge Group SO(2n), hep-th 9507008.
[DS] U. H. Danielsson, B. Sundborg, The Moduli Space and Monodromies of N = 2 Su-
persymmetric SO(2r + 1) Yang-Mills Theory, hep-th 9504102.
[DKP1] E. D’Hoker, I. M. Krichever, D. H. Phong, hep-th 96090 41.
[DKP2] E. D’Hoker, I. M. Krichever, D. H. Phong,, hep-th 9609 145.
[D1] R. Donagi, Decomposition of spectral covers , in Journees de Geometrie Algebrique
D’Orsay, Asterisque 218 (1993), 145-175.
[D2] R. Donagi, Spectral Covers , Current Topics in Complex Algebraic Geometry, (H.
Clemens and J. Kollar, eds.), MSRI Pub., vol. 28, 1995, pp. 65 -86, Alg Geom, 9505009.
[D3] R. Donagi, The tetragonal construction , Bull. Amer. Math. Soc. (N.S.) 4 (1981),
181-185.
[DEL] R. Donagi, L. Ein and R. Lazarsfeld, A non-linear deformation of the Hitchin dy-
namical system , AlgGeom 9504017.
[DM1] R. Donagi, E. Markman, Spectral curves, algebraically completely integrable Ham il-
tonian systems, and moduli of bundles , R. Donagi et al, Integrable systems and Quan-
tum Groups, LNM 1620, (1996), 1-119 Alg Geom, 9507017.
[DM2] R. Donagi, E. Markman, Cubics, Calabi-Yau threefolds, Integrable Systems and Mir -
rors, Israel Math. Conf. Proc., vol. 9, AMS, 1995, AlgGeom 940800 4.
[DW] R. Donagi, E. Witten, Supersymmetric Yang-Mills theory and integrable systems ,
Nucl. Phys B460 299 (1996), hep-th, 9510101.
[DH] J. J. Duistermaat, G. J. Heckman, On the Variation in the Cohomology of the Sym-
plectic Form of the Reduced Phase Space , Invent. Math. 69 (1982), 259.
[FS] L. D. Faddeev, A. A. Slavnov, Gauge Fields: Introduction to Quantum Theory , Ben-
jamin/Cummings, 1980.
[Fa] G. Faltings, Stable G-bundles and Projective Connections , Jour. Alg. Geo 2 (1993),
507-568.
[F] D. S. Freed, On special Kahler manifolds , preprint.
[Fr] P. Freund, Introduction to supersymmetry, Camb. Monographs on Math. Phys. ,
Camb. U. Press, 1986.
40 RON Y. DONAGI
[GHL1] C. Gomez, R. Hernandez, E. Lopez, hep-th 9604057.
[GHL2] C. Gomez, R. Hernandez, E. Lopez, hep-th 9608104.
[GKMMM] A. Gorsky, I. Krichever, A. Marshakov, A. Mironov, A . Morozov, hep-th 9505035.
[GN] A. Gorsky, N. Nekrasov, Elliptic Calogero-Moser system from two-dimensional cur-
rent algebra, hep-th 9401021.
[H] A. Hanany, On the quantum moduli space of vacua of N = 2 supersymmetric gauge
theories, hep-th 9509176.
[HO] A. Hanany, Y. Oz, On the quantum moduli space of vacua of N = 2 supersymmetric
SU (N ) gauge theories , hep-th 9505075.
[Hi] N. Hitchin,, Stable bundles and integrable systems , Duke Math. J. 54 (1987), 91-114.
[I1] V. I. Inozemtsev, The ﬁnite Toda lattices , Comm. Math. Phys. 121 (1989), 629-38.
[I2] V. I. Inozemtsev, Lax representation with spectral parameter on a torus for in tegrable
particle systems , J. Lett. Math. Phys. 17 (1989), 11-17.
[IM1] H. Itoyama, A. Morozov, hep-th 9511126.
[IM2] H. Itoyama, A. Morozov, hep-th 9512161.
[Ka] V. Kanev, Spectral curves, simple Lie algebras and Prym-Tjurin varie ties, Proc.
Symp. Pure Math. Part I 49 (1989), 627-645.
[KLMVW] A. Klemm, W. Lerche, P. Mayr, C. Vafa, N. W arner, hep- th 9604034.
[KLTY] A. Klemm, W. Lerche, S. Theisen, S. Yankielowicz, Simple Singularities and N =
2 Supersymmetric Yang-Mills Theory , Phys. Lett. 169 (1995), no. B344, hep-th
9411048.
[K] I. M. Krichever, hep-th 9205110.
[KP] I. M. Krichever, D. H. Phong, hep-th 9604199.
[LPG] K. Landsteiner, J. M. Pierre, S. B. Giddings,, hep-th 9 609059.
[L W] W. Lerche, N. P. W arner, hep-th 9608183.
[Mn] E. Markman, Spectral Curves and Integrable Systems , Comp. Math. 93 (1994), 255-
290.
[Mv] A. Marshakov, hep-th 9607159.
[Mc] E. Martinec, hep-th 9510204.
[MW1] E. Martinec, N. P. W arner, Integrable Systems and Supersymmetric Gauge Theory ,
hep-th 9509161.
[MW2] E. Martinec, N. P. W arner, hep-th 9511052.
[Ml] A. McDaniel, Representations of sl(n, C) and the Toda lattice , Duke Math. J. 56
(1988), 47-99.
[MS] A. McDaniel, L. Smolinsky, A Lie theoretic Galois Theory for the spectral curves of
an integrable system II, prep. (1994).
[Me] J. Y. Merindol, Varietes de Prym d’un Revetement Galoisien , prep. (1993).
[MN] J. A. Minahan, D. Nemeschansky, hep-th 9601059.
[MO] C. Montonen, D. Olive, Magnetic Monopoles as Gauge Particles? , Phys. Lett. 72B
(1977), 177.
[Mu] S. Mukai, Symplectic structure of the moduli space of sheaves on an abe lian or K3
surface, Inv. Math. 77 (1984), 101-116.
[NT] T. Nakatsu, K. Takasaki, hep-th 9509162.
[N] N. Nekrasov, Holomorphic bundles and many-body systems , hep-th 9503157.
[OP] M. A. Olshanetski, A. M. Perelomov, Classical integrable ﬁnite-dimensional systems
related to Lie algebras , Phys. Rep. 71C (1981), 313-400.
[SW1] N. Seiberg, E. Witten, Monopole Condensation, and Conﬁnement in N = 2 Super-
symmetric Yang-Mills Theory , Nucl. Phys. B426 (1994), 19, hep-th 9407087.
SEIBERG-WITTEN INTEGRABLE SYSTEMS 41
[SW2] N. Seiberg, E. Witten, Monopoles, duality and chiral symmetry breaking in N = 2
supersymmetric QCD , Nucl. Phys. B431 (1994), 484-550, hep-th 9408099.
[T] A. Treibich, Tangential polynomials and elliptic solitons , Duke Math. J. 59 (1989),
611-627.
[TV] A. Treibich, J. L. Verdier, Solitons Elliptiques , The Grothendieck Festschrift III
(1990), Birkh¨ auser, 437-480.
[W] E. Witten, Monopoles and Four Manifolds , hep-th/9411102.
[WB] J. W ess, J. Bagger, Supersymmetry and supergravity , Princeton U. Press, 1992.
Department of Mathemtics,
University of Pennsylvania,
Philadelphia, PA 19104-6395
Current address : School of Mathematics,
Institute for Advanced Study,
Princeton, NJ 08540
