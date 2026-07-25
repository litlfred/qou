# α_EM B2/R2 consolidation — R2-core landed + τ-identification pickup (2026-07-25)

**Context:** owner directive: *"1 / 2 but 4080 agent is stalled. pick up the work.
merge/cherrypick/manual use / consolidate."* Executed: (1) PR #4080 rebase-merged;
(2) the stalled epic `qou-6ufi` (τ-identification) picked up — the sibling's three
merged sorry-free Lean results consumed manually (no unmerged branches existed to
cherry-pick), Options A+C advanced by a new probe; (3) this consolidation.
Standing ruling respected throughout
([`2026-07-19-alpha-em-r2-owner-ruling.md`](2026-07-19-alpha-em-r2-owner-ruling.md)):
the per-loop identification is **not** derived-proved; `1/(8π)` stays phase-4;
nothing wired.

## 1. What merged (this tranche)

- **PR #4080** (`SchwingerMeasureShape.lean` + r2core probe): R2-core restated
  corpus-natively — *"the loop measure assigns one nat per proper-time e-fold
  (k_B = 1)"* — with its provable shell sorry-free (shape rigidity, nat reading,
  E-Jacobian 2, `c = 1` assembly) and the **new open ½-adjudication** (ρ-split vs
  E-Jacobian; each alone → `1/(8π)`, both → `1/(16π)` excluded).

## 2. The sibling's τ-identification results (epic `qou-6ufi`, merged before stall)

| Lean module (sorry-free) | Result |
|---|---|
| `LoopWeightRealSymmReduction` (#4151) | the B2 lift needs only **real + symmetric** — PSD/Gram positivity is surplus |
| `MarkovGramRealSymm` (#4154) | real+symmetric **discharged Markov-side**: any symmetric ℝ-bilinear form's Gram is symmetric; witness `SpechtIrreducible.bilinM_isSymm` |
| `SchurInvariantFormProportional` | **Option-B core**: commutant-scalar (Schur) ⟹ any two invariant forms proportional (`invariantForm_proportional_of_commutantScalar`) |

Stall point: the epic's five task beans all `todo`; open sub-pieces after B were
(i) S₅-equivariance of the τ-image on `std`, (ii) the scalar `c`.

## 3. The pickup (this PR) — Options A+C support probe

[`alpha_em_b2_tau_id_c_pin_probe.py`](../../computations/alpha_em/alpha_em_b2_tau_id_c_pin_probe.py)
(+ witness, 7/7):

- **Option A closed at first order**: the `(4,1)` std block of `H₅(q)` pinned
  concretely as rescaled reduced Burau `ρ(σᵢ) = −q⁻¹·Bᵢ(q²)` — braid + Hecke
  relations self-validated symbolically, not assumed.
- **The Schur hypothesis is concrete**: commutant dimension = 1 at exact q₀ (and
  at q = 1) — the exact `schur` hypothesis of the sibling's Option-B Lean core,
  instantiated at the actual α_EM block.
- **The Markov Gram, exactly**: the associative-form space (`G·ρ = ρᵀ·G`,
  symmetric) is **1-dimensional** at q₀; the generator `G_M` has exact rational
  entries — real + symmetric explicit (the Markov-side discharge realized), with
  positivity confirmed as the **bonus** #4151 says is unneeded.
- **Classical shadow**: at q = 1 the deck 4-cycle `(2345) = s₂s₃s₄` has eigenvalues
  `{1, i, −1, −i}` on `std` — the F-construction T2 dictionary tying this block to
  the `H^{1,0}(Bring)` carrier.
- **Option C, the honest half**: the Hodge Gram's `(3,1)` pattern
  `diag(5,5,5,1)·Im(τ₀)` (Braden–Northover isogeny frame) is **recorded**, and the
  frame obstruction **named**: that frame is not S₅-equivariant, so an entrywise
  ratio against `G_M` would be frame-dependent numerology. The scale `c` is
  extractable only through the S₅-equivariant transport — exactly Option B's open
  premise (i). **No ratio tuned; none reported as `c`.**

## 4. Consolidated wall status (one statement)

> `α_EM = [2]_q·(1 − h²α)` with per-loop measure `1/(8π)` is **derived conditional
> on R2; R2 is open** (owner ruling 2026-07-19). After this tranche R2's open
> content is exactly:
> 1. **R2-core** — one unit convention: *"one nat per proper-time e-fold
>    (k_B = 1)"* (same species as `discrete-planck-step`), + the ½-adjudication
>    (ρ-split vs E-Jacobian — which e-fold variable the convention counts).
> 2. **The τ-identification** — `W = complexify(Markov Gram at q₀)` on
>    `H^{1,0}(Bring) = std`, now reduced by Schur (sorry-free) + the exact `G_M`
>    to: (i) S₅-equivariance of the τ-image, (ii) the scalar `c`.
>
> Everything else — shape rigidity, nat reading, E-Jacobian, assembly, reality,
> symmetry, PSD-surplus, Schur proportionality, the concrete block and Gram — is
> machine-verified (sorry-free Lean or exact symbolic witness).

## 5. Next steps (priority)

1. **B(i) equivariance**: relate `bilinM_rep_invariant` (Hecke-side) to the
   S₅-action through the q → 1 / seminormal specialization — candidate Lean
   brick.
2. **C scale transport**: construct the S₅-equivariant frame on the period side
   (deck-eigenbasis refinement of the isogeny frame) and extract `c` honestly.
3. **E (mechanical)**: land the `MarkovTrace` general-n instance via the Ocneanu
   cyclicity bricks (#4126/#4110) — unblocks `TauFunctorReduction` F-laws.
4. Owner adjudications (unchanged, owner-level): the ½ reading; canonization of
   R2-core.

## Cross-references

- Attack plan: [`2026-07-24-alpha-em-b2-tau-identification-attack-options.md`](2026-07-24-alpha-em-b2-tau-identification-attack-options.md)
- R2-core: [`2026-07-19-alpha-em-r2core-schwinger.md`](2026-07-19-alpha-em-r2core-schwinger.md)
- Ruling (read-first): [`2026-07-19-alpha-em-r2-owner-ruling.md`](2026-07-19-alpha-em-r2-owner-ruling.md)
- Ledger: [`../coordination/alpha-em.md`](../coordination/alpha-em.md)
