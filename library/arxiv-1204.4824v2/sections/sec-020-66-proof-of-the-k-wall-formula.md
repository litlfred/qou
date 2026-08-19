---
doc_id: arxiv-1204.4824v2
doc_title: "Prepared for submission to JHEP Spectral networks"
section_id: sec-020-66-proof-of-the-k-wall-formula
section_title: "Proof of the K-wall formula"
section_number: 6.6
pages: 40-42
source_pdf: 1204.4824v2.pdf
source_sha256: bf01cbaa5a8712c8
doc_brief: "Spectral networks — We introduce new geometric objects called spectral networks. Spectral net- works are networks of trajectories on Riemann surfaces obeying certain local rules."
---
Here we provide the proofs omitted in §6.3.
First let us explain why L(γ) as deﬁned in (6.12) is indeed a 1-cycle, i.e. has no
boundary. For any two-way streetp, the boundary of pΣ lies over the boundary of p. More
precisely, a boundary point ofp may be either a branch point or a joint;pΣ has no boundary
over a branch point, but does have a boundary over a joint. So we need to check that L(γ)
has no boundary over a joint. To establish this we consider Figure 26. Let z denote the
ij
jk ik
ij
jkik
ji
ji
kj
kj
ki
ki
Figure 26. A joint where two-way streets meet. Each two-way street is shown slightly “resolved”,
as explained at the end of §6.2. The resolution here is the “American resolution,” as appropriate
since we are considering the limit ϑ→ϑ−
c .
joint in the ﬁgure. The coeﬃcient of z(i) in ∂L(γ) is αγ(p1) +αγ(p2)−αγ(p3)−αγ(p4),
and we would like to show that this vanishes. Consider the open paths ℘ and ℘′. The
constraint of twisted homotopy invariance says that F (℘,ϑ−
c ) = F (℘′,ϑ−
c ). In particular,
we can look at the pieces on both sides which involve paths which both begin and end on
sheet i:
F (℘,ϑ−
c )ii =F (℘′,ϑ−
c )ii. (6.19)
Directly computing the two sides of (6.19) we obtain
Q(p1)Q(p2) =Q(p3)Q(p4). (6.20)
This amounts to
αγ(p1) +αγ(p2) =αγ(p3) +αγ(p4), (6.21)
which is what we wanted to show.
– 38 –
Now let us explain why the jump formula (6.6) is true. We will show that the following
hold both forF(℘) =F (℘,ϑ +
c ) andF(℘) =K (F (℘,ϑ−
c )):
P1. F(℘) is a twisted homotopy invariant of ℘ (in the sense explained in §3.5).
P2. If ℘ does not meetWϑc, then
F(℘) =D(℘). (6.22)
P3. If ℘ and ℘′ have endpoints oﬀWϑc,F obeys the composition law
F(℘)F(℘′) =F(℘℘′). (6.23)
P4. If ℘ crossesWϑc exactly once at a point z on a one-way street p, thenF(℘) is of the
form
F(℘) =D(℘+)

1 +
∑
¯a∈Γs
ij
µ(a)Xa˜z

D(℘−), (6.24)
for some µ(a)∈ Z.
P5. If℘ crossesWϑc exactly once at a point z on a two-way streetp, and the intersection
between ℘ and p is positive (with respect to the orientation of p as a ji trajectory
and the underlying orientation of C as a complex curve), then F(℘) is of the form
F(℘) =D(℘+)

1 +
∑
¯a∈Γs
ji
µ(a)Xa˜z



1 +
∑
¯b∈Γs
ij
µ(b)Xb˜z

D(℘−) (6.25)
for some µ(a)∈ Z and µ(b)∈ Z.
ForF(℘) =F (℘,ϑ +
c ) these properties follow directly from what we have already said;
the most nontrivial one is P5, which is (6.5). To prove them for F(℘) =K(F (℘,ϑ−
c )) is
slightly harder. P1-3 are true of F (℘,ϑ−
c ) and clearly preserved by K. P4 is also true
of F (℘,ϑ−
c ), but we have to show it is preserved by K: this follows simply from the fact
thatK just multiplies each term by a function of the X˜γ, which indeed preserves the form
(6.24). P5 is the only really nontrivial one. We begin with the formula (6.4) for F (℘,ϑ−
c ),
and need to show that the action of K transforms it into the form (6.25). Expanding out
(6.4) we ﬁnd various classes of terms:
F (℘,ϑ−
c )ii =℘(i)
+

1 +
∑
¯a,¯b
µ−(a)µ−(b)XbXa

℘(i)
− =Q(p)℘(i), (6.26)
F (℘,ϑ−
c )ij =℘(i)
+

∑
¯b
µ−(b)Xb

℘(j)
− , (6.27)
F (℘,ϑ−
c )ji =℘(j)
+
(∑
¯a
µ−(a)Xa
)
℘(i)
−, (6.28)
F (℘,ϑ−
c )jj =℘(j), (6.29)
F (℘,ϑ−
c )kk =℘(k) for k /∈{i,j}. (6.30)
– 39 –
Within each class, the terms in the sum over ¯ a,¯b diﬀer only by multiplication by factors
X˜γ. Since L(γ) is a multiple of γ, it follows that ⟨γ,L (γ)⟩ = 0. Hence the action of
K on each class of terms is independent of the particular term. We consider them in
turn. For the ii terms,K acts by multiplication by ∏
γ∈Γc(1 +X˜γ)⟨℘(i),L(γ)⟩, but using
(6.12) we see that ⟨℘(i),L (γ)⟩ =−αγ(p) (since p is the only edge of W crossed by ℘)
and hence this reduces to multiplication by Q(p)−1. On the jj termsK similarly acts
by multiplication by Q(p). On the ij terms the action of K is more complicated: it
is multiplication by a new function H = ∏
γ∈Γc(1 + X˜γ)⟨℘(i)
+ +¯b+℘(j)
− ,L(γ)⟩. But we have
⟨℘(i)
+ + ¯b +℘(j)
− ,L (γ)⟩ =−⟨℘(j)
+ + ¯a +℘(i)
−,L (γ)⟩ as one readily sees using the facts that
cl(¯a +¯b) is proportional to L(γ) and⟨℘(i),L (γ)⟩ =−⟨℘(j),L (γ)⟩. It follows that the action
ofK on the ji terms is multiplication by H−1. These facts together are suﬃcient to imply
the desired P5. 28
Finally we must explain why these properties actually determineF(℘). As a warm-
up, suppose that there are only one-way streets. In that case we have shown in §4 and
§5 above that the properties P1-P4 are suﬃcient to determine all of the µ(a), and hence
also to ﬁx F(℘). The same kind of argument can be made in the presence of two-way
streets; the only new complication is that the local structure around joints and branch
points is more complicated. Nevertheless, a direct computation using only the fact that
F(℘) obey P1-P5 determines the µ(a) appearing there for all charges a oriented out of a
joint, in terms of theµ(a) for chargesa oriented into the same joint. (The resulting explicit
formulae are recorded in Appendix A, e.g. (A.3).) Inductively we can thus determine the
2d-4d degeneracies µ(a) everywhere onWϑc, just as we did in the (generic) case with only
one-way streets. Having done so the F(℘) are also determined by P1-P5. This completes
the proof.
