---
doc_id: arxiv-alg-geom-9705010v1
doc_title: "Seiberg-Witten Integrable Systems"
section_id: sec-010-2-why-integrable-systems-algebraically-integrabl
section_title: "§2. Why integrable systems Algebraically integrable systems"
section_number: null
pages: 16-18
source_pdf: 9705010v1.pdf
source_sha256: 30ab8d0cc2d8f1ae
toc_source: inferred
doc_brief: "Seiberg-Witten Integrable Systems — 32 sections: Front matter; Contents; Introduction"
---
Algebraically integrable systems
An algebraically integrable system consists of a complex algebraic manifold
X, an everywhere non-degenerate, closed holomorphic (2, 0)-form σ on X, and
a morphism π : X →B whose general ﬁber is a (polarized) abelian subvariety
Xb := π−1(b) which is Lagrangian with respect to σ. In practice, the object which
is naturally given is often an aﬃne open X0 ⊂X, the ﬁbers being aﬃne sub-
sets of abelian varieties. This is a straightforward algebraic analogue of the (real,
C∞) notion of integrable system in classical mechanics. As there, any function H
(“Hamiltonian”) on the base B determines a 1-form dπ∗H on X, and when con-
tracted with the symplectic form σ it gives a vector ﬁeld vH on X, tangent to the
ﬁbers of π. The pullbacks π∗H1, π∗H2 of two functions on B Poisson-commute,
and in particular the corresponding vector ﬁelds commute.
Locally on the base of an algebraically integrable system there is a natural
holomorphic ﬂat structure, depending on a discrete choice. The ﬁber homology
H1(Xb, Z) has a non-degenerate skew-symmetric pairing (induced by the polariza-
tion). The choice involved is that of a Lagrangian subspace V ∗
Z for this pairing.
This is often achieved by specifying a symplectic basis α1, . . . , αg, β1, . . . , βg of
H1(Xb, Z), and taking the subspace V ∗
Z spanned by the α cycles. This choice needs
to be made for one b ∈B, and (by Gauss-Manin) is propagated to nearby ﬁbers.
Integration over these α-cycles gives a local trivialization of the relative cotangent
bundle π∗ωX, and the symplectic form σ converts this to a ﬂat structure on (the
tangent bundle of) B, modelled on V := Hom(V ∗
Z , C).
Locally on the ﬂat base B, we can ask what kind of data is required to specify
an algebraically integrable system inducing the given ﬂat structure. We think of
the family of Abelian varieties, plus choice of α and β cycles, as speciﬁed by its
period map
p : B →Hg
to the Siegel half space Hg of g × g symmetric complex matrices with positive
imaginary part.
The total space π : X →B is then retrieved as pullback of
the universal abelian variety Xg →Hg. The question then is to understand the
SEIBERG-WITTEN INTEGRABLE SYSTEMS
17
condition on p for there to be a symplectic form on X for which π is a Lagrangian
ﬁbration. The ﬁxing of the ﬂat structure is achieved by thinking of Hg as open
subset of Sym2V ∗, where V is the tangent space to B (at any b ∈B).
The
derivative of the period map is
dpb ∈Hom(V, Sym2V ∗) = V ∗⊗Sym2V ∗.
A straightforward computation done in [DM2] shows that the condition is that dpb
lives in the subspace Sym3V ∗, for all b ∈B. So an integrable system with base B
is speciﬁed by a ﬁeld of cubics on the tangent bundle of B.
This ﬁeld of cubics is subject, of course, to a strong integrability condition. In
ﬂat local coordinates zi on B, let (pij(z)) be the period matrix and (cijk(z)) the
ﬁeld of cubics. Then equality of mixed partials
∂pij
∂zk
= cijk = ∂pik
∂zj
implies the existence of functions wi (locally) on B such that
pij = ∂wi
∂zj
.
These again have symmetric partials,
∂wi
∂zj
= pij = ∂wj
∂zi
,
so there is a single function F on B, called the prepotential, satisfying:
wi = ∂F
∂zi
pij =
∂2F
∂zi∂zj
cijk =
∂3F
∂zi∂zj∂zk
The prepotential determines also a Kahler potential on B
K := Im(
X
i
wi¯zi) = Im(
X
i
∂F
∂zi
¯zi)
and its associated Kahler form
i
2∂∂K = i
2
X
i,j
Im(pij)dzi ∧d¯zj.
Equivalently, this Kahler (1,1)-form on B is obtained by integration over the g-
dimensional ﬁbers Xb of the (g + 1, g + 1)-form σ ∧¯σ ∧tg−1 on X, where t is any
(1, 1)-form on X whose restrictions to ﬁbers give the polarization.
Conversely, given B with coordinates zi and a holomorphic function F, the
above formulas produce an algebraically integrable system over the open subset of
B where Im(
∂2F
∂zi∂zj ) > 0 : the family of abelian varieties is determined by its periods
pij, and the symplectic form is given by the cubic cijk. The slightly weaker notion
of an analytically integrable system (just replace abelian varieties by polarized
complex tori) is recovered over the open subset where Im(
∂2F
∂zi∂zj ) is invertible,
18
RON Y. DONAGI
cf. [DM2]. The Kahler “metric” in this case is still non-degenerate, but possibly
indeﬁnite.
We note that the wi play a role dual to that of the zi: the zi give the ﬂat
structure on B determined by integration over the α cycles, while the wi give the
ﬂat structure determined by integration over the β cycles. We also note that, up
to this point, the zi as well as the wi have been determined only up to arbitrary
additive constants. In other words, what we have are the vector ﬁelds ∂/∂zi, ∂/∂wi,
or the 1-forms dzi, dwi. We will discuss below the additional choice used in the SW
setup to ﬁx these additive constants.
Similar structures have arisen in various more specialized contexts, e.g. in the
WDVV equations of conformal ﬁeld theory and on moduli spaces of Calabi-Yau
threefolds, as well as in the Seiberg-Witten setup described in §1. They often go
under the title of “special geometry”. The point is that these specialized contexts
are not really needed: the structure of special geometry on B (consisting of a cov-
ering by open subsets on which an appropriate prepotential, dual ﬂat holomorphic
coordinate systems, and a Kahler metric are deﬁned), arises naturally on the base
of any algebraically integrable system. The converse is also true, locally, as we have
just seen. Globally, though, there is an integrability constraint: the monodromy
action (say on the coordinates zi, wi) in an integrable system involves integral sym-
plectic transformations plus (complex) translations, while special geometry allows
the symplectic transformation to be real instead of integral. We refer the reader
to [F] for a very clear diﬀerential-geometric discussion of special geometry and its
relationship to integrable systems.
