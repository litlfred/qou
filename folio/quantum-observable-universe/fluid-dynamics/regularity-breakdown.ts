import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:regularity-breakdown",
  lean: { ref: "qou:QOU.FluidDynamics.RegularityBreakdown" },
  title: "Regularity breakdown at $q = 1$ and a discretely self-similar blow-up scenario",
  uses: [
    "thm:q-ns-wellposedness",
    "prop:q-turbulence-spectrum",
    "rem:hamilton-jacobi-phase",
    "def:leray-profile",
    "def:substrate-parameter",
    "def:qns-unit-layers",
  ],
  cites: [
    "leray1934",
    "necas-ruzicka-sverak1996",
    "tsai1998",
    "seregin2012",
    "chae2013adss",
    "chae-wolf2016dss",
    "bradshaw-tsai2018survey",
  ],
  tags: [
    "tier:famous",
    "navier-stokes",
    "millennium-problem",
    "regularity",
    "critical-exponent",
    "blowup",
    "discretely-self-similar",
  ],
  authorNotes: [
    {
      kind: "refined-framing",
      date: "2026-11-27",
      body: "Owner ruling (Carl): Part A's data are held fixed in the substrate layer. Data fixed in the physical layer satisfy Part A with exponent 2 by the unit conversion alone (`physical_layer_conversion_diverges`). Over the weakened `QNsWellposednessContext` (modal balance with a free transfer term) Part A is trivially satisfiable (`partA_trivial_over_weakened_class`), so a Lean carrier for Part A needs a modal model of the actual nonlinearity; it is not encoded yet.",
      see: "docs/audits/2026-11-27-qns-part-a-enstrophy-order-parameter.md",
    },
    {
      kind: "caveat",
      date: "2026-11-24",
      body: "Formalisation audit (`qou-x60n`): `2026-08-24-undecided-carrier-witnesses.lean` records that the earlier existential `RegularityBreakdown` carrier (`∃ Re_c > 0`) was trivially inhabited at `1`.",
      see: "docs/audits/2026-08-24-undecided-carrier-witnesses.lean",
    },
    {
      kind: "note",
      date: "2026-11-24",
      body: "Formalisation audit (`qou-x60n`, `qou-hjf4`): `2026-08-30-conditional-cone-binders-unused-probe.lean` exposed degenerate `0 ≤ μ ≤ 0` bounds and unused binders in pre-repair `ConditionalCorollaries.lean`.",
      see: "docs/audits/2026-08-30-conditional-cone-binders-unused-probe.lean",
    },
    {
      kind: "note",
      date: "2026-11-24",
      body: "Formalisation refutability witness (`qou-x60n`, `qou-rq9n`): `2026-08-30-qns-carriers-are-refutable.lean` proves `¬ RegularityBreakdown (Set.Ioo 0 1)` and `RegularityBreakdown ∅`.",
      see: "docs/audits/2026-08-30-qns-carriers-are-refutable.lean",
    },
    {
      kind: "note",
      date: "2026-11-21",
      body:
        "**Base ring (§7c).** The Lean sibling `regularity-breakdown.lean` and the lemmas it uses (`DSSObstructions.lean`, L3–L5) are archimedean by construction and state their types over `ℝ`: they use `Real.log`, `Real.sqrt`, order and the topology of `ℝ`. Lemma L2 uses `Complex.exp`. The only generic-ring lemma, L1, is in `IntegerSpin.lean` over a `CommRing`.",
    },
    {
      kind: "refined-framing",
      date: "2026-11-21",
      body:
        "Restated on owner instruction (issue #8864; owner chose 'Full restatement plus Lean'). The conjecture is split into Part A (the $q$-family: $\\Omega(q) \\to \\infty$ as $q \\to 1^+$) and Part B (a classical backward discretely self-similar Navier--Stokes solution). Removed: the period 'set by the root-of-unity scaling $\\lambda_\\kappa$' ($q_\\kappa = e^{i\\pi/\\kappa}$ is a root of unity, Lean `qKappa_is_root_of_unity`); the vortex-sheet clause $d_H = 2$ (Chae--Wolf: one singular point; also contradicted `conj:ns-counterexample`); the 'QOU dictates a phase transition' sentence (an analogy, not derived); the explicit limit $\\varepsilon_k^{-1/3}$ in obstruction 3 (it did not match `prop:q-turbulence-spectrum`); and the Clay reframing as the limit $q \\to 1$ (that endpoint is Euler, since $\\nu_q \\to 0$). Enstrophy blow-up is now derived from Part B (Lean `RegularityBreakdown.enstrophy_blowup`). Part B is restricted to the class that survives Nečas--Růžička--Šverák, Tsai, Seregin and Chae: $|V| \\sim |y|^{-1}$, not in $L^3$. Lean backing: `QOU/Transcendental/FluidDynamics/DSSObstructions.lean`.",
    },
    {
      kind: "note",
      date: "2026-07-25",
      body:
        "**Sustained forcing.** The surreal-bridge campaign (ledger `docs/audits/2026-07-25-qns-surreal-bridge-campaign-ledger.md`) found that the in-model regimes not excluded by its analyses are sustained or forced turbulence. That concerns the forced Navier--Stokes equation, which is a different problem from Part B (unforced, fixed viscosity); it is recorded here as background for Part A only. All in-model/scope-(a).",
      see: "../../../../docs/audits/2026-07-25-qns-surreal-bridge-campaign-ledger.md",
    },
    {
      kind: "refined-framing",
      date: "2026-07-18",
      body:
        "Item 3 re-scoped from continuous backward-self-similar to *discretely* self-similar, the continuous case being excluded by Nečas--Růžička--Šverák (Acta Math. 176, 1996). The critical exponent $\\alpha$ is closure-dependent ($\\alpha = 1$ under the dissipation closure, Lean `enstrophy_alpha_one_of_dissipation_closure`; $\\alpha = 4/3$ under a Kolmogorov cascade); neither is rigorous, see `p2-critical-exponent`. Bean `qou-15gb`. Superseded in part by the 2026-11-21 restatement.",
      see: "../../../../docs/audits/2026-07-18-q-ns-classical-gap-decomposition.md",
    },
  ],
});
