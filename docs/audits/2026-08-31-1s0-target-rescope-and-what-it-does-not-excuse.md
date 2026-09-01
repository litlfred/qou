# The ¹S₀ *energy* is not a framework target; the ¹S₀ *boundness* still is

**Date:** 2026-08-31 · **Bean:** `qou-brng` · **Arc:** `bk-crossing-mass-binding`
**Route 3 of 4** (owner-selected, 2026-08-31) · **Scope:** a claims-narrowing
proposal, plus the much larger part of it that must *not* be narrowed.

The option was put as *"re-scope the ¹S₀ channels as out-of-model"*. Working it
splits cleanly in two, and **only the smaller half survives**. Recording both,
because the half that does not survive is the one an agent would be tempted to
take.

---

## 1. What legitimately comes out of scope: the −0.066 MeV **number**

The framework's binding functional is

    B(K) = -alpha * log(mu)

which is the binding energy **of a bound state** — the pole of the S-matrix on
the physical sheet. Nature's ¹S₀ two-nucleon channels have no such pole. They
carry a **virtual state**: a pole on the *second* Riemann sheet, with

    a_s(nn) ~ -18.9 fm      a_s(pp) ~ -7.8 fm      a_s(pn, 1S0) ~ -23.7 fm

against a force range of ~1.4 fm. The quoted "−0.066 MeV" is not the energy of
any state; it is `hbar^2/(2*mu_red*a_s^2)`, a *parameterisation* of near-threshold
scattering. Asking `-alpha*log(mu)` to reproduce it is asking one kind of object
to equal another.

Worse, it is a quantity the framework has no channel for **in principle**, and
the corpus already says so
(`docs/audits/2026-08-09-two-nucleon-channels-isospin-not-crossing-count.md` §4):

> the ¹S₀ scattering length is unnaturally large … i.e. a **near-critical fixed
> point** — fine-tuning, not symmetry. The framework produces `O(alpha) ~ 4.7 MeV`
> symmetric splittings and has no mechanism to tune one to threshold.

A framework whose natural scale is `alpha = 4.186 MeV` reproducing `0.066 MeV`
would require a cancellation to 1.6 %, from a structure with no small parameter.
That is not a precision failure; it is a category mismatch. **So: the ¹S₀ energy
should not appear as a scored row in any L2 accuracy table**, and the framework
should not claim it.

## 2. 🛑 What does NOT come out of scope, and this is the larger half

**The framework predicts the diproton and the dineutron are BOUND.** That is a
falsifiable claim about the existence of a state, and it is **wrong**:

    B_framework(pp) = +2.5416 MeV        nature: NO bound state
    B_framework(nn) = +3.3069 MeV        nature: NO bound state

Re-scoping the *energy* does not touch this. **Boundness is not a magnitude, it
is a sign, and the sign is a prediction the framework makes and gets wrong.** A
re-scope that quietly took the whole ¹S₀ row off the table would be using a
legitimate observation about *one* quantity to retire a failure about a
*different* one. That is exactly the move `AGENTS.md` §"Before declaring
refuted / ruled out" and §"Axiomatization is NOT a Proof" exist to prevent, run
in reverse.

Stated as the two claims they are:

| claim | status |
|---|---|
| "the framework predicts `B(pp) = −0.1 MeV`" | **withdrawn** — the target is not a binding energy, and the framework has no channel for a near-critical fine-tuning |
| "the framework predicts pp and nn are unbound" | **RETAINED, and currently FAILED** |

The second is the sector's open defect and it stays open. Everything the arc
established this session is about that one, not about the first:
`single_crossing_binds` (sorry-free), the stacked-family magnitude minimum, the
`mu_+ + mu_-  = 1` projector exclusion, and the Hoefsmit off-diagonal exclusion
all concern **whether anything in the algebra can produce `mu > 1` at all** —
i.e. boundness, not magnitude. None of them is affected by route 3.

## 3. What this changes in practice

**Changes:** any L2 / per-observable accuracy artifact that carries a ¹S₀
*energy* row should drop it as unscoreable, with a pointer here — the same
treatment `m_e` and `m_p` already get as calibration round-trips rather than
predictions (`AGENTS.md` §Precision goals, the `beats_100x_scoreable` rule).
**Nothing currently scores it**, so this is a pre-emptive rule rather than an
edit to a live number: it prevents a future agent from adding the row and
reporting a 6× or 60× miss on a quantity the framework never claimed.

**Does not change:** the L2 headline. The count stays **1/5 scoreable, 0/5
unconditional**. No row moves, no number improves. Route 3 buys honesty about
*what is being claimed*, not accuracy.

**Does not change:** the binding sector's blocker. `B(pp) > 0` and `B(nn) > 0`
remain wrong, every in-algebra mechanism for fixing them is now excluded, and
the L2 binding claim stays gated behind that — **signs before digits**, with the
signs still uncarried.

## 4. Why this is recorded rather than just done

Narrowing what a framework claims is a decision with a reader on the other end.
The owner selected route 3 among four on 2026-08-31; this document is what that
selection authorises and, more importantly, **what it does not**. An agent
reading "the ¹S₀ channels were re-scoped out" without §2 would conclude the
two-nucleon sector has no open defect. It has one, it is a sign error, and it is
the reason the binding route to 1 ppQ is blocked.

## References

- `docs/audits/2026-08-09-two-nucleon-channels-isospin-not-crossing-count.md`
  — the four-channel table, the Pauli spin↔isospin lock, the near-critical
  fixed-point observation, `content_keyed_interface_refuted`.
- `content/quantum-observable-universe/lean/QOU/QBeta/SingleCrossingAlwaysBinds.lean`
  — no single crossing can unbind while `q³ < q² + 1` (sorry-free).
- `computations/probes/stacked_unbinding_family_exclusion_probe.py` (#6407)
  — stacked family magnitude minimum; `mu_+ + mu_- = 1` projector exclusion.
- `computations/probes/hoefsmit_offdiagonal_exclusion_probe.py` (#6408)
  — the off-diagonal binds for every `q`; the projectors *are* the bond block.
- `computations/probes/two_nucleon_sector_sign_probe.py`, bean `qou-0pzi`
  — the sign failure itself.
