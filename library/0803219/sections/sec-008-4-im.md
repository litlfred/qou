---
doc_id: 0803219
doc_title: "ACTA MATHEMATICA VIETNAMICA 219 AN INTRODUCTION TO THE VOLUME CONJECTURE AND ITS GENERALIZATIONS"
section_id: sec-008-4-im
section_title: "Im"
section_number: 4
pages: 11-12
source_pdf: 0803219.pdf
source_sha256: 8e37e11b8c8953c8
---
N →∞
log
⏐⏐JN (K; exp(2π √ − 1/N ))
⏐⏐
N = Vol(K),
where Vol(K) is the simplicial volume (or Gromov norm ) of the knot complement
S3 \ K (see [13] and [54, Chapter 6]) . Note that Vol(K) is normalized so that it
coincides with the hyperbolic volume if K is a hyperbolic knot.
This conjecture is so far proved for the following knots and l inks:
• torus knots by Kashaev and O. Tirkkonen [25]. Note that their simplicial
volumes are zero since their complements contain no hyperbo lic pieces.
So in fact they proved that the left hand side of (2.1) converg es to 0.
See Theorem 4.1 and [9] for more precise asymptotic behavior s. See also
[15, 16, 17, 18] for related topics.
• the ﬁgure-eight knot 4 1 by T. Ekholm (see for example [46, Section 3]),
• the hyperbolic knots 5 2, 6 1, and 6 2 by Y. Yokota,
• Whitehead doubles of torus knots of type (2 , b ) by H. Zheng [60],
• twisted Whitehead links by Zheng [60],
• the Borromean rings by S. Garoufalidis and Lˆ e [12, Theorem 1 2],
• Whitehead chains, which generalizes both the Borromean rin gs and twisted
Whitehead links, by R. van der Veen [56].
Removing the absolute value sign of the left hand side of (2.1 ) we expect the
Chern–Simons invariant as its imaginary part.
Conjecture 2.2 (Complexiﬁcation of the Volume Conjecture, [49]) . For any
knot K in S3 we would have
(2.2) 2 π lim
N →∞
log JN (K; exp(2π √ − 1/N ))
N = Vol(K) +
√
− 1 CS(K),
where CS(K) is the Chern–Simons invariant of the knot complement [41] if K is
a hyperbolic knot. Note that we may regard the imaginary part of the left hand
side as a deﬁnition of a topological Chern–Simons invariant.
In [49], J. Murakami, M. Okamoto, T. Takata, Y. Yokota and the author
used computer to conﬁrm the Complexiﬁcation of the Volume Co njecture for
hyperbolic knots 6 3, 8 9, 8 20 and for the Whitehead link up to several digits. (So
we do not have rigorous proofs.)
Unfortunately it is observed in [9] that for torus knots exce pt for the trefoil
knot, the limit of (2.2) does knot exist. See Section 4 for det ails.
What happens if we replace 2 π √ − 1 with another complex number? Here is
our conjecture which generalizes the complexiﬁcation abov e.
230 HITOSHI MURAKAMI
Conjecture 2.3. Let K be a knot in S3. Then there exists a non-empty open
set O of C such that for any u ∈ O the sequence
{
log
(
JN
(
K; exp
(
(u + 2π
√
− 1)/N
)))
/N
}
N =2, 3,...
converges and if we put
(2.3) H(u) := ( u + 2π
√
− 1) lim
N →∞
log JN
(
K; exp
(
(u + 2π √ − 1)/N
))
N ,
then H(u) is analytic on O. Moreover if we put
v(u) := 2 d H(u)
d u − 2π
√
− 1,
then the function
h(u) := H(u) − π
√
− 1 u − 1
4 uv(u),
coincides with the f function appearing in (1.2) and (1.3) in Subsection 1.3 up
to a constant.
If H(0) exists, that is, if the limit of the right hand side of (2.3) exists, then
the function deﬁned by
˜f (u) := H(u) − π
√
− 1 u − 1
4 uv(u) − H(0)
coincides with the f function above modulo π 2Z. Note that 0 may not be in O.
Assuming Conjecture 2.3 above and the existence of H(0), we have from (1.5)
Vol(Ku) − Vol(K) = Im H(u) − Im H(0) − π Re u − 1
4 Im
(
uv(u)
)
+ 1
4 Im
(
uv(u)
)
= Im H(u) − Im H(0) − π Re u − 1
