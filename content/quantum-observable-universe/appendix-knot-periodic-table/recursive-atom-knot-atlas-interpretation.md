## Build-pipeline integration

The purpose of this integration is a single reproducible source of truth, so
the rendered appendix never drifts from the witnesses it summarizes. The atlas
is auto-rendered by
[`recursive_atom_knot_atlas_render.py`](https://github.com/litlfred/qou/blob/claude/mass-units-bridge-followups/computations/recursive_atom_knot_atlas_render.py).

**Sources of truth** (in order):

1. [`confined-particle.md`](#def:confined-particle) — GB-NF particle registry (canonical $T_w$).
2. [`mass-table-ppb.witness.json`](https://github.com/litlfred/qou/blob/claude/mass-units-bridge-followups/computations/mass-table-ppb.witness.json) — D..${}^{40}$Ca (manual-historical, recursive, magic-A).
3. [`methodology-deprecation.witness.json`](https://github.com/litlfred/qou/blob/claude/mass-units-bridge-followups/computations/methodology-deprecation.witness.json) — per-particle methodology audit.
4. [`hp_volume.py`](https://github.com/litlfred/qou/blob/claude/mass-units-bridge-followups/computations/hp_volume.py) — $\geq 50$-digit symbolic-$q$ Markov-closure $\to$ $\mathrm{Vol}_{\mathrm{hyp}}$.
5. [`y_lambda_wenzl_bridge_extended.py`](https://github.com/litlfred/qou/blob/claude/mass-units-bridge-followups/computations/y_lambda_wenzl_bridge_extended.py) — symbolic-$q$ Wenzl bridge for $y_\lambda$.

These compose in that order: the particle registry fixes the canonical $T_w$,
the mass-table witness supplies the tabulated masses, the methodology audit
tags each particle's derivation method, `hp_volume.py` supplies
$\mathrm{Vol}_{\mathrm{hyp}}$, and the Wenzl bridge supplies $y_\lambda$.

For `principled-derivation` entries (electron, proton, neutron) the
hyperbolic volume of the Markov closure is computed from the
$\sigma$-braid word at $\geq 50$ decimal digits via
`hp_volume_of_link_closure(braid_word, digits=50)` which calls
SnapPy's `Link(braid_closure=...).exterior.high_precision`
inside `mpmath.workdps(50)`. Updates to any input propagate via
[`witness_staleness_tracker.py`](https://github.com/litlfred/qou/blob/claude/mass-units-bridge-followups/computations/witness_staleness_tracker.py)
to the rendered appendix on the next `bun run build`.
