# Dispensation audit — stalled PRs #4371, #4373, #4140

**Date:** 2026-08-09
**Branch:** `claude/agent-prs-stalled-cleanup-lip0at`
**Scope:** verify that three stalled agent PRs are honestly dispensed — i.e.
that everything of value either landed on `main` or is recorded as open.

All three were already closed before this audit. The question was not whether
to close them but whether their closing records are **true**. Two are; one is
not.

## Summary

| PR | State | Closing record accurate? | Action taken |
|----|-------|--------------------------|--------------|
| #4373 | **merged** 2026-07-26 | n/a | none needed |
| #4371 | closed unmerged 2026-07-26 | **yes** | none needed |
| #4140 | closed unmerged 2026-08-02 | **no** — see below | salvage + correction |

## #4373 — merged

`lean(coxeter): pasted square + orbit invariants + monodromy
diagram-equivariance`. Merged to `main` (`b9fc1020`). Nothing outstanding.

## #4371 — closed in favour of #4376, content fully landed

Closed with: *"Closing in favour of the consolidated #4376."* Verified: all
three authored Lean files are present on `main` and **byte-identical** to the
PR head (`6278510e`) — same blob SHAs:

- `QOU/MassTheory/CableWidthBraneTowerLift.lean`
- `QOU/MassTheory/HeliumFourBodyCluster.lean`
- `QOU/MassTheory/S5So3WLambdaLift.lean`

The closing record is accurate. Nothing stranded.

## #4140 — closing record is inaccurate; 33 of 44 substantive files never landed

The closing comment (2026-08-02) states:

> "No unique content remains here, so closing."

That is **false as written**. Of 44 substantive (non-`.beans/`) files, 33 are
absent from `main`. The comment was right about the two files it named —
`ArgumentPrinciple.lean` (Thread 1) and `CategoricalLagrangianDMCubic.lean`
(salvaged via #4616) are both on `main` — but it generalized from those two to
the whole PR without checking the rest.

### Triage of the 33 unlanded files

Corpus-grep against `main` (per AGENTS.md §"Before declaring open") shows most
were independently re-reached by later, richer work, so the *substance* is not
lost even though the files are:

| Route | Unlanded artifacts | Verdict |
|-------|--------------------|---------|
| Anchor-blind Borel-sum correction | `2026-07-24-c3-barodd-fork-correction.md`, fork probes | **superseded** — `computations/qbeta/qbeta-c3-continuum-vol41-anchor-blind.witness.json` on `main` |
| DM-cubic / Berezinian 3-jet negative | `QbetaC3DMCubic.lean`, `2026-07-20-c3-dm-cubic-derivation-attempt.md`, probe + witness | **superseded** — `computations/a3_magnitude_berezinian_crossterm_probe.py` + the `QBeta/` suite (`SuperBerezinianA3Magnitude`, `BerezinianSelfAdjointCrossTerm`, `BerezinianBarOddIsolation`, `A3OffBlockDerivation`, `A3AntiSelfAdjointLift`) |
| Hopf-cubic residue | `QbetaC3HopfResidue.lean`, `2026-07-20-c3-hopf-cubic-residue-exploration.md` | **superseded** — `computations/qbeta/qbeta_hopf_cubic_shadow_bridge.py`, `qbeta_c3_kc19_kc20_consistency_probe.py` |
| Stokes / GGM order-3 | `QbetaC3Stokes.lean`, `2026-07-14-g3-stokes-via-3d-index.md` | **superseded** — the on-`main` aomega GZ-weight program (#4246, #4260) |
| `SuperDMBerezinian.lean` | — | **superseded** — as the closing note correctly said |
| **Formal-Habiro growth exclusion** | `QbetaC3Habiro.lean`, `2026-07-20-c3-habiro-route.md`, growth-dichotomy probe | **STRANDED** — nothing on `main` carries it (see below) |

Also unlanded and not re-created: the content-block siblings
`brings-surface/categorical-lagrangian-dm-cubic.{md,ts}`. The Lean file landed
via #4616 as a **library** file under `QOU/Brings/`, which needs no content
block (§0a), so this is a narrative gap rather than a defect. Not actioned.

### The one genuinely stranded item — and why it matters

`QOU/Mass/QbetaC3Habiro.lean` proves a growth dichotomy: a geometrically
growing sequence cannot be super-geometric. Applied to the ladder it yields a
**conditional** exclusion of the formal-Habiro route to `c_3`. Corpus-grep for
the claim on `main` (`not_formal_habiro`, `geometric_not_superGeometric`,
Gevrey-1-vs-finite-radius) returns **nothing** — this result exists nowhere
else.

It is decision-relevant because it sits in tension with the live registry.
`docs/coordination/ck-dk-canonical-registry.md` §9 currently reads the Habiro
framing as *correct but unconstructed* (line ~33) and lists the element `F(q)`
as an **OPEN keystone** (line ~75). If the exclusion applies, that keystone is
closed negatively, and dispatching an agent to construct `F(q)` is wasted
effort. So letting the file die on a closed branch risks exactly the
documented-waste pattern the corpus-grep discipline exists to prevent.

**Action:** salvaged to `main` — re-verified against current `main`
(`lean`-direct **exit 0**, zero warnings, sorry-free, axioms
`[propext, Classical.choice, Quot.sound]`), import wired into `QOU.lean`.

**Scope correction applied on the way in.** PR #4140's comment advertised this
as a *"proved scope-b structural exclusion"*. It is not. The dichotomy
`geometric_not_superGeometric` is proved outright, but the two corpus inputs
are §3b-cond **class hypotheses**, so the conclusion is conditional — and one
premise is load-bearing and unestablished:

> `c_k` are coefficients in `u = b·ℏ_q²`; a Habiro element's Ohtsuki expansion
> is in `(q−1)`. `FormalHabiroQOneExpansion c` asserts super-geometric growth
> of *that same sequence*, i.e. it presumes the two expansions are indexed by
> one variable. If the ladder-in-`u` is a re-expansion rather than literally
> the Ohtsuki series, the growth classes need not transfer and the exclusion
> does not bite.

Per AGENTS.md §"Conditional-proved ≠ premise-established", the docstrings were
edited before landing to state the conditionality and name the premise gap, and
to forbid citing the theorem as "the Q_β Habiro element is refuted". The
registry rows were **not** edited: resolving the identification is the open
step, filed as bean **`qou-dq4k`**.

## Verification

- `lean`-direct on `QOU/Mass/QbetaC3Habiro.lean`: exit 0, zero warnings,
  0 `sorry`, axioms `[propext, Classical.choice, Quot.sound]`.
- No CI run cited — auto-triggers are disabled repo-wide (AGENTS.md §10); the
  above is the verification gate.
- No compute re-run (no producer touched), no witness refreshed, nothing wired
  to production, no registry row changed, `q₀` untouched.
