## Build-pipeline integration

The atlas is auto-rendered by
[`recursive_atom_knot_atlas_render.py`](https://github.com/litlfred/qou/blob/claude/mass-units-bridge-followups/computations/recursive_atom_knot_atlas_render.py).

**Sources of truth** (in order):

1. [`confined-particle.md`](#def:confined-particle) — GB-NF particle registry (canonical $T_w$).
2. [`mass-table-ppb.witness.json`](https://github.com/litlfred/qou/blob/claude/mass-units-bridge-followups/computations/mass-table-ppb.witness.json) — D..${}^{40}$Ca (manual-historical, recursive, magic-A).
3. [`methodology-deprecation.witness.json`](https://github.com/litlfred/qou/blob/claude/mass-units-bridge-followups/computations/methodology-deprecation.witness.json) — per-particle methodology audit.
4. [`hp_volume.py`](https://github.com/litlfred/qou/blob/claude/mass-units-bridge-followups/computations/hp_volume.py) — $\geq 50$-digit symbolic-$q$ Markov-closure $\to$ $\mathrm{Vol}_{\mathrm{hyp}}$.
5. [`y_lambda_wenzl_bridge_extended.py`](https://github.com/litlfred/qou/blob/claude/mass-units-bridge-followups/computations/y_lambda_wenzl_bridge_extended.py) — symbolic-$q$ Wenzl bridge for $y_\lambda$.

For `principled-derivation` entries (electron, proton, neutron) the
hyperbolic volume of the Markov closure is computed from the
$\sigma$-braid word at $\geq 50$ decimal digits via
`hp_volume_of_link_closure(braid_word, digits=50)` which calls
SnapPy's `Link(braid_closure=...).exterior.high_precision`
inside `mpmath.workdps(50)`. Updates to any input propagate via
[`witness_staleness_tracker.py`](https://github.com/litlfred/qou/blob/claude/mass-units-bridge-followups/computations/witness_staleness_tracker.py)
to the rendered appendix on the next `bun run build`.

## SDP-uniqueness wiring (Lean side)

Each atlas entry has a corresponding **sorry-free SDP-uniqueness
theorem** in the Lean side, via the parameterised
`NucleusEmptySDPUniqueness` module and its three specialisation
layers. For any nucleus
characterised by mass number $A$ (yielding strand count $n = 3A$),
the canonical $T_w$ knot operator's uniqueness at the
empty-constraint SDP demonstration level is certified by:

$$
\texttt{nucleus\_uniqueness\_closed}\ (3A)\ : \ \text{(sorry-free, axiom-free)}
$$

Named wrappers exist at multiple granularity layers:

| Granularity | Lean file | Coverage |
|---|---|---|
| QOU-tracked R5-full nuclei | `Applied<Nucleus>Uniqueness.lean` (10 files) | $^2$H, $^3$H, $^3$He, $^4$He, $^6$Li, $^9$Be, $^{11}$B, $^{12}$C, $^{14}$N, $^{16}$O |
| Per-element (AME2020 ref) | `PeriodicTableUniqueness.lean` | 118 elements H..Og |
| Per-stable-isotope | `StableIsotopeUniqueness.lean` | 252 stable nuclides H..Bi |
| Generic | `NucleusEmptySDPUniqueness.lean` | Any $n : \mathbb{N}$ |

Usage example for any atlas entry: cite
`qou:QOU.BraidKnot.<isotope>_uniqueness_closed` in the
corresponding `.lean` content block's docstring. **Naming
convention**: the element symbol is taken from `AtomicMass.lean`;
elements whose short symbol collides with a reserved Lean
identifier (`n`, `p`, `s`, `b`, `k`, `v`, `y`, `i`, `u`, `w`)
receive an `_el` suffix (e.g. `n_el_uniqueness_closed` for
nitrogen, `b_el_uniqueness_closed` for boron). For atoms beyond
the named-isotope set, consumers can directly use
`@nucleus_uniqueness_closed (3*A)` with the appropriate $A$ value
from the atlas entry.

**What this wiring certifies**: the *abstract framework demonstration*
of $T_w$ uniqueness at the empty-constraint SDP for the
nucleus's strand count. The **real per-nucleus SDP** (with
non-empty constraints from the mass formula and multi-term cost)
is per-nucleus substantive open work — see
[`docs/coordination/2026-05-30-sdp-uniqueness-status.md`](https://github.com/litlfred/qou/blob/main/docs/coordination/2026-05-30-sdp-uniqueness-status.md)
for the gating analysis.

## Open

- **Principled derivation for ${}^{6}$Li, ${}^{7}$Li (and any new atom)**: the only
 admissible path is a **joint SDP on the full mass tower** — over all
 confinement levels $\ell$ and all atoms simultaneously — with
 **Gröbner–Shirshov filtration tracking** and **jet-order tracking**,
 yielding a canonical $T_w \in H_{n_0}(q_0)$ *per atom* as a structured
 certificate. Status: **certificate format proof-of-concept complete**
 ([`gb_filtration_jet_tracker.py`](https://github.com/litlfred/qou/blob/claude/mass-units-bridge-followups/computations/gb_filtration_jet_tracker.py)
 + [`gb-filtration-jet-order.witness.json`](https://github.com/litlfred/qou/blob/claude/mass-units-bridge-followups/computations/gb-filtration-jet-order.witness.json)).
 The reducer computes filtration grade + jet-order events exactly in
 symbolic $q$ via SymPy on the test cases $\sigma_1^3$ (electron) and
 $(\sigma_1 \sigma_2^{-1})^3$ (proton/neutron body). The joint-tower
 SDP solver consumes this certificate format. The Markov closure of $T_w$ is then taken in $S^3$ and
 $\mathrm{Vol}_{\mathrm{hyp}}$ is computed at $\geq 50$ decimal digits
 via `hp_volume_of_link_closure(braid_word, digits=50)`; comparison to
 the AME binding energy happens *a posteriori*. Per-atom volume-match search is FORBIDDEN as a
 derivation route — the SDP must be joint over the tower so the GB
 filtration and the jet ordering are consistent across confinement
 levels. Until that joint SDP is run, no principled ${}^{6}$Li / ${}^{7}$Li
 entry exists.
- **Structural rule for $\rho$ in $B = \rho \cdot m_e \cdot \mathrm{Vol}(K)$**:
 the pattern $\rho \in \{1, 2\}$ for $\ell \leq 2$ atoms does not extend to
 ${}^{6}$Li, ${}^{7}$Li. Open:
 derive $\rho(Z, N)$ from ILP / confinement structure.
- **Hyperbolic-knot identification beyond $\ell = 2$**: ${}^{9}$Be, ${}^{11}$B,
 ${}^{14}$N — no entries are in scope until a *principled* (GB-NF) derivation
 exists. Volume-match search will not be used.
- **Photon $\rho$-factor**: photon mass $= 0$ by definition (no $\rho$
 needed), but for the recursive structure may tie to gauge-boson
 Higgs coupling.
