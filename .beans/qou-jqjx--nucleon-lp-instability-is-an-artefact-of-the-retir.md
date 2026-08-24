---
# qou-jqjx
title: Nucleon LP instability is an artefact of the retired tr_M(e-) = z^3 weight
status: todo
type: task
created_at: 2026-08-24T20:58:50Z
updated_at: 2026-08-24T20:58:50Z
---

Found while closing qou-1ngr (gluon stabiliser feasible set), 2026-08-24.

`categorical-proton-properties.md:10` says the bare 9-crossing element B_3 x Delta_3(uud) violates Frobenius positivity and that "the gluon is strictly required by the LP dual"; the neutron block quotes tr_M = -0.006 (proton) and -0.132 (neutron) as the depth of that instability. Every one of those numbers comes from `computations/_deprecated/integer-lp-gluon.py` / `integer-lp-gluon.witness.json`, which computes the Markov trace with tr_M(e-) = z^3.

That weight was retired on 2026-05-19. The canonical value is TR_M[5] = h*z^2 + z (`tools/pyhecke/python/pyhecke/gram.py:220`, see `docs/audits/2026-05-19-trm5-markov-bug.md`), and `fundamental-knots-operator-basis.md` already quotes the corrected 0.551 in its operator table. The bare nucleon NF is dominated by its e- coefficient (~1.0), so the weight change moves tr_M by about +0.43.

Re-running the deprecated producer's own enumeration with only the trace weight swapped (scratch, no witness minted):

  retired  z^3:      proton base tr_M = -0.0059 UNSTABLE ; neutron -0.1322 UNSTABLE
  corrected h z^2+z: proton base tr_M = +0.4196 STABLE   ; neutron +0.2937 STABLE

If that holds up, the bare nucleon is already Frobenius-positive under the live convention, no gluon is required at all, and the min-|tr_M| optimum drops to a single sigma_0 at one crossing for both nucleons — which would erase the 2-versus-4 gluon-crossing asymmetry that carries m_n - m_p into CAL-2.

Caveat before acting: the scratch re-run reuses the deprecated script's own construction of the 9-crossing typed element (B_3, then sigma_0 / sigma_1 with -h/2 and -h shifts). If the live corpus builds the typed nucleon differently the base NF differs and the conclusion may not. Task: rebuild the typed nucleon against `pyhecke.gram` (canonical G and TR_M), decide whether the LP instability survives, and either re-witness the gluon selection or withdraw the "strictly required" claim.

Blocks: rem:categorical-proton-properties, rem:categorical-neutron-properties, rem:gluon-stabiliser-ledger (its caveat authorNote points here).
