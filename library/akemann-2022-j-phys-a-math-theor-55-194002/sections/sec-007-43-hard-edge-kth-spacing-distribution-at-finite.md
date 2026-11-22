---
doc_id: akemann-2022-j-phys-a-math-theor-55-194002
doc_title: "Consecutive level spacings in the chiral Gaussian unitary ensemble: from the hard and soft edge to the bulk"
section_id: sec-007-43-hard-edge-kth-spacing-distribution-at-finite
section_title: "Hard edge kth spacing distribution at finite-"
section_number: 4.3
pages: 20-21
source_pdf: Akemann_2022_J._Phys._A__Math._Theor._55_194002.pdf
source_sha256: 3753499c4b23f189
toc_source: outline
doc_brief: "Consecutive level spacings in the chiral Gaussian unitary ensemble: from the hard and soft edge to the bulk — 20 sections: Front matter; Consecutive level spacings in the ; Introduction"
---
Inserting the expression (72) as well as (57) into (42), we obtain the following relatively com-
pact expression for the spacing distribution at the hard edge between the kth and (k + 1)st
smallest eigenvalue for arbitrary k, with Nf flavours and topology ν at fixed n. Recalling the
definition of the shifted variables from (61), we have
(73)
The expression (73) is our first main result and will serve as the starting point for the asymptotic
analysis in the next section.
Before we come to this, let us make some comments on the duality between the index ν
and the number of flavours with mass 0. Indeed, when taking the limit mNf →0, the result
(73) reduces to the case Nf →Nf −1 and ν →ν + 1. This can be readily checked, while the
other limit mNf →∞leads to the partially quenched case Nf →Nf −1 and ν →ν, meaning
the index ν stays the same.
Let us give some simple examples. In the absence of flavours (Nf = 0) and zero-modes
(ν = 0), we obtain the following expression for the kth spacing in the χGUE with square
matrices
p(0,0)
k,n (s) =
2n
(k −1)!
 ∞
0
dxk
 xk
0
dx1 . . .
 xk
0
dxk−1
k
j=1
((xk + s)2 −x2
j)2x je−x2
j
× (xk + s) e−(n−k)(xk+s)2 det
)
K(χGUE)
2,n−1 (x2
c −(xk + s)2, x2
e −(xk + s)2)
*k
c,e=1.
(74)
Here, all shifted variables are explicitly written out. In particular, for the spacing between the
first and second eigenvalue (k = 1) we obtain a one-fold integral representation
p(0,0)
1,n (s) = 4
 ∞
0
dx1 s2(2x1 + s)2x1(x1 + s)e−x2
1−(n−1)(x1+s)2
×

L(2)
n−1(−s(2x1 + s))L(2)
n−2(−s(2x1 + s))−L(3)
n−2(−s(2x1 + s))L(1)
n−1(−s(2x1 + s))

,
(75)
where we inserted (53) for the kernel at equal arguments. This result still has to be unfolded,
as explained at the end of section 4.
In figure 2 (top row), we compare (75) for small values of n and the convergence to the
asymptotic limit. The result for k = 1 at n = 2 is already very close to the limiting result,
showing the optimal rate of convergence 1/n2 at the hard edge, as it was shown in [46]. This
certainly is also true when increasing k to k = 2 and k = 3, see bottom row of figure 2. The
19
J. Phys. A: Math. Theor. 55 (2022) 194002
G Akemann et al
Figure 2. Top left: the spacing distribution ¯p(0,0)
1,n (σ) between 1st and 2nd eigenvalue
(k = 1) at the hard edge, rescaled to first moment of unity, for different values of
n = 2 (blue), n = 6 (orange), n = 10 (green), and n = 20 (red). The dashed curve is the
bulk spacing distribution (A.1) for comparison. Top right: because the curves are almost
indistinguishable we also compare the difference Δ¯pk(s) between the asymptotic spacing
(90) to be derived in the next section, and our expression at finite-n (53), for n = 2 (blue),
n = 4 (orange), n = 6 (green), n = 8 (red), n = 10 (purple), and n = 20 (dashed black).
Bottom row: differences of the finite n spacing (73) to their asymptotic counterpart
(86) for k = 2, n = 4, 6, 8, 10, 20 (left), and k = 3, n = 4, 8, 20 (right). In both plots the
dashed line denotes the difference for n = 20, both with their first moment set to unity.
These plots illustrate the rapid convergence already at relatively small values of n. Please
note the different scales of the y-axis.
reason why the optimal rate of convergence applies here is that we unfold via the formula (44),
since in [46] it was shown that already a scaling is sufficient to reach this rate.
Since the deviations of the finite n-results and the asymptotic ones lie in the per mill regime,
we have plotted the difference Δ¯pk(s) = ¯p(0,0)
k,n (s) −¯p(0,0)
k
(s). The bar highlights the unfolding
(44), and p(0,0)
k
(s) is the asymptotic result (86).
