*Let
$R$ be a commutative ring, $q \in R^{\times}$ a unit,
$h = q - q^{-1}$, and
$[n]_q = q^{n-1} + q^{n-3} + \cdots + q^{-(n-1)}$ the symmetric
q-integer. The following five algebraic identities hold:*

**Muon set** *(canonical for $T(2,5)$, used by `conj:lepton-tower-h-n-plus-1-branching` at $m = 2$):*

$$
3 + h^2 = [3]_q
$$
$$
(2 + h^2) \cdot [2]_q = [4]_q
$$
$$
(3 + h^2) \cdot [4]_q = [3]_q \cdot [2]_q \cdot (2 + h^2)
$$

**Tau set** *(canonical for amphichiral $10_{43}$ candidate, used by `conj:lepton-tower-h-n-plus-1-branching` at $m = 3$):*

$$
[6]_q = [2]_q \cdot [3]_q \cdot (1 + h^2)
$$
$$
[5]_q \cdot [3]_q \cdot [2]_q \cdot (1 + h^2) = [5]_q \cdot [6]_q
$$

*Whenever $R$ is in addition a field and the relevant denominators are
nonzero, the last identity of each set is the cross-multiplied form of
the quotient presentations*
$\frac{3 + h^2}{2 + h^2} = \frac{[3]_q \cdot [2]_q}{[4]_q}$ *and*
$\frac{[5]_q \cdot [3]_q}{[6]_q} = \frac{[5]_q}{[2]_q \cdot (1 + h^2)}$.

## Lean

All five identities are proved in
[`three-halves-structural-factor.lean`](three-halves-structural-factor.lean)
over a generic commutative ring `[CommRing R]` with the modulus carried
as a unit `q : Units R`, each by a single `linear_combination` against
`↑q * ↑q⁻¹ = 1` — no `field_simp`, no division, no ordering. A field is
used only in the `RatioForm` section, where the two quotient
presentations are recovered from the cross-multiplied identities by
`div_eq_div_iff`. Generic-ring proofs apply at the substrate
$q_0 \approx 1.110$ by specialisation; numerical cross-checks at
50-dps mpmath verify each identity to $\leq 10^{-40}$ in the
[`tau-amphichiral-sdp-probe.witness.json`](../../../computations/probes/tau-amphichiral-sdp-probe.witness.json)
witness (assertions `lean_three_plus_h_sq_eq_bracket3`,
`lean_two_plus_h_sq_times_bracket2_eq_bracket4`,
`lean_bracket6_eq_bracket2_bracket3_times_one_plus_h_sq`).

## Role in the framework

The structural identities reveal that the canonical lepton-tower
closure factors $\xi_m$ live in a single $h$-graded family of
$q$-bracket products. Concretely:

- **Muon** ($m = 2$, $K_\mu = 4_1$): closure factor
  $\xi_2 = [3]_q \cdot [2]_q / [4]_q = (3+h^2)/(2+h^2)$ — closes
  $m_\mu/m_e$ via $\mathrm{Vol}(4_1)/\hbar_q^2$ to 0.034 % of CODATA.
- **Tau** ($m = 3$, $K_\tau = 10_{43}$ candidate): closure factor
  $\xi_3 = [5]_q \cdot [3]_q / [6]_q$ — closes $m_\tau/m_e$ via
  $\mathrm{Vol}(10_{43})/\hbar_q^2$ to +0.79 % of CODATA. The reduction
  $[6]_q = [2]_q \cdot [3]_q \cdot (1 + h^2)$ is the fundamental
  identity behind this closure.

The generic family is the subject of
`conj:lepton-tower-h-n-plus-1-branching`; this proposition supplies
the proved algebraic core for the muon (m=2) and tau (m=3) cases.
