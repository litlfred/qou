---
doc_id: arxiv-1304.2934v4
doc_title: "MOD-φ CONVERGENCE, I:"
section_id: sec-017-61-technical-preliminaries
section_title: "Technical preliminaries"
section_number: 6.1
pages: 45-46
source_pdf: 1304.2934v4.pdf
source_sha256: b7ed2a9e85264568
doc_brief: "MOD-φ CONVERGENCE, I: — In this paper, we use the framework of mod- φ convergence to prove pre- cise large or moderate deviations for quite general sequences of real valued random variables (Xn)n∈N"
---
(1) The random variables Xn satisfy the hypotheses of Deﬁnition 1.1 with c = + ∞
(in particular, ψ is entire on C).
(2) The Legendre-Fenchel transform F is essentially smooth, that is to say that
it takes ﬁnite values on a non-empty closed interval IF and that lim F′(x) =
lim h =±∞ when x goes to a bound of the interval IF (cf. [DZ98, Deﬁnition
2.3.5]).
The latter point is veriﬁed if φ is a Gaussian or Poisson law, which are the most impor-
tant examples.
Lemma 6.2. Let C be a closed subset of R. Either infu∈C F(u) = + ∞, or infu∈C F(u) = m
is attained and{x∈ C| F(x) = minu∈C F(u)} consists of one or two real numbers a ≤ b,
with a < η′(0) < b if a⁄= b.
ba
Cη′(0)
Fφ
2
FIGURE 6. The inﬁmum of F on an admissible closed set C is attained
either at a = sup(C∩ (−∞, η′(0)]), or at b = inf(C∩ [η′(0), +∞)), or at
both if F(a) = F(b).
Proof. Recall that F is strictly convex, since its second derivative is 1/ η′′(h), which is
the inverse of the variance of a non-constant random variable. Also, η′(0) is the point
where F attains its global minimum, and it is the expectation of the lawφ. If C∩ IF = ∅,
then F|C = + ∞ and we are in the ﬁrst situation. Otherwise, F|C is ﬁnite at some points,
so there exists M∈ R+ such that C∩{ x∈ R| F(x)≤ M}⁄ = ∅. However, the set{x∈
R| F(x)≤ M} is compact by the hypothesis of essential smoothness: it is closed as
the reciprocal image of an interval ]− ∞, M] by a lower semi-continuous function, and
bounded since limx→(IF)c|F′(x)| = + ∞. So, C∩{ x∈ R| F(x)≤ M} is a non-empty
compact set, and the lower semi-continuous F attains its minimum on it, which is also
minu∈C F(u). Then, if a≤ b are two points in C such that F(a) = F(b) = minu∈C F(u),
then by strict convexity of F, F(x) < F(a) for all x∈ (a, b), hence, (a, b)⊂ Cc. Also,
F(x) > F(a) if a⁄= b and x /∈ [a, b], so either a = b, or η′(0)∈ (a, b). □
We take the usual notations Bo and B for the interior and the closure of a subset
B⊂ R. Call admissible a (Borelian) subset B⊂ R such that there exists b∈ B with
46 VALENTIN FÉRAY, PIERRE-LOÏC MÉLIOT, AND ASHKAN NIKEGHBALI
F(b) < +∞, and denote then
F(B) = inf
u∈B
F(u) = min
u∈B
F(u),
and Bmin ={a∈ B| F(a) = F(B)}; according to the previous discussion,Bmin consists
of one or two elements.
