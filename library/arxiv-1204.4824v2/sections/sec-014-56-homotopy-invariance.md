---
doc_id: arxiv-1204.4824v2
doc_title: "Prepared for submission to JHEP Spectral networks"
section_id: sec-014-56-homotopy-invariance
section_title: "Homotopy invariance"
section_number: 5.6
pages: 30-34
source_pdf: 1204.4824v2.pdf
source_sha256: bf01cbaa5a8712c8
doc_brief: "Spectral networks — We introduce new geometric objects called spectral networks. Spectral net- works are networks of trajectories on Riemann surfaces obeying certain local rules."
---
Now let us consider a key consistency check of our story so far. We have claimed on general
physical grounds that F (℘,ϑ ) should be a homotopy invariant of ℘, or more precisely a
twisted homotopy invariant as described in §3.5. On the other hand, we have also given
a recipe which completely determines F (℘,ϑ ). So we can ask whether this recipe indeed
obeys the necessary twisted homotopy invariance.
To check this twisted homotopy invariance it is enough to check the invariance under
a few elementary moves, which we now consider in turn. This is the ﬁrst place where the
tricky minus signs mentioned in§3.5 play a decisive role.
First, consider a pair of paths ℘ and ℘′, neither of which meets any S-walls, and
which are not only homotopic but related by a regular homotopy, i.e. a homotopy through
immersions. In this case the constraint of twisted homotopy invariance requires that
F (℘,ϑ ) =F (℘′,ϑ ). (5.17)
But since neither path meets any S-walls, this reduces to
D(℘) =D(℘′), (5.18)
which is indeed true: the regular homotopy of ℘ to ℘′ lifts to a regular homotopy of each
℘(i) to ℘′(i).
– 28 –
Figure 18. A pair of paths that are homotopic but diﬀer by a unit of winding.
Next, consider the pair of paths in Figure 18. In this case the constraint of twisted
homotopy invariance requires that
F (℘,ϑ ) =−F (℘′,ϑ ). (5.19)
But neither of these paths meets any S-walls, so this reduces to
D(℘) =−D(℘′), (5.20)
which indeed follows by lifting the homotopy of ℘ to ℘′ to homotopies of ℘(i) to ℘′(i) and
using (4.1). We stress that this is a non-regular homotopy, which accounts for the sign
change.
Next, consider two paths ℘,℘′ which diﬀer by homotopy across anS-wall as shown in
Figure 19. The constraint of twisted homotopy invariance says
Figure 19. Two open paths ℘, ℘′ which diﬀer by a homotopy across an S-wall.
F (℘,ϑ ) =F (℘′,ϑ ). (5.21)
Let ¯a be the charge supported on theS-wall in the ﬁgure. The two intersectionsz± between
℘′ and the wall divide℘′ into℘′
+℘′
0℘′
−; let ˜z± be the tangent vectors to℘′ at the intersection
points. Then evaluating both sides directly, letting a be the charge supported along the
wall, and using the fact that µ(a) is constant along the wall, (5.21) becomes
D(℘) =D(℘′
+)(1 +µ(a)Xa˜z+)D(℘′
0)(1 +µ(a)Xa˜z−)D(℘′
−)
=D(℘′) +µ(a)·D (℘′
+)
(
Xa˜z+D(℘′
0) +D(℘′
0)Xa˜z−
)
D(℘′
−) (5.22)
+µ(a)2D(℘′
+)Xa˜z+D(℘′
0)Xa˜z−D(℘′
−).
The two soliton paths a˜z+ anda˜z− are both of type ij, so Xa˜z+D(℘′
0)Xa˜z− = 0. Using the
deﬁnition (4.8) one can check that the two terms in the parentheses correspond to paths
which diﬀer by one unit of winding; according to the rule (4.1), these two terms thus diﬀer
by a minus sign, and so cancel one another. Thus (5.22) reduces to
D(℘) =D(℘′) (5.23)
– 29 –
which is indeed true since the obvious homotopy of℘ into℘′ also gives homotopies between
each℘(i) and ℘′(i). Note that this would not have worked out without using the fact that
µ(a) is constant along the wall: indeed this shows that homotopy invariance requires µ(a)
to be constant along walls, thus making good on a promise we made in §4.3.
Next, consider two paths ℘,℘′ which diﬀer by homotopy across a joint, as in Figure 9
or Figure 10. We have already veriﬁed in §5.2 that in this case F (℘,ϑ ) =F (℘′,ϑ ): indeed
we used this constraint as part of our system for determining µ.
Figure 20. Two paths which diﬀer by homotopy across a branch point.
Finally we reach the most interesting case. Consider two paths ℘, ℘′ which diﬀer
by homotopy across a branch point, as shown in Figure 20. The constraint of twisted
homotopy invariance says
F (℘,ϑ ) =F (℘′,ϑ ). (5.24)
Evaluating both sides of (5.24), we obtain the explicit sums of paths shown in Figure 21.
Naively we seeK +3 terms in F (℘,ϑ ) andK +1 in F (℘′,ϑ ). The last two terms in F (℘,ϑ ),
running from sheet j to sheet j, are of the form Xa +Xa′, where a, a′ both project to the
same charge ¯a, but diﬀer by one unit of winding. These two terms thus cancel one another
thanks to our sign rule (4.1). The other K + 1 terms precisely match the K + 1 terms in
F (℘′,ϑ ). So the constraint (5.24) is indeed satisﬁed.
As an aside, note that this last constraint would not have worked out if there were
noS-walls emerging from the branch point: in other words, homotopy invariance of the
framed 2d-4d BPS spectrum really requires that spectrum to undergo wall-crossing. This
is closely analogous to the considerations of monodromy invariance that led Seiberg and
Witten to discover wall-crossing in the pure 4d BPS spectrum [45]. The constraint of
monodromy invariance also would not have worked out if we had taken µ =−1 instead of
µ = +1 in (5.12).
5.7 K = 2 theories and ideal triangulations
In the special case K = 2,Wϑ is enormously simpliﬁed: transverse intersections of S-walls
as discussed in §5.2 require at least 3 distinct sheets i, j, k, and there is no room for this
if K = 2. So in this case there are no joints where new S-walls could be born, and so
Wϑ consists simply of three S-walls emerging from each branch point. Assuming that the
parameters ma at the punctures Dn are generic enough, each of these S-walls asymptotes
to one of the punctures Dn.
When K = 2, then, the dual to the network Wϑ is an ideal triangulation T (Wϑ)
of C (determined up to isotopy). See Figure 22. Combinatorially speaking, the ideal
triangulation T (Wϑ) and the spectral network Wϑ contain the same information.
– 30 –
ii i
j i i
i ji
j i
i j
i j i
jj j
i jj
kk k
k k
Figure 21. The explicit sums of paths which occur in (5.24). In the equations shown in the ﬁgure,
we represent the formal variable Xa by an explicit picture of a smooth path on Σ, whose canonical
lift to ˜Σ represents the relative homology class a. The labels next to path segments show which
sheet of the covering Σ →C the segments are on. We have labeled the sheets in the same way as
we did in Figure 13.
Figure 22. A portion of a spectral network Wϑ with K = 2, and one face in the corresponding
ideal triangulation T (Wϑ) up to isotopy (green dashed lines). Each wall of Wϑ begins on a branch
point (orange cross) and asymptotes to a defect (blue dot); these defects are also the vertices of
T (Wϑ). Each branch point is contained in a unique face of T (Wϑ).
It has been natural to wonder what is the appropriate higher- K generalization of the
notion of ideal triangulation. In §9 below we propose a general deﬁnition of “spectral
network” which we believe is the right answer to this question. The Wϑ which we have
been discussing so far are examples of spectral networks.
– 31 –
