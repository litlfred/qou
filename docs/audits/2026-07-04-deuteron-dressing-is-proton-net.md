# 2026-07-04 — The deuteron (1−h/2) binding dressing IS the proton NF net coefficient

**Date:** 2026-07-04 · **Branch:** `claude/deuteron-1h2-dressing-derivation-2026-07-04` · **Bean:** `989t`

## Context

Follow-through on the owner request "improve D" → option #1 (derive the
`(1−h/2)` binding dressing). The prior session
([deuteron from-scratch ledger, PR #3266, merged](https://github.com/litlfred/qou/pull/3266))
established the exact reduction `Q_β = E₀·h·(2−h)/2` in ℚ(q) and the
observation that `B_D = E₀·(1−h/2)·Δtr` lands `+0.12%` of AME2020 with no
fit — but left the `(1−h/2)` factor unexplained (observation-tier, unwired).

## Result — the dressing is not a new object

The `(1−h/2)` is **exactly `net(p)`**, the proton `[u,u,d]` single-wrap
normal-form net coefficient in `H_3(q)` already carried by
[`conj:borromean-quark`](../../content/quantum-observable-universe/observations/borromean-quark.md)
(the same conjecture the neutron `Q`-value
[`prop:neutron-qvalue-symbolic`](../../content/quantum-observable-universe/particle-interactions/neutron-qvalue-symbolic.md)
already assumes). The load-bearing algebra, all exact in the field:

| identity | form |
|---|---|
| `Δ(net) = net(n) − net(p)` | `= −h·net(p)` (division-free) |
| `\|Δ(net)\|` | `= h·net(p)` (0 < h < 2) |
| `Q_β = \|Δ(net)\|·E₀` | `= E₀·h·net(p)` |
| **binding dressing** | `E₀·net(p)·Δtr = Q_β·Δtr/h` |

So the **bar-even binding dressing `net(p)`** and the **bar-odd `Q`-value
`Q_β`** are the same categorical object separated by the single Hecke
factor `h = q − q⁻¹` (itself bar-odd). This is the
[`prop:bar-parity-split`](../../content/quantum-observable-universe/mass-theory/bar-parity-split.md)
read at the deuteron: binding in the bar-even channel, β-decay in the
bar-odd channel, `h` bridging them.

## What this does and does not establish

- **Establishes (Lean, exact):** the three algebraic identities, conditional
  on `conj:borromean-quark` via the `[BorromeanQuark]` class hypothesis
  (`QOU.Mass.DeuteronBindingDressing`, `delta_net_eq_neg_h_net_p` /
  `qbeta_eq_E0_h_net_p` / `binding_dressing_eq_qbeta_over_h`). No new
  conjecture, no fit. This *reduces* the open question "why `(1−h/2)`?" to
  "why is the binding dressed by the proton NF net coefficient?" and ties it
  to the already-conjectured β-decay sector.
- **Does NOT establish:** that the binding functional *must* carry `net(p)`.
  The magnitude match `B_D ≈ E₀·net(p)·Δtr` (`+0.12%`) is observation-tier,
  conditional on `conj:borromean-quark`, and **D-specific** — the cross-A
  discriminator (PR #3266,
  `probe_d_dressing_cross_a`) shows the same dressing leaves A≥3 at
  −59%…−90%, so the extensive A≥3 deficit is a separate mechanism. **Not
  wired; the Δ_λ gate stands.**

## Tiering (per the (a)/(b) discipline)

- Algebraic identities: **exact**, Lean-formalized (conditional class).
- `Q_β(ansatz) = E₀·h·net(p) = 0.78365 MeV` vs Kashiwara production `Q_β
  = 0.78233 MeV`: `+0.17%` — the known CAL-2 cross-check spread.
- `B_D = E₀·net(p)·Δtr`: `+0.29%` (ansatz Q_β) / `+0.12%` (Kashiwara Q_β
  via `Q_β·Δtr/h`) — **observation-tier**, conditional on borromean-quark.

## Artifacts

- Content: [`prop:deuteron-binding-dressing-proton-net`](../../content/quantum-observable-universe/mass-theory/deuteron-binding-dressing-proton-net.md)
  (§3b-cond conditional proposition, `.ts`/`.md`/`.lean`).
- Lean: `content/quantum-observable-universe/lean/QOU/Mass/DeuteronBindingDressing.lean`
  (3 theorems; **hand-audited — Mathlib cache unavailable in this sandbox
  (release server 403, cache branch is QOU-only), CI confirms**. The
  tactics mirror the compiling parent `neutron_qvalue_symbolic.lean`
  bit-for-bit: `rw; ring`, `abs_of_nonpos` + `field_simp`).
- Probe: [`probe_d_dressing_is_proton_net.py`](../../computations/probes/probe_d_dressing_is_proton_net.py)
  → `probe-d-dressing-is-proton-net.witness.json` (audit-only, 2/2;
  `|Δ(net)| = h·net(p)` to 5e-61).

## Next (the wiring gate, unchanged)

Deriving that the binding functional *carries* `net(p)` (not just that it
numerically matches) is the remaining step to wire the `+0.12%` D result.
Candidate route: the single p-n interface of the deuteron chain contributes
its net coefficient to the bar-even binding channel — connect the interface
census (`closed_form_tau_M`) to the net-coefficient sum. Research-grade.
