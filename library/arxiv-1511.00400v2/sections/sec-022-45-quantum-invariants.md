---
doc_id: arxiv-1511.00400v2
doc_title: "Reidemeister torsion, hyperbolic three-manifolds, and character varieties Joan Porti ∗"
section_id: sec-022-45-quantum-invariants
section_title: "Quantum invariants"
section_number: 4.5
pages: 35-39
source_pdf: 1511.00400v2.pdf
source_sha256: 6cb493049394ce3a
doc_brief: "Reidemeister torsion, hyperbolic three-manifolds, and character varieties Joan Porti ∗ — This is a survey on Reidemeister torsion for hyperbolic thre e-manifolds of ﬁnite volume."
---
When (k1, k2) = (2, 0), Sym 2 is the adjoint representation and its torsion occurs
in the volume conjecture.
The role of the torsion in the expansion of the path integral is alread y men-
tioned in the work of Witten [102] and Bar-Natan Witten [3]. Of course the work
of Kashaev [47] and Murakami-Murakami [77] play a key role in the con jecture.
For a knot K, let JN (K; z) denote the colored Jones polynomial of K. If the
knot is hyperbolic, let u denote Thurston’s parameter of the Dehn ﬁlling space
(Deﬁnition 3.19). Denote the corresponding character by χu and let CS (K, χu)
denote the C-valued Chern-Simons invariant of a representation with characte r
χu, namely the real part is minus the Chern-Simons invariant and the ima ginary
part is the volume of the representation. The following version is tak en from
[76] by H. Murakami, who attributes it to [37, 20].
Conjecture 4.26. Let K be a hyperbolic knot. There exists a neighborhood
U ⊂C of the origin such that for u ∈U − πiQ, we have the following asymptotic
equivalence:
Jn(K; e
2πi +u
N ) ∼
N →∞
√−π
2 sinh( u
2 ) /par⟩nl⟩ft.alt1T2
K,m(χu)/par⟩nright.alt1
− 1
2
/par⟩nl⟩ft.alt3 N
2πi + u /par⟩nright.alt3
1
2
e
N
2πi +u CS(K,χu)
where m denotes the meridian of the knot.
Again this paper uses a diﬀerent convention for torsion from [76] a nd the
other references, as it is the opposite to the convention for analy tic torsion. It
has been checked for the ﬁgure eight knot and u real, 0 < u < log((3 +
√
5)/slash.l⟩ft2)
by Murakami in [76]. For torus knots, the volume is zero, but not the Chern
Simons invariant nor the torsion, and the asymptotic computations of Dubois-
Kashaev [24] and Hikami-Murakami [44] support the correspondin g conjecture
for torus knots.
Related to this conjecture, the torsion is also involved in a potential function,
introduced by Yokota [110]. From a diagram of the projection of a kn ot K, in
[81] Ohtsuki and Takata deﬁne ω2(K)−1 as the modiﬁed Hessian of the potential
function of the diagram. They justify (formally) that
/radical.alt1
ω2(K) is the term that
appears in the asymptotic development of the Kashaev invariant an d therefore
they conjecture
1
ω2(K) = ±2 i T2
K,m(χ̺).
In [81] they prove that the conjecture holds true for two bridge k nots.
35
There is also a remarkable contribution of Dimofte and Garoufalidis [1 9],
that deﬁne an invariant from an ideal triangulation of a knot exterio r and an
enhanced Neumann-Zagier datum. Enhanced Neumann-Zagier dat um means
that, besides the complex collection shape parameters of the ideal hyperbolic
tetrahedra, they use matrices with integer coeﬃcients that desc ribe how to glue
the tetrahedra and a collection of integers that code a combinator ial ﬂattening
(introduced in [78] by Neumann to calculate the Chern-Simons invaria nt combi-
natorially). Form these data, Dimofte and Garoufalidis construct a n invariant of
the hyperbolic manifold and they check numerically that it equals 1 /slash.l⟩ftT2
K,m(χ̺)
up to some constant.
5 Representations in PSLn+1(C)and the adjoint
In [82] I considered the torsion corresponding to the adjoint repr esentation as
a function on the variety of characters in SL 2(C), in fact PSL 2(C). Kitayama
and Terashima [55] considered the analog for PSL n+1(C), i.e. the torsion for the
adjoint representation.
Along the section M 3 denotes an oriented ﬁnite volume hyperbolic three-
manifold with one cusp, the case with more cusps would require furth er notation,
but here it is essentially the same. Consider the composition of the ho lonomy
with Sym n:
̺n∶ π1M 3 → PSLn+1(C).
As we deal with representations in PSL 2(C), the holonomy does not need to be
lifted to SL 2(C).
Theorem 5.1 ([62, 60]). The character of ̺n is a smooth point of the variety of
characters X(M 3, PSLn+1(C)), of local dimension n. It is locally parametrized
by the symmetric functions on any peripheral curve.
Corollary 5.2. There exists a unique irreducible component of the characte r
variety X(M 3, PSLn+1(C)) that contains the character of ̺n.
This component is called the distinguished component and it is denoted by
X0(M 3, PSLn+1(C)).
In the proof of Theorem 5.1, one shows that sln+1(C)Ad ̺n(π1T 2) ≅Cn. In
addition, if {a1, . . . , an} is a basis for sln+1(C)Ad ̺n(π1T 2), then
{a1 ∩ [T 2], . . . , an ∩ [T 2]}
is a basis for H2(M 3; Ad̺n) and
{a1 ∩ [γ], . . . , an ∩ [γ]}
a basis for H1(M 3; Ad̺n), here γ is a peripheral curve, non-trivial in H1(T 2; Z).
See [62, 60, 55] for details. For a generic character χρ in X0(M 3, PSLn+1(C)),
sl(n, C)Ad ρ(π1T 2) ≅Cn and a similar construction applies to ﬁnd a basis for
Hi(M 3; Adρ). Generalizing the construction of [82], Kitayama and Terashima
[55] deﬁne the torsion. Here we consider the possibility that the fun ction van-
ishes, but before an exceptional set must be removed.
36
Deﬁnition 5.3. A representation ρ∶ π1M 3 → PSLn+1(C) is exceptional if:
(a) sln+1(C)Ad ρ(π1M 3) ≠0 or
(b) dim /par⟩nl⟩ft.alt2sln+1(C)Ad ρ(π1T 2)/par⟩nright.alt2 > n, for the peripheral torus T 2.
The set of characters of exceptional representations is denote d by
En+1 ⊂X0(M 3, PSLn+1(C)).
Lemma 5.4. The set En+1 is Zariski closed in X0(M 3, PSLn+1(C)).
Proof. The deﬁning properties are Zariski closed in hom (π1M 3, PSLn+1(C)) and
invariant by conjugation, so the projection to X0(M 3, PSLn+1(C)) is a Zariski
closed subset, see [98] for instance.
Deﬁnition 5.5. Let χρ ∈X0(M 3, PSLn+1(C)) − En+1, choose {a1, . . . , an} a
basis for sln+1(C)Ad ρ(π1T 2) and let γ be a peripheral curve.
(a) If {a1 ∩ [γ], . . . , an ∩ [γ]} is a basis for H1(M 3; Adρ), deﬁne
T(M,γ )(χρ) = TOR(M 3, {a1 ∩ [γ], . . . , an ∩ [γ]},
{a1 ∩ [T 2], . . . , an ∩ [T 2]}); (34)
(b) otherwise set
T(M,γ )(χρ) = 0. (35)
This yields a function
TM,γ ∶ X0(M 3, PSLn+1(C)) − En+1 → C . (36)
It can be checked that it is a well deﬁned regular function, using the ideas of
[82, 55] and Proposition 3.16. For instance, when {a1∩[γ], . . . , an∩[γ]} is a basis
for H1(M 3; Adρ), then {a1∩[T 2], . . . , an∩[T 2]} is a basis for H2(M 3; Adρ) (be-
cause H2(M 3; Adρ) is naturally isomorphic to H2(T 2; Adρ) ≅H 0(T 2; Adρ)).
When there may be confusion, the index n + 1 may be included in the notation:
T n+1
M,γ ∶ X0(M 3, PSLn+1(C)) − En+1 → C. (37)
The following proposition relates TM,γ with the torsion T2n
(M,γ ) when we
consider symmetric powers of representations in PSL 2(C).
Proposition 5.6. For a generic character χρ ∈X0(M 3, PSL2(C)), including
the holonomy χ̺,
T n+1
M,γ (χρn ) =
n
/product.disp
i=1
T2i
M,γ (χρ).
Corollary 5.7. For a generic character χρ ∈X0(M 3, PSL2(C)), including the
holonomy χ̺,
T n+1
M,γ (χρn ) = T n
M,γ (χρn−1) T2n
M,γ (χρ).
37
Proof of Proposition 5.6. The proof is straightforward from Klebsh-Gordan for-
mula:
Ad ○ Symn =
n
/uni2295.big.disp
i=1
Sym2i (38)
and multiplicativity of the torsion for sums of representations.
The next theorem due to Weil [100], see also [58], gives a nice interpret ation
to TM,γ :
Theorem 5.8 ([100]). Let Γ be a ﬁnitely generated group and ρ an irreducible
representation with character χρ ∈X(Γ , PSLn+1(C)) − En+1. Then there is a
natural isomorphism
T Zar
χρ X(Γ , PSLn+1(C)) ≅H 1(Γ; Ad ρ)
where T Zar denotes the Zariski tangent space as a scheme.
In particular, if φ∶ Γ → Γ ′ is a group morphism, then the induced map in
cohomology corresponds to the tangent map
dφ∗∶ T Zar
χρ X(Γ ′, PSLn+1(C)) → T Zar
φ∗χρ X(Γ , PSLn+1(C)).
Few comments are in order here. First at all, the condition that χρ /slash.l⟩ft∈
En+1 is used to say that the inﬁnitesimal commutator of Ad ρ is trivial, i.e.
H 0(π1M 3; Adρ) = 0. Secondly, the variety of characters is not a variety but
a scheme: the deﬁning polynomial ideal may be not reduced, thus we must
consider the Zariski tangent space of the scheme, perhaps not r educed. Finally,
just mention that there are generalizations of this result when ρ is reducible,
see [4, 5].
This interpretation has a nice application for surface bundles over t he circle,
following again [82, 55]. Assume that M 3 is a bundle over a circle, with ﬁbre a
punctured surface Σ and monodromy ϕ∶ Σ → Σ, i.e.
M 3 = Σ × [0, 1]/slash.l⟩ft(x, 1) ∼(ϕ(x), 0).
It has a natural epimorphism π1M 3 → Z, corresponding to the projection of the
ﬁbration M 3 → S1. The induced map on the monodromy is denoted by
ϕ∗∶ X(Σ , PSLn(C)) → X(Σ , PSLn(C))
and the restriction to π1Σ of characters in X(M 3, P SLn(C)) restrict to the
ﬁxed point set of X(Σ , PSLn(C)). By Weil’s theorem, the map induced in
H 1(Σ; Ad ρ) can be interpreted as the diﬀerential dϕ∗. Thus, using Proposi-
tion 2.14, the twisted polynomial is
det(dϕ∗ − t Id).
Its evaluation at t = 1 vanishes because H ∗(M 3; Adρ) ≠ 0. The polyno-
mial is divisible by (t − 1)n, corresponding to the invariant curve γ = ∂Σ, as
dim H 1(γ; Adρ) = n. An argument using the exact sequences and the basis of
homology yields the following result:
38
Proposition 5.9. [82, 55] If M 3 is a punctured surface bundle, and γ the
boundary of the ﬁbre. Then
TM,γ = det(dϕ∗ − t Id)
(t − 1)n /divid⟩s.alt4
t=1
.
This result is very useful for computing the torsion, it allows to obta in it from
the variety of characters or moduli spaces without knowing the re presentation.
For instance Kitayama and Terashima use cluster algebras to compu te it [55].
In Subsection 5.2 we recall the method of [82] to compute it.
