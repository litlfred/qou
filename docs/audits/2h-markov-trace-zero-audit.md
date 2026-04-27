# ²H markov_trace = 0 audit

**Source.** [`folio-assistant/computations/atom-nf-symbolic-D.witness.json`](../../folio-assistant/computations/atom-nf-symbolic-D.witness.json)
(D = deuteron = ²H), witness from `atom_nf_symbolic_D.py`.

## What the witness reports

- `n_strands = 6` (²H lives in H_6, not H_2)
- 32 normal-form terms in `nf_top_terms`, each with a non-zero
  rational coefficient in q (degree-40-ish polynomials in q)
- `markov_trace`: `"0"` (string) — symbolically zero
- `at_q0.tr_M_D`: `"0j"` (complex zero) — numerically zero
- `J_62`: `"q - 1 + 2/q - 2/q**2 + 2/q**3 - 2/q**4 + q**(-5)"`
- `at_q0.J_62`: `1.027 + 0i` — non-zero

## What that means

The pipeline computes the symbolic Hecke NF of ²H's atom braid (via
GB-NF) and gets 32 non-trivial NF terms, but their Markov-trace sum
collapses to identically zero. Meanwhile the reference Jones
polynomial of 6_2 is non-trivial and evaluates to ≈ 1.027 at q_0.

**Therefore the Markov closure of ²H's atom braid is NOT 6_2 at the
Hecke-algebra level.** Either:

1. **²H's atom braid genuinely closes to a different link** (possibly
   a trivial / split link, since tr_M ≡ 0 is a strong identity that's
   compatible with split links — but most link types have non-zero
   Markov trace). The α\* = 0.546 anomaly from
   [`prop:atom-knot-mass-derivation`](../../content/quantum-observable-universe/braids-and-knots/atom-knot-mass-derivation.md)
   already showed 6_2 is structurally inconsistent with ²H's
   PSD profile; this corroborates from the trace side.
2. **There's a bug in `markov_trace_canonical.tr_M_element`** (the
   sum-over-NF function) that produces zero spuriously. To
   discriminate, run `tr_M(σ_0)` directly — it should equal
   z = 1/(q^{1/2} + q^{-1/2}), not zero. If it returns z, the
   sum-collapse is structural; if it returns zero, fix the bug.

## Discriminating test (run, **2026-04-27**)

```
$ python3 -c "from markov_trace_canonical import tr_M_word, Z_SYMB, H_SYMB; ..."

tr_M([])        in H2 = 1
tr_M([0])       in H2 = sqrt(q)/(q + 1)               = z          ✓
tr_M([0,1])     in H3 = q/(q + 1)**2                  = z²         ✓
tr_M([0,1,0])   in H3 = (sqrt(q)*(q+1) + q²-1)/(q+1)² = h·z² + z   ✓
```

All three canonical Markov-trace identities return the correct
symbolic values. **The trace function is not buggy.**

**Therefore the markov_trace = 0 result for ²H is structural.**
²H's atom braid genuinely closes to a link with zero Markov trace,
which is *not* 6_2 (J_{6_2}(q_0) ≈ 1.027). The historical 6_2 ID is
**structurally refuted** — corroborates the α\* = 0.546 PSD-cone
anomaly.

This is a strong identity: tr_M ≡ 0 in ℚ(q) means the symbolic Jones
polynomial of ²H's atom braid (= Markov closure as a link) is the
zero polynomial. The simplest such link is the unknot disjoint
union — i.e., split links with one trivial component. Whether ²H's
true link class is split needs further structural analysis (run
the closure, check for Reidemeister reductions to a split form).

## Connection to the ³H investigation

Both ²H (α\* = 0.546, tr_M = 0) and ³H (α\* = 0.424, multi-d blocks
all fail PSD) have `manual-historical-volume-match` methodology
tags. The PSD-cone failures and the trace collapse are pointing at
the same underlying cause:

- The historical knot IDs (6_2 for ²H, 8_11 for ³H) were assigned
  by *volume search* (Vol_hyp(K) ≈ B_AME / m_e), without a
  consistency check against the categorical pipeline's actual atom
  braid.
- The volume search is now flagged `deprecated-volume-match` in
  [`methodology-deprecation.witness.json`](../../folio-assistant/computations/methodology-deprecation.witness.json),
  but the historical entries persist in the witnesses until R5-full
  (SDP-as-solver) produces canonical T_w from the categorical
  pipeline directly.
- Once R5-full lands, the correct knot IDs will be read off from
  the SDP solution (or refuted, if the SDP shows the atom braid is
  not the closure of any single hyperbolic knot — possible for
  split/composite links).

## Next step

If it is to be done before R5-full: run the discriminating test
above. If `tr_M_element` is correct, both ²H and ³H need the
historical IDs flagged as **structurally refuted**, and any
paper-side narrative that says "²H closes to 6_2" needs an asterisk
pointing to this audit.
