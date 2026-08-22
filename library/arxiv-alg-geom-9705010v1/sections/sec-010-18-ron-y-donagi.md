---
doc_id: arxiv-alg-geom-9705010v1
doc_title: "Seiberg-Witten Integrable Systems"
section_id: sec-010-18-ron-y-donagi
section_title: "RON Y. DONAGI"
section_number: 18
pages: 18-20
source_pdf: 9705010v1.pdf
source_sha256: 30ab8d0cc2d8f1ae
doc_brief: "Seiberg-Witten Integrable Systems — 17 sections: RON Y. DONAGI; Introduction; References"
---
cf. [ DM2]. The Kahler “metric” in this case is still non-degenerate, but possibly
indeﬁnite.
We note that the wi play a role dual to that of the zi: the zi give the ﬂat
structure on B determined by integration over the α cycles, while the wi give the
ﬂat structure determined by integration over the β cycles. We also note that, up
to this point, the zi as well as the wi have been determined only up to arbitrary
additive constants. In other words, what we have are the vect or ﬁelds ∂/∂z i,∂/∂w i,
or the 1-forms dzi,dw i. We will discuss below the additional choice used in the SW
setup to ﬁx these additive constants.
Similar structures have arisen in various more specialized contexts, e.g. in the
WDVV equations of conformal ﬁeld theory and on moduli spaces of Calabi-Yau
threefolds, as well as in the Seiberg-Witten setup describe d in §1. They often go
under the title of “special geometry”. The point is that thes e specialized contexts
are not really needed: the structure of special geometry on B (consisting of a cov-
ering by open subsets on which an appropriate prepotential, dual ﬂat holomorphic
coordinate systems, and a Kahler metric are deﬁned), arises naturally on the base
of any algebraically integrable system. The converse is als o true, locally, as we have
just seen. Globally, though, there is an integrability cons traint: the monodromy
action (say on the coordinates zi,w i) in an integrable system involves integral sym-
plectic transformations plus (complex) translations, whi le special geometry allows
the symplectic transformation to be real instead of integra l. We refer the reader
to [ F] for a very clear diﬀerential-geometric discussion of spec ial geometry and its
relationship to integrable systems.
Seiberg-Witten Diﬀerentials
In the Seiberg-Witten picture of super Yang-Mills, there ar e the charges ai and
aD
i which are described locally as holomorphic functions on the quantum moduli
space B. There is less ambiguity in choosing these ai,a D
i than in the coordinates
zi,w i on the base of an algebraically integrable system: the group of their linear
combinations Σ niai +nD
i aD
i (with integer coeﬃcients ni) should be uniquely de-
termined in the pure SYM case, and determined modulo the mass es of the added
particles in general. A natural way to get functions with pre cisely such ambiguity
on the base of an integrable system π :X →B is to choose a meromorphic diﬀer-
ential 1-form λ onX and let ai,a D
i be its periods over a set of 1-cycles representing
αi,β i respectively and avoiding the poles of λ. We want ai,a D
i to be a possible
choice of the coordinates zi,w i, which are deﬁned up to translation (once we have
ﬁxed the αi,β i). In other words, we want
dai =dzi, da D
i =dwi.
Since dzi,dw i were deﬁned as the contraction of αi,β i respectively with the sym-
plectic form σ, the condition becomes simply:
dλ =σ.
The behavior of the singularities of λ is constrained by this condition. When
restricted to a general ﬁber Xb,λ will have poles along the union of some irreducible
divisors Db,j. One constraint is that the residue Res j of λ along Db,j is (locally
in B) independent of b. A Seiberg-Witten diﬀerential is a meromorphic 1-form λ
satisfyingdλ =σ and Res j =mj, the mass of the j-th particle. On an algebraically
SEIBERG-WITTEN INTEGRABLE SYSTEMS 19
integrable system with a speciﬁed Seiberg-Witten diﬀerent ial, the local coordinates
zi,w i can be speciﬁed as the charges ai,a D
i , with just the right ambiguity.
One way to describe an integrable system (though by no means t he only way!)
is in terms of a family C → B of spectral curves Cb. In the simplest situation,
the abelian varieties Xb are just the Jacobians J(Cb). More generally, Xb may
be realized as the Prym of Cb with respect to an involution, or as the generalized
Prym with respect to a correspondence, cf. [ D1]. An example of such a system,
due to Mukai [ Mu], is obtained from the Jacobians of a complete linear system
C → B of curves on a symplectic surface ( S, ¯σ). The symplectic form σ on X
then corresponds via Abel-Jacobi to the pullback to C of ¯σ. Mukai studied the case
whereS is a K3 surface. Taking S =T ∗E to be the cotangent bundle of some curve
E yields Hitchin’s system on E. One obtains many more examples by allowing S
to have a symplectic form ¯σ0 deﬁned only on an open subset S0 ⊂S, and imposing
appropriate restrictions on the intersection of the spectr al curves Cb with S −S0.
For example, we can take S to be the total space of the line bundle ωE(D) for
some eﬀective divisor D on E, to recover Markman’s system [ Mn] parametrizing
meromorphic Higgs bundles on E. Note that this S has a natural meromorphic 1-
form ¯λ, given away from D (i.e. where S can be identiﬁed with T ∗E) as the action
1-form ¯λ =pdq, whose diﬀerential is d¯λ = ¯σ0. It follows that the “tautological” 1-
form onC (pullback of ¯λ) induces the Seiberg-Witten diﬀerential λ on the integrable
system X =J(C/B) →B. The system discussed in §3 is of this form.
Linearity: complexiﬁed Duistermaat-Heckman
One feature of the Seiberg-Witten picture which we have not y et discussed is
the linear dependence of the symplectic form on the particle masses. From one point
of view, this linearity follows from existence of the Seiber g-Witten diﬀerential: the
equationσ =dλ implies that the cohomology class of σ is a ﬁxed linear combination
of the residues of λ, which are just the masses. On the other hand, linearity can a lso
be interpreted as arising from a complex analogue of the theo rem of Duistermaat-
Heckman [ DH].
Let (X,σ ) be a complex symplectic manifold (i.e. the symplectic form σ is
holomorphic, of type (2,0)) equipped with a Hamiltonian act ion of a complex re-
ductive group G. The Hamiltonian property of the action means that there is a
moment map µ :X → g∗ to the dual of the Lie algebra. Ignoring bad loci, we will
assume (or pretend) that there is a good non-singular quotie ntX/G. Let Ga ⊂G
be the stabilizer of a ∈ g∗ under the coadjoint action. The symplectic quotient Xa
(or X//aG) is deﬁned as
Xa :=µ−1(a)/Ga =µ−1(Oa)/G,
where Oa is the (coadjoint) orbit of a. It is again a complex symplectic manifold,
with form σa. As a ranges over orbits of a ﬁxed “type” in g∗, the topology of
Xa remains locally constant, so cohomologies of nearby Xa’s of ﬁxed type can
be identiﬁed. The complex Duistermaat-Heckman theorem say s that, under this
identiﬁcation, the cohomology class [ σa] ∈H 2(Xa) varies linearly with a.
Consider ﬁrst the abelian case where G =T is a torus T =Hom(Λ , C∗). The
moment map then factors
X →X/T → t∗,
