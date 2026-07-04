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
= h·\mathrm{net}(p)·E_0$. And that $Q$-value relation is **already derived,
not open** (corpus-grep — see the "Path A" section below):
[`prop:qbeta-counit-transition`](../../content/quantum-observable-universe/particle-interactions/qbeta-counit-transition.md)
derives the counit $\varepsilon$ as the *transition/reduction* observable
(Frobenius pairing against the canonical integral $\omega=G^{-1}\mathbf1$),
vs the Markov trace $\mathrm{tr}_M$ (pairing against $\mathbf1$) as the *loop/
mass* observable. A $\beta$-decay is a transition ⇒ counit.

**Therefore "why is binding dressed by net(p)?" has the same answer as
"why $Q_\beta$ uses the counit"** — because the bar-even binding channel, like
$\beta$-decay, reads the *reduction* content (counit), not the closed-loop
invariant ($\mathrm{tr}_M$). One derived answer, two faces (bar-even binding /
bar-odd decay). The residual open item is *not* the functional selection but
the **tower convergence** `conj:qbeta-trace-counit-convergence` (below). Note
the hybrid: `B_D = E₀·net(p)·Δtr` carries BOTH the counit net(p) dressing and
the Markov $\Delta\mathrm{tr}$ of the deuteron — the two functionals whose
$N{=}0$ ratio is $z$ per `prop:qbeta-counit-closed-form`.

## How close is `conj:borromean-quark`? (Tier A — discrete identification)

Closure-distance (from the keystone survey +
[`2026-05-09-conjecture-closure-tractability.md`](2026-05-09-conjecture-closure-tractability.md), Tier A):

- **Nearly hypothesis-free already:** the net coefficients
  $\mathrm{net}(p), \mathrm{net}(n)$ are derived (typed-crossing + exact
  Hecke NF + witness); promoting them from `[BorromeanQuark]` class *fields*
  to Lean *lemmas* is ~1 mechanical reduction lemma, no new mathematics.
- **The energy-scale ansatz is DERIVED, not open** (corpus-grep correction):
  the counit/trace functional selection is
  [`prop:qbeta-counit-transition`](../../content/quantum-observable-universe/particle-interactions/qbeta-counit-transition.md)
  and the closed form + gap are Lean-proved
  ([`prop:qbeta-counit-closed-form`](../../content/quantum-observable-universe/particle-interactions/qbeta-counit-closed-form.md),
  `QOU.Interactions.QBetaEnergyScale` / `QBetaCounitTrace` / `QBetaTowerBound`,
  sorry-free). The **one** genuine research-grade residual here is the
  *non-perturbative* **tower-convergence conjecture**
  `conj:qbeta-trace-counit-convergence`: that the tower-summed *trace* mass
  difference converges to $\varepsilon(\Delta)\cdot\mathfrak E_0$ with the
  $+0.17\%$ as its $N{=}0$ remainder.
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

## Path A — the corpus already derives it (corpus-grep correction)

Producer:
[`probes/probe_path_a_net_vs_trm_leading_order.py`](../../computations/probes/probe_path_a_net_vs_trm_leading_order.py)
→ `probes/probe-path-a-net-vs-trm-leading-order.witness.json` (audit-only).

**Correction (corpus-grep, per AGENTS.md STRICT).** An earlier revision of
this section framed "Path A" (derive the energy-scale ansatz by expanding the
mass tower) as a *novel refutation* and declared the counit-vs-trace functional
selection an *open question*. **Both are wrong** — the corpus already settles
this, Lean-verified. The corpus-grep I should have run first turns up:

- [`prop:qbeta-counit-closed-form`](../../content/quantum-observable-universe/particle-interactions/qbeta-counit-closed-form.md)
  (**Lean, sorry-free** — `QOU.Interactions.QBetaEnergyScale.Qbeta_closed`,
  `QOU.Interactions.QBetaCounitTrace`): proves exactly
  $\varepsilon(\Delta) = h^2/2 - h$, $\mathrm{tr}_M(\Delta) = h^2/2 - hz$, gap
  $h(z-1)$, equal iff $z=1$, and $z \le \tfrac12$ on the substrate.
- [`prop:qbeta-counit-transition`](../../content/quantum-observable-universe/particle-interactions/qbeta-counit-transition.md):
  **derives the functional selection** — both functionals are Frobenius
  pairings $\langle\cdot,\cdot\rangle_G = \mathrm{tr}_M(\cdot\,\cdot)$ against
  different distinguished elements: $\mathrm{tr}_M(\beta)=\langle\beta,\mathbf1\rangle$
  (closed loop → static **mass**), $\varepsilon(\beta)=\langle\beta,\omega\rangle$
  with $\omega=G^{-1}\mathbf1$ the canonical integral (crossing-stripped →
  net reduction → **decay/transition**). A $\beta$-decay is a *transition*
  (braid reduction, one crossing re-typed $d\to u$), so the counit is the
  natural observable — not a postulate.
- `QOU.Interactions.QBetaTowerBound` (**Lean, sorry-free**): `counit_lt_trace`,
  `trace_neg`, **`counit_dominates`** ($|\varepsilon(\Delta)| > |\mathrm{tr}_M(\Delta)|$),
  `E0_tower_gap`, residual monotonicity.

So my probe **rediscovered a Lean-proved result**. Its residual value is only
as an *independent cross-check via a different route*: I computed
$\mathrm{tr}_M(\Delta) = h^2/2 - hz$ from the **Wedderburn representation sum**
$\sum_\lambda y_\lambda \chi^\lambda$ (sqrt-free rational $H_3$ reps), whereas
the corpus prop derives it from the direct NF Markov weights — the two routes
agree, and $\Delta\mathrm{tr}_M/\Delta\mathrm{net} \to z$ confirms the corpus's
"falls short by a factor of two." That is the whole (modest) contribution; the
functional selection was **not** an open question.

**The genuinely open item is narrower and already named:**
`conj:qbeta-trace-counit-convergence` — the *non-perturbative* claim that the
tower-summed **trace** mass difference $\mathfrak m(n)-\mathfrak m(p)-m_e$
converges to $\varepsilon(\Delta)\cdot\mathfrak E_0$ (the counit form) with the
$+0.17\%$ as the $N{=}0$ remainder. The `QBetaTowerBound` lemmas are "the
provable frontier around" that conjecture; the convergence itself is the
research-grade open core. My leading-order $z$ result is one boundary data
point for it (the $N{=}0$ ratio), nothing more.

**Consequence for the deuteron dressing.** The functional selection that
justifies $\varepsilon$ (net) for the $Q$-value carries over to the bar-even
binding channel by the exact identity of this proposition
($B_D = E_0\,\mathrm{net}(p)\,\Delta\mathrm{tr} = \mathfrak Q_\beta\,\Delta\mathrm{tr}/h$).
So "why is binding dressed by net(p)?" inherits the *same* answer as the
$Q$-value (counit = transition/reduction observable, Frobenius-derived), and
the *same* residual open item (the tower-convergence conjecture). The hybrid
$E_0\,\mathrm{net}(p)\,\Delta\mathrm{tr}$ mixes the counit net(p) with the
Markov $\Delta\mathrm{tr}$ of the deuteron — consistent with, and now located
against, the counit/trace theory above.

## Deuteron Δ_λ term structure (2026-07-04, owner question)

Producer: [`probes/probe_d_delta_lambda_terms.py`](../../computations/probes/probe_d_delta_lambda_terms.py)
→ `probes/probe-d-delta-lambda-terms.witness.json` (audit-only). Reads the
committed 50-dps deuteron χ witnesses (bound / free / q⁻¹) — no re-derivation.

The binding formula is $B(K) = m_e\sum_{\lambda\vdash 6} y_\lambda(q)\,\chi^\lambda(\beta_K)\,\Delta_\lambda(K)$.
**What terms are involved** (β_D word length L = 23, tr_M(β_D) = 0.38836):
11 partitions of 6, each a product $y_\lambda\cdot\chi^\lambda(\beta_D)$ (both
exact Laurent in q). The binding trace difference $\sum_\lambda y_\lambda\Delta\chi^\lambda = 0.59517$
(= the #3295 Δtr), **dominated by three blocks**: $[4,2]$ (0.295), $[5,1]$
(0.160), and the self-conjugate $[3,2,1]$ (0.070) — two-row + hook + the SDP
self-dual fixed point. The high-row partitions ($[2^3]$, $[1^6]$, …) contribute
< 1 %.

**Symbolic relations that hold (exact / near):**

1. **Wedderburn closure** $\sum_\lambda y_\lambda\chi^\lambda(\beta_D) = \mathrm{tr}_M(\beta_D)$
   — exact (residual 4.8e-52). This is the scalar the collapse-last towers
   reproduce; it is the ONE hard constraint on any $\Delta_\lambda$.
2. **Bar-conjugate law is BROKEN by ≈2.6e-4.** $\chi^\lambda(\beta_D, q^{-1})$
   vs $(-1)^L\chi^{\lambda'}(\beta_D, q)$ (L = 23, sign $-1$) has max rel-resid
   **2.63e-4** — NOT exact. The break is the **colour-weighted p-n interface**
   (q₀-baked flavor split), at the same order as the convention-D trace gap
   (1.955e-4). So the clean q↔q⁻¹ / conjugate-partition symmetry that holds for
   an unweighted word is deliberately broken at the flavor-split scale; any
   $\Delta_\lambda$ closure inherits this asymmetry.
3. **No χ zeros at H_6** (unlike the H_3 Garside $\chi^{(2,1)}(\Delta)=0$): all
   11 $\chi^\lambda(\beta_D)$ are non-vanishing, so there is no "free" block to
   drop.
4. **(3,2,1) self-conjugate fixed point** carries the 3rd-largest binding term
   — the SDP self-dual block is a genuine load-bearing contributor, not a
   spectator.

**Δ_λ magnitude — under-determined at A=2 (quantified).** The binding is ONE
scalar equation $\sum_\lambda y_\lambda\chi^\lambda\Delta_\lambda = B_{AME}/m_e = 4.3534$
against **11 per-λ unknowns** ⇒ a **10-dimensional null space**. A *uniform*
$\Delta_\lambda = \delta$ has magnitude $\delta = (B_{AME}/m_e)/\mathrm{tr}_M = 11.21$
(direct form); the trace-canonical difference form gives the scalar Δtr =
0.595. **No unique symbolic $\Delta_\lambda(D)$ exists from deuteron data
alone** (confirms `probe_d_symbolic_prospects` P3). The relations above are the
constraints a closure must respect — Wedderburn-exact, colour-broken
bar-conjugate, dominant blocks $[4,2]/[5,1]/[3,2,1]$ — but they do not pin the
10 free directions; that requires cross-A (per PR #3266's cross-A
discriminator). **Not a closure ansatz** (Δ_λ gate); a structural map of the
terms and their exact constraints.
