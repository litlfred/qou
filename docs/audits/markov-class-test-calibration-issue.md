# Markov-class invariant test — calibration issue (correction to earlier audits)

**Status:** correction. Earlier commits claimed `²H/6_2`, `³H/8_11`,
`³He/L_6a4` were structurally refuted via the Markov-class invariant
ratio test. **That conclusion was premature**: the test as implemented
in `atomic_tr_m_mpfr_50dps.py` and `atomic_tr_m_via_wenzl_bridge.py`
compares `tr_M(T_w, q_0)` directly against the canonical Jones
polynomial `J_K(q_0)`, but those two quantities differ by a
**convention-dependent scaling factor** (writhe, normalisation,
strand count), not just by `q_0^k` for integer k.

## What the sanity check showed

The right-handed trefoil 3_1 is, by construction, the closure of
σ_1^3 in B_2. So `tr_M(σ_1^3)` should equal `J_{3_1}(q)` up to a
known convention factor. Run the test on the electron registry
entry (`braid_word = [1, 1, 1]`, n=2):

```
tr_M(σ_1^3, q_0)        = 0.7302040436...
J_{3_1}(q_0)             = 0.9595771600...   (using q + q³ − q⁴)
tr_M / J_{3_1}           = 0.7609643852...
log(|ratio|)/log(q_0)    = −2.618             ← not an integer
```

A "writhe-normalised match" would require the log-ratio to be
integer. **It isn't, even for a known-correct identification.**

Therefore the test methodology is mis-calibrated. The earlier
claims that:

- `²H/6_2  refuted` (log-ratio = −9.32)
- `³He/L_6a4 refuted` (log-ratio = −0.327)
- `³H/8_11 refuted`  (log-ratio = −34.13)

cannot be sustained on this evidence alone. They could all be
correct knot IDs whose log-ratios reflect convention factors,
not structural mismatch.

## Root cause

The Markov trace `tr_M(β)` and the Jones polynomial `J_K(q)` are
related by

  `V_K(q) = (-1)^{n-1} · q^{(3w-n+1)/4} · tr_M(β) / (q^{1/2} - q^{-1/2})^{n-1}`

where `n` is strand count and `w` is writhe — not just `q^k`. The
factor `(q^{1/2} - q^{-1/2})^{n-1}` and the writhe-correction `q^{(3w-n+1)/4}`
together form a much richer correspondence than my code's "is
log-ratio integer?" check assumed.

Even within a fixed convention, different sources publish J_K
under different sign / normalisation conventions (e.g., `q` vs
`q^{-1}`, `t` vs `q^2`).

## What's still validated

The Wenzl-bridge `tr_M` computation itself is internally consistent:

- Multiple representations of proton, neutron, ³He (all using the
  same 6-letter Borromean in B_3) give identical `tr_M` to 50 dps
  via the Hoefsmit + y_λ path.
- Deuteron (Z=1, N=1) at the **3A-strand convention** (B_6, 32
  NF terms) gives `tr_M(q_0) ≈ 0.388286471547`, matching
  `canonical-mass-table.witness.json` (independent older Python
  computation) to 6+ significant figures.
- The α* presentation-dependence finding stands: it's about the
  `dump_block_matrices` symmetric-part PSD test on different
  Markov-equivalent braid representatives, which doesn't depend on
  the J_K comparison.

## What is *also* worth noting (independent of J comparison)

Within our pipeline, the SAME atom under different braid
representations gives DIFFERENT `tr_M(q_0)`:

| Atom | Representation | tr_M(q_0) |
|------|----------------|-----------|
| ²H   | 3A-strand B_6 (atom_braid_word_3A) | 0.388286 |
| ²H   | SDP-witness B_3 (`[1,-2,1,1,1,-2]`) | 0.288326 |

`0.388 / 0.288 = 1.347`; `log/log(q_0) = +2.86` — non-integer.

If both representations are supposed to encode the same physical
deuteron, their `tr_M(q_0)` values should match exactly (Markov-
class invariance in our pipeline's own convention). The
discrepancy means **one of the two ²H representations is wrong
within QOU's own framework**, not necessarily that 6_2 is wrong as
a knot ID.

This is a smaller-scope, internal-consistency claim that the
data does support, and is worth tracking separately from the
J-vs-tr_M convention question.

## Action items

1. **Walk back the "structurally refuted" claims** for ²H/6_2,
   ³H/8_11, ³He/L_6a4 in commits `7412a3e5` and `72cfe1fa`.
   They aren't refuted by this evidence; they aren't confirmed
   either.
2. **Calibrate the J_K test** with the correct factor:
   - Determine the writhe `w` of each braid representative
     (sum of crossing signs).
   - Substitute the formula
     `V_K(q) = (-1)^{n-1} · q^{(3w-n+1)/4} · tr_M(β) / (q^{1/2}-q^{-1/2})^{n-1}`
     and check whether the corrected V_K matches the published J_K.
   - The trefoil sanity check at q_0: if calibrated correctly, log-
     ratio of (corrected V_K) / J_{3_1} should be 0 (integer 0,
     trivially passing).
3. **Investigate the within-pipeline 3A vs SDP-witness deuteron
   discrepancy** as an independent finding — that one IS internal,
   doesn't depend on convention factors.
4. **Update master-prop α\* table caveat** with the proper context:
   α\* presentation-dependence is still a real finding (commit
   `077f3baf` is correct), but the J_K refutations need calibration
   before being cited.

## Stability for downstream consumers

`atomic-tr-m-wenzl-bridge.witness.json` carries reliable `tr_M(q_0)`
values; only the `historical_K_comparison.writhe_match` boolean is
uncalibrated. Consumers should ignore that field until issue 2 is
resolved.
