---
doc_id: arxiv-1204.4824v2
doc_title: "Prepared for submission to JHEP Spectral networks"
section_id: sec-017-62-k-walls-and-the-degenerate-spectral-networks
section_title: "K-walls and the degenerate spectral networks Wc"
section_number: 6.2
pages: 34-38
source_pdf: 1204.4824v2.pdf
source_sha256: bf01cbaa5a8712c8
doc_brief: "Spectral networks — We introduce new geometric objects called spectral networks. Spectral net- works are networks of trajectories on Riemann surfaces obeying certain local rules."
---
There is also a second, more interesting kind of jump which can occur at a critical phase
ϑ =ϑc. In contrast to the previous case, these jumps do not arise because of a change in
the interaction betweenWϑ and℘. Rather, they arise because of a topology change in Wϑ
itself.
The claim that a topology change in Wϑ could occur as we continuously vary ϑ might
at ﬁrst seem strange. After all, we have given a recipe forWϑ in§5,ϑ enters this recipe only
20The meaning of the limit (6.1) is easy to understand if there are no other special values ϑ′
c in some
neighborhood of ϑc. However, it does sometimes happen that the special values accumulate. In that case
we have to explain what kind of limit we mean in (6.1). One possibility would be to ﬁx some R >0 and
work with a “Z-adic” norm where‖∑caXa‖ = ∑|ca|e−R|Z¯a|. We expect that in this norm the limit (6.1)
indeed exists. At any rate, in what follows we work formally, assuming that the limits make sense.
– 32 –
(ij)
ij
ij
Figure 23. The behavior of ij-trajectories approaching a branch point of type ( ij).
through the diﬀerential equation (3.1), and this equation evidently depends continuously on
ϑ. The point is that the solutions of (3.1) can nevertheless exhibit discontinuous behavior,
because of the phenomenon of bifurcation near the branch points: ij- or ji-trajectories
coming close to an (ij) branch point can veer oﬀ in one of two directions, as indicated in
Figure 23. This ﬁgure can be considered to depict either a foliation of C byij-trajectories
at ﬁxed ϑ or the evolution of an S-wall inWϑ as ϑ varies. From the latter viewpoint it
follows that the critical phases ϑc are those at which some S-wall of type ij or ji runs
directly into a branch point of type ( ij). We call the ϑc where this occurs K-walls. A
simple example is shown in Figure 24.
Figure 24. The simplest way in which Wϑ can jump at a K-wall. As ϑ→ϑc, twoS-walls merge
into a single two-way street running between two branch points. The two-way street supports two
distinct charges ¯a, ¯b.
To describe the relation between F (℘,ϑ +
c ) and F (℘,ϑ−
c ), it is convenient to work
directly with the limiting spectral network Wϑc. This limiting network has some features
not seen for the generic Wϑ. In particular, several (possibly inﬁnitely many) S-walls,
supporting diﬀerent charges, might coalesce into a single segment as ϑ→ϑc; hence a wall
p ofWϑc might support several distinct charges. Moreover, the S-walls coalescing onto p
might not all be oriented in the same direction; in this case we call p a two-way street.21
Again see Figure 24 for an example: the saddle connection in the middle of the ﬁgure is
21We now have two metaphors for the segments in a spectral network. They are walls because they are
the loci where framed 2d-4d BPS degeneracies jump. On the other hand we will ﬁnd that the metaphor of
streets is also very useful when tracking the solitons. Rather than insisting on one term, we will use them
as synonyms. We feel no inclination to go to wall-street.
– 33 –
a two-way street. Indeed, Wϑc always contains at least one two-way street, since we get a
two-way street whenever anS-wall runs into a branch point.
ij
jiij
ji
Figure 25. A path ℘ crossing a pair of nearly coincident S-walls, which coalesce into a two-way
street at ϑ =ϑc.
Now let us consider a path ℘ which crosses a two-way street p. A representative
picture of the situation when ϑ is near ϑc is indicated in Figure 25. 22 We deﬁne BPS
soliton degeneracies µ±(a,p ) along the walls ofWϑc by taking limits of µ(a,p ) as ϑ→ϑ±
c .
Applying the rules of §4.4 and taking the limit ϑ→ϑ±
c , we obtain formulas for F (℘,ϑ±
c ):
F (℘,ϑ−
c ) =D(℘+)

1 +
∑
¯b∈Γs
ij
µ−(b)Xb˜z



1 +
∑
¯a∈Γs
ji
µ−(a)Xa˜z

D(℘−), (6.4)
F (℘,ϑ +
c ) =D(℘+)

1 +
∑
¯a∈Γs
ji
µ+(a)Xa˜z



1 +
∑
¯b∈Γs
ij
µ+(b)Xb˜z

D(℘−). (6.5)
Here Γs
ij⊂ Γij(z,z ) denotes the set of charges supported along the two-way street.
Note that the order in these products really matters, since Xa˜z and Xb˜z do not com-
mute. A convenient way to think about this is to regard the limiting network Wϑc as
equipped with a bit of extra structure: each two-way street is resolved into two inﬁnitesi-
mally separated and oppositely oriented “lanes”. For ϑ−
c the division of lanes is according
to the American rule (drive on the right), while for ϑ+
c it is according to the British rule
(drive on the left). We can determine F (℘,ϑ±
c ) completely fromWϑc andµ±, using either
(6.4) or (6.5) as appropriate.
6.3 The jump of F (℘,ϑ ) at aK-wall
The jump of F (℘,ϑ ) at ϑc is given by a certain universal substitution K acting on the
formal variables Xa:
F (℘,ϑ +
c ) =K
(
F (℘,ϑ−
c )
)
. (6.6)
K is determined by the degenerate spectral networkWϑc. In this section we describe what
K is, deferring the proof of (6.6) to §6.6.
We are going to combine the soliton degeneracies on any two-way street p into a new
generating function Q(p). Unlike the generating functions F (℘,ϑ ) we have considered
before, Q(p) is written in terms of formal variables X˜γ with ˜γ∈ ˜Γ, where ˜Γ = H1(˜Σ; Z)
modulo shifts by 2H (cf. the deﬁnition of ˜Γ(˜z1, ˜z2) in§3.5). So these formal variables are
22In general the picture might be a bit more complicated than Figure 25, because there might be several
walls of type ij and/or of type ji which all coalesce at ϑ =ϑc. An example appears in Figure 27 below.
– 34 –
associated to closed paths, rather than the open ones we have encountered up to now. We
extend our multiplication rules,
X˜γXa =X˜γ+a, X ˜γX˜γ′ =X˜γ+˜γ′ (6.7)
(where the + denotes the obvious action of ˜Γ on ˜Γ(˜z1, ˜z2) or on ˜Γ). We also extend our
sign rules by imposing
XH =−1, (6.8)
so the two X˜γ corresponding to diﬀerent lifts of a single γ∈ Γ diﬀer only by a sign.
One can build closed paths from open ones: givena∈ ˜Γii(˜z, ˜z), there is a corresponding
cl(a)∈ ˜Γ which is obtained just by forgetting the basepoint ˜z(i). Using this we deﬁne
Q(p) = 1 +
∑
¯a∈Γs
ij,¯b∈Γs
ji
µ−(a,p )µ−(b,p )Xcl(a+b). (6.9)
(We will see later that we would have gotten the same Q(p) if we had used µ+ instead of
µ− on the right.) Q(p) is a power series in the variables X˜γ, of a constrained sort: every
γ that occurs is a sum ¯a + ¯b of charges supported at z, and hence has e−iϑcZγ∈ R−.
Now we make a new genericity assumption. Let Γ c⊂ Γ be the set of all γ∈ Γ with
e−iϑcZγ ∈ R−; we assume that Γ c is generated by a single element γ0. (This condition
holds automatically if our chosen u = (φ2,··· ,φK) is not on a wall of marginal stability in
the Coulomb branch.) Q(p) is then a power series in a single variable: choosing a lift ˜ γ0,
eachXcl(a+b) =±Xn
˜γ0 for some n> 0. Our next aim is to extract the BPS degeneracies by
rewriting this power series as a product, (6.11) below.
For eachγ∈ Γ we can deﬁne a preferred lift ˜γ by the following rule:23 representγ as a
union of smooth closed curves cm on Σ; then ˜γ is the sum of the canonical lifts of the cm to
˜Σ, shifted by
(∑
m≤nδmn + #(cm∩cn)
)
H (of course since we work modulo 2 H, all that
matters here is whether this sum is odd or even.) One can check directly that ˜γ so deﬁned
is independent of the choice of how we represent γ as a union of cm (this requirement is
what forced us to add the tricky-looking shift.) Moreover, with this deﬁnition one has
X˜γ+˜γ′ = (−1)⟨γ,γ′⟩X~γ+γ′. (6.10)
We are ready to factorize Q(p): there exist exponents αγ(p)∈ Z such that
Q(p) =
∏
γ∈Γc
(1−X˜γ)αγ(p). (6.11)
(Indeed, the equations determining the αγ(p) from Q(p) are upper-triangular and hence
can be solved.) Then, for any γ∈ Γc, deﬁne a 1-chain L(γ) on Σ by
L(γ) =
∑
p
αγ(p)pΣ, (6.12)
23In the ﬁrst preprint version of this paper we proposed a diﬀerent lifting rule based on the principle that
the product (6.11) should be ﬁnite. More recently, in studying more complicated examples, it has turned
out that sometimes this ﬁniteness is violated [46]. For completeness we have back-ported the corrected rule
from [46] to here.
– 35 –
wherep runs over the walls inWϑc, and pΣ is the oriented 1-chain obtained by lifting p as
in§3.1.
It is a crucial fact (proven in §6.6 below) that L(γ) so deﬁned is actually a 1- cycle.
This allows us to deﬁne24 an intersection number⟨¯c,L (γ)⟩ for any ¯c∈ Γ(z1,z 2). Moreover,
e−iϑc
∫
pΣ
λ∈ R−, soe−iϑcZ[L(γ)]∈ R; under our genericity assumption this implies that the
homology class [L(γ)] is a multiple of γ (though not necessarily a positive multiple). This
fact will be useful below.
Finally we can deﬁne our universal substitution K:
K(Xa) =
∏
γ∈Γc
(1−X˜γ)⟨¯a,L(γ)⟩Xa. (6.13)
