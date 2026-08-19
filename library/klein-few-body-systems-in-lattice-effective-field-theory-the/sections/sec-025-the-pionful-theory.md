---
doc_id: klein-few-body-systems-in-lattice-effective-field-theory-the
doc_title: "Bonn, November 2018"
section_id: sec-025-the-pionful-theory
section_title: "The pionful theory"
section_number: null
pages: 51-53
source_pdf: klein-few-body-systems-in-lattice-effective-field-theory-thesis.pdf
source_sha256: 7ecafdd08255d5c6
doc_brief: "Few-Body Systems in Lattice Effective Field Theory Dissertation Erlangung des Doktorgrades (Dr. rer. nat.) Mathematisch-Naturwissenschaftlichen Fakultät Rheinischen Friedrich-Wilhelms-Universität Bonn"
---
N = 0 case reﬂecting the improved dispersion relation approximation which is necessary as we receive
data points in diﬀerent regimes for diﬀerent lattice spacings. Therefore, we use N = 3.5 for the following
calculations.
Comparing the theoretical predictions with the experimental values gives the impression of a large
deviation particularly for r 3S 1
. As we only work at lowest order, we cannot expect to get the physical
value already. But we can perform a consistency check for our predictions as there exists a relation
between the binding energy, the scattering length and the eﬀective range, see e.g. Ref. [23]
EB≈− 1
2µa2
s
1 + re
as
+ 5r2
e
4a2
s
+...
 . (4.20)
This equation is valid for positive scattering length as and the expansion in re/as, with re the eﬀective
range, is useful provided|re|≪ as. As we do not include any partial wave mixing, we can use the expansion
up toO(r2
e/a2
s) and compare the physical binding energy in this scheme with our lattice predictions.
Then the binding energy is EB =−2.052(1) MeV for the physical values of the scattering length and the
eﬀective range and our lattice predictions give a binding energy of EB =−2.009(1)... − 1.999(1) MeV
showing that the relation in Eq. (4.20) is approximately fulﬁlled.
The constant value of b can be explained by the smearing function itself and the Fourier transformation
of the contact interaction given in Eq. (4.13) in dependence of the cutoﬀ/ lattice spacing. While we work
on the lattice, the Fourier transformation is limited by the maximum momentumπ/a. As we consider
the continuum limit, new contributions to the summation are added in Eq. (4.13) asπ/a→∞ and the
value of the normalization constant changes. The normalization constant f0 approaches a ﬁnite limit
and the new contributions are exponentially suppressed. Hence, the lattice spacing dependence of the
smearing constant should approach a constant value as long as other discretization errors are negligible.
This is also a good check for other regularizations procedures. We will use this condition to ﬁnd the best
regularization scheme in the upcoming section. It is quite remarkable that the pionless theory can be
regularized by such a constant Gaussian smearing leading to a-independent results for 0.5 ≲ a ≲ 2.0 fm.
Given that the typical extension of a nucleon is given by a scale of r≃ 0.85 fm, this means that the EFT
can be used for all momenta that do not lead to a resolution of the internal nucleon structure, at least in
the pionless theory. A direct comparison with the results of a continuum calculation is diﬃcult because
the occuring divergences are usually treated in a diﬀerent way. As done in Ref. [112], one can calculate
the scattering matrix using the bubble chain summation with a regularization ˜f (⃗p) = exp(−b⃗p2/2) similar
to the smeared contact interaction on the lattice instead of dimensional regularization or a ﬁnite cut-oﬀ.
Then the T-matrix is expanded up to and includingO(⃗p2) and matched to the eﬀective range expansion
parameters. The values one obtains are of the same order as the lattice values but do not match them
exactly. Note further that the extension to the three-particle system is not straightforward because of
the Eﬁmov eﬀect that requires the inclusion of a three-body contact interaction already at leading order
[113].
4.4 The pionful theory
Including pions is necessary for an eﬀective ﬁeld theory at higher energies. Therefore pions are included
according to Eq. (4.3) and the full Hamiltonian is
H = Hfree + Hcont + HOPE. (4.21)
45
Chapter 4 Regularization Methods for Nuclear Lattice E ﬀective Field Theory
A problem is caused by the singularities which arise in the short-range region of the OPE contribution.
On the one hand, this singularity exists for any lattice spacing as the relative distance⃗r = 0 is possible
and gives a very large but still ﬁnite contribution. On the other hand, minimizing the lattice spacing
leads to additional lattice points with non-zero but very small distances to the origin and which give an
additional large short-range contribution.
Firstly, we switch oﬀ the smearing of the contact interaction and include the pion-nucleon interaction
according to Eq. (4.3). In this case, the predictions for the eﬀective range parameter are not close to the
physical value and it is still necessary to include the smearing of the contact interaction [32].
In the case of smeared contact interaction and non-smeared pion-nucleon interaction the LECs do not
give a reasonably close value for the eﬀective range in the 3S 1-channel. The prediction is reasonable
and constant for a lattice spacing larger than 1 fm, but it does decrease towards zero for smaller lattice
spacings. As we do not include a regularization, the divergentπN-contribution for small lattice spacings
is more and more resolved for smaller lattice spacings resulting in a very sharp potential. The contact
interaction in combination with the smearing factor b can compensate this eﬀect but as the 1S 0- and
3S 1-channel do not have exactly the same dependence, while it is still possible to ﬁt to one of the eﬀective
ranges, the agreement for the other one gets worse.
Now we turn on the smearing of the pion-nucleon interaction. While a smearing in momentum space
according to Eq. (4.11) could be possible, we follow the arguments given in Ref. [22] and introduce the
regularization in position space as proposed in Eq. (4.14). Then, the new OPE potential reads
HOPE =− g2
A
8F2
π
∑
S 1,S 2,I
∑
⃗n1,⃗n2
˜f (⃗n1− ⃗n2
) GS 1S 2
(⃗n1−⃗n2
)ρa†,a
S 1,I
(⃗n1
)ρa†,a
S 2,I
(⃗n2
) . (4.22)
Throughout this chapter, we use n = 4 in Eq. (4.14), but we also checked for diﬀerent n and the results are
similar. Higher values of n are only necessary for strongly divergent contributions like two-pion-exchange
potentials which we neglect in this exploratory study.
In Fig. 4.2, the ﬁnite volume binding energy of the deuteron and the respective eﬀective range expansion
for the S-waves for a subset of the lattice spacings used are shown. Finite volume e ﬀects modify the
binding energy so that a correction according to Eq. (4.15) is necessary but higher order terms are still
negligible. Also the data points we obtain for the e ﬀective range expansion still have small enough
momenta squared so that the expansion up toO(p2) is feasible. The resulting LECs, the smearing constant
as well as the predictions for L = 34, 36, 38 are displayed in Tab. 4.3. While the value of the LECs are
diﬀerent to the pionless case, their general shape depending on the lattice spacing does not change and
the LECs remain negative as well. Also the smearing factor b remains in a certain range between 2.40
to 2.92×10−5 MeV−2, indicating that this regularization scheme works quite well. We do not show the
results for the smaller set of lattice sizes, but we have shown that ﬁnite volume eﬀects between these two
sets become negligible for lattice spacings larger than 0.7 fm. Assuming a large enough lattice there is a
rise in the smearing constant between 1.8 fm and 0.7 fm, and it is constant again for lattice spaces smaller
than 0.7 fm. While in the range from 0.7 fm and 1.8 fm the pion-nucleon contribution changes, the lattice
sites closest to the origin contribute more and more to the potential due to the divergent structure of the
potential. This eﬀect is compensated by the regularization at a certain range as we further decrease the
lattice spacing, and then the regularized potential does not change its shape anymore. Note that in the
intermediate range there are lattice artifacts in the OPEP which cause the oscillatory behavior of the
LECs as they appear at diﬀerent physical lengths and multiplied by a diﬀerent regularization factor. As
a result, we cannot see a plateau for the LECs C3S 1
and C1S 0
at a lattice spacing of a = 0.5 fm, but we
have to further decrease the lattice spacing. Simultaneously, we increase the number of lattice points to
46
