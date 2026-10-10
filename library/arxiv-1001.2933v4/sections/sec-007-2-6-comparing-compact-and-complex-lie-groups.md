---
doc_id: arxiv-1001.2933v4
doc_title: "Analytic Continuation Of Chern-Simons Theory"
section_id: sec-007-2-6-comparing-compact-and-complex-lie-groups
section_title: "Comparing Compact And Complex Lie Groups"
section_number: "2.6"
pages: 17-20
source_pdf: 1001.2933v4.pdf.txt
source_sha256: b02636c86d593c02
toc_source: inferred
---
2.6 Comparing Compact And Complex Lie Groups
If we do not require that the generalized integral ZH,C(k) should agree with the original
Chern-Simons integral ZH(k) when k is an integer, we have much more freedom in the
choice of the cycle C. We can take C to be any integer linear combination of Lefschetz
thimbles
C =
X
σ∈Σ
nσJσ, (2.26)
with coefficients nσ that jump in crossing Stokes lines to ensure that the homology cycle C
varies smoothly.
The functions ZH,C(k) of eqn. (2.20), as C runs over the possible choices, form a vector
space V. (This space is actually infinite-dimensional when one allows for the choices of lifts
to C of Chern-Simons invariants of critical points.) What are these functions good for, apart
from analytic continuation of Chern-Simons theory with gauge group H? They play a role
somewhat analogous to conformal blocks in two-dimensional conformal field theory. Let
us compare Chern-Simons theory of the compact group H to Chern-Simons theory of the
complex Lie group G = HC. For reasons that will become clear, we consider first the case of
a three-manifold M without knots.
As we have explained, the analytic continuation of the complex Chern-Simons theory as
a function of its coupling parameters is made using the same machinery as for a compact
Lie group. However, the complexification of a complex Lie group G is isomorphic to the
product G × G, and accordingly, the analytic continuation of Chern-Simons theory of gauge
group G is described by a pair of complex connections A, Ae. This assertion was part of the
derivation of eqn. (2.12), where we also showed that the analytically continued action is the
sum of a Chern-Simons action for A and a Chern-Simons action for Ae. We can thus build
17

an integration cycle for the analytically continued G-valued theory by taking the product
of two integration cycles for the analytically continued H-valued theory. Concretely, we
can consider an integration cycle for the analytically continued G-valued theory of the form
Jσ × Jτ , where Jσ and Jτ are Lefschetz thimbles for the analytically continued H-valued
theory. This gives a basis for the space of appropriate cycles, and hence the partition function
ZG(s, ℓ) of the G-valued theory can be expanded as a bilinear form in the functions ZH,σ(k)
of eqn. (2.23):
ZG(s, ℓ) = X
σ,τ
nσ,τZH,σ(k1)ZH,τ (k2). (2.27)
The coefficients nσ,τ jump in the usual way in crossing Stokes curves.
From the formulas (2.3) and (2.4) for the analytically continued action, one might expect
the coupling parameters to be k1 = t/2 = (ℓ + is)/2, k2 = et/2 = (ℓ − is)/2. Actually there
is a shift by the dual Coxeter number h of H and one has
k1 = t/2 − h, k2 = et/2 − h. (2.28)
This shift enters in comparing the integration measures DA and DA used in defining ZG
and ZH, or, differently put, it reflects the fact that in Chern-Simons theory with a compact
gauge group H, a one-loop correction shifts the effective value of k in many formulas to
k + h, while as shown in [48], there is no such shift for a complex Lie group. For more on
this, see section 2.7.1.
2.6.1 Knots Again
It is instructive to consider what happens to this formalism if we specialize to knots in S
3
,
again in the theory with gauge group G = HC. In the presence of a knot K, we must include
in the integrand of the path integral an extra factor that is the holonomy of the connection
A around K, in some representation R. What happens depends very much on what sort of
representation we pick. For example, one might pick an irreducible unitary representation
of G; these of course are infinite-dimensional. In this case, the simplification that will be
explained momentarily does not arise.
We will consider here a finite-dimensional and irreducible but non-unitary representation
that is related to an irreducible representation of the compact group H. The action of H
on an irreducible representation R can be extended to an action of G = HC in two ways;
in one case the matrix elements of the representations are holomorphic functions on G and
in the other case they are antiholomorphic. We will consider the case of a holomorphic
representation. Given a knot K and a G-valued connection A, holomorphy means after
analytic continuation that the trace of the holonomy around K is a function only of A
18

and not of Ae; as usual we denote this trace as TrRP exp 
−
H
K A

. Now consider the path
integral:
ZG(K;t, et) = Z
C
DA DAe exp itW(A)/2 + ietW(Ae)/2

TrRP exp −
I
K
A

. (2.29)
We want to express this integral in terms of Lefschetz thimbles. So consider the equations
for a critical point. (We will here proceed somewhat informally; the details of how to include
the holonomy factor in the Morse theory framework are explained in section 4.2.) Since
the holonomy factor only depends on A, the equation for Ae is unaffected by the presence
of the knot. This equation says simply that the curvature of Ae vanishes, and as S
3
is
simply-connected, this means that up to a gauge transformation we can take Ae = 0.
Consequently, there is essentially only one possible integration cycle for Ae; it is the
Lefschetz thimble Qe associated to the critical point at Ae = 0. Hence, the integration cycle C
is simply the product of Qe with some integration cycle Q for A. Since the integrand of the
path integral is also a product, it follows that the path integral is the product of an integral
over A and an integral over Ae (rather than a sum of such products, as in the more typical
case (2.27)). Moreover, the integral over Ae does not depend on the knot K. So the general
form of ZG(K;t, et) is
ZG(K;t, et) = Be(et)B(K;t), (2.30)
where only the second factor depends on the knot.
What will be B(K, t)? Rather like the knot invariant ZH(K; k) for the compact group
H, B(K, t) is defined by an integral of the form
Z
Q
DA exp(i(t/2)W(A)) TrRP exp −
I
K
A

(2.31)
for some integration cycle Q ⊂ UbC. What integration cycle shall we use?
In perturbation theory, ZG(K;t, et) is equal to ZH(K; k) (with k = t/2−h, and apart from
a factor Be that depends only on et and not on K). This relation was presented as exercise
6.32 in [49]. As a perturbative statement, it simply reflects the fact that we started with a
holomorphic representation whose holonomy depends on A and not Ae. When we compute
the expectation value of TrR P exp −
H
K A

in perturbation theory, it does not matter if Ae
is absent (the case of a compact gauge group H) or present but decoupled from A (the case
of the complex gauge group G, after analytic continuation to decouple A from A).
This relation between the G and H theories will hold as an exact statement, not just
an asymptotic one, if we simply take Q, the integration cycle used in constructing the
19

theory with complex gauge group G, to be the same integration cycle that was used in
analytically continuing the theory with compact gauge group H. This is a satisfying result,
but it is perhaps best understood as a definition. The original path integral (2.29) is not
convergent, even for the usual real values of the coupling parameters s and ℓ, if regarded
as an integral over the usual real cycle Ae = A. The reason for this is that the holonomy
factor TrRP exp −
H
K A

is exponentially growing in some directions. So the choice of Q
that reduces the knot invariants for G to those of H can be regarded as a definition of the
knot invariants for a holomorphic representation of G, rather than something we deduce
from a more primitive framework. By contrast, in the case of a unitary representation, the
holonomy can be expressed as an oscillatory integral by adding more integration variables;
this is explained in section 4.2. After doing so, the integral over the usual real cycle makes
sense.
