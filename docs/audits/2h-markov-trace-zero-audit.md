# ²H markov_trace = 0 audit — RESOLVED: stale witness

**TL;DR (2026-04-27 update).** The `markov_trace = "0"` claim in
[`atom-nf-symbolic-D.witness.json`](../../computations/atom-nf-symbolic-D.witness.json)
(timestamp 2026-04-24) is **stale**. A fresh re-run of
`atom_nf_symbolic_D.build_atom_nf_symbolic(1, 1)` followed by
`tr_M_element` on 2026-04-27 gives `tr_M(²H, q_0) ≈ 0.388286471547`,
matching the `tr_M_atom = 0.388286471547` value in the older
[`canonical-mass-table.witness.json`](../../computations/canonical-mass-table.witness.json)
(2026-04-18). So ²H's tr_M is NOT zero — the witness predates a
fix in the code path. **The historical 6_2 ID is not refuted by
this trace value (though it remains under suspicion via α\* = 0.546).**
Re-emit `atom-nf-symbolic-D.witness.json` to correct.

Fresh values via 3A-strand convention at q_0 = 1.1099786:
- proton  (Z=1, N=0): tr_M ≈ 1.06530623
- neutron (Z=0, N=1): tr_M ≈ 0.92323330
- ²H      (Z=1, N=1): tr_M ≈ 0.38828647

---

# Original audit (preserved for posterity)

**Source.** [`computations/atom-nf-symbolic-D.witness.json`](../../computations/atom-nf-symbolic-D.witness.json)
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

## Refinement — which "²H atom braid" exactly?

The `atom_nf_symbolic_D.py` script uses
`mass_at_3A_proper.atom_braid_word_3A` — the **3A-strand atom-braid
convention**: for an atom with A nucleons, each nucleon contributes
three strands (intra g_0, intra g_1, and inter-crossing). For
deuteron (A = 2), the result lives in H_6 (= 3A = 6 strands), not
H_2.

This is a different representation from the simple Borromean
braid σ_1 σ_2^{-1} σ_1 σ_2^{-1} on B_3 used elsewhere. Habiro
expansion in
[`habiro-coefficients-atomic.witness.json`](../../computations/habiro/habiro-coefficients-atomic.witness.json)
reports proton's tr_M as a non-zero degree-48 polynomial in u
= q^{1/2}; deuteron isn't included in that witness.

So the precise statement is: **the 3A-strand atom-braid of ²H in
H_6 has tr_M ≡ 0 in ℚ(q)**, while a different (simpler) braid
representation might give a non-zero trace. The PSD-cone result
(α\* = 0.546) is computed from a yet-different representation
(²H listed as `n_strands = ?` in `joint-tower-sdp-rust.witness.json`).

The cleanest interpretation: the historical 6_2 ID was assigned by
volume-search against B(²H)/m_e, and *no* of the three internal
representations (3A-strand, joint-tower-SDP, simple Borromean) is
guaranteed to close to 6_2. R5-full will pick the correct
canonical T_w from the categorical pipeline, decisively replacing
the volume-search shortcut.

## Remaining structural questions

1. Why does the 3A-strand braid of ²H have tr_M ≡ 0 identically?
   That's a strong identity — most braids don't. It may indicate
   the 3A-strand convention puts deuteron at a *trace-cancellation
   stratum* (one of the GB filtration's higher-codim slices). Worth
   running the same script on the 3A-strand proton (Z=1,N=0,A=1)
   and neutron (Z=0,N=1,A=1) to see if those traces are also zero
   or non-zero.
2. Is the α\* = 0.546 number consistent with the Habiro witness's
   non-zero deuteron expansion (which the description claims
   exists, even though the witness `results` field only contains
   proton and neutron)?

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
  [`methodology-deprecation.witness.json`](../../computations/methodology-deprecation.witness.json),
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
