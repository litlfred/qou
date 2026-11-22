---
doc_id: ft-dpm-quaternion-kernel-ieee-tit-2014
doc_title: "Quaternion Reproducing Kernel Hilbert Spaces: Existence and Uniqueness Conditions"
section_id: sec-001-s-ince
section_title: "INCE"
section_number: S
pages: 1-2
source_pdf: FT_DPM_Quaternion_Kernel_IEEE_TIT_2014.pdf
source_sha256: aa2f1eb73610a81b
toc_source: inferred
doc_brief: "Quaternion Reproducing Kernel Hilbert Spaces: Existence and Uniqueness Conditions — The existence and uniqueness conditions of quater- nion reproducing kernel Hilbert spaces (QRKHS) are established"
---
INCE
their
introduction
in
the
early
1980s
[1],
support vector machines (SVM) have become a de facto
standard for classiﬁcation and regression with application in
areas including semantic analysis [2], gene selection [3], and
ﬁnancial prediction [4]. An extension of the original SVM
algorithm to nonlinear classiﬁcation [5] employs the so-called
kernel trick [6], which enables operation in higher dimensional
spaces through the evaluation of a kernel function. The kernel
trick has also made it possible to efﬁciently implement support
vector regression (SVR) algorithms [7], whereby the output of
a system is modelled as an inner product between a nonlinear
transformation of the input and an optimal (ﬁxed) weighting
structure, in the so-called feature space [8], [9].
The theoretical justiﬁcation for the use of the kernel trick
is the reproducing property of the feature space. This is
guaranteed by the Riesz representation theorem [10, Th. 6.2.4],
Manuscript received April 22, 2013; revised February 4, 2014; accepted
June 14, 2014. Date of publication June 30, 2014; date of current version
August 14, 2014.
The authors are with the Department of Electrical and Electronic Engi-
neering, Imperial College London, London SW7 2AZ, U.K. (e-mail:
f.tobar@imperial.ac.uk; d.mandic@imperial.ac.uk).
Communicated by G. Moustakides, Associate Editor for Detection and
Estimation.
Color versions of one or more of the ﬁgures in this paper are available
online at http://ieeexplore.ieee.org.
Digital Object Identiﬁer 10.1109/TIT.2014.2333734
which replaces the inner product of feature samples with ker-
nel evaluations. Moreover, the Moore-Aronszajn theorem [11]
ensures the existence and uniqueness of RKHS for posi-
tive deﬁnite (real or complex) kernels, thus replacing the
cumbersome design of feature maps by a simple choice of
kernels and combination parameters (weights). Dictated by
the cost function, this class of algorithms includes kernel ridge
regression (KRR) [12], kernel least mean square (KLMS) [13],
kernel afﬁne projection algorithm (KAPA) [14] and kernel
recursive least squares (KRLS) [15].
Opportunities provided by the existing complex-valued
RKHS framework [11] are manifold, however, for practical
reasons related to the ease of tuning and the associated
physical meaning, only real-valued Gaussian and polynomial
kernels are typically considered. Kernel algorithms operating
in complex-valued feature spaces are mostly of a complex
kernel least mean square type [16]–[18]. Furthermore, higher-
dimensional extensions of RKHS (in real vector-valued feature
spaces [19], [20]) have also been developed and form the basis
for both the multikernel least squares and multikernel least
mean square [21], [22].
Recent developments in sensor technology have enabled
routine recordings of 3D and 4D data (inertial body sensors,
3D wind modelling), this has been followed by the advances
in linear estimation in the quaternion domain [23]–[28]. These
have highlighted the usefulness of quaternion-valued algo-
rithms to represent quadrivariate data. Quaternions [29] have
already shown advantages over real-valued vectors within sig-
nal processing, computer graphics, and robotics communities,
owing to their enhanced modelling of rotation, orientation,
and cross-information between multichannel data. In addition,
differential operators that enable gradient-based optimisation
in the quaternion ring H have just been developed based on
the HR calculus [30]. However, quaternion kernel estimation is
still an emerging ﬁeld [31], [32] and its development requires
rigorous existence and uniqueness conditions for quaternion
reproducing kernel Hilbert spaces, as these are pre-requisites
to provide a theoretical basis for kernel algorithms operating
in quaternion-valued feature spaces.
The aim of this work is to introduce the background theory
and provide a proof-of-concept for quaternion-valued kernel
estimation by establishing: (i) the existence and uniqueness
properties of reproducing kernel Hilbert spaces of quaternion-
valued functions, (ii) the notion of positive deﬁniteness and
reproducing property of quaternion RKHS, and (iii) the the-
oretical and practical differences between real, vector and
quaternion RKHS. To this end, we ﬁrst revisit the quaternion
0018-9448 © 2014 IEEE. Translations and content mining are permitted for academic research only. Personal use is also permitted,
but republication/redistribution requires IEEE permission. See http://www.ieee.org/publications_standards/publications/rights/index.html for more information.
ring and quaternion left Hilbert spaces in order to deﬁne the
quaternion RKHS (QRKHS). Quaternion versions of the Riesz
representation [10] and Moore-Aronszajn [11] theorems are
next presented (and compared to their real-valued counter-
parts) to introduce a unique relationship between QRKHSs and
positive deﬁnite kernels. This equips us with a theoretical basis
for quaternion kernel estimation, whereby the feature space has
a corresponding quaternion-valued reproducing kernel.
We also show that the so-introduced QRKHS serves as a
feature space of kernel regression algorithms within the kernel
ridge regression setting. Applications in 3D body sensor track-
ing and nonlinear channel equalisation support the approach.
