---
doc_id: arxiv-1108.3035v2
doc_title: "Random Matrix Theory for the Hermitian Wilson Dirac Operator and the chGUE – GUE Transition"
section_id: sec-001-2-the-random-matrix-model
section_title: "The Random Matrix Model"
section_number: 2
pages: 3-5
source_pdf: 1108.3035v2.pdf
source_sha256: 935bf1bd3e13821b
toc_source: outline
doc_brief: "Random Matrix Theory for the Hermitian Wilson Dirac Operator and the chGUE – GUE Transition — We introduce a random two-matrix model interpolating between a chiral Hermitian (2n + ν) × (2n+ν) matrix"
---
The Random Matrix Model
In this section we ﬁrst introduce our matrix model and explain why it describes the transition between
the diﬀerent symmetry classes of random matrices from the chGUE to the GUE. Then we point out
the relation to the related Wilson chiral RMT previously introduced in [20] as well as to WchPT in
the epsilon regime.
We want to compute the eigenvalue density correlation functions of the following Hermitian Wilson
Dirac operator:
/D5 =
 m11n
W
W †
−m11n+ν

+ H .
(2.1)
Here W is a rectangular matrix of size n × (n + ν) with complex elements, without further symmetry
restrictions. The non-negative parameter ν ≥0 is related to the number of zero-eigenvalues in the
limit to the chGUE. The real parameter m denotes the quark mass, as will become clearer below.
This ﬁrst part of /D5 is what we are used to in the chGUE (up to the sign in m). The second part
H = H† is a quadratic Hermitian matrix of size N ≡2n + ν with complex elements. It corresponds
to the GUE part of /D5, breaking chiral symmetry.
The matrices W and H are distributed with the following Gaussian probability measures:
P1(W)
=
exp

−
1
2(1 −a2)TrWW †

,
P2(H)
=
exp

−
1
4a2 TrH2

,
a ∈[0, 1] .
(2.2)
We expect that the simplest, Gaussian choice that we have made here is not important in the large-n
limit due to universality. We can now deﬁne the following Nf ﬂavour partition function
Z(Nf )
ν
(m; {zf}; a) ∼
Z
dHdW
Nf
Y
f=1
det[ /D5 + zf11N]P1(W)P2(H) ,
(2.3)
where we have inserted a product of Nf characteristic polynomials of real arguments zf, in addition
to the weight functions. The integration is over all independent matrix elements of W and H.
The role of the real parameter 0 ≤a ≤1 is to interpolate between two diﬀerent symmetry classes.
For Nf = 0 and m = 0 the limit a →0 leads to a delta function in all matrix elements of H, reducing
eq. (2.3) to the chGUE. In the opposite limit a →1 we obtain a delta function in all matrix elements
of W, and we are lead to the GUE of size N. For m̸ = 0 we interpolate between the eigenvalues
of the Dirac operator with ﬁnite quark mass m and the GUE coupled to a ﬁxed external ﬁeld with
eigenvalues ±m, as it was considered for example in [33].
In [20] a very similar Wilson chiral RMT was introduced which we will label by II. Starting from
a non-Hermitian Wilson Dirac operator DW ,
DW =

aA
W
−W †
aB

,
(2.4)
with W as above and A = A† n × n and B = B† (n + ν) × (n + ν) Hermitian matrices, respectively,
the Hermitian Wilson Dirac operator D5 in [20] was obtained by multiplying DW + m with γ5:
D5 =

11n
0
0
−11n+ν

(DW + m11N) =
 m11n
W
W †
−m11n+ν

+
 aA
0
0
−aB

,
(2.5)
which is Hermitian. The corresponding partition function with Gaussian weights reads
Z(Nf )
II,ν (m; {zf}, a) ∼
Z
dHdW
Nf
Y
f=1
det[D5 + zf11N] exp

−1
4Tr(A2 + B2 + 2WW †)

.
(2.6)
Because of symmetry the minus sign in the lower right corner in B in eq. (2.5) can be absorbed by
shifting B →−B in the integrand.
Both matrix models Z(Nf )
ν
and Z(Nf )
II,ν
enjoy the same relationship to WchPT in the epsilon regime
in the following large-N limit, stated here for equal arguments zf = z (see appendix A for the non-
degenerate case):
lim
N→∞Z(Nf )
ν
(m; z; a) = lim
N→∞Z(Nf )
II,ν (m; z; a) = Z(Nf )
ν
( ˆm, ˆz, ˆa) ,
(2.7)
where
Z(Nf )
ν
( ˆm, ˆz, ˆa) =
Z
U(Nf )
dU det[U]νe
1
2 mpΣV Tr(U+U†)+ 1
2zpΣV Tr(U−U†)−ap2V W8Tr(U2+U† 2) .
(2.8)
Here we have to match the large-N with the large-V inﬁnite volume limit1
ˆm ≡mpΣV = m
√
N ,
ˆz ≡zpΣV = z
√
N ,
and ˆa2 ≡a2
pV W8 = 1
4a2N .
(2.9)
While the equivalence eq. (2.7) for the second RMT eq. (2.6) was shown in [20] we will show this
equivalence for our model eq. (2.3) in appendix A.
Eq. (2.8), the partition function of WchPT after Fourier transform, usually contains two further
low-energy constants W6 and W7, apart from the inﬁnite volume chiral condensate Σ, and W8 which
encodes the eﬀects from a ﬁnite-lattice spacing to order O(a2), which we displayed. Because W6 and
W7 can be switched on at the expense of one additional Gaussian integral each [21], we will only
consider W6 = W7 = 0 in the following. The parameter mp denotes the standard (equal) quark-mass
term coupling to ¯ψψ in ﬁeld theory, whereas the zp denotes an additional source terms coupling to
¯ψγ5ψ which will be convenient later.
Because of the matching eq. (2.7) we will assume that both RMT eqs. (2.3) and (2.6) as well as
WchPT eq. (2.8) are in the same universality class, also regarding all eigenvalue density correlation
functions.
The matching between the two matrix models can be made more explicit on the level of matrix
elements. By redeﬁning H/a →H and W/
√
1 −a2 →W in eq. (2.1) we obtain to leading order
/D5 =
 m11n
W
W †
−m11n+ν

+

aA
aΩ+ 1
2a2W
aΩ† −1
2a2W †
aB

+ O(a4) ,
(2.10)
where
H =
 A
Ω
Ω†
B

.
(2.11)
The advantage of allowing for extra, oﬀ-diagonal matrix elements Ωin matrix H in our model is that
we can do a proper change of variables from {W, H} to {W, /D5}, keeping the same number of degrees
of freedom. This allows us to go to an eigenvalue basis as we will show in the next section.
Furthermore, the choice of parametrisation in a in our model is more convenient when studying
the symmetry transition from the chGUE at a = 0 to the GUE at a = 1. Compared to that in D5 eq.
(2.5) the transition starting at a = 0 corresponds to the chGUE too, then leading via a = O(1) of a
full N × N GUE to a decoupling for a ≫1 into two GUEs of sizes n and n + ν respectively.
