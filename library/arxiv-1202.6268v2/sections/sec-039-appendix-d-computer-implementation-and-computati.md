---
doc_id: arxiv-1202.6268v2
doc_title: "THE QUANTUM CONTENT OF THE GLUING EQUATIONS"
section_id: sec-039-appendix-d-computer-implementation-and-computati
section_title: "Appendix D. Computer implementation and computations"
section_number: null
pages: 46-47
source_pdf: 1202.6268v2.pdf
source_sha256: 209af6ae25439050
doc_brief: "THE QUANTUM CONTENT OF THE GLUING EQUATIONS — The gluing equations of a cusped hyperbolic 3-manifold M are a system of polynomial equations in the shapes of an ideal triangulation T of M that"
---
An enhanced Neumann-Zagier datum is a tuple ( z, A, B,f ) attached to a regular ideal
triangulation of a cusped hyperbolic manifold M. The program SnapPy [CDW] in its python
and sage implementation computes the gluing matrices G, G′, G′′ of Sections 2.4 and 4.4;
and therefore it can easily compute an enhanced Neumann-Zagier d atum ˆβT = (z, A, B,f ).
The shape parameters z are algebraic numbers that are computed numerically to arbitrary
precision (eg, 10000 digits) or exactly as algebraic numbers.
A Mathematica module of the authors computes (numerically or exactly) the n-loop in-
variants ST ,n for n = 0, 2, 3 as well as our torsion τT given as input the Neumann-Zagier
datum. As an example, consider the hyperbolic knot 912 with volume 8.836642343... and
the SnapPy ideal triangulation with 10 tetrahedra. Its invariant trace ﬁeld E912 is Q(x)
where x =−0.06265158··· +i 1.24990458... is a root of
x17− 8x16 + 32x15− 89x14 + 195x13− 353x12 + 542x11− 719x10 + 834x9
− 851x8 + 764x7− 605x6 + 421x5− 253x4 + 130x3− 55x2 + 18x− 3 = 0
E912 is of type [1 , 8] with discriminant 3 · 298171· 5210119· 156953399. Our torsion is given
by
τ912 = 1
2
(
15− 7x− 15x2 + 55x3− 67x4 + 81x5− 43x6− 112x7 + 303x8− 488x9
+606x10− 595x11 + 464x12− 289x13 + 143x14− 49x15 + 8x16)
= −3.133657804174628986··· + 14.061239582208047255...i
The two and three-loop invariants simplify considerably when multiplied by τ 3
912 and τ 6
912
respectively and are given by
S912, 2τ 3
912 = 1
26· 3
(
36263− 194718x + 503316x2− 971739x3 + 1582041x4− 2152164x5
+2372779x6− 2109742x7 + 1426659x8− 484152x9− 374803x10 + 836963x11
−859483x12 + 621288x13− 326550x14 + 109607x15− 16840x16)
= 398 .62270435384630954··· + 948.91209325049603870...i
S912, 3τ 6
912 = 1
27
(
2320213− 19092785x1 + 72589953x2− 186402605x3 + 382362100x4
−661985976x5 + 982969902x6− 1258919324x7 + 1402544816x8
−1359436057x9 + 1134208276x10− 803313515x11 + 473961630x12
−225394732x13 + 80872920x14− 19104127x15 + 2161102x16)
= 71793 .64335382669630··· + 204530.00105728258992...i
THE QUANTUM CONTENT OF THE GLUING EQUATIONS 47
The norm (N1,N 2,N 3) =
(
N(τ912),N (S912, 2τ 3
912),N (S912, 3τ 6
912)
)
of the above algebraic num-
bers is given by
N1 = 3 · 298171 · 5210119 · 156953399
217
N2 = 173137 · 2497646101253660962719786587619396709848261029974343408485645575954409
2102 · 317
N3 = 1601979456387778103376978278735985249091224621424605434099548771751970874984335599199394506045984185143
2119
Recall that although S2, 912 is deﬁned modulo an integer multiple of 1 /24, S3, 912 is deﬁned
without ambiguity and the numerator N3 is a prime number of 103 digits.
For a computation of the Reidemeister torsion τ R
M of the discrete faithful representation
of a cusped hyperbolic manifold M, we use a theorem of Yamaguchi [ Yam08] to identify it
with
τ R
M = 1
cM
dτ R
M (t)
dt |t=1
where cM is the cusp shape of M andτ R
M (t)∈EM [t±1] is the torsion polynomial ofM using
the adjoint representation of SL(2 , C). Using the hypertorsion package of N. Dunﬁeld (see
[DFJ]), we can compute τ R
M as follows:
cd Genus-Comp
sage:import snappy, hypertorsion
def torsion(manifold, precision=100):
M = snappy.Manifold(manifold)
p = hypertorsion.hyperbolic_adjoint_torsion(M, precisi on)
q = p.derivative()
rho = hypertorsion.polished_holonomy(M, precision)
z = rho.cusp_shape()
torsion = q(1)/z.conjugate()
return [M.name(), torsion]
For the above example, we have:
sage: torsion("9_12",500)
[’L105002’, -3.133657804174628986... + 14.061239582208 047255...*I]
numerically conﬁrming Conjecture
1.8. Further computations gives a numerical conﬁrmation
of Conjecture 1.8 to 1000 digits for all 59924 hyperbolic knots with at most 14 crossing s.
