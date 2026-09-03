---
doc_id: akemann-2022-j-phys-a-math-theor-55-194002
doc_title: "Mathematical and Theoretical PAPER • OPEN ACCESS Consecutive level spacings in the chiral Gaussian unitary ensemble: from the hard and soft edge to the bulk To cite this article: G"
section_id: sec-004-2-transition-from-bessel--and-airy--to-the-sine
section_title: "Transition from Bessel- and Airy- to the sine-kernel"
section_number: 2
pages: 5-6
source_pdf: Akemann_2022_J._Phys._A__Math._Theor._55_194002.pdf
source_sha256: 3753499c4b23f189
doc_brief: "Mathematical and Theoretical PAPER • OPEN ACCESS Consecutive level spacings in the chiral Gaussian unitary ensemble: from the hard and soft edge to the bulk To cite this article: G Akemann et al 2022"
---
The spacing between consecutive eigenvalues of random matrices with unitary symmetry in
the bulk of the spectrum is well-approximated by Wigner’s surmise [1, 11] for 2 × 2 GUE
matrices,
pWigner(s) = 32s2
π2 e−4s2/π.
(1)
We will also give a much more precise expression in appendix A, cf [14], which is universal.
In the present case of the χGUE also called complex Wishart–Laguerre ensemble, deviations
should show up at the hard edge because there the k-point correlation functions differ from the
ones in the bulk of the spectrum.
Before we address this question in terms of the nearest neighbour level spacing distribution
in detail, see section 3, let us investigatethe transition on the level of the kernelof the underlying
limiting determinantal point process, that is the transition from the Bessel-kernel at the hard
edge to the sine-kernel in the bulk. Additionally, we also discuss the transition from the Airy-
kernel at the soft edge to the sine-kernel in the bulk for completeness. Although we do not have
analytical results at the soft edge, we will numerically study this transition for the spacing as
well in section 5.3.
The eigenvalue statistics of the χGUE follows a determinantal point process. This means
the k-point correlation function of the eigenvalues has the form
Rk(x1, . . . , xk) = det [K(xa, xb)]a,b=1,...,k,
(2)
with correlation kernel K(xa, xb). This holds already at finite matrix size, see (48) in section 4,
as well as in the asymptotic scaling limit in the bulk, at the hard and soft edge. For example,
the microscopic level density is given by ρ(x) = R1(x).
The difference between the eigenvalue statistics at different locations in the spectrum can
be seen in the kernel which is the sine-kernel [14] inside the bulk of the spectrum,
Ksine(xa, xb) = sin[π(xa −xb)]
π(xa −xb)
,
(3)
and the Bessel-kernel [29, 30] at the hard edge of the spectrum,
Kν(xa, xb) = √xaxb
xbJν(xa)Jν−1(xb) −xaJν(xb)Jν−1(xa)
x2a −x2
b
,
(4)
where Jν is the Bessel function of the first kind and the index ν counts the number of zero
eigenvalues, measuring the strength of the repulsion from the origin. The Airy-kernel [30, 31]
KAiry(xa, xb) = Ai(xa)Ai′(xb) −Ai′(xa)Ai(xb)
xa −xb
,
(5)
is obtained at the soft edge of the spectrum, with Ai(x) and Ai′(x) the Airy function (of the first
kind) and its first derivative.All three kernels are universal for a broad class of systems and hold
for a much larger class of unitarily invariant ensembles of random matrices than Gaussian, see
the review by Kuijlaars [8, chapter 6]. For an extension to orthogonaland symplectic ensembles
see the book by Deift and Gioev [37].
In principle, all spectral information is contained in the kernels in the respective region of
the spectrum, including the spacing distribution. To assess the latter, one typically uses the gap
4
J. Phys. A: Math. Theor. 55 (2022) 194002
G Akemann et al
probability, the probability P[a,b] that an interval [a, b] does not contain eigenvalues, expressed
in terms of the Fredholm determinant of the corresponding kernel,
P[a,b] = det[1 −K[a,b]],
(6)
where the integral operator is
K[a,b]φ(x) =
 b
a
K(x, y)φ(y)dy,
(7)
for an arbitrary (L2-integrable) test function φ. The spacing distribution then follows by differ-
entiation, as it is explained in more detail in section 3. However, we will not follow this route
of Fredholm determinants and compute the spacing distribution in a different manner.
The second information that can be retrieved from the kernel is the mean level spacing. It
follows from the microscopic level density at large argument, which yields the macroscopic
level density at that point in the spectrum, which gives the inverse mean level spacing. This
quantity is important for the unfolding of the spacing distribution. From the sine-kernel we
have
R1,sine(x) = Ksine(x, x) = 1,
(8)
that is the mean level spacing is already normalised to unity. For the Bessel density we obtain
after using l’Hôpital’s rule
R1,ν(x) = Kν(x, x) = x
2

J2
ν(x) −Jν−1(x)Jν+1(x)
 x→∞
−→1
π ,
(9)
implying that the mean level spacing is π in this normalisation of the Bessel-kernel. We will
come back to this point in section 5. The soft edge is an exception, as here the macroscopic den-
sity vanishes at the point we zoom in. However, also here is it possible to unfold the spectrum
and we refer to [38].
The Bessel-kernel can yield the Airy- as well as the sine-kernel in certain limits, which is
rather expected. For instance, a large index ν pushes the spectral edge away from the origin so
that it becomes a soft edge, see e.g. [39], where this transition is studied on a microscopic level.
This limit is not in our main focus in the present work. On the other hand, when taking the limit
of large arguments in the Bessel-kernel, moving away from the hard edge, the sine-kernel is
obtained. We are interested how much the hard edge statistics differs from the bulk statistics
and will quantify this below in such a large-argument expansion.
To understand how the Bessel- and the sine-kernel are related, one needs to exploit the
following asymptotic expansion of the Bessel function [40, equation (10.17.3)]
Jν(x) =

2
πx

cos

x −π
