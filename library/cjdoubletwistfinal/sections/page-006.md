---
doc_id: cjdoubletwistfinal
doc_title: "THE COLORED JONES POLYNOMIAL AND KONTSEVICH-ZAGIER SERIES FOR DOUBLE TWIST KNOTS"
section_id: page-006
section_title: "Page 6"
section_number: null
pages: 6-6
source_pdf: cJdoubletwistfinal.pdf
source_sha256: a1e18db5232b39f4
toc_source: undetermined
doc_brief: "THE COLORED JONES POLYNOMIAL AND KONTSEVICH-ZAGIER SERIES FOR DOUBLE TWIST KNOTS — Using a result of Takata, we prove a formula for the colored Jones polynomial of the double twist knots K(−m,−p) and"
---
6
JEREMY LOVEJOY AND ROBERT OSBURN
and
Um,p(x; q)
=
X
n≥0
n=nm≥nm−1≥···≥n1≥0
n=sp≥sp−1≥···≥s1≥0
(−xq)n(−x−1q)n(−1)nq−(n+1
2 )
m−1
Y
i=1
qn2
i +ni

ni+1
ni
 p−1
Y
j=1
q−sj−sj+1sj

sj+1
sj

.
(1.25)
Neither Fm,p(q) nor Um,p(x; q) is deﬁned anywhere except at roots of unity. Note that
Fm,p(ζN) = JN(K(−m,p); ζN)
(1.26)
and
Um,p(−1; ζN) = JN(K(m,−p); ζN).
(1.27)
As a result of (1.4), (1.26) and (1.27), we immediately obtain the following duality at roots of
unity.
Corollary 1.4. If ζN is any Nth root of unity, then we have
Fm,p(ζN) = Um,p(−1; ζ−1
N ).
(1.28)
We expect (1.7), (1.12) and Theorems 1.1 and 1.2 in [23] to be of considerable interest to
those working at the overlap of number theory, quantum topology, combinatorics and physics.
Recently, Park [25] used (1.7) and (1.12) to check conjectures of Gukov and Manolescu [12]
concerning the existence of a two-variable invariant (with origins in string theory) for knot
complements. In [22], the ﬁrst author initiated the study of quantum q-series identities with
Corollary 1.3 as a key illustration. Furthermore, we suspect that the generalized Kontsevich-
Zagier series Fm,p(q) given by (1.15) are quantum modular forms.
The paper is organized as follows. In Section 2, we recall Takata’s main theorem and provide
some preliminaries. In Section 3, we prove Theorems 1.1 and 1.2. We conclude in Section 4 with
a discussion of the generalized Kontsevich-Zagier functions and the generalized U-functions for
the torus knots T(2,2t+1), along with some related questions.
2. Preliminaries
We begin by recalling the setup from [28]. Let l and t be coprime odd integers with l > t ≥1
and p′ := l−1
2 . For 1 ≤j ≤p′, deﬁne integers r(j) such that r(j) ≡(2j −1)t (mod 2l) and
−l < r(j) < l. We put σj := (−1)⌊(2j−1)t
l
⌋, r′(j) := |r(j)|+1
2
and ir′(j) = j (and thus ik = j if
and only if r′(j) = k). For an integer i, sgn(i) denotes the sign of i. Let n = (n1, . . . , np′) and
ns = 0 for s ≤0. Finally, deﬁne
κ(p′) =

−Nnp′
if σp′ = −1,
0
if σp′ = 1
(2.1)
and
τ(j) =
(
(−1)nj−nj−1
if σj = −1,
q(
nj−nj−1+1
2
)
if σj = 1.
(2.2)
