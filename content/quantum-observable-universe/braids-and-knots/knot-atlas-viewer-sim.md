**Recursive Knot-Atlas Viewer.**

*The Recursive Knot-Atlas Viewer is the interactive companion to
[`prop:recursive-atom-knot-atlas`](#prop:recursive-atom-knot-atlas).
It renders any knot or link from the atlas — basis-knots
$0_1, 3_1, 4_1, \mathcal{B}_3, L_H, 6_2, 8_{11}, L_{6a4}$ and every
ℓ = 1, 2 entry in the principled atlas table — as a parametric curve
projected through one of five user-selectable coordinate charts:*

1. *`briggs-klein-A1` — affine $(\Re w_1, \Im w_1, \Re w_2)$ slice;*
2. *`briggs-klein-A2` — $C_5$-symmetric pentagonal projection (default;
   surfaces the substrate's pentagonal motif);*
3. *`briggs-klein-A3` — Fubini–Study stereographic projection of the
   $\mathbb{CP}^1$ fibre;*
4. *`hyperbolic-B3` — volume-conformal "puff" skin from
   $\mathrm{Vol}_{\mathrm{hyp}}(K)$;*
5. *`polar-knot-projection` — standard 2D Markov-closure rendering for
   comparison with the historical literature.*

**Modes.**

*The viewer has two modes, selectable from the top bar:*

- *`basis-knot` — render a single basis or building-block knot from the
  `building_block_knots` panel of the witness;*
- *`confined-baryon` — render a confined composite (proton, neutron,
  light atom) with its sub-knot quark/nucleon constituents arranged
  about a categorical centre.  Three sub-knot **scaling formulas** are
  selectable:*
  1. *`S1` — $h^2$ Gröbner–Shirshov grade scaling;*
  2. *`S2` — energy-ratio scaling $E_\ell(q)/E_{\ell+1}(q)$ matching
     [`def:confinement-level`](#def:confinement-level) (default);*
  3. *`S3` — $q$-hook scaling $[h_x(\lambda)]_q$.*

*Three **categorical-centre** options are available:*
*$C_6$ (unknot at origin, default), $C_3$ (Wedderburn-block centroid),
and $C_1$ (Markov-trace centroid).  The categorical formulation of
the centroid options is referenced informally pending a dedicated
`def:knot-categorical-centroid` definition.*

**No-hardcoded-values contract.**

*The simulator HTML at
`folio-assistant/simulators/knot_atlas_viewer.html` carries no QOU
numeric or knot-identity values — every datum (q₀, $\mathrm{Vol}(4_1)$,
braid words, AME masses, $\rho$-factors, methodology tags, hyperbolic
volumes) is read at runtime from
`knot-atlas-viewer-data.witness.json`.  The witness emitter
[`knot_atlas_viewer_data.py`](folio-assistant/computations/knot_atlas_viewer_data.py)
sources all values from `q_parameter.py`,
`mass-table-ppb.witness.json`,
`methodology-deprecation.witness.json`, and
`gb-filtration-jet-order.witness.json`.  If a value is not in the
witness, the simulator cannot show it.*

**WASM acceleration.**

*The viewer probes for `/wasm/qou_knot_kernel.js` on load and uses
the Rust-compiled WASM kernel for live $q$-slider recomputes (Markov
closure, Wedderburn-block dimensions, hyperbolic-volume estimates)
when present; otherwise it falls back to JS-only rendering of the
static witness data.  The Pyodide-backed
[`pyhecke_native`](tools/pyhecke-native) Emscripten wheel is reserved
for the next slice (opt-in via `?backend=pyodide`).*

**Stable URLs and atlas integration.**

*Every interactive state — knot, mode, chart, scaling, centre, $q$ —
is encoded in the URL query string via the **⎘ link** button, so atlas
markdown tokens can link directly into a chosen viewer state (e.g.
`#/simulate/sim:knot-atlas-viewer/default-atlas-overview?knot=proton&mode=confined&chart=briggs-klein-A2`).
The atlas renderer
[`recursive_atom_knot_atlas_render.py`](folio-assistant/computations/recursive_atom_knot_atlas_render.py)
emits these links automatically for every braid/closure token in the
atlas table.*
