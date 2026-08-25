---
# qou-l7vf
title: 'ROAST (c3-via-Borel program state, 2026-08-01): we built rigorous scaffolding around a target we haven''t shown is in the right q-regime. #1 load-bearing UNEXAMINED premise: c3 (archimedean, real q0≈1.1097) = a resurgent Stokes datum (fibre-level, root-of-unity / |q|→1). If no fibre→observable bridge exists, the whole Borel/Kashaev route is mis-targeted and today''s scaffold is orthogonal to c3. TEST THE BRIDGE BEFORE transcribing more matrices.'
status: completed
type: task
created_at: 2026-08-01T19:38:36Z
updated_at: 2026-08-01T19:38:36Z
---

Adversarial assessment of the whole c₃-via-Borel push, per the
Critical-distance license. The discipline of the individual PRs today was
good (honest negatives, no fits, gaps beaned); this roast is about the
*program*, not the craftsmanship.

## 1. We reproduced machinery, not physics.
Everything that landed today — 5₂ AK integral (#4475), 4₁ Stokes series =
divisor function (#4474), the Lean conditional bridge (#4476), the realness
lemma (#4485), the Stokes prefactor now running — is **transcription and
formalization of published knot-invariant mathematics**. None of it derives a
single QOU observable. "4₁ Stokes series = σ₀(n)" is a lovely fact about the
figure-eight; it has **zero** QOU content — it's a self-check that our
arithmetic works. We built a very rigorous scaffold around an empty center.

## 2. The torsion tension points the wrong way and was charitably under-read.
τ_adj(4₁) = 1/√−3 (non-integer, in ℚ(√−3)); ρ_F = ν_SDP is an integer {1,2}.
The agent called it a "type/role mismatch" and preserved the internal
ρ_F = ν_SDP claim. Step back: the *appeal* of "ρ_F = Kashaev density" was that
the hyperbolic/Kashaev story would **explain** the density. The actual
topological density (the torsion) is a non-integer in a number field; the QOU
density is a small integer; there is **no derivation bridging them** (bean
b55d is a placeholder for a "normalization/order map" that does not exist).
That is not merely a "different slot" — it is a sign the "Kashaev density"
*naming* was aspirational: the corpus named ρ_F after a mechanism it does not
actually instantiate.

## 3. qnnq keeps being reframed, not closed — four wrong framings in one day.
"braid → (m,ℓ)" (wrong: summed, not selected) → "A_ω = 3 scalar" (wrong:
it's a matrix) → "ϑ off-lattice = obstruction" (wrong: category error, ϑ_K
transcendental by construction) → "ϑ_K free per-particle" (wrong: geometric
cusp shape is knot-fixed). Healthy error-correction — but a target that
dissolves under every close look may not be **well-posed**. The "surviving
open DOF" has been redefined four times in a day. And the *current* framing
("which Stokes-matrix entry does a braid select, and how does c₃ read off
it") still contains an untested load-bearing premise (§4).

## 4. THE load-bearing unexamined premise: c₃ is a resurgent Stokes datum.
c₃ is an **archimedean** coefficient — evaluated at the fixed real substrate
q₀ ≈ 1.1097 (observable level). The entire GGM/FW resurgent structure lives
at **q = root of unity / |q| → 1** (Kashaev N→∞) or in the formal-q fibre.
The corpus's OWN `meridian-holonomy-boost` says: at real q₀>1 the meridian
turn is a **boost**; only at |q|=1 is it a compact spin. Per AGENTS.md
§"Im(q) at fibre vs observable level", the Stokes/Kashaev data is a
**fibre-level** object. **Is there any established bridge from the
root-of-unity resurgent Stokes data to a real-q₀ archimedean coefficient?**
If NO, then c₃-via-Borel is attacking the wrong q-regime and today's entire
scaffold — however rigorous — is **orthogonal to c₃**. No amount of
transcribing GGM matrices fixes a regime mismatch. This question should be
answered BEFORE more transcription; it is the actual gate.

## 5. c₃ has a flip-flop graveyard — the danger is the NEXT step.
AGENTS.md documents the c₃ wire/un-wire flip-flop (6-entry ledger), the
dropped fitted-Habiro tower (+242 ppb regression), c₃=−2 as "near-match, not
Taylor-exact." The program has repeatedly mistaken near-matches for
derivations *here specifically*. Today was disciplined — but the next step
(reading c₃ off a Stokes matrix) is **exactly** where a plausible integer
coincidence would get mistaken for a derivation. Guard it hardest.

## Verdict + the one thing to do next
Not wasted — naming the exact objects (FW / GGM / McPhail-Snyder / torsion)
and proving the realness lemma are real value, and the discipline held. But
**we spent a day building rigorous scaffolding around a target we have not
shown is even in the right q-regime.** The single highest-value next action is
NOT the ri9w Stokes transcription — it is a **focused probe/argument on the
fibre→observable bridge (§4)**: does a real-q₀ archimedean c₃ have any rigorous
relationship to root-of-unity resurgent Stokes constants? If the honest answer
is "no known bridge," say so and re-scope c₃-via-Borel as fibre-structural
(interesting, not observable-closing) rather than spend more effort
transcribing matrices that would be orthogonal to the target. The ri9w agent's
output is only *meaningful* conditional on that bridge existing.
No fit, nothing wired.

## VERDICT (2026-08-01) — the roast's §4 worry was too strong; answer is (b) PARTIAL

Resolved by `docs/audits/2026-08-01-fibre-to-observable-bridge-verdict.md` (PR
#4520). The fibre-vs-observable *distinction* is correct and load-bearing, but
the implied "mis-targeted" worry is **refuted by the corpus** — recording the
correction here for honesty:

1. **The bridge EXISTS and is Lean-proved.** Quantum modularity
   (Zagier / Garoufalidis–Zagier) → the Ohtsuki-tower expansion at the
   *imaginary* substrate `b = √(log q₀/2π)·e^{iπ/4}` (so `2πb² = i·log q₀`) IS
   the fibre-object-evaluated-at-real-q₀ map — `OhtsukiTowerBarParity.lean`
   `even_rung_real` / `odd_rung_imaginary`, sorry-free. Median resummation
   (McSpirit–Rolen 2505.00799) is the "recover the value from divergent
   asymptotics" theorem; Wheeler et al. 2304.07001 prove the
   Habiro↔strange-identity↔Borel chain. So "is there ANY bridge?" — **yes.**
2. **c₃-even is CLOSED and never needed Borel** (substrate-exact ℚ(√3) ũ-ladder,
   archimedean face π²/5; feeds anchor-blind `Re 𝔙 = Vol`).
3. **c₃-odd is the genuine gap**, two-part: the smooth Borel–Padé sum of the 4₁
   tower is **anchor-blind** (no swing); the anchor-dependent 2.375 % swing is
   **Lean-forced onto the quantum complex volume 𝔙_q(Φ_b)**
   (`SRigidityPrune.no_anchor_invariant_realizes_swing`, sorry-free); and
   beneath it `S = Q_β/E₀` is a **CAL-2 input** (deriving it = Subgoal-2).

**Corrected verdict: (b) PARTIALLY on-target — scope-(a)-incomplete, NOT
scope-(b)-mis-targeted.** Not (a) because the value is undelivered
(anchor-blindness + the open integer-Stokes `A_ω = 3` keystone + S is a
calibration input). Not (c) because "mis-targeted" would be a scope-(b)
exclusion with no forbidding invariant — the *opposite* proved invariant forces
the odd channel onto the resurgent object. The scaffold this branch built is
therefore **on the right object**, not orthogonal — my roast over-claimed on
that point. The real remaining physics is `qou-ujmw` (derive `A_ω = 3` as a
DT / 3d-index count) + Subgoal-2 (derive `S = Q_β/E₀`). No fit, nothing wired.
