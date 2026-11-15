---
doc_id: deturck-melvin-gluck-komendarczyk-shonkwiler-2008-triple-lin
doc_title: "Triple linking numbers, ambiguous Hopf invariants and integral formulas for three-component links"
section_id: sec-007-the-fundamental-solution-of-the-laplacian-on-the
section_title: "The fundamental solution of the Laplacian on the 3-torus"
section_number: null
pages: 25-26
source_pdf: deturck-melvin-gluck-komendarczyk-shonkwiler-2008-triple-linking-numbers.pdf
source_sha256: db149864ce367da2
toc_source: outline
doc_brief: "Triple linking numbers, ambiguous Hopf invariants and integral formulas for three-component links — Three-component links in the 3-dimensional sphere were classi- fied up to link homotopy by John"
---
The fundamental solution of the Laplacian on the
3-torus
Proposition 1. The fundamental solution of the scalar Laplacian on the
3-torus T 3 = S1 × S1 × S1 is given by the formula
φ(x, y, z) = −1
8π3
∞
X
m,n,p=−∞
m2+n2+p2̸=0
ei(mx+ny+pz)
m2 + n2 + p2 .
Even though we have expressed φ in terms of complex exponentials, the
value of φ is real for real values of x, y and z because of the symmetry
of the coefficients, and can therefore also be expressed as a Fourier cosine
series.
Figure 12 shows the graph of the corresponding fundamental solution
of the scalar Laplacian on the 2-torus S1 × S1, displayed over the range
−3π ≤x, y ≤3π. If we think of the 2-torus as obtained from a square by
identifying opposite sides, then this shows the function φ to have a nega-
tive infinite minimum at the single vertex, two saddle points in the middle
of the two edges, and a maximum in the middle of the square. Presum-
ably the fundamental solution φ on the 3-torus displays a corresponding
distribution of critical points.
To see why the proposition is true, begin with functions u and v in
C∞(T 3), with Fourier series
u =
X
umnpei(mx+ny+pz)
and
v =
X
vmnpei(mx+ny+pz),
where the sums are over all (m, n, p) ∈Z3. The following observations
result from elementary calculations (ignoring convergence issues):
276
DETURC, GLUCK, KOMENDARCZYK, MELVIN et al
Figure 12: Fundamental solution of the scalar Laplacian on S1 × S1
 ∆u = −P(m2 + n2 + p2)umnpei(mx+ny+pz), so v is in the image of
the Laplacian if and only if the Fourier coefficient v000 = 0, i.e., iff
v has average value 0.
 The Fourier series of the convolution u∗v is given by coefficient-wise
multiplication, i.e.,
u ∗v = 8π3 X
umnpvmnpei(mx+ny+pz).
Thus, if v has average value zero, we have that ∆(φ ∗v) = v, and so
φ is the fundamental solution of ∆.
The theory of Sobolev spaces provides the analytical justification of these
formal observations in order to prove the proposition.
