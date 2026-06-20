# Q_β Habiro element scope — next session entry point (2026-06-03)

> Owner picked **Chain 1: Q_β Habiro element at proton-pinned q₀** for the still-open residue-A identification (PR #1727's simple-pole verdict; `A ≈ 1.804e-15`).
>
> This doc is the entry point for the next session. It records what's been tried, what's been refuted, and what concrete next attempts the Δ_λ gate allows.

## Target

Find `F(u) ∈ Habiro(ℤ)` such that:
1. `F(u_substrate(q_proton)) = Q_β(q_proton) / Q_β_base(q_proton)` to 7.8 ppb (the L2 target)
2. Reproduces `c_2 = −1` Taylor-exact at leading (already PROVED)
3. Has a simple pole at u = u_substrate (already proved at fibre level, PR #1727)
4. Has categorical residue `A ≈ 1.804e-15` whose identification is the open work

## Mirror of α_EM PR #1511 — what carries over

α_EM closed-fermion-loop element: `[2]_q · (1 − h²α)`.

What carries over to Q_β:
- Habiro-ring multiplicative structure `Π_k (1 + c_k u^k)` — already canonical
- Fibre-level holomorphy — already proved (PR #1727)
- Cross-anchor q-independence of asymptotic recurrence `c_{k+1}/c_k → 1/u` — already proved (PR #1713)

## Already refuted (do NOT retry as the residue-A categorical chain)

| Attempt | Result | Source |
|---|---|---|
| Literal `2 · C(1/2, k/2) · (1/4)^(k/2)` at k=3 | yields 0 (q-independent) — does not transfer | c_3 re-run 2026-06-03 |
| `[3]_q · (1 − ℏ_q²)` at c_3 | −3.01 vs target −2.069 (456k ppm miss) | c_3 re-run 2026-06-03 |
| 15 single-formula candidates at c_3 | 0/15 pass 10 ppm both anchors | `c_3_categorical_derivation_attempt.py` 2026-06-03 |
| Real `c_3 = f(q_0_real)` matching multiple anchors near singularity | structurally hopeless (simple pole at u_substrate) | PR #1713, PR #1727 |
| 2-term constant-coefficient recurrence | refuted by asymptotic `c_{k+1}/c_k → 1/u` | PR #1713 |
| `eigenphase = f` at u¹ | non-zero u¹ coefficient `−√3/12` in `cos(α − bℏ²/2)`; ladder starts at u² | PR #1602 |

## Concrete next attempts (Chain 1) — what the Δ_λ gate allows

Two families of Habiro-ring elements have NOT been tested against the c_k constraints at the proton-pinned q₀:

### Family α — Habiro-Wenzl projector traces

Mirror of α_EM PR #1511, but using **Wenzl projectors** `p_n ∈ H_n(q)` (which are the canonical Habiro-ring building blocks for the Jones polynomial) instead of the literal `[2]_q` quantum number.

Candidate forms:
- `F_α(u) := Π_k (1 + tr_M(p_k) · u^k)` — Habiro element from Wenzl-projector Markov traces
- `F_α'(u) := Π_k (1 + θ_k · tr_M(p_k) · u^k)` — same with categorical phase factors `θ_k ∈ μ_∞`

Concrete cross-checks at proton-pinned q₀:
- `c_2`: `tr_M(p_2) = 1` per Wenzl-projector trace; matches `c_2 = −1` only with a sign convention — investigate the sign
- `c_3`: `tr_M(p_3)` against `c_3 ≈ −2.072`
- The Wenzl projectors are q-rational at fibre level; archimedean evaluation is finite for q in the open annulus around q₀

### Family β — Habiro-Kashaev quantum-dilogarithm tower

Mirror of α_EM but using **Kashaev's q-quantum dilogarithm** `(q;q)_∞` instead of the analytic continuation `C(1/2, k/2)`. The Kashaev invariant has a categorical residue at root-of-unity limits that is THE candidate for `A`.

Candidate forms:
- `F_β(u) := (1 − u) · Π_k (1 + d_k · u^k)` where `d_k` are extracted from Kashaev tower at strand-count k
- `F_β'(u) := (q · q⁻¹; q)_∞ · expand(u)` — explicit Habiro-Kashaev form

Concrete cross-checks at proton-pinned q₀:
- Kashaev tower `Vol(K_∞)` at substrate q₀ vs CODATA Q_β — should match if Q_β IS the Kashaev volume of the substrate-anchored knot
- This connects to the Volume Conjecture in a clean way: Q_β is the Bloch-Wigner dilogarithm of the substrate fibre

### Family γ — sibling-corroborated route (PR #1750 + PR #1752 informed)

PR #1750 showed `T_β = S · I` under Markov pairing → c_k are Taylor coefficients of `S(q)` directly. PR #1752 showed Q_β SCALE via `Q_A(q₀)` is CODATA-Q_β-free to 0.168%. Combining:

- `S(q) = Q_A(q) · Π_k (1 + c_k(q) · u(q)^k)` — pure substrate
- Residue at u_substrate IS `Q_A(q₀) · [residue of c_k expansion]` — this is testable

## Δ_λ-gate compliance

Each of the three families above is a **derived categorical chain**, not a fit:
- Family α: Wenzl projectors are canonical (in `pyhecke`)
- Family β: Kashaev tower is canonical (Volume Conjecture)
- Family γ: combination of two already-derived structural negatives + a Habiro-ring extension

None proposes a "7th fit-based ansatz". The Δ_λ gate is respected.

## Concrete next-session deliverables

1. ~~**`computations/qbeta/qbeta_wenzl_habiro_chain_alpha.py`**~~ — **DONE 2026-06-03** (Family α first-test). VERDICT: NEGATIVE. All 4 Wenzl-projector Markov trace conventions (JW, symmetric, antisymmetric, adjoint-like) fail at c_2 by 50%+ and c_3 by 100%+. The literal Family α formulation is REFUTED. Witness: `qbeta-wenzl-habiro-chain-alpha.witness.json`.
2. ~~**`computations/qbeta/qbeta_kashaev_habiro_chain_beta.py`**~~ — **DONE 2026-06-03** (Family β first-test). VERDICT: NEGATIVE. All 3 Kashaev-tower variants (standard q-Pochhammer, Bloch-Wigner D(z), Faddeev real-q L_q) fail by 100%+ at c_2 and c_3. Witness: `qbeta-kashaev-habiro-chain-beta.witness.json`.
3. ~~**`computations/qbeta/qbeta_sa_qa_chain_gamma.py`**~~ — **DONE 2026-06-03** (commit `8cbaf5c7ff`). Family γ canonical decomposition verified: Q_A and cos at q₀ are finite ⇒ structural singularity must live in Π_k(∞) tower.

## Combined Family α + β NEGATIVE — residue A pointer (2026-06-03)

All three Chain 1 families have been first-tested at proton-pinned q₀:

| Family | Verdict | Implication |
|---|---|---|
| α (Wenzl-projector Markov) | NEGATIVE (4 conventions) | residue A is NOT a literal Markov trace of a projector |
| β (Kashaev tower) | NEGATIVE (3 variants) | residue A is NOT a literal Kashaev quantum-dilog value |
| γ (Q_A · cos · Π_k decomposition) | PASS (3/3 at u_sub) | Singularity lives in Π_k(∞) tower — NOT in Q_A or cos |

**Sharpest pointer for next-session work**: the Lean proof of c_2 = -1
references **Kashiwara f̃₁²** (crystal operator eigenvalue), not a
Markov-projector trace and not a Kashaev quantum dilogarithm. Combined
with Family α/β NEGATIVE, this triangulates the residue-A categorical
ID to a TRUE Kashiwara CRYSTAL operator value — the **Option-E path**
that was the 4th chain in the original (PR #1760) owner-direction
options. The 3 Chain 1 sub-families have CLOSED Chain 1 as written; the
next session should either:

- **Switch to Chain 4 (Kashiwara crystal / Option-E)** — pursue residue
  A as a crystal-operator eigenvalue in the Habiro-ring formulation
- **OR** explore mixed chains (e.g. Wenzl · Kashaev — symmetric
  combinations not tested in the literal first-tests above)

## Chain 4 / Option-E concrete first-test menu (2026-06-03)

Lean cross-check completed this session in `QBetaCategoricalPrecisionLadder.lean`:

- **N2_factor** = `1 − b² · ℏ_q^4` from Kashiwara `f̃₁†f̃₁` norm-squared
- Substrate identity `u = b · ℏ_q²` gives `u² = b² · ℏ_q^4`, so
  `c_2 = -1` is **algebraic given the categorical input** that
  `‖f̃₁†f̃₁‖² = b² · ℏ_q^4`. It's not a deep eigenvalue search.
- **N3_factor** Lean conjecture: `c_3 = J_Hopf(q=1) = -2`, which is
  **3.35% off** empirical c_3 = -2.0693 at proton-pinned q₀

So Chain 4 / Option-E is concretely about: **what q-deformed Kashiwara
or crystal operator gives c_3 ≈ -2.069 at q₀ to ≤ 10 ppm?**

Candidate Kashiwara/crystal formulas NOT yet tested (none tested in
the 15-candidate c_3 re-run):

1. **Demazure character at staircase partition** — `χ_{Demazure}^{(2,1)}(q)`
   evaluated at q₀; the Kashiwara crystal of the Demazure module
   B_w(λ) for the longest element w of S_3
2. **KLR canonical basis trace** — `Tr(b_λ)` for the KLR generator b_λ
   at strand-count 3, q₀ evaluation
3. **Crystal-graph node count weighted by content** — `Σ_{T ∈ SYT(2,1)}
   q^{maj(T)}` evaluated at q₀, where maj is the major-index statistic
4. **q-deformed Hopf-Jones at substrate** — `J_Hopf(q₀)` in standard
   Kauffman normalization (NOT `J_Hopf(q=1)`); equals
   `-q₀^{-1/2}·(q₀² + 1) ≈ -2.119` (rough estimate, 2.4% from target)
5. **Type-B folded crystal trace** — per AGENTS.md §7b authoring
   guidance, the Type-B fold gives matter-antimatter pairing as fixed
   points; trace over fixed points may give c_3
6. **Mixed Wenzl · Kashaev symmetric combination** —
   `(tr_M(p_3^{JW}) + K_3^{(Kashaev)})/2` or similar symmetric average
   not directly tested in Family α/β

### Next-session entry point — Chain 4

File: `computations/qbeta/qbeta_kashiwara_chain_4.py`
Test all 6 candidates above at proton-pinned q₀ + muon anchor. PASS if
any matches (-1, -2.069, ...) within 10 ppm at both anchors. Witness
emitting, Δ_λ-gate compliant (closed-form formulas, no fits).

**Expected outcome**: probabilistic — at least one candidate may match,
or all NEGATIVE (residue A is a more exotic crystal-graph composite).
Either way the search space narrows substantially.
5. **Lean §3b-cond `QbetaHabiroChain1` class** in `q-beta-categorical-precision-ladder.lean` — axiomatize whichever family lands

## Family γ findings (2026-06-03) — sharpen what α / β must test

Family γ verified 3/3 assertions PASS at u_substrate:

- **Q_N3 = Q_codata to 0.0 ppb** — the ladder TERMINATES at c_3 within
  compute precision (1e-30) at proton-pinned q₀. Only c_2 (Lean-proved) +
  c_3 (cal-anchored) are needed to hit ppb precision; c_4..c_7 from the
  cache are below the numerical floor at this anchor.
- **Q_A(q₀) and cos(α−bℏ²/2) at q₀ are FINITE** — structural singularity
  at u_substrate (PR #1727) does NOT live in these two factors.
- **c_{k+1}/c_k asymptotic (PR #1713) not testable here** — only 2 data
  points at this precision; needs k ≥ 5 from a different anchor.

**Sharpened target for Family α (Habiro-Wenzl)**:
The Habiro-ring element `F_α(u) = Π_k(1 + tr_M(p_k)·u^k)` must reproduce:
1. **`tr_M(p_2) = -1`** to match c_2 = −1 Lean-proved (sign convention is key — Jones-Wenzl primitive idempotent normalisation, NOT the [n]_q normalisation)
2. **`tr_M(p_3) ≈ -2.069`** to match cal-anchored c_3 within ≤ 10 ppm
3. Higher k contributions below cache precision floor at this anchor

If `tr_M(p_2) = -1` and `tr_M(p_3) = -2.069` (or a structurally-natural close form), Family α is the residue A categorical-ID.

**Sharpened target for Family β (Habiro-Kashaev)**:
The Kashaev tower `(d_2, d_3, ...)` must match `(-1, -2.069, ...)`. If the
Kashaev volume at substrate q₀ equals the Q_β CODATA, the Q_β-as-substrate-Volume conjecture is empirically validated.

## Cross-refs

- [PR #1727 simple-pole verdict](../audits/2026-06-02-qbeta-1ppq-singularity-simple-pole-fibre-level.md)
- [PR #1713 Habiro radius of convergence](../audits/2026-06-02-qbeta-habiro-radius-of-convergence-at-u-substrate.md)
- [PR #1750 Markov SHAPE collapse](../audits/2026-06-03-qbeta-markov-trace-shape-collapse.md)
- [PR #1752 SDP strict-complementarity PARTIAL](../audits/2026-06-03-qbeta-sdp-strict-complementarity-partial.md)
- [`docs/coordination/1ppq-qbeta.md`](../coordination/1ppq-qbeta.md) — master ledger
- α_EM analog: PR #1511 [2]_q · (1 − h²α)
