# 2026-05-22 — Strategy D exploration: λ_scale from canonical 𝓑_p (stage 1)

> **Audience.** A future agent picking up Strategy D for the CAL-4
> closure of the Borromean baryon mass formula. Stage 1 catalogues
> structural inputs, runs four LP/SDP/algebraic probes, and isolates
> the most promising lead. Does NOT close `λ_scale` in closed form —
> stage 2+ remain.
>
> **Per agent brief.**
> [`docs/agent-briefs/2026-05-22-lambda-scale-qdilog-tower-direct.md`](../agent-briefs/2026-05-22-lambda-scale-qdilog-tower-direct.md)
> Strategy D — direct categorical derivation via knot-operator-LP/SDP.
>
> **User constraint (2026-05-22).** "q_0 not special, just where we
> happen to be." Any candidate identity must be SMOOTH IN q across the
> substrate window, not numerically pinned at q_0. The exploration
> script enforces this via a q_0 ± ε locality sweep.

## TL;DR

1. **Leading-order ansatz confirmed.** `λ_scale ≈ 5/2 − h²·G` matches
   the 32-digit closure target at **−5.619 ppm** (`G` = Catalan). This
   is the legacy "5/2 − h²·G + O(h^4)" ansatz already noted in
   [`build_proton_mass_50dps_chain.py:86`](../../computations/build_proton_mass_50dps_chain.py).
2. **Next-order term:** the residual
   `ε := target − (5/2 − h²·G) = −1.3823e-5`
   matches **−h⁶/6 to within 0.66%** at q_0. The 0.66% mismatch is
   above 32-digit precision, so `−h⁶/6` is NOT the exact next-order
   term — a small higher-order correction (~h²/40 magnitude, no clean
   q-rational interpretation found yet) remains.
3. **Direct LP setups (D1, D2, D6) do not yield λ_scale.** The natural
   choices for cost vector (χ_λ, q^{c(λ)}) and Gram (y_λ diagonal)
   produce shadow prices dominated by the negative-χ_(1,1,1) channel
   or by unrelated structural objects. The LP formulation requires
   more structure than the brief sketch suggests — likely a positive
   cost vector + a different net-constraint object.
4. **Frobenius-dual LP (D3) is infeasible** with the natural demand
   vector u = y_λ · χ_λ over the 3-channel partition basis.
5. **Recommended stage 2.** PSLQ at 100 dps against an extended
   basis (`{h^{2k}·G^j·π^l}` for small k,j,l) to identify the exact
   higher-order correction to `5/2 − h²·G`. If a clean q-rational
   form emerges, it closes Migration Backlog #1 even without an LP
   formulation. Strategy D's LP angle is a separate ladder: it should
   be revisited with a positive-cost / SDP variant once the closed
   form is known.

## Structural inputs (at q_0)

Computed via
[`computations/strategy_d_lambda_scale_exploration.py`](../../computations/strategy_d_lambda_scale_exploration.py).

| Object | Value at q_0 (16 sig fig) |
|---|---|
| q_0 | `1.109978595554181` |
| Vol(𝓑_3) / ℏ_q² = R | `746.4178510331172` |
| tr_M^3(𝓑_p, q_0) (structural form T) | `1.065306228592389` |
| χ_(3)(𝓑_p, q_0) | `1.382494514546439` |
| χ_(2,1)(𝓑_p, q_0) | `1.807703320098158` |
| χ_(1,1,1)(𝓑_p, q_0) | `−0.7392235469701227` |
| y_(3)(q_0) | `0.4153957863345665` |
| y_(2,1)(q_0) | `0.2809296339798641` |
| y_(1,1,1)(q_0) | `0.02274494570570528` |
| target λ_scale (32-digit) | `2.4599527843613182892482457339493` |

(The 10-digit literal `2.4599527869` in
[`m_p_borromean_verification_50dps.py`](../../computations/m_p_borromean_verification_50dps.py)
carries only ~10 digits of information. Residuals smaller than 2.5e-9
cannot be probed against it; this exploration uses the 32-digit form
that appears in the bring_bloch_tier{1..5}_search scripts.)

**Note on Markov-trace normalization.** The structural form
`T(B_p, q) = Σ_λ y_λ · χ_λ` evaluated here gives **1.0653...** at
q_0, while the canonical Phase 5l witness
[`rho-constit-equals-tau-M-proton-phase5l.witness.json`](../../computations/rho-constit-equals-tau-M-proton-phase5l.witness.json)
reports tr_M^3(𝓑_p, q_0) = **1.2203628...**. Per
[`tau-M-proton-closed-form-phase5l1.witness.json`](../../computations/tau-M-proton-closed-form-phase5l1.witness.json)
the discrepancy is a normalization difference that "is NOT a simple
q-independent multiplicative constant"; Phase 5l.2 reconciliation
remains queued. **For Strategy D the choice between the two
normalizations changes the LP n_target by a factor ~1.15**, which
may matter for finding the right LP setup. Stage 2 should test
both normalizations.

## Probes

### Probe D1 — 3-channel LP, n_target = R

Setup:
- `t = [χ_(3), χ_(2,1), χ_(1,1,1)](𝓑_p, q_0)` (cost = Hecke characters)
- `G = diag(y_(3), y_(2,1), y_(1,1,1))` (Wedderburn diagonal)
- `n_target = R = Vol(𝓑_3) / ℏ_q² ≈ 746.42`

Result:
- `y_0* = −0.7392` (the negative-χ_(1,1,1) shadow price)
- `primal_obj / R = −0.7392`
- Active set: `[0, 1]` (channels (3) and (2,1), with (1,1,1) saturating)

**Verdict.** Unphysical — LP unbounded below in the negative-χ direction;
shadow price equals `χ_(1,1,1)` by direct inspection of the dual. Not
a structural object that encodes λ_scale.

### Probe D2 — 3-channel LP, n_target = tr_M^3(𝓑_p)

Same as D1 but with `n_target = 1.0653` (the structural Markov
trace at q_0). Same failure mode: `y_0* = −0.7392`, `primal_obj/R
≈ −0.00106`. Not λ_scale.

### Probe D3 — Frobenius-dual LP with demand u = y_λ · χ_λ

Setup uses `solve_frobenius_dual_lp(t, G, n_target=R, u_demand)`
which enforces equality constraints `Σ x_λ = R` and `G x = u`. The
3-variable LP with 4 equality constraints is over-determined and
infeasible. Result: `nan` shadow prices.

**Verdict.** The naïve Frobenius-dual setup is not well-posed.
Stage-2 reformulation: use only the net constraint and drop the
demand vector, OR add slack variables to make the demand
constraint a soft equality.

### Probe D4 — algebraic ratios

Per-ratio inspection of target vs. simple combinations of q,
tr_M, R, χ, h, z. Most striking:

- `target − 5/2 + h²·G = −1.382e-5` — confirms the leading
  `5/2 − h²·G` ansatz to **−5.619 ppm**.

### Probe D5 — residual ε := target − (5/2 − h²·G) at high precision

The residual ε = −1.3823487931e-5 (in fact ε = −5.619 ppm of target).
Per-candidate ratios:

| Higher-order candidate `C` | ε / C |
|---|---|
| `h^6 / 6` | `−0.99343441` |
| `h^6` | `−0.16557240` |
| `h^6 · G` | `−0.18076269` |
| `h^4 · G^2` | `−0.00862527` |
| `h^4 · ζ(2)` | `−0.00439929` |
| `ℏ_q^6` | `−14.61020286` |
| `(h · G)^2` | `−0.00037698` |

**The cleanest lead:** `ε ≈ −h^6 / 6` (Bernoulli `B_2 = 1/6`), with a
**0.66% deviation** that is real at 32-digit precision (the deviation
is 9.1e-8, well above the precision floor).

The 0.66% deviation cannot be cleanly explained by any of the
candidates tested. Possibilities for the structural decomposition:

- `ε = −h^6 / 6 · (1 − h²/40 + O(h^4))` — empirically close
  (deviation matches 1/40·h² to ~1%), but 1/40 has no
  obvious Bernoulli/zeta-function identification.
- `ε = −h^6 / 6 + h^8 · c` for some small c — gives a relative
  contribution of `(h^8 · c) / (h^6/6) = 6 · h² · c`, requiring
  `c ≈ -0.0067/(6·h²) ≈ -0.026`; not obviously clean either.
- The residual is a Faddeev Φ_q / Rogers Li_2^q expression at a
  natural argument — needs PSLQ against a q-dilog basis. This is
  the entry point to Strategy A / B of the brief.

### Probe D6 — LP with q^{c(λ)} cost

Setup:
- `t = [q^3, q^0, q^{-3}]` (q-content cost per partition; per
  [`prop:mass-formula-iterative-lp-dual`](../../content/quantum-observable-universe/braids-and-knots/)
  and the
  [`delta_n2_lp_dual_extraction.py`](../../computations/delta_n2_lp_dual_extraction.py)
  pattern)
- `G = diag(y_λ)`, `n_target = tr_M^3 = 1.0653`

Result:
- `y_0* = 0.7312` (positive, physical)
- `y_0* · R = 545.81` — not λ_scale (target = 2.46)
- Active set `[0, 1]`

**Verdict.** Physical shadow price, but doesn't match λ_scale.
The q-content cost vector encodes the "Δ_n²" mass-shift dual, not
the topological-volume shadow price.

## Q-locality

At q_0 ± 1e-4 and ± 1e-5 (32-digit precision), the structural
inputs R(q) and tr_M^3(𝓑_p, q) vary smoothly. Per the user
constraint, any closed-form λ_scale(q) must inherit this
smoothness — confirmed for the leading `5/2 − h²(q)·G` since `h(q)`
is itself a smooth function of q.

| ε (q − q_0) | R(q) | tr_M^3(𝓑_p, q) |
|---:|---:|---:|
| `−1e-4` | `747.6424` | `1.064648` |
| `−1e-5` | `746.5402` | `1.065240` |
| `0`     | `746.4179` | `1.065306` |
| `+1e-5` | `746.2956` | `1.065372` |
| `+1e-4` | `745.1966` | `1.065965` |

Derivatives: `dR/dq ≈ −12.2 / 1e-4`, `d(tr_M)/dq ≈ 6.6 / 1e-4`.
These can be used to check candidate closed forms against the
q-locality slope (a numerical-coincidence ansatz at q_0 would
generically have the wrong slope).

## Recommended stage 2

In priority order (each is independent of the others):

1. **PSLQ at 100 dps on the ε residual** against the basis
   `{h^k · G^j · π^l · ζ(2k') : k ∈ [4..10], j ∈ [0..2], l ∈ [0..2], k' ∈ [0..2]}`
   — about 60 basis elements. If a clean ℤ-linear combination of
   modest coefficients emerges, that closes Migration Backlog #1
   without needing the LP setup at all. This is the natural
   continuation of probe D5 and overlaps with **Strategy C** of
   the brief.

2. **Test against Li_2^q / Φ_q at natural algebraic arguments**
   (per Strategy A and B of the brief). Use
   [`_li_2_q_util.li_2_q`](../../computations/_li_2_q_util.py)
   and
   [`_phi_q_util.phi_q`](../../computations/_phi_q_util.py).
   Candidate arguments: `{q_0, 1/q_0, q_0², h², h²·G, −h², ...}`.

3. **Symbolic-q LP via KKT.** linprog can't take symbolic inputs,
   but the KKT optimality conditions for the partition-channel LP
   reduce to a small algebraic system in q. Solve symbolically with
   sympy; check whether any KKT solution branch gives a shadow
   price equal to the closed-form λ_scale(q) from stage 2.

4. **PSD-relaxed SDP variant.** Use
   [`solve_psd_operator_selection_sdp`](../../computations/lp_dual_solver.py)
   with the PSD constraint applied to the Hoefsmit (2,1)-block
   submatrix (the only block in the H_3 NF basis with non-trivial
   2×2 structure). The PSD constraint may regularize the
   negative-χ direction that broke D1/D2.

5. **Reconcile the two Markov-trace normalizations.** Per the note
   above, T(𝓑_p, q_0) = 1.0653 vs. canonical tr_M^3 = 1.2204
   differ by a non-q-independent factor. Phase 5l.2 reconciliation
   is queued; closing that resolves which n_target the Strategy D
   LP should use.

## Anti-patterns to avoid (per brief §Anti-patterns)

1. **Do not introduce a 7th-ansatz fit.** PSLQ against an
   exhausted basis is fit-search; only ℤ-linear combinations with
   modest coefficients (|c| ≤ 10²-ish) count as "structural". A
   PSLQ relation with coefficient 10⁸ is a numerical accident.
2. **Do not drop precision.** PSLQ at < 50 dps will produce false
   positives. Stage 2 PSLQ runs should use `mp.dps = 100` minimum.
3. **Do not switch q_0 conventions.** The 50-digit pin in
   [`q-pinning-50-digit.witness.json`](../../computations/q-pinning-50-digit.witness.json)
   is authoritative.

## Cross-references

- [`docs/agent-briefs/2026-05-22-lambda-scale-qdilog-tower-direct.md`](../agent-briefs/2026-05-22-lambda-scale-qdilog-tower-direct.md)
  — Strategy D brief (this exploration's spec)
- [`computations/strategy_d_lambda_scale_exploration.py`](../../computations/strategy_d_lambda_scale_exploration.py)
  — exploration script (this audit's compute)
- [`computations/strategy-d-lambda-scale-exploration.witness.json`](../../computations/strategy-d-lambda-scale-exploration.witness.json)
  — output witness with per-probe data
- [`computations/build_proton_mass_50dps_chain.py:86`](../../computations/build_proton_mass_50dps_chain.py)
  — legacy `5/2 − h²·G` ansatz
- [`computations/m_p_borromean_verification_50dps.py:100`](../../computations/m_p_borromean_verification_50dps.py)
  — production hardcoded literal (`LAMBDA_PROTON_DOC`)
- [`computations/bring_bloch_tier{1..5}_search_m_p.py`](../../computations/)
  — exhausted Bring-Bloch path (Strategy of brief §"Why Bring-Bloch is exhausted")
- [`computations/tau-M-proton-closed-form-phase5l1.witness.json`](../../computations/tau-M-proton-closed-form-phase5l1.witness.json)
  — symbolic closed form for T(𝓑_p, q)
- [`computations/rho-constit-equals-tau-M-proton-phase5l.witness.json`](../../computations/rho-constit-equals-tau-M-proton-phase5l.witness.json)
  — canonical tr_M^3(𝓑_p, q) per Phase 5l
- [`docs/canonical-derivation-cheat-sheet.md`](../canonical-derivation-cheat-sheet.md)
  §5 #1 — Migration Backlog item this work aims to close
- [`prop:lambda-scale-bring-bloch-identity`](../../content/quantum-observable-universe/braids-and-knots/lambda-scale-bring-bloch-identity.md)
  — paper-side block (now exhausted Bring-Bloch path)
- [`conj:borromean-baryon-mass-formula`](../../content/quantum-observable-universe/braids-and-knots/borromean-baryon-mass-formula.md)
  — formula using λ_scale
