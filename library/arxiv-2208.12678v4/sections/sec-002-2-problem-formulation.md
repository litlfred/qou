---
doc_id: arxiv-2208.12678v4
doc_title: "STATIONARY CURVES UNDER THE MÖBIUS-PLATEAU ENERGY"
section_id: sec-002-2-problem-formulation
section_title: "Problem Formulation"
section_number: 2
pages: 2-4
source_pdf: 2208.12678v4.pdf
source_sha256: 406d36ff4968091d
toc_source: outline
doc_brief: "STATIONARY CURVES UNDER THE MÖBIUS-PLATEAU ENERGY — Plateau problems with elastic boundary energies have been of recent theoretical and applied interest."
---
Denote the closed unit disk by D ⊂R2 and let γ : ∂D →R3 be a rectifiable simple closed curve. We
define the M¨obius energy [O’H03, FHW94] as
EM[γ] =
ZZ
∂D×∂D
"
1
|γ(y) −γ(x)|2 −
1
D(γ(y), γ(x))2
#
|˙γ(x)| |˙γ(y)| dydx,
(1)
where D(γ(x), γ(y)) denotes the geodesic distance between γ(x) and γ(y) along the curve γ. The M¨obius
energy blows up in self intersections, so the gradient descent will not encounter boundary catastrophes, an
issue which can occur in Euler-Plateau problems requiring strong assumptions to avoid [BY01]. Furthermore,
minimizers of the M¨obius energy enjoy nice regularity properties. Freedman, He, and Wang proved the
minimizers are C1,1 [FHW94], a result later strengthened to C∞regularity by He [He00], and finally to
analyticity by Blatt and Vorderobermeier [BV18].
For a fixed curve γ, we define the following class of parametrized discs that span the curve,
Dγ := {u : D →R3| u ∈W 1,2(D) ∩C0(D), u : ∂D →γ is monotone and onto}
The area of the image of u ∈Dγ can be computed as
Area(u) =
Z
D

|ux|2 |uy|2 −⟨ux, uy⟩2 1
2 dxdy
(2)
where ux and uy are the derivatives of u in x and y. We then have the following definition of the Plateau
energy,
EP [γ] = inf
u∈Dγ Area(u).
(3)
Note the Plateau energy is defined on curves, not surfaces. Furthermore, we restrict the topological class of
the candidate solutions to a disk. Our problem of interest can be stated as follows,
Problem 1. For fixed constants α, β ≥0, find a closed curve γ of prescribed length and knot type which
minimizes the M¨obius-Plateau energy,
E[γ] = αEM[γ] + βEP [γ].
(4)
3. Energy Minimization
In this section, we fix α = β = 1. Recall that a knot type refers to an equivalence class of rectifiable
simple closed curves in R3 with respect to ambient isotopy. A knot type is irreducible if a representative
cannot be realized as the connect sum of two nontrivially knotted curves. By convention, we will also say the
unknot is irreducible. We restrict to irreducible knot types in order to apply the results of [FHW94]. The
existence of M¨obius minimizers for composite knot types remains open due to the possibility of “pull-tight”
singularities in the gradient descent.
We define the following admissible class of closed curves for some irreducible knot type K,
A = {γ ∈C0,1(∂D, R3)| γ(∂D) is simple closed,
γ is of knot type K, Length(γ) = 2π, γ(0) = 0}
Here, C0,1(∂D, R3) denotes Lipschitz maps from ∂D ∼= S1 to R3. The constraints γ(0) = 0 (written with
an abuse of notation) and Length(γ) = 2π together ensure that the images of the curves in A are contained
in some ball of fixed radius. This compactness condition allows for lower semicontinuity with respect to
uniform convergence to imply the existence of a minimizer.
STATIONARY CURVES UNDER THE M ¨OBIUS-PLATEAU ENERGY
3
We also state some key results that are useful in the proof of the existence theorem.
Lemma 2 ([FHW94] Lemma 1.2). Let γ : X →R3 be a rectifiable curve in R3 parametrized by arc length.
If EM[γ] is finite, then γ is C bi-Lipschitz with constant C depending only on EM[γ]. Furthermore, C →1
as EM[γ] →0.
As noted in [FHW94], the M¨obius energy enjoys a property akin to absolute continuity: subarcs of a
curve with finite M¨obius energy can be chosen to have arbitrarily small energy provided that their length is
sufficiently small. Since the M¨obius energy is small, the (inverse) intrinsic and extrinsic distances are close
in L2, and so the subarcs are close to being isometrically embedded in R3.
Lemma 3 ([FHW94] Corollary 1.3). With γ as above such that EM[γ] is finite, we have that for any ε > 0,
there exists δ = δ(ε, γ) > 0 such that γ is a (1 + ε) bi-Lipschitz embedding on subarcs of γ with length less
than δ.
The (1 + ε) bi-Lipschitz property in the prior lemma is a weaker notion of an isometric embedding. In
proving the existence of minimizers for the M¨obius-Plateau energy, we will need to ensure that arc length is
preserved in the limit of a minimizing sequence. Were we afforded the luxury of our curves being isometric
embeddings of fixed length, length preservation in the limit would trivially follow. In general, total length
is not preserved in sequences of curves, even in a uniformly converging limit. In particular, the length could
shorten. However, we will soon see this weaker property is sufficient for the preservation of total length.
Lemma 4 ([FHW94] Lemma 4.2). Let γi : R/LiZ →R3 be a sequence of rectifiable simple closed curves
of uniformly bounded energy, EM.
Assume that the curves are all parametrized by arc-length and that
L = limi→∞Li > 0 exists. If γi(0) is a bounded sequence of points, then there is a subsequence γik of γi
which converges uniformly to a rectifiable simple curve γ : R/LZ →R3. Moreover, EM is sequentially lower
semicontinuous under this convergence, i.e.,
EM[γ] ≤lim inf
ik→∞EM[γik]
Theorem 5 ([FHW94] Theorem 4.3). Let K be an irreducible knot. There exists a simple loop γK : R/LZ →
R3 with knot-type K such that EM[γK] ≤EM[γ] for any other simple closed loop γ : R/LZ →R3 of the
same knot-type.
We begin the proof of existence by considering a minimizing sequence of E, {γk} ⊂A i.e.,
lim
k→∞E[γk] = inf
γ∈A E[γ].
This gives us a uniform bound on EM[γk], therefore, from Lemma 4 we have a subsequence (for which we will
use the same labelling) that converges uniformly to a simple closed C0,1 curve γ∞: ∂D →R3. Furthermore,
by applying the remark after Theorem 5 we can conclude that γ∞has the same knot-type K, even though
the M¨obius energy of the limit is not necessarily the infimum. It is also straightforward to conclude that
γ∞(0) = 0 and apply Fatou’s Lemma to see
Length(γ∞) =
Z 2π
0
|˙γ∞(s)| ds ≤lim inf
k→∞
Z 2π
0
|˙γk(s)| ds = lim inf
k→∞
Length(γk) = 2π.
We must still show Length(γ∞) ≥2π. Let ε > 0. Applying Lemma 3 we have that each γi is a (1 + ε)
bi-Lipschitz embedding on subarcs of length ≤δ = δ(i, ε). As the sequence converges locally uniformly, γ∞
is also a (1 + ε) bi-Lipschitz embedding, and we can assume this δ is independent of i and also works for
γ∞. Now take a partition 0 = s0 < s1 < · · · < sN = 2π with |si+1 −si| < δ and N large enough so that
Nδ > 2π. By the bi-Lipschitz property, we have |γ∞(si+1) −γ∞(si)| ≥(1 + ε)−1|si+1 −si| > (1 + ε)−1δ.
Summing this inequality over i yields Length(γ∞) ≥(1 + ε)−1Nδ > (1 + ε)−12π. As ε was arbitrary, we
conclude Length(γ∞) ≥2π, as desired, so therefore γ∞∈A.
We would like to now show that E is weakly lower semicontinuous with respect to uniform convergence
γk →γ∞. We already have lower semicontinuity in EM. So it remains to show that EP is lower semicontin-
uous, i.e.
EP [γ∞] ≤lim inf
k→∞EP [γk]
(5)
4
MAX LIPTON AND GOKUL G. NAIR
3.1. Lower Semicontinuity of EP . We define the Dirichlet energy of a mapping as
e(u) =
Z
D
|∇u|2 dxdy.
Lemma 6. Let γ ∈A, then
inf
u∈Dγ Area(u) = inf
u∈Dγ e(u)
Proof. Refer to [CM11] Lemma 4.4.
□
First we state the following version of the classical Plateau’s problem. See [Dou31, CM11] for the Lipschitz
and piecewise C1 cases, and [Sim14] for the rectifiable case.
Theorem 7. Given a rectifiable simple closed curve Γ ⊂R3, there exists a map u : D →R3 such that
(1) u : ∂D →Γ is monotone and onto.
(2) u ∈C0(D) ∩W 1,2(D)
(3) The image of u minimizes area among all maps from disks with boundary Γ.
Applying Theorem 7 to each of the simple closed curves γk(∂D) k = 1, 2, ..., ∞and using Lemma 6, we
get a sequence of Plateau solutions uk ∈Dγk. That is, for all k,
e(uk) = Area(uk) =
inf
u∈Dγk
Area(u) = EP [γk].
We can then rewrite (5), the inequality we seek to prove, as
e(u∞) ≤lim inf
k→∞e(uk).
(6)
The issue we must address is that the Plateau solutions uk might not converge to u∞as maps in any
sense. Nevertheless, we will still be able to extract a weak subsequential limit u∗, whose Dirichlet energy,
and therefore surface area, is equal to that of u∞.
