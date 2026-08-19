---
doc_id: bujack-et-al-2022-the-non-riemannian-nature-of-perceptual-co
doc_title: "RESEARCHARTICLE PSYCHOLOGICALANDCOGNITIVESCIENCEMS The non-Riemannian nature of perceptual color space RoxanaBujacka,1 ,EmilyTeti a,b,JonahMiller a,ElektraCaﬀrey a,c,andTereceL.Tur"
section_id: sec-001-234-fig-9-results-inx
section_title: "(Fig. 9) results in¯x"
section_number: 2.34
pages: 8-10
source_pdf: bujack-et-al-2022-the-non-riemannian-nature-of-perceptual-color-space.pdf
source_sha256: 2bc66a26d3901a29
doc_brief: "RESEARCHARTICLE PSYCHOLOGICALANDCOGNITIVESCIENCEMS The non-Riemannian nature of perceptual color space RoxanaBujacka,1 ,EmilyTeti a,b,JonahMiller a,ElektraCaffrey a,c,andTereceL.Turton a — 2 sections"
---
flog =54.
Discussion
The concavity of the scaling functionf in Fig. 9 is significant,
demonstrating the hypothesized existence of diminishing returns
in color difference perception. This reveals the non-Riemannian
structure of perceptual color space, contradicting the current
scientific paradigm.
It is particularly interesting that the best fit suggests a loga-
rithmic relationship between perceived differences and absolute
differences, supporting Helm (26), because this is the known
relation between perceived strengths of stimuli and their corre-
sponding physical strengths as described by the Weber–Fechner
law (6). Our findings hint at the potential existence of a second-
orderWeber–Fechnerlawstatingthattheperceiveddifferences,or
theirderivativesasthecasemaybe,growlogarithmicallywiththe
physical differences of the stimuli as well.|| More research must
go into the validation of this conjecture, however, because the
measurement of the absolute differences allows for some degree
of freedom other than theL∗ units and because other areas of
colorspaceandotherareasofsensationmightbehavesignificantly
differently. Until more research is conducted, we will need to
mathematically describe perceptual color space as the general
concept of a path-connected metric space.
Color metrics and measures in computer graphics, visualiza-
tion, image and video processing, color mapping, and quality
controlin thepaint andtextile industriesarebasedon andmeant
forsmallcolordifferences.Diminishingreturnsprovideanexpla-
nationofwhytheycannotbeconcatenatedtofaithfullyrepresent
large differences (67). If a mathematical relation between small
and large color differences can be found to hold not just along
the neutral axis but across the whole color space, an extension of
||The existence of a second-order Weber law has previously been suggested in a slightly
diﬀerentcontextbyWhittle(62,66).
the current metrics from small to large differences would become
possible. More experiments should be performed to cover the
whole color space to achieve this overarching goal in the future.
Materials and Methods
In this section, we describe our experimental design in full detail. Participants
were asked to judge two differences using a triad arrangement of stimuli, as
shown in Fig. 4. Differences in the triad ranged from small, barely perceptible
differences to large, obvious differences. The triads were constructed from stimuli
described by CIE LAB coordinates, where a
∗, b∗ = 0a n d L∗ is variable. These
triads are determined by the differences between the reference and the two tests,
d1 := |L∗
ref − L∗
t1 |, d2 := |L∗
ref − L∗
t2 |, [20]
and the difference of differences,
Δd := d1 − d2. [21]
The differences take on values between 0 and 30 in increments of 2.5, and Δd
takes on values of ±2.5, ±5, ±10. This gives a total of 64 triads. A summary of
the experimental design is shown in Fig. 11, where each of the 64 points repre-
sents a combination of differencesd
1 and d2. For each pair of differences, ﬁve tri-
ads are constructed using ﬁve values for the referenceL∗
ref = 30, 40, 50, 60, 70.
A sample size of 250 evaluations for each triad was found to produce high
agreement between the MLE and a true underlying relationship based on Monte
Carlo simulations. The large number of stimuli and responses needed, cou-
pled with the COVID-19 pandemic restrictions, made in-person studies infeasi-
ble during the course of this research. Instead, the experiment employed the
crowdsource platform MTurk (52) and used the survey software Qualtrics (68)
to implement and present the studies. Crowdsourced studies have been shown
to be a reliable method for conducting perception studies; known results in
visualization have been replicated using this approach (69–71), and over the last
two decades, the crowdsourced approach has become increasingly popular (72–
75).
** In particular, Turton et al. (71) probed the speciﬁc concern about using
MTurk for perceptual studies in color. A review of the use of crowdsourcing for
visualization is in Borgo et al. (76).
Fig. 11. Representationofthetriadsusedforsimulationsandexperimental
study. Each point represents ﬁve distinct experimental triads, each with a
diﬀerent L
∗ value for the standard. The values for the tests are calculated
usingthe xand y values.
**J. C. Roberts, J. Jackson, IEEE Conference on Visualization, October 1–6, 2017, Phoenix,
AZ.
8of10 https://doi.org/10.1073/pnas.2119753119 pnas.org
Downloaded from https://www.pnas.org by 136.47.145.179 on May 11, 2026 from IP address 136.47.145.179.
Participants. Only MTurk users located in the United States were recruited.
Participants were instructed that they could not participate in the study if they
had a color vision deﬁciency (CVD). An initial screening question rejected any
participants who stated that they had CVD. Additionally, a Ishihara color plate
CVD test preceded the study, and those with two or more incorrect answers were
removed before analysis (77).
A total of 1,498 participants completed the study, of which 62 (4%) were
excluded on the basis of a failed CVD test. Each participant responded to between
42 and 75 triads, where no participant responded to the same triad more than
once. Participants’ ages ranged from 18 to 80 (mean = 39.5, SD = 12.3). Partic-
ipants identiﬁed as 53.3% male, 45.4% female, and under 1% nonbinary/other
or declining to answer. Of the participants, 48.1% had at least an undergraduate
degree (BS, BA, etc.), with another 20.5% having some college experience or an
associate degree and 22.1% having educational levels beyond an undergraduate
degree. Less than 10% had only a high school diploma (or equivalent) or declined
to answer. Participants were compensated at the rate of at least the federal
hourly minimum wage for the median participant time. Los Alamos National
Laboratory’s Human Subjects Research Review Board (comparable with an aca-
demic institutional review board) approved this study. All participants provided
informed consent.
Stimuli. Participants were shown triads with the reference in the middle and
one test each to the left and the right. All stimuli in the triad were gray patches
with a∗, b∗ = 0 and variable L∗ values as deﬁned in CIE LAB. TheL∗ value of the
standard was constrained to fall between the values of the two tests to ensure
that participants compared each test with the standard rather than the two tests
with each other. The three stimuli in the triad were presented as an in-line row, as
shown in Fig. 4. The left/right position of the lighter test was randomized, as was
the order in which the triads were presented. The background was a dark blue
approximately equivalent to that used by Krantz (54).
Task. Participants were required to complete this study using a computer. A
Qualtrics-based check was used to reject participants using a tablet or mobile
device to avoid skew induced by insufﬁcient screen space. Participants were asked
which of the right and left tests was more different from the middle gray and to
respond using the “q” (for left) or “p” (for right) key. Participants had an average
of three training rounds to get acclimated to the task. To increase participant
engagement during the experimental trials, participants were informed whether
they made the correct choice based on the differences on the L
∗ axis. The effect
of training (i.e., practice and feedback) over time was not statistically signiﬁcant.
Even if there was increased accuracy due to learning the task, the randomization
of the order of triads would control for that.
Data Availability. Observer responses and source code of analysis framework
are publicly available in the GitHub repository ( https://github.com/lanl/color).
The data are described in the Abstract found in the Gray Experiment, Data folder
and are contained in the comma separated values ﬁle (78).
ACKNOWLEDGMENTS. Research presented in this article was supported by
Laboratory Directed Research and Development Program of Los Alamos National
Laboratory Project 20200512ECR and is published as LA-UR-21-24630. We thank
Kei Davis for his feedback and the anonymous reviewers for pointing out the
signiﬁcance of the difference between the L
∗ axis and the perceptual scale.
1. G. Wyszecki, W. S. Stiles, Color Science (Wiley, New York, NY, 1982), vol. 8.
2. B. Riemann, Uber die hypothesen, welche der geometrie zu grunde liegen. K¨onigliche Gesellschaft
der Wissenschaften und der Georg-Augustus-Universit¨at G¨ottingen 13, 1867 (1854).
3. H. Grassmann, Zur theorie der farbenmischung. Ann. Phys. 165, 69–84 (1853).
4. D. H. Krantz, Color measurement and color theory. I. Representation theorem for Grassmann
structures. J. Math. Psychol.12, 283–303 (1975).
5. H. von Helmholtz, Wissenschaftliche Abhandlungen (JA Barth, 1883), vol. 2.
6. G. T. Fechner, W. M. Wundt, Elemente der Psychophysik: Erster Theil (Breitkopf & H¨artel, 1889).
7. E. Schr ¨odinger, Grundlinien einer theorie der farbenmetrik im tagessehen.Ann. Phys. 368, 481–520
(1920).
8. D. Nickerson, K. F. Stultz, Color tolerance speciﬁcation. JOSA 34, 550–570 (1944).
9. L. Silberstein, Investigations on the intrinsic properties of the color domain. JOSA 28, 63–85 (1938).
10. L. Silberstein, Investigations on the intrinsic properties of the color domain. II. JOSA 33, 1–10 (1943).
11. W. Stiles, A modiﬁed Helmholtz line-element in brightness-colour space. Proc. Phys. Soc.58,4 1
(1946).
12. J. J. Vos, P . L. Walraven, An analytical description of the line element in the zone-ﬂuctuation model of
colour vision. I. Basic concepts.Vision Res. 12, 1327–1344 (1972).
13. D. B. Judd, Contributions to Color Science (Department of Commerce, National Bureau of Standards,
1979), vol. 545.
14. D. L. MacAdam, Judd’s contributions to color metrics and evaluation of color differences. Color Res.
Appl. 4, 177–193 (1979).
15. M Z ´era¨ı, O Triki, “A differential-geometrical framework for color image quality measures” inAdvances
in Visual Computing. ISVC 2010. Lecture Notes in Computer Science,G .B e b i set al., Eds. (Springer,
Berlin, Germany, 2010), vol. 6455, pp. 544–553.
16. D. Raj Pant, I. Farup, Riemannian formulation and comparison of color difference formulas. Color Res.
Appl. 37, 429–440 (2012).
17. K. D. Chickering, Optimization of the MacAdam-modiﬁed 1965 Friele color-difference formula. J. Opt.
Soc. Am. 57, 537–541 (1967).
18. L. Friele, Analysis of the Brown and Brown-MacAdam colour discrimination data. Farbe 10, 193–224
(1961).
19. L. Friele, Further analysis of color discrimination data. JOSA 55, 1314–1319 (1965).
20. D. L. MacAdam, Nonlinear relations of psychometric scale values to chromaticity differences. JOSA 53,
754–757 (1963).
21. D. L. MacAdam, Smoothed versions of friele’s 1965 approximations for color metric coefﬁcients. JOSA
56, 1784–1785 (1966).
22. H. L. Resnikoff, Differential geometry and color perception. J. Math. Biol.1, 97–131 (1974).
23. J. Vos, Line elements and physiological models of color vision. Color Res. Appl.4, 208–216 (1979).
24. J. J. Vos, From lower to higher colour metrics: A historical account. Clin. Exp. Optom.89, 348–360
(2006).
25. D. B. Judd, Ideal color space: Curvature of color space and its implications for industrial color
tolerances. Palette 29, 4–25 (1968).
26. C. E. Helm, Multidimensional ratio scaling analysis of perceived color relations. J. Opt. Soc. Am.54,
256–262 (1964).
27. W. S. Torgerson, Multidimensional scaling. I. Theory and method. Psychometrika 17, 401–419 (1952).
28. M. W. Cannon Jr., Perceived contrast in the fovea and periphery. J. Opt. Soc. Am. A2, 1760–1768
(1985).
29. T. Indow, Global color metrics and color-appearance systems. Color Res. Appl.5, 5–12 (1980).
30. J. O. Ramsay, Economical method of analyzing perceived color differences. J. Opt. Soc. Am.58, 19–22
(1968).
31. R. N. Shepard, The analysis of proximities: Multidimensional scaling with an unknown distance
function. II. Psychometrika 27, 219–246 (1962).
32. W. S. Torgerson, A theoretical and empirical investigation of multidimensional scaling. ETS Res. Bull.
Ser 1951, i–123 (1951).
33. H. Wright, Precision of color differences derived from a multidimensional scaling experiment. JOSA
55, 1650–1655 (1965).
34. G. Ekman, Dimensions of color vision. J. Psychol.38, 467–474 (1954).
35. C. A. Izmailov, E. Sokolov, Spherical model of color and brightness discrimination. Psychol. Sci.2,
249–260 (1991).
36. IC on Illumination, “Colorimetry” (Rep. CIE 015:2004, Commission internationale de l’Eclairage, CIE
Central Bureau, Vienna, Austria, 2004).
37. Bureau International des Poids et Mesures, Agreement between the international commission on
illumination and the international commission for weights and measures(2007).
https://www.bipm.org/en/liaison-partners/cie. Accessed 4 January 2022.
38. C. Helm, “A successive intervals analysis of color differences” (Ofﬁce of Naval Research Tech. Rep.,
Princeton University, Princeton, NJ, 1960).
39. D. B. Judd, Interval scales, ratio scales, and additive scales for the sizes of differences perceived
between members of a geodesic series of colors. JOSA 57, 380–386 (1967).
40. T. Indow, K. Kanazawa, Multidimensional mapping of Munsell colors varying in hue, chroma, and
value. J. Exp. Psychol.59, 330–336 (1960).
41. T. Indow, T. Shiose, An application of the method of multi-dimensional scaling to perception of
similarity or difference in colors.Jpn. Psychol. Res.1956, 45–64 (1956).
42. T. Indow, T. Uchizono, Multidimensional mapping of Munsell colors varying in hue and chroma. J. Exp.
Psychol. 59, 321–329 (1960).
43. R. N. Shepard, “Parametric representation of nonlinear data structures” in Multivariate Analysis:
Proceedings of an International Symposium Held in Dayton, Ohio,P .R .K r i s h n a i a h ,E d .( A c a d e m i c
Press, New York, NY, 1966), pp. 561–592.
44. I. Lissner, P . Urban, Toward a uniﬁed color space for perception-based image processing.IEEE Trans.
Image Process. 21, 1153–1168 (2012).
45. P . Urban, M. R. Rosen, R. S. Berns, D. Schleicher, Embedding non-Euclidean color spaces into Euclidean
color spaces with minimal isometric disagreement.J. Opt. Soc. Am. A Opt. Image Sci. Vis.24,
1516–1528 (2007).
46. S. M. Wuerger, L. T. Maloney, J. Krauskopf, Proximity judgments in color space: Tests of a Euclidean
color geometry. Vision Res. 35, 827–835 (1995).
47. R. J. Ennis, Q. Zaidi, Geometrical structure of perceptual color space: Mental representations and
adaptation invariance. J. Vis. 19, 1 (2019).
48. M. Zeyen et al., “Color interpolation for non-Euclidean color spaces” inIEEE Scientiﬁc Visualization
Conference (SciVis) (IEEE, New York, NY, 2018), pp. 11–15.
49. L. D. Grifﬁn, D. Mylonas, Categorical colour geometry. PLoS One 14, e0216296 (2019).
50. F. A. A. Kingdom, N. Prins, Psychophysics: A Practical Introduction(Academic Press, ed. 2, 2010).
51. J. K. Holden, E. M. Francisco, Z. Zhang, C. Baric, M. Tommerdahl, An undergraduate laboratory exercise
to study Weber’s law.J. Undergrad. Neurosci. Educ.9, A71–A74 (2011).
52. Amazon Mechanical Turk, Amazon Mechanical Turk. https://www.mturk.com/. Accessed 2 February
2021.
53. V. Bonnardel et al., Perceptual color spacing derived from maximum likelihood multidimensional
scaling. J. Opt. Soc. Am. A Opt. Image Sci. Vis.33, A30–A36 (2016).
54. D. H. Krantz, Small-step and large-step color differences for monochromatic stimuli of constant
brightness. J. Opt. Soc. Am.57, 1304–1316 (1967).
55. W. S. Torgerson, Theory and Methods of Scaling (APA PsycInfo, 1958).
56. L. L. Thurstone, Psychophysical analysis. Am. J. Psychol.38, 368–389 (1927).
57. L. T. Maloney, J. N. Yang, Maximum likelihood difference scaling. J. Vis. 3, 573–585 (2003).
58. L. L. Thurstone, A law of comparative judgment. Psychol. Rev.34, 273 (1927).
PNAS 2022 Vol. 119 No.18 e2119753119 https://doi.org/10.1073/pnas.2119753119 9of10
Downloaded from https://www.pnas.org by 136.47.145.179 on May 11, 2026 from IP address 136.47.145.179.
59. S. J. Messick, The perception of attitude relationships: A multidimensional scaling approach to the
structuring of social attitudes. ETS Res. Bull. Ser 1954, i–231 (1954).
60. K. Knoblauch et al., MLDS: Maximum likelihood difference scaling in R.J. Stat. Softw.25, 1–26 (2008).
61. D. H. Krantz, Rational distance functions for multidimensional scaling. J. Math. Psychol.4, 226–245
(1967).
62. P . Whittle, Brightness, discriminability and the “crispening effect” .Vision Res. 32, 1493–1507 (1992).
63. W. Sch ¨onfelder, Der Einﬂuss des Umfeldes auf die Sicherheit der Einstellung von Farbengleichungen.
Zeitschrift f ¨ur Sinnesphysiologie 63, 228–251 (1933).
64. H. Takasaki, Lightness change of grays induced by change in reﬂectance of gray background. J. Opt.
Soc. Am. 56, 504–509 (1966).
65. T. Kaneko, A reconsideration of the Cobb-Judd lightness function. Acta Chromatica 1, 103–110 (1964).
66. P . Whittle, Increments and decrements: Luminance discrimination.Vision Res.26, 1677–1691 (1986).
67. S. Abasi, M. Amani Tehran, M. D. Fairchild, Distance metrics for very large color differences.Color Res.
Appl. 45, 208–223 (2020).
68. Qualtrics, Introducing XM Discover. https://www.qualtrics.com/. Accessed 2 February 2021.
69. L. Harrison, F. Yang, S. Franconeri, R. Chang, Ranking visualizations of correlation using Weber’s law.
IEEE Trans. Vis. Comput. Graph.20, 1943–1952 (2014).
70. J. Heer, M. Bostock, “Crowdsourcing graphical perception: Using Mechanical Turk to assess
visualization design” in Proceedings of the SIGCHI Conference on Human Factors in Computing
Systems, S. Hudson, G. Fitzpatrick, Eds. (Association for Computing Machinery, New York, NY, (2010),
pp. 203–212.
71. T. L. Turton, C. Ware, F. Samsel, D. H. Rogers, “A crowdsourced approach to colormap assessment” in
EuroVis Workshop on Reproducibility, Veriﬁcation, and Validation in Visualization (EuroRV3),K .
Lawonn, N. Smit, D. Cunningham, Eds. (The Eurographics Association, 2017), pp. 1–5.
72. N. Moroney, G. Beretta, “The world wide ‘gamma”’ in Color and Imaging Conference N. Bonnier, P .
Urban, Eds. (Curran Associates, Inc., Red Hook, NY, 2010), vol. 2010, pp. 1–4.
73. T. L. Turton, A. S. Berres, D. H. Rogers, J. Ahrens, “ETK: An evaluation toolkit for visualization user
studies” in EuroVis 2017 - Short Papers, B. Kozlikova, T. Schreck, T. Wischgoll, Eds. (The Eurographics
Association, 2017), pp. 43–47.
74. J. Vuong et al., Versus—a tool for evaluating visualizations and image quality using a 2afc
methodology. Vis. Informatics 2, 225–234 (2018).
75. C. Ware et al., Measuring and modeling the feature detection threshold functions of colormaps.IEEE
Trans. Vis. Comput. Graph.25, 2777–2790 (2019).
76. R. Borgo, L. Micallef, B. Bach, F. McGee, B. Lee, “Information visualization evaluation using
crowdsourcing” in Computer Graphics Forum,J .H e e r ,H .L e i t t e ,T .R o p i n s k i ,E d s .( W i l e yO n l i n eL i b r a r y ,
2018), vol. 37, pp. 573–595.
77. J. Clark, The Ishihara test for color blindness. Am. J. Physiol. Opt.5, 269–276 (1924).
78. R. Bujack, E. Teti, J. Miller, E. Caffrey, T. Turton, Empirical data from judgments of achromatic color
differences. GitHub. https://github.com/lanl/color/blob/main/Gray
Experiment/data/gray complete
data release.csv. Deposited 28 January 2022.
79. M. R. Luo, G. Cui, B. Rigg, The development of the CIE 2000 colour-difference formula: Ciede2000.
Color Res. Appl.26, 340–350 (2001).
10of10 https://doi.org/10.1073/pnas.2119753119 pnas.org
Downloaded from https://www.pnas.org by 136.47.145.179 on May 11, 2026 from IP address 136.47.145.179.
