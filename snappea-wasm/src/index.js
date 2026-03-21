/**
 * @snappea/kernel — SnapPea hyperbolic 3-manifold computations in WebAssembly
 *
 * Computation-only module. No UI dependencies.
 * Embeddable in Node.js, browsers, Pyodide, Deno, Web Workers.
 */

let moduleFactory;
try {
  moduleFactory = require('./snappea_kernel.js');
} catch (e) {
  // Will be set during init() for ESM environments
  moduleFactory = null;
}

/**
 * Initialize the SnapPea WASM module.
 * @param {Object} [options]
 * @param {string} [options.wasmUrl] - Custom URL/path for the .wasm file
 * @returns {Promise<SnapPeaKernel>}
 */
async function init(options = {}) {
  const factory = moduleFactory || (await import('./snappea_kernel.js')).default;

  const moduleOpts = {};
  if (options.wasmUrl) {
    moduleOpts.locateFile = (path) => {
      if (path.endsWith('.wasm')) return options.wasmUrl;
      return path;
    };
  }

  const Module = await factory(moduleOpts);

  // Initialize the kernel
  Module.ccall('snappea_init', 'number', [], []);

  // Wrap C functions
  const _fromString = Module.cwrap('snappea_triangulation_from_string', 'number', ['string']);
  const _toString = Module.cwrap('snappea_triangulation_to_string', 'number', ['number']);
  const _freeString = Module.cwrap('snappea_free_string', null, ['number']);
  const _copy = Module.cwrap('snappea_copy_triangulation', 'number', ['number']);
  const _free = Module.cwrap('snappea_free_triangulation', null, ['number']);
  const _getName = Module.cwrap('snappea_get_name', 'string', ['number']);
  const _numTet = Module.cwrap('snappea_get_num_tetrahedra', 'number', ['number']);
  const _numCusps = Module.cwrap('snappea_get_num_cusps', 'number', ['number']);
  const _numOrCusps = Module.cwrap('snappea_get_num_or_cusps', 'number', ['number']);
  const _numNonorCusps = Module.cwrap('snappea_get_num_nonor_cusps', 'number', ['number']);
  const _orientability = Module.cwrap('snappea_get_orientability', 'number', ['number']);
  const _findStructure = Module.cwrap('snappea_find_complete_hyperbolic_structure', 'number', ['number']);
  const _volume = Module.cwrap('snappea_volume', 'number', ['number']);
  const _solutionType = Module.cwrap('snappea_solution_type', 'number', ['number']);
  const _setCusp = Module.cwrap('snappea_set_cusp_info', null, ['number', 'number', 'number', 'number']);
  const _doFilling = Module.cwrap('snappea_do_dehn_filling', 'number', ['number']);
  const _removeFilling = Module.cwrap('snappea_remove_dehn_fillings', null, ['number']);
  const _cuspTopology = Module.cwrap('snappea_get_cusp_topology', 'number', ['number', 'number']);
  const _chernSimons = Module.cwrap('snappea_chern_simons', 'number', ['number', 'number']);
  const _simplify = Module.cwrap('snappea_simplify', null, ['number']);
  const _orient = Module.cwrap('snappea_orient', null, ['number']);
  const _canonize = Module.cwrap('snappea_canonize', 'number', ['number']);
  const _homology = Module.cwrap('snappea_homology', 'number', ['number']);
  const _fundamentalGroup = Module.cwrap('snappea_fundamental_group', 'number', ['number', 'number']);
  const _version = Module.cwrap('snappea_version', 'string', []);

  const SOLUTION_TYPES = [
    'not_attempted', 'geometric', 'nongeometric', 'flat',
    'degenerate', 'other', 'no_solution', 'externally_computed'
  ];

  function readAndFreeString(ptr) {
    if (!ptr) return null;
    const str = Module.UTF8ToString(ptr);
    _freeString(ptr);
    return str;
  }

  /** @type {SnapPeaKernel} */
  const kernel = {
    triangulationFromString(data) {
      const ptr = _fromString(data);
      if (!ptr) throw new Error('Failed to parse triangulation data');
      return ptr;
    },

    triangulationToString(tri) {
      return readAndFreeString(_toString(tri));
    },

    copyTriangulation(tri) {
      const ptr = _copy(tri);
      if (!ptr) throw new Error('Failed to copy triangulation');
      return ptr;
    },

    freeTriangulation(tri) {
      _free(tri);
    },

    getName(tri) {
      return _getName(tri);
    },

    getNumTetrahedra(tri) {
      return _numTet(tri);
    },

    getNumCusps(tri) {
      return _numCusps(tri);
    },

    getOrientability(tri) {
      return _orientability(tri) === 1 ? 'orientable' : 'nonorientable';
    },

    findCompleteHyperbolicStructure(tri) {
      const type = _findStructure(tri);
      return SOLUTION_TYPES[type] || 'unknown';
    },

    volume(tri) {
      return _volume(tri);
    },

    solutionType(tri) {
      const type = _solutionType(tri);
      return SOLUTION_TYPES[type] || 'unknown';
    },

    setCuspInfo(tri, cuspIndex, m, l) {
      _setCusp(tri, cuspIndex, m, l);
    },

    doDehnFilling(tri) {
      const type = _doFilling(tri);
      return SOLUTION_TYPES[type] || 'unknown';
    },

    removeDehnFillings(tri) {
      _removeFilling(tri);
    },

    getCuspTopology(tri, cuspIndex) {
      return _cuspTopology(tri, cuspIndex) === 0 ? 'torus' : 'Klein_bottle';
    },

    getCuspFillingCoeffs(tri, cuspIndex) {
      const mPtr = Module._malloc(8);
      const lPtr = Module._malloc(8);
      Module.ccall('snappea_get_cusp_m_l', null,
        ['number', 'number', 'number', 'number'],
        [tri, cuspIndex, mPtr, lPtr]);
      const m = Module.getValue(mPtr, 'double');
      const l = Module.getValue(lPtr, 'double');
      Module._free(mPtr);
      Module._free(lPtr);
      return { m, l };
    },

    chernSimons(tri) {
      const knownPtr = Module._malloc(4);
      const value = _chernSimons(tri, knownPtr);
      const known = Module.getValue(knownPtr, 'i32') !== 0;
      Module._free(knownPtr);
      return known ? value : null;
    },

    simplify(tri) {
      _simplify(tri);
    },

    orient(tri) {
      _orient(tri);
    },

    canonize(tri) {
      return _canonize(tri);
    },

    homology(tri) {
      const ptr = _homology(tri);
      const json = readAndFreeString(ptr);
      return json ? JSON.parse(json) : [];
    },

    fundamentalGroup(tri, simplifyPresentation = true) {
      const ptr = _fundamentalGroup(tri, simplifyPresentation ? 1 : 0);
      const json = readAndFreeString(ptr);
      return json ? JSON.parse(json) : { num_generators: 0, relations: [] };
    },

    version() {
      return _version();
    },

    destroy() {
      Module.ccall('snappea_destroy', null, [], []);
    },

    // Expose raw Module for advanced use
    _module: Module
  };

  return kernel;
}

module.exports = { init };
