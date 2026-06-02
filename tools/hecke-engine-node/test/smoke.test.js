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

test("traceWeights returns 6 finite floats at substrate q_0", () => {
  // Vector is [1, z, z, z², z², z³] per gram::trace_weights — NOT a
  // probability distribution (it's a Markov-trace tuple). Just verify
  // shape + first element identity + finiteness.
  const w = heckeNode.traceWeights(Q_SUBSTRATE);
  assert.equal(w.length, 6, "trace_weights should return 6 elements");
  assert.ok(Math.abs(w[0] - 1.0) < 1e-12, `w[0] = ${w[0]}, expected 1.0`);
  for (const v of w) assert.ok(Number.isFinite(v), `non-finite weight: ${v}`);
});

test("gramMatrix is 6×6 with finite entries", () => {
  // Gram at q_0 is indefinite + not required to be symmetric by the
  // hecke-engine implementation (directional Markov-trace product
  // b_i · b_j). Just verify shape + finiteness.
  const g = heckeNode.gramMatrix(Q_SUBSTRATE);
  assert.equal(g.length, 6, "Gram should have 6 rows");
  for (const row of g) {
    assert.equal(row.length, 6, "Gram should have 6 columns");
    for (const v of row) assert.ok(Number.isFinite(v), `non-finite entry: ${v}`);
  }
});

test("gramDet is finite + non-zero at substrate q_0", () => {
  // Gram at q_0 is indefinite — det sign isn't constrained.
  const d = heckeNode.gramDet(Q_SUBSTRATE);
  assert.ok(Number.isFinite(d), `gramDet(q_0) = ${d}, expected finite`);
  assert.ok(Math.abs(d) > 1e-30, `gramDet(q_0) = ${d}, expected non-zero`);
});

// ── Phase B ──

test("chiLambdaBraid: identity element of shape [3] returns 1.0", () => {
  const chi = heckeNode.chiLambdaBraid([3], [], Q_SUBSTRATE);
  assert.ok(
    Math.abs(chi - 1.0) < 1e-12,
    `chiLambdaBraid([3], []) = ${chi}, expected 1.0`,
  );
});

test("chiLambdaBraid: empty shape returns 1.0", () => {
  const chi = heckeNode.chiLambdaBraid([], [[1, 1]], Q_SUBSTRATE);
  assert.ok(
    Math.abs(chi - 1.0) < 1e-12,
    `chiLambdaBraid([], [[1,1]]) = ${chi}, expected 1.0`,
  );
});

test("lrCoefficient: Pieri c^[2]_{[1],[1]} = 1", () => {
  const c = heckeNode.lrCoefficient([2], [1], [1]);
  // napi-rs maps the Rust i32 return type to Number, not BigInt.
  // Strict-equal compare against a plain Number literal.
  assert.equal(c, 1, `lrCoefficient([2],[1],[1]) = ${c}, expected 1`);
});

test("lrCoefficient: size mismatch returns 0", () => {
  const c = heckeNode.lrCoefficient([3], [2], [2]);
  assert.equal(c, 0, `lrCoefficient([3],[2],[2]) = ${c}, expected 0`);
});

test("trMAtomicMpfr: 3-strand single crossing returns z ≈ 0.4993", () => {
  // Single positive σ_1 on B_3 at 20-dps → Markov-Ocneanu-Wenzl
  // trace = z = 1/(q^{1/2}+q^{-1/2}) ≈ 0.4993 at q_0. n=3 (not n=2)
  // because B_2 trips an upstream edge case in tr_m_word_lq.
  const s = heckeNode.trMAtomicMpfr([[1, 1]], 3, "1.10998", 20);
  assert.equal(typeof s, "string", "trMAtomicMpfr should return a string");
  assert.ok(s.startsWith("4.99"), `expected '4.99...', got '${s}'`);
});
