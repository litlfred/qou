/**
 * wire-figures — bulk-wire authored SVGs into their target .md
 * blocks per the mapping below.  For each entry, appends a
 * markdown image embed at the END of the target .md (just before
 * any trailing whitespace), with the alt-text taken from the SVG's
 * .prompt.md title.
 *
 * Idempotent: skips entries whose target .md already references
 * the SVG (so re-running is safe).
 *
 * Run:
 *   bun run content/pipeline/wire-figures.ts
 *
 * @module content/pipeline/wire-figures
 */

import { readFileSync, writeFileSync, existsSync } from "fs";
import { join, dirname, relative } from "path";

const REPO_ROOT = join(import.meta.dir, "..", "..");
const CONTENT_ROOT = join(REPO_ROOT, "content", "quantum-observable-universe");

/**
 * Mapping: SVG slug → target `.md` path (relative to CONTENT_ROOT).
 * The SVG must live in the same chapter's `rendered/` directory as
 * the target .md (so the embed path becomes `rendered/<slug>.svg`).
 */
const MAP: Array<[string, string]> = [
  // Already wired by hand:
  // ["roadmap-flow-A",                "introduction/roadmap-diagram.md"],
  // ["r-matrix-skein-0",              "braids-and-knots/braid-action-tensor.md"],

  // Introduction
  ["three-fold-triangle-0",         "introduction/intro.md"],

  // Quantum universes
  ["frobenius-snake-0",             "quantum-universes/frobenius-pairing.md"],
  ["tannaka-krein-triangle-0",      "quantum-universes/tannaka-krein-overview.md"],

  // Quantum observable universes
  ["qu-to-qou-funnel-0",            "quantum-observable-universes/quantum-observable-universe.md"],
  ["dirac-square-blocks-0",         "quantum-observable-universes/dq-squared-proof.md"],
  ["instanton-self-dual-0",         "quantum-observable-universes/categorical-instanton.md"],

  // Lifting and descent
  ["brane-tower-stack-0",           "lifting-and-descent/recursive-brane-tower.md"],
  ["jet-prolongation-ladder-0",     "lifting-and-descent/jet-prolongation.md"],
  ["yekutieli-staircase-0",         "lifting-and-descent/yekutieli-lifting.md"],
  ["cosimplicial-descent-0",        "lifting-and-descent/cosimplicial-intro.md"],

  // Braids and knots
  ["particle-knot-dictionary-0",    "braids-and-knots/intro.md"],
  ["markov-closure-0",              "braids-and-knots/hadron-interpretation.md"],
  ["borromean-quarks-0",            "braids-and-knots/confined-particle.md"],
  ["lp-active-set-0",               "braids-and-knots/knot-operator-lp-selection.md"],
  ["mobius-pairing-0",              "braids-and-knots/mobius-energy-frobenius-kernel-proof.md"],
  ["schur-weyl-bose-fermi-0",       "braids-and-knots/categorical-boson-fermion.md"],
  ["mass-decomposition-0",          "braids-and-knots/atom-knot-mass-derivation.md"],
  ["knot-complement-rho-0",         "braids-and-knots/knot-complement-group.md"],
  ["crossing-energy-staircase-0",   "braids-and-knots/topological-mass-cat-transient-proof.md"],
  ["shell-closure-spectrum-0",      "braids-and-knots/shell-closure-stability.md"],

  // Models of QOUs
  ["ym-mass-gap-0",                 "models-of-qous/yang-mills-mass-gap.md"],

  // Algebraic substrate
  ["frobenius-hopf-cake-0",         "algebraic-substrate/frobenius-hopf-substrate.md"],
  ["spectral-trace-loop-0",         "algebraic-substrate/spectral-trace-intro.md"],
  ["s5-permutohedron-0",            "algebraic-substrate/magic-numbers-bring.md"],

  // Descartes universe
  ["bring-coral-3-tubes-0",         "descartes-universe/brings-surface.md"],
  ["color-tube-coords-0",           "descartes-universe/color-tube-coordinates.md"],
  ["exceptional-divisor-borromeans-0", "descartes-universe/down-quark.md"],
  ["descartes-polytope-0",          "descartes-universe/descartes-condition.md"],
  ["bring-power-sums-0",            "descartes-universe/brings-surface-example.md"],
  ["beta-decay-tower-0",            "descartes-universe/beta-decay-skein.md"],

  // Fluid dynamics
  ["q-vortex-spectrum-0",           "fluid-dynamics/geodesic-vortices.md"],
  ["madelung-decomposition-0",      "fluid-dynamics/madelung-fluid.md"],
  ["ns-obstruction-blowup-0",       "fluid-dynamics/ns-obstruction.md"],
  ["q-kolmogorov-0",                "fluid-dynamics/braid-fluid.md"],

  // Information theory
  ["regime-scale-0",                "information-theory/regime-table.md"],
  ["emergent-gravity-0",            "information-theory/emergent-gravity-info.md"],
  ["planck-time-cell-0",            "information-theory/planck-time.md"],

  // Particle interactions
  ["gs-reduction-tree-0",           "particle-interactions/nuclear-groebner-reduction.md"],

  // Observations
  ["substrate-consistency-window-0", "observations/substrate-consistency-window.md"],
  ["calibration-triangle-0",        "observations/three-calibration-discipline.md"],
  ["predicted-vs-codata-0",         "observations/atom-mass-full-hecke.md"],

  // Molecular construction
  ["h2-shared-trefoil-0",           "molecular-construction/h2-molecular-braid.md"],
  ["molecular-progression-0",       "molecular-construction/molecular-braid.md"],
  ["ch4-tetrahedron-symmetry-0",    "molecular-construction/ch4-tetrahedral-symmetry.md"],

  // Organic chemistry
  ["carbon-half-filled-0",          "organic-chemistry/carbon-valence.md"],
  ["threading-link-benzene-0",      "organic-chemistry/threading-link.md"],
  ["chain-vs-ring-0",               "organic-chemistry/chain-ring-comparison.md"],
  ["benzene-aromaticity-0",         "organic-chemistry/benzene-ring.md"],

  // Appendices
  ["knot-periodic-table-0",         "appendix-knot-periodic-table/knot-periodic-table.md"],
  ["knot-operations-grid-0",        "appendix-knot-operations/hecke-operations.md"],
  ["transfer-block-diagonal-0",     "appendix-transfer-matrices/tm-general-form.md"],
];

function readTitle(promptPath: string): string {
  if (!existsSync(promptPath)) return "";
  const raw = readFileSync(promptPath, "utf-8").replace(/\r/g, "");
  const m = raw.match(/^#\s+(.+?)\s*$/m);
  return m ? m[1].trim() : "";
}

let wired = 0;
let skipped = 0;
let missing = 0;

for (const [slug, mdRel] of MAP) {
  const mdPath = join(CONTENT_ROOT, mdRel);
  if (!existsSync(mdPath)) {
    console.warn(`  ⚠  ${slug} → ${mdRel}: target .md not found`);
    missing++;
    continue;
  }
  const chapterDir = dirname(mdPath);
  const svgPath = join(chapterDir, "rendered", `${slug}.svg`);
  if (!existsSync(svgPath)) {
    console.warn(`  ⚠  ${slug}: SVG not found at ${relative(REPO_ROOT, svgPath)}`);
    missing++;
    continue;
  }
  const md = readFileSync(mdPath, "utf-8");
  if (md.includes(`rendered/${slug}.svg`)) {
    skipped++;
    continue;
  }
  const promptPath = join(chapterDir, "rendered", `${slug}.prompt.md`);
  const title = readTitle(promptPath);
  const altText = title || slug;
  const imgRef = `\n\n![${altText}.](rendered/${slug}.svg)\n`;
  // Append at end of file, ensuring exactly one blank line before
  const trimmed = md.replace(/\s+$/, "");
  writeFileSync(mdPath, trimmed + imgRef);
  console.log(`  ✓  ${slug}  →  ${mdRel}`);
  wired++;
}

console.log(`\nWired ${wired} figure(s); skipped ${skipped} (already wired); ${missing} missing.`);
