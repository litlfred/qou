import { remark } from "../../schema/builders";

export default remark({
  authorNotes: [
    { kind: "note", body: "Lean sibling: archimedean specialisation over $\\mathbb{R}$ (AGENTS.md §7c). Underlying combinatorial content stays generic to any commutative ring with the same $q$-data." },
    {
      kind: "caveat",
      date: "2026-10-13",
      body:
        "**Re-scoped after owner ruling Q1 ($\\varTheta = f\\,\\xi^\\flat$, " +
        "2026-10-13).** The remark previously called $\\kappa^2$ \"the squared " +
        "Levi condition number\" and concluded: \"Because $\\kappa^2 > 0$, the " +
        "Levi form remains non-degenerate at the collision locus $\\Sigma$. Both " +
        "eigenvalues stay bounded away from zero. The local cohomology group " +
        "remains non-zero. The cohomological obstruction is preserved up to " +
        "$T^\\ast$. This is branch (A) of the conjecture: classical 3D " +
        "Navier–Stokes admits finite-time blowup\", with the Reading paragraph " +
        "adding that the collision preserves contact non-degeneracy, and caveat 4 " +
        "routing \"$\\kappa^2 > 0 \\Rightarrow$ blowup\" through the Levi-degeneracy " +
        "and counter-example conjectures. **Withdrawn:** in dimension 3 the Levi " +
        "datum is the single scalar $\\xi\\cdot\\mathrm{curl}\\,\\xi$, so there are no " +
        "two eigenvalues and no condition number; a straight anti-parallel pair " +
        "has Levi scalar 0 for every core shape; and branch (A) itself is " +
        "withdrawn in `conj:levi-degeneracy` (Beltrami counterexample). " +
        "**Kept, re-scoped to (a):** the ODE result — the proportionality ansatz " +
        "forces $\\kappa^2 = \\pi\\nu/(2\\Gamma+\\pi\\nu) > 0$, strictly below the " +
        "quasi-steady $\\pi\\nu/\\Gamma$ (`.lean` sibling: `proportionality_balance`, " +
        "`kappa_squared_pos`, `lambda_lt_quasi_steady`, unchanged) — as a " +
        "statement about core shape in the Townsend model. The opening paragraph " +
        "also quoted the lock as $\\pi\\nu/\\Gamma$, contradicting the block's own " +
        "boxed value and its Lean; it now quotes the boxed value. The per-channel " +
        "$\\beta = 1$ record (`levi_pair_channel_branch_b.lean`) is likewise a " +
        "statement about this aspect ratio. `conj:ns-counterexample` and " +
        "`def:ns-obstruction` dropped from `uses` (they fed only the withdrawn " +
        "conclusion); `prop:core-levi-form` added. Bean `qou-fm7s`.",
    },
  ],
  interprets: "conj:levi-degeneracy",
  label: "rem:hyperbolic-overlap-saturation",
  title:
    "Hyperbolic-overlap strain saturation: the core aspect ratio locks at $\\kappa^2 = \\pi\\nu/(2\\Gamma+\\pi\\nu)$",
  uses: [
    "prop:core-levi-form",
    "rem:townsend-biot-savart-strain",
  ],
  cites: ["townsend1951", "saffman1992", "moffatt1994"],
  tags: [
    "townsend",
    "hyperbolic-stagnation",
    "vortex-core",
    "levi-form",
    "strain-saturation",
    "fluid-dynamics",
    "navier-stokes",
    "blowup",
    "millennium-problem",
  ],
});
