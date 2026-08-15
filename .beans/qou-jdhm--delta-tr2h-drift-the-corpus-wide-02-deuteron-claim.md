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
