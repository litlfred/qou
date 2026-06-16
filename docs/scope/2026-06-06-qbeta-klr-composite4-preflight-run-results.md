# KLR tranche-2 Composite-4 preflight RUN — results (BUILD NOT AUTHORISED)

**Companion to [the preflight SCOPE](2026-06-06-qbeta-klr-composite4-wenzl-qpoch-preflight.md) (PR #1914).** One-session formalize-first preflight RUN gating the cont. 9 Option B (5-6 session Wenzl × q-Poch infra build). Verdict: **PARITY PASS / C_2 MAGNITUDE FAIL** ⇒ **build NOT authorised**.

## Result

[`qbeta_klr_composite4_preflight_run.py`](../../computations/qbeta/qbeta_klr_composite4_preflight_run.py) computes `A_k = tr_M(p_k^JW) · Q_k` for `Q_k ∈ {(q;q)_k, Y_k}` at both anchors (mp 65-dps) and tests against the proved `c_2 = -1` target:

| anchor | `(q;q)_2` | `Y_2 = q^{-3/2}(q;q)_2` | `A_2 = tr_M(p_2^JW)·Y_2` | `A_2 / c_2_target` |
|---|---|---|---|---|
| proton | `2.55208e-02` | `2.18234e-02` | **`-1.08969e-02`** | `1.08969e-02` |
| muon | `2.55208e-02` | `2.18234e-02` | **`-1.08969e-02`** | `1.08969e-02` |

Both anchors give identical A_2 to 6 figs (Composite 4 is q-rigid at this order). **A_2 is ~92× too small to be c_2 = -1.**

| gate | result |
|---|---|
| Parity (Y_3 bar-odd at k=3) | ✅ PASS (analytical, scope §3c; Gemini-corrected sign) |
| c_2 magnitude (|A_2| ≈ 1 at both anchors) | ❌ **FAIL by 92×** at both anchors |
| Verdict | **`PARITY_PASS_C2_MAGNITUDE_FAIL_BUILD_NOT_AUTHORISED`** |

2 assertions pass (parity gate; c_2 magnitude gate is **decisive** — passes-or-fails-by->10× at both anchors, not borderline).

## Why this is decisive (not a near-miss / fit-rescuable)

The bare cont. 9 ansatz `A_k = tr_M(p_k^JW) · (q;q)_k` and the Gemini-corrected renormalisation `A_k = tr_M(p_k^JW) · Y_k` are the only two **non-fit** normalisations the scope identified. Both give |A_2| ≈ 0.011 at q₀, off the proved c_2 = -1 target by a factor that is:
- **q-INDEPENDENT** (identical at proton and muon anchors to 6 figs) — so cannot be absorbed by a q-dependent normalisation,
- **NOT a near-match** (off by 92×, well beyond any cross-anchor swing or precision-floor noise),
- **NOT closeable by a constant rescaling** (introducing a global scalar `C` such that `C · A_2 = -1` would be a single-parameter FIT — forbidden by the Δ_λ gate + the 3-calibration discipline).

So Composite 4 in either of its non-fit forms **cannot source c_2 = -1**, let alone the bar-odd c_3. The 5-6 session Wenzl + `pyhecke` linear-`tr_M` extension build (cont. 9 Option B) would discover this failure *at the end*; the one-session preflight surfaces it *now*.

## What this saves + redirect

| state | cost |
|---|---|
| **Avoided**: cont. 9 Option B build that would fail at c_2 magnitude | ~5-6 sessions of Wenzl Lean + `pyhecke` linear-`tr_M` infra |
| **Spent**: this preflight (scope #1914 + RUN) | ~1 session (scope + RUN combined) |
| **Net**: formalize-first refutation savings | ~5× ROI on the preflight |

**Redirect (per cont. 9 menu, master infra scope §97-104):**

- **Option C — Composite 1 (Demazure × q-Pochhammer), 5-7 sessions**. Demazure character `D_w(λ)` is genuinely useful beyond Q_β (mass-formula crystal-multiplicity work). Same preflight pattern should apply before committing to the build: derive the analogous A_2 = D_w(λ)·(q;q)_k product and check c_2 magnitude.
- **Option D — Composite 3 (Type-B folded crystal), 12-17 sessions**. Aligns with CLAUDE.md §7b §"symmetric-crystal techniques" authoring guidance; highest theoretical value.
- **Option A — accept residue A as inherently CAL-3-anchored permanently**. Now reinforced by *three* corpus-side closures + a preflight refutation; the absolute c_3 closure is research-grade unknown.

## Cross-refs

- Preflight SCOPE (PR #1914 — the prediction this RUN now resolves): [`2026-06-06-qbeta-klr-composite4-wenzl-qpoch-preflight.md`](2026-06-06-qbeta-klr-composite4-wenzl-qpoch-preflight.md).
- Master KLR-infra roadmap: [`2026-06-03-qbeta-residue-a-klr-crystal-infra-scope.md`](2026-06-03-qbeta-residue-a-klr-crystal-infra-scope.md).
- Proved `c_2 = -1` / `Φ₁ = √2`: PR #1887, ledger cont. 14.
- Wenzl chain α NEGATIVE alone (cont. 5): [`qbeta_wenzl_habiro_chain_alpha.py`](../../computations/qbeta/qbeta_wenzl_habiro_chain_alpha.py), [`qbeta-wenzl-habiro-chain-alpha.witness.json`](../../computations/qbeta/qbeta-wenzl-habiro-chain-alpha.witness.json).
- Witness: [`qbeta-klr-composite4-preflight-run.witness.json`](../../computations/qbeta/qbeta-klr-composite4-preflight-run.witness.json).
