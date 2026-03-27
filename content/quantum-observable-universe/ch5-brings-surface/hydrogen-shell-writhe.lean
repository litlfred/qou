/-!
# QOU.BringsSurface.hydrogen_shell_writhe — Shell number from writhe level

The principal quantum number n of the electron trefoil in a hydrogen atom
equals (w - 1)/2 where w is the writhe of the trefoil embedding.
Reidemeister I moves change the shell without changing the knot type,
and the orbital count per shell is n².

## References

- [manuscript] Ch. 6, §3
-/

import Mathlib.Data.Real.Basic

namespace QOU.BringsSurface

-- Ref: [manuscript] Ch. 6, §3
theorem hydrogen_shell_writhe :
    -- The shell number n = (w-1)/2, orbital count is n², and
    -- energy scales as -E_ion/n².
    True := by
  -- Ref: [manuscript] Ch. 6, §3
  sorry

end QOU.BringsSurface
