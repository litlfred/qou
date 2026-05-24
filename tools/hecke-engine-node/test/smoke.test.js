/**
 * Smoke tests for @litlfred/hecke-engine-node.
 *
 * Mirrors the pyhecke-native smoke tests so behaviour parity is
 * verifiable side-by-side. Run with: node --test test/
 */

const test = require("node:test");
const assert = require("node:assert/strict");

const heckeNode = require("../index.js");

const Q_SUBSTRATE = 1.10998;  // substrate q_0; same constant pyhecke uses

test("version matches package.json", () => {
  const pkg = require("../package.json");
  assert.equal(heckeNode.version(), pkg.version);
});

test("markovZ is positive at substrate q_0", () => {
  const z = heckeNode.markovZ(Q_SUBSTRATE);
  assert.ok(z > 0, `markovZ(q_0) = ${z}, expected > 0`);
});

test("heckeH = q − q⁻¹ at substrate q_0", () => {
  const h = heckeNode.heckeH(Q_SUBSTRATE);
  const expected = Q_SUBSTRATE - 1 / Q_SUBSTRATE;
  assert.ok(
    Math.abs(h - expected) < 1e-12,
    `heckeH(q_0) = ${h}, expected ≈ ${expected}`,
  );
});

test("traceWeights returns 6 floats summing to ≈ 1 at substrate q_0", () => {
  const w = heckeNode.traceWeights(Q_SUBSTRATE);
  assert.equal(w.length, 6, "trace_weights should return 6 elements");
  const sum = w.reduce((a, b) => a + b, 0);
  // Normalised so weights sum to 1 — sanity check from gram.rs
  assert.ok(
    Math.abs(sum - 1) < 1e-10,
    `Σ weights = ${sum}, expected ≈ 1`,
  );
});

test("gramMatrix is 6×6", () => {
  const g = heckeNode.gramMatrix(Q_SUBSTRATE);
  assert.equal(g.length, 6, "Gram should have 6 rows");
  for (const row of g) {
    assert.equal(row.length, 6, "Gram should have 6 columns");
  }
});

test("gramMatrix is symmetric at substrate q_0", () => {
  const g = heckeNode.gramMatrix(Q_SUBSTRATE);
  for (let i = 0; i < 6; i++) {
    for (let j = i + 1; j < 6; j++) {
      assert.ok(
        Math.abs(g[i][j] - g[j][i]) < 1e-12,
        `Gram not symmetric: G[${i}][${j}] = ${g[i][j]} ≠ G[${j}][${i}] = ${g[j][i]}`,
      );
    }
  }
});

test("gramDet is positive at substrate q_0", () => {
  const d = heckeNode.gramDet(Q_SUBSTRATE);
  assert.ok(d > 0, `gramDet(q_0) = ${d}, expected > 0`);
});
