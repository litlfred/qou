---
doc_id: arxiv-0903.0853v3
doc_title: "Local analytic classification of q-difference equations"
section_id: sec-121-51-some-preparatory-notations-and-results-69
section_title: "SOME PREPARATORY NOTATIONS AND RESULTS 69"
section_number: 5.1
pages: 75-77
source_pdf: 0903.0853v3.pdf
source_sha256: d4295d4b18b2f08f
doc_brief: "Local analytic classification of q-difference equations — 229 sections: Vector bundles associated to q-diﬀ; The q-Euler equation and conﬂuent ; The symmetric square of the q-Eule"
---
Letλ,µ∈ C∗; since:
⏐
⏐
⏐
⏐1− z
µqn
⏐
⏐
⏐
⏐≥
⏐
⏐
⏐z
λ
⏐
⏐
⏐
⏐
⏐
⏐
⏐1− λ
µqn
⏐
⏐
⏐
⏐−
⏐
⏐
⏐1− z
λ
⏐
⏐
⏐,
one gets:
(5.1) dq(z, [µ])≥dq(λ, [µ])−ρ
(
1 +dq(λ, [µ])
)
when z∈D([λ];ρ) and ρ<M q.
Proposition 5.1.2. — Given two distinct q-spirals [λ] and [µ], there exists
a constant N >1 such that, for all ρ> 0 near enough from 0, if dq(z, [λ])>ρ
and dq(z, [µ])>ρ , then:
dq(z, [λ])dq(z, [µ])> ρ
N·
Proof. — By contradiction, assume that, for all N > 1, there exists
ρN > 0 and z ∈ C∗ such that dq(z, [λ]) > ρN and dq(z, [µ]) > ρN but
dq(z, [λ])dq(z, [µ])≤ ρN
N ; this would entail:
ρN <d q(z, [λ])< 1
N,
whence, after (5.1):
dq(z, [µ])≥dq(λ, [µ])−
(
1 +dq(λ, [µ])
)
/N.
In other words, when N→∞ , one would get:
dq(z, [λ])dq(z, [µ]) /greaterorsimilardq(λ, [µ]) ρN
(i.e. there is an inequality up to an o(1) term), contradicting the assumption
dq(z, [λ]) dq(z, [µ])< ρN
N .
Let Λ := ν1[λ1] +··· +νm[λm] be a divisor and let ρ> 0. We put:
(5.2) dq(z, Λ) :=
∏
1≤j≤m
(dq(z, [λj]))νj
and
D(Λ;ρ) :={z∈ C∗| dq(z, Λ)≤ρ} , D c(Λ;ρ) := C∗\D(Λ;ρ).
Proposition 5.1.2 implies that, if Λ = [λ] + [µ] with [λ]⁄= [µ], one has:
Dc([λ];ρ)∩Dc([µ];ρ)⊂Dc
(
Λ; ρ
N
)
as long as ρ is near enough from 0.
70 CHAPTER 5. SUMMATION AND ASYMPTOTIC THEORY
Proposition 5.1.3. — Let Λ :=ν1[λ1] +··· +νm[λm] be a divisor such that
[λi]⁄= [λj] for i⁄= j. There exists a constant N > 1 such that, for all ρ >0
near enough from 0, one has:
(5.3) Dc(Λ;ρ)⊂
⋂
1≤j≤m
Dc([λj];ρ1/νj)⊂Dc
(
Λ; ρ
N
)
.
Proof. — The ﬁrst inclusion comes from the fact that, if dq(z, [λj])≤ǫ1/νj for
some index j, then dq(z, Λ)≤ǫ, because dq(z, [λ])≤ 1 for all λ∈ C∗.
To prove the second inclusion, we use (5.1) in the same way as i n the proof
of proposition 5.1.2; details are left to the reader.
Taking the complementaries in (5.3), one gets:
(5.4) D
(
Λ; ρ
N
)
⊂
⋃
1≤j≤m
D
(
[λj];ρ1/νj
)
⊂D(Λ;ρ).
Modifying the deﬁnition (5.2) of dq(z, Λ) as follows:
(5.5) δ(z, Λ) := min
1≤j≤m
{dq(z, [λj])}νj,
one gets, for all small enough ρ:
Dδ(Λ;ρ) :={z∈ C∗ :δ(z, Λ)≤ρ} =
⋃
1≤j≤m
D([λj];ρ1/νj)
Relation (5.4) shows that the maps z ↦→dq(z, Λ) and z ↦→δ(z, Λ) deﬁne
equivalent systems of small neighborhoods relative to the d ivisor Λ; precisely,
for ρ→ 0:
D
(
Λ; ρ
N
)
⊂Dδ(Λ;ρ)⊂D(Λ;ρ).
Deﬁnition 5.1.4 . — Let ǫ≥ 0. We call germ of sector within distance ǫ
from divisor Λ any set:
S(Λ,ǫ ;R) ={z∈ C∗ :dq(z, Λ)>ǫ,|z|<R}, where R> 0.
When R = +∞, we write S(Λ,ǫ ) instead of S(Λ,ǫ ; +∞).
Note that S(Λ, 0;R) is the punctured open disk {0<|z|<R} deprived of
the q-spirals pertaining to divisor Λ. Since dq(z, Λ)≤ 1 for all z∈ C∗, one
has S(Λ, 1;R) = ∅; that is why we shall assume that ǫ∈]0, 1[. Last, each
sector within a short enough distance to Λ represents, on the elliptic curve
Eq = C∗/qZ, the curve Eq deprived of a family of ovals centered on the λj
with sizes varying like ǫ1/νj.
