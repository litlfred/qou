---
# qou-jqjx
title: Nucleon LP instability is an artefact of the retired tr_M(e-) = z^3 weight
status: completed
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


## Resolved 2026-08-24 — the instability is entirely the retired weight

Probe kept at `computations/probes/nucleon-lp-convention-probe.py` (no witness
minted; it is a convention comparison, not a corpus number).

Method answers the bean's own caveat: the typed nucleon is built by the
**retired script's own construction**, quoted line for line (`B_3`, then
`sigma_0` / `sigma_1` with the `-h/2` and `-h` shifts; proton lines 141-144,
neutron 164-168), so the only thing that varies between rows is the convention.
The construction is validated by reproducing the corpus's own published numbers
on the retired convention.

| convention | z | tr_M(e-) | proton | neutron |
|---|---|---|---|---|
| OLD (retired script) | 1/(sqrt q + 1/sqrt q) | z^3 | **-0.005936** | **-0.132224** |
| HALF (trace only) | old | h z^2 + z | +0.419562 | +0.293691 |
| **D (live)** | q^3/(q^2+1) | h z^2 + z | **+0.544370** | **+0.408267** |

Row 1 is the corpus's quoted `-0.006` / `-0.132`, reproduced to the digit. Row 3
is what `pyhecke.gram` exports and what `computations/universal-ilp.py` consumes
through `hecke_core` — i.e. the corpus's own *cited* live producer is already on
this convention while its prose quotes the retired one.

**Every intermediate step is positive too**, which kills the neutron block's
separate claim that "the sigma_0 channel violates Frobenius positivity following
the second quark crossing":

    proton  B_3 +0.998562 -> +0.605510 -> +0.279195 -> +0.544370
    neutron B_3 +0.998562 -> +0.501130 -> +0.172959 -> +0.408267

### The singular-Gram objection, checked rather than assumed

`gram.py`'s header warns that fixing the trace alone "drops a singular Gram into
a path with nothing to handle it", so the HALF row above is exactly the half-fix
it warns about. Checked directly: under D the Gram has `lambda_min = 3.1e-16`
against a next eigenvalue of 0.753, and the measured null vector matches the
header's closed form `(-1/q)^len(w)` to 3.3e-16 with `||G v||_max = 8.3e-17`. A
genuine radical.

**It does not reach this verdict.** Frobenius positivity tests `G x >= 0`, and
`G(x - c v) = G x` exactly when `G v = 0` — the test is already well defined on
the quotient. Measured: both nucleons carry a *large* radical component (-0.431,
-0.530), and projecting it out moves `min(G x)` by 5.6e-17 against margins of
+0.339 and +0.218. Margin-to-noise 1.1e15 and 6.9e14. The warning is about
inverting `G`, which this computation never does.

### Consequences, and the one that matters

1. "The bare 9-crossing element violates Frobenius positivity" — **false**.
2. "The gluon is strictly required by the LP dual" — **false**; bare is feasible.
3. The corpus's quoted optima now *lose to doing nothing*: proton `sigma_0.
   sigma_0` ranks 10/41 at 0.615 against bare 0.544; neutron `L_+.L_-` ranks
   26/41 at 0.690 against bare 0.408.
4. **The 4-versus-2 asymmetry is gone.** Under min-|tr_M| the optimum is a
   single `sigma_0` at ONE crossing for both nucleons (0.339 / 0.218) — ratio
   1:1. Under the minimum-crossing objective `def:universal-ilp-algorithm`
   actually states, 0:0. The neutron block says that split "is what carries the
   mass split into Q_beta", so `m_n - m_p` loses its stated mechanism.

Nothing is proposed in its place. That is deliberate: the derivation needs
re-deriving, not patching, and guessing a replacement would repeat the failure
mode that produced this — a number carried forward past the convention it was
computed in.

### Landed

Withdrawals as `authorNotes` plus struck prose on `rem:categorical-proton-
properties` and `rem:categorical-neutron-properties`; `rem:gluon-stabiliser-
ledger`'s open caveat (1) closed with the measurement. Its caveat (2)
(`qou-v5fp`) is made sharper, not moot: the two objectives no longer disagree
about which nucleon needs more gluon, they agree there is no asymmetry — so
v5fp still needs an answer but can no longer rescue the split either way.

**Not touched.** Quark content, charges, the NF coefficients themselves (the
Hecke multiplication table does not involve `tr_M`, so they are convention-
independent), beta decay, and the mass formula's other inputs.
