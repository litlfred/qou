---
doc_id: arxiv-2010.12819v2
doc_title: "The action of the Virasoro algebra in quantum spin chains. I. The non-rational case"
section_id: sec-039-c11-considerations-at-level-2
section_title: "C.1.1 Considerations at level 2"
section_number: null
pages: 44-45
source_pdf: 2010.12819v2.pdf
source_sha256: ddc0493d60d48e77
toc_source: outline
doc_brief: "The action of the Virasoro algebra in quantum spin chains. I. The non-rational case — We investigate the action of discretized Virasoro generators, built out of generators of the lattice"
---
At level 2 we typically expect two orthogonal states, which we call |w1⟩ and|w2⟩. To get the total projection
onto level 2 we consider
|χ|2≡
√
|⟨w1|χ⟩|2 +|⟨w2|χ⟩|2 (176)
and same for the anti-chiral quantities. In the case of degenerate conformal weights we furthermore again have
the issue of overlap, so that we once again must take into account twice as many states. However, the fourth
state is a singular Bethe state, so we do not include it in our form-factor computations to avoid regularization.
We label the norms with and without this fourth state as
|χ|∗
2 ≡
√
|⟨w1|χ⟩|2 +|⟨w2|χ⟩|2 +|⟨w3|χ⟩|2 +|⟨w4|χ⟩|2, (177a)
|χ|∗∗
2 ≡
√
|⟨w1|χ⟩|2 +|⟨w2|χ⟩|2 +|⟨w3|χ⟩|2. (177b)
We show the result for |χ|∗
2 obtained from exact diagonalization in Table 5 at Sz = 2,e = 1, before restricting
to|χ|∗∗
2 when going to higher sizes with form factors.
When using form factors, we need to know what conjecture to consider when we exclude the fourth, singular
Bethe state. It turns out that the second and third Bethe states, which are found in a degenerate eigenspace of
the Hamiltonian, have an almost zero contribution to the norm (or order O(10−3), respectively O(10−5), when
extrapolating the form-factor results). Meanwhile the ﬁrst and fourth states are at diﬀerent energies, and so by
the same argument as for level 1 (i.e., that we cannot favour chiral over anti-chiral, and so their energy must be
44
the same) we expect that the two Bethe states contribute equally. Excluding the fourth state will thus roughly
remove half the norm squared at Sz = 2,e = 1, up to the O(10−3) contribution from the second and third
states. Meanwhile, when we consider the chiral side at Sz = 2,e =−1 the conjecture simply remains zero.
N |χ|∗
2 Full norm
10 0.45377412 0.45904775
12 0.47363006 0.47883132
14 0.48751301 0.49234698
16 0.4976002 0.50267043
18 0.50516327 0.51126303
20 0.51098601 0.51895827
22 0.51557136 0.52628211
p5 0.54746072 0.84670007
p6 0.54780548 1.02083064
conj 0.54675127
Table 5: Norm at level 2 in the case of overlap. Shown is projection onto the four relevant states. In the right
column is the full norm for comparison. The presence of parasitic couplings in the latter case leads to a diﬀerent
result, which moreover cannot be reliably extrapolated. The conventions used for the extrapolations p5 and p6
are the same as in Table 1.
