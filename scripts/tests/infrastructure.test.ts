/**
 * Infrastructure tests — MCP config, scripts, schemas, deploy.
 *
 * Migrated from the original bash run-tests.sh, now type-safe
 * and producing structured TestReport output.
 */

import { describe, test, expect } from "bun:test";
import { readFileSync, existsSync } from "fs";
import { join } from "path";
import { execSync } from "child_process";
import { REPO_ROOT } from "./helpers";

// ── session-status.sh (replaced check-lean.sh) ─────────────────

describe("session-status.sh", () => {
  const script = join(REPO_ROOT, "scripts/session-status.sh");

  let output: string;
  let parsed: Record<string, unknown>;

  try {
    output = execSync(script, { encoding: "utf-8", timeout: 10_000 }).trim();
    parsed = JSON.parse(output);
  } catch {
    output = "";
    parsed = {};
  }

  test("outputs valid JSON", () => {
    expect(output.length).toBeGreaterThan(0);
    expect(() => JSON.parse(output)).not.toThrow();
  });

  test("has status object", () => {
    expect(parsed).toHaveProperty("status");
  });

  test("status has lean_mode field", () => {
    const status = parsed.status as Record<string, unknown> | undefined;
    if (status) {
      expect(status).toHaveProperty("lean_mode");
      const validModes = ["local", "remote", "local-degraded", "none"];
      expect(validModes).toContain(status.lean_mode);
    }
  });

  test("has summary field", () => {
    expect(parsed).toHaveProperty("summary");
  });
});

// ── check-no-lean-artifacts.sh ──────────────────────────────────

describe("check-no-lean-artifacts.sh", () => {
  test("passes on clean repo", () => {
    const script = join(REPO_ROOT, "scripts/check-no-lean-artifacts.sh");
    expect(() =>
      execSync(script, { cwd: REPO_ROOT, encoding: "utf-8", timeout: 5_000 })
    ).not.toThrow();
  });
});

// ── Config files ────────────────────────────────────────────────

describe("lean-mcp.config.json", () => {
  const configPath = join(REPO_ROOT, "lean-mcp.config.json");

  test("is valid JSON", () => {
    const content = readFileSync(configPath, "utf-8");
    expect(() => JSON.parse(content)).not.toThrow();
  });

  test("has required fields", () => {
    const config = JSON.parse(readFileSync(configPath, "utf-8"));
    expect(config).toHaveProperty("domain");
    expect(config).toHaveProperty("image");
    expect(config).toHaveProperty("mcp_internal_port");
    expect(config).toHaveProperty("auth");
  });
});

describe(".mcp.json", () => {
  const mcpPath = join(REPO_ROOT, ".mcp.json");

  test("is valid JSON", () => {
    const content = readFileSync(mcpPath, "utf-8");
    expect(() => JSON.parse(content)).not.toThrow();
  });

  test("has lean-lsp server", () => {
    const mcp = JSON.parse(readFileSync(mcpPath, "utf-8"));
    expect(mcp.mcpServers).toHaveProperty("lean-lsp");
  });
});

// ── Deploy infrastructure ───────────────────────────────────────

describe("Deploy infrastructure", () => {
  test("Caddyfile.template uses domain variable", () => {
    const caddyfile = readFileSync(
      join(REPO_ROOT, "deploy/Caddyfile.template"),
      "utf-8"
    );
    expect(caddyfile).toContain("${LEAN_MCP_DOMAIN}");
  });

  test("self-update.sh preserves .env", () => {
    const script = readFileSync(
      join(REPO_ROOT, "deploy/self-update.sh"),
      "utf-8"
    );
    expect(script).toContain("exclude='deploy/.env'");
  });
});

// ── .gitignore ──────────────────────────────────────────────────

describe(".gitignore", () => {
  const gitignore = readFileSync(join(REPO_ROOT, ".gitignore"), "utf-8");

  test("blocks deploy/.env", () => {
    expect(gitignore).toContain("deploy/.env");
  });

  test("blocks lean-archive/.lake/", () => {
    expect(gitignore).toContain("lean-archive/.lake/");
  });
});

// ── Schema files ────────────────────────────────────────────────

describe("Schema files", () => {
  test("qou-types.ts exists", () => {
    expect(existsSync(join(REPO_ROOT, "schemas/qou-types.ts"))).toBe(true);
  });

  test("proof-objects.schema.json is valid", () => {
    const content = readFileSync(
      join(REPO_ROOT, "schemas/proof-objects.schema.json"),
      "utf-8"
    );
    const schema = JSON.parse(content);
    expect(schema.$schema).toContain("json-schema.org");
    expect(schema).toHaveProperty("$defs");
  });

  test("proof-objects.json matches schema version", () => {
    const manifest = JSON.parse(
      readFileSync(join(REPO_ROOT, "proof-objects.json"), "utf-8")
    );
    expect(manifest.version).toBe("1.0");
    expect(manifest).toHaveProperty("objects");
    expect(manifest).toHaveProperty("manuscript");
  });
});
