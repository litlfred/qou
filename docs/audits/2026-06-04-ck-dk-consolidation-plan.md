# c_k / d_k consolidation — ONE canonical registry (plan)

**Date:** 2026-06-04
**PR:** (this branch — `claude/ck-dk-consolidation-2026-06-04`)
**Status:** DONE — registry delivered in this PR:
[`docs/coordination/ck-dk-canonical-registry.md`](../coordination/ck-dk-canonical-registry.md)
(+ machine-readable [`ck-dk-registry.json`](../coordination/ck-dk-registry.json)).
This doc is retained as the motivation/plan record.

## Why

The author reports paper / compute / audit docs **disagree** around
`c_k` and `d_k`, and asks to **consolidate to ONE approach/infra** with
explicit **canonical-vs-empirical** tracking. This has come up 3–4 times
(see the 2026-05-30 deep audit quoting prior author guidance: *"I don't
want to keep coming back to this"*), and the disagreement is real:

1. **Overloaded symbols.** `c_k` and `d_k` each denote ≥3 distinct
   objects across the corpus:
   - `c_k` = Q_β β-decay precision-ladder coefficients
     (`Q_β = Q_base·∏(1 + c_k·u^k)`).
   - `c_k(n)` = exponents in the cyclotomic expansion
     `F_n(z) = ∏(1 − q^{−k}z)^{−c_k(n)}` — a **different** object.
   - `(c_k, d_k)` = eigenvalue-factor pair in
     `χ_sym(β) = ∏_k (c_k q + d_k)` — a **different** object.
   - `d_k` = m_p mass brane-tower coefficients (the mass-side analog of
     the Q_β ladder).
   - `d_k` = chain-complex differential (`d_{k+1}∘d_k = 0`) —
     **unrelated** homological `d`.

2. **Drifted status.** Multiple audit docs each assert a different
   "current state" for the Q_β `c_k` ladder and m_p `d_k` tower, and they
   have flip-flopped (wired ↔ de-fit ↔ reverted) 4+ times:
   - `2026-05-30-qbeta-ck-mp-dk-deep-audit.md` — body SUPERSEDED by its
     own addendum.
   - `2026-05-31-qbeta-ck-truncation-order-canonical-framing.md`.
   - `2026-06-03-l2-closure-habiro-3-q-25-universal-template.md`.
   - `2026-06-04-c3-habiro-3rung-crossanchor-rigidity-falsification.md`.
   - AGENTS.md "c_3 SETTLED" note + the 6-entry flip-flop table in
     `docs/coordination/1ppq-qbeta.md`.

## Authoritative current state (2026-06-04, to be encoded in the registry)

| family | rung | status | form | wire |
|---|---|---|---|---|
| Q_β `c_k` | c_2 | **CANONICAL** (Taylor-exact, PROVED — Kashiwara f̃₁²) | −1 | **WIRED** (Q_N2) |
| Q_β `c_k` | c_3 | **EMPIRICAL** (proton-anchor near-match; FALSIFIED as real-q fibre element, cross-anchor) | J−ℏ² / [3]_q/25 candidates | conditional (§3b-cond), NOT wired |
| Q_β `c_k` | c_4 | **EMPIRICAL / artifact** (normalisation artifact in qbeta_1ppq_achieved) | c_3·b⁴ | NOT wired |
| Q_β `c_k` | c_5+ | **CONJECTURE** | 3c_3²+b | NOT wired |
| m_p `d_k` | d_4 | **EMPIRICAL** near-match (0.05%) | J²·11+2 = 46 | NOT wired |
| m_p `d_k` | d_5 | **EMPIRICAL** | J² = 4 | NOT wired |
| m_p `d_k` | d_6 | **TBD** (closest-integer, no form) | −29 | NOT wired |

Honest production: **Q_β = Q_N2 (c_2 only); m_p bare.** Only c_2 is
canonical-derived; everything else is empirical / conjectural / refuted.

## Deliverable — ONE registry

A single authoritative source of truth:
`docs/coordination/ck-dk-canonical-registry.md`, containing:

1. **Symbol disambiguation table** — every meaning of `c_k`/`d_k`, the
   canonical Q_β-ladder / m_p-tower senses flagged, the others
   cross-referenced (resolves the overloading).
2. **Per-rung registry** — status (CANONICAL-PROVED / EMPIRICAL-NEAR-
   MATCH / CONJECTURE / ARTIFACT / REFUTED / TBD), form, residual,
   anchor-dependence, authoritative producer (script / witness / Lean),
   current wire status.
3. **Production-wiring statement** — the ONE "what is wired."
4. **Supersession list** — every scattered doc this registry replaces,
   each to get a one-line "→ superseded by the registry" banner.
5. **Flip-flop guard** — the standing rule: no re-wire of c_3+/d_4+
   without owner approval + a passing cross-anchor test; the registry is
   the decision record.

Optional follow-up (noted, not in this PR): a machine-readable
`ck-dk-registry.json` the dashboards can read.

## Guards

- Canonical ⇔ Taylor-exact / proved to compute precision AND anchor-
  stable. Everything else is empirical (and labelled with its tier).
- No production wiring change in this PR — it is a consolidation of
  STATUS, not a re-wire (which is the flip-flop trap).
- Cross-link, don't duplicate: the registry points to the producers;
  the scattered docs point to the registry.
