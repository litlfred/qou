---
doc_id: arxiv-2604.16077v1
doc_title: "VOLUME CONJECTURE AND QUANTUM HYPERBOLIC INVARIANTS: THE FIGURE EIGHT KNOT COMPLEMENT"
section_id: sec-003-4-st-ephane-baseilhac-1-f-athi-ben-aribi2
section_title: "ST ´EPHANE BASEILHAC 1, F ATHI BEN ARIBI2"
section_number: 4
pages: 4-5
source_pdf: 2604.16077v1.pdf
source_sha256: 2f1140b9d5fee38a
doc_brief: "VOLUME CONJECTURE AND QUANTUM HYPERBOLIC INVARIANTS: THE FIGURE EIGHT KNOT COMPLEMENT — We compute the real part of the semi-classical limit of the se quence of quantum hyperbolic invariants (QHI) of"
---
make a kind of inﬁnite dimensional version of the QHI and shar e many structural features
with them. It is thus an interesting problem to clarify the re lations between the results of
this paper and those of Gu´ eritaud, Piguet-Nakazawa and the second author in [11], and of
Guilloux, Wong and the second author in [BA W, BAGW] concerni ng F AMED triangulations.
The relations between the QHI and the quantum invariants of R eshetikhin–Turaev or Turaev-
Viro type are very intringuing. As mentioned above, the QHI o f (S3,L ) coincide with the
Kashaev invariant ⟨41⟩N . As an example of relations between these invariants and the QHI
ofS3 \L for a hyperbolic link L, we exhibit in Appendix A a discrete Laplace-transform type
formula connecting the QHI of M =S3 \ 41 and ⟨41⟩N . This formula seems to generalize to
other knots. It may remind the reader of a conjecture of Ander sen-Kashaev [1, Conjecture
1]. Clarifying such relationships could be useful to unders tand the Volume Conjecture for the
colored Jones polynomials, since the QHI are intrinsically geometric, being rational functions
on varieties covering the geometric component of the variet y of PSL (2, C)-characters (see the
formula (80) and the comments thereafter).
Even more intringuing is the problem of extending Zagier’s q uantum modularity conjecture
([64, 34]) to the QHI.
In this direction, we note that a “parity” phenomenon simila r to the alternative (a) vs. (b)
in Theorem 1.1 happens with the Turaev-Viro invariants TV (M,q ) of cusped manifolds M
[21], and with the colored Jones polynomials JL,N (q) of hyperbolic links L at roots of unity q
[26]. Namely, it is conjectured that the sequence of invaria ntsTV (M, exp( 2iπ
N )), with N odd,
grows exponentially with growth rate Vol( M )/2π as N → +∞, whereas TV (M, exp(iπ
N )) is
expected to have polynomial growth (according to Witten’s a symptotic expansion conjec-
ture). Similarly, it is expected that JL,N (exp( 2iπ
N +1/2 )) has semi-classical limit Vol(S3 \L)/2π,
whereas it is known that for any integer l, JL,N (exp( 2iπ
N +l )) grows polynomially with N .
Plan of the paper. In Section 1.2 we give a state sum formulation of Theorem 1.1 t hat may
be more accessible to readers acquainted with the volume con jectures. Section 1.3 presents
the structure of the proof of Theorem 1.1.
The geometric setup of the QHI is described in Section 2. Sect ions 2.1 and 2.2 form a
self-contained toolbox, providing material and, we hope, e nough explanations in order to un-
derstand the QHI far beyond the case of M =S3 \ 41, which is developed in Section 2.3. So
Sections 2.1 and 2.2 could be skipped at a ﬁrst reading. Also, Section 2.4 may be skipped at a
ﬁrst reading; it introduces a logarithmic limit space for th e tower of quantum gluing varieties,
which is useful to understand geometrically all asymptotic al manipulations to follow.
The proof of Theorem 1.1 begins in Section 3. Sections 3.1 and 3.2 provide basic but fun-
damental asymptotic results on the functions used in the QHI state sum formulas. Section
3.3 presents general features of the QHI of cusped manifolds ; in particular, the notation
HN (M,ρ,h ρ,kc), which was not used previously in the literature on QHI, is e xplained.
The combination of Sections 3.4, 3.5 and 3.6 gives an integra l representation of the QHI
of M :=S3 \ 41.
The core of the analysis is developed in Section 4 and 5. In Sec tion 4 we consider as a warm-
up situation the asymptotics of simpliﬁed, so called “class ical” integrals. These integrals are
deﬁned in Section 4.1, where it is also shown how the critical sets of the integrands recover a
neighborhood of the geometric solution in the gluing variet y. The rest of Section 4 is devoted
to the asymptotics of the classical integrals for some speci ﬁc choices of logarithmic limits of
log-parameters, related to Theorem 1.1. In Section 5 we adap t this analysis to the genuine,
“quantum” integrals coming from the QHI of M .
VOLUME CONJECTURE AND QUANTUM HYPERBOLIC INV ARIANTS 5
Notations. In all the paper N is an odd integer greater than 1. We put
ζ :=e
2πi
N , C∗ := C \ {0} , C∗ := C \ {0, 1}.
We denote by Log the complex (Neperian) logarithm with imagi nary part in ] −π,π ], and
by arg(z) ∈] −π,π ] the principal determination of the argument of z ∈ C. It is used in any
evaluation of fractional or real powers of non-zero complex numbers; for instance x1/N :=
exp(Log(x)/N). Except for C∗ and C∗ just deﬁned, we reserve the notation ∗ to the complex
conjugation. The real and imaginary parts of a complex numbe r z are denoted R(z) and
I(z). Finally, we denote by = µN the equality up to multiplication by N -th root of 1.
Acknowledgments. The ﬁrst author had uncountable discussions with Riccardo B enedetti
on the topic of this work, which therefore owes much to his ide as. The second author was
supported by the FNRS in his “Research Fellow” position at UC Louvain under Grant no.
1B03320F, by the ANR project “SyTriQ” and by the grant “Tremp lin nouveaux entrants”
at Sorbonne-Universit´ e. We thank Elisha Falbel for sugges ting the compacity argument in
Section 4.5.1.
