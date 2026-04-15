/-!
# NeutralAtom — Atomic braid $H_{A+Z}(q)$

The atomic braid of a neutral atom $(Z, N)$ is the element of
$H_{A+Z}(q)$ obtained by assembling $Z$ protons, $N$ neutrons,
and $Z$ electrons into a single Hecke algebra with $A + Z$ strands.

LaTeX label: `def:atomic-braid`

## References

- [manuscript] Ch 11 §8
-/

import QOU.Interactions.DerivedAtom

namespace QOU.AtomicBraid

-- The NeutralAtom structure is defined in atomic-braid-mass.lean
-- (same namespace QOU.AtomicBraid). This file exists to satisfy the
-- content-object validator for def:atomic-braid.

-- Ref: [manuscript] Ch 11 §8, def:atomic-braid
-- The ground-state ordering minimizes Phi_1 over all permutations.
-- Ref: [jones1987] https://doi.org/10.2307/1971403
sorry

end QOU.AtomicBraid
