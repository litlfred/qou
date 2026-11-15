---
doc_id: helicity03mmj
doc_title: "Geometry of higher helicities"
section_id: sec-011-5-linking-of-foliations-and-brownian-motion
section_title: "Linking of Foliations and Brownian Motion"
section_number: 5
pages: 15-18
source_pdf: helicity03mmj.pdf
source_sha256: e364dad3afff3180
toc_source: outline
doc_brief: "Geometry of higher helicities — We revisit an interpretation of higher-dimensional helicities and Hopf–Novikov invariants from the point of view of the Brownian ergodic theorem."
---
An attempt to generalize the ergodic view on helicity to higher dimensions en-
counters the following diﬃculty. Consider, for instance, the Hopf invariant for a
map ρ: S2k−1 →Sk. Just like in the S3 →S2-case, it is deﬁned as the linking
number of the preimages in S2k−1 of two generic points in the target sphere Sk.
Alternatively, one can deﬁne it as the integral
Z
S2k−1 β ∧d−1β,
(4)
where a k-form β is the pullback to S2k−1 of any volume form on Sk, normalized by
the condition that the total volume of Sk equals 1. The analytic deﬁnition above
(generalized helicity) extends easily to the case of any exact k-form β on S2k−1, or
to generalized cross-helicity
Z
M
β ∧d−1γ
(5)
for a pair of two exact forms β and γ on an n-dimensional M, where deg β +
deg γ = n + 1. The problem is to give an ergodic interpretation of these integrals
in terms of certain foliations associated to these forms. It is probably more natural
to formulate the problem in the following converse way. Given two foliations F1
and F2 of linking dimensions in M with transverse holonomy invariant measures
β1 and β2, describe the average linking of their ﬁbers in terms of these measures.
The following deﬁnition makes the problem nearly tautological (though it becomes
more interesting when we later ﬁx a volume form on M.)
Deﬁnition 5.1. Let F1 and F2 be two foliations of linking dimensions k and l with
transverse holonomy-invariant measures β1 and β2 in a compact manifold M. The
cross-helicity of these foliations is
H(F1, F2) :=
ZZ
Mx×My
LF(x, y) ∧(β1(x) ⊗β2(y)) =
ZZ
Cx(F1)×Cy(F2)
LF(x, y),
where C(Fi) is the Ruelle–Sullivan cycle of the foliation Fi, and LF is a linking
form on M × M.
Remark 5.2. In the case of smooth βi the cross-helicity can be also deﬁned as
follows:
H(F1, F2) :=
Z
M
β1 ∧d−1β2 =
Z
C(F1)
d−1β2.
1004
B. KHESIN
The equivalence of these deﬁnitions follows from the main property of the linking
form: it deﬁnes an operator e
LF : Ω∗(M) →Ω∗(M), such that for an exact k-form u
the image is one of possible primitives: LF(u) = d−1u modulo an exact (k−1)-form.
Actually, this very property (or the equivalence of the above deﬁnitions) is a
higher-dimensional (somewhat tautological) analog of the helicity ergodic interpre-
tation in 3D: the linking characteristic of the foliations is expressed in the analytic
form. To give a more precise meaning to the linking of two foliations we will ﬁx
a volume form on M. The latter allows one to identify diﬀerential forms (or, in-
variant measures for the foliations) with polyvector ﬁelds (respectively, generalized
polyvector ﬁelds spanning these foliations).
Remark 5.3. Note that in dimension 3 for linking of two vector ﬁelds, as well as
for linking of one ﬁeld and a foliation in higher dimensions, one has a natural “time”
along the ﬁeld trajectories, which allows one to apply the Birkhoﬀergodic theorem,
as well a short path system. In higher dimension, where the interpretation should
be related to linking of possibly non-compact leaves of the foliations, one is lacking
both a natural expanding system of sets, comprising the linking of diﬀerent leaves,
and a natural generalization of short path systems.
A way around these diﬃculties is an application of a Brownian version of the
Birkhoﬀergodic theorem, cf. [22].
The latter allows one to consider averaging
of a function over leaves of a foliation. This averaging is made with the help of
a leaf Laplace–Beltrami operator, and can be thought of as the large time limit
of averaging over Brownian trajectories along the leaves. First we recall several
notions from foliation theory, see [13].
Deﬁnition 5.4. Let (M, F) be a compact foliated Riemannian manifold. Consider
the leaf diﬀusion operators D(t) for the leaf Laplacian ∆F . Then the Brownian
average of a function f on M is the following function
˜f(x) = lim
n→∞
1
n
n−1
X
t=0
(D(t)f)(x).
Here the leaf diﬀusion operator D(t) is deﬁned as the limit R →∞of the
truncated diﬀusion operator:
D(t, R)f(x) =
Z
f(z)p(x, z, t, R) dz,
where p(x, z, t, R) equals the heat diﬀusion kernel p(x, z, t) if the leaf distance
between x and z is not greater than R and it equals zero otherwise. (The diﬀusion
operators D(t, R) can be thought of as averaging a given heat source after the time
R, while the operator f →˜f as averaging f over Brownian paths corresponding to
the leaf Laplace–Beltrami operator, Fig. 2.)
Although for foliations with transverse holonomy invariant measure there are
various choices for a convenient measure in the ambient manifold, we will employ
the following general existence result due to L. Garnett.
Theorem 5.5 [13]. 1) Any compact foliated Riemannian manifold (M, F) has a
nontrivial harmonic measure ν, i. e., probability measure such that ⟨∆F f, ν⟩= 0
for all f smooth in the leaf direction, where ∆F is the leaf Laplacian;
GEOMETRY OF HIGHER HELICITIES
1005
R
x
z
Figure 2. Brownian trajectories on leaves
2) Let ν be a ﬁnite harmonic measure. Then the ergodic theorem holds, using
the leaf diﬀusion operators D(t) as follows: For any ν-integrable function f there
exists an ν-integrable Brownian average ˜f which is constant along the leaves and
⟨˜f, ν⟩= ⟨f, ν⟩.
This theorem allows one to interpret ergodically the above integrals (5) by con-
sidering a Brownian motion along the leaves of the foliations and evaluating a
certain linking form along this motion. As we will see, the corresponding number
measuring the mutual linking of the leaves of the two foliations coincides with the
Hopf-type integral.
Deﬁne a Brownian average linking of two foliation leaves as follows.
Let
(M, F1, F2) be a compact Riemannian manifold with two foliations of linking di-
mensions k and l. Given a volume-form µ on M, these foliations Fj can be deﬁned
by (generalized) polyvector ﬁelds (which we denote by the same letters), such that
iFjµ = βj.
Deﬁnition 5.6. The Brownian linking of the leaves of foliations F1 and F2 passing
through the two points x, y in M with respect to the measure µ is the Brownian
average ˜f(x, y) of the function
f(x, y) := iF(x,y)LF(x, y)
on M × M along the leaf of the foliation F(x, y) = F1(x) × F2(y) passing through
(x, y) ∈M × M.
The Brownian average function ˜f(x, y) is constant along the leaves of F =
F1 × F2, i. e., on any given pair of leaves of F1 and F2. Note also that the function
f measures the linking of the foliations F1 and F2 just like in the case of linking
of compact submanifolds. (If the measures βi, i = 1, 2, are supported on closed
non-intersecting surfaces Ni ⊂M, this is exactly their mutual linking number
lk(N1, N2) =
RR
iN1(x)×N2(y)LF(x, y), cf. Deﬁnition 3.13.)
Theorem 5.7. Consider a pair of foliations F1 and F2 of linking dimensions k and
l in a compact manifold M. Let ν be a harmonic measure on M×M for the foliation
F = F1×F2 for any Riemannian metric on M. Then the space average over M×M
for the Brownian ergodic average ˜f of the function f(x, y) := iF(x,y)LF(x, y) with
respect to the measure ν does not depend on the Riemannian metric on M and is
equal to the cross-helicity H(F1, F2) of the foliations.
1006
B. KHESIN
Proof. Fix a Riemannian metric on M and the product metric on M×M. According
to the Garnett theorem, there is a harmonic measure ν on M × M.
Consider the Brownian average for the function f(x, y) := iF(x,y)LF(x, y) along
the leaves of the foliation F = F1 × F2, where the polyvector F is deﬁned with the
help of the harmonic measure ν: iFν(x, y) = β1(x) ⊗β2(y).
The second part of the Garnett theorem immediately gives the required equality:
⟨˜f, ν⟩=
ZZ
M×M
˜fν =
ZZ
M×M
fν =
ZZ
M×M
(iFLF) ν
=
ZZ
M×M
LF ∧iFν =
ZZ
M×M
LF ∧(β1 ⊗β2) = H(F1, F2).
The latter expression is also equal to
R
M β1 ∧d−1β2 for smooth measures β1 and
β2. Note that the measure ν is smooth in the latter case, since it can be taken to
be the product of the (smooth) transverse holonomy-invariant measure β1 ⊗β2 and
the Riemannian measure along the leaves of the foliation F.
□
Remark 5.8. To give an ergodic interpretation of the higher Hopf invariant (4)
one should consider the linking of diﬀerent leaves of the same foliation deﬁned by
the form β. In the latter case one can guarantee that there exists a harmonic form
¯ν on M, such that the harmonic form on M × M is its square: ν = ¯ν ⊗¯ν.
For arbitrary transverse holonomy-invariant measures the harmonic measure ν
is not smooth in general, cf. [17]. Note that this “Brownian interpretation” does
not involve short path systems.
