---
doc_id: arxiv-1211.1812v5
doc_title: "Presheaves of superselection structures in curved spaceti mes Ezio Vasselli ezio.vasselli@gmail.com"
section_id: sec-009-42-twisted-nets-and-background-potentials
section_title: "Twisted nets and background potentials."
section_number: 4.2
pages: 23-28
source_pdf: 1211.1812v5.pdf
source_sha256: 211667ea1312d47f
doc_brief: "Presheaves of superselection structures in curved spaceti mes Ezio Vasselli ezio.vasselli@gmail.com — We show that superselection structures on curved spacetime s, that are expected to describe"
---
We show how a class of twists arises when a quantum ﬁeld interacts wit h a classical background
potential. We start by assuming that M is a globally hyperbolic spin manifold and consider the
free Dirac ﬁeld ψ∗ interacting with a (classical) closed 1–form A ∈Z 1
deRham(M ).
To this end we extract some informations from A. A ﬁrst point is that, since A is closed, for
any loop ℓ : [0, 1] → M the integral ∫
ℓA is independent of the choice of ℓ in its homotopy class,
thus we obtain the character
ζA :π1(M ) → T , ζA([ℓ]) := exp 2 πi
∫
ℓ
A . (4.6)
Moreover, since any diamond o ∈ ∆ is simply connected there is a local primitive φo ∈ C∞(o, R)
such that A|o =dφo , and we have
φo′ |o −φo = Λ o′o ∈ R ⇒ Λo′′o′ + Λo′o = Λ o′′o , ∀o ⊆o′ ⊆o′′ ∈ ∆ .
Let now b ∈ Σ 1(∆) and β : [0, 1] → |b| ⊂ M such that β(0) ∈∂1b , β(1) ∈∂0b . Then
∫
β
A =
∫
β
dφ|b| = φ|b|(β(1)) −φ|b|(β(0)) = φ∂0b(β(1)) −φ∂1b(β(0)) + Λb ,
where Λ b := Λ |b|∂0b − Λ |b|∂1b . Note that the family Λ = {Λb} is a cocycle and it can be veriﬁed
that it encodes the cohomology class of A (see [34, §3]). In particular the holonomy of A can be
reconstructed as follows. Let a ∈ ∆ and p :a →a, p =bn ∗... ∗b1 ; then using the isomorphism
(2.3) we have a homotopy class [ p] ∈ π1(M ) containing a loop ℓ : [0, 1] → M , ℓ = βn ∗... ∗β1 ,
where each curve βk , k = 1,...,n , fulﬁls the above properties with respect to bk ∈ Σ 1(∆) (see [35,
§2.5.1]). Thus, iterating the previous equality, we obtain
∫
ℓ
A =
∑
k
∫
βk
A =
∑
k
Λbk . (4.7)
We now deﬁne a net by means of the family φ and the free Dirac ﬁeld. To this end we consider the
spinor bundle DM → M , the space S∞
c (M,DM ) of compactly supported, C∞ -sections of DM
(spinors), and, for any o ∈ ∆, the space S∞
o (M,DM ) of spinors supported within o ∈ ∆. We note
that we can deﬁne the product
e2πiφos ∈S∞
o (M,DM ) , ∀o ∈ ∆ , s ∈ S ∞
o (M,DM ) .
Let us consider the free Dirac ﬁeld ψ∗ : S∞
c (M,DM ) →BH∗ in the sense of [12]. For any o ∈ ∆
we deﬁne the operator-valued distribution
ψo : S∞
o (M,DM ) →BH∗ , ψo(s) := ψ∗(e2πiφos) .
23
Clearly, deﬁning the ﬁeld ψo corresponds to considering the local gauge transformation
ψ∗(x) → e2πiφo(x)ψ∗(x) , x ∈o ,
which yields in o a solution for the Dirac equation with interaction given by A. The net of von
Neumann algebras F∗ = (F, ∗) ⊂BH∗ ,
Fo := {ψo(s) : s ∈ S ∞
o (M,DM )}′′ ⊂BH∗ , o ∈ ∆ ,
coincides with the one deﬁned by ψ∗ , thus at a ﬁrst stage F∗ does not seem to preserve informations
on the potential A; but, in the following lines, we shall show that this is not the case.
We consider global gauge transformations αz(ψo(s)) := zψo(s), s ∈ S ∞
o (M,DM ), z ∈ T, that
are unitarily implemented in the fermionic Fock space H∗ by universality of the CARs,
αz(ψo(s)) = Vzψo(s)V ∗
z , ∀z ∈ T , (4.8)
and set G∗ := {Vz,z ∈ T} ⊂ UH ∗ with grading element γ =V−1 . This yields the observable subnet
R∗ = (R, ∗)∆ , Ro =Fo ∩G′
∗ , o ∈ ∆.
Now, for any o ⊆o′ we consider the map
o′o(ψo(s)) := ψo′(s) = ψ∗(e2πi(φo+Λ o′ o)s) = e2πiΛ o′ oψo(s) , s ∈ S ∞
o (M,DM ) .
By universality, any o′o extends to a *-monomorphism o′o : Fo → Fo′ and we obtain a net
F = (F, )∆ . A natural representation of F can be constructed as follows: we deﬁne the Hilbert net
bundle H = (H,U )∆ ,
Ho ≡H∗ , Uo′o := Vexp 2πiΛ o′ o , ∀o ⊆o′ ,
and then note that, by (4.8),
o′o(t) = αexp 2πiΛ o′ o(t) = Uo′otU ∗
o′o , ∀o ⊆o′ , t ∈Fo .
The holonomy of H is easily computed using (4.6) and (4.7):
Up =
∏
k
Vexp 2πiΛ bk
= VζA([ℓ]) ∈G∗ , ℓ ∈ [p] ∈π1(M ) .
Thus F is a twisted net faithfully represented in the Hilbert net bundle H = (H,U )∆ . Performing
a parallel displacement around the loop p :a →a yields a phase factor aﬀecting the charged ﬁeld
operators,
adUp(ψa(s)) = ζA([ℓ])ψa(s) = exp 2 πi
∫
ℓ
A · ψa(s) , ℓ ∈ [p] ∈π1(M ). (4.9)
Thus, if v0 ∈ H∗ is the vacuum, then the relative phase exp 2 πi ∫
ℓA appears between the states
ψa(s)v0 , Upψa(s)v0 ∈H∗ (we use the notation in which ψa(s) is deﬁned by the creation operator).
To give an example we parametrize R4 by the coordinates x0,x 1,x 2,x 3 and deﬁne M = R4 −Sδ ,
where Sδ is the closed tube centered around the axis x3 and having ray δ >0 . The base ∆ is given
by the one of double cones contained in M , which generates a nontrivial topology in the sense that
π1(∆) ≃π1(M ) ≃ Z (note that M is homotopic to S1 ).
We consider a vector potential A′ ∈ Ω 1(R4) such that F :=dA′ ∈ Ω 2(R4) is supported within
Sδ . Note that this scenario is modeled in such a way to obtain a situation a nalogous to the one of
the Aharonov-Bohm eﬀect, see [19, §15.5]. We can always ﬁnd such 1–forms A′ by starting from
F ∈ Ω 2(R4) fulﬁlling the above property and deﬁning A′ as a primitive of F .
As a ﬁnal step we deﬁne A ∈ Ω 1(M ), A :=A′|M . In this way, the previous hypothesis say that
A is closed and we can apply the previous construction, that gives rise to the phase factor (4.9).
This last coincides with the phase aﬀecting the wavefunctions of elec trically charged particles in the
Aharonov-Bohm eﬀect (see [19, Eq.15.33]).
24
4.3 Current algebras on S1 .
We now apply Lemma 4.1 to current algebras on S1 deﬁned as in the approach of Buchholz-Mach-
Todorov ([6, 7]); here, at a ﬁrst stage, ﬁelds fulﬁlling braided commu tation relations appear, anyway
after a ”bosonization” procedure a causal ﬁeld net is constructe d. For a complete discussion of the
model we refer the reader to the above-cited references; here we limit ourselves to give the basic
deﬁnitions, needed to see how Lemma 4.1 applies.
The base ∆ of S1 is the one of intervals with proper closure, and we write o ⊥w ⇔o ∩e = ∅ .
We take a ﬁxed n ∈ N (with no squares in the factor decomposition, see the above-cited references),
parametrize S1 with complex numbers of modulus 1 , and for every o ∈ ∆ consider the space
Vn
o := {q ∈C∞(S1, C) : supp( q) ⊆o, zq(z) ∈ R, ∀z ∈S1,
∮ 1
2πiq(z)dz =
√
2n }. (4.10)
Here every q ∈ Vn
o is interpreted as a charge distribution supported within o ∈ ∆, see [6, Eq.2.24].
A ﬁeld net Fn
∗ = (Fn, )∆ ⊂BH∗ is deﬁned, with local von Neumann algebras
Fn
o = {φq ∈UH ∗ : q ∈ Vn
o }′′ , o ∈ ∆ ,
see [6, Eq.4.93] and the following remarks. The net Fn
∗ is bosonic in the sense that [ φq,φq′ ] = 0
whenever φq ∈ Fo , φq′ ∈ Fe with o ⊥ e , see the discussion after [6, Eq.4.82]. There is a gauge
group G∗ ≃ Z2n generated by a unitary
V = e2πi(2n)−1/2Q ∈UH ∗ : V 2n = 1 ,
on which we deﬁne the grading element γ = 1 ; in the previous expression Q denotes an unbounded
operator on H∗ aﬃliated with the von Neumann algebra generated by Fn , see [6, Eq.4.40], which
is interpreted as the charge. We have
VφqV ∗ = eiπ/nφq , ∀o ∈ ∆ , q ∈ Vn
o , (4.11)
see [6, Eq.4.94]. We can apply Lemma 4.1 with morphisms of the form
χ : Z ≃π1(S1) →G∗ ,
that are determined by the choice of χ(1) that must be of the type χ(1) = Vκ , κ ∈ {1,..., 2n − 1} .
As a consequence of Cor.4.3, the twisted net F deﬁned by χ has observable net isomorphic to the
untwisted net Rn
∗ = (Rn, )∆ generated by operators in Fn
∗ commuting with V . We note that V
is, indeed, a central element of the von Neumann algebra ⃗Rn ⊂BH∗ generated by the family Rn ,
see [6, Eq.4.90]. Any φq deﬁnes a localized automorphism of ⃗Rn ,
γq := adφq , γq(t) = t, ∀t ∈Re, e⊥ supp(q) .
Passing to the twisted net Fn we have a representation π : Fn → BH, where H = (H,U )∆ is the
Hilbert net bundle with ﬁbres Ho ≡H∗ , o ∈ ∆, deﬁned as in Lemma 4.1,
πo :Fn
o →BH∗ , adUo′o ◦πo = πo′ |F no , ∀o ⊆o′ ;
here any πo is the inclusion map Fn
o →BH∗ , thus in the sequel it will be dropped from the notation.
It is instructive to exhibit the eﬀect of the parallel displacement alon g a loop on the charged ﬁelds.
To this end, to ﬁx the ideas we take κ = 1 , that means χ(1) = V . Given a ∈ ∆, the homotopy
class of any loop p :a →a is labelled by an integer [ p] ∈ Z, thus
adUp(φq) = V [p]φqV [p],∗ = eiπ[p]/nφq , ∀φq ∈Fn
a ,
and a relative phase appears between the charged ﬁeld and its para llel displacement. We note
that the interpretation of ad Up(φq) as the displacement of the ﬁeld operator φq inducing the DHR
automorphism γq is in accord with the standard formulation of charge transporters , see [30, §3.4.5].
25
4.4 Existence of ﬁeld nets with a given gauge symmetry.
The following construction is on the line [14], where similar results are pr oven for the Minkowski
spacetime. We prove that for every suitable compact group G0 , globally hyperbolic spacetime M
and ﬂat bundle G → M with suitable structure group, there is a twisted ﬁeld net over which G acts
as a group of internal symmetries. The ”untwisted” net from which we start is deﬁned by means of
generalized free ﬁelds and yields a large class of toy models where the analysis of topologically trivial
superselection sectors of [22, 35] can be checked, as happens fo r [14] in the Minkowski spacetime.
In the sequel we shall consider a Z2 -graded group ( G0,γ ), not necessarily realized on a Hilbert
space, where G0 is compact and metrizable. Let λ be a symmetric and separating set 7 of irreducible
subrepresentations of the regular representation of G0 . We consider the corresponding Hilbert space
Lλ := ⊕̺∈λL̺ ⊂L2(G0)
on which G0 acts by means of the faithful unitary representation
G0 →ULλ , g ↦→gλ := ⊕̺g̺ , (4.12)
where any g̺ is a unitary acting on the irreducible, ﬁnite dimensional G0 -Hilbert space L̺ . The
grading element γ induces the spectral decomposition
Lλ =L+
λ ⊕L−
λ ,
which decomposes (4.12) into
G0 →UL ±
λ , g ↦→g±
λ := ⊕̺(γ)=±1g̺ . (4.13)
Finally, we consider a real structure (that is, an antilinear, isometr ic map) J :L+
λ →L+
λ , J 2 = 1 ,
commuting with (4.12) and stabilizing the subspaces L̺ for any ̺ ∈λ with ̺(γ) = 1 , so that we
have real structures J̺ : L̺ → L̺ . We denote the real subspace of J -invariant vectors in L+
λ by
L+,J
λ , which is a real Hilbert space with the scalar product induced by L+
λ .
Now, we say that a compactly supported f :M →L+,J
λ is C∞ whenever the function fv(x) :=
(f (x),v ) ∈ R, x ∈M , is C∞ for any v ∈L+,J
λ , and denote the corresponding real vector space by
C∞
c (M,L +,J
λ ). Given the decomposition f (x) = {f̺(x) ∈ L̺} , x ∈ M , we deﬁne the real vector
space
D+ := {f ∈C∞
c (M,L +,J
λ ) : f̺ ⁄= 0 for ﬁnite ̺ ∈λ} .
The representation (4.12) induces an action by invertible linear maps ,
G0 →GLD+ : fg(x) := g+
λf (x) , ∀f ∈ D + , g ∈G0 , x ∈M . (4.14)
Now, let us suppose that M has a spin structure (this is guaranteed for 4-dimensional globally
hyperbolic spacetimes, see [25] and related references). We cons ider the spinor bundle DM →M
(with ﬁbre C4 ), whose tensor product by L−
λ yields the bundle of Hilbert spaces D−
λM → M ,
D−
λM :=L−
λ ⊗DM . We have the direct sum decomposition
D−
λM ≃ ⊕ ̺(γ)=−1D̺M ,
where any D̺M := L̺ ⊗DM → M is a smooth vector bundle. Any section s : M → D−
λM
decomposes as s = {s̺ : M → D̺M } , and we say that s is C∞ whenever every s̺ is a C∞
7With symmetric we mean that if ̺ ∈λ then the same is true for the conjugate representation ̺ , whilst the term
separating indicates that for any g ⁄=g′ ∈G0 there is ̺ ∈λ such that ̺(g) ⁄=̺(g′) .
26
section. We denote the set of compactly supported, C∞ sections of D−
λM by S∞
c (M,D −
λM ) and
deﬁne
D− := {s ∈ S ∞
c (M,D −
λM ) : s̺ ⁄= 0 for ﬁnite ̺ ∈λ} ,
that is a complex vector space with action
G0 →GLD− : sg(x) := {g−
λ ⊗ 1}s(x) , ∀s ∈ D − , g ∈G0 , x ∈M . (4.15)
Lemma 4.4 (Existence of ﬁeld nets on hyperbolic spacetimes) . For any globally hyperbolic (spin)
manifold M and Z2 -graded group (G0,γ ), there are a Hilbert space H∗ with a faithful, strongly
continuous representationτ :G0 →UH ∗ , and a normal (τ (G0),τ (γ))-net of von Neumann algebras
F∗ on H∗ .
The proof of the previous Lemma is postponed to §A and is based on the construction of a
symplectic form on D+ and a scalar product on D− , that allow us to deﬁne, respectively,
• a selfadjoint Klein-Gordon ﬁeld φ(f ), f ∈ D + , on the Hilbert space Hφ
∗ ,
• a Dirac ﬁeld ψ(s), s ∈ D − , on the Hilbert space Hψ
∗ ,
and then deﬁne H∗ :=Hφ
∗ ⊗Hψ
∗ and F∗,a , a ∈ ∆, as the von Neumann algebra generated by
{eiφ(f ) ⊗ 1ψ , 1φ ⊗ψ(s) : f ∈ D + , s ∈ D − , supp (f ), supp (s) ⊆a} .
We now deﬁne the (compact) normalizer group
NλG0 := {V = ⊕̺V̺ ∈ULλ : V̺g̺V ∗
̺ ∈̺(G0) , ∀g ∈G0} .
Note that NλG0 acts by adjoint action on G0 and, since γ̺ = ±1 for any ̺ ∈λ, we have
VγλV ∗ =γλ , ∀V ∈NλG0 .
Moreover, any V ∈NλG0 splits as V =V + ⊕V − , V ± ∈UL ±
λ .
Theorem 4.5. Let M denote a globally hyperbolic (spin) manifold and (G0,γ ) a Z2 -graded group.
Given a symmetric, separating set λ for G0 and a morphism
χ :π1(M ) →NλG0 ,
there is a Z2 -graded net of C*-algebras F = (F, )∆ endowed with:
1. A Hilbert net bundle (H,U )∆ carrying a normal representation (π,U ) of F;
2. A gauge action G ×∆ π(F) →π(F) with ﬁxed-point net R causally represented on (H,U )∆ ,
where G = (G, ˆı)∆ is the group net bundle with ﬁbre G0 and holonomy adχ.
Proof. With the notation of the previous Lemma we deﬁne G∗ :=τ (G0) ⊂UH ∗ . So ( G∗,τ (γ)) is
a Z2 -group on H∗ , and by the previous Lemma we have a normal ( G∗,τ (γ))-net of von Neumann
algebras F∗ on H∗ . Now, by Lemma 4.1, to prove the Theorem it suﬃces to show that th e unitary
representation τ of the previous Lemma extends to a unitary representation τ of NλG0 taking
values in Nτ (γ)G∗ , in fact in such a case we would have the morphism τ ◦χ :π1(M ) →Nτ (γ)G∗ .
But the construction of the desired representation is easy, in fac t it suﬃces to deﬁne the actions
{ fV (x) := V +f (x) , ∀x ∈M , f∈ D +
sV (x) := {V − ⊗ 1}s(x), ∀x ∈M , s∈ D − , V ∈NλG0 ,
27
that yield, by universality of the CCRs and CARs, the desired extens ion τ fulﬁlling
τV {eiφ(f ) ⊗ 1ψ}τ ∗
V = eiφ(fV ) ⊗ 1ψ , τV {1φ ⊗ψ(s)}τ ∗
V = 1 φ ⊗ψ(sV ) .
The veriﬁcations that τ (NλG0) ⊆Nτ (γ)G∗ now are trivial (see (4.3)) and the Theorem is proved.
