# qou-brng sub-stubs closed — the log/free-energy bridge is the archimedean lift, magnitude is the one open number

**Date:** 2026-09-03 · **Type:** close-out synthesis (empty stubs `qou-0qkt`,
`qou-xjup`) + resolution-options assessment for the "magic-shell regime switch"
(bean `qou-fcn8`). **Discipline:** no fit, no closure claim, numerology guard on
the ℏ_q² fraction. Every negative scope-(a) unless a proved invariant licenses
(b).

Two `qou-brng` sub-beans (`qou-0qkt` "R2 archimedean-boundary lift
(free-energy/log bridge)", `qou-xjup` "residuals — coefficient, Hamiltonian
assignment, ℏ_q² saturation") were created 2026-08-30 as **empty placeholders**
and never worked. `qou-ge9f` (binding-channel taxonomy, completed 2026-08-31 —
*after* the stubs) and `qou-gwr9` (chain forced, Lean) now answer their
substance. This note records the close-out and re-scopes `qou-fcn8`.

## 1. `qou-0qkt` (archimedean-boundary lift / free-energy log bridge) — CLOSED, subsumed

The "free-energy/log bridge" **is** the log-family channel
$B = E_0\log(\mathrm{tr}_{\text{free}}/\mathrm{tr}_{\text{atom}})$ (taxonomy
channel 3) — a $-\log Z$ free-energy form, which is exactly what an
archimedean-boundary lift of the intensive trace-difference produces.

- **It lifts intensive → extensive, and this is now Lean, not conjecture.** On
  the strand-forced chain (`qou-gwr9`, `StrandLayoutForcesChain.lean`) the
  log-family binding is *exactly affine in $A$* (2nd finite difference
  $\sim10^{-51}$, `qou-ge9f`) — it saturates. The bridge exists.
- **It does not close the magnitude.** Measured
  ([`log_ratio_binding_prototype.py`](../../computations/log_ratio_binding_prototype.py)):
  the forced-chain log-ratio lands at **0.79–3.26× AME** (spread 4.15×) across
  D…⁷Be. The functional form is right; the coefficient is not.

So `qou-0qkt`'s question is answered: **yes, the free-energy/log form is the
archimedean lift and it is extensive-by-construction — but "extensive" is a
statement about its shape, not its coefficient.** Nothing to attack here that is
not the magnitude gap already carried by `qou-brng`.

## 2. `qou-xjup` (residuals: coefficient / Hamiltonian / ℏ_q² saturation) — CLOSED, subsumed

Its three threads each resolve to their honest state:

- **Coefficient** — the 0.79–3.26× forced-chain scatter above. This *is* the
  `qou-brng` magnitude gap; not an independent item.
- **Hamiltonian assignment** — identified, not open: the log form
  $E_0\log(\mathrm{tr}_f/\mathrm{tr}_a)$ is a free-energy $-\log Z$, so the
  "Hamiltonian" is the trace-log itself. The taxonomy fixes this.
- **ℏ_q² saturation** — **numerology-flagged.** The saturated fraction rises
  0.12 → 0.77 → 0.93 → 0.95·ℏ_q² with A; its one candidate mechanism (the
  volume-defect route) is **refuted** (scope-(a),
  `binding_volume_defect_route_refuted.py`), and `qou-brng`'s own verdict is
  *"more likely a numerical coincidence than a derived prediction."* A monotone
  approach to a round number that never reaches it (0.95 ≠ 1) is not a law.

Nothing in `qou-xjup` survives as an independent open item; all three are either
the tracked `qou-brng` coefficient or the guarded ℏ_q² coincidence.

## 3. Re-scope `qou-fcn8` (the "magic-shell regime switch") — the swing is smaller than it looked

My earlier roast framed this as "re-derive the nuclear shell model / risk a
fitted $M(A)$." **That was too pessimistic and is corrected here.** The
coordination is not a free function to fit:

- **The chain bond set is FORCED** by the 3-strands-per-nucleon layout
  (`qou-gwr9`, `StrandLayoutForcesChain.lean`) — not chosen. There is no $M(A)$
  to fit; bounded degree, hence saturation, follows from the forced layout, and
  `complete_graph_no_saturation` only ever bit the additive family.

So the "regime switch" is largely **dissolved**, not open: real nuclei saturate
because the forced chain has bounded coordination, Lean-proved. What genuinely
remains is **one number** — the log-family coefficient (0.79–3.26× scatter) —
which is identical to `qou-brng`.

**A discipline note on the tempting all-pairs column.** The same producer reports
an *all-pairs* bond count landing at **0.61–1.63×** — the only range in the arc
straddling 1. Do **not** read that as "closer, therefore better." The all-pairs
count is **not** the forced bond set; the canonical, Lean-forced number is the
chain's 0.79–3.26×. The all-pairs range straddling 1 is a different (non-forced)
bond topology, and choosing it because it straddles 1 is exactly the
shape/AME-fit the arc exists to avoid. `qou-ge9f` already showed the all-pairs
*extrapolation* is faithful to the true all-pairs *sum* (5.1 %) — a statement
about the extrapolator, not about which bond set is physical.

## 4. Better-resolution options for the coefficient (the honest menu)

The magnitude is now a single, sharply-localized open: **why is the forced-chain
log-family coefficient off by an A-dependent 0.79–3.26×?** Non-fit routes, and
their risks:

1. **A per-bond coordination correction** derived from the carrier-crossing
   quantisation (`CarrierCrossingQuantisation.lean`) — the per-bond energy may
   carry a degree-dependent factor the bare chain misses. *Risk:* a
   degree-dependent factor tuned to flatten the scatter is a fit; only a
   *derived* factor counts.
2. **The self-vs-mutual linking split** (`SelfMutualPartition.lean`,
   `qou-brng`'s surviving categorical route) — the coefficient may be fixed by
   the mutual-linking amplitude normalisation, which is the one categorical
   question left. *Status:* the direct attack (`qou-d3i9`) is completed and did
   not close it; this is genuinely hard.
3. **Accept the honest negative** — record that the framework fixes the binding
   *form* (extensive log-family, forced chain, both Lean) but **not** its
   coefficient without external nuclear-structure input, and that the ℏ_q²
   saturation is a guarded coincidence. This is the highest-integrity outcome if
   1–2 do not yield a *derived* factor.

**Recommendation (judgement):** the coefficient is not closeable by a better
*channel* or a better *bond set* — those are settled (log family, forced chain).
It is closeable only by a *derived* per-bond normalisation (route 1 or 2), and
absent that, route 3 is the honest terminus. Do not chase the ℏ_q² fraction.

## 5. Cross-references

- Taxonomy + chain-forced: `qou-ge9f`, `qou-gwr9`,
  [`StrandLayoutForcesChain.lean`](../../content/quantum-observable-universe/lean/QOU/Mass/StrandLayoutForcesChain.lean).
- Magnitude producer: [`log_ratio_binding_prototype.py`](../../computations/log_ratio_binding_prototype.py).
- ℏ_q² kernel + refuted mechanism: `qou-brng`,
  [`2026-08-21-binding-mass-rung-derivation.md`](2026-08-21-binding-mass-rung-derivation.md),
  [`binding_volume_defect_route_refuted.py`](../../computations/binding_volume_defect_route_refuted.py).
- Arc ledger: [`2026-08-29-bk-crossing-mass-binding-arc-reassessment.md`](../coordination/2026-08-29-bk-crossing-mass-binding-arc-reassessment.md).
