---
doc_id: arxiv-math-0405258v2
doc_title: "SECOND ORDER FREENESS AND FLUCTUATIONS OF RANDOM MATRICES: II. UNITARY RANDOM MATRICES"
section_id: sec-000-1-introduction
section_title: "Introduction"
section_number: 1
pages: 1-3
source_pdf: 0405258v2.pdf
source_sha256: dbd6bf5a94deebaf
doc_brief: "SECOND ORDER FREENESS AND FLUCTUATIONS OF RANDOM MATRICES: II. UNITARY RANDOM MATRICES — We extend the relation between random matrices and free probability theory from the level of expectations to"
---
In Part I of this series [MSp] we introduced the concept of second
order freeness as the mathematical concept for dealing with the la rge N
limit of ﬂuctuations of N × N-random matrices. Whereas Voiculescu’s
freeness (of ﬁrst order) provides the crucial notion behind the le ading
order of expectations of traces, our second order freeness is in tended
to describe in a similar way the structure of leading orders of global
ﬂuctuations, i.e., of variances of traces. In Part I we showed how ﬂ uc-
tuations of Gaussian and Wishart random matrices can be understo od
from this perspective. Here we give the corresponding treatment for
ﬂuctuations of unitary random matrices. Global ﬂuctuations of un itary
∗ Research supported by Discovery Grants and a Leadership Suppo rt Initiative
Award from the Natural Sciences and Engineering Research Counc il of Canada.
‡ Research supported by State Committee for Scientiﬁc Research ( KBN) grant
2 P03A 007 23, RTN network: QP-Applications contract No. HPRN-C T-2002-
00279, and KBN-DAAD project 36/2003/2004. The author is a hold er of a schol-
arship from the European Post-Doctoral Institute for Mathema tical Sciences.
† Research supported by a Premier’s Research Excellence Award fro m the
Province of Ontario.
1
2 J. A. MINGO, P. ´SNIADY, AND R. SPEICHER
random matrices have received much attention in the last decade, s ee,
e.g, the survey article of Diaconis [D].
Our main concern will be to understand the relation between unitary
random matrices and some other ensemble of random matrices which is
independent from the unitary ensemble. This includes in particular th e
case that the second ensemble consists of constant (i.e., non-ran dom)
matrices. A basic result of Voiculescu tells us that on the level of
expectations, independence between the ensembles goes over int o as-
ymptotic freeness. We will show that this result remains true on the
level of ﬂuctuations: independence between the ensembles implies that
we have asymptotic second order freeness between their ﬂuct uations.
Two important consequences of our investigations are the following .
¶ We get a generalization to the case of several independent unitary
random matrices of a classical result of Diaconis and Shahshahani
[DS]. Their one-dimensional case states that, for a unitary random
matrix U, the family of traces Tr( U n) converge towards a Gaussian
family where the covariance between Tr( U m) and Tr( U ∗n) is given by
n · δmn. In the case of several independent unitary random matrices,
one has to consider traces in reduced words of these random matr ices,
and again these converge to a Gaussian family, where the covarianc e
between two such reduced words is now given by the number of cyclic
rotations which match one word with the other. This result was also
independently derived by R˘ adulescu [R] in the course of his investig a-
tions around Connes’s embedding problem.
¶ We can show that we do not have universality of ﬂuctuations in
multi-matrix models. For unitarily invariant one-matrix models it
was shown by Johansson [J] (compare also [AJM]) that many random
matrix ensembles have the same ﬂuctuations as the ensemble of Gau ss-
ian random matrices. A main motivation for our investigations was
the expectation that many unitarily invariant models of multi-matrix
random ensembles should have the same ﬂuctuations as the ensemb le
of independent Gaussian random matrices. However, our theory o f
second order freeness shows that this is not the case.
The paper is organized as follows. In Section 2, we recall all the nec-
essary deﬁnitions and results around permutations, unitary rand om
matrices, and second order freeness. We will recall all the relevan t no-
tions from Part I, so that our presentation will be self-contained. How-
ever, for getting more background information on the concept of second
order freeness one should consult [MSp]. In Section 3, we derive our
FLUCTUATIONS OF UNITARY RANDOM MATRICES 3
main result about the asymptotic second order freeness between uni-
tary random matrices and another independent random matrix ens em-
ble. This yields as corollary that independent unitary random matrice s
are asymptotically free of second order, implying the above mention ed
generalization of the result of Diaconis and Shahshahani [DS]. Sec-
tion 4 shows how our results imply the failure of universality of global
ﬂuctuations in multi-matrix models.
