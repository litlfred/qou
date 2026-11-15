# Post-PR #1231 follow-up workplan — 2026-05-25

**Trigger:** Author directives after PR #1231 (crystal-Yekutieli correspondence audit) + PR #1233 (probes A-D) merged.

**Author asks (in order received):**

1. ❗ **Correct Mostow-Prasad misstatement** — I wrote "calibration of q_0 to the proton mass"; should be **m_μ/m_e** via CAL-2.
2. **Highlight tessellation privileged for compute in paper.** Investigate geometric realization on **Bring surface** using existing coordinate systems (ED = Exceptional Divisor; color tubes). Very explicit.
3. **Compare to tessellation of Bring's surface at Planck length** (information-theory context). Knot convolution happens on tessellation/simplicial complex (Yekutieli 2^k?). What does it look like on Bring?
4. **Hoefsmit (2,1) symbolic χ for β_Bor proved in paper/Lean?** Other related? Generalizations?
5. **Categorical derivation of why the Markov-trace closed form has its specific coefficients** (the rescoped "Path B" research question from PR #1231 §11).
6. **Fill compute gaps + wire all up** (from PR #1231 BIG review).
7. **H_3 vs H_{3A} legacy bug audit** (background investigation in progress).

## Scope decomposition

### TIER 0 — quick corrections (in-session, ≤30 min each)

| # | Task | Effort | Status |
|---|---|---|---|
| 0a | Correct Mostow-Prasad framing in PR #1231 audit (footnote or follow-up audit) | 15 min | NEW |
| 0b | Audit Hoefsmit χ proofs: what's in paper/Lean for (2,1) of H_3, β_Bor specifically | 30 min | NEW |

### TIER 1 — infrastructure / compute gap fills (in-session, 1-3 hours each)

| # | Task | Effort | Status |
|---|---|---|---|
| 1a | `alpha_k_jones_markov_h4.py` — H_4 Wedderburn atlas (Higgs T(2,8) + 4-strand) | 2h | IN PROGRESS |
| 1b | H_3 vs H_{3A} legacy bug audit (background agent running) | 30 min | IN PROGRESS |
| 1c | Bring-surface tessellation explicit table (ED, color tubes coordinates) | 2h | NEW |
| 1d | Probe D redo with matching framing (multi-tessellation consistency) | 1h | NEW |

### TIER 2 — research-grade scaffolds (in-session if quick, else deferred)

| # | Task | Effort | Status |
|---|---|---|---|
| 2a | Categorical derivation scaffold for Markov-trace coefficients (link D15-D17 paths) | 4h scaffold; weeks for full closure | NEW |
| 2b | Info-theory: knot convolution on Bring tessellation at Planck length | research-grade | NEW |

### TIER 3 — research-grade deferred (out-of-session)

- Wire D15 Pachner-Pentagon to production
- Wire D16 Bloch-group regulator
- Wire D17 DIM master Pentagon
- H_5 Wedderburn atlas (Bring-embeddable knots)
- Full Yekutieli MI k=3 64-cell sum

## In-session priority (this PR)

Ship Tier 0 + Tier 1 in PRs that each close a specific gap:

1. **PR A**: Mostow-Prasad correction (audit follow-up) — tier 0a
2. **PR B**: Hoefsmit χ Lean/paper audit — tier 0b  
3. **PR C**: H_4 Wedderburn atlas (this branch) — tier 1a
4. **PR D**: H_3 vs H_{3A} bug audit (after agent reports) — tier 1b
5. **PR E**: Bring-surface tessellation explicit table — tier 1c
6. **PR F**: Probe D redo — tier 1d
7. **PR G**: Categorical derivation scaffold (Tier 2a, partial only) — tier 2a

Sibling-coordination posts already up:
- PR #1214 (wiring-status taxonomy, 0/17 wired) — coordinated 2026-05-25
- TODO: PR #1220 (α-cluster recursion bug) — likely overlap with H_4 atlas
- TODO: PR #1228 (vol-density-derivation KLR path) — likely overlap with Tier 2a

## Mostow-Prasad clarification (record)

What I said (PR #1231 §11, wrong):
> "the framework's calibration of q_0 to the proton mass is not arbitrary — it's selecting the unique discrete-faithful representation of π_1(S³\𝓑_3)"

What I should have said:
> "Mostow-Prasad rigidity gives a UNIQUE holonomy repn $\rho: \pi_1(S^3 \setminus \mathcal{B}_3) \to PSL_2(\mathbb{C})$ (up to conjugation), so the hyperbolic structure of 𝓑_3's complement has no continuous moduli. The framework's CAL-2 calibration pins **q_0 via m_μ/m_e** (lepton mass ratio) to ONE specific real value compatible with this rigid algebraic data. m_p is a PREDICTED observable downstream, not a calibration anchor."

Fix: add a footnote to PR #1231's audit, or land a one-paragraph correction PR.

## Hoefsmit χ for β_Bor — what's known?

From PR #1233 probe B (sympy-symbolic): $\chi^{(2,1)}((\sigma_0 \sigma_1^{-1})^3) = -h^6 - 3h^4 + 2$ in h-series.

Need to check:
- Is this in any content block as a proposition? (likely in `borromean-markov-trace-closed-form.md`)
- Is this in any `.lean` file as a theorem?
- Generalizations: $\chi^{(2,1)}((\sigma_0 \sigma_1)^n)$ for general n? (probably yes — from `(σ_0σ_1)^3 = I` in PR #1201)
- Generalizations: $\chi^{(\lambda)}((\sigma_0 \sigma_1^{\pm 1})^n)$ for general λ? (PR #1165's binomial pattern is the H_2 analog)

Audit recommendation: search the repo, surface what exists, identify formalization gaps.

## Bring-surface tessellation explicit table

From `bring-embeddable-knots-table-data.md` + `b1-torus-knot-rows-theorem.md`:
- Bring = genus-4 Riemann surface with A_5 ≅ I (icosahedral) symmetry
- |A_5| = 60 fundamental domains
- Hosts torus knots T(2,3), T(2,9), T(3,4), T(3,5) (= SM EM + strong-force particles)
- Color tubes (3 of them) likely correspond to 3 specific A_5-orbits on Bring
- Exceptional Divisor (ED) likely the S_4 → A_5 ramification structure

What's needed:
- Explicit coordinate table: each A_5 fundamental domain → which color tube + ED stratum
- Cross-reference to Yekutieli 4^k (or 2^k? — author question) tessellation
- Visualization plan (svg or tikz)

## Info-theory + knot convolution on Bring at Planck length

Context (from `folio/quantum-observable-universe/information-theory/`):
- Knot convolution is the operator that combines two knot configurations
- At Planck length, the discretization becomes the actual physical tessellation
- The Yekutieli k → ∞ limit IS this Planck-scale tessellation

What's needed:
- Verify whether the framework's existing info-theory blocks use Yekutieli 2^k or 4^k
- Either way: what does this look like on Bring at the Planck scale?
- The 60 A_5 fundamental domains × Yekutieli refinement = total cell count at Planck

This is research-grade. In-session: document the question + scope; deferred for actual computation.

## Communication intent / /coordinate

Will post intent comments on:
1. PR #1214 — DONE (wiring-status taxonomy overlap)
2. PR #1220 — TODO (α-cluster recursion bug — likely overlaps with H_4 atlas)
3. PR #1228 — TODO (vol-density-derivation KLR path — likely overlaps with Tier 2a)

## Status checklist

- [ ] Tier 0a: Mostow-Prasad correction audit/footnote
- [ ] Tier 0b: Hoefsmit χ Lean/paper audit
- [x] Tier 1a: H_4 Wedderburn atlas (script written, awaiting run + commit)
- [ ] Tier 1b: H_3 vs H_{3A} bug audit (background agent → report → fix)
- [ ] Tier 1c: Bring-surface tessellation explicit table
- [ ] Tier 1d: Probe D redo with matching framing
- [ ] Tier 2a: Categorical derivation scaffold (partial)
- [x] Coord on PR #1214 (DONE)
- [ ] Coord on PR #1220
- [ ] Coord on PR #1228
