# Mirror drift: measured for the first time, and the direction is not uniform

**Date:** 2026-09-05
**Beans:** follow-on from `qou-tsnp` (the dead-lean-pointer sweep, PR #6787)
**Status:** decision brief. **Nothing here is applied.**

---

## The decision, first

**130 fully-qualified Lean names are declared twice in this corpus** — once in a
content-block `.lean` sibling (a `.lean` file sitting next to a block's `.ts`/`.md`,
under `content/<paper>/<chapter>/`) and once in the library tree
(`content/quantum-observable-universe/lean/QOU/**`). The sibling **wins**: `lean.ref`
resolution tries the sibling first (AGENTS.md §0a candidate 1) and only then the Lake
tree. So every per-block checker aimed at such a block reads the sibling's copy and
never sees the library declaration that `lake build` actually compiles.

**What is being decided is how much of that to reconcile, and whether to build the
instrument that would keep it from growing.**

Two things make this a decision rather than a chore, and both were unknown before today:

1. **The direction of staleness is not uniform.** Of the 163 substantive drifts,
   **91 have the library side newer and 70 have the sibling side newer.** There is no
   "the siblings are stale copies" rule to apply — a bulk pass in either direction
   would delete real work.
2. **There is no live instrument.** The gate `prepare-merge` §4a prescribes,
   `check-mirror-drift.ts`, **does not exist** — not in this repo and not in the
   `folio-assistant` clone. The one audit that sounds adjacent,
   [`scripts/lean-duplicate-fqn-audit.py`](../../scripts/lean-duplicate-fqn-audit.py),
   says in its own SCOPE note that it walks the library tree only and that
   *"a clean run here is not evidence that a name is unambiguous in the corpus."*
   So this surface has been unmeasured, and the numbers below are the first measurement.

---

## The measurement

Method: the FQN parser from `lean-duplicate-fqn-audit.py` (reused deliberately, so its
namespace-stack and comment-stripping calibration is not re-litigated), run over the
sibling surface as well as the library, then intersected.

| | count |
|---|---:|
| FQNs declared in **both** a content sibling and the library | **130** |
| sibling declarations involved | 282 |
| faithful (declaration signature identical) | 118 |
| **drifted** (signature differs) | **164** |
| — of those, cosmetic (a binder underscore, `hq` vs `_hq`) | 1 |
| — **substantive** | **163** |
| **LIVE shadows** — the block's own `lean.ref` names the shadowed FQN | **12** |
| — of those 12, drifted | 7 |

Drift by chapter (top): `quantum-observable-universes` 60, `mass-theory` 27,
`braids-and-knots` 12, `predicted-spectra` 9, `climax-volume-mass` 9,
`lifting-and-descent` 9.

**The 12 live shadows are the sharp subset.** Elsewhere the duplication is latent — the
block's `lean.ref` points somewhere else, so nothing is currently misdirected. In these
twelve, the ref names the exact duplicated name, so the checker demonstrably reads the
sibling:

| FQN | newer side |
|---|---|
| `QOU.BraidKnot.delta_q` | sibling |
| `QOU.Information.gravitationalConstant` | library |
| `QOU.Information.informationBandwidth` | sibling |
| `QOU.Information.operationalEntropy` | library |
| `QOU.Information.speedOfLight` | library |
| `QOU.Interactions.AlgebraicPrimality.IsAlgebraicallyPrime` | library |
| `QOU.qReebVectorField` | sibling |
| `QOU.LiftingDescent.ccg_cosimplicial_identities` | *(faithful)* |
| `QOU.PhiQPiece.subLink` | *(faithful)* |
| `QOU.qConnection` | *(faithful)* |
| `QOU.qExtDeriv` | *(faithful)* |
| `QOU.qLieBracket` | *(faithful)* |

## 🛑 The worked example that kills the obvious fix

The obvious move is *"the library is canonical; delete the sibling copies."* Here is why
that is wrong, from the live list above.

`QOU.Information.speedOfLight`:

```lean
-- library, QOU/MathConstants.lean:29
noncomputable def speedOfLight {M : Type*} (sp : ArchimedeanSubstrateField M)
    (p : M) : ℝ :=
  1 / (sp.field p - 1)

-- sibling, information-theory/information-speed-of-light.lean:49
--   "§7c: the temporal weight `q − 1` is carried as the unit `d : kˣ`, so
--    `c_q` is the ring element `↑d⁻¹` — no field structure is required."
def speedOfLight (d : kˣ) : k := (↑d⁻¹ : k)

theorem speedOfLight_mul (d : kˣ) : speedOfLight d * (d : k) = 1 :=
  Units.inv_mul d
```

The **sibling is the §7c-compliant version** — generic base ring, division-free, with
the defining relation discharged as a theorem — and the **library is the older
archimedean one**, specialised to `ℝ` for no reason the statement needs.
`gravitationalConstant` is the same shape (`Rˣ` units in the sibling, `ℝ` in the
library).

So on this row "library newer" means *the library was edited more recently*, **not**
*the library is better*. Recency and canonicality are different questions, and the
measurement above only answers the first. **Every reconciliation is a per-name
judgement about which side should survive**, and roughly half the time the answer will
be the sibling.

---

# The options

## (a) Build the instrument, gate the growth, change no content — *recommended, with (b)*

**What it means.** Land the measurement above as a committed, self-testing script with
a baseline, so the population is visible and cannot grow silently. Replace
`prepare-merge` §4a's reference to the non-existent `check-mirror-drift.ts` with it.
No content block or library file changes.

**What it costs.** A script plus a baseline file, and a §4a edit. Hours, not days.

**What it risks.** Very little — it changes no mathematics. The one real risk is a
**baseline that ratchets the wrong way**: this repo's rule is that baselines drain and
never grow, so a 130-entry baseline is a large standing debt that must not become a
place to park new duplicates.

**What it commits to.** Treating 130 as the high-water mark and draining from there.

## (b) Drain the 12 live shadows by hand — *recommended, with (a)*

**What it means.** For each of the twelve where the block's `lean.ref` actually names
the duplicated FQN, decide which side is canonical, keep that one, and make the ref
resolve to it — the disposition `TFromTraceCyclicity` and the D11 repair already
established.

**What it costs.** Twelve per-name judgements, each needing both files read and the
survivor `lean`-direct verified. Five are already faithful, so those are the cheap
ones. Realistically a day.

**What it risks.** Getting a canonicality call wrong deletes the better of two
implementations — see `speedOfLight`. Mitigated by reading both, never by recency.
Reversible from git in every case.

**What it commits to.** Nothing structural; it closes the subset that misdirects
checkers *today*.

## (c) Full reconciliation of all 130

**What it means.** Resolve every duplicated name corpus-wide.

**What it costs.** 130 judgements of the same kind as (b), across eight chapters, with
163 substantive signature differences to adjudicate. Weeks, and it is not parallel
work — the calls interact (a chapter's siblings often share a base-ring convention).

**What it risks.** The largest surface for a wrong canonicality call, and it competes
for attention with open mathematics. It would also touch `quantum-observable-universes`
(60 drifts) heavily — chapters whose siblings and library halves may have diverged for
reasons nobody has written down.

**What it commits to.** A long, mechanical arc.

## (d) Do nothing — the default

**What it means.** The 130 stay; the 12 keep misdirecting per-block checkers.

**What it costs.** Nothing today. Nothing is broken, no build fails, `lake build`
compiles the library halves regardless.

**What it risks.** Per-block QA verdicts on those twelve blocks are **about the sibling,
not about the declaration the library compiles**, and nothing says so. That is the same
class as the stale-sidecar problem: a verdict that reads as a pass but is about a
different artifact. And with no instrument, the number is free to grow.

---

## Blast radius in real terms

**No build breaks either way**, and that is the point: `lake build` compiles the library
half, the sibling compiles standalone, and neither notices the other. What is affected
is which declaration a *checker* audits — the `q-usage-*`, `wall-side-correct`,
`proof-statement-integrity` and `da-*` criteria all resolve through `lean.ref`, so on
those twelve blocks every one of those verdicts describes the sibling.

Two of the twelve are `QOU.Information.speedOfLight` and
`QOU.Information.gravitationalConstant` — constants that reach the paper's §9
information-theory chapter. A reader who follows the block's Lean reference gets the
sibling's generic-ring version; a reader who builds the library gets the `ℝ` one. They
are not the same statement, and nothing in the corpus currently says which is meant.

## Recommendation *(agent judgement, not a finding)*

**(a) and (b) together.** (a) because a gate that names a script which does not exist is
worse than no gate — it reads as covered. (b) because twelve is tractable and it is
exactly the subset that misdirects a checker today. I would **not** take (c) now: 130
per-name canonicality calls is a larger commitment than the defect warrants while the
extensive-term and `c_k` arcs are open, and (a) makes deferring it safe by making it
visible.

If you want only one: **(a)**. The measurement not existing is the part that lets this
grow.
