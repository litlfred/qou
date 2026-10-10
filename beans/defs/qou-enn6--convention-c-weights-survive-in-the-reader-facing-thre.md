
---

## 2026-10-10 — the prose half was NOT fully fixed: §2 still asserted the word this block's own line 27 names as a convention-C signature. FIXED.

Re-audit of the C→D migration tracker (session epic `qou-am5t`). The
RE-SCOPED note above is right that a sibling's two-convention table is option 1
done better than I proposed it. **But it credits the sibling with the whole of
option 1, and option 1 had two halves.** The weights half landed; the
"suppressed" half did not.

### The self-contradiction, in one reader-facing block

`observations/atom-mass-full-hecke.md`, as it stood on `main`:

- **line 27** — *"Any statement that the alternating block is **suppressed**
  describes convention C; under convention D that channel does not contribute
  at all, and a nonzero $\hat y_{\mathrm{alt}}$ is itself a convention-C
  signature."*
- **line 48**, Key observations §2, twenty-one lines later — *"Under canonical
  $q$-deformed weights, the alternating block is **suppressed**."*

So the block named "suppressed" as a C-signature and then asserted it about the
canonical convention, in the same block, in prose a reader reads top to bottom.
This is what the RE-SCOPED note meant by *"an interpretive claim, not just a
number"* — and that claim was the one part the sibling's fix did not reach,
presumably because the fix was aimed at the weights table.

### What §2 now says, and why it is corpus-derived rather than my reading

The heading *"Alternating channel sign flips"* was describing something real —
`tr_alt` genuinely alternates in sign across the table (`+1.022, −1.460,
+1.692, −1.984, …`). The defect was conflating the **trace** with the
**contribution**. §2 now separates them: the trace alternates; its contribution
is zero, because

```
QOU.SchurWeyl.ocneanuWeight_conventionD_eq_zero_of_three_rows
```

is sorry-free for general `n` over any field with `q² + 1 ≠ 0`, and the
alternating channel is the sign representation, whose partition `(1^n)` has
`n ≥ 3` rows. So `ŷ_alt = 0` **exactly** and `tr_alt` cannot reach `tr_full` at
all — "absent", not "small". The final sentence keeps the true part: the
apparent sign variation *in the total* was a classical-weighting artifact.

Independently corroborated inside the corpus, which is what makes this
exemption 2 rather than my judgement:
`braids-and-knots/jones-markov-trace.md:29` already states the same thing for a
reader — *"Under convention D that scalar **vanishes** precisely when
`ℓ(λ) ≥ 3`… The degeneracy is not a defect convention D introduced; it is what
convention D means"* — citing `TemperleyLiebTower.lean`, sorry-free. Two
reader-facing blocks now agree instead of one contradicting itself.

### Also fixed in passing: a real render-QA hit in the same block

The display-math block at `:11-16` had two lines beginning `+` inside `$$ … $$`
(two spaces of indent, which a markdown list parser still takes). That is a
named item in the AGENTS.md render-QA battery — the list-parser hijack.
Operators moved to end-of-line; **0 hits remain**.

One note for anyone re-running that battery: the naive Python guard
`line.strip()[:1] in '+-*'` returns **True for an empty line**, because
`'' in '+-*'` is `True`. That produced a phantom residual hit after the fix was
already correct, and it is the same class as every other row in the
detector-blindness taxonomy — the checker reporting about itself. Guard with
`s and s[0] in '+-*'`.

### Verification actually run (not "CI will catch it" — there is no CI)

Platform `folio-assistant` at the pin `717aa19a6`, cloned via
`scripts/setup-folio-assistant.sh`:

| check | result |
|---|---|
| `bun run scripts/run-validate.ts folio/quantum-observable-universe` | **✓ Valid — 9 issue(s)**, byte-identical to the 9 the pin's own notes record as expected. My edit adds none. |
| `qa-sweep … atom-mass-full-hecke.ts` (all **120** criteria) | **0 critical, 0 major, 0 minor**; 43 `needs-agent`, all pre-existing agent-judgement items |
| `qa-sweep … --only render-math-mode-envelope` | **0 findings** |
| grep battery by hand | `$` 76 (even), `$$` 2 (even), braces 57/57, `\bigl`/`\bigr` 0/0, `\begin`/`\end` 0/0, list-hijack **0** |

**What I did NOT do, and it is not an oversight.** `source_hashes.md` in
`atom-mass-full-hecke.qa.json` is now stale (`760156a395ce` → `277d3a409be7`)
and **qa-sweep did not re-stamp it** — it wrote nothing, and no `.qa.json`
anywhere in the tree is dirty after the sweep. The in-repo sidecars are frozen
at `updated_at: 2026-08-30`; the derived QA corpus moved to the cat-harness
`qa-reports` branch on an owner ruling of 2026-10-04 (`run-validate` says so in
its own `no-orphan-sidecar` warning, and `.folio-assistant-pin` records the
ruling). Hand-editing a frozen sidecar to make a hash match would be writing to
a surface the owner moved, so it waits.

Also noting `render-latex.ts` has **no CLI** at this pin — invoking it directly
exits 0 having run nothing. A silent `exit 0` from it is not a render check,
and I nearly recorded it as one.

### What remains, unchanged from the RE-SCOPED note

Option 3 only, and its blocker is confirmed **stronger** than recorded. The
bean says every `B/A_Skein` grep hit is under `_deprecated/`. Measured
2026-10-10: `grep -rln "B_over_A_Skein\|BA_Skein\|B/A_Skein\|ba_skein"
--include=*.py` returns **nothing at all** — not in `computations/`, not in
`_deprecated/`, nowhere. A looser case-insensitive `skein` grep returns only
Hecke/Skein-*relation* code and audit scripts, no `B/A` producer. So the
formula has no implementation in the tree under any of those names, and option
3's cost is genuinely unknown rather than merely unmeasured.

The `tr_full` D values are still recorded in the table above and in the
regenerated witness for whoever takes option 3 with `qou-5ll9`.

**Status: staying `todo`**, priority unchanged. The interpretive defect this
bean's first half was about is now closed; what is left is the three-column
table, which is `qou-5ll9`'s arc as much as this one's.
