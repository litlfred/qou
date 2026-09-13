---
doc_id: arxiv-2311.05446v3
doc_title: "NEW BRUNN–MINKOWSKI AND FUNCTIONAL INEQUALITIES VIA CONVEXITY OF ENTROPY"
section_id: sec-001-11-improved-brunnminkowski-inequalities
section_title: "Improved Brunn–Minkowski inequalities"
section_number: 1.1
pages: 1-3
source_pdf: 2311.05446v3.pdf
source_sha256: c5809730f598a56d
doc_brief: "NEW BRUNN–MINKOWSKI AND FUNCTIONAL INEQUALITIES VIA CONVEXITY OF ENTROPY — We study the connection between the concavity properties of a measureνand the convexity properties of the associated"
---
sure onR n. We say thatνsatisfies a Brunn–Minkowski inequality with
exponentaif for all Borel setsK 0,K 1⊆R n satisfyingν(K 0),ν(K 1)>0
and every 0≤t≤1 we have
ν((1−t)K 0 +tK 1)≥((1−t)ν(K 0)a +tν(K 1)a)1/a.(1)
Here (1−t)K 0 +tK1 ={(1−t)x+ty:x∈K 0, y∈K 1}is thet-Minkowski
averageof the setsK 0 andK 1. Note that the inequality becomes stronger
asaincreases. The prototypical example is the classical Brunn–Minkowski
inequality, which states that the Lebesgue measure satisfies ((1)) with ex-
ponenta= 1
n (see e.g. [25] for a survey on the Brunn–Minkowski inequality
and its importance). Whenνis not the Lebesgue measure, inequalities such
as (1) are sometimes called weighted Brunn–Minkowski inequalities.
More generally, from the works of Borell ([11], [10]) and Brascamp–Lieb
([14]), a characterization of all measuresνwhich satisfy ((1)) for some ex-
ponentais known:
Theorem 1.1.Letνbe a Borel measure onR n with densityϕwith respect
to the Lebesgue measure onR n, and fixa∈[−∞, 1
n]. Then the following are
equivalent:
1
arXiv:2311.05446v3  [math.MG]  20 Mar 2026
2 GAUTAM AISHWARYA AND LIRAN ROTEM
(1)νsatisfies a Brunn–Minkowski inequality with exponenta(we also
say thatνisa-concave).
(2)For allx,y∈R n withϕ(x),ϕ(y)>0and every0≤t≤1we have
ϕ((1−t)x+ty)≥

(1−t)ϕ(x) b +tϕ(y) b
1/b
,(2)
where 1
a = 1
b +n(we also say thatϕisb-concave).
For simplicity we assumed thatνhas a density, though Borell’s orig-
inal result is slightly more general. Note that the cases whereaorb
belong to{−∞,0,+∞}are interpreted in the limiting sense: We define
((1−λ)x a +λy a)1/a to be max(x,y) ifa=∞,x 1−λyλ ifa= 0, and
min(x,y) ifa=−∞.
Of special interest to us will be the casea=b= 0, when Borell’s theorem
essentially reduces to the Pr´ ekopa–Leindler inequality ([40, 32]): A measure
νislog-concave, i.e. it satisfies
ν((1−t)K 0 +tK 1)≥ν(K 0)1−tν(K1)t,(3)
if and only if its densityϕis of the formϕ=e −V whereV:R n→[0,∞) is
a convex function.
Borell’s theorem gives us the best possible Brunn–Minkowski inequality
satisfied by a measureνforallBorel setsK 0 andK 1. However, a better
inequality may hold for specific choices ofK 0 andK 1. For example, letγ
denote the standard Gaussian measure onR n, i.e. the measure with density
dγ
dx = 1
(2π)n/2e−|x|2/2. This is a log-concave measure, but in general it doesn’t
satisfy the Brunn–Minkowski inequality with any exponenta>0. However,
Kolesnikov–Livshyts ([29]) proved that ifK 0,K 1⊆R n are convex sets such
that 0∈K 0∩K 1, then we have
γ((1−t)K 0 +tK 1)
1
2n≥(1−t)γ(K 0)
1
2n +tγ(K 1)
1
2n.(4)
Eskenazis and Moschidis ([22]) further proved that ifK 0,K 1⊆R n are
convex andorigin-symmetric(i.e.K 0 =−K 0 andK 1 =−K 1), the exponent
1
2n improves to 1
n, which is the best possible. This settled a conjecture
of Gardner and Zvavitch ([26]). In fact, the original conjecture was that
perhaps the condition 0∈K 0∩K 1 is sufficient to have ((4)) with exponent
1
n, but Nayar and Tkocz ([37]) proved that this is not the case and suggested
that central symmetry may be the correct condition.
More generally, the following conjecture is widely believed:
Conjecture 1.2.Letνbe an even log-concave measure onR n. Then for
everyK 0,K 1⊆R n which are convex and origin-symmetric we have
ν((1−t)K 0 +tK 1)
1
n≥(1−t)ν(K 0)
1
n +tν(K 1)
1
n.(5)
One reason to believe this conjecture is the paper [33], which shows that it
would follow from another important conjecture, the log-Brunn–Minkowski
NEW BRUNN–MINKOWSKI AND FUNCTIONAL INEQUALITIES 3
conjecture. In particular, the results of B¨ or¨ oczky–Lutwak–Yang–Zhang ([12])
show that Conjecture 1.2 holds in dimensionn= 2.
In dimensionsn >2, not much is known. It is immediate from Borell’s
theorem that uniform measures on convex bodies satisfy the Brunn–Minkowski
inequality with exponent 1
n without any symmetry assumptions. The results
of [20] show that the conjecture holds in particular for rotation-invariant log-
concave measures (as well as some rotation-invariant measures that are not
log-concave). Livshyts ([34]) proved that the conjecture holds for all even
log-concave measures, but with the optimal exponent 1
n replaced by 1
n4+o(1) .
The proofs of all the results mentioned so far followed the same general
strategy. The idea was developed by Kolesnikov and Milman ([30], [31]) to
study various Brunn–Minkowski type inequalities, both onR n and in the
setting of Riemannian manifolds. The details will not be very important for
us, but roughly speaking one tries to prove that d2
dt2 (ν((1−t)K 0 +tK 1)a)≤
0 by directly computing this second derivative. Without loss of generality
it is enough to check this att= 0, which gives a functional inequality for
functionsf:∂K 0→R. Then the crucial step is to transform this inequality
to an inequality for functionsu:K 0→Rby takinguto be the solution of a
certain elliptic PDE withfas its Neumann boundary condition. As far as
we can tell this strategy strongly depends on the convexity ofK 0 andK 1,
and without this assumption no results are possible.
