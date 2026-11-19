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

import { spawnSync } from "child_process";
import { existsSync, mkdirSync, readdirSync, readFileSync, statSync, writeFileSync } from "fs";
import { tmpdir } from "os";
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

Your task is to audit submitted monograph prose blocks (\`.md\`) and their companion block manifests (\`.ts\`) for:
  - **Classes L1 & L2**: Fourth-wall Lean 4 / Mathlib / declaration-identifier leaks in reader-facing mathematical prose,
  - **Class L3**: John Milnor Monograph Voice A compliance (zero first/second-person pronouns \`we\`, \`our\`, \`us\`, \`I\`, \`you\` and zero editorializing),
  - **Class L4**: Architectural reading-order anachronisms (invoking concepts from later chapters before their defining chapter/section, forward cross-references in foundational chapters, and terminology drift on core objects),
  - **Convention-D, Two-Term QED, & ValueRegistry Discipline**: Zero stale Convention-C formulas and zero unbacked hardcoded multi-digit observables.

### NON-NEGOTIABLE QOU MONOGRAPH QA RUBRIC

1. **CLASSES L1 & L2 — ZERO FOURTH-WALL LEAN / MATHLIB / IDENTIFIER LEAKS IN PROSE (CRITICAL / MAJOR)**:
   - In the published QOU monograph, machine-checked formalization is linked exclusively via the block manifest's \`lean:\` field and the rendered marginal \`\\forall\` verification badge — NEVER inside reader-facing \`.md\` prose.
   - **Class L1 (\`L1_LEAN_PROSE\`)**: Flag ANY narrative prose mention of \`Lean\`, \`Lean 4\`, \`Lean carrier\`, \`Lean sibling\`, \`Lean backing\`, \`Lean file\`, \`Lean module\`, \`Lean structure\`, \`Mathlib\`, \`proved formally\`, \`formally proved\`, \`formalised in\` / \`formalized in\`, \`discharges the axiom\`, \`sorry-free\`, \`axiom-free\`, \`## Lean ...\` section headings, or \`**Lean.**\` paragraph lead-ins.
   - **Class L2 (\`L2_LEAN_IDENT\`)**: Flag ANY backticked Lean fully-qualified name (\`QOU.Foo.bar\`, \`Mathlib...\`, \`CategoryTheory...\`), \`.lean\` filename, Lean typeclass or type application (\`CommRing\`, \`Field\`, \`LinearOrderedField\`, \`IsQGeneric\`, \`[Add H]\`, \`HochschildZero R A\`), raw backticked block ID (\`def:foo\`, \`thm:bar\` instead of a prose markdown link \`[noun phrase](#def:foo)\`), or Lean \`snake_case\` / \`camelCase\` declaration identifier (\`dimQK0_eq_evDimQ_chernCharacter\`, \`su2Character_one\`, \`exteriorSquareDim_ne_zero_iff\`) appearing in \`.md\` prose.

2. **CLASS L3 — JOHN MILNOR MONOGRAPH VOICE A: ZERO FIRST/SECOND-PERSON PRONOUNS & EDITORIALIZING (MAJOR)**:
   - QOU monograph prose is written strictly in John Milnor's impersonal third-person Voice A (*Topology from the Differentiable Viewpoint*, *Characteristic Classes*): mathematical objects, morphisms, and functors are the grammatical subjects ("The counit $\\varepsilon$ induces...", "Applying the braided hexagon yields...", "Restricting to the $(2,1)$ sector gives...").
   - **Flag every first-person or second-person pronoun in mathematical prose (\`L3_VOICE_PRONOUN\`)**: \`we\`, \`we're\`, \`we've\`, \`we'll\`, \`our\`, \`ours\`, \`us\`, \`let's\`, \`I\`, \`my\`, \`you\`, \`your\`, and reader-address frames (\`the reader will see/note/observe\`). *(Genre note: an explicitly titled front-matter \`authors-note.md\` may use authorial voice for historical/acknowledgement framing if strictly segregated from mathematical exposition, but \`chapter-overview.md\`, \`intro-*.md\`, and all Part I–IV chapters must use pure third-person Voice A.)*
   - Flag lecturer-cadence openers (\`So the plan/idea is\`, \`Now let's\`, \`Basically,\`), editorializing intensifiers/superlatives (\`surprisingly\`, \`remarkably\`, \`a beautiful result\`, \`the most important consequence\`), repository/session chatter (\`bean qou-xxxx\`, \`PR #\`, \`this session\`, \`measured on 2026-...\`), and epistemic overclaiming (open conjectures phrased as proved results).

3. **CLASS L4 — ARCHITECTURAL READING-ORDER ANACHRONISMS & TERMINOLOGY DRIFT (\`L4_ANACHRONISM\` — MAJOR / CRITICAL)**:
   - Enforce the authoritative QOU Monograph Chapter Sequence:
     * **Front Matter (\`introduction/\`)**: High-level conceptual roadmap of the five-step pipeline. Must introduce intuitive motivation cleanly without presupposing undefined technical notation or leaking repository/Lean internals.
     * **Part I, Chapter 1 (\`quantum-universes/\`)**: Purely categorical foundations of a *Quantum Universe* $(\\mathbf{C}, \\varTheta, G, \\mathcal{S})$ over a rigid braided monoidal category $\\mathbf{C}$ (and Frobenius–Hopf algebra / groupoid axioms over a generic base ring). **STRICT CHAPTER-1 BOUNDARY**: The numerical or Laurent substrate parameter $q$, quantum integers $[n]_q$, $q$-dimensions $\\dim_q$ evaluated as $q$-brackets, cyclotomic polynomials $\\Phi_d(q)$, quantum groups $\\mathrm{SU}_q(2)$, Iwahori–Hecke algebras $H_n(q)$, Wedderburn block decompositions, and the \`"archimedean wall"\` are **NOT DEFINED IN CHAPTER 1**! Any remark, motivation, or example in \`quantum-universes/*.md\` that prematurely invokes $q$, $[n]_q$, $\\Phi_d(q)$, $H_n(q)$, $\\mathrm{SU}_q(2)$, \`"substrate parameter"\`, or \`"archimedean wall"\` (such as an out-of-place \`**On the substrate parameter.**\` passage) is a **MAJOR/CRITICAL Class L4 reading-order anachronism** that belongs in Chapter 2 Section 7+ or Part II.
     * **Part I, Chapter 2 (\`quantum-observable-universes/\`)**: Introduces Quantum Observable Universes, $q$-differential operators, the **substrate parameter $q$** (Section 7, \`sec:substrate-parameter\`), and the **Frobenius–Hopf substrate $A$ and categorical Reeb derivation** (Section 9, \`sec:algebraic-substrate-reeb\`). Blocks before Section 7 must not use $q$ as already defined, and blocks in Chapters 1–2 must not carry forward \`](#label)\` cross-references to later sections or Part II chapters.
     * **Part I, Chapter 3 (\`models-of-qous/\`)**: Explicit 5-step framing/preview gallery where forward previews of Part II–III stages are architecturally permitted when clearly signposted as previews.
     * **Part II (\`braids-and-knots\` $\\to$ \`brings-surface\` $\\to$ \`knots-particles-confinement\` $\\to$ \`eightfold-way\` $\\to$ \`mass-endomorphism\` $\\to$ \`climax-volume-mass\` $\\to$ \`mass-theory\` $\\to$ \`nuclear-interactions\` $\\to$ \`gravity-spacetime\`)**: Develops $H_n(q)$, Jones–Markov trace & Convention D, GPMT modified trace, Bring's surface $\\Sigma_4$ ($\\chi_{\\mathrm{eu}} = -6$), particle braids, mass endomorphism, and nuclear binding / $\\beta$-decay.
   - **Core Object & Notation Discipline**: Flag terminology or glyph drift on core objects — e.g. conflating the Frobenius–Hopf algebra object $A$ with the state bundle $\\mathcal{S}$ or fundamental representation $V_1$; writing bare $\\chi$ instead of $\\chi_{\\mathrm{eu}}$ for topological Euler characteristic; writing bare $E$ for energy instead of $\\mathfrak{E}$; writing bare $\\mathrm{SU}(3)$ when colour $\\mathrm{SU}(3)_{\\mathrm{c}}$ vs flavour $\\mathrm{SU}(3)_{\\mathrm{f}}$ is meant; or using inconsistent $q$-calculus conventions ($h_{\\mathrm{A}} = q - q^{-1}$, $\\hbar_q = 1 - q^{-1}$, $[n]_q = (q^n - q^{-n})/(q - q^{-1})$).

4. **CONVENTION-D, TWO-TERM QED, & VALUEREGISTRY DISCIPLINE (CRITICAL / MAJOR)**:
   - Flag any prose presenting excised Convention C ($z = \\sqrt{q}/(1+q)$ or non-Markov $(z, 1/2 - z, z)$) as canonical instead of Convention D ($z_D = q^3/(q^2+1)$, $w_{(3)}(z_D) = (q^4+1)/(q^2+1)^2$, $w_{(2,1)}(z_D) = q^2/(q^2+1)^2$, $w_{(1^3)}(z_D) = 0$).
   - Flag raw hardcoded multi-digit numerical predictions in prose or tables that bypass \`:val[...]\` / \`ValueRegistry\` witness macros.

### REQUIRED JSON OUTPUT SCHEMA
Respond ONLY with a single valid JSON object (no markdown fences outside the JSON) matching this structure:
{
  "target": "<primary file path>",
  "verdict": "PASS" | "CONDITIONAL" | "FAIL",
  "scores": {
    "fourth_wall_lean_clean": "PASS" | "WARN" | "FAIL",
    "milnor_voice_and_honesty": "PASS" | "WARN" | "FAIL",
    "reading_order_coherence": "PASS" | "WARN" | "FAIL",
    "convention_d_alignment": "PASS" | "WARN" | "FAIL",
    "value_registry_discipline": "PASS" | "WARN" | "FAIL",
    "notation_consistency": "PASS" | "WARN" | "FAIL"
  },
  "summary": "<2-3 sentence executive QA summary>",
  "findings": [
    {
      "severity": "CRITICAL" | "MAJOR" | "MINOR" | "NIT",
      "category": "L1_LEAN_PROSE" | "L2_LEAN_IDENT" | "L3_VOICE_PRONOUN" | "L4_ANACHRONISM" | "CONVENTION_DRIFT" | "HARDCODED_NUMBER" | "NOTATION",
      "file": "<relative file path>",
      "line": <line number or null>,
      "detail": "<precise issue description explaining why it violates L1/L2/L3/L4 or QOU invariants>",
      "suggested_edit": "<concise Milnor-Voice-A replacement text or structural relocation target>"
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

function discoverCompanionsForProse(mdAbsPath: string): string[] {
  const companions: string[] = [];
  const siblingTs = mdAbsPath.replace(/\.md$/, ".ts");
  if (siblingTs !== mdAbsPath && existsSync(siblingTs)) {
    companions.push(siblingTs);
  }
  return companions;
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
      mode === "redteam-lean"
        ? discoverCompanionsForLean(absPath, explicitMd, explicitProbe)
        : discoverCompanionsForProse(absPath);
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

function resolveClaudeCliBinary(): string | undefined {
  const candidates = [
    process.env.CLAUDE_BIN,
    join(process.env.HOME || "", ".local", "bin", "claude"),
    "/opt/homebrew/bin/claude",
    "/usr/local/bin/claude",
  ].filter((x): x is string => Boolean(x));
  for (const c of candidates) {
    if (existsSync(c)) return c;
  }
  const which = spawnSync("which", ["claude"], { encoding: "utf-8" });
  if (which.status === 0 && which.stdout.trim()) return which.stdout.trim();
  return undefined;
}

async function invokeViaClaudeCli(
  claudeBin: string,
  model: string,
  systemText: string,
  userText: string,
): Promise<{ text: string; usage: any }> {
  const proc = Bun.spawn(
    [
      claudeBin,
      "-p",
      "--model",
      model,
      "--effort",
      "low",
      "--setting-sources",
      "user",
      "--tools",
      "",
      "--strict-mcp-config",
      "--mcp-config",
      '{"mcpServers":{}}',
      "--no-session-persistence",
      "--output-format",
      "json",
      "--system-prompt",
      systemText,
      "--",
      userText,
    ],
    {
      cwd: tmpdir(),
      stdin: "ignore",
      stdout: "pipe",
      stderr: "pipe",
    },
  );
  const [stdout, stderr, exitCode] = await Promise.all([
    new Response(proc.stdout).text(),
    new Response(proc.stderr).text(),
    proc.exited,
  ]);
  if (exitCode !== 0) {
    try {
      const errEnv = JSON.parse(stdout.trim());
      if (errEnv?.api_error || errEnv?.result) {
        throw new Error(
          `claude CLI ${errEnv.api_error ?? "error"} (status ${errEnv.api_error_status ?? exitCode}): ${errEnv.result ?? ""}`,
        );
      }
    } catch (inner) {
      if (inner instanceof Error && inner.message.startsWith("claude CLI ")) throw inner;
    }
    throw new Error(`claude CLI exited with status ${exitCode}: ${(stderr || stdout).slice(0, 500)}`);
  }
  const envelope = JSON.parse(stdout.trim());
  if (envelope.is_error) {
    throw new Error(`claude CLI returned error: ${JSON.stringify(envelope).slice(0, 500)}`);
  }
  return {
    text: String(envelope.result ?? ""),
    usage: envelope.usage ?? {},
  };
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
    const firstBrace = rawText.indexOf("{");
    const lastBrace = rawText.lastIndexOf("}");
    if (firstBrace !== -1 && lastBrace > firstBrace) {
      try {
        return JSON.parse(rawText.slice(firstBrace, lastBrace + 1));
      } catch {
        // fall through to structured fallback
      }
    }
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

    const apiKey = loadAnthropicApiKeyIfPresent();
    const sdkClient = apiKey ? getAnthropic() : null;
    const claudeBin = !sdkClient ? resolveClaudeCliBinary() : undefined;
    if (!sdkClient && !claudeBin) {
      requireAnthropicClient();
    }

    async function evaluateOneUnit(u: AuditUnit): Promise<any> {
      const rel = relative(QOU_ROOT, u.primaryPath);
      const params = buildAnthropicMessageParams(u, model);
      const backendLabel = sdkClient ? "anthropic-sdk" : "claude-cli";
      console.error(
        `[claude-${mode}] Auditing ${rel} (companions: ${u.companionPaths.length}, model: ${model}, backend: ${backendLabel})...`,
      );
      let textBlocks = "";
      let usageInfo: any = {};
      let lastErr: unknown;
      for (let attempt = 0; attempt < 2; attempt++) {
        try {
          if (sdkClient) {
            const resp = await sdkClient.messages.create(params);
            textBlocks = resp.content
              .filter((b: any) => b.type === "text")
              .map((b: any) => b.text)
              .join("\n");
            usageInfo = resp.usage;
          } else {
            const cliResp = await invokeViaClaudeCli(
              claudeBin!,
              model,
              params.system[0]!.text,
              params.messages[0]!.content,
            );
            textBlocks = cliResp.text;
            usageInfo = cliResp.usage;
          }
          lastErr = undefined;
          break;
        } catch (err) {
          lastErr = err;
          if (attempt === 0) {
            await new Promise((r) => setTimeout(r, 2000));
          }
        }
      }
      if (lastErr !== undefined) {
        console.error(
          `  -> ${rel}: ERROR after retry: ${lastErr instanceof Error ? lastErr.message : String(lastErr)}`,
        );
        return {
          target: rel,
          verdict: "CONDITIONAL",
          summary: `API/CLI error during audit: ${lastErr instanceof Error ? lastErr.message.slice(0, 160) : String(lastErr).slice(0, 160)}`,
          findings: [],
        };
      }
      const parsed = parseJsonResponse(textBlocks, rel);
      parsed._usage = usageInfo;
      console.error(
        `  -> ${rel}: verdict=${parsed.verdict ?? "UNKNOWN"}, findings=${Array.isArray(parsed.findings) ? parsed.findings.length : 0}, ` +
          `tokens(in=${usageInfo?.input_tokens ?? 0}, cache_write=${usageInfo?.cache_creation_input_tokens ?? 0}, cache_read=${usageInfo?.cache_read_input_tokens ?? 0}, out=${usageInfo?.output_tokens ?? 0})`,
      );
      return parsed;
    }

    const results: any[] = [];
    if (units.length > 0) {
      // Run unit 0 first to populate the shared ephemeral prompt cache, then run remaining units in batches of 3.
      results.push(await evaluateOneUnit(units[0]!));
      const CONCURRENCY = 3;
      for (let idx = 1; idx < units.length; idx += CONCURRENCY) {
        const chunk = units.slice(idx, idx + CONCURRENCY);
        const chunkRes = await Promise.all(chunk.map((u) => evaluateOneUnit(u)));
        results.push(...chunkRes);
      }
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
