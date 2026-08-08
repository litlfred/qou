---
# qou-ndsa
title: 'Break the confinement-LP homogeneity: get the braid into t or G, not just n_target'
status: todo
type: task
priority: high
created_at: 2026-08-07T17:16:15Z
updated_at: 2026-08-07T17:16:15Z
---

THE ONLY SURVIVING FORM of the owner's SDP-offset proposal (2026-08-07).

Two readings have now been excluded, each for a DIFFERENT structural reason,
and both exclusions point at the same fix.

1. ANGLE-STRUCTURE LP (qbeta_sdp_angle_offset_theta_probe.py): the offset
   x_geom - x_LP vanishes identically (2.4e-16, 5.0e-16) because both anchors
   sit at the symmetric point — 4_1 is 2 regular ideal tetrahedra, B_3 is the
   regular ideal octahedron decomposition. PROVED in general:
   QOU/Knot/SymmetricOptimum.lean `optima_coincide` — two concave objectives
   INVARIANT under the symmetry share their optimum. An informative offset
   needs a SYMMETRY-BREAKING objective.

2. CONFINEMENT LP (qbeta_confinement_sdp_offset_homogeneity_probe.py): the
   canonical program `min t.x s.t. 1^T x = n_target, Gx >= 0` is HOMOGENEOUS —
   Gx >= 0 is a cone, so the feasible set at net n is n times the fixed
   polytope at 1. Measured: x*(n) = (n/n0)x*(n0) to 5.7e-14, offset angle drift
   EXACTLY 0, ||offset||/n constant. Because t and G come from pyhecke.gram and
   are KNOT-INDEPENDENT, with only n_target = |tr_M(K)| varying, two knots give
   PARALLEL offsets: the angle is the same number for every knot and the
   magnitude is a constant times tr_M(K). One knot-dependent number, not two —
   ratio-shaped, hence unfalsifiable by `ratio_attained`.

THE COMMON DIAGNOSIS: in both cases the braid's own content never reaches the
part of the program that could break the degeneracy. In (1) the objective is
symmetric; in (2) the knot enters only the scalar net constraint.

THE TASK: find or construct a confinement formulation in which the braid's
operator content enters the OBJECTIVE t or the GRAM G — not merely n_target.
Candidates to examine:
  - `solve_frobenius_dual_lp(t, G, n_target, u_demand)` — the u_demand vector
    is a per-channel demand PROFILE, not a scalar. If u_demand is knot-derived
    and not proportional to a fixed vector, homogeneity breaks and the offset
    direction becomes knot-dependent. CHECK THIS FIRST — it is the cheapest.
  - a Gram built from the braid word itself (G_ij = tr_M(beta_K b_i b_j))
    rather than from the bare NF basis.
  - the dense-PSD lift (`operator_selection_sdp.rs`), where off-diagonal
    correlations enter and the diagonal-lift equivalence fails.

ACCEPTANCE BAR (unchanged, and it is the whole point): the formulation must
yield BOTH theta values ABSOLUTELY, with the metric/normalization fixed IN
ADVANCE, and land on the A-free curve
(L - theta_mu^2)/(L - theta_p^2) = S_mu/S_p = -0.2453912076. A ratio does not
qualify — that is Lean-proved, not an opinion.

Cross-refs: PR #4513; qou-qnnq (the gap), qou-offl, qou-krvm.
