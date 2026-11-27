---
doc_id: arxiv-2010.12819v2
doc_title: "The action of the Virasoro algebra in quantum spin chains. I. The non-rational case"
section_id: sec-043-d-proof-of-133
section_title: "D Proof of (133)"
section_number: null
pages: 49-50
source_pdf: 2010.12819v2.pdf
source_sha256: ddc0493d60d48e77
toc_source: outline
doc_brief: "The action of the Virasoro algebra in quantum spin chains. I. The non-rational case — We investigate the action of discretized Virasoro generators, built out of generators of the lattice"
---
We wish to prove (133b), from which (133a) then also follows thanks to the known result (132). Within this
Appendix, we let⟨O⟩ refer to the ground-state expectation value of an operator O in the limit N→∞ . Using
the parity of the ground state we can restate (133b) as
⟨ejej+1⟩ = 3 sin3γI 1− sinγI 0
cosγ . (182)
In [56] the following ground-state expectation values are given for spin operators Sa =σa/2, a=x,y,z :
⟨Sx
jSx
j+2⟩ = − 1
2π sin 2γI(0)− 3 cos 2γ tanγ
4π3 I(2) + cos 2γ
4π2 I(1) + sin2γ
4π4 I(3), (183a)
⟨Sz
jSz
j+2⟩ = 1
4 + cot 2γ
π I(0) + 3 tanγ
2π3 I(2)− 1
2π2I(1)− sin2γ
2π4 I(3), (183b)
⟨Sx
jSx
j+1⟩ = − 1
4π sinγI(0) + cosγ
4π2 I(1), (183c)
⟨Sz
jSz
j+1⟩ = 1
4 + cotγ
2π I(0)− 1
2π2I(1), (183d)
where we have introduced the short-hand notations
I(0) =
∫ ∞
−∞
sinh(1−ν)t
coshνt sinht dt, (184a)
I(1) =
∫ ∞
−∞
t cosht
cosh2νt sinht dt, (184b)
I(2) =
∫ ∞
−∞
t2 sinh(1−ν)t
coshνt sinht dt, (184c)
I(3) =
∫ ∞
−∞
t3 cosht
cosh2νt sinht dt, (184d)
with γ =πν. By comparison with (17) and (125) we see that I0 =I(0)/π and I1 =I(2)/π3.
Using the expression (18) of the Temperley-Lieb generators in terms of Pauli matrices we now rewrite
⟨ejej+1⟩ in terms of spin operators. We use σaσb =δab1 +iϵabcσc to simplify the products, and by symmetry
we may discard any resulting term that involves an odd number of any given spin operator. We obtain
4⟨ejej+1⟩ =
⟨(
σxσx
j+1 +σy
jσy
j+1 + cosγ
(
σz
jσz
j+1− 1
)
+i sinγ
(
σz
j−σz
j+1
))
(
σx
j+1σx
j+2 +σy
j+1σy
j+2 + cosγ
(
σz
j+1σz
j+2− 1
)
+i sinγ
(
σz
j+1−σz
j+2
))⟩
=⟨σx
jσx
j+2⟩ +⟨σy
jσy
j+2⟩ + cos2γ
(
⟨σz
jσz
j+2⟩ + 1
)
− cosγ
(
⟨σx
jσx
j+1⟩ +⟨σx
j+1σx
j+2⟩
)
− cosγ
(
⟨σy
jσy
j+1⟩ +⟨σy
j+1σy
j+2⟩
)
− cos2γ
(
⟨σz
jσz
j+1⟩ +⟨σz
j+1σz
j+2⟩
)
+ sin2γ
(
⟨σz
jσz
j+2⟩ + 1
)
− sin2γ
(
⟨σz
jσz
j+1⟩ +⟨σz
j+1σz
j+2⟩
)
.
(185)
Using translation invariance of the ground state and U(1) symmetry we rewrite this as
⟨ejej+1⟩ = 2⟨Sx
jSx
j+2⟩ +⟨Sz
jSz
j+2⟩ + 1
4− 4 cosγ⟨Sx
jSx
j+1⟩− 2⟨Sz
jSz
j+1⟩. (186)
Inserting the results from (183) we see immediately that the terms withI(3) cancel, as well as the terms involving
no integrals at all, leaving
⟨ejej+1⟩ =
(
−2 1
2π sin 2γ + cot 2γ
π + 4 cosγ 1
4π sinγ− 2cotγ
2π
)
I(0)
+
(
2cos 2γ
4π2 − 1
2π2− 4 cosγ cosγ
4π2 + 2 1
2π2
)
I(1)
+
(
−23 cos 2γ tanγ
4π3 + 3 tanγ
2π3
)
I(2).
(187)
By trigonometric identities we then see that the terms involving I(1) cancel as well, and that we ﬁnally obtain
⟨ejej+1⟩ = sinγ
π cosγI(0) + 3 sin3γ
π3 cosγI(2) = 3 sin3γI 1− sinγI 0
cosγ , (188)
proving (133).
49
D.1 The limit γ→ 0
In the limitx→∞, γ→ 0 we expect that the integrals in (133) can be expressed in terms of the polylogarithms
Li2n+1(−1), following the result for the XXX spin chain [57]
⟨Sz
jSz
j+1⟩ = 1
12− 1
3ζa(1), (189a)
⟨Sz
jSz
j+2⟩ = 1
12− 4
3ζa(1) +ζa(3), (189b)
here written in terms of the alternating zeta function
ζa(s) =
∑
n>0
(−1)n−1
ns =−Lis(−1). (190)
More precisely, as γ→ 0 (186) simpliﬁes to
⟨ejej+1⟩ = 3⟨Sz
jSz
j+2⟩ + 1
4− 6⟨Sz
jSz
j+1⟩, (191)
such that by inserting (189) we expect that (133b) can be written as
⟨ejej+1 +ej+1ej⟩ = 1
2
(
1− 2 + 8ζa(1) + 1− 16ζa(1) + 12ζa(3)
)
= 6ζa(3)− 4ζa(1). (192)
Comparing the rescaled integrals sin 2n−1γ In in the limit of x→∞ to the integral representation
− Lis(−1) = 1
Γ(s)
∫ ∞
0
ts−1
et + 1 dt (193)
we ﬁnd
sin2n−1γ In = 2sinn−1(γ)
γn−1
∫ ∞
0
t2n sinh(xt)
sinh((x + 1)t) cosh(t) dt = 4sin2n−1(γ)
γ2n−1
∫ ∞
0
t2n
e2t + 1
( 1−e−2xt
1−e−2(x+1)t dt
)
−−−−→
x→∞
4
22n+1
∫ ∞
0
t2n
et + 1 dt =− 4
22n+1 Γ(2n + 1)Li2n+1(−1). (194)
In particular sinγ I0→− 2Li1(−1) = 2ζa(1) and sin 3γ I1→− Li3(−1) =ζa(3), such that
⟨ejej+1 +ej+1ej⟩ = 6 sin3γ I1− 2 sinγ I0
cosγ −−−−→
γ→0
6ζa(3)− 4ζa(1) (195)
indeed.
