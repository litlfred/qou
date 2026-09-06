---
doc_id: arxiv-1608.02961v3
doc_title: "Perturbative and nonperturbative aspects of complex Chern-Simons Theory Tudor Dimofte"
section_id: sec-000-1-introduction
section_title: "Introduction"
section_number: 1
pages: 1-8
source_pdf: 1608.02961v3.pdf
source_sha256: ef3805c23133b8f2
doc_brief: "Perturbative and nonperturbative aspects of complex Chern-Simons Theory Tudor Dimofte — We present an elementary review of some aspects of Chern-Simons theory with complex gauge group SL(N, C)."
---
2 Warmup: quantization of H(T 2) 4
2.1 Equivariant quantization . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 8
2.2 Holomorphic polarizations and CFT . . . . . . . . . . . . . . . . . . . . . . . 9
3 Complex Chern-Simons theory as a TQFT? 10
3.1 Symmetries, regularizations, and the 3d-3d correspondence . . . . . . . . . . 12
4 Three connections to three-manifold topology 13
4.1 Hyperbolic volumes, twisted torsion, and large N . . . . . . . . . . . . . . . 13
4.2 State-integral models and angle structures . . . . . . . . . . . . . . . . . . . 15
4.3 Embedded surfaces and M2 branes in the 3d index ( k = 0) . . . . . . . . . . 20
5 The Quantum Modularity Conjecture 22
arXiv:1608.02961v3  [hep-th]  15 Oct 2016
1 Introduction
Chern-Simons theory with complex gauge group came to prominence in the late 80’s, partly
as a tool for understanding three-dimensional gravity with a negative cosmological constant
[2, 3, 4, 5]. Many early developments were due to Witten. Since then, it has found a
multitude of applications and deep connections with many parts of theoretical physics and
mathematics. A highly incomplete list includes:
• Many further applications ofSL(2, C) Chern-Simons theory (and itsSL(2, R)×SL(2, R)
cousin) to three-dimensional quantum gravity and AdS/CFT. Similarly, SL(N, C)
Chern-Simons at largeN has been used to describe higher-spin theories of gravity [6, 7].
• Chern-Simons theory with gauge groupSL(N, C) can naturally be embedded in string/M-
theory, opening up many powerful perspectives and techniques for analyzing the for-
mer. As a notable example, the compactiﬁcation of N M5 branes on the product of
an ellipsoidally deformed lens space L(k, 1)b≃ S3
b/Zk and a three-manifold M (with
a topological twist along M) leads equivalently to SL(N, C) Chern-Simons theory at
level k on M [8, 9, 10] or an N = 2 supersymmetric theory TN[M] on the lens space
[11, 12, 13, 14]. This duality, known as the 3d-3d correspondence, ﬁts into a series of du-
alities involving the compactiﬁcation of ﬁve-branes on variousd-dimensional manifolds
Md, including the AGT correspondence [15] and the duality of Gukov-Gadde-Putrov
relating Vafa-Witten partition functions on M 4 and elliptic genera [16].
• There is a multitude of applications to three-dimensional geometry and topology. Fun-
damentally, partition functions of complex Chern-Simons theory on three-manifoldsM
provide new topological invariants, generalizing the famous invariants (including knot
polynomials) associated with compact Chern-Simons theory [17, 18]. As yet, a system-
atic computation of the complex invariants only exists for certain classes of manifolds
(e.g. hyperbolic ones [19, 20, 21, 22]), though new tools to attack the general case are
under development [23, 24].
The perturbative expansion of SL(2, C) Chern-Simons theory on a three-manifold M
encodes various topological invariants ofM, such as its hyperbolic volume and twisted
analytic torsion. In the case that M =S3\K is a knot complement in S3, it was con-
jectured by Gukov [25] that this expansion agrees with a (highly nontrivial) asymptotic
limit of colored Jones polynomials of K, providing physical motivation for a mathe-
matical statement known as the Volume Conjecture [26, 27]. The relation between
complex Chern-Simons theory and knot polynomials is essentially a result of analytic
continuation, albeit a subtle one [28].
The perturbative expansion of SL(2, C) Chern-Simons theory on knot complements
has been successfully reproduced [29, 30, 31] using the topological recursion of Eynard-
Orantin [32], a far-reaching formalism for the quantization of spectral curves.
The study of ﬁve-brane systems related to complex Chern-Simons theory recently led to
a vast generalization of the Volume Conjecture, involving asymptotic limits of colored
2
HOMFLY polynomials and their categoriﬁcation [33].
• There are several hints that complex Chern-Simons theory has quasi-modular proper-
ties, cf. [12, 34], though a complete physical characterization of these properties is still
missing. The asymptotic expansions of SL(2, C) Chern-Simons theory around various
singular points in the space of coupling constants (levels) [35], related by an action
of the modular group, provide evidence for the Quantum Modularity Conjecture of
Zagier [36].
• There are close connections between complex Chern-Simons theory and the mathemat-
ical theory of cluster algebras, cf. [37, 38]. Cluster algebras play an essential role in the
(local) description and quantization of phase spaces that complex Chern-Simons the-
ory attaches to two-dimensional boundaries, cf. [39, 40, 41], and Chern-Simons theory
on three-manifolds is associated with cluster-algebra morphisms.
• Very recently,SL(2, C) Chern-Simons theory at integer levels (in terms of (2.1) below,
this means k∈ Z and is∈ Z) has been proposed as an eﬀective theory of quantum
Hall systems [42]. Excitingly, this may lead to tests of complex Chern-Simons theory
in the lab.
In this short review, we will only be able to touch upon a few of these topics and connec-
tions. We will actually begin in Section 2 with some basic concepts in complex Chern-Simons
theory, including the deﬁnition of the Hilbert spaces H[Σ] assigned to two-dimensional ori-
ented manifolds. One of the most prominent distinctions between Chern-Simons theory with
complex and compact gauge groups is that, in the complex case, these Hilbert spaces are
inﬁnite-dimensional. As an illustrative example, we will outline the simple quantization of
the torus Hilbert spaceH[T 2] for gauge group SL(2, C), and its dependence on the coupling
constants or “levels” of the theory. We also review some features of the reﬁned orequivariant
quantization of Hilbert spaces recently developed by Gukov and Pei [23].
This prepares us in Section 3 to discuss one of the most fundamental open problems in
complex Chern-Simons theory: deﬁning the theory as a full TQFT. In essence, this means
being able to assign Hilbert spaces H[Σ] to any oriented surface and wavefunctionsZ[M]∈
H[∂M ] to any oriented three-manifold, in such a way that the standard cutting-and-gluing
axioms of Atiyah and Segal are obeyed [43]. As we shall review, the diﬃculty with cutting
and gluing in complex Chern-Simons theory stems from the inﬁnite-dimensional nature of
Hilbert spaces, and the fact that, naively, wavefunctions often vanish or diverge. Some
very promising routes to overcoming these diﬃculties are suggested by embedding complex
Chern-Simons theory in string/M-theory, and using additional symmetries to regulate zeroes
or inﬁnities [44, 23, 24]. Interestingly, these symmetries are related to categoriﬁcation of
Chern-Simons theory.
In the second half of this review, we then discuss a few relations between complex Chern-
Simons theory and the topology and geometry of three-manifolds. In each case, we view these
relations in light of string/M-theory and the 3d-3d correspondence. In Section 4, we will
3
discuss 1) asymptotic expansions of SL(N, C) Chern-Simons partition functions, their rela-
tion to hyperbolic volumes, and their behavior at large N vis ` a visholography of ﬁve-brane
systems; 2) state-sum/integral models for SL(N, C) Chern-Simons theory, their relation to
positive angle structures on ideal triangulations of three-manifolds, and the corresponding
implication for positivity of operator dimensions in theories T [M] built from ideal triangu-
lations; 3) the interpretation of the SL(N, C) partition function at level k = 0 as counting
surfaces in a three-manifold M, BPS operators in T [M], and BPS M2 branes ending on
wrapped M5 branes in M-theory (related to recent mathematical work [45]). In Section
5, we will state some of the observations and conjectures about “quantum” modularity in
Chern-Simons theory.
We emphasize that the 3d-3d correspondence provides the main link between complex
Chern-Simons theory and localization methods in supersymmetric gauge theories, which are
the focus of this collection of articles. Particularly relevant are the reviews of T. Dumitrescu
(Contribution [46]) and B. Willett (Contribution [47]). The basic idea is that whenever
T [M] can be explicitly described as (say) a gauge theory, its partition function on spaces
such as S3 or S3/Zk is readily computed by supersymmetric localization. This has led to
new formulations and reﬁnements of Chern-Simons partition functions on M, which in turn
produce invariants of 3-manifolds,
SUSY localization forT[M]
complex CS theory onM
+ reﬁnement/categoriﬁcation...
topological invariants ofM
(1.1)
Unfortunately, we will not say very much about connections of complex Chern-Simons
theory to cluster algebras, topological recursion, categoriﬁcation, gravity, or many other
fascinating topics. We hope that some of the references above will guide readers interested
in these subjects.
2 Warmup: quantization of H(T 2)
To get a feel for the structure of complex Chern-Simons theory, we begin with a (seemingly)
elementary exercise: the quantization of the phase space that SL(2, C) Chern-Simons theory
attaches to a two-torus.
First, some generalities. As discussed in [5], the action of complex Chern-Simons theory
on a Euclidean three-manifold M takes the form
Ik,s = 1
2(k +is)SCS(A) + 1
2(k−is)SCS(A), (2.1)
where SCS = 1
4π
∫
M Tr
(
A∧A + 2
3A∧A∧A
)
is the usual Chern-Simons functional. Here
A is a connection on an SL(2, C) bundle over M, and A is its complex conjugate. The
group SL(2, C) contains SU (2) as its maximal compact subgroup (in fact, as a complex
manifold, SL(2, C)≃T∗SU (2)), and on a compact 3-manifold M there can be large gauge
4
transformations g :M→SL(2, C) that wrap nontrivially around the compact SU (2). The
path-integral integration measure exp(iIk,s) is invariant under large gauge transformations
on a closedM so long ask∈ Z. On the other hand, the coupling constants is unconstrained.
For a unitary theory — which in Euclidean space means that partition functions are
conjugated under orientation reversal — the action must be real, which forces s to be real.
We will assume this to be true in the quantization below, though eventually in partition
functions we will ﬁnd that we can analytically continue s in a straightforward manner.
There also exist exotic unitarity structures with s imaginary [5], which will lead to slightly
diﬀerent Hilbert spaces.
As an aside, in the relation to 3d Euclidean gravity with a negative cosmological constant,
one identiﬁes the Hermitian and anti-Hermitian parts of A = w +ie as a vielbein ( e) and
a spin connection ( w). The part of the action Ik,s proportional to s becomes the usual
Einstein-Hilbert action, while the part proportional to k is a gravitational Chern-Simons
term [3]. The classical solutions of Chern-Simons theory on a three-manioﬂd M are ﬂat
SL(2, C) connections, which become identiﬁed with (possibly degenerate) metrics of constant
negative curvature, i.e. hyperbolic metrics, in 3d gravity.
Geometric quantization of complex Chern-Simons theory on a general surface Σ was ﬁrst
discussed in [5] and recently revisited in [48], using a holomorphic polarization. A more
modern perspective on quantization, based on the topological A-model, appears in [49],
following [50] (see also [51]). In the case of Σ = T 2, we can take a more pedestrian approach,
following [22, 21].
The Hilbert space that Chern-Simons theory assigns to any surface Σ is a quantization
of the classical phase space
P[Σ] =Mﬂat(SL(2, C), Σ)≃ Hom(π1(Σ),SL (2, C)). (2.2)
This is the space of complex ﬂat connections on Σ (modulo gauge transformations), or
equivalently, the space of representations of the fundamental group of Σ in SL(2, C). The
spaceP[Σ] is a ﬁnite-dimensional complex symplectic variety, possibly singular, equipped
with the Atiyah-Bott holomorphic symplectic form
Ω =
∫
Σ
δA∧ δA. (2.3)
Of course, the actual symplectic form we use for quantization should be real; the Chern-
Simons action (2.1) tells us to take
ωk,s = k +is
4π Ω +k−is
4π Ω = k
2π Re Ω− s
2π Im Ω. (2.4)
Famously, the spaceP[Σ] is hyperk¨ ahler. It admits an entireCP1 of complex structures,
one of which is singled out in the description (2.2) as a space of complex ﬂat connections. The
other complex structures can be made manifest by rewriting P[Σ] as Hitchin’s moduli space
P[Σ]≃M Hit(SU (2), Σ) associated to the compact group SU (2) [52]. Similarly, the space
P[Σ] admits a CP1 of real symplectic forms, spanned by the hyperk¨ ahler triplet (ωI,ωJ,ωK),
5
where ωI = Re Ω and ωJ = Im Ω above. The third form ωJ is a K¨ ahler form in our
chosen complex structure. Notably, 1
4π2ωI represents a nontrivial integral cohomology class
inH2(P[Σ], Z), while ωJ,ωK are cohomologically trivial. This provides another explanation
for the quantization of the level k: in geometric quantization, one requires ωk,s to be the
ﬁrst Chern class of a line bundle, which can only happen if it has integral periods, whence
k∈ Z, but s is unconstrained.
Now let us specialize to Σ = T 2. Flat connections on a torus are determined by the
holonomies ρA,ρB along the A and B cycles, up to SL(2, C) conjugation. Since the funda-
mental group π1(T 2) = Z2 is abelian, the holonomies commute and can be simultaneously
diagonalized.1 Letting x,y denote their eigenvalues, we ﬁnd
P[T 2] = (C∗× C∗)/Z2≃{ (x,y )∈ (C∗)2}/(x,y )∼ (x−1,y−1). (2.5)
The Z2 action here is just that of the Weyl group, acting as residual gauge transformations.
The holomorphic symplectic form is
Ω = 2dy
y ∧ dx
x , (2.6)
reﬂecting the nontrivial intersection of A and B cycles on T 2, whence
ωk,s = k
π (d log|y|∧d log|x|−d argy∧d argx)−s
π (d log|y|∧d argx+d argy∧d log|x|). (2.7)
As anticipated, the period of 1
2πωk,s on the compact (S1×S1)/Z2 cycle inP[T 2] is equal to
k, and is properly quantized.
In order to diagonalize the real symplectic form ωk,s, we deﬁne b to be the complex
number with Re(b)> 0 and
b2 = k−is
k +is, (2.8)
and make a change of variables 2 from (x,y )∈ (C∗)2 to (µ,ν ;m,n )∈ R2× (R/2kZ)2 :
x = exp iπ
k
(
−ibµ−m
)
, ¯x = exp iπ
k
(
−ib−1µ +m
)
,
y = exp iπ
k
(
−ibν−n
)
, ¯y = exp iπ
k
(
−ib−1ν +n
)
. (2.9)
Notice that if s is real then|b| = 1, so (x,y ) and (¯x, ¯y) are complex conjugates, as written.
Then the symplectic form collapses to
ωk,s = π
kdν∧dµ− π
kdn∧dm. (2.10)
1More precisely: the holonomies can simultaneously be put in Jordan normal form.
2The new variables absorb some powers of the coupling constants k, b, which obfuscates the eﬀect of the
classical limit k→∞ , e.g. in (2.11). It is important to keep in mind that the natural functions on the phase
space are still x, ¯x, y, ¯y.
6
We proceed to quantize the space as if it were just C∗× C∗, and restore Weyl invariance
later. The functions ν,µ and n,m can simply be quantized to operators with canonical
commutation relations
− [ν, µ] = [n, m] = k
iπ. (2.11)
Of course, since m is periodic the spectrum of n is quantized, and vice versa; altogether,
both the eigenvalues of both m and n must belong to Z/(2kZ). The well-deﬁned operators
are actually quantizations x, ¯x, y, ¯y of the C∗-valued functions in (2.9), with x = exp iπ
k
(
−
ibµ− m
)
, etc. For these we ﬁnd
yx =q
1
2 xy, ¯y¯x = ˜q
1
2 ¯x¯y ; x¯y = ¯yx, y¯x = ¯xy, (2.12)
with
q
1
2 := exp 2πi
k +is = exp iπ
k (b2 + 1), ˜q
1
2 := exp 2πi
k−is = exp iπ
k (b−2 + 1). (2.13)
Thus, abstractly, we see that the quantized operator algebra consists of two independent
Weyl algebras (or “quantum torus” algebras), one in x, y and one in ¯x, ¯y.
There are many equivalent ways to represent the operator algebra on a Hilbert space
H[T 2]. The simplest is to take
H[T 2]k,s =L2(R)⊗ C2|k|≃{f(µ,m )} (2.14)
to consist of functions of a real variable µ and an integer m∈ Z/(2kZ). Equivalently, we
may take functions of x and ¯x. Formally, in geometric quantization, this corresponds to
choosing a particular “real” polarization — taking sections of a line bundle L→P [Σ] with
c1(L) = ωk,s that are covariantly constant with respect to ν and n. The operators x, ¯x act
on f(µ,m ) as multiplication by x, ¯x, while y, ¯y are shifts
yf(µ,m ) =f(µ +ib,m− 1), ¯yf(µ,m ) =f(µ +ib−1,m + 1). (2.15)
To restore Weyl-invariance, we restrict to the Z2-invariant part of the Hilbert space, i.e.
functions that are even
f(µ,m ) =f(−µ,−m). (2.16)
Correspondingly, we should restrict to a subalgebra of the operator algebra that is invariant
under ( x, ¯x, y, ¯y)→ (x−1, ¯x−1, y−1, ¯y−1). This subalgebra is generated by operators X =
x + x−1, Y = y + y−1, and T = xy + x−1y−1 (and their conjugates), which obey
X2 + Y2 +q− 1
2 T2 = XTY + 2(1 +q−1). (2.17)
When k = 0, complex Chern-Simons theory still make sense (as long as s⁄= 0), but the
above quantization procedure requires a slight modiﬁcation [20]. The change of variables
(2.9) does not make sense, and is not necessary, since ωk=0,s is already diagonalized. Indeed,
ωk=0,s is the canonical symplectic form on C∗× C∗ when viewed as the cotangent bundle
7
T∗(S1×S1). We expect quantization to produce H[T 2]0,s = L2(Z× Z). To see it, simply
write (x,y ) = (e
π
sm+iθ,e
π
sn+iφ). The symplectic form becomes
ωk=0,s =−dn∧dθ +dm∧dφ. (2.18)
These canonically-conjugate functions are quantized to operators with [ θ, n] =−[φ, m] =i.
Since θ,φ are periodic with period 2 π, the eigenvalues of m, n must be integers. We can
represent the operator algebra (say) on functions f(m,n ) of two integers, such that
xf(m,n ) =q
m
4f(m,n− 1), ¯xf(m,n ) = ˜q−m
4f(m,n + 1),
yf(m,n ) =q
n
4f(m + 1,n ), ¯yf(m,n ) = ˜q−n
4f(m− 1,n ), (2.19)
where now (2.13) reduces to
q
1
4 = ˜q− 1
4 := expπ
s . (2.20)
With these new deﬁnitions of q and ˜q, the operators satisfy the standard quantum-torus
relations (2.12). Alternatively, and equivalently, we may take the Hilbert space to contain
functions g(m,ζ ) of an integer m and a phase ζ =eiθ, with
xg(m,ζ ) =q
m
4ζg (m,ζ ), ¯xg(m,ζ ) = ˜q−m
4ζ−1g(m,ζ ).
yg(m,ζ ) =q
n
4 g(m + 1,q
1
4ζ), ¯yg(m,ζ ) = ˜q−n
4 g(m− 1, ˜q−n
4ζ). (2.21)
Again, we impose Weyl-invariance at the end by restricting to even functions f(m,n ) =
f(−m,−n) or g(m,ζ ) =g(−m,ζ−1).
