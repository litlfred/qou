---
doc_id: s0894-0347-08-00618-8
doc_title: "AMERICAN MATHEMATICAL SOCIETY"
section_id: sec-002-21-negative-dependence-concepts
section_title: "Negative dependence concepts"
section_number: 2.1
pages: 4-9
source_pdf: S0894-0347-08-00618-8.pdf
source_sha256: 7c0b2ca41992b21c
doc_brief: "AMERICAN MATHEMATICAL SOCIETY — 20 sections: Introduction; A plethora of negative dependence ; Negative dependence concepts"
---
ate polynomial is said to bemulti-aﬃne if it has degree at most one in each variable.
Denote by Pn, n ∈ N, the set of all probability measures on the Boolean algebra
2[n]. (In the ﬁnite case we will always assume that the σ-algebra is the full alge-
bra.) For i ∈ [n]t h ei-th coordinate function on 2[n] is an atomic (binary) random
variable given byXi(S)=1i f i ∈ S and 0 otherwise, whereS ⊆ [n], while the char-
acteristic function χS of S is deﬁned byχS(T)=1i f T = S and 0 otherwise. Using
the inclusion-exclusion principle one can show that any such characteristic function
may be written as a multi-aﬃne polynomial in X1,...,X n. Any scalar function
F =∑
S⊆[n] F(S)χS on 2[n] may therefore be viewed as a multi-aﬃne polynomial
in X1,...,X n. By abuse of notation the latter is written as F(X1,...,X n), and
NEGATIVE DEPENDENCE AND THE GEOMETR Y OF POL YNOMIALS 525
then µ(F)=
∫
Fdµ. However, in what follows the Xi’s always stand for (proba-
bilistic) random variables, and we will use other variables (such asx, y, z, w)w h e n
working with arbitrary functions/polynomials.
Let Pn be the set of all multi-aﬃne polynomials inn variables f(z1,...,z n)w i t h
non-negative coeﬃcients such thatf(1)=1 ,w h e r e1 =( 1,..., 1) ∈ Rn denotes the
“all ones vector”. There is a 1-1 correspondence between Pn and Pn:i f µ ∈ Pn we
may form its generating polynomial, namely
gµ(z)=
∫
zSdµ(S)=
∑
S⊆[n]
µ(S)zS,z =( z1,...,z n),z S :=
∏
i∈S
zi,
and if
(1) f(z)=
∑
S⊆[n]
aSzS ∈P n
we deﬁne a measure µf on 2[n] by setting µf (S)= aS, S ⊆ [n]. It is clear that
gν ∈P n, µf ∈ Pn, gµf = f,a n dµgν = ν for any ν ∈ Pn, f ∈P n. For convenience,
we will sometimes use the symbol ∂i for ∂/∂zi 1 ≤ i ≤ n, and the multi-index
notation ∂S =∏
i∈S ∂i, S ⊆ [n].
The NLC property for measures inPn translates into the corresponding property
– again called the negative lattice conditionand denoted by NLC – for polynomials
in Pn:ap o l y n o m i a lf ∈P n satisﬁes NLC if and only if its corresponding measure
µf ∈ Pn does. This amounts to saying that
(NLC) ∂Sf(0,..., 0) ∂T f(0,..., 0) ≥ ∂S∪T f(0,..., 0) ∂S∩T f(0,..., 0),
which in notation (1) becomes aSaT ≥ aS∪T aS∩T for all S, T ⊆ [n].
The so-called “closure” operations discussed in e.g. [65, II.A] may also be refor-
mulated in terms of generating polynomials:
(i) Products. If µ1 ∈ Pn1 has generating polynomial gµ1 (z1,...,z n1 ) ∈P n1
and µ2 ∈ Pn2 has generating polynomial gµ2 (z1,...,z n2 ) ∈P n2 , then the
product µ1 × µ2 is the measure µ ∈ P[n1 +n2] with generating polynomial
gµ(z1,...,z n1 +n2 )= gµ1 (z1,...,z n1 )gµ2 (zn1+1,...,z n1 +n2 ) ∈P n1 +n2 .
(ii) Projections. Given S ⊆ [n]a n dµ ∈ Pn the projection of µ onto 2S is the
measure µ′∈ P|S| with generating polynomial
gµ(z1,...,z n)
⏐⏐
zi =1,i ∈[n]\S ∈P |S|.
Note that in order for this deﬁnition to make sense we should also relabel
the variables using indices in [|S|]. However, we allow ourselves this abuse
of notation here and in what follows.
(iii) Conditioning. Let µ ∈ Pn with generating polynomial gµ(z1,...,z n) ∈P n
and ﬁx some i ∈ [n]. The measure obtained from µ by conditioning the
i-th random variable Xi to be 0 is the measure on 2[n]\{i} with generating
polynomial
gµ(z1,...,z n)
⏐⏐
zi =0
gµ(z1,...,z n)
⏐⏐
zi =0,z j =1,j ⁄=i
∈P n−1,
5 2 6 J .B O R C E A ,P .B R ¨AND ´EN, AND T. M. LIGGETT
while the measure obtained fromµ by conditioningXi to be 1 is the measure
on 2[n]\{i} with generating polynomial
lim
zi →∞
gµ(z1,...,z n)
gµ(z1,...,z n)
⏐⏐
zj =1,j ⁄=i
= ∂igµ(z1,...,z n)
∂igµ(1,..., 1) ∈P n−1.
Note that these conditional probability measures are well deﬁned provided
that the denominators appearing in the above expressions are non-zero.
(iv) External ﬁelds (as pointed out in [65, II.A], this name is borrowed from the
Ising model). If µ ∈ Pn has generating polynomial gµ(z1,...,z n) ∈P n and
ai,1 ≤ i ≤ n, are non-negative real numbers, then the measure obtained
from µ by imposing the external ﬁeld ( a1,...,a n) is the measure in Pn
with generating polynomial
gµ(a1z1,...,a nzn)
gµ(a1,...,a n) ∈P n,
which is well deﬁned provided that gµ(a1,...,a n) ⁄=0 .
(v) Symmetrization. Denote the symmetric group on n elements by Sn.F o r
σ ∈ Sn and S ⊆ [n]l e tσ(S)= {σ(s): s ∈ S}.G i v e nµ ∈ Pn deﬁne a
measure σ(µ) ∈ Pn by setting σ(µ)(S)= µ(σ(S)), S ⊆ [n]. The (full or
complete) symmetrization of µ is the measure
µs = 1
n!
∑
σ∈Sn
σ(µ) ∈ Pn.
Note that the generating polynomial of µs is
gµs (z)= 1
n!
∑
σ∈Sn
gσ(µ)(z)= 1
n!
∑
σ∈Sn
∑
S⊆[n]
aσ(S)zS
=
n∑
k=0
∑
|S|=k aS
(n
k
) ek(z1,...,z n) ∈P n,
(2)
where∑
S⊆[n] aSzS = gµ(z)a n d ek,0 ≤ k ≤ n,i st h e k-th elementary
symmetric function (see [72, §3.4] for a proof of the last identity).
(vi) Partial symmetrization. Let µ ∈ Pn,0 ≤ θ ≤ 1, 1 ≤ i<j ≤ n,a n d
τ =( ij) ∈ Sn be the transposition that permutes i and j. The partial
symmetrization of µ with respect to τ and θ is the measure
(3) µτ,θ = θµ +( 1 − θ)τ(µ) ∈ Pn
whose generating polynomial is obviously gµτ,θ = θgµ +( 1 − θ)gτ (µ) ∈P n.
Remark 2.1. All these “closure” operations are in fact well deﬁned for arbitrary
complex measures on 2 [n] if one drops the normalization factors appearing in the
denominators of the above expressions (these were used just to make sure that the
resulting measures are again probability measures). In §4 we will actually use the
partial symmetrization procedure (3) for complex measures on 2[n].
The corresponding “closure” operations for generating polynomials – i.e., prod-
ucts, projections, conditioning, external ﬁelds, symmetrization, partial symmetriza-
tion and truncations (cf. Deﬁnition 2.15 in §2.5)– are deﬁned simply by considering
the resulting polynomials for each of the operations discussed above for measures.
NEGATIVE DEPENDENCE AND THE GEOMETR Y OF POL YNOMIALS 527
Deﬁnition 2.1. A complex measureµ on 2[n] is calledsymmetric or exchangeable if
σ(µ)= µ for anyσ ∈ Sn, or equivalently, its generating polynomialgµ is symmetric
in all n variables. We say that µ is almost symmetric or almost exchangeable if gµ
is symmetric in all but possibly one variable.
Deﬁnition 2.2. If A is a collection of subsets of [n], we let χA :2 [n] → R be the
characteristic function of A deﬁned by χA(S)=1i f S ∈A and χA(S)=0i f S/∈A .
An increasing event A on 2[n] is a collection of subsets of [n] that is closed upwards
under containment, i.e., if A ∈A and A ⊆ B ⊆ [n], then B ∈A . Such an event
depends only on the set I(A): = I1 ∪···∪ Im (that is, on the variables/coordinate
functions Xi with i ∈I (A)), where I1,...,I m are the minimal sets of A with
respect to inclusion. Any (non-identically zero) non-negative increasing function f
on 2[n] may be written as f =∑k
i=1 aiχAi for some increasing events Ai on 2[n]
and ai > 0, 1 ≤ i ≤ k. Clearly, f depends on the set I(f): = I(A1) ∪···∪I (Ak).
The weakest negative dependence property is the following (see, e.g., [65]).
Deﬁnition 2.3. Am e a s u r e∈ Pn is said to be pairwise negatively correlated,o r
p-NC for short, if µ(Xi)µ(Xj) ≥ µ(XiXj) whenever 1 ≤ i ⁄= j ≤ n.I nt e r m so ft h e
generating polynomial gµ this translates into the inequalities
∂igµ(1)∂jgµ(1) ≥ ∂i∂jgµ(1), 1 ≤ i ⁄= j ≤ n,
where 1 ∈ Rn is as before the “all ones vector”. We say that a polynomial f ∈P n
is p-NC (pairwise negatively correlated) if it satisﬁes the above inequalities.
As shown by the following example, NLC does not necessarily imply p-NC.
Example 2.1. The measure µ ∈ P4 with generating polynomial
gµ(z1,z 2,z 3,z 4)= 1
2(z1z2 + z3z4)
trivially satisﬁes NLC but µ(X1X2)= 1
2 while µ(X1)µ(X2)= 1
4 ,s o µ is not p-NC.
Deﬁnition 2.4 (Deﬁnition 2.4 in [65]). Am e a s u r eµ ∈ Pn or a polynomial f ∈P n
satisﬁes the hereditary negative lattice condition or h-NLC if every projection sat-
isﬁes NLC. One further says that µ (respectively, f) satisﬁes the strong hereditary
negative lattice condition or h-NLC+ if every measure (respectively, polynomial)
obtained from µ (respectively, f) by imposing an external ﬁeld satisﬁes h-NLC.
Deﬁnition 2.5. A polynomial f ∈P n is called a Rayleigh polynomial if
(4) ∂f
∂zi
(x) ∂f
∂zj
(x) ≥ ∂2f
∂zi∂zj
(x)f(x)
for all x =( x1,...,x n) ∈ Rn
+ and 1 ≤ i, j ≤ n, where as usual R+ =( 0, ∞). More
generally, a multi-aﬃne polynomial inR[z1,...,z n] with non-negative coeﬃcients is
called a Rayleigh polynomial if it satisﬁes the above condition. A measure µ ∈ Pn
is said to be a Rayleigh measure if its generating polynomial gµ is Rayleigh.
The notion of a Rayleigh polynomial was introduced in [72,§3.1], the terminology
being motivated by its similarity with the Rayleigh monotonicity property of the
(Kirchhoﬀ) eﬀective conductance of linear resistive electrical networks; see [20, 73].
It was ﬁrst considered for uniform measures on the set of bases of a matroid [20] as
a strengthening of weaker notions studied in [29, 69]. The following properties of
Rayleigh polynomials are consequences of Deﬁnition 2.5.
5 2 8 J .B O R C E A ,P .B R ¨AND ´EN, AND T. M. LIGGETT
Proposition 2.1. If f(z1,...,z n) is Rayleigh, then so are the following polynomi-
als:
(1) ∂Sf(z1,...,z n) for any S ⊆ [n];
(2) f(z1 + α1,...,z n + αn) whenever αi ≥ 0, i ∈ [n];
(3) f(z1,...,z n)|zi=αi for any αi ≥ 0, 1 ≤ i ≤ n;
(4) f(a1z1,...,a nzn) for all ai ≥ 0, i ∈ [n];
(5) the “inversion” of f, i.e., the polynomial z1 ··· znf(z−1
1 ,...,z −1
n );
(6) the polynomial in nk variables f
(
k−1∑k
i=1 z1i,...,k −1∑k
i=1 zni
)
.
To prove (1) note that by induction it is enough to do it forS = {i} and arbitrary
i ∈ [n]. This follows by ﬁrst writing
f(z1,...,z n)= zi∂if(z1,...,z n)+ f(z1,...,z n)|zi =0
and then letting zi →∞ in the Rayleigh inequalities (4) for f corresponding to
pairs of variables indexed by distinct j, k ∈ [n] \{ i}.
Proposition 2.2. Am e a s u r ei nPn or a polynomial in Pn is Rayleigh if and only
if it is h-NLC+.
Proof. In [72, Theorem 4.4] it was proved that iff ∈P n is Rayleigh, thenf satisﬁes
NLC, which combined with Proposition 2.1 shows thatf is h-NLC+. To prove the
converse statement, let i, j ∈ [n]w i t hi ⁄= j and set
g(zi,zj)= f(z1,...,z n)|zk =1,k ∈[n]\{i,j}.
If f is h-NLC+, then g satisﬁes NLC (which in this case implies that g(zi,zj)
is in fact a real stable polynomial; see Deﬁnition 2.9 in §2.2 and Theorem 4.1
in §4). In particular, we deduce that ∂i∂jf(1) ≤ ∂if(1)∂jf(1), where 1 stands
for the “all ones vector” as in Deﬁnition 2.3. Using the external ﬁeld condition
given in Deﬁnition 2.4 we see that the aforementioned inequality also holds for the
polynomial f(x1z1,...,x nzn) whenever xi ≥ 0, i ∈ [n], which by Deﬁnition 2.5
amounts to saying that f is Rayleigh. □
Remark 2.2. It is interesting to note that one actually has the following analog of
Proposition 2.2 for the h-NLC property: a measure µ ∈ Pn – or its generating
polynomial gµ ∈P n –i sh - N L Ci fa n do n l yi fgµ satisﬁes the Rayleigh inequalities
(4) for all x =( x1,...,x n)w i t hxi ∈{ 0, 1, ∞}, i ∈ [n].
Deﬁnition 2.6. A homogeneous Rayleigh measure is one whose generating poly-
nomial is homogeneous and Rayleigh. The set of all measures that are projections
of homogeneous Rayleigh measures is denoted by PHR.
Let us now recall the key concept of negative association. For probability mea-
sures this notion is usually deﬁned as follows (cf., e.g., [55, 65, 72]).
Deﬁnition 2.7. Am e a s u r eµ ∈ Pn is called negatively associated or NA if∫
Fdµ
∫
Gdµ ≥
∫
FGdµ
for any increasing functionsF,G on 2[n] that depend on disjoint sets of coordinates
(cf. Deﬁnition 2.2). One says thatµ is conditionally negatively associatedor CNA if
each measure obtained fromµ by conditioning on some (or none) of the values of the
variables is NA. Finally, µ is called strongly conditionally negatively associated or
NEGATIVE DEPENDENCE AND THE GEOMETR Y OF POL YNOMIALS 529
CNA+ if each measure obtained fromµ by imposing external ﬁelds and projections
is CNA.
Remark 2.3. It is clear from the deﬁnitions that each of the ﬁve properties h-NLC,
Rayleigh/h-NLC+, NA, CNA, and CNA+ implies p-NC.
Remark 2.4. As explained in [65], one has the following subordination relations:
CNA ⇒ h-NLC and CNA+ ⇒ Rayleigh/h-NLC+. In §4.2 and §7 below we show
that PHR ⇒ CNA+ and that this implication is strict.
We note that NA can fail to imply NLC even for symmetric measures:
Example 2.2. Let as before ek,0 ≤ k ≤ n,b et h e k-th elementary symmetric
function inn variables and consider the measureµ ∈ P3 with generating polynomial
gµ(z1,z 2,z 3)= 1
15 [3 + 2e1(z1,z 2,z 3)+2 e2(z1,z 2,z 3)] .
It is not diﬃcult to check that µ is NA but not NLC.
Deﬁnition 2.8. The diagonal specialization of a polynomial f ∈ C[z1,...,z n]i s
the univariate polynomial
t ↦→ ∆(f)(t): = f(t ,...,t ).
A real sequence {ak}n
k=0 is log-concave if a2
k ≥ ak−1ak+1,1 ≤ k ≤ n − 1, and it is
said to have no internal zeros if the indices of its non-zero terms form an interval
(of non-negative integers). We say that a non-negative sequence {ak}n
k=0 is
• LC if it is log-concave with no internal zeros;
• SLC (strongly log-concave) if the sequence {k!ak}n
k=0 is LC;
• ULC (ultra log-concave) if the sequence
{
ak/
(n
k
)}n
k=0 is LC.
Clearly, ULC ⇒ SLC ⇒ LC. If µ ∈ Pn the sequence
{
µ
( n∑
i=1
Xi = k
)}n
k=0
=
{∆(gµ)(k)(0)
k!
}n
k=0
is called the rank sequence of µ as well as of its generating polynomial gµ ∈P n.
Am e a s u r ei nPn is then said to be ULC, SLC or LC if its rank sequence is ULC,
SLC or LC, respectively.
