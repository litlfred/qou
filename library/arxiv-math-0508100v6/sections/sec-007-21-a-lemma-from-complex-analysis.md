---
doc_id: arxiv-math-0508100v6
doc_title: "ASYMPTOTICS OF THE COLORED JONES FUNCTION OF A KNOT"
section_id: sec-007-21-a-lemma-from-complex-analysis
section_title: "A lemma from complex analysis"
section_number: 2.1
pages: 8-8
source_pdf: 0508100v6.pdf
source_sha256: 9cc100a86b40c336
doc_brief: "ASYMPTOTICS OF THE COLORED JONES FUNCTION OF A KNOT — To a knot in 3-space, one can associate a sequence of Laurent p olynomials, whose nth term is the nth colored Jones polynomial."
---
of Theorem 1.2 to the strong convergence. This uses the next lemma on normal fa milies that is sometimes
referred to by the name of Vitali or Montel’s theorem. For a reference, see [ Hil62, Sch93]. The lemma
exhibits the power of holomorphy, coupled with uniform boundednes s.
Lemma 2.1. If
fn : {z ∈ C : |z| < r } → { z ∈ C : |z| ≤ M }
is a uniformly bounded sequence of holomorphic functions such that for every m ≥ 0, we have:
lim
n→∞
f (m)
n (0) = am.
Then,
• The limit f (z) = lim n fn(z) exists pointwise for all z with |z| < r .
• f is holomorphic,
• The convergence is uniform on compact subsets, and
• For every m, f (m)(0) = am.
In other words, weak convergence and uniform boundedness imply strong convergence.
Proof. {fn}n is uniformly bounded, so it is a normal family, and contains a converge nt subsequence fj → f .
Convergence is uniform on compact sets, and f is holomorphic, and for every m ≥ 0, limj f (m)
j (0) = f (m)(0) =
am.
If {fn}n is not convergent (uniformly on compact sets), since it is a normal f amily, then there exist two
subsequences that converge to f and g respectively, with f ⁄= g. Applying the above discussion, it follows
that f and g are holomorphic functions with equal derivatives of all orders at 0. Thus, f = g, giving a
contradiction. □
Theorem 1.3 follows from Lemma 2.1 and the following result, whose proof will be given in Section 4.
Theorem 2.2. (Proof in Section 4.2) For every knot K there exists an open neighborhood UK of 0 ∈ C and
a positive number M such that for α ∈ UK, and all n ≥ 1, we have:
|fK,n (α)| < M.
2.2. The main diﬃculty for uniform bounds. Before we proceed with the proof of Theorem 2.2, let
us point out the main diﬃculty. As we will see later, JK,n (q) is a Laurent polynomial in q whose span
(i.e., the exponents of its monomials) are O(n2) and whose coeﬃcients are eO(n). In addition, due to our
normalization, JK,n (1) = 1. In other words, the O(n2) many exponentially growing coeﬃcients of JK,n (q)
add up to 1. When we evaluate JK,n (eα/n ), we want to bound the result independent of n. This will happen
only if major cancellations occur. How can we control these cancella tions? The answer to this is a key
cyclotomic expansion of the colored Jones function, which we review next.
