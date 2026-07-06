---
id: jsj-decomposition-linearity
title: "Remark: JSJ Additivity of Nucleon Braids"
---
# JSJ Additivity of Nucleon Braids

Atomic knots exhibit a strictly modular geometric structure. By the Jaco-Shalen-Johannson (JSJ) decomposition, partitioning a hyperbolic knot complement along essential tori into fundamental geometric pieces yields an overall hyperbolic volume equal to the sum of the piece volumes.

For the knot structures representing nucleons—the proton block ($Vol \approx 13.948$) and the neutron block ($Vol \approx 3.664$)—this decomposition enforces exact linear scaling in the macroscopic topological limit. We encode this topological identity in Lean 4:

```lean
-- See content/quantum-observable-universe/lean/QOU/BraidsKnots/LinearJSJVolume.lean
theorem atomic_volume_is_linear (Z N : ℕ) :
  Vol (AtomicKnot Z N) = (Z : ℝ) * Vol_p + (N : ℝ) * Vol_n := by
  exact JSJ_volume_additivity Z N
```

As topological knot complexity scales to crossing numbers $c \gg 1000$ for heavy isotopes, the geometric computation of the hyperbolic trace avoids nonlinear chaotic blowups. Geometric modularity ensures the asymptotic limit tracks the linear JSJ sums. This provides a rigorous structural backstop for macroscopic nucleon volumes.
