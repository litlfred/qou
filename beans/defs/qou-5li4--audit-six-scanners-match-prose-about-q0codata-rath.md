---
# qou-5li4
title: 'AUDIT: six scanners match prose ABOUT q0/CODATA rather than code USING it — 3 are gates, 1 under-reports this epic''s own counts'
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-26T03:58:32Z
updated_at: 2026-11-16T18:12:00Z
parent: qou-2002
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


## 2026-08-26 — `_source_normalise.py` landed; consumer wiring deliberately NOT

Added [`computations/audits/_source_normalise.py`](computations/audits/_source_normalise.py):
`code_only()` (tokenize; blank COMMENT + triple-quoted STRING; **preserve line
and column**), `blank_declaration_prose()`, `code_only_ast()`. Runs its own
`--selftest`, which fails loudly if a future narrowing breaks line preservation
or lets a reason string indict its own claim.

### The finding that came out of building it is bigger than the one that prompted it

This bean recorded that `hardcoded_literal_audit`'s docstring strip corrupts
line numbers (476 reported for a string at 647). Measured across 400 live
producers, the same `re.sub(r'\"\"\".*?\"\"\"', "")` does something worse:

    files where the old strip DELETES lines : 397 of 400
    total lines removed from the scan       : 18942
    worst single file                       : 482  (_li_2_q_util.py)
    code_only line-count preserved          : 400/400, asserted

Those lines are not merely **mis-numbered**, they are **never scanned**. A
`--strict` gate has been silently blind to ~19k lines of the corpus it audits.

### Why the wiring is not in this change

I wired `hardcoded_literal_audit` to `code_only` and its `i9_violation` count
moved **248 → 332 scripts**. That is consistent with recovering unscanned lines
— but I could not *characterise* the +84, and I should say why rather than
imply the check was skipped: my diff of old-vs-new flagged lists compared two
**truncated** displays (the audit prints 24 rows then "… and 320 more"), so it
reported 24 = 24 and no delta. A vacuous check, of the same family this bean is
about.

**A +84 on a strict gate that I cannot explain is not shippable**, so it was
reverted. It needs the full list (not the display), a sample of the newly-hit
lines, and its own review.

### Two scope corrections to this bean's own text

- **The evidence case is not reachable by `code_only`.** `canonical_tower.py`'s
  note is **implicitly-concatenated single-quoted** strings, not a docstring.
  `code_only` deliberately leaves single-quoted strings intact — they carry
  real declared values (`VAR = "1.1099785827..."") the audit must still see. So
  wiring this module fixes the POSITIONS and the COVERAGE, **not** that false
  positive. Separating a sentence from a declared constant is the pattern-shape
  question, not a normalisation one.
- Consequently "fixes all six by import" is **too strong**. It gives all six a
  correct, shared, line-preserving normaliser; each still needs its own pattern
  reviewed.


## 2026-08-26 — `blank_message_strings` folded in from PR #5810; and my ratchet worry was unfounded

### Capability added, contributed by a sibling

#5810 offered a pass `code_only` deliberately lacks, and it is worth having.
`code_only` leaves single-quoted strings intact — correct, they carry declared
values — which also leaves **message** strings matchable. Their measured case:

    raise SystemExit(f"ANCHOR STRADDLE in q-pinning-50-digit.witness.json: ...")

A guard whose whole purpose is to PREVENT reading the muon pin, read by a
classifier as evidence that it does. The canonical shape of this defect class.

`blank_message_strings(tree)` blanks str constants inside an **f-string**, a
**`raise`**, or a **`print`/`warn`/`log`**-family call — **except** when the
string is an argument to an `OPERATIVE_CALL` (`open`, `Path`, `read_text`,
`mpf`, `Decimal`, `json.load`, `witness_path`, …), because those *act on* it.
**That carve-out is the load-bearing half**; without it the pass blanks genuine
reads. Orthogonal to `blank_declaration_prose`, which keys on dict keys rather
than call context.

Verified on the real file rather than the synthetic case:
`qbeta_habiro_residual_probe` goes **2 → 1** occurrences — the guard message
blanked, the genuine `record_upstream(COMP / 'q-pinning-50-digit.witness.json')`
read untouched. The selftest now covers both halves and fails if either breaks.

### A fifth private implementation exists and should be retired

#5810 landed `_code_only_text()` in `q0_producer_pin_classifier.py` an hour
before this module, and flagged it themselves: it **joins tokens with a space**,
so it does not preserve line numbers — the exact 476-vs-647 defect. It currently
gates only a boolean, so no position is reported off it, but it should become
`from _source_normalise import code_only`. Recorded so it does not quietly
become the fifth unshared copy this module exists to end.

### My precision-gates worry, checked and unfounded

#5805 warns that `precision-gates.sh` on a branch **behind** main walks ratchets
**backwards** — it regenerates tree-measuring audits and says "commit the
regenerated one", and `git log` on the new entries finds main commits, which
reads as "main's, so commit it". They measured `drained_files 913 → 888` at 46
behind while both HEAD and origin/main carried 913.

**I saw that same 913 → 888** and reverted it — but attributed it to this
container missing `sympy`/`numpy`/`scipy`/`clarabel`. Their diagnosis is the
better one for that number. Both were true of my situation; only theirs explains
the ratchet direction.

**Checked whether I committed anything backwards: I did not.** The two audit
witnesses I committed in the #5797 arc match `origin/main` exactly today —
`Q0_OK 972`, `Q0_ANCHOR_MISSING 1649`, `proton-pin 1682`. The revert was right
even though half my reasoning for it was wrong.


## 2026-11-16 — all six scanners wired to `_source_normalise` with self-tests (PR #8146)

Extended `computations/audits/_source_normalise.py` with two line/column-preserving passes (`code_and_numeric_strings_only(src)`, which blanks comments, docstrings, and non-numeric prose strings / `FSTRING_MIDDLE` tokens while keeping numeric string constants like `mp.mpf("0.78233341")` intact, and `identifiers_only(src)`, which blanks all comments and string literals) and wired all six scanners:

1. **`computations/audits/hardcoded_literal_audit.py`**: Replaced `re.sub(r'\"\"\".*?\"\"\"', "", text, flags=re.DOTALL)` with `code_and_numeric_strings_only(text)`, fixed `has_banner` to use `ast.get_docstring` (so shebang-prefixed files like `canonical_tower.py` have their `CLASS-A` banner recognised), and skipped `codata_2022_source.py`. Live `i9_violation` count drops `338 → 293` (`349 → 325` scripts, removing 24 prose-only false-positive files including `canonical_tower.py`). Added `--self-test`.
2. **`computations/audits/canonical_script_input_audit.py`**: Matched identifier markers against `identifiers_only(text)` (removing 208 prose-only `Q_β-only-hadronic` false positives) and added AST import inspection (`_imports_q0_from_q_parameter`) so importing only non-`q₀` symbols (`MASS_RATIO_MU_E` in `knot-volumes.py`, `vol_4_1_at` in `hyperbolic_volumes.py`, etc.) does not set `uses_canonical_q0_source: True`. Added `--self-test`.
3. **`computations/audits/q0_consistency_audit.py`**: Wired `code_and_numeric_strings_only` so prose-string mentions (`q0AnchorReason`) classify as `stale-docstring` and separated pin recognizers (`PROTON_PREFIX`, `_PROTON_SIG`) and anti-straddle guards (`if not q.startswith("1.10997858275")`) into `pin-recognizer-or-guard` instead of `production-hardcode`. Added `--self-test`.
4. **`scripts/convention-c-taint.py`**: Applied `code_only` in `_read_source`, `_module_sources`, and `_read_context_refs`, removing 282 phantom comment/docstring read-edges (`2496 → 2214` edges) and adding an 8th self-test case (`selftest: 8/8`).
5. **`computations/audits/derived_alpha_em_usage_audit.py`**: Wired `code_and_numeric_strings_only` into `classify()` and `scan()`, removing 11 prose-only false-positive `INPUT` flags (`64 → 53`, including `coulomb_mirror_killswitch_probe.py:195` and f-string prose in `wlambda_binding_a3_mirror_selection.py:129`). Extended `--self-test` (`12/12 PASS`).
6. **`computations/audits/q0_muon_population_partition.py`**: Evaluated `direct_pinners()` against `code_only(text)`, recovering `derived_masses.py` (previously exempted by its own docstring mentioning `q_parameter`) and dropping 2 audit scripts (`mech5_pin_bind_taint_audit.py`, `proton_pin_assertion_check.py`) that quoted `d["derived_50_digit"]["q"]` in comments/docstrings. Added `--self-test`.
- Note on `q0_producer_pin_classifier.py`: measured replacing `_code_only_text` (which strips all `STRING` tokens) with `code_only` (which keeps single-quoted strings); keeping single-quoted strings caused 23 false `BOTH` flips where `"ANCHOR"` appeared in a string literal alongside `"ideal"`/`"muon"`, so `_code_only_text`'s all-string strip in `q0_producer_pin_classifier.py` is intentionally retained (`--selftest` passes).
- Kept at `status: in-progress` for owner review. PR #8146 (`5c6c5fb610a38f0405e9d280b16b0999a8124c8f`).
