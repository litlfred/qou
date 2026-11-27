# The input ceiling: `mpf(Q_50_DIGIT_STR)`, and why it cannot be swept

Owner-selected 2026-11-20 (option 3 of four). Bean `qou-oiz3`.
**The classification is why the sweep could not be blind. The sweep then ran,
over the 588 non-deliberate consumers, with the 207 deliberate ones left alone.**

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
| files whose raw text contains `mpf(Q_50_DIGIT_STR)` | 810 |
| -- of those, **prose only** (mention it, never call it) | 6 |
| **real call sites** | **804** |
| -- **DELIBERATE 50-digit pin, must not change** | **207** |
| -- FIXABLE | 589 |
| -- unpatchable (no import to extend) | 8 |

(809/803/206 before the alias-prefix fix in S4a; the pattern had been matching
the `mpf(...)` suffix of `mp.mpf(...)`, which found the file either way but
under-counted by one.)

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

## 4. The mover rate is 50 %, and TWO earlier figures of mine were wrong

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

**Settled with a working patcher: 20 of 20 candidates completed both arms,
10 MOVED / 10 IDENTICAL -- a 50 % mover rate.** Applied to the 322 fine
witnesses behind fixable producers, that is ~160 expected to move.

So two figures of mine were wrong in sequence: 6/6 (environment contamination)
and then n = 2 (a broken patcher, below). The measured rate is 50 %.

## 4a. The patcher: two bugs, and the reason I gave for the first was invented

**Bug 1 -- the `$` anchor.** A `^...$`-anchored regex with `[^\n#]*` before the
anchor missed **535 of 589** import lines (91 %), every one of them ending in
`# noqa: E402`, which the character class cannot cross. I attributed this in
writing to *parenthesised multi-line imports*. Measured afterwards: **588 of
589 imports are SINGLE-line**. The reason was invented rather than observed,
and the real one is a trailing comment.

**Bug 2 -- the module alias, which actively corrupted files.** The call prefix
must be CONSUMED. A pattern allowing only `mpmath.` or bare matches the
`mpf(...)` *suffix* of `mp.mpf(...)`, so substituting yields `mp.Q_MP` -- an
`AttributeError: module 'mpmath' has no attribute 'Q_MP'` at import time.
Measured distribution of the 871 sites:

| prefix | count |
|---|---:|
| `mp.` | 661 |
| bare | 197 |
| `mpmath.` | 10 |
| `_mp.` | 3 |

so the bug corrupted **76 %** of sites. It surfaced as 14 of 20 A/B candidates
failing their PATCHED arm while their CONTROL arm passed -- which is exactly
what a control arm is for, and is why that design is worth the extra run.

The patcher is now AST-based: it locates the `ImportFrom` node that brings in
`Q_50_DIGIT_STR` and inserts `, Q_MP` after the alias token, preserving the
trailing comment; and it finds call sites in `code_only()` output and applies
those spans to the raw text, which `_source_normalise` preserves offsets for.
**588 of 589 patch cleanly, AST-valid before and after.**

## 4b. The three gates on the sweep

Any failure reverts the batch:

1. every patched file parses (`ast.parse`);
2. no patched file carries the mangling signature `<alias>.Q_MP` in code;
3. no patched file retains a residual `mpf(Q_50_DIGIT_STR)` call in code.

All three green on 588/588. Checked through `code_only()`, so a docstring
mentioning the call is not read as one. The 64 other `.Q_MP` occurrences in
`computations/` are legitimate module accesses -- `q_parameter.Q_MP` 48,
`C.Q_MP` 9, `qp.Q_MP` 4, `QP.Q_MP` 2, `constants.Q_MP` 1 -- and none is in the
batch.

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
