/**
 * Regression guard for bean `qou-v4ht`.
 *
 * A `triage pending` exemption is a *promise*, not a verdict: it says a human
 * call is still owed. Once the review ledger records `genuine` for that key the
 * promise has been kept, so the hit must COUNT — the adjudication outranks the
 * heuristic.
 *
 * History: the type-matched-projection exemption was introduced deliberately as
 * "tracked-not-counted", with promotion to a hard failure named in its own
 * comment as "a deliberate follow-up". The follow-up never happened, so
 * adjudicated defects stayed suppressed indefinitely. Measured on 2026-08-22
 * against `main`: the artifact reported `total_defects = 53` while the ledger
 * held **123** `genuine` — because **76** confirmed defects were still exempt
 * under the single reason "type-matched projection (field name escapes
 * CONCLUSION_FIELD; tracked, triage pending)". Anyone sizing the remaining
 * vacuity work off the committed artifact planned for under half the queue.
 *
 * These tests are deliberately self-contained — a synthetic `.lean` file plus a
 * synthetic ledger — so they assert the INVARIANT rather than a corpus count
 * that legitimately moves as siblings drain the backlog.
 *
 * Run:  bun test content/pipeline/lean-vacuity-ledger-promotion.test.ts
 */
import { test, expect } from "bun:test";
import { readFileSync, writeFileSync, mkdirSync, rmSync, existsSync } from "node:fs";
import { resolve } from "node:path";
import { spawnSync } from "node:child_process";

const REPO_ROOT = resolve(import.meta.dir, "..", "..");
const SCRIPT = resolve(REPO_ROOT, "folio/pipeline/lean-vacuity-axiom-audit.ts");

/** Scratch dir under the repo: the scanner resolves paths against REPO_ROOT. */
const TMPDIR = resolve(REPO_ROOT, "folio/quantum-observable-universe/.vacuity-promotion-selftest");
const LEAN_REL =
  "folio/quantum-observable-universe/.vacuity-promotion-selftest/Probe.lean";
const LEAN_ABS = resolve(REPO_ROOT, LEAN_REL);
const LEDGER = resolve(TMPDIR, "ledger.json");
const REPORT = resolve(TMPDIR, "report.json");

/**
 * A self-assuming projection whose field name escapes `CONCLUSION_FIELD`
 * (`summands_detected` matches no `claim_` / `_holds` / `_eq` convention), but
 * whose declared field type IS the conclusion. That is exactly the shape the
 * type-match exemption fires on.
 *
 * The carried proposition is an opaque `P` on purpose. An earlier draft used
 * `(1 : Nat) = 1`, which ALSO trips the trivial-true detector — so the file
 * carried a second, counted hit and `total_defects` was never 0, making the
 * test fail for a reason unrelated to what it is guarding. Keeping `P` opaque
 * isolates the projection as the file's only finding.
 */
const PROBE = `
namespace VacuityPromotionSelfTest

class ProbeCtx (P : Prop) where
  summands_detected : P

theorem probe_decl (P : Prop) [ctx : ProbeCtx P] : P :=
  ctx.summands_detected

end VacuityPromotionSelfTest
`;

function runAudit(ledgerRel?: string) {
  const args = ["run", SCRIPT, LEAN_REL, "--quiet", "--json", REPORT];
  if (ledgerRel) args.push("--review-ledger", ledgerRel);
  const r = spawnSync("bun", args, { cwd: REPO_ROOT, encoding: "utf8" });
  const report = existsSync(REPORT)
    ? JSON.parse(readFileSync(REPORT, "utf8"))
    : undefined;
  return { r, report };
}

function hitsOf(report: any): any[] {
  return Object.values(report?.flagged ?? {}).flat() as any[];
}

test("a triage-pending exemption is LIFTED once the ledger adjudicates the key genuine", () => {
  mkdirSync(TMPDIR, { recursive: true });
  try {
    writeFileSync(LEAN_ABS, PROBE);

    // 1. With no ledger verdict, the hit is exempt and does not count.
    writeFileSync(
      LEDGER,
      JSON.stringify({ $schema: "lean-vacuity-review/v1", entries: {} }),
    );
    const before = runAudit();
    const exemptHit = hitsOf(before.report).find((h) =>
      /triage pending/.test(h.exempt_reason ?? ""),
    );
    // Guard the premise: if the detector stops producing this shape, the test
    // must fail loudly rather than pass vacuously.
    expect(exemptHit).toBeDefined();
    expect(exemptHit.exempt).toBe(true);
    expect(before.report.total_defects).toBe(0);

    // 2. Record a `genuine` verdict for exactly that key.
    const key = `${LEAN_REL}::${exemptHit.decl}::${exemptHit.category}`;
    writeFileSync(
      LEDGER,
      JSON.stringify({
        $schema: "lean-vacuity-review/v1",
        entries: { [key]: { verdict: "genuine", category: exemptHit.category } },
      }),
    );

    // 3. The same scan must now COUNT it, and say so.
    const after = runAudit(
      "folio/quantum-observable-universe/.vacuity-promotion-selftest/ledger.json",
    );
    const promoted = hitsOf(after.report).find((h) => h.decl === exemptHit.decl);
    expect(promoted.exempt).toBeFalsy();
    expect(promoted.promoted_from_exempt).toMatch(/triage pending/);
    expect(after.report.total_defects).toBe(1);
    expect(after.report.total_promoted_from_exempt).toBe(1);
  } finally {
    rmSync(TMPDIR, { recursive: true, force: true });
  }
});

test("a `legit` or `advisory` verdict does NOT lift the exemption", () => {
  // Only `genuine` promotes. `legit`/`advisory` are verdicts that the hit is
  // not a defect, so lifting on them would invert the ledger's meaning and
  // manufacture defects out of adjudicated non-defects.
  mkdirSync(TMPDIR, { recursive: true });
  try {
    writeFileSync(LEAN_ABS, PROBE);
    writeFileSync(
      LEDGER,
      JSON.stringify({ $schema: "lean-vacuity-review/v1", entries: {} }),
    );
    const probe = runAudit();
    const hit = hitsOf(probe.report).find((h) =>
      /triage pending/.test(h.exempt_reason ?? ""),
    );
    expect(hit).toBeDefined();
    const key = `${LEAN_REL}::${hit.decl}::${hit.category}`;

    for (const verdict of ["legit", "advisory"]) {
      writeFileSync(
        LEDGER,
        JSON.stringify({
          $schema: "lean-vacuity-review/v1",
          entries: { [key]: { verdict, category: hit.category } },
        }),
      );
      const { report } = runAudit(
        "folio/quantum-observable-universe/.vacuity-promotion-selftest/ledger.json",
      );
      expect(report.total_defects).toBe(0);
      expect(report.total_promoted_from_exempt).toBe(0);
    }
  } finally {
    rmSync(TMPDIR, { recursive: true, force: true });
  }
});
