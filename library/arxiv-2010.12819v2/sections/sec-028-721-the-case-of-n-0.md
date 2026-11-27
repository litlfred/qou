---
doc_id: arxiv-2010.12819v2
doc_title: "The action of the Virasoro algebra in quantum spin chains. I. The non-rational case"
section_id: sec-028-721-the-case-of-n-0
section_title: "The case of n =0"
section_number: 7.2.1
pages: 29-32
source_pdf: 2010.12819v2.pdf
source_sha256: ddc0493d60d48e77
toc_source: outline
doc_brief: "The action of the Virasoro algebra in quantum spin chains. I. The non-rational case — We investigate the action of discretized Virasoro generators, built out of generators of the lattice"
---
We now turn back to the comparison between (116) and (117). The ﬁrst observation is that the right-hand-side
of (116) contains trigonometric functions of p/N,n/N while the right-hand side of (117) is linear in p,n . While
this discrepancy could, by itself, explain why (116)⁄↦→ (117), that is in fact not the case. Expanding the sinuses
in powers of their arguments (at ﬁxed p,n and with N large), it turns out that whenever n⁄= 0 the terms in
(116) that are subleading in the expansion fall oﬀ fast enough separately (this will not be the case at n = 0),
compared to the leading term (2 p +n)
{
2[ej, [ej+1,ej+2]] +√Q(ejej+1 +ej+1ej)
}
. The leading term by itself
goes as O(1/N2) since the whole right-hand side of (116) is a term of O(1). Since the subleading terms come
with prefactors 1/N2, 1/N4,... relative to this leading term, it is enough that [ej, [ej+1,ej+2]], (ejej+1 +ej+1ej)
and ej on their own have matrix elements that decay with N (i.e., being of order O(1/Nr) with r > 0). If
they furthermore decay faster than 1 /N (r >1) we may also ignore the subleading terms in the expansion of
exponentials in n/N, so that we may put all phase factors on the same form. Numerical results indicate that
this indeed holds: the case of n =−1 is shown in Figure 3, with slopes around r = 2, while the case of n =−2
29
Figure 3: Absolute value of matrix elements, plotted with logarithmically scaled axes for sizesN = 10, 12,..., 24.
A linear ﬁt is performed, excluding the lowest two sizes. The ﬁt indicates that the matrix elements decay as
O(1/Nr), where the estimated slope r is shown on each curve. The ground state |gs⟩ is given for the lattice
parameters Sz =e =eφ = p = 0. For the other choices of state |v⟩ any non-zero lattice parameter is speciﬁed,
with the others remaining zero. For each state |v⟩ the state |u⟩ corresponds to the same choice of lattice
parameters up to a change in momentum sector, p→ p + 1. The lowest energy state for each choice of lattice
parameters is used. The absolute values of the matrix elements are independent of j.
is shown in Figure 8 in Appendix E—here the ﬁnite size eﬀects are larger, but the results still indicate r >1.
Keeping terms of leading order only, we have
[Lp+n + ¯L−p−n, L−p− ¯Lp] = N
2π
( γ
π sinγ
)3{
(3p + 2n)
N∑
j=1
e2iπn(j+1)/N[ej, [ej+1,ej+2]]
+ (p +n)
√
Q
2L∑
j=1
e2iπn(j+1)/N(ejej+1 +ej+1ej)− 2p
N∑
j=1
e2iπn(j+1)/Nej
}
+ O
( 1
Nr−1
)
. (118)
We can now analyze the right-hand side by using a family of operators introduced in [1] as alternatives to the
basic generators L, ¯L14. From the expression of what is denoted ˆh(3) in KS (2.54) and using the result KS
(2.58)15 we have that
N
2π
( γ
π sinγ
)3 N∑
j=1
e2iπn(j+1)/N :2[ej, [ej+1,ej+2]] +
√
Q(ejej+1 +ej+1ej): ↦→
(
Ln + ¯L−n− c
12δn,0
)
, (119)
where normal-order notation here means that the average in the ground state has been subtracted. As discussed
at the beginning of this section, this normal ordering does not change the matrix elements when n⁄= 0, and we
shall use the left-hand side of (119) without normal ordering for the rest of this subsection.
14These alternatives were obtained by using the fact that all derivatives of the logarithm of the transfer matrix with respect to
the spectral parameter u at u = 0 produce terms converging, in the weak-scaling sense, to the Hamiltonian and momentum of the
associated CFT.
15Generalized to n⁄= 0 in the same way as in KS (3.33).
30
Grouping by p and n and dividing through by N
2π
(
γ
π sinγ
)3
we have from (118) the terms
2p
[
3
2
N∑
j=1
e2iπn(j+1)/N[ej, [ej+1,ej+2]] +
√Q
2
N∑
j=1
e2iπn(j+1)/Nejej+1 +ej+1ej−
N∑
j=1
e2iπn(j+1)/Nej
]
+n
[
2
N∑
j=1
e2iπn(j+1)/N[ej, [ej+1,ej+2]] +
√
Q
N∑
j=1
e2iπn(j+1)/Nejej+1 +ej+1ej
]
, (120)
from which we subtract
2p
[
2
N∑
j=1
e2iπn(j+1)/N[ej, [ej+1,ej+2]] +
√
Q
N∑
j=1
e2iπn(j+1)/Nejej+1 +ej+1ej
]
+n
[
2
N∑
j=1
e2iπn(j+1)/N[ej, [ej+1,ej+2]] +
√
Q
N∑
j=1
e2iπn(j+1)/Nejej+1 +ej+1ej
]
. (121)
We thus ﬁnd, thanks to (119), that in the scaling limit [ Lp+n + ¯L−p−n, L−p− ¯Lp] behaves asLn + ¯L−n (recall,
n⁄= 0 in this section) plus the following expression:
N
2π
( γ
π sinγ
)3
2p
[
− 1
2
N∑
j=1
e2iπn(j+1)/N[ej, [ej+1,ej+2]]
−
√Q
2
N∑
j=1
e2iπn(j+1)/Nejej+1 +ej+1ej−
N∑
j=1
e2iπn(j+1)/Nej
]
. (122)
In order to have (116)↦→ (117) atn⁄= 0, we need the matrix elements of (122) between any two relevant scaling
states (∆p =n) to tend to zero with N. As discussed in the beginning of this section, it suﬃces to evaluate a
single summand for a ﬁxed value of j. For this reason we deﬁne the remainder R at n⁄= 0 to be
R =−[ej, [ej+1,ej+2]]−
√
Q(ejej+1 +ej+1ej)− 2ej. (123)
In order for the matrix elements of (122) between scaling states to tend to zero with N, we need that matrix
elements of R be of O(1/Nr) for r strictly larger than 2. Results for n =−1 are shown in Figure 4, while
results for n =−2 are shown in Figure 9 in Appendix E. These two cases seem to have r >2 indeed, which
would indicate that the limit of the commutator is indeed the commutator of the limits for the states under
consideration. Therefore, we have evidence for the following materialization of (117a):
Exchange of commutators and limits: We have the conjecture
[Lp+n + ¯L−p−n, L−p− ¯Lp]↦→ (2p +n)(Ln + ¯L−n), for n⁄= 0. (124)
Figure 4: Absolute value of matrix elements of R as deﬁned in (123), plotted using the same conventions as in
Figure 3.
31
Figure 5: Absolute value of matrix elements, plotted using the same conventions as in Figure 3 but with the
choice of|u⟩ =|v⟩. The operators are here normal ordered: :O:≡ O−O∞ with O∞ being the ground state
expectation value as N→∞ . This value is given for ej in (16), and for ejej+1 +ej+1ej and [ej, [ej+1,ej+2]] in
(133).
