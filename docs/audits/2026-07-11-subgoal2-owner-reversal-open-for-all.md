# Owner ruling: Subgoal-2 opened for all agents (general reversal of the 2026-05-08 decline)

**Date:** 2026-07-11
**Branch:** `claude/subgoal2-owner-reversal-open-for-all-2026-07-11`
**Type:** Owner ruling (records a standing scope decision; no compute).

## The ruling

The repo owner has **generally reversed** the 2026-05-08 coordination-ledger decline of
Subgoal-2 (the research-grade precision leg — 100× targets *below* the CAL-2 floor). The
previous state was: Subgoal-2 out of scope except for a **narrow** carve-out (2026-06-19,
the s5-so3 keystone geometric-realization build only), with all other Subgoal-2 work
requiring explicit per-item owner sign-off.

**New state (2026-07-11): Subgoal-2 is open for all agents.** The geometric /
substrate-derivation routes to the Subgoal-2 targets are no longer owner-gated and need
no per-item sign-off:

- absolute **m_p / m_n / m_⁴He** (3 ppt / 6 ppt / 0.6 ppt targets);
- **substrate-derivation of q_0** (the CAL-2 modulus);
- the per-isotope binding **`M_n(K)`** edge-set / coordination-graph closure — i.e. the
  M₃/M₄ weights of `conj:binding-manybody-eq-jet-filtration`;
- the **s5-so3 keystone** (`conj:s5-so3-fiber-action`), previously the only in-scope item.

## Why now — the trigger

The qou-v0yw binding-weight closure hit exactly this gate. The 13-part audit
[`2026-07-11-eigenfunction-weight-kernel-link-and-wn-derive-or-refute.md`](2026-07-11-eigenfunction-weight-kernel-link-and-wn-derive-or-refute.md)
(#3545) + #3534 established that the M₃/M₄ body-order weights are *extractable* from the
anchors (`w₂,w₃,w₄ = 4.353, 9.331, 15.919` MeV, Coulomb-corrected, no fit) but do **not
close** by any parameter-free constant-ratio kernel (best miss 6.9%), and that the only
honest closure path — a *derived* `R(q,x)` q-difference kernel / geometric bond-count — was
**owner-gated** behind the s5-so3 keystone. The per-order count PR
[#3588](https://github.com/litlfred/qou/pull/3588) confirmed the fit-free 2-body backbone
(`M_2=C(A,2)`), converging with the audit's Part-13 max-contact packing. The remaining
closure was blocked *only* by this gate plus the anti-fit rule; the owner has lifted the
gate.

## What the reversal does NOT change — anti-fit / anti-laundering stays

"Open for all" grants permission to **pursue and derive** the geometric / substrate routes.
It is **orthogonal** to the honesty discipline, which remains in force unchanged:

- the **Δ_λ "no seventh fit-based ansatz"** rule;
- the §**"Axiomatization is NOT a Proof"** anti-laundering rule;
- **"sorry-free ≠ derived"** and **"conditional-proved ≠ premise-established."**

Concretely: a `wₙ(K)` obtained by inverting the AME anchors is still a **fit** and must be
labelled one — it may **not** be wired to production dashboards as canonical. Only a
*derived* `R(q,x)` / geometric bond-count / substrate q_0 may be wired as canonical. If the
owner later wants fit-based results themselves wired as canonical, that is a **separate
ruling** not granted here.

## Where recorded (authoritative sites updated)

- [`AGENTS.md`](../../AGENTS.md) §"Precision goals" → Subgoal-2 (general-reversal banner).
- [`docs/precision-goals.md`](../precision-goals.md) §Subgoal-2 (general-reversal banner).
- [`docs/coordination/s5-so3-keystone.md`](../coordination/s5-so3-keystone.md) (top banner).
- [`docs/coordination/2026-06-05-step9-binding-closure.md`](../coordination/2026-06-05-step9-binding-closure.md) (cont.11).
- Bean `qou-v0yw` updated: the non-gated 2-body piece is done (#3588); the M₃/M₄ geometric
  closure is now open (ungated) for all agents.
