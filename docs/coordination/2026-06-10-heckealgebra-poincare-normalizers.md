# Coordination ledger — HeckeAlgebra H₃(q) Poincaré-normalizer reconstruction

Goal: turn `QOU/Mathlib/HeckeAlgebra.lean` green by fixing the Wedderburn
idempotency math bug diagnosed in PR #2088; document the normalizer
convention paper-side.

## Sessions

### 2026-06-10 — pickup + reconstruction (PR #2091, `claude/awesome-sagan-br883o`)

- **Pickup context.** PR #2088 (branch `claude/heckealgebra-finish-2026-06-09`)
  stalled after pushing only its diagnosis commit; the in-container
  Poincaré reconstruction edits were lost with the container. #2091
  cherry-picked the diagnosis commit and redid the reconstruction from
  the transcript + first principles. #2088 closed in favor of #2091
  (owner-approved).
- **The math.** Trivial-block projector forces normalizer
  `P(q) = Σ_{w∈S₃} q^{2ℓ(w)} = 1+2q²+2q⁴+q⁶ = (1+q²)(1+q²+q⁴)`;
  sign block forces `P(q⁻¹)`; `P ≥ 1 > 0` unconditionally
  (`H3.poincare_pos`). Relation to the balanced factorial:
  `P(q) = q^{ℓ(w₀)}·[3]_q!` — using bare `[3]_q!` for both blocks was
  the bug. Only `q ≠ 0` survives as hypothesis.
- **Lean outcome.** `lake build QOU.Mathlib.HeckeAlgebra` exit 0
  (3088 jobs); 4 standalone sorry-free theorems (`H3.blockSym3_sq`,
  `H3.blockAlt3_sq`, `H3.blockMixed21_sq`,
  `H3.blockSym3_blockAlt3_orthogonal`) + thin
  `H3WedderburnIdempotency_canonical`; H₄ Markov witness and two
  `No goals` residuals fixed; zero `sorry` in the module.
- **Tactic gotchas recorded** (audit-doc Resolution section):
  (1) one `instance … where` = ONE declaration = one heartbeat budget
  across all field proofs — split heavy fields into standalone
  theorems; (2) sequential `unfold A B C` does not revisit occurrences
  exposed by later entries — use `simp only [defs]` for fixpoint
  unfolding; (3) `simp` normalizes `(⟨6,⋯⟩ : Fin 24)` to the `Fin`
  literal — state hypotheses at the literal or bridge by defeq `have`.
- **Paper-side.** Normalizer convention documented in
  `rem:h3-hecke-idempotents` (braids-and-knots), QA sidecar refreshed
  (scoped to the one block; chapter-wide sweep churn reverted).
- **Cross-PR coordination.**
  - #2087 (full-lib repair) merged mid-flight; absorbed by rebase.
  - #2094 / #2095 (repair-thread continuations): notified that
    `Mathlib/HeckeAlgebra.lean` is green here and that
    `BraidKnot/H3HeckeIdempotents`'s "unterminated comment" red root
    is fixed on this branch (nested `/-` from the docstring text
    `q/-q⁻¹` — grep pattern `q/-` for siblings). `Archimedean/HeckeH3`
    deliberately NOT touched (remains in the repair tranche).
  - Follow-up filed: issue #2098 — H₄ projector placeholders still
    carry the balanced normalizer; fix = `P₄(q) = Σ_{w∈S₄} q^{2ℓ(w)}`
    when real coefficient tables get wired.
- **CI.** All pushes hit the GitHub Actions billing signature
  (4 checks, ≤5 s, simultaneous; 6 consecutive rounds verified by
  check-run timings). Local gates (`lake build`, `bun run validate`)
  green throughout; no retrigger commits.
