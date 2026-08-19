---
doc_id: arxiv-1512.04993v2
doc_title: "Complexity, action, and black holes"
section_id: sec-039-a1-comments-on-hamiltonian-locality-and-gate-sim
section_title: "A.1 Comments on Hamiltonian locality and gate simplicity"
section_number: null
pages: 57-64
source_pdf: 1512.04993v2.pdf
source_sha256: b8047bc3d3815406
doc_brief: "Complexity, action, and black holes — Our earlier paper “Complexity Equals Action” conjectured that the quantum computational complexity of a holographic state is given by the classical action of a"
---
In the previous section, it was mentioned that the elements of the gate set {Gα} are
taken to be close to the identity Gα = I +iδHα, with the Hα taken to be simple
Hermitian operators. Here, we will elaborate a bit on what is meant by simple in this
context, and whether it is reasonable to have a bound on complexity. 18
18We thank Douglas Stanford for questions and discussions leading to the creation of this section.
56
An individual Hα will be a product of operators at neighboring points, with the
number of such operators deﬁning the size or weight of the Hα. We will call a gate set
k-local if all elements of {Hα} have a size less than or equal to k. When we say that
the Hα should be simple, what we mean is that k should be small.
In this paper, we are mostly interested in estimating the complexity of Hamiltonian
time evolution. Thus, our gate set should be adept at approximating U(t) = e−iHt.
In the limit of small δ, we can suggestively write a gate as Gα =eiδHα. This suggests
a reasonable choice for the {Hα} could be the individual terms in the Hamiltonian.
Certainly this makes it clear how this gate set can approximate Hamiltonian time
evolution.
Even with a more general gate set, this also suggests a reasonable value fork. If the
Hamiltonian isk-local, then we should at least choose a gate set that is also onlyk-local.
There’s some reasonable intuition behind this: a Hamiltonian with locality k means
that interactions are roughly spread over at most k degrees of freedom. Presumably
in a circuit approximation of Hamiltonian evolution, one should only be able to use
gates that mix together at most k degrees of freedom per gate. However, by measuring
the complexity with a gate set that either depends directly on the H (by explicitly
choosing the Hα to be the terms in H) or by picking the k-locality of the Hα to equal
the k-locality of the Hamiltonian, we see that the complexity C will be a function of
both the Hamiltonian and the state. By changing the properties of H, we have to
change the way in which we measure C.19
Instead, let’s consider the more general case, where we choose a j-local gate set,
but have a k-local Hamiltonian. In that case, C has the desirable property of being a
function of j and the state |ψ⟩, but no longer a function of H. Now, it’s easy to see
that the bound discussed in this paper
dC
dt≤ 2
πℏ⟨ψ|H|ψ⟩, (A.5)
cannot hold without modiﬁcation. As a simple example, consider the case of k≫ j.
(For instance if the system hasN degrees of freedom,H is a random 2N×2N Hermitian
matrix, and j is O(1).) For k∼N, a small amount of time evolution will lead to near
exponential complexity as measured by the j-local gate set and violate the bound.
Therefore, we need to consider the dependence on both j and k explicitly
dC
dt≤ g(k)
f(j)
2
πℏ⟨ψ|H|ψ⟩, (A.6)
where the monotonically increasing functions f(j),g (k) capture the dependence of
the complexity on the locality of the gate set and the Hamiltonian. A reasonable
19In particular, we thank Douglas Stanford for emphasizing this point.
57
assumption is that these are the same functions of their argument (since they’re trying
to account for the same type of dependence). Thus, for the natural choice discussed
above j = k, these factors cancel, and Eq. A.6 reduces to Eq. A.5. For the case
considered previously k≫ j, we see that the bound becomes harder and harder to
violate, compensating for the large increase of complexity under time evolution as
measured by the j-local gate set. In the other limit of k≪ j, the rate of complexity
growth is vanishing. This is because the gate set is so large that the reference system
is never more than O(1) gates away from the time-evolved state; the complexity will
always stay small.
A comment on the relevance of the ground state
The complexiﬁcation bound we propose has the unusual property of depending on the
energy of the ground state of the Hamiltonian H. Given the ground state, |0⟩, and a
state of interest, |ψ⟩, one might think that it could be possible to change the energy
of the ground state ⟨0|H|0⟩ without altering the complexodynamics of ⟨ψ|H|ψ⟩. By
arbitrarily lowering the ground state, it appears we could make the diﬀerence⟨ψ|H|ψ⟩−
⟨0|H|0⟩ arbitrarily large.
Let’s explore this idea a bit further. We can lower the ground state by an amount
∆> 0 by adding a term to the Hamiltonian
H′ =H− ∆|0⟩⟨0|. (A.7)
The ground state of the perturbed Hamiltonian H′ has ground state energy⟨0|H|0⟩−
∆<⟨0|H|0⟩. Additionally, if the ground state has negligible support on |ψ⟩ such that
⟨0|ψ⟩≪ 1, then the complexodynamics remain unchanged ⟨ψ|H′|ψ⟩≈⟨ ψ|H|ψ⟩. This
appears to let us shift the complexiﬁcation bound by an arbitrary amount. However,
the catch is that the ground state projector |0⟩⟨0| is a high-weight operator of O(N)
and will destroy the locality of the Hamiltonian.
If instead we take ∆ < 0 and try to make the complexiﬁcation bound tighter, the
ground state will quickly cross the gap and become an excited state. Since the gap is
O(N−1), this would only be a 1 /N correction to the bound.
B Spherical shock waves at ﬁnite time and energy
We will work inD = 2+1 dimensions for simplicity. The shock wave has energy E and
the black hole has energy M, so we want to patch together a spacetime with energy
E +M (to the left of the shock) and a spacetime with energy M (to the right of the
58
shock). See Fig. 18. We will follow [26, 51] for the matching conditions between the
two spacetimes.
Let us associate coordinates ( u,v ) with the patch with energy M and (˜u, ˜v) with
the patch with energy E +M. Because of the increase in mass, the horizons are at
diﬀerent radii in the two spacetimes, rh and ˜rh, respectively. In the patch with energy
M, the relationship between Kruskal coordinates and Schwarzschild coordinates in the
asymptotic region to the left of the horizon is
u =
√r−rh
r +rh
e−rhtL/𝓁2
AdS, v =−
√r−rh
r +rh
erhtL/𝓁2
AdS, (B.1)
and in the patch with energy M +E the relationship is 20
˜u =
√
r− ˜rh
r + ˜rh
e−˜rhtL/𝓁2
AdS, ˜v =−
√
r− ˜rh
r + ˜rh
e˜rhtL/𝓁2
AdS, (B.2)
where on this boundary, time runs backwards so that the upper left of Fig. 18 is at
tL =−∞.21 We must have ˜rh > rh since the horizon jumps out when it swallows the
shock, and in fact the two horizon radii are related by
˜rh =rh
√
M +E
M =rh
√
1 +ϵ, (B.3)
where we’ve deﬁned ϵ≡E/M.
We will parametrize the shock wave by its boundary time tw and its energy ϵ. In
the (u,v ) coordinates, we can describe the shock wave as traveling along a null surface
of constant u =u0. In the (˜u, ˜v) coordinates, the shock wave travels on a null surface
at constant ˜u = ˜u0. We see from Eq. B.1 and Eq. B.2 that by demanding that the
shock leave the boundary at time tw that these surfaces are given by
u0 =e−rhtw/𝓁2
AdS, ˜u0 =e−˜rhtw/𝓁2
AdS, (B.4)
respectively.
Next, we need to relate the (˜u, ˜v) coordinates to the (u,v ) coordinates. The match-
ing conditions [51] amount to ensuring that the metric is continuous. First, we match
across the radius of the transverse space. This gives
˜rh
1− ˜u0˜v
1 + ˜u0˜v =rh
1−u0v
1 +u0v (B.5)
20We have ﬁxed a relative boost ambiguity by demanding that the boundary time tL is continuous.
21Note: in this Appendix we have reversed our time conventions for precursors W (t). Here, we
will take both left boundary Hamiltonian time evolution tL and Killing time evolution in the bulk to
increase to the past.
59
Figure 18: Kruskal diagram of shock wave at ﬁnite time tw. The white region to the
right of the shock has energy M and is covered by coordinates (u,v ). The gray region
to the left of the shock has energy M +E and is covered by coordinates (˜u, ˜v). The
shock is drawn in blue and travels along the surface u0 = e−rhtw/𝓁2
AdS or equivalently
˜u0 =e−˜rhtw/𝓁2
AdS.
Solving for ˜v, we see that it’s a fractional linear transformation of v,
˜v(v) = 1
˜u0
((˜rh−rh) + (˜rh +rh)u0v
(˜rh +rh) + (˜rh−rh)u0v
)
(B.6)
Now normally we’d expand Eq. B.6 in the limit ϵ→ 0 and tw→∞ , with ϵ/u0 ﬁxed.
Then, we’d ﬁnd ˜v(v) =v +ϵ/4u0 and that crossing the shock induces a simple shift. At
this order, we’d also have ˜rh =rh, and we’d pick ˜u(u) =u to satisfy the ﬁnal matching
condition. However, since tw→∞ , the shock would have to lie on the horizon u = 0.
Since ϵ→ 0, the shock would have to have vanishing mass.
Instead, let’s study ﬁnite energy shocks at ﬁnite time, keeping ϵ and tw ﬁnite and
arbitrary. The only thing left to do is to relate ˜u and u. The ﬁnal matching condition
[51] is that guvdudv =g˜u˜vd˜ud˜v along the shock
− 4𝓁2
AdS
(1 +uv)2dudv|u=u0 =− 4𝓁2
AdS
(1 + ˜u˜v)2d˜ud˜v|˜u=˜u0 (B.7)
This reduces to the following condition on ˜u′(u)
˜u′(u)|u=u0 =u
√1+ϵ−1
0
√
1 +ϵ. (B.8)
While there is still some freedom in the function ˜ u(u) away from the shock, we can
simply satisfy Eq. B.8 by taking
˜u =u
√1+ϵ. (B.9)
60
This condition makes the ﬁrst derivative smooth across the shock on the boundary,
but causes a kink across the shock on the singularity.
Now that we have ˜u(u) and ˜v(v), we can ﬁnd out how far the horizon jumps out
after absorbing the shock by inverting ˜v(v) = 0. This is the analog of the simple shift
we are used to
v(˜v = 0) =− 1
u0
(√1 +ϵ− 1√1 +ϵ + 1
)
, (B.10)
which goes like−ϵ/4u0 in the limit ϵ→ 0, exactly as expected from [26]. The Kruskal
diagram is shown in Fig. 18. Below the shock in the white region, we use the ( u,v )
coordinates. Above the shock in the gray region, we use coordinates (˜ u(u), ˜v(v)). We
see that (as expected) there’s no kink across the shock at the boundary, but there is a
kink at the matching across the singularity.
Let us make a brief remark on the action ofW in the geometry shown in Fig. 18. As
we will explain in the next subsection, we ﬁnd something very diﬀerent from Eq. 6.15.
Here, for times tL before the perturbation tw the rate of growth with tL would be M,
but for times after the perturbation, the rate would be M +E. This is indicative of
the fact that this geometry actually represents energy E being injected into the state
on the left boundary at time tL.
B.1 Precursor at ﬁnite time and energy
While the geometry Fig. 18 considered in the last section is a proper solution to Ein-
stein’s equations, it is not the correct dual to the state
|ψ⟩ =W (tw)|TFD⟩, (B.11)
whereW (tw) =e−iHLtwW eiHLtw andW is an operator smeared over the spatial sphere
with energy ϵM, and ϵ is ﬁxed but not necessarily small. This is no longer a small
perturbation—its energy scales withN 2—but we can still consider its backreaction and
the geometry dual to the state.
The correct procedure for constructing the geometry is described in [29]. First, we
start with the thermoﬁeld double state, which is dual to the eternal AdS black hole
geometry. Then, we evolve back by time tw and apply the operator W . Finally, we
evolve forward by tw back to tL = 0. We can think of this in terms of a time fold,
where the perturbation is added on the second sheet. The ﬁnal geometry is given by
continuing the ﬁnal sheet before and after the perturbation. The upshot is that the
perturbation travels away from the boundary into the future and into the past.
The Kruskal diagram of this geometry is shown in Fig. 19. The correct picture
for the state Eq. B.11 is that of the perturbation emerging from the past singularity,
61
Figure 19: Kruskal diagram of shock wave at ﬁnite time tw. The white region to
the right of the shock has energy M and is covered by coordinates ( u,v ). The gray
region to the left of the shock has energy M +E. Above the shock, it’s covered by
coordinates (˜u, ˜v). Below it’s covered by (¯u, ¯v). The shock is drawn in blue. When
leaving the boundary it travels along the null surface u0 = e−rhtw/𝓁2
AdS or equivalently
˜u0 = e−˜rhtw/𝓁2
AdS. When approaching the boundary it travels along the null surface
v0 =−erhtw/𝓁2
AdS or equivalently ¯v0 =−e˜rhtw/𝓁2
AdS.
materializing on the boundary at time tL = tw, and then traveling oﬀ into the future
singularity. Additionally, note that the past horizon shrinks by some amount after
ejecting the perturbation, and the future horizon grows outward by a diﬀerent amount
after swallowing the perturbation. These are the analogs of the simple shifts usually
considered in the inﬁnite time shock wave geometries.
The right way to think about the diﬀerence between the geometries in Fig. 18 and
Fig. 19 is that in the former case, energy E is injected into the left CFT at time tw.
Before that time, there the CFT had average energyM and there was no perturbation.
In the latter case, the state in the Schr¨ odinger picture is given by Eq. B.11. We can
time evolve the state on the left side via the time evolution operator eiHtL, but at all
times the perturbation is present and the system has energyM +E. This is important,
because these two geometries give diﬀerent predictions for the complexity of the state
for times tL before tw.
The coordinates above and to the left of the shock are still the (˜ u, ˜v) coordinates
considered in the last section. The transformation between these coordinates and the
(u,v ) coordinates is given by Eq. B.6 and Eq. B.9. Let’s label the coordinates below
the shock (¯u, ¯v). The matching procedure is analogous to what we did before, so we
62
will brieﬂy state the results. The past moving shock travels along the surface
v0 =−erhtw/𝓁2
AdS, ¯v0 =−e˜rhtw/𝓁2
AdS. (B.12)
The shock hits the boundary at (u0,v 0) and (¯u0, ¯v0). Using the deﬁnition of the bound-
ary and direct comparison to Eq. B.4, we can easily identify the relations
v0 =−u−1
0 , ¯v0 =−˜u−1
0 . (B.13)
From this, we can simply write down the full coordinate transformations
¯u(u) =−˜u0
((˜rh−rh)u0− (˜rh +rh)u
(˜rh +rh)u0− (˜rh−rh)u
)
, ¯v(v) =−(−v)
√1+ϵ. (B.14)
Similar to before, there was freedom in the metric matching condition in how we extend
the ¯v(v) function away from the shock.
Finally, as noted in Eq. B.10, the analog of the simple shift for the future horizon
is given by v(˜v = 0). For the past horizon, the shift is given by
u(¯u = 0) = u0
ϵ
(
1−
√
1 +ϵ
)2
, (B.15)
which goes like u0ϵ/4∼ 0 in the limit of ϵ/4u0 ﬁxed.
