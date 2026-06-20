# Q_β bridge — narrowing the open derivation (2026-05-31)

## What this is

The Q_β "bridge" is the genuine open derivation step:

> find the substrate-canonical `f` with `Q_β = m_e · f(Δtr_M, q)` that is
> **Taylor-exact at canonical q₀** (residual < compute precision), so the
> c_k ladder coefficients become derivations rather than the q₀-dependent
> near-matches that have flip-flopped four times.

This doc consolidates a session (2026-05-31) spent "working on the actual
bridge". It does **not** close the bridge — it **rules out six candidate
mechanisms** (one of them cross-confirming an existing framework
falsification), records the structural facts established, and points at
the single remaining direction. The purpose is flip-flop prevention:
future sessions should not re-tread the dead ends below.

## Established structural facts (not in dispute)

1. **The residual is in the SCALING, not Δ(net).** Per
   [`neutron-qvalue-symbolic.md`](../../content/quantum-observable-universe/particle-interactions/neutron-qvalue-symbolic.md):
   Form A's +1677 ppm overshoot is a scaling error — "the derived
   `E_0 = m_e/(q(q−1))` is the single-level approximation; the exact
   tower-summed E_0 absorbs the 0.17%". The c_k are the scaling/E_0
   expansion, not a Δ(net) correction.

2. **The cos eigenphase is the dominant, right-direction scaling.** At
   canonical q₀ (`qbeta-scaling-bridge-investigation.witness.json`):

   | stage | err vs CODATA |
   |---|---|
   | Q_A (Form A) | 1.68×10⁶ ppb |
   | × cos(α − bℏ_q²/2) [N=1 eigenphase] | 73 826 ppb |
   | × (1 − u²) [c_2, Taylor-exact] | 1 277 ppb |

3. **The multi-block character sum reproduces Δtr_M exactly.**
   `Σ_λ y_λ · χ_λ(β_n − β_p) = −0.1420729 = Δtr_M` (verified,
   `qbeta-per-block-paper-closed-forms.witness.json`), with per-block
   leading-order (ε¹) coefficients **(3): −2, (2,1): −1, (1,1,1): −2**.

4. **c_3 ≈ −2 originates in the trivial/sign blocks, not the standard
   block.** The empirical c_3 leading order is −2, matching the (3) and
   (1,1,1) blocks (both −2) — NOT the (2,1) block (−1) that the
   single-block eigenphase is built from. So the refinement lives in the
   blocks *outside* the current eigenphase.

## What the bridge is NOT (six ruled-out mechanisms)

| # | candidate mechanism | verdict | evidence |
|---|--------------------|---------|----------|
| 1 | `Δtr_M` is Form A's net-winding slot Δ(net)_A | **NO** | leading Taylor orders differ (−5/4 vs −2); swap misses CODATA by −240000 ppm — `qbeta-delta-tr-vs-formA.witness.json` (item 1) |
| 2 | `Q_β = m_e·|Δtr_M|·(substrate constant)` | **NO** | `g(q₀) = Q_codata/(m_e|Δtr_M|) = 10.776` is not a clean substrate constant (closest q²/(q−1) at 3.96%) — item 1 |
| 3 | geometric E_0 tower `1/(1−ℏ_q²)` | **NO** | wrong direction: Q_β needs factor 0.9983 (<1), geometric gives 1.0099 (>1) — scaling investigation |
| 4 | symmetric Li_2^q E_0 tower | **NO** | wrong direction: gives 1.0098 (>1) — scaling investigation |
| 5 | per-block `dim_q²` decomposition `c_k = Σ_λ dim_q²(λ)·c_k^(λ)` | **NO** (falsified) | LO pattern (−2,−1,−2) gives −8, not −2, at c_3 — [`per-wedderburn-block-c5-c6.md`](../../content/quantum-observable-universe/mass-endomorphism/per-wedderburn-block-c5-c6.md) + [`-per-block-ck-extraction-rule.md`](-per-block-ck-extraction-rule.md) |
| 6 | y_λ-weighted per-block uniform rule `c_k^(λ) ≡ c_k` | **NO** | `Σ_λ y_λ(q₀) = 0.7191 ≠ 1` (Wenzl-bridge weights aren't a probability measure at q≠1) — `qbeta_per_block_uniform_rule_verify.py` |

Mechanisms 5–6 were **already** documented as falsified in the framework
(`per-wedderburn-block-c5-c6.md` §"open R&D — no known non-trivial
per-block decomposition rule"); this session cross-confirmed them
independently. The per-block structure is real at the **χ_λ-character
level** (fact 3), but does **not** lift to the precision-ladder
coefficient level.

## The one remaining direction (open, skeptical prior)

Per `per-wedderburn-block-c5-c6.md`, the substantive next direction is
the **Khovanov–Rozansky / KLR-canonical-basis route** (Path 2 of
[`-qbeta-ladder-closure-path.md`](-qbeta-ladder-closure-path.md)), which
operates at the **link-Markov-closure level** (the full Markov trace of
the β-decay tangle) rather than per-block.

**Skeptical prior (AGENTS.md §7b audit precedent, 2026-05-30 KLR dialog
assessment):** the KLR/crystal techniques are *authoring guidance, not
proof-restructure triggers*; the assessment found 0/6 candidate proofs
would meaningfully shorten with a KLR layer. So the KR/KLR route is the
remaining lead but is **not** a promising one — it should be attempted
only with the §7b caveat in mind (do not re-pitch KLR as a
positivity-by-construction or Δ_λ-closure shortcut; those are recurrent
failure modes the §7b audit flags).

## Honest bottom line

- The bridge is **genuinely research-grade and open.** This session did
  not close it; it narrowed the search by ruling out six mechanisms.
- **Production stays Q_N2** (1277 ppb, the μ-p substrate tension floor).
  c_2 = −1 is the only Taylor-exact (derived) rung.
- The c_3+ are **cal-anchored** (reusable calibrated constants, circular,
  labeled, NOT predictions — `qbeta-ck-cache.witness.json`).
- Do **not** re-wire any of mechanisms 1–6 as a derivation. The discipline
  lock (deep-audit addendum §4) catches q₀-dependent residuals as
  form-fitting.

## Witnesses / files

- `computations/qbeta/qbeta-delta-tr-vs-formA.witness.json` (item 1)
- `computations/qbeta/qbeta-scaling-bridge-investigation.witness.json`
- `computations/qbeta/qbeta-per-block-paper-closed-forms.witness.json`
- `computations/qbeta/qbeta_per_block_uniform_rule_verify.py`
- `computations/qbeta/qbeta-ck-cache.witness.json` (cal-anchored tier)
- `content/.../mass-theory/q-beta-categorical-precision-ladder.lean` (§3b-cond `QbetaC3StructuralFormClass`)
- `content/.../braids-and-knots/habiro-precision-ladder-equivalence.lean` (§3b-cond `QbetaHabiroTaylorBridgeClass`)
