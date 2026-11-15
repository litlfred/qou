---
doc_id: arxiv-2302.08363v2
doc_title: "On the structure of trans-series in quantum field theory"
section_id: sec-000-introduction
section_title: "Introduction"
section_number: null
pages: 2-3
source_pdf: 2302.08363v2.pdf
source_sha256: c2244e03b17048fb
toc_source: outline
doc_brief: "On the structure of trans-series in quantum field theory — Many observables in quantum field theory can be expressed in terms of trans-series, in which one adds to the perturbative series a typically"
---
Introduction
1
2
Trans-series and their structure
2
3
The large N sigma model, revisited
4
4
Complex Chern–Simons theory
8
5
Integrable models
10
5.1
The free energy of integrable models
10
5.2
Bosonic models
13
5.2.1
Trans-series computation
14
5.2.2
Numerical analysis
19
5.3
The Gross–Neveu model
23
5.3.1
Summary of the recursive problem
24
5.3.2
Leading orders in ˜α
27
5.3.3
Numerical analysis
28
5.3.4
Large N solution
30
6
Conclusions and open problems
30
1
Introduction
It is widely believed that renormalized perturbation theory gives the asymptotic expansions of
observables in quantum field theory (QFT), when the coupling is small. The perturbative series
obtained in this way are typically factorially divergent, therefore they can only give approximate
results for the observables.
However, there are many situations in mathematics and physics
where perturbative series can be upgraded to trans-series, which provide exponentially small
corrections to the perturbative series. These trans-series then lead to exact results by using Borel
resummation. An example where this happens is the theory of non-linear ODEs developed by
´Ecalle, Costin and others (see [1–5], and [6] for a very readable introduction). Another example is
the exact WKB method in quantum mechanics, where an exact version of the Bohr–Sommerfeld
quantization condition is obtained by resumming a trans-series [7–9].
It has been conjectured in various forms and occasions that perturbative series in QFT
can be also upgraded to trans-series, in such a way that exact results can be obtained by their
resummation, in some domain of convergence of the coupling constant. Proving such a statement
in a non-trivial QFT is rather difficult, and even checking it (say, numerically) is not easy, since
there are very few examples in QFT where one can compute the actual trans-series reliably.
The resummation of a trans-series has, roughly speaking, two steps. First, one resums each
factorially divergent power series in the coupling constant, associated to a given exponential
correction. Then, one has to sum over all the exponentially small corrections. This last sum
– 1 –
is typically over an infinite number of terms, and its convergence (or lack thereof) poses an
additional problem. In the case of non-linear ODEs, both steps can be performed, and the sum
over exponentially small corrections converges to the actual solution of the ODE, provided the
expansion parameter is not too large [1–3]. In the case of generic observables in QFT, it has been
argued [10–12] that the sum of exponentially small corrections is generically factorially divergent.
In particular, it does not hold in the case of two-point functions in asymptotically free theories,
like the Adler function in QCD. The reason is that the singularity structure of general correlation
functions cannot be reproduced with a convergent trans-series. This phenomenon is sometimes
called, in the context of renormalon physics, the divergence of the OPE, and it is at the basis of
the so-called violation of quark-hadron duality (see [13] for a recent review). In these cases, the
reconstruction of the exact answer by Borel resummation of the trans-series is more involved,
since one has to do a further resummation of the factorially divergent series of exponentially
small corrections
In this paper we want to explore a property of trans-series, inspired by the theory of non-
linear ODEs, which provides indirect evidence for the convergence (or not) of the trans-series.
In a trans-series expansion we have typically two small expansion parameters: the coupling
constant g, and an appropriate exponential thereof e−A/g. At a given order in the exponential,
the resulting series in g is typically factorially divergent. However, one can consider the opposite
regime: at each order in g, one has a series in e−A/g, which we will simply call partial series.
In the theory of non-linear ODEs, it can be proved [4] that all the partial series are convergent,
and with the same radius of convergence. We will call this property the convergence property of
partial series. This property also holds in the trans-series appearing naturally in the exact WKB
method in quantum mechanics, like e.g. in the Delabaere–Pham formula [14, 15] and in the exact
quantization conditions of [7, 8]. In this paper we show that the convergence of the partial series
also holds in some interesting examples in QFT. In particular, we give evidence that it holds for
an observable much studied recently from the point of view of resurgence, namely the free energy
of integrable, asymptotically free 2d QFTs [16–30]. It is expected that the convergence property
of the partial series leads to the convergence of the full resummed trans-series, as it happens in the
case of ODEs [4]. The advantage of the convergence property is that it can be addressed directly
in the formal trans-series, before Borel resummation. The evidence we give for the convergence
property in the case of the free energy shows that this observable behaves very differently from
correlation functions. In particular, its singularity structure must be qualitatively different from
what is found in e.g. typical two-point functions.
This paper is organized as follows. In section 2 we present the basic structure of trans-
series in quantum field theory, and we define the partial series collecting the different series of
exponentially small corrections. In section 3 we look at a simple example where the convergence
of partial series can be tested in detail, namely the two-point function of the large N sigma
model. In 4 we consider a similar simple example in complex Chern–Simons theory. The core of
the paper is contained in section 5, where we test the convergence of partial series in the case
of the free energy of integrable models. Finally, we conclude with a summary of the results and
prospects for future developments.
