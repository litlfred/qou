---
doc_id: arxiv-2103.07383v1
doc_title: "On the Analyticity of Critical Points of the Generalized Integral Menger Curvature in the Hilbert Case"
section_id: sec-011-a-properties-of-analytic-functions
section_title: "A Properties of analytic functions"
section_number: null
pages: 25-26
source_pdf: 2103.07383v1.pdf
source_sha256: 9dca35ea16490ad8
toc_source: outline
doc_brief: "On the Analyticity of Critical Points of the Generalized Integral Menger Curvature in the Hilbert Case — We prove the analyticity of smooth critical points for generalized integral Menger cur- vature"
---
Properties of analytic functions
In this section we aim to recall some statements related to analytic functions, which are used
in the paper. For further information on analytic functions we refer the reader for instance to
[KP02]. First we note that analytic functions can be characterized as follows, cf. for example
[Vor20, Corollary 3.2].
Proposition A.1. Let f ∈C∞(R/Z, Rn) and s > 0. Then the function f is analytic on R/Z if
there are positive constants r and C such that
∥f (k)∥H1+s ≤C k!
rk
holds for all integers k ≥0.
This can be seen by using [KP02, Proposition 1.2.12] together with a standard covering
argument, Morrey’s inequality (see e.g. [AF03, Paragraph 4.16]), the equivalence of the W 1,2-
and the H1-norm on R/Z (cf. [Rei12, Lem. 1.2] or [AF03, 7.62]) as well as the embedding
Hs ⊆Ht for any t < s (cf. [Tay96, Chapter 4, Proposition 3.4]).
In addition, we need a special case of the Cauchy-Kovalevsky theorem, which can be derived
for example from [Fol95, (1.25)].
25
Theorem A.2 (Cauchy-Kovalevsky – ODE case). Suppose the function G : R2n →Rn is
real analytic around (c0, c1) for some c0, c1 ∈Rn, and the function f ∈C∞((−ε, ε), Rn) of the
form f(x) = (f1(x), . . . , fn(x)), for any ε > 0, is a solution of the initial value problem
f ′′(x) = G(f(x), f ′(x)) for x ∈(−ε, ε) with
f(0) = c0, and
f ′(0) = c1.
Then the function f is real analytic around 0.
The statement can be proven by the method of majorants, e.g. as explained in the proof
of [KP02, 2.4.1]. At this point we remark that the strategy of proof for the main statement,
Theorem 1.2, is motivated from this method.
B
