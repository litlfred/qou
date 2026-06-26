# R5-full witness staleness + rescoped-TODO triage (2026-06-25)

Context: follow-up to the placeholder-bean resweep (PR #2799). The honest
counter (`scripts/count-actionable-placeholders.ts`) flagged 9 genuine
TODO/FIXME markers in the rescoped beans `b3pe` (Archimedean, 3), `95jh`
(BraidKnot, 5), `mlt7` (mass-endomorphism, 1). This doc triages all 9 and
records a **data-integrity finding**: the `³He` R5-full witness Lean values
are stale relative to the 2026-06-22-regenerated witness JSON.

## 1. Data-integrity finding — `Helium3Witness.lean` is stale

[`content/quantum-observable-universe/lean/QOU/BraidKnot/Helium3Witness.lean`](../../content/quantum-observable-universe/lean/QOU/BraidKnot/Helium3Witness.lean)
hardcodes values "from PR #608's `r5-full-canonical-knot-solver.witness.json`".
That JSON was **regenerated 2026-06-22** (commit `265a87a692`,
`regen(witness): item-2 pyhecke+scipy pass — 64 more producers → canonical`).
The current JSON ([`computations/r5-full-canonical-knot-solver.witness.json`](../../computations/r5-full-canonical-knot-solver.witness.json),
`data.per_atom_results`) no longer matches the frozen Lean values:

| field | Lean `Helium3Witness` (frozen, PR #608) | current JSON `he3` row (`per_atom_results[1]`) |
|---|---|---|
| `rho_star` | **3** | **4** |
| `alpha_gap` | 0 | 0.0 |
| `primal_obj` | 1 (**PLACEHOLDER**) | **0.14290601294812244** |
| `dual_obj` | 1 (**PLACEHOLDER**) | **0.14290601294812244** |
| `duality_gap` | (|p−d| = 0) | 0.0 |
| per-block min-eigs | 1.87 / 0.53 / 0.53 | not emitted in current summary |

The `per_atom_results[0]` row is labelled `atom="deuteron"` with `rho_star=3,
primal=dual=0.0023291934497948617`. The fact that the *deuteron* row's
`rho_star=3` equals the frozen Lean *He3* `rho_star=3` is a **coincidence**
(old-PR#608-he3 and new-regen-deuteron both happen to be 3), **not** an
atom-label swap — confirmed by the regen commit date post-dating the Lean
freeze.

**Why it matters / why a blind refresh is unsafe.** `Helium3Witness`'s
downstream `helium3StrictComplementarityCert` (and `AppliedHelium3Uniqueness`)
rely on the frozen all-positive min-eigs (empty active set ⇒ strict-interior
optimum). The current JSON summary does **not** emit per-block min-eigs, so a
refresh of `rho_star` 3→4 + `primal/dual` → 0.14291 must be checked against
whether the regenerated he3 optimum is still strict-interior. **Recommended:
refresh under the witnessed-values discipline only after the producer
re-emits per-block min-eigs**, or wire `primal/dual` to the JSON now and leave
`rho_star`/cert pending an explicit min-eig check. Tracked as a follow-up
(do not silently edit).

## 2. "Doesn't run for" root causes (Tritium / Deuteron)

Both are genuine **compute-infra gaps**, not Lean edits:

- **Tritium ([`TritiumWitness.lean`](../../content/quantum-observable-universe/lean/QOU/BraidKnot/TritiumWitness.lean), `rho_star=2` placeholder).**
  The H_5 Hoefsmit seminormal representation is implemented **only in Rust**
  (`tools/hecke-engine`); the Python pipeline that emits the witness JSON
  (`computations/hecke/hecke_characters.py`, H_3/H_4 only) cannot compute it.
  **Fix = port the H_5 Hoefsmit seminormal to Python** (or route the R5-full
  solver through the Rust engine for `tritium`). Substantial.
- **Deuteron ([`DeuteronWitness.lean`](../../content/quantum-observable-universe/lean/QOU/BraidKnot/DeuteronWitness.lean), `rho_star=1` placeholder).**
  The solver **does run**, but the single-term cost `B = m_e·ρ·|tr_M(T_w)|`
  under-constrains and returned a non-canonical winner `σ₂σ₁⁶σ₂⁻¹` (≠ the
  historical `6₂`). The current JSON `deuteron` row records that single-term
  result (`rho_star=3, primal=dual=0.00233`). **Fix = re-run with the full
  multi-term cost** (T2–T6 of `thm:knot-mass-formula-unified`), PR #608
  follow-up #1.

## 3. Triage of all 9 rescoped TODOs

| marker | bean | resolvable now? | blocker / path |
|---|---|---|---|
| `SnapPyAxioms`: `snappy_figure_eight_volume` | b3pe | no | needs `snappy_figure_eight_volume.py` producer (witnessed-values discipline) |
| `SnapPyAxioms`: `snappy_three_twist_volume` | b3pe | no | needs `snappy_three_twist_volume.py` producer |
| `BorromeanVolumeCatalan` §6 open-questions | b3pe | partial | #1 already discharged (stale framing); #2/#3 need a Mathlib Lebesgue-integral extension |
| `Helium3Witness` `primal_obj` placeholder | 95jh | partial | refresh from JSON `he3` (§1); cert min-eig check pending |
| `Helium3Witness` `dual_obj` placeholder | 95jh | partial | as above |
| `TritiumWitness` placeholder | 95jh | no | H_5 Hoefsmit Python port (§2) |
| `DeuteronWitness` placeholder | 95jh | no | multi-term cost re-run (§2) |
| `QBetaPerBlockChiClosedForms` order-3..7 Taylor coeffs | 95jh | **ALL DONE (3–7)** | `c₃ = −41/9` (explicit closed form) + `c₄ = 149/18`, `c₅ = −1729/108`, `c₆ = 111/4`, `c₇ = −3665/81` (via a new sorry-free **iterated-Leibniz recurrence** `iteratedDeriv_mul_eq_sum` on `f·D = N`, since Mathlib v4.24 lacks it + `iteratedDeriv_pow`/`ContDiffAt→DifferentiableAt(iteratedDeriv)`). 5 reusable private helpers added |
| `qbeta-per-block-chi-closed-forms` (mass-endo duplicate) | mlt7 | (sibling) | same `delta_tau_M_surrogate` content; apply the same infra |

## 4. Recommendations

1. **He3 stale witness** — refresh `Helium3Witness.lean` to the 2026-06-22 JSON
   `he3` row, gated on the producer re-emitting per-block min-eigs (so the
   strict-complementarity cert can be re-derived rather than assumed). File a
   data-integrity bean.
2. **Tritium / Deuteron** — keep the explicit, non-`instance` placeholders;
   they correctly signal the H_5-Hoefsmit / multi-term-cost dependencies. Close
   only when those compute tasks land.
3. **QBeta order-3..7 — ALL formalized sorry-free on this branch.** Order-3
   `c₃ = −41/9` via the explicit closed-form template
   (`delta_tau_M_surrogate_taylor_coeff_3`). **Orders 4–7 now also proved**
   (`delta_tau_M_surrogate_taylor_coeff_4..7`: `149/18`, `−1729/108`, `111/4`,
   `−3665/81`) — the explicit template caps at order-3 (order-4 needs the
   degree-≈57 `deriv3`), so orders 4–7 use a **general iterated-Leibniz
   recurrence** built from scratch: `iteratedDeriv_mul_eq_sum` (Leibniz, by
   induction + Pascal reindex), `iteratedDeriv_pow_eq` (monomial), a
   `ContDiffAt`-local `DifferentiableAt (iteratedDeriv …)` helper, and a
   polynomial-iterated-derivative-at-1 evaluator — all of which Mathlib v4.24
   lacks. The recurrence `Σ C(n,k)·f⁽ᵏ⁾(1)·D⁽ⁿ⁻ᵏ⁾(1) = N⁽ⁿ⁾(1)` recovers each
   `f⁽ⁿ⁾(1)` from the lower derivatives. Cross-checked against the witness JSON.
   The 5 helpers are reusable (candidates for upstreaming).
4. **SnapPy / Borromean §6** — leave; gated on producer scripts / Mathlib
   integration infra.

Net: of the 9 rescoped markers, the **2 QBeta Taylor-coefficient items are now
fully resolved** (orders 3–7 proved sorry-free, including a from-scratch
iterated-Leibniz infrastructure that backfills a real Mathlib gap); the
remaining 7 are gated on compute-infra (Tritium/Deuteron), producer scripts
(SnapPy), a Mathlib Lebesgue-integral extension (Borromean §6), or a
data-integrity decision (He3). The headline remaining actionable item is the
**He3 stale-witness refresh** (§1).
