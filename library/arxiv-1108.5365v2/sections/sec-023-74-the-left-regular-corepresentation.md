---
doc_id: arxiv-1108.5365v2
doc_title: "Representation of the Quantum Plane, its Quantum"
section_id: sec-023-74-the-left-regular-corepresentation
section_title: "The left regular corepresentation"
section_number: 7.4
pages: 66-72
source_pdf: 1108.5365v2.pdf
source_sha256: 000961ede2234231
doc_brief: "Representation of the Quantum Plane, its Quantum — We give complete detail of the description of the GNS represe ntation of the quantum plane A and its dual ˆA as a von Neumann algebra."
---
With the construction of the multiplicative unitary W, we can talk about the
corepresentation induced by it. By the unitary transformations g iven in Section
6.3, we can choose the Hilbert space to be Hcorep⊗ ˆHcorep so that the action can
be nicely described.
66
Recall that the left regular corepresentation is given by
f⊗g↦→W′(f⊗g⊗ 1⊗ 1), (7.58)
where f⊗g∈H corep⊗ ˆHcorep and W′ = W3412∈B (Hcorep⊗ ˆHcorep)⊗A⊗ ˆA.
Here we realize A⊗ ˆA as operators in the 3rd and 4th components.
Theorem 7.20. The left regular corepresentation is given by
f (s1,t 1)g(s2,t 2)↦→
=
∫
R+i0
∫
R
∫
C
f (s1−α +τ,t 1−σ)g(s2 +σ,t 2)
Gb(−iσ)Gb(−iα +iσ)Gb( Q
2 +is1−it1 +iτ )Gb( Q
2 +is1−is2−iσ +iτ )
Gb(Q +iτ )Gb( Q
2 +is1−it1−iα +iσ +iτ )Gb( Q
2 +is1−is2−iα +iτ )
e2πiσ(t1−s1−τ )e2πis1τAib−1s1Bib−1τ⊗ ˆBib−1α ˆAib−1(t1+s2−s1−τ )dσdαdτ,
where the contour C of σ goes above σ = 0 and below σ =α.
Proof. Since we have used a permutation, now W′ reads
W′ = W3412 =W31V ′′
14 ˆW42V ∗
14. (7.59)
On the spaceHcorep⊗ ˆHcorep, the coaction of the components of W is given by:
W31 :f (s1,t 1)g(s2,t 2) ↦→
∫
R+i0
f (s1 +τ,t 1)g(s2,t 2) e2πis1τ
Gb(Q +iτ )Aib−1sBib−1τdτ,
ˆW42 :f (s1,t 1)g(s2,t 2) ↦→
∫
R+i0
f (s1,t 1)g(s2 +σ,t 2)Gb(−iσ) ˆBib−1σ ˆAib−1s2dσ.
The actions for V andV ′′ are harder to describe since they involve formally Aib−1p.
Therefore we use S (cf. Proposition 6.17) to sent the ﬁrst component back to Hrep
67
and obtain their actions.
SV ∗
14S−1 :f⊗g
↦→ S·
( ∫
R+i0
Bib−1τ⊗ ˆBib−1τ ˆA−ib−1τGb(−iτ )dτ
)
e
i
2πb 2 log ˆA⊗log A·
∫
R
f (α−s1,α−t1)g(s2,t 2)Gb(Q
2−it1 +is1)e−2πi(α−s1)s1dα
= S·
∫
R+i0
∫
R
f (α−s1−τ,α−t1)g(s2,t 2)Gb(Q
2−it1 +is1 +iτ )Gb(−iτ )·
e−2πi(α−s1−τ )(s1+τ ) ˆBib−1τ ˆAib−1s1dαdτ
=
∫
R
∫
R+i0
∫
R
f (α−β +s1−τ,α−β +t1)g(s2,t 2)Gb( Q
2 +it1−is1 +iτ )Gb(−iτ )
Gb( Q
2 +it1−is1)
·
e−2πi(α−β+s1−τ )(β−s1+τ )e2πi(β−s1)s1 ˆBib−1τ ˆAib−1(β−s1)dαdτdβ
shifting α↦→α +β +τ,β ↦→β +s1:
=
∫
R
∫
R+i0
∫
R
f (s1 +α,t 1 +α +τ )g(s2,t 2)Gb( Q
2 +it1−is1 +iτ )Gb(−iτ )
Gb( Q
2 +it1−is1)
·
e−2πi(αβ+ατ +s1τ ) ˆBib−1τ ˆAib−1βdαdτdβ,
and ﬁnally for V ′′:
SV ′′
14S−1 :f⊗g
↦→ S·
(
e
i
2πb 2 log ˆA∗⊗log ˆA−1
∫
R+i0
ˆBib−1τ
∗ ⊗ ˆBib−1τeπiτ 2
Gb(−iτ )dτ
)
·
∫
R
f (α−s1,α−t1)g(s2,t 2)Gb(Q
2−it1 +is1)e−2πi(α−s1)s1dα
= S·
∫
R+i0
∫
R
f (α−s1α−t1 +τ )g(s2,t 2)Gb(Q
2−it1 +is1 +iτ )
e−2πi(α−s1)s1eπiτ 2
Gb(−iτ ) ˆA−ib−1t1 ˆBib−1τdαdτ
=
∫
R
∫
R+i0
∫
R
f (α−β +s1,α−β +t1 +τ )g(s2,t 2)Gb( Q
2 +it1−is1 +iτ )Gb(−iτ )
Gb( Q
2 +it1−is1)
e−2πi(α−β+s1)(β−s1)eπiτ 2
e2πi(β−s1)s1e2πiτ (t1−β) ˆBib−1τ ˆAib−1(t1−β)dαdτdβ
shifting α↦→α +β,β ↦→t1−β:
=
∫
R
∫
R+i0
∫
R
f (s1 +α,t 1 +α +τ )g(s2,t 2)Gb( Q
2 +it1−is1 +iτ )Gb(−iτ )
Gb( Q
2 +it1−is1)
e−2πiα(t1−s1)e2πiβ(α+τ )eπiτ 2
ˆBib−1τ ˆAib−1βdαdτdβ.
68
Combining, we have
f⊗g
↦→V ∗
∫
R
∫
R+iǫτ
∫
R
dαdτdβf (s1 +α,t 1 +α +τ )g(s2,t 2)·
Gb( Q
2 +it1−is1 +iτ )Gb(−iτ )
Gb( Q
2 +it1−is1)
e−2πi(αβ+ατ +s1τ ) ˆBib−1τ ˆAib−1β
↦→ˆW
∫
R+iǫσ
∫
R
∫
R+iǫτ
∫
R
dαdτdβdσf (s1 +α,t 1 +α +τ )g(s2 +σ,t 2)·
Gb( Q
2 +it1−is1 +iτ )Gb(−iτ )Gb(−iσ)
Gb( Q
2 +it1−is1)
e−2πi(αβ+ατ +s1τ )e2πis2τ ˆBib−1(σ+τ ) ˆAib−1(β+s2).
The integral for β and σ are independent, hence we can interchange them. Fur-
thermore from the decay properties for f⊗g and the asymptotic properties for
Gb(−iτ )Gb(−iσ), the integral for α,τ andσ is absolutely convergent, hence we can
interchange the order so that dσ goes to the inner most layer.
↦→V ′′
∫
R
∫
R+iǫ′
τ
∫
R
∫
R
∫
R+iǫτ
∫
R
∫
R+iǫσ
dσdαdτdβdα ′dτ ′dβ′
f (s1 +α +α′,t 1 +α +α′ +τ +τ ′)g(s2 +σ,t 2)
Gb( Q
2 +it1−is1 +iτ +iτ ′)Gb(−iτ )Gb(−iσ)
Gb( Q
2 +it1−is1 +iτ ′)
Gb( Q
2 +it1−is1 +iτ ′)Gb(−iτ ′)
Gb( Q
2 +it1−is1)
·
e−2πi(αβ+ατ +(s1+α′)τ )e2πis2τe−2πiα′(t1−s1)e2πiβ ′(α′+τ ′)eπiτ ′2
e2πiβ ′(σ+τ )
ˆBib−1(σ+τ +τ ′) ˆAib−1(β+β′+s2)
shifting α↦→α−α′,β↦→β−β′,τ ↦→τ−τ ′:
=
∫
R
∫
R+iǫ′
τ
∫
R
∫
R
∫
R+iǫτ −iǫ′
τ
∫
R
∫
R+iǫσ
dσdαdτdβdα ′dτ ′dβ′
f (s1 +α,t 1 +α +τ )g(s2 +σ,t 2)Gb( Q
2 +it1−is1 +iτ )Gb(iτ ′−iτ )Gb(−iσ)Gb(−iτ ′)
Gb( Q
2 +it1−is1)
e2πiβ ′(α+σ+τ )e2πiα′(β+s1−t1)e2πi(α+s1−s2)(τ ′−τ )−2πiαβ+πiτ ′2
ˆBib−1(σ+τ ) ˆAib−1(β+s2).
The integral over dβdα′ are just Fourier transforms, hence we can integrate over
69
α′ to get β =t1−s1:
=
∫
R
∫
R+iǫ′
τ
∫
R+iǫτ −iǫ′
τ
∫
R
∫
R+iǫσ
dσdαdτdτ ′dβ′
f (s1 +α,t 1 +α +τ )g(s2 +σ,t 2)Gb( Q
2 +it1−is1 +iτ )Gb(iτ ′−iτ )Gb(−iσ)Gb(−iτ ′)
Gb( Q
2 +it1−is1)
e2πiβ ′(α+σ+τ )e2πi(α+s1−s2)(τ ′−τ )−2πiα(t1−s1)+πiτ ′2
ˆBib−1(σ+τ ) ˆAib−1(t1+s2−s1).
Next from the decay properties for Gb(iτ ′−iτ )Gb(−iτ ′) this is integrable over τ ′.
By shifting τ↦→τ−σ−α we see also that the integrations over σ,τ,α are absolutely
convergent, and furthermore integrations over α,σ do not depend on β′. Hence we
can interchange the order for dτdτ ′ and then dσdα to get
∫
R
∫
R+iǫσ
∫
R
∫
R+iǫτ −iǫ′
τ
∫
R+iǫ′
τ
dτ ′dτdβ ′dσdα.
Using the reﬂection properties, we bring Gb(−iτ ′) to the denominator. Notice that
the contour goes above τ ′ = 0 and below τ ′ = τ , hence we can integrate over τ ′
using Lemma 3.9 to get
=
∫
R
∫
R+iǫσ
∫
R
∫
R+iǫτ −iǫ′
τ
dτdβ ′dσdαf (s1 +α,t 1 +α +τ )g(s2 +σ,t 2)
Gb( Q
2 +it1−is1 +iτ )Gb(−iσ)Gb(−iτ )Gb( Q
2−iα +is2−is1)
Gb( Q
2 +it1−is1)Gb( Q
2−iα−iτ +is2−is1)
e2πiβ ′(α+σ+τ )e−2πi(α+s1−s2)τ −2πiα(t1−s1) ˆBib−1(σ+τ ) ˆAib−1(t1+s2−s1)
=
∫
R
∫
R+iǫσ
∫
R
∫
R+iǫτ −iǫ′
τ
dτdβ ′dσdαf (s1−α,t 1−α +τ )g(s2 +σ,t 2)
Gb( Q
2 +is1−it1)Gb(−iσ)Gb(−iτ )Gb( Q
2 +is1−is2−iα +iτ )
Gb( Q
2 +is1−it1−iτ )Gb( Q
2 +is1−is2−iα)
e2πiβ ′(σ+τ −α)e2πi(t1−s1)(τ −α) ˆBib−1(σ+τ ) ˆAib−1(t1+s2−s1),
where we used the reﬂection properties again, and ﬂipping α↦→−α. Now we can
integrateτ and β′ by Fourier transform to get τ =α−σ. However, this should be
interpreted as a function of σ over R, and then analytic continued to R+iǫσ, so that
the contour for σ will be pushed under the pole for σ =α inGb(−iτ )↦→Gb(iσ−iα).
70
We get
=
∫
R
∫
C
dσdαf (s1−α,t 1−σ)g(s2 +σ,t 2)
Gb( Q
2 +is1−it1)Gb(−iσ)Gb(iσ−iα)Gb( Q
2 +is1−is2−iσ)
Gb( Q
2 +is1−it1−iα +iσ)Gb( Q
2 +is1−is2−iα)
e2πi(t1−s1)σ ˆBib−1α ˆAib−1(t1+s2−s1).
Finally we apply W31 to get
↦→W
∫
R+iǫτ
∫
R
∫
C
dσdαdτf (s1−α +τ,t 1−σ)g(s2 +σ,t 2)
Gb(−iσ)Gb(−iα +iσ)Gb( Q
2 +is1−it1 +iτ )Gb( Q
2 +is1−is2−iσ +iτ )
Gb(Q +iτ )Gb( Q
2 +is1−it1−iα +iσ +iτ )Gb( Q
2 +is1−is2−iα +iτ )
e2πiσ(t1−s1−τ )e2πis1τAib−1s1Bib−1τ⊗ ˆBib−1α ˆAib−1(t1+s2−s1−τ ).
We can further simplify the expression by the following unitary trans formations,
which will also be used in the right picture:
s2 ↦→ s2−t1,
s1 ↦→ s1 + s2
2 ,
t1 ↦→ t1 + s2
2 ,
or equivalently
f⊗g↦→f (s1 + s2
2 ,s2
2 −t1)g(t1 + s2
2 ,t 2), (7.60)
so that the expression becomes:
=
∫
R+iǫτ
∫
R
∫
C
dσdαdτf (s1−α +τ,t 1−σ)g(s2,t 2)
Gb(−iσ)Gb(−iα +iσ)Gb( Q
2 +is1−it1 +iτ )Gb( Q
2 +is1 +it1−iσ +iτ )
Gb(Q +iτ )Gb( Q
2 +is1−it1−iα +iσ +iτ )Gb( Q
2 +is1 +it1−iα +iτ )
e2πiσ(t1−s1−τ )e2πis1τeπis2τAib−1(s1+ s2
2 )Bib−1τ⊗ ˆBib−1α ˆAib−1( s2
2 −s1−τ ).
(7.61)
71
