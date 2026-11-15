---
doc_id: phys-rep09
doc_title: "The Magnus expansion and some of its applications"
section_id: sec-014-an-improved-radius-of-convergence
section_title: "An improved radius of convergence"
section_number: null
pages: 18-19
source_pdf: phys-rep09.pdf
source_sha256: cd345d3df9358efc
toc_source: outline
doc_brief: "The Magnus expansion and some of its applications — Article history: Accepted 13 November 2008 Available online 25 November 2008 editor: D.L."
---
The previous results on the convergence of the Magnus series have been established for n x n real matrices: if A(t) is a
real n x n matrix, then (67) gives a condition for Y(t) to have a real logarithm. In fact, under the same condition, the Magnus
series (40) converges precisely to this logarithm, i.e., its sum §2(t) satisfies exp(2(t)) = Y(t) [71].

One should have in mind, however, that the original expansion was conceived by requiring only that A(t) be a linear
operator depending on a real variable t in an associative ring (Theorem 1). The idea was to define, in terms of A, an operator
§2(t) such that the solution of the initial value problem Y’ = A(t)Y, Y(0) = I, for a second operator Y is given as Y = exp 2.
The proposed expression for £2 is an infinite series, satisfying the condition that “its partial sums become Hermitian after
multiplication by i if iA is a Hermitian operator” [4]. As this quotation illustrates, Magnus expansion was first derived in the
context of quantum mechanics, and so one typically assumes that it is also valid when A(t) is a linear operator in a Hilbert
space. Therefore, it might be desirable to have conditions for the convergence of the Magnus series in this more general
setting. In [31], by applying standard techniques of complex analysis and some elementary properties of the unit sphere,
the bound r, = z has been shown to be also valid for any bounded normal operator A(t) in a Hilbert space of arbitrary
dimension. Next we review the main issues involved and refer the reader to [31] for a more detailed treatment.

Let us assume that A(t) is a bounded operator in a Hilbert space #, with 2 < dim # < oo. Then we introduce a new
parameter e € C and denote by Y(t; ¢) the solution of the initial value problem

WY = ayy, (0) =1 70
ane ; (0) =I, (70)

where | now denotes the identity operator in #. It is known that Y(t; ¢) is an analytic function of ¢ for a fixed value of t. Let
us introduce the set B, C C characterized by the real parameter y,

t
By = [> ec: if \|A(s)||ds < 7}.
0

Here ||.|| stands for the norm defined by the inner product on #,, i.e., the 2-norm introduced in Section 1.2.

If t is fixed, the operator function g(¢) = log Y(t; €) is well defined in B, when y is small enough, say y < log2,
as an analytic function of ¢. As a matter of fact, this is a direct consequence of the results collected in Section 2.7.2: if,
in particular, |e| Io \|A(s)||ds < log2, the Magnus series corresponding to (70) converges and its sum (2(t; €) satisfies
exp(2(t; €)) = Y(t; €). In other words, the power series 2(t; €) coincides with g(e) when |e| to \|A(s) lds < log 2, and so
the Magnus series is the power series expansion of y(¢) around ¢ = 0.

Theorem 6. The function g(e) = log Y(t; €) is an analytic function of ¢ in the set B,, with

B, = ecc: il f tatsias < x}
)

If #€ is infinite dimensional, the statement holds true if Y is a normal operator.
In other words, y = z. The proof of this theorem is based on some elementary properties of the unit sphere S! in a Hilbert
space. Let us define the angle between any two vectors x # 0, y # Oin #, Ang{x, y} = a,0 < a < , from

_ Re(x, y)

~ Uxilyl?

where (-, -) is the inner product on #. This angle is a metric in S', i.e., the triangle inequality holds in $'.
The first property we need is given by the next lemma [67].

Lemma 7. For any x € #,x # 0, Ang{Y(t; €)x, x} < |e] Io \|A(s) |Ids.

Observe that if Y is a normal operator in #, i.e. YY' = Y'Y (in particular, if Y is unitary), then ||Y*x|| = ||Yx|| for allx € 3
and therefore Ang{Y'x, x} = Ang{Yx, x}.

The second required property provides useful information on the location of the eigenvalues of a given bounded operator
in # [72].

Lemma 8. Let T be a (bounded) operator on #. If Ang{Tx, x} < y and Ang{T'x, x} < y for anyx 4 0,x € H, where Tt
denotes the adjoint operator of T, then the spectrum of T, 0 (T), is contained in the set

Ay = {z= |zle €C: |o| < y}.
Proof (of Theorem 6). Let us introduce the operator T = Y(t; €), with e € B,, y < mz. Then by Lemma 7, Ang{Tx, x} < y for
all x ¥ 0, and thus, by Lemma 8,

a(T) C Ay. (71)

If dim # = oo and we assume that Y(t; €) is a normal operator, then (71) also holds.
S. Blanes et al. / Physics Reports 470 (2009) 151-238 169
From Eq. (70) in integral form,
t
Y(t; e¢) =I+ ef A(s)Yds,
0

one gets ||Y|| < 1+ |e| ty |A(s)|| IY ||ds, and application of Gronwall’s lemma [73] leads to

t
Y(t: e)Il < exp (ie [ \ACyids)
i)

An analogous reasoning for the inverse operator also proves that

IY"(t; 6)I| < exp (ie | IA(ies)
0

In consequence,
IT <e” and |T~'| <e”.
IfA £0 € o(T), then |A| < ||T|| [74] and therefore |A| < e”. In addition, i € o(T~'), so that |A| > e~”. Equivalently,

o(T)c {zeC:e” <|z| <e"}=G,. (72)
Putting together (71) and (72), one has
o(T) CG,N Ay = Ay.

Now choose any value y’ such that y < y’ < m (e.g.,y’ = (vy +7)/2) and consider the closed curve P = 0.A,. Notice that
the curve I” encloses o (T) in its interior, so that it is possible to define [75] the function g(e) = log Y(t; e) by the equation

ve) = mal logz (zl — Y(t; €))~' dz, (73)
vr

where the integration along I” is performed in the counterclockwise direction. As is well known, (73) defines an analytic
function of ¢ in B,, [75] and the result of the theorem follows.

Theorem 9. Let us consider the differential equation Y’ = A(t)Y defined in a Hilbert space #€ with Y(0) = I, and let A(t) bea
bounded operator in #. Then, the Magnus series 2(t) = ran Q2x(t), with 2, given by (51) converges in the interval t € [0, T)
such that

T
il |A(s)||ds < 2
0

and the sum Q(t) satisfies exp 2(t) = Y(t). The statement also holds when # is infinite-dimensional if Y is a normal operator
(in particular, if Y is unitary).
Proof. Theorem 6 shows that log Y(t; ¢) = g(e) is a well defined and analytic function of e for

t
if |A(s)||ds < x.
0

It has also been shown that the Magnus series Q(t; €) = aa e* 2, (t), with 2, given by (51), is absolutely convergent
when |e| to \|A(s) lds < € = 1.0868... and its sum satisfies exp 2(t; ©) = Y(t; €). Hence, the Magnus series is the power
series of the analytic function g(e) in the disk |e| < &/ ty |A(s)||ds. But g(e) is analytic in B, > Bz and the power series

has to be unique. In consequence, the power series of g(e) in B, has to be the same as the power series of y(e) in Bz, which
is precisely the Magnus series. Finally, by taking « = 1 we get the desired result. ©
