# lean-docs — rendered Lean docs for qou (state branch, never merged)

doc-gen4 HTML for the qou Lean packages **QOU, UGB, Fred2005**, at `lean/`, for the
site build to mount and publish at the `lean` route (and for the paper PDF's ∀ links,
which read `lean/declarations/declaration-data.bmp`).

- Source render: lake-cache branch `cat/folio-assistant-sci/lake-cache/qou-docgen4-v4-24-0`
  (doc-gen4 1cd7a11, Lean v4.24.0, mathlib f897ebc; built 2026-10-11 from qou 5697c31 by
  `lake -R -Kenv=dev build QOU:docs UGB:docs Fred2005:docs`).
- Staged with `folio-assistant-sci/adapters/paper/lean/lean-render.ts --modules QOU,UGB,Fred2005
  --no-rail`: Lake `.hash`/`.trace` left out, Mathlib/core pages pruned and their links
  rewritten to the community mathlib4 docs. **Not railed** — the site build's rail pass
  (`rail-standalone-pages.ts --foreign-site`) adds the harness chrome at publish.
- Known gap: the render predates every Lean change since 5697c31, and content-block
  sibling `.lean` files (the `QOUBlocks` library) are not documented at all.
  See `manifest.json`.
