---
doc_id: arxiv-hep-ph-9502366v1
doc_title: "Chiral Perturbation Theory"
section_id: sec-017-10-large-nc-limit-u1a-anomaly-and-strong-cp-viol
section_title: "Large-NC limit, U(1)A anomaly and strong CP violation"
section_number: 10
pages: 42-45
source_pdf: 9502366v1.pdf
source_sha256: 56df064956ca03f8
toc_source: inferred
doc_brief: "Chiral Perturbation Theory — An introduction to the basic ideas and methods of Chiral Perturbation Theory is presented."
---
In the large-NC limit the U(1)A anomaly (Adler 1969, Adler and Bardeen 1969,
Bell and Jackiw 1969) is absent.
The massless QCD Lagrangian (2.1) has then a
larger U(3)L⊗U(3)R chiral symmetry, and there are nine Goldstone bosons associated
with the SCSB to the diagonal subgroup U(3)V . These Goldstone excitations can be
conveniently collected in the 3 × 3 unitary matrix
eU(φ) ≡⟨0| eU|0⟩U(φ) ≡⟨0| eU|0⟩exp
n
i
√
2eΦ/f
o
,
eΦ ≡η1
√
3
I3 +⃗
λ
√
2⃗
φ ,
(10.1)
where we have explicitly factor out from the eU(φ) matrix its vacuum expectation
value. Under the chiral group, eU(φ) transforms as eU →gR eUg†
L
(gR,L ∈U(3)R,L).
To lowest order in the chiral expansion, the interactions of the nine Goldstone bosons
are described by the Lagrangian (3.17) with eU(φ) instead of U(φ). Notice that the η1
kinetic term in ⟨Dµ eUDµ eU †⟩decouples from the φ’s and the η1 particle becomes stable
in the chiral limit (Di Vecchia et al 1981).
To lowest non-trivial order in 1/NC, the chiral symmetry breaking eﬀect induced
by the U(1)A anomaly can be taken into account in the eﬀective low-energy theory,
through the term (Di Vecchia and Veneziano 1980, Witten 1980, Rosenzweig et al
1980)
LU(1)A = −f 2
4
a
NC
 i
2
h
log (det eU) −log (det eU †)
i2
,
(10.2)
which breaks U(3)L⊗U(3)R but preserves SU(3)L⊗SU(3)R⊗U(1)V . The parameter a
has dimensions of mass squared and, with the factor 1/NC pulled out, is booked to be
of O(1) in the large-NC counting rules. Its value is not ﬁxed by symmetry requirements
alone; it depends crucially on the dynamics of instantons. In the presence of the term
(10.2), the η1-ﬁeld becomes massive even in the chiral limit: Mη2
1 = 3a/NC + O(M).
Deeply related to the U(1)A anomaly is the possible presence of an additional term
in the QCD Lagrangian,
Lθ = θ0
g2
64π2 ǫµνρσ Gµν
a (x)Ga,ρσ(x) ,
(10.3)
with θ0, the so-called vacuum angle, a hitherto unknown parameter.
This term
violates P, T and CP and may lead to observable eﬀects in ﬂavour conserving
transitions. Owing to the U(1)A-anomaly, the θ0-vacuum is not invariant under U(1)A
transformations, gR = g†
L = eiβI3 (Nf = 3 is the number of light-quark ﬂavours):
θ0 −→θ0 −2Nfβ .
(10.4)
To simplify the discussion, let us ﬁx the external scalar and pseudoscalar ﬁelds
in (3.10) to the values s = f
M and p = 0, where f
M denotes the full mass matrix
emerging from the Yukawa couplings of the light quarks in the electroweak sector. In
full generality, f
M is non-diagonal and non-Hermitian. However, with the help of an
appropriate SU(3)L ⊗SU(3)R transformation one can always restrict f
M to the form
f
M = exp
 i
3 arg(det f
M)

M ,
(10.5)
with M the diagonal (and positive-deﬁnite) quark-mass matrix (3.12). The phase
arg(det f
M) could be reabsorbed by a simple U(1)A rotation of the quark ﬁelds;
however,
because of the U(1)A-anomaly, the U(1)A rotation which eliminates
arg(det f
M) from the mass term generates a new θ0-vacuum
θ ≡θ0 + arg(det f
M) .
(10.6)
The combination θ remains invariant under arbitrary U(1)A transformations.
In order to analyze the implications of the θ term on the eﬀective chiral theory,
it is convenient to put the full θ-dependence on the quark-mass matrix. Performing
an appropriate chiral transformation, we can eliminate the term (10.3) from the QCD
Lagrangian, and write the mass matrix in the form f
M = exp {iθ/3} M.
In the
absence of the anomaly term (10.2), the θ phase could be reabsorbed by the U(1)A
transformation
eU −→eiθ/6 eU eiθ/6 .
(10.7)
In the presence of the U(1)A anomaly, and hence the term (10.2), this transformation
generates new physical interactions:
L2 + LU(1)A = f 2
4 ⟨Dµ eUDµ eU †⟩−V ( eU) ,
(10.8)
V ( eU) = −f 2
4


⟨eχ† eU + eU †eχ⟩−
a
NC
(
i
2
"
log
 
det eU
det eU †
!#
−θ
)2

,
(10.9)
where now the matrix eχ = 2 eB0M ≡diag(eχ2
u, eχ2
d, eχ2
s) is real, positive and diagonal.
If the term proportional to a/NC were absent, we could take without loss of
generality ⟨0| eU|0⟩= 1 and the diagonal entries eχ2
i would correspond to the Goldstone
boson masses.
In the presence of the anomaly, however, we should minimize the
potential energy V ( eU) in order to ﬁx ⟨0| eU|0⟩.
With eχ diagonal, ⟨0| eU|0⟩can be
restricted to be diagonal as well and of the form
⟨0| eU|0⟩= diag(e−iϕu, e−iϕd, e−iϕs) .
(10.10)
The minimization conditions ∂V/∂ϕi = 0 restrict the ϕi’s to satisfy the Dashen
(1971)–Nuyts (1971) equations:
eχ2
i sin ϕi =
a
NC
 
θ −
X
j
ϕj
!
≡
a
NC
¯θ ,
(i = u, d, s).
(10.11)
The ϕi’s appearing in the eﬀective Lagrangian can be reabsorbed in Hermitian matrices
χ and H deﬁned by
⟨0| eU †|0⟩eχ ≡χ + iH ,
eχ† ⟨0| eU|0⟩≡χ −iH .
(10.12)
Equations (10.11) ﬁx H to be proportional to the unit matrix: H =
a
NC ¯θ I3.
The eﬀective bosonic Lagrangian as a functional of U(φ), with ⟨0|U|0⟩= 1, is then
(Pich and de Rafael 1991b):
L2 + LU(1)A = f 2
4

⟨DµUDµU † + χ(U + U †)⟩−
a
NC
(
¯θ2 −1
4

log
 det U
det U †
2)
−i a
NC
¯θ

⟨U −U †⟩−log
 det U
det U †

.
(10.13)
The diagonalization of the quadratic piece of the Lagrangian gives rise to the
physical ﬁelds. In the isospin limit (mu = md = ˆm), only the η1 and η8 mix:
η = η8 cos θP −η1 sin θP ,
η′ = η8 sin θP + η1 cos θP .
(10.14)
From the measured pseudoscalar-mass spectrum, one can get the values of the mixing
angle and the parameter a: θP ≈−20◦, a = M 2
η + M 2
η′ −2M 2
K = 0.726 GeV2. Since
eχ2
u, eχ2
d ≪eχ2
s, a/NC and ˆm ≪ms, equations (10.11) imply the approximate relation
a
NC
¯θ ≈
θ
P
i eχ−2
i
+ Nc/a ≈1
2M 2
πθ .
(10.15)
The last term in (10.13) generates strong CP-violating transitions between
pseudoscalar particles.
In particular it induces the phase-space allowed decays
η1,8 →ππ.
Comparing the prediction Br(η →π+π−) = 1.8 × 102 θ2 with the
present experimental upper bound, Br(η →π+π−) < 1.5 × 10−3, one gets the limit
|θ| < 3 × 10−3 (Pich and de Rafael 1991b).
