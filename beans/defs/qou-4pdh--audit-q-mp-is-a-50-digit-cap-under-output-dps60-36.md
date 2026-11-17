---
# qou-4pdh
title: 'AUDIT: Q_MP is a 50-digit cap under OUTPUT_DPS=60 — 366 files publish ~10 digits the source does not carry'
status: in-progress
type: task
priority: normal
created_at: 2026-10-10T08:36:49Z
updated_at: 2026-11-17T08:04:32Z
parent: qou-9nnz
---


Surfaced by the `pr7318-merge` sub-agent while resolving six identical merge
conflicts on PR #7318, where both sides had independently fixed the same
float64 defect and chosen different replacements. **Re-measured independently
here before being recorded** — the figures below are mine, taken at the current
`main`, not carried from the agent's report, and they agree with it to every
digit it published.

## The decision, up front

`Q_MP` — the cached `mpmath.mpf` substrate modulus that **366 Python files**
import from `computations/substrate/q_parameter.py` — is constructed at 50
decimal digits, while the corpus serializes witness values at
`OUTPUT_DPS = 60`. So any quantity derived from `Q_MP` and written to a witness
carries roughly **ten published digits that contain no information from the
source string**. The question for the owner is whether to change that, and at
what scope.

**Nothing is changed by this bean.** It is a measurement and a framing.

## The measurement

`q_parameter.py:203-204`:

```python
_mp.mp.dps = max(_mp.mp.dps, 50)
Q_MP       = _mp.mpf(_d["q"])
```

`_d["q"]` is the 50-significant-digit string from
`q-pinning-50-digit.witness.json`. Both `Q_MP` and `mpf(Q_50_DIGIT_STR)` read
**that same string**; they differ only in the ambient `mp.dps` at the moment
the `mpf` is constructed. `set_compute_dps()` raises the ambient to
`COMPUTE_DPS = 70`, so an `mpf` built *after* that call gets more bits than the
one cached at import.

Measured in `Fraction` against the exact decimal — **never in mpmath**, because
measuring the loss at the precision you are measuring reads `0.0` by
construction:

| | mantissa bits | relative error vs the exact 50-digit decimal | inside the `1e-60` serialization width? |
|---|---:|---|---|
| `Q_MP` (cached at import) | **167** | `2.0148085403388985e-50` | **no** |
| `mpf(Q_50_DIGIT_STR)` (built at 70 dps) | **236** | `4.594107363943758e-72` | yes |

Ratio `2.01e-50 / 4.59e-72 ≈ **4.39e21**`. Live constants confirmed in the same
run: `COMPUTE_DPS = 70`, `OUTPUT_DPS = 60`.

Blast radius: `grep -rln '\bQ_MP\b' --include=*.py`, excluding
`.claude/worktrees/` and `_deprecated/`, gives **366 files**.

## The construction comment is deliberate, and it is ALSO stale — these are two different facts

`q_parameter.py:196-202` does not do this by accident. It argues for it:

> *"50 dps — this is the intended compute floor, NOT a temporary bump, so it is
> set globally … 50 dps ≫ the 1e-10 observable reproduction tolerance and the
> 1e-15 (1 ppQ) L1 target, so it does not regress either precision leg; the
> q-pinning witness's 70-digit q is read in full and only the compute working
> precision is pinned at 50. Producers that need more raise it via
> `set_compute_dps()`."*

**The L1 half of that argument is correct and this bean does not dispute it.**
50 dps is thirty-five orders below the 1e-15 L1 target; no L1 claim is at risk.

**Two parts of it no longer hold.**

1. *"the q-pinning witness's 70-digit q is read in full"* — the **string** is
   read in full on the line above; the `mpf` on the next line does not retain
   it. 167 bits is 50.3 decimal digits. So the sentence is true of `_d["q"]`
   and false of `Q_MP`, one line apart.
2. *"50 dps is where compute should stay"* was written against a world where
   that was the ceiling. It is not: `COMPUTE_DPS = 70` and `OUTPUT_DPS = 60`
   today. AGENTS.md's own L1 row carried the superseded `65/50` figures until
   2026-09-06 (bean `qou-0z4i`), so this comment is of that vintage. A comment
   asserting the floor equals the ceiling, in the module that configures both,
   is the kind of stale label this corpus keeps recording.

**The defect is therefore NOT "50 dps is too low for compute". It is the
mismatch between a 50-digit input and a 60-digit output.** Digits 51–60 of any
`Q_MP`-derived serialized value are an artifact of binary expansion, not
information. That is a *laundering* concern — publishing precision that was
never there — which is a different and narrower claim than an L1 regression,
and it is the one that bites.

Independently visible in PR #7318's own witness diffs: every numeric move
against the pre-merge values lands at **1e-48 … 1e-50**, exactly where the cap
sits, and the merged `q_input` reads `…449912187360000000000` where the
`Q_MP` side read `…4499121873 57763605672` — a tail that is the 167-bit
binary's expansion rather than anything from the source.

## Options

### 1. Do nothing (the default)

- **What it means.** `Q_MP` keeps 167 bits. The 366 importers keep publishing
  ~10 non-informative digits in any value they serialize from it.
- **What it costs.** Nothing now.
- **What it risks.** The corpus keeps publishing digits it did not derive. Each
  future merge where two agents fix the same float64 site can resolve the wrong
  way, as nearly happened on #7318 — the branch that fixed a 2.7e-17 defect
  introduced a 2.0e-50 one and read as the better side.
- **What it commits to.** Nothing. Fully reversible.

### 2. Raise `Q_MP`'s construction precision only (one line)

- **What it means.** Build `Q_MP` at `COMPUTE_DPS` instead of `max(dps, 50)`,
  so the cached constant carries the whole source string. One line in
  `q_parameter.py`; no call site changes.
- **What it costs.** One line. Then **366 files' numbers can move at the
  1e-48…1e-50 level**, so every witness derived from `Q_MP` becomes
  `scriptHash`-fresh-but-numerically-different, and the witness-staleness
  machinery will not flag it (the producers did not change).
- **What it risks.** A corpus-wide numeric movement with no detector. Any
  recorded assertion with a tolerance tighter than ~1e-48 could flip; PR
  #7318's evidence says the real moves are 1e-48 and looser, and every
  assertion it checked is at a ~1 % threshold, so nothing flipped there — but
  that is 7 witnesses, not 366 files.
- **What it commits to.** Re-running the affected producers, which is the
  expensive part and is not bounded by this bean.

### 3. Deprecate `Q_MP` in favour of `mpf(Q_50_DIGIT_STR)` at the call site

- **What it means.** What PR #7318 chose for its six files: each producer
  constructs its own `mpf` after `set_compute_dps()`, so precision follows the
  ambient rather than the import order.
- **What it costs.** 366 files, mechanically. Same numeric movement as option 2
  and the same re-run obligation.
- **What it risks.** The same, plus 366 files of diff — which under
  AGENTS.md's own warning buries any real finding under mechanical churn.
- **What it commits to.** Removing a widely-used constant, so every future
  importer has to know the idiom.

### 4. Record the cap and gate it

- **What it means.** Leave `Q_MP` as it is, correct the stale sentences in its
  docstring, and add a gate that fails when a value derived from `Q_MP` is
  serialized at more than 50 digits. The cap stops being invisible without any
  number moving.
- **What it costs.** A docstring fix plus one audit script. No producer re-runs.
- **What it risks.** Little; a gate can be warn-only first (cf. the 2026-08-25
  precision hook, offered blocking and declined).
- **What it commits to.** Nothing numeric. It makes options 2/3 measurable
  later instead of guessed at.

## Recommendation (my judgement, not a finding)

**Option 4, then option 2 if the gate shows it matters.** The reason is
AGENTS.md's own posture on exactly this shape: a corpus-wide sweep off a
measurement nobody has gated is how a real finding gets buried, and the
blast-radius number here (366 files) is large enough that the sweep is the
expensive decision, not the one-line fix. Option 4 costs a docstring and a
script and converts "366 files might be affected" into "N serialized values
actually exceed the cap", which is the number the owner needs in order to pick
between 1, 2 and 3.

Note that **option 2 alone would qualify under AGENTS.md exemption 1** (it
strictly increases precision and makes a wrong number impossible), so an agent
could in principle take it without asking. I am not taking it, because the
exemption covers the *edit* and not the 366 producer re-runs it obliges, and
because the construction comment shows the 50 was chosen rather than
overlooked — which makes it an owner question rather than a slip.

## Blast radius in real terms

Not "366 importers" but: `computations/alpha/*` (the α_EM chain, five files),
`atomic_tr_m_helium4.py` (the `|tr_M|` trace feeding the mass channel),
`_li_2_q_util.py` (the `vol_density_*` family the mass formula calls),
`a_operator/*` (the A-operator extracts), and ~20 files under
`computations/audits/` — including `cached_accessor_shape_audit.py`, which is
itself the detector for the layer-straddle class. The α chain and the `|tr_M|`
trace are the two that reach reader-facing numbers.

## What is NOT claimed

- **No L1 regression.** 50 dps is thirty-five orders below the 1e-15 L1 target.
  The construction comment is right about that.
- **No published number is shown to be wrong.** The claim is that digits 51–60
  of `Q_MP`-derived serialized values carry no information — not that digits
  1–50 are incorrect. They are not.
- **No count of actually-affected witnesses.** 366 is the count of files naming
  `Q_MP`; how many serialize a derived value past 50 digits is unmeasured, and
  measuring it is option 4.

## Reproduce

```sh
grep -rln '\bQ_MP\b' --include=*.py . | grep -v worktrees | grep -v _deprecated | wc -l
python3 - <<'PY'
import sys; sys.path[:0]=['computations','computations/substrate']
from fractions import Fraction
import mpmath as mp
from q_parameter import Q_MP, Q_50_DIGIT_STR
import qou_substrate.precision as P
exact = Fraction(Q_50_DIGIT_STR)
def to_frac(x):
    s,m,e,_ = mp.mpf(x)._mpf_
    v = Fraction(m) * Fraction(2)**e
    return -v if s else v
mp.mp.dps = P.COMPUTE_DPS
for lbl, v in (("Q_MP", Q_MP), ("mpf(Q_50_DIGIT_STR)", mp.mpf(Q_50_DIGIT_STR))):
    print(lbl, mp.mpf(v)._mpf_[3], "bits  rel err",
          float(abs(to_frac(v) - exact) / exact))
print("COMPUTE_DPS", P.COMPUTE_DPS, " OUTPUT_DPS", P.OUTPUT_DPS)
PY
```

## Implementation & Witness Progress (PR #8269)
- Branch: `qou-10v9-07ts-324i-49vn-4pdh-5mxd` (`7a961cf268c0cf36c3f70fd39f92645c16c9a30a`), PR: `litlfred/qou#8269`
- Lean 4 module: `folio/quantum-observable-universe/lean/QOU/Eightfold/ChiRustNondeterminismOverrideBlindnessChiCacheStalenessQmpDigitCapAndMagnusFarCommutativity.lean` (0 sorry, 0 axioms, 0 vacuity findings)
- Probe & witness: `computations/probes/chi_rust_nondeterminism_override_blindness_chi_cache_staleness_qmp_digit_cap_and_magnus_far_commutativity_probe.py` -> `computations/probes/chi-rust-nondeterminism-override-blindness-chi-cache-staleness-qmp-digit-cap-and-magnus-far-commutativity.witness.json` (`allPassed: true`, `scriptCommitSha: e7b85e53d7a8855337daf870617a2e9a6b0acc11`)
