---
doc_id: arxiv-1412.4711v1
doc_title: "CHARACTER VARIETIES FOR SL (3, C): THE FIGURE EIGHT KNOT"
section_id: sec-000-introduction
section_title: "Introduction"
section_number: null
pages: 1-3
source_pdf: 1412.4711v1.pdf
source_sha256: 4fb1d6ee062cca8c
doc_brief: "CHARACTER VARIETIES FOR SL (3, C): THE FIGURE EIGHT KNOT — We give a description of several representation varieties of the fundamental group of the complement of the ﬁgure eight knot in PGL(3, C) or"
---
Representation varieties of ﬁnitely presented groups into Lie groups has
been studied since a long time. A recent by Sikora paper with many ref-
erences is [21]. In this paper we concentrate on the representations of
3-manifold groups in PGL(3 , C) or SL(3 , C). The case of surface groups
have been studied more extensively and their representation varieties into
SL(3, C) are treated by Lawton in [15]. On the other hand, only recently
the study of representations of 3-manifold groups into SL(3, C) or PGL(3, C)
has been started. See for instance the work of Porti and Menal-Ferer [17], of
Garoufalidis, Goerner, Thurston and Zickert [13, 12] and of Bergeron with
the two ﬁrst named authors [1] among others. One has to keep in mind
the deep study which was started in the last decades of the last century on
representations into SL(2, C) by several authors among them Thurston [22].
It gives a paradigm for the present study in the case of PGL(3 , C).
Let Γ 8 be the fundamental group of the ﬁgure eight knot complement.
We present here a thorough study of the space of representations of Γ 8 into
PGL(3, C) and SL(3, C). It turns out that all the irreducible representations
we ﬁnd in PGL(3 , C) can be lifted to SL(3 , C). Therefore, most of the
computations will be made in PGL(3, C) but we will occasionally work with
SL(3, C).
We begin with a review of diﬀerent versions of this space (representation
variety, character variety, decorated representations among others) and the
coordinates we use to study these varieties in a rather general setting. A
diagram, displayed in Figure 2, shows the several representation spaces and
their relations. The main coordinate system we use is derived from projec-
tive ﬂag decorations of ideal triangulations of a 3-manifold as introduced
in [1] (see also [12]). Another view of these spaces is given in [23] using
Ptolemy coordinates, which are coordinates for aﬃne ﬂags decorations of
1
arXiv:1412.4711v1  [math.GT]  15 Dec 2014
2 E. FALBEL, A. GUILLOUX, P.-V. KOSELEFF, F. ROUILLIER AND M. THISTLETHWAITE
ideal triangulations. Those work are accessible through the website CURVE
[9].
Then we proceed in section 3 to an explicit description of these diﬀerent
spaces for the group Γ 8 and the diﬀerent maps relating these spaces. We
use coordinates on a Zariski open set of our spaces which are associated to a
given triangulation. In particular, we describe a Zariski open set (called the
deformation variety) of the set of decorated representations into PGL(3 , C)
given by coordinates we introduced in [1]. The main theorem is Theorem 2:
Given the standard triangulation of the ﬁgure eight knot complement, there
exits precisely three irreducible components of the deformation variety. Each
component is smooth of dimension two. Whereas this result is stated and
proved only for the deformation variety, we strongly believe this is also the
case for the whole character variety. A precise statement and proof should
appear elsewhere. This section begins with a reminder about Groebner basis
and saturation, then a presentation of the actual equations for the ﬁgure
eight knot complement in§3.2. We then proceed with a general presentation
of our method to achieve computations. Eventually, we give precisions of
the speciﬁc case of the ﬁgure eight knot complement. The three components
are ﬁnally described in subsection 3.4. It turns out that each representation
can be lifted to an SL(3 , C) representation. Once these components are
identiﬁed, we may check the properties stated in the theorem (irreducibility,
smoothness...).
The next section 4 is devoted to some more precise understanding of these
components: description the A-variety associated to this knot (it is a natural
analog of the A-polynomial), identiﬁcation of the boundary unipotent rep-
resentation and identiﬁcation of the space of representations in PGL(2 , C).
Finally, in section 5, we describe a deformation method to obtain a
parametrization of some generators of Γ 8 on each irreducible components.
This method allows one to obtain a particular irreducible component of the
representation variety containing a given representation. It is based on a
Newton method and LLL algorithm and was successfully used in other con-
texts [5, 4]. We applied it to the boundary unipotent representations of the
fundamental group of the ﬁgure eight knot complement. A great interest of
this method is that its output is indeed a parametrization of matrices. It
opens the path to a geometric study of those representations, see e.g. [7].
However it does not belong to its scope to determine all the irreducible com-
ponents. We insist on the fact that it is the conjunction of both methods
that gives a satisfactory result: a parametrization of each component.
We thank Nicolas Bergeron, Martin Deraux, Matthias Goerner, Julien
March´ e, Pierre Will, Maxime Wolﬀ and Christian Zickert for many discus-
sions and exchanges during this project. The authors are grateful to the
ANR ’Structures G´ eom´ etriques Triangul´ ees’ which has ﬁnanced this project
during the last two years.
3
