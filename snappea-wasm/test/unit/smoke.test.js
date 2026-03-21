/**
 * T0 — Smoke tests for snappea-wasm
 *
 * These verify the absolute basics:
 * - WASM module loads
 * - Triangulation can be parsed and round-tripped
 * - Basic properties are accessible
 * - Volume computation returns reasonable values
 */

import { describe, it, expect, beforeAll, afterAll } from 'vitest';
import { readFileSync } from 'fs';
import { join } from 'path';

// The init function — adjust path based on build output location
let init;
let kernel;

beforeAll(async () => {
  // Dynamic import to handle both CJS and ESM
  const mod = await import('../../dist/index.js');
  init = mod.init || mod.default?.init;
  kernel = await init();
});

afterAll(() => {
  if (kernel) kernel.destroy();
});

describe('T0 — Smoke Tests', () => {
  it('should return a version string', () => {
    const version = kernel.version();
    expect(version).toBeTruthy();
    expect(typeof version).toBe('string');
  });

  it('should parse a triangulation from string', () => {
    const data = readFileSync(
      join(__dirname, '../fixtures/m004.tri'),
      'utf-8'
    );
    const tri = kernel.triangulationFromString(data);
    expect(tri).toBeTruthy();
    expect(tri).not.toBe(0);
    kernel.freeTriangulation(tri);
  });

  it('should read basic properties of m004 (figure-eight knot)', () => {
    const data = readFileSync(
      join(__dirname, '../fixtures/m004.tri'),
      'utf-8'
    );
    const tri = kernel.triangulationFromString(data);

    expect(kernel.getName(tri)).toBe('m004');
    expect(kernel.getNumTetrahedra(tri)).toBe(2);
    expect(kernel.getNumCusps(tri)).toBe(1);
    expect(kernel.getOrientability(tri)).toBe('orientable');

    kernel.freeTriangulation(tri);
  });

  it('should compute the volume of m004', () => {
    const data = readFileSync(
      join(__dirname, '../fixtures/m004.tri'),
      'utf-8'
    );
    const tri = kernel.triangulationFromString(data);

    // Must compute the hyperbolic structure before querying volume
    kernel.findCompleteHyperbolicStructure(tri);
    const vol = kernel.volume(tri);
    // The figure-eight knot complement has volume ~2.0298832128
    expect(vol).toBeCloseTo(2.0298832128, 6);

    kernel.freeTriangulation(tri);
  });

  it('should round-trip a triangulation through string serialization', () => {
    const data = readFileSync(
      join(__dirname, '../fixtures/m004.tri'),
      'utf-8'
    );
    const tri = kernel.triangulationFromString(data);
    const serialized = kernel.triangulationToString(tri);
    expect(serialized).toBeTruthy();
    expect(serialized).toContain('Triangulation');
    expect(serialized).toContain('m004');

    // Parse the serialized version
    const tri2 = kernel.triangulationFromString(serialized);
    expect(kernel.getName(tri2)).toBe('m004');
    expect(kernel.getNumTetrahedra(tri2)).toBe(2);
    kernel.findCompleteHyperbolicStructure(tri2);
    expect(kernel.volume(tri2)).toBeCloseTo(2.0298832128, 6);

    kernel.freeTriangulation(tri);
    kernel.freeTriangulation(tri2);
  });

  it('should copy a triangulation', () => {
    const data = readFileSync(
      join(__dirname, '../fixtures/m004.tri'),
      'utf-8'
    );
    const tri = kernel.triangulationFromString(data);
    kernel.findCompleteHyperbolicStructure(tri);
    const copy = kernel.copyTriangulation(tri);

    expect(copy).not.toBe(tri);
    expect(kernel.getName(copy)).toBe('m004');
    expect(kernel.volume(copy)).toBeCloseTo(2.0298832128, 6);

    kernel.freeTriangulation(tri);
    kernel.freeTriangulation(copy);
  });

  it('should get solution type', () => {
    const data = readFileSync(
      join(__dirname, '../fixtures/m004.tri'),
      'utf-8'
    );
    const tri = kernel.triangulationFromString(data);
    kernel.findCompleteHyperbolicStructure(tri);
    const type = kernel.solutionType(tri);
    expect(type).toBe('geometric');
    kernel.freeTriangulation(tri);
  });

  it('should throw on invalid triangulation data', () => {
    expect(() => {
      kernel.triangulationFromString('not a valid triangulation');
    }).toThrow();
  });

  it('should compute homology', () => {
    const data = readFileSync(
      join(__dirname, '../fixtures/m004.tri'),
      'utf-8'
    );
    const tri = kernel.triangulationFromString(data);
    const h = kernel.homology(tri);
    // m004 (figure-eight knot complement) has H_1 = Z (no torsion)
    expect(Array.isArray(h)).toBe(true);
    kernel.freeTriangulation(tri);
  });

  it('should compute fundamental group', () => {
    const data = readFileSync(
      join(__dirname, '../fixtures/m004.tri'),
      'utf-8'
    );
    const tri = kernel.triangulationFromString(data);
    const fg = kernel.fundamentalGroup(tri);
    expect(fg).toHaveProperty('num_generators');
    expect(fg).toHaveProperty('relations');
    expect(fg.num_generators).toBeGreaterThan(0);
    kernel.freeTriangulation(tri);
  });
});
