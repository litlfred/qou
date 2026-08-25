---
# qou-niah
title: Third live z spelling 1/[2]_q sits at no Wenzl level
status: todo
type: task
created_at: 2026-08-16T12:54:36Z
updated_at: 2026-08-16T12:54:36Z
---

z = 1/(q + q^-1) = q/(q^2+1), numerically 0.4972905456 at the proton pin. It is NOT z_C (0.4993203342) and NOT z_D (0.6126880371). Its formal Wenzl level is 2.6136.

Live in executable code, not just prose:
  - computations/probes/meson_lepton_knot_dictionary_probe.py:104, inside a
    function named markov_trace_h2 whose docstring self-labels it 'Wenzl
    Jones-Markov' — i.e. it names C/D's referent while computing neither.
  - computations/probes/casimir_phi_q_markov_probe.py:126, as z_M_v3.

Neither is a production file, and the registry's discovery pattern structurally
cannot see them: its R4/R5 rule requires the function name to contain
'borromean'. The registry logs the 1/delta vs z_C confusion as a PROSE
conflation (bean qou-98g5) listing two non-code sites; these two are code.

Proved (symbolic-exact, scope-(b)) in computations/probes/wenzl_level_family.py
check W9 that it is at no level, by a DIFFERENT invariant than z_C: q/(q^2+1)
IS in Q(q), so the field argument does not apply; instead z_r has numerator
q^(2r-1), so numerator degree 1 forces r = 1, and z_1 = q != q/(q^2+1).

Next step: decide whether these two probes are wrong (should be z_D) or are
deliberately computing something else and should say so. Also worth widening
the registry's R4/R5 discovery pattern, which cannot currently reach them.

Found while mapping the Wenzl level family, PR #5229.
