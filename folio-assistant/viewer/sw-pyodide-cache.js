/**
 * Service Worker — Pyodide & heavy dependency cache.
 *
 * Strategy: Cache-first for immutable CDN assets (Pyodide WASM, packages).
 * On first simulator open, Pyodide is fetched from CDN and cached.
 * Subsequent loads serve from cache instantly (~0ms vs ~40MB download).
 *
 * Also caches: KaTeX, Three.js, and other simulator dependencies.
 *
 * Registration: The viewer registers this SW on first simulator open,
 * not on page load (no overhead for non-simulator users).
 *
 * Cache keys:
 *   pyodide-v<version>  — Pyodide core + packages
 *   simulator-deps      — KaTeX, Three.js, D3, etc.
 */

const PYODIDE_CACHE = "pyodide-v1";
const DEPS_CACHE = "simulator-deps-v1";
const WASM_CACHE = "qou-wasm-v1";

// Patterns that should be cache-first (immutable CDN assets)
const CACHE_PATTERNS = [
  // Pyodide (WASM + JS + packages)
  /cdn\.jsdelivr\.net\/pyodide/,
  /pyodide-cdn2\.iodide\.io/,
  /files\.pythonhosted\.org.*\.whl$/,
  // KaTeX (math rendering)
  /cdn\.jsdelivr\.net\/npm\/katex/,
  /cdnjs\.cloudflare\.com\/ajax\/libs\/KaTeX/,
  // Three.js (3D rendering)
  /cdn\.jsdelivr\.net\/npm\/three/,
  /unpkg\.com\/three/,
  // D3.js (visualization)
  /cdn\.jsdelivr\.net\/npm\/d3/,
  /d3js\.org/,
  // QOU WASM kernels (Rust→WASM, served from gh-pages /wasm/)
  /\/wasm\/.*\.(?:js|wasm)$/,
  // Pyodide-loaded Emscripten wheels (Slice C)
  /\.whl(?:\?wasm32)?$/,
];

// Determine which cache to use based on URL
function getCacheName(url) {
  if (/\/wasm\//.test(url)) return WASM_CACHE;
  if (/pyodide|\.whl/.test(url)) return PYODIDE_CACHE;
  return DEPS_CACHE;
}

// ── Install ──────────────────────────────────────────────────────
self.addEventListener("install", (event) => {
  // Activate immediately (don't wait for old SW to retire)
  self.skipWaiting();
});

// ── Activate ─────────────────────────────────────────────────────
self.addEventListener("activate", (event) => {
  event.waitUntil(
    caches.keys().then((keys) => {
      // Clean up old cache versions
      const validCaches = [PYODIDE_CACHE, DEPS_CACHE, WASM_CACHE];
      return Promise.all(
        keys
          .filter((k) => !validCaches.includes(k))
          .map((k) => caches.delete(k))
      );
    })
  );
  // Claim all open tabs immediately
  self.clients.claim();
});

// ── Fetch ────────────────────────────────────────────────────────
self.addEventListener("fetch", (event) => {
  const url = event.request.url;

  // Only intercept matching CDN requests
  const shouldCache = CACHE_PATTERNS.some((p) => p.test(url));
  if (!shouldCache) return;

  event.respondWith(
    (async () => {
      const cacheName = getCacheName(url);
      const cache = await caches.open(cacheName);

      // Cache-first: return cached response if available
      const cached = await cache.match(event.request);
      if (cached) return cached;

      // Fetch from network and cache for next time
      try {
        const response = await fetch(event.request);
        if (response.ok) {
          // Clone before caching (response body can only be consumed once)
          cache.put(event.request, response.clone());
        }
        return response;
      } catch (err) {
        // Network error — return a meaningful error response
        return new Response("Network error — asset not cached yet", {
          status: 503,
          headers: { "Content-Type": "text/plain" },
        });
      }
    })()
  );
});

// ── Message handling ─────────────────────────────────────────────
self.addEventListener("message", (event) => {
  if (event.data?.type === "CACHE_STATUS") {
    // Report cache status back to the requesting page
    Promise.all([
      caches.open(PYODIDE_CACHE).then((c) => c.keys()),
      caches.open(DEPS_CACHE).then((c) => c.keys()),
      caches.open(WASM_CACHE).then((c) => c.keys()),
    ]).then(([pyodideKeys, depsKeys, wasmKeys]) => {
      event.source?.postMessage({
        type: "CACHE_STATUS_RESPONSE",
        pyodide: {
          cached: pyodideKeys.length > 0,
          entries: pyodideKeys.length,
        },
        deps: {
          cached: depsKeys.length > 0,
          entries: depsKeys.length,
        },
        wasm: {
          cached: wasmKeys.length > 0,
          entries: wasmKeys.length,
        },
      });
    });
  }

  if (event.data?.type === "CLEAR_CACHE") {
    // Allow manual cache clearing (e.g., for version upgrades)
    Promise.all([
      caches.delete(PYODIDE_CACHE),
      caches.delete(DEPS_CACHE),
      caches.delete(WASM_CACHE),
    ]).then(() => {
      event.source?.postMessage({ type: "CACHE_CLEARED" });
    });
  }
});
