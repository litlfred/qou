---
doc_id: arxiv-math-0304010v1
doc_title: "Kerov's central limit theorem for the Plancherel measure on Young diagrams"
section_id: page-028
section_title: "Page 28"
section_number: null
pages: 28-28
source_pdf: 0304010v1.pdf
source_sha256: fc2296c027b3feb0
toc_source: undetermined
doc_brief: "Kerov's central limit theorem for the Plancherel measure on Young diagrams — Consider random Young diagrams with ﬁxed number n of boxes, dis- tributed according to the Plancherel measure Mn."
---
The right–hand side was found in Proposition 5.3, while the left–hand side can be
evaluated using Proposition 3.7. The result is the same, which concludes the proof
of (5.3).
Now let us show that (5.3) implies (5.2). Indeed, (5.2) is equivalent to
lim
n→∞
Z ¯λ(x) −|x|
2
xkdx =
Z Ω(x) −|x|
2
xkdx
in probability, for k = 0, 1, . . . .
By Proposition 2.2, this is equivalent to
lim
n→∞epk[¯λ( · )] = epk[Ω]
in probability, for k = 2, 3, . . . .
Applying Chebyshev’s inequality we see that to prove this, it suﬃces to check that
the ﬁrst and the second moments of the random variable epk[¯λ( · )] converge, as
n →∞, to epk[Ω] and ep 2
k [Ω], respectively. But this is a particular case of (5.3)
corresponding to f = epk and f = ep 2
k , respectively.
□
Theorem 5.5 (Law of large numbers, 2nd form). Let λ range over Yn, and
let us view ¯λ( · ) as a random function deﬁned on the probability space (Yn, Mn),
where Mn is the Plancherel measure. Let Ωbe as above. Then we have
lim
n→∞sup
x∈R
|¯λ(x) −Ω(x)| = 0
in probability.
(5.5)
We need two lemmas.
Lemma 5.6. There exists an interval I ⊂R such that the probability that ¯λ(x)−|x|
is supported by I tends to 1 as n →∞.
Proof. This follows from a ﬁner result due to Hammersley [Ha]. He has proved that
there exists a constant c such that for any ε > 0
lim
n→∞Mn{λ ∈Yn | |λ1 −c√n| < ε,
|λ′
1 −c√n| < ε} = 1.
Actually, the constant c equals 2 (this was ﬁrst proved by Vershik–Kerov [VeK1],
[VeK3]), and at present much more is known about the asymptotics of λ1, see, e.g.,
the expository paper [AD]. But, for our purpose, the old Hammersley’s result is
enough.
□
Lemma 5.7. Fix an interval I = [a, b] ⊂R, and let Σ denote the set of all real–
valued functions σ(x) on R, supported by I and satisfying the Lipschitz condition
|σ(x1) −σ(x2)| ≤|x1 −x2|.
On the set Σ, the weak topology deﬁned by the functionals
σ 7→
Z
σ(x)xkdx,
k = 0, 1, . . .,
coincides with the uniform topology deﬁned by the supremum norm ∥σ∥= sup |σ(x)|.
This fact was pointed out in [Ke2, §2.5].
Proof. Clearly, the uniform topology is stronger than the weak topology. Let us
check the inverse claim. Given x ∈I and ε > 0, let
V (x, ε) = {σ ∈Σ | |σ(x)| ≤ε}.
28
