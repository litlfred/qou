# Over-zealous binding-closure framing — audit-of-audits + rescope (2026-06-23)

**Branch:** `claude/bold-mendel-5994kg` · **PR #2612**
**Status:** review + framing rescope. **No math retracted.** Every flagged
refutation's *numeric/structural result stands*; only over-broad *prose* that
foreclosed a still-live sibling direction was narrowed.
**Discipline:** critical-distance license (challenge framings on the merits) +
corpus-grep (the surviving sibling is confirmed to exist before a closure is
called "over-reaching").

## Trigger

The qbk2 q-Bessel "quadratic action" binding refutation
([`2026-06-20-qbessel-yweighted-gap-deflation.md`](2026-06-20-qbessel-yweighted-gap-deflation.md),
[`2026-06-20-binding-gate-stocktake-post-qbk2.md`](2026-06-20-binding-gate-stocktake-post-qbk2.md))
correctly killed a **narrow** claim — "the forced-`y_λ`-weighted quadratic-action
*term* equals the deuteron binding" (15–80× too small) — but its stocktake framing
risked being read as "the q-heat/Reeb **kernel** can't do binding," which is
over-zealous: (a) the kernel survives as the keystone `W_λ` realization, and
(b) a **sibling functional of the same `Z_q` heat trace** — the **log-free-energy**
`B = E₀·log(tr_free/tr_atom)` (the bond-graph route) — is **on-scale, 0.57–2.36×**
([`2026-06-10-binding-bond-graph-compute-audit-and-derivation.md`](2026-06-10-binding-bond-graph-compute-audit-and-derivation.md)).
Owner asked: are there *other* over-zealous closures that "closed doors
incorrectly"? This is the answer.

## Method

Three parallel read-only review agents over `docs/audits/`, `docs/coordination/`,
`docs/workplans/`, `docs/scope/`, sliced by theme
({binding/Δ_λ/mass/ρ/ν_SDP} · {Q_β/c_k/Habiro/q-Bessel/residue} ·
{substrate-q₀/KLR/SDP/keystone/λ(K)/Lean-vacuity}). Rubric per doc: *what NARROW
claim was established → what BROAD framing is used → is a surviving sibling
foreclosed (corpus-grep-confirmed) → class (framing / wrong / no) → confidence.*
Calibration: a false "over-zealous" flag is as harmful as the original over-claim;
well-scoped refutations and correctly-labelled scope-decisions are **not** flags.

## Finding — the corpus is overwhelmingly well-disciplined

The dominant result is **negative**: the critical-distance + corpus-grep + "Im(q)
fibre-vs-observable" + "machinery≠values" disciplines have made the refutation
docs unusually self-aware — most name the surviving sibling in the same artifact
and disclaim broad foreclosure. **Zero "wrong" (flawed) refutations** were found.
Explicitly cleared as well-scoped: the residue-A docs, c3-habiro rigidity, the
qbk2/stocktake cluster itself, the α_EM cluster, ν-SDP-saturation,
deuteron-closure-overclaim-corrected, refuted-ansatz-lemmas, keystone-arena, and
**every** substrate-q₀ reference (correctly "*declined 2026-05-08*", never
"refuted/impossible").

## The genuine over-reaches (all "framing" class — prose, not math)

| # | doc | narrow claim (correct) | over-broad framing | surviving sibling foreclosed | conf |
|---|-----|------------------------|--------------------|------------------------------|------|
| 1 | [`2026-06-17-signed-crossing-binding-refutation.md`](2026-06-17-signed-crossing-binding-refutation.md) | signed **integer** crossings can't make D's 0.57 fractional bond | "**entire crossing-counting family closed**; only the stalled volume route left" + *"do not re-propose"* | the on-scale log-free-energy / `B_sym` (fractional log of the same trace); the Pauli-channel→complete-graph route (`2026-06-20-chirality-forces-complete-graph-topology.md`, best non-fit, RMS 6.19) | **HIGH** |
| 2 | [`2026-06-04-c4-gap-no-constant-kernel-recursion.md`](2026-06-04-c4-gap-no-constant-kernel-recursion.md) | depth-2 + one depth-3 constant-kernel fit fail | title **"CANNOT be closed by ANY constant-kernel recursion"** (test only covered depth ≤ 3) | the **k-dependent / non-constant** kernel — the actual open keystone (its own body keeps it alive; registry C5) | med-high |
| 3 | [`2026-06-17-b3-dense-sdp-lever-closed.md`](2026-06-17-b3-dense-sdp-lever-closed.md) | dense-SDP selects mesonic `L±`, not 𝓑₃ | **"Δ_λ gate closed on EVERY compute lever"** | the on-scale log-free-energy / `B_sym` lever (the SDP-*selection* arc never touched it) | med |
| 4 | [`2026-06-17-delta-lambda-two-remaining-directions-closed.md`](2026-06-17-delta-lambda-two-remaining-directions-closed.md) | LP/continuous selection + α-cluster sidestep both fail | title **"both closed"** / **"fully bounded"** (its own Verdict (1) says *"real gap… Open"*) | the unbuilt dense Wedderburn-projector SDP + topological-criterion promotion (its own body); + log-free-energy | med |
| 5 | [`2026-06-16-b-sym-linear-chain-closed-form.md`](2026-06-16-b-sym-linear-chain-closed-form.md) | `B_sym` is exactly the additive A−1 chain; chain under-binds magic ⁴He | **"no bond-count topology can fix it"** | a Pauli-channel-weighted complete graph (later sibling, best non-fit) | med |
| 6 | [`../coordination/gap-a-path-b-lambda.md`](../coordination/gap-a-path-b-lambda.md) | ~18 *fitted* per-partition ansätze refuted | **"no per-partition ansatz survives"** (a finite refuted set is not a non-existence proof) | signed/chirality categorical-Vol route + owner-gated `s5-so3` Vol (kept open in the same ledger) | low |

## The unifying pattern

**Five of six sit in the binding gate (2026-06-16/17), and all skip the same
on-scale sibling** — the log-free-energy functional `B = E₀·log(tr_free/tr_atom)`
(= `B_sym`, 0.57–2.36× AME; identical to the bond-graph / archimedean form). Each
refutation's *numbers are sound*; the *prose* generalizes from "this functional /
this integer-family / this lever is dead" to "the whole approach / every lever is
closed," silently passing over the functional that *is* on-scale. The single
recurring fix is to scope the verdict to what the probe actually tested and to name
the on-scale sibling — exactly the qbk2 pattern.

## Actions taken (this PR)

1. **Rescoped all 6** verdict/title sentences (framing only; each carries a dated
   "Rescope note" pointing here). No numeric or structural result was changed.
2. **Wired the on-scale sibling into canonical compute** —
   [`binding_log_free_energy.py`](../../computations/binding_log_free_energy.py)
   (→ [`binding-log-free-energy.witness.json`](../../computations/binding-log-free-energy.witness.json))
   computes `B = E₀·log(|tr_free|/|tr_atom|)` on the **canonical lossless `tr_M`**
   (not the per-bond approximation): extensive + on-scale 0.57–2.36×, vs the
   canonical *linear* difference which saturates (0.025–0.21× AME). MBA appendix
   step-9b synced.
3. **Narrow Lean guard** —
   [`QBesselQuadraticActionTerm.lean`](../../content/quantum-observable-universe/lean/QOU/QBeta/QBesselQuadraticActionTerm.lean)
   pins the qbk2 quadratic-action term as ≥15× too small (decidable ℚ inequality,
   sorry-free), with a docstring scoped *only* to that term (kernel + log-functional
   explicitly preserved).

## What this does and does NOT claim

- It does **not** re-open any refuted *numeric* result, propose a 7th Δ_λ ansatz,
  or claim the binding gate closed. The Δ_λ / per-isotope binding gate **remains
  open** (`precision-goals.md`: 3/7 L2 met).
- It **does** record that the still-live directions — the log-free-energy
  functional (on-scale, edge-set/occupancy residual = lever 2), the channel-topology
  route, the k-dependent recursion kernel, the categorical-Vol / `s5-so3` keystone —
  must not be treated as foreclosed by the rescoped verdicts.

## Cross-references

- [`2026-06-20-binding-gate-stocktake-post-qbk2.md`](2026-06-20-binding-gate-stocktake-post-qbk2.md) — the four binding paths' live status.
- [`2026-06-10-binding-bond-graph-compute-audit-and-derivation.md`](2026-06-10-binding-bond-graph-compute-audit-and-derivation.md) — the derived per-bond kernel + log-free-energy form.
- [`2026-05-18-delta-lambda-gating-context.md`](2026-05-18-delta-lambda-gating-context.md) — the gate definition + the six failed ansätze + the retraction.
- [`../../content/quantum-observable-universe/appendix-mass-binding-algorithms/mba-step09b-per-isotope-binding.md`](../../content/quantum-observable-universe/appendix-mass-binding-algorithms/mba-step09b-per-isotope-binding.md) — appendix, synced with the log-free-energy functional.
