---
doc_id: s0025-5718-07-02027-3
doc_title: "Li(p)-service? An algorithm for computing p-adic polylogarithms"
section_id: sec-006-8-concluding-remarks
section_title: "Concluding remarks"
section_number: 8
pages: 24-29
source_pdf: S0025-5718-07-02027-3.pdf
source_sha256: 080b5ac8542ff19c
doc_brief: "Li(p)-service? An algorithm for computing p-adic polylogarithms — We describe an algorithm for computing Coleman’s p-adic poly- logarithms up to a given precision."
---
In this section we describe how to make the estimates in it uniform for all ele-
ments in a ﬁxed ﬁnite extension of Qp, analyze the corresponding asymptotic time
and make a remark about an alternative approach for computing the constant term
of the Fn,ζ(t).
Remark 8.1. In case one wants to compute Li n(z)f o rs e v e r a lz in a ﬁeld F with
ﬁnite ramiﬁcation index e over Qp it is probably more eﬃcient to compute the
(approximations of the truncated) power series in Algorithm 7.10 as they are needed
using universal estimates and to remember them.
Namely, if z lies in the residue disc U
a with a ⁄= ∞,t h e nvp(z − a) ≥ 1/e.F o r
log(z)w i t hz in F ∗ we observe thatvp(log(z)) ≥ min{vp(log(p)),vp(log(y))}− vp(e)
for somey in U1 b e c a u s ew ec a nt a k eb = e in Remark 2.2 and log(η) = 0 for any root
of unityη.T h e ny =1 +x with vp(x) ≥ 1/e and, form ≥ 0, ypm
=( 1 +x)pm
=1 +x′
with
vp(x′) ≥ min{m +1 /e,(m − 1) +p / e ,...,1+ pm−1/e, pm/e}
as one easily sees by induction on m.I fw ec h o o s em ≥ 0 such that this minimum
is at least 1 /(p − 1), i.e., such that pm ≥ e/(p − 1), then vp(pm log(1 + x)) =
vp(log(1 + x′)) ≥ vp(x′) ≥ 1/(p − 1) by [16, Lemma 5.5]. Therefore vp(log(z)) ≥
min{vp(log(p)), 1/(p − 1) − m}− vp(e) for all z in F ∗.
Using those bounds one can obtain, in each of the four cases in the algorithm,
universal estimates for the lengths of the power series involved, etc., or the precision
required for z. However, for the computation of log(z) or its powers up to a given
precision in (2) the estimates involve the relative precision of z. The same applies
to 1 − z when we calculate log(1 − z) in (4)(d).
We conclude by analyzing the time needed by the algorithm. For simplicity we
only deal with the main case, that is of elementsz satisfying |z| = |z−1| =1 ,t r e a t e d
in part (3) of the algorithm. We recall theO
∼ notation (see for example [15]), where
being O∼(x)m e a n sb e i n gO(x lnc(x)) for some constant c.
Theorem 8.2. Suppose that z satisﬁes |z| = |z − 1| =1 a n db e l o n g st oaﬁ x e d
ﬁnite extension F of Qp with ramiﬁcation index e and residue extension degree f.
Then Algorithm 7.10 computes Lin(z) up to precision N with
O∼(N 2f(fnp+ne ln(p)+e2 ln(p)))
additions and multiplications and O∼(p) divisions, provided that 2n logp(N) <N ,
2n logp(2e) <N and 2p logp(N) <N .
Proof. We assume thatF is given explicitly as a purely ramiﬁed extension of degree
e of an unramiﬁed extension F unr of Qp of degree f. We begin by describing basic
operations in Qp, F unr, F and polynomial rings above these ﬁelds, as applied in our
algorithm. One ﬁrst of all observes that we can always work in the rings of integers
of these ﬁelds: in step (c) the coeﬃcients are always inZ
p by Proposition 6.1, while
in steps (f) and (g) the coeﬃcients are in F unr but have bounded denominators by
Proposition 6.7, and it is possible to multiply ﬁrst by a ﬁxed power ofp to eliminate
these denominators and divide out this power in the end. Working withZp up to a
ﬁxed precision k means working in Z/pk. Arithmetic operations modulo powers of
2 are easily done on a computer by ignoring most signiﬁcant bits, so let us suppose
Li(p) -SER VICE? AN ALGORITHM FOR p-ADIC POLYLOGARITHMS 1129
that p ⁄= 2. Then we can avoid doing divisions in these computations by using
Montgomery arithmetic [12].
Recall that in Montgomery arithmetic one represents a numberx in Z/pk by its
so called Montgomery representativexM := Rx (mod pk), where R is a power of 2t,
with t the length of a computer word in bits, such thatR>p k.O p e r a t i o n si nZ/pk
are replaced by equivalent operations on representatives, the main beneﬁt being
that multiplication can be done without using division with remainder, costing a
ﬁxed multiple of the cost of integer multiplication instead, and with no additional
cost for the other operations.
If x is known to be divisible by p,t h e ns oi sx
M and (x/p)M = xM /p.F u r -
thermore, in this case we can compute xM /p as xM · p−1 (mod R), where p−1 is
a precomputed inverse modulo R. Thus, no divisions are required. In general,
dividing by pju,w h e r eu is invertible, requires the computation of the inverse of u
modulo p, for which a gcd algorithm is used, and then a Newton iteration method
to lift this to an inverse of u modulo pk. We may precompute the inverses of all
elements modulo p, and even the most naive algorithm for this will only require
O∼(p) divisions. We may in fact notice that the only divisions that are actually
carried out during the algorithm are by integers in the range from 2 to max(tsl, gsl).
Thus, it is reasonable to simply precompute once the inverses of all of these inte-
gers. After this has been done operations in Z
p to precision k cost a ﬁxed multiple
of the same operation in Z with integers which are of size at mostpk,a n di t sc o m -
plexity is O∼(k ln(p)) additions and multiplications for multiplication if fast integer
multiplication [15, Theorem 8.24] is used. Addition is clearly faster.
We must also take into account the cost of the conversion from and to Mont-
gomery representatives. The former is smaller than a single multiplication and
has to be done only at the very end. The latter involves a division by p
k.S i n c e
z is initially represented as a polynomial of degree ef with Z/pk coeﬃcients, we
will have to convert to Montgomery form all of these coeﬃcients. We further have
to convert 1. Other elements that may appear in the algorithm are derived from
these. We need certain roots of unity in the algorithm, but for their computation
we use z as a starting point for Newton iterations. We also need certain integers
when computing the coeﬃcients of the power series we are working with. These
are easily seen to be consecutive integers (for example denominators one obtains
when integrating power series), so we will get them by successively adding 1’s in
the Montgomery representation. To eliminate divisions in the conversion we may
observe that division with remainder by p
k may be replaced by multiplication by
a precomputed R′/pk,w h e r eR′, again a power of 2t, should be bigger than all the
possible Rx (say R′ = R2), followed by division by R′ (shifting by a number of
computer words). The amount of multiplications required here is negligible com-
pared with the overall complexity (we neglect the complexity of the computation
of R
′/pk, which has to be done only once for each p and ﬁxed precision). The con-
clusion is that conversion to and from Montgomery representatives does not add to
the overall complexity.
Next we describe arithmetic inOF unr and OF , the valuation rings ofF unr and F.
These rings can be realized as extensions of the formZp[x]/(g), with g an appropri-
ate polynomial. By using polynomial Montgomery arithmetic (this is described for
1130 AMNON BESSER AND ROB DE JEU
polynomials over ﬁelds in [11] but can trivially be adapted to other rings as well)
we are again reduced to additions and multiplications of degree at most deg(g). We
can use FFT multiplication to do this withO∼(deg g) additions and multiplications
in Zp [15, Theorem 8.23].
This completes the estimate of the complexity of the basic operations. Let us
summarize this as follows. We have to do three types of multiplications, whose
complexity estimates for precision x are as follows:
• multiplications in Qp,w h i c ht a k eO∼(x ln(p)),
• multiplications in F unr,w h i c ht a k eO∼(xf ln(p)),
• multiplications in F,w h i c ht a k eO∼(xfe ln(p))
where all numbers count additions and multiplications. Now let us consider each
of the steps in Algorithm 7.10(3).
(a) By its deﬁnition and Remark 8.1 we have tsl = O(Ne). Here we are using
our assumptions on the size diﬀerences between N, n and e. Indeed, we
have to guarantee that k/e − n logp(k) >N for all k> tsl.W e s h a l l
show that we can take tsl =2 Ne. Since the function k/e − n logp(k)i s
increasing from 2Ne onward provided 2N ln(p) ≥ n, which is guaranteed
by our conditions, we only need to make sure that n logp(2Ne) <N .B u t
this is true by the ﬁrst two of our conditions, which can be rewritten as
N − n logp(N) >N /2 >n logp(2e).
(b) Here we have gsl = O(pN), again using our conditions.
(c) Now we have to compute the expansion of the gm(v)’s to gsl places. There
are n steps, each consisting of a polynomial multiplication of lengthO(pN)
with the coeﬃcients up to precisionN. Note that this computation is done
in Qp.I ti sd o n ei nt i m eO∼(n · pN · N ln(p)) = O∼(npN 2).
(d1) We ﬁnd ˜ζ in F unr by using Newton’s method to solve xpf −1 =1 . A st h e
required precision is O(N), under our assumptions the algorithm will be
about ln(N) steps, each consisting of about ln(pf )= f ln(p) multiplications
which are carried out again to precision N in F unr. The total complexity
is O∼(ln(N) · f ln(p) · Nf ln(p)) = O∼(Nf 2 ln2(p)).
(d2) Each of the gm(v) has to be evaluated at f elements derived from powers
of the ˜ζ. T h i si sd o n ei nF unr. As the precision is O(N) and the polyno-
mials are of length O(pN), the complexity is O∼(n · f · Np · Nf ln(p)) =
O∼(np(Nf )2).
(e) For the calculation of Li m(ζ) for all m ≤ n we evaluate the expression in
Proposition 4.2 of length f, which involves an addition and multiplication
in F unr,a n dp o w e r so fp. The total time for this is O∼(n · f · Nf ln(p)) =
O∼(nf 2N ln(p)) since there are no denominators involved and, takingtsl =
2Ne as before, the required precision is O(N) by our assumptions.
(f) The computation of Fn,ζ(t)i n v o l v e sn times multiplication of polynomials
of degree O(Ne) with coeﬃcients in F unr, hence takes time
O∼(n · Ne · Nf ln(p)) = O∼(nfeN 2 ln(p)).
Note that we used the fact that we can work with polynomials with coeﬃ-
cients in OF unr by multiplying by pN by Proposition 6.7 and our assump-
tions, dividing out this power of p and the end. The resulting precision
needed in OF unr is at most 3N under our assumptions.
Li(p) -SER VICE? AN ALGORITHM FOR p-ADIC POLYLOGARITHMS 1131
(g) This step consists of evaluating a polynomial of degreeO(Ne)a ta ne l e m e n t
of OF ,s oi tt a k e st i m eO∼(Ne · Nfe ln(p)) = O∼(f(Ne)2 ln(p)). Again we
used the fact that the relevant coeﬃcients of pN Fn,ζ(t) lie in OF unr ⊆O F .
Looking at the time complexities of all the steps we see that those of (d2), (f)
and (g) dominate, and their sum gives our time estimate. □
Remark 8.3. (1) The estimates in Theorem 8.2 are based on computing the value
at z from scratch. As mentioned in Remark 8.1, if we want to compute Li n(z)
for several z in the same residue disc Uζ, then it is more eﬃcient to compute the
approximation of the truncation of Fn,ζ(t) and remember it, since then only (g)
will have to be performed again.
(2) The time estimates in Theorem 8.2 are worst case estimates. Ifz is closer to
the root of unityζ the complexities of (f) and (g) are reduced, since one needs fewer
terms in the power series expansion around ζ to achieve the required precision.
Example 8.4. Tables 1 through 4 give the cpu times (in seconds) taken by the
calculation of Lin(z) up to precision N using Algorithm 7.10, for various F, N, n,
p and z. In all cases we used F = Qp(ζ,π )w i t hζ ⁄=1ap r i m i t i v e(pf − 1)-th root
of unity and π a root of the Eisenstein polynomial q(x). So F unr = Qp(ζ)i st h e
unramiﬁed extension of Qp of degree f, F = F unr(π) is totally ramiﬁed of degree
e =d e g (q(x)) over F unr and vp(π)=1 /e.
We used the branch of the logarithm for which log( p)=0( s e eR e m a r k2 . 2 ) ,
which, as mentioned in Remark 7.4, only makes a diﬀerence in (2) and (4), corre-
sponding to Tables 2 and 4 respectively. The algorithm was implemented in version
2.12-19 of MAGMA [14] (but using a correct implementation of the logarithm in-
stead of the ﬂawed built-in version) with universal estimates as in Remark 8.1,
and the calculations were performed on an Intel Pentium 4 CPU (2.66GHz) with
500MB of RAM. The programs that were used for creating Tables 1 through 4 are
available on http://www.few.vu.nl/~jeu.
Tables 1 through 4 correspond precisely to (1) through (4) in Algorithm 7.10
so that Theorem 8.2 corresponds to Table 3. In this table we have split out the
times according to what has to be done only once for each N, n and p (Time 1,
for the computation of g
n(v) in (3)(a)–(c)), what has to be done once for each
residue disc Uζ (Time 2, for the computation of Fn,ζ(t) in (3)(d)–(f)), and the
evaluation of Fn,ζ(t)a t z − ζ (Time 3, for (3)(g)), which has to be carried out
for all z in Uζ unless they are close together. Similarly the times in Table 4 have
been split out according to the time needed for the computation ofHn(t)a n ds o m e
universal constants (Time 1, corresponding to (4)(a)–(c)) and the computation of
− logn−1(z)l o g ( 1− z)/(n − 1)! and evaluation of Hn(t)a t t = z − 1( T i m e2 ,
corresponding to (4)(d)–(e)).
We mention that all calculations were done from scratch for each part, whereas
one could easily combine the computation of gn(v) in (3)(c) with that in (4)(b) if
p ⁄= 2 by increasing gsl and/or the precision in Qp as necessary. Since, in practice,
for larger values of N, most of the time in (3) and (4) is taken up by this step, this
would be a substantial saving.
1132 AMNON BESSER AND ROB DE JEU
Table 1. Timings for Lin(π(ζ − 1)).
q(x) np e f N Time
x8 − 2 4 282 1 00 .020
x8 − 2 4 2821 0 00 .190
x4 − 3x + 3 1 0 343 1 00 .030
x4 − 3x + 3 10 3 4 3 100 0 .250
x3 − 11x + 1 151 1 3 31 0 0 .010
x3 − 11x + 1 151 1 3 3 1 0 0 0 .150
x3 − 37x + 3 753 7 3 21 0 0 .010
x3 − 37x + 3 753 7 3 2 1 0 0 0 .160
x2 + 101 3 101 2 2 10 0 .000
x2 + 101 3 101 2 2 100 0 .080
Table 2. Timings for Lin((ζ − 1)/π).
q(x) np e f N Time
x8 − 2 4 282 1 00 .100
x8 − 2 4 2821 0 00 .500
x4 − 3x + 3 1 0 343 1 00 .210
x4 − 3x + 3 10 3 4 3 100 1 .540
x3 − 11x + 1 151 1 3 31 0 0 .040
x3 − 11x + 1 151 1 3 3 1 0 0 0 .750
x3 − 37x + 3 753 7 3 21 0 0 .030
x3 − 37x + 3 753 7 3 2 1 0 0 0 .690
x2 + 101 3 101 2 2 10 0 .010
x2 + 101 3 101 2 2 100 0 .180
Table 3. Timings for Lin(ζ +( ζ − 1)π).
q(x) np e f N Time 1 Time 2 Time 3
x8 − 24 2 8 2 1 0 0 .020 0 .060 0 .040
x8 − 2 4 2821 0 0 0 .100 0 .200 0 .130
x4 − 3x +3 1 0 3 4 3 1 0 0 .380 0 .330 0 .070
x4 − 3x + 3 10 3 4 3 100 1 .630 1 .150 0 .250
x3 − 11x + 1 151 1 3 31 0 0 .380 0 .570 0 .010
x3 − 11x + 1 151 1 3 3 1 0 0 6 .980 1 .600 0 .080
x3 − 37x + 3 753 7 3 21 0 2 .440 0 .630 0 .000
x3 − 37x + 37 5 37 3 2 100 65 .850 2 .370 0 .060
x2 + 101 3 101 2 2 10 7 .390 11 .110 0 .000
x2 + 101 3 101 2 2 100 368 .070 14 .480 0 .030
Li(p) -SER VICE? AN ALGORITHM FOR p-ADIC POLYLOGARITHMS 1133
Table 4. Timings for Lin(1 + (ζ − 1)π).
q(x) np e f N Time 1 Time 2
x8 − 24 2 8 2 1 0 0 .500 0 .080
x8 − 2 4 2821 0 0 4 .620 0 .300
x4 − 3x +3 1 0 3 4 3 1 0 0 .650 0 .160
x4 − 3x + 3 10 3 4 3 100 3 .470 0 .590
x3 − 11x + 11 5 11 3 3 10 0 .330 0 .040
x3 − 11x + 11 5 11 3 3 100 7 .270 0 .270
x3 − 37x + 37 5 37 3 2 10 1 .980 0 .030
x3 − 37x + 37 5 37 3 2 100 71 .260 0 .230
x2 + 101 3 101 2 2 10 5 .750 0 .020
x2 + 101 3 101 2 2 100 363 .550 0 .080
Remark 8.5. In (5.11) (where p = 2) we calculate the constant term of Hn(t)
without ever using gn(v). We can do this also for Fn,ζ(t)i f p is any prime and ζ is
any root of unity of order dividing pf − 1, at the cost of possibly having to adjoin
the pf -th roots of unity to the ﬁeld. Namely, by Proposition 2.10(1) we have that
Lin(ζpf
)= pf (n−1) ∑
ηpf =1
Lin(ηζ),
and since ζpf
= ζ this determines the constant of integration in (4.6) just as in the
proof of (5.11) because all ηζ lie in Uζ. However, since this involves pf evaluations
as in Algorithm 7.10(3)(g) in a ﬁeld of degreepf −pf −1 over Qp(ζ), this, in general,
would be less eﬃcient than our approach, which requires only f evaluations in
Qp(ζ)o f gn(v). Moreover, this power series is independent ofζ and f so that, once
computed for given p and N, it can be used for any residue disc Uζ with ζ ⁄=1a
root of unity of order relatively prime to p.
