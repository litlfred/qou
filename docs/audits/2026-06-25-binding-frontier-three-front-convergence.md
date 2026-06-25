# Binding-frontier: three-front convergence on one owner-gated object (2026-06-25)

**Branch:** `claude/jolly-wright-6kc4d2` · **PR:** #2750 · supersedes nothing
(synthesis of an investigation, not a new claim).

After PR #2734 merged, the author asked to pursue three binding-improvement
fronts in parallel: (1) the A=4 interface operator (Option E PROBE 2),
(2) the Lever-1 fibre kernel `R(q,x)`, (3) the s5-so3 keystone pre-work. This
note records what a thorough corpus investigation found: **every actionable,
non-owner-gated piece of all three fronts is already banked / recorded /
pruned, and all three converge on a single owner-gated object** — the
abelianised λ_SW Cartan-connection holonomy on the coral elliptic curve `E_q`
reproducing `θ = 0.7815` (equivalently `tr B = τ = 2.6424`).

## The convergence (one picture)

```
A=4 interface operator (front 1)         Lever-1 R(q,x) (front 2)
  supplies the BOUNDED piece               supplies the EXTENSIVE piece
  under-binds ⁴He −70.8%, SATURATES        depth-2 R=x²−τx+1, λ₊≈2.185>1
        │                                        │
        │  the missing extensive growth IS ──────┘
        ▼                                        ▼
        └──────────► magnitude set by τ = 2.6424 ◄──────────┐
                              │                              │
                     geometric origin of τ                  │
                              ▼                              │
        s5-so3 keystone (front 3): coral E_q identified,     │
        Picard–Fuchs route pruned ─ open step = abelianised  │
        λ_SW holonomy = θ=0.7815  ── OWNER-GATED ────────────┘
```

## Front 1 — A=4 interface operator: exists, evaluated, structurally bounded

- The multi-nucleon interface operator `Δ_I^K` is implemented for general
  `(Z,N)`: `binding_via_interface_knot.py` (T1+T2+T3 Li₂^q tower) and the
  per-block A-operator `he4_9_3_interface_operator_probe.py` →
  `a4_interface_trace_integration_all.py` (Option E PROBE 2).
- **Recorded evaluation** ([`interface-4body-assembly.witness.json`](../../computations/interface-4body-assembly.witness.json),
  0 free parameters): the interface/many-body-topology binding **under-binds
  ⁴He by −70.8% (chain) / −68.8% (complete)** vs AME 28.296 MeV. The deficit
  **saturates**: ⁴He/D scaling is 2.70–2.89 vs AME **12.72**.
- **Interpretation (scope-(a), per the "before declaring refuted" rule).** The
  interface operator *alone* does not reproduce ⁴He binding — it supplies a
  bounded, saturating contribution (~30% of ⁴He). This is a **scope-limited
  negative**, NOT a structural exclusion: a compositional/trace object is
  already many-body, so "insufficient by itself" says nothing about whether it
  belongs in the multi-term closure. The **missing piece is the extensive
  (∝A) growth**, which is front 2's mechanism, not a tunable factor on the
  interface operator. The Δ_λ "no 7th fit-ansatz" gate forbids closing the 70%
  by fitting a scale.
- **Sandbox note (reproducibility).** A *fresh* A=4 interface run is
  **native-gated** here: `he4_9_3_interface_operator_probe.py` needs
  `pyhecke_native.seminormal_matrices_mpfr`, and the wheel will not build
  because both `tools/pyhecke-native/Cargo.toml` and
  `tools/hecke-engine/Cargo.toml` pin (via `[patch.crates-io]`) the SDP
  backend `github.com/litlfred/Clarabel.rs@9673209`, an unfetchable revision
  in this environment (403 / `revision not found`). Workaround for a
  native-capable session: clarabel is *optional* (behind `clarabel-sdp/-mpfr`,
  off by default), so fully severing it from `hecke-engine` (the optional dep
  + the 3 `clarabel-*` features + the ~11 `required-features` bins) lets the
  seminormal kernel build. Not done here (invasive working-tree edit to
  vendored manifests for a number the corpus already records).
- **Hygiene gap (follow-up).** `a4_interface_trace_integration_all.py` reads
  per-λ traces from an ephemeral `/tmp/a4_trace.log` and emits **no witness**.
  It should call the probe (or read a committed trace) and emit a proper
  `*.witness.json`. Filed as a follow-up; execution is native-gated.

## Front 2 — Lever-1 `R(q,x)`: banked

Resolved in **PR #2718** (2026-06-24, bean `z2bn`), reproduced firsthand this
session via `binding_selection_rule_tau_closure.py`:
- depth-2 kernel `R(q,x) = x² − τx + 1`, `det = 1`;
- τ **algebraically fixed** (no fit) by selection-rule anchors
  `τ = 3(3q⁴+8q²+3)/(4q(q+1)²)`, **τ(q₀) = 2.6423863133015**;
- characteristic roots `λ₊ ≈ 2.1846 > 1`, `λ₋ ≈ 0.4577`; `lambdaPlus_gt_one`
  Lean-proved sorry-free (`BindingRecurrenceSpectral.lean`). **Calibration
  (sibling #2752):** `λ₊` confirms extensivity *qualitatively* but is a
  fixed-τ *seed artifact* — the physical `lw(n)` sequence is **super-geometric**
  (grows faster than `λ₊`), so `λ₊` is a lower bound, not the literal growth
  rate. The qualitative "binding is extensive" conclusion is *reinforced*, not
  weakened.
- Residual open ID: `a_D^(n) = lw(n−1)` geometric↔algebraic (conj #1765) — and
  the geometric origin of τ (below). No new kernel-class search is warranted
  (formalize-first already pruned it: the spectral invariant λ₊(τ)>1 is proved
  and the kernel satisfies it).

## Front 3 — s5-so3 keystone pre-work: curve identified, route pruned

From [`lever1-coral-eq-monodromy-integrality.witness.json`](../../computations/lever1-coral-eq-monodromy-integrality.witness.json)
(probe, no fit) and `docs/audits/2026-06-24-lever1-coral-eq-monodromy-integrality.md`:
- **Curve identified:** coral `E_q` = descartes `E_q`, `j(q₀) ≈ 129.86`;
  classical limit `j(1)=128`, `p(1)=2/3`, `r(1)=20/27` exact.
- **Picard–Fuchs route formalize-first-pruned.** The topological Gauss–Manin
  monodromy of an elliptic family lies in `SL₂(ℤ)` (preserves `H¹(E,ℤ)`) →
  **integer trace**. But `tr B = τ = 2.6424 ∉ ℤ`. Therefore B is **not** the
  topological monodromy — so computing the period monodromy (the keystone
  agent's proposed "b-3") would yield the wrong, integer-trace object. The
  integrality invariant *prunes* that computation before running it.
- **Open step (owner-gated):** B is the abelianised λ_SW Cartan-connection
  holonomy (real/hyperbolic, `τ = 2cosh θ`, `θ ≈ 0.7815`). Computing this
  holonomy at q₀ is the s5-so3 keystone — the narrow Subgoal-2 reversal
  (2026-06-19) covers exactly this geometric build; it is hard DG/WRT.
- The other listed pre-work (S₄-invariant fixed field → algebraic
  `j(Bring/S₄)`) is likewise redundant: `j ≈ 129.86` is already confirmed.

## What this means for "improve binding"

The three fronts are three views of one bottleneck. The bounded piece (front 1)
is maxed (and cannot be honestly pushed further without a banned fit); the
extensive piece (front 2) is banked; the magnitude τ that sets the extensive
piece has its geometric origin in **one owner-gated object** (front 3). So:

- **No non-gated, non-fitting forward step remains on binding *magnitude*.**
- The genuine unlock is the owner-gated keystone holonomy (θ=0.7815 from coral
  `E_q`'s abelianised λ_SW connection). Everything else is done.
- ρ-free *ratios* (Lever 3, bean `thb7`) remain the one parameter-free
  *falsifiable-prediction* avenue (A=3 mirror `B(³H)/B(³He)` ≈ +1.67% banked;
  extending to ⁷Li/⁷Be needs H_21 χ — native-gated for fresh compute).

## Coordination — independent sibling corroboration (2026-06-25 cluster)

This synthesis aggregates a hot, crowded cluster; multiple sibling PRs reached
the same conclusions independently (strong corroboration), and this doc ties
them into one cross-front map:

- **#2755** (`lever1-tau-anchor-closure`) — Lean-formalizes (sorry-free) "wired
  anchors ⇒ τ>2 ⇒ binding kernel extensive" and states the identical
  convergence: all FOCUS levers reduce to the one owner-gated holonomy; the
  period probe is already refuted (integer-trace). This is the **Lean half** of
  front 2 / the prune; this doc is the cross-front **narrative** half.
- **#2752** (`spectral-bridge calibration`) — the λ₊ re-scope absorbed above:
  physical `lw(n)` is super-geometric; `λ₊` is a seed artifact.
- **#2754** (`SDP interface-selection`) — independently confirms front 1: the
  interface operator alone has an irreducible ~2.41× ceiling (scope-(a)); the
  open residual is collective, not the interface.
- **#2749** (`KL-Betti deuteron`) — KL-Betti magnitude is contributive (×2.0)
  but non-closing (scope-(a)); refines the PROBE-4 magnitude claim.

No inconsistency requiring escalation: all four agree on the (a)-scope framing
and the single owner-gated bottleneck. The only correction propagated here is
the λ₊ seed-artifact calibration (#2752).

## Discipline notes

- Interface "doesn't close ⁴He" is recorded as **scope-(a)** (construction
  alone), not a structural exclusion — the interface term is a permanent valid
  contribution to a multi-term closure.
- No fit was made; nothing was wired to production. The τ reproduction and all
  cited residuals are from committed witnesses.
- The native-gate is an *environment* limitation, not a code defect.
