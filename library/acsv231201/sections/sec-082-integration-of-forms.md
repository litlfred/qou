---
doc_id: acsv231201
doc_title: "Analytic Combinatorics in Several Variables Expanded Second Edition"
section_id: sec-082-integration-of-forms
section_title: "Integration of forms"
section_number: null
pages: 470-474
source_pdf: ACSV231201.pdf
source_sha256: 1a664d0bf666041e
toc_source: outline
doc_brief: "Analytic Combinatorics in Several Variables Expanded Second Edition — 100 sections: Front matter; Preface to the second edition; Preface to the first edition"
---
The only thing remaining before deﬁning integration on manifolds is to discuss
domains of integration. For each p ≥1, let ∆p denote the standard p-simplex
A.3 Integration of forms
453
in Rp deﬁned by
∆p =
(x1, . . . , xp) ∈Rp : xi ≥0 for all i and
p
X
i=1
xi ≤1
.
By convention, if p = 0 then ∆p is deﬁned to be a single point. Associated with
the standard simplices are p+2 ways of embedding ∆p as a face of ∆p+1. To be
explicit, for each 1 ≤i ≤p + 1 let κp
i : ∆p →∆p+1 be the embedding obtained
by inserting a zero in the ith position,
κp
i (x1, . . . , xp) = (x1, . . . , xi−1, 0, xi+1, . . . , xp),
and let κp
0 : ∆p →∆p+1 embed into the diagonal face,
κp
0(x1, . . . , xp) =
1 −
p
X
i=1
xi , x1, . . . , xp
.
We now ﬁx an m-manifold M in Rn. For each 0 ≤p ≤m, a smooth p-
simplex (or simply p-simplex) in M is deﬁned to be a map σ : ∆p →M
which extends to a smooth map of a neighborhood of ∆p in Rp into M. Deﬁne
the space Cp(M) of p-chains on M to be the space of ﬁnite formal linear
combinations P ciσi of p-simplices in M with coeﬃcients ci ∈C. A chain
P ciσi is said to be supported on a set X ⊆M whenever all σi in the sum map
into X.
Deﬁnition A.20 (boundary operator). For any 1 ≤p ≤m, the boundary op-
erator on p-chains is the linear map ∂: Cp →Cp−1 which takes a p-simplex
σ : ∆p →M and returns the (p −1)-chain ∂σ : ∆p−1 →M deﬁned by
∂σ :=
p
X
i=0
(−1)i σ ◦κp−1
i
.
(A.3.1)
Figure A.2 illustrates the boundary operator on a singular 2-simplex.
A crucial property of the boundary operator is that it gives the zero map
when applied twice.
Proposition A.21. For any manifold M and 1 ≤p ≤d the map ∂2 = 0.
Exercise A.10. Verify ∂2 = 0 by proving that κp+1
i
◦κp
j = κp+1
j+1 ◦κp
i for all p ≥0
and i ≤j (where κb
a is identically zero if a or b are negative or a > p).
For a domain A ⊆Rn with standard coordinates x1, . . . , xn, we deﬁne the
integral of a top level form ω = f(x)dx1 ∧· · · ∧dxn on A to be the usual
Riemann–Lebesgue integral
Z
A
ω =
Z
A
f(x) dx1 ∧· · · ∧dxn =
Z
A
f(x) dV ,
454
Integration on manifolds
σ
σ(0,0)
σ(0,1)
σ(1,0)
σ    κ1
0
σ    κ1
1
σ    κ1
2
Figure A.2 A 2-simplex and its boundary.
where dV is Lebesgue measure in Rn.
Remark A.22. In order for this deﬁnition of integration to be consistent, we
must write the wedge product in increasing order. For instance, in two dimen-
sions dy ∧dx = −dx ∧dy, so
Z
A
f(x, y)dy ∧dx = −
Z
A
f(x, y)dx ∧dy = −
Z
A
f(x, y)dxdy
even though
Z
A
f(x, y)dxdy =
Z
A
f(x, y)dydx
as Riemann integrals (since f is smooth).
If M is an oriented manifold then for any p-simplex σ : ∆p →M, integra-
tion of a p-form ω over σ is deﬁned by
Z
σ
ω :=
Z
∆p σ∗(ω),
where σ∗is the pullback of ω by σ from a form on M to a form on ∆p ⊂Rp. It
is important to note that we have deﬁned integration not over a set (the range
of σ) but over a parametrization (σ itself). Integration over a chain is deﬁned
by linearity,
Z
Pr
i=1 aiσi
ω :=
rX
i=1
ai
Z
σi
ω .
Example A.23. If M = Rd then we can write any d-simplex σ = (σ1, . . . , σd),
where each σi is a smooth map from ∆d to R. Example A.19 implies that for
any d-form ω = a(x)dx1 ∧· · · ∧dxd,
Z
σ
ω =
Z
∆p σ∗(ω) =
Z
∆p a(σ(x))(det J)dx1 · · · dxd ,
A.3 Integration of forms
455
where J is the Jacobian matrix of σ : Rd →Rd and the ﬁnal integral is the
Riemann integral of a smooth function on Rd. This mirrors the usual change of
variables formula seen in a ﬁrst calculus course.
◁
We often want to integrate over manifolds, but our formal deﬁnition of inte-
gration holds over chains. Integration over a manifold can be deﬁned by divid-
ing the manifold into a ﬁnite collection of chains, provided (i) how we divide
up the manifold does not aﬀect the result, and (ii) we can orient the chains in
a consistent way so that the integral is uniquely determined up to a sign de-
pending on a global orientation. Recall from above that a manifold M is called
oriented if for any charts (U, φ) and (V, ψ) on M with nonempty intersection
W = U ∩V the smooth function φ ◦ψ−1 from ψ(W) ⊂Rm to φ(W) ⊂Rm has
positive Jacobian determinant. We do not attempt to deﬁne integration over
non-orientable manifolds.
Assume that the p-manifold M is orientable and ﬁx one of its two orienta-
tions. We say that a p-simplex σ : ∆p →M is a positively oriented simplex
with respect to this orientation of M if for any oriented chart (U, φ) of M the
diﬀerential σ∗: TpRm →Tσ(p)M with respect to the bases ∂/∂xk and ∂/∂φk
of TpRm and Tσ(p)M has positive determinant. If M is also compact then a
triangulation of M is a ﬁnite set σ1, . . . , σr of positively oriented p-simplices
satisfying certain conditions set out at greater length in the deﬁnition of a sim-
plicial complex in Section B.1 of Appendix B. These conditions imply that the
simplices divide M into regions, meaning that each map is one-to-one on the
interior of ∆m, the images of the interiors are disjoint, and the union of the
images is all of M. Triangulation represents M as a p-chain Pr
j=1 σ j, so the
integral of a p-form ω over M is deﬁned by linearity,
Z
M
ω :=
rX
j=1
Z
σj
ω .
(A.3.2)
The integral does not depend on which oriented triangulation we chose [War83,
Section 4.8], so (A.3.2) deﬁnes the integral of a p-form over an orientable p-
manifold (up to a sign that depends on the orientation chosen).
Exercise A.11. Give an explicit oriented triangulation of S 2 and use it to inte-
grate f(x, y) = xy2 on S 2.
Above we deﬁned the diﬀerential map, which takes a smooth function on
a manifold M – in other words, a 0-form f ∈E0(M) – and returns a 1-form
d f ∈E1(M). We now extend this map to the diﬀerential operator (or exterior
456
Integration on manifolds
derivative operator) d : E∗(M) →E∗(M) deﬁned locally in a chart (U, φ) by
d( f dφI) :=
X
1≤j≤m
∂f
∂φ j
dφj ∧dφI .
The diﬀerential maps a p-form to a (p + 1)-form, applying d twice gives the
zero map (this is usually written d2 = 0), and if ω ∈Ep(M) and η ∈Eq(M)
then
d(ω ∧η) = d(ω) ∧η + (−1)pω ∧d(η) .
(A.3.3)
The diﬀerential still commutes with pullbacks, meaning d(ψ∗(ω)) = ψ∗(dω)
for any smooth map ψ.
Exercise A.12. Prove that (A.3.3) holds.
We introduce the diﬀerential to state Stokes’s Theorem, our last result on the
integration of forms.
Theorem A.24 (Stokes’s Theorem). Let p ≥1 and suppose that ω is a (p−1)-
form on a manifold M of dimension at least p. If C is a p-chain on M then
Z
∂C
ω =
Z
C
dω .
Stokes’s Theorem follows from our deﬁnitions, integration by parts, and
some elementary computations; see [War83, Theorem 4.7] for details.
