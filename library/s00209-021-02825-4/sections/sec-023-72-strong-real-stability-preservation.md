---
doc_id: s00209-021-02825-4
doc_title: "Mathematische Zeitschrift (2022) 300:1359–1400 A representation theoretic explanation of the Borcea–Brändén characterization Jonathan Leake 1 © The Author(s) 2021"
section_id: sec-023-72-strong-real-stability-preservation
section_title: "Strong real stability preservation"
section_number: 7.2
pages: 27-29
source_pdf: s00209-021-02825-4.pdf
source_sha256: 85ca5ec21f42a988
doc_brief: "Mathematische Zeitschrift (2022) 300:1359–1400 A representation theoretic explanation of the Borcea–Brändén characterization Jonathan Leake 1 © The Author(s) 2021 — In 2009, Borcea and Brändén"
---
Borcea–Brändén characterization. In this section, we duplicate the outline of our previous
discussion on complex operators, making use of arguments similar to those found in [ 1]t o
ﬁll in the gaps.
Further, we also obtain a characterization of a certain class of operators which preserve
ray- and interval-rootedness. The question of a full characterization of such operators is as
of yet still an open problem (see [ 3]). Here, we answer this question for operators which
preserve both strong ray- or interval-rootedness as well as weak real-rootedness.
7.1 Weak real stability preservation
Borcea and Brändén obtain the following characterization of weak real stability preserving
linear operators. Recall the notion of proper position (denoted by ≪ ) given in Deﬁnition 4.8.
Theorem 1.2 (Borcea–Brändén) Fixλ ∈ Nm
0 and any linear operator T: Rλ[x1,..., xm]→
R[x1,..., xm]. The following are equivalent.
(i) T maps real stable polynomials to weakly real stable polynomials.
(ii) One of the following holds:
(a) Symb BB (T) is H2m
+ -stable.
(b) Symb BB (T) is (Hm
− × Hm
+)-stable.
(c) T has image of dimension at most two, and is of the form
T : p ↦→ q · ψ1(p) + r · ψ2(p)
where q, r ∈ R[x1,..., xm] are weakly real stable such that q ≪ r , and ψ1,ψ 2 are
real linear functionals.
As in the case of complex operators, the degeneracy condition (ii)(c) is the result of allow-
ing weak real stability preserving operators. We now give an example which demonstrates
its necessity.
123
1386 J. Leake
Example 7.1 Deﬁne T : Rn[x]→ R[x] via:
T :
n∑
k=0
( n
k
)
ak xk ↦→ an xn + an−2xn−1 = (an x + an−2)xn−1
This operator obviously preserves weak real stability. We then have that Symb BB (T) =
(z2 + x)xn−1, which is not H2
+-stable nor (H− × H+)-stable.
Again, the degeneracy condition is required for the characterization but obscures the con-
nection between an operator and its symbol. To remove it, we now turn to our characterization
of strong real stability preserving operators.
7.2 Strong real stability preservation
We state and prove our strong real stability preservation characterization here, and then derive
the Borcea–Brändén characterization as a corollary. The proof here takes a bit more work
than in the complex case, and will rely on many of the real stability results discussed in Sect.
4.3. This extra work is essentially taken from the proof of Theorem 1.2 found in [1].
Theorem 7.2 Fix λ ∈ Nm
0 , α ∈ Nl
0, and a linear operator T ∈ Hom(V(λ), V(α)) such that
T restricts to a real linear operator from VR(λ) to VR(α). The following are equivalent.
(i) T preserves strong real stability.
(ii) Symb (T) is either (H−
m × Hl
+)-stable or (H−
m × Hl
−)-stable.
Proof (i) ⇒ (ii). Fixing (z0 : w0) ∈ H−
m ,w eh a v et h a t(w0x − z0 y)λ is Hm
+-stable. If
(z0 : w0) ∈ R
m
,t h e nT[(w0x − z0 y)λ] is nonzero and real stable by assumption. Combining
the symbol lemma (Lemma3.7) and the evaluation symbol lemma (Lemma5.10), this implies
Symb(T)(z0,w 0, x, y) = (−1)λT[(w0x − z0 y)λ] is both Hl
+-stable and Hl
−-stable.
On the other hand, suppose(z0 : w0)/∈ R
m
. By Lemma4.10,w eh a v et h a tT[(w0x−z0 y)λ]
is either Hl
+-stable, Hl
−-stable, or zero. Now suppose there are (z0 : w0), (z′
0 : w′
0) ∈
H−
m\R
m
such that T[(w0x − z0 y)λ] is Hl
+-stable and T[(w′
0x − z′
0 y)λ] is Hl
−-stable. By
a homotopy argument, there exists (z′′
0 : w′′
0) ∈ H−
m\R
m
such that T[(w′′
0 x − z′′
0 y)λ] is
(Hl
+ ∪ Hl
−)-stable or zero. By Lemma 4.11, T[c0(w′′
0 x − z′′
0 y)λ] is either real stable or zero
for some complex scalar c0 ⁄= 0.
Let c0(w′′
0 x − z′′
0 y)λ = q(x, y) + ir (x, y) for q, r ∈ VR(λ), which are both real stable or
zero by Hermite-Biehler (Proposition 4.9). Note further that r ⁄≡ 0s i n c e(z′′
0 : w′′
0)/∈ R
m
.
However, since T(q + ir ) = T(q) + iT (r) is real stable or zero and T restricts to real linear
operator, it must be that T(r) ≡ 0. This contradicts the fact that T strongly preserves real
stability.
So, Symb(T)(z0,w 0, x, y) = (−1)λT[(w0x − z0 y)λ] is either Hl
+-stable (in the x, y
variables) for all (z0 : w0) ∈ H−
m\R
m
,o r Hl
−-stable for all (z0 : w0) ∈ H−
m\R
m
.
Combining this with the (z0 : w0) ∈ R
m
case, we have that Symb(T) is either (H−
m × Hl
+)-
stable or (H−
m × Hl
−)-stable.
(ii) ⇒ (i). By the complex stability characterization (Theorem 6.2), T maps Hm
+-stable
polynomials to either nonzero Hl
+-stable polynomials or nonzero Hl
−-stable polynomials.
Since T restricts to a real linear operator on VR(λ), T preserves strong real stability. ⊓⊔
As a ﬁnal note, the “homotopy argument” used in the previous proof is not quite that of
the proof found in [1], though it is similar. Here, one just needs to be a bit more careful about
the precise homotopy with respect to points at inﬁnity.
123
A representation theoretic explanation... 1387
