---
doc_id: arxiv-1704.00850v3
doc_title: "Estimating the spectral gap of a trace-class Markov operator"
section_id: sec-003-4-data-augmentation-operators-and-an-integral-re
section_title: "Data augmentation operators and an integral representation of sk"
section_number: 4
pages: 7-9
source_pdf: 1704.00850v3.pdf
source_sha256: 09dd9c99453ba251
doc_brief: "Estimating the spectral gap of a trace-class Markov operator — The utility of a Markov chain Monte Carlo algorithm is, in large part, determined by the size of the spectral gap of the corresponding"
---
In order to formally deﬁne DA, we require a second measure space. Let (SV,V,ν ) be a σ-ﬁnite measure
space such thatV is countably generated. Also, rename S and π, SU and πU, respectively. Consider the
random element (U,V ) taking values inSU×SV with joint pdfπU,V (·,·). Suppose the marginal pdf ofU is
the target,πU(·), and denote the marginal pdf ofV byπV (·). We further assume that the conditional densities
πU|V (u|v) := πU,V (u,v )/πV (v) andπV|U(v|u) := πU,V (u,v )/πU(u) are well deﬁned almost everywhere
inSU×SV. Recall that Φ is a Markov chain on the state space SU with Mtdp(u,·), u∈ SU. We call Φ a
DA chain, and accordingly,P a DA operator, ifp(u,·) can be expressed as
p(u,·) =
∫
SV
πU|V (·|v)πV|U(v|u)ν(dv). (3)
Such a chain is necessarily reversible with respect toπU(·). To simulate it, in each iteration, one ﬁrst draws
the latent elementV usingπV|U(·|u), whereu∈SU is the current state, and then givenV =v, one updates
7
the current state according to πU|V (·|v). A DA operator is non-negative, and thus possesses a positive
spectrum (Liu et al., 1994).
Assume that (3) holds. Given k∈ N, the power sum of P ’s eigenvalues,sk, if well deﬁned, is closely
related to the diagonal components of p(k)(·,·). Just as we can calculate the sum of the eigenvalues of a
matrix by summing its diagonals, we can obtain sk by evaluating
∫
SU
p(k)(u,u )µ(du). Here is a formal
statement.
Theorem 2. The DA operatorP is trace-class if and only if
∫
SU
p(u,u )µ(du)<∞. (4)
If (4) holds, then for any positive integerk,
sk :=
κ∑
i=0
λk
i =
∫
SU
p(k)(u,u )µ(du). (5)
Theorem 2 is a combination of a few standard results in classical functional analysis. It is fairly well-
known, but we were unable to ﬁnd a complete proof in the literature. An elementary proof is given in the
appendix for completeness. For a more modern version of the theorem, see Brislawn (1988).
It is often possible to exploit Theorem 2 even when Φ is not a DA Markov chain. Indeed, suppose
that Φ is reversible, but is not a DA chain. Then P is not a DA operator, but P 2, in fact, is. (Just take
πU,V (u,v ) =πU(u)p(u,v ).) If, in addition,P is Hilbert-Schmidt, which is equivalent to
∫
SU
∫
SU
(p(u,u′))2πU(u)
πU(u′) µ(du)µ(du′)<∞,
then by a simple spectral decomposition (see e.g. Helmberg, 2014,§28 Corollary 2.1) one can show thatP 2
is trace-class, and its eigenvalues are precisely the squares of the eigenvalues ofP . In this case, the spectral
gap of P can be expressed as 1 minus the square root of P 2’s second largest eigenvalue. Moreover, by
Theorem 2, fork∈ N, the sum of thekth power ofP 2’s eigenvalues is equal to
∫
SU
p(2k)(u,u )µ(du)<∞.
We now brieﬂy describe the so-called sandwich algorithm, which is a variant of DA that involves an
extra step sandwiched between the two conditional draws of DA (Liu and Wu, 1999; Hobert and Marchev,
2008). Lets(v,·), v∈SV be a Markov transition function (Mtf) with invariant densityπV (·). Then
˜p(u,·) =
∫
SV
∫
SV
πU|V (·|v′)s(v,dv′)πV|U(v|u)ν(dv), u∈SU, (6)
is an Mtd with invariant density πU(·). This Mtd deﬁnes a new Markov chain, call it ˜Φ, which we refer to
as a sandwich version of the original DA chain, Φ. To simulate ˜Φ, in each iteration, the latent element is
ﬁrst drawn from πV|U(·|u), and then updated using s(v,·) before the current state is updated according to
8
πU|V (·|v′). Sandwich chains often converge much faster than their parent DA chains (see e.g. Khare and
Hobert, 2011).
Of course, ˜p(u,·) deﬁnes a Markov operator on L2(πU), which we refer to as ˜P . It is easy to see that,
if the Markov chain corresponding to s(v,·) is reversible with respect to πV (·), then ˜p(u,·) is reversible
with respect to πU(·). Thus, when s(v,·) is reversible, ˜P 2 is a DA operator. Interestingly, it turns out that
˜p(u,·) can often be re-expressed as the Mtd of a DA chain, in which case ˜P itself is a DA operator. Indeed,
a sandwich Mtd ˜p(u,·) is said to be “representable” if there exists a random element ˜V inSV such that
˜p(u,u′) =
∫
SV
πU| ˜V (u′|v)π ˜V|U(v|u)ν(dv), (7)
whereπU| ˜V (u′|v) andπ ˜V|U(v|u) have the apparent meanings (see, e.g. Hobert, 2011). It is shown in Propo-
sition 3 in Section 5 that whenP is trace-class and ˜p(u,·) is representable, ˜P is also trace-class. In this case,
let{˜λi}˜κ
i=0 be the decreasingly ordered positive eigenvalues of ˜P taking into account multiplicity, where
0≤ ˜κ≤∞ . Then ˜λ0 = 1, and ˜λ1≤λ1 < 1 (Hobert and Marchev, 2008). For a positive integerk, we will
denote∑˜κ
i=0 ˜λk
i by ˜sk. Henceforth, we assume that ˜p(u,·) is representable and we treat ˜P as a DA operator.
It follows from Theorem 2 that in order to ﬁndsk or ˜sk, all we need to do is evaluate
∫
SU
p(k)(u,u )µ(du)
or
∫
SU
˜p(k)(u,u )µ(du), where ˜p(k)(u,·) is the k-step Mtd of the sandwich chain. Of course, calculating
these integrals (in non-toy problems) is nearly always impossible, even for k = 1. In the next section, we
