# Composite β⁻ sign: what actually makes 1,009 of 1,010 rows wrong (2026-11-27)

Accuracy epic `qou-myts`, vector 8. Filed against `qou-wxhi` / `qou-cds1`, which
turn out not to be the cause.

## Claim

The accuracy scorecard's Table 3.4b (`scripts/generate-accuracy-scorecard.py:793-805`)
predicts 0 of 1,009 composite β⁻ decays exothermic. **The c_k ladder plays no part in it.**
Table 3.4b computes `Q = M(Z,N) − M(Z+1,N−1) − m_e` from
`computations/mass-table-comprehensive.witness.json`, and every one of the 1,009
rows gives the **same** value, −1.793042 MeV (equal to within the witness's 6-decimal
rounding), whatever Z and A are.

Probe: `computations/probes/composite_beta_sign_decomposition_probe.py`, 8/8, mpmath.
The number splits exactly into four parts for each n → p swap:

| piece | MeV | what it is |
|---|---|---|
| (m_n − m_p) predicted | +0.836433 | the nucleon split (same input as the free neutron) |
| − m_e | −0.510999 | |
| − self term | −0.555678 | `α·ln(V_p/V_n)`: the Q-CLT proxy has no free baseline, so a lone p "binds" −0.5095 and a lone n +0.0462 MeV |
| − bond term | −1.562798 | `α·ln(f_pp/f_nn)`, with f_pp = z_D and f_nn = z_D − h. The 1-D chain p…p n…n swaps one nn bond for one pp bond each time |
| **sum** | **−1.793042** | matches the witness to 1e-6 |

Here α = m_e·8·Catalan = 3.7445 MeV is the proxy's scale.

## What each piece means

* **Self term.** This is a departure from the ruled binding law (owner ruling
  2026-11-25: `B = E₀·log(tr_free/tr_atom)`), not physics. The mass table's
  `try_binding_q_clt_proxy` and `try_binding_symbolic_log_trace`
  (`computations/mass_table_comprehensive.py:390-465`) compute `−α·Σ ln|V|` on the
  atom alone, so nucleon self-energy is counted a second time inside B, on top of
  m_n − m_p already in the unbound mass.
* **Bond term.** This is the T_z-odd slope of the bond channel. It is already proved
  structural: `QOU.MassTheory.BondChannelTzParity` (the bond layer is charge-symmetric
  iff h = 0) and `QOU.MassTheory.PairIsospinAssignment` (C(f_pp) = −f_nn). Bean `qou-1pig`.
  The charge-product repair `qou-nial` was priced there and lost.
* **Free neutron −58 %.** Q(n) = 0.3254 MeV is exactly (m_n − m_p)_pred − m_e. That is
  the nucleon-split front (brief C1), and the c_k ladder is not involved there either.
  Production wires only c₂.

## Repairs, priced (reported, none selected against AME)

| | Q per swap | exothermic rows |
|---|---|---|
| R0 as is | −1.793 MeV | 0 / 1009 |
| R1 ruled free-baseline subtraction | −1.237 MeV | 0 / 1009 |
| R2 R1 + the T_z-even part of the bond (strong channel only) | +0.325 MeV | 1009 / 1009, but the same Q for every nucleus |

R2 fixes the sign and still carries no nuclear information. Dependence on Z and A has to
come from the Coulomb, T(T+1) and flavour terms that sibling threads own. Under R0 or R1,
any term they add is measured against a −1.24 to −1.79 MeV offset per swap that has
nothing to do with their term.

## Scope

Scope (a): this is a statement about this construction. No empirical value enters any
assertion except the check against the committed witness.
