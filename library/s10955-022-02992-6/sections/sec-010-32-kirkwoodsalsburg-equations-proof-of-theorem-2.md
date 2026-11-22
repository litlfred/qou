---
doc_id: s10955-022-02992-6
doc_title: "Cluster Expansions: Necessary and Sufficient Convergence Conditions"
section_id: sec-010-32-kirkwoodsalsburg-equations-proof-of-theorem-2
section_title: "Kirkwood–Salsburg Equations: Proof of Theorem 2.1"
section_number: 3.2
pages: 17-19
source_pdf: s10955-022-02992-6.pdf
source_sha256: aa73d797a89eaf06
toc_source: outline
doc_brief: "Cluster Expansions: Necessary and Sufficient Convergence Conditions — We prove a new convergence condition for the activity expansion of correlation functions in equilibrium statistical mechanics"
---
To prove our main result, Theorem 2.1, we will show that the activity expansions ρ satisfy the
Kirkwood–Salsburg inequalities and, moreover, that equality holds for non-negative interac-
tions. To do so, we will need to establish a recursive formula for the coefﬁcients ψn,n+k of
ρn given in terms of multi-rooted graphs.
Lemma 3.5 Let n ∈N, k ∈N0 and (x1, . . . , xn) ∈Xn. Abbreviate s = s(x). For L ⊂[k],
let ℓdenote the cardinality of L. Then for all (y1, . . . , yk) ∈Xk,
ψn,n+k(x1, . . . , xn, y1, . . . , yk) = 
1≤i≤n:
i̸=s

1 + f (xs, xi)
 
L⊂[k]

i∈L f (xs, yi)
	
×ψn−1+ℓ,n−1+k

x′
2, . . . , x′
n, (yi)i∈L, (y j) j∈[k]\L

.
Furthermore, if n ≥2,
ψn,n(x1, . . . , xn) =

1≤i≤n:
i̸=s

1 + f (xs, xi)

ψn−1,n−1

x′
2, . . . , x′
n

.
The lemma is proven in [14, Lemma 4.1] and holds true as well for pair potentials that may
take negative values. The index set L corresponds to the non-root vertices adjacent to the
selected vertex s. Similar recurrent relation are well-known from the literature and have been
employed in the context of both activity and density (virial) expansions for a long time (see,
e.g., [20, Eq. 5]).
We now want to translate the recurrence relation for coefﬁcients ψn,n+k from Lemma 3.5
into integral equations for partial sums and series. For a non-negative activity function, we
set
˜ρn(x1, . . . , xn; z) := z(x1) · · · z(xn)
∞

k=0
1
k!

Xk
ψn,n+k(x1, . . . , xn, y)
λk
z(d y).
Notice that ρn(x1, . . . , xn; z) is absolutely convergent if and only if ˜ρn(x1, . . . , xn; z) < ∞,
and, in the case of non-negative potentials,
˜ρn(x1, . . . , xn; z) = (−1)nρn(x1, . . . , xn; −z)
holds due to the alternating-sign property from Corollary 3.3.
Let ˜SN(z) = ( ˜SN,n(·; z))n∈N be the vector of partial sums given by
˜SN,n(x1, . . . , xn; z) := z(x1) · · · z(xn)
N−n

k=0
1
k!

Xk
ψn,n+k(x1, . . . , xn, y)
λk
z(d y)
33
Page 18 of 47
S. Jansen, L. Kolesnikov
if N ≥n, and 0 otherwise. The summand for k = 0 is to be read as |ψn,n(x1, . . . , xn)|.
Proposition 3.6 For general pair-interactions, we have
˜ρ(z) ≤ez + ˜K s
z ˜ρ(z)
(3.3)
and
˜S1(z) = ez,
˜SN+1 ≤ez + ˜K s
z ˜SN(z) (N ≥1).
Moreover, for non-negative potentials, we get the equalities
˜ρ(z) = ez + ˜K s
z ˜ρ(z)
(3.4)
and
˜SN+1 = ez + ˜K s
z ˜SN(z) (N ≥1).
Proof The equality ˜S1(z) = ez follows from the deﬁnition of ˜S1(z) and ψ1,1(x1) = 1. For
the recurrence relation, we employ arguments from [14, Sect. 4] and combine them with the
alternating sign property from Corollary 3.3 to argue equality in the case of non-negative
potentials.
Consider ﬁrst ˜SN+1,n(z) with 2 ≤n ≤N + 1. Deﬁne
Rn,ℓ(x1, . . . , xn; y1, . . . , yℓ) := z(xs)
n

i=2
(1 + f (xs, x′
i))
ℓ

i=1
 f (xs, yi)
.
Fix n ≥2. Lemma 3.5 and the triangle inequality yield
ψn,n+k(x1, . . . , xn, y1, . . . , yk)

≤

L⊂[k]
Rn,ℓ(x1, . . . , xn; yL)
ψn−1+ℓ,n−1+k

x′
2, . . . , x′
n, yL, y[k]\L
,
(3.5)
where ℓ= #L. When we integrate over y1, . . . , yk, all sets L with the same cardinality
contribute the same, therefore
1
k!

Xk
ψn,n+k(x1, . . . , xn, y1, . . . , yk)
 λk
z(d y)
≤
k

ℓ=0
1
ℓ!(k −ℓ)!

Xk Rn,ℓ(x1, . . . , xn; y1, . . . , yℓ)
ψn−1+ℓ,n−1+k

x′
2, . . . , x′
n, y
 λk
z(d y).
Summing over k = 0, . . . , N + 1 −n we obtain a double sum over k and ℓ. A change in
summation indices from (ℓ, k) to (ℓ, m) = (ℓ, k −ℓ) yields
˜SN+1,n(x1, . . . , xn; z) ≤
N+1−n

ℓ=0
1
ℓ!

XℓRn,ℓ(x1, . . . , xn; y1, . . . , yℓ)

· · ·

λℓ
z

d(y1, . . . yℓ)

,
{· · · } =
N+1−n−ℓ

m=0
1
m!

Xm
ψn−1+ℓ,n−1+ℓ+m

x′
2, . . . , x′
n, y
 λm
z

d(yℓ+1, . . . yℓ+m)

.
The term in curly braces is nothing else but ˜SN,n−1+ℓ(x′
2, . . . , x′
n, y1, . . . , yℓ). For ℓ≥
N + 1 −n, the function ˜SN,n−1+ℓ(·; z) is identically zero. It follows that
˜SN+1,n(x1, . . . , xn; z) ≤
∞

ℓ=0
1
ℓ!

XℓRn,ℓ(x1, . . . , xn; y) ˜SN,n−1+ℓ(x′
2, . . . , x′
n, y)λℓ
z

d y

.
Cluster Expansions: Necessary...
Page 19 of 47
33
This proves the inequality ˜SN+1,n(·; z) ≤( ˜K s
z SN(z)

n(·). The cases n ≥N +2 and n = 1 are
treated in a similar fashion, we leave the details to the reader. For the equality ˜SN+1,n(·; z) =
( ˜K s
z SN(z)

n(·) in the case of non-negative potentials, notice that for such potentials (3.5)
holds with an equality — due to the alternating-sign property from Corollary 3.3.
Finally, by passing to the limit N →∞in the recurrence relation for ˜SN(z), the inequality
(3.3) for ˜ρ(z) follows (and in the case of non-negative potentials the ﬁxed point equation
(3.4) is obtained). Notice that all exchanges of limits, sums and integrals are permitted by
monotone convergence and because all terms involved are non-negative.
⊓⊔
Proof of Theorem 2.1 For the implication (i) ⇒(ii), suppose there exists a sequence ξ =
(ξn)n∈N of measurable non-negative functions ξn : Xn →R+ such that ez + ˜K s
z ξ ≤ξ. We
prove by induction over N that ˜SN(z) ≤ξ for all N ∈N. For N = 1, we have
˜S1 = ez ≤ez + ˜K s
z ξ ≤ξ.
If ˜SN ≤ξ for some N ∈N, then
˜SN+1 ≤ez + ˜K s
z ˜SN(z) ≤ez + ˜K s
z ξ ≤ξ,
where the ﬁrst inequality holds by Proposition 3.6 and the second one due to the inductive
hypothesis and the monotonicity of ˜K s
z on non-negative functions.
This completes the induction and proves ˜SN ≤ξ for all N. Passing to the limit N →∞,
we ﬁnd ˜ρ ≤ξ. This proves the absolute convergence (ii) as well as the bound (2.6).
Left to show is the implication (ii) ⇒(i) under the additional assumption that the potential
is non-negative. Suppose that ρn(x1, . . . , xn; z) is absolutely convergent, for all n ∈N and
(x1, . . . , xn) ∈Xn. Then ˜ρn(x1, . . . , xn; z) is ﬁnite everywhere and we may set
ξn(x1, . . . , xn) := ˜ρn(x1, . . . , xn; z).
Proposition 3.6 yields ξ = ez + ˜K s
z ξ hence a fortiori ξ ≥ez + ˜K s
z ξ, as a pointwise inequality
for all vector entries. This proves (i).
⊓⊔
