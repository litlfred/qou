---
doc_id: arxiv-alg-geom-9705010v1
doc_title: "Seiberg-Witten Integrable Systems"
section_id: sec-014-meromorphic-higgs-bundles
section_title: "Meromorphic Higgs bundles"
section_number: null
pages: 22-24
source_pdf: 9705010v1.pdf
source_sha256: 30ab8d0cc2d8f1ae
toc_source: inferred
doc_brief: "Seiberg-Witten Integrable Systems — 32 sections: Front matter; Contents; Introduction"
---
Fix a curve E, an eﬀective divisor D on it, and an integer n ≥2. The total space
of the system is the moduli space X of equivalence classes of pairs (V, ϕ), where
V is a rank-n vector bundle on E with trivial determinant, ϕ : V →V ⊗ωE(D)
is a traceless endomorphism with values in ωE(D), and the pairs are subject to an
appropriate semistability condition. The base is
B := ⊕n
i=2H0(E, (ωE(D))⊗i),
and the map π : X →B sends a pair (V, ϕ) to (the sequence of coeﬃcients of) the
characteristic polynomial
det(t · I −ϕ).
(It is best to think of t as a ﬁber coordinate taking values in ωE(D).)
The generic ﬁbers of π are abelian varieties. Consider the surface S which is
the total space of ωE(D). The points b = (b2, . . . , bn) ∈B parametrize a linear
system of curves Cb ⊂S, given by the equation tn + b2tn−2 + · · · + bn = 0. Let
λ be the tautological meromorphic 1-form on S. Then the pair (V, ϕ) determines
a sheaf L := coker (ϕ −λ · Id) on S whose support is the curve Cb. In fact, for
(V, ϕ) generic, L is a line bundle on Cb. Thus we have a map π−1(b) →Pic(Cb).
If we were working with GL(n)-bundles rather than SL(n)-bundles (remove the
restrictions det V ≈O, trace (ϕ) = 0), this would be an isomorphism of π−1(b) with
a component of Pic(Cb). The restrictions mean that we get instead a translate of
Prym(Cb/E).
This construction, modelled on Hitchin’s system [Hi], works much more gen-
erally, cf. [D2]. In particular, the structure group SL(n) can be replaced by any
reductive G. The total space X now parametrizes pairs (V, ϕ) with V a G-bundle
over E, and ϕ a section of ad(V ) ⊗ωE(D). The base is replaced by
B := ⊕r
i=1H0(E, (ωE(D))⊗di),
where r is the rank of G and di are the degrees of the basic invariant polynomials
on the Lie algebra g. Once we choose a representation ρ of G, we get a family of
spectral curves {Cρ,b | b ∈B} in S as before.
As shown in [D2], [Fa] and further references therein, the generic ﬁber of π can
be identiﬁed as (a translate of) a certain distinguished abelian variety Prym(Cb)
which is an isogeny summand in the Jacobian J(Cρ,b) for each representation ρ. The
most natural way to view this is to abandon the spectral curves Cρ,b altogether,
in favor of the cameral cover Cb →E, a Galois cover with group W, the Weyl
group of G. This is the pullback to E, via the classifying map E 99K t/W ≈g/G
determined locally in E by the point b ∈B, of the W-cover t →t/W. (t is the
SEIBERG-WITTEN INTEGRABLE SYSTEMS
23
Cartan subalgebra, and the classifying map is really a map from the total space of
(ωE(D))∗to t/W. The local form above depends on the choice of a local section
of the line bundle (ωE(D))∗, so is really deﬁned only modulo homotheties). Now
J(Cb) decomposes according to the irreducible representations of the Galois group
W, and the distinguished Prym, Prym (Cb), is the component corresponding to
the action of W on the weights. (The question of the dependence of the spectral
Jacobian on ρ was raised in [AM] and studied, in the case of the Toda system, in
[Ml]. A solution, under some conditions, was given in [Ka]. The case E = P1 was
analyzed in [AHH] and [B], and the general case is in [D2], [Me]). In this section
we will use only the SL(n) system, postponing the appearance of other groups to
§4.
The total space X is not symplectic, but has a Poisson structure [B], [Mn]. In
general, a Poisson structure on an algebraic manifold X is a Lie bracket operation
on OX satisfying the properties of the usual Poisson bracket. Equivalently, it can
be given by a section α of ∧2TX satisfying an integrability condition. If α is non-
degenerate on some open set X0, then its inverse σ = α−1 is a two-form on X,
and the integrability condition says that σ is closed, i.e. σ then gives a symplectic
structure. In general, a Poisson manifold admits a natural foliation by submanifolds
(whose conormal bundles consist of the null spaces of α) which inherit a symplectic
structure. A typical example is g∗, which has the natural (Kirillov-Kostant) Poisson
bracket, the symplectic leaves being precisely the coadjoint orbits. More generally,
a Hamiltonian G-action on a symplectic manifold Y induces a Poisson structue on
X = Y/G. This is the ordinary quotient; the symplectic quotients Xa := Y//aG,
for a ∈g∗, are recovered as the symplectic leaves of X. (The Kirillov-Kostant
Poisson structure on g∗is recovered when we take Y := T ∗G).
Markman’s construction of the Poisson structure is based on the moduli space
MD of “bundles with a level-D structure” on E : MD parametrizes equivalence
classes of stable pairs (V, η) where
η : VD
∼
−→On
D
is a trivialization of the ﬁbers of V at points of D (sending the given volume element
of VD to the standard one on On
D, since our structure group is SL(n)). Consider
the cotangent bundle Y := T ∗MD. By elementary deformation theory, its points
are (equivalence classes of) triples (V, η, ϕ) with (V, η) ∈MD and (V, ϕ) ∈X, a
meromorphic Higgs bundle with poles on D. The symmetry group G is the product
of copies of SL(n), one for each point of D. (More precisely, G = {g ∈AutD(On
D) |
det g = 1}, allowing for possibly non-reduced D.)
The G action on MD (with
quotient M = M0, the moduli of stable bundles on E) lifts to a Hamiltonian action
on Y :
g : (V, η, ϕ) 7→(V, g ◦η, ϕ),
with quotient X = Y/G, so we get a Poisson structure on X. The moment map
µ : Y →g∗≈g
sends (V, η, ϕ) to ϕη, the element of EndD(On
D) which is conjugate via η to the
residue ResDϕ ∈EndD(VD). The symplectic leaf Xa, for a ∈g, can therefore be
identiﬁed as the moduli space of pairs (V, ϕ) ∈X such that ResDϕ is conjugate to
the given a. In particular, each abelian variety π−1(b) ≈Prym(Cb/E) is contained
in one symplectic leaf Xa, and is a Lagrangian subvariety there.
24
RON Y. DONAGI
A number of special cases of this construction are well known. When D = 0,
we get Hitchin’s system [Hi] on T ∗M. When E has genus 0, we get the polynomial
matrices system studied in [AHH] and [B]. For more details and examples, see
[Mn] or [DM1].
For the SYM theory with adjoint matter, we take E to be the elliptic curve
whose τ parameter (in the halfplane H) is the coupling constant of the theory. We
are looking for a 1-parameter family of integrable systems (parametrized by mass
m), each having an (n −1)-dimensional base and (n −1)-dimensional ﬁbers. One
checks easily that dim(Xa) equals the dimension of the adjoint orbit of a; so we are
looking for orbits of the smallest possible dimension 2(n −1). There is essentially
only one 1-parameter family of possibilities: D consists of a single point ∞∈E, and
a is the conjugacy class of the diagonal matrix with eigenvalues m(1, 1, . . . , 1, 1−n).
This conjugacy class consists of all diagonalizable SL(n) matrices A with
rank(A −m · Id) ≤1.
(As m →0 there is one further, nilpotent, orbit of the right dimension: the con-
jugacy class of the elementary matrix e12.
But this turns out to give a trivial
