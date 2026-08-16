---
doc_id: arxiv-2301.02038v1
doc_title: "Contemporary Mathematics Vinogradov’s Cohomological Geometry of Partial Diﬀerential Equations"
section_id: sec-006-22-interpreting-horizontal-cohomologies
section_title: "interpreting horizontal cohomologies"
section_number: 2.2
pages: 12-15
source_pdf: 2301.02038v1.pdf
source_sha256: 27b303939826ab39
doc_brief: "Contemporary Mathematics Vinogradov’s Cohomological Geometry of Partial Differential Equations — Secondary Calculus is a formal replacement for diﬀerential cal- culus on the space of solutions of a"
---
mologies have nice interpretations, sometimes informal, s ometimes more precise. In
this subsection we illustrate some of them. We begin with hor izontal cohomology
with trivial coeﬃcients.
Example 2.1 (Constrained Variational Principles) . Top horizontal cohomolo-
gies with trivial coeﬃcients Hn(E ) can be (informally) interpreted as variational
principles constrained by the PDE E0. To see this, consider a cohomology class
[L]∈Hn(E ). Locally
L = L (x,...,u I,... ) dnx, where dnx :=dx1∧···∧ dxn,
for some local function L ∈ C∞(E ). Now, let N ⊆ P be a compact, oriented
n-dimensional solution of E (without boundary). We can pull-back L along the
embedding j∞ : N → E . If we do so, we get a honest top form on N that we
VINOGRADOV’S COHOMOLOGICAL GEOMETRY OF PDES 13
can integrate using compactness and the orientation. Thus w e have a well deﬁned
functional
F :N↦→F[N ] :=
∫
N
j∞∗L.
IfN is locally given by (1.1) and the coordinates x1,...,x n onN deﬁne the positive
orientation, then F locally looks like
(2.2) F[N ] =
∫
L
(
x,..., ∂|I|f
∂xI ,...
)
dnx.
Actually F does only depend on the cohomology class of L. Additionally, we see
from (2.2) that we can interpret F, and hence [L] as a (coordinate free version of)
a variational principle with Lagrangian density L , imposed on (certain) solutions
of E0.
Example 2.2 (Conservation Laws) . Top minus 1 horizontal cohomologies with
trivial coeﬃcients can be interpreted as conservation laws for the PDE E0. To see
this consider a cohomology class [J]∈Hn−1(E ). Locally
J =Ji(x,...,u I,... ) dn−1xi,
where
dn−1xi := (−)i+1dx1∧···∧ ˆdxi∧···∧ dxn,
for some local functions Ji∈ C∞(E ), i = 1,...,n . The cocycle condition dJ = 0
in local coordinates reads
Di|EJi = 0,
so J can be seen as a conserved current along solutions of E0. Now, let N ⊆ P
be a solution of E and let Σ ⊆ N be a compact, oriented hypersurface (without
boundary) in N . We can pull-back J along j∞ : N→ E . If we do so, we get a
honest (n− 1)-form on N that we can integrate on Σ using compactness and the
orientation. The integral ∫
Σ
j∞∗J
does only depend on (the horizontal cohomology class [J] and on) the homology
class of Σ inN . In this sense, it is conserved along every N . Summarizing, [J] can
be seen as the conservation law associated to the conserved c urrentJ. Notice that
lower degree horizontal cohomologies can be similarly seen as lower degree conserved
charges to be integrated on higher codimensional submanifo lds. For instance the
electric charge is a degree (n− 2) horizontal cohomology class for the Maxwell
equations on a vacuous n-dimensional space-time.
Example 2.3 (Inﬁnitesimal Symmetries) . In this example we discuss degree 0
horizontal cohomologies with coeﬃcients in V . The 0-th cohomology H 0(E, V ) is
just the kernel of the operator
d : Γ( V )→ Ω 1(E, V )
and it consists of parallel sections with respect to the Bott connection. It is easy
to see that a section Y mod Γ( C ) of V , with Y ∈ X(E ), is parallel with respect to
the Bott connection if and only if Y is an inﬁnitesimal symmetry of the E0. We
conclude that the natural inclusion
XE/Γ( C )→ X(E )/Γ( C ) = Γ( V )
14 F ABRIZIO PUGLIESE, GIOV ANNI SPARANO, AND LUCA VITAGLIAN O
establishes a bijection between non-trivial inﬁnitesimal symmetries of E0 and the
0-th cohomolgy H 0(E, V ).
LetY ∈ XC . Remember from Remark 1.2 that the vector ﬁeld Y might not pos-
sess a ﬂow. However, when Y possesses a ﬂow, then the latter maps n-dimensional
integral submanifolds of C to n-dimensional integral submanifolds. So, morally,
it deﬁnes a ﬂow on the space of solutions of E0. If two inﬁnitesimal symmetries
diﬀer by a trivial inﬁnitesimal symmetry then their ﬂows (if they exist) induce the
same ﬂow on the space of solutions, because the ﬂow of a trivia l symmetry ﬁxes ev-
ery n-dimensional integral submanifold. We conclude that nontr ivial inﬁnitesimal
symmetries can be informally seen as vector ﬁelds on the spac e of solutions. This
remark will be relevant in the next subsection.
Example 2.4 (Euler Lagrange Equations) . We now discuss top horizontal co-
homology with coeﬃcients in transverse 1-forms V ∗. We begin noticing that there
is a map
dsec :Hn(E )→Hn(E, V ∗)
deﬁned as follows. Let [L]∈Hn(E ), and choose any n-form ω∈ Ωn(E ) projecting
toL∈ Ω •(E ) under Ω •(E )→ Ω •(E ). The diﬀerential dω belongs to the ideal C Ω •.
Hence, it has the following property: the contraction
iXn··· iX1dω
with any n vector ﬁelds X1,...,X n in C is a transverse diﬀerential 1-form:
iXn··· iX1dω∈ V Ω 1 = C Ω 1.
Hence we have a well-deﬁned, skew-symmetric and C∞(E )-multilinear map
̟ : Γ( C )×···× Γ( C )→ V Ω 1, (X1,...,X n)↦→iXn··· iX1dω
which we can interpret as an element in Ωn(C, V ∗), also denoted ̟. As ddω = 0 ,
we get d̟ = 0 . The cohomology class [̟]∈ Hn(E, V ∗) does only depend on the
cohomology class [L], and we put
dsec[L] = [̟].
We now provide a more concrete description of the map dsec :Hn(E )→Hn(E, V ∗).
For simplicity, from now on, in this example, we will only con sider the case when E0
is the empty PDE 0 = 0 , hence E =J ∞(P,n ). For the sake of brevity, we denote
J ∞ = J ∞(P,n ). When E = J ∞, there is a simple description of Hn(E, V ∗).
Namely, there is a vector space isomorphism
Γ
(
V ∗⊗∧nC ∗) ∼
=
Hn(J ∞, V ∗)
deﬁned as follows. First notice that there is a vector bundle projection
V →V
mapping a transverse vector v mod C at the point z =N ∞
p ∈J ∞ to
dπ(v) modTpN∈TpP/TpN =Vz.
Dually, there is a vector bundle inclusion
V ∗֒→V ∗.
Accordingly, there is an inclusion
(2.3) Γ
(
V ∗⊗∧nC ∗)
֒→
Ωn(J ∞, V ∗).
VINOGRADOV’S COHOMOLOGICAL GEOMETRY OF PDES 15
that can be described in local coordinates as follows. Let v1,...,v m∈ Γ(V ∗) be the
dual basis of the local basis v1,...,v m∈ Γ(V ) described in Subsection 1.2. Then
the inclusion (2.3) maps
vα⊗ dnx↦→dnx⊗ (duα−uα
idxi), α = 1,...,m.
Proposition 2.5. The composition
(2.4) Γ
(
V ∗⊗∧nC ∗)
֒→
Ωn(J ∞, V ∗)−→Hn(J ∞, V ∗)
is a vector space isomorphism. Moreover, for L∈ Ωn(J ∞) locally given by
L = L (x,...,u I,... ) dnx
the section E[L] of V ∗⊗∧nC ∗ corresponding todsec[L] via (2.4) is locally given by
E[L] =
∑
|I|<∞
(−)|I|DI
( ∂L
∂uα
I
)
vα⊗
dnx.
In view of the ﬁrst part of the above proposition, the top coho mologyHn(J ∞, V ∗)
is in bijection with the C∞(J ∞)-module of sections of a vector bundle over J ∞.
Hence it makes sense to speak about the zero locus in J ∞ of a cohomology class
inHn(J ∞, V ∗). From the second part of the proposition, the zero locus of dsec[L],
equivalently the zero locus of E[L], is the Euler-Lagrange equations corresponding
to the variational principle [L] (see Example 2.1):
∑
|I|<∞
(−)|I|DI
( ∂L
∂uα
I
)
= 0.
Similarly, one can show that there is a map
dsec :
Hn(J ∞, V ∗)→Hn(J ∞,∧2V ∗)
(see the next subsection) mapping a system of m PDEs
Eα(x,...,u I,... ) = 0
to the associated Helmoltz conditions for variationality.
