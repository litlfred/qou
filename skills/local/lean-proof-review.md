---
name: lean-proof-review
roles: [collaborator, owner]
description: >
  Review Lean 4 formalizations for mathematical soundness, statement integrity,
  vacuity freedom, §7c base-ring generality, and Mathlib4 / Lean Reservoir
  community style (`#lint`, `BP001`–`BP009`). Records structured verdicts in
  per-block `.qa.json` sidecars and `docs/audits/lean-vacuity-review-ledger.json`.
allowed-tools: Read Write Edit Bash Grep Glob
---

# Lean 4 Proof & Reservoir Style Review (`lean-proof-review`)

## 1. Overview (Sidecar & Ledger Architecture)

Reviews of `.lean` library modules and content-block siblings record verdicts in per-block **`<block>.qa.json` sidecars** (via [`folio/pipeline/qa-agent-entry.ts`](../../folio/pipeline/qa-agent-entry.ts)) and the standalone library ledger `docs/audits/lean-vacuity-review-ledger.json` (via [`folio/pipeline/lean-vacuity-axiom-audit.ts`](../../folio/pipeline/lean-vacuity-axiom-audit.ts)).

> **Purged legacy artifacts:** Do **not** read or write `proof-objects.json`, `chapters/*.tex`, or `agent_review.py` (`proof-objects.json` has been frozen since the content-object migration; see [`docs/audits/2026-06-03-proof-objects-json-extractor-broken.md`](../../docs/audits/2026-06-03-proof-objects-json-extractor-broken.md)).

---

## 2. Five Mandatory Review Dimensions

### Review Type 1 — Compilation & Kernel Trust (`lean-proof-check`)
- Type-checks cleanly under single-threaded `lean-overlay-env.sh` (`LEAN_NUM_THREADS=1 nice -n 15`; **never** bare `lake build` — see [`lean-build-hygiene.md`](lean-build-hygiene.md)).
- Kernel axiom check (`lean_verify` MCP or [`scripts/lean-axiom-guard.py`](../../scripts/lean-axiom-guard.py)):
  - **Tier-A / Tier-B Reservoir modules:** strictly `[propext, Classical.choice, Quot.sound]` ONLY (`0 sorry`, `0` custom `axiom`, `0` `Lean.ofReduceBool` / `native_decide`).
  - **QOU modules:** zero uncited `sorry` or `axiom`; no hidden axiom-in-instance laundering (`proof-no-axiom-class-laundering`).

### Review Type 2 — Mathlib4 & Lean Reservoir Best-Practices (`BP001`–`BP009` + `#lint`)
Run [`scripts/lean-best-practices-lint.py`](../../scripts/lean-best-practices-lint.py) (`--diff` or `--package <Pkg>`):
- **`BP001`:** `set_option autoImplicit false` present; zero `autoImplicit true`.
- **`BP002`:** `import`s precede `/-! ... -/` module docstring; Apache-2.0 copyright + `/-- ... -/` public declaration docstrings (`docBlame`).
- **`BP003`:** Minimal targeted `import Mathlib.<Module>` (zero bare `import Mathlib`, avoid `import Mathlib.Tactic`).
- **`BP004`:** `UpperCamelCase` structures/classes/inductives; `snake_case` theorems/lemmas (`_of_` suffix on conditional hypotheses).
- **`BP008` & `BP009`:** Zero upward `QOU.*` imports inside Tier-A (`MathlibExt`) and Tier-B (`HeckeTemperleyLieb`, `TwistedFrobeniusHopf`, `ToricConicOpt`, `CompactQuantumMetrics`, `QCalculus`, `BraidKnotOctonion`) modules; zero new ad-hoc synonym directories under `lean/QOU/`.
- **Mathlib4 `#lint` checks:** verify zero `docBlame`, `simpNF` (simp normal-form), `unusedArguments`, and `dupNamespace` warnings (`@[simp]` and `@[ext]` API completeness on new algebraic structures).

### Review Type 3 — §7c Base-Ring & Universe Generality (`BP005`, `BP006`)
- Algebraic and $q$-combinatorial identities stated over `{R : Type*} [CommRing R]` / `[Field R]` / `[LinearOrderedField R]`, never gratuitously over `ℝ`.
- Zero mixing of generic `[CommRing R]` and concrete `: ℝ` in the same file (`wall-side-correct`).
- Zero decimal literals (`1.1097`), `Float`, `CODATA`, or `substrate_q` in community libraries or pre-wall chapters.
- Category declarations universe-polymorphic: `(C : Type u) [Category.{v} C]`.

### Review Type 4 — Statement Integrity (`proof-statement-integrity`)
Adopted from AlphaProof Nexus `verify_integrity` + SafeVerify ([`docs/audits/2026-06-06-alphaproof-nexus-comparative-assessment.md`](../../docs/audits/2026-06-06-alphaproof-nexus-comparative-assessment.md)):
- **Unweakened signature:** For any touched `theorem`/`lemma` backing a `proposition`/`corollary`/`theorem`/`lemma` block, verify via `git diff origin/main...HEAD -- '*.lean'` that binders, hypotheses, and conclusion were **not** weakened to make the proof pass (unless explicitly approved by the author and mirrored in `.md` + `.ts` in the same diff).
- **Non-vacuity (`BP007` + [`lean-proof-vacuity-audit.md`](lean-proof-vacuity-audit.md)):** Confirm zero self-assuming projections (`:= d.claim_foo`), zero `: True` conclusions or fields, zero `Int`/`Bool` fake-Lean wrappers (`no-import-wrapper`), and zero `X - X = 0` definitional-subtraction tautologies (`sub-zero-tautology`).

### Review Type 5 — Content-Object Triple Equivalence (`proof-narrative-lean-equivalence`)
- `.ts` `lean.ref` (`"<pkg>:<Decl>"` in [`schemas/lean-packages.ts`](../../schemas/lean-packages.ts)) resolves to the reviewed Lean declaration.
- Sibling `.md` carries a substantive `**Proof.**` matching the Lean proof's mathematical structure (see [`proof-narrative-lean-equivalence.md`](proof-narrative-lean-equivalence.md)).

---

## 3. Standard CPU-Throttled Review Recipe

```bash
export LEAN_NUM_THREADS=1 RAYON_NUM_THREADS=1 OMP_NUM_THREADS=1 \
       OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1

# 1. Inspect signature diffs on provable declarations:
nice -n 15 git diff origin/main...HEAD -- '*.lean' | grep -E '^[-+][[:space:]]*(theorem|lemma|def|structure|class|axiom) ' || true

# 2. Run static Mathlib4/Reservoir + vacuity + import-boundary linter:
nice -n 15 python3 scripts/lean-best-practices-lint.py --diff

# 3. Check KG DAG cut-edge invariant:
nice -n 15 python3 scripts/lean-kg-detangler.py --summary-only

# 4. Type-check via isolated overlay (never bare `lake build`):
nice -n 15 bash scripts/lean-overlay-env.sh init
nice -n 15 bash scripts/lean-overlay-env.sh build QOU/<Subgraph>/<Module>.lean

# 5. Run vacuity & sidecar preflight:
nice -n 15 bash scripts/check-sidecars.sh
```

---

## 4. Verdicts & Checklist

| Verdict | Meaning |
|---|---|
| `APPROVE` | Type-checks, axiom-clean, `lean-best-practices-lint.py --diff` clean, §7c-general, non-vacuous, `.md` equivalent |
| `REQUEST_CHANGES` | Any critical/major defect (weakened statement, vacuity, `BP008` leak, gratuitous `ℝ`, compile failure) |
| `NEEDS_DISCUSSION` | Mathematical restatement or conjecture-demotion requiring owner decision |

- [ ] Compiled cleanly via `lean-overlay-env.sh` / `lean_diagnostic_messages` with `LEAN_NUM_THREADS=1 nice -n 15`
- [ ] `lean-best-practices-lint.py --diff` reports `critical=0` (`BP001`–`BP009`)
- [ ] Provable signatures unchanged vs `origin/main` (or author-approved restatement in `.md` + `.ts`)
- [ ] Kernel axioms verified clean (`[propext, Classical.choice, Quot.sound]` on proved claims)
- [ ] Verdict recorded in `.qa.json` sidecar / vacuity ledger
