# Color-weighting coverage audit + flavor-split closed-form probe (2026-06-29)

**Branch:** `claude/color-weighting-flavor-split-audit-2026-06-29`
**Follows:** the L1 peel float64 fix (PR #3084) — the cross-check now certifies
the color-weighted trace at 1 ppQ, which motivated verifying the
color-weighting is applied *consistently* everywhere it should be.

## Part A — color-weighting `h(½ − δ/4)` coverage (option 2)

**Question.** Is the canonical color-weighted p-n crossing
`σ − h·(½ − δ/4)·𝟙`, with δ = `flavor_split_subleading(q)`, applied
consistently across compute — same δ, same coefficient — everywhere the p-n
bridge appears?

**Method.** Grep + per-consumer inspection of the ~23 non-deprecated files
that reference `flavor_split_subleading` / the `½ − δ/4` crossing weight.

**Result — CONSISTENT. No gaps found.**

| Check | Finding |
|---|---|
| δ source | `flavor_split_subleading(q)` in every consumer — `closed_form_tau_M.py:281`, `chi_cd_mpfr.py:70`, `chi_monotone_transfer.py`, `markov_peel.py` (symbolic mirror), the binding probes. |
| `flavor_split_leading` usage | ONLY inside `_li_2_q_util.py`, to *build* `subleading = leading·(1+ℏ_q³)`. No consumer uses leading-only as the color-weighting. |
| crossing coefficient | `½ − δ/4` uniform across production + probes (`z − h(½−δ/4)` for the binding factor; `σ − h(½−δ/4)·𝟙` for the Hecke crossing). |
| L1 cross-check | markov_peel and chi-cache (the two independent color-weighted implementations) agree at ~1e-50 post-#3084 — direct proof they use the *same* δ to 50 dps. |
| apparent sign anomaly | `derived_bond_graph_binding.py:104` `f_bar["pn"] = z + h(½−δ/4)` is the **intentional bar-conjugate** `f̄` of `f["pn"] = z − h(½−δ/4)` (archimedean bar-norm `tr_M·tr̄_M`, per the line-98 comment) — NOT a sign bug. |

The color-blind legs (Hoefsmit, Habiro) correctly *omit* the weighting and
diverge ~1.8e-4 at A≥2 by construction (handled as informational in both
`cross_check_trM_1ppb.py` and, post-#3084, the peel producer's bridge check).

## Part B — is `(1+ℏ_q³)` a series? does inverting close Δm_pn? (option 3)

**Question.** `(1+ℏ_q³)` is exactly the first two terms of the geometric
series `1/(1−ℏ_q³) = 1 + ℏ_q³ + ℏ_q⁶ + …`. Is the denominator a series, and
does the closed form `leading/(1−ℏ_q³)` close the Δm_pn gap?

**Probe:** `computations/probes/flavor_split_geometric_closure_probe.py`
(witness `flavor-split-geometric-closure-probe.witness.json`).

| form | δ = Δm_pn/M_N | err vs CODATA |
|---|---|---|
| `leading` = (q−1)²(1−q⁻⁴)/3 | 0.0013757112 | 0.128% |
| `leading·(1+ℏ_q³)` (canonical) | 0.0013770494 | **0.0305%** |
| `leading/(1−ℏ_q³)` (closed-form hypothesis) | 0.0013770507 | 0.0304% |
| CODATA Δm_pn/M_N | 0.0013774699 | — |

**Findings (scope-(a) — numerical, not a structural exclusion):**

1. **The subleading correction is real and material:** `(1+ℏ_q³)` cuts the
   error ~4× (0.128% → 0.0305%) vs leading-only.
2. **The geometric closed form does NOT close Δm_pn.** `1/(1−ℏ_q³)` differs
   from `(1+ℏ_q³)` only at O(ℏ_q⁶) ≈ 9.5e-7 (rel 9.5e-7), a sub-ppm nudge —
   the residual to CODATA stays ~0.03%, ~300× larger. The missing physics is
   not in the denominator's higher geometric terms.
3. **The closed form is a HYPOTHESIS, not a derived identity.** The
   derivation frames `(1+ℏ_q³)` as a specific *"3-loop substrate-Planck"*
   correction (`flavor_split_subleading` docstring), not as a geometric
   series. Treating it as `1/(1−ℏ_q³)` without an independent derivation that
   the correction is geometric is exactly the clean-looking-formula move the
   three-calibration discipline flags. **NOT wired to production δ.**

## Part C — `(1 + ℏ_q³)` is an UNPROVEN production factor (flag)

The L1 fix (#3084) made this visible: peel and chi-cache now agree at ~1e-50
on a color-weighting δ that *includes* the `(1 + ℏ_q³)` subleading factor. So
the factor is now baked, to 50 dps, into every production color-weighting
consumer (`closed_form_tau_M`, `markov_peel`, `chi_cd_mpfr`, the binding
probes — all via `flavor_split_subleading`). **Yet it has no derivation.**

Corpus-grep status (per AGENTS.md "Before declaring open/unproved"):

| where a derivation would live | found? |
|---|---|
| compute docstring | only a **label** — `_li_2_q_util.py:165`: *"(1+ℏ_q³) 3-loop substrate-Planck correction"* |
| content block (`flavor-split-substrate.md`) | **no** — documents only the *leading* `(q−1)²(1−q⁻⁴)/3` |
| Lean | **no** proof of the subleading factor |
| witness | **no** witness derives `(1+ℏ_q³)`; they only *consume* `flavor_split_subleading` |

**Assessment.** The leading term `(q−1)²(1−q⁻⁴)/3` is derived (physical
accounting in the content block). The `(1 + ℏ_q³)` multiplier is **posited**,
not derived — its sole justification is the docstring phrase "3-loop
substrate-Planck." It improves the Δm_pn match ~4× (0.128% → 0.0305%), which
is suggestive but is also exactly the signature of an underived `h^k`
shape-fix that the production-vs-exploratory discipline exists to catch
(cf. AGENTS.md §production-vs-exploratory: "where does this h^k come from").

**This is a (a)-scope flag, not a refutation:** the factor may well be
correct; the point is it is *unproven and unlabelled* while living in
production at 50-dps precision. Required disposition (one of):

1. **Derive it** — a content block / Lean lemma showing the substrate-Planck
   correction is `(1 + ℏ_q³)` (and whether the series continues — see Part B's
   geometric `1/(1−ℏ_q³)` hypothesis, which is the natural next question
   *only if* the factor is shown to be geometric).
2. **Label it** — mark `flavor_split_subleading` as `posited` / `fitted` (not
   `canonical`) per the production-vs-exploratory tiering, so downstream
   consumers and the canonical-watcher see it is an unproven correction.

Until one of these is done, `(1 + ℏ_q³)` should not be cited as a derived
result.

## Recommendations (follow-ups, not done here)

- **Doc-currency gap (owner-review):** the content block
  [`observations/flavor-split-substrate.md`](../../content/quantum-observable-universe/observations/flavor-split-substrate.md)
  documents only the *leading* `(q−1)²(1−q⁻⁴)/3`; the `(1+ℏ_q³)` subleading —
  which is what every compute consumer actually uses and which is 4× more
  accurate — is undocumented in the canonical content. Documenting it (with
  the honest "3-loop substrate-Planck, not yet a rigorous derivation"
  framing) is a content change to a calibration-sensitive block and is left
  for owner review rather than edited unilaterally here.
- **If the geometric closed form is ever pursued:** formalize-first — derive
  that the substrate-Planck correction is geometric *before* swapping
  `(1+ℏ_q³)` → `1/(1−ℏ_q³)`; the ℏ_q⁶ payoff is sub-ppm and does not justify
  a calibration-sensitive change on its own.

## Reproduce

```bash
python3 computations/probes/flavor_split_geometric_closure_probe.py
```
