# The input ceiling: `mpf(Q_50_DIGIT_STR)`, and why it cannot be swept

Owner-selected 2026-11-20 (option 3 of four). Bean `qou-oiz3`.
**The sweep was NOT run. The classification was, and it is the reason.**

## 1. The defect is real and the fix direction is proved

`Q_50_DIGIT_STR` carries 50 significant digits while `OUTPUT_DPS` is 60, so a
producer that builds `q` from the STRING serializes ten digits nothing supplies.
Measured at `mp.dps = 120` against an independent `q_at(110)` solve:

| `q` source | relative distance from the solve |
|---|---|
| `mpf(Q_50_DIGIT_STR)` | **1.91571e-50** |
| `Q_MP` | **6.97057e-72** |

So substituting `Q_MP` is **strictly more correct by a factor 2.75e21**, which
puts the change inside AGENTS.md ASK-OWNER exemption 1. `Q_MP =
q_at(_DPS_DEFAULT)` with `_DPS_DEFAULT = 70` since `14a9e822427`.

`Q_50_DIGIT_STR` itself must **not** change -- its name is its specification and
1216 files import it. The fix belongs at the consumer.

## 2. 206 of the 803 call sites want 50 digits DELIBERATELY

This is the finding, and it is why a `sed` over the pattern is wrong.
[`computations/audits/q50_digit_cap_classify.py`](../../computations/audits/q50_digit_cap_classify.py):

| | count |
|---|---:|
| files whose raw text contains `mpf(Q_50_DIGIT_STR)` | 809 |
| -- of those, **prose only** (mention it, never call it) | 6 |
| **real call sites** | **803** |
| -- **DELIBERATE 50-digit pin, must not change** | **206** |
| -- FIXABLE | 589 |
| -- unpatchable (no import to extend) | 8 |

The deliberate signal is never in the call, which is identical either way. It is
in the file's name, in the name of the artifact it emits, or in a pin comment on
the line:

| why deliberate | count |
|---|---:|
| emits an artifact whose own name says `50dps` | 159 |
| ...and a pin comment on the line | 23 |
| ...and the filename says 50 | 13 |
| pin comment on the line only | 11 |

**159 of them emit something named `50dps`.** Re-pinning their `q` to 70 digits
would make that name a lie while the run still exits 0 -- a silent corruption of
exactly the kind the anti-laundering discipline exists to prevent. Of the 589
fixable, 322 back a witness fine enough for the change to show.

## 3. Two false-positive classes removed, and the corpus already had the fix

**Prose.** A first classifier matched raw text and convicted its own sibling
audit scripts, whose *docstrings* contain the literal `mpf(Q_50_DIGIT_STR)`.
`computations/audits/_source_normalise.code_only()` -- which this corpus ships
for precisely this, and whose header notes that a bare-token pattern needs it
while an anchored assignment-shaped one does not -- blanks comments and
docstrings in place, preserving line and column. 809 -> 803.

**Exposure to the module rather than to the fix.** An earlier exposure sweep
over-matched **6x** (1519 candidates) because a one-hop import rule flagged
every producer importing `q_parameter`, which *defines* `q_int`. Direct calls
only. Recorded in `2026-11-20-exposed-witness-identification.md`.

## 4. The mover rate is NOT established, and the first figure was contaminated

A first A/B reported **6 of 6 MOVED** and that figure is **withdrawn**. It
compared a patched run against the **committed** witness, so it attributed
environment churn to the patch: installing `pyhecke_native` in this container
strengthens the recorded `environment` block, and the producer says so on
stdout (*"recording a STRONGER environment block than the copy on disk;
rewriting provenance only (payload unchanged)"*). The tell is that one of the
six, `chi_at_q0_via_matrix_m_mpfr.py`, is **prose-only** -- it never calls the
pattern -- so it could not have moved because of the substitution at all.

Re-run with a **control arm in the same environment** (unpatched run -> A,
patched run -> B, compare A vs B), the sample that completed both arms is
**1 MOVED, 1 IDENTICAL**. Seven of ten were unpatchable by that harness's
`$`-anchored import regex, which fails on a parenthesised multi-line import --
a limitation of the patcher, not a fact about the corpus.

So: **n = 2.** No rate is claimed. Establishing one needs a patcher that handles
multi-line imports and a sample large enough to mean something, both of which
are tractable and neither of which is done.

## 5. Environment findings, recorded because they gate everything above

A bare container cannot run these producers at all, and three separate things
had to be installed before any A/B was possible:

- `sympy`, `numpy`, `scipy` -- absent; the first sample's five "IDENTICAL"
  verdicts were producers exiting rc=1 in 0 s on `ModuleNotFoundError`, which a
  verdict comparing JSON without requiring a successful run reported as
  agreement. A verdict must be unreachable when the run failed.
- `mpmath >= 1.4` -- the container had 1.3.0 under `python3`; the corpus uses an
  API it lacks (`AttributeError: module 'mpmath' has no attribute ...`).
- `pyhecke_native` -- not on PyPI, as AGENTS.md records; `maturin build
  --release` in `tools/pyhecke-native/` works and yields a cp311 wheel. **171
  of the capped producers reference it.**

## 6. What should happen next

1. Fix the patcher to handle parenthesised multi-line imports, then A/B a real
   sample of the 322 fixable-and-fine witnesses with the control arm.
2. Sweep the fixable set **excluding the 206**, in reviewable batches, each with
   its witnesses refreshed in the same commit.
3. The 206 keep their pin. If any of them is in fact an accident rather than a
   decision, that is a per-file judgement and not a sweep.
