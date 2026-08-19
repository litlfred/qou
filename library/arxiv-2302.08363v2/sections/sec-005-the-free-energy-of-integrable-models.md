---
doc_id: arxiv-2302.08363v2
doc_title: "Prepared for submission to JHEP On the structure of trans-series in quantum field theory"
section_id: sec-005-the-free-energy-of-integrable-models
section_title: "The free energy of integrable models"
section_number: null
pages: 11-14
source_pdf: 2302.08363v2.pdf
source_sha256: c2244e03b17048fb
doc_brief: "On the structure of trans-series in quantum field theory — Many observables in quantum field theory can be expressed in terms of trans-series, in which one adds to the perturbative series a typically"
---
Two-dimensional, integrable, asymptotically free quantum field theories are an interesting family
of toy models where one can obtain an explicit but highly non-trivial trans-series for the free
energy [16–30], and therefore one can hope that the convergent property of the partial series can
be tested in detail.
In integrable quantum field theories, the free energy is a quantity that can be computed after
we introduce into the Hamiltonian H a chemical potential h coupled to a conserved charge Q:
H→ H−hQ. (5.1)
For each model, there can be different convenient choices of the charge Q. The ground state of
the Hamiltonian (5.1) is a finite density state characterized by the free energy per unit volume
F (h) =− lim
V,β→∞
1
Vβ log Tr e−β(H−hQ), (5.2)
– 10 –
<latexit sha1_base64="jz0V9JJd+Wt4y1gboOCedDNi1rY=">AAAB6nicbVDLSgMxFL2pr1pfVZdugkVwVWbE10YounFZ0T6gHUomzbShSWZIMkIZ+gluXCji1i9y59+YtrPQ6oELh3Pu5d57wkRwYz3vCxWWlldW14rrpY3Nre2d8u5e08SppqxBYxHrdkgME1yxhuVWsHaiGZGhYK1wdDP1W49MGx6rBztOWCDJQPGIU2KddD+8kr1yxat6M+C/xM9JBXLUe+XPbj+mqWTKUkGM6fheYoOMaMupYJNSNzUsIXREBqzjqCKSmSCbnTrBR07p4yjWrpTFM/XnREakMWMZuk5J7NAselPxP6+T2ugyyLhKUssUnS+KUoFtjKd/4z7XjFoxdoRQzd2tmA6JJtS6dEouBH/x5b+keVL1z6tnd6eV2nUeRxEO4BCOwYcLqMEt1KEBFAbwBC/wigR6Rm/ofd5aQPnMPvwC+vgGHdaNtA==</latexit>
h = m
Figure 3 . The free energy F(h) has a branch cut singularity at h =m.
whereV is the total volume of space andβ is the total length of Euclidean time. For convenience,
we will write our equations in terms of
F(h) =F (h)−F (0). (5.3)
As found by Polyakov and Wiegmann [46, 47],F(h) can be computed by the Bethe ansatz. This
amounts to the following integral equation for a Fermi density ϵ(θ):
ϵ(θ)−
Z B
−B
K(θ−θ′)ϵ(θ′)dθ′ =h−m cosh(θ), θ ∈ [−B,B ]. (5.4)
In this equation, m is the mass of the particles charged under Q. The kernel of the integral
equation K(θ) is given by
K(θ) = 1
2πi
d
dθ logS(θ), (5.5)
whereS(θ) is theS-matrix appropriate for the scattering of the charged particles. The endpoints
±B of the Fermi density are fixed by the boundary condition
ϵ(±B) = 0. (5.6)
As we will see later, the boundary condition determines the parameter B in terms of h/m. Once
we find the solution ϵ(θ) to (5.4), the free energy is given by
F(h) =−m
2π
Z B
−B
ϵ(θ) cosh(θ)dθ. (5.7)
Note that we calculate F(h) for h > m, such that the ground state has particles in it. At the
threshold value h = m, the one particle state has the same energy as the vacuum and we have
F(m) = 0. In fact,F(h) has a branch cut singularity ash→m+, as it can be verified by explicit
calculations, see Fig. 3. For example, for the O(3) non-linear sigma model, one has [48]
F(h)∼ (h−m)3/2, h →m+. (5.8)
While it might be easy to numerically extract the free energy from (5.4) and (5.7), the key
challenge is to study these equations in the weakly coupled regime h≫ m, which corresponds
– 11 –
to the limit B ≫ 1, and to extract the complete asymptotics, including exponentially small
corrections. In [18], a powerful technique to extract perturbative corrections was found, while
in [24] an analytic method to extract exponentially small corrections analytically, directly from
the Bethe ansatz, was developed. More recently, [29] put together these two developments and
obtained explicit results for the full trans-series. Since we will only consider the very first partial
series, we will follow the method in [24]. It is possible that more systematic results might be
obtained by implementing the method of [29].
The first step is to reexpress (5.4), (5.6), (5.7) in the Fourier space of the θ variable and use
the Wiener–Hopf approach [48–50]. We consider the Fourier transform of the kernel
˜K(ω) =
Z
R
eiωθK(θ)dθ (5.9)
and its Wiener–Hopf factorization
1− ˜K(ω) = 1
G+(ω)G−(ω), (5.10)
where G±(ω) is analytic in the upper (respectively, lower) complex half plane. The functions
G±(ω) will depend on the specific model, but we will only consider the case in which K(θ) is an
even function, which implies that G−(ω) =G+(−ω). It will be convenient to define
σ(ω) = G−(ω)
G+(ω). (5.11)
We further introduce
g+(ω) = ih1− e2iBω
ω + imeB
2
e2iBω
ω− i− 1
ω + i

, (5.12)
which is the Fourier transform of a function related to the expression appearing on the r.h.s. of
the integral equation (5.4) (for details, see [24]). Lastly, we define
ϵ±(ω) = e±iBω˜ϵ(ω), (5.13)
where ˜ϵ(ω) is the Fourier transform of the Fermi density ϵ(θ).
As shown in [48, 50], the integral equation (5.4) can be reformulated as the following equation
Q(ω) = 1
2πi
Z
R
G−(ω′)g+(ω′)
ω +ω′ + i0 dω′ + 1
2πi
Z
R
e2iBω′
σ(ω′)Q(ω′)
ω +ω′ + i0 dω′, (5.14)
which has to be solved for Q(ω). The solution Q(ω) determines ϵ+(ω) through the equation
ϵ+(ω)
G+(ω) = 1
2πi
Z
R
G−(ω′)g+(ω′)
ω′−ω− i0 dω′ + 1
2πi
Z
R
e2iBω′
σ(ω′)Q(ω′)
ω′−ω− i0 dω′. (5.15)
A relationship between B and h/m is determined by the boundary condition (5.6), which in
Fourier space takes the form
lim
κ→+∞
κϵ+(iκ) = 0. (5.16)
Finally, from (5.7), the free energy can be written as
F(h) =− 1
2πmeBϵ+(i). (5.17)
– 12 –
