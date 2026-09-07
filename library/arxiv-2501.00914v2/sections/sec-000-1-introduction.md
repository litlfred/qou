---
doc_id: arxiv-2501.00914v2
doc_title: "L-SPACES AND KNOT TRACES"
section_id: sec-000-1-introduction
section_title: "Introduction"
section_number: 1
pages: 1-3
source_pdf: 2501.00914v2.pdf
source_sha256: d94bd6edf8544d4a
doc_brief: "L-SPACES AND KNOT TRACES — There has been a great deal of interest in understanding which knots are characterized by which of their Dehn surgeries."
---
Given a knotK⊂S 3 and an integern, then-traceX n(K) is the smooth, oriented 4-manifold
with boundary obtained fromB 4 by attaching ann-framed 2-handle alongK⊂∂B 4. We say that
Xn(K)detectsKif its oriented diffeomorphism type determinesK— that is, if
Xn(J)∼=Xn(K)
implies thatJ=K. In this paper, we propose and study the following question:
Question 1.1.For which knotsK⊂S 3 and integersndoesX n(K)detectK?
Then-traceX n(K) is far from detectingKin general [Akb77, Lic79, AJOT13]. This is promi-
nently illustrated in Piccirillo’s proof that the Conway knot is not slice, a key part of which involves
finding a different knot with the same 0-trace [Pic20].
One way to prove thatX n(K) detectsKis to show that its boundaryS 3
n(K), which is the result
ofn-framed Dehn surgery onK, does — in other words, thatnis acharacterizing slopeforK. A lot
of effort has gone into understanding characterizing slopes for knots. Building on work by Lackenby
[Lac19] and McCoy [McC20], Sorya recently proved that for any knotKall rational numbers with
sufficiently large denominator are characterizing slopes, and ifKis composite then all non-integers
are characterizing [Sor24]; see also [SW24]. Deciding whether a givenintegercharacterizes a certain
knot seems to be much harder in general, and this is especially true for the integern= 0.
On this last point, Gabai proved in 1987 that 0 is a characterizing slope for the unknot, figure-8,
and trefoils in [Gab87], and these were the only knots known to be characterized by their 0-surgeries
until we showed in 2022 that everynearly fiberedgenus-1 knot is as well [BS25, BS24b]. But it is
still open, for example, whether 0 is a characterizing slope even for the torus knotT 2,5.
By contrast, our main result says that the 0-trace detects every L-space knot:
Theorem 1.2.IfKis an L-space knot thenX 0(K)detectsK.
Here,K⊂S 3 is anL-space knotif some positive Dehn surgery onKis a Heegaard Floer L-space,
meaning a rational homology 3-sphereYsuch that
dimdHF(Y) =|H 1(Y;Z)|.
1
arXiv:2501.00914v2  [math.GT]  13 Mar 2026
2 JOHN A. BALDWIN AND STEVEN SIVEK
This class of knots includes all positive torus knots, as well as any other knot with a positive lens
space surgery, like the (−2,3,7)-pretzel knot.
Theorem 1.2 follows from a combination of two results which may each be of independent interest.
The first says that any single trace detectswhethera given knot is an L-space knot:
Theorem 1.3.IfKis an L-space knot andX n(J)∼=Xn(K), thenJis also an L-space knot and
has the same genus asK.
Then= 0 case, which suffices for Theorem 1.2, can be deduced from our work in [BS22], which
in turn was inspired by our proof in [BS23] thatinstantonL-space knots are fibered. The general
case builds on this but is considerably more involved; it further relies on results by Hayden–Mark–
Piccirillo [HMP21], which also enable us to prove in Theorem 4.6 that any traceX n(K) withn≥0
determines theZ/2Z-graded Heegaard Floer homology of each positive rational surgery onK.
The second and more surprising ingredient in Theorem 1.2 is our result that if two L-space knots
have the same 0-surgery then they are the same:
Theorem 1.4.IfJandKare L-space knots such thatS 3
0(J)∼=S3
0(K), thenJ=K.
Theorem 1.4 relies on a deep relationship between the symplectic Floer homology of a surface dif-
feomorphism and the Heegaard Floer homology of its mapping torus, established via a combination
of work by Lee–Taubes [LT12] and Kutluhan–Lee–Taubes [KLT20].
We used this relationship in joint work with Hu [BHS25] to prove that ifKis a genus-2 hyperbolic
L-space knot then the pseudo-Anosov representative of its monodromy has no fixed points, en route
to proving that Khovanov homology detects the cinquefoils; this was later used to prove thatT 2,5
is the only genus-2 L-space knot [FRW24]. In [Ni23, Ni22], Ni extended our argument to show that
the monodromy ofanynontrivial fibered knotK⊂S 3 is freely isotopic to a map with at most
dim [HFK(K,g(K)−1)−1
fixed points; see also Ghiggini–Spano [GS22]. This is particularly useful when
dim [HFK(K,g(K)−1) = 1,
which holds, for instance, wheneverKis an L-space knot; more generally, we call such knotsffpf,
since they are fibered with fixed-point-free monodromy. Theorem 1.4 is then a special case of our
stronger result, Theorem 2.10, which says that no two ffpf knots have the same 0-surgery.
Our proof of Theorem 2.10 goes very roughly as follows: suppose thatKis an ffpf knot with
fiber surface Σ and monodromyh. Let ˆΣ be the closed surface obtained by capping off Σ with a
disk, and let ˆhbe theclosed monodromyobtained by extendinghby the identity over this disk, so
thatS 3
0(K) is the mapping torus of ˆh. The ffpf condition further implies [Ni20] thathisveering.
We combine this with Ni’s results about fixed points to argue that the canonical Nielsen–Thurston
form of ˆhhas a unique fixed point at the center of the capping disk. Removing the fiber over this
fixed point then recovers the knot complementS 3\K.
Now letJbe another ffpf knot with closed monodromy ˆgsuch that
S3
0(J)∼=S3
0(K).
Since this manifold has a unique fibration, ˆgis conjugate to ˆh. We then use the rigidity of pseudo-
Anosovs within their mapping classes [FLP12] to show that the conjugating homeomorphism iden-
tifies the unique fixed points of the Nielsen–Thurston forms of ˆgand ˆh. It follows that
S3\J ∼=S3\K,
and hence thatJ=Kby [GL89].
L-SPACES AND KNOT TRACES 3
