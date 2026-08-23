---
doc_id: arxiv-2507.13873v1
doc_title: "Probing the singularity at the holographic screen via q-holography"
section_id: sec-010-holographic-counterterm
section_title: "Holographic counterterm"
section_number: null
pages: 29-31
source_pdf: 2507.13873v1.pdf
source_sha256: fa1d38d08dc4976a
doc_brief: "Probing the singularity at the holographic screen via q-holography — We study the emergence ofq-deformed spacetime in a lower-dimensional gravitational system whose asymptotic region geometrizes the"
---
The GHY boundary action with appropriate counter term is of the form
−
I
∂M
dτ
√
h

ΦK−
Z Φ
c
V (Φ)dΦ
1/2
, (B.7)
where the lower boundc of the counterterm integral is arbitrary and just corresponds to an
energy offset.12 We can motivate this counterterm explicitly by looking at the full on-shell
Euclidean action
SE =−1
2
Z
M
d2x√g (ΦR +V (Φ))−
I
∂M
dτ
√
h

ΦK−
sZ Φ∂
c
V (Φ)dΦ

. (B.8)
UsingR =−V′(Φ) and denotingF (r) =
Rr
rh
drV (r), the bulk on-shell action on the classical
solution in “Schwarzschild gauge” leads to the following expression
Son-shell
b =−β
2
Z r∂
rh
dr(−rF′′ +F′) =−β
2 [−rF′ + 2F ]r∂
rh (B.9)
=−β
2 [−r∂V (r∂) + 2F (r∂) +rhV (rh)]. (B.10)
The GHY boundary term + counterterm on the other hand gives:
Son-shell
∂ =−β
2
"
r∂V (r∂)− 2
p
F (r∂)
Z Φ
c
V (Φ)dΦ
1/2#
. (B.11)
12This specific boundary term was used in the case of sinh dilaton gravity in [36] and for sine dilaton
gravity in [59]. Here we compile the more general story. The argument follows largely the computation
presented in [101] for the case of (deformations of) JT gravity.
28
The GHY term (in darkblue) cancels a corresponding divergent bulk contribution, and the
total on-shell action reduces to
Son-shell
b +Son-shell
∂ =−2πΦh−β
 
F (r∂)−
p
F (r∂)
Z Φ
c
V (Φ)dΦ
1/2!
, (B.12)
where we usedV (rh) = 4π/β to disentangle the entropy contribution and the energy term.
The boundary counterterm is the unique option that only depends on the fields (and
not on properties of a specific solution). The resulting final expression for the ADM energy
is then suggestively written as
EADM =−
Z Φ∂
Φh
V (Φ)dΦ +
sZ Φ∂
Φh
V (Φ)dΦ×
Z Φ∂
c
V (Φ)dΦ ≈ 1
2
Z Φh
c
V (Φ)dΦ, (B.13)
under the assumption thatΦ∂ is such that
R Φ∂
V (Φ)dΦ→ +∞. The first term here comes
from the bulk on-shell term, and the second term coming from the boundary counterterm.
This result is precisely the known expression for the ADM energy of a general dilaton gravity
model.
For the specific case of the sinh (and sin) dilaton potentials, one can check that the
boundary counterterm can be equivalently written explicitly in various guises:
I
∂M
dτ
√
h
r
cosh(2πb2Φ)− 1
2π2b4 =
I
∂M
dτ
√
h
r
cosh(2πb2Φ)
2π2b4 =
I
∂M
dτ
√
h exp(πb2Φ)
2πb2 ,
(B.14)
which are equivalent since we have to take the leading term in the asymptotic expansion for
Φ∂→ +∞.
For the leftmost expression of (B.14) (which we used in the main text (3.1)), the−1
corresponds to the choice of integration constantc = 0 above. This is done to precisely
reproduce JT gravity in theb→ 0 limit.13
The rightmost form (B.14) on the other hand is natural when obtaining this system
from the perspective of two Liouville actions, and can be readily shown to lead to the same
on-shell energy expression:
EADM = 1
2
Z Φh
c
V (Φ)dΦ, (B.15)
and hence the same physics as the other two ways of writing the boundary term.
13There is an order of limits issue here, since to find JT we have to takeb→ 0 before taking Φ∂→ +∞,
corresponding to the near-boundary UV region of sinh dilaton gravity deviating from the JT AdS2 spacetime
as discussed in subsection 3.1.
29
As an aside, in the first-order formulation of dilaton gravity, the holographic boundary
term is directly chosen to be the Casimir of the Poisson algebra (spanned by 3 generators
(Φ0, Φ1, Φ∂)) as
1
2
I
∂M
dτ

Φ2
0 + Φ2
1 +
Z Φ∂
c
V (Φ)dΦ

. (B.16)
The on-shell energy computation would now instead be
EADM =−
Z Φ∂
Φh
V (Φ)dΦ + 1
2
Z Φ∂
Φh
V (Φ)dΦ + 1
2
Z Φ∂
c
V (Φ)dΦ = 1
2
Z Φh
c
V (Φ)dΦ, (B.17)
yielding indeed the same expression for the energy.
