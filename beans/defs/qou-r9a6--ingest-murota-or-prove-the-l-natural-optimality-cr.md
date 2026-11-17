---
# qou-r9a6
title: 'Ingest Murota (or prove the L-natural optimality criterion): the Xbot arc''s one load-bearing citation resolves to nothing in the corpus'
status: in-progress
type: task
priority: normal
created_at: 2026-10-11T08:35:32Z
updated_at: 2026-11-17T23:08:23Z
parent: qou-3e6w
---

The `Xbot` L♮ route — which certified `e_inf` without G1 and closed `qou-as81` — rests on
**Murota, *Discrete Convex Analysis* (SIAM 2003), Ch. 7: the L♮ optimality criterion**, that for
an L♮-concave `g : ℤ^n → ℝ ∪ {−∞}` a domain point is a *global* maximiser iff no `±χ_S` move
improves it.

That theorem is what turns `rev_e_infinity_xbot_lnatural_probe.py`'s M5 steepest-ascent fixed
point into **the** integer maximum. Without it M5 certifies a local optimum and nothing more. It
is therefore load-bearing for:

- the G1-free cut of **25** (M6),
- `e_inf` certified without G1 (the join probe, 4/4),
- the close of bean `qou-as81`.

## The corpus cannot check it

Measured on `main` after the 335 commits that landed on 2026-10-10/11: **0 hits** for *Murota* /
*discrete convex analysis* in `library/INDEX.md`, across **60,059** library files. A six-path
corpus-grep the day before — `library/INDEX.md`, `library/*/sections/`, **`library/*/ocr/`** (the
fourth tier the documented path misses), `beans/`, `content/`, `folio/`, `computations/`,
`docs/` — returned one unrelated hit (`s00453-026-01372-w`, Algorithmica 2026, concentration of
submodular functions). So the citation resolves to nothing a reader or a later agent can open.

**This is not a defect in the probe.** Citing a standard published theorem is legitimate. What
is recorded here is that the corpus holds no copy, so nothing in the repository can verify the
step, and a referee asking "where is the criterion?" has no in-repo answer.

## The companion result is already closed, which is why this one stands out

Murota §7.1 — the *sufficient condition*, that separable concave plus concave functions of
pairwise differences is L♮-concave — was the probe's other citation and **no longer needs one**:
`QOU/BraidKnot/LNaturalConcaveForm.lean` proves it (8 theorems, sorry-free), via
`concave_exchange_inward` for the separable part and `parity_spread` for the differences. So the
arc is one theorem away from citation-independence, and it is a specific, named one.

## Two ways to close it, with costs

1. **Ingest Murota** (`uploads/` → `library/<doc-id>/`). Cheapest by far, makes the citation
   resolvable, and pays off beyond this arc — discrete convex analysis is the right frame for
   any integer-programming structure in the corpus. Does **not** make the step machine-checked.
2. **Prove the criterion.** For the `±χ_S` direction the standard route is: L♮-concavity gives
   that the "steepest" move is an s-t min cut because the `χ_S` gain is a supermodular set
   function (the probe's M4 already verifies the min-cut move against brute force over all `2^n`
   subsets, both signs — so the *implementation* is checked, just not the criterion). Expensive,
   and the right scope is a Lean file beside `LNaturalConcaveForm.lean`.

**Recommendation (judgement, not a finding): do (1) now and treat (2) as optional.** The
mathematics is not in doubt; what is missing is that the repository cannot show its own work on
a load-bearing step of a closed arc.

## Default if nothing is done

`qou-as81` stays correctly closed, the cut of 25 stays correct, and the arc keeps one unresolvable
citation. Nothing breaks — this is about auditability, not correctness.

## 2026-10-12 — option (2) DONE, and it was cheap: the criterion needs only midpoint concavity

(Stream 4 of #7735, session_01PmZzY27QHceKGXwNivRt64; owner "go" on #7579, which merged.)

**The comparison, after measuring.** This bean costed (2) as "expensive" because it routed through
min-cut / supermodularity. That route is not needed. The local ⟹ global direction follows from
**discrete midpoint concavity alone** — the property `LNaturalConcaveForm` already proves for the
arc's objective — by a two-step argument:

- **distance one:** if `y − x ∈ {−1,0,1}ⁿ`, the midpoints are exactly `x + χ_S` and `x − χ_T`
  (`S = {y > x}`, `T = {y < x}`), so midpoint concavity + no improving `±χ` move gives `g y ≤ g x`;
- **halving:** if `‖y − x‖_∞ ≤ d`, `d ≥ 2`, both midpoints are within `d − 1`; strong induction.

`QOU/BraidKnot/LNaturalOptimality.lean`, theorem `global_of_local`: sorry-free,
`lean -DautoImplicit=false -s 65536` exit 0, axioms `[propext, Classical.choice, Quot.sound]`.
Generic over any domain `D ⊆ ℤ^ι` and values in any linearly ordered cancellative additive monoid.

| | (1) ingest Murota | (2) prove it — **done** |
|---|---|---|
| cost | needs a copy of a copyrighted SIAM monograph; only the owner can upload it | ~150 lines, one session |
| machine-checked | no | yes, for the local⟹global direction |
| covers | the whole of Ch. 7 | exactly the step M5 uses |

**Recommendation (judgement):** (1) is now optional — worth doing for the wider library, no longer
needed for this arc.

**What stays a non-Lean link (do not compress this).** The bridge to the Python objective `G` is
unchanged: midpoint concavity of `G` rests on `LNaturalConcaveForm` + the probe's C1 source assertion
+ C2b grid check (tier recorded there). `global_of_local` additionally takes as hypotheses that the
effective domain is **closed under both midpoints** (true for the L♮-convex box + difference
constraints, not separately machine-checked against the probe) and that M5's fixed point has no
improving `±χ_S` (the probe's M4 checks its min-cut move against brute force). Steepest-ascent
termination is not proved here and is not needed for the certificate.

Status `in-progress` (not closed): the owner may still want (1).

## Claim reset 2026-11-15

Was in-progress with no bean update since October 2026. Reset to todo by the owner-approved bean triage (same rule as the 2026-10-04 reset). Nothing in the work was judged. Re-claim it if you pick it up.

## 2026-11-15 (Round 44, PR #8044, commit `704fca1db0eda5cb6a4a400ce4fd936a3248f86e`) — `boxDiffDomain` midpoint closure proved

Per owner ruling `Q-3E6W-2 = 1` (session `session_012EE90758AE4945AC814D43`), extended `folio/quantum-observable-universe/lean/QOU/BraidKnot/LNaturalOptimality.lean` (and wired it into `QOU/BraidKnot.lean`) with the midpoint-closure proof for the L♮-convex polyhedron of box + pairwise difference constraints (`boxDiffDomain lo hi c = {u | (∀ i, lo i ≤ u i ∧ u i ≤ hi i) ∧ ∀ i j, u i - u j ≤ c i j}`):
- `ceilMid_mem_boxDiffDomain`, `floorMid_mem_boxDiffDomain`, `boxDiffDomain_midpoint_closed`
- `global_of_local_boxDiffDomain`: specialises `global_of_local` to `boxDiffDomain lo hi c` with `hmidD` discharged automatically.
- Verified with `lean -DautoImplicit=false -s 65536`: 0 errors, 0 warnings, 0 `sorry`, axioms `[propext, Classical.choice, Quot.sound]`.
- Status kept at `in-progress` (not closed).



## 2026-11-17 sibling sweep
Sibling session that worked this was archived; no new leftover beyond what this bean holds.
Recorded 2026-11-17 from the stale-sibling-session sweep (table: /mnt/project-files/qou-sibling-consolidation/table.md). Source session archived; work not lost.
