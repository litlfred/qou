---
doc_id: s00209-021-02825-4
doc_title: "A representation theoretic explanation of the Borcea–Brändén characterization"
section_id: sec-026-72-strong-real-stability-preservation
section_title: "Strong real stability preservation"
section_number: 7.2
pages: 28-29
source_pdf: s00209-021-02825-4.pdf
source_sha256: 85ca5ec21f42a988
toc_source: outline
doc_brief: "A representation theoretic explanation of the Borcea–Brändén characterization — In 2009, Borcea and Brändén characterized all linear operators on multivariate polynomials which preserve the property"
---
We state and prove our strong real stability preservation characterization here, and then derive
the Borcea–Brändén characterization as a corollary. The proof here takes a bit more work
than in the complex case, and will rely on many of the real stability results discussed in Sect.
4.3. This extra work is essentially taken from the proof of Theorem 1.2 found in [1].
Theorem 7.2 Fix λ ∈Nm
0 , α ∈Nl
0, and a linear operator T ∈Hom(V (λ), V (α)) such that
T restricts to a real linear operator from VR(λ) to VR(α). The following are equivalent.
(i) T preserves strong real stability.
(ii) Symb(T ) is either (H−
m × Hl
+)-stable or (H−
m × Hl
−)-stable.
Proof (i) ⇒(ii). Fixing (z0 : w0) ∈H−
m, we have that (w0x −z0y)λ is Hm
+-stable. If
(z0 : w0) ∈R
m, then T [(w0x −z0y)λ] is nonzero and real stable by assumption. Combining
the symbol lemma (Lemma 3.7) and the evaluation symbol lemma (Lemma 5.10), this implies
Symb(T )(z0, w0, x, y) = (−1)λT [(w0x −z0y)λ] is both Hl
+-stable and Hl
−-stable.
Ontheotherhand,suppose(z0 : w0) /∈R
m.ByLemma4.10,wehavethat T [(w0x−z0y)λ]
is either Hl
+-stable, Hl
−-stable, or zero. Now suppose there are (z0 : w0), (z′
0 : w′
0) ∈
H−
m\R
m such that T [(w0x −z0y)λ] is Hl
+-stable and T [(w′
0x −z′
0y)λ] is Hl
−-stable. By
a homotopy argument, there exists (z′′
0 : w′′
0) ∈H−
m\R
m such that T [(w′′
0x −z′′
0 y)λ] is
(Hl
+ ∪Hl
−)-stable or zero. By Lemma 4.11, T [c0(w′′
0x −z′′
0 y)λ] is either real stable or zero
for some complex scalar c0̸ = 0.
Let c0(w′′
0x −z′′
0 y)λ = q(x, y) + ir(x, y) for q,r ∈VR(λ), which are both real stable or
zero by Hermite-Biehler (Proposition 4.9). Note further that r̸ ≡0 since (z′′
0 : w′′
0) /∈R
m.
However, since T (q + ir) = T (q) + iT (r) is real stable or zero and T restricts to real linear
operator, it must be that T (r) ≡0. This contradicts the fact that T strongly preserves real
stability.
So, Symb(T )(z0, w0, x, y) = (−1)λT [(w0x −z0y)λ] is either Hl
+-stable (in the x, y
variables) for all (z0 : w0) ∈H−
m\R
m, or Hl
−-stable for all (z0 : w0) ∈H−
m\R
m.
Combining this with the (z0 : w0) ∈R
m case, we have that Symb(T ) is either (H−
m ×Hl
+)-
stable or (H−
m × Hl
−)-stable.
(ii) ⇒(i). By the complex stability characterization (Theorem 6.2), T maps Hm
+-stable
polynomials to either nonzero Hl
+-stable polynomials or nonzero Hl
−-stable polynomials.
Since T restricts to a real linear operator on VR(λ), T preserves strong real stability.
⊓⊔
As a ﬁnal note, the “homotopy argument” used in the previous proof is not quite that of
the proof found in [1], though it is similar. Here, one just needs to be a bit more careful about
the precise homotopy with respect to points at inﬁnity.
A representation theoretic explanation...
1387
