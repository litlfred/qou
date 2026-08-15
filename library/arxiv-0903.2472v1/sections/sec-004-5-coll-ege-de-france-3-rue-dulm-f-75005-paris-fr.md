---
doc_id: arxiv-0903.2472v1
doc_title: "Exact Results for Perturbative Chern-Simons Theory with Complex Gauge Group"
section_id: sec-004-5-coll-ege-de-france-3-rue-dulm-f-75005-paris-fr
section_title: "Coll` ege de France, 3 rue d’Ulm, F-75005 Paris, France"
section_number: 5
pages: 1-10
source_pdf: 0903.2472v1.pdf
source_sha256: 637cfd1d4d833c02
doc_brief: "Exact Results for Perturbative Chern-Simons Theory with Complex Gauge Group — We develop several methods that allow us to compute all-loop partition functions in perturbative Chern-Simons theory with"
---
Abstract: We develop several methods that allow us to compute all-loop partition
functions in perturbative Chern-Simons theory with comple x gauge group GC, sometimes
in multiple ways. In the background of a non-abelian irreduc ible ﬂat connection, per-
turbative GC invariants turn out to be interesting topological invarian ts, which are very
diﬀerent from ﬁnite type (Vassiliev) invariants obtained in a theory with compact gauge
group G. We explore various aspects of these invariants and present an example where
we compute them explicitly to high loop order. We also introd uce a notion of “arithmetic
TQFT” and conjecture (with supporting numerical evidence) thatSL(2, C) Chern-Simons
theory is an example of such a theory.
CALT-68-2716
Contents
1. Introduction and summary 1
2. Perturbation theory around a non-trivial ﬂat connection 9
2.1 Feynman diagrams and arithmetic TQFT 9
2.2 Quantization of Mﬂat (GC, Σ) 14
2.2.1 Analytic continuation 17
2.2.2 A hierarchy of diﬀerential equations 19
2.3 Classical and quantum symmetries 22
2.4 Brane quantization 24
3. A state integral model for perturbative SL(2, C) Chern-Simons theory 26
3.1 Ideal triangulations of hyperbolic 3-manifolds 26
3.2 Hikami’s invariant 31
3.3 Quantum dilogarithm 33
3.4 A state integral model for Z (ρ)(M ; ℏ) 38
4. Examples and computations 42
4.1 Numerical veriﬁcation of the arithmeticity conjecture 43
4.2 Perturbative SL(2, C) invariants for the ﬁgure-8 knot complement 47
4.2.1 Quantization 50
4.2.2 State integral model 54
1. Introduction and summary
Three-dimensional Chern-Simons gauge theory is a prominen t example of a topological
quantum ﬁeld theory (TQFT). By now, Chern-Simons theory wit h a compact gauge group
G is a mature subject with a history going back to the 1980’s (se e e.g. [16, 33] for excellent
reviews) and with a wide range of applications, ranging from invariants of knots and 3-
manifolds [52] on one hand, to condensed matter physics [25, 39] and string theory [35] on
the other.
In this paper, we will be interested in a version of Chern-Sim ons gauge theory with
complex gauge group GC. Although at ﬁrst it may appear merely as a variation on the
subject, the physics of this theory is qualitatively diﬀeren t from that of Chern-Simons
gauge theory with compact gauge group. For example, one impo rtant diﬀerence is that to
a compact Riemann surface Σ Chern-Simons theory with compac t gauge group associates
a ﬁnite-dimensional Hilbert space HΣ , whereas in a theory with non-compact (and, in
particular, complex) gauge group the Hilbert space is inﬁni te-dimensional. Due to this and
– 1 –
other important diﬀerences that will be explained in further detail below, Chern-Simons
gauge theory with complex gauge group remains a rather myste rious subject. First steps
toward understanding this theory were made in [53] and, more recently, in [22].
As in a theory with a compact gauge group, the classical actio n of Chern-Simons gauge
theory with complex gauge group GC is purely topological — that is, independent of the
metric on the underlying 3-manifold M . However, since in the latter case the gauge ﬁeld A
(a gC-valued 1-form on M ) is complex, in the action one can write two topological term s,
involvingA and ¯A:
S = t
8π
∫
M
Tr
(
A∧ dA + 2
3A∧A∧A
)
(1.1)
+
¯t
8π
∫
M
Tr
(
¯A∧ d ¯A + 2
3
¯A∧ ¯A∧ ¯A
)
.
Although in general the complex coeﬃcients (“coupling cons tants”) t and ¯t need not be
complex conjugate to each other, they are not entirely arbit rary. Thus, if we write t =k +σ
and ¯t =k−σ, then consistency of the quantum theory requires the “level ”k to be an integer,
k∈ Z, whereas unitarity requires σ to be either real, σ∈ R, or purely imaginary, σ∈iR;
see e.g. [53].
Given a 3-manifold M (possibly with boundary), Chern-Simons theory associates to
M a “quantum GC invariant” that we denote as Z(M ). Physically, Z(M ) is the partition
function of the Chern-Simons gauge theory on M , deﬁned as a Feynman path integral
Z(M ) =
∫
eiSDA (1.2)
with the classical action (1.1). Since the action (1.1) is in dependent of the choice of metric
on M , one might expect that the quantum GC invariantZ(M ) is a topological invariant
of M . This is essentially correct even though independence of me tric is less obvious in the
quantum theory, and Z(M ) turns out to be an interesting invariant. How then does one
compute Z(M )?
One approach is to use topological invariance of the theory. In Chern-Simons theory
with compact gauge group G, the partition function Z(M ) can be eﬃciently computed by
cuttingM into simple “pieces,” on which the path integral (1.2) is eas y to evaluate. Then,
via “gluing rules,” the answers for individual pieces are as sembled together to produce
Z(M ). In practice, there may exist many diﬀerent ways to decompos eM into basic building
blocks, resulting in diﬀerent ways of computing Z(M ).
Although a similar set of gluing rules should exist in a theor y with complex gauge
groupGC, they are expected to be more involved than in the compact cas e. The underlying
reason for this was already mentioned: in Chern-Simons theo ry with complex gauge group
the Hilbert space is inﬁnite dimensional (as opposed to a ﬁni te-dimensional Hilbert space
in the case of compact gauge group G). One consequence of this fact is that ﬁnite sums
which appear in gluing rules for Chern-Simons theory with co mpact group G turn into
integrals over continuous parameters in a theory with non-c ompact gauge group. This is
one of the diﬃculties one needs to face in computing Z(M ) non-perturbatively, i.e. as a
closed-form function of complex parameters t and ¯t.
– 2 –
A somewhat more modest goal is to compute Z(M ) perturbatively, by expanding the
integral (1.2) in inverse powers of t and ¯t around a saddle point (a classical solution). In
Chern-Simons theory, classical solutions are ﬂat gauge con nections, that is gauge connec-
tionsA which obey
dA +A∧A = 0 , (1.3)
and similarly for ¯A. A ﬂat connection on M is determined by its holonomies, that is by a
homomorphism
ρ :π1(M )→GC. (1.4)
Of course, this homomorphism is only deﬁned modulo gauge tra nsformations, which act
via conjugation by elements in GC.
Given a gauge equivalence class of the ﬂat connection A, or, equivalently, a conjugacy
class of the homomorphism ρ, one can deﬁne a “perturbative partition function” Z (ρ)(M )
by expanding the integral (1.2) in inverse powers of t and ¯t. Since the classical action (1.1)
is a sum of two terms, the perturbation theory for the ﬁelds A and ¯A is independent. As a
result, to all orders in perturbation theory, the partition function Z (ρ)(M ) factorizes into
a product of “holomorphic” and “antiholomorphic” terms:
Z (ρ)(M ) = Z (ρ)(M ;t)Z (ρ)(M ; ¯t). (1.5)
This holomorphic factorization is only a property of the per turbative partition function.
The exact, non-perturbative partition function Z(M ) depends in a non-trivial way on both
t and ¯t, and the best one can hope for is that it can be written in the fo rm
Z(M ) =
∑
ρ
Z (ρ)(M ;t)Z (ρ)(M ; ¯t), (1.6)
where the sum is over classical solutions (1.3) or, equivale ntly, conjugacy classes of homo-
morphisms (1.4).
In the present paper, we study the perturbative partition fu nctionZ (ρ)(M ). Due to the
factorization (1.5), it suﬃces to consider only the holomor phic part Z (ρ)(M ;t). Moreover,
since the perturbative expansion is in the inverse powers of t, it is convenient to introduce
a new expansion parameter
ℏ = 2πi
t , (1.7)
which plays the role of Planck’s constant. Indeed, the semic lassical limit corresponds to
ℏ→ 0. In general, the perturbative partition function Z (ρ)(M ; ℏ) is an asymptotic power
series in ℏ. To ﬁnd its general form one applies the stationary phase app roximation to the
integral (1.2):
Z (ρ)(M ; ℏ) = exp
(
1
ℏS(ρ)
0 − 1
2δ(ρ) log ℏ +
∞∑
n=0
S(ρ)
n+1ℏn
)
. (1.8)
This is the general form of the perturbative partition funct ion in Chern-Simons gauge
theory with any gauge group, compact or otherwise. It follow s simply by applying the
– 3 –
stationary phase approximation to the integral (1.2), whic h basically gives the standard
rules of perturbative gauge theory [52, 3, 4, 5] that will be d iscussed in more detail below.
For now, we note that the leading term S(ρ)
0 is the value of the classical Chern-Simons
functional evaluated on a ﬂat gauge connection A(ρ) associated with a homomorphism ρ,
S(ρ)
0 = − 1
4
∫
M
Tr
(
A(ρ)∧dA(ρ) + 2
3A(ρ)∧A (ρ)∧A (ρ)
)
. (1.9)
Moreover, the coeﬃcient of the next-leading term, δ(ρ), is an integer (which, like all other
terms, depends on the 3-manifold M , the gauge group GC, and the classical solution ρ).
Each coeﬃcient S(ρ)
n is obtained by summing over Feynman diagrams with n loops. For
example, the “two-loop term” S(ρ)
2 is obtained by adding contributions of the two kinds of
Feynman diagrams shown in Figure 1. Although certain featur es of the Feynman rules in
Chern-Simons theory with complex gauge group GC are similar to those in a theory with
compact gauge group G, we will see that there exist important diﬀerences.
b)a)
Figure 1: Two kinds of 2-loop Feynman diagrams that contribute to S(ρ)
2 in Chern-Simons gauge
theory.
In Chern-Simons theory with compact gauge group, one often d evelops perturbation
theory in the background of a trivial (or reducible) ﬂat conn ectionA(ρ). As a result, the
perturbative coeﬃcients S(ρ)
n have a fairly simple structure; they factorize into a produc t
of topological invariants of M — the ﬁnite type (Vassiliev) invariants and varations there of
— and group theory factors [33]. In particular, they are rati onal numbers.
The situation is very diﬀerent in Chern-Simons theory with co mplex gauge group; the
S(ρ)
n are completely new, unexplored invariants of M . From the physics point of view, one
novelty of the complex case is that it involves perturbation theory in the background of a
genuinely non-abelian ﬂat connection, a problem that has no t been properly addressed in
the existing literature. One of our goals below will be to mak e a few modest steps in this
direction. As we shall see, in general, the information abou t the gauge group GC and the
3-manifold M is mixed within S(ρ)
n (M ) in a non-trivial way. In particular, in this case the
S(ρ)
n (M )’s are not ﬁnite type invariants and are typically not valued in Q.
If we take ρ to be the trivial representation, denoted as ρ = 0 (and corresponding
to a trivial ﬂat connection A(0) = 0), the perturbative invariants S(0)
n (M ) are actually
identical to those in Chern-Simons theory with compact gaug e group G. Then Z (0)(M ; ℏ)
can be obtained from the perturbative partition function of Chern-Simons theory with
– 4 –
gauge group G simply by allowing ℏ to be complex, 1
Z (0)
GC
(M ; ℏ) = Z (0)
G (M ; ℏ). (1.10)
Both sides of this equation have the form of the asymptotic se ries (1.8) with S(0)
0 = 0.
This example, however, is very special, as one can see e.g. by considering hyperbolic
3-manifolds, which, in a sense, constitute the richest and t he most interesting class of 3-
manifolds. A hyperbolic structure on a 3-manifold M corresponds to a discrete faithful
representation of the fundamental group π1(M ) into Isom +(H3)∼
=PSL (2, C), the group of
orientation-preserving isometries of 3-dimensional hype rbolic space H3. One can compose
this representation with a morphism φ from PSL (2) to a larger algebraic group to obtain
a group homomorphism
ρ :π1(M )֒→PSL (2, C)
φ
−→GC. (1.11)
The ﬂat connection A(ρ) associated with this homomorphism is genuinely non-abelia n and
the corresponding perturbative invariants S(ρ)
n are interesting new invariants of the hyper-
bolic 3-manifold M . See Table 2 on page 52 for the simplest example of this type.
Standard textbooks on quantum ﬁeld theory tell us how to syst ematically compute
the perturbative invariants S(ρ)
n for any n, starting with the classical action (1.1) and a
classical solution (1.3), and using the Feynman diagrams me ntioned above. This compu-
tation will be reviewed in section 2 for the problem at hand. H owever, direct computation
of Feynman diagrams becomes prohibitively complicated whe n the number of loops n be-
comes large. Therefore, while Feynman diagrams provide the ﬁrst-principles approach to
calculating Z (ρ)(M ; ℏ), it is useful to look for alternative ways of computing and d eﬁning
the perturbative GC invariants of M .
Such alternative methods often arise from equivalent physi cal descriptions of a given
system. In some cases, interesting equivalent description s are obtained merely via diﬀer-
ent gauge choices. A relevant example is the much-studied Ch ern-Simons gauge theory
with compact gauge group G. Perturbative expansion of this theory around the trivial
ﬂat connection A(0) = 0 in the covariant Landau gauge leads to the conﬁguration sp ace
integrals for the Vassiliev invariants, while in the non-co variant light-cone gauge it leads
to the Kontsevich integral [33]. This example illustrates h ow a simple equivalence of two
physical descriptions (in this case, based on diﬀerent gauge choice) leads to an interesting
mathematical statement. Much deeper examples involve non- trivial duality symmetries in
quantum ﬁeld theories. For example, duality was the key elem ent in the famous work of
Seiberg and Witten [45] that led to an exact description of th e moduli space of vacua in
N = 2 gauge theory and to a new way of computing Donaldson invari ants of 4-manifolds.
Similarly, in the present case of Chern-Simons gauge theory with complex gauge group,
there exist several ways to quantize the theory. When combin ed with topological invari-
ance, they lead to multiple methods for computing the pertur bative invariant Z (ρ)(M ; ℏ).
Mathematically, each of these methods can be taken as a deﬁni tion of Z (ρ)(M ; ℏ); however,
1In a theory with compact gauge group, one frequently uses the “level” k as the coupling constant. It is
related to ℏ via ℏ = iπ/ (k + h∨), where h∨ is the dual Coxeter number of G, e.g. h∨ = N for G = SU (N ).
– 5 –
it is important to realize that they all have a common origin a nd are completely equivalent.
In the mathematical literature, this is usually stated in th e form of a conjecture. To wit,
the following are equivalent:
• F eynman diagrams: This is the most traditional approach, which was already
mentioned earlier and which will be discussed in more detail in Section 2.1. It gives
Z (ρ)(M ; ℏ) as an asymptotic power series of the form (1.8) where every c oeﬃcient
S(ρ)
n can be systematically computed by evaluating Feynman diagr ams.
• Quantization ofMﬂat (GC, Σ) : According to the general axioms of topological quan-
tum ﬁeld theory [2], Chern-Simons gauge theory associates a Hilbert space HΣ to a
closed surface Σ (not necessarily connected), and, similar ly, it associates a vector in
HΣ to every closed 3-manifold M with boundary Σ. In Chern-Simons theory with
complex gauge group GC, the space HΣ is obtained by quantizing the classical phase
spaceMﬂat (GC, Σ), which is the moduli space of ﬂat GC connections on Σ. Therefore,
in this approach Z (ρ)(M ; ℏ) is obtained as the wave function of a state associated with
M . (If M is a closed 3-manifold without boundary, one can consider e.g. a Heegaard
decompositionM =M+∪Σ M− along Σ and apply this approach to each handlebody,
M+ andM−.) In particular, as we explain in Section 2.2, Z (ρ)(M ; ℏ) obeys a system
of Schr¨ odinger-like equations
ˆAi Z (ρ)(M ; ℏ) = 0 , (1.12)
which, together with appropriate boundary conditions, uni quely determineZ (ρ)(M ; ℏ).
One advantage of Chern-Simons theory with complex gauge gro up is that the classical
phase space Mﬂat (GC, Σ) is a hyper-K¨ ahler manifold, a fact that considerably sim -
pliﬁes the quantization problem in any of the existing frame works (such as geometric
quantization [54], deformation quantization [6, 32], or “b rane quantization” [24]).
• “Analytic continuation”: Since GC is a complexiﬁcation of G, one might expect
that Chern-Simons theories with gauge groups G andGC are closely related. This is
indeed the case [22]. For example, if M = S3 /integerdivideK is the complement of a knot (or
a link) in the 3-sphere, one can compare the perturbative GC invariantZ (ρ)(M ; ℏ)
with the expectation values of a Wilson loop supported on K⊂ S3 in Chern-Simons
theory with compact gauge group G. The deﬁnition of the Wilson loop operator,
WR(K) := Tr R P exp
∮
KA, involves a choice of a representation R of G, and the
expectation value
PG,R(K;q) := ⟨WR(K)⟩ (1.13)
is a certain polynomial invariant of K. Letting R =Rλ be the irreducible representa-
tion of G with highest weight λ, the invariant quadratic form −Tr on the Lie algebra
g = Lie(G) identiﬁes λ with an element λ∗ of the Cartan subalgebra t⊂ g. Then,
one considers a double-scaling limit such that
ℏ→ 0, λ ∗→∞ , u := ℏλ∗ = ﬁxed. (1.14)
– 6 –
Taking this limit and analytically continuing to complex va lues of u, one has [22]
Z (ρ)(M ; ℏ)
Z(S3; ℏ) = asymptotic expansion of PG,Rλ (K;q), (1.15)
where q = e2ℏ and ρ is determined by u. Further details will be explained in Sec-
tion 2.2.1.
• State sum model: Finally, using the topological nature of the theory, one can
construct Z (ρ)(M ; ℏ) by decomposing M into more elementary pieces. In particular,
one can consider a decomposition of M into tetrahedra, i.e. a triangulation,
M =
N⋃
i=1
∆ i. (1.16)
Since each tetrahedron ∆ i is a 3-manifold with boundary, it deﬁnes a state (a vector)
in the Hilbert space associated to the boundary of ∆ i. Then, gluing the tetrahedra
together as in (1.16) leads to an expression for Z(M ) as a sum over diﬀerent states.
Of course, the result cannot depend on the choice of the trian gulation. A well-known
example of such a state sum model is the Turaev-Viro invarian t [50].
In general, states associated to the tetrahedra ∆ i are labeled by representations of the
gauge group, which means that the set of labels is discrete in a theory with compact
gauge group, but is continuous in a theory with non-compact g auge group. Therefore,
in Chern-Simons theory with complex gauge group GC one might hope to deﬁne the
perturbative GC invariant Z (ρ)(M ; ℏ) as an integral over states, starting from the
initial data of a triangulation (1.16) and a homomorphism ρ. We will therefore use
the word “state integral” instead of using the more familiar term “state sum” for
invariants deﬁned in this way. Constructing such an invaria nt for the simplest theory
with GC = SL(2, C) is one of the main goals of the present paper, and will be
considered in detail in section 3.
Of the diﬀerent approaches just outlined, the ﬁrst three have been used previously to tackle
Chern-Simons theory with complex gauge group, while the fou rth is new. In principle one
can compute Z (ρ)(M ; ℏ) following any of these four approaches individually. Howe ver,
as we show in Section 2, combining them together dramaticall y improves computational
power. For example, when M is a knot complement, one can combine approaches 2 and
3 to learn that the operators ˆAi in (1.12) should also annihilate the polynomial invariants
PG,R(K;q) computed by Chern-Simons gauge theory with compact gauge g roup G,
ˆAi PG,R(K;q) = 0 . (1.17)
(The normalization by Z(S3) is not important here.) This provides a very simple method
for ﬁnding the ˆAi’s — see sections 2.2 and 4.2.1 for further details and a concr ete example.
In turn, combining approaches 2 and 3 with the ﬁrst approach i mplies that, in the
limit (1.14), the asymptotic expansion of the polynomial in variantPG,R(K;q) has the form
– 7 –
(1.8). For G =SU (2) (whose complexiﬁcation is GC =SL(2, C)) this statement is already
known as a generalization of the Volume Conjecture, ﬁrst pro posed in [22] and further
reﬁned in [38, 23]. In particular, if G =SU (2) and R is its n-dimensional representation,
the polynomial PG,R(K;q) is called the “ n-colored Jones polynomial” of K and is denoted
Jn(K;q). The proposed relation (1.15) then says that the asymptoti c expansion of the
colored Jones polynomial reproduces the perturbative SL(2, C) invariant Z (ρ)(M ; ℏ); in
particular, the expansion has the structure (1.8) with a ver y interesting dependence on
both ρ and ℏ.
In Section 3, we describe the fourth approach. Building on th e work of Hikami [26,
27], we construct a state sum model for perturbative SL(2, C) Chern-Simons theory on a
hyperbolic 3-manifold M (possibly with boundary). Schematically, the state sum mod el
has the form
Z (ρ)(M ; ℏ) =
∫
Cρ
e
1
2ℏ f (p)
N∏
j=1
Φ ℏ
(
∆ j
) ±1
N −b0(Σ)∏
i=1
dpi√
4πℏ
, (1.18)
where Φ ℏ(∆ j) is the quantum dilogarithm function, associated to every t etrahedron ∆ i in
a triangulation of M , b0(Σ) is the number of connected components of Σ, and f (p) is a
simple quadratic polynomial of the integration variables pi.
One limitation of the construction of the state sum model, in the form stated here,
is that it applies only to hyperbolic 3-manifolds. Although we expect that it can be
extended to arbitrary 3-manifolds with boundary, we will no t presently attempt to seek
such a generalization. Hyperbolic 3-manifolds do provide t he richest and, in a sense, the
most interesting laboratory for studying SL(2, C) Chern-Simons theory. There are various
other questions that we do not address here. One obvious exam ple is to deﬁne a state sum
model for perturbative Chern-Simons theory with complex ga uge group GC not equal to
SL(2, C) (or PSL (2, C) = SL(2, C)/{±1}). A much deeper issue would be to go beyond
perturbation theory, even in the simplest case of GC =SL(2, C). Indeed, once we have a
state sum model that allows the computation of all perturbat ive invariantsS(ρ)
n to arbitrary
order n, the next natural question is whether there exists a state su m model that allows a
non-perturbative computation of Z(M ), as a function of q =e2ℏ . We leave these questions
for future work.
By the end of this paper we will have developed several tools t hat allow us to solve
perturbative Chern-Simons gauge theory with complex gauge group exactly, in some cases
in more than one way. By an exact solution we mean a straightfo rward method that
explicitly determines (at least in principle) all perturba tive invariants S(ρ)
n . In Section 4,
we illustrate how these methods work in the case of the ﬁgure- 8 knot complement (the
simplest hyperbolic knot complement) and compare the resul ts of diﬀerent calculations.
As expected, we ﬁnd perfect agreement.
Even in this simplest example, the perturbative invariants S(ρ)
n turn out to be highly
non-trivial (see e.g. Table 2). As we illustrate in this example, the new perturbat ive
invariantsS(ρ)
n computed by Chern-Simons gauge theory with complex gauge gr oup GC in
the background of a non-abelian irreducible ﬂat connection A(ρ) contain much interesting
– 8 –
information about the geometry of M . We believe that studying these invariants further,
both physically and mathematically, can lead to exciting de velopments in both subjects.
