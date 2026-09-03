---
doc_id: arxiv-1409.2849v1
doc_title: "MOD-GAUSSIAN CONVERGENCE AND ITS APPLICATIONS FOR MODELS OF STATISTICAL MECHANICS"
section_id: sec-002-12-the-method-of-joint-cumulants
section_title: "The method of joint cumulants"
section_number: 1.2
pages: 5-7
source_pdf: 1409.2849v1.pdf
source_sha256: 7bf9646716fbb247
doc_brief: "MOD-GAUSSIAN CONVERGENCE AND ITS APPLICATIONS FOR MODELS OF STATISTICAL MECHANICS — In this paper we complete our understanding of the role played by the lim- iting (or residue) function in the"
---
Kxr≥3 as the limiting residue in mod-Gaussian convergence is a phenomenon that oc-
curs not only for sums of i.i.d. random variables, but more generally for sums of pos-
sibly non identically distributed and/or dependent random variables. For instance,
(1) the number of zeroes of a random Gaussian analytic function ∑∞
k=0(NC)k zk in
the disk of radius 1− 1
n;
(2) the number of triangles in a random Erdös-Rényi graph G(n, p);
are both mod-Gaussian convergent after proper rescaling, and with limiting function
of the form exp(Lz3), with the constantL depending on the model (see again [FMN13]).
The reason behind these universal asymptotics lies in the following method of cumu-
lants. If X is a random variable with convergent Laplace transform E[ezX ] on a disk,
we recall that its cumulant generating function is
log E[ezX ] = ∑
r≥1
κ(r)(X)
r! zr, (3)
which is also well-deﬁned and holomorphic on a disk around the origin. Its coefﬁcients
κ(r)(X) are the cumulants of the variable X, and they are homogenenous polynomials
in the moments of X; for instance, κ(1)(X) = E[X], κ(2)(X) = E[X2]− E[X]2, and
κ(3)(X) = E[X3]− 3 E[X2] E[X] + 2 E[X]3.
Consider now a sequence of random variables (Wn)n∈N with κ(1)(Wn) = 0, and for
r≥ 2,
κ(r)(Wn) = Kr αn (1 + o(1)), (4)
with αn→ +∞. This assumption is inspired by the case of a sum Wn = ∑n
i=1 Yi of
centred i.i.d. random variables for which κr(Wn) = n κ(r)(Y). If it is satisﬁed, then one
can formally write
log E
[
e
z Wn
(αn)1/3
]
= ( αn)−2/3 κ(2)(Wn) z2
2 + (αn)−1 κ(3)(Wn) z3
6 + ∑
r≥4
κ(r)(Wn)
r! ((αn)−1/3z)r
≃ (αn)1/3 K2 z2
2 + K3 z3
6 + ∑
r≥4
Kr zr
r! (αn)1−r/3
≃ (αn)1/3 K2 z2
2 + K3 z3
6
whence the mod-Gaussian convergence of Xn = ( αn)−1/3 Wn, with parameters tn =
K2 (αn)1/3 and limiting function exp (K3 z3/6). The approximation is valid if the o(1)
6 PIERRE-LOÏC MÉLIOT AND ASHKAN NIKEGHBALI
in the asymptotics of κ(2)(Wn) is small enough (namely o((αn)−1/3)), and if the series
∑r≥4 can be controlled, which is the case if
∀r,|κ(r)(Wn)|≤ (Cr)r αn (5)
for some constant C. The method of cumulants in the setting of mod-Gaussian con-
vergence amounts to prove (4) for the ﬁrst cumulants of the sequence (Xn)n∈N, and
(5) for all the other cumulants. From such estimates one then obtains mod-Gaussian
convergence for an appropriate renormalisation of (Wn)r≥3, with limiting function
exp(Kr zr/r!), where r is the smallest integer greater or equal than 3 such that Kr⁄= 0.
This method of cumulants works well with sequences (Wn)n∈N that write as sums
of (weakly) dependent random variables. Indeed, cumulants admit the following gen-
eralization to families of random variables, see [LS59]. Denote Qr the set of partitions
of [ [1, r] ]={1, 2, 3, . . . ,r}, and µ the Möbius function of this poset (see [Rot64] for basic
facts about Möbius functions of posets):
µ(Π) = (−1)𝓁(Π)−1 (𝓁(Π)− 1)!
where 𝓁(Π) = s if Π = π1⊔ π2⊔···⊔ πs has s parts. The joint cumulant of a family
of r random variables with well deﬁned moments of all order is
κ(X1, . . . ,Xr) = ∑
Π∈Qr
µ(Π)
𝓁(Π)
∏
i=1
E
[
∏
j∈πi
Xj
]
.
It is multilinear and generalizes Equation (3), since
κ(X1, . . . ,Xr) = ∂r
∂z1∂z2··· ∂zr
⏐⏐⏐⏐
z1=···=zr=0
(
log E[ez1X1+···+zrXr ]
)
κ
(
X, . . . ,X| {z }
r times
)
= κ(r)(X).
Suppose now that Wn = W = ∑n
i=1 Yi is a sum of dependent random variables. By
multilinearity,
κ(r)(W) = ∑
i1,...,ir
κ(Yi1, . . . ,Yir ), (6)
so in order to obtain the bound (5), it sufﬁces to bound each "elementary" joint cumu-
lant κ(Yi1, . . . ,Yir ). To this purpose, it is convenient to introduce the dependency graph
of the family of random variables (Y1, . . . ,Yn), which is the smallest subgraph G of
the complete graph on n vertices such that the following property holds: if (Yi)i∈I and
(Yj)j∈J are disjoint subsets of random variables with no edge ofG between a variableYi
and a variable Yj, then (Yi)i∈I and (Yj)j∈J are independent. Then, in many situations,
one can write a bound on the elementary cumulant κ(Yi1, . . . ,Yir ) that only depends
on the induced subgraph G[i1, . . . ,ir] obtained from the dependency graph by keeping
only the vertices i1, . . . ,ir and the edges between them. In particular:
(1) κ(Yi1, . . . ,Yir ) = 0 if the induced graph G[i1, . . . ,ir] is not connected.
(2) if|Yi|≤ 1 for all i, then|κ(Yi1, . . . ,Yir )|≤ 2r−1 ST(G[i1, . . . ,ir]), where ST(H) is
the number of spanning trees on a (connected) graph H.
MOD-GAUSSIAN CONVERGENCE AND APPLICATIONS FOR MODELS OF STATISTICAL MECHANICS 7
By gathering the contributions to the sum of Formula (6) according to the nature and
position of the induced subgraphG[i1, . . . ,ir] in G, one is able to prove efﬁcient bounds
on cumulants of sums of dependent variables, and to apply the method of cumulants
to get their mod-Gaussian convergence. We refer to [FMN13] for precise statements,
in particular in the case where each vertex in G has less than D neighbors, with D
independent of the vertex and of n. In Section 5, we shall apply this method to a case
where G is the complete graph onn vertices, but where one can still ﬁnd correct bounds
(and in fact exact formulas) for the joint cumulants κ(Yi1, . . . ,Yir ): the one-dimensional
Ising model.
