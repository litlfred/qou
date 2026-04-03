/**
 * @snappea/kernel — SnapPea hyperbolic 3-manifold computations in WebAssembly
 */

export type SolutionType =
  | 'not_attempted'
  | 'geometric'
  | 'nongeometric'
  | 'flat'
  | 'degenerate'
  | 'other'
  | 'no_solution'
  | 'externally_computed'
  | 'unknown';

export type CuspTopology = 'torus' | 'Klein_bottle';
export type Orientability = 'orientable' | 'nonorientable';

/** Opaque handle to a SnapPea Triangulation (WASM heap pointer) */
export type TriangulationPtr = number;

export interface FillingCoeffs {
  m: number;
  l: number;
}

export interface GroupPresentation {
  num_generators: number;
  relations: string[];
}

export interface InitOptions {
  /** Custom URL/path for the .wasm file */
  wasmUrl?: string;
}

export interface SnapPeaKernel {
  /* --- Triangulation I/O --- */

  /** Parse a SnapPea-format triangulation string. Throws on invalid input. */
  triangulationFromString(data: string): TriangulationPtr;

  /** Serialize a triangulation to SnapPea format. */
  triangulationToString(tri: TriangulationPtr): string | null;

  /** Deep-copy a triangulation. */
  copyTriangulation(tri: TriangulationPtr): TriangulationPtr;

  /** Free a triangulation. Must be called to avoid memory leaks. */
  freeTriangulation(tri: TriangulationPtr): void;

  /* --- Basic properties --- */

  getName(tri: TriangulationPtr): string;
  getNumTetrahedra(tri: TriangulationPtr): number;
  getNumCusps(tri: TriangulationPtr): number;
  getOrientability(tri: TriangulationPtr): Orientability;

  /* --- Hyperbolic structure --- */

  /** Compute the complete hyperbolic structure. Returns the solution type. */
  findCompleteHyperbolicStructure(tri: TriangulationPtr): SolutionType;

  /** Get the hyperbolic volume. */
  volume(tri: TriangulationPtr): number;

  /** Get the current solution type. */
  solutionType(tri: TriangulationPtr): SolutionType;

  /* --- Dehn filling --- */

  /** Set filling coefficients on a cusp. */
  setCuspInfo(tri: TriangulationPtr, cuspIndex: number, m: number, l: number): void;

  /** Compute the filled hyperbolic structure. Returns the solution type. */
  doDehnFilling(tri: TriangulationPtr): SolutionType;

  /** Remove all Dehn fillings, restoring the complete structure. */
  removeDehnFillings(tri: TriangulationPtr): void;

  /* --- Cusp info --- */

  getCuspTopology(tri: TriangulationPtr, cuspIndex: number): CuspTopology;
  getCuspFillingCoeffs(tri: TriangulationPtr, cuspIndex: number): FillingCoeffs;

  /* --- Invariants --- */

  /** Chern-Simons value, or null if unknown. */
  chernSimons(tri: TriangulationPtr): number | null;

  /** Homology as array of elementary divisors (torsion coefficients). */
  homology(tri: TriangulationPtr): number[];

  /** Fundamental group presentation. */
  fundamentalGroup(tri: TriangulationPtr, simplifyPresentation?: boolean): GroupPresentation;

  /* --- Operations --- */

  /** Randomize/simplify the triangulation. */
  simplify(tri: TriangulationPtr): void;

  /** Orient the triangulation. */
  orient(tri: TriangulationPtr): void;

  /** Canonize the triangulation. Returns 0 on success. */
  canonize(tri: TriangulationPtr): number;

  /* --- Lifecycle --- */

  /** Module version string. */
  version(): string;

  /** Clean up all resources. Call when done. */
  destroy(): void;

  /** Raw Emscripten Module for advanced use. */
  _module: any;
}

/** Initialize the SnapPea WASM module. */
export function init(options?: InitOptions): Promise<SnapPeaKernel>;
