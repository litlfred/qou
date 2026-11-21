## Provenance of the atlas entries

Every entry is computed from a single reproducible chain of sources, so the
table never drifts from the witnesses it summarizes. The atlas
is auto-rendered by
[`recursive_atom_knot_atlas_render.py`](../../../computations/recursive_atom_knot_atlas_render.py).

**Sources of truth** (in order):

1. [Confined particle](#def:confined-particle) — GB-NF particle registry (canonical $T_w$).
2. [`mass-table-ppb.witness.json`](../../../computations/mass-table-ppb.witness.json) — D..${}^{40}$Ca (manual-historical, recursive, magic-A).
3. [`methodology-deprecation.witness.json`](../../../computations/methodology-deprecation.witness.json) — per-particle methodology record.
4. [`hp_volume.py`](../../../computations/hp_volume.py) — $\geq 50$-digit symbolic-$q$ Markov-closure $\to$ $\mathrm{Vol}_{\mathrm{hyp}}$.
5. [`y_lambda_wenzl_bridge_extended.py`](../../../computations/y_lambda_wenzl_bridge_extended.py) — symbolic-$q$ Wenzl bridge for $y_\lambda$.

These compose in that order: the particle registry fixes the canonical $T_w$,
the mass-table witness supplies the tabulated masses, the methodology record
tags each particle's derivation method, `hp_volume.py` supplies
$\mathrm{Vol}_{\mathrm{hyp}}$, and the Wenzl bridge supplies $y_\lambda$.

For `principled-derivation` entries (electron, proton, neutron) the
hyperbolic volume of the Markov closure is computed from the
$\sigma$-braid word at $\geq 50$ decimal digits via
`hp_volume_of_link_closure(braid_word, digits=50)` which calls
SnapPy's `Link(braid_closure=...).exterior.high_precision`
inside `mpmath.workdps(50)`. When any input changes,
[`witness_staleness_tracker.py`](../../../computations/witness_staleness_tracker.py)
marks the affected entries stale and the atlas is recomputed from the sources
above; no entry is maintained by hand.
