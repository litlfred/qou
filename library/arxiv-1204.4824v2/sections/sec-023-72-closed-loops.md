---
doc_id: arxiv-1204.4824v2
doc_title: "Prepared for submission to JHEP Spectral networks"
section_id: sec-023-72-closed-loops
section_title: "Closed loops"
section_number: 7.2
pages: 43-45
source_pdf: 1204.4824v2.pdf
source_sha256: bf01cbaa5a8712c8
doc_brief: "Spectral networks — We introduce new geometric objects called spectral networks. Spectral net- works are networks of trajectories on Riemann surfaces obeying certain local rules."
---
A more interesting possibility is shown in Figure 27. This case involves an S-wall which
winds around a cylinder in C many times, more and more tightly as ϑ→ϑc. In this case
two two-way streets appear simultaneously at ϑ =ϑc; let p denote one of them. p begins
and ends at the same branch point, and the soliton degeneracies are a bit more interesting
than the previous case: there are inﬁnitely many nonvanishing µ−(·), coming from the
inﬁnite set of windings of the S-wall around the cylinder, which have all coalesced onto p.
Explicitly
µ−(a) = 1, µ −(b +n(a +b)) = 1 for all n≥ 0, (7.6)
with all other µ−(·) vanishing. Hence by (6.9),
Q(p) = 1 +Xcl(a+b) +Xcl(2(a+b)) +··· (7.7)
= (1−Xcl(a+b))−1. (7.8)
Deﬁneγ = cl(¯a +¯b). The preferred lift of γ is ˜γ = cl(a +b), so we haveQ(p) = (1−X˜γ)−1,
which means αγ(p) = −1. Now, to compute L(γ) we must sum the contributions from
both two-way streets — call them p1 and p2 — so we obtain
L(γ) =−p1
Σ−p2
Σ. (7.9)
Both p1
Σ and p2
Σ are in the homology class γ, so [L(γ)] =−2γ, or
Ω(γ) =−2. (7.10)
Thus we have recovered the result of [3, 6]: this pair of closed trajectories represents a BPS
vectormultiplet.
In [3] we derived the result Ω( γ) =−2 in this situation (in the special case K = 2),
by a rather delicate analysis of the jumps of the vacuum expectation values of line defects
– 41 –
Figure 27 . A more complicated way in which S-walls can collide head-on. At ϑ < ϑc, the S-
wall supporting charge a winds once clockwise around the cylinder and then disappears toward
the bottom, while the S-wall supporting charge b winds many times counterclockwise around the
cylinder and eventually disappears toward the top. In the ﬁgure, for clarity we truncate the latter
S-wall after it has wound around a few times. At the critical ϑ = ϑc, all of the windings of the
S-wall supporting charge b coalesce onto a single closed trajectory. At ϑ > ϑc these twoS-walls
exchange roles.
associated to closed paths. This analysis gave the right answer but depended on the
assumption that at ϑ =ϑc the third trajectory emerging from the branch points in Figure
27 ends on a puncture. As Ivan Smith pointed out to us, this assumption can be violated
for higher genus C: the cylinder of closed trajectories could be dividing C into two pieces,
one of which contains no puncture. Our present analysis using line defects associated to
open paths is much simpler and is free of such extra assumptions.
Incidentally, from the point of view of the theoryS[g,C,D ] these two closed trajectories
would not seem to be the whole story. Indeed, these two ij-trajectories are actually the
two ends of a one-parameter family of closedij-trajectories, which sweep out a cylinder on
– 42 –
C. Any member of this family is a BPS string. So physically speaking we should regard
this Ω(γ) =−2 as giving the contribution from this whole one-parameter family, not just
from the two ends of the family. From our current point of view though, the ends play a
privileged role, in that they areS-walls, while the trajectories in the interior of the cylinder
are not.
Finally, although we have hidden it up to this point, the behavior of the networks Wϑ
asϑ→ϑc is actually rather complicated. In Figure 27, at ϑ<ϑ c, we see twoS-walls which
wind many times around the cylinder. There we truncated them at some ﬁnite distance
in order not to make the ﬁgure too confusing. In Figure 28 we show the full S-walls at
some particular ϑ<ϑ c. Note that the two winding S-walls thread past one another many
times before they escape the cylinder. As we vary ϑ slightly, the angle at which they are
threaded changes, and there are inﬁnitely many critical phases ϑn at which they actually
collide head-to-head. The critical phases ϑn accumulate at the value ϑc. At each of these
critical phases we have a saddle connection and the networkWϑ jumps, just as we discussed
in§7.1. We analyzed this limiting process rather closely in [3]; but we emphasize that in
Figure 28. Another picture of the S-walls on the cylinder for ϑ near the critical phase ϑc. Here
we do not truncate the walls, and we distinguish diﬀerent walls by giving them diﬀerent colors.
our current analysis, if all we want to know is the BPS degeneracy Ω( γ) which appears
exactly at the critical phase ϑc, it is not necessary to study this inﬁnite sequence of jumps.
