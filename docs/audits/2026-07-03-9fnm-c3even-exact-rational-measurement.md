# 9fnm — c₃^even measured exactly; the even-channel u-ladder form is exactly obstructed

**Date:** 2026-07-03
**Bean:** `9fnm` (the gated measurement
[`2026-07-02-1jrh`](2026-07-02-1jrh-aw-one-recurrence-formalize-first-prune.md)
named as its decisive experiment)
**Branch / PR:** `claude/aj-conjecture-qou-tz4dyd` / [#3262](https://github.com/litlfred/qou/pull/3262)
**Producer:** [`computations/qbeta/qbeta_ck_sseries_exact_rational.py`](../../computations/qbeta/qbeta_ck_sseries_exact_rational.py)
(witness `qbeta-ck-sseries-exact-rational.witness.json`; exact ℚ(√3)[[s]]
truncated-series arithmetic — no mp.taylor, no fit; 4/4 assertions; ~5 s)

**Bottom line.** The measurement 1jrh gated on is done — exactly — and it
returns more than a rung: the net-route (bar-even / binding) ladder is
**exactly obstructed** in the `∏(1+c_k u^k)` form. All findings scope (a)
(this ansatz / this ladder variable, as-is), tiered per the c_k discipline.

## Exact rungs (net route, standard c₁ = 0 convention)

| rung | exact (ℚ(√3)) | numeric |
|---|---|---|
| c₂^even | `−1049/144 − 5√3/12` | **−8.00641…** (the predecessor's −8.006, now exact) |
| c₃^even | `841/144 + 604739√3/12960` | **+86.6612** |
| c₄^even | `−2483340421/1451520 − 120701√3/1920` | −1819.74 |

The predecessor's refusal of c₃⁺ (odd-order mp.taylor noise ~10⁴) is
resolved: those "unstable" odd orders are **real exact structure** (below).

## The exact obstruction (the load-bearing finding)

Order-by-order residual `log R − model` after fixing c₂..c₄ at even orders:

- `[s²] = 9/8` exactly, `[s³] = −3.908…`, `[s⁵], [s⁷], … ≠ 0` — the k ≥ 2
  ladder produces **nothing** at s²/s³, so the standard-convention ansatz
  fails **before any c_k is chosen**.
- **c₁-inclusive re-solve:** `c₁' = 3√3/4` absorbs s² exactly, rungs shift
  to (c₂', c₃', c₄') = (−11.913, +132.455, −2699.84) — but
  `[s³] = −1.658… ≠ 0` **survives**, with all higher odd orders nonzero.

So: **no rung assignment makes the net route a `∏(1+c_k u^k)` ladder in
`u = b·ℏ_q²`** — and the rung values are convention-dependent projections
(c₂: −8.006 vs −11.91), not intrinsic constants. Scope (a): this constrains
the *ansatz with this ladder variable*, not the AW ingredient; the odd-in-s
residual pattern **is the measured size of the missing structure** (per the
refuted-discipline permanence principles). Note the odd channel is
unaffected: its `c₁ = 0` seed and `c₂ = −1` are proved on the brane-tower
route, a different object.

## The 1jrh Casoratian test, as far as it can now be run

- **W₂ = c₂^even·c₃^odd − c₃^even·c₂^odd = +102.67** — robustly positive
  (c₃^even = +86.7 is far from the −16 ambiguity threshold 1jrh worried
  about; also positive in the c₁-inclusive convention, +156). No sign
  violation at this rung.
- **W₃ (CONDITIONAL on the CAL-anchored, untrusted-tier c₄^odd ≈ −0.97):
  −3723.5, so sign(W₃/W₂) = −1 — violating the AW-positivity prediction
  (+1).** Per 1jrh's own caveat this is conditional on the c₄^odd tier and
  is **not** a durable refutation; it is a tier-flagged red flag.
- Both inherit the obstruction caveat: if the even channel is not a
  u-ladder at all, the "two parities of ONE recurrence *in these rungs*"
  premise is undermined on the even side independently of any sign.

## Follow-up (same day, bean `ai81`) — the even-channel variable, found

[`computations/qbeta/qbeta_even_channel_bar_split_probe.py`](../../computations/qbeta/qbeta_even_channel_bar_split_probe.py)
(witness `qbeta-even-channel-bar-split.witness.json`) split log R **exactly**
under the bar involution σ: s ↦ −s/(1+s) (series composition, no numerics)
and tested the companion-bar-odd-variable hypothesis of
`conj:binding-qbeta-complex-volume`. Results (all exact):

1. **The ladder variable itself was mis-normalized corpus-wide**: u = b·ℏ_q²
   is NOT bar-even — ℏ(1/q) = −q·ℏ(q) exactly, so u∘σ = q²·u (bar-weight 2).
   The genuinely bar-even ladder variable is **ũ = q·u = q·b·ℏ_q²**
   (agrees with u at leading order, differs at higher rungs).
2. **(a) The bar-even part E of log R IS exactly a ũ-series** through s¹¹:
   5 rungs (e₁ = 3√3/4 — matching 9fnm's c₁′ exactly, a cross-check —
   e₂ ≈ −15.035, e₃ ≈ −58.409, e₄ ≈ −276.55, e₅ ≈ −1817.30), with all 6
   over-determining residual orders **exactly zero**. The honest bar-even
   rungs are these e_k, read from E after exact bar-projection — not the
   mixed-parity projections of 9fnm/predecessor.
3. **(b) The bar-odd part**: O/h (h = q − 1/q, exactly bar-odd) is a
   ũ-series through s¹⁰ (d₁ ≈ −1.607, d₂ ≈ −16.137, …), failing exactly
   and only at s¹¹ (residual ≈ −13000.75). The natural absorber is an
   h³·F(ũ) term (odd powers of h); discriminating it needs a higher
   truncation order — **flagged as the next measurement, not fitted**
   (one failing order vs multiple new coefficients would be
   under-determined at this ORD, the Δ_λ-gate pattern).

Net: to this truncation, **log R = E(ũ) + h·D(ũ) + O(s¹¹) in the odd
sector** — the even channel is a clean ũ-ladder once the parity split and
the ũ-normalization are done exactly. Scope (a) throughout; no wiring.

## Disposition

1. **Bean `9fnm` closes**: c₃^even is measured (exactly, both conventions);
   the Casoratian test is run to the extent its inputs allow.
2. **`conj:binding-qbeta-complex-volume` / `ChannelLeonardDuality` are NOT
   refuted** — the obstruction is (a)-scoped to the `u`-ladder form. The
   productive re-pose: find the even-channel **ladder variable** (or the
   complex-𝔙 normalisation) in which the s-odd structure is absorbed —
   e.g. a bar-odd companion variable pairing with `u`, or the ζ₄-residue
   constraint of the conjecture's fields. The exact residual table in the
   witness is the target data for that search.
3. **Do not wire anything**: c_k≥3 remain owner-gated (registry §8,
   proton+muon cross-anchor test); the exact rungs here are net-route
   projections, not production constants.
