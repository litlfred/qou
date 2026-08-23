---
doc_id: arxiv-hep-th-9306069v2
doc_title: "The stretched horizon and black hole complementarity"
section_id: sec-015-34-a-causal-description-of-the-stretched-horizon
section_title: "A causal description of the stretched horizon"
section_number: 3.4
pages: 30-34
source_pdf: 9306069v2.pdf
source_sha256: a140d10424f73233
doc_brief: "The stretched horizon and black hole complementarity — Three postulates asserting the validity of conventional qu antum theory, semi-classical general relativity and the statistical basis for"
---
Our aim is a self-contained description of black hole evolut ion as seen by a distant
observer in which no reference need be made to events behind t he stretched horizon. It will
also become clear that such a formulation has signiﬁcant adv antages in the low energy sector,
compared to a semi-classical description which focuses on b oundary conditions imposed at
the boundary curve γ cr. In particular, the stretched horizon oﬀers a uniﬁed view, i n which
it is no longer necessary to treat the cases of large and small incident energy ﬂux separately.
We saw earlier that the stretched horizon begins to expand in what appears to be a
teleological manner before the incoming matter arrives. On e might be concerned that this
would preclude a conventional causal Hamiltonian descript ion of the quantum stretched
horizon. We do not believe this to be the case. From a formal po int of view, the cause of the
horizon expansion is a gravitational dressing which is atta ched to the incoming energy ﬂux.
Consider the initial state description in tortoise coordin ates. Suppose an incoming ﬂux of
energy is described by T++(σ +). The functions P+ and M are given in tortoise coordinates
by
P+(σ +) =
σ+
∫
−∞
due −uT++(u),
M(σ +) =
σ+
∫
−∞
duT ++(u),
(3. 37)
and the ﬁeld Ω is given by
Ω = e2σ +
[
P∞ −P+(σ +)
]
eσ+
+M(σ +) −κ
4
[
σ + + log(P∞ +e−σ−
)
]
(3. 38)
Let us subtract from Ω the functional form Ω which it would have in the absence of any
incoming matter,
Ω = e2σ − κ
2σ. (3. 39)
30
We obtain
ω ≡ Ω − Ω = ω in(σ +) +ω out(σ −), (3. 40)
where
ω in(σ +) =
(
P∞ −P+(σ +)
)
eσ+
+M(σ +),
ω out(σ −) = −κ
4 log
(
1 +P∞eσ−)
.
(3. 41)
We see that the free ﬁeld ω consists of an incoming part and an outgoing part. We can use
the outgoing ω ﬁeld to determine the outgoing energy-momentum ﬂux.
Since the incoming part is completely determined by the inco ming energy ﬂux, we will
consider it to be a “dressing” of the incoming matter. It can b e written
ω in(σ +) =
∫
duT ++(u)W (σ + −u), (3. 42)
where
W (σ + −u) = Θ( u −σ +)e(σ+−u) + Θ( σ + −u). (3. 43)
In other words, a bit of energy δM arriving along the curve σ + = u must be accompanied
by an ω dressing which has the value W (σ + −u)δM . The ω dressing precedes the incoming
fi ﬂux, and is the ﬁrst thing that strikes the stretched horizon . By time reversal symmetry,
a bit of outgoing energy δM departing along the curve σ − =v also has an ω dressing given
byW (v −σ −)δM .
In a complete quantum theory, the outgoing state would be des cribed by a vector in
the physical state space of fi-particles, from which it would be possible to compute the
expectation value of T−−. This would not be feasible, however, even if we knew the exac t
nature of the microstructure of the stretched horizon. As we shall now see, thermodynamic
arguments can give information about ω out, which is suﬃcient to compute T−−.
The ω dressing of the incoming matter satisﬁes
(∂ + −∂ 2
+)ω in(σ +) = T++. (3. 44)
By time reversal we obtain a relation between ω out and T−−:
(∂ − +∂ 2
−)ω out(σ −) = −T−−. (3. 45)
31
This can be written as a condition at the stretched horizon,
dω out
dt = −T−−
(
t, ˆσ S(t)
)
−d2ω out
dt2 (3. 46)
The outgoing thermal ﬂux T−− is assumed to originate at the thermally excited stretched
horizon. The entropy of the stretched horizon is given by ω =ω in+ω out, since at the stretched
horizon, ω = A.
In thermal equilibrium, T−− should be a well-deﬁned function of the thermodynamic
state of the stretched horizon, and thus of the entropy ω S. More generally, for non-
equilibrium processes such as the onset and end of Hawking ev aporation, the ﬂux may
depend on the detailed time history. Nevertheless, we will c onsider a simpliﬁed model in
whichT−− depends only on the instantaneous value of ω S, and the sign of its time derivative.
In other words, we shall allow for the possibility that T−−(ω ) has diﬀerent functional forms
at the beginning and end of the evaporation. Thus, we assume t he radiated ﬂux is a function
of ω ,
T−− =T−−(ω ) = T−−(ω in +ω out). (3. 47)
Substituting this into (3.46) gives
˙ω out + ¨ω out = −T−−(ω out +ω in). (3. 48)
Since ω in(t) is known in terms of T++, we have obtained a diﬀerential equation for ω out.
To obtain agreement with the semi-classical theory for larg e black holes, we assume that
T−−(ω ) approaches the value κ
4 for ω ≫ κ . Of course, T−−(ω ) should be zero for ω = 0,
which is the ground state of the stretched horizon. Furtherm ore, if one requires that the
onset of the Hawking radiation, for a massive black hole, agr ees with the semi-classical result
(3.21), then one is led to a speciﬁc form for T−−(ω ) during the heating phase at early times.
This can be constructed as follows. Deﬁne a function z(ω ) by
ω =z(ω ) − κ
4 log
(
1 + 4
κ z(ω )
)
, (3. 49)
then choose
T−−(ω ) = κ
4
[
1 − 1
(1 + 4
κz(ω ))2
]
. (3. 50)
For massive black holes, it can be shown that ω (t) as given by (3.40) solves (3.48) until near
32
the end of the evaporation.
We can now see an important advantage of the stretched horizo n formulation, concerning
the endpoint of Hawking evaporation. In the semi-classical RST model [23], overall energy
conservation could only be achieved by having a negative ene rgy “thunderpop” at the end
of the evaporation process. The negative energy was bounded and small, but nevertheless
an embarrassment [25]. In contrast, consider the sum of (3.4 4) and (3.45), evaluated at the
stretched horizon,
˙ω in − ¨ω in + ˙ω out + ¨ω out =T++ −T−−. (3. 51)
Integrating both sides of (3.51) over time reveals that ener gy is conserved, i.e.,
∫
dtT ++ =
∫
dtT −− (3. 52)
as long as ω begins and ends at zero. This is assured in the remote past, when the stre tched
horizon coincides with the boundary curve. For the late time evolution of ω , we return to
(3.48). From (3.41) we see that the late value of ω in is the total infalling mass, so ω in →M∞.
Inserting this into (3.48) leads to the following diﬀerenti al equation for ω out at late time:
¨ω out + ˙ω out +T−−(ω out +M∞) = 0 . (3. 53)
This is the equation for the damped motion of a particle subje ct to a restoring force, with
equilibrium position at ω out +M∞ = 0. Provided the motion is overdamped, we ﬁnd that ω ,
and therefore T−−, tend smoothly to zero at late times. This places a condition onT−−(ω ),
namely that it goes to zero no slower than ω
4 . Comparing with (3.49) and (3.50) we see that
T−− must depend diﬀerently on ω during the cooling and heating phases.
33
