---
doc_id: acsv231201
doc_title: "Analytic Combinatorics in Several Variables Expanded Second Edition"
section_id: sec-040-deformations
section_title: "Deformations"
section_number: null
pages: 232-239
source_pdf: ACSV231201.pdf
source_sha256: 1a664d0bf666041e
toc_source: outline
doc_brief: "Analytic Combinatorics in Several Variables Expanded Second Edition — 100 sections: Front matter; Preface to the second edition; Preface to the first edition"
---
Finally, we end this chapter with a treatment of critical points and critical val-
ues at inﬁnity. After giving a rigorous deﬁnition of such points we show how, in
their absence, to construct the deformations that prove Lemmas 7.25 and 7.28.
These two lemmas then imply Theorems 7.15 and 7.30.
7.5.1 Critical points at inﬁnity
As described above and in Appendix C, the results of Morse theory typically
require a proper height function so that certain gradient ﬂows are guaranteed
to reach points of low height, except when they get stuck near critical points.
This properness condition is often satisﬁed in classical contexts by studying
compact spaces, however our singular varieties are not compact and we often
have non-proper height functions.
Our goal, therefore, is to formulate weaker but still suﬃcient conditions for
there to be no topological obstructions to deforming our Cauchy integral to
points of low height, proving results like Lemma 7.14 and Theorem 7.35 above.
A considerable stream of topological research has gone into deﬁning bifurca-
tion values, at which the height function is not a locally trivial ﬁbration and the
topology of the space changes. While exact conditions for these topological
obstructions remain murky, we care only about pushing down domains of in-
tegration to lower height, and may thus proceed by generalizing our deﬁnition
of critical points (and critical values) to include “points at inﬁnity.”
We begin by deﬁning the binary relation R ⊆Cd
∗× CPd−1 that holds for a
pair (z, ˆr) when the diﬀerential dh ˆr|S of the height function h ˆr restricted to
the stratum S containing z vanishes at z. To facilitate computation we view ˆr
as an element of CPd−1.
Deﬁnition 7.42 (CPAI). Let R be the closure in CPd ×CPd−1 of the relation R.
A critical point at inﬁnity (CPAI) in the direction ˆr∗is a limit point (z∗, ˆr∗) in
R of points (z, ˆr) ∈R such that z∗< Cd
∗. When necessary we refer to our usual
notion of critical points (not at inﬁnity) as aﬃne critical points to distinguish
them from critical points at inﬁnity.
In other words, a critical point at inﬁnity in the direction ˆr∗is a limit, lying
either at inﬁnity or on a coordinate plane, of a sequence z(k) of critical points
contained in strata S k such that the projection of ˆr∗to the tangent space of Nk
at z(k) converges to zero as k →∞(i.e, ˆr∗lies in the “limit normal space” of
the sequence z(k)) – see Figure 7.28.
To track the heights of CPAIs, given ˆr ∈CPd−1 we deﬁne the ternary relation
7.5 Deformations
215
Figure 7.28 A sequence of points moving out to inﬁnity, such that the logarith-
mic gradient of Q approaches the vector v pointing straight up. This sequence
witnesses a critical points at inﬁnity in the direction v.
T ( ˆr) ⊆Cd
∗× CPd−1 × R containing elements (z, y, η) such that (z, y) ∈R and
h ˆr(z) = η.
Deﬁnition 7.43 (CVAI). Let T ⊆CPd ×CPd−1×R be the closure of the ternary
relation T in CPd × CPd−1 × R. We call η a critical value at inﬁnity (CVAI) if
some point (z∗, ˆr∗, η) is in T and z∗< Cd
∗.
7.5.2 Vector ﬁelds and ﬂows
The results we prove in this section are based on [BMP22, Theorem 1].
Theorem 7.44 (homotopy equivalences in the absence of CVAI). Fix a direc-
tion ˆr and a Whitney stratiﬁcation {S α : α ∈I} of (Cd
∗, M).
(i) If there are neither aﬃne critical values nor CVAI in the interval [a, b]
then the inclusion of M≤a into M≤b is a homotopy equivalence. The same
is true replacing M by any stratum S of V∗.
(ii) If there are no CVAI in [a, b] but there is a single aﬃne critical value c ∈
[a, b] and it corresponds to the set of critical points z1, . . . , zm then there
is a stratiﬁed ﬂow deforming any chain C in M down to a chain in the
union of M<c with suﬃciently small balls about each zi. When [c −ε, c +
ε] ⊆(a, b), this induces a homotopy equivalence between (Mc+ε, Mc−ε)
and the direct sum of attachment spaces Mz,loc deﬁned in Section 7.3
above (see also Deﬁnition C.31 and Figure C.6 in Appendix C).
The ﬁrst part Theorem 7.44 directly implies Lemma 7.25. The main work
216
Overview of analytic methods for multivariate GFs
in proving Theorem 7.44 comes from establishing the following result, which
requires bounding elements of a vector ﬁeld. Although general stratiﬁed spaces
do not come equipped with Riemannian metrics, we deal only with spaces
embedded in Cd  R2d and the norm of any vector or covector refers to the
norm inherited from this embedding.
Lemma 7.45 ([BMP22, Lemma 2]). Suppose a < b are real numbers such that
h ˆr has no CVAI in the interval [a, b] and one aﬃne critical value in c ∈[a, b],
not at either endpoint. Then there is a vector ﬁeld v on Cd
∗∩h−1
ˆr [a, b] with the
following properties.
(i) v is smooth on strata and continuous on Cd
∗;
(ii) v is tangent to strata;
(iii) v is a controlled vector ﬁeld in the sense of [Mat70, Section 9];
(iv) v is bounded;
(v) v has unit downward speed, meaning dh ˆr(v) ≡−1.
The ﬁrst, relatively easy, step in establishing Lemma 7.45 is to show that
|dh ˆr| is bounded away from zero except near critical points.
Lemma 7.46 ([BMP22, Lemma 1]). Suppose h is a Morse function on a strat-
iﬁed space V∗⊆Cd
∗, with no CVAI in [a, b]. Then, excluding an arbitrarily
small neighborhood N of critical points, the diﬀerential dh has its magnitude
bounded away from zero, meaning |dh| ≥δ(N) > 0.
Proof
It suﬃces to prove the result when dh is restricted to an arbitrary
stratum S . Let S [a,b] denote the elements of S with height in [a, b] and let
L = Rd × (R/2πR)d denote the logarithmic parametrizing space for Cd
∗via
the exponential map exp : L →Cd
∗. In this parametrization, h ˆr becomes
˜h = h ˆr ◦exp. This parametrization is useful because d˜h is the constant vec-
tor ˆr (formally, d˜h = Pd
j=1 r jdxj + 0dy j is a constant with respect to the
embedding in L obtained from the embedding in Cd
∗, pulled back via exp).
We use tildes to denote inverse images under this parametrization, meaning
]
critical = exp−1[critical] is the inverse image of the set of critical points
of the Morse function h.
Assume towards a contradiction that the norm of the tangential diﬀerential is
not bounded from below on eS [a,b]\N, where N is a neighborhood of
]
critical
in L, and let ˜xk be a sequence in eS [a,b] \ N for which |d˜heS ( ˜xk)| goes to zero.
This sequence has no limit points whose height lies outside of [a, b] and no
limit points in
]
critical[a,b]. There are also no aﬃne limit points outside of
]
critical, because if x →y with y in a substratum eS y then |d˜heS y(y)| ≤
lim infx→y |d˜heS (x)| since the projection of the diﬀerential onto a substratum is
7.5 Deformations
217
at most the projection onto eS . By compactness, {xk} must have a limit point x ∈
CPd. It follows from ruling out noncritical points, and aﬃne stationary points
with heights inside or outside of [a, b], that x lies at inﬁnity. The sequence
therefore deﬁnes a CPAI of height c, contradicting the hypothesis and proving
the lemma.
□
With Lemma 7.46 in hand, we outline the proof of Lemma 7.45 before re-
turning to Theorem 7.44.
Sketch of proof of Lemma 7.45
This lemma for proper height functions is the
usual Morse theoretic construction of stratiﬁed gradient-like vector ﬁelds, as
found in standard references [GM88; ABG70]. It is proved by using a partition
of unity to piece together the unit-speed downward gradient of h ˆr restricted
to each stratum and then extended to a neighborhood of the stratum in Cd
∗via
the local product structure. Property (v), unit downward speed, then follows
from Lemma 7.46. In the nonproper case, the biggest headache is extending to
the product; this was the motivation for the notion of control data, developed
in [Mat70]. When h ˆr is not proper, there is no a priori guarantee that the de-
scent rate divided by the magnitude of the vector remains bounded away from
zero, even locally. This is because the Whitney condition ﬁts these C∞strata
in a way that is in principle only C0. In fact, Mather’s argument contains the
seeds of a proof for this fact, which is accomplished via some linear algebra
and further explicit use of the Whitney conditions. See [BMP22, Lemma 2] for
full details.
□
Proof of Theorem 7.44
Let v be the vector ﬁeld constructed in Lemma 7.45,
altered so as to be zero on M≤a. This vector ﬁeld deﬁnes a ﬂow Φ(x, t) such
that
• d
dtΦ(x, t) = v(x) when h ˆr(x) ∈(a, b];
• Φ(x, t) is deﬁned for 0 ≤t ≤h ˆr(x) −a and, for t in this range, h ˆr(Φ(x, t)) =
h ˆr(x) −t;
• the map ψ(x) = Φ(x, b −a) is a continuous map on M≤b with range M≤a
and ﬁxing M≤a.
It follows from these properties that the inclusion ι : M≤a →M≤b is a ho-
motopy equivalence: ψ ◦ι is the identity map on M≤a while ι ◦ψ is homotopic
to the identity map on M≤b via the homotopy Φ on M≤b × [0, b −a]. This is
suﬃcient to imply conclusion (i) of Theorem 7.44, and also proves the weaker
version of (ii) found in [BMP22], namely that any cycle in M≤b may be de-
formed to lie in the union of M≤c−ε with arbitrarily small neighborhoods of
218 Overview of analytic methods for multivariate GFs

each critical point. However, this argument does not imply that the deforma-
tion is induced by a homotopy equivalence.

To that end, let x(a) = min{|a — z| : z € critical} denote distance to the
critical set. For s > 0, define a new vector field v, by

v(x) Kw) 28
vs(Z) = ¥ p(k(x))v(a) K(x) € [s/2, 5] ,
0 K(x) < s/2

where p is a smooth nondecreasing function with p(s/2) = 0 and k(s) = 1.

Fix € > 0 with [c — €,c + €] € (a,b) and let ®,(x, 1) denote the flow defined
similarly to ® but with v, in place of v. Let T(x) = ®,(a, 2e) denote the time
2e map for the flow ®,. Because h = hp is nonincreasing along ®,, points in
Mec-¢ remain inside Mz-_,, hence the flow defines a homotopy equivalence
between the pairs (M +2, Mc_<) and (X, M;_<), where X = t[Me+.].

Define a modified height function g = ho tT. We claim that g has the same
critical points as h in h-\([c—e, c+6]). To see this, first observe that trajectories
of ®, are either rest trajectories at points in the set Vo = {a : vs(a) = 0} or else
never enter Vo. Indeed, this follows from the fact that v, is tangent to all strata,
smooth on every stratum, and that trajectories of a flow defined by a smooth
vector field cannot merge. Inside Vo, the height functions h and g are equal,
and hence have the same critical points. Outside Vo, the differential dg|s can
never vanish because dg|s(v) < 0; this follows from the fact that for v € S, the
map dg(v)(x) = d(ho t)(v)(a) sends v to dh(Dr(v)). On trajectories, the map
Dr carries vs € Tz(S) to p(t(x)) € Tr(~)(S), where p(t(x)) > 0. Thus

dg(vs)(@) = p(t(a))dh(ws)(t(@)) = —p(t(a)) < 0,

showing that dg|s is nonvanishing outside Vo and proving the claim.

The map Tf takes all points of Mz.,, into M<,_,, except possibly for those
whose trajectories come within distance s of the critical set within time 2e.
Because v is bounded, trajectories coming within s of the (finite) critical set
within time 2¢ are all contained in some compact set K, independent of s €
[0, 1]. Therefore, the difference X \ M__, is bounded and g is a proper height
function on the pair (X, M._.), in the sense that the inverse image of a compact
set in X \ M_, is compact.

We may now apply the results of stratified Morse theory (see Theorem D.21
in Appendix D). The result is that the pair (X, Mzc_.) is homotopy equivalent
to the direct sum of pairs (N(z) U M--5, Mc_s) as 2 varies over the critical
points of height c and N(z) can be chosen to be arbitrarily small neighbor-
hoods of these, after which 6 is chosen sufficiently small. We have seen, in
7.5 Deformations
219
addition, that each cycle in X may be deformed into the union of Mc−δ and the
neighborhoods N(z) by running the ﬂow vs, hence the homotopy equivalence
is induced by this ﬂow. Finally, having shown that the ﬂow induces a homotopy
equivalence between (Mc+ε, Mc−ε) and (X, Mc−ε), we can pick s suﬃciently
small and N(z) and δ so that δ < ε, ﬁnishing the proof of part (ii).
□
Notes
The rigorous foundation of the main theorems of this book in the framework of
Morse theory is new to the second edition. Before the appearance of [BMP22],
Morse-theoretic results were not available because h ˆr is not, in general, a
proper function. Therefore, in the ﬁrst edition, Morse theory was used only as
a motivation and individual results were obtained via hands-on deformations
and surgeries, informed by Morse theory but proved as special cases, tailored
to the individual hypotheses.
Asymptotic formulae in the presence of smooth strictly minimal points ﬁrst
appeared in [PW02], followed by formulae for strictly minimal multiple points
in [PW04]. Results proving the irrelevance of non-critical minimal points were
derived in [Bar+10], and then in greater generality in [BP11], with an overview
presented in [Pem10]. The proof sketch of Lemma 7.6 was suggested to us by
Tony Pantev.
The second part of Theorem 7.44 is an improvement on the result originally
published in [BMP22]. There, it was shown that cycles may be pushed down
into the union of levels below the critical value and neighborhoods of the crit-
ical points, but not that this union is homotopy equivalent to the space at a
level above the critical value. The sticking point is that the latter requires a
deformation remaining at all times within the union, which requires geometric
facts developed at length throughout [GM88]. The present proof avoids this by
using the results of [BMP22] to eliminate escape to inﬁnity, then ﬁnishing by
using results of [GM88] as a black box.
Additional exercises
Exercise 7.15. When d = 2, the map Relog : V∗→Rd is locally one-to-one at
most points. We say that amoeba( f) is a doublet if Relog−1(x) has cardinality
precisely 2 for all x in the interior of amoeba( f). Give a proof by picture that
if amoeba( f) is a doublet then there is a natural isomorphism κ between the
reduced homology group ˜H0(amoeba( f)c) and H1(V∗), deﬁned by κ([x′] −
[x]) = INT(T(x), T(x′)).
220
Overview of analytic methods for multivariate GFs
Exercise 7.16. Let Q(x, y) = 5 −x −x−1 −y −y−1 and F(x, y) = 1/Q(x, y).
(a) Sketch amoeba(Q) and mark a point in each component of amoeba(Q)c.
(b) Recall that the Fourier series of F is the series ˆF(x, y) = P
a,b∈Z ca,bei(ax+by),
where
ca,b =
1
(2π)2
Z π
−π
Z π
−π
F(x, y)e−in(ax+by)dxdy.
The Fourier series ˆF is related to the Laurent expansion of F corresponding
to one component of amoeba( f)c. Identify this component, and describe
the relation.
(c) Prove that amoeba(Q) is a doublet.
(d) Let x = (0, 0) and x′ = (0, 2). Show that x and x′ are in diﬀerent
components of the complement of amoeba(Q), and describe or sketch
INT(T(x), T(x′)).
(e) Find all critical points of V∗in the direction r = (1/3, 2/3) and mark them
on your sketch from part (a).
(f) Deform the intersection cycle γ you found in part (d) until its highest and
lowest points are critical points in direction r = (1/3, 2/3). At which of
these points is the phase h ˆr maximized on γ?
(g) What does your result tell you about the coeﬃcients of the Fourier series
for F?
Exercise 7.17. For Q(x, y, z) = z(x −y)(x −y + z −xyz), as in Exercise 7.12,
state the dimension of the stratum containing the origin, describe the normal
link, and describe the local homology group H3(Mp,loc) when p is the origin
and r is a direction of your choice (as usual, M = Cd
∗\ VQ).
