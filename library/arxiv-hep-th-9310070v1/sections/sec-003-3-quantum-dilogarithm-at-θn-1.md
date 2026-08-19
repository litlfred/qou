---
doc_id: arxiv-hep-th-9310070v1
doc_title: "September, 1993 Quantum Dilogarithm"
section_id: sec-003-3-quantum-dilogarithm-at-θn-1
section_title: "Quantum Dilogarithm at θN = 1"
section_number: 3
pages: 5-8
source_pdf: 9310070v1.pdf
source_sha256: b979ebf2f47a4653
doc_brief: "September, 1993 Quantum Dilogarithm — A quantum generalization of Rogers’ ﬁve term, or “pentagon” dilogarithm identity is suggested. It is shown that the classical limit gives usua l Rogers’ identity."
---
When |θ| = 1, deﬁnition (1.4) of the quantum dilogarithm needs qualiﬁ cation because the
inﬁnite product is not convergent. In this section we restri ct ourselves to a particular case,
θN = 1, for some integer, N ≥ 2, and properly modify the formulae of Section 2.
Let θ = ω, where ω is a primitive N -th root of unity. We choose ω together with its
square root ω1/2 as
ω = exp(2πi/N), ω 1/2 = exp(πi/N). (3.1)
In this case, operators, satisfying algebra (2.1), can be re alized as N -by-N matrices, since
their N -th powers are the central elements. Let us ﬁx them equal to th e minus identity
operator :
ˆU N = −1, ˆV N = −1. (3.2a)
As a consequence of this choice we have also
(− ˆU ˆV )N = −1. (3.2b)
The spectrum of any operator, ˆA, whose N -th power is −1, is given by N distinct numbers
ωn−1/2, n = 0, 1, . . . , N − 1, (3.3)
so, all operators ˆU , ˆV , and − ˆU ˆV have one and the same spectrum (3.3). Index n in (3.3)
can be considered (mod N ), i. e. as an element of ZN .
Before speciﬁcation of the quantum dilogarithm, following [8], for complex variables
a, b, c, constrained by Fermat equation
aN + bN = cN , (3.4)
deﬁne the function
w(a, b, c|0) = 1 , w (a, b, c|n) =
n∏
j=1
b/(c − aωj), n ≥ 1, (3.5)
which depends on n only (mod N ) due to relation (3.4):
w(a, b, c|n + N ) = w(a, b, c|n). (3.6)
Quantum dilogarithm Ψ( ˆA), depending on an operator argument, ˆA with spectrum (3.3),
can be deﬁned as an operator, commuting with ˆA, and with spectrum given by
Ψ( ωn−1/2) = Ψ( ω−1/2)w(a, b, c|n), (3.7)
where Ψ( ω−1/2) is a non-zero complex factor to be speciﬁed later. Using deﬁ nition (3.7),
it is easy to derive the “functional” relation on Ψ( ˆA):
Ψ( ω−1 ˆA)Ψ( ˆA)−1 = (c − ω1/2a ˆA)/b, (3.8)
4
which completely determines operator Ψ( ˆA) up to a complex factor. Now, we formulate
our statement.
Theorem. The following “quantum pentagon ” identity holds :
Ψ( ˆV )Ψ ′( ˆU) = Ψ ′′( ˆU )Ψ ′′′(− ˆU ˆV )Ψ ′′′′( ˆV ), (3.9)
where Ψ # (# symbolizes any number of dashes from zero to four) are deﬁned by (3.8) with
a#, b#, c# satisfying (3.4), and
yy ′′ = y′y′′′′, y ′ = y′′y′′′, x ′′′ = xx′,
x′′ = x′y′′′′, x ′′′′ = xy′′, (3.10a)
for
x# = ω1/2a#/b#, y # = c#/b#. (3.10b)
To prove the theorem, note that the combination
Ψ ′′( ˆU )−1Ψ( ˆV )Ψ ′( ˆU )Ψ ′′′′( ˆV )−1 (3.11)
commutes with operator − ˆU ˆV , provided relations (3.10) hold. Therefore (3.11) is some
function of − ˆU ˆV . It is a simple task to show that this function satisﬁes (3.8) . So, relation
(3.9) holds up to some complex factor. The latter can be put to unity after the proper
choice of Ψ #(ω−1/2) in (3.7). In the case where detΨ #( ˆA) = 1, their N -th powers are
Ψ #(ω−1/2)N = (b#/c#)N(N+1)/2/H(a#/c#), (3.12)
where
H(x) = (1 − x)N
N−1∏
j=1
(1 − xωj)j. (3.13)
In the basis, where operator ˆU is diagonal, one can show that relation (3.9) is nothing
else but the restricted star-triangle relation introduced by Bazhanov and Baxter [8] (see
formulae (1.19), (1.20) in their paper).
Let us comment on what is the “classical” limit of (3.9). Clea rly, it should correspond
to N → ∞. Asymptotics (1.5) for the function (3.5) take the form:
w(a, b, c|m) =
√
1 − x
1 − xtm
exp( 1
ǫ [L2(xtm) − L2(x)])(1 + O(ǫ)), (3.14a)
where
ǫ = 2πi/N, x = a/b, |a| < |b|, (3.14b)
and
tm = lim
N→∞
ωm, m → ∞, m/N = ﬁxed . (3.14c)
5
To deﬁne the “symbol” of a ﬁnite dimensional operator, in ana logy with Section 2, con-
sider two basis sets {|n⟩}and {|m⟩}, n, m ∈ ZN , which diagonalize operators ˆU and ˆV ,
respectively:
⟨n| ˆU|n′⟩= ωn−1/2δn,n′ , ⟨n| ˆV |n′⟩= ω−1/2δn,n′+1, (3.15a)
⟨m| ˆV |m′⟩= ωm−1/2δm,m′, ⟨m| ˆU |m′⟩= ω−1/2δm,m′−1. (3.15b)
The scalar products are given by
⟨n|n′⟩= δn,n′ , ⟨n|m⟩= ω−nm, ⟨m|m′⟩= N δm,m′ , (3.16)
while the decompositions of the unit operator are
1 =
∑
n∈ZN
|n⟩⟨n| = 1
N
∑
m∈ZN
|m⟩⟨m|. (3.17)
The “U-V” symbol of an operator, ˆA, is deﬁned as a mixed matrix element
( ˆA)n,m = ⟨n| ˆA|m⟩
⟨n|m⟩ , (3.18)
the symbol of a product of ˆA and ˆB being
( ˆA ˆB)n,m = 1
N
∑
n′,m′∈ZN
ω−(n−n′)(m′−m)( ˆA)n,m′( ˆB)n′,m. (3.19)
Calculating the symbol of (3.9), we will have a direct analog for (2.16) with a double
sum instead of integrals. To apply the stationary phase meth od, we have to convert these
summations into integrals. For this purpose, ﬁrst let us wri te the following equality:
N−1∑
m=0
1
z − ωm = N
z(1 − z−N ) (3.20)
for any complex z. Then, using Cauchy’s formula and (3.20), we have with expon ential
accuracy
N−1∑
m=0
f (ωm) ∼ N
2πi
∮
S1
f (z) dz
z , N → ∞ (3.21)
for any function f (z). Repeating calculations from Section 2, using (3.21), one can show
that (3.9) in the limit N → ∞ is reduced to (1 .3b) as well.
6
Summary
In this paper we have shown that the quantum identity (2.4) fo r the function (1.4) with
operator arguments satisfying (2.1) in the classical limit is reduced to Rogers’ dilogarithm
identity (1.3). We used the “q-p” symbols (2.10), (2.12) of t he operators ˆU , ˆV , and − ˆU ˆV
to convert (2.4) into the integral identity (2.16), as well a s asymptotics (1.5), and the
stationary phase method to evaluate the integrals.
In Section 3 we proved another, ﬁnite dimensional counterpa rt of the quantized Rogers’
identity (3.9). The deformation parameter in this case is a r oot of unity θN = 1 for some
integer N ≥ 2. The quantum dilogarithm is a function on Fermat curve and i s given
explicitly by (3.4), (3.5), (3.7), and (3.12). The classica l limit of (3.9), corresponding to
N → ∞, also coincides with (1.3).
It is remarkable that the ﬁve term identity, which can be show n to be equivalent to
(3.9), but written in diﬀerent terms, has been found already by Bazhanov and Baxter [8].
They used it as a local integrability condition for three dim ensional statistical models. An
interesting question in connection with this is whether one can supply a three dimensional
interpretation for the quantum dilogarithm identity. In fa ct, the answer to this question
is aﬃrmative, and it will be the subject of a subsequent publi cation.
