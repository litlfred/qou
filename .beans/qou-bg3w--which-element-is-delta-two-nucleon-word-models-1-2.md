---
# qou-bg3w
title: Which element is Delta? Two nucleon-word models (1-/2-crossing vs 11-crossing) both carry the name, and a possible third in pyhecke
status: todo
type: task
priority: high
created_at: 2026-08-28T15:47:38Z
updated_at: 2026-08-28T15:48:11Z
---

Parent: `qou-cds1`. Surfaced by
`computations/qbeta/qbeta_delta_element_fork_pricing_probe.py` (15/15, exact
symbolic Q(q)) and
`docs/audits/2026-08-28-cds1-two-nucleon-word-models.md`.

## The question

`qbeta-counit-closed-form.md` names ONE object -- *"Delta = NF(n) - NF(p), the
single-wrap normal-form difference of the neutron and proton typed-crossing
elements in H_3(q)"* -- and asserts two closed forms for it,

    eps(Delta) = h^2/2 - h        tr_M(Delta) = h^2/2 - h*z .

TWO different elements of H_3(q) answer to that description, and BOTH closed
forms hold for the smaller and FAIL for the larger. Nobody has chosen.

| | Delta_S | Delta_L |
|---|---|---|
| source | `deuteron-binding-dressing-proton-net.md` net coefficients | `hecke_core._PROTON_G0/_G1` etc. |
| crossings | 1 (p), 2 (n) -- DERIVED, see below | 11 each |
| net(Delta) | h^2/2 - h = epsNPq = -0.187207 | -0.233198 |
| tr_M^z | h^2/2 - h z (AFFINE in z) | QUADRATIC in z |
| chi^(2,1) | 0 identically | -0.106814 |

Delta_S's crossing count is derived, not assumed: a typed crossing (sigma+d)
has net = 1+d and net is multiplicative across DISTINCT generators, so
net(n) = 1 - 3h/2 + h^2/2 = (1 - h/2)(1 - h) exactly. Delta_L's 11 matches
`q-beta-c3-hopf-three-fold-markov.md`'s *"both 11 typed crossings"*.

Mechanism: net is NOT multiplicative WITHIN one generator, because
T_0^2 = h T_0 + 1 reduces -- net(T_0^2) = 1+h vs net(T_0)^2 = 1. So an
11-crossing word cannot carry a 1-crossing coefficient. Structural, not a slip.

## Why it is load-bearing for qou-cds1

1. The D-frame trace baseline (`-15.451 %`, `92.1x the entire five-rung
   ladder`) takes its counit from Delta_S and its Markov trace from Delta_L.
   Priced consistently on Delta_S it is **257.26x** -- the published figure
   UNDERSTATES by 2.793x. (Calibrated: the probe reproduces the committed
   92.1058... exactly, which is what proves the attribution.)
2. qou-cds1's **(D1)** -- `2*alpha = net(Delta) - tr_M^z(Delta)`, the ONLY
   derivation of the ladder phase the corpus has -- is AFFINE in z only because
   Delta_S is supported on {gamma, sigma0, sigma1}. On Delta_L it is quadratic,
   so alpha = (z-1)h/2 is not the counit-minus-trace gap there at all.
   **If Delta_L is canonical, (D1) is unavailable** and branch 3
   (KZ / Kohno-Drinfeld holonomy) is the only remaining home for a derivation
   of alpha.

## A possible THIRD model -- FLAGGED, NOT CLAIMED

`pyhecke.atom.PROTON_NF` / `NEUTRON_NF` have coordinate sums 0.999125 and
0.810835, difference **-0.188291** -- within 0.58 % of epsNPq, matching neither
Delta_S (-0.187207 exactly) nor Delta_L (-0.233198).

Those constants are stored **float64** and I did **not** verify that pyhecke
uses the same basis ordering, so the coordinate sum may not be `net`. Check the
basis convention FIRST; do not treat -0.188291 as a measurement until then.

## Not the same question as qou-avt6 / qou-goc9

Those are about the **augmentation** (sigma -> q, an algebra map). This is
about the **coordinate sum** `net` (T_w -> 1), which is what epsNPq actually is
(qou-99qc) and what Q_A is computed from. Under `net` the element DOES exist --
it is Delta_S. Neither result implies the other; do not merge them.

## What would close this

An owner/corpus call on which element the decay channel is about, or a
derivation that selects one. Until then the D-frame re-derivation cannot be
posed, because the phase leg's status depends on the answer.
