---
doc_id: arxiv-1301.4504v4
doc_title: "Quantum Computation vs. Firewalls"
section_id: sec-015-52-reissner-nordstrom
section_title: "Reissner-Nordstrom"
section_number: 5.2
pages: 43-44
source_pdf: 1301.4504v4.pdf
source_sha256: 201acc5bb1d4b6a0
doc_brief: "Quantum Computation vs. Firewalls — In this paper we discuss quantum computational restrictions on the types of thought experiments recently used by Almheiri, Marolf, Polchinski, and Sully to argue"
---
Another way Alice could try to extend the lifetime of her black hole is by giving it some
charge. The Reissner-Nordstrom black hole of mass M and charge Q has metric
ds2 =−dt2f(r) + dr2
f(r) +r2dΩ2
2, (5.1)
where
f(r) = 1− 2GM
r + GQ2
r2 ≡ (r−r+)(r−r−)
r2 (5.2)
and
r± =GM±
√
G(GM 2−Q2). (5.3)
Its entropy is
S = πr2
+
G ≡ πr2
+
𝓁2
p
(5.4)
and its temperature is
T = r+−r−
4πr2
+
. (5.5)
We see when M𝓁P =Q, the black hole is extremal and the temperature is zero. If we
start the black hole with mass above extremality, it will radiate and gradually approach
extremality. The relevant point here is that as it does this, the temperature decreases
– 42 –
and semiclassically it appears that the decay takes an inﬁnite amount of time. More
precisely if we deﬁne the energy above extremality to be
E =M−Q𝓁−1
p , (5.6)
the energy-temperature relation is
E = 2π2Q3T 2𝓁p (5.7)
and a simple calculation tells us that, for a black hole which starts with energy E0≤
Q𝓁−1
p , we have
E(t) = E0
1 +αtE0Q−4. (5.8)
Here α is some order one numerical constant. Thus it appears that the black hole
takes an inﬁnite amount of time to reach extremality. There is a well-known problem
with this argument however [20, 21], which is that from (5.7) we see that when the
temperature reaches
T∼ 1
Q3𝓁p
(5.9)
the remaining energy E above extremality is no longer bigger than the temperature
T . At this point the semiclassical description of the evaporation process breaks down,
and quantum gravity is necessary to understand what happens next. This is related
to an instability of AdS2 called fragmentation [21], and in the cases where it can
be understood in string theory it is always true that the geometry breaks apart into
something that has little resemblance to the original Reissner-Nordstrom geometry.
It is easy to see that no matter whether we start with E near extremality or much
larger, this instability always sets in well before the exponential of the initial entropy.
For example, say that we start with E0≤ Q (setting 𝓁p = 1). The initial entropy is
of order Q2, while the time to reach the instability is of order Q7. Alternatively if we
start with E0≫Q then we are back to the Schwarzschild situation where evaporating
back down toE≈Q𝓁−1
P takes a time of orderE3
0≈S3/2
0 , and the additional time to get
down to the instability is Q7≪ S7/2
0 . The total evaporation time is always bounded
by a polynomial in S0. Thus charged black holes, near extremal or otherwise, are of no
use to Alice.
