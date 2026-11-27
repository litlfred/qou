---
doc_id: arxiv-0712.2456v4
doc_title: "Nonlinear Fluid Dynamics from Gravity"
section_id: sec-023-5-the-metric-and-stress-tensor-at-second-order
section_title: "The metric and stress tensor at second order"
section_number: 5
pages: 24-28
source_pdf: 0712.2456v4.pdf
source_sha256: c5fb02c494169403
toc_source: inferred
doc_brief: "Nonlinear Fluid Dynamics from Gravity — Black branes in AdS 5 appear in a four parameter family labeled by their velocity and temperature."
---
In order to obtain the metric and stress tensor at second orde r in the derivative expansion,
we follow the method outlined in § 3 and implemented in detail in § 4 to leading order.
Concretely, we choose coordinates such that β(0)
i = 0 and b(0) = 1 at the point xµ = 0.
The metric g(0) + g(1) given in (4.24) may be expanded to second order in derivative s.
This involves Taylor expanding g(0) to second order and g(1) to ﬁrst order, the second order
analogue of (4.1). As we have explained in § 3.4, at this stage we also make the substitution
b(0) → b(0) + b(1), and treat b(1) as an order ε term, and so retain only those expressions
that are of ﬁrst derivative order in b(1) (and contain no other derivatives). This process is
straightforward and we will not record the (rather lengthy) resultant expression here. To
this expression we add the as yet undetermined metric ﬂuctua tion
g(2)
αβ dxα dxβ = −3 h2(r) dv dr + r2 h2(r) dxi dxi + k2(r)
r2 dv2 + 2 j(2)
i (r)
r2 dv dxi + r2α(2)
ij dxi dxj.
(5.1)
We plug this metric into Einstein’s equations and obtain a se t of linear second order
diﬀerential equations that determine h2, k2, j(2)
i , α(2)
ij . As in the previous section, SO(3)
symmetry ensures that the equations for the scalars h2, k2, the vectors j(2)
i , and the tensor
α(2)
ij do not mix. Moreover, as we have explained in § 3, the equations that determine
these unknown functions are identical to their ﬁrst order co unterparts in the homogeneous
terms, but diﬀer from those equations in the sources. As a res ult, the only new calculation
we have to perform in order to obtain the metric at second orde r is the computation of the
source terms. Once these terms are available, the correspon ding equations may easily be
integrated, as in the previous section.
Recall that the input metric into Einstein’s equations incl udes terms that arise out
of the Taylor expansion of g(0) + g(1) that have explicit factors of the coordinates xµ .
Nonetheless, a very simple argument assures us that the sour ce terms in the equations
that determine g(2) must all be independent of xµ . The argument runs as follows: We
have explicitly constructed g(1) in the previous section so that EM N
(
g(0) + g(1))
= OM N
where OM N is a local expression constructed out of second order or high er xµ derivatives
of velocity and temperature ﬁelds. It follows that xµ dependence of sources, which may be
obtained by Taylor expanding OM N about xµ = 0, occurs only at the three derivative level
or higher. It follows that source terms at the two derivative level have no xµ dependence.
Clearly, this argument has a direct analogue at arbitrary or der in perturbation theory.
A crucial input into the argument of the last paragraph was th e fact that g(0) + g(1)
satisﬁes Einstein’s equations in a neighbourhood of xµ = 0 (and not just at that point).
As we have seen in the previous section, the fact that the ener gy conservation equation is
obeyed at xµ = 0 allows us to express all ﬁrst derivatives of temperature i n terms of ﬁrst
derivatives of velocities (see (4.10) and (4.4)). In additi on, β(0)
i and b(0) must be chosen
so that (3.12) is satisﬁed. The sixteen equations (3.12) can be grouped into sets that
transform under SO(3) as two scalars, three vectors and one tensor ( i.e., 5). We will now
explain how these constraints may be used to solve for 16 of th e independent expressions
of second order in derivatives of velocity and temperature ﬁ elds.
In order to do this, let us ﬁrst list all two derivative ‘sourc e’ terms that can be built
out of second derivatives of b(0) or β(0)
i , or out of squares of ﬁrst derivatives of β(0)
i . These
expressions may be separated according to their transforma tion properties under SO(3) as
scalars, vectors and tensors and higher order terms. The hig her order pieces will not be
of interest to us. An exhaustive list of these expressions th at transform in the 1, 3 or 5 is
given in Table 1. 20 We deﬁne the vector ℓi as the curl of the velocity i.e.,
1 of SO(3) 3 of SO(3) 5 of SO(3)
s = 1
b ∂2
v b vi = 1
b ∂i∂vb tij = 1
b ∂i∂jb − 1
3 s δij
s = ∂v∂iβi vi = ∂2
v βi tij = ∂(iℓj)
s = 1
b ∂2b vi = ∂vℓi tij = ∂vσij
S = ∂vβi ∂vβi vi = 9
5∂jσji − ∂2βi Tij = ∂vβi ∂vβj − 1
3 S δij
S = ℓi ∂vβi vi = ∂2βi Tij = ℓ(i ∂vβj) − 1
3 S δij
S = (∂iβi)2 Vi = 1
3(∂vβi)(∂jβj) Tij = 2 ǫkl(i ∂vβk ∂j)βl + 2
3 S δij
S = ℓi ℓi Vi = −ǫijk ℓj ∂vβk Tij = ∂kβk σij
S = σij σij Vi = σij ∂vβj Tij = ℓi ℓj − 1
3 S δij
Vi = ℓi ∂jβj Tij = σik σk
j − 1
3 S δij
Vi = σij ℓj Tij = 2 ǫmn(i lm σn
j)
Table 1: An exhaustive list of two derivative terms in made up from the temperature
and velocity ﬁelds. In order to present the results economic ally, we have dropped the
superscript on the velocities βi and the inverse temperature b, leaving it implicit that these
expressions are only valid at second order in the derivative expansion.
ℓi = ǫijk ∂jβk , (5.2)
and the symmetric traceless tensor σij has been previously deﬁned in (4.17).
As a simple check on the completeness of expressions in Table 1, notice that the number
of degrees of freedom in those of the tabulated expressions t hat are formed from a product
of two single derivatives is 5 (in the scalar sector), 5 × 3 (in the vector sector), and 7
20Note that the tensors are symmetric in their indices. The sym metrization as usual is indicated by
parentheses.
× 5 in the tensor sector, leading to a total of 55 real parameters . Together with degrees
of freedom from the two 7s and one 9 that can also be formed from the product of two
derivatives (but will play no role in our analysis) this give s 78 degrees of freedom. This
is in agreement with the expected 1
2 × 12 × 13 =78 ways of getting a symmetric object
from twelve parameters (the ﬁrst derivatives of the velocit y ﬁelds). On the other hand, the
genuinely two derivative terms in Table 1 have 3 × 1 + 5× 3 + 3× 5 = 33 degrees of freedom
which together with a two derivative term that transforms in the 7 (which however plays
no role in our analysis) is the expected number 40 = 10 × 4 of two derivative terms arising
from temperature and velocity ﬁelds.
Assuming that we have already employed the ﬁrst order conser vation equation (3.6) to
eliminate the ﬁrst derivatives of b, we have to deal with the constraint equation (3.12) at
the second order. Using the list of second order quantities g iven in Table 1, it is possible to
show that (3.12) take the form of the following linear relati ons between these two derivative
terms:
s = 1
3 s − S + 1
9 S + 1
6 S − 1
3 S
s = s − S + 1
2 S − S
vi = 10
9 vi + 1
9 vi + 1
3 Vi − 1
3 Vi − 2
3 Vi
vi = 10
9 vi + 1
9 vi − 2
3 Vi + 1
6 Vi − 5
3 Vi
vi = −1
3 Vi + Vi
tij = tij + Tij + 1
3 Tij + 1
4 Tij + Tij .
(5.3)
Given these relations we now proceed to analyze the potentia l source terms arising from
the metric (4.24) at O (ε2). The analysis, as before, can be done sector by sector – the
computations for the scalar, vector and tensor sectors are g iven in § 5.1, § 5.2 and § 5.3,
respectively.
