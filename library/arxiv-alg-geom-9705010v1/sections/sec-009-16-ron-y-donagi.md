---
doc_id: arxiv-alg-geom-9705010v1
doc_title: "Proceedings of Symposia in Pure Mathematics"
section_id: sec-009-16-ron-y-donagi
section_title: "RON Y. DONAGI"
section_number: 16
pages: 16-18
source_pdf: 9705010v1.pdf
source_sha256: 30ab8d0cc2d8f1ae
doc_brief: "Seiberg-Witten Integrable Systems Ron Y. Donagi Contents Introduction §1. Some physics background Electromagnetism Yang-Mills theory Quantization Supersymmetry N = 2 super Yang-Mills — 17 sections: RO"
---
with particles in representations ρi, i = 1,...,N f , is
β =c2(ad) −
∑
i
c2(ρi)
where ad is the adjoint representation. For the classical al gebras we can adjust the
scaling of the Killing form so that c2(F ) = 1 where F is the fundamental repre-
sentation. With this normalization, c2(ad) = 2 h∨
g, where h∨
g is the dual Coxeter
number. For SU (n) we have h∨
g = n, so the SU(2) theory, for example, remains
asymptotically free with Nf = 0, 1, 2 or 3 particles in the fundamental representa-
tion F , and becomes scale invariant for Nf = 4 fundamental particles or for one
particle in the adjoint representation. These are precisel y the cases studied and
solved in [ SW2].
It is natural to ask whether the four dimensional, N =2 SYM theory with ar-
bitrary gauge groups G and collection of particles ρi with β ≤ 0 can be similarly
solved in geometric terms via families of abelian varieties and meromorphic one-
forms. This question will occupy us in the remainder of this w ork.
§2. Why integrable systems
Algebraically integrable systems
An algebraically integrable system consists of a complex al gebraic manifold
X, an everywhere non-degenerate, closed holomorphic (2 , 0)-form σ on X, and
a morphism π : X → B whose general ﬁber is a (polarized) abelian subvariety
Xb :=π−1(b) which is Lagrangian with respect to σ. In practice, the object which
is naturally given is often an aﬃne open X0 ⊂ X, the ﬁbers being aﬃne sub-
sets of abelian varieties. This is a straightforward algebr aic analogue of the (real,
C∞) notion of integrable system in classical mechanics. As the re, any function H
(“Hamiltonian”) on the base B determines a 1-form dπ∗H on X, and when con-
tracted with the symplectic form σ it gives a vector ﬁeld vH on X, tangent to the
ﬁbers of π. The pullbacks π∗H1,π ∗H2 of two functions on B Poisson-commute,
and in particular the corresponding vector ﬁelds commute.
Locally on the base of an algebraically integrable system th ere is a natural
holomorphic ﬂat structure, depending on a discrete choice. The ﬁber homology
H1(Xb, Z) has a non-degenerate skew-symmetric pairing (induced by t he polariza-
tion). The choice involved is that of a Lagrangian subspace V ∗
Z for this pairing.
This is often achieved by specifying a symplectic basis α1,...,α g,β 1,...,β g of
H1(Xb, Z), and taking the subspace V ∗
Z spanned by the α cycles. This choice needs
to be made for one b ∈ B, and (by Gauss-Manin) is propagated to nearby ﬁbers.
Integration over these α-cycles gives a local trivialization of the relative cotang ent
bundle π∗ωX , and the symplectic form σ converts this to a ﬂat structure on (the
tangent bundle of) B, modelled on V :=Hom(V ∗
Z, C).
Locally on the ﬂat base B, we can ask what kind of data is required to specify
an algebraically integrable system inducing the given ﬂat s tructure. We think of
the family of Abelian varieties, plus choice of α and β cycles, as speciﬁed by its
period map
p :B → Hg
to the Siegel half space Hg of g ×g symmetric complex matrices with positive
imaginary part. The total space π : X → B is then retrieved as pullback of
the universal abelian variety Xg → Hg. The question then is to understand the
SEIBERG-WITTEN INTEGRABLE SYSTEMS 17
condition on p for there to be a symplectic form on X for which π is a Lagrangian
ﬁbration. The ﬁxing of the ﬂat structure is achieved by think ing of Hg as open
subset of Sym 2V ∗, where V is the tangent space to B (at any b ∈ B). The
derivative of the period map is
dpb ∈Hom(V,Sym 2V ∗) = V ∗ ⊗Sym 2V ∗.
A straightforward computation done in [ DM2] shows that the condition is that dpb
lives in the subspace Sym 3V ∗, for all b ∈B. So an integrable system with base B
is speciﬁed by a ﬁeld of cubics on the tangent bundle of B.
This ﬁeld of cubics is subject, of course, to a strong integra bility condition. In
ﬂat local coordinates zi on B, let ( pij(z)) be the period matrix and ( cijk (z)) the
ﬁeld of cubics. Then equality of mixed partials
∂pij
∂zk
=cijk = ∂pik
∂zj
implies the existence of functions wi (locally) on B such that
pij = ∂wi
∂zj
.
These again have symmetric partials,
∂wi
∂zj
=pij = ∂wj
∂zi
,
so there is a single function F on B, called the prepotential, satisfying:
wi = ∂F
∂zi
pij = ∂2F
∂zi∂zj
cijk = ∂3F
∂zi∂zj∂zk
The prepotential determines also a Kahler potential on B
K :=Im(
∑
i
wi ¯zi) = Im(
∑
i
∂F
∂zi
¯zi)
and its associated Kahler form
i
2∂∂K = i
2
∑
i,j
Im(pij)dzi ∧d¯zj.
Equivalently, this Kahler (1,1)-form on B is obtained by integration over the g-
dimensional ﬁbers Xb of the (g + 1,g + 1)-form σ ∧ ¯σ ∧tg−1 on X, where t is any
(1, 1)-form on X whose restrictions to ﬁbers give the polarization.
Conversely, given B with coordinates zi and a holomorphic function F, the
above formulas produce an algebraically integrable system over the open subset of
B whereIm( ∂2F
∂zi∂zj
)> 0 : the family of abelian varieties is determined by its perio ds
pij, and the symplectic form is given by the cubic cijk . The slightly weaker notion
of an analytically integrable system (just replace abelian varieties by polarized
complex tori) is recovered over the open subset where Im( ∂2F
∂zi∂zj
) is invertible,
