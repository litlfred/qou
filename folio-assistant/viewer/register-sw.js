/**
 * Register the Pyodide cache Service Worker.
 *
 * Call this lazily — e.g., when a user first opens a simulator,
 * not on page load. This avoids any overhead for users who never
 * interact with simulators.
 *
 * Usage:
 *   import { registerPyodideSW, getCacheStatus } from './register-sw.js';
 *   await registerPyodideSW();           // register on first simulator open
 *   const status = await getCacheStatus(); // check what's cached
 */

let _registration = null;

/**
 * Register the Service Worker (idempotent — safe to call multiple times).
 * Returns the ServiceWorkerRegistration.
 */
export async function registerPyodideSW() {
  if (_registration) return _registration;
  if (!("serviceWorker" in navigator)) {
    console.warn("[sw] Service Workers not supported");
    return null;
  }

  try {
    _registration = await navigator.serviceWorker.register(
      "/sw-pyodide-cache.js",
      { scope: "/" }
    );
    console.log("[sw] Pyodide cache SW registered");
    return _registration;
  } catch (err) {
    console.error("[sw] Registration failed:", err);
    return null;
  }
}

/**
 * Query the SW for cache status.
 * Returns { pyodide: { cached, entries }, deps: { cached, entries } }.
 */
export function getCacheStatus() {
  return new Promise((resolve) => {
    if (!navigator.serviceWorker?.controller) {
      resolve({ pyodide: { cached: false, entries: 0 }, deps: { cached: false, entries: 0 } });
      return;
    }

    const handler = (event) => {
      if (event.data?.type === "CACHE_STATUS_RESPONSE") {
        navigator.serviceWorker.removeEventListener("message", handler);
        resolve(event.data);
      }
    };
    navigator.serviceWorker.addEventListener("message", handler);
    navigator.serviceWorker.controller.postMessage({ type: "CACHE_STATUS" });

    // Timeout after 2s
    setTimeout(() => {
      navigator.serviceWorker.removeEventListener("message", handler);
      resolve({ pyodide: { cached: false, entries: 0 }, deps: { cached: false, entries: 0 } });
    }, 2000);
  });
}

/**
 * Clear all cached assets (e.g., for version upgrades).
 */
export function clearCache() {
  return new Promise((resolve) => {
    if (!navigator.serviceWorker?.controller) {
      resolve(false);
      return;
    }

    const handler = (event) => {
      if (event.data?.type === "CACHE_CLEARED") {
        navigator.serviceWorker.removeEventListener("message", handler);
        resolve(true);
      }
    };
    navigator.serviceWorker.addEventListener("message", handler);
    navigator.serviceWorker.controller.postMessage({ type: "CLEAR_CACHE" });

    setTimeout(() => {
      navigator.serviceWorker.removeEventListener("message", handler);
      resolve(false);
    }, 2000);
  });
}
