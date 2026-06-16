# q ↔ CAL anchor drift, and a validity review of four "local-q" routes

**Date:** 2026-06-16
**Branch:** `claude/gracious-lovelace-uzuovl`
**Scope:** exploration only — documents a documentation-drift finding
about what pins `q₀`, and gives an outside-view validity assessment of
four proposed routes for making `q` a *local* field `q(p)`. No
production wiring is changed by this audit.

---

## Part A — The anchor drift (what currently pins `q₀`?)

The corpus disagrees with itself, three ways, about what calibrates the
substrate parameter. Only the **live compute** is authoritative; every
paper-side statement is stale relative to the 2026-05-28 re-pin.

| Source | `q₀` anchor | 3rd calibration | `Q_β` role |
|---|---|---|---|
| **Live compute** — [`constants.py`](../../tools/qou-substrate/python/qou_substrate/constants.py) (`:8`, `:24`, `:37`) | **`m_p/m_e` (proton)** | — | — |
| [`three-calibration-discipline.md`](../../content/quantum-observable-universe/observations/three-calibration-discipline.md) (paper proposition) | `m_μ/m_e` (muon) | `Q_β` | **input** |
| [`epistemic-status-of-calibrations.md`](../../content/quantum-observable-universe/observations/epistemic-status-of-calibrations.md) (paper remark) | `m_μ/m_e` (muon) | `Q_β` | **input** |
| [`canonical-derivation-cheat-sheet.md`](../canonical-derivation-cheat-sheet.md) §1 diagram | `m_μ/m_e` (muon) | **`m_π`** | derived |
| `CLAUDE.md` cheat-sheet table | neutron β-decay `τ_n` → `Q_β` | pion width → `m_π` | input (via `τ_n`) |
| [`README.md`](../../tools/qou-substrate/README.md) (`:29`) | prints the **muon** `q₀` value | — | — |

**Two independent forks:**

1. **`q₀` anchor: muon vs proton vs neutron.** The live value is
   **proton-anchored** — re-pinned 2026-05-28 (commit `01c18125`) from
   `m_μ/m_e` to `m_p/m_e = 1836.152673426` (CODATA 2022, 0.06 ppb, "the
   most precise anchor"; `σ(q₀) ≈ 0.0029 ppb = 2853 ppQ` vs 1.22 ppb on
   the muon anchor). `m_μ/m_e` is now a **prediction** (agrees ~9.5σ; the
   old muon `q₀ = 1.10997859555418…` is −11.5 ppb away). The CLAUDE.md
   table's "neutron β-decay `τ_n`" is a *third* description that matches
   neither the live proton anchor nor the paper's muon anchor. See
   [`2026-05-30-q0-repin-stale-witness-audit.md`](2026-05-30-q0-repin-stale-witness-audit.md).
   The m_μ L2 status is itself **convention-dependent** — ratio-anchored
   (`m_e × (m_μ/m_e)_CODATA`) meets the 100× target to numerical noise,
   while the bare-categorical (`4₁` Geom) prediction misses ~964× —
   reconciled in [PR #1556](https://github.com/litlfred/qou/pull/1556).
   The ratio-anchored convention *is* "read `q₀` off the lepton ratio",
   the defensible kernel of "q is the ratio" (box below).

2. **3rd calibration: `Q_β` vs `m_π`.** The paper blocks make `Q_β` the
   third *input* (fixing the hadronic scale `𝔈₀ = Q_β/|Δ(net)|`). The
   cheat-sheet diagram makes `m_π` the third input and `Q_β` *derived*
   from CAL-1 + CAL-2. These are **different calibration bases**; the
   framework can admit only one (the no-fourth-CAL discipline).

**Owner resolution (2026-06-16):** `q₀` is proton-anchored (matches
live), and the third calibration is `m_π` with `Q_β` derived (matches
the cheat-sheet diagram). Under this basis the three inputs are
`{m_e (scale), m_p/m_e → q₀, m_π (chiral/Goldstone scale)}`, and **both**
`m_μ/m_e` and `Q_β` are predictions. This is internally coherent and
consistent with the live compute; it conflicts with the two paper blocks
(`three-calibration-discipline`, `epistemic-status-of-calibrations`),
which therefore carry stale calibration framing.

**Action taken** (this branch): author-notes added to the two stale
paper blocks recording the live state + the owner resolution (per
CLAUDE.md §4d — status/caveat belongs in `authorNotes` metadata, not
scholarly prose). The full prose migration of the proposition statement
(changing the calibration basis, which ripples into
`prop:three-calibration-inputs`, the Wedderburn-count proposition, and
the SDP `m_π`-independence validation) is left as a tracked follow-up,
**not** silently rewritten here.

> **"q is the ratio" — the defensible kernel.** Because every mass is
> `m(K) = m_e · VolDensity(K, q₀)`, the `m_e` cancels in any ratio, so
> every mass ratio is a pure function of `q₀`. Thus `q₀` is *coordinatized
> by* any one measured dimensionless ratio (canonically the lepton ratio,
> now the proton ratio) — a bijective reparameterization, **not** an
> identity. `q₀` fixes *all* ratios simultaneously; it is not equal to any
> single one. The epistemic-status block confirms over-determination:
> `α_EM⁻¹` or tritium `t₁/₂` pin the same `H¹` datum to ~0.3%.

---

## Part B — Validity review of the four "local-q" routes

The user proposed four routes for promoting `q` from a global constant to
a local field `q(p)`. Outside-view assessment, in confidence order.

### Route 4 — "Fix the drift" — ✅ VALID, highest value/lowest risk

The proton-anchor and `m_μ/m_e`-is-a-prediction facts are directly
verifiable in `constants.py`. Author-noting them is correct and
overdue. The `CAL-3 = m_π` part is a genuine content judgment (it
contradicts the paper blocks) but is well-grounded in the cheat-sheet
diagram and the owner's resolution. **Done as author-notes** (reversible,
render-skipped by default); prose migration flagged as follow-up.

### Route 2 — "Germ-dynamics: δq(p) from the parallelogram + q-heat eqn" — ✅ VALID (mostly already exists)

This is the strongest of the four — it assembles **two existing blocks**:

- [`two-observer-parallelogram.md`](../../content/quantum-observable-universe/quantum-observable-universes/two-observer-parallelogram.md)
  **already derives `δq(p)`**: each observation perturbs the substrate at
  `p` by `δq_i(p)`, giving `q_i'(p) = q(p) + δq_i(p)`, and the
  obstruction is the commutator `[q_1'(p), q_2'(p)]`. This is exactly the
  germ-level (first-jet, `A/𝔪_p²`) curvature picture.
- [`q-gaussian-solves-q-heat.md`](../../content/quantum-observable-universe/information-theory/q-gaussian-solves-q-heat.md)
  gives the `q`-heat equation `∂_t G_q = −Δ_q G_q` with the
  Reeb-invariant Gaussian, the "clock at rate `q⁻²`" interpretation, and
  it **already cites `prop:local-substrate-q`**.

**What is solid:** the germ `δq(p)` = parallelogram commutator
(holonomy/curvature contracted on the loop) — standard differential
geometry, already in the corpus. **What is a motivated ansatz (not
derived):** an *evolution law* for `q(p)` itself, e.g. a `q`-harmonic-map
heat flow `∂_t q = −Δ_q q`. The q-heat block governs diffusion of a
scalar density at *fixed* `q`; making `q(p)` itself the diffusing field
is a new (well-motivated) postulate. **Honest verdict:** kinematics
solid and corpus-backed; the specific PDE is a clearly-labeled ansatz,
not a theorem. Worth authoring as the connective proposition.

### Route 3 — "Un-stub the Lean so q(p) is a real field" — ✅ VALID (and it repairs a broken file)

[`substrate-parameter.lean`](../../content/quantum-observable-universe/quantum-observable-universes/substrate-parameter.lean)
**does not currently compile**: `field_ne_zero`, `field_ne_one`, and
`planck_nonneg` all reference fields (`field_pos`, `field_ge_one`,
`not_root_of_unity`) that are **commented out** with the (correct) note
"archimedean; not meaningful over `R_q`". The structure's `field` is
`M → R_q` with `R_q = LaurentPolynomial ℤ`, which is **not ordered** — so
`0 < field p` is genuinely type-incorrect there. The comments are right;
the dangling theorems are the bug.

**The §7c-correct fix is NOT to uncomment the order properties over
`R_q`.** It is to keep the categorical `SubstrateParameter` formal over
`R_q` (and make it compile by repairing the dangling theorems) **and add
a separate `ℝ`-valued `ArchimedeanSubstrateField (M)`** structure —
`field : M → ℝ` with `field_pos`, `field_ge_one`, not-root-of-unity —
living on the archimedean side of the substrate wall. *That* makes
"`q(p)` is a real field" literally true while respecting the base-ring
discipline (CLAUDE.md §7c). **Verdict:** valid, concrete, bounded; it
both delivers the user's ask and fixes a compile break. Caveat: this
sandbox has no Lean LSP/`lake` available, so the repair is
type-correct-by-construction but **not build-verified** — flagged for a
Lean-CI pass.

### Route 1 — "Fixed-point: does `∇_q² = (q−1)𝓕_q^intr` select q₀?" — ⚠ HALF-VALID (the stated condition does NOT select q₀)

The `q`-flat-connection identity
`∇_q² = (q−1)𝓕_q^intr`
([`q-flat-connection.md`](../../content/quantum-observable-universe/q-geometric-langlands/q-flat-connection.md))
holds for **every** `q` — it is the *definition* of `q`-flatness with
intrinsic curvature, parametric in `q`. It therefore **cannot** single
out the numerical `q₀ ≈ 1.1097`. The naive reading of the route is
**false**.

**However**, the *general* program — "`q₀` is the distinguished point of
the `𝔾_m`-family, selected by a fixed-point / extremal condition" — is a
legitimate, currently **re-opened** research direction. `substrate-parameter.md`
states `q` is "*not* intrinsic to the triple… records where one sits in
the `𝔾_m`-family", i.e. `q₀` is a *modulus*; and
[`epistemic-status-of-calibrations.md`](../../content/quantum-observable-universe/observations/epistemic-status-of-calibrations.md)
lists "spectral collapse, K-theoretic period, Bring `χ=−6` fixed-point,
categorical endomorphism fixed-point" as candidate derivations of `q₀`.
A *defensible* reformulation is therefore: `q₀` selected by
**extremizing the intrinsic-curvature functional `‖(q−1)𝓕_q^intr‖`** or by
a **Reeb closed-orbit / period-integrality** condition — **not** by
`q`-flatness, which is generic. **Verdict:** sketch as a conjecture with
the correction baked in; do **not** claim it derives `q₀`.

> **Scope flag (STRICT).** Substrate-derivation of `q₀` was **declined
> 2026-05-08** as out-of-scope (CLAUDE.md Subgoal-2) and **re-opened**
> recently per the epistemic-status block. The owner question driving
> this session is the reversal. Any `q₀`-selection work stays at
> research-direction / conjecture status until a closure clears the
> three-calibration discipline review — it must not be wired to
> production or quoted as a derived result.

---

## Summary ranking

| Route | Verdict | Action |
|---|---|---|
| 4 — fix drift | ✅ valid, do now | author-notes (done); prose migration = follow-up |
| 2 — germ-dynamics | ✅ valid, ½ exists | author connective prop; PDE labeled as ansatz |
| 3 — un-stub Lean | ✅ valid, repairs break | §7c-correct fix; flag for Lean-CI |
| 1 — fixed-point | ⚠ half-valid | sketch as conjecture; "∇_q² selects q₀" is false; q₀-selection is re-opened research |
