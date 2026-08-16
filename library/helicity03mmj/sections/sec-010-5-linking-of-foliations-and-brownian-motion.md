---
doc_id: helicity03mmj
doc_title: "MOSCOW MA THEMA TICAL JOURNAL"
section_id: sec-010-5-linking-of-foliations-and-brownian-motion
section_title: "Linking of Foliations and Brownian Motion"
section_number: 5
pages: 15-22
source_pdf: helicity03mmj.pdf
source_sha256: e364dad3afff3180
doc_brief: "MOSCOW MATHEMATICAL JOURNAL — We revisit an interpretation of higher-dimensional helicities and Hopf–Novikov invariants from the point of view of the Brownian ergodic theorem."
---
An attempt to generalize the ergodic view on helicity to higher dimensions en-
counters the following diﬃculty. Consider, for instance, the Hopf invariant for a
map ρ : S2k−1 → Sk. Just like in the S3 → S2-case, it is deﬁned as the linking
number of the preimages in S2k−1 of two generic points in the target sphere Sk.
Alternatively, one can deﬁne it as the integral
∫
S2k−1
β ∧ d−1β, (4)
where a k-form β is the pullback to S2k−1 of any volume form on Sk, normalized by
the condition that the total volume of Sk equals 1. The analytic deﬁnition above
(generalized helicity ) extends easily to the case of any exact k-form β on S2k−1, or
to generalized cross-helicity ∫
M
β ∧ d−1γ (5)
for a pair of two exact forms β and γ on an n-dimensional M , where deg β +
deg γ = n + 1. The problem is to give an ergodic interpretation of these integrals
in terms of certain foliations associated to these forms. It is probably more natural
to formulate the problem in the following converse way. Given two foliations F1
and F2 of linking dimensions in M with transverse holonomy invariant measures
β1 and β2, describe the average linking of their ﬁbers in terms of these measures.
The following deﬁnition makes the problem nearly tautological (though it becomes
more interesting when we later ﬁx a volume form on M .)
Deﬁnition 5.1. Let F1 and F2 be two foliations of linking dimensions k and l with
transverse holonomy-invariant measures β1 and β2 in a compact manifold M . The
cross-helicity of these foliations is
H(F1, F2) :=
∫ ∫
Mx×My
LF (x, y ) ∧ (β1(x) ⊗ β2(y)) =
∫ ∫
Cx(F1)×Cy(F2)
LF (x, y ),
where C(Fi) is the Ruelle–Sullivan cycle of the foliation Fi, and LF is a linking
form on M × M .
Remark 5.2. In the case of smooth βi the cross-helicity can be also deﬁned as
follows:
H(F1, F2) :=
∫
M
β1 ∧ d−1β2 =
∫
C(F1)
d−1β2.
1004 B. KHESIN
The equivalence of these deﬁnitions follows from the main property of the linking
form: it deﬁnes an operator ~LF : Ω ∗(M ) → Ω∗(M ), such that for an exact k-form u
the image is one of possible primitives: LF (u) = d−1u modulo an exact ( k−1)-form.
Actually, this very property (or the equivalence of the above deﬁnitions) is a
higher-dimensional (somewhat tautological) analog of the helicity ergodic interpre-
tation in 3D: the linking characteristic of the foliations is expressed in the analytic
form. To give a more precise meaning to the linking of two foliations we will ﬁx
a volume form on M . The latter allows one to identify diﬀerential forms (or, in-
variant measures for the foliations) with polyvector ﬁelds (respectively, generalized
polyvector ﬁelds spanning these foliations).
Remark 5.3. Note that in dimension 3 for linking of two vector ﬁelds, as well as
for linking of one ﬁeld and a foliation in higher dimensions, one has a natural “time”
along the ﬁeld trajectories, which allows one to apply the Birkhoﬀ ergodic theorem,
as well a short path system. In higher dimension, where the interpretation should
be related to linking of possibly non-compact leaves of the foliations, one is lacking
both a natural expanding system of sets, comprising the linking of diﬀerent leaves,
and a natural generalization of short path systems.
A way around these diﬃculties is an application of a Brownian version of the
Birkhoﬀ ergodic theorem, cf. [ 22]. The latter allows one to consider averaging
of a function over leaves of a foliation. This averaging is made with the help of
a leaf Laplace–Beltrami operator, and can be thought of as the large time limit
of averaging over Brownian trajectories along the leaves. First we recall several
notions from foliation theory, see [ 13].
Deﬁnition 5.4. Let (M, F) be a compact foliated Riemannian manifold. Consider
the leaf diﬀusion operators D(t) for the leaf Laplacian ∆ F . Then the Brownian
average of a function f on M is the following function
˜f (x) = lim
n→∞
1
n
n−1∑
t=0
(D(t)f )(x).
Here the leaf diﬀusion operator D(t) is deﬁned as the limit R → ∞ of the
truncated diﬀusion operator:
D(t, R )f (x) =
∫
f (z)p(x, z, t, R ) dz,
where p(x, z, t, R ) equals the heat diﬀusion kernel p(x, z, t ) if the leaf distance
between x and z is not greater than R and it equals zero otherwise. (The diﬀusion
operators D(t, R ) can be thought of as averaging a given heat source after the time
R, while the operator f → ˜f as averaging f over Brownian paths corresponding to
the leaf Laplace–Beltrami operator, Fig. 2.)
Although for foliations with transverse holonomy invariant measure there are
various choices for a convenient measure in the ambient manifold, we will employ
the following general existence result due to L. Garnett.
Theorem 5.5 [13]. 1) Any compact foliated Riemannian manifold (M, F) has a
nontrivial harmonic measure ν, i. e., probability measure such that ⟨∆F f, ν ⟩ = 0
for all f smooth in the leaf direction, where ∆F is the leaf Laplacian ;
GEOMETRY OF HIGHER HELICITIES 1005
R
x z
Figure 2. Brownian trajectories on leaves
2) Let ν be a ﬁnite harmonic measure. Then the ergodic theorem holds, using
the leaf diﬀusion operators D(t) as follows : For any ν-integrable function f there
exists an ν-integrable Brownian average ˜f which is constant along the leaves and
⟨ ˜f , ν ⟩ = ⟨f, ν ⟩.
This theorem allows one to interpret ergodically the above integrals ( 5) by con-
sidering a Brownian motion along the leaves of the foliations and evaluating a
certain linking form along this motion. As we will see, the corresponding number
measuring the mutual linking of the leaves of the two foliations coincides with the
Hopf-type integral.
Deﬁne a Brownian average linking of two foliation leaves as follows. Let
(M, F1, F2) be a compact Riemannian manifold with two foliations of linking di-
mensions k and l. Given a volume-form µ on M , these foliations Fj can be deﬁned
by (generalized) polyvector ﬁelds (which we denote by the same letters), such that
iFj µ = βj.
Deﬁnition 5.6. The Brownian linking of the leaves of foliations F1 and F2 passing
through the two points x, y in M with respect to the measure µ is the Brownian
average ˜f (x, y ) of the function
f (x, y ) := iF (x,y)LF (x, y )
on M × M along the leaf of the foliation F(x, y ) = F1(x) × F2(y) passing through
(x, y ) ∈ M × M .
The Brownian average function ˜f (x, y ) is constant along the leaves of F =
F1 × F2, i. e., on any given pair of leaves of F1 and F2. Note also that the function
f measures the linking of the foliations F1 and F2 just like in the case of linking
of compact submanifolds. (If the measures βi, i = 1 , 2, are supported on closed
non-intersecting surfaces Ni ⊂ M , this is exactly their mutual linking number
lk(N1, N 2) =
∫∫
iN1(x)×N2(y)LF (x, y ), cf. Deﬁnition 3.13.)
Theorem 5.7. Consider a pair of foliations F1 and F2 of linking dimensions k and
l in a compact manifold M . Let ν be a harmonic measure on M ×M for the foliation
F = F1×F2 for any Riemannian metric on M . Then the space average over M ×M
for the Brownian ergodic average ˜f of the function f (x, y ) := iF (x,y)LF (x, y ) with
respect to the measure ν does not depend on the Riemannian metric on M and is
equal to the cross-helicity H(F1, F2) of the foliations.
1006 B. KHESIN
Proof. Fix a Riemannian metric on M and the product metric on M ×M . According
to the Garnett theorem, there is a harmonic measure ν on M × M .
Consider the Brownian average for the function f (x, y ) := iF (x,y)LF (x, y ) along
the leaves of the foliation F = F1 × F2, where the polyvector F is deﬁned with the
help of the harmonic measure ν: iF ν(x, y ) = β1(x) ⊗ β2(y).
The second part of the Garnett theorem immediately gives the required equality:
⟨ ˜f , ν ⟩ =
∫ ∫
M ×M
˜f ν =
∫ ∫
M ×M
f ν =
∫ ∫
M ×M
(iF LF ) ν
=
∫ ∫
M ×M
LF ∧ iF ν =
∫ ∫
M ×M
LF ∧ (β1 ⊗ β2) = H(F1, F2).
The latter expression is also equal to
∫
M β1 ∧ d−1β2 for smooth measures β1 and
β2. Note that the measure ν is smooth in the latter case, since it can be taken to
be the product of the (smooth) transverse holonomy-invariant measure β1 ⊗ β2 and
the Riemannian measure along the leaves of the foliation F. □
Remark 5.8. To give an ergodic interpretation of the higher Hopf invariant ( 4)
one should consider the linking of diﬀerent leaves of the same foliation deﬁned by
the form β. In the latter case one can guarantee that there exists a harmonic form
¯ν on M , such that the harmonic form on M × M is its square: ν = ¯ν ⊗ ¯ν.
For arbitrary transverse holonomy-invariant measures the harmonic measure ν
is not smooth in general, cf. [ 17]. Note that this “Brownian interpretation” does
not involve short path systems.
6. Novikov’s Integrals
Novikov’s invariants [21] can be thought of as a generalization of the Hopf-type
invariants to a wide class of maps. In particular, he constructed an analog of
the Whitehead operations in the homotopy groups for closed diﬀerential forms on
manifolds. In [ 21], Novikov deﬁned a set of invariants on manifolds of an arbitrary
dimension, and we consider the four-dimensional case for illustration.
Consider the invariants designed to distinguish various homotopy classes of the
maps S4 → R3 \ {a, b }. Their geometric realization in diﬀerential forms on S4 is
as follows. Consider a pair of closed 2-forms α and β on S4 satisfying the following
conditions:
α ∧ α = β ∧ β = α ∧ β = 0.
One can easily check
Proposition 6.1. The integrals
J(α; α, β ) =
∫
S4
α ∧ d−1α ∧ d−1β
and
J(β; α, β ) =
∫
S4
β ∧ d−1α ∧ d−1β
do not depend on the choices of d−1α and d−1β.
GEOMETRY OF HIGHER HELICITIES 1007
   
@¡1B
A
U
C
@¡1CB
Figure 3. The linking of three surfaces A, B, and C in a four-sphere
Remark 6.2. Consider the foliations A and B in S4 deﬁned by the kernel subspaces
of the 2-forms α and β. The conditions α ∧ α = β ∧ β = 0 on the pair α, β give the
restrictions on the rank of the forms: rk( α), rk(β) ≤ 2, so that they deﬁne kernel
foliations of dimension 2 in S4. The third condition α ∧ β = 0 ensures that these
kernel foliations have non-transversal intersection. Namely, their leaves at generic
points form a 1-dimensional foliation. Moreover, the distribution spanned by the
sum of the kernels of α and β is integrable and deﬁnes a 3-dimensional foliation
[1]. In [ 16] the integrals above were given an ergodic interpretation in terms of
a generalized (non-generic) linking numbers of the corresponding foliations in the
spirit of Section 4.3 (see also [ 17]).
Here we take a somewhat diﬀerent point of view, inspired by the paper [ 22].
We discuss below the higher linking numbers related to these integrals, while a
Brownian-type ergodic interpretation in terms of linking of the corresponding foli-
ations is achieved by applying the Brownian ergodic theorem [ 13] discussed in the
preceding Section.
More generally, consider the topological meaning of the integral
J(α; β, γ ) =
∫
S4
α ∧ d−1β ∧ d−1γ.
for a triple of exact 2-forms α, β and γ in S4, such that α∧β = α∧γ = 0, providing
that it does not depend on the choices of the potential forms d−1β and d−1γ.
Deﬁnition 6.3. Let A, B , and C be two-dimensional surfaces in S4, such that A
is disjoint with B and C. Then there is the mutual linking number of such a triple:
lk(A; B, C ) := # A ∩ ∂−1B ∩ ∂−1C,
i. e., the intersection number of A with 3-dimensional ﬁlms spanning B and C, see
Fig. 3.
This deﬁnition makes sense for any homological 4-sphere M 4 with H1(M ) =
H2(M ) = 0. In R4 there exists also a Gauss-type formula for this linking number.
Deﬁnition 6.4 [22]. Consider a 6-dimensional manifold Σ 6 := A × B × C ⊂ (R4)3.
Choose points x ∈ A, y ∈ B and z ∈ C and normalize the vectors x − y and x − z
1008 B. KHESIN
in R4. Then we obtain a Gauss type map of 6-dimensional manifolds, from Σ 6 to
S3 × S3 ⊂ R4 × R4, given by the formula:
ρ : ( x, y, z ) ↦→
( x − y
|x − y| , x − z
|x − z|
)
.
Its degree can be explicitly written as the integral:
1
4π4
∫ ∫ ∫
A×B×C
∑
i⁄=k
∑
j⁄=l
xi − yi
|xi − yi|4
xj − zj
|xj − zj|4 dxk ∧ dxl ⊗ dyi ∧ dyk ⊗ dzj ∧ dzl. (6)
The following result was proved jointly with S. Tabachnikov.
Theorem 6.5. (i) The mutual linking number of a triple is well-deﬁned, i. e., it
does not depend on the choices of ∂−1B and ∂−1C.
(ii) In R4 this linking number coincides with the degree of the Gauss map :
lk(A; B, C ) = deg ρ.
Proof. (i) Let A, B and C be the three surfaces in S4 such that A is disjoint with
B and C. If V = ∂−1B and W = ∂−1C are 3-dimensional ﬁlms spanning B and
C, then V ∩ W is a surface U with boundary. This boundary does not intersect A,
since A is disjoint with B and C, and hence # A ∩ U is well deﬁned. When V is
changed to V ′ with the same boundary B, U is replaced by a homologous U ′, and
therefore, the intersection number lk( A; B, C ) = # A ∩ U ′ = #A ∩ U is the same.
(ii) Now suppose that the three initial surfaces are in R4. Fix two unit vectors,
say v and w, and consider the cylinders, say Cv and Cw obtained from B and C
by parallel translating them along v and w, respectively. If one moves B and C
suﬃciently far away in this way, then the mutual linking of A, B, C will be zero.
It changed when Cv ∩ Cw intersected A. Such an intersection means that there are
points x ∈ A, y ∈ B and z ∈ C, such that the vector y − x is collinear with −v and
z − x with −w. In other words, this is the degree of the map ρ, computed as the
number of preimages of the point ( −v, −w) ∈ S3 × S3, cf. [ 22]. □
In order to give the ergodic interpretation of these invariants we need to introduce
the corresponding mutual linking form and describe its properties. Deﬁne a multi-
linking form M LF as a (2 , 2, 2)-form on S4 × S4 × S4 satisfying
∫ ∫ ∫
A×B×C⊂S4×S4×S4
M LF = lk(A; B, C )
for any triple of surfaces A, B, C discussed above. Introduce the operator ~M LF :
Ω∗(S4) × Ω∗(S4) → Ω∗(S4), acting as follows:
β(y) ⊗ γ(z) ↦→
∫ ∫
S4
y×S4
z
M LF(x, y, z ) ∧ (β(y) ⊗ γ(z)).
Remark 6.6. A similar operator ~LF : Ω ∗(M ) → Ω∗(M ) corresponding to a linking
form LF ∈ Ω∗(M × M ) on a manifold M sends
β(y) ↦→
∫
My
LF (x, y ) ∧ β(y).
GEOMETRY OF HIGHER HELICITIES 1009
The key property of this operator is that it sends an exact form to its potential:
~LF (β) = d−1β. (A linking form is not unique, and so is not a potential.) This
property is related to the fact that the diﬀerential of the linking form gives the
δ-form δ(x, y ) supported on the diagonal ∆ ⊂ M × M : LF (x, y ) = d−1
y δ(x, y ), see
details in [ 2].
Proposition 6.7. (i) The operator ~M LF corresponding to a multi-linking form
M LF sends the product of two exact forms into the product of their potentials :
~M LF : β(y) ⊗ γ(z) ↦→ d−1β(x) ∧ d−1γ(x).
In other words, the form M LF(x, y, z ) satisﬁes the property dy dzM LF(x, y, z ) =
δ(x, y )δ(x, z ) ( modulo addition of an exact in x term).
(ii) The multi-linking form M LF(x, y, z ) can be chosen to be L1-integrable on
(S4)3.
Proof. (i) By the Stokes formula
∫ ∫ ∫
A×B×C
M LF =
∫ ∫ ∫
A×∂−1B×∂−1C
dy dzM LF,
while by the deﬁnition of the multilinking,
∫ ∫ ∫
A×B×C
M LF = lk(A; B, C ) =
∫ ∫ ∫
A×∂−1B×∂−1C
δ(x, y )δ(x, z ).
Then for the image ~M LF(β(y) ⊗ γ(z)) we have
∫ ∫
S4
y×S4
z
M LF(x, y, z ) ∧ (β(y) ⊗ γ(z))
=
∫ ∫
S4
y×S4
z
dy dzM LF(x, y, z ) ∧ (d−1
y β(y) ⊗ d−1
z γ(z))
=
∫ ∫
S4
y×S4
z
δ(x, y )δ(x, z ) ∧ (d−1
y β(y) ⊗ d−1
z γ(z)) = d−1β(x) ∧ d−1γ(x).
(ii) The singularities of the mutual linking form are near the diagonals x = y
and x = z. Since it is a “local problem,” we can use the Gauss-type formula for R4.
In the latter case integrability is evident from the explicit expression above. □
The integrability of the linking form allows one to substitute the foliations to this
form and apply the Brownian ergodic theorem to give the ergodic interpretation of
the invariants. Namely, consider the triple of 2-foliations A, B and C related to a
triple of 2-forms α, β and γ of rank 2 on S4, satisfying the conditions α ∧ β = α ∧ γ.
Theorem 6.8. Let ν be a harmonic measure on (S4)3 for the foliation F = A×B×
C for any Riemannian metric. Then the space average over (S4)3 for the Brownian
ergodic average ˜g of the function g := iF M LF with respect to the measure ν does
not depend on the Riemannian metric on (S4)3 and is equal to the Novikov invariant
J(α; β, γ ).
1010 B. KHESIN
The proof mimics the consideration of the preceding section and uses the above
two properties of the form M LF:
⟨˜g, ν ⟩ =
∫ ∫ ∫
(S4)3
(iA×B×C M LF)ν
=
∫ ∫ ∫
S4
x×S4
y×S4
z
M LF(x, y, z ) ∧ (α(x) ⊗ β(y) ⊗ γ(z))
=
∫
S4
x
α(x) ∧ d−1β(x) ∧ d−1γ(x) = J(α; β, γ ).
Remark 6.9. This theorem was inspired in part by the work [ 22], where a similar
statement was proved under an additional restrictive assumption on the proper be-
havior of the foliation leaves at inﬁnity (one assumes that the foliation is amenable).
In the latter case there is a reformulation of such averaging in terms of closures of the
leaves by means of “small caps,” similar to the short path approach for trajectories
in three dimensions. By lifting this assumption, we have to stick to the Brownian
averaging along the leaves of a foliation, without possibility of closing them up,
but now such averaging is applicable to a variety of cases, and in particular, to all
higher-dimensional versions of the invariants discussed above.
