---
# qou-5li4
title: 'AUDIT: six scanners match prose ABOUT q0/CODATA rather than code USING it — 3 are gates, 1 under-reports this epic''s own counts'
status: todo
type: task
priority: normal
created_at: 2026-08-26T03:58:32Z
updated_at: 2026-08-26T04:02:29Z
---

Split out of `qou-1c4y`, which records six instances of this defect found the
hard way while building the q₀ independence checker. A dispatched audit swept
the rest of the corpus for peers. Every accusation below was verified by running
the scanner in-process or re-tokenizing the accused file — not by reading code.

## The class

**A scanner matches text that DESCRIBES the thing rather than text that DOES
it.** This corpus is full of careful prose about q₀, CODATA literals and
anchors *precisely where the code is careful not to use them*, so a raw-text
scanner systematically convicts the files that are most correct. Four
sub-classes: (1) docstring/comment, (2) a self-describing declaration or note
field, (3) module-name vs imported symbol, (4) cone traversal into a provider.
A fifth is recorded on `qou-1c4y`: a function PARAMETERISED on q is not a
function that READS q₀.

## Six vulnerable scanners, ranked

**1. `hardcoded_literal_audit.py` — sub-class 2, confirmed IN THE COMMITTED
WITNESS, `--strict` gate.** Strips triple-quoted blocks but not ordinary string
literals. `canonical_tower.py:647` carries a witness note reading *"this module
does NOT use the β-decay Q-value 0.78233341 MeV as E_0"* — filed as an
`i9_violation` with `rel_err: 0.0`. The module's own denial is the evidence
against it. `codata_2022_source.py`, the CODATA source of truth, is convicted on
its own docstrings. **Bonus:** the docstring strip deletes newlines instead of
blanking them, so every line number after the first docstring is wrong — the
witness says 476, the string is at 647. Measured: ≥31 prose-only hits / 20 files
of 700 hits / 248 files.

**2. `canonical_script_input_audit.py` — sub-classes 3 AND 1.** `from
q_parameter import` sets `uses_canonical_q0_source: true` on module name alone;
11 of 770 true rows import only non-q₀ symbols, including `knot-volumes.py` with
`MASS_RATIO_MU_E` — the exact file `qou-1c4y` names. The audit already has a
separate `MASS_RATIO_MU_E` marker and still credits the module. Separately, 28
markers fire from prose only, and **24 rows carry scheme `Q_β-only-hadronic`** —
a calibration-discipline claim — where `Q_beta` appears in no code token.

**3. `q0_consistency_audit.py` — sub-class 2, `--strict`, 187
`production-hardcode`.** Verified prose rows include another detector's `PINS`
reference table, an English sentence in a probe, and — the sharpest — pin
**recognizers** (`PROTON_PREFIX`, `_PROTON_SIG`) and an anti-straddle **guard**
(`if not q.startswith("1.10997858275")`). Text that *identifies or defends* a
pin, convicted as text that *hardcodes* one.

**4. `scripts/convention-c-taint.py` — sub-class 1 inside a FIXPOINT.** 231 of
3661 read-edges (6.3 %) exist only in comments, and one phantom edge taints a
subtree. Measured: of the live taint set, **2 of 5 exist only because of a prose
edge**. The verified instance is a comment written to say the producer does NOT
touch that witness.

**5. `derived_alpha_em_usage_audit.py` — gate exit code.** `CONSUMED` is
`r"=\s*[^=]|return\s|[*/+-]"`, so **a hyphen in an English sentence counts as
consumption**. 5 of 50 blocking `INPUT` rows are prose, the best self-refuting:
a string reading *"alpha_EM DERIVED from q0 (was CODATA 1.43996)"* — the audit
flags the sentence announcing the derivation it wants.

**6. `q0_muon_population_partition.py` — SAME DEFECT, OPPOSITE SIGN: a false
NEGATIVE, and it feeds this epic's headline counts.** `ROUTES_ANCHOR` is matched
against raw text and used as an EXEMPTION. `derived_masses.py` binds q₀ straight
out of the pinning witness and is silently exempted because its docstring
explains *"this module computes at the muon pin regardless of what
`q_parameter` would…"*. The sentence denying that it routes through
`q_parameter` is read as proof that it does. **2 producers under-reported**, so
the `qou-1c4y` direct-pin counts are a floor, not a total.

## Audited and found SOUND — do not re-check

The Python half of `precision-gates.sh` (all `ast.parse`-based, so **no blocking
precision gate is exposed**), `float64_leak_audit.py` (tokenize, preserves
line/col), `q0_hardcoded_pin_audit.py`, `scripts/real-sorry-scan.py` (exists to
fix this class on the Lean side), `legacy_formula_audit.py` (vulnerable in
principle, 0 hits today), `guarded_off_audit.py`, `fitted_labelled_canonical_audit.py`,
`e0_calibration_audit.py`, `content/pipeline/trace-convention-audit.ts` (scans
`.md`, where prose IS the artifact — different failure mode).

Not looked at, so do not infer clean: `lean-vacuity-axiom-audit.ts`, the ~35
`computations/audits/` scanners over `.json`/`.md`/`.lean`, `scripts/lean-*.py`,
the rest of `content/pipeline/*.ts`.

## The fix worth doing once

The corpus already contains **four independent correct implementations** —
`float64_leak_audit._blank_triple_quoted`, `q0_hardcoded_pin_audit`'s tokenize
pass, `real-sorry-scan.py`'s Lean stripper, and
`q0_independence_checker._blank_declaration_prose` — **and none is shared**.
Every vulnerable scanner re-derives it privately or fails to.

One module, `computations/audits/_source_normalise.py`, exporting
`code_only(src)` (tokenize; blank `COMMENT` + triple-quoted `STRING`; preserve
line and column) and `blank_declaration_prose(tree, keys)`, fixes all six by
import — and fixes #1's line-number corruption for free.

## Ordering note

#1, #3 and #5 gate on exit code, so their false positives are enforced. #6 is
the one that has already corrupted a number I published. #4 is triage noise by
its own docstring ("a review queue … not a verdict") and can wait.


## 2026-08-26 — one more AUDITED AND SOUND: `convention_frame_staleness_audit.py`

Checked because sibling PR #5815 leans on its 47-candidate list to confirm a
471× Q_β regression, and the file reads raw text (`text = py.read_text()`, line
100) with no AST or tokenize pass — the shape this bean is about.

**It is clean, and the suspicion did not survive measurement.** Its `D_BOUND`
regex is `^`-anchored and ASSIGNMENT-shaped:

    ^\s*{_Z_NAME}\s*=\s*[^=\n]*\*\*\s*3\s*/\s*\(\s*\w+\s*\*\*\s*2\s*\+\s*1\s*\)

A `#` comment cannot match (the `#` precedes the name), and docstring prose
almost never presents as a bare left-anchored assignment. Measured over all live
`computations/**/*.py`: **212 raw-text matches, 212 code-only matches, 0
prose-only.** Re-tokenized with COMMENT and triple-quoted STRING blanked while
preserving line and column.

The author had already reasoned about the failure mode from the other side — the
constant carries a note explaining why it is a NAME list rather than "any
assignment", *"the shape alone over-matches badly (121 candidates unfiltered vs
137 producers here)"*.

**Generalisable:** raw-text matching is not itself the defect. An
`^`-anchored, assignment-shaped pattern is structurally immune to both prose
sub-classes without needing a tokenizer. The six vulnerable scanners above are
vulnerable because their patterns are *bare-token* (a literal, a module name, a
symbol) and so match anywhere — including inside the sentence explaining why the
file does not do the thing. **Pattern shape, not input normalisation, is the
cheaper fix where the target is an assignment.**
