---
doc_id: arxiv-2605.22763v1
doc_title: "Advancing Mathematics Research with AI-Driven Formal Proof Search"
section_id: sec-021-erdős-846
section_title: "Erdős #846"
section_number: null
pages: 39-41
source_pdf: 2605.22763v1.pdf
source_sha256: 1fe6b92bb5eb0b45
toc_source: outline
doc_brief: "Advancing Mathematics Research with AI-Driven Formal Proof Search — 29 sections: Front matter; Introduction; AlphaProof Nexus"
---
Theorem. Let 𝐴⊂ℝ2 be an infinite set for which there exists some 𝜖> 0 such that in any
subset of 𝐴of size 𝑛there are always at least 𝜖𝑛with no three on a line.
Is it true that 𝐴is the union of a finite number of sets where no three are on a line?
Proof. We will show that there exists an infinite set 𝐴⊂ℝ2 for which any 𝑛-element subset
contains at least 𝑛/2 points with no three on a line, but 𝐴is not the union of a finite number
of sets where no three are on a line.
Let 𝐾∞be the countably infinite complete graph with vertex set 𝑉= {𝑥1, 𝑥2, . . . }. We
choose the sequence of real numbers (𝑥𝑖)∞
𝑖=1 such that it grows sufficiently fast to avoid
39
Advancing Mathematics Research with AI-Driven Formal Proof Search
any accidental roots of polynomials that will arise in our collinearity condition, by setting
𝑥𝑛= 1004𝑛.
We construct our point set 𝐴⊂ℝ2 by mapping each edge 𝑒= {𝑥𝑖, 𝑥𝑗} of 𝐾∞to a point 𝑃𝑒
as follows:
𝑃𝑒= (𝑥𝑖+ 𝑥𝑗, 𝑥2
𝑖+ 𝑥𝑖𝑥𝑗+ 𝑥2
𝑗)
(1)
Let 𝐴= {𝑃𝑒| 𝑒∈𝐸(𝐾∞)}.
Lemma. Three points in 𝐴are collinear if and only if their corresponding edges form a
triangle in 𝐾∞.
Proof of Lemma. First, assume three edges form a triangle in 𝐾∞with vertices 𝑎, 𝑏, 𝑐∈𝑉.
The corresponding points in 𝐴are:
𝑃𝑎𝑏= (𝑎+ 𝑏, 𝑎2 + 𝑎𝑏+ 𝑏2)
𝑃𝑏𝑐= (𝑏+ 𝑐, 𝑏2 + 𝑏𝑐+ 𝑐2)
𝑃𝑐𝑎= (𝑐+ 𝑎, 𝑐2 + 𝑐𝑎+ 𝑎2)
The slope 𝑚of the line connecting 𝑃𝑎𝑏and 𝑃𝑏𝑐is given by:
𝑚= (𝑏2 + 𝑏𝑐+ 𝑐2) −(𝑎2 + 𝑎𝑏+ 𝑏2)
(𝑏+ 𝑐) −(𝑎+ 𝑏)
= 𝑐2 −𝑎2 + 𝑏𝑐−𝑎𝑏
𝑐−𝑎
Factoring the numerator yields:
𝑚= (𝑐−𝑎)(𝑐+ 𝑎) + 𝑏(𝑐−𝑎)
𝑐−𝑎
= 𝑎+ 𝑏+ 𝑐
By symmetry, the slope of the line connecting 𝑃𝑏𝑐and 𝑃𝑐𝑎is also 𝑎+ 𝑏+ 𝑐. Because the slopes
are equal, the three points are collinear.
Conversely, suppose three distinct edges do not form a triangle. We must show their
corresponding points are not collinear. The condition that these points are collinear is
equivalent to the determinant of their 3 × 3 augmented coordinate matrix evaluating to zero.
Because the sequence (𝑥𝑖)∞
𝑖=1 grows quickly enough, any polynomial evaluated on its terms
is strictly dominated by the highest power of its largest variable. By sorting the endpoints
of the three edges, we can group the expanded determinant into three topological cases
based on whether the largest vertex is present in one, two, or all three of the edges. In
every case, because the edges are distinct and do not form a triangle, the coefficient of the
dominant highest-degree term is bounded strictly away from zero. Furthermore, the massive
gap between consecutive terms in the sequence ensures that the lower-degree terms are
strictly bounded and cannot sum to cancel the leading term out. Therefore, the determinant
never evaluates to zero, and no accidental collinearities occur. □
Lemma. Any 𝑛-element subset of 𝐴contains at least 𝑛/2 points with no three on a line.
Proof of Lemma. Let 𝑆⊂𝐴be an arbitrary subset of size 𝑛. The elements of 𝑆correspond
to a subgraph 𝐺𝑆⊂𝐾∞containing exactly 𝑛edges. Every graph with 𝑛edges contains a
bipartite subgraph 𝐵𝑆with at least 𝑛/2 edges. Because 𝐵𝑆is bipartite, it contains no odd
cycles and is therefore triangle-free. By the previous lemma, the corresponding points in 𝐴
40
Advancing Mathematics Research with AI-Driven Formal Proof Search
contain no collinear triplets. This provides a subset of at least ⌈𝑛/2⌉points with no three on
a line, satisfying the condition with 𝜖= 1/2. □
To complete the proof of the theorem, assume for contradiction that 𝐴can be covered by
a finite number of sets where no three are on a line; that is, 𝐴= Ð𝑟
𝑘=1 𝐴𝑘.
This partition naturally induces an 𝑟-coloring on the edges of 𝐾∞. By the infinite Ramsey
Theorem, any finite coloring of the edges of the infinite complete graph must contain a
monochromatic triangle. Consequently, there exists some color class 𝑘containing three edges
that form a triangle. By the lemma, these three edges map to three collinear points in 𝐴𝑘.
This contradicts the assumption that 𝐴𝑘contains no three collinear points.
Therefore, 𝐴cannot be covered by finitely many sets with no three on a line.
□
We originally communicated the result in https://www.erdosproblems.com/fo
rum/thread/846#post-4447 to the ErdosProblems site, and share the Lean proof at
https://github.com/google-deepmind/alphaproof-nexus-results/blob/ma
in/APNOutputs/ErdosProblems/erdos_846.lean. This result was independently
discovered by an internal model at OpenAI [49]. In the discussion at the ErdosProblems site,
it was pointed out that this result also follows from a projection argument of Reiher, Rödl
and Sales [50].
