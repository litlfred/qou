---
doc_id: arxiv-1611.09182v1
doc_title: "Standard model physics from an algebra?"
section_id: sec-047-811-introduction
section_title: "Introduction"
section_number: 8.1.1
pages: 67-70
source_pdf: 1611.09182v1.pdf
source_sha256: 6b40549b96d40ac7
doc_brief: "Standard model physics from an algebra? — 57 sections: Abstract; Acknowledgements; Introduction"
---
The SU (5) grand uniﬁed theory oﬀers a classic example of what it means to be a grand
uniﬁed theory. It was proposed in 1974 by H. Georgi and S. Glashow, [38], and can be seen
to successfully unify the gauge groups of the standard model. However, the SU (5) model
only partially uniﬁes a generation of quarks and leptons.
The group SU (5) has rank 4, as with the standard model’s gauge group, GSM ; that
is, its Lie algebra has a 4-dimensional Cartan subalgebra, [48]. The Lie algebra of SU (5)
59
essentially doubles the gauge symmetry of the standard model by subsuming the standard
model’s 12 symmetry generators, and then incorporating another 12, for a total of 24.
Irreducible representations for SU (5) are listed as
1, 5, 10, 15, 24, 35, 40, 45, 50,...
Most descriptions of the SU (5) model give a generation of quarks and leptons, which
stretches across the 5 ∗ and the 10 , and optionally, the singlet, 1 . This singlet can be
included so as to represent the right-handed neutrino. In contrast, gauge bosons lie in the
24, while the Higgs ﬁelds typically are represented by the 5 and the 24.
Despite its anticipated candidacy as a suitable ﬁt to nature, the SU (5) grand uniﬁed
theory has run into trouble with experiment. For example, the theory predicts proton
decay, with a lifetime of 1031±2 years, depending on the details and source of the calculation,
[53], [48]. This is generally seen to be at odds with the ﬁndings of the Super-kamiokande
experiment, [20], [21], which gives a proton lifetime of ≥ 5.9× 1033 years at the 90%
conﬁdence level.
8.1.2 GSM inside SU (5)
Here, we detail the embedding of the standard model’s gauge group into SU (5), as given
in [7].
Elements of SU (5) can be written down as 5 × 5 complex matrices, wherein we may
embed the standard model’s gauge group, [7], [48]. Starting with SU (2) and SU (3), we
have
(h2 0
0 h3
)
∈ SU (5), (8.1)
where h2 is a 2 × 2 matrix representing elements of SU (2), and h3 is a 3 × 3 matrix,
representing elements of SU (3). Written in this way, the SU (2) and SU (3) subgroups
clearly commute with each other. We might then ask, what groups remain in SU (5),
which commute with both of these SU (2) and SU (3) subgroups?
It is straightforward to see, [7], [64], that any 5 × 5 matrix commuting with
(h2 0
0 h3
)
60
must be of the form
H1 =
(c2 I2×2 0
0 c3 I3×3
)
, (8.2)
forc2,c 3∈ C. Furthermore, for H1 to be an element of SU (5), it must have a determinant
of one, so that
H1 =
((h1)3 I2×2 0
0 ( h1)−2 I3×3
)
, (8.3)
where h1∈ C.
Putting these all together, we see that it is possible to map any element of SU (3)×
SU (2)×U(1) into SU (5),
((h1)3h2 0
0 ( h1)−2h3
)
∈ SU (5), (8.4)
where h1∈U(1), h2∈SU (2), and h3∈SU (3).
Now, it turns out that after considering the action of the SU (2) and SU (3) subgroups
on the 5∗ and the 10, we see that thisU(1) of equation (8.3) is none other thanU(1)Y , weak
hypercharge. That is, SU (5) theory is able to elegantly explain the strikingly inelegant
arrangement of hypercharges asserted by the standard model.
A question now arises, as to whether or not every element of SU (3)×SU (2)×U(1) is
mapped to a unique element of SU (5)’s subgroup. That is, we might ask, is this mapping
invertible? It turns out that the answer is no, [7], as it is possible to ﬁnd distinct elements
of SU (3)×SU (2)×U(1), given by
(
h3 =z2
n I3×3, h2 =z−3
n I2×2, h1 =zn
)
∈ SU (3)×SU (2)×U(1), (8.5)
which each map to the same identity element of our SU (5) subgroup,
(z3
nz−3
n I2×2 0
0 z−2
n z2
n I3×3
)
= I5×5 ∈ SU (5). (8.6)
61
The above elements, zn, are restricted to be sixth roots of unity, zn = e2πin/6, since
z−3
n I2×2∈SU (2) andz2
n I3×3∈SU (3) must each have a determinant of one. This generates
the ﬁnite group Z6.
So it turns out that our subgroup of SU (5) is not SU (3)×SU (2)×U(1), but rather,
SU (3)×SU (2)×U(1)/Z6. This could be problematic for SU (5) theory, if the standard
model representations were indeed able to distinguish between these six values of zn.
However, by checking explicitly one can show that the standard model representations
are insensitive to these distinct values of zn. Furthermore, Z6 is said, [7], to constitute the
entire kernel of this representation. This leaves us with the conclusion that the standard
model’s gauge group is not SU (3)×SU (2)×U(1), but rather, SU (3)×SU (2)×U(1)/Z6.
