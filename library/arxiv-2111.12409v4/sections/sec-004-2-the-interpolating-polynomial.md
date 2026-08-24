---
doc_id: arxiv-2111.12409v4
doc_title: "On the generalisation of Roth’s theorem Paolo Dolce Francesco Zucconi 0 Introduction 1 0.1 History . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . ."
section_id: sec-004-2-the-interpolating-polynomial
section_title: "The interpolating polynomial"
section_number: 2
pages: 7-8
source_pdf: 2111.12409v4.pdf
source_sha256: 3f0b94ee06fe79bf
doc_brief: "On the generalisation of Roth’s theorem — We present two generalisations of Roth’s approximation theorem on proper adelic curves, assuming some technical conditions on the behavior of the logarithmi"
---
We ﬁx a proper adelic curve X = (K, Ω , φ) and an algebraic closure of K. In this section we recall the
existence of an interpolating polynomial δ ∈ K[X1, . . . , XN ] associated to some elements α 1, . . . ,α n ∈
KN having some explicit bounds on: the degree, the d-index at all the α j’s and the height. The
complete construction of δ can be found in [ Cor97], and we will recall it in appendix A.
We ﬁx for the whole section the following data: two natural nu mbers n, N ≥ 2, and a vector
d = ( d1, . . . , dN ) ∈ (R>0)N . We say that two vectors α = ( α(1), . . . , α(N)), β = ( β(1), . . . , β(N)) are
componentwise diﬀerent if α(j) ⁄= β(j) for j = 1, . . . , N.
Deﬁnition 2.1. The d-index of P (X1, . . . , XN ) ⁄= 0 at α ∈ KN is the real number:
Indα ,d(P ) := min
i∈NN
{ N∑
j=1
ij
dj
∈ R : ∆ iP (α ) ⁄= 0
}
Let’s ﬁx t ∈ R such that 0 < t < N , the following two sets will play a central role in the theory :
Gt :=
{
i ∈ NN : ij ≤ dj ∀j = 1, . . . , N, and
N∑
j=1
ij
dj
≤ t
}
,
Ct :=
{
(x1, . . . , xN ) ∈ [0, 1]N :
N∑
j=1
xj ≤ t
}
The Lebesgue measure of Ct will be denoted as V (t), and for simplicity of terminology we will refer
to it simply as “volume”.
Lemma 2.2. The cardinality of Gt is asymptotic to d1d2 . . . dN V (t).
Proof. See [ BG06, p. 157].
7
Now ﬁx some vectors α 1, . . . ,α n ∈ KN where α h = ( α(1)
h , . . . , α(N)
h ) for every h = 1 , . . . , n and
let X = ( X1, . . . , XN ) be a vector of variables. For any two multi-indices a = ( a1, a2, . . . , aN ) and
i = (i1, i2, . . . , iN ) of NN we use the following notations:
(
a
i
)
:=
(
a1
i1
)(
a2
i2
)
. . .
(
aN
iN
)
α i
h := (α(1)
h )i1 (α(2)
h )i2 . . . (α(N)
h )iN
X i := X i1
1 X i2
2 . . . XiN
N
with the convention
(p
q
)
= 0 if 0 ≤ p < q for the binomial coeﬃcient. Now, consider γ ∈ R such that
0 < γ < 1
2nN 2 ; we always assume that
dj+1
dj
≤ γ for any j = 1, . . . , N − 1 , which means in particular
that dj = O(d1) for any j. We also put η := 2γn < 1
N 2 and d := d1d2 . . . dN .
We have the following result about the existence of a polynom ial δ(X1, . . . , XN ) ∈ K[X1, . . . XN ]
with some prescribed properties. In the appendix A we will sk etch Corvaja’s construction ofδ(X1, . . . , XN )
adapting it to the case of adelic curves:
Proposition 2.3. Assume that in the adelic curve X the condition hX(2) ≤ log 2 is satisﬁed and
assume that the number η ∈ R is chosen as explained above. Let’s ﬁx some vectors α 1, . . . ,α n, β ∈ KN
that are pairwise componentwise diﬀerent. Moreover let’s ch oose some parameters s, t1, . . . , tn ∈ R,
with 0 < s < 1 and 0 < t h < N
2 for h = 1 , . . . , n such that the following condition on volumes is
veriﬁed:
(1 + η)N < V (s) +
n∑
h=1
V (th) < 1 + 2N η (10)
Then there exists a polynomial δ(X1, . . . XN ) ∈ K[X1, . . . , XN ] satisfying the following properties:
(1) δ(β ) ⁄= 0;
(2) deg Xj δ ≤ ddjV (s) + O(d), for 1 ≤ j ≤ N ;
(3) Ind α h,d(δ) ≥ dV (s)
(
th − s − 2N 2 η
V (s)
)
+ O(dN−1
1 ), for 1 ≤ h ≤ n;
(4) hX(δ) ≤ d
N∑
j=1
dj
(
log 2 +
n∑
h=1
V (th)h(α(j)
h )
)
+ O(d log d);
Proof. See [ Cor97, Proposition 2.6].
