---
doc_id: arxiv-2010.12819v2
doc_title: "The action of the Virasoro algebra in quantum spin chains. I. The non-rational case"
section_id: sec-024-62-modules-w0qpm2
section_title: "Modules W0,qpm2"
section_number: 6.2
pages: 26-27
source_pdf: 2010.12819v2.pdf
source_sha256: ddc0493d60d48e77
toc_source: outline
doc_brief: "The action of the Virasoro algebra in quantum spin chains. I. The non-rational case — We investigate the action of discretized Virasoro generators, built out of generators of the lattice"
---
We now switch to the modules W0,q2 and W0,q−2 as deﬁned in (28). There will be several diﬀerences compared
to the case of Wj,1. First, the resonance criterion (11) is fulﬁlled. Second, due to having Sz = 0, the chiral and
anti-chiral sectors will have same charges (66) and play the same role. Third, withSz = 0 the lattice momentum
(80) will change by ∆ p = N
2 whenever the Bethe integers are shifted one step. Since the lattice momentum
p is deﬁned modulo the system size, as are the Bethe integers themselves, we cannot distinguish an electric
excitation e from−e and only the absolute value |e| matters.
For the module W0,q2 we have from (37)
F0,q2 = q−c/24¯q−c/24
P (q)P (¯q)
∑
n∈Z
qhn+1/(x+1),0 ¯qhn+1/(x+1),0
= q−c/24¯q−c/24
P (q)P (¯q)
∑
n∈Z
qhn,1 ¯qhn,1. (110)
Note that the dual module W0,q−2 leads to the same generating function of levels in the continuum limit. And
yet, the nature of the Virasoro modules is profoundly diﬀerent in both cases, in accordance with the discussion
made in Section 4. We ﬁnd the following result:
XXZ spin-chain modules with zero magnetization: We have the scaling limits
W0,q2↦→
(⨁
n>0
~V(d)
n,1⊗~V(d)
n,1
)
⊕
(
V0,1⊗ V0,1
)
, (111a)
W0,q−2↦→
(⨁
n>0
V(d)
n,1⊗ V(d)
n,1
)
⊕
(
V0,1⊗ V0,1
)
. (111b)
Note that since we are in the Sz = 0 sector, we expect the problem to be symmetric under the exchange of
chiral and antichiral sectors, in agreement with this conjecture.
We discuss numerical checks of this statement below, but it is (partly) a simple consequence of the structure
of the Temperley-Lieb algebra modules themselves, since the Ln are made out of ej. The numerical results in
support of (111) are presented in Appendix C.2.
Having shown that the identity state 1 belongs to the module W0,q2, we can also directly measure the central
charge for various values of x /∈ Q, through a numerical study of the matrix element
⟨1|L2L−2|1⟩ = c
2. (112)
While the discussion has so far focussed on matrix elements of a single generator Ln, we encounter here for
the ﬁrst time an example of matrix elements of a product of two generators. To follow up on the issue of
“parasitic couplings”—brieﬂy discussed at the end of Section 5.2—we employ two diﬀerent methods to evaluate
26
Figure 2: Finite-size estimates for the central charge c, obtained from (112) for various N, plotted against x
π .
The left panel shows the actual estimates for c, and the right panel their ratio with respect to the CFT result
(“Conj”). We display the results for N = 10, 14,..., 22 obtained by two methods, “No cutoﬀ” and “Cutoﬀ”,
as explained in the main text. Also shown are extrapolations “extr” of the two data sets, obtained from a
7th-order polynomial ﬁt to an extended set of sizes N = 8, 10,..., 22.
this matrix element. In the ﬁrst (denoted “No cutoﬀ” in the caption to Figure 2), we simply compute the
total norm of (112), whereas in the second (denoted “Cutoﬀ”) we insert a projector onto the scaling states
in-between the product of L2 and L−2 before computing the norm. We show in the left panel of Figure 2 how
these ﬁnite-size estimates converge towards the conjectured CFT value c = 1− 24α2
0, for x ranging from 4π/10
to 21π/10. We also display, in the right panel, the relative convergence, where we have divided through by the
conjectured central charge. It is seen that although both methods give results close to the conjectured result,
only the second one (“Cutoﬀ”) leads to full agreement over the whole range of x-values. The reason is that the
ﬁrst method (“No cutoﬀ”) suﬀers from parasitic couplings to non-scaling states. We defer the full discussion of
this crucial phenomenon to Section 7.
