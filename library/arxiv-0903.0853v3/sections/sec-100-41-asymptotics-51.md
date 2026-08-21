---
doc_id: arxiv-0903.0853v3
doc_title: "Local analytic classification of q-difference equations"
section_id: sec-100-41-asymptotics-51
section_title: "ASYMPTOTICS 51"
section_number: 4.1
pages: 57-58
source_pdf: 0903.0853v3.pdf
source_sha256: d4295d4b18b2f08f
doc_brief: "Local analytic classification of q-difference equations — 229 sections: Vector bundles associated to q-diﬀ; The q-Euler equation and conﬂuent ; The symmetric square of the q-Eule"
---
f (k): by deﬁnition, they depend only on the class of f.
So let f be aC∞ function in the Whitney sense on K ′. The functions f (k)
are continuous on K ′ and for all n∈ N, the family
(
f (k))
(restricted to K ′)
satisﬁes the following conditions, that are called Whitney conditions of order
n∈ N and that we shall denote Wn(K ′):
lim
(
f (k)(x1,y 1)−∑
|h|≤n
f (k+h)(x2,y2)
h! (x1−x2,y 1−y2)h
)
||(x1−x2,y 1−y2)||n−|k| = 0,
where the limit is taken for ( x1,y 1)→ (x0,y 0)∈K ′, (x2,y 2)→ (x0,y 0)∈K ′,
with (x1,y 1), (x2,y 2)∈K ′ and (x1,y 1)⁄= (x2,y 2).
Conversely a family
(
f (k))
k∈N2 of continuous functions on K ′ is the family
of Taylor jets of an element ofC∞
W hitney(K ′) if and only if it satisﬁes Whitney
conditions Wn(K ′) for all n∈ N (this is Whitney’s theorem, see [ 29, 28 ]).
Note that, with the usual identiﬁcation of C with R2, setting z := x + iy
and using ∂
∂z , ∂
∂ ¯z instead of ∂
∂x , ∂
∂y , for all n∈ N we can replace Whitney
conditions Wn(K ′) by equivalent conditions ˜Wn(K ′), that we do not state
more explicitly here. In our case of interest (functions sat isfying the Cauchy-
Riemann equation ∂f/∂z = 0), they take the form of condition (iii) of the
lemma above.
Proposition 4.1.3. — Let U be a Σ-invariant open set of C. Then, f ∈
A (U∞) if, and only if, for every invariant strict subset K⊂U , one has:
f|K∈ Ker
(∂
∂¯z :C∞
W hitney
(
K∪{ 0}, C
)
→C ∞
W hitney
(
K∪{ 0}, C
) )
.
Proof. — Let f∈C ∞
W hitney
(
K∪{ 0}, C
)
. If for all invariant strict subset K⊂
U, one has:
f|K∈ Ker
(∂
∂¯z :C∞
W hitney
(
K∪{ 0}, C
)
→C ∞
W hitney
(
K∪{ 0}, C
) )
,
then, the function f is holomorphic on V , its Taylor jet ˆf at 0 is formally
holomorphic ( i.e. it satisﬁes the Cauchy-Riemann equation), ˆf = ∑
n≥0
anzn
and f is asymptotic to ˆf on V , f∈ A (U∞).
Conversely let f∈ A (U∞); then, for all p∈ N, f (p)∈ A (U∞) and for all
r∈ N∗, we have ∂r
∂ ¯zrf (p) = 0.
52 CHAPTER 4. THE q-ANALOGS OF BIRKHOFF-MALGRANGE-SIBUYA THEOREMS
We can apply lemma 4.1.2 to each function f (p),p∈ N, to the eﬀect that f
satisﬁes conditions ˜Wn(K) for all n∈ N (this is assertion (iii) of the lemma);
therefore it satisﬁes also Whitney conditions Wn(K) for all n∈ N and, using
Whitney theorem, we get f∈C ∞
W hitney
(
K∪{ 0}, C
)
.
