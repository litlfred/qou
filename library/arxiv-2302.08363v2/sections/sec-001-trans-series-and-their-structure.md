---
doc_id: arxiv-2302.08363v2
doc_title: "On the structure of trans-series in quantum field theory"
section_id: sec-001-trans-series-and-their-structure
section_title: "Trans-series and their structure"
section_number: null
pages: 3-5
source_pdf: 2302.08363v2.pdf
source_sha256: c2244e03b17048fb
toc_source: outline
doc_brief: "On the structure of trans-series in quantum field theory — Many observables in quantum field theory can be expressed in terms of trans-series, in which one adds to the perturbative series a typically"
---
Trans-series and their structure
In this paper we will consider trans-series involving two small parameters: a coupling constant g
and an exponentially small term of the form
y = g−be−A/g.
(2.1)
– 2 –
These trans-series are of the form
Φ =
X
ℓ≥0
yℓφℓ(g),
(2.2)
where
φℓ(g) =
X
n≥0
an,ℓgn
(2.3)
are formal power series in g. Some of the examples we will consider will be however slightly
more general, including for example logarithmic terms, or involving finite sums of expressions
like (2.2). The series φ0(g) is the perturbative series, and the higher order series φℓ(g), with
ℓ≥1, are non-perturbative corrections. These could be of the instanton or the renormalon type,
and in this paper we will consider both of them. In general the coefficients an,ℓfor ℓ≥1 are
complex and they depend on a choice of lateral resummation (in the case of ODEs, there is a
dependence on a trans-series parameter C, and different choices of resummation lead to different
choices of C). We will specify such a choice as needed.
The series φℓ(g) are typically Gevrey-1, i.e. their coefficients have the factorial growth
an,ℓ∼n!,
n ≫1,
(2.4)
at fixed ℓ. This means that φℓ(g) have zero radius of convergence. One way to make sense of
these series is to use generalized or lateral Borel resummations s±(φ)(g) (see e.g. [31] for an
introductory survey of Borel resummation techniques). We will assume that these resummations
exist, for sufficiently small g. The Borel resummed trans-series is then given by
s±(Φ) =
X
ℓ≥0
yℓs±(φℓ)(g).
(2.5)
As we see, this object is itself an infinite sum over all exponentially small corrections. Even if the
lateral Borel resummations exist and one can make sense in this way of the factorially divergent
series φℓ(g), the sum over the infinite number of non-perturbative sectors is potentially a new
source of divergences. In the case of nonlinear ODEs, this infinite sum is known to converge
provided Re(g/A) is not too large [2], but in general one has to address this convergence issue.
We can reorganize Φ in a different way, suggested by the work of [4] on non-linear ODEs:
for each fixed power of g, n, we consider the series
Gn(y) =
X
ℓ≥0
an,ℓyℓ,
(2.6)
so that we can write, formally,
Φ =
X
n≥0
gnGn(y).
(2.7)
We will call Gn(y) the n-th partial series of the trans-series Φ. An important result of [4] is that,
for non-linear ODEs, the partial series Gn(y) are convergent, and they have the same radius of
convergence for all n. Generically, we expect
an,ℓ∼ℓ−bnR−ℓ,
ℓ≫1,
(2.8)
for fixed n. The common radius of convergence is R, while the exponents bn depend in general
on n.
– 3 –
In many situations, like the one considered in [4], the convergence property of the partial
series is closely related to the convergence of the sum over exponential corrections in the Borel
resummed trans-series (2.5).
Heuristically, this can be argued as follows.
If g is sufficiently
small, we can approximate the lateral Borel resummations appearing in (2.5) by uniform optimal
truncations, i.e. we can truncate all factorially divergent series φℓ(g) in (2.3) at the same n = N⋆.
This is because all these series have the same rate of divergence. The resulting approximation
is nothing but the sum of the first N⋆functions Gn(y), which is convergent if the partial series
converge.
Let us note that the radius R signals the occurrence of a common singularity in the functions
Gn(y). One can ask what is the relation between the location of the singularity in the Gns, and
the location of the singularities of the exact function represented by the resummed trans-series Φ.
As explained in [4], the singularity in the Gns gives the first term in an asymptotic approximation
to the singularities of the exact function. In the case of nonlinear ODEs, one also has that, for
a fixed |y| < R in the common domain of convergence, the functions Gn(y) grow factorially [4],
Gn(y) ∼n!,
n ≫1.
(2.9)
Therefore, the expansion (2.7) provides an asymptotic representation of the Borel-resummed
trans-series for small g and |y| < R which is very different from the asymptotic representation
provided by φ0(g). We believe that the behavior (2.9) also occurs in the QFT trans-series which
satisfy the convergence property.
In the following sections, we will consider interesting examples in QFT where the convergence
property of the trans-series holds.
