**Proposition (lepton-tower closure structural identities).** *Let
$R$ be a field, $q \in R$ with $q \neq 0$, $h = q - q^{-1}$, and
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
\frac{3 + h^2}{2 + h^2} = \frac{[3]_q \cdot [2]_q}{[4]_q}
$$

**Tau set** *(canonical for amphichiral $10_{43}$ candidate, used by `conj:lepton-tower-h-n-plus-1-branching` at $m = 3$):*

$$
[6]_q = [2]_q \cdot [3]_q \cdot (1 + h^2)
$$
$$
\frac{[5]_q \cdot [3]_q}{[6]_q} = \frac{[5]_q}{[2]_q \cdot (1 + h^2)}
$$

## Lean

All five identities are proved in
[`three-halves-structural-factor.lean`](three-halves-structural-factor.lean)
over generic `[Field R]` per AGENTS.md §7c, using
`field_simp; ring`. Generic-ring proofs apply at the substrate
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
  $m_\mu/m_e$ via $\mathrm{Vol}(4_1)/\hbar_q^2$ to 0.034 % of CODATA
  (`docs/audits/-lepton-bring-surface-h3-3channel-convention.md`).
- **Tau** ($m = 3$, $K_\tau = 10_{43}$ candidate): closure factor
  $\xi_3 = [5]_q \cdot [3]_q / [6]_q$ — closes $m_\tau/m_e$ via
  $\mathrm{Vol}(10_{43})/\hbar_q^2$ to +0.79 % of CODATA
  (`docs/audits/-t6-f-ell-derivation-attempt.md`
  followup section). The reduction
  $[6]_q = [2]_q \cdot [3]_q \cdot (1 + h^2)$ is the fundamental
  identity behind this closure.

The generic family is the subject of
`conj:lepton-tower-h-n-plus-1-branching`; this proposition supplies
the proved algebraic core for the muon (m=2) and tau (m=3) cases.
