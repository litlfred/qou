---
doc_id: arxiv-0811.1338v1
doc_title: "Modern Theory of Nuclear Forces"
section_id: page-034
section_title: "Page 34"
section_number: null
pages: 34-34
source_pdf: 0811.1338v1.pdf
source_sha256: 9a57cb6e014d3ead
toc_source: undetermined
doc_brief: "Modern Theory of Nuclear Forces — 52 sections: Page 1; Page 2; Page 3"
---
Monte Carlo techniques, Hubbard-Stratonovich transfor-
mations, and non-local updating schemes such as a hy-
brid Monte Carlo. A third feature is the close theoretical
link between nuclear lattice simulations and chiral eﬀec-
tive ﬁeld theory. One can write down the lattice Feyn-
man rules and calculate lattice Feynman diagrams using
precisely the same action used in the non-perturbative
simulation. Since the lattice formalism is based on chi-
ral eﬀective ﬁeld theory we have a systematic power
counting expansion, an a priori estimate of errors for
low-energy scattering, and a clear theoretical connection
to the underlying symmetries of QCD. The ﬁrst studies
combining lattice methods with eﬀective ﬁeld theory for
low-energy nuclear physics looked at inﬁnite nuclear and
neutron matter at nonzero density and temperature (see
Sec. III.E). Most of the formalism for chiral EFT on the
lattice was developed in (379). Nuclear lattice simula-
tions were used to study the triton at leading-order in
pionless eﬀective ﬁeld theory with three-nucleon interac-
tions (380).
Let us brieﬂy discuss the principles underlying such
nuclear lattice simulations (for a detailed discussion, we
refer to Refs. (379; 381)). In this framework, nucleons
are represented as point-like Grassman-ﬁelds and pions
as point-like instantaneous pseudoscalar ﬁelds. The lat-
tice is deﬁned by a volume L3 × Lt, with L(Lt) the
spatial (temporal) size. The corresponding lattice spac-
ings are called a and at, respectively. Typically, calcu-
lations are carried out using a lattice length L ≃20 fm
and the lattice spacing a ≃2 fm which corresponds to
the cutoﬀΛ = π/a ≃300 MeV. At present, computa-
tional resources prevent one from using smaller lattice
sizes (larger UV cutoﬀs). Still, the use of various forms
of improved actions allows one to access the systematic
errors inherent in such simulations.
The basic quantity in nuclear lattice simulations is the
correlation function. For A nucleons in Euclidean space
it is deﬁned by
ZA(t) = ⟨ΨA| exp(−τH)|ΨA⟩,
(2.57)
where |ΨA⟩refers to a Slater determinants for A free nu-
cleons, H is the Hamiltonian of the system and τ the Eu-
clidean time. The ground state energy of the A-nucleon
system can be derived from the asymptotic behavior of
the correlation function for large τ,
E0
A = −lim
τ→∞
d
dτ ln ZA(τ).
(2.58)
The expectation value of any normal ordered operator O
can be derived in a similar way by
⟨Ψ0
A|O|Ψ0
A⟩=
lim
τ←∞
ZO
A (τ)
ZA(τ) ,
(2.59)
ZO
A (t) = ⟨ΨA| exp(−τH/2)O exp(−τH/2)|ΨA⟩,
where |Ψ0
A⟩denote the ground states of A-nucleon sys-
tem.
It is convenient to describe NN contact interac-
tions by standard bilinear nucleon density operators us-
ing the Hubbard-Stratonovich transformation. Using the
relation exp(ρ2/2) ∼
R
ds exp(−s2/2 −s ρ) one can ex-
press terms quadratic in the nucleon density operator ρ as
terms linear in ρ in the presence of auxiliary background
ﬁelds (collectively denoted by s). In this representation,
the full correlation function is related to the path integral
over pions and auxiliary ﬁelds,
ZA(t) = N
Z
Ds
Y
I=1,2,3
DπIDsI exp(−Sππ −Sss)
×⟨ΨA|M (Lt−1)(πI, s, sI) · · · M (0)(πI, s, sI)|ΨA⟩.
(2.60)
Here Sππ and Sss are free actions for pions and aux-
iliary ﬁelds s, sI (where s/sI couples to the isospin-
independent/dependent nucleon bilinear),
I
denotes
isospin indices and N is an (irrelevant) normalization
constant. M (n) is a transfer matrix deﬁned as an n’th
step in the temporal direction. We remark that the am-
plitude ⟨ΨA|M (Lt−1)(πI, si) · · · M (0)(πI, si)|ΨA⟩is just
a Slater determinant of single nucleon matrix elements
Mi,j with i, j = 1, . . . , A.
To be speciﬁc, we give here the leading order action
starting with the free theory. The presentation here is
somewhat sketchy. For an extensive discussion see (381).
The free actions for the auxiliary ﬁelds and the pions are
Sss(s, sI) = 1
2
X⃗
n
s(⃗n)2 + 1
2
3
X
I=1
X⃗
n
sI(⃗n)2 ,
Sππ(πI) = αt
2
3
X
I=1
X⃗
n
πI(⃗n)(−∆+ M 2
π)πI(⃗n) ,
(2.61)
where Mπ is the physical pion mass and αt = at/a.
For nucleons one may use an O(a4) improved free lat-
tice Hamiltonian deﬁned by
Hfree =
1
m
3
X
k=0
X⃗
ns,ˆls,i,j
fk

a†
i,j(⃗ns)(ai,j(⃗ns + kˆls)
+ai,j(⃗ns −kˆls))

,
(2.62)
where the operators a†
i,j(⃗ns) and ai,j(⃗ns) are the nucleon
creation and annihilation operators,⃗ns are spatial coor-
dinates, ˆls are spatial unit vectors, the indices i and j rep-
resent spin and isospin indices, respectively, and the co-
eﬃcients fk are f0,1,2,3 = 49/2, −3/4, 3/40, −1/180. To
deﬁne the interactions one introduces nucleon-density op-
erators with diﬀerent spin/isospin polarizations
ρa†,a(⃗ns) =
X
i,j
a†
i,j(⃗ns)ai,j(⃗ns),
ρa†,a
I
(⃗ns) =
X
i,j,j′
a†
i,j′(⃗ns)[τI]j′,jai,j(⃗ns),
(2.63)
ρa†,a
I,S (⃗ns) =
X
i,i′,j,j′
a†
i′,j′(⃗ns)[σS]i′,i[τI]j′,jai,j(⃗ns).
