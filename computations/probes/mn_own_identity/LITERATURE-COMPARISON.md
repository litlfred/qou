# m_n by its own identity: where the error comes from, against the literature (2026-11-21)

Scope: the compute of this directory (the convention-D proton identity read for the neutron,
three-strand readings N0/N1/N2 and four-strand arms L-A/L-B/L-C). The Q_β route (`Q_β = m_e·R(q)`,
`R ≤ 3/4`) belongs to another thread and is not redone here. CODATA and the literature values
below are comparison points only; none enters a proof or a fit. Numbers of this framework are
recomputed with mpmath at 50 dps at the muon pin (CAL-2, CODATA 2022 `m_μ/m_e`).

## 1. The literature split of m_n − m_p = 1.29333 MeV (n − p)

| source | QCD part (m_d − m_u) | QED part | total | in library |
|---|---|---|---|---|
| Borsanyi et al. (BMW) 2015, lattice QCD+QED | +2.52(17)(24) | −1.00(07)(14) | 1.51(16)(23) | `arxiv-1406.4088v2` |
| Walker-Loud, Carlson, Miller 2012, Cottingham | (+2.53(40) lattice input) | −1.30(03)(47) (elastic −1.39(02)) | | `arxiv-1210.7777v1` |
| Gasser, Leutwyler 1975 Cottingham | | −0.76(30) | | cited in `arxiv-1210.7777v1` |
| Gasser, Leutwyler, Rusetsky 2020, Compton sum rule | +1.87(16) | −0.58(16) | | `arxiv-2008.05806v2` |

(Signs converted to n − p; the papers quote p − n.) Two facts are common to all of them:
the splitting is a **difference of two terms of opposite sign**, a strong one (`m_d > m_u` makes
the neutron heavier, ≈ +2.0 to +2.5 MeV, i.e. 2.0–2.7 × 10⁻³ of m_N) and an electromagnetic one
(the proton's charge makes it heavier, ≈ −0.6 to −1.3 MeV, i.e. 0.6–1.4 × 10⁻³). And both
**vanish in the isospin limit** `m_u = m_d`, `α = 0`, where `m_n = m_p` exactly.

## 2. Where each piece of this compute sits against that split

**(a) The proton side is not the source.** Muon pin: m_p = 938.271861 MeV, −243.86 ppb. The
calibration error propagated from σ(m_μ/m_e) = 22 ppb is 25.7 ppb (sensitivity
d ln m_p / d ln(m_μ/m_e) = 1.155), so this is the known 9.5σ μ–p tension. It is 5600× smaller
than the n–p gap (1376.5 ppm of m_n).

**(b) N0 (m_n = m_p) is exactly the isospin limit.** The functional is `u ↔ d` symmetric
(`wholeTrace_reflect`) and the two-term connected part is 0. In literature terms it contains
neither the QCD term nor the QED term, so its −1.2933 MeV miss is the whole of both. This is not
a numerical error in the compute; it is the absence of both isospin-breaking sources.

**(c) A consequence that the literature makes sharp: the identity hits the wrong mass.** An
isospin-symmetric functional should land near the isospin-symmetric nucleon mass, which to first
order in the breaking is the doublet average (m_p + m_n)/2 = 938.9188 MeV. The identity lands on
m_p to 0.24 ppm instead. The offset is (m_p+m_n)/2 − m_p = 0.6467 MeV = **1.2655 m_e**. So, if the
identity is the isospin-limit mass, a proton-specific −1.27 m_e is sitting inside the constant −12
(or the scale). The "−12" is owned by sibling item 3; this is passed to it as a measured
constraint, not a correction.

**(d) The framework's u/d asymmetry is too large by an order of magnitude.** The only place u and
d differ in this compute is the T³ weight `K = q^{±1}` and the crossing structure. The sizes it
produces, against the literature's breaking fractions:

| quantity | size | vs (m_n−m_p)/m_n = 1.3765 × 10⁻³ |
|---|---|---|
| N1 own-sector ratio, 1 − q⁻² | 0.1883 (neutron lighter) | ×137, wrong sign |
| L-B selected word, h²/(1−h²), h = q − q⁻¹ | 0.04570 (neutron heavier) | ×33, right sign |
| BMW QCD part alone | 2.68 × 10⁻³ | ×1.95 |
| BMW QED part alone | −1.06 × 10⁻³ | ×−0.77 |

In QCD the strong breaking is first order in (m_d − m_u)/Λ ≈ 2.5 MeV / m_N. Here the breaking
enters through q itself (2 ln q = 0.209, h² = 0.0437), with no separate small parameter for
m_d − m_u. The flavour grading is the same q that sets the masses, so any reading that lets K or a
u–d crossing see the state gives a splitting of order q − 1 or h², 30–140× too big. A
neutron-heavier result of the right size needs a breaking parameter of order 10⁻³ that the
current objects do not contain. (h⁴ = 1.91 × 10⁻³ is of that order; that is an observation of
magnitude only, not a derivation, and nothing here proposes it.)

**(e) The two-term trace removes exactly the term that carries the EM splitting.** On a
nucleon, the pair charge Σ_{i<j} Q_iQ_j is a scalar on each weight space: 0 on uud, −1/3 on udd.
The ruled (connected) two-term trace subtracts that scalar, so it is 0 for both nucleons
(`pairSum_eq_of_total_eq`; four strands `twoTerm_connected_zero`). In the Cottingham analysis the
dominant EM piece is the elastic (Born) term, ≈ −1.39 MeV (WLCM 2012), which is set by the nucleon
charge form factors, i.e. by the total charge squared Q_N² = ΣQ_i² + 2Σ_{i<j}Q_iQ_j (p 1, n 0). That
is the scalar part the connected trace removes. The corpus already proves the raw part has the
literature's sign: with a repulsive like-charge coupling w_N > 0, s_q ≥ 0 the neutron comes out
lighter (`PairwiseChargeEnergyBeta.nucleon_em_split_neg`, split −w_N/3 − s_q/3). So the EM half of
the literature split is not missing from the algebra; it is removed by the connected subtraction,
and its coupling w_N (c_em) is not derived. Whether the ruled two-term trace should keep the
scalar charge part for an EM self-energy is a question for the owner; nothing is changed here.

**(f) L-C is a structural mismatch, not a size error.** The convention-D trace multiplies over a
split union (tr_D(σ₀σ₁σ₀) = 0.691), masses add. Nothing in the literature corresponds.

## 3. Summary of the error, term by term

| literature term (n − p) | this compute | status |
|---|---|---|
| QCD, m_d − m_u: ≈ +1.9 to +2.5 MeV | no quark-mass parameter; K/crossing asymmetry gives 30–140× too much | missing as a separate small parameter |
| QED, mainly elastic: ≈ −0.6 to −1.3 MeV | present in the raw two-term part with the right sign; removed by the connected subtraction; coupling not derived | removed by a ruling, size underived |
| isospin-symmetric mass ≈ (m_p+m_n)/2 | identity gives m_p to 0.24 ppm; 1.27 m_e offset sits in the −12 | constant carries a proton-specific piece |
| proton calibration | −244 ppb, 9.5σ μ–p tension | not the source (5600× smaller) |

Every derivable term in these arms is included; the two terms above that are absent (a
m_d − m_u parameter and c_em) are absent because nothing in the corpus derives them.
