---
doc_id: arxiv-2010.12819v2
doc_title: "The action of the Virasoro algebra in quantum spin chains. I. The non-rational case"
section_id: sec-046-g-the-ordinary-xxz-case
section_title: "G The ordinary XXZ case"
section_number: null
pages: 55-55
source_pdf: 2010.12819v2.pdf
source_sha256: ddc0493d60d48e77
toc_source: outline
doc_brief: "The action of the Virasoro algebra in quantum spin chains. I. The non-rational case — We investigate the action of discretized Virasoro generators, built out of generators of the lattice"
---
Going back to the bosonization in section 3.2, we can note that if we deﬁned more general local interactions,
replacing the factor i sinγ
2 byiλ in (18), we would obtain the twist
Tλ =−1
4 : (∂ϕ)2 : +i 2λ
sinγα0∂2ϕ (201)
and the central charge
cλ = 1− 96α2
0
λ2
sinγ2 . (202)
We can use this additional freedom to explore the “ordinary” XXZ case, which we shall deﬁne shortly, in terms
of a unitary c = 1 CFT, and to interpolate between this CFT and the c = 1− 6
x(x+1) CFT described above.
We now describe what we mean by the “ordinary” XXZ case. In this setting we forget for a moment the
Temperley-Lieb algebra, and remove the telescoping terms in the deﬁnition of the Hamiltonian density. We
consider instead the XXZ Hamiltonian as a sum of diﬀerent local, Hermitian interactions. Based on (55) we
deﬁne
hXXZ
j =− γ
π sinγfj, (203)
where we recall that
fj =−σ−
j σ+
j+1−σ+
j σ−
j+1− cosγ
2 σz
jσz
j+1 + cosγ
2 . (204)
We can once more consider twisted boundary conditions parametrized by φ, “smeared out” over all N sites for
numerical convenience. Written out explicitly we ﬁnd
fj =... ⊗ 1⊗


0 0 0 0
0 q+q−1
2 −eiφ/N 0
0 −e−iφ/N q+q−1
2 0
0 0 0 0

⊗ 1⊗.... (205)
By the same reasoning as in Section 2.4 we next introduce a momentum operator
PXXZ =−i
( γ
π sinγ
)2 N∑
j=1
[fj,fj+1] (206)
with a lattice momentum density pXXZ
j =i[hXXZ
j , hXXZ
j−1 ] = −i
( γ
π sinγ
)2
[fj−1,fj]. This leads to the following
alternative discretization of the Virasoro generators:
LXXZ
n = L
4π

− γ
π sinγ
L∑
j=1
einj2π/L
(
fj−e∞ + iγ
π sinγ [fj,fj+1]
)
 + 1
24δn0, (207a)
¯LXXZ
n = L
4π

− γ
π sinγ
L∑
j=1
e−inj2π/L
(
fj−e∞− iγ
π sinγ [fj,fj+1]
)
 + 1
24δn0. (207b)
Notice that in these expressions we have used the value c = 1 for the central charge, irrespective of x.
