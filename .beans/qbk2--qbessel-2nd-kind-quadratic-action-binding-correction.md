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
Owner closes (humans close beans per CLAUDE.md §4a).

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
