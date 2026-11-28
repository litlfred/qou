# The Coulomb term ledger on the ring-valued mass (gap G3, ranks 0, 1, 2)

Date: 2026-11-27. Bean: `qou-tcl3` (under `qou-s028`, accuracy epic `qou-myts`).
Lean: `QOU/Nuclear/CoulombRingLedger.lean` (generic field, no measured value).
Builds on: `QOU/Nuclear/CoulombIsospinChannel.lean` and
`docs/audits/2026-11-27-coulomb-isospin-channel.md` (PR #9691, the charge structure), and the
ring-valued mass `def:mass-identity` (PRs #9789, #9805; binding readings PR #9793).

## 1. Question

PR #9691 derived the EM channel as an *energy*, `ε·Z(Z − 1)/2`, with a scalar pair weight `ε`.
Since then the corpus mass is ring-valued (`m = [2]ⁿ q^{−2w} ∫_A ρ(β)`), and an energy is a
*reading* of a ring element: the log reading `E₀·log` (binding, PR #9793) or the energy
reading `U = −q∂_q log` (PR #9789). Does the Coulomb ledger survive the move to the ring, and
what does the ring change?

## 2. Result

Put the EM channel on the ring as one factor `μ` per proton pair, `m = m_s · μ^{C(Z,2)}`, and
call any map with `ρ(xy) = ρx + ρy`, `ρ1 = 0` a reading. Both corpus readings are readings
(`log`; and `logDer_mul` proves it for `−q∂_q log` from the Leibniz rule alone).

| ledger entry | value on the ring | Lean |
|---|---|---|
| rank 0 | `ε·A(A − 2)/8` (+ `ε·T(T+1)/6` multiplet piece, owned by G2) | `reading_ledger`, `em_rank_zero` |
| rank 1 | `ε·(A − 1)/2 · T_z` | `reading_ledger` |
| rank 2 | `ε·½ · T_z²` | `reading_ledger` |
| pair weight | `ε = ρ(μ)`, one ring element read by the binding's reading | `reading_ledger` |
| ratios | `b/c = A − 1`, `a/c = A(A − 2)/4`, independent of reading and of `μ` | `reading_ratio_invariant` |
| mirror split | `ρ(μ)·(A − 1)·T_z` | `reading_mirror` |
| two readings | log and energy pair weights are two readings of the same `μ` | `two_readings_one_mu` |

So ranks 0, 1, 2 survive the ring unchanged. The ring changes one thing: `ε` is no longer a free
constant per reading. It is a reading of one ring element `μ`. A binding computed in the log
reading and one computed in the energy reading must use the matching reading of the same `μ`.

## 3. Consequences recorded as conditionals (hypotheses visible)

* **Monomial `μ = q^s`** (a unit of `K[q, q⁻¹]`): the energy reading is `ε = −s`, an integer in
  the electron's unit (`monomial_reading`), and `m(1)` is unchanged (`monomial_at_one`). So a
  monomial EM factor is invisible at `q = 1`, as the γγ bonds are (PR #9793: binding is exactly 0
  at `q = 1` in the energy reading).
* **Quark level:** `9·Q_iQ_j ∈ {4, −2, 1}` (`quark_exponent_integral`). A per-quark-pair ring
  factor `ν^{Q_iQ_j}` is a ring element only when `ν = μ₀⁹`. The internal exponents are `0`
  (uud) and `−3` (udd) in ninths (`internal_exponents`): the `−N/3` self-energy of #9691.
* **Framing:** `[2]^{3A} q^{−2w}` depends only on `3A` and the writhe, and the braid channel is
  rank 0, so the framing correction adds no `T_z` dependence. It cannot stand in for EM.

## 4. What is open (named, not parametrised)

* **Which `μ`.** No corpus ring element is derived for the photon-exchange factor. `ε` remains
  the open scale of #9691 (`r_rms`, beans `qou-mbfv`, `qou-usft`). Nothing here selects `μ`,
  and no measured value is used anywhere.
* **Wiring.** Unchanged from #9691: the mass table carries `E_EM_MeV` on the ruled binding
  only. Nothing new is wired.
* **G2 `T(T+1)`** (bean `qou-tcl2`, held by the owner): cited via `em_rank_zero`, not touched.

Scope: (a). These are exact algebraic statements; no number is compared to data in this doc.
