---
# qou-2cvs
title: 'Infra: FaddeevPhi holomorphicity endowment — ratio Ψ/Φ entire (hratio; closes uniqueUpToScalar via the landed reduction)'
status: todo
type: task
priority: normal
tags:
    - alien-habiro
created_at: 2026-07-18T18:06:37Z
updated_at: 2026-07-18T18:06:37Z
parent: qou-89f9
---

The surviving hard input after FaddeevRigidityReduction.lean (uniqueUpToScalar_of_ratio_entire, exit 0) reduced G3 rigidity to 3 named hyps. hratio = 'Ψ/Φ entire' is the endowment. NOT 'Φ_b entire' (false — meromorphic, poles on 1/b-lattice). Decompose: (i) add Φ_b holomorphic/meromorphic field to the FaddeevPhi class (honest structural strengthening — true of Φ_b); (ii) DIVISOR CANCELLATION — two solutions of the same difference eqs share zeros+poles ⇒ ratio removable-singularity ⇒ entire+nowhere-zero. Hard half is (ii): meromorphic-divisor argument, Mathlib meromorphic API thin. Also land hspan (b²∉ℝ, substrate arg b=π/4; fails real b) and hibinv-everywhere (identity theorem off dual lattice). Given all 3, the landed reduction closes uniqueUpToScalar by direct application. Anti-laundering: do NOT axiomatize hratio to 'close' it.
