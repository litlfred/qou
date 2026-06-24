# Devil's-advocate audit — Wave 3 (structural / proof core)

**Watcher:** [`local/devils-advocate-watcher`](../../.claude/skills/local/devils-advocate-watcher.md)
**Date:** 2026-06-24 · **Branch:** `claude/lucid-gates-92e98s`
**Model:** claude-opus-4-8 · L1 formalist + L2 skeptical physicist + L3 algebraist + L4 reproducibility/citation + adjudicator.

Wave 3 attacks the structural/proof core: the operator-selection LP, the Wedderburn decomposition step, the Yekutieli non-abelian Stokes step, the Hecke-from-braiding construction, and the archimedean-functor uniqueness. As before, `da-referee-verdict: open-objection` means *a referee argument survived rebuttal*, not that the block is proven false.

## Results

| Block | Verdict | Strongest objection |
|-------|---------|---------------------|
| [`operator-selection-lp`](../../content/quantum-observable-universe/mass-theory/operator-selection-lp.md) | **🔴 open-objection** | The mandated LP **dual certificate** (`y0_star`/`y_star`/`active_set`/`duality_gap`) is emitted with **`null` values** in the confinement witness — the validator checks key *presence*, not non-null, so it passes CI while the `.md`'s active-set `{σ₀, L₋}` is unbacked by any computed dual. |
| [`mba-step05-wedderburn`](../../content/quantum-observable-universe/appendix-mass-binding-algorithms/mba-step05-wedderburn.md) | 🟡 survivable | `.md` calls `wedderburn_weight()`'s output the "Wenzl–Markov `y_λ`", but it computes `w̃_λ = dim_q²/[n]_q!` (equal only on self-conjugate λ — the §7aa weight-family conflation); witness contract misdescribed. |
| [`archimedean-functor-uniqueness`](../../content/quantum-observable-universe/mass-theory/archimedean-functor-uniqueness.md) | 🟡 survivable | Prose claims uniqueness on **ℂ∖{0,1}** via the complex Bloch–Wigner `D`, but the Lean proves a weaker **real-slice `ℝ→ℝ`** statement and the §3b-cond banner overstates which classes gate it (`ArchimedeanLimit` is absent from the signature). |
| [`archimedean-yekutieli`](../../content/quantum-observable-universe/brings-surface/archimedean-yekutieli.md) | 🟡 survivable | Cheat-sheet markets "Step 2 Stokes ⇒ Hecke ✅ proved", but `NonAbelianStokes.lean` is a self-confessed vacuous `True`-skeleton and the Hecke quadratic is H_n(q)'s *defining* relation (from the R-matrix), not derived from Stokes. |
| [`hecke-algebra-from-braiding`](../../content/quantum-observable-universe/braids-and-knots/hecke-algebra-from-braiding.md) | 🟡 survivable | Writes the Hecke relation on `T = τ(c_{V,V})` (§7a bans `T` as the generator symbol) while the quotient ideal uses `σ_i` — internally inconsistent, minor. |

## Highlights

- **`operator-selection-lp` (open).** The headline find of wave 3 and a **new** one (grep of `docs/audits/` + `docs/coordination/` shows it was never flagged). AGENTS.md makes the LP/SDP **dual** first-class infra — the shadow prices *are* the binding-energy structure. Here the witness emits the dual keys with `null` values, and `lp_dual_witness_validator.py` only checks *presence*, so it passes CI while computing no dual at all; the `.md` active-set claim is therefore unbacked. → **Author-assist + tooling:** recompute the dual (route through `lp_dual_solver.py`) and tighten the validator to reject `null` dual values (a one-line `--strict` upgrade that would have caught this).

- **`mba-step05-wedderburn` (survivable, 2 major).** Two appendix maintenance-contract drifts — exactly what the §"appendix sync" rule exists to catch: the documented Python API conflates the Wedderburn–Plancherel weight `w̃_λ = dim_q²/[n]_q!` with the Wenzl–Markov `y_λ` (distinct at `q≠1` per §7aa), and the named witness records EW-sector LP probes rather than the per-partition `(d_λ, y_λ)` table the `.md` claims. The underlying math is sound and in-regime (semisimple at `q₀>1`).

- **`archimedean-functor-uniqueness` (survivable, 2 major).** The Lean theorem is genuine, sorry-free, and non-vacuous — but it proves a real-slice (`ℝ→ℝ`) uniqueness-up-to-scalar, while the prose advertises complex Bloch–Wigner uniqueness on ℂ∖{0,1} (the version that actually pins the hyperbolic volume) and claims two class hypotheses gate it when only `BlochSuslinUniqueness` does. The single real DOF (the scalar) is honestly named and pinned — *not* a hidden-DOF violation.

- **`archimedean-yekutieli` (survivable).** The objection is a **status-label** overclaim in the coordination cheat-sheet ("✅ proved") against a §3b-cond `True`-skeleton, not a false theorem in the target `example` block (which stays within policy: q symbolic, interprets a conjecture). The genuine finite-slice ordered-product content *is* proved.

- **`hecke-algebra-from-braiding` (survivable, minor).** A `remark` block; the construction (quotient by the two-factor minimal polynomial, braid relations retained, eigenvalues `q, −q⁻¹`) is correct. Only the `T`-vs-`σ_i` notation inconsistency survives.

## Disposition

- **Author-assist + tooling (queued):** `operator-selection-lp` null-dual witness (recompute dual + harden `lp_dual_witness_validator.py` to reject null values).
- **Auto-discharge candidates (doc-sync, deferred to author):** `mba-step05-wedderburn` API/witness-contract wording; `archimedean-functor-uniqueness` §3b-cond banner + ℂ→ℝ re-scope; `hecke-algebra-from-braiding` `T`→`σ_i` notation; the cheat-sheet "✅ proved" → "✅ (§3b-cond conditional)" label. These touch prose/notation/status framing — surfaced for author judgement, not auto-applied (math-adjacent).

## Running tally (waves 1–3, 14 blocks)

**3 open-objection · 9 survivable-objection · 2 clean.** Recurring failure classes the adversary has now surfaced three times each:

1. **Durable artifact ⟂ narrative** — `.lean`/`.ts` encodes a claim the `.md` disavows or weakens (λ_scale revival; retracted ratio form; real-slice Lean vs complex prose; §3b-cond banner vs actual signature).
2. **Status-label / tag overclaim** — "✅ proved" / "no-fitting" / "closed form" / "verified" applied to §3b-cond skeletons, near-matches, or empty-assertion witnesses.
3. **Witness hollowness** — empty assertion arrays or `null` dual values that pass presence-only CI checks.

Each is a candidate for a *targeted* mechanical sweep (a script checker could catch #2 and #3 cheaply).
