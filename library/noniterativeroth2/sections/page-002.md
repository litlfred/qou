---
doc_id: noniterativeroth2
doc_title: "A PROOF OF ROTH’S THEOREM ON ARITHMETIC PROGRESSIONS"
section_id: page-002
section_title: "Page 2"
section_number: null
pages: 2-2
source_pdf: noniterativeroth2.pdf
source_sha256: 83bbcdf45da069e5
toc_source: undetermined
doc_brief: "A PROOF OF ROTH’S THEOREM ON ARITHMETIC PROGRESSIONS — We present a proof of Roth’s theorem that follows a slightly diﬀerent structure to the usual proofs, in that there is not much iteration."
---
2
ERNIE CROOT AND OLOF SISASK
number of Fourier coeﬃcients; and, (2) one has a quantative version of Varnavides’s
theorem. This might prove especially useful in certain contexts, because the particular
sets on which our method achieves a density increment (via Varnavides) are unrelated
to the particular additive characters where the Fourier transform of S is “large”. 1
2. Notation
We shall require a modicum of notation: given a function f : Fp →[0, 1], we write
Λ(f) := Ex,d∈Fpf(x)f(x + d)f(x + 2d)
(where E represents an averaged sum; thus the E above represents p−2 P). Thus Λ
gives an average of f over three term arithmetic progressions; when f is the indicator
function of a set A, this is just the number of progressions in A divided by p2. We shall
make use of the Fourier transform bf : Fp →C of a function f, given by
bf(r) := Ex∈Fpf(x)e2πirx/p,
as well as the easily-veriﬁed Parseval’s identity
X
r∈Fp
| bf(r)|2 = Ex|f(x)|2.
It is also easy to check that
Λ(f) =
X
r∈Fp
bf(r)2 bf(−2r).
(2.1)
Given a set T ⊆Fp, we will furthermore use the notation
Λ(T) := Λ(1T).
Finally, we will use the notation ||t||T to denote the distance from t to the nearest
integer.
3. Proof of Theorem 1.1
Let
κ := lim sup
N→∞
r3(N)/N.
We shall show that κ = 0, which will prove the theorem.
Let N ⩾2 be an integer, and then let p be a prime number satisfying
2N < p < 2N(1 + O(1/ log N)).
The fact that such p exist is a consequence of the Prime Number Theorem.
1That is, the progression to which we pass with each iteration, is unrelated to the additive characters
of places where ˆS is “large”.
