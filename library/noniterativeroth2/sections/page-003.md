---
doc_id: noniterativeroth2
doc_title: "A PROOF OF ROTH’S THEOREM ON ARITHMETIC PROGRESSIONS"
section_id: page-003
section_title: "Page 3"
section_number: null
pages: 3-3
source_pdf: noniterativeroth2.pdf
source_sha256: 83bbcdf45da069e5
toc_source: undetermined
doc_brief: "A PROOF OF ROTH’S THEOREM ON ARITHMETIC PROGRESSIONS — We present a proof of Roth’s theorem that follows a slightly diﬀerent structure to the usual proofs, in that there is not much iteration."
---
A PROOF OF ROTH’S THEOREM ON ARITHMETIC PROGRESSIONS
3
Let S ⊂[N] be a set free of three term progressions with |S| = r3(N). Thinking of S as
a subset of Fp in the obvious way, we shall write f = 1S : Fp →{0, 1} for the indicator
function of S. Let
R := {r ∈Fp : | bf(r)| ⩾(2 log log p/ log p)1/2}.
By Parseval’s identity, this set of large Fourier coeﬃcients cannot be too big; certainly,
|R| ⩽log p/2 log log p.
We may therefore dilate these points of R to be contained in a short part of Fp. Indeed,
by Dirichlet’s box principle there is an integer dilate x satisfying
|x| < p1−1/(|R|+1) ≪p/ log p,
such that
∥xr/p∥T ⩽p−1/(|R|+1) < 1/ log p.
(3.1)
Taking such an x, deﬁne
B := {0, x, 2x},
and deﬁne h to be the normalised indicator function for B, given by
h(n) := 1B(n)/3.
Then, we convolve f with h, to produce the new function
g(n) := (f ∗h)(n) = (f(n) + f(n −x) + f(n −2x))/3.
Since
bf(r) −bg(r) = bf(r)(1 −bh(r)),
it is easy to check using (3.1) that
| bf(r) −bg(r)| ≪(log log p/ log p)1/2.
From this, along with the Cauchy-Schwarz inequality, Parseval’s identity, and equation
(2.1), one can quickly deduce that
|Λ(f) −Λ(g)| ≪(log log p/ log p)1/2,
and therefore since Λ(f) ≪1/p (because S is free of three term arithmetic progressions),
we deduce
Λ(g) ≪(log log p/ log p)1/2.
(3.2)
Deﬁne
T := {n ∈Fp : g(n) > 0},
and note that from (3.2), along with the obvious facts Λ(T) ≪Λ(g), we deduce
Λ(T) ≪(log log p/ log p)1/2.
We furthermore have that since |x| ≪p/ log p, the set T is a subset of [N +O(N/ log p)].
So, if we let T ′ be those elements of T lying in [N], then
|T ′| = |T| −O(p/ log p), and Λ(T ′) ⩽Λ(T).
We have now created a set T ′, potentially much larger than S, but with only a few
more three term progressions. The following lemma, a variant of Varnavides’ theorem
