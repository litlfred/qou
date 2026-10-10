---
# qou-jdhm
title: 'Delta-tr(2H) drift: the corpus-wide +0.2% deuteron claim needs 0.5952, binding_canonical returns 0.5566'
status: completed
type: task
created_at: 2026-08-15T15:39:42Z
updated_at: 2026-08-15T15:39:42Z
---


Found while doing bean `qou-bind` (the one-line `hyperbolic`-flag fix in
`computations/binding_link_volumes.py`). Not fixed there: the fix is not local to that
file and requires a physics judgement this session cannot make alone.

## The measurement

`binding_link_volumes.py` computes `B = m_e × Vol(K_bind) × Δtr` and its docstring
claimed the deuteron matched at **+0.2%**. It does not, and the repo's own committed
witness has never said it did:

```
binding-link-volumes.witness.json
  deuteron_endomorphism_holds   "passed": false
  computed  = 6.306958776805962      (i.e. err = −6.31%)
  tolerance = 1
```

Running the script today reproduces exactly that: **−6.3%**.

**+0.2% is precisely the claim that Δtr(²H) = 0.5952.** Measured this session:

```
Δtr needed to give +0.2%                             = 0.5952835748896166…
hardcoded, binding_per_bond_decomposition.py:126     = 0.5952
binding_canonical(1, 1, use_closed_form=True) TODAY  = 0.5566260326923999
```

The +0.2% figure agrees with that hardcoded constant to four digits, and the function
the constant is *attributed to* no longer returns it. So this is one drift, not two
independent errors.

## Why this is not a one-line fix

**1. It is load-bearing in at least 7 files**, all quoting +0.2% as an established
result:

- `computations/binding_error_source.py:11,105` — "sits below the ceiling → works (+0.2%)"
- `computations/binding_multibond_wenzl.py:9`
- `computations/binding_per_bond_decomposition.py:126` — the hardcode itself
- `computations/probe_volume_wedderburn_delta_lambda.py:126` — "Known: D +0.2%"
- `computations/volume_binding_four_point.py:95`
- `computations/binding_link_volumes.py:168` — witness `notes` field
- `content/quantum-observable-universe/lean/QOU/MassComputationChainRoadmap.lean`

**2. `binding_per_bond_decomposition.py` computes a "METHOD DISCREPANCY" against the
stale constant.** It sets `dtr_canonical_2H = mpf("0.5952")` and reports the gap to its
own H_{3A}-direct value (0.424). That reported gap is measured against a number the
production function no longer produces, so the discrepancy figure is itself wrong —
a second-order error that will survive any fix that only touches prose.

**3. The open question is which Δtr is correct**, and that is a physics judgement:

- did `binding_canonical`'s Wenzl-bridge closed form change behaviour (a regression),
- or was 0.5952 always copied from a different trace convention (a mis-citation)?

`git log -S` on the constant plus a bisect of `binding_canonical` would settle it.

⚠ **Do NOT "fix" the −6.3% by reinstating 0.5952.** If `binding_canonical` is right
then +0.2% was never a real match and the honest reading is that the single-link
endomorphism fails at *every* A — which is a **cleaner** negative than the corpus
currently claims, not a dirtier one. There is then no special deuteron success needing
explanation, and `volume_binding_four_point.py`'s exclusion note (which already calls
the Hopf → Vol(𝓑₃) substitution "unjustified", 2026-08-07 ledger §6) becomes the
straightforwardly correct account.

## Done already

`binding_link_volumes.py`'s docstring now states −6.3%, cites the witness, and records
the trace above with a pointer to this bean. Its stdout is byte-identical to before
(verified by diff) — the docstring was the only thing wrong there.

---
**2026-08-15 (later) — RESOLVED as a diagnosis. It is not a regression, not a mis-citation,
and NOT a physics judgement. It is a convention change the owner already ruled on.**

I opened this bean saying the open question was "which Δtr is correct", and called that a
physics judgement someone else had to make. **That framing was wrong.** Traced:

| value | convention | status |
|---|---|---|
| `0.5952` | **C** — `z = 1/(√q + 1/√q) ≈ 0.4993203` | **EXCISED by owner ruling 2026-08-09** |
| `0.5566260326923999` | **D** — `z = q³/(q²+1) ≈ 0.6126880` | current, canonical |

Measured this session, at `q₀`: C = `0.49932033418369445241`, D = `0.61268803714646525160`
— matching the two docstrings exactly.

### The chain, verified rather than inferred

- `dtr_canonical_2H = mpf("0.5952")` entered on **2026-06-15** (`d27b002745`, a refactor —
  not a physics change), i.e. while the corpus was on convention C.
- `binding_canonical.py`'s own trace computation has **not changed since**: the diff
  `d27b002745..HEAD` on that file touches nothing matching
  `tr_M_free|tr_M_atom|use_closed_form|closed_form`. So the function did not regress.
- What changed is **underneath it**. `closed_form_tau_M.markov_z` now documents itself:
  *"OWNER RULING 2026-08-09: convention C excised. This returned C's `0.4993203` until
  then; it now returns D's `0.6126880`."*
- The selection is described as **FORCED, not stipulated** — `lem:feynman-eigenbasis-
  decomposition` gives `y_(1^3) = 0`, and the sorry-free
  `QOU.BraidsAndKnots.MarkovTraceTLUniqueness.markovWeights_eq_jones_of_threeRow_eq_zero`
  makes the faithful normalised Markov trace unique and equal to `q³/(q²+1)`.

**So there is nothing to adjudicate.** ⚠ Do NOT "restore" 0.5952 — that would reinstate an
excised convention against an owner ruling backed by a Lean uniqueness theorem.

### A dead end worth recording so nobody repeats it

I first tried to reproduce 0.5952 by rebinding `tr_M_element`'s default `z` to convention
C. **It changed nothing** — both runs gave 0.5566. The reason is that
`use_closed_form=True` does not go through `tr_M_element` at all; it routes via
`tr_M_via_wenzl_bridge_mpfr` / `closed_form_tau_M`. The `z` default that
`binding_canonical`'s docstring discusses governs the *symbolic* path only. An experiment
that "confirms" a convention by patching the wrong entry point will silently agree with
whatever it was going to say anyway.

### Relationship to `qou-wgta` (P0, open) — and that bean is STALE on this path

`qou-wgta` is the C→D excision campaign. Two of its enumerated items cover this code:

- **item 6** — "`binding_canonical.py` … registered C implementation, 62 consumers, never
  switched";
- **item 3** — "`y_lambda_wenzl_bridge.py` … HYBRID … the binding channel's production
  trace is interface=D, constituent=C", i.e. reproducible under neither convention.

**Item 3 is no longer true, verified here.** `y_lambda_wenzl_bridge.py` now opens *"This
module is **convention D**, z = q³/(q² + 1). It was convention C … in four places"*, and
both `markov_z` and `markov_z_numeric` return D. So the closed-form path is **pure D**
today, and today's `0.5566` is a consistent convention-D number rather than a hybrid
artefact. That materially changes what this bean is about: it is stale *prose*, not a
wrong *number*.

**`qou-wgta` is a sibling's bean and is left untouched** — someone owning it should
re-audit its item list, since at least item 3 has been closed without the bean being
updated.

### What this bean is now: mechanical, and its own registry rule names the defect

`docs/coordination/trace-convention-registry.md` states the rule this violates:

> Any τ / tr_M value quoted below 0.1 % precision, and any cross-method comparison of
> trace values, must name its convention id from this registry with the script or Lean
> decl cited. **Convention-silent trace values are not comparable.**

Every one of the seven `+0.2%` sites is convention-silent, and two are worse than silent:

1. `binding_per_bond_decomposition.py:126` hardcodes `dtr_canonical_2H = mpf("0.5952")`
   and computes a printed **"METHOD DISCREPANCY"** percentage from it against a *live*
   H_{3A} value. So the headline gap that script reports is measured against an excised
   convention — a second-order error that survives any prose-only fix.
2. `binding_link_volumes.py` — already corrected (see bean `qou-bind`).

Remaining sites quoting `+0.2%`: `binding_error_source.py:11,105`,
`binding_multibond_wenzl.py:9`, `probe_volume_wedderburn_delta_lambda.py:126`,
`volume_binding_four_point.py:95`, `MassComputationChainRoadmap.lean`.

**Fix shape:** replace the hardcode with a *live* call to `binding_canonical` so it cannot
go stale again, and name the convention at each quoted value per the registry rule. No
number needs to be chosen; it needs to be computed and labelled.

---
**2026-08-15 — FIXED, all six sites. One verification is still in flight and is named below.**

| site | change | kind |
|---|---|---|
| `binding_link_volumes.py` | docstring → −6.3%, cites witness | done under `qou-bind` |
| `binding_per_bond_decomposition.py:126` | **hardcode → live call** | code |
| `binding_error_source.py:11,105` | → −6.3%, convention named | comment |
| `binding_multibond_wenzl.py:9` | → −6.3%, convention named | comment |
| `probe_volume_wedderburn_delta_lambda.py:126` | → −6.3%/−56% | comment |
| `volume_binding_four_point.py:95` | exclusion note strengthened | comment |

The one **code** change replaces `dtr_canonical_2H = mpf("0.5952")` with a live
`binding_canonical(1, 1, use_closed_form=True)`. Computing rather than substituting is
the point: a hardcoded trace value cannot track a convention change, which is exactly how
this went wrong. Measured live: `0.5566260326923999`.

**This one changes output**, unlike the `qou-bind` fix which was byte-identical. The
printed METHOD DISCREPANCY moves from ~29 % to ~24 % against the documented H_{3A} value
0.424. That is the correction landing, not a side effect — the old gap was measured
against an excised convention.

### What survives, checked site by site rather than assumed

The corrections are to *numbers*, and at every site the surrounding *argument* holds:

- **`binding_error_source`** — its FINDING (Δtr intensive and saturating, binding
  extensive) is untouched. −6.3 % at A=2 against −59 %/−88 % at A≥3 shows the same ceiling
  behaviour +0.2 % did. What is lost is the claim the deuteron *works*. That is a
  **cleaner** reading: there is no special A=2 success needing separate explanation.
- **`binding_multibond_wenzl`** — the A-flatness argument is untouched; its hypothesis was
  motivated by the combined Δtr being A-independent, not by the deuteron matching.
- **`volume_binding_four_point`** — its exclusion is now **better** founded than when
  written: no deuteron success to exclude, only a near-miss.

### ⚠ A near-miss worth recording: one grep hit was a false positive

`MassComputationChainRoadmap.lean` matches `0.2%`, but it is
`betaDecayRecovery_at_N0_within_0_2_percent` — a **β-decay recovery tolerance**, nothing to
do with the deuteron Δtr. Sweeping it would have corrupted an unrelated Lean claim. The
seven-file count in this bean's header was therefore **six**; a grep across a corpus that
reuses a number is a candidate list, not a work list.

### Verified

- New code path executed in isolation inside the module's own import environment: returns
  `0.5566260326923999`, gap arithmetic intact.
- All four comment-only files parse (`ast.parse`).
- `probe-float64-guard.py --diff` with files passed explicitly: **33 hits across the four,
  identical to HEAD** (verified by stashing). A first attempt at the code fix passed
  `float(Q_BETA_MEV)` and added one hit; replaced by passing the `mpf` through, since
  `binding_canonical` stringifies it anyway.

### ⚠ NOT verified

**A full end-to-end run of `binding_per_bond_decomposition.py` has not completed.** It
takes > 40 min (H_{3A} Wedderburn sums) and a baseline run started before the edit was
still going when this was written. The isolated path is what is verified. Whoever next
touches this file should run it once and confirm the printed gap and the witness.

Witness deliberately **not** regenerated, same reason as `qou-bind`: this container's
python is weaker than the one that produced the committed witnesses (mpmath 1.3.0 vs
1.4.1, no scipy, no pyhecke_native).

### Still open, and it belongs to someone else

`qou-wgta` (P0) is the corpus-wide C→D sweep and is **still `todo`** with 174 py + 61 lean
files enumerated. This bean fixed only the six deuteron-Δtr sites. That bean is a
sibling's, untouched — but its **item 3 is stale** (the `y_lambda_wenzl_bridge` hybrid it
describes is now pure D, verified here), so whoever owns it should re-audit its list before
working from it.

---
**2026-08-15 — the verification loose end is CLOSED, by testing the change instead of the
pipeline.**

The three previous entries all ended "a full end-to-end run of
`binding_per_bond_decomposition.py` has not completed". It still has not, after **three**
attempts, each dying at the same place: the `³H` H_{3A} Wedderburn sum, immediately after
the `2H` row. Not a resource problem — 16 GB total with 15 GB free and no cgroup limit —
and the corpus's own note in `binding_canonical.py` says the A=3 aggregate runs
"~5000–12000 sympy ops" with `simplify` exceeding 30 minutes. It is simply longer than the
window available to it.

**Chasing a fourth run was the wrong move, and the right one was to test what changed.**
The edited region needs exactly **one** value from the expensive computation —
`results["2H"]["delta_tr"]` — and the partial runs measured it: `0.424083`. So the tail was
executed verbatim against that real input:

```
METHOD DISCREPANCY (2H): binding_canonical Δtr = 0.5566  [trace convention D, computed live]
  vs H_3A-direct Δtr = 0.4241  (24% gap)

OLD behaviour (hardcoded convention-C 0.5952) would have printed:
  binding_canonical Δtr = 0.5952   gap = 29%
```

Tail executed without error; the `wb.add_data` call populated. **This confirms the
prediction made when the fix landed** — "the printed gap moves from ~29 % to ~24 %" — with
the exact real H_{3A} value rather than the documented approximation `0.424` I used then.

**Why this is not a weaker check than the full run.** The full run would exercise the same
lines with the same inputs, plus forty minutes of H_{3A} arithmetic that the change does not
touch and that three runs have already reproduced identically at `2H`. Targeting the changed
code with a measured input tests the thing that changed; the pipeline run would mostly test
sympy.

**Residual, stated honestly:** nothing verifies that the `³H`/`³He` branches still populate
`results` correctly — but the change does not touch them, and they were already producing
output before the fix (`-28.6%` at `2H` printed identically pre- and post-edit).

Bean scope is now complete: diagnosis (convention C excision, owner-ruled), the code fix
(hardcode → live), five prose corrections, and verification. Setting **completed**.

The corpus-wide C→D sweep remains `qou-wgta`'s, which is a sibling's bean and untouched —
noting again that its **item 3 is stale** (`y_lambda_wenzl_bridge` is pure D now, verified
here), so its list wants re-auditing before anyone works from it.
