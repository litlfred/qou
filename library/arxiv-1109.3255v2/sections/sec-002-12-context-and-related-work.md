---
doc_id: arxiv-1109.3255v2
doc_title: "FLOER COHOMOLOGY IN THE MIRROR OF THE PROJECTIVE"
section_id: sec-002-12-context-and-related-work
section_title: "Context and related work"
section_number: 1.2
pages: 5-10
source_pdf: 1109.3255v2.pdf
source_sha256: dd4579be8e9b7e25
doc_brief: "FLOER COHOMOLOGY IN THE MIRROR OF THE PROJECTIVE PLANE AND A BINODAL CUBIC CURVE — We construct a family of Lagrangian submanifolds in the Landau– Ginzburg mirror to the projective plane equipped"
---
1.2.1. Manifolds with eﬀective anticanonical divisor and Landau– Ginzburg models.
The class of spaces originally considered in mirror symmetry were Cala bi–Yau mani-
folds. Roughly speaking, the mirror to a compact Calabi–Yau manifold X is another
compact Calabi–Yau manifold X ∨ of the same dimension. For example, it is in this
context that we have the equivalence, discovered by Candelas–de la Ossa–Green–
Parkes [10] and proven mathematically by Givental [15] and Lian–Liu– Yau [33], be-
tween the Gromov–Witten theory of the quintic threefold V5 ⊂ P4 and the theory
of period integrals on a family of Calabi–Yau threefolds known as “mirr or quintics.”
However, mirror symmetry can be considered for other classes of manifolds such as
manifolds of general type (Ω n
X ample), for which a proposal has recently been made
by Kapustin–Katzarkov–Orlov–Yotov [27], and (our present conc ern) manifolds with
an eﬀective anticanonical divisor. In both of these latter cases th e mirror is not a
manifold of the same class.
LetX be an n–dimensional K¨ ahler manifold with an eﬀective anticanonical divisor
D. We regard D as part of the data, and write ( X,D ) for the pair. We also choose
a meromorphic ( n, 0)–form Ω with no zeros and polar locus equal to D. According
to Hori–Vafa [25] and Givental, the mirror to ( X,D ) is a Landau–Ginzburg model
(X ∨,W ), consisting of a K¨ ahler manifold X ∨, together with a holomorphic function
W :X ∨ → C, called the superpotential.
The mirrors of toric Fano manifolds were derived by Hori–Vafa [25, §5.3] based
on physical considerations. Let X be an n–dimensional toric Fano manifold, and
let D be the complement of the open torus orbit. The mirror is then X ∨ = ( C∗)n
with a superpotential W given by a sum of monomials corresponding to the one-
dimensional cones in the fan for X. Choose a polarization OX (1) with corresponding
moment polytope P , a lattice polytope in Rn. For each facet F of P , let ν(F ) to
be the primitive integer inward-pointing normal vector, and let α(F ) be such that
⟨ν(F ),x ⟩ +α(F ) = 0 is the equation for the hyperplane containing F . Then mirror
Landau-Ginzburg model is given by
(7) X ∨ = (C∗)n, W =
∑
F facet
e−2πα(F )zν(F ),
where zν(F ) is a monomial in multi-index notation.
In the case where X is toric but not necessarily Fano, a similar formula for the
mirror superpotential is expected to hold, which diﬀers by the addit ion of “higher
order” terms [14, Theorems 4.5, 4.6].
The Hori–Vafa formula contains the case of the projective plane CP2 with the toric
boundary as anticanonical divisor. If x,y,z denote homogeneous coordinates, then
Dtoric can be taken to be {xyz = 0}, the union of the coordinate lines. We then have
(8) X ∨
toric = (C∗)2, W toric =z1 +z2 + e−Λ
z1z2
where Λ is a parameter that measures the cohomology class of the K ¨ ahler formω on
CP2.
The example with which we are primarily concerned in this paper is also CP2, but
with respect to a diﬀerent, non-toric boundary divisor. Consider t he meromorphic
6 JAMES PASCALEFF
(2, 0)–form Ω = dx ∧ dz/(xz − 1), whose polar locus is the binodal cubic curve
D = {xyz −y3 = 0}. Thus D =L ∪C is the union of a conic C = {xz −y2 = 0} and
a line {y = 0}. The construction of the mirror to this pair ( CP2,D ) is due to Auroux
[7], and we have
X ∨ = {(u,v ) ∈ C2 |uv ⁄= 1}, W =u + e−Λv2
uv − 1
(9)
A direct computation shows that both superpotentials Wtoric andW have the same
critical values
(10) {3e−Λ /3e−2πi(n/3) |n = 0, 1, 2}.
It is also easy to see that any regular ﬁber of W −1
toric(c) ⊂ X ∨
toric is a three-times-
punctured elliptic curve, while any regular ﬁber W −1(c) ⊂ X ∨ is a twice-punctured
elliptic curve. This is an example of the general expectation that par tially smoothing
the anticanonical divisor corresponds to partially compactifying th e total space of the
Landau–Ginzburg model.
1.2.2. Torus ﬁbrations and aﬃne manifolds. One justiﬁcation that (8)–(9) are ap-
propriate mirrors is found in the Strominger–Yau–Zaslow proposal, which expresses
mirror symmetry geometrically in terms of dual torus ﬁbrations, a r elationship also
known as T–duality. Ideally, one would expect that X \D and X ∨ are dual special
Lagrangian torus ﬁbrations over the same base B. When this holds true, the mirror
X ∨ can be constructed as the complexiﬁed moduli space of special Lagrangian ﬁbers
of X \D [35], [23],[7, §2]. The superpotential W can be expressed as a function on
this moduli space counting Maslov index two disks with boundary on th e Lagrangian
ﬁbers of X \D, weighted by symplectic area and the holonomy of a local system [7].
For our purposes, a Lagrangian submanifold L of a K¨ ahler manifoldX with mero-
morphic (n, 0)–form Ω is called special of phase φ if Im(e−iφΩ) |L = 0. Obviously
this only makes sense in the complement of the polar locus D. The inﬁnitesimal
deformations of a special Lagrangian submanifold are given by H 1(L; R), and are
unobstructed [35]. If L ∼=T n is a torus, H 1(L; R) is an n–dimensional space, and in
good cases the special Lagrangian deformations of L are all disjoint, and form the
ﬁbers of a ﬁbration π : X \D → B, where B is the global parameter space for the
deformations of L.
Assuming this, deﬁne the complexiﬁed moduli space of deformations of L to be
the space ML consisting of pairs ( Lb, Eb), where Lb =π−1(b) is a special Lagrangian
deformation of L, and Eb is a U(1) local system on Lb. There is an obvious projection
π∨ : ML →B given by forgetting the local system. The ﬁber ( π∨)−1(b) is the space
of U(1) local systems on the given torus Lb, which is precisely the dual torus L∨
b . In
this sense, the ﬁbrations π and π∨ are dual torus ﬁbrations, and the SYZ proposal
can be taken to mean that the mirror X ∨ is precisely this complexiﬁed moduli space:
X ∨ = ML. The picture is completed by showing that ML naturally admits a complex
structureJ ∨, a K¨ ahler formω∨, and a holomorphic (n, 0)–form Ω ∨. One ﬁnds that Ω ∨
is constructed from ω, whileω∨ is constructed from Ω, thus expressing the interchange
of symplectic and complex structures between the two sides of the mirror pair. For
details we refer the reader to [23],[7, §2].
MIRROR OF THE PROJECTIVE PLANE 7
However, this picture of mirror symmetry cannot be correct as st ated, as it quickly
hits upon a major stumbling block: the presence of singular ﬁbers in t he original
ﬁbration π : X \ D → B. These singularities make it impossible to obtain the
mirror manifold by a ﬁberwise dualization, and generate “quantum co rrections” that
complicate the T-duality prescription. Attempts to overcome this d iﬃculty led to
the work of Kontsevich and Soibelman [30, 31] and Gross and Sieber t [19, 20, 21]
that implements the SYZ program in an algebro-geometric context. In the case of
K3 surfaces, the work of Fukaya–Oh–Ohta–Ono [13] relates this p roblem to the wall–
crossing of holomorphic disk moduli spaces. It is also this diﬃculty whic h motivates
us to consider the case of CP2 relative to a binodal cubic curve, where the simplest
type of singularity arises.
In the case of X with eﬀective anticanonical divisor D, we can see these corrections
in action if we include the superpotential W into the SYZ picture. As W is to be
a function on X ∨, which is naively ML, W assigns a complex number to each pair
(Lb, Eb). This number is a count of holomorphic disks with boundary on Lb, of Maslov
index 2, weighted by symplectic area and the holonomy of Eb:
(11) W (Lb, Eb) =
∑
β∈π2(X,Lb),µ(β)=2
nβ(Lb) exp(−
∫
β
ω)hol(Eb,∂β )
where nβ(Lb) is the count of holomorphic disks in the class β passing through a
general point of Lb.
In the toric case, X \D ∼= (C∗)n, and we the special Lagrangian torus ﬁbration
is simply the map Log : X \D → Rn, Log(z1,...,z n) = (log |z1|,..., log |zn|). This
ﬁbration has no singularities, and the above prescriptions work as s tated. In the toric
Fano case, we recover the Hori–Vafa superpotential (7).
In the case of CP2 with the non-toric divisor D, the torus ﬁbration has one singular
ﬁber, which is a pinched torus (a focus-focus singularity). The abo ve prescription
breaks down: one ﬁnds that the superpotential counting disks is n ot a continuous
function on the moduli space of special Lagrangians. This leads one to redeﬁne X ∨
by breaking it into pieces and re-gluing so as to make W continuous, leading to (9) [7].
We ﬁnd that X ∨ also admits a special Lagrangian torus ﬁbration with one singular
ﬁber.
In general, the structure of a special Lagrangian torus ﬁbration π :X →B yields
the structure of an tropical aﬃne manifold on the base B. This is a manifold with
a distinguished collection of aﬃne coordinate charts, such that the transition maps
between aﬃne coordinate charts lie in Aﬀ Z(Rn) = GL(n, Z) ⋊ Rn, the group of aﬃne
linear transformations with integral linear part. When singular ﬁber s are present
in the torus ﬁbration, we simply regard the aﬃne structure as being undeﬁned at
the singular ﬁbers and call the resulting structure on the base a singular tropical
aﬃne manifold . In fact, the base B inherits two aﬃne structures, one from the
symplectic form ω, and one from the holomorphic ( n, 0)–form Ω. The former is called
the symplectic aﬃne structure , and the latter is called the complex aﬃne structure .
Let us recall brieﬂy how the local aﬃne coordinates are deﬁned. Fo r the symplec-
tic aﬃne structure, we choose a collection of loops γ1,...,γ n that form a basis of
H1(Lb; Z). Let X ∈TbB be a tangent vector to the base, and take ˜X be any vector
8 JAMES PASCALEFF
ﬁeld along Lb which lifts it. Then
(12) αi(X) =
∫ 2π
0
ωγi(t)( ˙γi(t), ˜X(γi(t)))dt
deﬁnes a 1-form on B: since Lb is Lagrangian, the integrand is independent of the lift
˜X, and αi only depends on the class of γi in homology. In fact, the collection ( αi)n
i=1
forms a basis of T ∗
bB, and there is a coordinate system ( yi)n
i=1 such that dyi = αi;
these are the aﬃne coordinates. This deﬁnition actually shows us th at there is a
canonical isomorphism T ∗
bB ∼= H1(Lb; R). This isomorphism induces an integral
structure on T ∗
bB: (T ∗
bB)Z ∼=H1(Lb; Z), which is preserved by all transition functions
between coordinate charts. Thus, when an aﬃne manifold arises as the base of a torus
ﬁbration in this way, the structural group is reduced to Aﬀ Z(Rn) = GL(n, Z) ⋊ Rn,
the group of aﬃne linear transformations with integral linear part.
The complex aﬃne structure follows exactly the same pattern, only that we take
Γ 1,..., Γ n to be ( n − 1)–cycles forming a basis of Hn−1(Lb; Z), and in place of ω we
use Im(e−iφΩ). Now we have an isomorphism T ∗
bB ∼= Hn−1(Lb; R), or equivalently
TbB ∼=H1(Lb; R), which induces the integral structure.
The aﬃne manifolds we consider in this article satisfy a stronger integ rality condi-
tion, which requires the translational part of each transition func tion to be integral
as well. We use the term integral aﬃne manifold to denote an aﬃne manifold whose
structural group has been reduced to Aﬀ( Zn) = GL(n, Z) ⋊ Zn. Such aﬃne manifolds
are “deﬁned over Z” and have an intrinsically deﬁned lattice of integral points.
For an integral aﬃne manifold, it makes sense to speak of tropical s ubvarieties.
These are certain piecewise linear complexes contained in B, which in some way cor-
respond to holomorphic or Lagrangian submanifolds of the total sp ace of the torus
ﬁbration. Tropical geometry has played a role in much work on mirror symmetry, par-
ticularly in the program of Gross and Siebert, and closer to this pape r, in Abouzaid’s
work on mirror symmetry for toric varieties [1, 3]. See [26] for a gen eral introduction
to tropical geometry. Though most of the methods in this paper ar e explicitly sym-
plectic, tropical geometry appears in section 2, where we compute the tropicalization
of the ﬁber of the superpotential, and in section 5, where a class of tropical curves
corresponding to holomorphic polygons is considered.
1.2.3. Homological mirror symmetry. The results on Floer cohomology that we prove
fall under the heading homological mirror symmetry (HMS) [28], whic h holds that
mirror symmetry can be interpreted as an equivalence of categorie s associated to the
complex or algebraic geometry of X, and the symplectic geometry of X ∨, and vice–
versa. The categories which are appropriate depend somewhat on the situation, so
let us focus on the case of the a manifold X with anticanonical divisor D, and its
mirror Landau–Ginzburg model ( X ∨,W ).
Associated to (X,D ), we take the derived category of coherent sheaves Db(CohX),
while to (X ∨,W ) we associate a Fukaya-type A ∞-category F(X ∨,W ) whose objects
are certain Lagrangian submanifolds of X ∨, morphism spaces are generated by in-
tersection points, and the A ∞ product structures are deﬁned by counting pseudo-
holomorphic polygons with boundary on a collection of Lagrangian sub manifolds.
Our main reference for Floer cohomology and Fukaya categories is t he book of Seidel
[41].
MIRROR OF THE PROJECTIVE PLANE 9
The superpotential W enters the deﬁnition of F(X ∨,W ) by restricting the class
of objects to what are termed admissible Lagrangian submanifolds . In this paper,
it will mean that we allow Lagrangian submanifolds that are not closed b ut which
have boundary on a reducible hypersurface whose components ar e deﬁned by setting
one term of the superpotential equal to a constant. Historically, there have been
several attempts to formulate the notion of admissibility. Originally, Kontsevich [29]
and Hori–Iqbal–Vafa [24] considered those Lagrangian submanifoldsL, not necessarily
compact, which outside of a compact subset are invariant with resp ect to the gradient
ﬂow of Re( W ). An alternative formulation, due to Abouzaid [1, 3], trades the non -
compact end for a boundary on a ﬁber {W = c} of W , together with the condition
that, near the boundary, the L maps by W to a curve in C. A further reformulation,
which is more directly related to the SYZ picture, replaces the ﬁber {W = c} with
the union of hypersurfaces ⋃
β{zβ = c}, where zβ is the term in the superpotential
(11) corresponding to the class β ∈π2(X,π −1(b)), and admissibility means that near
{zβ = c}, L maps by zβ to a curve in C. The admissibility condition we use in this
paper is closest to this last formulation.
With these deﬁnitions, homological mirror symmetry amounts to an e quivalence
of categories DπF(X ∨,W ) →Db(CohX), where Dπ denotes the split-closed derived
category of the A ∞–category. This piece of mirror symmetry has been addressed
many times [9, 8, 37, 1, 3, 11], including results for the projective pla ne and its toric
mirror.
However, in this article, we emphasize less the equivalences of categ ories themselves,
and focus more on geometric structures which arise from a combina tion of the HMS
equivalence with the SYZ picture. When dual torus ﬁbrations are pr esent on the
manifolds in a mirror pair, one expects the correspondence betwee n coherent sheaves
and Lagrangian submanifolds to be expressible in terms of a Fourier– Mukai transform
with respect to the torus ﬁbration [32]. In particular, Lagrangian s ubmanifolds L ⊂
X ∨ that are sections of the torus ﬁbration correspond to line bundles on X, and the
Lagrangians L(d) we consider are of this type.
In this context, our Theorem 1.1 can be interpreted as yielding an em bedding (at
the cohomology level) of the subcategory of F(X(B),W ) containing the Lagrangians
L(d) into Db(Coh CP2).
1.2.4. Distinguished bases. The combination of SYZ and HMS also gives rise to the
expectation that, at least in favorable situations, the spaces of s ections of coherent
sheaves on X can be equipped with distinguished bases. Suppose that F : F(X ∨) →
Db(X) is a functor implementing the HMS equivalence. Let L1,L 2 ∈ Ob(F(X ∨)) be
two objects of the Fukaya category supported by transversely intersecting Lagrangian
submanifolds. Then
(13) HF (L1,L 2) ∼= RHom(F (L1),F (L2)).
Suppose furthermore that the diﬀerential on the Floer cochain co mplex CF (L1,L 2)
vanishes, so that HF (L1,L 2) ∼= CF (L1,L 2). As CF (L1,L 2) is deﬁned to have a
basis in bijection with the set of intersection points L1 ∩L2, one obtains a basis of
RHom(F (L1),F (L2)) parametrized by the same set via the above isomorphisms. If
F is some sheaf of interest, and by convenient choice of L1 and L2 we can ensure
F (L1) ∼= OX and F (L2) ∼= F, then we will obtain a basis for H i(X, F).
10 JAMES PASCALEFF
WhenE andE∨ are mirror dual elliptic curves, this phenomenon is evident in the
work of Polishchuk–Zaslow [36] and especially M. Gross [6, Ch. 8]. Both E and E∨
may be written as special Lagrangian S1-ﬁbrations over the same base B ∼=S1. The
base has an integral aﬃne structure as R/Z. The Lagrangians L(d) ⊂E∨ are sections
of this torus ﬁbration with slope d, and their intersection points project precisely to
the fractional integral points of the base B.
(14) L(0) ∩L(d) ↔B
(1
d Z
)
:= 1
d -integral points of B
Under HMS, we obtain F (L(0)) = OE andF (L(d)) = OE(d). the basis of intersection
pointsL(0) ∩L(d) corresponds to a basis of Γ( E, OE(d)) consisting of theta functions.
Another illustration is the case of toric varieties and their mirror Lan dau-Ginzburg
models [1, 3]. In this case, Abouzaid constructs a family of Lagrangia n submanifolds
L(d) mirror to the powers of the ample line bundle OX (d). These Lagrangian sub-
manifolds are topologically discs with boundary on a level set of the su perpotential,
W −1(c) for some c. For d> 0, the Floer complex CF ∗(L(0),L (d)) is concentrated in
degree zero. Hence
(15) CF 0(L(0),L (d)) = HF 0(L(0),L (d)) = H 0(X, OX (d)).
The basis of intersection points L(0) ∩L(d) corresponds to the basis of characters
of the algebraic torus T = ( C∗)n which appear in the T -module H 0(X, OX (d)). The
same formula (14) is valid in the case of toric varieties, where the bas e B is the
moment polytope P of the toric variety X. Abouzaid interprets P as a subset of the
base of the torus ﬁbration on X ∨ = ( C∗)n (the ﬁbration given by the Cliﬀord tori),
which moreover appears as a chamber bounded by a tropical variet y corresponding
to a level set W −1(c) of the superpotential.
As is explained in section 2, these features are also present in our ca se. The base
B is identiﬁed with the base of the torus ﬁbration on CP2 \D, with its symplectic
aﬃne structure, and also identiﬁed as a subset of base of the toru s ﬁbration on X ∨
with its complex aﬃne structure, bounded by the tropicalization of a level set of the
superpotential. We once again ﬁnd a bijection between the intersec tion points of our
Lagrangians L(d) and the fractional integral points of the aﬃne base.
Ongoing work of Gross–Hacking–Keel [17] seeks to extend these c onstructions to
other manifolds, such as K3 surfaces, using a purely algebraic and t ropical framework.
In this paper we are concerned with extensions to cases that are t ractable from the
point of view of symplectic geometry, although the tropical analog o f our results is
described in section 5.
