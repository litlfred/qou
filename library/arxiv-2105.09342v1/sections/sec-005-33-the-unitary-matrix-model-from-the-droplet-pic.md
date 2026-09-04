---
doc_id: arxiv-2105.09342v1
doc_title: "A Unitary Matrix Model for q-deformed Plancherel Growth"
section_id: sec-005-33-the-unitary-matrix-model-from-the-droplet-pic
section_title: "The unitary matrix model from the droplet picture"
section_number: 3.3
pages: 12-15
source_pdf: 2105.09342v1.pdf
source_sha256: 57ae12327da7b9a1
doc_brief: "A Unitary Matrix Model for q-deformed Plancherel Growth — In this paper we construct a unitary matrix model that captures the asymptotic growth of Young diagrams under q-deformed Plancherel measure."
---
In order to give a Hilbert space description of the q-deformed growth process we need to
ﬁnd a UMM whose large N phase can capture the growth of Young diagrams. For ordinary
Plancherel growth it was shown in [1] that using the Frobenius formula one can write the
partition function as GWW model. In case ofq-deformed Plancherel growth (3.3), it is tricky
to use the Frobenius formula for q-deformed dimension. So, we take a diﬀerent route. We
12
use the droplet picture [6, 8] to ﬁnd the UMM that captures the asymptotic growth of Young
diagrams under q-deformed Plancherel measure. Eynard [2] also gave a matrix model for q-
deformed Plancherel growth. The partition function was given by an integral over hermitian
matrices with eigenvalues running over a circle of some speciﬁed radius. Similar connection
was also pointed out in [20]. Here, we explicitly ﬁnd the unitary matrix model.
It was ﬁrst observed in [6] and subsequently by [1, 8, 21] that the large N phases of a
generic UMM (known as single plaquette model), given by
Z =
∫
[DU] exp
[
N
∞∑
n=1
βn
n
(
TrUn + TrU†n)
]
, (3.31)
can be described in two diﬀerent but equivalent ways - in terms of eigenvalue distribution
and Young diagram distribution 2. Diﬀerent large N phases can be characterised by both
eigenvalue density and Young diagram distribution. Therefore, it is expected that there is
a relation between these two descriptions. The relation is given by [8]
h2− 2S(θ)h +S2(θ)−π2ρ2(θ) = 0 (3.32)
where
S(θ) = 1
2 +
∑
n
βn cosnθ. (3.33)
The relation (3.32) allows us to provide a phase space picture for diﬀerent large N phases
of UMM in terms of free fermi droplets (two dimensional distributions). These distribu-
tions/droplets are similar to Thomas-Fermi distributions. Equation (3.32) has two possible
solutions, h±(θ) given by
h±(θ) =S(θ)±πρ(θ). (3.34)
Using this relation, one can deﬁne a distribution ω(h,θ ) in a two dimensional plane spanned
by (h,θ )
ω(h,θ ) = Θ
((h−h−(θ))(h+(θ)−h)
2
)
(3.35)
such that the eigenvalue distribution can be obtained by integrating out h for a given θ
ρ(θ) = 1
2π
∫
dh ω(h,θ ) = h+(θ)−h−(θ)
2π . (3.36)
The distribution also satisﬁes the normalisation condition
1
2π
∫
dh dθ ω(h,θ ) = 1. (3.37)
2It is well known that eigenvalues of unitary matrices behave like position of free fermions [22] and the
hook lengths of Young diagrams are like momenta of these fermions [6, 23].
13
The function S(θ) can also be written in terms of phase space geometry as following
S(θ) = 1
2πρ
∫ ∞
0
dh h ω(h,θ ) = h+(θ) +h−(θ)
2 . (3.38)
Integratingω(h,θ ) over θ for a given h, one obtains a distribution of hook numbers h
u(h) = 1
2π
∫
dθ ω(h,θ ) with
∫
dh u(h) = 1. (3.39)
Ifω(h,θ ) has a single boundary for a given h andθ >0, then there is another identiﬁcation
between eigenvalueθ and the Young diagram density
πu(h) =θ. (3.40)
In general, it is diﬃcult to ﬁnd the Young diagram distributions for diﬀerent large N phases
of (3.31). However using the droplet picture one can obtain the dominant representations
in the large N limit for diﬀerent phases of (3.31) [8].
Contrary to [8], here we know the large N phases of (3.3) in terms of dominant Young
diagrams. Our goal is to ﬁnd the corresponding eigenvalue distribution and hence the UMM.
From the Young diagram distribution of automodel class (3.25), we see thatu(h) is a smooth
function of h. Inverting the relation, we ﬁnd that h and θ (using 3.40) satisfy
h = 1− 1
λ log
[
1− 2λξ cosθ +λ2ξ2]
. (3.41)
Comparing this with (3.36) and (3.38), we have
S(θ) =πρ(θ) = h+(θ)
2 = 1
2− 1
2λ log
[
1− 2λξ cosθ +λ2ξ2]
= 1
2 +
∞∑
n=1
ξnλn−1
n cosnθ
(3.42)
and
h−(θ) = 0. (3.43)
Now, comparing (3.42) with (3.33), we get
βn = ξnλn−1
n . (3.44)
In order to complete the story, we note that the regularised partition function (3.3)
admits a phase transition in the large N limit at
ξ = 1
λ(eλ/2− 1). (3.45)
14
Forξ > 1
λ(eλ/2− 1), the Young diagram density does not saturate the upper bound and is
given by (see Appendix A for derivation)
u(h) = 1
π cos−1
[1 +eλe−2λh− 2eλ/2e−λh(1 +λξ) +λξ(2e−λh +λξ)
2λ(1−e−λh)ξ
]
. (3.46)
We need to conﬁrm that the dictionary (3.36) and (3.38) renders the same UMM in this
phase of the theory. Inverting (3.46), we see that there exist two possible solutions for h
for a given πu(h) = θ. It is easy to check using (3.38) that we obtain the same S(θ) (see
Appendix A for details). Thus, we conclude that the asymptotic (large N) structure of the
q-deformed partition function (3.3) is captured by a UMM (3.31) with βn given by (3.44).
The q-deformed growth of Young diagrams is captured by the no-gap phase of this UMM.
