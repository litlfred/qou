---
doc_id: arxiv-2208.13448v2
doc_title: "ON THE COMPUTATION OF THE DIFFERENCE GALOIS GROUPS OF ORDER THREE EQUATIONS"
section_id: sec-000-1-introduction
section_title: "Introduction"
section_number: 1
pages: 1-2
source_pdf: 2208.13448v2.pdf
source_sha256: 8bfa244cf7ca867d
doc_brief: "ON THE COMPUTATION OF THE DIFFERENCE GALOIS GROUPS OF ORDER THREE EQUATIONS — In this paper we consider the problem of computing the diﬀere nce Galois groups of order three equations for a large"
---
Diﬀerence Galois theory is the subject of many recent papers b ecause, for instance, of
its application to (diﬀerential) transcendence of solution s of diﬀerence equations. More
precisely, consider a ﬁeld k equipped with an automorphism φ. Let C ⊂ C be an
algebraically closed ﬁeld of characteristic 0. Typical exa mples we are going to consider in
this paper are
• (Case S, shift) k = C(z) and φY (z) = Y (z + h) with h ∈ C ∗;
• (Case Q, q-diﬀerence) k = C
(
z1/∗)
:= ∪∞
ℓ=1C(z1/ℓ) and φY (z) = Y (qz) with
q ∈ C ∗ that is not a root of unity;
• (Case M, Mahler) k = C
(
z1/∗)
and φY (z) = Y (zp) with p ≥ 2 an integer;
• (Case E, elliptic) Let Λ be a lattice of C. Without loss of generality, we assume
that Λ = Z + Zτ with Im( τ ) > 0. Let ℘(z) be the corresponding Weierstrass
function. In this example, k = Mer(Λ ∞) := ∪∞
ℓ=1C(℘(z/ℓ), ∂z ℘(z/ℓ)) and
φY (z) = Y (z + h) with h ∈ C∗ such that hZ ∩ Λ = {0}.
Then, consider the diﬀerence system
φY = AY, A ∈ GLn(k).
The algebraic relations between functions which are entrie s of matrix solutions of the
diﬀerence system are reﬂected by a diﬀerence Galois group, whi ch is an algebraic group
attached to a diﬀerence equation (see for example [ VdPS97, Phi15]). Roughly speaking, if
the diﬀerence Galois group is suﬃciently big then there are no algebraic relations between
these functions. Moreover, thanks to a diﬀerential Galois th eory for diﬀerence equations
Date: July 6, 2023.
2010 Mathematics Subject Classiﬁcation. 39A06, 12H05.
Key words and phrases. Diﬀerence Galois theory, Algorithm, Diferential transcen dance.
This project has received funding from the ANR De rerum natur a project (ANR-19-CE40-0018).
1
2 THOMAS DREYFUS AND MARINA POULET
(see [ HS08]), one can attach a diﬀerential algebraic group to a diﬀerence equation, which
is Zariski-dense in the diﬀerence Galois group. Under condit ions on the diﬀerence Galois
groups, this theory may also prove that some solutions of lin ear diﬀerence equations do
not satisfy algebraic diﬀerential equations (see [ HS08, AS17, DHR18, ADHW20, ADH21,
ADR21, DHR21]) and has been recently used to prove that, in some cases, the generating
series of walks in the quarter plane are diﬀerentially transc endental, see for instance
[DHRS18]. There are many other applications of diﬀerence Galois theo ry that motivate
