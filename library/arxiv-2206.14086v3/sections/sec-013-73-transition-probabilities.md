---
doc_id: arxiv-2206.14086v3
doc_title: "KPZ limit theorems Jinho Baik∗"
section_id: sec-013-73-transition-probabilities
section_title: "Transition probabilities"
section_number: 7.3
pages: 10-12
source_pdf: 2206.14086v3.pdf
source_sha256: b6c27f820f963079
doc_brief: "KPZ limit theorems Jinho Baik∗ — One-dimensional interacting particle systems, 1+1 random growth models, and two-dimensional di- rected polymers deﬁne 2d height ﬁelds."
---
We mentioned in Subsection 3.4 that one way of proving a KPZ limit theorem for the TASEP is to compute
the transition probabilities explicitly and then take an appropriate sum to ﬁnd the ﬁnite-time distribution
functions. The summation part is often more technical, but here we discuss the transition probabilities to
see how (7.4) arises.
Suppose that there are only N particles for the TASEP on Z. Let WN = {(a1, · · · , aN) ∈ZN : a1 <
· · · < aN} be the ordered set of the particle locations. Sch¨utz [80] showed that
PY (X; t) = det
 1
2πi
I
sj−i+1(s + 1)−xi+yj+i−jetsds
N
i,j=1
(7.5)
for X and Y in WN, where the contour is a circle that encloses the points s = 0, −1.
For the periodic TASEP, the particle locations can be represented by the set
WL
N = {(a1, · · · , aN) ∈ZN : a1 < · · · < aN < a1 + L}.
Note that if we consider the TASEP on a ring, this set keeps track of global circulations of the particles. We
showed in [9] that
PY (X; t) =
I
det
"
1
L
X
w
wj−i+1(w + 1)−xi+yj+i−jetw
w + N/L
#N
i,j=1
dz
2πiz
(7.6)
for X, Y ∈WL
N, where the integral contour for z is any circle enclosing the origin, and the sum inside is over
the roots of the equation
wN(w + 1)L−N = z.
(7.7)
See Figure 12.
10
Figure 12: Bethe roots when L = 24 and N = 8 for three values of z
We now explain the equation (7.7). Due to the periodicity, if A = (a1, · · · , aN) is in WN(L), then A′ =
(a2, · · · , aN, a1 +L) also represents the same particle conﬁguration of the periodic TASEP. Thus, the transi-
tion probability should remain the same if we replace (x1, · · · , xN) and (y1, · · · , yN) by (x2, · · · , xN, x1 + L)
and (y2, · · · , yN, y1 + L), respectively. We can check directly that the determinant in (7.6) is unchanged
thanks to the equation (7.7). Equation (7.7) takes care of the labeling ambiguity in the periodic case. Here
the variable z could have been any ﬁxed constant, but making it as a free parameter turns out to be the
right choice. Since (7.5) and (7.6) were found by solving the Kolmogorov forward equation using the Bethe
ansatz method, the roots of (7.7) are called the Bethe roots.
Now, if we set L = 2N, w = −1
2 +
s
2
√
2N , and z = (−4)−Nζ in (7.7), and let N →∞, then the equation
becomes e−s2/2 = ζ, which is (7.4).
8
Integrable diﬀerential equations
Distribution functions of the KPZ ﬁxed point have connections to deterministic integrable diﬀerential equa-
tions. As proved in 1994 [86], the Tracy-Widom distribution is expressible in terms of the Painlev´e II equation,
one of a family of six special nonlinear ordinary diﬀerential equations [43]. The papers [2,20,73,87,92] also
found diﬀerential equations for equal-time, multi-position distribution functions of the KPZ ﬁxed point. We
state the following result for multi-point distributions for both inﬁnite and periodic domains.
Deﬁne the parameters
ti = τi/3,
yi = γi,
xi = hi,
and let
∂t =
m
X
i=1
∂ti,
∂y =
m
X
i=1
∂yi,
∂x =
m
X
i=1
∂xi.
Theorem 8.1 ( [12,13]). Let K = Kζ be the operator in either (7.1) or (7.3). If det(1 −K)̸ = 0, which holds
for all but at most countably many parameters, then
∂2
x log det(1 −K) = −rT p
for complex-valued m × 1 vector functions p(t, y, x) and r(t, y, x) which satisfy the equations
∂yp = 1
2∂2
x p −prT p,
∂yr = −1
2∂2
x r + rpT r
(8.1)
and
∂tp + ∂3
x p −3(∂xp)rT p −3prT (∂xp) = 0,
∂tr + ∂3
x r −3(∂xr)pT r −3rpT (∂xr) = 0.
(8.2)
Equation (8.2) is a coupled system of vector-valued modiﬁed Korteweg-De Vries (mKdV) equations. The
scalar mKdV equation is ∂tf +∂3
x f −6(∂xf)f 2 = 0. On the other hand, equation (8.1) forms a coupled system
11
(n, k)
0
t1n
t2n
n
