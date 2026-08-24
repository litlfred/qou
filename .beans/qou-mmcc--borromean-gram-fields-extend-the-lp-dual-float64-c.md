---
# qou-mmcc
title: 'borromean gram fields: extend the LP-dual float64 carve-out, or migrate the numpy path?'
status: todo
type: task
created_at: 2026-08-24T19:10:43Z
updated_at: 2026-08-24T19:10:43Z
---

The LAST entry in witness_raw_float64_audit's regressed list (108 -> 116), and
the only one of the original 13 that is genuinely a decision rather than work.
Deliberately not actioned.

WHY IT IS NOT LIKE THE OTHERS
The other twelve were all "the precision existed and was cast away at a
boundary". This one is not:

  computations/borromean-axial-coupling.py:101
      GRAM = np.array(_gram_data["gram_matrix"], dtype=float)
  :116
      GRAM_INV = np.array(_gram_data["gram_quotient_inverse"], dtype=float)
  :222
      pairing = float(u_A @ G_inv_A @ obs_A_vec)

A real numpy linear-algebra path. Feeding mpf into it triggers the
object-dtype trap this session already proved live in mass_at_3A_proper --
an mpf scalar times a float64 ndarray promotes to object dtype and `@`
becomes a pure-Python O(dim^3) loop. The file's own comment at :107 states
its accuracy claim in float64 terms ("pseudo-inverse of gram_matrix to
3.8e-16 relative").

IT IS ALREADY IN THE CARVED-OUT FAMILY, JUST NOT THE CARVED-OUT FIELD LIST
The witness carries the LP-dual fields primal_obj / dual_obj / duality_gap
and is gated by lp_dual_witness_validator.py. witness_raw_float64_audit
carves out exactly that family:

    LP_DUAL_F64_FIELDS = frozenset({
        "x_star", "y_star", "y0_star", "u_lambda_star",
        "primal_obj", "dual_obj", "duality_gap",
    })

The 116 float64 fields here are gram_matrix (36), gram_inverse (36),
char_on_basis (12), shadow_prices (6) and friends -- the bound-state
observable fields, gated by bound_state_observable_validator.py, which are
not in that set.

WHY IT IS AN OWNER CALL
Extending a carve-out is not a sweep. The sibling carve-out in that same
audit file is annotated "qou-7kq3, owner-approved 2026-08-15", and the
audit's own instruction is "do not add a file to a baseline, do not
--rebaseline, and do not hand-edit a number, to make this green".

THE TWO OPTIONS
  A. Extend LP_DUAL_F64_FIELDS (or add a sibling set) to cover the
     bound-state observable fields, on the same declared grounds as the
     existing carve-outs: f64 BY CONSTRUCTION, no higher-precision source to
     carry from. Cheap, and honest if the grounds hold.
  B. Migrate the gram path to mpmath linear algebra. Correct in principle,
     but it is a dim^3 pure-Python loop unless the whole chain moves, and the
     upstream gram witness would have to emit at higher precision first --
     it currently cannot, since the LP/SDP solver producing it is float64.

My reading is that A is right and B is not worth it, because the source data
genuinely has no more precision to carry. But that is a judgement about what
the gram matrix IS, not something to infer from the audit.
