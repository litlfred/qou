---
doc_id: arxiv-2605.22763v1
doc_title: "Advancing mathematics research with AI-driven formal proof search"
section_id: sec-003-deployment-in-mathematics-research
section_title: "Deployment in Mathematics Research"
section_number: null
pages: 6-8
source_pdf: 2605.22763v1.pdf
source_sha256: 1fe6b92bb5eb0b45
doc_brief: "Advancing mathematics research with AI-driven formal proof search — 14 sections: Introduction; AlphaProof Nexus; Systematic Evaluation on Open Prob"
---
Optimization Theory.Agent (D) resolved an open question in optimization: proving an
exactO( 1/𝑡) convergenceratefortheAnchoredGradientDescent-Ascent(GDA)algorithmfor
min-max convex-concave optimization, thereby tightening the slower bound established by
[52]. The proof departs from continuous-time ordinary differential equations (ODE) analysis
used in previous work, instead using a discrete-time recurrence-based approach. The agent
did not merely verify a fixed algorithm: we marked the learning schedule as a parameter
within anEVOLVE-VALUE block in the input file, allowing the agent to simultaneously search
for the schedule and the proof, ultimately discovering a novel parameter choice that yields
the stronger guarantee. We previously released a deformalized version of the proof as a
preprint [58]. Subsequent work [13] has extended this result.
Graph Theory.Thegraph reconstruction conjecture[ 61] is one of the oldest open problems
in combinatorics. It asserts that every finite simple graph with at least three vertices is
determined, up to isomorphism, by the multiset of its vertex-deleted subgraphs, known as its
deck. AlphaEvolve [46] experiments helped us formulate two bipartite variants of the graph
reconstruction conjecture, along with a proposed full reconstruction algorithm. For one of
these variants, our agent produced a complete proof. For the full algorithmic reconstruction
statement, the agent generated proof sketches and strategies that helped clarify the structure
of the problem and led to simplified reformulations of the conjectures originally suggested by
AlphaEvolve. A paper based on the results of this collaboration is currently in preparation.
6
Advancing Mathematics Research with AI-Driven Formal Proof Search
ID Conjecture Summary Proof Technique
12(i) (1970) Existence of𝐴⊂ℤ + s.t. 𝑎∤(𝑏+𝑐)
with|𝐴∩[ 1,𝑁]|/
√
𝑁 > 𝛿 >0infinitely often
Block-based construction via CRT and 3-AP
avoiding sets
12(ii) (1970) Existence of𝐴⊂ℤ + s.t. 𝑎∤(𝑏+𝑐)
with|𝐴∩[ 1,𝑁]|≫𝑁 1−𝜖 for any𝜖 and 𝑁
sufficiently large
Block-based construction via CRT and 3-AP
avoiding sets
125 (1996){˝𝜖𝑘3𝑘|𝜖𝑘 ∈ {0, 1}}+{ ˝𝜖𝑗4𝑗|𝜖𝑗 ∈
{0,1}}has lower density zero
Inductive thinning via Diophantine approx.
3𝑚≈4 𝑘
138∗ (1981) Van der Waerden numbers satisfy
𝑊(𝑘+1)−𝑊(𝑘)→∞
Greedy coloring extension with monochro-
matic intersection lemma
152 (1994) Sufficiently large Sidon sets𝐴 con-
tain many isolated points in𝐴+𝐴
Elementary argument by bounds on interior
points, shifted neighbors and quadruples
741(i) (1994) If 𝐴+𝐴 has upper density, there
exists a decomposition𝐴=𝐴 1⊔𝐴 2 s.t. 𝐴1+
𝐴1,𝐴 2+𝐴 2 have positive upper density
Bounding of upper density of𝐴𝑖+𝐴 𝑖 via
cases on upper density of𝐴
741(ii) (1994)Existenceofabasis 𝐴oforder2with
𝐴1+𝐴 1, 𝐴2+𝐴 2 having bounded gaps for
all𝐴 1,𝐴 2 such that𝐴=𝐴 1⊔𝐴 2
Explicit construction via rapidly growing se-
quence
846 (1992) Existence of infinite set 𝐴 such
that any finite subset contains many non-
collinear points, but is not a finite union of
non-collinear sets
Label 𝐾∞ vertices with terms from fast-
growing sequence, apply map on edges
{𝑖, 𝑗} ↦→ (𝑥𝑖+𝑥 𝑗,𝑥 2
𝑖 +𝑥 𝑖𝑥𝑗+𝑥 2
𝑗) to obtain
𝐴
26∗,† (1995) Existence of𝐴 such that upper den-
sity of𝐴+𝑘is<1− 1
4 for all naturals𝑘
Block-based construction using increasing
sequence of primes, CRT, and bounding u.
density by cases
Table 1| Open problems from the ErdosProblems repository autonomously resolved
by our full-featured agent.The asterisk indicates a variant of the main problem with this
number. Problem #26 (annotated with†) is a more general variant of a question posed by
Erdős, but was not posed by Erdős himself.
Separately, the agent proved an open graph theory conjecture regarding a bound on the
maximum number of leaves over all spanning trees of a graph𝐺, relating it to the maximum
number, over all vertices𝑣∈𝐺 , of independent sets in the neighborhood of𝑣. The problem
was posed by Graffiti [19], an automated conjecturing system, in 1996, and points to an
interesting future opportunity to close the loop between AI-based conjecturing and proof.
Algebraic Geometry.We evaluated our full-featured agent on eight algebraic geometry
problems, from textbook-style exercises to open research questions on Hilbert functions,
solving two of the four open problems. One of these problems had been a well-known
open question for approximately fifteen years. This problem concerned pure𝑂-sequences,
equivalently the Hilbert functions of monomial Artinian level algebras [57]. Their shape
and positivity properties have been studied intensively in recent years [9]. Although log-
concavity fails for broad families of pure𝑂-sequences, the case of codimension3and type
2was identified as the principal remaining open case [68]. The agent’s proof establishes
log-concavity in this case; the argument is substantial, using a nontrivial reformulation of the
Hilbert function and a detailed case analysis of the resulting second-difference inequalities.
7
Advancing Mathematics Research with AI-Driven Formal Proof Search
Additive Combinatorics.Our agent helped resolve problem #57 from Green’s well-known
list of open conjectures [27]. The problem asks whether two specific quadratically structured
function spaces coincide. The functions of interest map elements of an Abelian group𝐺 to
the complex numbers. Here, our agent autonomously solved a variant of the problem in
which the functions are real-valued, but a personal communication from Green clarified that
the complex-valued case was the intended challenge. While the agent could not immediately
provetheintendedversionoftheproblem,numericalheuristicsusingfloating-pointarithmetic
provided a candidate counterexample (the cyclic groupℤ/3ℤ and a specific separating
functional). We formalized the problem of whether this counterexample disproves the correct
conjecture, and the agent autonomously proved that it indeed does. A paper on the result is
in the works [22].
Quantum Optics.With Mario Krenn, we investigated a set of quantum optics problems
concerning the existence of monochromatic quantum graphs with𝑁 vertices and𝑑 colors
drawn from domains such as the reals, the complex numbers, and{−1, 0, 1}. These con-
structions correspond to𝑁-particle quantum states with local Hilbert space dimension𝑑 –
in particular, high-dimensional Greenberger–Horne–Zeilinger (GHZ) states realizable via
linear optics [39]. Our agent resolved multiple conjectures of this form, in particular with
𝑁=𝑑∈{4,6,10}. A paper on these results is in preparation [38].
