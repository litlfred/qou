# Agent task backlog — stalled / in-flight threads (catalogued 2026-06-09)

Consolidated from several stalled agent sessions so the work is not lost.
Each theme lists merged context, open PRs, concrete TODOs, owner directions,
and blockers. Status markers: ✅ done · ▶ next · ⏸ blocked · 🔗 coordinate.

---

## 1. Hecke recursion / reduced-block kernel (Phase 1.x compute)

- ✅ **#2056 merged** — Phase 1.3 q-Young wire-in.
- 🟢 **#2062 open** — Phase 1.4 reduced-block kernel + oblique-projector
  finding + design doc + measured data. All Gemini/Copilot comments fixed in
  code (threads pending API-rate-limit to resolve).
- **Toolchain unlock (correcting a stale handover):** Rust **is** available —
  `cargo`/`rustc` 1.94.1; `pyhecke-native` builds via maturin (~40s), wheel
  installed. The old "Rust unavailable" claim was false.
- **Verification achieved:** mpfr one-level *and* the reduced kernel match the
  canonical Rust `chi_q_via_gp` — **18/18 at A=4, 4/4 at A=5** (not just
  self-consistent). Sector dim bounded (≤10) as dim V_λ → 60; mpfr 2.66× faster
  than Rust on low-dim A=5. Braid word confirmed nested-bridge
  (`β₀·σ₃·β₁·σ₆·…`); existing Rust `chi_via_matrix_m_mpfr` is one-level only.

**TODO**
- ▶ Tier-3 recursion (the actual A≥6 speedup) — transfer-matrix / bridge-table
  formulation; verify against Rust at each step. *(Hard part is a **correct**
  recursion — the single-level kernel already had a subtle oblique-projector
  bug caught against the dense reference; build carefully, don't ship
  unverified compute.)*
- ▶ Rust port of the reduced/recursive kernel into `hecke-engine`.
- ▶ A=6→9 catalogue sweep (now runnable with the wheel).
- Decision (agent leaned this): **merge #2062 first** (clean + reviewed unit),
  build recursion + Rust port on a fresh branch.

## 2. Casimir + m_μ convergence (the 4₁ Habiro lever)

- 🟢 **#2052 open** — STATUS.md housekeeping.
- **Casimir status:** leading `1/d⁴` prefactor `π²/720` derived unconditionally
  (`ξ₂=0` now structural). First q-correction is at **1/d⁶** (not 1/d⁴),
  carried by the figure-8 knot **4₁**, with `J_{4₁}(q) = 1 + (3/4)h²` — the
  `3/4` is Lean-proved exact (`jones41_three_quarters`, no sorry, no fitting).
- **High-value finding — Casimir and m_μ converge:** the Casimir 1/d⁶
  q-correction **and** the m_μ Tier-1 gap both run through the **same figure-8
  (4₁) Habiro element** (muon = 4₁ per `prop:skein-mass-relation`; both use the
  substrate q₀ that 4₁'s volume defines). One piece of work advances both.

**TODO**
- ▶ **m_μ chain audit (Tier-1)** — localize the 210 ppb residual (ledger step 1;
  *not* fitting). This is where the 4₁ Habiro lever lives. **Owner: "start the
  m_μ chain audit now."**
- ▶ 4₁ Habiro element — advances both the m_μ gap and the Casimir d⁶ correction.
- ▶ Yekutieli-homotopy lift — explicit categorical `N_⊙(A,d)` object (Casimir
  sub-problem 1 remainder).
- ▶ Interacting-mode mode-sum — absolute 1/d⁶ coefficient magnitude.
- ⏸ Lean v4.24.0 cleanup (Tier-2) — blocked: no `lake` in that sandbox
  (`release.lean-lang.org` firewalled); needs a Lean-capable env or CI.
- 🔗 Detangler (Tier-3) — overlaps active sibling **#2030**; coordinate, don't
  duplicate.

## 3. JetOrderIndependence linkage (three-knot jet order)

- ✅ **#1990 merged**.
- 🟢 **#2063 open** — `JetOrderIndependence.ofMonotoneBase` constructor wiring
  `jacobianRank_eq_three_of_base` to the concrete `jacobianRank` (addresses
  Copilot's substantive point on #1990). Instance rerouted through
  `ofMonotoneBase`; `.md` synced. **Verified EXIT 0, no errors, no sorry**
  (real lean vs restored v4.24.0 Mathlib oleans, lake-bypass recipe);
  `bun run validate` exit 0. Subscribed.

**TODO**
- ▶ `/prepare-merge` #2063.
- ◽ (optional) matrix-submatrix lower-bound lemma — turns the last stated
  matrix-realization *input* into a proved lemma (its Mathlib rank-submatrix
  API was unverifiable under the sandbox firewall; not fabricated).

## 4. float64 purge + Q_β bridge

- ✅ **#2036, #2050 merged**.
- 🟢 **#2053 open** — batch 7 float64 drain.
- **float64:** ~59% done (156→64 hits). High-value work (L1 `markov_peel`
  destroyer, the critical QA criterion, 92 destroyers) done & merged. Remaining
  64 is a low-value long tail (probe/audit scripts) + 3 deferred structural
  rewrites (~5 more batches).
- **Q_β bridge:** the multi-block fundamental-rep **eigenphase** is the correct
  structural object — q₀-stable to 0.00003% through 6 orders (first sustained
  positive signal; structural, not coincidental). But the ansatz family
  `{cos, exp, 1+α}` is insufficient (misses CODATA −1.1%…−15.9%; experiment #4
  `cedd209503` ruled out 3 more mechanisms). **Verdict: OPEN** — the composition
  with Form A is more complex than `f(α_eff)`.

**TODO (owner-directed)**
- ▶ **Keep float64 going** — merge #2053, continue the tail batches.
- ▶ Q_β bridge: pursue the eigenphase ∘ Form A composition via **q-hyperbolic /
  geometric** structure — **owner: "look at q-hyperbolic and geometric.. not
  ansatz."** The open question is now sharply defined (eigenphase is right;
  what is its composition with Form A?).

## 5. lean_ci / docs / viewer (env + doc-gen pipeline)

- Agent stalled mid-task.
- **Owner constraints (honor these):**
  - CI failures = **billing**, not code → build **locally** with the
    lake-cache infra.
  - Leverage **doc-gen4's existing HTML** — do *not* build a parallel page.
  - Do *not* replicate `mapping.json` / `proof-objects.json` data — derive
    fresh to avoid **drift**.
  - **Diagnose first:** go back to the last successful paper build and find
    **why `lean_ci.yml` has been failing since April** before building any
    overlay.

**TODO**
- ▶ **Diagnose `lean_ci.yml` failure since April** (from last successful build) —
  **do this first.**
- ▶ Refresh docs (build locally w/ lake-cache).
- ▶ Build folio Lean index (leverage doc-gen4 HTML).
- ▶ Viewer cross-link (no data replication).

---

## 6. Field-typeclass over-strength burn-down (this session — in flight)

- ✅ Audit tool `field_typeclass_audit.py` + witness + doc **merged** (#2066);
  pilot `SurrealRateCalculus [Field F]→[CommRing F]` merged.
- 🟢 **branch `claude/field-typeclass-burndown-2026-06-09`** (open) — 12 more
  division-free relaxations (ClassicalLimitObstruction, GradedTraceResidueSplit
  ×8, HoefsmitV21Cos, QClt/TraceLocality → LinearOrderedCommRing), building.
- **3-way classification** (see `docs/audits/2026-06-09-field-typeclass-over-strength.md`):
  division-free (mechanical → CommRing), **q-power-Laurent** (reframable over
  `ℤ[q,q⁻¹]` / `[CommRing R]`+unit, denominators cleared — owner direction),
  **non-unit division** (genuinely `Frac(R)`; keep generic `[Field R]`, do not
  specialize to ℚ(q)).

**TODO**
- ▶ Reframe q-power-Laurent character modules (BorromeanChiPerRep,
  DerivedCharacterCatalogue) over `[CommRing R]` + unit witness (per-module
  proof refactor; build-verified).
