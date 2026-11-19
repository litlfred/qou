#!/usr/bin/env bun
/**
 * QOU Claude Adversarial Red-Team & Agentic Monograph QA Runner
 * (`scripts/claude-redteam-and-qa.ts`)
 *
 * Uses the existing `@anthropic-ai/sdk` installation in
 * `folio-assistant/cat-harness-tools` with:
 *   1. **Anthropic Prompt Caching** (`cache_control: { type: "ephemeral" }`) on
 *      the shared QOU Adversarial Red-Team & Milnor-Voice QA System Rubrics,
 *   2. **Anthropic Message Batches API** (`client.messages.batches`) for 50%
 *      cost reduction across multi-file Lean / compute / prose audits.
 *
 * Subcommands:
 *   - `redteam-lean <lean-or-probe-paths...> [--md <path>] [--probe <path>] [--model <id>] [--out <json>] [--dry-run]`
 *   - `qa-prose <chapter-or-md-paths...> [--model <id>] [--out <json>] [--dry-run]`
 *   - `batch-submit --mode <redteam-lean|qa-prose> <paths...> [--model <id>] [--dry-run]`
 *   - `batch-collect <batchId> [--out <json>]`
 *
 * Zero-credit safety:
 *   - `--help` works without `ANTHROPIC_API_KEY`.
 *   - `--dry-run` builds and validates the exact Anthropic payload (including
 *     ephemeral cache breakpoints and paired companion files) and prints a
 *     summary without making any network calls.
 */

import { existsSync, mkdirSync, readdirSync, readFileSync, statSync, writeFileSync } from "fs";
import { basename, dirname, extname, join, relative, resolve } from "path";
import { getAnthropic } from "../folio-assistant/cat-harness-tools/src/core/anthropic.ts";

const QOU_ROOT = resolve(import.meta.dir, "..");
const BATCH_CACHE_DIR = join(QOU_ROOT, ".cache", "claude-batches");

const DEFAULT_REDTEAM_MODEL = "claude-opus-4-6";
const DEFAULT_QA_MODEL = "claude-sonnet-4-6";

// ── Shared Ephemeral-Cached System Rubrics (>4096 chars so caching activates on all Claude 4.x models) ──

const REDTEAM_LEAN_SYSTEM_RUBRIC = `You are the Principal Adversarial Red-Team Auditor for the Quantum Observable Universe (QOU) mathematical physics monograph and Lean 4 formalization corpus.

Your mission is to perform an uncompromising, line-anchored formal and numerical red-team audit of each submitted Lean 4 module, its companion Python/mpmath compute probe (and witness JSON if present), and its corresponding monograph prose block (.md).

### NON-NEGOTIABLE QOU CORPUS INVARIANTS (RED-TEAM CHECKLIST)

1. **ZERO FITTING / ZERO POST-HOC PARAMETER SELECTION AGAINST CODATA OR AME2020 (CRITICAL)**:
   - Every physical prediction in QOU must be a parameter-free algebraic, representation-theoretic, or topological function of the substrate parameter \`q_0\` and the two calibration anchors (\`m_e\`, \`m_p\` or \`m_mu\`).
   - Check whether any rational coefficient, exponent, sign, or branch choice in the Python probe or Lean theorem was inverted from CODATA/AME2020 experimental targets (e.g., solving for a coefficient \`c_k\` from \`Q_codata / Q_pred - 1\` and presenting it as a derived prediction).
   - If a probe evaluates a pre-registered family of parameter-free candidates (such as Kohno-Drinfeld full-twist framing \`C_KD^{(k)}(q) = (q^k + q^{-k})/2\`, GPMT modified-trace completions \`tr_M^{z_D} \\mp t_D^{(1^3)}\`, Wedderburn / Jucys-Murphy content moments, or the 4 parameter-free Cartan QED weightings \`'plain'\`, \`'KnKp'\`, \`'Kp3'\`, \`'q'\`), verify that ALL candidates are reported honestly with their exact residuals and that open gaps remain explicitly flagged rather than tuned away.

2. **ZERO FLOAT64 / BINARY64 CONTAMINATION (CRITICAL)**:
   - Every Python compute probe must execute at high-precision MPFR/mpmath arithmetic (\`set_compute_dps(50)\` or \`60\` or \`80\` at module scope).
   - Flag ANY occurrence of \`float(\`, binary64 literals passed into \`mp.mpf(0.123)\`, \`math.sqrt\`, \`math.cos\`, or float64 intermediate conversions.

3. **ZERO LEAN 4 VACUITY, DEFINITION-COLLAPSE, OR BORROWED-NAME LAUNDERING (CRITICAL)**:
   - **No \`sorry\` or \`axiom\`**: Any \`sorry\`, \`axiom\`, or \`admit\` is an automatic \`FAIL\`.
   - **Hypothesis Satisfiability at Physical \`q_0 \\approx 1.10997858 > 1\`**: Check every hypothesis of every \`theorem\` and \`lemma\`. Are all denominator non-vanishing hypotheses (\`q \\neq 0\`, \`q^2 + 1 \\neq 0\`, \`q^4 + q^2 + 1 \\neq 0\`, \`q > 1\`) genuinely satisfied at \`q_0 > 1\`? Flag any contradictory hypothesis pair that makes a theorem vacuously true!
   - **No Definition-Collapsed Tautologies**: Flag any definition where the right-hand side is defined as a constant or already-simplified target and the theorem merely proves \`f x = target\` by \`rfl\` while claiming a non-trivial physical derivation in the docstring.
   - **No Borrowed-Name / Symbol-Collision Laundering**: Verify that every defined symbol satisfies the true mathematical defining conditions of its name (e.g., distinguishing the retracted non-Markov coefficient \`1/2 - z_D\` from the true Convention-D Wedderburn weight \`w_{(2,1)}(z_D) = q^2/(q^2+1)^2\`, and distinguishing the unprojected D-frame phase \`alpha_D\` from the mirror-covariant bar-odd projection \`alpha_D^{proj} = alpha_D - h^2/4\`).

4. **CONVENTION-D & TWO-TERM QED CONSISTENCY (MAJOR)**:
   - Convention C (\`z_C = \\sqrt{q}/(1+q)\`) was excised by owner ruling (2026-08-09 / 2026-08-15); Convention D (\`z_D = q^3/(q^2+1)\`, where \`w_{(1^3)}(z_D) = 0\`) is canonical across both mass and decay channels.
   - If Convention C appears, it must be explicitly labeled as an excised comparison baseline, never as canonical.
   - When the two-term Borromean \`V^3\` QED proton pin \`q_{2t}\` (\`m_p^{QCD}(q_{2t}) + M_p^{QED,conn}(q_{2t}) = m_p^{CODATA}\`) is used, check that the proton QED self-energy \`+M_p^{QED,conn}\` is included consistently in \`m_n = m_p + m_e + Q_\\beta\` so it is not double-subtracted.

5. **SPEC-VS-PROSE & WITNESS FIDELITY (MAJOR)**:
   - Verify that every polynomial numerator, denominator, power of \`q\`, and sign in the Lean 4 theorems matches the Python compute probe and the prose docstrings character-for-character.

### REQUIRED JSON OUTPUT SCHEMA
Respond ONLY with a single valid JSON object (no markdown fences outside the JSON) matching this structure:
{
  "target": "<primary file path>",
  "companions": ["<companion path 1>", "..."],
  "verdict": "PASS" | "CONDITIONAL" | "FAIL",
  "scores": {
    "no_fitting": "PASS" | "WARN" | "FAIL",
    "no_float64": "PASS" | "WARN" | "FAIL",
    "lean_non_vacuity": "PASS" | "WARN" | "FAIL",
    "spec_prose_fidelity": "PASS" | "WARN" | "FAIL"
  },
  "summary": "<2-3 sentence executive verdict>",
  "findings": [
    {
      "severity": "CRITICAL" | "MAJOR" | "MINOR" | "NIT",
      "category": "NO_FITTING" | "NO_FLOAT64" | "LEAN_VACUITY" | "CONVENTION_D" | "FIDELITY",
      "file": "<relative file path>",
      "line": <line number or null>,
      "symbol": "<theorem or function name>",
      "detail": "<precise technical finding and required fix if any>"
    }
  ]
}`;

const QA_PROSE_SYSTEM_RUBRIC = `You are the Principal Monograph Editor and Mathematical Physics QA Auditor for the Quantum Observable Universe (QOU) folio.

Your task is to audit submitted monograph prose blocks (\`.md\`) and chapter manifests (\`.ts\`) for mathematical consistency, Convention-D & Two-Term QED alignment, ValueRegistry discipline, and Milnor-style monograph voice.

### NON-NEGOTIABLE QOU MONOGRAPH QA RUBRIC

1. **STALE CONVENTION-C OR ONE-TERM FORMULA DRIFT (CRITICAL)**:
   - Flag any prose passage that still presents Convention C (\`z = \\sqrt{q}/(1+q)\` or the retracted non-Markov weight vector \`(z, 1/2 - z, z)\`) as canonical without noting the 2026-08-15 Convention-D ruling (\`z_D = q^3/(q^2+1)\`, \`w_{(3)}(z_D) = (q^4+1)/(q^2+1)^2\`, \`w_{(2,1)}(z_D) = q^2/(q^2+1)^2\`, \`w_{(1^3)}(z_D) = 0\`).
   - Flag any passage claiming \`1/2 - z_D\` is a Wedderburn weight (it fails Markov conditions \`h2\` and \`h3\`).
   - Check whether discussions of the \`\\mu\\text{--}p\` tension (\`211.2\\text{ ppb}\` at the 1-term proton pin) or \`Q_\\beta\` / \`m_n\` residuals reflect or properly cross-reference the parameter-free two-term connected 4th-order Borromean \`V^3\` QED correction (\`M_p^{QED,conn} = +220.08\\text{ eV}\`, \`\\Delta m_{QED}^{conn} = -331.70\\text{ eV}\`) and the GPMT \`(1^3)\` modified-trace / Kohno-Drinfeld full-twist framing bridges where relevant.

2. **HARDCODED NUMERICAL PREDICTIONS BYPASSING VALUEREGISTRY (MAJOR)**:
   - Flag raw hardcoded multi-digit decimal predictions in prose tables or inline math that are not backed by a named witness JSON or \`ValueRegistry\` macro.

3. **MILNOR MONOGRAPH VOICE & EPISTEMIC HONESTY (MAJOR)**:
   - QOU prose must read like John Milnor's *Topology from the Differentiable Viewpoint* or *Characteristic Classes*: crisp definitions, explicit hypotheses, clear separation between proved theorems (\`0 sorry\`, \`0 axiom\`), scope-(a)/(b) negative exclusions, and open conjectures.
   - Flag any meta-commentary, PR/commit/bean changelog chatter inside reader-facing monograph prose (belongs in audit docs or code comments, not the book!), or overstated claims where an open conjecture is phrased as a closed derivation.

4. **UNDEFINED SYMBOLS & BROKEN CROSS-REFERENCES (MINOR)**:
   - Flag LaTeX macros or notation used before definition or inconsistent with the QOU notation register (\`h = q - q^{-1}\`, \`\\hbar_q = (q-1)/q = 1 - q^{-1}\`, \`[n]_q = (q^n - q^{-n})/(q - q^{-1})\`).

### REQUIRED JSON OUTPUT SCHEMA
Respond ONLY with a single valid JSON object (no markdown fences outside the JSON) matching this structure:
{
  "target": "<primary file path>",
  "verdict": "PASS" | "CONDITIONAL" | "FAIL",
  "scores": {
    "convention_d_alignment": "PASS" | "WARN" | "FAIL",
    "value_registry_discipline": "PASS" | "WARN" | "FAIL",
    "milnor_voice_and_honesty": "PASS" | "WARN" | "FAIL",
    "notation_consistency": "PASS" | "WARN" | "FAIL"
  },
  "summary": "<2-3 sentence executive QA summary>",
  "findings": [
    {
      "severity": "CRITICAL" | "MAJOR" | "MINOR" | "NIT",
      "category": "CONVENTION_DRIFT" | "HARDCODED_NUMBER" | "VOICE_VIOLATION" | "NOTATION",
      "file": "<relative file path>",
      "line": <line number or null>,
      "detail": "<precise issue description>",
      "suggested_edit": "<concise replacement text if applicable>"
    }
  ]
}`;

// ── File Discovery & Companion Pairing ──────────────────────────────────────

interface AuditUnit {
  id: string;
  primaryPath: string;
  companionPaths: string[];
  mode: "redteam-lean" | "qa-prose";
}

function numberLines(content: string): string {
  return content
    .split(/\r?\n/)
    .map((line, idx) => `${String(idx + 1).padStart(4, " ")}: ${line}`)
    .join("\n");
}

function discoverCompanionsForLean(leanAbsPath: string, explicitMd?: string, explicitProbe?: string): string[] {
  const companions: string[] = [];
  if (explicitProbe) {
    const p = resolve(QOU_ROOT, explicitProbe);
    if (existsSync(p)) companions.push(p);
  }
  if (explicitMd) {
    const m = resolve(QOU_ROOT, explicitMd);
    if (existsSync(m)) companions.push(m);
  }

  // Parse docstrings in the Lean file for `Compute companion:` or `Witness:` or `computations/...`
  try {
    const text = readFileSync(leanAbsPath, "utf-8");
    const pathMatches = text.match(/computations\/[A-Za-z0-9_./-]+\.(?:py|json)/g) ?? [];
    for (const rel of pathMatches) {
      const abs = resolve(QOU_ROOT, rel);
      if (existsSync(abs) && !companions.includes(abs)) {
        companions.push(abs);
      }
    }
    const mdMatches = text.match(/folio\/quantum-observable-universe\/[A-Za-z0-9_./-]+\.md/g) ?? [];
    for (const rel of mdMatches) {
      const abs = resolve(QOU_ROOT, rel);
      if (existsSync(abs) && !companions.includes(abs)) {
        companions.push(abs);
      }
    }
  } catch {
    // ignore read error
  }
  return companions;
}

function expandTargetPaths(rawPaths: string[], mode: "redteam-lean" | "qa-prose"): string[] {
  const out: string[] = [];
  const exts = mode === "redteam-lean" ? new Set([".lean", ".py"]) : new Set([".md"]);

  function walk(p: string) {
    if (!existsSync(p)) {
      throw new Error(`Path does not exist: ${p}`);
    }
    const st = statSync(p);
    if (st.isFile()) {
      out.push(p);
      return;
    }
    if (st.isDirectory()) {
      for (const entry of readdirSync(p).sort()) {
        if (entry.startsWith(".") || entry === "node_modules" || entry === ".lake") continue;
        const child = join(p, entry);
        const cst = statSync(child);
        if (cst.isDirectory()) {
          walk(child);
        } else if (exts.has(extname(entry))) {
          out.push(child);
        }
      }
    }
  }

  for (const raw of rawPaths) {
    walk(resolve(QOU_ROOT, raw));
  }
  return Array.from(new Set(out));
}

function buildAuditUnits(
  rawPaths: string[],
  mode: "redteam-lean" | "qa-prose",
  explicitMd?: string,
  explicitProbe?: string,
): AuditUnit[] {
  const files = expandTargetPaths(rawPaths, mode);
  return files.map((absPath, idx) => {
    const rel = relative(QOU_ROOT, absPath);
    const slug = rel
      .replace(/[^A-Za-z0-9_-]/g, "_")
      .replace(/_+/g, "_")
      .slice(-54);
    const id = `qou_${idx}_${slug}`.slice(0, 64);
    const companions =
      mode === "redteam-lean" ? discoverCompanionsForLean(absPath, explicitMd, explicitProbe) : [];
    return {
      id,
      primaryPath: absPath,
      companionPaths: companions,
      mode,
    };
  });
}

function buildUserPromptForUnit(unit: AuditUnit): string {
  const relPrimary = relative(QOU_ROOT, unit.primaryPath);
  const primaryText = readFileSync(unit.primaryPath, "utf-8");

  const parts: string[] = [
    `### PRIMARY TARGET FILE: \`${relPrimary}\``,
    "```",
    numberLines(primaryText),
    "```",
  ];

  for (const comp of unit.companionPaths) {
    const relComp = relative(QOU_ROOT, comp);
    const raw = readFileSync(comp, "utf-8");
    // Truncate very large witness JSONs to keep token budget sharp while preserving assertions & header
    const clipped =
      comp.endsWith(".json") && raw.length > 18000
        ? raw.slice(0, 9000) + "\n... [TRUNCATED MIDDLE OF WITNESS JSON] ...\n" + raw.slice(-7000)
        : raw;
    parts.push(`### COMPANION FILE: \`${relComp}\``, "```", numberLines(clipped), "```");
  }

  parts.push(
    unit.mode === "redteam-lean"
      ? "Perform the full QOU Adversarial Red-Team Audit on the primary target and its companions, and return ONLY the required JSON object."
      : "Perform the full QOU Monograph Prose QA Audit on the primary target, and return ONLY the required JSON object.",
  );

  return parts.join("\n\n");
}

function buildAnthropicMessageParams(unit: AuditUnit, model: string) {
  const systemText = unit.mode === "redteam-lean" ? REDTEAM_LEAN_SYSTEM_RUBRIC : QA_PROSE_SYSTEM_RUBRIC;
  const userText = buildUserPromptForUnit(unit);
  return {
    model,
    max_tokens: 4096,
    temperature: 0,
    system: [
      {
        type: "text" as const,
        text: systemText,
        cache_control: { type: "ephemeral" as const },
      },
    ],
    messages: [
      {
        role: "user" as const,
        content: userText,
      },
    ],
  };
}

// ── Environment & Anthropic Client Resolution ───────────────────────────────

function loadAnthropicApiKeyIfPresent(): string | undefined {
  if (process.env.ANTHROPIC_API_KEY && process.env.ANTHROPIC_API_KEY.trim() !== "") {
    return process.env.ANTHROPIC_API_KEY.trim();
  }
  const home = process.env.HOME || "";
  const keyFile = join(home, ".config", "anthropic", "key");
  if (existsSync(keyFile)) {
    const k = readFileSync(keyFile, "utf-8").trim();
    if (k) {
      process.env.ANTHROPIC_API_KEY = k;
      return k;
    }
  }
  const envFile = join(home, ".anthropic_env");
  if (existsSync(envFile)) {
    const lines = readFileSync(envFile, "utf-8").split(/\r?\n/);
    for (const line of lines) {
      const m = line.match(/^\s*(?:export\s+)?ANTHROPIC_API_KEY\s*=\s*["']?([^"'\s]+)["']?/);
      if (m && m[1]) {
        process.env.ANTHROPIC_API_KEY = m[1];
        return m[1];
      }
    }
  }
  return undefined;
}

function requireAnthropicClient(): NonNullable<ReturnType<typeof getAnthropic>> {
  const apiKey = loadAnthropicApiKeyIfPresent();
  const client = getAnthropic();
  if (!apiKey || !client) {
    console.error(
      "ERROR: ANTHROPIC_API_KEY is not set (checked process.env.ANTHROPIC_API_KEY, ~/.config/anthropic/key, and ~/.anthropic_env).\n" +
        "Tip: Use `--dry-run` to preview the exact request payload and prompt-cache structure without an API key.",
    );
    process.exit(1);
  }
  return client;
}

// ── Output Parsing & ASCII Table Rendering ──────────────────────────────────

function parseJsonResponse(rawText: string, fallbackTarget: string): any {
  const cleaned = rawText
    .trim()
    .replace(/^```(?:json)?\s*/i, "")
    .replace(/\s*```$/, "");
  try {
    return JSON.parse(cleaned);
  } catch {
    return {
      target: fallbackTarget,
      verdict: "CONDITIONAL",
      summary: "Model returned non-JSON response; raw output captured in raw_text.",
      raw_text: rawText,
      findings: [],
    };
  }
}

function renderVerdictTable(results: any[]) {
  console.log("\n" + "=".repeat(108));
  console.log("QOU CLAUDE ADVERSARIAL RED-TEAM & MONOGRAPH QA SUMMARY");
  console.log("=".repeat(108));
  console.log(
    `${"TARGET".padEnd(56)} | ${"VERDICT".padEnd(12)} | ${"FINDINGS".padEnd(10)} | SUMMARY`,
  );
  console.log("-".repeat(108));
  for (const r of results) {
    const tgt = String(r.target ?? "unknown").slice(-56).padEnd(56);
    const verdict = String(r.verdict ?? "UNKNOWN").padEnd(12);
    const findingsCount = Array.isArray(r.findings) ? r.findings.length : 0;
    const critCount = Array.isArray(r.findings)
      ? r.findings.filter((f: any) => f.severity === "CRITICAL").length
      : 0;
    const fLabel = `${findingsCount} (${critCount}C)`.padEnd(10);
    const sum = String(r.summary ?? "").replace(/\s+/g, " ").slice(0, 60);
    console.log(`${tgt} | ${verdict} | ${fLabel} | ${sum}`);
    if (Array.isArray(r.findings)) {
      for (const f of r.findings) {
        const loc = f.line ? `${f.file || r.target}:${f.line}` : `${f.file || r.target}`;
        console.log(`  [${f.severity || "INFO"}] (${f.category || "GEN"}) ${loc} — ${f.detail}`);
      }
    }
  }
  console.log("=".repeat(108) + "\n");
}

// ── CLI Option Parser & Help ────────────────────────────────────────────────

function printHelp() {
  console.log(`
QOU Claude Adversarial Red-Team & Agentic Monograph QA Runner
Usage:
  bun run scripts/claude-redteam-and-qa.ts <subcommand> [options] <paths...>

Subcommands:
  redteam-lean <paths...>   Adversarial red-team audit of Lean 4 modules + companion Python probes & witnesses
                            Checks: Zero fitting, Zero float64, Zero Lean vacuity/definition-collapse, Spec fidelity.
  qa-prose <paths...>       Semantic & Milnor-voice QA audit of monograph .md blocks
                            Checks: Convention-D & 2-term QED alignment, ValueRegistry discipline, Milnor voice.
  batch-submit <paths...>   Submit an Anthropic Message Batch (50% cost discount + ephemeral prompt caching)
                            Requires: --mode <redteam-lean|qa-prose>
  batch-collect <batchId>   Retrieve status/results of a submitted Message Batch and render summary table

Options:
  --mode <mode>             Mode for batch-submit: 'redteam-lean' or 'qa-prose'
  --model <model-id>        Anthropic model ID (default: ${DEFAULT_REDTEAM_MODEL} for redteam-lean, ${DEFAULT_QA_MODEL} for qa-prose)
  --md <path>               Explicit companion .md prose block for redteam-lean
  --probe <path>            Explicit companion Python compute probe for redteam-lean
  --out <json-path>         Write structured JSON report to disk
  --dry-run                 Build and validate exact Anthropic payloads + prompt-cache structure with zero API calls
  -h, --help                Show this help message
`);
}

interface ParsedArgs {
  subcommand: string;
  mode?: "redteam-lean" | "qa-prose";
  model?: string;
  md?: string;
  probe?: string;
  out?: string;
  dryRun: boolean;
  help: boolean;
  positionals: string[];
}

function parseArgs(argv: string[]): ParsedArgs {
  const res: ParsedArgs = {
    subcommand: "",
    dryRun: false,
    help: false,
    positionals: [],
  };

  let i = 0;
  while (i < argv.length) {
    const arg = argv[i]!;
    if (arg === "-h" || arg === "--help") {
      res.help = true;
      i++;
    } else if (arg === "--dry-run") {
      res.dryRun = true;
      i++;
    } else if (arg === "--mode" && i + 1 < argv.length) {
      const m = argv[i + 1]!;
      if (m !== "redteam-lean" && m !== "qa-prose") {
        throw new Error(`Invalid --mode ${m}; expected 'redteam-lean' or 'qa-prose'`);
      }
      res.mode = m;
      i += 2;
    } else if (arg === "--model" && i + 1 < argv.length) {
      res.model = argv[i + 1]!;
      i += 2;
    } else if (arg === "--md" && i + 1 < argv.length) {
      res.md = argv[i + 1]!;
      i += 2;
    } else if (arg === "--probe" && i + 1 < argv.length) {
      res.probe = argv[i + 1]!;
      i += 2;
    } else if (arg === "--out" && i + 1 < argv.length) {
      res.out = argv[i + 1]!;
      i += 2;
    } else if (arg.startsWith("-")) {
      throw new Error(`Unknown flag: ${arg}`);
    } else {
      if (!res.subcommand) {
        res.subcommand = arg;
      } else {
        res.positionals.push(arg);
      }
      i++;
    }
  }
  return res;
}

// ── Main Execution ──────────────────────────────────────────────────────────

async function main() {
  const args = parseArgs(process.argv.slice(2));
  if (args.help || !args.subcommand) {
    printHelp();
    process.exit(0);
  }

  if (args.subcommand === "redteam-lean" || args.subcommand === "qa-prose") {
    const mode = args.subcommand;
    if (args.positionals.length === 0) {
      console.error(`ERROR: ${mode} requires at least one file or directory path.`);
      process.exit(1);
    }
    const model = args.model ?? (mode === "redteam-lean" ? DEFAULT_REDTEAM_MODEL : DEFAULT_QA_MODEL);
    const units = buildAuditUnits(args.positionals, mode, args.md, args.probe);

    if (args.dryRun) {
      const previews = units.map((u) => {
        const params = buildAnthropicMessageParams(u, model);
        const sysChars = params.system[0]!.text.length;
        const userChars = params.messages[0]!.content.length;
        return {
          custom_id: u.id,
          mode: u.mode,
          model: params.model,
          primary_file: relative(QOU_ROOT, u.primaryPath),
          companion_files: u.companionPaths.map((c) => relative(QOU_ROOT, c)),
          prompt_cache_control: params.system[0]!.cache_control,
          system_rubric_chars: sysChars,
          system_rubric_est_tokens: Math.ceil(sysChars / 3.8),
          user_payload_chars: userChars,
          user_payload_est_tokens: Math.ceil(userChars / 3.8),
          max_tokens: params.max_tokens,
        };
      });
      console.log(
        JSON.stringify(
          {
            dry_run: true,
            subcommand: mode,
            unit_count: previews.length,
            units: previews,
          },
          null,
          2,
        ),
      );
      if (args.out) {
        const outAbs = resolve(QOU_ROOT, args.out);
        mkdirSync(dirname(outAbs), { recursive: true });
        writeFileSync(outAbs, JSON.stringify({ dry_run: true, units: previews }, null, 2));
      }
      return;
    }

    const client = requireAnthropicClient();
    const results: any[] = [];
    for (const u of units) {
      const rel = relative(QOU_ROOT, u.primaryPath);
      const params = buildAnthropicMessageParams(u, model);
      console.error(
        `[claude-${mode}] Auditing ${rel} (companions: ${u.companionPaths.length}, model: ${model})...`,
      );
      const resp = await client.messages.create(params);
      const textBlocks = resp.content
        .filter((b: any) => b.type === "text")
        .map((b: any) => b.text)
        .join("\n");
      const parsed = parseJsonResponse(textBlocks, rel);
      parsed._usage = resp.usage;
      results.push(parsed);
    }

    renderVerdictTable(results);
    if (args.out) {
      const outAbs = resolve(QOU_ROOT, args.out);
      mkdirSync(dirname(outAbs), { recursive: true });
      writeFileSync(outAbs, JSON.stringify({ mode, model, results }, null, 2));
      console.error(`[claude-${mode}] Wrote JSON report -> ${outAbs}`);
    }
    return;
  }

  if (args.subcommand === "batch-submit") {
    const mode = args.mode ?? "redteam-lean";
    if (args.positionals.length === 0) {
      console.error("ERROR: batch-submit requires at least one file or directory path.");
      process.exit(1);
    }
    const model = args.model ?? (mode === "redteam-lean" ? DEFAULT_REDTEAM_MODEL : DEFAULT_QA_MODEL);
    const units = buildAuditUnits(args.positionals, mode, args.md, args.probe);
    const requests = units.map((u) => ({
      custom_id: u.id,
      params: buildAnthropicMessageParams(u, model),
    }));

    if (args.dryRun) {
      console.log(
        JSON.stringify(
          {
            dry_run: true,
            subcommand: "batch-submit",
            mode,
            model,
            request_count: requests.length,
            requests: requests.map((r, idx) => ({
              custom_id: r.custom_id,
              primary_file: relative(QOU_ROOT, units[idx]!.primaryPath),
              companion_files: units[idx]!.companionPaths.map((c) => relative(QOU_ROOT, c)),
              cache_control: r.params.system[0]!.cache_control,
              est_input_tokens: Math.ceil(
                (r.params.system[0]!.text.length + r.params.messages[0]!.content.length) / 3.8,
              ),
            })),
          },
          null,
          2,
        ),
      );
      return;
    }

    const client = requireAnthropicClient();
    console.error(`[claude-batch] Submitting ${requests.length} requests (mode=${mode}, model=${model})...`);
    const batch = await client.messages.batches.create({ requests });
    mkdirSync(BATCH_CACHE_DIR, { recursive: true });
    const manifestPath = join(BATCH_CACHE_DIR, `${batch.id}.json`);
    const manifest = {
      batch_id: batch.id,
      created_at: batch.created_at,
      processing_status: batch.processing_status,
      mode,
      model,
      item_map: Object.fromEntries(
        units.map((u) => [
          u.id,
          {
            primary_file: relative(QOU_ROOT, u.primaryPath),
            companion_files: u.companionPaths.map((c) => relative(QOU_ROOT, c)),
          },
        ]),
      ),
    };
    writeFileSync(manifestPath, JSON.stringify(manifest, null, 2));
    console.log(JSON.stringify({ batch_id: batch.id, status: batch.processing_status, manifest: manifestPath }, null, 2));
    return;
  }

  if (args.subcommand === "batch-collect") {
    const batchId = args.positionals[0];
    if (!batchId) {
      console.error("ERROR: batch-collect requires a <batchId> positional argument.");
      process.exit(1);
    }
    const client = requireAnthropicClient();
    const status = await client.messages.batches.retrieve(batchId);
    console.error(`[claude-batch] Batch ${batchId} status: ${status.processing_status}`);
    if (status.processing_status !== "ended") {
      console.log(JSON.stringify(status, null, 2));
      return;
    }

    const manifestPath = join(BATCH_CACHE_DIR, `${batchId}.json`);
    const itemMap: Record<string, { primary_file: string }> = existsSync(manifestPath)
      ? JSON.parse(readFileSync(manifestPath, "utf-8")).item_map ?? {}
      : {};

    const results: any[] = [];
    const stream = await client.messages.batches.results(batchId);
    for await (const entry of stream) {
      const target = itemMap[entry.custom_id]?.primary_file ?? entry.custom_id;
      if (entry.result.type === "succeeded") {
        const textBlocks = entry.result.message.content
          .filter((b: any) => b.type === "text")
          .map((b: any) => b.text)
          .join("\n");
        const parsed = parseJsonResponse(textBlocks, target);
        parsed.custom_id = entry.custom_id;
        parsed._usage = entry.result.message.usage;
        results.push(parsed);
      } else {
        results.push({
          target,
          custom_id: entry.custom_id,
          verdict: "FAIL",
          summary: `Batch item result type: ${entry.result.type}`,
          findings: [],
        });
      }
    }

    renderVerdictTable(results);
    if (args.out) {
      const outAbs = resolve(QOU_ROOT, args.out);
      mkdirSync(dirname(outAbs), { recursive: true });
      writeFileSync(outAbs, JSON.stringify({ batch_id: batchId, results }, null, 2));
      console.error(`[claude-batch] Wrote batch results -> ${outAbs}`);
    }
    return;
  }

  console.error(`ERROR: Unknown subcommand '${args.subcommand}'. Run with --help for usage.`);
  process.exit(1);
}

main().catch((err) => {
  console.error("ERROR:", err instanceof Error ? err.message : err);
  process.exit(1);
});
