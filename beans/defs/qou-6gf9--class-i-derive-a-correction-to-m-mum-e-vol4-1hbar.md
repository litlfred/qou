---
# qou-6gf9
title: 'Class I: derive a correction to m_mu/m_e = Vol(4_1)/hbar_q^2 (the 11.5 ppb mu-p residual)'
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-08T09:31:00Z
updated_at: 2026-11-20T14:28:57Z
parent: qou-2002
---

Attack the Class I mu-p residual on the **muon carrier** `m_mu/m_e = Vol(4_1)/hbar_q^2`
(distinct angle from the Q_beta `c_k` ladder and from the `F_Bor` `c_4` dressing).
Hypothesis: the carrier is the leading term of a series and the ~11.5 ppb q_0 tension
(= +209.755 ppb on m_mu at the proton pin, 9.53 sigma) is its first correction.

Route stays on the right side of the permanent 2026-08-02 owner gate (`qou-eic1`):
it corrects a **mass-ratio relation at fixed q_0**; it does not derive `q_0`.

## Outcome (2026-08-08) — NOT CLOSED. Three prunes landed; the front is bounded.

Audit: `docs/audits/2026-08-08-mu-p-residual-carrier-order-and-bar-parity-prune.md`
Probe: `docs/audits/scripts/mu_p_carrier_order_window_probe.py`
Lean:  `folio/quantum-observable-universe/lean/QOU/BraidKnot/MuPCarrierBarParity.lean` (generic)
     + `folio/quantum-observable-universe/lean/QOU/BraidKnot/MuPCarrierOrderWindow.lean` (archimedean)
       (`lean`-direct exit 0 on both + real 4-module import cone via
        `lean-direct-cone.sh`; 0 sorries; `#print axioms` clean on all 11 decls;
        `check-sidecars.sh` clean)

Measured at the proton pin: `t = 2.09754920524e-7` (+209.755 ppb, 9.534 sigma),
`sigma_exp/t = 10.49 %`.

1. **Order window** (Lean `order_window`, scope-(b) vs the stated class). A monomial
   `t = |c|*hbar_q^k` with small-height `|c| in [1/5,5]` forces `k in {6,7}`
   (`c_6 = 0.22169`, `c_7 = 2.23747`). Kills the Ohtsuki / volume-conjecture reading:
   1-loop overshoots 4.7e5x, 2-loop 4.7e4x. NOT claimed: the `|c| in [1/2,2]`
   emptiness — knife-edge (`c_7` -> 2.003 at -1 sigma).
2. **Bar-parity selection rule** (Lean, generic `[Field K]`). `hbar_{q^-1} = -q*hbar_q`,
   so the bar-even monomials are exactly the tower of `w := q*hbar_q^2 = [2]_q - 2`.
   Consequence, proved against the *production* defs: **`delta_R9` and `delta_V9` of
   `MmuR9V9Closure.lean` are bar-MIXED** — they fail the same precondition that
   disqualified the projector shift (#2584). Exclusion is *conditional* on that
   precondition, which is argued (4_1 amphichirality) not proved. And the bar-even
   `w`-tower admits **no** order with a small-height coefficient (j=3 -> 0.16211,
   j=4 -> 14.877).
3. **Entropy bound.** `t` is a **0.98-significant-digit** datum; the indistinguishable
   order-6 window `c in [0.19844, 0.24494]` is 21 % wide and swallows 12/12 hand-listed
   small-height constants — including 0.2075, the coefficient of an *already-refuted*
   mechanism. Matching cannot identify a closure; only an a-priori coefficient can.
   Corollary: `delta_V9` is **19.45x below** the resolution of the datum it closes, and
   `R9+V9` (-1.418 ppb) is five times *worse* than `R9` alone (-0.287 ppb).

Stays clear of the permanent q_0-derivation gate (`qou-eic1`): `q_0` is held fixed.
Touches neither `F_Bor` nor the Borromean trace, so no exposure to the unconfirmed
6.7 % `tr_M_atomic` convention gap under `qou-3qrv`.

## GAP (open) — what would actually close this

A **bar-even** correction, not a single monomial (requirement 2 above rules pure
monomials out in both `hbar_q` and `w`), whose coefficient is **fixed before the fact**.
The only surviving route named in the corpus is the Sigma(2,3,5) WRT / s5-so3 Habiro
series (bean `s5bb`), whose coefficients come from quantum topology rather than from
matching. Nothing here advances that route; it only shows every cheaper route is closed.

## Follow-up filed (not actioned — out of scope for this branch)

Relabel the `MmuR9V9Closure.lean` m_mu rungs to record (i) bar-mixedness and
(ii) that `delta_V9` is sub-resolution, and re-measure its quoted "0.036x L2 miss" at
the documented proton pin (not reproducible there: R9+V9 gives -1.418 ppb).



## 2026-09-03 (session tender-keller) — consolidation pass, claimed

Owner picked the s5-so3 / GAP-A-4 lane ("4") among four. Corpus-grep before
acting: the WRT line for W_lambda reached its deflationary terminus 2026-06-22
(s5bb: WRT data and W_lambda are Schur-Weyl DUAL, not equal); qou-2v7k names the
real wall as the Beasley-Witten S^3/2I localization construction (class
BWVacuumRowIsHecke, no genuine instance) with NO in-session tractable probe. So
there is no honest first step on the CONSTRUCTION this session. What IS bounded
and formalize-first: consolidate this bean's three prunes into one Lean
exclusion — a bar-even monomial in (hbar_q, q) with small-height coefficient
cannot carry the 209.755 ppb residual at the proton pin (bar-even forces the
w-tower, w = q + 1/q − 2; the w-tower has no small-height order: t/w^3 ≈ 0.162,
t/w^4 ≈ 14.9). The w-tower half was MEASURED here, never Lean-proved. Target
file: QOU/BraidKnot/MuPCorrectionAdmissibility.lean (additive; does not touch
GapA4MuonBranching.lean). Scope (b) on that class; constructs nothing.



## 2026-09-03 — LANDED (PR #6476, commit 4dbfd2ee31): the consolidation Lean

QOU/BraidKnot/MuPCorrectionAdmissibility.lean: bar_even_monomial_iff (the
CONVERSE half of the selection rule, 1 < q), wGen bounds on the pin window,
no_small_height_w_monomial (the measured t/w^3 = 0.162 < 1/5, t/w^4 = 14.9 > 5
now PROVED for every order j), capstone no_bar_even_small_height_monomial
(+ hbarQ bridge), and the content-bearing GapA4CorrectionAdmissible structure
with monomial_not_admissible. Scope (b) on {single monomial in (hbar_q, q),
bar-even, |c| in [1/5, 5]}; constructs nothing; bar-even precondition stays
argued, carried as a hypothesis. Companion content block
rem:mu-p-residual-two-readings (574d8531e1) documents the residual with both
readings (R1 falsifiable +2.1e-7 prediction of the bare relation / R2
unclosed bar-even series — the conservative reading) and what decides. GAP
unchanged: the a-priori coefficient. Note GapA4MuonBranching.lean's
target_correction_constraint is a def : Prop carrying a float fit target at a
q0 literal 580 ppb off the pin — handed to the docstring/def-Prop drain (#6471).



Released 2026-09-03 after the consolidation landed (PR #6476). Status back
to todo: the GAP — a bar-even correction with an a-priori coefficient — is
unchanged and nobody is on it; the Lean now records exactly which cheap class
is excluded (single small-height bar-even monomial, any order, any pin in the
window) so the next attempt starts past it.


## 2026-09-04 (session tender-keller, PR #6572) — stale decimals, one route measured and closed, one narrowing proved

### A. THIS BEAN'S DECIMALS ARE PRE-CODATA-2022. Do not quote them.

`t = 2.09754920524e-7` (209.755 ppb, 9.534 sigma) is the CODATA-2018 value.
`fca08de7d2` (2026-08-22, owner ruling) moved the muon anchor to CODATA 2022:

  quantity        this bean      live
  t               209.755 ppb    211.165 ppb  (mu-substrate-tension-audit-100dps
                                               data.residual_ppb_at_canonical_q0)
  c_6 = t/hbar^6  0.221693       0.223230
  t/w^3           0.162109       0.163199
  t/w^4           14.8767        14.9767

**No verdict moves** -- every landed theorem is stated for
`t in [1.8e-7, 2.4e-7]`, which covers both vintages -- but the decimals in the
prune list above are stale and get quoted.

### B. Prune 2's PRECEDENT is half-retracted (not the prune itself)

This bean cites #2584's projector-shift disqualification as the precedent for
its bar-even precondition, via "delta_R9 and delta_V9 are bar-MIXED". Bean
`qou-j3u0` + `computations/probes/keystone-wlambda-vs-ylambda-projected-shift.witness.json`
refuted the bar-mixed leg on 2026-08-30: the W-weighted shift is bar-EVEN
(`delta(q) - delta(1/q) = 4.009e-50` at dps 50). Cause: the original went
through `ph.trace_weights_n`, a float64 API, where `y_(3,1,1) = 0` exactly
(>2 rows, SU(2) Schur-Weyl), so one side of the comparison was vacuous.

The magnitude leg SURVIVES: `over_210ppb_factor = 3354404.899`, i.e. 3.35e6x.
So the exclusion holds and is scope-(a); "the Markov-trace surface is
exhausted" was scope-(b) resting on the retracted parity leg and is now
scope-(a). The Lean here is unaffected -- `MuPCarrier.hbarGen_bar` etc. are
unconditional algebra. It is this bean's PROSE that is stale.

### C. MEASURED AND CLOSED — the 4_1 cyclotomic ladder cannot carry t

The corpus's strongest a-priori candidate is `QOU/BraidKnot/HabiroNewtonLadder.lean`
(sorry-free): every term of the figure-eight colored-Jones cyclotomic expansion
is bar-even, all cyclotomic coefficients are 1, and `Lam_1 - lam_0 = w` exactly.
So it is literally "a bar-even correction whose coefficient is fixed before the
fact", on the muon's OWN carrier knot. Nobody had ever compared it to t.

Measured, mpmath 60 dps at the proton pin, over all N <= 12:

    P_k(N) = prod_{j=1..k} (q^N + q^-N - q^j - q^-j)     (zero for k >= N)

    smallest nonzero |P_k(N)|:  N=5 k=4 -> 1.1465e-3   = 5430 x t
                                N=6 k=5 -> 1.2573e-3   = 5954 x t
                                N=4 k=3 -> 1.7197e-3   = 8144 x t
    any term inside [1.8e-7, 2.4e-7]?  NO

Structural reason, not a coincidence: each factor is an integer polynomial in
w with lowest term `(N^2 - j^2)w`, so `P_k(N) ~ M_k w^k` with
`M_k = k!(2k+1)!/(k+1)!` the minimum over N > k (1260 at k=3, 72576 at k=4).
`M_k w^k` bottoms out near k=4-5 at ~1e-3 and grows either side. **The ladder's
magnitude floor sits at order w; t sits at order w^3.** Two orders of w apart.

Scope-(a) on "a single cyclotomic ladder term supplies the residual" -- which
is the shape actually proposed. A SUM over the ladder is O(1) and is a
different question.

### D. PROVED — the two-term bar-even sum is sign-forced and pinned

New Lean `QOU/BraidKnot/MuPTwoTermSum.lean` (see PR #6572 for verification).
`no_bar_even_small_height_monomial` quantifies over ONE exponent pair; a sum
lies outside it, and no probe/Lean/audit/bean anywhere had tested one. Orders
3 and 4 are the only pair that can bracket t. Over the whole pin window and the
whole residual window, `t = c3 w^3 + c4 w^4` with both small-height forces:

  * `sum_signs_forced`  -- `0 < c3` and `c4 < 0`: the tower must ALTERNATE.
    Neither sign assumed; both are consequences.
  * `sum_c3_pinned`     -- `1/5 <= c3 <= 1/4`. Width 1/20 against a
    small-height band of width 48/10: the cubic rung is pinned to ~1 % of its
    a-priori range.
  * `sum_c4_bounded`    -- `c4 <= -4/5`, so c4 occupies `[-5, -4/5]`, 44 % of
    the band rather than all of it.

At the exact pin the feasible set is tighter still: `c4 in [-5, -3.3772317]`,
`c3 in [1/5, 0.21768309]`. Worked point `(0.2014, -3.5)` reproduces t to
3.8e-4 relative -- so the family is NOT empty; this is a narrowing, not an
exclusion. Value: a derived pair now has a sharp prediction to fail without a
numerical comparison. The entropy bound still forbids MATCHING one.

### E. The library holds an explicit Sigma(2,3,5) Habiro series, UNCITED

`library/arxiv-2605.15740v1` (Lovejoy, Osburn, Storzer, *Bailey pairs, Eichler
integrals and unified WRT invariants*) gives the unified WRT invariant of the
Poincare homology sphere in closed form:

    I(Sigma(2,3,5); q) = (1-q)^-1 * sum_{n>=0} q^n (q^{n+1})_{n+1}

It is registered as `lovejoy2026` in `content/schema/references.ts:12904` and
`grep -rn lovejoy2026` across content/ docs/ computations/ returns **empty** --
registered at intake, never cited, never used. Its `q^{-1/120}` twist is the
same one `keystone-colored-sigma235-wrt.witness.json` measured numerically
(`Psi_LZ/S_JL = q0^{-1/120}` at 70 dps).

**And `HabiroMagnitudeA3.pochAbs_unbounded` does NOT foreclose it.** Check the
binders: `hq : 1 < q` (this route evaluates at the bar image
`1/q0 = 0.9009 < 1`, inside the convergence disk) and `ha : forall n, 1 <= |a n|`
(Habiro coefficients in Z[q^{+-1}] need not satisfy it). The naive reading
"Habiro is dead at the substrate" would close the one route this bean names,
and it is wrong.

Not attempted here. Cheapest next measurement: bar-symmetrise `I(Sigma(2,3,5);q)`,
expand in w about q=1, read `[w^3]` and `[w^4]`, compare to `t/w^3 = 0.163199`
and `t/w^4 = 14.977`. Pass or fail, the coefficients are a-priori.

### F. GAP status: still OPEN

Nothing here closes it. C removes the corpus's strongest a-priori candidate by
measurement; D narrows the next shape; E identifies a held source nobody has
used and shows the obstruction that appears to block it does not reach it.


## 2026-09-04 later (PR #6603) — the Sigma(2,3,5) route, first measurement

Probe `computations/mu_p_habiro_basis_order_probe.py`, witness
`mu-p-habiro-basis-order.witness.json`, 3/3. Source read from
`library/arxiv-2605.15740v1` (`lovejoy2026`), previously uncited.

**Structural, and it is the durable part.** The Habiro basis
`(q;q)_n (q^-1;q^-1)_n = prod (1-q^j)(1-q^-j) = prod (2 - q^j - q^-j)` is
IDENTICALLY the bar-even tower `(-1)^n prod f_j` of MuPCarrierBarParity
(verified to 8.1e-69 off-anchor). So the bar-even precondition -- which this
bean and the Lean both carry as an ARGUED assumption from 4_1 amphichirality --
is **automatic** for any Habiro-ring element in its own basis. That upgrades the
standing of every conditional exclusion here when the candidate is Habiro.

**Magnitude.** t/|omega_n| passes through small height, minimum n=9 at 0.5770.

**But six CONSECUTIVE orders qualify (n=6..11)**, so the tower is dense near t
and magnitude agreement is nearly free -- the entropy bound in a new coordinate.
Recorded as a caution, not a finding. **a_n(Sigma(2,3,5)) is NOT computed**, and
Habiro coefficients are in Z[q^{+-1}] not Z, so no cheap integrality argument
exists either. This is about the BASIS, not the manifold.

**No conflict with no_small_height_w_monomial**: omega_n ~ (n!)^2 w^n, so this
is the non-unit-height escape the Lean leaves open, with (n!)^2 structurally
determined rather than chosen.

**Regime confirmed**: I(Sigma(2,3,5); 1/q0) = 14.9174984765, converged; diverges
at q0 > 1. HabiroMagnitudeA3.pochAbs_unbounded (binders: 1 < q, and
|a_n| >= 1) does not reach the bar-image evaluation.

**Next, and it is the decisive step**: extract a_n(Sigma(2,3,5)) from the series
and evaluate a_n * omega_n at the pin. Until then nothing here is evidence.


## 2026-09-04 later (PR #6663) — the Sigma(2,3,5) route: CLOSED in this coordinate

Probe `computations/mu_p_sigma235_ohtsuki_resolution_probe.py`, witness
`mu-p-sigma235-ohtsuki-resolution.witness.json`, 3/3.

**The coefficients, exact, and a free check.** Taylor-expanding the
`lovejoy2026` series at q=1 over the rationals gives integers
1, -6, 45, -464, 6224, -102816, 2015237, -45679349, 1175123730, ...
`lambda_1 = -6` reproduces Ohtsuki's `lambda_1 = 6*lambda_Casson` with
`lambda_Casson(Sigma(2,3,5)) = -1` -- so the transcription and the extraction
are both verified against a known invariant, not merely self-consistent.

**Factorially divergent.** `|lambda_(n+1)/lambda_n|` is LINEAR in n
(7.5, 10.3, 13.4, 16.5, 19.6, 22.7, 25.7, 28.8, 31.8, 34.9 ~ 3n).

**The finding.** At `x0 = q0-1 = 0.10998` the terms turn over at n=2 with least
term **0.5443**. An asymptotic series cannot resolve below its least term, so
the intrinsic resolution of this object at the substrate is 0.5443 against
`t = 2.1116e-7` -- a factor **2.58e6**. NO truncation supplies t.

**This EXPLAINS the previous entry's caution rather than repeating it.** The
basis omega_n does pass through t's magnitude at six consecutive orders; the
manifold's own coefficients grow factorially, so the products never land there.

**Scope-(b)** for the class (every truncation of the Taylor/Ohtsuki expansion at
q0). **Scope-(a)** for the route: does NOT exclude a Borel/median resummation
(the standard way below a least term -- resurgence sources are held), evaluation
at a root of unity where the Habiro element is actually defined
(`I(M;zeta) = Z_zeta(M)`), a different Brieskorn sphere, or the exact
Habiro-basis coefficients `a_n(q) in Z[q^{+-1}]` (not computed here; the q=1
Taylor coefficients are a coarser object).

## GAP status after this: OPEN, and now with NO named surviving route

The bean named exactly one route with a-priori coefficients. That route is
closed in the coordinate it was named in. What remains un-foreclosed is a
strictly harder ask -- a resummation, or a root-of-unity evaluation -- and
neither is a small next step. An honest reading is that the cheap end of this
GAP is exhausted, and the next attempt should be scoped as research rather than
as a measurement.



## Claim reset 2026-10-04

Was in-progress with no bean update since 2026-09-04 and no main commit naming it since 2026-09-20 (owner decision 3). Re-claim with `bun run beans:claim` if you pick it up.


## Round 46 Update (2026-11-16 — PR `litlfred/qou#8142`)

- **Status**: `in-progress` (exact Laurent-polynomial Habiro-basis probe landed in Round 46; kept `in-progress` per strict non-closure rule).
- **Exact Laurent-Polynomial Habiro-Basis Probe & Witness**:
  - Added `computations/probes/mu_p_carrier_habiro_laurent_coefficients_probe.py` and `computations/probes/mu-p-carrier-habiro-laurent-coefficients.witness.json` (50-dps `mpmath` + exact $\mathbb{Z}[q, q^{-1}]$ Laurent arithmetic, 5/5 assertions passing, 0 raw `float64`s, 0 `float64` padding hits).
  - Verifies in exact $\mathbb{Z}[q, q^{-1}]$ arithmetic ($n = 0 \dots 8$) that the figure-eight Habiro cyclotomic coefficients $a_n(q) = (-1)^n q^{-n(n+1)/2} \in \mathbb{Z}[q, q^{-1}]$ satisfy $c_n(q) = a_n(q)(q; q)_n^2 = (q; q)_n(q^{-1}; q^{-1})_n = \omega_n(q)$ identically with zero coefficient discrepancy and exact bar-evenness $c_n(q^{-1}) = c_n(q)$.
  - Compares the Laurent-kept rungs $c_1(q_0) = -w(q_0) = -0.01089686670712230$ and $c_2(q_0) = w(q_0)h(q_0)^2 = +4.762607286525835 \times 10^{-4}$ against the leading $q=1$ Taylor terms in $h^2 = (q_0 - q_0^{-1})^2$ ($-h(q_0)^2/4$ and $+h(q_0)^4/4$):
    - $\Delta_{h^2} c_1(q_0) = c_1(q_0) - (-h(q_0)^2/4) = +w(q_0)^2/4 = +2.96854260081976 \times 10^{-5}$ ($141.524 \times t_{\text{2018}}$, $140.579 \times t_{\text{live}}$);
    - $\Delta_{h^2} c_2(q_0) = c_2(q_0) - h(q_0)^4/4 = -w(q_0)^2 h(q_0)^2 / 4 = -1.297437419491036 \times 10^{-6}$ ($6.18549 \times t_{\text{2018}}$, $6.14419 \times t_{\text{live}}$).
  - Neither $n=1$ nor $n=2$ (nor their Laurent-vs-$h^2$-Taylor shifts) lies inside the $[1.8 \times 10^{-7}, 2.4 \times 10^{-7}]$ $\mu\text{--}p$ carrier residual window.
- **PR**: `https://github.com/litlfred/qou/pull/8142` (`7ba86df415ad231cf6e834adee99dcb383115c6d`).


---

**2026-11-20 — PR #8565 (`claude/two-term-qed-derivation-2026-11-20`), `QEDHigherOrderCovariance.lean` (17 thms, sorry-free, lean-direct exit 0) + `computations/probes/two_term_qed_derivation_joint_pin_probe.py` + `docs/audits/2026-11-20-two-term-qed-derivation.md`.**
- All-orders local class: covariance forces y_ab = t·x_ab with one t in {0, −h} (`exact_local_covariant`); the exact per-pair rescaling factor on V³ is 1 (`facU_borromean`), so the second-order (two-insertion) term of the local class is 0 for p and n.
- Naive photon-exchange double sum D is not braid-covariant (shifts by −(Q0Q1)² under σ1σ1⁻¹); its completion S²/2 = 0 on V³.
- No degree≤2 (order-α) charge weight couples to μ̄₁₂₃ (`quad_alternating_eq_zero`). The even degree-4 c₃ μ̄² term remains the only braid-dependent survivor; c₃ still underived.
- Joint pin (scope (a), conditional on α_em form B): α_em pins q0 +0.053 ppb from the proton identity, the muon identity +11.614 ppb. A proton-only term reaching m_μ sends α⁻¹ to +79.00 ppb. So no proton-side term (derived or not) satisfies m_μ and α_em together; the evidence points at the muon carrier (qou-6gf9).

**2026-11-20T14:28:57Z — OWNER: open this front (Lean-first); CAL-2 unchanged for now.** New evidence from PRs #8562 /
#8565: α_em form B and the one-term m_p identity agree on q₀ to 0.053 ppb (2.4σ); the two-term proton
re-pin puts α 495σ off; covariant QED insertions give zero proton self-energy on V³ through Vassiliev
degree 3 (#8552, #8557, #8565). So the μ–p residual points at the muon carrier Vol(4₁)/ℏ_q². Needed size
(diagnostic only, not a target to tune to): δ_μ = −211.2058 ppb (−9.09e-5·α/π, −3.97e-3·α²). Owner
reverted #8554 to the one-term default pin (two-term kept as a named comparison).
