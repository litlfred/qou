# Habiro framing of the keystone coupling — a flagged lead, and what it eases in exposition

**Date:** 2026-06-16
**Branch:** `claude/keystone-habiro-coupling-lead-2026-06-16`
**Status:** structural **lead** (identification, not derivation) + a concrete **exposition-easing** payoff for the
Q_β c_k ladder. No fit; coupling stays open.
**Discipline:** critical-distance (name the objects; refuse the unfalsifiable correspondence-chain).

## The lead (identification only)

Per #2409 the keystone full-Hecke trace is a Habiro-ring element at `q₀` (colour face). Its **spacetime**
counterpart is canonically named: the `2I` spin lift → `S³/2I` = the **Poincaré homology sphere**, whose WRT
invariant is the **Lawrence–Zagier quantum modular form** — a specific, well-studied Habiro-ring element. So the
keystone "coupling" is, in the Habiro ring, a relation between **two named elements**:

| side | Habiro element |
|---|---|
| spacetime | `WRT(S³/2I)` = Lawrence–Zagier quantum modular form (2I/E₈ McKay) |
| colour | full-Hecke Markov trace at `q₀` (principal specialization) |

**Verified arithmetic anchors** (`scripts/keystone_habiro_coupling_lead.py`, exit 0): `|2I|=120`,
`h(E₈)=h^∨(E₈)=30`, `|2I|=4·h(E₈)`, `dim E₈=248=rank·(h+1)=8·31`; `S³/2I` is the Poincaré homology sphere.

> **⚠ Critical-distance flag.** This **names** the two Habiro elements; it does **not** derive the coupling or
> the masses. Pushing to "the coupling *is* [formula]" by chaining `2I→E₈→Poincaré→Lawrence–Zagier→Habiro→masses`
> would be an **unfalsifiable correspondence-chain** — explicitly **not** done. The spacetime⊥colour coupling
> (the generation shift) remains the open keystone.

## What it eases — the Q_β c_k ladder (the honest payoff)

Given the coupling is open, the Habiro framing's concrete value is **exposition-easing**, chiefly for Q_β:

- Near `q=1` (the `q₀` regime) a Habiro-ring element has a **canonical Ohtsuki (perturbative) expansion**; its
  coefficients **are** the Ohtsuki invariants.
- The Q_β precision ladder `Q_β = Q_base·∏(1 + c_k u^k)` (`u = b·ℏ_q²`) is exactly such an expansion —
  [`docs/coordination/1ppq-qbeta.md`](../coordination/1ppq-qbeta.md) already invokes Ohtsuki, and CLAUDE.md
  names "the Q_β Habiro element" as the *permanent* `c_k` fix.
- **Reframing `c_k` as the Ohtsuki invariants of one Habiro element dissolves the per-coefficient mystery and the
  6-entry flip-flop framing**: the `c_k` are not free near-matches to settle one-by-one (`c_3` Taylor-exact?
  wired? un-wired?), they are the canonical Ohtsuki series of a single quantum invariant. "Is `c_3` fundamental"
  becomes "what is the 3rd Ohtsuki invariant" — a determined object, not a fit.

This is an **exposition / framing** simplification (a cleaner, principled account of an existing convergent
series), **not** a new physical claim and **not** a closure of the `c_k` values.

## Secondary easing — q₀-observables as one class

The same lens unifies the *exposition* of the q₀-observables: each predicted observable (masses, Q_β, …) is a
**quantum knot/3-manifold invariant (Habiro-ring element) evaluated at the substrate `q₀`** — one framing in
place of separate per-observable derivations. Again exposition-level; the per-observable physics is unchanged.

## Net

The Habiro framing is a **structural identification + an exposition simplification** (Q_β `c_k` → Ohtsuki
invariants; q₀-observables → Habiro evaluations), with a real bridge between the keystone and the Q_β goal (one
ring). It is **not** a derivation of the coupling — that is flagged open, and the unfalsifiable chain is refused.
No fit.

## Cross-references

- `docs/audits/2026-06-16-keystone-infinite-dim-full-hecke-realization.md` (#2409) — the three faces; Habiro home
- `docs/coordination/1ppq-qbeta.md` — Q_β c_k ladder (Ohtsuki already invoked); CLAUDE.md "Q_β Habiro element"
- `docs/coordination/s5-so3-keystone.md` — keystone ledger (coupling open)
- `scripts/keystone_habiro_coupling_lead.py` — arithmetic anchors (exit 0)
