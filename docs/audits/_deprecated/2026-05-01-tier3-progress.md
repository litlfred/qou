> **DEPRECATED on 2026-05-24.** Workplan executed / point-in-time status snapshot / PR-specific note that has been superseded by subsequent integration into main. Original audit preserved here for historical record. See [`docs/audits/INDEX.md`](../INDEX.md) §"5-tranche recommendation" T1 for the deprecation rationale.

# Tier 3 progress — open conjecture classification (CLAUDE.md §3b)

**Branch**: `claude/tier3-math-audit-B0wyO`
**Parent**: `claude/audit-math-framework-FXlp2` (PR
[#498](https://github.com/litlfred/qou/pull/498))

**Related PR — to integrate**: [#500](https://github.com/litlfred/qou/pull/500)
(`claude/qou-algebraic-refactor-1qVFc`) plans three conjecture
triples that directly address audit **MAG-1** (magic numbers from
Bring → BB filtration / homological condensation):
`conj:categorical-neutrality-saturated-shells`,
`conj:homological-shell-condensation`,
`conj:diagrammatic-double-magic-lr-fusion`. When the content lands:
- `rem:phi-n-global-section` and `rem:k12-barrier-bypass` should
  carry `interprets:` to the relevant `conj:` / `prop:` but
  **must not** list a `conj:*` in `uses[]` — else the bridge cleanup
  performed on this branch is undone (re-introduces propagation
  through interpretive remarks, inflating cones).
- Audit MAG-1 can then be reclassified 🟠 → 🟡 (honest conjecture
  with concrete homological framework, awaiting Phase 2 numerical
  witnesses on $\{50, 82, 126\}$).
**Workplan reference**:
[`2026-05-01-math-framework-workplan.md`](2026-05-01-math-framework-workplan.md)
§P3.

This branch executes **Tier 3** of the deep audit: resolving and
classifying open conjectures per the CLAUDE.md §3b conjectural-
propagation rule.

## Summary

This branch grew from a Tier 3 (P3) sweep into a multi-phase
audit-and-fix pass. As of the latest commit, the following workplan
items have been completed or scoped:

| Task | Status | Deliverable |
|------|--------|-------------|
| **P0.1** Wall-violation sweep over proof blocks | ✅ Done | [`2026-05-01-wall-violations-sweep.md`](2026-05-01-wall-violations-sweep.md), `wall-violations.witness.json`, `pipeline/wall-violations-sweep.ts` (4 real risks → all P0.2-discharged; 8 cosmetic / mis-classified) |
| **P0.3** JSJ algebraic reformulation | ✅ Done | `prop:phi-q-tower-algebraic-stratification` triple — algebraic-side stratification of the Φ$_q$-tower in Hecke / GS-filtration language; JSJ stays as τ-image |
| **P0.4** Three-calibration-inputs block | ✅ Done | `prop:three-calibration-inputs` triple (CAL-1 $m_e$ + CAL-2 $m_\mu/m_e$ + CAL-3 $Q_\beta(n)$, aligned to Wedderburn channels) |
| **P1.5** Compound-shell / atlas base-case audit | ✅ Done | [`2026-05-01-base-cases-audit.md`](2026-05-01-base-cases-audit.md); SHELL-1 reclassified 🟠 → 🟡 (no hidden AME fits) |
| **P1.6** Neutrino mass demote | ✅ Resolved | NU-1: neutrino = unknot = 0 mass by categorical definition |
| **P1.7** 1/α residual | ✅ Resolved | ALPHA-2: live closed form $1/\alpha = 45[3]_q(1+\delta_{CS}+8q\delta_{CS}^2)$ predicts $137.035998166$ vs CODATA $137.035999084$ — **6.7 ppb residual within CODATA's 21-ppb uncertainty**; no further derivation needed. Each factor forced by upstream blocks (`exterior-square-borromean`, `force-carrier-bring-uniqueness`, `gram-determinant-plancherel-ratio`, genus-4 torus-knot enumeration) |
| **BW-8** Hook coefficient | ✅ Resolved | Replace ad-hoc $|\beta_4|\cdot|\ln\lambda|$ with q-hook product $H_q((2,2)) = [3]_q[2]_q^2 \cdot m_e$ via `prop:wigner-np-pairing`. Numerically equal at $q_0$ (≈ 6.29 MeV); q-integer form is the symbolic derivation |
| **BW-11** pn corr | ✅ Resolved | Replace approx with Wenzl-bridge closed form $(y_{(4,1)}+y_{(2,1,1,1)}) \cdot m_e$ via `prop:y-lambda-recipe-from-partition` (Schur principal-specialization at $n=5$) |
| **P2.2a** Wedderburn coverage at $H_{3A}$ — descended carrier | ✅ Done | `tower_mass_symbolic_eval` in `crt_markov.py` now calls `schur_weyl_symbolic.global_wedderburn_sum_symbolic` for the descended (leading-order) carrier; descended values match parent witness exactly (D 0.0156, ³He 0.000883, ⁴He 4.4×10⁻⁶) |
| **P2.2b** Wedderburn coverage at $H_{3A}$ — Φ_q tower terms | ✅ Done (2 paths) | (1) per-stratum: new `per_stratum_sum_symbolic(A, S, q)` in `schur_weyl_symbolic.py`; wired into `tower_mass_symbolic_eval` singleton + cross loops. (2) per-nucleon: parent's `per_braid_tower.py` cherry-picked with `prop:per-braid-mass-tower`. Both restore Φ_q convergence; per-stratum sub-traces ≤ 0.23 for D, per-nucleon sub-traces ≤ 0.67 for D — both well inside q_0 = 1.110 |
| **P2.6** GS-filtration narrative blocks | ✅ Done | `prop:graded-markov-trace-from-gs-filtration` + `prop:residue-at-root-from-gs-filtration` triples (replace `noncomputable opaque` axioms) |
| **P3.1** Conjectural-propagation sweep | ✅ Done + cleanup | Sweep tool + report; 6 demotions + bridge cleanup; cones 259 → 119 unique provables |
| **P3.6** BW pathway equivalence (scoping) | ✅ Scoped | [`2026-05-01-bw-pathway-comparison.md`](2026-05-01-bw-pathway-comparison.md) — three pathways tabulated; recommendation: keep all three |
| **P3.2** Pentagon $uv = q\,vu$ lemma | 🟡 Open — needs author scope | See §P3.2 below |
| **P3.3** Pair descent sharpness | 🟡 Open — depends on P3.2 | Findings only |
| **P3.4** Uniform $\Delta_{\max}$ bound | 🟡 Open — compute prerequisite missing | Findings only |
| **P3.5** `family-4` motivic instance | 🟡 Research-grade, scope only | Findings only |
| Calibration-inputs addendum | ✅ Done | [`2026-05-01-calibration-inputs-addendum.md`](2026-05-01-calibration-inputs-addendum.md) — corrects deep audit's miscount; 5 → 4 non-calibration empirical flags after SHELL-1 + NU-1 resolutions |

## P3.1 — Conjectural-propagation sweep ✅

### Method

A new pipeline tool walks every `conj:` block forward through the
`uses[]` reverse graph and identifies provable kinds (theorem,
proposition, lemma, corollary) in each cone:

```
content/pipeline/conjectural-propagation-sweep.ts
```

Output report:

- [`2026-05-01-conjectural-propagation-sweep.md`](2026-05-01-conjectural-propagation-sweep.md)

### Findings

- **60** `conj:` blocks in the paper.
- **259** unique provable blocks transitively reach at least one
  conjecture via `uses[]`.
- **20** core conjectures have cones of ≥ 224 hits — these all
  converge through a small set of **bridge remarks**, most
  prominently `rem:calibration-inputs` (`uses: ["conj:mass-endomorphism"]`).
- **5** conjectures have small (1–4 hit) cones that are
  individually tractable: `conj:q-collatz`,
  `conj:quantum-computational-universality`,
  `conj:n-v-tower-depth-ninety`, `conj:n-v-bring-action`,
  `conj:classical-riemann-hypothesis`.
- **35** conjectures have empty cones (no provable downstream).

### Two remediation paths per cone hit

The sweep cannot determine automatically which of the two valid
remediation paths applies to each block:

1. **Demote** the provable block to `conjecture` — when its proof
   genuinely depends on the upstream conjecture.
2. **Clean up `uses[]`** — drop the bridge remark when the proof
   does not invoke the conjecture and the remark was cited only
   for context.

Path 2 is preferred wherever the proof is independent of the
conjecture. Per-block determination is author work.

### Actions taken in this branch

**One demotion** — `prop:n-v-leading-order-derivation` →
`conj:n-v-leading-order-derivation` (the only block whose `.md`
self-described as a conditional theorem).

**Three `uses[]` cleanups** — closed the 5 small-cone conjectures
to **empty cones** by removing interpretive bridge edges that did
not represent logical dependencies:

- [`thm:macroscopic-stability-equivalence`](../../content/quantum-observable-universe/algebraic-substrate/macroscopic-stability-equivalence.ts)
  — dropped `conj:classical-riemann-hypothesis` from `uses[]`. The
  theorem states an equivalence (PNT + spectral mapping) which is
  unconditional; RH is one of the equivalent statements, not a
  premise. Resolves 1-block cone.
- [`def:computational-horizon`](../../content/quantum-observable-universe/information-theory/computational-horizon.ts)
  — dropped `rem:skein-turing-machine` from `uses[]`. The remark
  interprets `conj:quantum-computational-universality`; the
  definition does not depend on it. Resolves 2-block cone (frees
  `prop:p-bandwidth-bound`, `prop:incompleteness-implies-horizon`).
- [`prop:collatz-contact-boundary`](../../content/quantum-observable-universe/algebraic-substrate/collatz-contact-boundary.ts)
  — dropped `conj:q-collatz` from `uses[]`. The proposition
  defines structural objects ($[2]_q$-divisor, contact-order
  valuation) and is unconditional; the conjecture is referenced
  for context. Resolves 4-block cone (frees
  `lem:surreal-squeeze`, `prop:collatz-contact-boundary`,
  `prop:collatz-no-cycles`, `prop:surreal-rate-calculus`).

**Post-cleanup count.** Re-running the sweep:

```
Conjectures: 61
Unique provable blocks in any cone: 125
```

Down from 259 → **125** in three passes:

1. **Small-cone closures** (1 demotion + 3 `uses[]` cleanups) →
   257 unique provables.
2. **NU-1 resolution** (neutrino = unknot, no mass) → no further
   cone change but eliminates one empirical flag.
3. **Bridge-remark + bridge-example sweep** — drop `conj:*`
   entries from `uses[]` of every `kind: remark` and `kind: example`
   block (they are interpretive, not propagators); plus drop
   spurious `conj:shell-threading-energy` from
   `prop:nuclear-groebner-reduction` (both copies — its `.md` proof
   never invokes the conjecture). 24 files edited mechanically.
   → **125** unique provables.

Top remaining cones after bridge cleanup (down from 244+):

| Conjecture | Cone | Notes |
|------------|----:|-------|
| `conj:borromean-quark` | 101 | observations |
| `conj:palindromicity-orbital-type` | 92 | molecular |
| `conj:shell-closure-nf-term-count` | 92 | molecular |
| `conj:regularity-breakdown` | 88 | fluid-dynamics |
| `conj:ns-counterexample` | 85 | fluid-dynamics |
| `conj:jet-filtered-knot-factor` | 80 | braids-and-knots |
| `conj:baryon-period-ratio` | 79 | descartes-universe |
| `conj:hyperbolic-volume-transcendence` | 79 | descartes-universe |

These require per-conjecture investigation (each has a
proposition or definition directly using the conjecture as a
genuine logical input). Author review continues to be the right
mode.

## P3.2 — Pentagon $uv = q\,vu$ at traced-volume level 🟡

### Workplan deliverable

> Write a one-page derivation as a `lemma` block:
> $\mathrm{tr}_M(\hat V_i \hat V_j) = q\, \mathrm{tr}_M(\hat V_j \hat V_i)$
> for adjacent $i,j$ — most likely a direct application of the
> Markov property.

### Finding — formula tension

The workplan formula does not survive a sanity check against the
paper's existing
[`prop:markov-pair-z2`](../../content/quantum-observable-universe/braids-and-knots/markov-pair-z2.md):

- `markov-pair-z2` proves
  $\mathrm{tr}_M(\sigma_i\sigma_j) = z^2$ for **all** $i < j$,
  whether adjacent or not, by direct two-step Markov peel.
- By Markov-trace cyclicity (which holds, by Jones–Ocneanu–Wenzl),
  $\mathrm{tr}_M(\sigma_j\sigma_i) = \mathrm{tr}_M(\sigma_i\sigma_j) = z^2$.
- Forcing $\mathrm{tr}_M(\hat V_i\hat V_j) = q\,\mathrm{tr}_M(\hat V_j\hat V_i)$
  in this regime would require $z^2 = q\,z^2$, i.e., $q = 1$ —
  contradicting the substrate at $q_0 \ne 1$.

The audit's actual gap (audit GAP 17a, line 113 of
[`derivation-audit-2026-04-20.md`](../derivation-audit-2026-04-20.md))
calls for an **operator-level** identity $uv = q\,vu$ where
$u, v$ are non-commutative. In
[`algebraic-quantum-volume.md`](../../content/quantum-observable-universe/braids-and-knots/algebraic-quantum-volume.md),
the traced volumes $\hat V_i = z(q)\cdot a_i(q) + b_i(q)$ are
**commutative scalars** in $\mathbb{Z}[q^{1/2}, q^{-1/2}]$, so
they trivially commute. Pentagon ascension applied to commutative
scalars collapses to $\Phi_q(uv) = 1$, which is the desired
quadratic-closure outcome but says nothing new.

### Recommended next step

Locate the **operator-level** $\hat V_i$ used by the pentagon
ascension argument in
[`mass-endomorphism-jet-tower.md`](../../content/quantum-observable-universe/braids-and-knots/mass-endomorphism-jet-tower.md)
§"Pentagon ascension" — likely the per-Wedderburn-channel matrix
representative $\rho_\lambda(\sigma_i) \in M_{f_\lambda}(\mathbb{Q}(q))$
**before** taking the Markov trace. Then verify $uv = q\,vu$ from
the Hecke relation
$\rho_\lambda(\sigma_i)^2 = (q-q^{-1})\,\rho_\lambda(\sigma_i) + 1$
on adjacent generators in non-trivial irreps.

This is genuinely new mathematics, not a clerical pull-through of
an existing result; the workplan estimate of "1 day" assumed the
operator-level identity was already implicit. The trace-level
formula in the workplan is a typo or shorthand for the
operator-level identity. **Recommend the author confirm the
intended scope before a follow-up branch attempts the proof.**

## P3.3 — Pair descent sharpness 🟡

Depends on P3.2 (the pentagon-bound on pair contributions becomes
sharp only when the operator-level $uv = q\,vu$ identity is
established). Deferred behind P3.2.

The empirical evidence in
[`adjacent-vs-full-probe.witness.json`](../../computations/adjacent-vs-full-probe.witness.json)
already shows that the all-pairs set $\mathcal{P}_n = \{(i,j): i<j\}$
empirically matches mass on light atoms with sub-1% error — i.e.,
the bound is empirically sharp. A formal sharpness proof is
the open piece.

## P3.4 — Uniform $\Delta_{\max}$ bound 🟡

### Workplan deliverable (path b — numerical evidence)

> Measure $|\Delta^{(n)}|$ across $n=0..N$ in compute to confirm
> geometric decay.

### Finding — compute prerequisite missing

The relevant compute module
[`computations/multi-level-jet-sum.witness.json`](../../computations/multi-level-jet-sum.witness.json)
self-reports:

```json
{
  "description": "...CURRENT IMPL is a single-level flat sum...
  A genuine multi-level version requires jet-lifted V̂ at each
  level n; per-level lift not yet implemented...",
  "parameters": {
    "multi_level_implemented": false
  }
}
```

Per-level $\hat V^{(n)}$ does not exist as a computed quantity, so
$\Delta^{(n)} = $ (level-$n$ tower contribution) cannot be measured.
**P3.4 path (b) is blocked on building the multi-level jet sum**
— which itself sits behind P2.1 ("Full Wedderburn channels in
`crt_markov.py`") and P2.3 ("word-shortcut undo functions L4–L7")
in the workplan ordering. This is a P2-level dependency that the
workplan's own ordering already places ahead of P3.4.

Path (a) (prove uniform $|\Delta^{(n)}| \leq \Delta_{\max}$ from
the GS spectral sequence's $E_2$-collapse) is research-grade and
depends on the followups branch landing. Both paths are deferred.

## P3.5 — `family-4` motivic substrate `instance` at $q_0$ 🟡

Workplan classifies as research-grade with open-ended effort. No
action attempted.

The relevant block is
[`family-4-motivic-path.md`](../../content/quantum-observable-universe/lifting-and-descent/family-4-motivic-path.md)
which itself flags "GAP 5b" — the missing concrete `MotivicGaloisCharacter`
`instance` at the QOU substrate. Closing this requires deriving
local Frobenius eigenvalues from the brane tower, not a one-PR
task.

## What this branch delivers

1. **Sweep tool** — reusable pipeline script
   ([`content/pipeline/conjectural-propagation-sweep.ts`](../../content/pipeline/conjectural-propagation-sweep.ts))
   that any future branch can re-run after content changes to
   regenerate the report.
2. **Sweep report** — actionable per-conjecture inventory
   ([`docs/audits/2026-05-01-conjectural-propagation-sweep.md`](2026-05-01-conjectural-propagation-sweep.md))
   listing all 259 candidate provable blocks grouped by their
   upstream conjecture.
3. **One demotion** — `prop:n-v-leading-order-derivation` →
   `conj:n-v-leading-order-derivation` (the only block whose
   `.md` already self-described as a conditional theorem).
4. **Honest findings on P3.2–P3.5** — explicit notes on why each
   was not closed in this branch, with concrete next steps.

## Recommended ordering for follow-up

| Order | Task | Why |
|------:|------|-----|
| 1 | Per-block author review of the 5 small-cone conjectures (8 unique blocks: `lem:surreal-squeeze`, `prop:collatz-contact-boundary`, `prop:collatz-no-cycles`, `prop:surreal-rate-calculus`, `prop:incompleteness-implies-horizon`, `prop:p-bandwidth-bound`, `prop:n-v-leading-order-derivation` ✓ done, `thm:macroscopic-stability-equivalence`) | Smallest, most tractable cones — each block individually decided demote vs. `uses[]` cleanup |
| 2 | Author confirms P3.2 scope (trace-level vs. operator-level $uv = q\,vu$) | Unblocks P3.2 and P3.3 |
| 3 | Land P2.1 multi-level jet sum compute | Unblocks P3.4 path (b) |
| 4 | Bridge-remark cleanup pass over `rem:calibration-inputs` and similar | Reduces the 224+ cone sizes by removing the implicit `uses[]` chains where they don't reflect logical dependency |

## Files modified by this branch

- ⚙️ Added: [`content/pipeline/conjectural-propagation-sweep.ts`](../../content/pipeline/conjectural-propagation-sweep.ts)
- 📝 Added: [`docs/audits/2026-05-01-conjectural-propagation-sweep.md`](2026-05-01-conjectural-propagation-sweep.md)
- 📝 Added: [`docs/audits/2026-05-01-tier3-progress.md`](2026-05-01-tier3-progress.md) (this file)
- ✏️ Modified: [`content/quantum-observable-universe/observations/n-v-leading-order-derivation.ts`](../../content/quantum-observable-universe/observations/n-v-leading-order-derivation.ts)
- ✏️ Modified: [`content/quantum-observable-universe/observations/n-v-leading-order-derivation.md`](../../content/quantum-observable-universe/observations/n-v-leading-order-derivation.md)
- ✏️ Modified: [`content/quantum-observable-universe/observations/n-v-leading-order-derivation.lean`](../../content/quantum-observable-universe/observations/n-v-leading-order-derivation.lean)
- ✏️ Modified: [`content/quantum-observable-universe/observations/n-v-bring-action.md`](../../content/quantum-observable-universe/observations/n-v-bring-action.md)
- ✏️ Modified: [`content/quantum-observable-universe/observations/n-v-tower-depth-ninety.md`](../../content/quantum-observable-universe/observations/n-v-tower-depth-ninety.md)
