---
doc_id: arxiv-hep-th-9408113v2
doc_title: "Dilogarithm identities"
section_id: sec-007-8-anatol-n-kirillov
section_title: "Anatol N. Kirillov"
section_number: 8
pages: 8-10
source_pdf: 9408113v2.pdf
source_sha256: dadd96e1155e820f
doc_brief: "Dilogarithm identities — We study the dilogarithm identities from algebraic, analytic, asymptotic, K-theoretic, combinatorial and representation-theoretic points of view."
---
1.1.4. Dilogarithm of complex argument. Wigner-Bloch’s function .
By using the integral representation
Li2(z) =−
∫ z
0
log(1−t)
t dt,
Euler’s dilogarithm Li2(x) can be analytically continued as a multivalued complex fun ction
to the complex plane cut along the real axis from 1 to + ∞.
Proposition A (E. Kummer (1840)). Assume that r,θ are the real numbers and
|r|< 1, then
Li2(reiθ) =− 1
2
∫ r
0
log(1− 2x cosθ +x2)
x dx
+i
{
w log(r) + 1
2Cl 2(2w) + 1
2Cl 2(2θ)− 1
2Cl 2(2θ + 2w)
}
,
where
w = tan −1
( r sinθ
1−r cosθ
)
, and Cl 2(θ) =
∞∑
n=1
sin(nθ)
n2 =−
∫ θ
0
log|2 sin(t/2)|dt
is Clausen ’s function.
Proposition B (F. Newman (1847)).
Li2(eiθ) = π2B2
( θ
2π
)
+iCl2(θ),
whereB2(x) :=− 1
π2
∞∑
n=1
cos 2nπx
n2 is the second modiﬁed Bernoulli polynomial.
In recent studies in K-theory the Wigner-Bloch dilogarithm function D(z) has played
an important role [Bl]. It can be related to Clausen’s functi on via the formula
D(z) := arg(1−z) log|z|− Im
∫ z
0
log(1−t)
t dt
= 1
2{Cl 2(2θ) +Cl 2(2w)−Cl 2(2θ + 2w)},
where θ = arg(z), w = arg(1−z) and D(z) = 0 for z∈ R∪{∞} .
The dilogarithm D: C∪{∞}→ R is a real-analytic function on C\ [0, 1], continuous
on C∪{∞} . We summarize the basic properties of Wigner-Bloch’s dilog arithm in the next
Proposition (see e.g. [Bl], [Bro2]).
Dilogarithm identities 9
Proposition C. Forz∈ C∪{∞} , we have
i) D(z) +D(1−z) = 0, D(z) +D(1/z) = 0, D(z) = D(z),
ii) D(zn) = n
n−1∑
k=0
D
(
exp
(2πki
n
)
z
)
,
iii) (Five-term relation) If z,w ∈ C\ [0, 1], then
D(z) +D(w) = D(zw) +D
(z(1−w)
1−zw
)
+D
(w(1−z)
1−zw
)
.
There is a geometric interpretation of the number D(z) and consequently of Cl 2(t) =
D(eit). Namely, for a complex number z , the volume of the asymptotic simplex with
vertices 0, 1,z and∞ in 3-dimensional hyperbolic space is equal to |D(z)|. Some formulae
for the Wigner-Bloch dilogarithm can be interpreted as rela tions between the volumes of
corresponding simplexes. For more details, see [Mi2], [Mi3 ], [Za1], [Za4].
1.1.5. Multivariable functional equations (L. Rogers (1906), G. R ay (1990)).
Using the analytic methods, Rogers [Ro] had proved the follo wing dilogarithm identity.
Proposition D (L. Rogers). Deﬁne the polynomial
r(x,t ) := 1−t−
n∏
j=1
(1−αjx)
of degree n in x for nonzero complex numbers α1,...,α n. Let {xl := xl(t)}, l = 1,...,n
be the algebraic functions satisfying r(xl,t ) = 0 . Then we have
n∑
j=1
n∑
l=1
[L(αj/αl)−L(αjxl)] = L(1−t).
The special case n = 2 leads to the form of Hill’s equation (see Remark in Section 1.3)
with two independent variables and ﬁve dilogarithmic terms .
Example. Let us assume α1 = ... = αn = 1 and 1 −t = yn. Then xl = ζly, where
ζl = exp
(2πil
n
)
, and Rogers’ identity is reduced to the so-called factoriza tion formula
L(yn) = n
n∑
l=1
L(ζly).
A remarkable generalization of Rogers’ multivariable iden tity for dilogarithm was dis-
covered by G. Ray [Ray]. Since the statement of the most gener al dilogarithm identity in
the paper [Ray] is rather involved, we present here only an im portant particular case of
the general Ray’s result.
