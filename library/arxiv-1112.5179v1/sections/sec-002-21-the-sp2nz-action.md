---
doc_id: arxiv-1112.5179v1
doc_title: "3-Manifolds and 3d Indices"
section_id: sec-002-21-the-sp2nz-action
section_title: "The Sp(2N,Z) action"
section_number: 2.1
pages: 8-10
source_pdf: 1112.5179v1.pdf
source_sha256: b58af08336c40994
toc_source: outline
doc_brief: "3-Manifolds and 3d Indices — We identify a large class R of three-dimensional N = 2 superconformal ﬁeld the- ories."
---
The Sp(2N, Z) action
In [22], an Sp(2N, Z) action on 3d SCFT’s with N U(1) ﬂavor symmetries was introduced.5
The index (2.5) in the charge basis transforms very transparently under this action. Namely,
4This is a possibly more reﬁned version of the requirement of positive monopole operator dimensions used
to discuss the IR behavior of N = 4 gauge theories [47].
5We refer the reader to [22], as well as [19], for details of Sp(2N, Z) transformations on SCFT’s.
Our
notation here closely follows that in [19].
– 7 –
for g ∈Sp(2N, Z), we have6
Ig◦T (g γ; q) = IT (γ; q) .
(2.7)
For simplicity, we can illustrate the action (2.7) for N = 1 (i.e. a single U(1) ﬂavor symmetry)
by looking at the action of the two generators T and S of Sp(2, Z) ≃SL(2, Z).
A T transformation simply adds one unit of Chern-Simons coupling for the background
U(1) gauge ﬁeld. The eﬀect of the CS coupling for the ﬂavor symmetry background gauge
ﬁeld is simply to shift the ﬂavor charge of a state by an amount proportional to the magnetic
ﬂux. Therefore
IT◦T (m, e + m; q) = IT (e, m; q) ,
(2.8)
which is compatible with the matrix representing T,
T :
m
e

7→
1
0
1
1
m
e

.
(2.9)
An S transformation makes the background gauge ﬁeld dynamical, and adds a super-
symmetric FI term for it. This eﬀectively couples the resulting theory to a background U(1)
for a new ﬂavor symmetry, whose conserved current is the magnetic ﬂux of the old, now
gauged, ﬂavor symmetry. Thus, the new electric charge is the old magnetic ﬂux. Gauging
the old ﬂavor symmetry also means that we should project onto states of zero gauge charge.
However, turning on a magnetic ﬂux m′ for the new ﬂavor symmetry shifts the gauge charge
of a state by m′, so in eﬀect we project onto states of gauge charge −m′. Altogether we ﬁnd
IS◦T (−e, m; q) = IT (m, e; q) ,
(2.10)
which is compatible with the matrix representing S,
S :
m
e

7→
0 −1
1
0
m
e

.
(2.11)
From these matrix representations, it is easy to check that I(ST)3◦T (γ; q) = IT (γ; q), and
IS2◦T (γ; q) = IT (−γ; q), as expected from the group relations (ST)3 = id. and S2 = C,
where C acts as charge conjugation.
The T and S transformations (2.8)–(2.10) could also be written in a “fugacity” basis for
the index (2.3). We ﬁnd
IT◦T (m; q, ζ) = ζm IT (m; q, ζ) ,
(2.12)
IS◦T (m′; q, ζ′) =
X
m∈Z
I
dζ
2πiζ ζ′mζm′ IT (m; q, ζ) ,
(2.13)
with the integration done, as usual, on the unit circle. In this form, it is easier to see that
the transformations agree with the general rules of [15, 17] for gauging ﬂavor symmetries and
adding Chern-Simons terms to the index.
6Note that the Sp(2N, Z) transformation acts non-trivially on the (−1)e·m factor we included in the deﬁ-
nition of the fermion number. We will return to this in Section 2.2.
– 8 –
