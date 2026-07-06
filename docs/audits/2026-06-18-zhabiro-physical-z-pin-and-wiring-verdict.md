# z-Habiro / Φ_q wiring — physical-z pin + production-wire verdict

**Date:** 2026-06-18
**Branch:** `claude/great-babbage-4vngb1`
**Continues:** PR #2460 (numerical Φ_q bridge) roadmap **step 1** —
"pin the physical z (`|V̂_i|`), replace the representative `ℏ_q²`."
**Verdict:** the physical z is *already pinned in the corpus*; pinning it
**confirms the wire is blocked, not enabled**. The merged z-Habiro Lean
(#2447) + the numerical bridge (#2460) are a valid checkpoint for the
**algebraic Cauchy-limit** half only; they have **no non-regressing
production continuation**.

## 1. The question

PR #2460 verified the merged z-Habiro Lean numerically at q₀ (`eulerCoeff`
recurrence 6e-57; `eulerTrunc = Σ cₘ Pₘ` 2e-51) and flagged that the
N=0 → Φ_q correction is **9.36 %** at the *representative* scale `z = ℏ_q²`,
"so the physical brane-tower variable z (`|V̂_i|`) differs from this scale."
Roadmap step 1 was to pin the real z and decide the production wire.

## 2. The physical z is `|V̂_i^full|` — already pinned (corpus-grep result)

The brane-tower argument is **not** an open quantity. It is

> `z_i = |V̂_i^full|` = the **additive Wedderburn traced volume per generator**
> ([`def:algebraic-quantum-volume`], the argument of the dilog in
> [`prop:mass-endomorphism-tower`]).

It is computed in production at 50 dps and bounded **< 1** (the `full`
channel). Exact values (from `terms-2-3-atom-per-gen-mpfr-50dps.witness.json`,
the source that "feeds `mass_formula_6term_mpfr_50dps.term_23_brane_tower_mp`",
+ `mass-endomorphism.witness.json` for the electron):

| particle | per-generator `|V̂_i^full|` | max |
|---|---|---|
| electron | 0.59385 | 0.594 |
| proton | 0.98901, 0.97107 | 0.989 |
| neutron | 0.85421, 0.97551 | 0.976 |
| deuteron | 0.98901, 0.97107, 0.26415, 0.85421, 0.97551 | 0.989 |
| tritium | …, 0.15961, 0.85421, 0.97551 (8 gens) | 0.989 |
| helium-3 | …, 0.36868, 0.98901, … (8 gens) | 0.989 |

These match the conjecture's stated `z_i ∈ [0.85, 1.0]` for the near-pole
generators. `ℏ_q² ≈ 0.0098` is **two orders of magnitude smaller** than the
physical z — PR #2460's "9.36 % ≠ 0.75 %" observation was the symptom of that
gap. **The physical z was never unknown; it was a representative-scale
mismatch.**

> **Retraction note (do not reuse).** `spectral-coordinates-all-atoms.witness.json`
> reports `V_hat` values **> 1** (1.88, 1.70, …). Those are *Hoefsmit
> matrix-product eigenvalues*, **RETRACTED 2026-05-27** — they are NOT the
> additive Wedderburn traced volumes used in the tower. Use the `full` channel
> above.

## 3. At the physical z, Φ_q regresses; the production −Li₂^q is bounded

Probe [`computations/probes/zhabiro_physical_z_pin.py`] (mpmath 50 dps,
witness `zhabiro-physical-z-pin.witness.json`) evaluates both forms at each
exact physical z_i:

- **Φ_q(z) = ∏(1 − q^{−k} z)^{−1}** — Faddeev, the **SUPERSEDED**
  `brane-legacy` tower mode.
- **−Li₂^q(−z) = Σ (−1)^{n+1} z^n /(n·[n]_q)** — symmetric, the **PRODUCTION**
  `li2q` tower mode (`prop:mass-endomorphism-tower`; sweep default).

| atom | max `|V̂_i|` | max Φ_q(z_i) | max −Li₂^q(−z_i) | Φ_q / Li₂^q |
|---|---|---|---|---|
| electron | 0.5938 | 629.9 | 0.524 | 1.2 × 10³ |
| proton | 0.9890 | 6.71 × 10⁵ | 0.815 | 8.2 × 10⁵ |
| neutron | 0.9755 | 4.75 × 10⁵ | 0.806 | 5.9 × 10⁵ |
| deuteron | 0.9890 | 6.71 × 10⁵ | 0.815 | 8.2 × 10⁵ |
| tritium | 0.9890 | 6.71 × 10⁵ | 0.815 | 8.2 × 10⁵ |
| helium-3 | 0.9890 | 6.71 × 10⁵ | 0.815 | 8.2 × 10⁵ |

Probe cross-checks (all pass) anchor the implementation to production:
- `Φ_q(ℏ_q²) − 1 = 9.35979 %` ✓ reproduces PR #2460's 9.36 %.
- `Φ_q(0.59385) = 629.93542` ✓ reproduces `mass-endomorphism.witness.json`
  electron `single = 629.9354`.

**Why Φ_q "passes" m_p/m_e (1.84 %) yet is pathological.** The huge
per-generator Φ_q values largely *cancel in the m_p/m_e ratio* (both legs
diverge together → 1869.85 vs 1836.15). They do **not** cancel in
isospin-sensitive observables: at q₀ the Φ_q divergence near `|V̂_i| → 1`
amplifies tiny p/n asymmetries into hundreds of MeV — the mirror-nucleus
prediction T − ³He ≈ **−737 MeV** vs CODATA +0.019 MeV
(`brane-tower-isospin-diagnosis.witness.json`). That pathology is why
`prop:mass-endomorphism-tower` was revised to `−Li₂^q(−|V̂_i|)` and the Φ_q
product survives only as a diagnostic.

**In-corpus regression proof.** `vhat-std-vs-full-tower-compare.witness.json`
already records that the `std` channel (where `|V̂₀| = 1.146 > 1`) gives
`T2_single = +inf → m_p = +inf`, verdict **"REGRESSES"**. Any evaluator that
is unbounded as `z → 1` (Φ_q, or any z ≥ 1) is structurally excluded.

## 4. The real blocker is n⋆, and it is refuted

A *truncated* Φ_q could in principle stay finite — but only with a canonical
level-selection rule `n⋆` (the truncation depth per particle). That rule is
the open part of [`conj:brane-tower-z-habiro`], and **all six probed families
are refuted** (`docs/audits/2026-06-17-refuted-ansatz-lemmas.md`;
`brane-tower-z-habiro.lean :: nStar_all_probed_forms_refuted`): scalar
uniform-`k`; scalar `ℓ·n₀+k`; per-eigenvalue operator-valued; multiplicity /
Type-B fold; pair-knot product-volume; pair-knot Markov-trace (Gram + SDP).
The ³He gap is a **structural deficit** of the brane-tower formula at the
`A=3 / n₀=9` regime, not an operator-volume choice.

## 5. Verdict on the wire (roadmap steps 2–3)

- **Step 1 (pin z): DONE** — `z_i = |V̂_i^full| < 1`, exact values §2.
- **Step 2 (route per-generator Φ_q through canonical compute): BLOCKED** —
  it regresses (§3); production already uses the bounded `li2q` form.
- **Step 3 (validate dashboards without regressing): UNREACHABLE** as a Φ_q
  wire — the only rescue (`n⋆`) is refuted (§4).

The bridge in #2460 remains correct and useful: it is the **Lean ↔ numeric
checkpoint for the algebraic Cauchy-limit infrastructure** (the surviving half
of the conjecture). It does not, and should not, feed the production mass
table.

## 6. Productive next steps (not a Φ_q production wire)

1. **Promote `PhiQConvergence` to a theorem.** The survivable half —
   `Φ_q(z) = ∏(1−q^{−k}z)^{−1}` is a well-defined positive real on `|z| < q`
   — is the part that *can* leave conjecture status (`summable_q_inv_geometric`
   + `quantumDilog_factors_nonzero` proved; `Multipliable` in progress). This
   is the honest continuation of the merged Lean.
2. **³He structural-gap branch** — the one open empirical thread the n⋆
   refutations isolate.
3. **Land #2460 as the algebraic-limit checkpoint** (no production claim) and
   close the "wire Φ_q into the mass table" line as refuted here.

## Cross-references

- `computations/probes/zhabiro_physical_z_pin.py` + `zhabiro-physical-z-pin.witness.json`
- `content/quantum-observable-universe/mass-theory/mass-endomorphism-tower.md` (`prop:mass-endomorphism-tower`)
- `content/quantum-observable-universe/mass-theory/brane-tower-z-habiro.md` (`conj:brane-tower-z-habiro`)
- `content/quantum-observable-universe/mass-theory/phi-q-categorical-truncation.md`
- `docs/audits/2026-06-17-refuted-ansatz-lemmas.md` (six n⋆ refutations)
- `docs/audits/2026-06-17-zhabiro-item-2i-conditional-closure.md` (the merged Lean)
- witnesses: `terms-2-3-atom-per-gen-mpfr-50dps`, `mass-endomorphism`,
  `vhat-std-vs-full-tower-compare`
- PRs #2442, #2447 (Lean), #2460 (bridge)
