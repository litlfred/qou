---
doc_id: arxiv-2104.07437v4
doc_title: "Peacock patterns and new integer invariants in topological string theory"
section_id: sec-005-3-examples
section_title: "Examples"
section_number: 3
pages: 10-11
source_pdf: 2104.07437v4.pdf
source_sha256: a0f28a6b61618467
toc_source: outline
doc_brief: "Peacock patterns and new integer invariants in topological string theory — Topological string theory near the conifold point of a Calabi–Yau threefold gives rise to factorially divergent power series"
---
integers. However, there is a third category of examples involving inﬁnitely many integer Stokes
constants. This is the case of “peacock patterns,” which was studied in detail in [11, 12] in the
case of complex CS theory. We conjecture that peacock patterns are typical of theories based on
quantum curves. This includes topological string theory on toric CY threefolds (as we discuss in
this paper), (complex) CS theory, and the exact WKB method for generic diﬀerence equations.
Let us now discuss in more detail how to apply the framework of the previous section to the
perturbative series deﬁned in (2.11). We ﬁrst recall that, as explained in (2.11), for every set
of integers N, topological string theory provides a single perturbative series ΦN(gs). It is easy
to verify in examples that these series are Gevrey-1 and resurgent functions, and we conjecture
that this is the case in general. We also expect that each of these series will be accompanied
by additional series (or basic trans-series), leading to a minimal resurgent structure BΦN . This
structure can be found by studying the singularities of their Borel transforms.
This is indeed the case, and, as we will see in the examples discussed below, one ﬁnds a
“peacock pattern structure” very similar to the one described in [11, 12] in complex CS theory.
More precisely, the minimal resurgent structure BΦN consists of the following ingredients. There
is a ﬁnite number of Gevrey-1 series
Φσ;N(gs),
σ = 0, 1, · · · , ℓN,
(2.31)
where Φ0,N(gs) = ΦN(gs) is the original series (2.11). The total number of these series, ℓN + 1,
depends, as we have indicated, on N, and on the CY we are considering. In addition to this
ﬁnite number of basic trans-series, we have an inﬁnite family of them, labelled by an additional
integer n ∈Z, and of the form
Φσ,n;N(gs) = Φσ;N(gs)e−n A
gs ,
n ∈Z,
(2.32)
where A is a complex constant which depends on N and on the CY. Note in particular that the
singularities of the Borel transforms bΦσ;N(ζ) form inﬁnite towers in the Borel plane, spaced by
– 9 –
integer multiples of A. The minimal resurgent structure is then of the form
BΦN = {Φσ,n;N(gs)}σ=0,··· ,ℓN; n∈Z.
(2.33)
Given the structure (2.32), the Stokes constants Sσσ′,n;N are labelled by a pair of indices
σ, σ′ = 0, · · · , ℓN and an integer n, and we conjecture that they are integers, after a natural
normalization of the fundamental series in (2.31). They can be naturally organized as q-series,
Sσσ′;N(q) =
X
n∈Z
Sσσ′,n;Nqn.
(2.34)
Let us note that the formal series (2.32) represent additional sectors of the topological string
which are invisible in perturbation theory (in particular, they involve explicit non-perturbative
corrections in the string coupling constant gs). We believe that they are closely related to the
trans-series constructed in [29, 30] by using the holomorphic anomaly. At this moment, however,
the geometric and physical meaning of these sectors is not clear.
The above procedure can be summarized as a “resurgent machine” in which we start with
perturbative series and we end up, conjecturally, with integer invariants organized in q series.
Schematically,
perturbative series −→integer invariants/q-series.
(2.35)
We should mention that this procedure to obtain integer invariants and q-series from perturbative
series is diﬀerent from the one suggested in [51–57], in the context of Chern–Simons theory with
a compact gauge group. In those papers, the perturbative series is upgraded to a q-series, in such
a way that the former is recovered through the so-called radial asymptotics of the latter. In that
upgrading, the q-series is not deﬁned in a unique way from the perturbative series. In contrast, in
the procedure described above, the perturbative series determines uniquely the diﬀerent q-series,
since it determines uniquely the set of Stokes constants.
3
Examples
We will now present some non-trivial examples of the above construction, focusing on the case
of toric CY manifolds3. A very useful tool in the determination of the Stokes constants deﬁned
