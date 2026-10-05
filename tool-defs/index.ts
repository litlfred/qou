/**
 * qou's Tool nodes: one per computation script that a content block wires to a
 * witness. Each Tool's output is that witness, a `computation-witness` node.
 *
 * Story TOOLS T5 (bean `qou-a3l1`) and the owner's ruling of 2026-10-04:
 * *"all witnesses tools will need to go into the KG"*.
 *
 * ## Why this directory is `tool-defs/`, not `tools/`
 *
 * qou's `tools/` holds its Rust and Python packages (`pyhecke`,
 * `qou-substrate`, `hecke-engine`, …), and renaming it would touch 601 files,
 * including paper content and every producer's script hash. The owner ruled on
 * 2026-10-05 (option A on bean `qou-kbqy`) to declare the Tool graph at a new
 * path instead; `qou.json` declares this directory with the `tools` graph kind.
 *
 * ## Generated, never hand-listed
 *
 * The producers come from `producers.json`, which `scripts/gen-producer-tools.ts`
 * writes from the block manifests' `computation: { script, witness }` fields.
 * A producer whose script is not in the tree, or that names no witness, gets no
 * Tool; the generator reports both counts as findings.
 *
 * A Tool here only DECLARES how to run a producer; nothing runs at load. To
 * check that running one still reproduces its witness, use the platform's
 * `witness-parity` Tool.
 */
import { readFileSync } from "node:fs";
import { join } from "node:path";
import { defineTool, type ToolDefinition } from "../folio-assistant/cat-harness/schemas/tool.js";
import { toolTypeIri } from "../folio-assistant/cat-harness/schemas/tool-types.js";

interface Producer {
  script: string;
  witnesses: string[];
  blocks: string[];
  scriptExists: boolean;
}

/** `computations/qbeta/foo_bar.py` → `produce-qbeta-foo-bar`. */
export function toolId(script: string): string {
  const stem = script.replace(/^computations\//, "").replace(/\.py$/, "");
  return `produce-${stem.replace(/[^A-Za-z0-9]+/g, "-").replace(/^-|-$/g, "").toLowerCase()}`;
}

export function producers(): Producer[] {
  const raw = JSON.parse(readFileSync(join(import.meta.dir, "producers.json"), "utf8")) as { producers: Producer[] };
  return raw.producers.filter((p) => p.scriptExists && p.witnesses.length > 0);
}

/**
 * The first step of `processes/content/witness-refresh.bpmn`: list the
 * producers a refresh would run, writing nothing. It wraps the existing
 * `computations/run_pipeline.py --dry-run --content-only` rather than
 * re-deriving the list, so the plan and the runner cannot disagree.
 */
export function refreshPlanTool(baseUrl?: string): ToolDefinition {
  return defineTool({
    id: "witness-refresh-plan",
    title: "Plan a witness refresh",
    description:
      "List the content-wired computation scripts a witness refresh would run, without running any of them or writing a witness. " +
      "Wraps `computations/run_pipeline.py --dry-run --content-only`. The first activity of `processes/content/witness-refresh.bpmn`; " +
      "the refresh itself waits on the owner's approval in that process.",
    install: { none: true },
    invoke: { shell: "python3 computations/run_pipeline.py --dry-run --content-only" },
    io: { inputs: [], outputs: [] },
    satisfies: ["compute-audit"],
    requires: { runtime: ["python3"], network: false },
  });
}

/**
 * The check of `processes/content/lean-regenerate-and-diff.bpmn` (TOOLS T9):
 * regenerate the machine-written Lean in memory and diff it against the
 * committed files. Exit 0 identical, 1 drift, 2 unknown (a generator could
 * not run); it writes nothing.
 */
export function leanRegenCheckTool(baseUrl?: string): ToolDefinition {
  return defineTool({
    id: "lean-regenerate-check",
    title: "Check the generated Lean is in sync",
    description:
      "Regenerate the machine-written Lean in memory with `scripts/gen-gluing-lean.py` (every knot block of " +
      "`QOU/Knot/GeneratedGluing.lean`) and `scripts/gen-hecke-corner-column.py 3` (`BokutShiaoCornerDepth3` in " +
      "`UGB/GrobnerShirshov/HeckeCompletion.lean`), and diff each against the committed text. Exit 0 identical, " +
      "1 drift (with a unified diff), 2 unknown when a generator cannot run — never reported as a pass. Writes nothing.",
    install: { none: true },
    invoke: { shell: "python3 scripts/check-generated-lean.py" },
    io: { inputs: [], outputs: [] },
    satisfies: ["lean-generation"],
    requires: { runtime: ["python3"], network: false },
  });
}

/**
 * TOOLS T14 (bean `qou-ll3i`): the generator that keeps `qou-mass`'s vendored
 * `_internal/` modules equal to their `computations/` sources.
 *
 * `downstream`, not `maintains`: `maintains` names a PUBLISHED artefact that
 * `check:maintained-artefacts` looks for in `_site/`, and `_internal/` is a
 * committed package directory the site never carries (schemas/tool.ts,
 * "Why this is not `maintains`"). The drift gate is the compute-QA gate
 * `qou-mass-vendor-drift`, which runs `--check` and writes nothing. Running
 * this Tool regenerates the copies, which waits on the owner (TOOLS report
 * §5.7), so it is declared here and is not part of any automatic process.
 */
export function qouMassVendorSyncTool(): ToolDefinition {
  return defineTool({
    id: "qou-mass-vendor-sync",
    title: "Regenerate qou-mass's vendored modules",
    description:
      "Regenerate `qou-mass/src/qou_mass/_internal/` from the `computations/` modules it vendors, flattening the " +
      "directory layout and dropping `import _path_bridge`; nothing else is rewritten. `--check` (exit 1 on drift) is " +
      "the compute-QA gate `qou-mass-vendor-drift`; this Tool is the `--apply` that fixes the drift, and it needs " +
      "the owner's approval because it rewrites the vendored copies.",
    install: { none: true },
    invoke: { shell: "python3 scripts/sync-qou-mass-vendor.py --apply" },
    io: { inputs: [], outputs: [] },
    satisfies: ["compute-audit"],
    requires: { runtime: ["python3"], network: false },
    downstream: {
      output: "qou-mass/src/qou_mass/_internal",
      inputs: ["scripts/sync-qou-mass-vendor.py", "computations"],
      judgedAt: "checkout",
    },
  });
}

/**
 * C9 story B2 (issue #7528): is the committed `references.bib` what the
 * CSL-JSON bibliography generates? Regenerates into a temp file and compares,
 * ignoring only the `% Generated:` timestamp. Writes nothing in the tree.
 */
export function referencesBibCheckTool(): ToolDefinition {
  return defineTool({
    id: "references-bib-check",
    title: "Check references.bib against the bibliography",
    description:
      "Regenerate `references.bib` from `folio/schema/references.ts` with the platform's `export-bibtex.ts` into a temp " +
      "file and compare it with the committed copy, ignoring the `% Generated:` timestamp line. Exit 0 current, 1 drift " +
      "(with the first differing line), 2 could not run. Writes nothing in the tree; regenerating the committed file is " +
      "a separate, deliberate step.",
    install: { none: true },
    invoke: { shell: "bun run scripts/check-references-bib.ts" },
    io: { inputs: [], outputs: [] },
    satisfies: ["bib-qa"],
    requires: { runtime: ["bun"], network: false },
  });
}

interface ComputeQaGate {
  id: string;
  node: string;
  title: string;
  mode: "strict" | "warn" | "advisory";
  diff: boolean;
  setup: string | null;
  command: string;
}

/**
 * One Tool per compute-QA gate (TOOLS T7, bean `qou-4dj1`), from
 * `compute-qa-gates.json`, which `scripts/compute-qa.py --write-tool-defs`
 * generates from the runner's own table. The activity each gate belongs to is
 * named in `processes/tools/compute-qa.bpmn`.
 */
export function computeQaTools(): ToolDefinition[] {
  const raw = JSON.parse(readFileSync(join(import.meta.dir, "compute-qa-gates.json"), "utf8")) as { gates: ComputeQaGate[] };
  return raw.gates.map((g) =>
    defineTool({
      id: `compute-qa-${g.id}`,
      title: `compute-QA: ${g.title}`,
      description:
        `Run the compute-QA gate \`${g.id}\` (${g.mode}), activity \`${g.node}\` of processes/tools/compute-qa.bpmn: ` +
        `\`${g.command}${g.diff ? " <changed .py files>" : ""}\`. ` +
        "Writes its verdict to test/results/compute-qa/ (gitignored; published with qa:publish). " +
        (g.setup ? `Needs setup first: ${g.setup}.` : "Needs no setup."),
      install: { none: true },
      invoke: { shell: `python3 scripts/compute-qa.py --gate ${g.id}${g.diff ? " --base origin/main" : ""}` },
      io: { inputs: [], outputs: [] },
      satisfies: ["compute-audit"],
      requires: { runtime: g.command.startsWith("bun ") ? ["python3", "bun"] : ["python3"], network: false },
    }),
  );
}

export function tools(baseUrl?: string): ToolDefinition[] {
  return [refreshPlanTool(baseUrl), leanRegenCheckTool(baseUrl), qouMassVendorSyncTool(), referencesBibCheckTool(), ...computeQaTools(), ...producerTools(baseUrl)];
}

function producerTools(baseUrl?: string): ToolDefinition[] {
  const B = baseUrl ?? "";
  const t = (n: Parameters<typeof toolTypeIri>[1]): string => toolTypeIri(B, n);
  return producers().map((p) =>
    defineTool({
      id: toolId(p.script),
      title: `Produce ${p.witnesses.length === 1 ? p.witnesses[0]!.replace(/^.*\//, "") : `${p.witnesses.length} witnesses`}`,
      description:
        `Run the computation \`${p.script}\`, which writes ${p.witnesses.map((w) => `\`${w}\``).join(", ")}. ` +
        `Wired from ${p.blocks.length} content block(s): ${p.blocks.map((b) => `\`${b}\``).join(", ")}. ` +
        "Declared from the block manifests by scripts/gen-producer-tools.ts; check that a run reproduces the committed witness with the platform's `witness-parity` Tool.",
      install: { none: true },
      invoke: { shell: `python3 -u ${p.script}` },
      io: {
        inputs: [],
        outputs: p.witnesses.map((w) => ({
          name: w.replace(/^.*\//, "").replace(/\.witness\.json$/, ""),
          schema: t("RepoPath"),
          description: `\`${w}\`, a computation-witness node.`,
        })),
      },
      satisfies: ["compute-integration-watcher"],
      requires: { runtime: ["python3"], network: false },
      downstream: { output: p.witnesses[0]!, inputs: [p.script], judgedAt: "checkout" },
    }),
  );
}
