---
doc_id: sm10137-eng
doc_title: "Sbornik: Mathematics 215:12 1607–1632 Matematicheski˘ı Sbornik 215:12 30–55 Rate of convergence in the central limit theorem for the determinantal point process with Bessel kernel "
section_id: sec-035-1-an-estimate-for-r1-we-have
section_title: "An estimate for R1. We have"
section_number: 1
pages: 18-18
source_pdf: sm10137_eng.pdf
source_sha256: afd51b0231f4dc41
doc_brief: "Sbornik: Mathematics 215:12 1607–1632 Matematicheski˘ı Sbornik 215:12 30–55 Rate of convergence in the central limit theorem for the determinantal point process with Bessel kernel S. M. Gorbunov — We"
---
|R1(x, y)| ⩽
1
(x + y)2 (|b′(0)| + ∥b′′∥L1).
By Lemma 5 b′′ is absolutely integrable, so we have the following expression for
the derivative:
∂yR1(x, y) = −
2
π(x + y)3

cos(2ϕν)b′(0) +
Z ∞
0
cos((x + y)t −2ϕν)b′′(t) dt

−
1
π(x + y)2
Z ∞
0
sin((x + y)t −2ϕν)tb′′(t) dt.
Next we integrate the second term by parts:
1
(x + y)
Z ∞
0
d(cos((x + y)t −2ϕν))tb′′(t) dt = cos((x + y)t −2ϕν)tb′′(t)

∞
0
−
1
(x + y)
Z ∞
0
cos((x + y)t −2ϕν)(tb′′′(t) + b′′(t)) dt,
where the limit at infinity is zero by Lemma 5.
These calculations imply the
following estimate for x, y ⩾1:
|∂yR1(x, y)| ⩽
2
(x + y)2 (|b′(0)| + ∥b′′∥L1 + ∥tb′′′(t)∥L1).
Finally, applying Corollary 1 and Lemma 5 we obtain the required estimate for
some constant C and R ⩾1:
∥χ[R,∞)R1χ[R,∞)∥J1 ⩽C∥b∥˙B
√
R
.
