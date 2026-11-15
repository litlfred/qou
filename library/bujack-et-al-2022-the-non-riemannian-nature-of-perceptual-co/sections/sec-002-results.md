---
doc_id: bujack-et-al-2022-the-non-riemannian-nature-of-perceptual-co
doc_title: "The non-Riemannian nature of perceptual color space"
section_id: sec-002-results
section_title: "Results"
section_number: null
pages: 5-6
source_pdf: bujack-et-al-2022-the-non-riemannian-nature-of-perceptual-color-space.pdf
source_sha256: 2bc66a26d3901a29
toc_source: inferred
doc_brief: "The non-Riemannian nature of perceptual color space — 7 sections: Front matter; Experiment; Analysis"
---
Regression. The best-fit regression line produces the coefficients
in Table 1. The coefficient of interest is significantly negative
(β¯d = −0.005, p < 0.001), supporting the existence of dimin-
ishing returns. This coefficient indicates that the frequency that
participants select a given test approaches chance when differ-
ences are larger. This effect can be seen in Fig. 5, showing how
participants’ responses are closer to chance with increased average
Table 1.
Coeﬃcients of the regression line
Coeﬃcient
Estimate
t statistic
Signiﬁcance
β0
0.161
t(60) = 8.894
< 0.001
βΔd=5
0.048
t(60) = 2.815
0.010
βΔd=10
0.119
t(60) = 6.632
< 0.001
β¯d
−0.005
t(60) = −5.566
< 0.001
The regression model produced a good ﬁt to the experimental data: R2 = 0.556, F(3, 60) =
25.00, P < 0.001. The β-coeﬃcients are unstandardized for interpretability.
difference, ¯d, despite the value for the difference of differences,
Δd, being the same. This suggests the existence of diminishing
returns; however, it relies on the L∗axis being nearly perceptually
uniform. This assumption may not be appropriate, so we inter-
pret the negativity of the β¯d as weakly supporting our claim of
nonadditivity and as motivation to carry out further analysis.
MLE. To assess the validity and stability of the MLE-approximated
scaling function, we used a combination of cross-validation
and bootstrapping. We used 10 different test/train splits where
each test set included a random selection of 50 responses per
triad, leaving between 199 and 254 responses per triad in the
training set. The training set contained a total of 75,896 trials.
To obtain CIs around the learned scaling function, we used 100
bootstrapped samples of size 48,000 or ∼150 responses per triad
from each training set.
For each training set, a function g : R →R mapping from L∗
to perceived strength and a function f : R →R mapping from
the difference in perceived strengths to the perceived difference
were estimated. Their concatenation then provides the perceived
difference to two stimuli xi, xj via
f (|g(xi) −g(xj)|).
[17]
This approach was introduced by Krantz (61) in 1967 but aban-
doned because of the large number of parameters to estimate.
We first estimate the perceptual function g to transform the L∗
Fig. 5.
Degree of consensus is the absolute value of selecting a given
test minus 50%. The negative slope of the lines indicates that participants’
responses tend toward chance with increasing average diﬀerence in the triad,
despite the diﬀerence of diﬀerences remaining constant. A 95% CI around
each line is shown in gray.
Downloaded from https://www.pnas.org by 136.47.145.179 on May 11, 2026 from IP address 136.47.145.179.
values to perceived strengths ψ and then, use the difference in ψ
to estimate the difference scaling function f.
The perceptual function g is modeled using a monotonic spline
with four nonzero control points. The values of these points are
estimated in the optimization. These control points, along with
the point (0, 0), completely determine the spline function. The
SD was set to σ = 1. After the estimation, g was rescaled to fit the
original domain [0, 100] since a new SD will be used to estimate
the scaling function.
Four functional forms of the difference scaling function f are
used in the MLE. The first is a spline of the same form used to
approximate g. The remaining three are parameterized forms of
the hypothesized functions previously suggested to account for
diminishing returns. For these functions, the differences in ψ
were first scaled to fall in [0, 1]. In each of these functions, the
polynomial (20), the logarithm (26), and the sine (35), there is a
parameter to determine the shape, a, and a parameter to determine
the range, b:
fpoly(Δψ) = bΔψa,
flog(Δψ) = b log(aΔψ + 1)
log(a + 1)
,
fsin(Δψ) = b
sin( Δψπ
2a+1)
sin(
π
2a+1).
[18]
The optimal values of these parameters were found by the MLE.
In all functional forms of f, the SD was set to one.
All models, including the case of modeling only g and a baseline
case where the L∗values are scaled linearly to the optimal range
for an SD of one, were evaluated based on their ability to predict
participant responses in the test set. The average accuracy of these
models and error bars are the 95% confidence level is shown in
Fig. 6. Models were trained using data from all triads; however,
accuracy is visualized across the five levels of the standard. We see
here that the baseline accuracy is much lower for triads with darker
standards.
The most accurate models are the ones that include both g and
f, specifically when f takes the spline form (green line) or the log
Fig. 6.
Accuracy of optimal models.
Fig. 7.
Optimal perceptual function g from Eq. 17 mapping L∗values to
perceived grayness, ψ. The shaded region indicates the middle 95% of all
learned models across test sets and bootstrapped training sets.
(purple line). The models using the polynomial and sine for f have
a larger spread and are not significantly higher than when using
only the g transformation.
The average perceptual function g and a 95% CI are shown in
Fig. 7. The dashed line represents what would have been learned
if the L∗axis perfectly described the data. The deviation from the
dashed line occurs near the L∗of the background, suggesting that
this may be due to the crispening effect (62).
The average learned scaling function f using the flexible spline
form is shown in Fig. 8. The dashed black line indicates the
function that would have been learned if there was no evidence
of diminishing returns.
The average scaling functions using the parameterized hypoth-
esized forms of f are shown in Fig. 9, with the spline function
shown in black for comparison. The parameterized logarithm falls
closest to the spline, which is in accordance with their similar and
high accuracies in Fig. 6.
