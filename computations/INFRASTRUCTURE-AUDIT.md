# Infrastructure audit — word shortcuts + jet/brane quadratic

Per user feedback, two systemic requirements:

1. **Symbolic in q throughout** — all Markov trace and V̂ computations
   should be in $\mathbb{Z}[q^{\pm 1}]$ (sympy or CRT reconstruction),
   with $q_0$ substitution only at the FINAL step.
2. **Whenever a word shortcut is applied**, there must be an
   `undo-to-quark` function that re-expands the shortcut back to its
   level-$k$ NF.  Infrastructure needs an audit for all shortcut
   usages.
3. **Quadratic structures (SDP) required at every jet level** — not
   just level 3 (pair).  Cross-terms at levels 4 (shell), 5
   (cross-shell), 6 (atom-electron), 7 (molecule) each need their own
   2×2 PSD block structure.

## Current word shortcuts in the codebase

| Shortcut | Where applied | Undo needed | Current status |
|----------|---------------|-------------|----------------|
| Proton = 1 word in H_3 | `mass_endomorphism.proton_cross` | Expand to 9 quark crossings + gluon | Defined as crossings_per_gen, implicitly expands |
| Neutron = 1 word in H_3 | `mass_endomorphism.neutron_cross` | Expand to 9 quark crossings + gluon | Same |
| Nucleon-shorthand atom (level 3) | `confinement_adaptive.py`, `heavy_atom_opts.py` | Expand to 3A quark strands | No undo function; per-nucleon chars cached |
| Magic-shell shorthand (level 4) | Not yet in code | Expand to full shell NF | Missing |
| Atom (nucleus+electrons, level 6) | Not yet in code | Expand to nucleus + Z electrons | Missing |
| Molecule (level 7) | Not yet in code | Expand to Σ atoms | Missing |

**Audit conclusion**: the level 3 (nucleon) shorthand HAS an implicit
undo via `atom_per_generator_volumes` expanding to 3A strands.
Levels 4–7 shortcuts don't exist yet — they need to be created WITH
their undo functions.

## Jet-level quadratic SDP — infrastructure needs

Each confinement level has adjacent-generator cross-terms requiring
a 2×2 PSD block:

| Level | Cross-term | PSD block structure | Status |
|-------|-----------|--------------------|---------|
| 2 (nucleon) | Intra-Borromean adjacent pairs | Σ z² Φ_q(V_0 V_1) | In mass_endomorphism.py |
| 3 (pair) | Adjacent inter-nucleon pairs | Σ z² Φ_q(V_i V_j) | In hecke_core.atom_per_generator_volumes |
| 4 (shell-magic) | Shell-closure adjacent | NOT IMPLEMENTED | Missing |
| 5 (cross-shell) | Shell-straddling cross | NOT IMPLEMENTED | Missing |
| 6 (atom-electron) | Electron-nucleus coupling | NOT IMPLEMENTED | Missing |
| 7 (molecule) | Covalent bond cross | NOT IMPLEMENTED | Missing |

Existing: `sdp_cross_channel.py` has continuous 2×2 PSD for level 3
(adjacent inter-nucleon pairs).  Needs to extend to higher levels.

## Path forward

Three parallel tracks:

### Track A: Symbolic-in-q arithmetic
- Replace `mass_from_tower` with symbolic version that keeps
  V̂_i^full as sympy Poly in $q$
- Evaluate at $q_0$ with mpmath only at final step
- For large A: sympy too slow → use CRT reconstruction of polynomial
  coefficients from mod-p evaluations
- `tower_binding_symbolic.py` exists but hits polynomial explosion
  at A=4 — CRT is the scalable path

### Track B: Shortcut infrastructure
- Define `undo_shortcut(level)` for each level's word shortcut
- For each level's primitive, provide the $J^\ell(q) \to J^{\ell-1}(q)$
  embedding explicitly
- Audit all current shortcut usages and add undo calls where needed

### Track C: Multi-level quadratic SDP
- Extend `sdp_cross_channel.py` to levels 4-7
- Each level contributes its own 2×2 PSD block constraints
- Combined MISDP: solve jointly across levels with integer constraints
- The quadratic cross-term at each level is bounded by the
  arithmetic-geometric mean constraint (already used in MISDP)

## Current files

- `mass_endomorphism.py` — per-nucleon tower (level 2)
- `hecke_core.py::atom_per_generator_volumes` — level 3 tower
- `confinement_level_walk.py` — level walk cache (levels 1-7
  structural only; no mass data yet for 4-7)
- `heavy_atom_opts.py` — opts 2, 3, 5, 7 cache (but level 5 = level 3
  shorthand, not level 4 shell-word)
- `sdp_cross_channel.py` — continuous SDP at level 3
- `misdp_cross_channel.py` — MISDP at level 3 (via enumeration)
- `tower_binding_full.py` — level 3 tower with ILP (~2.5% accuracy for
  A ≥ 11)
- `tower_binding_symbolic.py` — sympy symbolic (works for A ≤ 3)

## Next steps

1. **Implement undo_to_quark(atom, level)**: takes any
   level-ℓ word and expands to quark level. Start with level 3→2
   (already implicit), add 4→3, 5→3, 6→3, 7→3.
2. **Extend SDP to shell level (4)**: define shell-word operators,
   shell-closure PSD blocks.
3. **CRT polynomial reconstruction**: evaluate Markov traces at several
   rational $q_i$, reconstruct $\mathbb{Z}[q^{\pm 1}]$ polynomial
   coefficients, evaluate at $q_0$ exactly.
