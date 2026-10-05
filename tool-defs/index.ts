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

export function tools(baseUrl?: string): ToolDefinition[] {
  return [refreshPlanTool(baseUrl), leanRegenCheckTool(baseUrl), ...producerTools(baseUrl)];
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
