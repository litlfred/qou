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

## Why is binding dressed by the proton net coefficient? (answered — it is ONE gap with the Q-value)

`net(p)` is the **unweighted single-wrap normal-form net coefficient** of
the proton's typed-crossing word in $H_3(q)$ — and it is already *derived*,
not postulated: the typed-crossing operators
[`def:typed-crossing-operator`](../../content/quantum-observable-universe/particle-interactions/typed-crossing-operator.md)
$C(u,u)=\sigma$, $C(d,d)=\sigma-h$ (Hecke $\sigma^{-1}$),
$C(u,d)=\sigma-\tfrac{h}{2}$ (the u↔d-swap-forced mean) reduce the proton
word $\sigma_0(\sigma_1-\tfrac{h}{2})$ to NF with identity/$\gamma$
coefficient $\mathrm{net}(p)=1-\tfrac{h}{2}$ (compute witness
`computations/nf-qvalues.witness.json`).

So the deuteron binding dressing is *not* a free choice — but neither is it
fully derived. This proposition's identity `B_D = E₀·net(p)·Δtr = Q_β·Δtr/h`
shows the binding dressing `net(p)` is the **bar-even image of the exact same
object as the $Q$-value** $Q_\beta = |\Delta(\mathrm{net})|·E_0
= h·\mathrm{net}(p)·E_0$. And that $Q$-value relation
$Q_\beta = |\Delta(\mathrm{net})|·E_0$ **is the known open core of
`conj:borromean-quark`** — its "energy-scale ansatz" (Step 8 of
[`docs/audits/2026-05-24-q-beta-net-ansatz-fitting-finding.md`](2026-05-24-q-beta-net-ansatz-fitting-finding.md)),
postulated "by construction" and *not yet derived* from the canonical
per-braid mass tower [`prop:per-braid-mass-tower`](../../content/quantum-observable-universe/braids-and-knots/per-braid-mass-tower.md).

**Therefore "why is binding dressed by net(p)?" is the same open question as
"why $Q_\beta = |\Delta(\mathrm{net})|·E_0$?"** — the unweighted-NF-net ↔
leading-order-energy identification (Step 6/8 of the borromean-quark
closure). One gap, two faces (bar-even binding / bar-odd decay). Note the
hybrid: `B_D = E₀·net(p)·Δtr` carries BOTH the *unweighted* net(p) dressing
and the *Markov-weighted* trace difference Δtr — the Step-6 "unweighted net
vs weighted trace" tension is exactly this mixing.

## How close is `conj:borromean-quark`? (Tier A — discrete identification)

Closure-distance (from the keystone survey +
[`2026-05-09-conjecture-closure-tractability.md`](2026-05-09-conjecture-closure-tractability.md), Tier A):

- **Nearly hypothesis-free already:** the net coefficients
  $\mathrm{net}(p), \mathrm{net}(n)$ are derived (typed-crossing + exact
  Hecke NF + witness); promoting them from `[BorromeanQuark]` class *fields*
  to Lean *lemmas* is ~1 mechanical reduction lemma, no new mathematics.
- **The genuine residual is the energy-scale ansatz (Step 8, Path A):**
  derive $Q_\beta = |\Delta(\mathrm{net})|·E_0$ (equivalently, via this
  proposition, $B_D = E_0·\mathrm{net}(p)·\Delta\mathrm{tr}$) as the
  leading-order $h$-expansion of the per-braid mass tower:
  $\mathfrak m(n) - \mathfrak m(p) - m_e = |\Delta\mathrm{net}|·E_0 + O(h^3)$.
  **Unexecuted.** Closing it closes *both* the $Q$-value and this binding
  dressing.
- **Plus** the un-Lean-able physical identifications (confinement from the
  Brunnian property, up/down = braid-exponent sign, $T(2,n)$ fermion/boson
  split) — motivated, outside Lean scope.

**Doc-hygiene flag (not fixed here — keystone block, judgment call):** the
conjecture block's `lean.ref` points at `QOU.Archimedean.BorromeanQuark`,
whose instance is discharged *definitionally* (hollow — `volume_calibrates_mass`
closes by `rfl`). The genuinely-conjectural content (net coefficients + $Q$-value
ansatz, no instance) lives in the sibling `QOU.ParticleInteractions.BorromeanQuark`
that this PR's Lean actually consumes. A reader of only the referenced file
would wrongly conclude the conjecture is closed. Worth re-pointing the
`lean.ref` (or splitting the block) — flagged for the owner.

## Path A attempted — REFUTED at leading order (the obstruction is the Markov weight z)

Producer:
[`probes/probe_path_a_net_vs_trm_leading_order.py`](../../computations/probes/probe_path_a_net_vs_trm_leading_order.py)
→ `probes/probe-path-a-net-vs-trm-leading-order.witness.json` (audit-only).

Path A hoped to *derive* the energy-scale ansatz
$Q_\beta = |\Delta(\mathrm{net})|·E_0$ (equivalently $B_D = E_0·\mathrm{net}(p)·\Delta\mathrm{tr}$)
as the leading-order $h$-expansion of the per-braid mass tower — i.e. that the
unweighted **net** (counit $\varepsilon$: every NF basis element weight 1)
equals the mass functional's **Markov trace** $\mathrm{tr}_M$ (the $z$-weighted
sum) at leading order. **It does not.** Computing both on the exact nucleon
single-wrap $\Delta(\mathrm{NF}) = (h^2/2)\gamma - (h/2)\sigma_0 - (h/2)\sigma_1$
(sqrt-free rational $H_3$ reps, braid+Hecke verified):

$$
\frac{\Delta(\mathrm{tr}_M)}{\Delta(\mathrm{net})} \;\xrightarrow{\;h\to 0\;}\; \tfrac12 \;=\; z\big|_{q\to1}, \qquad z=\frac{1}{\sqrt q+1/\sqrt q}.
$$

So net and $\mathrm{tr}_M$ differ by exactly the Markov weight $z\approx 0.489$
**at O(1), not O(h)** — this is a *scope-(a)* refutation of the naive Path A.
The energy-scale ansatz's use of the **counit** $\varepsilon$ (giving net) in
place of the Markov trace is therefore a genuine **structural functional
choice**, not a leading-order coincidence of the mass tower. (This confirms
and quantifies the note in
[`prop:neutron-qvalue-symbolic`](../../content/quantum-observable-universe/particle-interactions/neutron-qvalue-symbolic.md):
"the counit $\varepsilon$ used here versus the Markov trace $\mathrm{tr}_M$ of
the mass formula" — Form A/Form B differ by the $z$ normalization.)

**Reframed wiring gate (borromean-quark Step 8 / Step 6).** Closing the ansatz
is NOT an $h$-expansion of the mass tower. The real open question is
**why the $\beta$-decay / binding channel augments (counit $\varepsilon$)
rather than Markov-traces** — i.e. a derivation that the observable in this
channel is the augmentation of the NF element, not its Jones–Markov trace.
Until that functional choice is derived, both the neutron $Q$-value and the
`+0.12%` D binding dressing remain observation-tier (conditional on
`conj:borromean-quark`). The naive mass-tower-expansion route is closed
(refuted); future work should target the counit-vs-trace functional selection,
not the $h$-expansion.

Note this also explains the **hybrid** structure of $B_D = E_0·\mathrm{net}(p)·\Delta\mathrm{tr}$
flagged above: it carries the counit net(p) *and* the Markov $\Delta\mathrm{tr}$
— two functionals that differ by $z$ — which is precisely why it is a
near-match rather than a clean single-functional derivation.
