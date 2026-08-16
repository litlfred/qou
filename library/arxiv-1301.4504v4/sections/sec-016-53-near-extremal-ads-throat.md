---
doc_id: arxiv-1301.4504v4
doc_title: "Prepared for submission to JHEP DEDICATED TO JOHN PRESKILL ON THE OCCASION OF HIS 60 TH BIRTHDAY Quantum Computation vs. Firewalls Daniel Harlowa Patrick Haydenb aPrinceton Center "
section_id: sec-016-53-near-extremal-ads-throat
section_title: "Near Extremal AdS Throat"
section_number: 5.3
pages: 44-46
source_pdf: 1301.4504v4.pdf
source_sha256: 201acc5bb1d4b6a0
doc_brief: "DEDICATED TO JOHN PRESKILL ON THE OCCASION OF HIS 60 TH BIRTHDAY Quantum Computation vs. Firewalls Daniel Harlowa Patrick Haydenb aPrinceton Center for Theoretical Science, Princeton University, Princ"
---
Recall the AdSd Schwarzschild geometry
ds2 =−f(r)dt2 + dr2
f(r) +r2dΩ2
d−2, (5.10)
– 43 –
with
f(r) = 1 +
(r
R
)2
− α
rd−3. (5.11)
A scalar ﬁeld on this background feels an eﬀective potential. In particular if we look
for solutions of the Klein-Gordon equation of the form
φ≡r−d−2
2 e−iωtY𝓁(Ωd−2)Ψω𝓁(r), (5.12)
it is not hard to see that Ψ ω𝓁 must obey a Schrodinger-type equation
− d
dr2
∗
Ψω𝓁 +Veff (r)Ψω𝓁 =ω2Ψω𝓁. (5.13)
Here r∗ is a “tortoise” type coordinate obeying
r′
∗(r) =f−1, (5.14)
and the eﬀective potential is
Veff (r) =R−2
(
1 +
(R
r
)2
− αR2
rd−1
)[(
m2 + d(d− 2)
4R2
)
r2
+
(
𝓁(𝓁 +d− 3) + (d− 2)(d− 4)
4
)
+ (d− 2)2
4 · α
rd−3
]
.
(5.15)
The details of this potential do not matter, but we see that it vanishes linearly at the
only real positive root of f(r), that is at the horizon, and that it grows quadratically
withr at larger. Near the horizon the solution then behaves as Ψ ω𝓁∼eiω(±r∗−t), while
at large r we haveφ∼r−∆± with the usual AdS/CFT formula
∆± = d− 1
2 ± 1
2
√
(d− 1)2 + 4R2m2. (5.16)
The idea of this section is to cut oﬀ this geometry at some large value of r and
sew it onto Minkowski space, after which the eﬀective potential (5.15) would go back
to zero provided we set the scalar ﬁeld mass m2 to zero. The black hole would then be
able to decay via massless quanta tunneling out of this potential into the Minkowski
region, and by choosing the crossover value of r to be large we could adjust the decay
time independently of the entropy of the black hole. We can also “outsource” the
computation by putting the computer out in the Minkowski region, which allows us
to buy a large redshift factor enhancement in the time it takes to do the computation
from the point of view of Alice living down by the black hole.
– 44 –
There is a new problem with this construction however, which is that any attempt
to send the result of the computation from the Minkowski region back down the throat
to the vicinity of the black hole has to get back through the potential barrier. The signal
the computer sends down the throat will need to be very low energy, so its absorption
probability will be exponentially small. Nonetheless one could imagine trying to send
the signal repeatedly, hoping that eventually one of the times it will get through. This
approach gets much harder as the size of the signal we wish to send increases, but
unlike the previous examples it is not obvious that it cannot be done and we need to
analyze it more carefully.
