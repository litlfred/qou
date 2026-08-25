# The corpus is one CODATA edition behind, in 1969 places

**Date:** 2026-08-19 · **PR:** (this branch) · **Predecessor:** PR #5149
**Producer:** [`codata_corpus_literal_scan.py`](../../computations/codata_corpus_literal_scan.py)
**Witness:** [`codata-corpus-vintage-scan.witness.json`](../../computations/codata-corpus-vintage-scan.witness.json)

## What prompted it

The owner supplied the muon-electron mass ratio from NIST — `206.768 2827(46)`
— with the instruction *"should already be in corpus… ALL CODATA… check
first"*, together with the upload of `library/allascii.txt` (then `uploads/`), NIST's complete
2022 listing (commit `9409cb1`).

It was already in the corpus. **Twice, with two different values**, which is
the finding.

| value | edition | sites |
|---|---|---|
| `206.7682827` | CODATA-2022 ✓ | `codata_2022_source.py` |
| `206.7682830` | one edition earlier, labelled "CODATA 2022" | production registry + ~128 others |

`codata_2022_source.py` was corrected on 2026-08-09 (PR #4860, its own comment
calls it a *"vintage correction"*). The production registry
`qou_substrate.constants` — 309 in-repo importers — was not. The two registries
disagreed with each other for six days and nothing could notice, because until
`allascii.txt` landed **there was no authoritative table in the repository to
check against**. Every CODATA value was a literal checked, at best, against
another literal.

## Fixed in PR #5149

`qou_substrate.constants` now reads both mass ratios from the table
(`qou_substrate/data/allascii.txt`, vendored byte-identical, guarded by a
drift test). Two straddles were removed:

1. `MASS_RATIO_MU_E` — the value, 1.451 ppb (0.065 σ).
2. `MASS_RATIO_P_E_ERR` — the **uncertainty**: `1.1e-7` where 2022 says
   `3.2e-8`, 3.4× too wide. The *value* prints identically in both editions,
   so a value-only check passes while the error bar is a different vintage.
   The first audit pass missed exactly this; the audit now compares
   uncertainties too.

Measured consequences, reported rather than smoothed:

| | before | after |
|---|---|---|
| `Q` (proton pin) | `1.1099785827513808` | **unchanged** |
| `Q_ERR` | 3.2e-12 | 9.2e-13 |
| σ(q₀), proton anchor | 0.0029 ppb | 0.00083 ppb |
| muon anchor looser by | 429× (stated) | 1474× |
| μ–p tension | 11.534 ppb | **11.614 ppb — worse** |

`Q` not moving is the load-bearing fact: **no witness needs regeneration.**
And the tension getting *worse* independently reproduces the note already in
`codata_2022_source.py` (m_μ L2 miss 963.6× → 970.2×). Two routes agreeing is
a check on both.

## The wider sweep — "other issues like this?"

Yes. It is not a handful; it is close to the whole constant set.

The scan compares every corpus literal of ≥7 significant digits against all
293 table rows and reports those that are **near but not equal** — the exact
signature of a stale edition. Result: **275 distinct literals across 1962
sites.**

| literal | table (2022) | sites | offset | σ |
|---|---|---|---|---|
| `938.27208816` (m_p) | `938.27208943` | 349 | 1.354 ppb | **4.38 σ** |
| `939.56542052` (m_n) | `939.56542194` | 173 | 1.511 ppb | 2.96 σ |
| `0.51099895…` (m_e) | `0.51099895069` | 172+82+53 | 1.35 ppb | 4.31 σ |
| `137.035999084` (1/α) | `137.035999177` | 124 | 0.679 ppb | **4.43 σ** |
| `206.7682830` (m_μ/m_e) | `206.7682827` | 77+51 | 1.451 ppb | 0.065 σ |
| `1875.61294257` (m_d) | `1875.61294500` | 65 | 1.296 ppb | 4.19 σ |
| `2808.39160743` (m_h) | `2808.39161112` | 49 | 1.314 ppb | 4.19 σ |
| `2808.92113298` (m_t) | `2808.92113668` | 47 | 1.317 ppb | 4.20 σ |
| `931.49410242` (u) | `931.49410372` | 23 | 1.396 ppb | **4.48 σ** |
| `3727.3794066` (m_α) | `3727.3794118` | 19 | 1.395 ppb | 4.33 σ |

Two things make this a single phenomenon rather than ten accidents: the
offsets are all the **same sign** and the **same order** (1.3–1.5 ppb), and
each literal is *full length* — not truncated, just from an earlier
adjustment.

Two outliers do **not** fit that pattern and want separate eyes:

- `3727.379378` (m_α, 18 sites) — 9.068 ppb, **28.2 σ**. Two editions back,
  not one.
- `137.035944` (1/α, 18 sites) — 402.6 ppb, **2630 σ**. Not any CODATA
  adjustment; something else is going on at those sites.

## Why the existing audit could not catch this

[`codata_truncation_audit.py`](../../computations/codata_truncation_audit.py)
(2026-08-11) already covers hand-typed CODATA constants, and its framing is
right — its own docstring says *"the canonical table is READ, not typed"*, and
warns that a checker which hardcodes constants *"would go stale on the next
CODATA revision in exactly the way it is meant to detect."*

But the table it reads is `codata_constants`, an **in-repo module**. So it
detects a literal that is a short *prefix* of the registry value, and is
structurally blind to a literal that is full-length and from a different
edition. `938.27208816` has all eleven significant digits; nothing about it
looks truncated; it is 4.38 σ wrong.

The two audits are complementary and both are wanted:

| | compares against | catches |
|---|---|---|
| `codata_truncation_audit` | `codata_constants` (in-repo) | truncation |
| `codata_corpus_literal_scan` | `library/allascii.txt` (NIST) | wrong edition |

The general lesson is the one this session kept meeting: **a correction lands
at one site and never reaches the consumers that restate it.** The defence is
not more diligence, it is removing the restatement — read the authority, do
not transcribe it.

## Scope, and what is deliberately not claimed

**Scope-(a), scope-limited.** No physical conclusion in the corpus moves. Every
offset is ~1.3–1.5 ppb, far below the L2 100× targets that are missed by
factors of 25–1000, and the μ–p tension (11.5 ppb) is an order of magnitude
larger. Nothing here rescues or damages any prediction. What it fixes is that
the corpus can now *tell*.

**The "CODATA-2018" identification is not verified.** Only the 2022 table is in
the repository. That these literals are specifically the 2018 adjustment is
inferred from the coherence of the offsets plus recall, and PR #4860's own
"vintage correction" wording. It is not checked against a 2018 table, because
there is none here. The finding that does not depend on it — and is fully
verified — is that **each literal disagrees with the committed 2022 table by
3–4.5 σ**. If someone uploads the 2018 listing, the attribution becomes
checkable; until then it is stated as inference.

**1962 sites is not 1962 bugs.** The scan separates them:

- **SOURCE** (`.py` / `.lean` / `.ts`) — code that computes a wrong number.
  **447 sites.** These are the actionable set.
  > **🛑 CORRECTED 2026-08-21 — this bullet is wrong for 87 % of its own
  > count, and the error is mine.** "Code that computes a wrong number"
  > describes only the **executable** sites. Classified, the 448 sites split
  > **61 code / 381 prose / 6 adjudicated**: the large majority sit inside a
  > comment or a docstring and compute nothing. **The actionable set is ~61,
  > not 447.** See the second addendum below — the over-count is not merely
  > cosmetic, it points the drain at the wrong work.
- **RECORD** (`*.witness.json`, audit outputs, `.md` tables) — **1515 sites**,
  history. A
  committed witness records what a producer *actually computed*. Rewriting it
  to match the new table would falsify the record. The fix is to correct the
  producer and re-run it, which is a scoped, announced act — not an idle sweep.

`computations/audits/hardcoded-literal-audit.witness.json` alone accounts for
~550 of the raw hits: it is an audit's own *listing* of literals, not uses of
them. Counting those as defects would be double-counting the detector.

## Not done here

The sweep itself. This PR delivers the **detector and the measurement**, not
the drain. Correcting the source sites means re-running their producers and
regenerating their witnesses, which is a large, announced tranche and needs
its own scope — and per the standing directive, a witness is never edited to
make a gate green. (The figure originally given here was **447**; the
corrected actionable count is **~61**, per the addendum below.)

---

## Addendum — what landed on main, and how it re-scopes this

Reviewed at rebase time (main had moved 378 commits). Four landings bear on
this work; one changes the plan materially.

### 1. `uploads/` → `library/` (381 files)

The table this whole audit reads was relocated. Every reference here, in the
scan, and in the package drift test was repointed. Worth noting because a
detector that reads a moved authority fails *open* — it would have raised
`FileNotFoundError` rather than silently reporting "clean", but a differently
written one would not.

### 2. The α_EM outlier was a FALSE POSITIVE — and hid a real defect

I flagged `137.035944` as *"2630 σ, not any CODATA edition"* and put it ahead
of the drain. **It is not a CODATA transcription at all**: it is the
framework's own derived α⁻¹ (CS-corrected, Witten κ), which is supposed to
differ from the measured value. This note's own text says the scan "cannot
tell that from a genuinely different quantity that sits nearby"; I then
singled it out anyway. The scan behaved correctly; the triage did not.

Underneath it was a real defect of a different kind — a **layer straddle**:

| | α⁻¹ | vs CODATA |
|---|---|---|
| registry, proton-pinned, exactly resummed | `137.0359350939756` | −467.6 ppb |
| hardcoded literal (muon anchor, truncated tower) | `137.035944` | −402.6 ppb |
| **literal vs registry** | | **65.0 ppb** |

Two producers fed a muon-anchored constant into proton-pinned compute and
printed "399 ppb" for a residual that is 468 ppb. Fixed by calling the
derivation instead of copying its value. Effect on `m_K/m_π` — the one L2
success — is **0.0066 ppb**; the headline stays **1 / 5 scoreable**. The
defect was in what the number *claimed*, not what it did.

### 3. `qou-m9xp` — the pin file self-contradicts (open, `todo`)

`computations/q-pinning-50-digit.witness.json` states `q0Anchor: muon` with
muon *numbers*, while `calibration_inputs.anchor` and
`physical_anchoring_bound.anchor` both say `m_p/m_e`. A reader gets whichever
answer they grep for. Related: `qou-cezp` found the 262 Q0_FLIPs were **one**
corrupted anchor definition, and `2e4745448d` restored the muon anchor the
re-pin sweep had overwritten with its own target.

This is the same disease as the CODATA straddle — an authority disagreeing
with itself — in the *pin* rather than the *constant*. It is upstream of the
drain: correcting a producer's CODATA literal while it reads a
self-contradicting pin file fixes the smaller error.

### 4. 113 producers cannot be imported — **this re-scopes the drain**

`producer_importability_audit` (2132 producers checked, **113 unimportable**)
closes the detector gap *"witness staleness when the producer cannot run at
all."*

The drain's method is *fix the literal, re-run the producer, regenerate the
witness.* For an unimportable producer that method does not exist. So
`qou-7ot6` is not one tranche but two, and the split has to be made before
starting rather than discovered midway:

- **7ot6-a** — source sites whose producer imports and runs. Mechanical.
- **7ot6-b** — sites in the 113. Blocked on importability first; the CODATA
  literal is the lesser problem there.

**Do not** "fix" a 7ot6-b site by editing its committed witness to match.
That is the one move this note forbids throughout, and an unimportable
producer is exactly the case where it looks most tempting.

### Not overlapping

`docs/audits/2026-08-16-colour-level-and-tln-compute.md` Task 0 audits
**experiment-inverted** values (anti-fit discipline — "Δ_λ from inverted
CODATA = NOT ALLOWED"). That asks whether a value was *fitted to* experiment;
this asks whether a value was *transcribed from the wrong edition*. Different
questions, no duplication.

### One bug fixed in already-merged code

`codata_table_vintage_audit.py` (merged by #5149) compared values with `==` on
`mpf`. Two `mpf` built from the same decimal string at different working
precisions differ in the last bit, so after the rebase it reported **all 8**
constants as disagreeing by ~1e-17 while their printed digits were identical.
Now compared with a 1e-15 relative tolerance — far below any real edition
difference (~1e-9), far above construction noise (~1e-17), so detection power
is unchanged. Back to 8 checked, 0 disagree.

---

## Addendum 2 (2026-08-21) — the detector's headline was wrong for 87 % of its count

Tranche **b** of the drain began by re-measuring, and the first defect it
found was in the detector this document delivers.

### The measurement

Every `.py` / `.lean` / `.ts` near-miss was reported as a *"SOURCE site
(compute a wrong number)"*. Classified by whether the literal is actually
executable:

| class | sites | can it compute anything? |
|---|---:|---|
| **CODE** | **61** | yes — the actionable queue |
| **PROSE** | 381 | no — inside a comment or a string |
| **ADJUDICATED** | 6 | executable, but marked reviewed (`noqa: P31`) |
| *(RECORD, unchanged)* | 1501 | no — witness / audit output |

So the actionable queue is **~61, not 447** — the original figure over-stated
it by about **7×**.

### Why the direction matters more than the size

Tranche **a** moved this count **447 → 448**. That is not a regression. A
drain that replaces a stale literal with a registry read and **records the
superseded value beside it** — which is what good provenance looks like —
lands in PROSE. Counting prose as defects therefore makes the number *rise*
when the corpus gets better, and rewards deleting the provenance comment to
bring it back down. Only CODE gates under `--strict` now.

### Two defects in the classifier itself, both mine, both recorded

1. **Line-keyed classification under-counts code.** A first, throwaway
   measurement keyed on line number and reported **53** code sites against a
   true **61**: `X = 938.27208816  # was 939.56542052` is executable code with
   a comment, and a line-keyed classifier calls the whole line a comment. The
   committed version uses `tokenize` and classifies by **column span**.

2. **Untracked strings over-count code — the opposite of what I argued.** The
   first `.lean`/`.ts` classifier handled comments only, on the reasoning that
   an untracked string could merely let a delimiter open a comment that is not
   there, i.e. an *under*-report. Wrong in the direction that matters: prose
   inside a string is then classified `code`. Measured,
   [`content/values/registry.ts:647`](../../content/values/registry.ts) is a
   CODATA value quoted inside a `description:` string and was reported as
   executable. The committed version runs a character-level state machine that
   tracks strings; the docstring making the wrong claim is corrected in place
   rather than deleted.

### Self-reference, third instance in this arc

Writing the docstring that explains all of the above moved `prose_sites`
**381 → 397** — the scan counting its own explanation of the defect. The
scanner's source now joins its witness and this document in `SELF_ARTIFACTS`,
for the same reason: an artifact *about* a finding is not an instance of it.

### Verification

`codata_corpus_literal_scan.py --self-test` covers all 11 classifier shapes
and the 4 adjudication-marker cases. Every one is a defect this file actually
had, not a hypothetical. `scripts/precision-gates.sh`: all blocking gates
green.
