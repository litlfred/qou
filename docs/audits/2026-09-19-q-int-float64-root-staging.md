# The float64 `q_int` root fix — staged plan and measured blast radius

**Bean** `qou-oiz3` (in-progress). **Branch** `claude/qint-float64-root-fix-2026-09-19`.
**Measured** 2026-09-19 against `origin/main` `665c91e403a`. Every figure below is
reproduced by [`computations/audits/q_int_float64_cone_audit.py`](../../computations/audits/q_int_float64_cone_audit.py);
none of them is maintained by hand.

---

## 1. The defect, and the file previously named for it

PR #7245's report named "four functions in `tools/pyhecke/python/pyhecke/wedderburn.py`".
**`q_int` is not there.** It is at

```python
# tools/qou-substrate/python/qou_substrate/constants.py:190
def q_int(n):
    """Quantum integer [n]_q = (q^n - q^{-n}) / (q - q^{-1})."""
    return (Q**n - Q_INV**n) / HA
```

`Q`, `Q_INV` and `HA` are the module's **binary64** globals (`Q` at `:150` is a
`_solve_q_proton_f64` Newton solve; `Q_INV` `:177`, `HA` `:178`). Verified at that
location this session.

**There is a SECOND float64 definition, and it is the one a sweep would miss.**
`computations/substrate/q_parameter.py:169` *redefines* `q_int` inside the
`ideal`/`muon` anchor branch, closing over the muon `Q` as a default argument:

```python
def q_int(n, _Q=Q, _QI=Q_INV, _HA=HA):
    return (_Q**n - _QI**n) / _HA
```

So the fix has **two** definition sites, not one, and the second is invisible to a
grep of `qou_substrate`.

### What is already correct, and must not be re-fixed

`q_int_at` (`:432`) and `q_int_classical_at` (`:455`) are already exact mpmath, and
their no-mpmath fallbacks (`:511`, `:514`) already **raise** rather than degrading to
f64 (owner directive 2026-09-07 — AGENTS.md's own worked example of exemption 1).
`q_int_err` (`:203`) is an uncertainty-propagation helper; binary64 there is
harmless and is deliberately out of scope.

### The mechanism, restated

`pyhecke.wedderburn` imports the float64 `q_int` (`:38`, falling back to
`qou_substrate.constants` at `:42`) and calls it at exactly two sites — `:65` inside
`q_hook_product` and `:73` inside `q_factorial` — both accumulating into an
`mp.mpf("1.0")`. `wedderburn_weight` is `q_dimension(λ)**2 / q_factorial(n)` on top
of them. The results are therefore **mpf-typed and float64-valued**: they print 40
digits and carry ~16. `isinstance(x, mpf)` is not evidence of precision.

---

## 2. Measured blast radius — and both recorded figures were wrong, in opposite directions

`qou-oiz3` records **"124 python files, 243 witnesses"**. Re-measured:

| question | command | measured 2026-09-19 | recorded | verdict |
|---|---|---|---|---|
| files **mentioning** `q_hook_product` / `q_factorial` / `wedderburn_weight` (word-boundary) | `q_int_float64_cone_audit.py` | **105** | 124 | recorded **HIGH by 18 %** |
| **value cone** — importers of the q_int-derived Hecke/Wedderburn layer | same | **1290** | 124 | recorded **LOW by 12.3×** |
| committed witnesses with a producer in the value cone | same | **917** | 243 | recorded **LOW by 3.8×** |
| …of those, carrying ≥30 significant digits | same | **673** | — | the real refresh budget |
| shim cone (importers of `q_parameter` / `qou_substrate.constants`) | same | 3921 | — | **not a measure of this defect** |

Both readings are correct for their own question, which is why they must be quoted
with the question attached — the same failure class AGENTS.md records for its own
importer table (wrong by two orders of magnitude) and for the `9.5σ` / `9.70σ` pair.

**One measurement trap, recorded because it inverts the answer.** Resolving a dotted
import by its **last component** puts `from qou_substrate.constants import Q` and
`from pyhecke.constants import …` in the same bucket, and `pyhecke/constants.py` is a
root. That single conflation reports the cone as **3921 files — the entire corpus —
instead of 1290.** The audit matches the full path suffix instead. A second trap:
the audit imports the Hecke layer to measure the error, so it appears in its **own**
cone and inflated every count by one until it was made to exclude itself.

---

## 3. The error is NOT bounded by float64 eps — it grows with the tower

Measured this session at `COMPUTE_DPS + 10 = 80` dps, proton pin, by swapping only
`q_int` in `pyhecke.wedderburn` and recomputing `wedderburn_weight` over every
partition:

| n | blocks | worst λ | relative move | × float64 eps |
|---:|---:|---|---|---:|
| 3 | 3 | (3) | 3.0495805e-16 | 1.4 |
| 4 | 5 | (2,2) | 8.804973e-16 | 4.0 |
| 5 | 7 | (3,1,1) | 6.9548236e-16 | 3.1 |
| 6 | 11 | (4,1,1) | 8.7499765e-16 | 3.9 |
| 9 | 30 | (3,3,1,1,1) | 1.6189461e-15 | 7.3 |
| **12** | **77** | **(4,4,2,2)** | **2.4104405e-15** | **10.9** |

The growth is structural: `q_factorial(n)` multiplies **n** float64-valued factors,
so the error accumulates with the strand count rather than sitting at the floor.
`n = 12` is the A = 4 atom (3 strands per nucleon), which under convention D is 7
nonzero blocks and builds in 0.04 s — it is not an exotic corner.

**The paper-level consequence.** The framework's L1 target is *internal cross-method
agreement ≤ 1 ppQ = 1e-15 at substrate q₀*. At n = 12 the f64-fed Wedderburn weights
differ from the exact ones by **2.41e-15 — 2.4× that target.** So L1 is not met in
the Wedderburn-weight layer, and the miss is invisible because the quantities are
`mpf` and print 40 digits.

This also **corrects a per-block figure** in `qou-oiz3`. That bean records the
residual at λ = (2,2) as `1.0212424e-15`; the pure-weight move measured here is
**8.804973e-16**. The two differ because the bean measured the residual with its own
branch's `μ_λ` excision applied. Do not reconcile them into one number.

**Secondary finding, confirmed.** `Q_MP = q_at(_DPS_DEFAULT)` with
`_DPS_DEFAULT = 50` (`constants.py:247`, `:331`), so the whole `_MP` family carries
**50 digits** while `COMPUTE_DPS = 70` and `OUTPUT_DPS = 60`. Measured
`|Q_MP − q_at(90)| = 1.1000161e-51` this session (the bean records `9.9102461e-52` —
same order, measured at a different working precision). A producer that calls
`set_compute_dps()` and then `fmt`s a `Q_MP`-derived value at 60 digits publishes
~10 **manufactured** digits. This is the `fmt()` padding class, and its consumer
base is the shim cone (3921 files), i.e. much wider than `q_int`'s. **It is a
separate defect and is not fixed by this arc.**

---

## 4. The fix recipe — proven, not proposed

Routing the Wedderburn primitives through the exact `q_int_at` is **type-preserving**
(mpf in, mpf out) and therefore cannot break a consumer's types. The one thing that
must not be got wrong is the **anchor**: `q_int_at`'s default `q` is `q_at(dps)`,
which is *always proton*, so a naive swap would silently re-pin every `ideal_muon`
producer. The anchor-correct handle is `q_parameter.q_at`, which the muon branch
rebinds (`q_parameter.py:228`).

Verified this session under both anchors:

```
QOU_Q0_ANCHOR=''       q_parameter.Q = 1.1099785827513808   q_at(60) = 1.109978582751380807591669
                       [4]_q f64 = 4.109682411207942   exact = 4.1096824112079411617605687891   rel 1.4425e-16
QOU_Q0_ANCHOR='ideal'  q_parameter.Q = 1.109978595642739    q_at(60) = 1.109978595642739046681795
                       [4]_q f64 = 4.109682435806692   exact = 4.10968243580669280986579456072   rel 1.12725e-16
```

So the Stage-2 edit is, in `tools/pyhecke/python/pyhecke/wedderburn.py`:

```python
try:
    from q_parameter import q_at as _q_at          # anchor-aware (muon branch rebinds it)
except ImportError:
    from qou_substrate.constants import q_at as _q_at
from qou_substrate.constants import q_int_at

def _q_int(n):                     # ambient-dps, anchor-correct, exact
    d = mp.mp.dps
    return q_int_at(n, q=_q_at(d + 10), dps=d)
```

and the same at `q_parameter.py:169` for the muon branch.

---

## 5. Why this is staged, and what the stages are

### The constraint that decides it

A change to `wedderburn.py` is an **import-cone** change: the producers' own source
bytes do not move, so `witness.scriptHash` does not drift and **not one of the 917
witnesses is flagged stale by any gate in the tree.** That is
`cosmetic_import_cone_drift` — the only bucket that has *grown* across five
measurements of `witness_staleness_triage.py` (4 → 9), and the bucket whose own
label records "measured 2/2 moved". Landing the code without the refresh would
leave **673 witnesses publishing digits that are wrong, with every detector green.**

Constraint: *land a stage whole or not at all* (PR #5049 merged the witnesses and
held the manifest; the half that landed is the half that broke `main`).

### Partition of the 917

| class | count | evidence |
|---|---|---|
| **(a) cheap re-runs** | ≤ 906 | 21 witnesses record a wall time < 300 s; **888 record no time at all**, so this class is an upper bound, not a measurement |
| **(b) long-compute** | ≥ 3 measured + the known heavy ones | `phi-per-nucleon-orbit-exhaustion` 2558.5 s, `he4-binding-k-stage2` 2086.2 s, `chi-lambda-he4-full-partition-table` 317.1 s, all from their own witnesses. Plus, from BASELINE rather than from a witness: `hecke_core_legacy.binding_energy(1,1)` = **1233.9 s** for ²H, the *smallest* bound atom (`hecke_core_legacy` is in the cone), and `hadron_knot_table` (also in the cone, also `ideal_muon`) ran **> 50 min** on one bound atom and exited 124 |
| **(c) refuse by design** | **3** | `atomic_tr_m_mpfr_50dps`, `he4_stage2_ranking_seminormal_xcheck`, `cross_check_trM_1ppb` — all three of the producers AGENTS.md names are **in the cone** |
| **(d) anchor-defining** | **0** | `q_pinning_50_digit` is **NOT** in the cone. Measured, and it is the single most de-risking fact here: the 2026-08-19 `Q0_FLIP` 262-witness breakage cannot be re-run by this arc |

**The muon layer is heavily represented**: **8 of the 19 `ideal_muon` producers are
in the cone**, and 3 of those 8 are the refuse-by-design set and a 4th is
`hadron_knot_table`. Against 350 of 914 `physical_proton`.

**The wall-cost partition is not measurable from the witnesses.** 888 of 917 record
no timing field. Any stage budget below is therefore a *plan*, not a forecast, and
each stage must re-time its own producers before committing to the next.

### The stages

| stage | scope | witness budget | gate to enter the next stage |
|---|---|---|---|
| **1 — STAGING (this PR)** | the audit script, this doc, the bean. **No source change.** | **0** | `precision-gates.sh --changed` clean of new reds; the audit reproduces every figure here |
| **2 — the two definition sites + `wedderburn.py`, with the ≥30-digit `physical_proton` producers refreshed** | the code fix; refresh the proton subset of the 673 | ~250–300, re-timed first | every refreshed witness re-runs green; the muon subset untouched and *declared* untouched |
| **3 — the `ideal_muon` subset** | 8 producers, of which 3 refuse by design and 1 is >50 min | 8 | each of the 3 refusals resolved individually (their guards are correct; they need a per-producer decision, not a sweep) |
| **4 — the long-compute tail** | `binding_energy`-backed, `hadron_knot_table`, `he4-binding-k-stage2`, `phi-per-nucleon-orbit-exhaustion` | ~10 | wall-clock measured per producer before it is started |
| **5 — the 151 mid-depth + 93 shallow** | witnesses that may or may not move | 244 | run last; many will be byte-identical |

**Stages 2–5 are scoped and NOT started.** Stage 2 alone is ~250–300 producer runs
of largely unknown wall cost, against an idle-pass budget AGENTS.md caps at **3
witnesses**. It is not one tranche, and this document exists so that the next agent
sizes it from a script rather than from a sentence.

### What would make stage 2 landable

The single highest-value follow-up is **empirical**: sample ~20 in-cone producers,
run each twice (main code vs patched), and measure how many witnesses actually move
rather than how many *could*. If the actual mover rate is low — and the memory
BASELINE for the `substantive` verdict says such over-flagging runs ~41 % — stage 2
shrinks accordingly. That sample was **not** run here, deliberately: this checkout
is shared with a live sibling session and producers write sibling witnesses, so a
half-finished producer sweep on it is exactly the failure this staging exists to
avoid.

---

## 6. Do not

- **Do not `--rebaseline`** or add anything to `raw-float64-baseline.json`. Baselines
  drain, never grow. This defect is invisible to that ratchet anyway — the values are
  `mpf` and serialise as strings.
- **Do not swap `q_int` → `q_int_at` without routing through `q_parameter.q_at`.**
  That silently re-pins 8 `ideal_muon` producers to proton.
- **Do not `git checkout -- computations/`** to clean up after a gate run; it is what
  the gate prints and it discards every uncommitted source edit in the tree.
- **Do not treat the 917 as stale-flagged.** No gate in the tree sees this.
