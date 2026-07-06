# Q_β c_3 — categorical derivation attempt (NEGATIVE result, 2026-05-31)

**Status:** NEGATIVE — c_3 stays tier `near-match`. No single-formula
structural candidate reproduces the empirical c_3 at both q₀ anchors to
the Taylor-exact threshold (≤ 10 ppm).

**Compute reference:**
[`c_3_categorical_derivation_attempt.py`](../../computations/c_3_categorical_derivation_attempt.py)
→ `c-3-categorical-derivation-attempt.witness.json` (15 candidates, 0
passing).

**Authority:** This audit complements the truncation-order canonical
framing ([`2026-05-31-qbeta-ck-truncation-order-canonical-framing.md`](2026-05-31-qbeta-ck-truncation-order-canonical-framing.md))
by ruling out the c_3-level shortcut. **Canonical c_3 verdict on main:**
[`2026-05-31-qbeta-c3-q0-stability-verdict.md`](2026-05-31-qbeta-c3-q0-stability-verdict.md)
(commit `ced5e2830`) — independently SETTLED c_3 as NEAR-MATCH via a
65-dps re-run of the truncation-order analysis. This audit and the
canonical verdict reach the same conclusion from different methodologies
(single-formula derivation search vs q-stability re-measurement). The
Habiro generating-function direction (parallel α_EM PR #1511) remains
the only open path.

---

## What was attempted

The Q_β precision ladder is
$Q_\beta = Q_{\text{base}} \cdot \prod_{k \geq 2} (1 + c_k \cdot u^k)$
with $u = b \cdot \hbar_q^2 \approx 0.00852$. The coefficient
$c_2 = -1$ is PROVED Taylor-exact (q₀-independent at 10⁻⁵⁰ compute
precision). The coefficient $c_3 \approx -2$ is currently tagged
NEAR-MATCH because empirical extraction at two q₀ anchors gives
different values:

| anchor | q₀ | c_3 empirical |
|---|---|---|
| muon-pin (stale, pre-#1422) | 1.1099785955541805 | −2.0097 |
| m_p-pin (current canonical) | 1.1099785827513808 | −2.0693 (mult) / −2.0625 (add) |

Cross-anchor swing 2.97 %. A true Taylor coefficient of a convergent
series at compute precision 10⁻⁵⁰ must be q₀-anchor-independent; this
swing rules out the q-independent J_Hopf(q=1) = −2 identification at
face value.

This probe asked: **is there a q-dependent categorical formula that
reproduces both empirical c_3(q₀) values to ≤ 10 ppm?** If yes, that
formula promotes c_3 to Taylor-exact.

## Candidates evaluated (15)

| # | Candidate | Formula | m_p-pin miss | muon-pin miss |
|---|---|---|---|---|
| a1 | bar-sym Hopf trace ×−2 | $-2 \cdot \frac{1}{2}(\mathrm{tr}_M(\sigma_1^2;q) + \mathrm{tr}_M(\sigma_1^2;q^{-1}))$ | 6 ppm wrong magnitude | wrong (−2.0026) |
| a2 | bar-sym J_Hopf | $\frac{1}{2}(J_{\text{Hopf}}(q)+J_{\text{Hopf}}(q^{-1}))$ | wrong sign/size | wrong |
| b  | J_Hopf at q₀ | $-q^2(1+q^2)$ | 328 927 ppm | 368 366 ppm |
| c1 | −[2]_q | $-(q+q^{-1})$ | 28 244 ppm | **595.5 ppm** |
| c2 | −[2]_q²/2 | $-(q+q^{-1})^2/2$ | 22 949 ppm | 6 047 ppm |
| c3 | −[2]_q·(1−ℏ_q²/2) | first-order Habiro-like | 33 014 ppm | 4 316 ppm |
| d1 | −tr_M(σ_1²) Wedderburn | $-(w_t q^2 + w_s q^{-2})$ | 500 900 ppm | 486 088 ppm |
| d2 | −2·tr_M(σ_1²) | $-2(w_t q^2 + w_s q^{-2})$ | **1 515 ppm** | 27 824 ppm |
| d3 | −(q²+q⁻²) | un-weighted block-eigenvalue sum | 9 110 ppm | 16 921 ppm |
| e1 | −tr_M(σ_1²·σ_2²) | $-(hz+1)^2$ at H_3 | 408 642 ppm | 393 107 ppm |
| e2 | −2·tr_M(σ_1²·σ_2²) | doubled H_3 disjoint Hopf | 178 802 ppm | 213 786 ppm |
| e3 | −tr_M(σ_1³) | $-((h^2+1)z + h)$ trefoil-like | 645 961 ppm | 636 660 ppm |
| e4 | J_Hopf − 6·ℏ_q² | closest cache-row | 1 742 ppm | 24 483 ppm |
| f1 | Habiro 2·C(½,3/2)·(¼)^{3/2} | α_EM-style binomial | wrong (≈0) | wrong (≈0) |
| f2 | −[3]_q·(1−ℏ_q²) | quantum-3 + 1-loop | 456 417 ppm | 499 640 ppm |

**Pass threshold:** ≤ 10 ppm at BOTH anchors (the empirical compute
floor at which a true Taylor coefficient can be distinguished from a
near-match).

**Pass count:** **0**.

## Best miss + structural finding

| Best (by worst-anchor) | Worst miss | Best anchor |
|---|---|---|
| d3) −(q² + q⁻²) | 16 921 ppm | 9 110 ppm |
| d2) −2·tr_M(σ_1²) | 27 824 ppm | 1 515 ppm |
| c1) −[2]_q | 28 244 ppm | **595.5 ppm (muon-pin)** |

The most informative miss is **c1) −[2]_q at muon-pin = 595.5 ppm**.
This explains the historical "0.004 % match" claim cited in the
deep-audit at the muon-pin anchor: at that q₀, the simple −[2]_q
candidate is close enough that combined with the rest of the ladder
the residual hits the Q_AME compute precision. At the canonical
m_p-pin q₀, the same formula misses by 25 000 ppm — an order of
magnitude beyond any acceptable Taylor-exact tolerance.

This is **independent confirmation of the deep-audit's retraction**:
the four-session wire/un-wire flip-flop happened because each
"wiring" wave anchored a candidate at one q₀ where it happened to
match, without cross-checking at the second anchor. The two-anchor
check unmasks all 15 candidates.

## Negative result interpretation

The c_3 q-swing **cannot be cured by a single closed-form structural
candidate**. The empirical c_3(q) is **intrinsically running**: it is
the Taylor coefficient of a q-dependent generating function evaluated
at the canonical q₀, not a single closed expression in q₀ alone.

Concretely, every closed candidate $f(q)$ tested has the form
$f(q) = -2 + g(q) \cdot \hbar_q^2 + O(\hbar_q^4)$ for some
substrate constant $g$ — and the OBSERVED leading correction at
$q = 1$ is $g_{\text{obs}} \approx 6.9 \pm$ scale-dependence. No
combination of (substrate b, [k]_q, J_Hopf, Wedderburn weights,
3-strand Markov traces, or Habiro binomials at fixed order) reproduces
both $g$ AND its q₀-anchor variation.

The remaining direction is the **Q_β Habiro element** itself: a
q-series $\psi_{Q_\beta}(q) = \sum_{n \geq 0} a_n(q) \cdot u^n$
whose Taylor coefficients $a_n$ ARE the $c_n$ for all $n \geq 2$
simultaneously. The c_3-level shortcut (find one formula for $c_3$
alone) is ruled out by this probe.

## What structural input would close c_3?

1. **Habiro generating function identified** — parallel α_EM
   PR #1511's [2]_q·(1−h²α). Once the Q_β q-series is named, every
   $c_k$ for $k \geq 2$ becomes a closed binomial/binomial-quotient
   coefficient, exact at all q (not just q=1), with rigorous
   truncation bound $|c_{N+1} u^{N+1}|$.

2. **Substrate-derived q₀ + Hopf cofactor** — if the framework
   eventually derives $q_0$ from purer principles (Subgoal-2,
   currently out of scope per the 2026-05-08 coordination ledger),
   the "muon-pin vs m_p-pin" distinction would collapse to a single
   anchor and the q-swing would become a single number to derive
   structurally.

3. **Wedderburn-block coupling at order 3** — d2) misses m_p-pin by
   1515 ppm, the closest of all 15 candidates at that anchor. A
   refined block-coupling formula that adds the second-order
   crossed-block term (currently undefined) might close the gap.
   This is a partial direction — it would only address half the
   problem (one anchor) without explaining the cross-anchor swing.

Of these, (1) is endorsed by the truncation-order audit; (2) is
explicitly declined by the coordination ledger; (3) would be a
useful partial probe but does not promote c_3 to Taylor-exact alone.

## Verdict

| Question | Answer |
|---|---|
| Did any candidate match both q₀ anchors ≤ 10 ppm? | **NO** |
| Best worst-anchor miss | 16 921 ppm (d3, ~1700× the threshold) |
| Best single-anchor miss | 595.5 ppm (c1 at muon-pin) — confirms why the flip-flop happened at the muon anchor |
| Categorical formula promoting c_3 to Taylor-exact | **none found** |
| Structural input still needed | Q_β Habiro generating function (open) |
| c_3 tier verdict | **stays `near-match`** per #1479 discipline |
| Wire/un-wire flip-flop reopened? | **NO** — the truncation-order framing covers it |

## Sibling cross-reference — PR #1581 Finding B reframing

Sibling PR [#1581](https://github.com/litlfred/qou/pull/1581) (three-dashboard-probes) Finding B independently audited the c_3 q₀-stability question and concluded:

> Rule A (c_3 = J_Hopf(q=1) = −2 constant) is the only structurally legitimate Taylor coefficient. Rule B (c_3 = J_Hopf(q_0) = −2.044 evaluation) is q_0-DEPENDENT, which by definition disqualifies it as a Taylor coefficient of a q-series. The "3.47% m_p-pin swing" the deep audit attributed to c_3 being mis-wired is actually Rule B's q-dependence — **= bounded c_4·u⁴ truncation error**, NOT evidence c_3 is wrong.

**This audit's NEGATIVE result is consistent with #1581 Finding B.** I attempted to find a single-formula categorical candidate that matches the empirical c_3(q_0) at BOTH anchors to ≤ 10 ppm — equivalent to trying to derive the apparent q-dependence. #1581 Finding B explains *why* this had to fail: the apparent q-dependence isn't a property of c_3, it's the missing-c_4 truncation noise leaking into the c_3 extraction.

The combined verdict: **c_3 = −2 IS the correct Taylor coefficient (Rule A), and the open work is identifying the Habiro generating function (per PR #1511 α_EM template)**, not deriving a "q-running c_3".

## Cross-references

- Canonical framing: [`2026-05-31-qbeta-ck-truncation-order-canonical-framing.md`](2026-05-31-qbeta-ck-truncation-order-canonical-framing.md)
- Sibling reframing (Rule A is legitimate; swing is c_4 truncation): PR [#1581](https://github.com/litlfred/qou/pull/1581) Finding B
- Bridge narrowing (6 mechanisms ruled out at the Q_β chain level): [`2026-05-31-qbeta-bridge-narrowing.md`](2026-05-31-qbeta-bridge-narrowing.md)
- Cached cal-anchored c_3: [`qbeta-ck-cache.witness.json`](../../computations/qbeta/qbeta-ck-cache.witness.json)
- α_EM Habiro precedent: PR #1511 (merged), [`alpha_em_habiro_taylor_investigation.py`](../../computations/alpha/alpha_em_habiro_taylor_investigation.py)
- Original c_3 derivation (Track-C structural prediction): [`q-beta-c3-hopf-three-fold-markov.md`](../../content/quantum-observable-universe/mass-theory/q-beta-c3-hopf-three-fold-markov.md)
- Truncation analysis: [`qbeta_ck_truncation_order_analysis.py`](../../computations/qbeta/qbeta_ck_truncation_order_analysis.py)
- Probe witness: `c-3-categorical-derivation-attempt.witness.json`
- Run log: `/tmp/c3_categorical_derivation_attempt.log`

## Checklist for future sessions

Before re-attempting c_3 categorical derivation:

- [ ] Have I tested the candidate at BOTH q₀ anchors (muon-pin AND
      m_p-pin)? A muon-pin-only match is a known flip-flop trigger.
- [ ] Is my "pass threshold" ≤ 10 ppm at the worst anchor? (Q_AME
      compute floor; below this you're in noise.)
- [ ] Am I proposing a Q_β **Habiro generating function** (the
      open direction) or a single-coefficient closed form (ruled out
      by this audit's 15 candidates)?
- [ ] If a single-coefficient candidate, does it satisfy
      $|f(q_0^{\text{mp}}) - f(q_0^{\text{muon}})|/|f| \leq 10^{-5}$?
      If not, it cannot resolve the q-swing.
- [ ] Have I cross-referenced the cache row in
      `qbeta-ck-cache.witness.json` to confirm I'm not re-treading a
      structural candidate already considered?
