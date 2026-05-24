/**
 * @litlfred/witness-schema — Zod schemas for the QOU witness JSON format.
 *
 * The canonical schema is `tools/witness-schema/schema/witness.schema.json`.
 * This file ships Zod schemas that validate against the same shape, so any
 * TypeScript / JavaScript consumer can parse + type-check a `*.witness.json`
 * file produced by `qou_substrate.witness.WitnessBuilder`.
 *
 * @example
 * ```ts
 * import { ComputationWitness } from "@litlfred/witness-schema";
 * import { readFileSync } from "fs";
 *
 * const raw = JSON.parse(readFileSync("hyperbolic-volumes.witness.json", "utf-8"));
 * const witness = ComputationWitness.parse(raw);
 *
 * console.log(witness.engineVersion, witness.commitSha);
 * for (const a of witness.assertions) {
 *   console.log(a.name, "→", a.computed, "vs", a.expected, "→", a.passed);
 * }
 * ```
 */

import { z } from "zod";

export const ComputationEngine = z.enum([
  "snappea",
  "sympy",
  "mpmath",
  "sage",
  "python",
  "numpy",
  "scipy",
  "closed-form",
  "python+mpmath",
  "python+numpy+cvxpy",
]);
export type ComputationEngine = z.infer<typeof ComputationEngine>;

const ComputedOrExpected = z.union([z.number(), z.string()]);

export const ComputationAssertion = z
  .object({
    name: z.string(),
    computed: ComputedOrExpected,
    expected: ComputedOrExpected,
    passed: z.boolean().optional(),
    tolerance: z.number().optional(),
    unit: z.string().optional(),
    source: z.string().optional(),
  })
  .passthrough();
export type ComputationAssertion = z.infer<typeof ComputationAssertion>;

export const UpstreamWitnessHash = z
  .object({
    path: z.string(),
    sha256: z.string(),
    size_bytes: z.number().int().optional(),
    commitSha: z.string().optional(),
    scriptCommitSha: z.string().optional(),
    computedAt: z.string().optional(),
  })
  .passthrough();
export type UpstreamWitnessHash = z.infer<typeof UpstreamWitnessHash>;

export const ComputationWitness = z
  .object({
    engine: ComputationEngine,
    engineVersion: z.string(),
    computedAt: z.string(),
    assertions: z.array(ComputationAssertion),

    commitSha: z.string().optional(),
    scriptCommitSha: z.string().optional(),
    scriptHash: z.string().optional(),
    scriptFile: z.string().optional(),
    name: z.string().optional(),
    description: z.string().optional(),
    contentBlock: z.string().optional(),
    auditOnly: z.string().optional(),
    durationMs: z.number().optional(),
    allPassed: z.boolean().optional(),
    parameters: z.record(z.string(), z.unknown()).optional(),
    data: z.record(z.string(), z.unknown()).optional(),
    caveats: z.array(z.string()).optional(),
    upstream_witness_hashes: z.array(UpstreamWitnessHash).optional(),
  })
  .passthrough();
export type ComputationWitness = z.infer<typeof ComputationWitness>;

export const VERSION = "0.1.0";
