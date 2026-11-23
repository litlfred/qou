---
doc_id: s10052-020-08615-2
doc_title: "Sum rule for the Compton amplitude and implications for the proton–neutron mass difference"
section_id: sec-034-appendix-c-derivation-of-the-sum-rule
section_title: "Appendix C: Derivation of the sum rule"
section_number: null
pages: 24-25
source_pdf: s10052-020-08615-2.pdf
source_sha256: 23becb0b1a2e7f1b
toc_source: outline
doc_brief: "Sum rule for the Compton amplitude and implications for the proton–neutron mass difference — The Cottingham formula expresses the leading contribution of the electromagnetic interaction to the"
---
To calculate the limiting value of the dispersion integral (21),
we ﬁrst use partial fractions and split the integral into two
parts:
¯T disp = −¯Sa + ¯T disp′,
¯Sa = −m2
Q2
 xth
0
dx
¯F(x, Q2)
Q2 + m2x2 ,
¯T disp′ = 4m2ν2
Q2
 xth
0
dx
¯F(x, Q2)
Q4 −4m2x2ν2 −iϵ .
(C.1)
The reason for denoting the ﬁrst term by −¯Sa is that it is
independent of ν and hence amounts to a contribution to the
subtraction function.
To perform the limit in the remainder, we decompose the
structure function into two parts with ¯F = ( ¯F−FR)+FR. In
the difference ¯F −¯FR, the terms proportional to x1−α cancel.
We assume that the remainder is sufﬁciently smooth for x →
0, so that ( ¯F −FR)/x2 is integrable and the integration can
be interchanged with the limit.7 This leads to
¯T disp′ →−¯Sb + ¯T disp′′,
7 If the singularity is more complicated, the sum rule does not get lost,
but the explicit form must be adapted.
123
¯Sb =
1
Q2
 xth
0
dx
¯F −¯FR
x2
,
¯T disp′′ =

α>0
bα(Q2)
Q2
Jα,
Jα =
 xth
0
dx
x1−α
ξ2 −x2 −iϵ ,
(C.2)
with ξ = Q2/(2mν). The integral Jα represents a hypergeo-
metric function. What remains to be done is to work out the
behaviour of this function at small values of ξ.
This can be done by making use of the known proper-
ties of the hypergeometric functions. Alternatively, one may
observe that the contributions from the critical region x ∼ξ
remain the same if the integral is extended to inﬁnity – it can
then be done explicitly. On the interval xth < x < ∞, on the
other hand, the limit can be interchanged with the integral,
which can then be done explicitly as well. The result reads
Jα = −
π
2 sin 1
2πα
e−1
2 iπαξ−α +
1
αxα
th
+ O(ξ2).
(C.3)
The ﬁrst term is proportional to να. The Reggeon ampli-
tudes speciﬁed in Eq. (18) have the same behaviour when
ν becomes large. Indeed, one readily checks that the two
expressions agree, so that
lim
ν→∞( ¯T disp′′ −¯T R) = −¯Sc
¯Sc = −

α>0
bα(Q2)
αxα
th
.
(C.4)
Collecting terms, the formula (22) yields ¯S = ¯Sa + ¯Sb + ¯Sc.
This agrees with the expression (23) for ¯S quoted in Sect. 5.
