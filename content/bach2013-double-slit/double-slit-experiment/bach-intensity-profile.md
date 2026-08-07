The intensity profile was digitized from Figure 3e of \cite{bach2013}
(6235 electron detections, central five diffraction orders).  The
digitization was performed by threshold-based bright pixel extraction
from the arXiv PDF (arXiv:1210.6243v1), producing a 150-bin histogram
of horizontal electron positions mapped to scattering angle via the
measured fringe spacing.

**Experimental parameters**:
$a = 50$ nm, $d = 280$ nm, $\lambda = 50$ pm, $E = 600$ eV.

The digitized data spans $\pm 2.56$ mrad in scattering angle and shows
five resolved interference maxima consistent with the
double-slit geometry.  The central peak is normalized to unity.

The standard Fraunhofer prediction for these parameters is

$$
  I(\theta) = \cos^2\!\left(\frac{\pi\,d\sin\theta}{\lambda}\right)
  \cdot \mathrm{sinc}^2\!\left(\frac{\pi\,a\sin\theta}{\lambda}\right),
$$

which predicts fringe spacing
$\Delta\theta = \lambda / d \approx 0.179$ mrad.

The digitized profile is used in the
[double-slit simulator](/double_slit_simulator.html) alongside the
standard QM prediction and the QOU $q$-deformed model for direct
three-way comparison.
