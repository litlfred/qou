---
doc_id: arxiv-2605.19310v1
doc_title: "A FOURIER-FREE DENSITY-INCREMENT PROOF OF ROTH’S THEOREM MARK LEWKO"
section_id: sec-003-8-mark-lewko
section_title: "MARK LEWKO"
section_number: 8
pages: 8-9
source_pdf: 2605.19310v1.pdf
source_sha256: 047d492babc63d2f
doc_brief: "A FOURIER-FREE DENSITY-INCREMENT PROOF OF ROTH’S THEOREM — We give an elementary, Fourier-free proof of Roth’s theorem."
---
7.Proof of Roth’s theorem and the quantitative bound
Proof of Theorem 1. Fix α0> 0 and suppose, for contradiction, that there
are arbitrarily large N and 3AP-free setsA⊂ [N] with|A|≥α 0N. Applying
Proposition 9, then rescaling the progression it gives back to an interval, pro-
duces a new 3AP-free set with density increased by at least cα11
0 . Repeating
this, the density exceeds 1 afterO(α −11
0 ) steps.
It remains only to ensure that the iteration can be run for that many
steps. At each step the ambient length is replaced by a progression of length
at least cα16
0 N 1/2
j . Since the number of steps depends only on α0, choosing
the original N sufficiently large in terms of α0 keeps every intermediate
interval above the threshold in Proposition 9. This contradiction proves the
theorem.□
A more careful analysis gives an explicit double-logarithmic bound.
Corollary 10.There is an absolute constantC >0such that
r3(N)≤C N
(log logN) 1/11
for all sufficiently largeN.
Proof. Let A⊂ [N] be 3AP-free, and write α =|A|/N. Set J =⌊c0α−11⌋,
wherec0> 0 is a sufficiently small absolute constant. If the density increment
can be applied J times, then each step increases the density by at least cα11,
since the densities only increase. After J steps the density would exceed 1,
which is impossible.
It remains to check that the lengths stay large enough for J steps. At each
step, after rescaling the subprogression back to an interval, Proposition 9
gives
αj+1≥α j +cα 11
j , N j+1≥cα 16
j N 1/2
j .
Sinceα j≥α, the length estimate implies
logNj+1≥ 1
2 logNj−Clog(e/α).
Iterating this crude bound gives
logNj≥2−j logN−Clog(e/α).
Thus, if logN≥C 2J log(e/α), then every Nj with j≤J remains larger
than a fixed power of α−1, and in particular remains above the threshold
required by Proposition 9. SinceJ∼α −11, this condition follows from
log logN≥Cα −11,
after increasingC.
Therefore, if log logN were larger than a sufficiently large constant times
α−11, the iteration could run forJ steps and force the density above 1. Hence
A FOURIER-FREE DENSITY-INCREMENT PROOF OF ROTH’S THEOREM 9
log logN≲α −11, soα≲(log logN) −1/11. Sinceα=|A|/N, this gives
r3(N)≲ N
(log logN) 1/11.
This proves the corollary.□
8.Further remarks
Although the proof above is written without Fourier analysis, several
of the steps have a simple Fourier interpretation. Let e(x) = e2πix/m and
bf(ξ) =P
x∈Zmf(x)e(−ξx). One then has bR(ξ) =|bf(ξ)|2. Hence Parseval
gives
E(f) =
X
t∈Zm
R(t)2 = 1
m
X
ξ∈Zm
|bf(ξ)| 4.
Thus, up to the normalization convention, E(f) is the fourth power of what
is called in the modern Gowers-style literature the U 2-norm. In the usual
modern Fourier-analytic proofs of Roth’s theorem, the implication from a
small 3-term progression count to a largeU 2-norm is standard.
The key non-negativity statement in Lemma 2 also has a short Fourier
explanation. Ifh,k∈Z ×
m andλ=kh −1, then
(8.1)X
d∈Zm
R(hd)R(kd) =
X
t∈Zm
R(t)R(λt) = 1
m
X
ξ∈Zm
|bf(ξ)| 2|bf(−λ−1ξ)|2≥0.
As future research directions, it would be interesting to develop Fourier-free
analogues of the following arguments:
(1) a proof of a polylogarithmic Roth bound of the formr(n)≲n (logn )−c
forc>0;
(2) the energy-increment proof of Roth’s theorem;
(3) Gowers’ argument [3] for 4-term arithmetic progressions.
