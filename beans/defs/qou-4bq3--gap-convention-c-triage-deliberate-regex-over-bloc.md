---
# qou-4bq3
title: 'GAP: convention-c-triage DELIBERATE regex over-blocks 8 of 24 B3 verdicts'
status: completed
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-25T01:09:17Z
updated_at: 2026-10-10T10:49:18Z
parent: qou-cdx1
---


## Defect

`scripts/convention-c-producer-migrate.py:58`

    DELIBERATE = re.compile(r"(_c\b|_C\b|C_|_c_|zc$|z_c)", re.I)

The `C_` alternative is compiled with `re.I`, so it matches the substring
`c_` inside ordinary identifiers. `scripts/convention-c-triage.py` uses it
(via `_file_has_c_reference`) to class a site B3 "deliberate comparison —
leave it; it measures the excision", so a false positive tells an agent to
skip a real defect.

## SCOPE: this does NOT affect the audit's actionable count

Recorded first because it is the easy thing to get wrong. The regex lives in
`convention-c-producer-migrate.py` and is consumed by
`convention-c-triage.py`. It is **not** what produces the `deliberate` flag in
`convention-c-producer-audit.py`: that audit's `scan()` filters candidate
targets on `"z" in nm.lower()` (line 730), so a `c_`-style collision inside an
ordinary identifier can never reach it. Verified by reading the filter, not
inferred. All 15 of the audit's `deliberate` verdicts are genuine
`z_C`-family names.

So a before/after measured with `convention-c-producer-audit.py` is unaffected
by this bug. What moves is the **triage's B3 verdicts**, i.e. the advice an
agent is given about which sites to skip.

## Measured, 2026-08-25 (corrected)

**8 of 24 B3 verdicts (33%)** rest ONLY on this collision. An earlier version
of this bean said 7 of 23; that undercounted by one.

| file | matched | in scope of |
|---|---|---|
| `computations/audits/weight_factor_audit.py` | `__doc__`, `q_fac_n` | #5738 |
| `computations/canonical_lepton_braid_words.py` | `desc_tr_M` | #5738 |
| `computations/habiro/habiro_exact_mass_endomorphism.py` | `c_mp` | #5739 |
| `computations/probes/m_pi_hecke_prediction_probe.py` | `c_Lminus`, `c_Lplus`, `c_e_minus`, `c_sigma1` | #5739 |
| `computations/probes/pentagon_multipair_borromean_h4_probe.py` | `c_4` | #5739 |
| `computations/probes/t6_tau_h5_embedding_probe.py` | `qfac_3` | #5739 |
| `computations/t6_lepton_h3_3channel_convention.py` | `qfac_3` | #5739 |
| `computations/t6_three_halves_factor_probes.py` | `qfac_3` | #5739 |

The missed one is `canonical_lepton_braid_words.py`, matching on the `c_`
inside `desc_tr_M` (line 168) -- a local variable holding a Markov trace, as
un-convention-C a name as exists in this corpus. Systematic, as expected:
`c_k` coefficients, `q_fac`/`qfac` quantum factorials and now `desc_*` are all
pervasive here. The other 16 B3s are sound -- audit `deliberate` flag, or a
real `z_C`/`pin_C`.

Method, so the number is re-derivable: run `convention-c-triage.py`, take every
file with a B3 verdict, and ask whether `DELIBERATE` still matches under a
**case-sensitive** pattern. Six such files remain on PR #5738's branch, which
has already migrated the two `c_`/`desc_` cases out of B3; 6 + 2 = 8 of 24.

## Every one of the 8 was a real defect, and all 8 are now migrated

The verdict was wrong in all eight cases, not merely unreliable: #5738
migrated the first two and #5739 the other six, in each case by **reading the
site rather than trusting the verdict**. That is the practical lesson --
B3 is advice, not a finding.

## Confirmed true positive

`weight_factor_audit.py` `check_C8` was classed B3 and is a genuine defect:
it asserted `z_C` AS THE SPECIFICATION ("any consumer hardcoding a
different value would be a bug"). Migrated on PR #5738 by reading the site
rather than trusting the verdict. The `C8` is a check number, not convention C.

## Fix

Do NOT simply anchor as `\bC_`: `_` is a word character, so `\bc_` still
matches a name that STARTS with `c_` (`c_4`, `c_mp`). The C-convention
alternatives want to be case-SENSITIVE — `z_C`, `pin_C`, `Z_C` are
capitalised by convention; the lowercase `c_` prefix is the ambiguous one.
Split into a case-sensitive group for the C spellings, keep `re.I` only
where safe. Re-run the triage and confirm the 16 genuine B3s are unchanged.

## Not fixed on PR #5738

Deliberately: shared tooling a sibling agent was running concurrently
against the other half of the surface. Changing its verdicts mid-flight
would have been worse than the false positives.

## Consequence for the sibling drain -- resolved, recorded for the next reader

6 of the 8 were in PR #5739's scope and could have been left as "deliberate
comparisons" on a verdict that does not hold. They were not: #5739 migrated
all six. The risk this bean describes is therefore realised-and-survived
rather than hypothetical -- which is the argument for fixing the regex before
the next drain, when no one may check.


## 2026-10-10 re-audit verdict: **LIVE** (bean `qou-am5t`)

`convention-c-triage.py`'s DELIBERATE regex compiles `C_` with `re.I` and so
matches `c_` inside ordinary identifiers, over-blocking 8 of 24 B3 verdicts --
a detector telling an agent to skip a real site. Live: a false DELIBERATE is
the dangerous direction, and the value audit does not use this regex.

Full 41-bean triage table and the method behind it: [`docs/coordination/convention-d-migration-status.md`](../../docs/coordination/convention-d-migration-status.md) §9.

## 🛑 2026-10-10: ALREADY FIXED — my own "LIVE" verdict six lines up is WRONG

Measured on `main` `ac111c1814`. **The regex this bean is about does not exist
any more**, and has not since 2026-08-25. `convention-c-producer-migrate.py:58`
— the line this bean names — is not a regex; line 66 reads

    DELIBERATE = is_deliberate_c_name

imported from **[`scripts/lib/convention_c_names.py`](../../scripts/lib/convention_c_names.py)**,
a shared module that replaced the two copies of the `re.I` blob with **three
case-aware patterns**:

| pattern | matches | why |
|---|---|---|
| `_C_TOKEN` = `(?:^\|_)C(?:_\|$)` | `z_C`, `pin_C`, `C_LABEL` | CASE-SENSITIVE — the corpus capitalises the label |
| `_Z_C` = `(?:^\|_)[zZ]_?[cC](?:_\|$\|(?=[A-Z0-9]))` | `z_c`, `zC`, `zc1` | a lowercase `c` counts only anchored to `z` |
| `_CONV_C` = `(?:^\|_)(?:conv\|convention)_?[cC](?:_\|$)` | `convention_c`, `conv_C` | the convention spelled as a word |

and this bean's **"## Fix" section is what was implemented**, almost to the
letter: it asked for a case-sensitive group for the C spellings, keeping `re.I`
only where safe. `re.I` survives on `_CONV_C` alone, where it cannot collide.

**The fix carries a regression lock naming this bean.** `SELFTEST_MUST_NOT_MATCH`
holds all eight false-B3 bases from the table above — `q_fac_n`, `qfac_3`,
`c_mp`, `c_Lminus`, `c_Lplus`, `c_e_minus`, `c_sigma1`, `c_4`, `__doc__` — plus
`desc_tr_M`, annotated *"found here 2026-08-25, NOT in the bean: an eighth false
B3"*, i.e. the implementer independently re-found the same eighth case this bean
records. Verified rather than read: **51 selftest rows, 0 FAIL.**

It also measured more than this bean did, and in the useful direction: **1112
distinct names / 5316 occurrences** matched only through the collision, against
the 8 B3 verdicts measured here. And it records a replacement blind spot
honestly — a file whose only marker is a camelCase `zPrimeC`, with no
underscored `_C` and no `z`+`c` adjacency, is invisible; the obvious widening
(a trailing camelCase `C`) was measured at **~45 % precision** (22 genuine / 26
false: `CShR4` is a free cumulant, `SL2C` is SL(2,ℂ)) and rejected on the
grounds that a detector at 45 % trains its readers to ignore it.

### How the wrong verdict happened, because it is the failure this repo keeps recording

The 2026-10-10 triage called this LIVE off the bean's own `## Not fixed on PR
#5738` section plus its `## Fix` prescription, **without grepping for the
symbol**. The corpus-grep checklist exists for precisely this, and one command
would have settled it:

    grep -rn 'is_deliberate_c_name' --include='*.py' .

A bean's `## Status` / `## Not fixed` note is **not authoritative** — AGENTS.md
says that of source-file status notes and §path-6 says it of beans, and this is
an instance of the second. Worse, the bean is *specific and well-measured*,
which is what made it persuasive: it names a file, a line number and a regex,
and all three went stale together.

Related: the sibling-bean trap recorded in AGENTS.md §4 — *"a sibling's bean is
not a primary source either"*. This one was my own, which is no better.

**Status: closeable.** The subject is a detector regex, not a conjecture, so
13a does not hold it open. Closing.

## Follow-up the same day: the triage output CONFIRMS the fix, and shows what the fix now misses

Ran `convention-c-triage.py --json` on `main` `ac111c1814` — **133 records, 119
`deliberate=True`, 14 `deliberate=False`** — specifically to check whether any
surviving `deliberate` verdict still rests on a collision. **None does.** Every
reason string now names the C-named target itself:

    B3: the target `z_c` is itself C-named — labelled comparison
    B3: the target `z_C_historical() -> return` is itself C-named
    B3: the target `Z_C` is itself C-named
    B3: the target `zC` is itself C-named
    B3: the target `z_C_expr` / `z_C_num` / `z_C_of_t` / `_zC` is itself C-named

Not one `c_k`, `q_fac_n`, `qfac_3`, `desc_tr_M` or `__doc__` among them — i.e.
the 1112 colliding names are gone from the verdict basis, measured from the
output rather than from the patterns. And the reason string names the symbol,
which closes the bean's *other* complaint, the one about legibility: the module
docstring states it as *"the whole cost of the old regex was that 'this file
references a C-named symbol' gave a reader no way to see the symbol was
`__doc__`"*. Now it does.

### 🛑 And this corrects a claim of mine from earlier in the same session

I reported `computations/qbeta/qbeta_ck_cache.py:140` in chat as *"a live
production file NOT in the registry's blocked list"*, offered as the one
genuinely-live residual in the shape audit's actionable set. **That is wrong.**
Read the site:

    if convention != "C":
        raise ValueError(...)

    # Convention C, reached ONLY via the explicit --historical-convention-C
    # flag. C was excised by owner ruling (2026-08-09, re-affirmed 2026-08-15
    # and 2026-08-26); this path exists solely so the committed witness stays
    # machine-reproducible, and it is never the default.
    z = sqrt(q) / (1 + q)

The default D path *prints REFUSING TO RUN and exits 2*, and the whole site is
adjudicated and `completed` under bean `qou-ckwt`, whose record states it:
*"C is reachable only via `--historical-convention-C`. The witness now records
`"markov_convention": "C"` plus a note."* So the most alarming entry in the
actionable list — the canonical `c_k` producer, the file AGENTS.md's own `c_k`
banner names — is a **false positive**, and I had the corpus-grep path (path 6,
beans) that would have told me so.

### Why it is a false positive, which is the part worth keeping

The target is a bare **`z`**. The deliberateness is carried by a
`convention != "C"` raise, a function parameter and a CLI flag — **not by any
identifier** — so `is_deliberate_c_name` cannot see it however the patterns are
widened, because there is nothing to widen onto. That is not a defect in the
fix; it is the fix's declared trade being paid for the first time, and in the
**acceptable direction**: this *under*-blocks, so a false "actionable" costs a
reader one site visit, where the `re.I` bug *over*-blocked and a false
"deliberate" hid a real defect behind an excuse. Recorded as **row 52** of
[`docs/audits/2026-08-15-detector-blindness-taxonomy.md`](../../docs/audits/2026-08-15-detector-blindness-taxonomy.md)
and in `convention_c_names.py`'s own "Deliberately NOT matched" list, beside the
camelCase blind spot it sits next to.

**The bean stays `completed`** — its subject is the over-blocking regex, which
is gone. The under-blocking is a new, differently-signed, and by design.
