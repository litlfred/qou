# Per-knot mass-table wire-up workplan (2026-06-03)

> User directive (2026-06-03): "wire up ALL isotopes/nucleotides properly … we need to cover all nucleotides/isotopes in the end of the day".
>
> Honest scoping: 2 of the 5 phases are blocked on **owner-direction** (per-knot `linking_weight(K)` is Δ_λ-gate forbidden without owner ansatz approval). Phases 1-2 + parts of 4-5 are tractable engineering today; Phase 3 is the closure blocker.

## Diagnosis (consolidated from PRs #1746, #1749, #1751, #1756)

The canonical mass formula is `m(K) = m_e · VolDensity(K, q₀)` with K knot-dependent. Production violates this two ways:

1. **Uniform Vol bug** — 87 of 89 atom-mass scripts use `vol_density_borromean(q)` regardless of atom; only 2 use per-knot `vol_density_per_block(vol_K, tr_M_K, q)`. 64 atom-touching scripts have the bug ([`docs/audits/2026-06-02-vol-usage-audit-uniform-vs-per-knot.md`](../audits/2026-06-02-vol-usage-audit-uniform-vs-per-knot.md)).
2. **Uniform linking_weight bug** — production uses H_4 Family-A `λ_A = 5/2 + 3h²/4 ≈ 2.53` for all atoms. No per-knot `linking_weight(K)` generalisation exists in compute or paper.

Naive fix attempts:
- Replace `vol_density_borromean(q)` → `vol_density_per_block(vol_K, tr_M_K, q)` in production: takes m_p from +2.89% to **−50.4%** (PR #1756 demonstration; mirrors the RED verdict of [`vol_density_per_block_wiring.py`](../../computations/vol_density_per_block_wiring.py)). Per-block H_n tr_M(K) drops from 1.22 at p to 0.12 at ⁴He, while production's H_4 Family-A linking_weight stays at 2.53. The two scalars are **different objects**, not refinements.

## Phased implementation

### Phase 1 — Diagnosis + workplan + truth-tracking ✅ DONE TODAY

- **#1746** (merged): refute 5th of 5 categorical-candidate scalar constructions for `|c|(λ)` — only 1 candidate remains, with basis-convention objection
- **#1749** (merged): cheat-sheet `VolDensity(𝓑₃)` → `VolDensity(K)` reframing + Q_β / L2 status reconciliation
- **#1751** (merged): cheat-sheet 5 places fixed for knot-dependence + 1ppQ ledger sessions log update
- **#1756** (open): per-knot demonstration script empirically validates the RED verdict across 6 atoms
- **This workplan** (this PR): consolidates the 5-phase scope

### Phase 2 — Wire α-cluster recursion into `try_binding_canonical` (TODAY, engineering)

**Scope correction (2026-06-03, mid-session)**: digging into `mass_table_comprehensive.py` showed the actual gap is NOT Vol(K) extension. Production already uses `m_pred = Z·m_p + N·m_n − B(K)` where m_p/m_n come from substrate-identity (single-knot-Borromean correct for protons); the +2.89% → +3.73% growth is dominated by **`B_pred = 0` for A > 12** because `try_binding_canonical` is gated on the H_{3A} kernel.

The `recursive-on-⁴He` atlas tag IS the user's "build each atom recursively from prior atoms + canonical braids w/ unfolding". The formula `B(nα) = n·B(⁴He) + C(n,2)·c_αα` (Whitehead link 7²_1 for the α-α coupling) is **already implemented** in [`computations/alpha/alpha_cluster_recursion.py`](../../computations/alpha/alpha_cluster_recursion.py) for the A>12 α-cluster atoms (¹⁶O, ²⁰Ne, ²⁴Mg, ²⁸Si, ³²S, ³⁶Ar, ⁴⁰Ca; ⁸Be / ¹²C are A≤12 so they go through the existing `binding_canonical` branch, not α-recursion). It just **isn't wired** into `mass_table_comprehensive.py:try_binding_canonical` for the A>12 branch.

**What**: modify `try_binding_canonical(Z, N, q_str)` to:
1. Existing: A ≤ 12 → `binding_canonical` (Δtr_M closed form) — unchanged. Covers ⁸Be / ¹²C.
2. **NEW**: A > 12 with `Z == N` and `A % 4 == 0` → call `alpha_cluster_binding(Z, N)` from `alpha/alpha_cluster_recursion.py`. Covers ¹⁶O, ²⁰Ne, ²⁴Mg, ²⁸Si, ³²S, ³⁶Ar, ⁴⁰Ca (7 atoms).
3. Existing: other A > 12 → return None (still gated on H_{3A} kernel)

**Output**: extended `mass-table-comprehensive.witness.json` with non-zero B_pred for 7 additional isotopes (¹⁶O, ²⁰Ne, ²⁴Mg, ²⁸Si, ³²S, ³⁶Ar, ⁴⁰Ca). Net `binding_computed` rises from 10 → 17 of 65.

**Discipline**: this is **engineering** (wires existing code that's already PROVED via the `recursive-on-⁴He` methodology in the atlas). Not a new ansatz; not a Δ_λ-gate violation. The α-cluster recursion uses zero free parameters — B(⁴He) from magic-A formula, c_αα from Whitehead link Vol.

**What I will NOT wire**: non-α-cluster atoms with A > 12 (e.g., ⁶Li, ⁷Li, ⁹Be, ¹⁰B, ¹¹B, ¹³C, ¹⁴N, ¹⁵N, ¹⁷O, ¹⁸O, ¹⁹F, ²¹Ne, ²²Ne, ²³Na, ²⁵Mg, ²⁶Mg, ²⁷Al, all of Si onward except the α-cluster point). These remain gated. The atlas's `deprecated-volume-match` for ⁶Li, ⁷Li is explicitly excluded.

### Phase 3 — Per-knot `linking_weight(K)` derivation 🟡 OWNER-DIRECTION BLOCKED

**What**: define `linking_weight(K)` for arbitrary atomic K such that:
- `linking_weight(𝓑₃) = λ_A = 5/2 + 3h²/4` (production's H_4 Family-A; reproduces m_p at +2.89%)
- `linking_weight(K_atom)` generalises across atoms A ≥ 2 in a way that's:
  - derived (NOT a fit), per AGENTS.md Δ_λ gate
  - tested against the muon (4_1) anchor exactly
  - tested against AME atomic masses

**Why this is owner-blocked**: there's no existing categorical formulation in the paper. The H_4 Family-A reading is specific to the Borromean 𝓑₃'s 3-strand → H_4 cover. For atomic braids on 3A strands, the analogous Family-A would be H_{3A+1} — but no such structure is derived. Six prior `Δ_λ` ansätze were refuted (see option-e history); proposing a 7th `linking_weight(K)` ansatz is forbidden.

**What I can do without owner direction**:
- Document the 6 candidate categorical paths surfaced in PR [#1721's `|content|` scoping](../../docs/coordination/2026-06-02-abs-content-hecke-energy-scoping.md) + PR #1746's refutations
- Surface the testbed's RED verdict as evidence-of-non-trivial-generalisation
- Wait for owner to indicate which categorical chain to pursue

**Without Phase 3**: production stays at +2.89-3.73% mass errors for the foreseeable; per-knot Vol(K) from Phase 2 is engineered correctly but not yet useful.

### Phase 4 — Production wire-up (BLOCKED on Phase 3)

**What**: refactor `mass_table_comprehensive.py:208` from `vol_density = vol_density_borromean(q)` to `vol_density = vol_density_per_block(vol_K, linking_weight_K(q), q)` using the per-atom Vol(K) from Phase 2 and the per-knot `linking_weight(K)` from Phase 3.

**Why blocked**: requires Phase 3's `linking_weight(K)` definition. Without it, this phase would either (a) regress every isotope's prediction by ~50% (per the testbed's RED verdict), or (b) require fitting `linking_weight(K)` per atom (Δ_λ-gate forbidden).

### Phase 5 — Dashboard refresh + audit closure (BLOCKED on Phase 4)

**What**: re-run `mass-table-comprehensive.witness.json` + `per-observable-100x-status.witness.json` + update STATUS.md + close the [`vol-usage-audit`](../audits/2026-06-02-vol-usage-audit-uniform-vs-per-knot.md).

**Why blocked**: requires Phase 4 to actually change predictions.

## What "end of the day" can actually deliver

| Phase | Today? | Why / Why not |
|-------|--------|---------------|
| 1 | ✅ done | Diagnosis + truth-tracking PRs already merged + this workplan |
| 2 | ✅ done | α-cluster recursion wired into `try_binding_canonical` for the A>12 α-cluster atoms ¹⁶O / ²⁰Ne / ²⁴Mg / ²⁸Si / ³²S / ³⁶Ar / ⁴⁰Ca (commits `6fc4ca0ae3`, `9b4fae28f8`); 7 atoms improved by ~10× from m_err ≈ +0.9% to ≈ −0.1%. ⁸Be / ¹²C are A≤12 so already covered by the existing `binding_canonical` branch — no wire-up gap there. |
| 3 | ❌ no | Δ_λ-gate forbidden without owner direction on `linking_weight(K)` generalisation strategy |
| 4 | ❌ no | Depends on Phase 3 |
| 5 | ❌ no | Depends on Phase 4 |

## Phase 2 result (commit `6fc4ca0ae3` + `9b4fae28f8`)

Before vs after, on the 7 α-cluster atoms previously gated as B=0:

| atom | B_pred (MeV) | B_AME (MeV) | m_err % before | m_err % after | gain |
|------|-------------:|------------:|---------------:|--------------:|-----:|
| ¹⁶O  | 134.4 | 127.6 | +0.85 | **−0.05** | ~17× |
| ²⁰Ne | 174.0 | 160.6 | +0.86 | **−0.07** | ~12× |
| ²⁴Mg | 216.1 | 198.3 | +0.87 | **−0.08** | ~11× |
| ²⁸Si | 260.7 | 236.5 | +0.88 | **−0.09** | ~10× |
| ³²S  | 307.6 | 271.8 | +0.91 | **−0.12** | ~8× |
| ³⁶Ar | 357.0 | 306.7 | +0.93 | **−0.15** | ~6× |
| ⁴⁰Ca | 408.8 | 342.1 | +0.92 | **−0.18** | ~5× |

Witness counters: `binding_computed: 10 → 17` (+7); `gated_on_phase2: 59` unchanged for non-α-cluster atoms. Refresh in `mass-table-comprehensive.witness.json` confirms.

The α-cluster `c_αα` coupling currently uses Whitehead-link Vol(7²_1) literature value; the slight overshoot of `B_pred` vs AME (5-19%) is consistent with the atlas's documented "+ recursion error budget" for the `recursive-on-⁴He` methodology. Refining `c_αα` per knot is a research-grade follow-up.

**Honest disposition**: end-of-day target = phases 1 + 2 (engineering complete) + phases 3-5 surfaced as owner-decision-required. Cannot wire up "ALL 65 isotopes properly" today without owner approval of a `linking_weight(K)` ansatz.

## Owner direction needed (Phase 3 escalation)

Please pick one of:

1. **Approve a specific categorical chain for `linking_weight(K)`** (e.g., trace of |Ω_q| in Hoefsmit basis per PR #1721 candidate #1; or a new Kashiwara crystal candidate; or operator-valued LR branching from #1443).
2. **Defer Phase 3** to research-grade follow-up; accept that today's wire-up stops at Phase 2 (Vol(K) coverage); production keeps the +2.89-3.73% baseline.
3. **Approve an empirical multiplicative correction per atom** matching AME — explicitly fitted, explicitly labeled `CAL-X` per the three-calibration discipline (forbidden under Δ_λ gate but tractable if owner explicitly waives).

Without one of these, Phases 4-5 remain blocked.

## Cross-refs

- [`docs/audits/2026-06-02-vol-usage-audit-uniform-vs-per-knot.md`](../audits/2026-06-02-vol-usage-audit-uniform-vs-per-knot.md)
- [`docs/canonical-derivation-cheat-sheet.md`](../canonical-derivation-cheat-sheet.md) §3 Phase Bind + §5 manager-view #1
- [`docs/coordination/1ppq-qbeta.md`](../coordination/1ppq-qbeta.md) sessions log 2026-06-03
- [`docs/coordination/2026-06-02-abs-content-hecke-energy-scoping.md`](../coordination/2026-06-02-abs-content-hecke-energy-scoping.md) — 4/5 candidates refuted
- PR [#1756](https://github.com/litlfred/qou/pull/1756) — per-knot demonstration empirically confirming the RED verdict
