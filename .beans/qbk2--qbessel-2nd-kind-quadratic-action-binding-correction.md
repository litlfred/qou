---
# qbk2
title: 'EXPLORE: q-Bessel 2nd-kind "quadratic action" as a mass/binding correction term'
status: in-progress
type: task
priority: normal
created_at: 2026-06-20T11:30:00Z
updated_at: 2026-06-20T12:30:00Z
parent: qz9k
---

> **GATE RUN 2026-06-20 (PR pending).** Formalize-first gate executed
> ([`docs/audits/2026-06-20-qbessel-second-kind-quadratic-action-gate.md`](../docs/audits/2026-06-20-qbessel-second-kind-quadratic-action-gate.md),
> `computations/qbeta/qbessel_second_kind_quadratic_action_gate.py`, ALL PASSED).
> Result: the 2nd-kind solution `g₂ = w^{-ν}Σd_k w^k` is parameter-free (q-Casoratian
> q-Abel `D·w^ν = const`, gate 1 ✓) but `~w^{-ν}`-SINGULAR at the substrate origin, so
> regularity EXCLUDES it from the on-shell regular-rep binding sum — the 2nd-kind
> "quadratic action" correction is **identically zero on-shell**, non-trivial only
> off-shell (q-Bessel resolvent `G ~ g₁(x_<)g₂(x_>)/D` with the `-w` source). PRUNES the
> on-shell binding scan. Any continuation must be off-shell (resolvent + explicit
> source) and still clear the cross-anchor gate. Owner closes (§4a).
>
> **OFF-SHELL FOLLOW-UP 2026-06-20 (PR pending).**
> ([`docs/audits/2026-06-20-qbessel-offshell-resolvent-quadratic-correction.md`](../docs/audits/2026-06-20-qbessel-offshell-resolvent-quadratic-correction.md),
> `computations/qbeta/qbessel_offshell_resolvent_quadratic_correction.py`, ALL PASSED).
> Result: the coincidence-limit propagator `G(w)=g₁g₂/D` is REGULAR at the origin
> (finite limit `1/(q^{-ν}-1)`) — the `w^{-ν}` singularities of `g₂` and the Casoratian
> `D` cancel. So the QUADRATIC (bilinear) 2nd-kind object IS origin-admissible though
> the linear `g₂` is not: "quadratic action" names exactly the channel where the 2nd
> kind survives on-shell. REFINES the gate (linear exclusion stands; quadratic
> propagator distinct + admissible). STILL OPEN for a binding number: needs (i) the
> physical source the propagator contracts against, (ii) the cross-anchor gate; and
> bar-parity of `G` is ν-DEPENDENT (mixed sector — gate 2 caveat). No fit; nothing
> wired. Owner closes (§4a).
>
> **WIRING GATE 2026-06-20 — VERDICT: DO NOT WIRE (PR #2536).**
> ([`docs/audits/2026-06-20-qbessel-quadratic-binding-wiring-gate.md`](../docs/audits/2026-06-20-qbessel-quadratic-binding-wiring-gate.md),
> `computations/qbeta/qbessel_quadratic_binding_wiring_gate.py`). Ran the one-loop
> correction `δB=Σ_λ y_λ[G(w_atom)-G(w_free)]` on the real deuteron per-block characters.
> Four obstructions: (1) DECISIVE — `δB` swings 3.89..17.15 (63% spread) across equally-
> natural `(ν_λ,w_λ)` choices ⇒ the order+argument map is a free functional knob ⇒
> disguised 7th Δ_λ ansatz; (2) 83% of the correction is growth-sector (the blocks that
> cancelled in the A≥3 refutation); (3) natural integer rep-levels hit the Neumann log
> resonance `q^k=q^ν` (singular g₂); (4) mixed bar-parity. The only Lean-wireable lemma is
> the Casoratian regularity — a q-Bessel FACT, not a binding claim, so proving it does NOT
> make δB real (no production wiring, no appendix-mass-binding sync). Unblocking needs an
> INDEPENDENT substrate derivation of the order+argument map. The qbk2 exploration is
> structurally COMPLETE (object identified + characterised + shown non-wireable as-is);
> owner closes (§4a).

> **UNBLOCKER REFUTED 2026-06-20 — binding direction CLOSED (PR pending).**
> ([`docs/audits/2026-06-20-qbessel-unblocker-forced-order-refutation.md`](../docs/audits/2026-06-20-qbessel-unblocker-forced-order-refutation.md),
> `computations/qbeta/qbessel_unblocker_forced_order_refutation.py`). Attempted the
> substrate-forcing of `(ν_λ, w_λ)`. (R1, computed): the only rep-theoretic order
> `ν_λ=dim_λ-1` is INTEGER for every block ⇒ Neumann log-resonance where the #2533
> power-series `g₂` is SINGULAR (verified, deuteron). (R2, structural): the genuine
> integer-order log-Neumann `Y_n~J_n log(x)+reg` needs the RADIAL `x`, but the Markov
> trace fixes only the ANGULAR `θ_λ`; angular/radial are independent E_q(2) coordinates,
> so `x` is the SAME free knob that gave #2536's 63% swing — now named (the missing
> radial coordinate). A parameter-free correction needs a NEW substrate datum (canonical
> per-block radial coordinate) the trace cannot supply. The admissible object (#2530/#2533)
> stays real; its use as a parameter-free binding correction is refuted. qbk2 binding
> direction CLOSED; owner closes the bean (§4a).

> **REOPENED 2026-06-20 by owner Reeb-flow steer (PR pending).**
> ([`docs/audits/2026-06-20-qbessel-reeb-flow-radial-argument.md`](../docs/audits/2026-06-20-qbessel-reeb-flow-radial-argument.md),
> `computations/qbeta/qbessel_reeb_flow_radial_forced.py`). Owner: "did you use the Reeb
> bundle? there is a rotational flow on knot operations." #2538-R2 was incomplete — the
> Reeb FLOW supplies the radial datum: the rotation/growth split IS the angular/radial
> split (growth `θ_λ=arccosh` is a flow length, RADIAL). So `x_λ=θ_λ` is substrate-FORCED
> (no map freedom) and with `ν_λ=dim-1` BOTH order+argument are fixed ⇒ #2536's decisive
> 63%-swing obstruction is RESOLVED. Classical first pass (deuteron): (F) forced YES, (S)
> survives free→atom YES (δ=-0.172≠0), (C) scale ~25× small (crude: uniform weights +
> classical q→1 Bessel + large-order ν=15 suppression). Honest status: FORCED + SURVIVING,
> scale OPEN. Next forced test: q-deformed Hahn-Exton log-Neumann Y_ν(x;q) + real y_λ
> weights (NOT a tuned prefactor). #2538 "closed" was premature; direction LIVE again.

Owner-seeded exploration (2026-06-20): "2nd kind has a quadratic action that can be used in
mass/binding as corrections." Queued, NOT started.

## The idea

The Hahn–Exton q-Bessel q-difference equation is **second order**, so it has a second linearly
independent solution — the q-analogue of the Bessel **second kind** (Neumann `Y_ν` / the singular
partner). The existing corpus q-Bessel work
(`docs/audits/2026-06-13-reeb-phase-qbessel-identification.md`) develops only the **first kind**
`J_ν` (rotation regime) and the **modified** `I_ν` (growth regime). The second-kind / singular
solution is undeveloped. The owner's conjecture: its contribution enters mass/binding as a
**correction quadratic** in the relevant coupling (a second-order / `|Y|²`-type term beyond the
leading `J`/`I` contribution).

## Corpus-grep (before declaring this open)

- `grep -rn "q-bessel\|second kind\|Y_\\\\nu\|Neumann"` over `docs/`, `content/`, `computations/`:
  the 2026-06-13 audit + `QBesselContiguityRecurrence.lean` cover 1st-kind J and modified I only;
  no 2nd-kind (Y/Neumann) development found. Legitimate to queue.
- Adjacent: the keystone q-heat-kernel lead (`2026-06-20-keystone-qbessel-heat-kernel-lead.md`)
  notes 2nd-kind is the orbifold-fixed-point (singular) solution — same object, different use
  (keystone index vs binding correction).

## Formalize-first gate (STRICT — clear before any wide compute)

This is a binding-correction ansatz, so it sits under the Δ_λ / mass-multiplier discipline.
Before running any sweep it MUST clear:

1. **Refuted-class check.** Is this a disguised 7th Δ_λ ansatz? The six failed closures +
   GAP-A-4's 22 no-fit closures are CLOSED — a 2nd-kind term must NOT reintroduce a fitted
   per-partition multiplier (`docs/audits/2026-05-18-delta-lambda-gating-context.md`,
   `2026-06-05-gap-a4-final-retrospective.md`).
2. **Bar-parity.** Which bar sector (even=cosh/c_2, odd=sinh/c_3) does the 2nd-kind term live in?
   State it before computing (cf. the Jacobi–Anger bar-grading in the 2026-06-13 audit).
3. **Cross-anchor gate.** A single substrate-fixed coupling must reproduce the correction at the
   proton AND muon anchors with NO per-anchor refit (a refit = refutation, not a result).
4. **q-holonomic, not C-finite.** The 2nd-kind coefficients are q-holonomic (q-shift-dependent),
   matching the #1839 "no low-order constant recurrence" finding — verify, don't assume C-finite.
5. **Im(q)/regime explicit.** Rotation (real η, J/Y) vs growth (imag η, I/K); never silently
   `.real`.

## Definition of done

Either (a) a derive-or-refute structural statement: the 2nd-kind term IS / IS NOT a
cross-anchor-stable, bar-correct correction (TIERED report); or (b) a clean refutation on the same
footing as the f-map. No fit, no 7th ansatz, nothing wired to production without owner sign-off.
Owner closes (humans close beans per AGENTS.md §4a).

---

> **REOPENED + q-DEFORMED SCALE (2026-06-20, owner Reeb-flow steer).**
> Owner: "did you use the Reeb bundle? there is a rotational flow on knot operations."
> The unblocker refutation (#2538) was INCOMPLETE — the Reeb FLOW supplies the radial
> datum: growth `θ_λ=arccosh(|r|)` is a flow length (radial), so `x_λ=θ_λ` is
> substrate-FORCED (#2541, PR merged) ⇒ #2536's 63%-swing obstruction RESOLVED;
> correction forced + surviving but ~25× small at the classical first pass.
> q-DEFORMED scale test (#2545): Hahn-Exton `J_ν(x;q)` ≠ classical at fixed x, so done
> in the #2533 `G_q` convention — `|δ_q|/(B(D)/m_e)=6.16` vs classical 0.04 (~150× q-
> enhancement, into the binding ballpark, cross-anchor stable 3.3%). BUT critical-distance
> diagnostics DISQUALIFY it as forced: 43% swing under the ±0.5 half-integer proxy + 64%
> single-block domination by a dim=1 block at unphysical ν=−0.5. Status: PROMISING LEAD,
> proxy-limited — SUGGESTIVE not established. GATING next step: the genuine integer-order
> log-Neumann `Y_n` (ν→n limit, no ±0.5 proxy) + real `y_λ` weights + bar-parity. Matching
> B(D) by choosing the offset/prefactor would be a fit. No fit; nothing wired. (Direction
> is LIVE again; #2538 "closed" was premature.)

> **INTEGER-ORDER PROXY-FREE TEST (2026-06-20, PR pending).** #2545's 6× was a
> resonance-POLE artifact: G_q has a SIMPLE POLE at every forced integer ν≥1 (Neumann
> resonance) AND a CONFLUENT double-root at ν=0 (dim=1; indicial roots coincide,
> Casoratian→0). The ν±0.5 proxy sat 0.5 from these. Proxy-free PV (finite part of the
> antisymmetric pole, ε→0 convergent) on the dim≥2 blocks: δ_PV=5.52, ratio 1.27× B(D),
> un-dominated (31.6%), cross-anchor stable (0.76%) — ON scale, encouraging. BUT NOT
> established: (i) the dim=1 CONFLUENT blocks diverge (need the ν=0 confluent log
> solution — unsolved); (ii) PV-vs-rigorous-Y_n (L'Hôpital ν→n) unjustified. Two open
> constructions gate any claim. Reeb-flow argument (forced, surviving) stands; scale
> plausible but not honestly closed. No fit; nothing wired.

> **RIGOROUS (reduction-of-order) + LEAN (2026-06-20, PR #2549).** Resolved BOTH #2547
> gates with one construction: reduction of order recovers g2 from g1 + Casoratian
> (Jackson sum), resonance-free, finite at every integer order INCLUDING the ν=0
> confluent case. Self-checks pass (L[g2]~1e-30, Cas=w^-ν). Deuteron δ_rig=9.72,
> ratio 2.23× B(D)/m_e, un-dominated (25%), dim=1 finite, cross-anchor 5.9%. Progression:
> #2545 6.16 (proxy artifact) → #2547 1.27 (PV dim≥2 only) → #2549 2.23 (rigorous, all
> blocks). LEAN: QOU/QBeta/QCasoratianAbel.lean (casoratian_abel + qbessel_casoratian_qabel,
> the q-Abel backbone, sorry-free, generic CommRing) — a q-Bessel MACHINERY lemma, NOT a
> binding claim. Honest: strongest evidence yet that the direction is real (rigorous,
> on-scale ~2×, proxy-free) but NOT established — remaining gap needs real y_λ Markov
> weights + bar-parity (and cross-anchor 5.9% is a modest flag). 2.23→1 must come from
> forced y_λ, NOT a tuned prefactor. No fit; nothing wired.

> **GAP-NARROWING = DEFLATION (2026-06-20, forced y_λ weights).** Applied the canonical
> Markov weights y_lambda_at to the rigorous #2549 correction (binding sum is
> m_e Σ y_λ χ_λ Δ_λ; y_λ substrate-fixed → no knob). The 2.23× COLLAPSES: (A) Σ y·ΔG =
> -0.013×, (B) Σ y·χ·ΔG = -0.056× — both ~1-6% of B(D), i.e. ~20-80× TOO SMALL. The
> Markov measure concentrates on low blocks ([6],[5,1], y≈0.059, small ΔG) while the
> large-ΔG blocks driving the unweighted 2.23× carry tiny weight (y≈0.007). So the
> on-scale appearance (#2545/#2547/#2549) was an UNWEIGHTED-sum artifact. VERDICT: the
> q-Bessel "quadratic action" does NOT supply the binding correction — refuted as a
> binding mechanism by its own forced weighting (no fit could close 20-80× without
> abandoning the forced weights). STANDS: Reeb-flow radial (forced, real), reduction-of-
> order construction (rigorous), QCasoratianAbel.lean (sorry-free machinery). DOES NOT
> STAND: the physics/binding claim. Honest end of the binding thread. No fit; nothing wired.
