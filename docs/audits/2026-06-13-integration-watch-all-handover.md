# Handover: `/integration-watch all` — remaining work

**Scope:** Drain the remaining integration-watcher findings that this session
could not safely complete in-sandbox (Lean criticals blocked by missing Mathlib
oleans; compute/detangler drain is research/authoring-heavy).
**Discovered by:** `/integration-watch all` on 2026-06-13 (branch
`claude/beautiful-galileo-g73tos`, PR #2246).
**Severity:** major (no criticals remain live after verification).
**Estimated effort:** B ≈ 1–2 h with a Mathlib cache; D ≈ days (per-bucket).

## What this session completed (13 commits on PR #2246)

- Populated + **verified** all 4 watcher backlogs (`todos/*-queue.json`):
  proof 43 resolved / 6 queued · canonical (1 genuine fit fixed) · compute
  **65 → 40** (24 false-positives demoted by the verify pass) · detangler 54.
- `fix(lean-ref)` casing ×7 — aligned block `lean.ref` URIs to actual `.lean` decls.
- `fix(canonical)` term6-binding-density **proposition → remark** (author-approved;
  6-file + index cascade).
- `audit` proof citation drain — **51 axioms cited + 15 cite-position fixes**.
- Demoted a false-positive compute "critical" (tr_M conflict resolved #1422) and
  resolved the 6 UNSURE compute items (0 demoted — none were false positives).

## Remaining: B — 3 proof criticals (LSP/Mathlib session)

Documented in-source in `content/quantum-observable-universe/predicted-spectra/`:

| Decl (file) | State | Exact discharge |
|---|---|---|
| `hadronic_melt_at_supergolden` (spectrahedral-phase-collapse.lean) | real stmt, cited `sorry` | `det = f₁·f₂·(u³+u−1)`, `f₁,f₂>0` for `u>0` ⇒ `det<0`; use the `GramMatrixH3Symbolic` factorization |
| `lepton_unconditional_stability` (same) | **sorry-typed non-statement** | replace type with `∀ n : ℕ, (0:ℝ) < q^n`; `fun n => pow_pos (by linarith) n` |
| `molecular_bond_instability` (same) | **sorry-typed non-statement** | needs real H₂ k=7 (2,1) Wedderburn-trace threshold stmt (q≈1.17) + the H₂ trace defs |
| `tilting_module_rigidity` (tilting-module-rigidity.lean) | real stmt, cited `sorry` | close via `Rigid.module_forces_words` given a bridge `IsCemeteryModule T → E.inCemetery (C.nodeOf T)` |

**Blocker:** in-sandbox `lake env lean` fails — `Mathlib.Data.Real.Basic.olean`
absent. `lake exe cache get` → 403; the `lake-cache/qou-v4-24-0` branch carries
only QOU oleans (813M), not Mathlib. Toolchain `lean-v4.24.0` IS installed and
symlinked to `/usr/local/bin`. **Recommended:** run in CI (Mathlib cache present)
or build Mathlib from source first.

## Remaining: D — drain compute (40) + detangler (54)

**compute (`todos/compute-integration-watcher-queue.json`, 40 queued):**
- **I1-proven-no-probe ×9** — write a probe + production consumer per block
  (compute-author skill). See `docs/audits/2026-05-19-i1-hecke-cluster-handover.md`.
- **I9-hardcoded-codata ×21** — route literals through the CODATA registry / mark
  Class-B/C/D exempt (canonical-watcher discipline).
- **I6 schema-drift ×2** (`per-pair-wedderburn`, `topic2-mirror-pair`) — fix the
  *producer* to emit dict-shaped `data` (not a list). **Overlaps PR #1878** — coordinate.
- **I2 mass-table + KLR ×5** — open Δ_λ / Rule-14 research (Track-A gate; do NOT
  fit a 7th ansatz per CLAUDE.md).
- **AGGREGATE cal-overcount / witness-provenance-i14** — real but scope-stale; re-run
  the full-corpus dashboards for current numbers.

**detangler (`todos/detangler-integration-watcher-queue.json`, 54 queued):** all
semantic/restructure — 3 logical cross-chapter fwd-refs, 20 sparse sections,
18 isolated blocks, 12 cross-chapter edge aggregates. Needs editorial judgment
(chapter-complexity-review + content-validation).

## Author decisions surfaced (6 UNSURE outcomes)
- `prop:borromean-hopf-energy-crossover`, `prop:eos-borromean-cfl` — analytic vs.
  needs-a-numerical-probe? (author call)
- `prop:neutron-prediction-comparison` — its `.lean` "validation" is **vacuous**
  (`stable_neutron_max_error` closes `∃n_obs` with `n_obs:=n_pred`); needs a real
  AME2020 witness + non-trivial theorem.

## Follow-ups (cheap)
- Add `boydvandenberghe2004` to `content/schema/references.ts` so the 3 SDP axioms
  that fell back to `[manuscript]` can upgrade to a published key.
- 9 **pre-existing** `validate-refs` errors (untouched files: MetallicPiecewise,
  JonesPolynomial, Scratch — bad keys `murakami1996`/`kauffman1987`/`audit`/`probe`/
  `metallichierarchy`); add the missing CSL entries.

## Acceptance criteria
- [ ] B: the 3 criticals proved/properly-stated, `lake build QOU` green.
- [ ] D-compute: I1×9 wired, I6×2 producer-fixed, I9×21 routed/exempted.
- [ ] D-detangler: fwd-refs + sparse/isolated sections resolved.
- [ ] CI green (or §5f flake documented); one-voice sweep on any prose touched.
