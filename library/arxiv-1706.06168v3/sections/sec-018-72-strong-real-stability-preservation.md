---
doc_id: arxiv-1706.06168v3
doc_title: "A Representation Theoretic Explanation of the Borcea-Brändén Characterization"
section_id: sec-018-72-strong-real-stability-preservation
section_title: "Strong Real Stability Preservation"
section_number: 7.2
pages: 24-26
source_pdf: 1706.06168v3.pdf
source_sha256: ab3383a95f369922
---
We state and prove our strong real stability preservation charac terization here, and then derive the Borcea-
Br¨ and´ en characterization as a corollary. The proof here takes a bit more work than in the complex case,
and will rely on many of the real stability results discussed in §4.3. This extra work is essentially taken from
the proof of Theorem 1.2 found in [ BB09a].
Theorem 7.2. Fix λ ∈ Nm
0 , α ∈ Nl
0, and a linear operator T ∈ Hom(V (λ),V (α)) such that T restricts to a
real linear operator from VR(λ) to VR(α). The following are equivalent.
(i) T preserves strong real stability.
(ii) Symb(T ) is either (H−
m
× Hl
+)-stable or (H−
m
× Hl
−)-stable.
Proof. (i) ⇒ (ii). Fixing ( z0 :w0) ∈ H−
m
, we have that ( w0x −z0y)λ is Hm
+ -stable. If ( z0 :w0) ∈ R
m
, then
T [(w0x −z0y)λ] is nonzero and real stable by assumption. Combining the symbol lem ma (Lemma 3.7) and
the evaluation symbol lemma (Lemma 5.10), this implies Symb( T )(z0,w 0,x,y ) = ( −1)λT [(w0x −z0y)λ] is
both Hl
+-stable and Hl
−-stable.
On the other hand, suppose ( z0 :w0) ⁄∈R
m
. By Lemma 4.10, we have that T [(w0x −z0y)λ] is either Hl
+-
stable, Hl
−-stable, or zero. Now suppose there are ( z0 :w0), (z′
0 :w′
0) ∈ H−
m
\ R
m
such that T [(w0x −z0y)λ]
24
is Hl
+-stable and T [(w′
0x −z′
0y)λ] is Hl
−-stable. By a homotopy argument, there exists ( z′′
0 :w′′
0 ) ∈ H−
m
\ R
m
such that T [(w′′
0x −z′′
0y)λ] is ( Hl
+ ∪ H l
−)-stable or zero. By Lemma 4.11, T [c0(w′′
0x −z′′
0y)λ] is either real
stable or zero for some complex scalar c0 ⁄= 0.
Let c0(w′′
0x −z′′
0y)λ =q(x,y ) +ir(x,y ) for q,r ∈VR(λ), which are both real stable or zero by Hermite-
Biehler (Proposition 4.9). Note further that r ⁄≡0 since ( z′′
0 : w′′
0 ) ⁄∈R
m
. However, since T (q +ir) =
T (q) +iT (r) is real stable or zero and T restricts to real linear operator, it must be that T (r) ≡ 0. This
contradicts the fact that T strongly preserves real stability.
So, Symb(T )(z0,w 0,x,y ) = ( −1)λT [(w0x −z0y)λ] is either Hl
+-stable (in the x,y variables) for all ( z0 :
w0) ∈ H−
m
\ R
m
, or Hl
−-stable for all ( z0 :w0) ∈ H−
m
\ R
m
. Combining this with the ( z0 :w0) ∈ R
m
case,
we have that Symb(T ) is either ( H−
m
× Hl
+)-stable or ( H−
m
× Hl
−)-stable.
(ii) ⇒ (i). By the complex stability characterization (Theorem 6.2), T maps Hm
+ -stable polynomials to
either nonzero Hl
+-stable polynomials or nonzero Hl
−-stable polynomials. Since T restricts to a real linear
operator on VR(λ), T preserves strong real stability.
As a ﬁnal note, the “homotopy argument” used in the previous pro of is not quite that of the proof found
in [ BB09a], though it is similar. Here, one just needs to be a bit more careful ab out the precise homotopy
with respect to points at inﬁnity.
7.3 Deriving the Real Borcea-Br¨ and´ en Characterization
As in the complex case, we now obtain the Borcea-Br¨ and´ en weak real stability characterization as a corollary
to our strong real stability characterization given in Theorem 7.2. To this end, we start by giving a sort of
real stability version of Lemma 6.11. The proof of this lemma is similar in spirit to that of the strong real
stability characterization given above.
Lemma 7.3. Fix λ,α ∈ Nm
0 and a linear operator T ∈ Hom(V (λ),V (α)) such that T restricts to a real
linear operator from VR(λ) to VR(α). The following are equivalent.
(i) T preserves weak real stability.
(ii) One of the following holds:
(a) T maps H+
m
-stable polynomials to nonzero Hm
+ -stable polynomials.
(b) T maps H+
m
-stable polynomials to nonzero Hm
− -stable polynomials.
(c) T has image of dimension at most two, and is of the form
T :p ↦→q ·ψ1(p) +r ·ψ2(p)
whereq,r ∈VR(α) are weakly real stable such that q ≪r, and ψ1,ψ 2 are real linear functionals.
Proof. (i) ⇒ (ii). By the complex characterization (Theorem 6.2), we only need to consider evaluation
symbols when demonstrating ( a) or (b). For any ( z0 :w0) ∈ H m
− , Lemma 4.10 then implies T [(w0x −z0y)λ]
is either Hm
+ -stable, Hm
− -stable, or identically zero. We now show that ( c) holds if ( a) and (b) do not.
If neither ( a) nor ( b) holds for evaluation symbols, then there exist ( z0 : w0), (z′
0 : w′
0) ∈ H m
− such that
T [(w0x −z0y)λ] is Hm
+ -stable or zero and T [(w′
0x −z′
0y)λ] is Hm
− -stable or zero. As in the proof of the strong
real stability characterization (Theorem 7.2), a homotopy argument implies there exists ( z′′
0 : w′′
0 ) ∈ H m
−
such that T [(w′′
0x −z′′
0y)λ] is ( Hm
+ ∪ Hm
− )-stable or zero. Lemma 4.11 then implies T [c0(w′′
0x −z′′
0y)λ] is real
stable or zero, for some complex scalar c0 ⁄= 0.
For the sake of simplicity, we denote q0(x,y ) = q0(x1,y 1,...,x m,y m) := c0(w′′
0x −z′′
0y)λ. Since the set
of H+
m
-stable polynomials is open in V (λ), let B(0) be some open ball centered at 0 such that q0 +iB(0)
consists of nonzero H+
m
-stable polynomials. So, for any r0 ∈ B(0), Lemma 4.10 implies T (q0) +iT (r0) is
either Hm
+ -stable, Hm
− -stable, or zero. Hermite-Biehler then implies T (r0) is real stable or zero whenever
r0 ∈B(0) ∩VR(λ). Therefore, T [VR(λ)] consists of real stable polynomials, and ( c) follows from Lemma 4.12.
25
(ii) ⇒ (i). If ( c) holds, then ( i) follows from Hermite-Biehler. Otherwise, suppose WLOG that ( a)
holds. We can then use an argument similar in spirit to that of Lemma 6.11 to show that T maps Hm
+ -stable
polynomials to weakly Hm
+ -stable polynomials. Since T restricts to a real operator, this implies ( i).
As in Lemma 6.11, we use the previous lemma to link the characterizations of weak and strong stability
preserving operators as follows. Applying the necessary maps to c onvert Symb(T ) to Symb BB (T ) below
gives essentially the characterization of weak real stability preser ving operators given in Theorem 1.2.
Corollary 7.4. Fix λ,α ∈ Nm
0 and a linear operator T ∈ Hom(V (λ),V (α)) such that T restricts to a real
linear operator from VR(λ) to VR(α). The following are equivalent.
(i) T preserves weak real stability.
(ii) One of the following holds:
(a) Symb(T ) is (Hm
− × Hm
+ )-stable.
(b) Symb(T ) is (Hm
− × Hm
− )-stable.
(c) T has image of dimension at most two, and is of the form
T :p ↦→q ·ψ1(p) +r ·ψ2(p)
whereq,r ∈VR(α) are weakly real stable such that q ≪r, and ψ1,ψ 2 are real linear functionals.
Proof. Apply the complex characterization (Theorem 6.2) to conditions ( ii)(a) and ( ii)(b) of Lemma 7.3
above.
