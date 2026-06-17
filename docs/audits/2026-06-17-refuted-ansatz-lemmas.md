# Refuted-ansatz lemmas — audit record (2026-06-17)

**Branch:** `claude/remove-deuteron-binding-prediction-2026-06-17`
**Principle (owner directive):** refuted-ansatz *lemmas* (lab-notebook
dead-ends recording that a specific construction the authors tried
*failed*) do not belong in the rendered paper — they belong here, in an
audit doc. **Formalize-first gates** (proved exclusion results of the
form "class C cannot work, here is the invariant that forbids it") are
legitimate paper content and **stay**.

A corpus sweep distinguished the two. This doc preserves the refutation
*records* for the material removed from the paper, and documents the
reclassification of three borderline blocks that turned out to be gates,
not dead-ends.

## Removed from the paper

### `rem:per-partition-k-lambda-rule` (was `mass-theory/per-partition-k-lambda-rule`)

A remark whose body is a refutation table: six candidate per-partition
`k_λ` selection ansätze, all empirically refuted:

1. **scalar-eigenvalue family** — refuted
2. **per-eigenvalue operator-valued** (uniform `k`) — refuted
3. **Type-B fold** — refuted
4. **multiplicity-refined** — refuted
5. **pair-knot product-volume** — refuted
6. **pair-knot Markov-trace** — refuted

The surviving open question — "does a structural `k_λ` / `n⋆` selector
exist?" — is **not** refuted; it is the open part of
[`conj:brane-tower-z-habiro`](../../content/quantum-observable-universe/mass-theory/brane-tower-z-habiro.md),
which the paper keeps as an honest open conjecture. Only the
failed-candidate enumeration moves here.

### Refuted `n⋆` families split out of `conj:brane-tower-z-habiro`

The brane-tower conjecture stays in the paper (it is an *open*
conjecture, not a refuted lemma, and is referenced by ~33 sibling
blocks). The conjecture asserts a canonical level-selection rule `n⋆`
*exists*; that existence claim is open. The empirical record of which
specific `n⋆` candidates were *tried and refuted* is moved here:

**Uniform-`k` sweep** (`probe_phiq_uniform_k.py`, atoms {D, T, ³He},
`k ∈ {1,2,3,4,5,6,8,10}`):

- **Absolute form** `B = m_e·ρ·(tr_M + tower^(k) + σ_{3A})` overshoots at
  every uniform `k`; error grows monotonically (+775 % at `k=1` to
  +1.27×10⁶ % at `k=10`). No uniform absolute-form `k` closes the gap.
- **Subtractive form** `B = E₀·(tower_free^(k) − tower_atom^(k))` has a
  sign-flip at `k=2`: `Δtower^(k=1) < 0`, `Δtower^(k≥2) > 0`. At `k=2`:
  B(D) ≈ +1.74 MeV (−22 %), B(T) ≈ +5.18 MeV (−39 %),
  B(³He) ≈ +18.05 MeV (+134 %).
- **³He overshoots at every `k≥2`** in subtractive form (two near-pole
  `|V̂| ≈ 0.989` entries vs D's one).
- **5 naive N=0 → N=1 structural lifts** all failed (PR #637 commit
  e1b005b2).

The sign-flip at `k=2` (smallest depth including the Hecke quadratic
slice `σ²=(q−q⁻¹)σ+1`) is recorded as a structural observation, not a
closure.

**Convergence half (the provable part).** Independent of `n⋆`, the
analytic statement that the brane tower `Φ_q(z) = ∏_{k≥1}(1−q^{-k}z)^{-1}`
is a well-defined positive real is being formalized in
[`PhiQConvergence.lean`](../../content/quantum-observable-universe/lean/QOU/MassEndomorphism/PhiQConvergence.lean)
(`summable_q_inv_geometric` + `quantumDilog_factors_nonzero` proved;
`Multipliable` in progress). This is the part of the conjecture that
*can* be promoted to a theorem; the `n⋆` half remains open.

## Reclassified as gates — KEPT in the paper

Two blocks the prose-scan flagged as dead-ends are in fact
exclusion/open-gate documentation that other blocks depend on:

- **`rem:alpha-em-derivation-open-problems`** — `em-coupling-projection.md`
  cites it specifically for *"the multiplicative-family ruling"*
  (block-diagonal Gram deformations **cannot** close the 1.55×10⁻³ α_EM
  gap). That is a proved exclusion result a sibling block leans on — a
  gate, not a dead-end. **Kept.**
- **`alg:delta-lambda-closure`** (`mba-sidecar-delta-lambda-closure`) —
  the appendix's honest open-gate documentation (title: "Track-A blocker
  — open gate"), under the mass-binding-algorithms sync contract;
  `mba-step09b-per-isotope-binding` cites it as the conjectural input.
  Open-problem documentation, not a refuted-lemma-as-result. **Kept.**

Net: **1 clean removal** (`per-partition-k-lambda-rule`) **+ 1 split**
(`brane-tower-z-habiro` refuted-`n⋆` material → this doc); the other two
candidates are gates and stay.
