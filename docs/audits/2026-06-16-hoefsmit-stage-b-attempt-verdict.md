# Hoefsmit Stage B (exact operator-level c₄..c₈) — attempt verdict

**Date:** 2026-06-16
**Branch:** `claude/gracious-lovelace-uzuovl` (PR #2346)
**Status:** FORMALIZE-FIRST VERDICT — the attempt resolves to a structural
reduction, not a numeric c₄..c₈ table. No production wiring changed.

## What was attempted

Per the [1ppQ keystone recipe](2026-06-04-qbeta-1ppq-keystone-exact-construction-recipe.md)
§6 option 1 and the [state-of-play synthesis](2026-06-10-qbeta-ck-state-of-play-synthesis.md):
build the Hoefsmit-rep β-decay operator `T_β` per Wedderburn block of
`H₃(q)`, read its `N=k` operator levels, and obtain **exact, unbiased**
`c₄..c₈` (replacing the +1.7%-biased SDP extraction), with `c₂ = −1` /
`c₃ ≈ −2` as per-stage gates.

## What the attempt found (the four blockers, all pre-existing in the corpus)

1. **No rigorous "operator level → c_k" map exists yet.** The one
   `probe_q_beta_operator_valued_N3.py` labelled "operator-valued" is a
   **CODATA candidate-fit**: it tests ~14 ansätze (`b³` tail, product-cos,
   exp-resum, Padé, matrix-exp) against `Q_AME` and back-solves
   `c₃_emp = (Q_AME/Q_N2 − 1)/(b³ℏ_q⁶)`. That is extraction, not derivation
   — the exact failure mode the recipe's "formalize-first" §92 warns
   against (a probe emitting a subtly-wrong c_k that passes no structural
   check).

2. **The scalar `u`-reversion is singular** (already established, PR #1840 /
   `qbeta_ck_from_operator_markov_trace_probe.py`): `u = b·ℏ_q²` is
   *quadratic* in `t = q−1` near `q=1` (`u ~ (√3/2)·t²`), so expressing the
   ladder factor `R(q) = Q_β/[Q_A·cos(α_eff)]` as a scalar Taylor series in
   `u` around `u=0` needs a `√u` branch — non-analytic. The c_k are **not**
   scalar-q Taylor coefficients.

3. **The extraction precision floor** ([holonomic c₁₁ verdict](2026-06-04-qbeta-ck-holonomic-c11-attempt-verdict.md),
   synthesis §4): `σ(c_k) = σ_R/u^k`, `σ_R ≈ 6×10⁻⁷` (AME neutron Q-value).
   Only `c₂` (0.8% determined) and `c₃` (49%, marginal) are data-determined;
   `c₄` is 101× below the noise floor. So `c₄..c₈` can **never** come from
   extraction at any anchor count — only from a framework derivation.

4. **The decisive structural fact — c_k≥3 are q-DEPENDENT, not constants.**
   - `c₂ = −1` is the one **q-independent** rung: the operator's `N=2`
     brane factor is exactly `(1 − b²ℏ_q⁴) = (1 − u²)`, whose `u²`
     coefficient is `−1` with **no residual q**. This is why c₂ is the only
     CANONICAL (Taylor-exact, anchor-stable) rung.
   - `c₃` **swings 2.37% between anchors** (`−2.07` at proton-q₀ vs `−2.02`
     at muon-q₀; `dc₃/dq ≈ 4.6×10⁶`, refuted as any real-q formula). A
     q-independent constant cannot swing. ⇒ the operator's `N=3⁺` levels
     carry residual q-structure **beyond** the single combination `u`.

## Verdict

**"Exact operator-level c₄..c₈ as constants" do not exist.** Blocker 4 is
the crux: beyond `N=2`, the operator levels are **q-rational functions
`c_k(q)`**, not numbers. The β-decay ladder factor
`R(q) = Q_β(q)/[Q_A(q)·cos(α_eff(q))]` depends on `q` through **more than**
the single variable `u = b·ℏ_q²`; the object that packages the `c_k(q)` is
precisely the **fibre-level kernel `R(q,ξ)` / element `F(q)`** — the open
keystone (registry §3, synthesis §2). "Stage B as a constant-c_k table" is
therefore refuted by the same evidence (anchor swing + scalar-reversion
singularity + precision floor) that refuted the scalar and SDP routes.

This is a *formalize-first prune*: a one-line structural argument (c₃
swings ⇒ c_k≥3 are q-functions) eliminates the entire "extract c₄..c₈
constants" search before spending a multi-session H₄/H₅ symbolic compute on
an object that the analysis shows does not exist as posed.

## What IS rigorous and what the genuine next step is

- **Rigorous, validated:** `c₂ = −1` is the exact, q-independent operator
  gate (`N=2` level `= (1−u²)`). Any kernel `R(q,ξ)` must reproduce it.
- **The two genuine paths** (both still open, per synthesis §6):
  1. **Operator `c_k(q)` as q-rational rungs** — re-pose Stage B as
     *extract the q-rational FUNCTIONS* `c_k(q)` (not constants) from the
     exact `H₃` operator (`qbeta_symbolic_tbeta_min_l2.py` gives the exact
     symbolic `T_β`; the `N=k` levels need the `b`-graded expansion of the
     exact `Δ(net)(q)` operator, not a scalar-`u` series). These q-rational
     rungs are the "clean rungs" §6 wants to feed the kernel search, and
     they exhibit the swing explicitly (evaluate at proton + muon q₀). For
     `k≥4` the `H₃` NF basis (max word length 3) is exhausted — genuine
     `c₄..c₈` rungs require `H_n`, n≥4 (Hoefsmit reps for `λ⊢4,5,…`, longer
     braid words). This is a real but **large** symbolic build.
  2. **Derive the kernel `R(q,ξ)` directly** (the genuine keystone). All
     constraints pinned: depth ≥ 3 (or non-constant q-rational), bar-odd
     `a₁ = √2·Φ₂`, ζ₄ residue, simple pole at `u_substrate`, `q=1` shadow
     `c₃→−2`, anchor-stability gate. Freshest lead: the q-heat depth-1
     kernel (`exp_q` Jackson equation, synthesis §3-bis).

- **Default:** accept `c₂`-only in production (Q_β = 1279 ppb = 164× off
  target; m_n/Δ_pn inherit). Heavily backed (3 corpus closures + 4 KLR
  preflight refutations).

## Production guard (unchanged)

Any `c_k≥3` wiring to production still requires owner approval + a passing
**proton+muon cross-anchor test** (registry §8). The 2026-06-16 refresh of
`habiro-exact-qbeta` is a live reminder: a `c₃` tuned at muon-q₀ collapses
to 0.168% at proton-q₀.

## Cross-references

- [1ppQ keystone recipe](2026-06-04-qbeta-1ppq-keystone-exact-construction-recipe.md)
  (the executable recipe + the 2026-06-04 scalar-route-ruled-out finding)
- [state-of-play synthesis](2026-06-10-qbeta-ck-state-of-play-synthesis.md)
  §2 (kernel), §4 (precision floor), §6 (live menu)
- `computations/qbeta/qbeta_symbolic_tbeta_min_l2.py` (exact symbolic `T_β`)
- `computations/probe_q_beta_operator_valued_N3.py` (the fit, NOT a derivation)
- Registry tiers: [`ck-dk-canonical-registry.md`](../coordination/ck-dk-canonical-registry.md)
