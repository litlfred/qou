# ũ = q·u — the ladder variable's bar-weight, and what it touches (read-first)

**Date:** 2026-07-03
**Bean:** `mjim`
**Producer of the finding:**
[`computations/qbeta/qbeta_even_channel_bar_split_probe.py`](../../computations/qbeta/qbeta_even_channel_bar_split_probe.py)
(bean `ai81`, witness `qbeta-even-channel-bar-split.witness.json`, exact);
persistence to s¹⁷:
[`computations/qbeta/qbeta_bar_split_ord17_probe.py`](../../computations/qbeta/qbeta_bar_split_ord17_probe.py)
(bean `08ds`).

## The finding (exact, one line)

Under the bar involution σ: q ↦ 1/q (on s = q−1: σ(s) = −s/(1+s)):

    ℏ_q ∘ σ = −q·ℏ_q       (ℏ_q = (q−1)/q)
    b ∘ σ = b               (b = √(q⁴+q²+1)/(q²+1) is bar-even)
    ⇒  u ∘ σ = q²·u        (u = b·ℏ_q² has bar-WEIGHT 2, it is NOT bar-even)
    ⇒  ũ := q·u = q·b·ℏ_q² is the bar-even ladder variable.

ũ and u agree at leading order (both ~ (√3/2)s²), so every leading-order
statement about "the ladder variable" is unaffected; they differ at the
first subleading order, so **every rung beyond the leading one changes
value with the normalization**.

## Why it matters (what was implicitly wrong)

The c_k precision-ladder discipline (registry, 1jrh lineage, the Casoratian
program) treats the ladder `∏(1+c_k u^k)` and its bar-parity structure as
if `u` were a bar-symmetric variable. It is not: a "bar-even series in u"
is not a bar-even function unless the variable itself is bar-even. The
corpus-wide consequences, verified exactly on the net route (ai81/08ds):

1. The bar-even part of log R **is exactly a ũ-series** (through s¹⁷,
   margin 9) — the clean structure only appears in the ũ normalization
   after an exact parity split.
2. Rung values are normalization-dependent (net route: c₂ = −8.006 in the
   `u`, c₁=0 convention vs e-rungs in ũ after the split, e₁ = 3√3/4) —
   comparing rungs across documents requires stating the variable.
3. The 1jrh "one recurrence, two parities" test's even-channel inputs
   must be read in ũ; the h·D(ũ) + h³·F(ũ) odd-sector form is exactly
   refuted (08ds), and the surviving odd-sector search (ζ₄-residue route,
   bean `0zr0`) should be posed in (ũ, h) variables from the start.

## Standing rule (for c_k / ladder authors)

**State the ladder variable explicitly, and prefer ũ = q·b·ℏ_q² when
bar-parity is load-bearing.** A rung value quoted without its variable
(u vs ũ) and its c₁-convention is under-specified beyond leading order.
This does not invalidate leading-order results (c₂ = −1 bar-odd
brane-tower, Taylor-exact, is unaffected), and per the refuted-discipline
it re-scopes nothing to (b): it is a normalization clarification, scope (a).

## Cross-references to update on contact (not mass-edited here)

- [`2026-07-02-1jrh-aw-one-recurrence-formalize-first-prune.md`](2026-07-02-1jrh-aw-one-recurrence-formalize-first-prune.md)
  — its `u = b·ℏ_q²` is the weight-2 variable; the Casoratian test's
  even-channel rungs should be re-read per
  [`2026-07-03-9fnm-c3even-exact-rational-measurement.md`](2026-07-03-9fnm-c3even-exact-rational-measurement.md).
- `docs/coordination/ck-dk-canonical-registry.md` — rung tables are
  u-convention; annotate on next touch.
- [`channel-rotation-askey-lit`](../../content/quantum-observable-universe/mass-endomorphism/channel-rotation-askey-lit.md)
  — the recurrence-tie discussion inherits the ũ reading.
