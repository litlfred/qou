# Vacuity-defect fix playbook (95 genuine defects)

Companion to `docs/audits/2026-06-26-vacuity-candidate-triage.md` (the triage)
and `docs/audits/2026-06-26-vacuity-candidate-triage.json` (machine list). This
is the **how-to** for fixing the 95 genuine vacuity defects, written so a swarm
of agents (or humans) can each take a `.beans/` work-unit and execute it
self-contained. Every fix is **compile-verified**.

## Build environment (already set up; persists on disk)

```bash
export PATH="$HOME/.elan/bin:$PATH"
export no_proxy="127.0.0.1,localhost"; export NO_PROXY="127.0.0.1,localhost"
cd content/quantum-observable-universe/lean   # the qou Lake package
```

- Lean **4.24.0** + Lake via `elan`; Mathlib (rev pinned in `lakefile.toml`)
  **built from source** — 3097 oleans cached under `.lake/packages/mathlib`.
  The olean cache host is policy-blocked, so do **not** `lake exe cache get`;
  the source build is already done and incremental.
- `lake build <Module>` compiles a single module fast (deps cached). Module
  names mirror paths, e.g. `QOU.Archimedean.knot_operator_selection`.
- Many defect files are **orphan modules** not imported by the `QOU` root, so
  `lake build QOU` does not build them — build each **explicitly** by module
  name to verify.

## Verification loop (mandatory per file)

```bash
# 1. compile
lake build <Module>            # must end "Build completed successfully"
# 2. confirm the flag is cleared (from repo root)
bun run content/pipeline/lean-vacuity-axiom-audit.ts <path>.lean --json /tmp/v.json
#    → "0 defect candidate(s)"
```
Commit only after **both** pass. Never clear a flag by gaming the detector
(e.g. `by exact ⟨…⟩` instead of `⟨…⟩`) — that leaves the proof vacuous and
violates AGENTS.md §3b "No audit-dodging".

## The three fix patterns (each proven + verified)

### A. Mechanical-derive — concrete computational claims
When the claim is a real computation (a term count `= 12!`, a finite sum, a
decidable fact), **derive it** and isolate any empirical input as a hypothesis.
Exemplar: `QOU/Archimedean/PauliWitness/witness_12C.lean` —

```lean
class Witness12CPauli where
  F_Pauli : ℝ
  pauli_approx : |F_Pauli - 0.129| < 0.005      -- the lone open empirical input
theorem witness_12C [pauli : Witness12CPauli] :
    (6:ℕ)=6 ∧ (6:ℕ)=6 ∧ Nat.factorial 12 = 479001600 ∧ (12:ℕ)=12 ∧
    |pauli.F_Pauli - 0.129| < 0.005 :=
  ⟨rfl, rfl, by decide, rfl, pauli.pauli_approx⟩
```
Tactics: `rfl`, `by decide`, `by norm_num`. Never `native_decide` (adds
`Lean.ofReduceBool`). Never hardcode an observable as `x = x` — keep empirical
values as hypotheses.

### B. Genuine-formalize — claims reducible to real Mathlib structure
When the claim reduces to a real mathematical object Mathlib has, **formalize
it and derive**. Exemplar: `QOU/Archimedean/archimedean_braid_structure.lean` —
the braid image is `Dic₃`; formalize `Dic₃ := QuaternionGroup 3` (order 12 via
`QuaternionGroup.card`), carry the genuine categorical input as a group iso
`himg : G ≃* Dic₃`, and **derive** `Fintype.card G = 12` by
`(Fintype.card_congr himg.toEquiv).trans dic3_card`. Prefer this over C when a
faithful Mathlib structure exists (groups, polynomials, perms, etc.).

### C. Name the conditional conjecture — irreducibly abstract claims
Only when the claim is genuinely abstract over opaque/uninterpreted types and
no Mathlib structure applies: convert the fake `theorem … := ⟨ctx.claim_*⟩`
into `def name (ctx : Ctx) : Prop := <statement>` — honestly **names** the
conditional conjecture without faking a proof (§3b: "naming is not a logical
claim"). The context class is the carrier; an instance is the conjecture (none
= honest open state). This is the fallback, not the default — try B first.

Self-assuming projections (`:= ⟨ctx.claim_i, …⟩`): prefer B; else C.
`: True := trivial` / `X=X:=rfl`: prefer A (state the real computable prop);
if abstract, C. Placeholder-stub files: if a real formalization exists
elsewhere, point the `lean.ref` at it; else A/C as applies.

## Definition of done (per work-unit / bean)

- every listed file: `lake build <Module>` green **and** audit shows 0 flags;
- no new `sorry` unless cited (`-- Ref:`) per §3b "queue it";
- commit per cluster with the verification noted; push to
  `claude/ree-epsilon-lean-explain-knl2p0`.

## Done so far (templates to copy)

- `witness_4He`, `witness_8Be`, `witness_12C` — pattern A.
- `descartes_braid_structure` — pattern B (`Dic₃`).
