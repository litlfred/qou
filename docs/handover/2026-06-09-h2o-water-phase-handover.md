# Handover — H₂O / water-phase + matter-hierarchy session (2026-06-08/09)

> **Status:** owner away ~1 week. This is the durable handover for the
> next agent. Everything below is **already merged to `main`** unless
> marked TODO. Read this first, then `STATUS.md` + the linked docs.

## 1. What landed (4 PRs merged this session)

| PR | Title | Delivered |
|----|-------|-----------|
| **#1999** | phase-transition foundations + metallic-q proof | machine-verified `q−q⁻¹=n ⟺ q=δ_n` (metallic ratios); phase-symmetry-from-knot-operator model; 6 audit/coordination docs |
| **#2009** | q-hierarchy conjecture narrowed | `[2]_{δ_n}=√(n²+4)` (quantum dimension) + golden self-similarity `φ²=φ+1` (axiom-clean) |
| **#2002** | optical-fibre / 1D QOU section | 5 blocks; non-interaction = split-link Markov-trace multiplicativity (Lean-verified) |
| **#2014** | **H₂O build** | `sec:h2o-computation` (6 blocks); ~12 axiom-clean Lean theorems |

All Lean was verified via the **cache + direct-`lean`** recipe (§4); content-block `.lean` siblings are not in the lib graph, so they're verified standalone, not by CI's `lake build`.

## 2. The H₂O / water-ice content map (`content/quantum-observable-universe/molecular-construction/`)

`sec:h2o-computation` (between CH₄ and benzene), 6 blocks:

1. `def:h2o-molecular-braid` — H₂O = `O(8,8)` + 2 `H` in `H₂₈(q)`, assembled by the **assembly projector** `e_{λ,μ}`, `λ=(24,2,2)`. Lean (`decide`, axiom-free): `water_total`=28, `water_numBonding`=2 (the two O–H bonds = `k−1` cross-block generators), `water_h_swap_symmetry`.
2. `rem:h2o-c2v-from-projector` — **C₂ᵥ = Stab(e_{λ,μ})** under H₁↔H₂. The general principle (now realized at molecular scale): *a structure's point symmetry is the stabilizer of its assembly projector* (benzene S₃, water S₂).
3. `rem:h2o-bent-geometry` — physical picture: 104.5°, 4 H-bond directions → ice I_h.
4. `prop:tetrahedral-hbond-directions` — Lean `tetrahedral_cos`: the 4 directions are the tetrahedron vertices `(±1,±1,±1)` (even sign count) ⇒ **cos θ₀ = −1/3, θ₀ ≈ 109.47°**.
5. `prop:h2o-bond-angle-shift` — Lean `bond_angle_shift`: harmonic well `a(θ−θ₀)² + bθ` minimised at **θ₀ − b/(2a)**; the 109.5→104.5 reduction is the quadratic minimum displaced by the linear lone-pair term.
6. `prop:ice-pauling-residual` — Lean `pauling_multiplicity`: `C(4,2)·(1/2)² = 3/2` ⇒ **S = R ln(3/2) ≈ 3.37 J mol⁻¹K⁻¹**.

## 3. Predictive vs experimental (the scorecard)

| Quantity | Predicted | Experimental | Verdict |
|---|---|---|---|
| Tetrahedral angle θ₀ | `arccos(−1/3)` = **109.47°** (proved, 0 params) | ice O–O–O ≈ 109.5° | ✓ exact |
| Ice residual entropy | `R ln(3/2)` = **3.371 J mol⁻¹K⁻¹** (proved, 0 params) | 3.41 ± 0.2 (Giauque–Stout 1936) | ✓ **~1%** |
| O–H bonds | **2** (proved) | 2 | ✓ |
| H–O–H bent angle | bent & reduced (structure proved); = 104.5° at observed `b/(2a)` | 104.5° | ◑ structure exact; **magnitude is an input** |

## 4. ⭐ IMMEDIATE NEXT TASK (owner's explicit steer): make the bond angle predictive

`θ* = θ₀ − b/(2a)` is proved as a *form*, but `b/(2a)` (the ~5°) is currently **read off experiment**. To upgrade the ◑ row → ✓, **compute `a` and `b` from Φ₁**:

- **`a` = Φ₁ bending curvature** — 2nd derivative of the H₂O strand-arrangement energy `Φ₁` (the quantum-dilogarithm volume) at the symmetric tetrahedral configuration. The angular stiffness.
- **`b` = Φ₁-weight difference** between oxygen's lone-pair "phantom" sites and its bonding sites — the net lone-pair push.
- **How:** the **LP-dual / Φ₁-minimization over `H₂₈(q)` strand orderings** — the *same compute pattern as CH₄* (`ch4-lp-dual-binding.py` / `ch4-tetrahedral-symmetry`; reuse `molecular-frobenius-lp` and the `Φ₁` machinery).
- **Deliverable:** a witnessed compute script + `prop:h2o-bond-angle-prediction` emitting `a`, `b`, predicted `b/(2a)` → predicted angle vs 104.5°; then update `prop:h2o-bond-angle-shift` / `rem:h2o-bent-geometry` to ✓.
- **⚠ GATE:** needs **canonical Python (`pyhecke`/`numpy`/`cvxpy`)**, which is **MISSING in the web sandbox** — run in a Python-enabled env (local / CI runner). Emit `*.witness.json`.

## 5. Other open threads (priority order)

1. **Freezing/boiling/sublimation temps** (the original headline) — derive the **running-q fixed point** of `T_boil/T_freeze = [n_K]_q`. ⚠ The fixed-q₀ *integer* reading is **REFUTED** — see [`docs/audits/2026-06-08-phase-transition-ratio-formalize-first.md`](../audits/2026-06-08-phase-transition-ratio-formalize-first.md). Phases = inter-molecular Hopf-link count (gas 0 / liquid partial / ice 4 tetrahedral). Research-grade.
2. **Upper-q regime sweep** — golden→silver→bronze metallic ladder; the **bar-symmetry `q=φ²` probe** (one-line formalize-first check, *do this before any scan*). Full spec: [`docs/audits/2026-06-08-q-regime-map-coordination.md`](../audits/2026-06-08-q-regime-map-coordination.md) §3b.
3. **Easy provable H₂O extensions** (if wanted): ice density anomaly (open tetrahedral packing < close-packing ⇒ ice floats); C₂ᵥ vibrational modes (3 = 2A₁ + B₂).

## 6. Infra notes — READ BEFORE Lean/compute work

- **Lean verify (works in web sandbox):** restore the cache, then verify with **direct `lean` + manual `LEAN_PATH`** — do **NOT** run `lake env lean` / `lake build` (re-resolves deps and *wipes* the restored oleans). Use **specific imports**, never bare `import Mathlib` (cache omits the root olean). Two gotchas + full recipe: [`docs/coordination/2026-06-08-lean-cache-architecture.md`](../coordination/2026-06-08-lean-cache-architecture.md) and `.claude/skills/local/lean-environment-setup.md`.
  ```bash
  ROOT=$(git rev-parse --show-toplevel); TGZ=$(mktemp)
  SLUG=$(cut -d: -f2 "$ROOT/lean-toolchain" | tr -d '\r' | tr . -)
  git fetch --depth=1 origin "lake-cache/qou-$SLUG" \
    && git ls-tree --name-only FETCH_HEAD | grep '^lake-oleans\.tgz\.part' | sort \
       | while read -r p; do git show "FETCH_HEAD:$p"; done > "$TGZ" \
    && tar xzf "$TGZ" -C "$ROOT" && rm -f "$TGZ"
  LP=$(find "$ROOT/.lake/packages" -maxdepth 5 -type d -path '*/.lake/build/lib/lean' | tr '\n' ':')
  LP="$LP$ROOT/.lake/build/lib/lean:$ROOT/content/quantum-observable-universe/lean/.lake/build/lib/lean"
  env LEAN_PATH="$LP" ELAN_NO_OVERRIDE_NOTICE=1 lean path/to/File.lean   # EXIT 0 = green
  ```
- **`bun run validate <paper>` is slow + fully buffered** (~5 min, no progress output) — be patient or trust CI; it is *not* hung.
- **Canonical Python (`pyhecke`/`numpy`/`cvxpy`/`mpmath`) is MISSING in the web sandbox** — any Φ₁ / witness / LP-dual / mass compute is blocked here; defer to a Python-enabled env.
- **Molecular LP-dual gap:** [`docs/audits/2026-06-08-molecular-chapter-currency-wiring-audit.md`](../audits/2026-06-08-molecular-chapter-currency-wiring-audit.md) — 0/6 molecular scripts emit LP duals (the chapter's own thesis is "dual shadow price = binding energy"). The math is current; only the compute plumbing is behind.

## 7. Coordinate

Active sibling **#2003** (`claude/affectionate-hopper-seYEv`, CO bond-order = LP active-set) touches the same `molecular-construction` chapter — flag conflicts on `co-*` blocks / the chapter manifest. It's the natural place to start closing the LP-dual gap (§6).

## 8. Key reference docs (all on `main`)

- Phase-symmetry-from-knot-operator model: `docs/audits/2026-06-08-phase-symmetry-from-knot-operators-model.md`
- Phase-transition ratio (formalize-first refutation): `docs/audits/2026-06-08-phase-transition-ratio-formalize-first.md`
- q-regime + metallic hierarchy: `docs/audits/2026-06-08-q-regime-map-coordination.md`
- Metallic-q proof writeup: `docs/audits/2026-06-08-metallic-q-hierarchy-proof.md`
- Molecular-chapter currency+wiring audit: `docs/audits/2026-06-08-molecular-chapter-currency-wiring-audit.md`
- Lean-cache architecture (the recipe): `docs/coordination/2026-06-08-lean-cache-architecture.md`

---

**TL;DR for the next agent:** the H₂O/water-ice physics is built and Lean-verified (2 exact predictions + a ~1% residual-entropy match). The one open prediction is the **bond angle** — start by **computing `a` and `b` from Φ₁** (§4) in a Python-enabled env to turn 104.5° into a real prediction.
