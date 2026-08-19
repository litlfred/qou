---
doc_id: modularqholonomicmodules
doc_title: "MODULAR q-HOLONOMIC MODULES"
section_id: sec-003-14-the-generalised-q-hypergeometric-equation-is
section_title: "The generalised q-hypergeometric equation is modular"
section_number: 1.4
pages: 6-7
source_pdf: modular.qholonomic.modules.pdf
source_sha256: 640303a68dd75453
doc_brief: "MODULAR q-HOLONOMIC MODULES — We introduce the notion of modular q-holonomic modules whose fundamental matrices deﬁne a cocycle with improved analyticity properties and show that the generalised"
---
might expect, modular q-holonomic modules are abundant. This section concerns the gen-
eralised q-hypergeometric equation
(r−1∏
j=0
(1−q−1bjσ)−t
r∏
j=1
(1−ajσ)
)
f = 0 (11)
for a functionf =f(t,a,b,q ) wherea = (a1,...,a r) andb = (b0,...,b r−1) withb0 =q, where
σ is the operator that shifts t toqt. This equation is a q-deformation of the hypergeometric
equation (a regular singular linear diﬀerential equations with singularities at 0 , 1,∞), itself
a generalisation of the Gauss hypergeometric equation. The hypergeometric equation has a
rich history related to, among other things, periods in algebraic geometry and in the Gauss-
Manin connection of the middle cohomology of the Dwork family of smooth hypersurfaces;
see for example [7, 47] and references therein.
The generalisedq-hypergeometric equation (11) was introduced and studied by Heine, who
shows that this equation has a solution, analytic at t = 0, given by the q-hypergeometric
series
rφr−1(a;b;q,t ) =
∞∑
k=0
(a1;q)k... (ar;q)k
(b1;q)k... (br−1;q)k(q;q)k
tk. (12)
The generalised q-hypergeometric equation and the q-hypergeometric series are classical ex-
amples of functions that appear in many areas of research, and for a comprehensive treat-
ment, we refer the reader to the book of Gasper–Rahman [38] and references therein.
Consider the matrices
U =W (f (1),f (qb−1
1 ),...,f (qb−1
r−1)), V =W (g(a−1
1 ),...,f (a−1
r )) (13)
where W denotes the Wronskian of r functions f1,...,f r, which is an r×r matrix deﬁned
byW (f1,...,f r)ij = (σi−1fj) for i,j = 1,...,r and
f (q−1bj )(t,a,b,q ) =Bj(a,b,q )θ(q−1bjt;q)
θ(t;q)
rφr−1(qa/bj;qb/bj;q,t ) (14)
for j = 0,...,r − 1 with B0 = 1 and, for j >0,
Bj(a,b,q ) =
( r∏
i=1
(ai;q)∞(qbi−1/bj;q)∞
(qai/bj;q)∞(bi−1;q)∞
)
(q;q)3
∞
θ(q−1bj;q), (15)
and
g(a−1
j )(t,a,b,q ) =Aj(a,b,q )θ(q−1ajt;q)
θ(q−1t;q)
rφr−1(qai/b;qai/a;q,qb 1...b r−1a−1
1 ...a −1
r t−1) (16)
for j = 1,...,r with
Aj(a,b,q ) = (q;q)2
∞
θ(q−1aj;q)∏r
i=1,i⁄=j(ai/aj;q)∞
r∏
i=1
(ai;q)∞(bi−1/aj;q)∞
(bi−1;q)∞
. (17)
MODULAR q-HOLONOMIC MODULES 7
The calculation of the monodromy is a classical result and follows from [38, Eq.(4.5.2)]. The
monodromy
−→
M(t,a,b,q ) =V (t,a,b,q )−1U(t,a,b,q ) is given explicitly by
−→
M(t,a,b,q ) =


1 (q;q)3
∞θ(b1t;q)θ(a1/b1t;q)θ(a1;q)
θ(t;q)θ(a1t;q)θ(b1;q)θ(a1/b1;q) ... (q;q)3
∞θ(br−1t;q)θ(a1/br−1t;q)θ(a1;q)
θ(t;q)θ(a1t;q)θ(br−1;q)θ(a1/br−1;q)
1 (q;q)3
∞θ(b1t;q)θ(a2/b1t;q)θ(a2;q)
θ(t;q)θ(a2t;q)θ(b1;q)θ(a2/b1;q) ... (q;q)3
∞θ(br−1t;q)θ(a2/br−1t;q)θ(a2;q)
θ(t;q)θ(a2t;q)θ(br−1;q)θ(a2/br−1;q)
: : : ...
1 (q;q)3
∞θ(b1t;q)θ(ar/b1t;q)θ(ar;q)
θ(t;q)θ(art;q)θ(b1;q)θ(ar/b1;q) ... (q;q)3
∞θ(br−1t;q)θ(ar/br−1t;q)θ(ar;q)
θ(t;q)θ(art;q)θ(br−1;q)θ(ar/br−1;q)

 . (18)
Then from the modularity of the Dedekindη-function and the Jacobiθ-function the matrix
−→
M
satisﬁes the modular transformation (6) with weights κU = (0, 1,..., 1) and κV = (0,..., 0).
When a,b are specialised at points where there are singularities, one can take coeﬃcients
of the expansion around these points to deﬁne U,V .
Theorem 1.4 states that the generalised q-hypergeometric equation is modular. The the-
orem will also hold when we specialise the values of a,b . This is because the integral repre-
sentations of the cocycle will be regular at these specialisations and the factorisation of the
integral will similarly involve the expansion around these points as it will involve computation
of residues of higher order.
Theorem 1.4. The two cocycles (4) ΩU and ΩV are equal and modular.
The proof of the above theorem is given in Section 3 and uses an integral representation of
the solutions of Equation (11) in terms of a special function, the Faddeev quantum diloga-
rithm [23, 24], the factorisation of the corresponding integrals (so-called state integrals) as a
bilinear combination functions of z,τ and (z/τ,−1/τ) along the lines of [30], combined with
an explicit description of the self-duality of the corresponding q-holonomic module. What
is more, the U and the V cocycles are obtained by moving the contour of integration of
the state integral upwards or downwards, respectively, and this is one explanation of their
equality. We also remark that the above theorem is valid for r = 1, where the corresponding
cocycle is none other than a ratio of two Faddeev quantum dilogarithms.
