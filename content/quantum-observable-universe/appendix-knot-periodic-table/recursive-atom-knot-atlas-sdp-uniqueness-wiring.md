## SDP-uniqueness wiring (Lean side)

**What this wiring certifies**: the *abstract framework demonstration*
of $T_w$ uniqueness at the empty-constraint SDP for a nucleus's
strand count. The **real per-nucleus SDP** (with non-empty
constraints from the mass formula and multi-term cost) is
per-nucleus substantive open work — see
[`docs/coordination/2026-05-30-sdp-uniqueness-status.md`](https://github.com/litlfred/qou/blob/main/docs/coordination/2026-05-30-sdp-uniqueness-status.md)
for the gating analysis.

Within that scope, each atlas entry has a corresponding sorry-free
SDP-uniqueness theorem on the Lean side. Take $^4$He: with mass
number $A = 4$ the strand count is $n = 3A = 12$, and the canonical
$T_w$ knot operator's uniqueness at the empty-constraint SDP
demonstration level is certified by the single parameterised
statement

$$
\texttt{nucleus\_uniqueness\_closed}\ (3A)\ : \ \text{(sorry-free, axiom-free)}
$$

instantiated at $3A = 12$. The same statement, supplied by the
parameterised `NucleusEmptySDPUniqueness` module, covers any nucleus
once $A$ (equivalently $n = 3A$) is fixed.

Named wrappers expose this at four granularity layers — from the ten
QOU-tracked R5-full nuclei, through per-element and per-stable-isotope
coverage, down to the generic module valid for any $n : \mathbb{N}$:

| Granularity | Lean file | Coverage |
|---|---|---|
| QOU-tracked R5-full nuclei | `Applied<Nucleus>Uniqueness.lean` (10 files) | $^2$H, $^3$H, $^3$He, $^4$He, $^6$Li, $^9$Be, $^{11}$B, $^{12}$C, $^{14}$N, $^{16}$O |
| Per-element (AME2020 ref) | `PeriodicTableUniqueness.lean` | 118 elements H..Og |
| Per-stable-isotope | `StableIsotopeUniqueness.lean` | 252 stable nuclides H..Bi |
| Generic | `NucleusEmptySDPUniqueness.lean` | Any $n : \mathbb{N}$ |

To cite a specific entry, use
`qou:QOU.BraidKnot.<isotope>_uniqueness_closed`; for atoms outside
the named-isotope set, apply `@nucleus_uniqueness_closed (3*A)`
directly with the atlas $A$. Element symbols follow `AtomicMass.lean`,
with an `_el` suffix where the short symbol collides with a reserved
Lean identifier (e.g. `n_el_uniqueness_closed` for nitrogen).
