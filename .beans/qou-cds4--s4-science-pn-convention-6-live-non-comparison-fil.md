---
# qou-cds4
title: 'S4 (SCIENCE): p/n convention — 6 live non-comparison files + 28 witnesses off bring_color_weighted'
status: in-progress
type: task
priority: normal
created_at: 2026-08-15T00:00:00Z
updated_at: 2026-08-21T17:01:20Z
---

Parent: `qou-cdx1`. Ruling R3: `pn_convention="bring_color_weighted"` is
canonical.

## Measured 2026-08-15 (live Python assignments, excluding `_deprecated/`)

| value | assignment sites |
|---|---|
| **`bring_color_weighted`** (canonical) | **16** |
| `chi_lambda_braid` | **9** |
| `strict_averaged` | **6** |

83 files mention `pn_convention` overall (`.py`+`.json`+`.md`).
**28 committed witnesses** record a non-colour-weighted `pn_convention`.

## R3 is largely already true

`bring_color_weighted` is already the default in the production path:
`closed_form_tau_M.py` (×4) and `mass_at_3A_proper.py`. R3 makes it canonical
and puts the alternatives on notice.

## The 8 live Python files off-canon

```
computations/_habiro_coefficient_extract.py
computations/atomic_tr_m_helium4_canonical.py
computations/binding_bring_enhancement_compare.py      <- name says comparison
computations/binding_canonical.py                      <- READ THIS FIRST
computations/binding_combiner_markov_peel_fallback.py  <- PN_CONVENTION = "strict_averaged"
computations/chi_monotone_transfer.py
computations/closed_form_tau_M_verification_phase5q.py
computations/iterative_knot_builder.py
```

**`binding_canonical.py` first.** A file with `canonical` in its name assigning a
non-canonical p/n convention is either a naming defect or a real one, and the
two need different fixes.

`*_compare` and `*_fallback` are plausibly legitimate under R3 — a **labelled**
comparison against a non-canonical convention is fine. Confirm the label exists;
do not assume it from the filename.

## Why SCIENCE and not hygiene

`chi_lambda_braid` vs `strict_averaged` vs `bring_color_weighted` is the p/n
interface factor — the Bring colour-weighted asymmetry. Switching it moves
binding numbers. This is not a rename.

---

## TRIAGE DONE 2026-08-21 — none of the 8 is a silent drift; 2 labels were wrong

Read all eight, resolving control flow rather than grepping assignments. **Every
one passes `pn_convention` EXPLICITLY** — there is no file picking up a
convention from a default it does not name. So the risk this bean was framed
around ("28 witnesses off canon") is not a drift risk; it is a labelling and
authorisation question.

| file | explicit? | label | verdict |
|---|---|---|---|
| `binding_canonical` | yes | yes, line 211 | **NOT a defect** — see below |
| `binding_bring_enhancement_compare` | yes | yes — canonical vs historical baseline | legitimate |
| `binding_combiner_markov_peel_fallback` | yes | yes — **structural** | legitimate |
| `closed_form_tau_M_verification_phase5q` | yes ×3 | it *is* the Phase-5q verification | legitimate |
| `iterative_knot_builder` | yes | yes — structural | legitimate |
| `_habiro_coefficient_extract` | yes | calls `chi_lambda_braid` *"the production convention"* | **label stale under R3** |
| `atomic_tr_m_helium4_canonical` | yes + witness declares | called it **"the default"** — false | **FIXED, see below** |
| `chi_monotone_transfer` | yes | **none at the call site** | **unlabelled** |

### `binding_canonical.py` — the bean's first item, and it is clean

*"A file with `canonical` in its name assigning a non-canonical p/n convention is
either a naming defect or a real one."* It is **neither**. The
`pn_convention="strict_averaged"` at line 290 sits inside `if use_closed_form:`
(line 254), and the signature is `use_closed_form: bool = False` — so the
**default path is the canonical transfer path**, and the off-canon branch is
reached only when a caller opts in. Line 211 labels that branch exactly:
*"`use_closed_form=True` still takes precedence: it is the strict_averaged-
convention path retained for that family of callers (`mass_table_comprehensive`,
`binding_factor_f_*`, …)"*, and the opt-in callers are enumerable and match:
`binding_factor_f_sequence`, `binding_link_volumes`,
`binding_shell_enhancement_derivation`, and two probes.

The suspicion was reasonable from a grep and does not survive reading the
control flow.

### `atomic_tr_m_helium4_canonical.py` — a real latent trap, now fixed

Two prose references described `chi_lambda_braid` as **"the default"**. It is
not: `closed_form_tau_M`'s default is `bring_color_weighted` at all four sites
(`closed_form_tau_M.py:245,344,392,495`), which R3 makes canonical.

The computation itself was never wrong — the file passes the convention
explicitly (`:117`, `:123`) and **declares it in the witness** (`:154`), which is
the right hygiene. The hazard was latent: a reader told the argument merely
restates the default would delete it as redundant, silently switching this file
to `bring_color_weighted` and **invalidating the 1e-49 Phase-5q agreement the
docstring cites**, which was measured under `chi_lambda_braid`.

Corrected both references, and recorded at the call site that the explicit
argument is **load-bearing**. No number moved. This is the campaign's recurring
shape once more — *a description that outlived the thing it describes* — and the
only reason it was harmless so far is that the author passed the argument anyway.

### `binding_combiner_markov_peel_fallback.py` — worth quoting, it is the good case

Its justification is structural, not preferential: the canonical crossing
`σ − h·(½ − δ/4)·1` carries `δ = flavor_split_leading(q₀)`, a *numeric* function
of q₀, and *"a numeric δ cannot be represented as an exact polynomial in the
formal symbol q, so the exact-symbolic trace path can only carry the color-blind
averaged crossing"*. That is a reason R3 cannot overrule — the exact-symbolic
route is not *choosing* a convention, it is reporting the only one it can
represent.

### What is actually left for this bean

1. **`chi_monotone_transfer.py`** — the one unlabelled site. Needs a one-line
   justification or a migration; not guessable from the call site.
2. **`_habiro_coefficient_extract.py`** — calls `chi_lambda_braid` *"the
   production convention"*, which R3 superseded. Label-only.
3. **The 28 witnesses** recording a non-colour-weighted `pn_convention` — untouched
   here. Now that the producers are known to be explicit and mostly labelled, the
   witness question is "which of these were produced by a legitimately off-canon
   route", and the answer is per-producer, above.

**Not attempted:** migrating any of them. R3 makes `bring_color_weighted`
canonical, and this bean says correctly that switching it *moves binding
numbers* — that is science and needs its own authorisation, not a hygiene sweep.
