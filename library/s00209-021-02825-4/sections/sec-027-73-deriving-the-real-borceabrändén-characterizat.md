---
doc_id: s00209-021-02825-4
doc_title: "A representation theoretic explanation of the Borcea–Brändén characterization"
section_id: sec-027-73-deriving-the-real-borceabrändén-characterizat
section_title: "Deriving the real Borcea–Brändén characterization"
section_number: 7.3
pages: 29-30
source_pdf: s00209-021-02825-4.pdf
source_sha256: 85ca5ec21f42a988
toc_source: outline
doc_brief: "A representation theoretic explanation of the Borcea–Brändén characterization — In 2009, Borcea and Brändén characterized all linear operators on multivariate polynomials which preserve the property"
---
As in the complex case, we now obtain the Borcea–Brändén weak real stability character-
ization as a corollary to our strong real stability characterization given in Theorem 7.2. To
this end, we start by giving a sort of real stability version of Lemma 6.11. The proof of this
lemma is similar in spirit to that of the strong real stability characterization given above.
Lemma 7.3 Fix λ, α ∈Nm
0 and a linear operator T ∈Hom(V (λ), V (α)) such that T
restricts to a real linear operator from VR(λ) to VR(α). The following are equivalent.
(i) T preserves weak real stability.
(ii) One of the following holds:
(a) T maps H+
m-stable polynomials to nonzero Hm
+-stable polynomials.
(b) T maps H+
m-stable polynomials to nonzero Hm
−-stable polynomials.
(c) T has image of dimension at most two, and is of the form
T : p →q · ψ1(p) + r · ψ2(p)
where q,r ∈VR(α) are weakly real stable such that q ≪r, and ψ1, ψ2 are real
linear functionals.
Proof (i) ⇒(ii). By the complex characterization (Theorem 6.2), we only need to consider
evaluation symbols when demonstrating (a) or (b). For any (z0 : w0) ∈Hm
−, Lemma 4.10
then implies T [(w0x −z0y)λ] is either Hm
+-stable, Hm
−-stable, or identically zero. We now
show that (c) holds if (a) and (b) do not.
If neither (a) nor (b) holds for evaluation symbols, then there exist (z0 : w0), (z′
0 : w′
0) ∈
Hm
−such that T [(w0x −z0y)λ] is Hm
+-stable or zero and T [(w′
0x −z′
0y)λ] is Hm
−-stable or
zero. As in the proof of the strong real stability characterization (Theorem 7.2), a homotopy
argument implies there exists (z′′
0 : w′′
0) ∈Hm
−such that T [(w′′
0x −z′′
0 y)λ] is (Hm
+ ∪Hm
−)-
stable or zero. Lemma 4.11 then implies T [c0(w′′
0x −z′′
0 y)λ] is real stable or zero, for some
complex scalar c0̸ = 0.
For the sake of simplicity, we denote q0(x, y) = q0(x1, y1, . . . , xm, ym) := c0(w′′
0x −
z′′
0 y)λ. Since the set of H+
m-stable polynomials is open in V (λ), let B(0) be some open
ball centered at 0 such that q0 + i B(0) consists of nonzero H+
m-stable polynomials. So,
for any r0 ∈B(0), Lemma 4.10 implies T (q0) + iT (r0) is either Hm
+-stable, Hm
−-stable, or
zero. Hermite-Biehler then implies T (r0) is real stable or zero whenever r0 ∈B(0) ∩VR(λ).
Therefore, T [VR(λ)] consists of real stable polynomials, and (c) follows from Lemma 4.12.
(ii) ⇒(i). If (c) holds, then (i) follows from Hermite-Biehler. Otherwise, suppose WLOG
that (a) holds. We can then use an argument similar in spirit to that of Lemma 6.11 to show
that T maps Hm
+-stable polynomials to weakly Hm
+-stable polynomials. Since T restricts to
a real operator, this implies (i).
⊓⊔
As in Lemma 6.11, we use the previous lemma to link the characterizations of weak and
strong stability preserving operators as follows. Applying the necessary maps to convert
Symb(T ) to SymbBB(T ) below gives essentially the characterization of weak real stability
preserving operators given in Theorem 1.2.
Corollary 7.4 Fix λ, α ∈Nm
0 and a linear operator T ∈Hom(V (λ), V (α)) such that T
restricts to a real linear operator from VR(λ) to VR(α). The following are equivalent.
(i) T preserves weak real stability.
1388
J. Leake
(ii) One of the following holds:
(a) Symb(T ) is (Hm
−× Hm
+)-stable.
(b) Symb(T ) is (Hm
−× Hm
−)-stable.
(c) T has image of dimension at most two, and is of the form
T : p →q · ψ1(p) + r · ψ2(p)
where q,r ∈VR(α) are weakly real stable such that q ≪r, and ψ1, ψ2 are real
linear functionals.
Proof Apply the complex characterization (Theorem 6.2) to conditions (ii)(a) and (ii)(b) of
Lemma 7.3 above.
⊓⊔
