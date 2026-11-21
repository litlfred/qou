---
doc_id: arxiv-math-0203194v1
doc_title: "Period mappings and differential equations. From C to Cp"
section_id: sec-099-m-totaros-theorem
section_title: "Totaro's theorem."
section_number: M
pages: 237-256
source_pdf: 0203194v1.pdf
source_sha256: 6f35e530f07116dc
toc_source: inferred
doc_brief: "Period mappings and differential equations. From C to Cp — 101 sections: Front matter; Purpose of this book.; Contents of this book."
---
233
slope grading of the isocrystal (V ⊗K0, b(id ⊗σ)). (The sign of our ν is
diﬀerent from the one in [Kot85].) For a suitable positive integer s, sν is
regarded as a one-parameter subgroup of G over K0.
Deﬁnition 2.3. A σ-conjugacy class ¯b of G(K0) is decent if there is an
element b ∈¯b such that
(bσ)s = sν(p)σs
for some positive integer s.
One knows that, for a decent σ-conjugacy class ¯b, b and ν as above are
deﬁned over Qps. If G is connected and k is algebraically closed, then any
σ-conjugacy class is decent. [Kot85]
2.4. Let K be a totally ramiﬁed ﬁnite extension of K0 in K0. For a one-
parameter subgroup λ : Gm →G over K and an element b ∈G(K0), we
have an exact ⊗-functor
I : RepQp(G) →MF(K)
which is deﬁned by V 7→(V ⊗K0, b(id⊗σ), F.
λ). Here VK,λ,j is the subspace
of V ⊗K of weight j with respect to λ and
F i
λ = ⊕
j≥i VK,λ,j
is the weight ﬁltration associated to λ.
Deﬁnition 2.5. A pair (λ, b) as above is weakly admissible if and only if
the ﬁltered isocrystal I(V ) over K is so for any object V in RepQp(G).
To see the weak admissibility for (λ, b), it is enough to check the weak
admissibility of I(V ) for a faithful representation V of G.
Indeed, any
representation of G appears as a direct summand of V ⊗m ⊗(V ∨)⊗n and
I(V )⊗m ⊗(I(V )∨)⊗n is weakly admissible by Faltings (see 1.3). Here V ∨
(resp. I(V )∨) is the dual of V (resp. I(V )).
3. Totaro’s theorem.
In this section we assume that k is algebraically closed.
3.1. Let G be a reductive algebraic group over Qp. We ﬁx a conjugacy class
of a one-parameter subgroup λ : Gm →G over K0. Here two one-parameter
subgroups λ, λ′ are conjugate if and only if gλg−1 = λ′ for some element
g ∈G(K0). Then, there is a ﬁnite extension E of Qp in K0 such that the
conjugacy class of λ is deﬁned over E. Let us suppose that λ is deﬁned over
E and denote by ˘E the composite ﬁeld EK0 in K0
3.2. Two one-parameter subgroups of G over K0 are equivalent if and only
if they deﬁne the same weight ﬁltration for any object in RepQp(G). Note
that, if two one-parameter subgroups are equivalent, then they belong to
the same conjugacy class.
234
C. p-ADIC SYMMETRIC DOMAINS AND TOTARO’S THEOREM
Consider the functor
R 7→{the equivalence classes in the conjugacy class of λ deﬁned over R}
on the category of E-algebras. If one deﬁnes an algebraic subgroup of G
over E by
P(λ)(K0) = {g ∈G(K0) | gλg−1 is equivalent to λ},
then P(λ) is parabolic and the functor above is represented by the projective
variety GE/P(λ). We denote this homogeneous space over E by Fλ. If V
is a faithful representation in RepQp(G) and if we denote by Flagλ(V ) the
ﬂag variety over Qp which represents the functor
R 7→
 the ﬁltrations F. of V ⊗R as R-modules such that
F i is a direct summand and rankRF i = dimK0 F i
λ(V ⊗K0)

on the category of Qp-algebras, then there is a natural E-closed immersion
Fλ →Flagλ(V ) ⊗Qp E.
3.3. Let b ∈G(K0). For a ﬁnite extension K of ˘E, a point ξ in Fλ(K)
is called weakly admissible if and only if the pair (ξ, b) is weakly admissi-
ble. This condition is independent of the choice of the representative in the
equivalence class ξ. We denote by Fwa
λ,b(K) the subset of weakly admissi-
ble points. Totaro gave a characterization of Fwa
λ,b in the sense of geometric
invariant theory. [Tot96] We explain his theory in the rest of this section.
3.4. For a maximal torus T in GK0, let X∗(T) be the free abelian group of
characters, X∗(T) the free abelian group of one-parameter subgroups, and
< , >: X∗(T) × X∗(T) →Z the perfect pairing with χ(ξ(t)) = t<χ,ξ>. If
N(T) is the normalizer of T in G, the Weyl group W(T) = N(T)/T acts
X∗(T) via inner automorphisms.
Now we ﬁx an invariant norm || || on G, a non-negative real valued
function on the set of one-parameter subgroups of GK0, such that
a) ||gξg−1|| = ||ξ|| for any g ∈G(K0),
b) for any maximal torus T, there is a positive deﬁnite rational valued
bilinear form ( , ) on X∗(T) ⊗Q with (ξ, ξ) = ||ξ||2,
c) ||γ(ξ)|| = ||ξ|| for γ ∈Gal(K0/K0), where γ(ξ)(t) = γ(ξ(t)).
The bilinear form on X∗(T) ⊗Q as above is invariant under the action
of the Weyl group by (a). For any maximal torus T, invariant norms are
in one-to-one correspondence with (Gal(K0/K0), W(T))-invariant positive
deﬁnite rational valued bilinear forms on X∗(T) ⊗Q since all maximal tori
are conjugate and, if gξg−1 ∈X∗(T) for ξ ∈X∗(T) and g ∈G(K0), then
there is h ∈W(T) with gξg−1 = hξh−1 by [MFK94]. (See also [Kem78]
and [Tot96].) Hence, such an invariant norm exists.
3.5. Now we assume that G is connected. Let U(λ) be the unipotent radical
of P(λ), whose elements act on the graded space gr F.
λ trivially. Then there
is a bijection between the set of maximal tori of G in P(λ) and the set of
3. TOTARO’S THEOREM.
235
maximal tori of P(λ)/U(λ) by the natural projection T 7→T. Hence, the
invariant norm on G induces the one on P(λ)/U(λ). Fix a maximal torus
T of G. Since the image of λ is contained in the center of P(λ)/U(λ), the
perfect pairing associated to the invariant norm determines the dual of λ
in X∗(T ). This dual can extend to a character ⊗Q of P(λ)/U(λ). Now we
deﬁne a G-line bundle ⊗Q, Lλ, on Fλ by the associated one to the negative
of the dual character ⊗Q of λ. By construction, the line bundle ⊗Q, Lλ,
depends only on the conjugacy class of λ and is ample.
Let J be a smooth aﬃne group scheme over Qp such that
J(Qp) = {g ∈G(K0) | g(bσ) = (bσ)g}
(which is introduced in [RZ96]). Since JK0 ⊂GK0, the pull back Lλ ˘E of
Lλ on Fλ ˘E is an ample J ˘E-line bundle.
By the same construction as above, ν in 2.2 gives a character ⊗Q of
P(ν). The opposite of this character ⊗Q determines a J ˘E-action ⊗Q on the
trivial line bundle on Fλ ˘E since JK0 ⊂P(ν). We denote it by L0
ν.
We put a J ˘E-line bundle ⊗Q, L = Lλ ˘E ⊗L0
ν, on Fλ ˘E. Then it is ample
and depends only on b and the conjugacy class of λ. We denote by Fss
λ (L)
the set of semistable points in Fλ with respect to L in the sense of D.
Mumford [MFK94].
Theorem 3.6. [Tot96] Suppose that G is connected and reductive. For any
ﬁnite extension K of ˘E, we have
Fwa
λ,b(K) = Fss
λ ˘E(L)(K).
We shall sketch Totaro’s proof. First, let G = GL(n) and let us consider
the invariant norm induced by the pairing
(α, β) =
X
i,j
ij dimK0 gri
F.
αgrj
F.
β(Kn)
for one-parameter subgroups ⊗Q, α, β of GL(n) over K. If one puts µα(V ) =
(
X
i
i dimK gri
F.
α(V ⊗K))/ dim V , then one has
(α, β) =
Z
(µα(F j
β) −µα(V )) dimK F j
βdj + µα(V )µβ(V ) dim V.
So, (ξ, b) is weakly admissible if and only if (ξ, α) + (ν, α) ≤0 for any
one-parameter subgroup α of GL(n) over K0 with the ﬁltration F.
α as
subisocrystals.
In other words, (ξ, b) is weakly admissible if and only if
(ξ, α) + (ν, α) ≤0 for any one-parameter subgroup α of J over Qp. Hence,
the assertion follows from the calculation of Mumford’s numerical invariant
below.
Lemma 3.7. If µ(ξ, α, L) is Mumford’s numerical invariant of ξ ∈Fλ for a
one-parameter subgroup α of J over Qp, then
µ(ξ, α, L) = −(ξ, α) −(ν, α).
236
C. p-ADIC SYMMETRIC DOMAINS AND TOTARO’S THEOREM
Next, let G be arbitrary, V a faithfully representation of G, and consider
the invariant norm on G induced from the above norm by the natural immer-
sion G →GL(V ). The Mumford’s numerical invariant of weakly admissible
points is non-negative for any one-parameter subgroup of J(GL(V )). Hence
it is so for any one-parameter subgroup of J, and the weak admissibility
implies the semistability. To see the converse, one needs to show that, if
ξ ∈Fss
λ (L)(K), (ξ, α) + (ν, α) ≤0 for any one-parameter subgroup α of
J(GL(V )) over Qp. If α is semistable for the GK-line bundle Lα on Fα, the
assertion follows from the ﬁrst part. In the case where α is not semistable,
one can use Kempf’s ﬁltration [Kem78] and Ramanan and Ramanathan’s
work [RR84], and obtains the required inequality.
Finally one needs to prove the independence of the choice of the norm.
Suppose that the identity is valid for the particular norm.
Since G is a
quotient of a product of a torus and some simple algebraic groups by a
ﬁnite central subgroup [BT65], one can reduce the assertion in the case of
tori and simple groups. In the case of tori it was proved in [RZ96], and in
the case of simple groups it is true since the norm of the simple group comes
from the Killing form up to a positive rational multiple.
□
4. p-adic symmetric domains.
Let k be the algebraic closure of the prime ﬁeld Fp, Cp the p-adic com-
pletion of a ﬁxed algebraic closure Qp of Qp, and K0 = bQur
p
the p-adic
completion of the unramiﬁed extension in Cp.
4.1. Let G be a reductive group over Qp, b ∈G(K0), and ﬁx a conjugacy
class {λ} of a one-parameter subgroup λ of G over Qp.
Rapoport and Zink gave a rigid analytic structure on Fwa
λ,b as an admis-
sible open subset in Fλ ˘E and call it the p-adic symmetric domain associated
to the triple (G, {λ}, b) in [RZ96]. This notion of p-adic symmetric domains
is diﬀerent from that of M. van der Put and H. Voskuil in [vdPV92]. In-
deed, for any discrete co-compact subgroup Γ of G( ˘E), the quotient Fwa
λ,b/Γ
is not always a proper analytic space over ˘E.
Theorem 4.2. [RZ96] The set Fwa
λ,b of weakly admissible points with respect
to b in Fλ(Cp) is an admissible open subset of Fλ ˘E as a rigid analytic space.
Now we sketch the proof of the theorem in [RZ96]. By [Kot85] one may
assume that the σ-conjugacy class of b is decent with the decent equation
(bσ)s = sν(p)σs as in 2.3. Let V be a faithful representation in RepQp(G),
Vs = V ⊗Qps, and Φs = b(id⊗σ). Then (V ⊗K0, b(id⊗σ)) = (Vs, Φs)⊗QpsK0.
Put Vs = ⊕
λ Vs,j to be the isotypical decomposition for Φs. The functor
R 7→{V ′ ⊂Vs⊗QpsR | V ′ is a direct summand with V ′ = ⊕
j V ′∩(Vs,j⊗QpsR)}
on the category of Qps-algebras is represented by a disjoint sum T ′ of closed
subschemes of Grassmannians of Vs. T ′ descends to a Qp-variety T and one
4. p-ADIC SYMMETRIC DOMAINS.
237
has
T(Qp) = {Φs-stable subspaces of Vs}.
Indeed, Φs gives a descent datum α : T ′ →T ′σ, where T ′σ(R) is a set of
direct summands of Vs,λ ⊗Qps,σ R with the isotypical decomposition, and
αs−1 ◦· · · ◦α : T ′ →T ′ is the identity by the decent equation.
Consider the closed subscheme over Qps
H ⊂(Flagλ(V ) × T) ⊗Qp Qps
which consists of pairs (F., V ′) such that
X
i
i rank gri
F.∩V ′ (V ′) > ordp(det(Φs|V ′
j )).
Then, by the deﬁnition of weak admissibility, one has
Fwa
λ,b(Cp) = Fλ(Cp) ∩

Flagλ(V )(Cp) −
[
t∈T(Qp)
Ht

,
where Fλ(Cp) is identiﬁed with the image of the immersion Fλ(Cp) ⊂
Flagλ(Cp).
Fix embeddings of Flagλ(V ) and T in projective spaces over Qp and a
ﬁnite set {fj} of bi-homogeneous polynomials of deﬁnition of Flagλ(V ) × T
with integral coeﬃcients. For ǫ > 0, consider a tubular neighbourhood
Ht(ǫ) = {x ∈Flagλ(V )(Cp) | |fj(x, t)| < ǫ for all j}
of Ht.
Here we choose unimodular representatives for x and t’s and | |
is an absolute value on Cp.
Then there is a ﬁnite set S ⊂T(Qp) such
that S
t∈T(Qp) Ht(ǫ) = S
t∈S Ht(ǫ) for the local compactness. Fǫ = Fλ(Cp) ∩
(Flagλ(V )(Cp)−S
t∈T(Qp) Ht(ǫ)) is an admissible open subset of Fwa
λ,b ˘E, hence
F1 ⊂F 1
2 ⊂F 1
3 ⊂· · ·
is an admissible covering of Fwa
λ,b ˘E.
□
238
C. p-ADIC SYMMETRIC DOMAINS AND TOTARO’S THEOREM
Bibliography
[AB01]
Y. Andr´e and F. Baldassarri, De Rham cohomology of diﬀerential modules on
algebraic varieties, Progress in Mathematics, vol. 189, Birkh¨auser, 2001.
[And90]
Y. Andr´e, p-adic Betti lattices, in: p-adic analysis, Proc. Trento conf. on p-
adic analysis (F. Baldassarri, S. Bosch, and B. Dwork, eds.), Lecture Notes
in Math, vol. 1454, Springer, 1990, 23–63.
[And92]
Y. Andr´e, R´ealisation de Betti des motifs p-adiques, preprint IHES, 1992.
[And95]
Y. Andr´e, Th´eorie des motifs et interpr´etation g´eom´etrique des valeurs p-
adiques de G-functions, Number theory (S. David, ed.), Cambridge Univ.
Press., 1995, 37–60.
[And96]
Y. Andr´e, G-functions et transcendance, J. Reine Angew. Math. 476 (1996),
95–125.
[And98]
Y. Andr´e, p-adic orbifolds and p-adic triangle groups, R.I.M.S. Kokyuroku,
vol. 1073, 1998, 136–159.
[And02a]
Y. Andr´e, Repr´esentations galoisiennes et op´erateurs de Bessel p-adiques,
preprint, to appear in Ann. Inst. Fourier, 2002.
[And02b]
Y. Andr´e, Filtrations de type Hasse-Arf et monodromie p-adique, Invent.
Math. 148 (2002), 285–317.
[And]
Y. Andr´e, A geometric description of Gal(Qp/Qp) and a p-adic avatar of
ˆ
GT,
preprint, 2002.
[Bal82]
F. Baldassarri, Diﬀerential modules and singular points of p-adic diﬀerential
equations, Adv. in Math. 44 (1982), 155–179.
[BBM82]
P. Berthelot, L. Breen, and W. Messing, Th´eorie de Dieudonn´e cristalline II,
Lecture Notes in Math., vol. 930, Springer, 1982.
[BC91]
J.F. Boutot and H. Carayol, Uniformisation p-adique des courbes de Shimura:
les th´eor`em de ˇCerednik et de Drinfeld, in: Ast´erisque, vol. 196–197, S.M.F.,
1991, 45–158.
[BD98]
M. Bertolini and H. Darmon, Heegner points, p-adic l-functions, and the
ˇCerednik-Drinfeld uniformization, Invent. Math. 131 (1998), 453–491.
[BDR80]
S. Bosch, B. Dwork, and P. Robba, Un th´eoreme de prolongement pour des
fonctions analytiques, Math. Ann. 252 (1980), 165–173.
[Ber90]
V.G. Berkovich, Spectral theory and analytic geometry over non-Archimedean
ﬁelds, Mathematical Surveys and Monographs, no. 33, A.M.S., 1990.
[Ber93]
V.G. Berkovich, ´Etale cohomology for non-Archimedean analytic spaces, Inst.
Hautes ´Etudes Sci. Publ. Math. 78 (1993), 5–161.
[Ber99]
V.G. Berkovich, Smooth p-adic analytic spaces are locally contractible, Invent.
Math. 137 (1999), no. 1, 1–84.
[Be84]
P. Berthelot, Cohomologie rigide et th´eorie de Dwork: le cas des sommes
exponentielles, S.M.F. Ast´erisque 119–120 (1984), 17–49.
[Be86]
P. Berthelot, G´eom´etrie rigide et cohomologie des vari´et´es alg´ebriques de car-
act´eristique p > 0, M´emoire de la SMF 23 (1986), 7–32.
[Be96]
P. Berthelot, Cohomologie rigide et cohomologie rigide `a supports propres,
preprint IRMAR 96-03 (1996).
239
240
BIBLIOGRAPHY
[BGR84]
S. Bosch, U. G¨untzer, and R. Remmert, Non-Archimedean Analysis, Springer-
Verlag, 1984, Grundlehren der Math. Wiss.
[BL93]
S. Bosch and W. L¨utkebohmert, Formal and rigid geometry I, Rigid spaces,
Math. Ann. 295 (1993), 291–317.
[BLR90]
S. Bosch, W. L¨utkebohmert, and M. Raynaud, N´eron models, Ergebnisse der
Math., vol. 21, Springer, 1990.
[BM79]
P. Berthelot and W. Messing, Th´eorie de Dieudonn´e cristalline I, Ast´eisque
63 (1979), 17–38.
[BeO83]
P. Berthelot and A. Ogus, F-isocrystals and De Rham cohomology I, Invent.
Math. 72 (1983), 159–199.
[Bou64]
N. Bourbaki, Alg`ebre I, deuxi`eme ed., Hermann, 1964.
[Bou74]
N. Bourbaki, Topologie g´en´erale, Hermann/CCLS, 1974.
[Bou83]
N. Bourbaki, Vari´et´es diﬀ´erentielles et analytiques, fascicule de r´esultats,
CCLS, Paris, 1983.
[Bre99]
C. Breuil, Representations semi-stables et modules fortement divisibles, In-
vent. Math. 136 (1999), 89–122.
[Bre00]
C. Breuil, Groupes p-divisibles, groupes ﬁnis et modules ﬁltr´es, Annals of
Math. 152 (2000), 489–549.
[BT65]
A. Borel and J. Tits, Groupes r´eductifs, Inst. Hautes ´Etudes Sci. Publ. Math.
27 (1965), 55–151.
[BZ95]
J.F. Boutot and T. Zink, The p-adic uniformization of Shimura curves,
preprint 95-107, Sonderforschungsbereich 343, Univ. Bielefeld., 1995.
[Car61]
C. Caratheodory, Funktionentheorie II, Birkh¨auser, 1961.
[CC89]
D. Chudnovsky and G. Chudnovsky, Computational problems in arithmetic of
linear diﬀerential equations. some diophantine applications, Number Theory,
Lecture Notes in Math., vol. 1383, Springer, 1989, 12–49.
[ˇCer76]
I.V. ˇCerednik, Uniformization of algebraic curves by discrete subgroup of
PGL2(kw) with compact quotients,, Math. USSR-Sb. 29 (1976), 55–78.
[CF00]
P. Colmez and J.-M. Fontaine, Construction des repr´esentations p-adiques
semi-stables, Invent. Math. 140 (2000), no. 1, 1–43.
[Cho96]
F. Choucroun, Groupes d’automorphismes et fronti`eres d’arbres: le cas ho-
mog`ene, Progress in probability, vol. 40, Birkh¨auser, 1996, 209–221.
[C86]
G. Christol, Fonctions et ´el´ements alg´ebriques, Paciﬁc J. Math. 125 (1986),
1–37.
[Chl98]
Chambert-Loir, Cohomologie cristalline: un survol, Exposition. Math. 16
(1998), 333–382.
[CM97]
G. Christol and Z. Mebkhout, Sur le th´eor`em de l’indice des ´equations
diﬀ´erentielles p-adiques II, Ann. of Math. 146 (1997), 345–410.
[CM00]
G. Christol and Z. Mebkhout, Sur le th´eor`em de l’indice des ´equations
diﬀ´erentielles p-adiques III, Annals of Math. 151 (2000), 385–457.
[Col90]
R. Coleman, On the Frobenius matrices of Fermat curves, in: p-adic analysis,
Proc. Trento conf. on p-adic analysis (F Baldassarri, S. Bosch, and B. Dwork,
eds.), Lecture Notes in Math, vol. 1454, 1990, 173–193.
[Co91]
P. Colmez, P´eriodes des vari´et´es ab´eliennes `a multiplication complexe, Ann.
of Math. 138 (1993), 625–683.
[Co92]
P. Colmez, P´eriodes p-adiques des vari´et´es ab´eliennes, Math. Ann. 292
(1992), 629–644.
[Co94]
P. Colmez, Les nombres alg´ebriques sont denses dans B+
dR, P´eriodes p-adiques,
Ast´erisque, vol. 223, S.M.F., 1994.
[Co98]
P. Colmez, Int´egration p-adique, Ast´erisque, vol. 248, S.M.F., 1998.
[Cox74]
H.M.S. Coxeter, Regular complex polytopes, 1991, 2nd ed., Cambridge Univ.
Press, 1974.
BIBLIOGRAPHY
241
[Cox79]
H.M.S. Coxeter, The non-euclidian symmetry of Escher’s picture “circle limit
III”, Leonardo (1979), 19–25, Pergamon Press
[CR94]
G. Christol and P. Robba, Equations diﬀ´erentielles p-adiques; applications
aux sommes exponentielles, Hermann, 1994.
[Cr85]
R. Crew, F-isocrystals and p-adic representations, Algebraic Geometry - Bow-
doin, Proc. Symp. Pure Math. 17 (1985), 111–138.
[Cr00]
R. Crew, Canonical Extensions, Irregularities, and the Swan Conductor,
Math. Ann. 316 (2000), 19–37.
[CW01]
P. Cohen and G. W¨ustholz, A panorama in Number Theory, ch. Applications
of the Andr´e-Oort conjecture to transcendence, Cambridge Univ. Press, 2001.
[Del71]
P. Deligne, Travaux de Shimura, S´em. Bourbaki 389, Lecture Notes in Math.,
vol. 244, Springer, 1971.
[Del74]
P. Deligne, Th´eorie de Hodge III, Inst. Hautes ´Etudes Sci. Publ. Math. 44
(1974), 5–78.
[Del89]
P. Deligne, Le groupe fondamental de la droite projective moins trois points,
Galois groups over Q, Publ. Math. Sci. Res. Inst., vol. 16, Springer Verlag,
1989, Proc. Workshop, Berkeley/CA (USA) 1987, 79–297.
[dJ95a]
A.J. de Jong, Crystalline Dieudonn´e module theory via formal and rigid ge-
ometry, Inst. Hautes ´Etudes Sci. Publ. Math. 82 (1995), 5–96, erratum ibid.
87 (1998), 175.
[dJ95b]
A.J. de Jong, ´Etale fundamental groups of non-archimedean analytic spaces,
Compositio Math. 97 (1995), 89–118.
[dJvdP96]
A.J. de Jong and M. van der Put, Etale cohomology of rigid analytic spaces,
Doc. Math. 1 (1996), 1–56.
[DM93]
P. Deligne and G. Mostow, Commensurabilities among lattices in PU(1, n),
Princeton Univ. press, 1993.
[Dri76]
V.G. Drinfeld, Coverings of p-adic symmetric regions, Functional. Anal. Appl.
10 (1976), 29–40.
[dSh87]
E. de Shalit, Iwasawa theory of elliptic curves with complex multiplication,
Acad. Press, 1987.
[Dw69]
B. Dwork, p-adic cycles, Inst. Hautes ´Etudes Sci. Publ. Math. 37 (1969),
27–115.
[Dw74]
B. Dwork, Bessel functions as p-adic functions of the argument, Duke Math.
J. 41 (1974), 711–738.
[Dw82]
B. Dwork, Lectures on p-adic diﬀerential equations, Springer, NY, 1982.
[Dw83]
B. Dwork, On the Boyarsky principle, Amer. J. Math. 285 (1983), 115–156.
[Elk98]
N. Elkies, Shimura curve computations, Algorithmic number theory (J.P. Buh-
ler, ed.), L. N. Comput. Sci., vol. 1423, Springer, 1998, 3rd international
symposium, ANTS-III, Portland, O, USA, June 21–25 Proceedings, 1–47.
[Esc71]
M.C. Escher, The world of M.C. Escher, New York H. N. Abrams, 1971.
[Fal95]
G. Faltings, Mumford-Stabilit¨at in der algebraischen Geometrie, Proceedings
of ICM 1994 (Z¨urich), Birkh¨auser, 1995, 648–655.
[FM87]
J.-M. Fontaine and W. Messing, p-adic periods and p-adic etale cohomology,
Contemporary Mathematics 67 (1987), 179–207.
[Fon79]
J.-M. Fontaine, Modules galoisiens, modules ﬁltr´es et anneaux de Barsotti-
Tate, Ast´erisque, vol. 65, Soci´et´e Math´ematique de France, 1979.
[Fon94]
J.-M. Fontaine, Repr´esentations p-adiques semi-stables, P´eriods p-adiques,
S´eminaire de Bures, 1988, Ast´erisque, 223, S.M.F., (1994), 113–184.
[For29]
L. Ford, Automorphic functions, 1951, 2nd ed., Chelsea, New York, 1929.
[FvdP81]
J. Fresnel and M. van der Put, G´eom´etrie analytique rigide et applications,
Progress in Math, vol. 18, Birkh¨auser, Boston, Basel, Stuttgart, 1981.
[GH94a]
B. Gross and M. Hopkins, Equivariant vector bundles on the Lubin-Tate mod-
uli space, A.M.S. Contemp. Math. 158 (1994), 23–88.
242
BIBLIOGRAPHY
[GH94b]
B. Gross and M. Hopkins, The rigid analytic period mapping, Lubin-Tate
space, and stable homotopy theory, Bull. Amer. Math. Soc. (N.S.) 30 (1994),
76–86.
[GI63]
O. Goldmann and N. Iwahori, The space of p-adic norms, Acta. Math. 109
(1963), 137–177.
[Gor01]
U. G¨ortz, On the ﬂatness of models of certain Shimura varieties of PEL type,
Math. Ann. 321 (2001), 689–727.
[Gou97]
F.G. Gouvˆea, p-adic numbers, An Introduction, 2nd ed., Universitext,
Springer-Verlag, 1997.
[Gra86]
J. Gray, Linear diﬀerential equations and group theory from Riemann to
Poincar´e, Birkh¨auser, 1986.
[Gre81]
L. Greenberg, Homomorphisms of triangle groups into PSL(2, C), Riemann
surfaces and related topics, Ann. Math. Studies, vol. 97, 1981, Proc. 1978
Stony Brook Conf., 167–181.
[Gri71]
P. Griﬃths, Periods of integrals on algebraic manifolds III, Inst. Hautes
´Etudes Sci. Publ. Math. 38 (1971), 125–180.
[Gro70]
A. Grothendieck, Groupes de Barsotti-Tate et cristaux, Actes, Congr`es Intern.
Math., no. 1, 1970, 431–436.
[Gro74]
A. Grothendieck, Groupes de Barsotti-Tate et cristaux de Dieudonn´e, Presses
de l’Univ. Montr´eal, 1974.
[Gun67]
R. Gunning, Special coordinate covering of Riemann surfaces, Math. Ann.
170 (1967), 67–86.
[GvdP80]
L. Gerritzen and M. van der Put, Schottky groups and Mumford curves, Lec-
ture Notes in Math., vol. 817, Springer-Verlag, 1980.
[H81]
E. Hecke, Vorlesungen ¨uber die Theorie der algebraischen Zahlen, (Lectures
on the theory of algebraic numbers), vol. 77, Springer verlag, 1981.
[Heh75]
D. Hehjal, On Schottky and Teichm¨uller spaces, Adv. in Math. 15 (1975),
133–156.
[Her80a]
F. Herrlich, Die Ordnung der Automorphismengruppe einer p-adischen Schot-
tkeykurve, Math. Ann. 246 (1980), 125–130.
[Her80b]
F. Herrlich, Endlich erzeugbare p-adische diskontinuirliche Gruppen, Arch.
Math. 35 (1980), 505–515.
[Hub96]
R. Huber, ´Etale cohomology of rigid analytic varieties and adic spaces, As-
pects of Mathematics, vol. 30, Vieweg-Verlag, Wiesbaden, 1996.
[Hu87]
D. Husem¨oller, Elliptic curves, Graduate Texts in Mathematics, vol. 111,
Springer Verlag, 1987.
[Ic97]
T. Ichikawa, Schottky uniformization theory on Riemann surfaces and Mum-
ford curves of inﬁnite genus, J. reine angew. Math. 486 (1997), 45–68.
[IK98]
M.-N. Ishida and F. Kato, The strong rigidity theorem for non-archimedean
uniformization, Tˆohoku Math. J. (2) 50 (1998), 537–555.
[Iv86]
B. Iversen, Cohomology of sheaves, Universitext, Springer-Verlag, Berlin, Hei-
delberg, New York, Tokyo, 1986.
[Ka72]
N. Katz, Algebraic solutions of diﬀerential equations. p-curvature and the
Hodge ﬁltration, Invent. Math. 18 (1972), 1–118.
[Ka73]
N. Katz, Travaux de Dwork, S´eminaire Bourbaki, Lecture Notes in Math 317
(1973), 167–200.
[Ka81]
N. Katz, Serre-Tate local moduli, Surface Alg´ebriques, Lecture Notes in
Math., vol. 868, Springer, 1981, 138–202.
[Ka90]
N. Katz, Exponential sums and diﬀerential equations, Annals of Math. Stud-
ies, vol. 124, Princeton University press, 1990.
[Kat98]
F. Kato, On p-adic uniformization of fake projective planes, preprint: Max-
Planck-Institut f¨ur Mathematik Bonn (1998).
[Kat01]
F. Kato, p-adic schwarzian triangle groups of mumford type, preprint, 2001.
BIBLIOGRAPHY
243
[Kem78]
G. Kempf, Instability in invariant theory, Ann. of Math. 108 (1978), 299–316.
[Kie67a]
R.
Kiehl,
Der
Endlichkeitssatz
f¨ur
eigentliche
Abbildungen
in
der
nichtarchimedischen Funktionentheorie, Invent. Math. 2 (1967), 191–214.
[Kie67b]
R. Kiehl, Die de Rham Kohomologie algebraischer Mannigfaltigkeiten ¨uber
einem bewerteten k¨orper, Inst. Hautes ´Etudes Sci. Publ. Math. 33 (1967),
5–20.
[Kie67c]
R. Kiehl, Theorem A und Theorem B in der nichtarchimedischen Funktionen-
theorie, Invent. Math. 2 (1967), 256–273.
[Ko79]
N. Koblitz, The hypergeometric function with p-adic parameters, Proceedings
of the Queen’s Number Theory Conference (Ontario), 1979, 319–328.
[Ko80]
N. Koblitz, p-adic analysis: a short course on recent works, London L.N.M.,
vol. 42, Cambridge Univ. Press, 1980.
[Kot85]
R.E. Kottwitz, Isocrystals with additional structure, Compositio Math. 56
(1985), 201–220.
[Kot92]
R.E. Kottwitz, Points on some Shimura varieties over ﬁnite ﬁelds, J. Amer.
Math. Soc. 5 (1992), 373–444.
[Kra96]
D. Krammer, An example of an arithmetic Fuchsian group, J. reine angew.
Math. 473 (1996), 69–85.
[Kur79]
A. Kurihara, On some examples of equations deﬁning Shimura curves and
the Mumford uniformization, J. Fac. Sci. Univ. Tokyo Sect. IA Math. (1979),
277–300.
[Kur80]
A. Kurihara, Construction of p-adic unit balls and the Hirzebruch proportion-
ality, Amer. J. Math. 24 (1980), 129–174.
[Laf79]
G. Laﬀaille, Construction de groupes p-divisibles:
le cas de dimension 1,
Ast´erisque 65 (1979), 103–124.
[La90]
S. Lang, Cyclotomic Fields I and II, Graduate Text in Math., Springer-Verlag,
1990.
[LiO98]
K. Li and F. Oort, Moduli of supersingular abelian varieties, Lecture Notes
in Math., vol. 1680, Springer, 1998.
[L¨ut90]
W. L¨utkebohmert, Formal-algebraic and rigid-analytic geometry, Math. Ann.
286 (1990), 341–371.
[L¨ut93]
W. L¨utkebohmert, Riemann’s existence problem for a p-adic ﬁeld, Invent.
Math. 111 (1993), 309–330.
[Mag74]
W. Magnus, Non-euclidian tesselations and their groups, vol. 61, Acad. Press,
1974.
[May91]
D. Mayer, Continued fractions and related transformations, Ergodic theory,
symbolic dynamics, and hyperbolic spaces (Ser. C., ed.), Oxford University
Press, 1991, 175–222.
[Mer54]
S.N. Mergelyan, Uniform approximations to functions of a complex variable,
Trans. Amer. Math. Soc. 101 (1954), 31–122.
[Mes72]
W. Messing, The crystals attached to Barsotti-Tate groups, Lecture Notes in
Math., vol. 264, Springer, 1972.
[Mes76]
W. Messing, qSerre−Tate = qDwork, Notices Amer. Math. Soc., 1976.
[MFK94]
D. Mumford, J. Fogarty, and F. Kirwan, Geometric Invariant Theory, third
enlarged editin ed., Ergebnisse der Math., vol. 34, Springer-Verlag, 1994.
[Mic81]
J.F. Michon, Courbes de Shimura hyperelliptiques, Bull. Soc. Math. France
109 (1981), 217–225.
[Mic84]
J.F. Michon, Courbes de Shimura, S´eminaire de Th´eorie des Nombres Paris
1982–1983, Progress in Mathematics, vol. 51, Birkh¨auser, 1984.
[MM74]
B. Mazur and W. Messing, Universal extensions and one-dimensional crys-
talline cohomology, Lecture Notes in Math., vol. 370, Springer, 1974.
[Moc96]
S. Mochizuki, A theory of ordinary p-adic curves, Publ. R.I.M.S. Kyoto 32
(1996), 957–1151.
244
BIBLIOGRAPHY
[MoRo69]
E. Motzkin and P. Robba, Prolongement analytique en analyse p-adique,
S´eminaire de Th´eorie des Nombre, Bordeaux, 1968–1969, multigraphed.
[Mu72a]
D. Mumford, An analytic construction of degenerating abelian varieties over
complete rings, Compositio Math. 24 (1972), 239–272.
[Mu72b]
D. Mumford, An analytic construction of degenerating curves over complete
local rings, Compositio Math. 24 (1972), 129–174.
[Mu79]
D. Mumford, An algebraic surface with K ample, (K2) = 9, pg = q = 0,
Amer. J. of Math. 101 (1979), 233–244.
[Mus78]
G.A. Mustaﬁn, Nonarchimedean uniformization, Math. USSR-Sb. 34 (1978),
187–214.
[Oes84]
J. Oesterl´e, Nombres de Tamagawa et groupes unipotents en caract´eristique,
Invent. Math. 78 (1984), 13–88.
[Ogg83]
A. Ogg, Real points on Shimura curves, papers dedicated to Shafarevich,
Progress in Math, vol. 35, Birkh¨auser, 1983.
[O90]
A. Ogus, A p-adic analogue of the Chowla-Selberg formula, in: p-adic analysis,
Proc. Trento conf. on p-adic analysis (F Baldassarri, S. Bosch, and B. Dwork,
eds.), Lecture Notes in Math, vol. 1454, Springer, 1990, 319–341.
[O00]
A. Ogus, Elliptic crystals and modular motives, preprint (2000).
[P00]
G. Pappas, On the arithmetic moduli schemes of PEL Shimura varieties, J.
of Alg. Geom. 9 (2000), no. 3, 577-605.
[Ram98]
L. Ramero, On a class of ´etale analytic sheaves, J. Algebraic Geom. 7 (1998),
no. 3, 405–504.
[Rap92]
A. Rapinchuk, Congruence subgroup problem for algebraic groups: Old and
new, S.M.F. Ast´erisque 209 (1992), 73–84.
[Ray74]
M. Raynaud, G´eom´etrie analytique rigide d’apr`es Tate, Kiehl,.. table ronde
d’analyse non-archimedienne, Bull. Soc. math. France M´em. 39–40 (1974),
319–327.
[Ray94]
Raynaud, Revˆetements de la droite aﬃne en caract´eristique p > 0 et conjec-
ture d’Abhyankar, Invent. Math. 116 (1994), 425–462.
[Re89]
E. Reyssat, Quelques aspects des surfaces de Riemann, Progress in Math.,
vol. 77, Birkh¨auser, 1989.
[Ro75]
P. Robba, Solutions born´ees des syst`emes diﬀ´erentiels lin´eaires. Application
aux fonctions hyperg´eom´etriques, Groupe d’´etude d’analyse ultram´etrique,
exp. 5, 1975.
[Ro86]
P. Robba, Une introduction na¨ıve aux cohomologies de Dwork, M´em. Soc.
Math. France (N.S.) 23 (1986), 61–105.
[RR84]
S. Ramanan and A. Ramanathan, Some remarks on the instability ﬂag,
Tˆohoku Math. J. 36 (1984), 269–291.
[RR96]
M. Rapoport and M. Richartz, On the classiﬁcation and specialization of F-
isocrystals with additional structure, Compositio Math. 103 (1996), 153–181.
[RZ96]
M. Rapoport and Th. Zink, Period space for p-divisible groups, Ann. of Math.
Study, vol. 141, Princeton University press, 1996.
[Sai94]
K.
Saito,
Algebraic
representation
of
the
Teichm¨uller
spaces,
The
Grothendieck Theory of Dessins d’Enfants (L. Schneps, ed.), vol. 200, London
Math. Soc., 1994.
[Schn37]
T. Schneider, Arithmetische Untersuchungen elliptischer Integrale, Math.
Ann. 113 (1937), 1–13.
[Scho85]
A.J. Scholl, A trace formula for F-crystals, Invent. Math. 79 (1985), 31–48.
[Sch99]
H. Schoutens, Embedded resolution of singularities in rigid analytic geometry,
Ann. Fac. Sci. Toulouse, VI. Ser. 8 (1999), no. 2, 297–330.
[Ser67]
J.-P. Serre, Complex multiplication, Algebraic Number Theory (J. Cassels and
A. Fr¨ohlich, eds.), Academic Press, 1967.
[Ser68a]
J.-P. Serre, Abelian l-adic representations and elliptic curves, Benjamin, 1968.
BIBLIOGRAPHY
245
[Ser68b]
J.-P. Serre, Corps locaux, Hermann, 1968.
[Ser77]
J.-P. Serre, Arbres, amalgames, sl2, Ast´erisque, vol. 46, S.M.F., 1977.
[Ser94]
J.-P. Serre, Cohomologie galoisienne, 5`eme ed., vol. 5, Springer, 1994.
[Shi67]
G. Shimura, Construction of class ﬁelds and zeta functions of algebraic curves,
Ann. of Math. 85 (1967), 58–159.
[Shi71]
G. Shimura, Introduction to the arithmetic theory of automorphic functions,
Iwanami Shoten–Princeton Univ. Press, 1971, Kanˆo memorial lectures.
[Si90]
C. Simpson, Transcendental aspects of the Riemann-Hilbert correspondence,
Illinois J. Math. 34 (1990), no. 2.
[Si94]
C. Simpson, Moduli of representations of the fundamental group of a smooth
projective variety I, Inst. Hautes ´Etudes Sci. Publ. Math. 79 (1994), 47–129.
[SvdP97]
M. Singer and M. van der Put, Galois theory of diﬀerence equations, Lecture
Notes in Math., vol. 1666, Springer, 1997.
[SPM91]
J. Stienstra, M. van der Put, and B. van der Marel, On p-adic monodromy,
Math. Z. 208 (1991), 309–325.
[Tak77]
K. Takeuchi, Commensurability classes of arithmetic triangle groups, J. Fac.
Sci. Univ. Tokyo Sect. IA Math. 24 (1977), 201–212.
[Ta66]
J. Tate, p-divisible groups, Proc. of the conference on Local Fields, 1966,
158–183.
[Ta71]
J. Tate, Rigid analytic spaces, Invent Math. 12 (1971), 257–289.
[Ta93]
J. Tate, A review of non-archimedean elliptic functions, Proc. of the con-
ference on Elliptic Curves and Modular Forms (Hong-Kong), International
Press, 1993, 162–184.
[Ter73]
T. Terada, Probl`eme de Riemann et fonctions automorphes provenant des
fonctions hyperg´eom´etriques de plusieurs variables, J. Math. Kyoto Univ. 13
(1973), 557–578.
[Tot96]
B. Totaro, Tensor products in p-adic Hodge theory, Duke Math. J 56 (1996),
79–104.
[Tsu98]
N. Tsuzuki, Finite local monodromy of overconvergent unit-root F-isocrystal
on a curve, Amer. J. of Math. 120 (1998), 1165–1190.
[Uen87]
K. Ueno, Compact rigid analytic spaces — with special regard to surfaces,
Advanced Studies in Pure Math., vol. 10, 1987, Algebraic Geometry, Sendai,
1985, 765–794.
[Var98a]
Y. Varshavsky, p-adic uniformization of unitary Shimura varieties, Inst.
Hautes ´Etudes Sci. Publ. Math. 57 (1998), 57–119.
[Var98b]
Y. Varshavsky, p-adic uniformization of unitary Shimura varieties II, J. Dif-
ferential Geom. 49 (1998), 75–113.
[vdM89]
B. van der Marel, Formal groups and diﬀerential equations, Master’s thesis,
Groningen, 1989.
[vdP82]
M. van der Put, Cohomology on aﬃnoid spaces, Compositio Math. 45 (1982),
165–198.
[vdP83]
M. van der Put, ´Etale coverings of a Mumford curve, Ann. Inst. Fourier 33
(1983), no. 1, 29–52.
[vdP87]
M. van der Put, A note on p-adic uniformization, Indag. Math. 49 (1987),
313–318.
[vdP88]
M. van der Put, Monodromie d’une ´equation diﬀ´erentielle p-adique, Groupe
d’´etude d’analyse ultram´etrique, Publ. Universit´e Paris 7, 1987/88.
[vdP89]
M. van der Put, Les courbes de shimura, J. Th. Nombres Bordeaux, Ser. II 1
(1989), no. 1, 89–102.
[vdP92a]
M. van der Put, Discrete groups, Mumford curves and theta functions, Ann.
Fac. Sci. Toulouse, Ser. Math. 1 VI (1992), no. 3, 399–438.
[vdP92b]
M. van der Put, Uniformization of varieties over local ﬁelds, Nieuw Arch.
Wiskd. IV (1992), no. 1-2, 57–75, Ser. 10.
246
BIBLIOGRAPHY
[vdPV92]
M. van der Put and H. Voskuil, Symmetric spaces associated to split algebraic
groups over a local ﬁeld, J. Reine Angew. Math. 433 (1992), 69–100.
[vdPV00]
M. van der Put and H. Voskuil, Discontinuous subgroups of PGL2(K),
preprint University Groningen, 2000.
[Vig80]
M.F. Vign´eras, Arithm´etique des alg`ebres de quaternions, Lecture Notes in
Math., vol. 800, Springer, 1980.
[Wa69]
W. Waterhouse, Abelian varieties over ﬁnite ﬁelds, Ann. Sci. ´Ecole Norm.
Sup. (4) 2 (1969), 521–560.
[Wol88]
J. Wolfart, Wertehypergeometrischer Funktionen, Invent. Math. 92 (1988),
187–216.
[Yo87]
M. Yoshida, Fuchsian diﬀerential equations, Aspects of Math., vol. 11, Vieweg,
1987.
[Yo97]
M. Yoshida, Hypergeometric functions, my love (modular interpretation of
conﬁguration spaces), Aspects of Math., vol. 32, Vieweg, Publ. Max Planck
Inst., 1997.
[You92]
P.T. Young, Ap´ery numbers, Jacobi sums, and special values of generalized
p-adic hypergeometric functions, J. Number Theory 41 (1992), 231–255.
[Yu95]
J.K. Yu, On the moduli of quasi-canonical liftings, Compositio Math. 96
(1995), no. 3, 293–321.
[EGA I]
A. Grothendieck and J. Dieudonn´e, El´ements de G´eom´etry Alg´ebrique I, Inst.
Hautes ´Etudes Sci. Publ. Math., vol. 4, 1960.
[EGA IV]
A. Grothendieck and J. Dieudonn´e, El´ements de G´eom´etry Alg´ebrique IV,
´Etude locale des sch´emas et des morphismes de sh´emas (quatri`eme partie),
Inst. Hautes ´Etudes Sci. Publ. Math., vol. 32, 1967.
[SGA 1]
A. Grothendieck, Revˆetements ´etales et groupe fondamental (SGA1), Lecture
Notes in Math., vol. 224, Springer, 1971.
Grothendieck’s
        Mysterious Functor
