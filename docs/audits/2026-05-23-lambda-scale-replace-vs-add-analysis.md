# λ_scale 3 % gap — post-Yekutieli residual analysis + Tier 6 / HOMFLYPT probe rationale

**Date:** 2026-05-23
**Branch:** `claude/lambda-scale-3pct-audit-2026-05-23`
**Cluster:** post-§5-closure forward work — cheat-sheet §5 item #1
**Context:** the cheat-sheet's §5 was marked CLOSED today (`1988f68fb`, `ee6f86b10`) with all 5 pipeline-discipline migrations done; forward work has shifted to **scientific closure** of the λ_scale 3 % residual (`docs/canonical-derivation-cheat-sheet.md:166`).

## 1. State of play after §5 closure

The cheat-sheet §5 forward-work item #1 names **Strategy I (Yekutieli per-cell curvature)** as the live direction. Numerics + q-locality verified in PR #978 / commit `a832fee70`:

| candidate | algebraic form | numeric @ q_0 | m_p_pred | ε vs CODATA |
|---|---|---:|---:|---:|
| Family A (production) | `5/2 + (3/4)·h²` | 2.5328 | 966.0496 MeV | **+29 605 ppm** |
| Yekutieli (PR #978, ADD) | `5/2 + (3/4 − G)·h²` | 2.4927 | 950.78 MeV | **+13 313 ppm** (2.22× win) |
| ~~Bare REPLACE~~ (falsified 2026-05-18) | ~~`5/2 − G·h²`~~ | 2.45997 | 938.28 MeV | 5.6 ppm (coincidence) |
| **CODATA target** | — | 2.4600 | 938.27 MeV | 0 |

The **bare REPLACE form `5/2 − G·h²` was falsified** by `docs/audits/2026-05-18-conjecture-falsification.md` — the natural π_HS categorical realization `(1/4)·Σ_{λ⊢4} dim_q V_λ` provably gives `+3h²/4`, not `−G·h²`, and the 5.6 ppm CODATA match was deemed a PSLQ-style numerical coincidence. The audit doc's recommendation A — test alternative substrate forms giving `5/2 + (negative h²)` — is what Strategy I (ADD) addresses by introducing the Yekutieli per-cell correction.

## 2. New observation — Strategy I's residual matches +(3/4)·h²

The Yekutieli ADD form closes 2.22× of the wedge but leaves a 1.33 % residual. Numerical decomposition at q_0 (50 dps, MPFR):

```
(λ_Y − λ_fit) / h²    =  0.75032…
        compare:  3/4   =  0.75
              difference   ≈ 3.16 × 10⁻⁴   (~ 316 ppm of the coefficient)
```

The **post-Yekutieli residual is essentially `+(3/4)·h²` — i.e., exactly the Family A contribution that Yekutieli was meant to *correct*, not *cancel*.** Algebraically:

```
        λ_Y         =  5/2 + (3/4 − G)·h²
        λ_fit       ≈  5/2 + (3/4 − G − 3/4)·h²   = 5/2 − G·h²    (the falsified bare form)
        residual h² ≈  3/4
```

So Strategy I's ADD reading and the REPLACE reading **converge on the same numerical answer at the h² level** (modulo the residual `3/4` worth of h²). The visible difference between them is whether the Yekutieli correction is *additive* on top of Family A (current framing) or *replaces* Family A's contribution to the m_p formula (falsified framing).

This raises a structural question that the cumulative audit trail has not formally addressed:

> If the Yekutieli per-cell correction is genuinely additive on top of Family A, the m_p formula evaluation should leave a residual matching some other categorical term. Numerically that residual is `+(3/4)·h²` — *exactly the Family A contribution itself*. Why should the residual recapitulate the term being corrected?

Two reconciliations are possible:

| reconciliation | implication |
|---|---|
| **(a) The 1.7 ppt match between residual and `+3/4·h²` is itself coincidental.** Strategy I's bijection, if proved, gives 2.22× closure; the remaining 1.33 % requires a *third*, independent correction whose value happens to be near `+3/4·h²`. | Strategy I bijection + a yet-unidentified third correction (Strategy K, deeper Yekutieli, or other). |
| **(b) Family A's contribution to the m_p formula is structurally absent — the Yekutieli correction is the *whole* λ_scale, not an addition.** The 1.33 % "residual" is the wedge between an ADD reading that incorrectly includes Family A and a REPLACE reading that doesn't. | The falsified `5/2 − G·h²` form is *empirically* closer because the m_p formula's λ_scale was never `(1/4)·Σ dim_q V_λ` to begin with. The Family A object is mathematically valid but answers a different question. |

The 2026-05-18 falsification ruled out (b) on **structural** grounds (no categorical derivation gives `−G·h²` directly from H_4 Wedderburn data). But it did not test (a) — whether some *other* substrate term gives the `+3/4·h²` residual after Strategy I lands. This is a fresh subquestion.

## 3. Bring-Bloch tier ladder — exhausted

| tier | basis size | hyperbolic knots in basis | relation_found | witness |
|---:|---:|---|:-:|---|
| 0 | small | — | False | `bring-bloch-tier0-search.witness.json` |
| 1 | small | hyperbolic knots ≤ 8 cr. | False | |
| 2 | 33 | + 9-crossing prime hyperbolic | False | |
| 3 | 33 | + targeted entries | False | |
| 4 | 40 | + 10-crossing prime hyperbolic | False | |
| 5 | 52 | + 11-crossing prime hyperbolic | **False** | `bring-bloch-tier5-search-m-p.witness.json` |

Tier 5's docstring (`bring_bloch_tier5_search_m_p.py:19-27`) enumerates five remaining possibilities and concludes hypothesis (e) — *structurally inaccessible via hyperbolic volumes alone* — is dominant. The CAL-4 acknowledgment in `00083b94e` (8-search cumulative case) and the cheat-sheet §5 forward-work refresh both treat the Bring-Bloch route as effectively closed.

**Tier 6 probe (this PR).** Extending the basis to 12-crossing prime hyperbolic knots is the next mechanical step under hypothesis (d). The script `bring_bloch_tier6_search_m_p.py` runs PSLQ at maxcoeff 10⁵ against a ~75-element basis. Expected outcome: confirmatory negative, closing off remaining "what about 12+ crossings?" speculation.

## 4. HOMFLYPT skein — Strategy J lean probe negative, deep recursion not yet attempted

Strategy J (`3a1b11069 spike(strategy-j): proton/neutron tr_M-ratio probe — negative on structural`) tested ~20 candidate ratios of `{tr_M(β_p), tr_M(β_n), ℏ_q, h_q, q_0, G}` against 7 observable targets. Best **pure-substrate** candidate `1 + ℏ_q²·tr_n` lands at 0.45 % vs m_n/m_p — about 3000× worse than ppb closure. The commit notes:

> "Full HOMFLYPT skein recursion COULD produce richer combinations but would need to beat 0.45 % by a factor of 10⁵⁺ to reach ppb, which is implausible given the prior 7 negative searches in the CAL-4 enumeration."

Two scoping observations on this conclusion:

- The Strategy J probe targets **m_n/m_p ratio**, not λ_scale directly. A HOMFLYPT skein probe targeting **λ_scale's `+(3/4)·h²` residual** (from §2 above) is a different search.
- Strategy J uses only scalar tr_M values. A genuine HOMFLYPT polynomial is 2-variable `(α, z)`; its evaluation produces structurally richer Laurent polynomial coefficients that the scalar reduction collapses away.

**Deep dive probe (this PR).** `lambda_scale_homflypt_skein_recursion_probe.py` computes HOMFLYPT polynomials for the proton's canonical braid word + small comparison knots, evaluates at the substrate parameters, and runs PSLQ on the 2-variable basis specifically against the post-Yekutieli residual `+(3/4)·h²` from §2, not just against m_n/m_p. Expected outcome: confirmatory negative (the 8-search cumulative case is strong), but the probe formally tests Strategy J's "deep recursion COULD produce" caveat with a sharper target.

## 5. Recommended next steps after this audit

| priority | action | who | scope |
|---|---|---|---|
| 1 | **Strategy I bijection proof** — H_4 half-symmetric Wedderburn projection ↔ 8 octahedral cells | math/category-theory specialists | research-grade; closes 2.22× win to provable status |
| 2 | **§2 reconciliation** — test whether the post-Yekutieli `+(3/4)·h²` residual admits a third independent categorical correction | future spike | depends on #1 landing; small once Strategy I structure is locked |
| 3 | Tier 6 + HOMFLYPT-recursion probes (this branch) | this PR | confirmatory negatives; close off remaining speculation routes |
| 4 | **REPLACE-vs-ADD note in `production-vs-exploratory-discipline.md`** — record the §2 structural ambiguity so future agents don't re-derive it | docs / discipline owner | small |

Item #2 is the most actionable new direction from this audit — once Strategy I's bijection lands, the residual at `+(3/4)·h²` becomes a sharply-defined target for a follow-up probe (much narrower than the original 3 % gap).

## References

- `docs/canonical-derivation-cheat-sheet.md` §3 + §5 (post-2026-05-23 closure state)
- `docs/audits/2026-05-18-conjecture-falsification.md` (REPLACE form `5/2 − G·h²` falsified)
- `00083b94e content(lambda-scale-bring-bloch): formal acknowledged-CAL-4 status`
- `a832fee70 compute(strategy-i): Yekutieli per-cell curvature probe`
- `3a1b11069 spike(strategy-j): proton/neutron tr_M-ratio probe — negative on structural`
- `61923f2c0 fix(λ_scale): rip fitted CAL-4 out of production — PROVED Family A everywhere`
- `m_p_borromean_verification_50dps.py:117-187` (production compute trail)
- `_li_2_q_util.py:170-198` `lambda_scale_family_a(q, q_inv=None)`
- `lambda_scale_strategy_i_yekutieli_probe.py` (PR #978's verified probe)
- `bring_bloch_tier5_search_m_p.py:19-27` (5-tier ladder hypothesis enumeration)
- PR #916 (Strategy I/J enumeration)
- PR #842 / #854 (original `5/2 − h²·G` falsification PRs)
