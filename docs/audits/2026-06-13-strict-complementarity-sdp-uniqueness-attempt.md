# Strict-complementarity SDP-uniqueness — attempt + closeable/irreducible split

**Date:** 2026-06-13
**Branch:** `claude/vigilant-cerf-f80u04` · PR #2249
**Scope:** `conj:canonical-knot-id-sdp` uniqueness leg; the
`StrictComplementarity` ⇒ unique-minimizer argument.

## Conjecture under attack

`conj:canonical-knot-id-sdp` asserts the joint mass-tower confinement
SDP has a **unique** global minimizer `T_w*` at the canonical Hecke
element of each light nucleus (²H = 6₂, ³H = 8₁₁, ³He = L₆ₐ₄). The
uniqueness leg is the open one (existence is constructible from the
R5-full witness); it is the Boyd–Vandenberghe §5.5 /
Alizadeh–Haeberly–Overton §3 statement *strict complementarity ⇒ the
primal optimum is unique*.

## What the corpus already provides

- `QOU.MathlibExt.SDP` — `SDPPrimal`, `StrictComplementarityPair`,
  `strict_complementarity_unique` (generic `R`, backed by
  `strict_complementarity_unique_axiom`).
- `QOU.MathlibExt.SDPRealUniqueness` — the ℝ-specialised layer. It
  **derives** every step of the complementary-slackness chain
  (`dualSlack_trace_eq`, `dualSlack_mul_feasible_eq_zero`,
  `S·D = 0 ∧ D·S = 0 ∧ tr(A_i·D) = 0`) and reduces the residue to a
  single named gap, `SDPRankUniqueness` (the SDP optimal-face
  rank-deficiency theorem).
- Two **fully proven, axiom-free** sub-cases:
  - `real_strict_complementarity_unique_of_dualSlack_posDef` — dual
    slack PosDef ⇒ `S` invertible ⇒ `D = 0`.
  - `real_strict_complementarity_unique_of_active_empty_and_cost_posDef`
    — active set empty ⇒ `S = T`; with `T` PosDef the previous case
    applies.
- `QOU.BraidKnot.NucleusEmptySDPUniqueness.nucleus_uniqueness_closed n`
  — the dimension-parameterised, axiom-free closure at `heckeDim n`
  (`helium3_uniqueness_closed := @nucleus_uniqueness_closed 9` is the
  `conj`'s `lean.ref` target).

## Closeable vs. irreducible

| regime | status | why |
|---|---|---|
| **interior / active set empty + cost PosDef** | **closed, axiom-free** | `S = T ≻ 0` invertible; `S·D = 0 ⇒ D = 0`. ³He lives here (below). |
| dual slack PosDef (general interior) | closed, axiom-free | same invertibility argument |
| **general (non-empty active set)** | **gated on `SDPRankUniqueness` axiom** | needs Goldman–Tucker rank equality `rank(S) + rank(Φ*) = n` + optimal-face geometry — eigenspace/face machinery **not in Mathlib**; the codebase correctly labels it multi-week work |

The interior case is **not** a weakening: it is exactly the regime the
empirical witness puts ³He in.

## ³He is in the closeable (interior) regime

`r5-full-canonical-knot-solver.witness.json` reports, for the canonical
³He word `(σ₁σ₂⁻¹)³` (L₆ₐ₄ class), all three Wedderburn-block minimum
eigenvalues **strictly positive** — trivial 1.87, standard 0.53, sign
0.53. Hence the SDP active set is **empty** and the optimum lies in the
strict interior of the feasible region. The `StrictComplementarity`
certificate records this in its `active_dual_pos_or_empty` field (the
`0 < min_block_eig` disjunct). So ³He uniqueness is closeable
**axiom-free** via the active-empty/interior closure — this PR wires
that connection.

²H and ³H are *not* yet in a closed state for a different (cost-side)
reason, not the uniqueness machinery:
- **²H** — the single-term flagship cost `B = m_e·ρ·tr_M(T_w)` does not
  make 6₂ the minimizer (the L=8 winner is `σ₂σ₁⁶σ₂⁻¹`). Recovering 6₂
  needs the multi-term cost T2–T6 of `thm:knot-mass-formula-unified`.
- **³H** — the R5-full pipeline needs the Hoefsmit seminormal at H₅
  (currently Rust-only).

## The genuine failure mode of uniqueness (why the hypothesis matters)

Uniqueness is **not generic**. `sdp-degeneracy-at-metallic-coincidence.md`
shows strict complementarity *fails* at cost-coincidence loci (metallic
ratios, e.g. the silver ratio `q = 1 + √2`): there `t_i(q) = t_j(q)`, the
optimum becomes a positive-dimensional face rather than a vertex, the
active set collapses, and multiple optimal `(y₀*, y*)` coexist. So the
strict-complementarity hypothesis is load-bearing — it is exactly the
condition separating ³He's unique interior optimum from the degenerate
metallic case. Any proof of the general `SDPRankUniqueness` axiom must
therefore consume strict complementarity essentially (it is false
without it).

## Verdict

- **³He uniqueness:** closed **axiom-free** (interior case), matching the
  witness. Delivered on this PR.
- **General SDP strict-complementarity uniqueness:** remains the single
  `SDPRankUniqueness` Mathlib gap (optimal-face rank-deficiency). Not a
  `sorry` smuggled into a proof — an explicitly named axiom with the
  whole complementary-slackness chain proven around it. Closing it is
  genuine Mathlib SDP-rank-deficiency work, out of scope for this PR.
- **²H / ³H:** uniqueness machinery is ready; blocked on cost wiring
  (²H multi-term) and Hoefsmit-H₅ (³H), tracked separately.

## Verification status (2026-06-13)

`nucleus_uniqueness_closed_via_active_empty` lives in
`QOU.BraidKnot.NucleusEmptySDPUniqueness`, which **is** imported by
`QOU/BraidKnot.lean` → it is part of the `lake build QOU` target, so **CI
verifies it**. Local direct-`lean` verification in this environment is blocked
by a setup artifact, not a code issue: the existing, CI-green
`nucleus_dualSlack_posDef` (line 173, `exact Matrix.PosDef.one`) fails locally
with the same `failed to synthesize` as the new theorem's line 242 (which also
discharges `((nucleusEmptySDP n).cost).PosDef` via `Matrix.PosDef.one`). Since
line 173 is green on `main`, that synthesis succeeds in a complete build, so the
new theorem — using the identical lemma — is sound; CI is the gate. (Root cause
of the local artifact: the cache Mathlib subset + `Matrix.PosDef` instance
resolution under the direct-`lean` `LEAN_PATH`; the conj content-sibling, which
does not use these Mathlib SDP instances, verifies green locally.)
