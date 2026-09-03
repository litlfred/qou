---
doc_id: arxiv-0908.3425v1
doc_title: "Chiral Perturbation Theory: Introduction and Recent Resul ts in the One-Nucleon Sector S. Scherer"
section_id: sec-017-application-to-qcd
section_title: "Application to QCD"
section_number: null
pages: 22-25
source_pdf: 0908.3425v1.pdf
source_sha256: 5e88d45bbc1c1b9b
doc_brief: "Chiral Perturbation Theory: Introduction and Recent Resul ts in the One-Nucleon Sector S. Scherer — We provide an introduction to the basic concepts of chiral pe rturbation theory and discuss some"
---
The symmetry groups relevant to the application in QCD are
G = SU(N) × SU(N) = {(L,R )|L ∈ SU(N),R ∈ SU(N)} and H = {(V,V )|V ∈ SU(N)} ∼= SU(N).
Let ˜g = ( ˜L, ˜R) ∈ G. We characterize the left coset ˜ gH through the SU( N) matrix U = ˜R ˜L†
[Balachandran et al., 1991] such that ˜gH = (
/BD , ˜R ˜L†)H. This corresponds to the convention of choosing
as the representative of the coset the element which has the u nit matrix in its ﬁrst argument. The
transformation behavior of U under g = (L,R ) ∈G is obtained by multiplication in the left coset:
g˜gH = (L,R ˜R ˜L†)H = ( /BD ,R ˜R ˜L†L†)(L,L )H = ( /BD ,R ( ˜R ˜L†)L†)H,
i.e.
U = ˜R ˜L† ↦→U ′ =R( ˜R ˜L†)L† =RUL †. (84)
22
As mentioned above, we need to introduce an x dependence to account for the fact that we are dealing
with ﬁelds:
U(x) ↦→RU (x)L†. (85)
For the physically relevant cases the corresponding unitar y matrices may be parameterized as
U(x) = exp
(
iφ(x)
F0
)
, (86)
where, for N = 2,
φ =
3∑
i=1
φiτi ≡
(
π0 √
2π+
√
2π− −π0
)
(87)
and, for N = 3,
φ =
8∑
a=1
φaλa ≡




π0 + 1
√
3η
√
2π+ √
2K +
√
2π− −π0 + 1√
3η
√
2K 0
√
2K − √
2 ¯K 0 − 2√
3η



. (88)
The origin φ(x) = 0, i.e. U0 =
/BD , denotes the ground state of the system. Under transformati ons of
the subgroup H = {(V,V )|V ∈ SU(N)} corresponding to rotating both left- and right-handed quar k
ﬁelds in QCD by the same V , the ground state remains invariant,
U0 ↦→VU 0V † =VV † = /BD =U0.
On the other hand, under “axial transformations,” i.e. rota ting the left-handed quarks by A and the
right-handed quarks by A†, the ground state does not remain invariant,
U0 ↦→A†U0A† =A†A† ⁄=U0,
which is consistent with the assumed spontaneous symmetry b reakdown.
The traceless and Hermitian matrices of Eqs. (87) and (88) co ntain the Goldstone boson ﬁelds.
We want to discuss their transformation behavior under the s ubgroup H = {(V,V )|V ∈ SU(N)}.
Expanding
U = /BD +iφ
F0
− φ2
2F 2
0
+ · · ·,
we immediately see that the transformation behavior of Eq. ( 85) restricted to the subgroup H,
/BD +iφ
F0
− φ2
2F 2
0
+ · · · ↦→V (/BD +i φ
F0
− φ2
2F 2
0
+ · · ·)V † = /BD +iVφV †
F0
− VφV †VφV †
2F 2
0
+ · · ·,
implies
φ ↦→VφV †. (89)
However, this corresponds exactly to the fact that the Golds tone bosons transform according to the
adjoint representation under SU(3) V , i.e. they transform as an octet.
For group elements of G of the form ( A,A †) one may proceed in a completely analogous fashion.
However, one ﬁnds that the ﬁelds φa do not have a simple transformation behavior under these group
elements.
23
3.2 Eﬀective Lagrangian and power-counting scheme
The application of eﬀective ﬁeld theory (EFT) to strong inte raction processes has become one of the most
important theoretical tools in the low-energy regime. The b asic idea consists of writing down the most
general possible Lagrangian, including all terms consistent with assumed symmetry principles, and the n
calculating matrix elements with this Lagrangian within so me perturbative scheme [Weinberg, 1979].
A successful application of this program thus requires two m ain ingredients:
(1) A knowledge of the most general eﬀective Lagrangian;
(2) an expansion scheme for observables in terms of a consist ent power-counting method.
3.2.1 The lowest-order eﬀective Lagrangian
In terms of the SU(3) matrix U(x) of Eqs. (86) and (88) the most general, chirally invariant, eﬀective
Lagrangian with the minimal number of derivatives reads
Leﬀ = F 2
0
4 Tr
(
∂µU∂ µU †
)
, (90)
where F0 ≈ 93 MeV is a free parameter which later on will be related to the pion decay π+ →
µ+νµ. Because of the trace property Tr( AB) = Tr(BA), the Lagrangian is invariant under the global
SU(3)L × SU(3)R transformation U ↦→RUL † of Eq. (85). The global U(1) V invariance is trivially
satisﬁed, because the Goldstone bosons have baryon number z ero, thus transforming as φ ↦→φ under
U(1)V which also implies U ↦→U.
The substitution φa(t,⃗ x) ↦→ −φa(t,⃗ x) or, equivalently, U(t,⃗ x) ↦→U †(t,⃗ x) provides a simple method
of testing, whether an expression is of so-called even or odd intrinsic parity, i.e., even or odd in the
number of Goldstone boson ﬁelds. For example, the Lagrangia n of Eq. (90) is even. Since the Goldstone
bosons of QCD are pseudoscalars, the true parity transforma tion is given by φa(t,⃗ x) ↦→ −φa(t, −⃗ x) or,
equivalently,U(t,⃗ x) ↦→U †(t, −⃗ x).
The purpose of the multiplicative constant F 2
0/4 in Eq. (90) is to generate the standard form of
the kinetic term 1
2∂µφa∂µφa, which can be seen by expanding the exponential U = /BD +iφ/F0 + · · ·,
∂µU =i∂µφ/F0 + · · ·, resulting in
Leﬀ = F 2
0
4 Tr
[
i∂µφ
F0
(
−i∂µφ
F0
)]
+ · · · = 1
4∂µφa∂µφbTr(λaλb) + · · · = 1
2∂µφa∂µφa + Lint,
where we made use of Tr( λaλb) = 2δab. Since there are no other terms containing only two ﬁelds, th e
eight ﬁelds φa indeed describe eight independent massless particles.
There are no other independent, chirally invariant terms co ntaining only two derivatives. A term of
the type Tr[(∂µ∂µU)U †] may be re-expressed as
Tr[(∂µ∂µU)U †] = ∂µ[Tr(∂µUU †)] − Tr(∂µU∂ µU †),
i.e., up to a total derivative it is proportional to the Lagra ngian of Eq. (90). However, in the present
context, total derivatives do not have a dynamical signiﬁca nce, i.e. they leave the equations of motion
unchanged and can thus be dropped. The product of two invaria nt traces is excluded at lowest order,
because Tr(∂µUU †) = 0.
Let us turn to the vector and axial-vector currents associat ed with the global SU(3) L × SU(3)R
symmetry of the eﬀective Lagrangian of Eq. (90). To that end, we parameterize
L = /BD −iǫL
a
λa
2 , (91)
R = /BD −iǫR
a
λa
2 . (92)
24
In order to construct J µ
aL, set ǫR
a = 0 and choose ǫL
a =ǫL
a (x). Using
U †U =
/BD ⇒ ∂µ(U †U) = 0 ⇒ ∂µU †U = −U †∂µU, (93)
the variation of the Lagrangian can be brought into the form
δLeﬀ = F 2
0
4 i∂µǫL
a Tr
(
λa∂µU †U
)
.
Applying the method of Ref. [Gell-Mann and L´ evy, 1960], we o btain for the left currents
J µ
aL = ∂δLeﬀ
∂∂µǫL
a
=iF 2
0
4 Tr
(
λa∂µU †U
)
, (94)
and, completely analogously, choosing ǫL
a = 0 and ǫR
a =ǫR
a (x), for the right currents
J µ
aR = ∂δLeﬀ
∂∂µǫR
a
= −iF 2
0
4 Tr
(
λaU∂ µU †
)
. (95)
Combining Eqs. (94) and (95) the vector and axial-vector cur rents read
J µ
aV = J µ
aR +J µ
aL = −iF 2
0
4 Tr
(
λa[U,∂ µU †]
)
, (96)
J µ
aA = J µ
aR −J µ
aL = −iF 2
0
4 Tr
(
λa{U,∂ µU †}
)
. (97)
Furthermore, because of the symmetry of Leﬀ under SU(3) L × SU(3)R, both vector and axial-vector
currents are conserved. Using the substitution U ↔U † and Eq. (93), the vector current densities J µ
aV
of Eq. (96) contain only terms with an even number of Goldston e bosons and the axial-vector current
densitiesJ µ
aA of Eq. (97) only terms with an odd number of Goldstone bosons. To ﬁnd the leading term
let us expand Eq. (97) in the ﬁelds,
J µ
aA = −iF 2
0
4 Tr
(
λa
{
/BD + · · ·, −iλb∂µφb
F0
+ · · ·
})
= −F0∂µφa + · · ·.
We conclude that the axial-vector current has a non-vanishi ng matrix element when evaluated between
the vacuum and a one-Goldstone boson state:
⟨0|J µ
aA(x)|φb(p)⟩= ⟨0| −F0∂µφa(x)|φb(p)⟩= −F0∂µ exp(−ip ·x)δab =ipµF0 exp(−ip ·x)δab. (98)
Equation (98) is the manifestation of Eq. (81) at lowest orde r in the eﬀective ﬁeld theory.
