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
