# lean-docs — Lean knowledge-graph viewer for qou (state branch, never merged)

A thin viewer (`lean/index.html`, `viewer.js`) plus JSON shards loaded on demand
(`lean/data/index.json`, `names.json`, `m/<Module>.jsonld`, `m/<Module>.<k>.sig.json`)
for the qou Lean packages **QOU, UGB, Fred2005** and their **content-block sibling
modules** (QOUBlocks, UGBBlocks, Fred2005Blocks). Mounted at `lean/` by
`state-mount --id lean-docs`; the site build copies it to the `lean` route.

- Open a declaration: `lean/#/m/<Module>/<declName>` (module page: `lean/#/m/<Module>`).
  `data/names.json` is `[[declName, moduleIdx, kindIdx], ...]` indexing `data/index.json` `modules`.
- Built from qou 7341d18daa5d: doc-gen4 1cd7a11 `single` per module (doc-data only; its
  static HTML is not published), Lean v4.24.0, mathlib f897ebc, then
  `lean-kg-publish.ts --no-rail`. **Not railed** — the site build adds the chrome.
- Provenance, counts and coverage: `manifest.json`.
