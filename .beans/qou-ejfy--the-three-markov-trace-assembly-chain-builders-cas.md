---
# qou-ejfy
title: The three Markov-trace assembly chain builders cast a 60-digit mpf to float64
status: in-progress
type: bug
priority: normal
created_at: 2026-09-19T06:00:38Z
updated_at: 2026-09-19T07:12:20Z
---

## Measured on `origin/main` @ `665c91e403` (2026-09-19)

`python3 computations/witness_raw_float64_audit.py` — **REGRESSED 0, NEW 1**.
The three fixes merged in PR #7161 all hold 53 commits later. The one NEW:

    1  computations/audits/braid-encoding-audit.witness.json

Seven float fields in that witness; six are integral (`1.0`/`0.0` in
`word_cd`) and are the 2026-08-24 integral-float reclassification, not a
precision finding. The seventh is real:

    /data/tr_M_cross_check/proton/markov_trace_assembly_chain = 0.629328402202922

## The audit only ECHOES it — the defect is two producers upstream

`braid_encoding_audit.py:417` reads `target_value` out of
`computations/markov-trace-assembly-proton.derivation.json`, which stores it
as a raw JSON float. That file is written by
`computations/build_markov_trace_assembly_proton_chain.py`, whose line 82 is

    PROTON_TR_M_Q0 = float(tr_m_nucleon("proton"))

`tr_m_nucleon` returns an **mpf carrying 60 digits**. Measured, all three:

| nucleon | mpf (60 dps) | stored float64 | digits discarded |
|---|---|---|---|
| proton   | `0.629328402202921918165345746778485927600219400634359762811677` | `0.629328402202922` | 44 |
| neutron  | `0.475133517155682212506090232675005799558407634708751231268857` | `0.4751335171556822` | 44 |
| deuteron | `0.151968339204231607592665697751066141271240964655261151310301` | `0.1519683392042316` | 44 |

**All three sibling builders carry the identical cast** —
`build_markov_trace_assembly_{proton,neutron,deuteron}_chain.py` at lines
82 / 51 / 66 respectively, each feeding `target_value=` and the leaf step's
`output_value=`. One defect class, three files.

## This is a REGRESSION of a drain that had already landed

Bean `qou-btqh` (completed, merged PR #6569, 2026-09-04) drained exactly this
field, 6 -> 0, and removed the baseline entry — stricter than 0. The three
builders were then **written fresh on 2026-09-13** under bean `qou-nhkv` (the
proton derivation was an orphan whose only builder was deprecated), and they
reintroduced the cast. Because `qou-btqh` had removed the baseline row, the
reappearance registers as **NEW**, not REGRESSED — worth knowing when reading
the ratchet: a drained-then-regressed file does not announce itself as a
regression.

`braid_encoding_audit.py:591-595` still carries `qou-btqh`'s comment saying
"Upstream tr_M values now arrive as full-precision STRINGS (the producers were
drained to carry mpmath.mpf end to end)". For the proton assembly chain that
sentence is now false.

## The three consumers are all string-safe, and two GAIN precision

- `applied_uniqueness_mass_table.py:241` — `mp.mpf(str(d.get("target_value")))`.
  Gains 44 digits.
- `markov/assembly_chain_11_letter_recompute_probe.py:121` — `str(...)`, and its
  tolerance is **derived from the stored precision** (`_sig` digits -> `1e-(sig-1)`).
  Its own comment at line 173 complains that the chain "stores `target_value` as
  a 16-significant-digit float". Full precision tightens that check from ~1e-15
  to ~1e-59.
- `audits/braid_encoding_audit.py:417` — passes through `_to_mpf(str(x))`.

`derivation_chain.py:756` types `target_value: Any` and serializes it verbatim,
so a string needs no schema change.

## Independent corroboration that the mpf is the right value

`build_markov_trace_assembly_proton_chain.py:240` records that
`assembly_chain_11_letter_recompute_probe` independently obtains
`0.62932840220292191817` on the same canonical element by a route sharing no
code path. That matches the mpf digit for digit and does **not** match the
stored float, which stops at `...402202922`.

## Authorisation

Removing a `float()` from a compute path is exemption (1) — increases precision —
under the 2026-09-07 ASK-THE-OWNER directive. No baseline is touched.


## FIXED — three producers, two lines each, no baseline touched

`build_markov_trace_assembly_{proton,neutron,deuteron}_chain.py`: drop the
`float()`, keep the mpf for arithmetic, serialize once with `_precision.fmt`
into a `*_TR_M_Q0_STR`, and use that for `target_value=` / `output_value=`.
`float()` survives only inside f-strings, which is display. `structural_check`
never reads either field numerically (`derivation_chain.py:756` types
`target_value: Any`), and nothing outside these three modules imports the
constants, so the blast radius is the three derivation JSONs.

Diff is **exactly two lines per derivation file**, both float -> full-precision
string. Nothing else moved.

## The three consumers, measured before and after

### 1. `markov/assembly_chain_11_letter_recompute_probe.py`

Side by side, same command, only the derivations differing:

| check | on `main` | with the fix |
|---|---|---|
| `p_matches_live_producer_at_proton` | PASS, rel **1.30035e-16**, tol 1e-14 (15 digits stored) | PASS, rel **0**, tol **1e-59** (60 digits stored) |
| `n_matches_live_producer_at_proton` | PASS, rel **2.63212e-17**, tol 1e-15 (16 digits stored) | PASS, rel **0**, tol **1e-59** |
| `p_matches_live_producer_at_muon2022` | FAIL, rel 0.450733 | FAIL, rel 0.450733 — identical |
| `n_matches_live_producer_at_muon2022` | FAIL, rel 0.518971 | FAIL, rel 0.518971 — identical |

Exit 1 both before and after; the two muon failures are pre-existing and
untouched (those `LIVE` entries are hardcoded pre-ruling copies — no
muon-pinned assembly witness exists to read, as the probe's own comment says).

**The residual WAS the cast.** 1.3e-16 and 2.6e-17 are the binary64 floor, not
a disagreement: with the mpf carried through, the recompute and the stored value
agree to every digit the probe evaluates and `rel` is identically 0. The bar it
clears tightened by ~44 orders at the same time.

**I expected this to break and it did not — record why.** The probe derives its
tolerance from the STORED precision alone (`_sig` digits -> `1e-(sig-1)`), which
assumes the recompute always carries more. It evaluates at `sp.N(..., 30)`, so a
60-digit stored value sets a 1e-59 bar the 30-digit recompute could not clear on
a nonzero residual. It passes only because the residual is *exactly* zero — both
sides round to the same 30 digits. So the tolerance rule has a latent hole (it
should cap at `min(stored, recompute)`), and this change did not expose it.
Left alone deliberately: touching it would be a tolerance edit, which is not a
precision fix and not corpus-derived.

### 2. `applied_uniqueness_mass_table.py` — exit 0, 3 assertions all passed

Two findings in its witness diff, both of them the point:

- `rel_vs_reference` for all three nucleons goes `1.300e-16 / 2.632e-17 /
  4.996e-17` -> **`"0.0"`**. The corpus was recording a fabricated disagreement
  between the assembly chain and the canonical reference that was purely the
  cast.
- `"tr_M_q0": "0.629328402202922000000000000000000000000000000000000000000000"`
  — a 16-digit float padded to 60 with **44 fabricated zeros**. This is the
  float64-padding defect named in the AGENTS.md TRAP list ("false precision,
  reached from the other direction"), and it is now a real 60-digit value.

### 3. `audits/braid_encoding_audit.py` — exit 0

`markov_trace_assembly_chain` now carries 60 digits. Assertion (2) still FAILS
by design (bean `qou-soj6`, the ~0.666 two-route tr_M gap); its `computed` moves
only in the 17th digit (`...94810326` -> `...94853755`), i.e. the gap is
unchanged and is now computed at full precision on both sides. Its six remaining
float64 fields are the integral `word_cd` `1.0`/`0.0` entries, which the
ratchet reclassifies as integral-valued, not a precision finding.

## Ratchet

`witness_raw_float64_audit.py --strict`: **NEW 0, REGRESSED 0, exit 0** (was
NEW 1 on `main`). Drained files 34 -> 35. No baseline entry added, widened or
rebaselined.

## Environment note — the numbers are NOT environment-sensitive

The first run recorded a weaker provenance block than the committed witness
(`clarabel` dropped; mpmath 1.4.1 -> 1.3.0, because installing `sympy` pins
`mpmath<1.4` and silently downgraded it). Rather than commit the weaker record
I installed `clarabel==0.11.1`, forced `mpmath==1.4.1`, and re-ran all four
producers: **all three target values are byte-identical under mpmath 1.3.0 and
1.4.1**. So this is one case where the environment hazard was checked and found
not to apply.


## precision-gates.sh --changed: RED on ten gates, NONE of them mine

`scripts/precision-gates.sh --changed` exits 1 with

    RED: q0-anchor flip, q0-anchor refill ratchet, import-time dps ratchet,
         never-raises-dps ratchet, float64-padding ratchet, module-const
         precision, reference-literal ratchet, witness-value copy ratchet,
         q0-value drift ratchet, mixed mpf/f64 -> serializer

**Attributed file-by-file rather than assumed.** Each gate re-run on its own
and its output grepped for the eight files this change touches
(`markov-trace-assembly*`, `applied-uniqueness*`, `braid-encoding*`,
`build_markov_trace_assembly*`):

| gate | exit | cites my files |
|---|---|---|
| q0-anchor flip | 1 | **0** |
| q0-anchor refill ratchet | 1 | **0** |
| import-time dps ratchet | 1 | **0** |
| never-raises-dps ratchet | 1 | **0** |
| module-const precision | 1 | **0** |
| float64-padding ratchet | 1 | **0** |
| reference-literal ratchet | 1 | **0** |
| witness-value copy ratchet | 1 | **0** |
| q0-value drift ratchet | 1 | **0** |
| mixed mpf/f64 -> serializer | 1 | **0** |

Consistent with PR #7435's independent reading, "precision-gates red on main
alone".

### The gate-trade (`qou-3jwy`) was checked, not assumed

A float64 drain can push the float64-**padding** ratchet up. Measured both ways
by restoring `origin/main`'s version of the five data files and re-running:

    with the fix   : baseline 13, NEW 63
    on main        : baseline 13, NEW 63

Identical, and neither run cites any file I touched. **No gate-trade.**

Two things fall out of that measurement worth recording:

- The padded `"tr_M_q0": "0.6293284022029220000...0"` on main — 16 real digits
  and 44 zeros — is **not** detected by the padding audit. I removed it anyway
  (it is now a real 60-digit value), but the detector has a blind spot at that
  shape. Not chased here.
- I expected `witness_value_copy` to be the risk, since `target_value` now
  equals the canonical reference string exactly, which is what a value-copy
  detector looks for. It does not fire on any of these. Recorded because the
  guess was reasonable and wrong.

### Tree hygiene

Every gate run rewrites tree-measuring audit witnesses. `precision-gates.sh`
names them and says DO NOT COMMIT (bean `qou-v0t8`); all reverted, tree clean
at 0 dirty before each commit.


## The other two sites of `float(<canonical mpf accessor>)` — adjudicated, so nobody "fixes" them twice

Grep for the defect class (`float(tr_m_nucleon(...))` and friends) across
`computations/` returns four sites beyond the three fixed here. Two are
adjudicated below; recorded because both look like the same defect and only one
is.

### `audits/derivation_convention_frame_audit.py:156-158` — NOT a defect, leave it

    return {"p": float(tr_m_nucleon("proton")), ...}

`canon` is consumed only by `_findings`, which scans **text** for numeric
literals, parses each with `float(raw)`, and flags those disagreeing by more
than `REL_TOL`. Both sides are floats by construction — the object under test
*is* a source/doc literal, which is ≤17 digits anyway — and the comparison is a
loose relative-tolerance check. The floats never reach a witness: there is no
`add_data`/`add_assertion` carrying them, and the file has no baseline row.
Carrying mpf would change nothing. Under the 2026-09-07 ASK-THE-OWNER directive
this is "tidying an inconsistency", which is explicitly **not** exempt.

### `probe_bring_residue_resolvent.py:85` — a REAL one, and invisible to every witness detector

    vals = [float(canonical_resolvent(q, n)) for n in POLE_ORDERS]
    distinct_count = len(set(round(v, 20) for v in vals))

The stored field is an `int`, so no float enters the witness and the ratchet,
the padding audit and the `.assertions[].computed` sweep are all structurally
blind to it. `round(v, 20)` on a binary64 is a no-op past ~17 digits, so the
code implies a 1e-20 distinctness bar it cannot certify.

**Impact measured: none.** Minimum pairwise separation of the four values is
**0.0645**, fourteen orders above the binary64 floor, so `distinct_count` is 4
either way. A false precision claim, not a wrong number.

Recorded on bean `qou-p77d` (in-progress, already holds this file's drain
ledger) via `--body-append`; its status was NOT touched. Not fixed here: the
re-run would commit a weaker provenance block (`python 3.13.12 -> 3.11.15`,
numpy and scipy likewise — the Python version is not installable away), and it
is a different domain from this PR.


## A sibling claimed these 60 digits are ~16 real digits. Measured: they are ~50.

PR #7440 (`qou-oiz3`) commented on #7438 that this chain's upstream returns an
mpf that is **float64-VALUED**, so *"the 60-digit `mpf` carried ~16 real digits
to begin with"*. That is a claim about **this PR's numbers**, so it was verified
rather than accepted or dismissed.

### What holds

`qou_substrate.constants.q_int` **is** binary64 — read at the primary source,
`constants.py:189-191`: `Q_INV = 1.0/Q`, `HA = Q - Q_INV`,
`q_int(n) = (Q**n - Q_INV**n)/HA`, with `Q` a Python float.

And the names are in the cone. Transitive import closure of
`atomic_tr_m_mpfr_50dps.py` is **51 in-repo modules**, `qou_substrate` reached,
containing `q_int` in 8, `wedderburn_weight` in 2, `q_factorial` in 1,
`q_hook_product` in 2.

### What is refuted

`tr_m_nucleon` is a witness READ — `canonical_trm_reference:164` returns
`abs(mp.mpf(rows[atom]["tr_M_at_q0_50dps"]))` — so the question is the accuracy
of the recorded string. `markov_weights_symbolic.tr_M_canonical` builds the
canonical 11-letter element symbolically over ℚ(q) and evaluates only at an
exact-rational substitution, so `q_int` (which closes over a float module
constant) is not on that path however many cone modules mention it:

                eval@30 dps   eval@60 dps   eval@90 dps
    proton  rel =     0       1.4249977e-50  1.4249977e-50
    neutron rel =     0       5.7903247e-50  5.7903247e-50

**Stable from 60 to 90 dps**, so it is not arithmetic noise — it is where the
producer stopped. The field is named `tr_M_at_q0_50dps` and delivers exactly
that: **~50 accurate digits, digits ~51-60 serialization padding.**

Second, independent discriminator: `mpf(float(v)) != v` for all three nucleons
(7.60e-17 / 3.77e-17 / 2.69e-17), so the value is not a promoted double either.

### The reusable lesson, and it is the corpus's own, inverted

**A text match in a cone module is not proof the value flowed through it.**
13 of 51 modules carry those names; the path that computes this quantity is
symbolic and reaches none of them. The detector-blindness taxonomy has ~46 rows
of a detector MISSING a real instance; this is the same failure running the
other way — cone membership read as a data-flow fact, over-selecting.

Consequence for #7440, raised there: its 673-witness figure is derived from the
import cone and needs re-deriving by data flow. At least these three are not in
it. The cheap per-witness discriminators are the two above.

### Effect on this PR: none, except that its claims are stronger

The fix preserves ~50 accurate digits rather than ~16 — so "discarded 44
digits" understates nothing and overstates nothing. `rel_vs_reference -> 0.0`
remains a statement about two recordings of the same ~50-digit quantity.
