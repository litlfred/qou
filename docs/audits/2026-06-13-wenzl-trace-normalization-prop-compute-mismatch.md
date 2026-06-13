# Audit — `prop:h3-markov-wenzl-weights` (Jones/TL) vs the canonical compute trace (Ocneanu/Wenzl-Schur)

**Date:** 2026-06-13
**Trigger:** owner request — "check all compute for these issues" after
[`c2df3870`](https://github.com/litlfred/qou/commit/c2df3870) ("uniform-Wenzl
claim was WRONG — corrected to closed-form (1/2, 1/4, 0)") landed on `main`
via PR #2191.
**Flag thread:** [PR #2191 follow-up comment](https://github.com/litlfred/qou/pull/2191#issuecomment-4696810137).
**Verdict:** the corrected prop matches the canonical compute **at q=1** but
its **q-dependent closed forms diverge from the compute at q≠1**. The prop's
closed forms are the **Jones/Temperley–Lieb** weights (`y_(1³)≡0`); the mass
pipeline uses the **full-Hecke / Ocneanu** Markov trace (`y_(1³)≠0`), proven
canonical in
[`2026-05-05-y-lambda-tr-m-equivalence-proof.md`](2026-05-05-y-lambda-tr-m-equivalence-proof.md).
**No compute or mass numbers are changed by this audit** — it documents the
inconsistency and the adjudication the author must make.

## 1. What `c2df3870` fixed (correctly)

PR #2191 originally codified `prop:symmetric-point-wenzl-markov-uniform`
claiming the H_n Wenzl/Markov weights are **uniform at the symmetric point**,
`y_λ(q=1) = 1/[2]_q^{\,n−1}|_{q=1} = 1/2^{n−1}` — for H_3 that reads
`(y_(3), y_(2,1), y_(1³))|_{q=1} = (1/4, 1/4, 1/4)`. A Gemini review caught
this as false. `c2df3870` renamed the block to `prop:h3-markov-wenzl-weights`
and corrected the q=1 values to **(1/2, 1/4, 0)**, with q-dependent closed
forms

$$
y_{(3)}(q) = \frac{[4]_q}{[2]_q^{3}}, \qquad
y_{(2,1)}(q) = \frac{1}{[2]_q^{2}}, \qquad
y_{(1^3)}(q) = 0 \ \text{(identically)},
$$

justified by the Temperley–Lieb quotient (the Jones polynomial kills the
fully-antisymmetric 3-row partition) and a chirality argument (the
Jones-normalised trace is not bar-involution invariant).

**At q=1 this is consistent with the compute** — see the table below. The
fix was a genuine improvement over the uniform claim.

## 2. The residual mismatch at q≠1

The mass pipeline's H_3 weights are produced by
[`y_lambda_wenzl_bridge_numeric`](../../folio-assistant/computations/y_lambda_wenzl_bridge.py)
(the **Wenzl Schur-principal specialization**, Path B of the 2026-05-05
equivalence proof) and cached in
[`y-lambda-at-q0.witness.json`](../../folio-assistant/computations/y-lambda-at-q0.witness.json).
Comparing the live cache to the prop's closed forms:

| λ | compute (Ocneanu/Wenzl-Schur), q=1 | prop closed form, q=1 | compute, q₀ (live cache) | prop closed form, q₀ |
|---|---|---|---|---|
| (3)   | 1/2 | 1/2 | `0.41539579536061…` | `[4]/[2]³ = 0.50531…` |
| (2,1) | 1/4 | 1/4 | `0.28092963103101…` | `1/[2]² = 0.24731…` |
| (1³)  | 0   | 0   | **`0.02274494257734…`** | **`0`** |

Both columns satisfy the Markov normalisation `Σ_λ y_λ · d_λ = 1`
(`d = (1,2,1)`), so both are *legitimate* Markov-normalised weight systems —
**but they are different traces**:

- The prop's closed forms are the **Jones / Temperley–Lieb** weights:
  `y_(1³) ≡ 0` because the Jones polynomial factors through TL_3, killing the
  3-row partition.
- The compute uses the **full Hecke / Ocneanu** Markov trace with parameter
  `z = 1/(q^{1/2} + q^{-1/2})`. For λ=(1³) the Wenzl Schur-principal
  specialization gives
  `s_(1³) = Q^{3}·(1−Q^{r})(1−Q^{r−1})(1−Q^{r−2}) / ((1−Q³)(1−Q²)(1−Q))`,
  which is **generically nonzero** — hence `y_(1³)(q₀) ≈ 0.0227 ≠ 0`.

This Ocneanu reading is the one **proven canonical** in
[`2026-05-05-y-lambda-tr-m-equivalence-proof.md`](2026-05-05-y-lambda-tr-m-equivalence-proof.md):
Path A (ladder linear system encoding `tr_M(σ_i)=z`) equals Path B (Wenzl
Schur) as a Laurent-polynomial identity over ℤ, for **all three** partitions
of 3 including (1³).

## 3. Why the headline masses are unaffected

For a 1-dimensional rep, `σ_i` acts by a scalar: `χ^{(3)}(β) = q^{w}` (trivial,
`σ_i ↦ q`) and `χ^{(1³)}(β) = (-q^{-1})^{w}` (sign, `σ_i ↦ -q^{-1}`), where
`w = writhe(β)`.

- **Physical braids (nucleons, nuclei) are writhe-0, π = id**, so
  `χ^{(3)} = χ^{(1³)} = 1` and only the combination `y_(3) + y_(1³)` and
  `y_(2,1)` enter. Moreover the **headline proton/neutron masses do not use
  the `y_λ·χ_λ` sum at all** — they use the Borromean mass-splitting closed
  form `Δm/M_N = ℏ_q²·h_q·[2]_q·(1+ℏ_q³)/3`
  ([`m_p_borromean_verification_50dps.py`](../../folio-assistant/computations/m_p_borromean_verification_50dps.py)).
  So `m_p`, `m_n`, and the atomic-mass headline numbers are **independent of
  this split**.

- **Where it bites:** `closed_form_tau_M(Z, N, q, τ_p, τ_n)` and the per-knot /
  hadron-knot tables
  ([`per_knot_mass_table_demonstration.py`](../../folio-assistant/computations/per_knot_mass_table_demonstration.py),
  [`hadron_knot_table.py`](../../folio-assistant/computations/hadron_knot_table.py))
  evaluate `tr_M` on **writhe≠0** braids, where `χ^{(3)} = q^{w}` and
  `χ^{(1³)} = (-q^{-1})^{w}` differ and the individual `y_(3)` vs `y_(1³)`
  split *does* matter. Under the prop's Jones/TL weights these tables would
  give different numbers than the compute's full-Hecke weights.

## 4. Other compute carrying a stale y_λ understanding

Two **exploratory probes** (not production; both pre-date the c2df3870 fix)
encode their own q=1 weight assumptions that are inconsistent with both the
corrected prop and the compute:

- [`borromean_h3_2_1_irrep_derivation.py`](../../folio-assistant/computations/borromean_h3_2_1_irrep_derivation.py)
  (lines 17, 226, 230–231): comments assert
  `y_(3) = y_(2,1) = y_(1,1,1) = 1/6` at q=1 (a Plancherel-squared reading),
  and elsewhere "`y_(3) + y_(1,1,1)` both give 1."
- [`crystal_yekutieli_probes_abcd.py`](../../folio-assistant/computations/crystal_yekutieli_probes_abcd.py)
  (lines 157–169): uses `y_(1,1,1) = 1/(q + 1/q + 2)` (nonzero, → 1/4 at q=1),
  i.e. the full-Hecke reading — **consistent with the compute, not the prop**.

These are truth-tracking probes; they should be reconciled to whichever
convention the author declares canonical (§5), but they do not feed production.

## 5. Adjudication required (author's call)

The mismatch is a genuine fork that the framework's own naming does not
settle — CLAUDE.md §7a calls the trace "the Jones polynomial" (suggesting TL,
`y_(1³)=0`), yet the entire validated compute pipeline + the 2026-05-05 proof
use the full-Hecke Ocneanu trace (`y_(1³)≠0`). Two coherent resolutions:

1. **Compute is canonical (Ocneanu/full-Hecke).** `prop:h3-markov-wenzl-weights`
   should either be **scoped/renamed** to make clear it describes the Borromean
   **Jones polynomial** specifically (where `χ^{(1³)}=0` makes the TL reading
   correct *for that braid*), or its q-dependent closed forms should be
   replaced with the **Wenzl-Schur** forms (`y_(1³)≠0`). This matches the
   proven-canonical compute and leaves all numbers unchanged.

2. **Jones/TL is canonical.** Then the Wenzl-Schur weights in
   `y_lambda_wenzl_bridge_numeric` (and the whole `closed_form_tau_M` /
   binding / per-knot pipeline) are mis-normalised and must be re-derived in
   the TL normalisation — a high-blast-radius change. The 2026-05-05 proof and
   ~250 ppb mass accuracy argue against this, but it is the author's call if
   the physical model intends the Jones trace.

Recommendation: **(1)** — treat the compute as canonical and scope the prop.

## 6. Reproduction

```bash
cd folio-assistant/computations
# live canonical H_3 weights at q_0 (Wenzl-Schur):
python3 - <<'PY'
import json
d=json.load(open("y-lambda-at-q0.witness.json"))
def w(o):
    if isinstance(o,dict):
        if o.get("partition") and "y_at_q0_50dps" in o and sum(o["partition"])==3:
            print(o["partition"], o["y_at_q0_50dps"])
        [w(v) for v in o.values()]
    elif isinstance(o,list):
        [w(v) for v in o]
w(d)
PY
# → [3] 0.4153957…  [2,1] 0.2809296…  [1,1,1] 0.0227449…   (y_(1^3) ≠ 0)
```

Compare to the prop's `[4]_q/[2]_q³ = 0.50531`, `1/[2]_q² = 0.24731`, `0` at
`q₀ = 1.1097`.

## Files referenced

- `content/quantum-observable-universe/mass-theory/h3-markov-wenzl-weights.md` (the prop, on `main` via `c2df3870`)
- `folio-assistant/computations/y_lambda_wenzl_bridge.py` (`y_lambda_wenzl_bridge_numeric`)
- `folio-assistant/computations/y-lambda-at-q0.witness.json` (live cache)
- `folio-assistant/computations/closed_form_tau_M.py` (`compute_tau_M_nucleon_H3`, the consumer)
- `docs/audits/2026-05-05-y-lambda-tr-m-equivalence-proof.md` (Ocneanu canonical proof)
