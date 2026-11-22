import { remark } from "../../schema/builders";

export default remark({
  authorNotes: [
    {
      kind: "caveat",
      date: "2026-10-13",
      body:
        "**Re-scoped (owner decision 2026-10-13, Q1: $\\varTheta = f\\,\\xi^\\flat$).** " +
        "This block previously called $\\kappa^2 = V_2/V_1$ the *squared Levi " +
        "condition number* and read $\\kappa^2 \\to 0$ as \"the Levi form is " +
        "strictly degenerate at the collision locus; the local cohomology group " +
        "vanishes … the system maintains global regularity — branch (B) under the " +
        "point-vortex assumption\". Under the re-scope the Levi datum of " +
        "$\\ker\\varTheta = \\xi^\\perp$ is the scalar $\\xi\\cdot\\mathrm{curl}\\,\\xi$ " +
        "and there is no condition number in dimension 3. $\\kappa^2$ is kept as " +
        "what it is, the squared core aspect ratio of the Townsend covariance, and " +
        "every computed result stands: the ODE pair, the closed form, and " +
        "`kappa_squared_tends_to_zero` (sorry-free). Removed: the identification " +
        "with a Levi condition number, and the inference from flattening to " +
        "degeneracy, vanishing cohomology and regularity. For a straight pair the " +
        "Levi scalar is $0$ for every core shape. The overlap breakdown paragraph is " +
        "unchanged. Audit: `docs/audits/2026-10-12-ns-v1-geometric-depletion.md` §3.3.",
      see: "../../../docs/audits/2026-10-12-ns-v1-geometric-depletion.md",
    },
    { kind: "note", body: "Lean sibling: archimedean specialisation over $\\mathbb{R}$ (AGENTS.md §7c). Underlying combinatorial content stays generic to any commutative ring with the same $q$-data." },
  ],
  interprets: "conj:levi-degeneracy",
  label: "rem:townsend-biot-savart-strain",
  title:
    "Townsend evolution under Biot--Savart strain: the first-order core flattening $\\kappa \\to 0$",
  uses: ["prop:core-levi-form"],
  cites: ["townsend1951", "saffman1992", "moffatt1994"],
  tags: [
    "townsend",
    "biot-savart",
    "vortex-core",
    "levi-form",
    "strain",
    "fluid-dynamics",
    "navier-stokes",
    "millennium-problem",
  ],
});
