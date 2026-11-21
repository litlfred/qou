---
doc_id: arxiv-alg-geom-9705010v1
doc_title: "Seiberg-Witten Integrable Systems"
section_id: sec-012-linearity-complexiﬁed-duistermaat-heckman
section_title: "Linearity: complexiﬁed Duistermaat-Heckman"
section_number: null
pages: 19-21
source_pdf: 9705010v1.pdf
source_sha256: 30ab8d0cc2d8f1ae
toc_source: inferred
doc_brief: "Seiberg-Witten Integrable Systems — 32 sections: Front matter; Contents; Introduction"
---
One feature of the Seiberg-Witten picture which we have not yet discussed is
the linear dependence of the symplectic form on the particle masses. From one point
of view, this linearity follows from existence of the Seiberg-Witten diﬀerential: the
equation σ = dλ implies that the cohomology class of σ is a ﬁxed linear combination
of the residues of λ, which are just the masses. On the other hand, linearity can also
be interpreted as arising from a complex analogue of the theorem of Duistermaat-
Heckman [DH].
Let (X, σ) be a complex symplectic manifold (i.e. the symplectic form σ is
holomorphic, of type (2,0)) equipped with a Hamiltonian action of a complex re-
ductive group G. The Hamiltonian property of the action means that there is a
moment map µ : X →g∗to the dual of the Lie algebra. Ignoring bad loci, we will
assume (or pretend) that there is a good non-singular quotient X/G. Let Ga ⊂G
be the stabilizer of a ∈g∗under the coadjoint action. The symplectic quotient Xa
(or X//aG) is deﬁned as
Xa := µ−1(a)/Ga = µ−1(Oa)/G,
where Oa is the (coadjoint) orbit of a. It is again a complex symplectic manifold,
with form σa. As a ranges over orbits of a ﬁxed “type” in g∗, the topology of
Xa remains locally constant, so cohomologies of nearby Xa’s of ﬁxed type can
be identiﬁed. The complex Duistermaat-Heckman theorem says that, under this
identiﬁcation, the cohomology class [σa] ∈H2(Xa) varies linearly with a.
Consider ﬁrst the abelian case where G = T is a torus T = Hom(Λ, C∗). The
moment map then factors
X →X/T →t∗,
20
RON Y. DONAGI
and we assume both maps are bundles, at least over some open t∗
0 ⊂t∗.
The
T -bundle X →X/T has ﬁrst chern class
c1 ∈H2(X/T, Λ∗).
For each a in t∗
0, this restricts to a class (still denoted by c1) in H2(Xa, Λ∗). The
theorem in this case says that for a, a0 ∈t∗
0 = Λ ⊗C,
[σa] −[σa0] = ⟨c1, a −a0⟩.
Because of possible monodromy of the ﬁbers of X/T over t∗
0, both sides may be
multivalued, so we should think of the linearity as being local in a.
Next, let G be an arbitrary reductive group, and consider reduction at a regular
semisimple element a. This means that the stabilizer Ga is a maximal torus T ⊂G.
The coadjoint orbits of semisimple elements are parametrized by the quotient t∗/W
of the dual Cartan by the Weyl group. Let g∗
0, t∗
0 denote the open subsets of g∗, t∗
respectively parametrizing regular semisimple elements. The parameter space for
regular semisimple coadjoint orbits is then
t∗
0/W ≈g∗
0/G.
The moment map in this nonabelian situation no longer factors. The closest we get
to factorization is the commutative diagram:
X0
ւ
ցµ
X0/G
g∗
0
ց
ւ
t∗
0/W = g∗
0/G
with X0 := µ−1(g∗
0). Somewhat surprisingly, it is easy to reduce this situation to
the abelian case, by considering Y := µ−1(t∗). The symplectic form of X restricts
to a symplectic form on Y , and the T -action on Y is Hamiltonian with respect
to this form, so there is a moment map µT : Y →t∗compatible with µ via the
inclusions Y ⊂X and t∗⊂g∗. Now for a ∈t∗
0 there is an obvious identiﬁcation
of symplectic manifolds X//aG ≈Y//aT , so the dependence of the symplectic
class [σa] of X//aG on a ∈t∗
0 is again locally linear. (In the original case with G
compact, the multivaluedness is replaced by discontinuities across walls, resulting
in [σa] being linear on each Weyl chamber).
What happens when a is allowed to degenerate? If G is compact, a remains
semisimple (though not regular), and there is a fairly obvious linearity for all such
a in a given open face f0 of the Weyl chamber, i.e.
a face f minus its proper
subfaces.
In the complex reductive case, there are more possibilities: the most
natural orbit which corresponds to an a in a complexiﬁed open face f0 consists of
elements which are not semisimple but regular, in the sense that their centralizers
have the minimal possible dimension. The closure of this orbit consists of a ﬁnite
number of other orbits. The smallest of these orbits (the unique closed orbit, which
is in the closure of each of the others) consists of the semisimple elements. Although
we will not encounter non-regular elements in the integrable systems we need in
the following section, it seems worthwhile to point out that linearity is indeed a
general phenomenon applicable to all strata.
SEIBERG-WITTEN INTEGRABLE SYSTEMS
21
We identify g, t with g∗, t∗via an invariant form. Consider an arbitrary stratum
S ⊂g corresponding to a face f0 ⊂f ⊂t. S is a bundle over (a ﬁnite quotient of the
complexiﬁed) f0, and the ﬁbers are (co)adjoint orbits of a ﬁxed type. This bundle
has local sections, which can be taken of the form n + f0, where n is some ﬁxed
nilpotent in the reductive subalgebra l = lf (= common centralizer of all elements
of f0). All elements a = n + t of this section have the same centralizer c in g. (c
is the centralizer in l of n). Since f is the center of l, it is contained in c, which
actually decomposes as c = f + d with d semisimple. Let D ⊂G be the subgroup
corresponding to d. The reduction to the abelian case now proceeds as follows: We
observe that µ−1(n + f0)/D is symplectic, and has a residual Hamiltonian action
of the subtorus F ⊂T whose algebra is f. Let µF be the moment map to f (which
we identify with f ∗). Then for a = n + t as above, we have an isomorphism of
symplectic manifolds:
X//aG ≈µ−1
F (t)/F = (µ−1(n + f0)/D)//tF.
Since the symplectic form on the right varies linearly with t (which parametrizes
a = n + t), we conclude that [σa] varies linearly with a, as claimed.
In a sense, there is linearity even as we degenerate from one stratum to another.
We illustrate this phenomenon with the following example.
The left action of G on itself lifts to a Hamiltonian action of G on X := T ∗G ≈
G × g∗. The quotient map X →X/G is
G × g∗→g∗
(g, a) 7→a,
while the moment map sends
(g, a) 7→ad∗
ga.
The symplectic quotients
X//aG = Oa
are the coadjoint orbits.
These ﬁt, as discussed above, into a ﬁnite number of
continuous families, each indexed by the W-quotient of some open face.
Inside
each family we expect linearity.
As we move between families, the cohomology
(and even the dimension) jumps. Yet there is a way to express linearity uniformly
for all a ∈g∗. Let Ga, ga be the stabilizers of a in G, g respectively. Then a restricts
to a ∈g∗
a which is Ga-invariant, so it gives an element of (g∗
a)Ga, a bi-invariant 1-
formon Ga. This gives a class in H1(Ga, C), which is then sent to H2(Oa, C) by
the transgression map (= the coboundary map E01
2
→E20
2
in the Leray spectral
sequence of the ﬁbration G →Oa, with ﬁber Ga, where Epq
2 = Hp(Oa, Hq(Ga, C))).
The image is seen to be [σa], and the construction is obviously linear on each
f0 ⊂f ⊂t, since the stabilizers are actually constant there.
