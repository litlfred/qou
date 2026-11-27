---
doc_id: arxiv-1406.4088v2
doc_title: "Ab initio calculation of the neutron-proton mass difference"
section_id: sec-018-9-extracting-hadron-masses
section_title: "Extracting hadron masses"
section_number: 9
pages: 32-33
source_pdf: 1406.4088v2.pdf
source_sha256: d8f2ff1efb5bea30
toc_source: outline
doc_brief: "Ab initio calculation of the neutron-proton mass difference — 27 sections: Front matter; 1; Outline"
---
Extracting hadron masses
To calculate hadron propagators we ﬁx the smeared photon and gluon ﬁelds to Coulomb gauge. We use local
hadron operators, in which the quark ﬁelds are Gaussian smeared, with a smearing radius of about 0.3 fm. We
observe, as in many other studies that reducing the noise in hadron propagators can be efﬁciently done by using
many different quark sources per gauge conﬁguration. In the case of the nucleon propagator we use several
hundred different source positions. For these propagator calculations we use the 2-level multi-grid approach of
Ref. (60) and also the variance reduction technique of Ref. (61).
We fold the propagators around the midpoint of the lattice in time and ﬁt them with standard one-state func-
tions. To obtain the mass splittings our method is to jointly ﬁt the isospin partners with the mass difference, the
average mass and the two amplitudes as ﬁt parameters (10). Fitting the propagators separately and subtracting
the ﬁtted values yields results that are consistent with the joint ﬁt method and the statistical errors are of similar
size. All plateau ﬁts take into account the correlation between the timeslices and isospin partners. In order to
have a stable correlation matrix we only ﬁt ten time slices at once.
Selecting the ﬁt interval for a given hadronic channel is a highly non-trivial task. In order to get rid of the
excited states one wants to take large values for the timeslice, where the mass ﬁt starts (tmin). However, taking
values that are too large results in suboptimal signal/noise ratios. Since our goal is to reach precisions on the
sub-permil level, a reliable, robust and controlled method is needed to choose the proper ﬁt intervals.
The most popular way to select a good ﬁt range is to calculate the correlated χ2 of a mass ﬁt and use ranges
for which the χ2/dof is about one. Note that this procedure is not fully satisfactory. The values of the χ2/dof for
a given hadron channel should follow instead the χ2 distribution. Thus we want to determine the probability
that from a given tmin the χ2/dof values follow the expected distribution (or equivalently the corresponding
goodnesses of the ﬁts are uniformly distributed). Since we have 41 independent ensembles it is possible to look
at the distributions of the χ2/dof for various tmin values. Fig. S11 shows the expected cumulative probability
distributions of the ﬁt qualities (which has to be linear) and the measured distribution. Both the nucleon and Ξ
channels are depicted. As expected the larger the tmin the closer the measured distribution is to the expected
one.
The standard way to statistically interpret Fig. S11 is to carry out a Kolmogorov-Smirnov analysis (62).
Thus one determines the maximum value of the absolute difference between the expected and measured cu-
mulative probability distributions (D). This is then used to deﬁne a signiﬁcance level or probability (P) that the
measured distribution can indeed be one originating from the expected uniform distribution. We start our ﬁts
from tmin values, for which this probability is larger than 0.3. In addition, to estimate the possible contribution
of excited states, we use another ﬁt range starting from one timeslice later. (Since the excited states have even
smaller contributions for ﬁt ranges which start even later, one might use them too. However, due to the increas-
ing noise this provides no new information). Obviously, for different hadronic channels the proper tmin values
are different. They are collected in Tab. S5.
