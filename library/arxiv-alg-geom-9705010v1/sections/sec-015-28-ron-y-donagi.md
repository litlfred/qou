---
doc_id: arxiv-alg-geom-9705010v1
doc_title: "Seiberg-Witten Integrable Systems"
section_id: sec-015-28-ron-y-donagi
section_title: "RON Y. DONAGI"
section_number: 28
pages: 28-30
source_pdf: 9705010v1.pdf
source_sha256: 30ab8d0cc2d8f1ae
doc_brief: "Seiberg-Witten Integrable Systems — 17 sections: RON Y. DONAGI; Introduction; References"
---
supersymmetries of N = 4 SYM are broken when the theory is perturbed by the
addition of a mass term to the Lagrangian). The extra symmetr y of the N =
4 theory means that “everything” (i.e. the ingredients of th e special geometry
package encountered in §2: the quantum moduli space, the Kahler metric, the
prepotential...) can be computed explicitly. The outcome m atches perfectly to the
corresponding quantities for Hitchin’s system [ Hi], i.e. the system of holomorphic
(no poles) Higgs bundles on E. (This computation is in §2.3 of [ DW]). So the
physics predicts that our system should specialize, as m → 0, to Hitchin’s for
SU (n), which it of course does. (This is not really an honest “test ”, since we
started out searching for deformations of Hitchin’s system , so this limit was built
in from the beginning).
τ to ∞: the ﬂow to pure N=2
One of the most interesting limits occurs as both m andτ go to inﬁnity simul-
taneously, with τ proportional to log(m). Equivalently, after an obvious rescaling,
we can keep m = 1 and let the elliptic curve degenerate ( τ → ∞ ) while adjusting
the coeﬃcients uℓ in the spectral curves Cu.
The physics of this limit is easy to work out. Essentially, th e mass going to
inﬁnity means that in this limit the particle is so heavy that it cannot be aﬀected
by the rest of the system; we get the pure N=2 theory, with no ma ss. This theory
was solved in [AF] and [KLTY]. The solution does not involve τ , as we saw in the
section on adding matter: instead of τ having a limit (which was there called τcl),
it now goes to ∞. The spectral curves found in [AF] and [KLTY] have the explic it
equation:
C′
b :w2 = (zn +b2zn−2 + · · · +bn)2 + 1
in the (z,w )-plane, where the coeﬃcients bk play a role analogous to our uℓ.
In [DW], we show that these curves are indeed recovered as the appropriate
limits of the spectral curves for the theory with adjoint mas s. This is done by
substituting the τ → ∞ limit into the explicit equations obtained above for the Cu,
and performing the relevant rescalings. Instead of repeati ng the derivation here,
we will describe the geometry of this degeneration.
The pure N=2 curve C′
b is the ﬁbre product over P1 (with coordinate v) of the
rational two-sheeted cover w2 =v2 + 1 and the (again rational, with coordinate z)
n-sheeted cover v = zn +b2zn−2 + · · · +bn. In the adjoint theory, the analogue
of the double cover is just the elliptic curve E → P1 (which becomes rational in
the limit τ → ∞ ), and Cu is again an n-sheeted branched cover of E, but it is no
longer the ﬁber product of E with any n-sheeted cover of P1. The degree 2 map
ψ : C → P1
z and the degree n map P1
z → P1
v arise only in the limit: C becomes
hyperelliptic.
The type of corank-1 degeneration involved in going from Cu toC′
b can be seen
more generally. Consider a degree n branched cover π :C →E where E is elliptic
andC has genus n. Up to isogeny, the Jacobian decomposes J(C) ≈P ×E, where
P is the Prym. There are the Abel-Jacobi and Abel-Prym maps:
AJ :C →J(C)
AP :C →P
and their derivatives
φ :C → Pn−1
SEIBERG-WITTEN INTEGRABLE SYSTEMS 29
ψ :C → Pn−2.
Here φ is the canonical map and ψ is the composition of φ with linear projection
from the point 0 ∈ Pn−1 determined by the isogeny.
In the degeneration, we want each of E,C to acquire a node: the singular curves
are E0,C 0, with normalizations E′,C ′, and singular points p0 ∈ E0,q 0 ∈ C0 with
branches pi,q i,i = 1, 2 in the normalizations. The Jacobians J(C),J (E) become
non-compact: J(E0) is a C∗, while J(C0) is a C∗-extension of J(C′); but the Prym
P remains compact. This type of degeneration occurs when π′ :C′ →E′ is totally
ramiﬁed above each of the pi: π′−1(pi) = nqi. In this case we still have the Abel-
Jacobi and Abel-Prym maps, going to the compactiﬁed Jacobia ns. The derivative
φ is still the canonical map of the singular C0; its image has a node at 0 = φ(q0).
On the other hand, ψ is no longer a morphism on C0; its restriction ψ′ :C′ → Pn−2
is now the canonical map of C′.
Within the 2 n − 2-dimensional family of all covers π : C → E we restrict
attention to the n-dimensional family of our spectral curves. Here there exis t points
p ∈E,q ∈C such that AJ(C) at q is tangent to π∗(E) at p. This is equivalent to
saying that AP :C →P (C/E ) is ramiﬁed at q, or that the linear system giving ψ
has a base point at q, or that φ(q) = 0.
Combining these two eﬀects, we ﬁnd that when the corank-1 deg eneration
described above occurs within the family of spectral curves , the two branches
φ(q1),φ (q2) are tangent at 0. Equivalently, the canonical map ψ′ satisﬁes ψ(q1) =
ψ(q2); so C′ is hyperelliptic, ψ is two-to-one, and O(p1 +p2) is the hyperelliptic
bundle. It follows immediately that the two maps, of degrees 2 and n respectively,
fromC′ to P1 ﬁt in a cartesian diagram. The corank-1 degeneration of the s pectral
curves (for the adjoint theory) therefore reproduces exact ly the spectral curves of
the pure N = 2 theory.
Higgs to ∞: symmetry breaking
This time we ﬁx both the curve E and the mass m, and instead we ﬂow to
the theory whose gauge group is some Levi subgroup G ⊂SU (n). Fix a diagonal
matrix ψ, and consider the ﬂow sending a Higgs bundle ( V,ϕ ) in our system to
(V,ϕ s) where ϕs := ϕ +sψ. (As before we decompose V = ⊕Li and let ψ act
diagonally. The ﬂow is well-deﬁned only on the n!-sheeted cover of the system
on which this decomposition exists). The physics predicts t hat the limit of the
SU (n) integrable system as s → ∞ along this ﬂow should be the G-system, where
G ⊂SU (n) is the centralizer of ψ.
For generic ψ, with distinct eigenvalues, this is clear: After rescaling we have
ϕs ∼ϕ′
s :=ψ + 1
sϕ, so the limiting spectral curve is det( t−ψ) = 0, which consists of
n copies of E meeting at ∞. The Prym is then the product J(E)(n−1), independent
of the initial (V,ϕ ). This trivial system corresponds to the Abelian structure group
U (1)n−1 which is the maximal torus of SU (n) and the centralizer of ψ.
In general, ψ will have, say,k distinct eigenvalues with multiplicitiesn1,...,n k,
Σ ni =n. The centralizer is
G =U (1)k−1 × Π k
i=1SU (ni).
Now the limit of the spectral curves of ϕ′
s is non-reduced, consisting of k compo-
nents, the i-th with multiplicity ni. What we need is the limit of the Jacobians.
This clearly has a factor (up to isogeny) from each component , and by rescaling
around the i-th eigenvalueψi ofψ (i.e. setting t −ψi =s−1˜t) we see that this factor
