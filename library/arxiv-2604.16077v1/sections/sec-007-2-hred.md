---
doc_id: arxiv-2604.16077v1
doc_title: "VOLUME CONJECTURE AND QUANTUM HYPERBOLIC INVARIANTS: THE FIGURE EIGHT KNOT COMPLEMENT"
section_id: sec-007-2-hred
section_title: "Hred"
section_number: 2
pages: 6-8
source_pdf: 2604.16077v1.pdf
source_sha256: 2f1140b9d5fee38a
doc_brief: "VOLUME CONJECTURE AND QUANTUM HYPERBOLIC INVARIANTS: THE FIGURE EIGHT KNOT COMPLEMENT — We compute the real part of the semi-classical limit of the se quence of quantum hyperbolic invariants (QHI) of"
---
N (M,ρ,κ ; s) (the reduced QHI ).
• (Formula (81)) Refomulating this factorization on the tria ngulation (T,b ) of
M :=S3 \K shown in Figure 1, one can write the state sum HN,(T,b,c )(uN, vN )
of HN (M,ρ,h ρ,kc) (the subject of Theorem 1.2) as
HN,(T,b,c )(uN, vN ) = ( u−1
0,N v−1
0,N )
N−1
2 Hred
N (u0,N, u1,N, v0,N, v1,N ).
VOLUME CONJECTURE AND QUANTUM HYPERBOLIC INV ARIANTS 7
II) (Getting rid of the symmetry defect, Lemma 3.10) With a qu ick computation, we
check that limN →+∞(2π/N)Log
⏐
⏐
⏐(u−1
0,N v−1
0,N )
N−1
2
⏐
⏐
⏐ = 0.
These two steps imply that in the proof of Theorem 1.2 we can re place HN,(T,b,c )(uN, vN )
with Hred
N (u0,N, u1,N, v0,N, v1,N ). From known results it has the factorization formula (82):
Hred
N (u0,N, u1,N, v0,N, v1,N ) =
gN (u0,N )gN (v∗
0,N )∗
|gN (1)|2 ΣN (u0,N, u1,N ) ΣN (v∗
0,N, v∗
1,N )∗.
III) (Getting rid of gN (1), gN (u0,N ) and gN (v∗
0,N ), Formula (68) and Lemma 3.8) With
quick computations, we establish that |gN (1)| =
√
N , and thus gN (1) is in PM (N ).
Also, by using a uniform estimate of the quantum dilogarithm functions (Lemma 3.3)
we show that in the situation of Theorem 1.2 the functions gN (u0,N ) and gN (v∗
0,N )
are in PM (N ).
Together with the steps I-II, this further step implies that , in order to prove Theorem 1.2, it
is enough to show that lim N →+∞(2π/N)Log |ΣN (.,. )| is equal to either Vol( M )/2 (case (a))
or 0 (case (b)), both for Σ N (u0, u1) and for Σ N (v∗
0,N, v∗
1,N ).
IV) (Writing Σ N as as an integral, Lemma 3.11) Using properties of the quantu m dilog-
arithm ˆSN (.), we re-write Σ N (u0,N, u1,N ) as in formula (85) :
ΣN (u0,N, u1,N ) = 1 + 1
ˆSN (l0,N )
N −1∑
β=1
e
2πi
N β2−l1β ˆSN (l0,N + 2βiπ/N ),
where (lk,N ) is a sequence of logarithms of ( uk,N ) of a speciﬁc form. Using the residue
theorem, we re-write this formula as in (88):
ΣN (u0,N, u1,N ) = 1 + 1
ˆSN (l0,N )
N
4iπ
∫
CN
e
N
2iπ (z2−l1,Nz) ˆSN (l0,N +z) coth(Nz
2 )dz
whereCN is a closed rectangular contour circling the segment [ 2iπ
N , 2iπ− 2iπ
N ] and close
to it. We denote by is−
N and 2iπ −is+
N its intersection points with iR; by construction
s±
N :=α± π
N with α± ∈]0, 2[.
V) (Getting rid of ˆSN (l0,N ), Lemma 3.8) With properties of the quantum dilogarithms,
we establish that ˆSN (l0,N ) is in PM (N ).
VI) (Equivalence of Theorem 1.1 and Theorem 1.2, Section 3.6 ) Using the description of
the quantum gluing variety in Section 2.3, we show that the tw o cases (a) and (b)
in Theorem 1.1 correspond to the cases (a) and (b) in Theorem 1 .2. Moreover, in
the above integral these cases correspond to having lk,∞ := limN →+∞ lk,N such that
l0,∞ = −2iπ, l1,∞ = iπ, and l0,∞ = −2iπ, l1,∞ = 2iπ respectively. The same facts
occur for Σ N (v∗
0, v∗
1).
We then turn to the semi-classical limit of the integral
(1)
∫
CN
e
N
2iπ (z2−l1,Nz) ˆSN (l0,N +z) coth(Nz
2 )dz.
Somewhat counter-intuitively, we begin with simpler integ rals, over the segment [ is−
N, 2iπ −
is+
N ] instead of CN , where we ﬁx s−
N =α− π
N , α− ∈]0, 1[ (whereas s+
N =α+ π
N has α+ ∈]0, 2[
arbitrary), and with integrands deﬁned by using functions f±(z), depending on l0,∞ and
