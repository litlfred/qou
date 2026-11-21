---
doc_id: arxiv-math-0110009v3
doc_title: "arXiv:math/0110009v3 [math.MG] 3 Sep 2003"
section_id: sec-003-2-lattices-fourier-transforms-and-poisson-summat
section_title: "Lattices, Fourier transforms, and Poisson summation"
section_number: 2
pages: 4-6
source_pdf: 0110009v3.pdf
source_sha256: bb0c97f2de33b0dd
toc_source: inferred
doc_brief: "arXiv:math/0110009v3 [math.MG] 3 Sep 2003 — We develop an analogue for sphere packing of the linear programming bounds for error-correcting codes, and use it to prove upper bounds for the density of"
---
Given a lattice Λ ⊂Rn, the dual lattice Λ∗is deﬁned by
Λ∗= {y | ⟨x, y⟩∈Z for all x ∈Λ};
it is easily seen to be the lattice with basis given by the dual basis to any
basis of Λ. The covolume |Λ| = vol(Rn/Λ) of a lattice Λ is the volume of any
fundamental parallelotope. It satisﬁes |Λ||Λ∗| = 1. Given any lattice Λ with
NEW UPPER BOUNDS ON SPHERE PACKINGS I
693
shortest nonzero vectors of length r, the density of the corresponding lattice
packing is
πn/2
(n/2)!
r
2
n 1
|Λ|,
and the center density is therefore (r/2)n/|Λ|.
The Fourier transform of an L1 function f : Rn →R will be deﬁned by
bf(t) =
Z
Rn f(x)e2πi⟨x,t⟩dx.
Proposition 2.1.
Let α = n/2 −1. If f : Rn →R is a radial function,
then
bf(t) = 2π|t|−α
Z ∞
0
f(r)Jα(2πr|t|)rn/2 dr,
where “f(r)” denotes the common value of f on vectors of length r.
For a proof, see Theorem 9.10.3 of [AAR]. Here Jα denotes the Bessel
function of order α.
We will deal with functions f : Rn →R to which the Poisson summation
formula applies; i.e., for every lattice Λ ⊂Rn and every vector v ∈Rn,
(2.1)
X
x∈Λ
f(x + v) = 1
|Λ|
X
t∈Λ∗
e−2πi⟨v,t⟩bf(t),
with both sides converging absolutely. It is not hard to verify that the right-
hand side of the Poisson summation formula is the Fourier series for the left-
hand side (which is periodic under translations by elements of Λ), but of course
even when the sum on the left-hand side converges, some conditions are needed
to make it equal its Fourier series.
For our purposes, we need only the following suﬃcient condition:
Deﬁnition 2.2.
A function f : Rn →R is admissible if there is a constant
δ > 0 such that |f(x)| and | bf(x)| are bounded above by a constant times
(1 + |x|)−n−δ.
Admissibility implies that f and bf are continuous, and that both sides of
(2.1) converge absolutely. These two conditions alone do not suﬃce for Poisson
summation to hold, but admissibility does. For a proof for the integer lattice
Zn, see Corollary 2.6 of Chapter VII of [SW]. The general case can be proved
similarly, or derived by a linear change of variables.
We could deﬁne admissibility more broadly, to include every function to
which Poisson summation applies, but the restricted deﬁnition above appears
to cover all the useful cases, and is more concrete.
694
HENRY COHN AND NOAM ELKIES
