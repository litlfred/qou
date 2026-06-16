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

## Empirical follow-up (2026-06-16) — the s-series compute attempt

After the structural verdict, the decisive in-budget compute was
attempted: the `s = q−1` series-match (no singular u-reversion) of the
operator ladder `R(q) = Q_β(q)/[Q_A(q)·cos(α_eff(q))]` against
`∏(1+c_k u^k)`, with the `c₂ = −1` gate
(`computations/qbeta/qbeta_ck_sseries_operator_match_probe.py`, WIP). It
surfaced **two concrete blockers** that confirm the "1–2 session" rating:

1. **Wrong operator object (the q=1 test).** The placeholder
   `Q_β(q) = E_0(q)·τ_M(T_β)(q)` with `E_0 = 1/(q(q−1))` **diverges** at
   `q=1`, but the true `Q_β(1) = Q_A(1) = 2·m_e` is **finite**. So the
   canonical `Q_β = |Δ(net)(q)|·E_0(q)` requires the GB-reduced
   `Δ(net)(q)` to carry a `(q−1)` **zero** cancelling the `E_0` pole.
   `free-neutron-decay.witness.json` stores only **numeric** net coeffs
   at `q₀` — `Δ(net)(q)` as a symbolic q-function must be produced by
   running `free-neutron-decay.py::reduce_verbose` with a **symbolic** q.
2. **Performance.** Full `sympy` series to `s^{2·8+3}` with
   `sqrt(q)/cos/log` **times out (>9 min)**. The match must use a
   **numeric mpmath s-Taylor** + numeric triangular solve, keeping the
   `c₂ = −1` gate.

Neither blocker is fundamental — they are exactly the careful setup the
synthesis budgets at 1–2 sessions.

### Completed run (2026-06-16, both blockers fixed)

Both blockers were then resolved and the probe **ran to completion**:

- **Object fixed.** `Δ(net)(q)` reconstructed **symbolically** by summing
  the `coefficient_symbolic` per-word entries in
  `free-neutron-decay.witness.json`:
  `Δ(net)(q) = (q¹⁴+2q¹³−5q¹²−10q¹¹+10q¹⁰+24q⁹−16q⁸−32q⁷+16q⁶+24q⁵−10q⁴−10q³+5q²+2q−1)/(4q⁷)`.
  Validated: `Δ(net)(q₀) = −0.18829060` vs witness `−0.18829062` (Δ=1.8e-8);
  the numerator has a `(q−1)` zero (sum of coeffs at q=1 is 0), so
  `Q_β = |Δ(net)|·E₀` is finite at q=1 and `R(q→1) = 1.0` exactly. Object
  **validated**: `|Δ(net)|·E₀ = 0.788 MeV ≈ Q_β`.
- **Perf fixed.** Switched to numeric `mp.taylor` (60 dps) for the s-series.
- **Result — the c₂ gate FAILS:** the net-route ladder gives
  **`c₂ ≈ −8.006`, not the canonical `c₂ = −1`**. (Caveat: high-order
  `mp.taylor` is numerically unstable here — odd-order `[s^odd] log R ~ 10⁴`
  — so c₃⁺ from this route are not yet trustworthy; an exact-rational
  Taylor is needed for those. But `c₂` at `s⁴` is low-order and robust.)

**Finding:** the `|Δ(net)|·E₀` **net-route** (the *binding-like*
`E₀·Δ(trace)` object) does **not** reproduce the canonical `c₂ = −1`,
which lives in the τ_M **brane-tower** route. The two are
**parallel-but-distinct ladders** — same `E₀·Δ(trace)` template, different
objects (and, per `substrate-cohomology-calibration-story`, conjugate
bar-parities: binding/net = bar-even mass side, the Q_β brane-tower
precision ladder = bar-odd sinh side). This empirically corroborates the
structural verdict (c_k≥3 are q-dependent / route-dependent, not universal
constants). The `−8` is suggestive next to binding's `m_e·8G`, but one
number is not identified.

Witness: `computations/qbeta/qbeta-ck-sseries-operator-match.witness.json`
(c₂ gate assertion FAILS by design — flags the net-route ≠ brane-tower).
The attempt thus did emit a c₂, gated it, and correctly **refused** to
trust c₃⁺ (gate fail + numerical instability) — formalize-first correct.

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
