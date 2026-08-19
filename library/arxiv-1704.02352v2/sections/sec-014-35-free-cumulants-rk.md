---
doc_id: arxiv-1704.02352v2
doc_title: "GAUSSIAN FLUCTUATIONS OF JACK-DEFORMED RANDOM YOUNG DIAGRAMS"
section_id: sec-014-35-free-cumulants-rk
section_title: "Free cumulants Rk"
section_number: 3.5
pages: 23-29
source_pdf: 1704.02352v2.pdf
source_sha256: 9a14dd6ee33248d3
doc_brief: "GAUSSIAN FLUCTUATIONS OF JACK-DEFORMED RANDOM YOUNG DIAGRAMS — We introduce a large class of random Y oung diagrams which can be regarded as a natural one-parameter deformation of so me classi- cal Y"
---
representation theory it is convenient to parametrize the s hape of the Y oung
diagram λ by free cumulants Rk(λ) (which depend on the parameter α in
our settings). In the context of the representation theory o f the symmetric
groups these quantities have been introduced by Biane [Bia9 8].
For the purposes of the current paper it is enough to know that for a ﬁxed
Y oung diagramλ its sequence of functionals of shape and its sequence of
free cumulants are related to each other by the following sim ple systems of
equations [DF ´S10, Eqs. (14) and (15)]:
Sl =
∑
i≥1
1
i! (l − 1)i−1 ∑
k1,...,ki≥2
k1+···+ki=l
Rk1 · · · Rki, l ≥ 2,(3.6)
Rl =
∑
i≥1
1
i! (−l + 1)i−1 ∑
k1,...,ki≥2
k1+···+ki=l
Sk1 · · · Ski, l ≥ 2,(3.7)
where we use a shorthand notation Sk = Sk(λ), Rk = Rk(λ). In fact,
the above-cited papers [Bia98, DF ´S10] concerned only the special isotropic
case α = 1 , however the passage to the anisotropic case α ⁄= 1 does not
create any difﬁculties, see the work of Lassalle [Las09] (wh o used a differ-
ent normalization constants) as well as of the ﬁrst-named au thor and Féray
[DF16] (whose normalization we use).
3.6. The case α = 1 . The main advantage of free cumulants lies in the
combination of the following two facts.
• Each free cumulant Rk of a given Y oung diagram λ can be efﬁ-
ciently calculated [Bia98] and its dependence on the shape o f λ
takes a particularly simple form (more speciﬁcally, “ Rk is a ho-
mogeneous function”).
24 MACIEJ DOŁ ˛ EGA AND PIOTR ´SNIADY
• The family (γ, R2, R3, . . .) forms a convenient algebraic basis of
the algebra P with deg γ = 1 and deg Rk = k. In the special case
α = 1 (which corresponds to γ = 0 ) the expansion of Chl in this
basis takes the following, particularly simple form:
(3.8) Chl = Rl+1 + (terms of degree at most l − 1).
One of the consequences of (3.8) is that in the special case α = 1 the
relationship announced in Theorem 2.3( b) between the reﬁned asymptotics
of the four quantities (2.6)–(2.9) for ℓ = 1 takes the following, particularly
simple form. Assume that there exists some sequence (al) with the property
that
χn(l) = al+1 n− l−1
2 + O
(
n− l+1
2
)
for all l ≥ 1;(3.9)
note that it is a stronger version of (2.10) with const2 ≡ 0; then
Eχn(Chl) = al+1 n
l+1
2 + O
(
n
l−1
2
)
for all l ≥ 1;(3.10)
Eχn(Rl+1) = a′
l+1 n
l+1
2 + O
(
n
l−1
2
)
for all l ≥ 1,(3.11)
Eχn(Sl) = a′′
l n
l
2 + O
(
n
l−2
2
)
for each l ≥ 2,(3.12)
where
a′
l+1 = al+1(3.13)
and
a′′
l =
∑
i≥1
1
i! (l − 1)i−1
∑
k1,...,ki≥2
k1+···+ki=l
a′
k1 · · · a′
ki,(3.14)
see (3.6) for the last equality and [ ´Sni06] for more details.
3.7. Details of Theorem 2.3 part ( a) in the generic case α ⁄= 1 . The
original proof of [ ´Sni06, Theorem and Deﬁnition 1] was based on the idea
of expressing various elements F of the algebra of α-polynomial functions
P (1) (such as the characters Chπ or the conditional cumulants κ• of such
characters) as polynomials in the basis R2, R3, . . . of free cumulants and
studying the top-degree of such polynomials, as we did in Sec tion 3.6. In
our more general context of α ⁄= 1 (or, in other words, γ ⁄= 0 ) the cor-
responding polynomial for F might have some extra terms which depend
additionally on the variable γ. These extra terms might inﬂuence the as-
ymptotic behavior of random Y oung diagrams. We shall discus s this issue
in more detail in the remaining of this section as well as in Se ction 3.9.
JACK-DEFORMED RANDOM YOUNG DIAGRAMS 25
3.7.1. The ﬁrst-order asymptotics when α is constant. The ﬁrst-named au-
thor and Féray [DF16, Proposition 3.7] proved that the degre e of
(3.15) F := Ch l
with respect to the ﬁltration from Section 3.6 remains equal to l + 1 even
when we pass from P (1) to P or, in other words, that the degree of the
extra terms is bounded from above by l + 1. In the asymptotics when α
is a constant and does not depend on n (or, more generally, when the con-
stant g from (1.9) fulﬁlls g = 0 ), it follows that γ = O(1) ≪ O
(
n
deg γ
2
)
.
Since each extra term is divisible by the monomial γ, it follows that the
contribution of the extra terms is negligible when compared to the unique
original top-degree term Rl+1. It follows that in this asymptotics the rela-
tionships between the quantities (al), (a′
l) and (a′′
l ) which provide the ﬁrst-
order asymptotics of, respectively, the characters, the me an value of free
cumulant, and the mean value of the functionals of shape, rem ain the same
as in Section 3.6 for the case α = 1.
From Theorem 3.2 it follows that an analogous result holds tr ue for the
conditional cumulant (covariance)
(3.16) F := κ•(Chl1, Chl2)
and the degree of F remains equal to l1 + l2 when we pass from P (1) to
P. A reasoning similar to the one above implies that not only th e proof of
[ ´Sni06, Theorem and Deﬁnition 1] remains valid in our context for ℓ = 2 ,
but also the relationships between the quantities (2.6)– (2.9) which provide
the ﬁrst-order asymptotics of cumulants remain the same as i n [ ´Sni06, The-
orem 3].
Anticipating the proof of Theorem 1.5, the above considerat ions imply
the following explicit description of the covariance of the limiting Gaussian
process ∆ ∞.
Corollary 3.5. The covariance of the Gaussian process ∆ ∞ describing the
limit ﬂuctuations of random Young diagrams from Theorem 1.5 coincides
with its counterpart for α = 1 from [ ´Sni06, Theorem 3] .
3.7.2. The ﬁrst-order asymptotics in the double scaling limit. In the asymp-
totics when α = α(n) depends on n in a way described in Section 1.11 with
g ⁄= 0 , the extra terms in both examples (3.15), (3.16) considered above
are of the same order as the original terms. It follows that th e relation-
ship between the quantities (al), (a′
l) and (a′′
l ) is altered and depends on the
constant g from (1.9), see Section 3.9.2 below. Also the covariance of t he
Gaussian process describing the ﬂuctuations of random Y oun g diagrams is
altered; ﬁnding an explicit form for this covariance is curr ently beyond our
26 MACIEJ DOŁ ˛ EGA AND PIOTR ´SNIADY
reach because no closed formula for the top-degree part of th e conditional
cumulant κ•(Chl1, Chl2) (an analogue of the results of [ ´Sni18, Section 1]
for Chn) is available.
3.8. Reﬁned asymptotics of characters. In order to ﬁnd more subtle re-
lationships between the asymptotics of various quantities appearing in The-
orem 2.3 we need an analogue of Equation (3.8) between the cha racter Chl
and the free cumulants in the generic case α ⁄= 1 . We present below two
such formulas: the one from Section 3.8.1 is conceptually si mpler and will
be sufﬁcient for the scaling when α is ﬁxed; in the case of the double scaling
limit we will need a more involved formula from Section 3.8.2 .
3.8.1. The rough estimate. We start with the formula expressing the top-
degree part of the normalized Jack character Chl modulo terms divisible
by γ2 which follows follows from [Las09, Section 11] combined wit h the
degree bounds of the ﬁrst-named author and Féray [DF16, Prop osition 3.7]
as well as from [ ´Sni18, Theorem A.3]:
(3.17) Chl =
[
Rl+1+
+ γ
∑
i≥1
∑
k1+···+ki=l
l
i(k1 − 1) · · ·(ki − 1)Rk1 · · · Rki+
+(terms divisible by γ2 )
]
+
(terms of degree at most l − 1).
3.8.2. Closed formula for top-degree part of Jack characters. Let us ﬁx
an integer l ≥ 1. We will view the symmetric group S(l) as the set of
permutations of the set [l] := {1, . . . , l} and its subgroup
S(l − 1) :=
{
σ ∈ S(l) : σ(l) = l
}
as the set of permutations of the same set [l] which have l as a ﬁxpoint.
Consider the set
Xl =
{
(σ1, σ2) ∈ S(l) × S(l) :
the group generated by σ1, σ2 acts transitively on the set [l]
}
.
The group S(l − 1) acts on Xl by coordinate-wise conjugation:
π · (σ1, σ2) :=
(
πσ1π−1, πσ2π−1)
.
The orbits of this action deﬁne an equivalence relation ∼ on Xl; the corre-
sponding equivalence classes have a natural combinatorial interpretation as
JACK-DEFORMED RANDOM YOUNG DIAGRAMS 27
non-labeled, rooted, bicolored, oriented maps with l edges which is out of
scope of the current paper (see [ ´Sni18, Section 1.4.3] for details).
For a permutation π we denote by C(π) the set of its cycles.
We say that a triple (σ1, σ2, q) is an ‘expander’ [ ´Sni18, Appendix A.1],
see also [DF ´S10], if σ1, σ2 ∈ S(l) are permutations and q : C(σ2) →
{2, 3, . . .} is a function on the set of cycles of σ2 with the following two
properties: ∑
c∈C(σ2)
q(c) = |C(σ1)| + |C(σ2)|
and for every set A ⊂ C(σ2) such that A ⁄= ∅ and A ⁄= C(σ2) we have that
#
{
c ∈ C(σ1) : c intersects at least one of the cycles in A
}
>
∑
d∈A
[
q(d) − 1
]
.
The following is a reﬁned version of the formula (3.17).
Lemma 3.6 ([ ´Sni18, Theorem A.3 and Theorem 1.6]) . F or each integer
l ≥ 1 the expansion of the character Chl as a polynomial in the variables
γ, R2, R3, . . . is given by
(3.18) Chl =
∑
[(σ1,σ2)]∈Xl/∼
γl+1−|C(σ1)|−|C(σ2)| ∑
q : C(σ2)→{2,3,... }
(σ1, σ2, q) is an expander
∏
c∈C(σ2)
Rq(c)+
+ (terms of degree at most l − 1).
where the ﬁrst sum runs over the representatives of the equiv alence clases.
3.9. Proof of part ( b) of Theorem 2.3.
3.9.1. The scaling when α is constant. Part ( b) of Theorem 2.3 concerns
the trivial case ℓ = 1 which one can easily prove from scratch, based on
(3.17). We shall present a detailed proof only for a speciﬁc c ase which will
be useful in applications (more speciﬁcally, for the proof o f Theorem 1.5
from Section 6) and we shall assume that the reﬁned asymptoti cs of char-
acters speciﬁed in part ( b) of Theorem 2.3 holds true for the quantity (2.6).
The other implications are analogous.
For a speciﬁc choice of the constants
χn(l) = al+1 n− l−1
2 + bl+1 n− l
2 + o
(
n− l
2
)
for l ≥ 1(3.19)
28 MACIEJ DOŁ ˛ EGA AND PIOTR ´SNIADY
for some sequences (al) and (bl), it is a simple exercise to use (2.1) and
(3.17) in order to show that
Eχn(Chl) = al+1 n
l+1
2 + bl+1 n
l
2 + o
(
n
l
2
)
for l ≥ 1,(3.20)
Eχn(Rl+1) = a′
l+1 n
l+1
2 + b′
l+1 n
l
2 + o
(
n
l
2
)
for l ≥ 1,(3.21)
where (a′
l) is given again by (3.13) and (b′
l) is the unique sequence which
fulﬁlls
(3.22) bl+1 = b′
l+1 + γ
∑
i≥1
∑
k1+···+ki=l
l
i (k1 − 1) · · · (ki − 1)ak1 · · · aki.
In particular, (3.20) shows that the reﬁned asymptotics of c haracters speci-
ﬁed in part ( b) of Theorem 2.3 holds true for the quantity (2.7).
Consider now the quantity under the limit symbol in (2.8) for ℓ = 1 and
for the speciﬁc choice of x1 = Sl. Equation (3.6) implies that the reﬁned
asymptotics of characters speciﬁed in part ( b) of Theorem 2.3 holds true for
the quantity (2.8):
(3.23) Eχn(Sl) = a′′
l n
l
2 + b′′
l n
l−1
2 + o
(
n
l−1
2
)
for each l ≥ 2,
with the constants given by (3.14) and
(3.24) b′′
l =
∑
i≥1
1
(i − 1)! (l − 1)i−1 ∑
k1,...,ki≥2
k1+···+ki=l
b′
k1a′
k2 · · · a′
ki.
We conclude the proof by pointing out that for ℓ = 1 the expression under
the limit symbol in (2.8) coincides with its counterpart fro m (2.9). □
Remark 3.7. One can see that generically for α ⁄= 1 and γ ⁄= 0 (even if
the initial characters χn(l) have small subleading terms which corresponds
to bl ≡ 0) the subleading terms in (3.23) are much bigger than their co un-
terparts for α = 1 from (3.12), namely they are of order 1
√n times the
leading asymptotic term. As we shall see in Section 6, this le ads to non-
centeredness of the limiting Gaussian process ∆ ∞.
3.9.2. The double scaling limit. In the double scaling limit g ⁄= 0 consid-
ered in Section 1.11 the reasoning presented in Section 3.9. 1 above remains
valid if one replaces all the references to (3.17) by Lemma 3. 6. Note, how-
ever, that the relationship (3.13) in this new context takes the form
al+1 =
∑
[(σ1,σ2)]∈Xl/∼
gl+1−|C(σ1)|−|C(σ2)| ∑
q : C(σ2)→{2,3,... }
(σ1, σ2, q) is an expander
∏
c∈C(σ2)
a′
q(c),
JACK-DEFORMED RANDOM YOUNG DIAGRAMS 29
while (3.22) takes the form
bl+1 =
∑
[(σ1,σ2)]∈Xl/∼
(
l + 1 − |C(σ1)| − |C(σ2)|
)
g′ gl−|C(σ1)|−|C(σ2)|×
×
∑
q : C(σ2)→{2,3,... }
(σ1, σ2, q) is an expander
∏
c∈C(σ2)
a′
q(c)+
+
∑
[(σ1,σ2)]∈Xl/∼
gl+1−|C(σ1)|−|C(σ2)|×
×
∑
q : C(σ2)→{2,3,... }
(σ1, σ2, q) is an expander
∑
c∈C(σ2)
b′
q(c)
∏
c′∈C(σ2)\{c}
a′
q(c′).
4. T ECHNICAL RESULTS
