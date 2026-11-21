---
doc_id: arxiv-math-0008027v1
doc_title: "arXiv:math/0008027v1 [math.GT] 3 Aug 2000"
section_id: sec-004-33-hyperbolicity-condition
section_title: "Hyperbolicity condition"
section_number: 3.3
pages: 8-9
source_pdf: 0008027v1.pdf
source_sha256: 8bce0b8a1bca372e
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.927
latex_coverage_ratio: 0.953
doc_brief: "arXiv:math/0008027v1 [math.GT] 3 Aug 2000 — I follow Y."
---
Now we have a *topological* ideal tetrahedron decomposition of $S^3\setminus{K}$. To introduce a complete hyperbolic structure, we regard each tetrahedron as an ideal hyperbolic tetrahedron parameterized by a complex number with positive imaginary part. This complex parameter $z$ is chosen as follows. First recall that an ideal hyperbolic tetrahedron can be characterized by a Euclidean triangle. (If we consider the upper half space model of the hyperbolic space, then an ideal hyperbolic tetrahedron can be located so that one ideal vertex is at the infinity and the other three are on the $xy$-plane. Then one face of the tetrahedron is in a hemisphere and the other three are in upper half planes perpendicular to the $xy$-plane. Our triangle is the intersection of the three half planes and the $xy$-plane.) If one puts the triangle on the complex plane with two vertices on $0$ and $1$, then the other is on $z$. Note that there are three ways to choose such a parameter (Figure [1](#fig:triangle){reference-type="ref" reference="fig:triangle"}).

![Similar triangles parameterized by different complex numbers.](triangle.eps){#fig:triangle}

For the tetrahedron with vertex $b_2^{\ast}$ we associate $b\in\mathbb{C}$ and that with $d_4^{\ast}$ we associate $d\in\mathbb{C}$, where $\ast$ is $+$, $-$, $r$, or $l$. In the cusp torus the triangle labeled $b_2^{\ast}$ and $d_4^{\ast}$ are similar to the triangles parameterized by $b$ and $d$ respectively for any $\ast$.

It is well known that if the following two conditions are satisfied, then an ideal tetrahedron decomposition parameterized as above defines a hyperbolic structure (more precisely complete hyperbolic structure). (See for example [@Neumann/Zagier:TOPOL85; @Neumann92].)

1.  Consistency condition: at each vertex in the cusp torus, the product of the parameter around the vertex is $1$, and

2.  Cusp condition: the products of the parameters along the latitude and the meridian are $1$. Here the parameter of a triangle along a loop is the parameter associated to the small triangle cut by the loop.

::: rem
The consistency condition means that at each edge of the tetrahedron decomposition the sum of the dihedral angles is equal to $2\pi$. The cusp condition means that the cusp torus is Euclidean.
:::

In our example we have two edges, one connecting $b_2^l=b_2^-$ and $b_2^r=b_2^+$ and the other connecting $d_4^l=d_4^+$ and $d_4^r=d_4^-$. So from the consistency condition we have the following two equations since the consistency conditions of two vertices on the torus are the same if they belong to the same edge. $$\begin{aligned}
  b\left(\frac{1}{1-d}\right)b\left(1-\frac{1}{d}\right)
  \left(1-\frac{1}{b}\right)\left(1-\frac{1}{d}\right)&=1,
  \\
  d\left(\frac{1}{1-b}\right)\left(\frac{1}{1-d}\right)
  \left(\frac{1}{1-b}\right)d\left(1-\frac{1}{b}\right)&=1.
\end{aligned}$$ From the cusp condition we have the following two equations. $$\begin{aligned}
  \mu&: b^{-1}d=1,
  \label{eq:meridian}
  \\
  \lambda&:
  \left(\frac{1}{1-b}\right)^{-1}d
  \left(1-\frac{1}{b}\right)^{-1}\left(\frac{1}{1-d}\right)
  \\
  &\quad\times\left(\frac{1}{1-b}\right)^{-1}d
  \left(1-\frac{1}{b}\right)^{-1}\left(\frac{1}{1-d}\right)
  =1.\notag
\end{aligned}$$ From [\[eq:meridian\]](#eq:meridian){reference-type="eqref" reference="eq:meridian"} we have $b=d$ and then the rest are all equivalent to $b^2-b+1=0$. Since the imaginary part of $b$ should be positive, we have $b=d=\exp(\pi\sqrt{-1}/3)$ and so the two tetrahedra should be regular.
