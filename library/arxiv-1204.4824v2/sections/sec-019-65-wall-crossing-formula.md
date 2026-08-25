---
doc_id: arxiv-1204.4824v2
doc_title: "Prepared for submission to JHEP Spectral networks"
section_id: sec-019-65-wall-crossing-formula
section_title: "Wall-crossing formula"
section_number: 6.5
pages: 38-40
source_pdf: 1204.4824v2.pdf
source_sha256: bf01cbaa5a8712c8
doc_brief: "Spectral networks — We introduce new geometric objects called spectral networks. Spectral net- works are networks of trajectories on Riemann surfaces obeying certain local rules."
---
In§2.3 of [5], we wrote a 2d-4d wall-crossing formula which should be obeyed by the
degeneracies µ and ω in any coupled 2d-4d system. We have given an explicit description
24Diﬀerent representatives of the class ¯c diﬀer by addition of 1-boundaries, and the 1-cycle L(γ) has zero
intersection with any 1-boundary; this would not have worked if L(γ) were merely a 1-chain.
25This is possible because the jump occurs when framed 2d-4d BPS bound states form/decay by bind-
ing/releasing 4d BPS particles.
26More precisely, (6.13) should be compared with (2.30) of [5], except for the detail that in this paper we
are working with framed protected spin characters at y = 1 rather than y =−1. The needed modiﬁcation
for y = 1 has not quite appeared anywhere before, although in (3.26) of [21] we did give the jump of
the framed degeneracies (without surface defects) at y = 1. We also noted there (in §6.4) that under the
assumption that there are no “exotic BPS states,” the jump becomes somewhat simpler (because then all
of the factors (−1)m appearing in (3.26) are the same). Strictly speaking then, (6.13) should be compared
with the most obvious combination of (2.30) of [5] and (3.26) of [21], taking into account this simpliﬁcation.
A ﬁnal detail: in (2.30) of [5] there appeared an undetermined ±1-valued cocycle σ; in (6.13) this sign is
encoded in the choice of lift ˜γ of γ.
– 36 –
of µ and ω in the theories we are now considering. So it is natural to ask whether one
can show directly that the µ and ω deﬁned here indeed obey this formula. In a sense, our
deﬁnition of ω above was engineered so that this will be true. We will not be able to give
a complete proof here, but let us at least explain the idea.
The basic strategy of proof was already explained in [5], as follows. Letu = (φ2,...,φ K)
denote a point of the Coulomb branch. Let ℘ denote a path in C which both begins and
ends at some point z. As we vary the basepoint z we can likewise deform the path ℘ (in a
unique way up to homotopy), giving a family of paths ℘(z). Now let z,ϑ andu vary along
small contractible loops z(t),ϑ(t),u(t) (0≤t≤ 1) in parameter space, with z(0) =z, and
consider the corresponding generating functions F (℘(z(t)),ϑ (t),u (t)),27 which we denote
simply as F (℘,t ).
Since t is a closed contractible loop we have
F (℘,t = 0) = F (℘,t = 1). (6.16)
On the other hand, as t varies, F (℘,t ) jumps at various critical tc. These jumps occur
either when z(t) crosses anS-wall inWϑ(t) or when ϑ(t) crosses aK-wall. At each critical
tc, the jump of F (℘,t ) is given by an explicit transformation J(tc) of the formal variables
Xa. Writing the total jump as J =∏
tcJ(tc) (with the product taken in order of increasing
tc), (6.16) thus says
J[F (℘,t = 0)] = F (℘,t = 0). (6.17)
Now, the statement of the 2d-4d wall-crossing formula is that J is the identity, or more
concretely,
J[Xa] =Xa for every a∈ Γ(z,z ). (6.18)
The most direct way to obtain (6.18) from (6.17) would be to show that any Xa for
a∈ Γ(z,z ) can be obtained as a linear combination of the F (℘,t = 0) for various paths
℘ from z to z. We have not proven this, and indeed (as one sees by considering simple
examples) it cannot literally be true except under some restrictions on the type of surface
defectsDn we allow; in general we expect to have to extend the set of allowed ℘ to include
some paths which run into the surface defects, as we did in [21].
Even after extending the set of allowed ℘ appropriately, it does not appear to be
straightforward to show that anyXa can be obtained as a linear combination of theF (℘,t =
0). We believe this is an interesting and important question (related to conjectures of Fock-
Goncharov on the relation between universally positive Laurent polynomials and tropical
points; we discussed the K = 2 case of this connection in [21].) However, we can also
propose an alternative “poor man’s” approach to proving (6.18). The idea is that even if
we cannot show that we can express Xa literally as a function of the F (℘,t = 0), we can
at least do so up to at most a ﬁnite ambiguity. More precisely, we claim that the group
G of automorphisms obeying the equation (6.17) is ﬁnite. This point will be explained in
§10.5 below. Assuming it for now, we conclude in particular that J is of ﬁnite order. But
27Up until now we have usually represented these generating functions as F (℘,ϑ ), holding u ﬁxed and
implicit; but to recover the usual statement of the wall-crossing formula we have to let u vary.
– 37 –
the automorphisms J(tc) are all “upper triangular”, in the sense that each J(tc) is of the
form 1 +X where all of the X belong to a common pronilpotent group. It follows that J
is also of this form; but then J cannot have ﬁnite order without being the identity.
