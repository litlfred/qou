# Which witnesses PR #5517 actually moves — attributed, not assumed

**Date** 2026-08-23 · **Beans** `qou-z36p`, `qou-b3l8` · **PRs** #5545 (stacked on #5517)

PR #5517 makes `char_fast._compiled_sigmas` a genuine function of `q` and
refreshes two witnesses. This audit asks the question the PR leaves open: of
everything downstream of that call, what else moves, and for each move, is
#5517 the cause?

The distinction matters because two of the candidate witnesses move for
reasons that have nothing to do with #5517, and one of those moves is
**four orders larger** than anything #5517 could produce. Refreshing them
inside a precision PR would have smuggled a substantive change past a
reviewer reading the diff as round-off.

## Method

Three-way, one venv, one machine:

| leg | tree |
|---|---|
| **committed** | the blob in git |
| **before** | fresh run at #5517's branch point, `9e85a43628` |
| **after** | fresh run at #5517's head, `ed36cf64c1` |

Both fresh legs run in their own detached worktree, `git checkout -- computations qou-mass`
+ `git clean` **before and after every run** — producers write sibling
witnesses, so a single-file check leaves a dirty tree that reads as real work.

`origin/main`'s tip is the wrong "before" and was not used: main has moved five
commits past the branch point and two of them touch adjacent compute (#5510's
mpf scoping, the `A_operator_per_interface_probe` p/n fix). The branch point
isolates #5517's five commits and nothing else.

A first attempt at this measurement (previous session, container reclaimed
before anything was committed) compared a "main" run that had in fact been
produced with branch code. That comparison returned `0.0` and looked like a
clean negative. It was vacuous. Hence the worktrees.

## 0. A blocker: the extract producer cannot finish a run

`sublemma_2_1_A_operator_extract.py` raises

```
TypeError: unsupported format string passed to mpf.__format__
```

on its own per-λ progress line and dies **before the witness is written**, so
the committed witness could not be regenerated at all — on `main`, at the
branch point, or on #5517's head.

The line predates the float64 port and was correct then: `max_rel` was a Python
float. The port (`416285fc17`, bean `qou-zck8`) made it an `mpf` — mpmath
implements no `__format__` for the `e` presentation type — and left
`{max_rel:>10.2e}` in place. The committed witness is stamped `09:34:59`,
**seven minutes before that commit**, which is how it reached `main` unnoticed.

Fixed with `mp.nstr` (a display conversion, inside what the NO-FLOAT64
directive permits in an f-string). It moves no number: with the fix applied at
the branch point, all eleven committed `max_relative_residual` values reproduce
**exactly**.

## 1. `sublemma-2-1-A-operator-extract` — #5517 is the cause; the move is a correction

| λ ⊢ 6 | rank | committed | before | after |
|---|---|---|---|---|
| (6,) | 1 | 1.46e-71 | 1.46e-71 | 1.46e-71 |
| (5,1) | 9 | 2.87e-16 | 2.87e-16 | **3.11e-71** |
| (4,2) | 25 | 1.24e-15 | 1.24e-15 | **5.33e-71** |
| (4,1,1) | 26 | 1.08e-15 | 1.08e-15 | **4.58e-71** |
| (3,3) | 17 | 1.20e-15 | 1.20e-15 | **3.14e-71** |
| (3,2,1) | 32 | 1.48e-15 | 1.48e-15 | **1.01e-70** |
| (3,1,1,1) | 26 | 9.61e-16 | 9.61e-16 | **4.84e-71** |
| (2,2,2) | 17 | 1.18e-15 | 1.18e-15 | **4.42e-71** |
| (2,2,1,1) | 25 | 1.69e-15 | 1.69e-15 | **5.52e-71** |
| (2,1,1,1,1) | 9 | 3.04e-16 | 3.04e-16 | **3.74e-71** |
| (1,1,1,1,1,1) | 1 | 2.14e-71 | 2.14e-71 | 2.14e-71 |

*committed = before* on every row, so there is no staleness confounding the
attribution.

**The control is the two rows that do not move.** λ = (6,) and (1⁶) are the
trivial and sign irreps: every σᵢ acts as a scalar, so no rep matrix ever
entered, so a defect in the rep could not have touched them — and did not.
They were already at ~1e-71 before. Every `rank > 1` row was pinned at the
float64 floor and drops ~55 orders. That pattern is what distinguishes a
correction from a different answer.

**Nothing structural moved:** 16 scalar / 19 operator blocks, 11 of 11
consistent, identical per-λ scalar-consistency list.

**Worst entry move, relative to its own block's scale: 1.508e-15** — λ=(4,2),
on an entry of size 0.128. The float64 floor.

One entry moves by 100 % of itself, `-3.153e-21 → 1.447e-72`. That figure means
nothing: it is a structural zero, and the "after" value is the better one.
Quoting entry-relative error there would invert the verdict, which is why the
number above is scale-relative.

### The witness was carrying a note that #5517 falsified

Both the witness and `evaluate_word_matrix.__doc__` carried a prominent
ACCURACY CEILING section telling readers that no digit past the 16th means
anything, and naming its cause — `_cached_seminormal` substituting q at build
time — with the remark that *"no amount of mpmath in THIS file can lower it"*
and that the upstream trap is *"deliberately NOT fixed here."* #5517 fixed it
upstream. Left standing, that note would instruct every future reader to
discard 55 orders of now-genuine precision.

Measured on `evaluate_word_matrix` directly — shape (3,2,1), the five-generator
word, dps 70 — perturbing `Q0` at the k-th digit and reading the largest
relative change in the returned matrix:

| digit perturbed | before | after |
|---|---|---|
| 16 | **0.0** | 2.1e-16 |
| 30 | **0.0** | 2.1e-30 |
| 45 | **0.0** | 2.1e-45 |
| 60 | **0.0** | 2.1e-60 |

Exactly zero at every depth before; linear response at every depth after. So
`accuracy_ceiling_relative` moves `~1e-16 → ~1e-50` — the depth of the
`Q_50_DIGIT_STR` literal, not of the rep. The old text is preserved in a new
`accuracy_ceiling_history` field so the change is legible rather than silent.

**What that figure is not.** It is internal consistency at a given q₀ literal.
The physical q₀ is pinned by a CODATA ratio and is known to nothing like 50
digits; digits past that describe the model evaluated at that literal, not the
world.

## 2. `sublemma-2-1-alpha-shift-extract` — not #5517, and deliberately left alone

The committed witness differs from a fresh run by **1.745e-7** on
`alpha_shift.value_re`. The cause is in the parameters block:

```
committed  q_0 = 1.1099785955541805   (muon)
fresh      q_0 = 1.1099785827513808   (proton, q_parameter.Q)
                             rel = 1.153e-8   (11.53 ppb)
```

The producer reads `from q_parameter import Q as Q0`, so **any** regeneration
silently re-pins it. The same 1.745e-7 appears at the branch point and at the
head, so #5517 is not the cause.

#5517's own effect here is **7.34e-14** — and this producer is float64
throughout (`chi_lambda_fast`, not the `_mp` variant), so at its own resolution
that is round-off, not an accuracy claim in either direction.

Second, independent defect: a fresh run **drops four provenance fields** the
committed witness carries — `scriptFile`, `commitSha`, `engine`, `auditOnly`.
This is the bare-producer class AGENTS.md warns about, where re-running deletes
the very fields an audit keys on. Fix the producer to emit provenance *before*
anyone regenerates this witness.

Both are recorded as `qou-b3l8`. Neither belongs in a precision PR.

## 3. `sublemma-2-1-h9-tritium-verify` — #5517's own claim, independently reproduced

| comparison | worst substantive difference |
|---|---|
| committed@branch-point vs fresh@branch-point | none — only `durationMs`, 23 → 37 ms |
| fresh@branch-point vs committed@PR-head | `h6_extract_frame_guard_max_rel` **5.513e-15 → 9.772e-16** |
| running the producer on #5517's head | wrote **nothing** — the shipped witness reproduces |

So the pre-PR witness was exactly reproducible, #5517's stated tritium move is
the only substantive change, and the refreshed value is itself reproducible.

**No undisclosed sibling writes.** `sublemma_2_1_h9_tritium_verify.py` mentions
`sublemma-2-1-A-operator-extract-h9-{nn,pn}.witness.json` in its source, but a
full run touches neither — those are reads.

## 4. Scope of what is still unmeasured

22 modules import `char_fast` directly. **Eight of them write a witness** —
not twelve, which is what a first pass of this audit reported and what an
earlier revision of this section said.

> **Correction.** The twelve came from regexing `*.witness.json` string
> literals out of each module and treating every hit as an output. Four of the
> twelve only *read* those files: `canonical_tr_m_via_branching`,
> `chi_atom_fmatrix_recoupling`, `chi_monotone_transfer`, and
> `probes/delta_lambda_master_formula_h3_probe`. The same conflation ran the
> other way too — `nuclide_braid_pipeline` and
> `probes/qbeta_operator_identification_probe` both name
> `q-pinning-50-digit.witness.json`, which is the **anchor-defining** witness
> AGENTS.md forbids re-pinning, and both merely **read** it. There is no
> anchor-rewrite hazard here; checking the call sites is what established
> that, and the filename grep alone would have reported one.
>
> A second instance, same class: `chi-deuteron-h6-at-q0-50dps.witness.json`
> was flagged as a likely mover on the reasoning that #5517's own evidence
> calls the 50-digit deuteron χ "34 digits of noise". Its actual producer is
> `chi_at_q0_via_hoefsmit_mpfr.py`, which reaches `tr_m_wenzl_bridge_mpfr` and
> `pyhecke_native` and **never touches `char_fast`** — it imports
> `mass_at_3A_proper` only for `atom_braid_word_3A`, the braid word, not the
> rep. #5517 cannot move it. The prediction was refuted before it cost a run.

The eight writers, with what each actually emits:

| module | writes | status |
|---|---|---|
| `sublemma_2_1_deuteron_branching` | `sublemma-2-1-deuteron-branching` | refreshed by #5517 |
| `sublemma_2_1_h9_tritium_verify` | `sublemma-2-1-h9-tritium-verify` | refreshed by #5517; reproduced in §3 |
| `sublemma_2_1_A_operator_extract` | `sublemma-2-1-A-operator-extract` | refreshed here (§1) |
| `sublemma_2_1_alpha_shift_extract` | `sublemma-2-1-alpha-shift-extract` | deliberately not — §2, `qou-b3l8` |
| `sublemma_2_1_h12_he4_phase25` | `he4-canonical-tr-m-block-fingerprint` | measuring |
| `nuclide_braid_pipeline` | `nuclide-braid-<sym>` | **unmeasured** |
| `probes/poly_q_proof_probe` | `poly-q-proof` | **unmeasured** |
| `probes/qbeta_operator_identification_probe` | `qbeta-operator-identification-probe` | **unmeasured** |

So the open set is three witnesses plus the H12 one, not nine. None of the four
is claimed either way here.

The transitive import cone is not a useful scoping tool for this question:
`computations/` uses a flat namespace, so 572 modules and 201 witness-writers
reach `char_fast` through *some* path. Direct importers that evaluate the rep
are the actionable set — and "evaluate", not "mention", is the operative word,
which is the whole content of the correction above.
