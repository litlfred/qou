---
# qou-8bxv
title: 'Two Skein normalisations are live: AGENTS 7a mandates h=q-1/q, the beta rate uses s=sqrt-q'
status: in-progress
type: task
priority: high
created_at: 2026-09-05T09:51:36Z
updated_at: 2026-09-05T10:21:17Z
---

## 2026-09-05 — measured, Lean-carried, PR #6820

Producer `computations/markov/skein_normalisation_two_conventions_audit.py` 8/8;
Lean `QOU/Braiding/SkeinNormalisation.lean` 7 decls, lean-direct exit 0,
sorry-free, generic `{K} [Field K]`; audit doc
`docs/audits/2026-09-05-two-skein-normalisations-are-live.md`.

**The two relations are NOT rescalings.** Weight ratio on `(L_+ : L_-)` is `1`
in (H) and `q^2` in (J); a rescaling `[L] -> c[L]` fixes that ratio, so they
agree only at `q^2 = 1`. Lean `no_rescaling_of_skein_weights`. This is the part
that matters — the natural reading "one relation, bracket normalised
differently" is measurably false.

**Bridge (exact):** `h_1 = s*(q^1/2 + q^-1/2)`; `h_1^2 = [2]_q^2 - 4 =
s^2*([2]_q + 2)`; ratio `[2]_q + 2 = 4.0108968667071222998` at the proton pin.
The factorisation itself is ALREADY in the corpus
(`braids-and-knots/bar-involution-c5-algebraic-identities.md`) — the finding is
the live inequivalence, not the identity.

**Why it hid:** the cofactor `[2]_q + 2` is bar-EVEN while `s` is bar-ODD, so
bar parity — the usual separator here — cannot see the split.

**The straddle, sharper than first stated.** `prf:trace-ratio-observable`
(observations/trace-ratio-observable-proof.md L21, L29) takes the vertex
amplitude as `|skein_amp|^2`, `skein_amp = q^(1/2) - q^(-1/2)` — live (J).
`prf:hadron-half-life` item 1 REPLACES that `s^2` with `tr_Markov((s1 s2)^5)`
computed under the (H) Hecke relation. So the substitution changes the
CONVENTION as well as the coupling, and neither block says so.

**qou-ix74 unaffected:** `|W|^2/s^2 = 129.40510740356669955` (J) and
`|W|^2/h_1^2 = 32.263384401056933328` (H). Both far too large for a 10-17 %
correction. Register defect, not magnitude defect — stated explicitly because
the two preceding corrections in this arc (qou-xql6's s^4 power, qou-q2l7's
withdrawn order argument) WERE magnitude defects.

**Closes qou-q2l7's open remainder:** the `{1/2,1/2}` exponent pair is FORCED
by (J), not chosen.

**Surface:** 8 blocks, 5 chapters, all live at measurement.

### Two self-corrections

1. Producer said "seven content blocks" in three places against its own
   measured 8 (witness key was named `J_seven_content_blocks`). Fixed at the
   producer.
2. I nearly retracted a CORRECT claim. `grep skein_amp` returns hits only under
   `computations/_deprecated/`, and I read that as the citation pointing at
   dead code. The Python VARIABLE NAME is deprecated; the SYMBOL is live in a
   live content block. Conflating a variable name with a content-block symbol
   by shape was the error — the same class as the arity conflations AGENTS.md
   warns about.

### NEW and OPEN — a third weighting

`prf:hadron-half-life` item 4 carries `S_ab(q) = (q*mu_a + q^-1*mu_b) /
(q^(1/2) + q^(-1/2))`: (J)'s asymmetric numerator weights over the BAR-EVEN
cofactor, not the bar-odd bridge `s` that (J) would put there. Neither (H) nor
(J). Three readings open — a third normalisation, a sign slip for `s`, or a
deliberate symmetrising normalisation because it is a mass not an amplitude.
Deciding needs the derivation of `S_ab`; out of scope here, flagged so the
two-convention framing is not read as exhaustive.

### Still not decided (author's)

Restate the rate in (H) to match §7a, or amend §7a to record (J) as the
physics-sector convention. Nothing measured forces either. No content block and
no AGENTS.md line edited on this branch.
