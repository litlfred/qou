---
doc_id: arxiv-2509.20302v1
doc_title: "Universality in the resurgence of generalized Tracy-Widom distributions"
section_id: sec-005-32-generic-relations
section_title: "Generic relations"
section_number: 3.2
pages: 4-5
source_pdf: 2509.20302v1.pdf
source_sha256: 59837f5b511c9e07
doc_brief: "Universality in the resurgence of generalized Tracy-Widom distributions — We analyze determinants associated with Bessel kernels and generic symbol functions, which govern a class of ob- servables"
---
For generic {xj} the non-perturbative corrections of
order e−8πgxj satisfy the same equations as for x1,
merely x1 is replaced with x j. Thus we can conclude
that D{j} ≡D{0,...,0,1,0,...,} has the same form as D{} but
Figure 3: Cut structure on the Borel plane of B[D{1}](s) for a symbol
with {x1,x2,x3|y1,y2}. This is the same cut structure we would have
for {x2,x3|x1,y1,y2}.
with I{j}
n
= I{}
n +
2(−1)n
(2πxj)2n−1 . The corresponding Stokes
constant is
S{j} = eiπℓβ
4πxj
Φ(2iπxj)
Φ′(−2iπxj)
(18)
= −ieiπℓβ ∏
m̸=j
(xj +xm)
(xj −xm) ∏
m
(xj −ym)
(xj +ym)
(19)
and the alien derivatives are
∆jD{} = −2S{j}D{j} ;
∆2
jD{} = 0
(20)
We can think of D{j} as the perturbative part corre-
sponding to Φ{j}. Since Φ{j} has no zero at x j (rather a
pole there) we do not expect any singularity on the Borel
plane at xj neither a non-perturbative correction at order
e−8πx jg or any higher multiple of them. Indeed, this is
what we found by analysing the asymptotic behaviour
of D{j}
k
as well as the analytic structure of B[D{j}](s)
in many cases.
However,
the non-perturbative corrections D{j}
will still have Borel singularities related to xk and
its asymptotic behaviour indicates corrections of the
form e−8πxkg.
Since our argumentations work for
generic {x1,...,xj,...|y1,y2,...} it will also work for
{x1,..., ˆxj,...|xj,y1,y2,...}, where with the hat we in-
dicated that xj is absent.
Thus, following from the
resurgence relations (14), we can say that D{j,k} ≡
D{0,...0,1,0,...,0,1,0,...} must have the same expansion as
the perturbative part but with the replacements In →
I{j,k}
n
, where
I{j,k}
n
= I{j}
n
+
2(−1)n
(2πxk)2n−1 = I{k}
n
+
2(−1)n
(2πx j)2n−1
(21)
The corresponding Stokes constants are
S{j,k} = S{j}S{k} (xj −xk)2
(xj +xk)2
(22)
where the extra factor is due to the fact that we need
to take eiπℓβ
4πxk
Φ{j}(2iπxk)
Φ{j}′(−2iπxk) rather than the same expression
with Φ, which defines S{k}. Observe that the result does
4
not depend on which order we take the non-perturbative
corrections. Stating in a different manner
∆j∆kD{} = ∆k∆jD{}
(23)
Repeating the same procedure further we can see that
D{j1,...,jn} has exactly the same expansion as D{}, but
we have to replace In with I{ j1,...,jn}
n
, which is obtained
from In by flipping the signs of x jks
I{j1,...,jl}
n
= In +
l
∑
k=1
2(−1)n
(2πx jk)2n−1
(24)
Similarly, the Stokes constants are
S{j1,...,jl} = ∏
m
S{ jm} ∏
m<n
(xjm −xjn)2
(xjm +xjn)2
(25)
and the alien derivatives read as
∆kD{j1,...,jl} = −2S{k,j1,...,jl}
S{ j1,...,jl} D{k,j1,...,jl}
(26)
from which it follows that different alien derivatives
commute ∆j∆kD{ j1,...,jl} = ∆k∆jD{ j1,...,jl}.
It is also
true that ∆2
kD{j1,...,jl} = 0.
By slightly changing the normalization of the expan-
sion function
S{δ j}D{δj}(g) = ∏
j
(S{ j})δ j ¯D{δj}
(27)
the determinant can be formulated as an infinite param-
eter trans-series
D(g,{σ}) = Ae4πg∑i(xi−yi)g
β2+2ℓβ
2
×
(28)
∑
{δi=0,1}
e−8πg∑i δixi(∏
i
σδi
i ) ¯D{δi}(g)
Since the alien derivaties are proportional to deriva-
tives wrt. the trans-series parameters ∆jD(g,{σ}) =
−2∂σjD(g,{σ}) the Stokes automorphism, which con-
nects the two lateral resummations, shifts the trans-
series parameters as σj →σj + 2S{ j}, and the median
resummation provides the physical answer: σj = S{j}.
