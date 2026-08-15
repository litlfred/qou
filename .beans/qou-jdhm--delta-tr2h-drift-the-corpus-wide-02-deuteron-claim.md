---
# qou-jdhm
title: 'Delta-tr(2H) drift: the corpus-wide +0.2% deuteron claim needs 0.5952, binding_canonical returns 0.5566'
status: todo
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
