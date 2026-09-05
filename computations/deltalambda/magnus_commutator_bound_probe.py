#!/usr/bin/env python3
"""magnus_commutator_bound_probe.py — a SIGN-KEEPING bound, from an identity this corpus already
proved and then did not use. (qou-o6ov)

WHY. #6754 closed the arc's chain end-to-end and measured that it is 2–550× loose, with the loss
concentrated in ONE link:

    |tr X| ≤ √(dim·‖X‖_F²)                                                              (link 1)

That link replaces a SIGNED trace by a norm, discarding every cancellation among the eigenvalues —
and the measurement says that discarded cancellation is the dominant part of the effect at large b.
So the majorant route gives the shape of the decay and structurally cannot give its size. A useful
bound has to keep the sign information.

THE IDENTITY IS ALREADY PROVED, AND WAS NEVER USED AS A BOUND. `QOU.MassTheory.
trace_mul_commutator_eq` (MagnusCurvatureCommutator.lean, #6534, sorry-free) states

    tr (ρ·(xy − yx)) = tr ((ρx − xρ)·y)

i.e. tr(ρ[x,y]) = tr([ρ,x]·y). Applied to Ω₂^P = c·Σ_a [σ_a, σ_{a+1}]:

    tr_λ(ρ·Ω₂^P) = c · Σ_a tr_λ( [ρ, σ_a] · σ_{a+1} )                                       (C)

I proved that in #6534 as a structural identity about where the curvature trace lives, and then
spent the following PRs bounding ‖ρ·Ω₂‖_F anyway. It is exactly the sign-keeping reformulation the
#6754 measurement asks for.

WHY (C) SHOULD BE TIGHTER, and it is two separate gains, reported separately below:
  (i) `|tr(AB)| ≤ ‖A‖_F·‖B‖_F` (Cauchy–Schwarz for the Frobenius inner product) carries NO √dim
      factor, where link 1 does. On its own that is a √dim improvement — a factor 14.7 at dim 216.
  (ii) ‖[ρ, σ_a]‖_F retains the cancellation between ρσ_a and σ_aρ. Bounding ‖ρ·Ω₂‖_F destroys it;
       ρ is a long word and σ_a nearly commutes with most of it, so the commutator is far smaller
       than the product of the norms.

    |tr_λ(ρ·Ω₂^P)| ≤ c · Σ_a ‖[ρ, σ_a]‖_F · ‖σ_{a+1}‖_F                                    (NEW)

WHAT IS BEING TESTED. (C) is a theorem, so checking it numerically tests the ARITHMETIC. What is
NOT a theorem, and is the point: whether (NEW) is materially tighter than the old chain, per shape
and per level — and whether it still DECAYS with b, since a tighter bound that stops decaying would
be useless for this bean. Both are reported; a tighter-but-flat bound is called out as a failure,
not presented as progress.

The two gains are separated by also reporting (NEW) with the commutator replaced by ‖ρ‖_F‖σ_a‖_F,
which isolates how much comes from dropping √dim versus from the commutator itself. Without that
split, a √dim win would be indistinguishable from a cancellation win.

scope-(a); NO-FLOAT64 (mpf; dps asserted at every compute entry). Nothing wired.
"""
from __future__ import annotations

import argparse
import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, _HERE)
sys.path.insert(0, os.path.dirname(_HERE))  # computations/

import mpmath as mp  # noqa: E402

import he4_magnus_omega2_sign_sparse_probe as base  # noqa: E402
from mass_at_3A_proper import atom_braid_word_3A  # noqa: E402

_WANT_DPS = None


def _assert_dps(where):
    if _WANT_DPS is not None and mp.mp.dps != _WANT_DPS:
        raise RuntimeError(f"mp.mp.dps is {mp.mp.dps}, expected {_WANT_DPS}, at {where}")


def measure(lam, gens, q, ngen):
    """One column sweep giving everything both bounds need.

    Returns dict with the signed trace, ‖X‖_F², ‖ρ‖_F², ‖[ρ,σ_a]‖_F² per a, ‖σ_a‖_F² per a,
    and the identity-(C) right-hand side computed independently of the left.
    """
    _assert_dps(f"measure({lam})")
    per_gen, dim = base.block_structure(tuple(lam))
    sig = base.sigma_csr(per_gen, dim, q)
    c = 4 / (q + 1 / q) ** 2
    rev = list(reversed(gens))
    na = ngen - 1

    tr = mp.mpf(0)                       # tr(ρ Ω₂^P)          — the target
    frob_X = mp.mpf(0)                   # ‖ρ Ω₂^P‖_F²         — the old route
    frob_rho = mp.mpf(0)                 # ‖ρ‖_F²
    frob_comm = [mp.mpf(0)] * na         # ‖[ρ,σ_a]‖_F²        — the new route
    rhs_C = [mp.mpf(0)] * na             # tr([ρ,σ_a] σ_{a+1}) — identity (C), computed separately

    def apply_rho(v):
        for g in rev:
            v = base.spmatvec(sig[g], v)
        return v

    for j in range(dim):
        e = [mp.mpf(0)] * dim
        e[j] = mp.mpf(1)

        # --- old route: X e_j = ρ·Ω₂^P e_j, giving the trace and ‖X‖_F together ---
        acc = [mp.mpf(0)] * dim
        for a in range(na):
            u = base.spmatvec(sig[a], base.spmatvec(sig[a + 1], e))
            w = base.spmatvec(sig[a + 1], base.spmatvec(sig[a], e))
            for r in range(dim):
                acc[r] += u[r] - w[r]
        Xe = apply_rho([c * x for x in acc])
        tr += Xe[j]
        for x in Xe:
            if x:
                frob_X += x * x

        # --- ρ e_j, shared across every a ---
        re = apply_rho(e)
        for x in re:
            if x:
                frob_rho += x * x

        # --- new route: [ρ,σ_a] e_j = ρ(σ_a e_j) − σ_a(ρ e_j) ---
        for a in range(na):
            lhs = apply_rho(base.spmatvec(sig[a], e))
            rhs = base.spmatvec(sig[a], re)
            comm = [lhs[r] - rhs[r] for r in range(dim)]
            for x in comm:
                if x:
                    frob_comm[a] += x * x
            # tr(A·B) with A = [ρ,σ_a], B = σ_{a+1}, computed as Σ_j (A (B e_j))_j — so A must be
            # applied to σ_{a+1} e_j, NOT to e_j. Deliberately recomputed from ρ and σ rather than
            # reusing the `comm` vector above: `comm` is A e_j, which is the wrong argument, and
            # reusing it would silently compute a different quantity that still looks plausible.
            sae = base.spmatvec(sig[a + 1], e)
            lhs2 = apply_rho(base.spmatvec(sig[a], sae))
            rhs2 = base.spmatvec(sig[a], apply_rho(sae))
            rhs_C[a] += lhs2[j] - rhs2[j]

    frob_sig = []
    for a in range(ngen):
        s = mp.mpf(0)
        for i, entries in enumerate(sig[a]):
            for _col, v in entries:
                s += v * v
        frob_sig.append(s)

    return {
        "dim": dim, "tr": mp.re(tr), "frob_X": frob_X, "frob_rho": frob_rho,
        "frob_comm": frob_comm, "frob_sig": frob_sig, "rhs_C": rhs_C, "c": c,
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--A", type=int, default=3)
    ap.add_argument("--dps", type=int, default=65)
    ap.add_argument("--max-dim", type=int, default=200,
                    help="the new route costs ~5x the old per shape; cap for a first pass")
    args = ap.parse_args()
    global _WANT_DPS
    _WANT_DPS = args.dps
    mp.mp.dps = args.dps

    q = base.Q0
    A = args.A
    n = 3 * A
    Z, N = A // 2, A - A // 2
    gens = [int(t[2]) for t in atom_braid_word_3A(Z, N)]
    ngen = max(gens) + 1

    print(f"[comm] n={n}: the SIGN-KEEPING bound from trace_mul_commutator_eq (#6534, Lean-proved)")
    print(f"[comm]   tr_λ(ρΩ₂^P) = c·Σ_a tr_λ([ρ,σ_a]·σ_(a+1))          (C)")
    print(f"[comm]   |tr_λ(ρΩ₂^P)| ≤ c·Σ_a ‖[ρ,σ_a]‖_F·‖σ_(a+1)‖_F      (NEW)")
    print(f"[comm] vs the old link 1  |tr| ≤ √(dim·‖ρΩ₂^P‖_F²)   (mp.dps = {args.dps})\n")
    print("     b   λ                    dim    |tr|         OLD bound      NEW bound     "
          "NEW/OLD   NEW slack   (C) |Δ_rel|")

    rows, skipped = [], []
    worst_id = mp.mpf(0)
    for lam in base.partitions(n):
        lam = tuple(lam)
        _pg, d = base.block_structure(lam)
        if d > args.max_dim:
            skipped.append((lam, d))
            continue
        m = measure(lam, gens, q, ngen)
        dim, tr, cc = m["dim"], m["tr"], m["c"]
        if dim == 1:
            continue                                  # exact-zero endpoints
        old = mp.sqrt(dim * m["frob_X"])
        new = cc * sum(mp.sqrt(m["frob_comm"][a]) * mp.sqrt(m["frob_sig"][a + 1])
                       for a in range(ngen - 1))
        idc = cc * sum(m["rhs_C"])
        den = abs(tr) if abs(tr) > mp.mpf(10) ** -40 else mp.mpf(1)
        rel = abs(idc - tr) / den
        worst_id = max(worst_id, rel)
        b = sum(lam) - lam[0]
        rows.append((b, lam, dim, abs(tr), old, new, m))
        print(f"    {b:>2}   {str(lam):<20} {dim:>4}  {mp.nstr(abs(tr),7):>11}  "
              f"{mp.nstr(old,7):>12}  {mp.nstr(new,7):>12}  {mp.nstr(new/old,4):>8}  "
              f"{mp.nstr(new/den,5):>9}   {mp.nstr(rel,3):>9}")

    print()
    idok = worst_id < mp.mpf(10) ** -(args.dps // 2)
    print(f"  identity (C) reproduces the direct trace on every shape?  {'YES ✓' if idok else 'NO ✗'}"
          f"  (worst |Δ_rel| = {mp.nstr(worst_id,3)})")
    if not idok:
        print("  ⇒ (C) is a THEOREM (trace_mul_commutator_eq), so a mismatch is an ARITHMETIC")
        print("    defect in this probe, not a refutation. Stopping rather than reporting bounds.")
        return

    holds = all(t <= nb * (1 + mp.mpf(10) ** -40) for _b, _l, _d, t, _o, nb, _m in rows)
    print(f"  (NEW) bounds |tr| on every shape?  {'YES ✓' if holds else 'NO ✗'}")

    ratios = [nb / o for _b, _l, _d, _t, o, nb, _m in rows]
    slacks = [nb / t for _b, _l, _d, t, _o, nb, _m in rows if t > 0]
    print(f"\n  NEW/OLD ratio: {mp.nstr(min(ratios),4)} … {mp.nstr(max(ratios),4)}   "
          f"(<1 means the new bound is tighter)")
    print(f"  NEW slack over the true |tr|: {mp.nstr(min(slacks),4)}× … {mp.nstr(max(slacks),4)}×"
          f"   [old was 2.041× … 550.2×, #6754]")

    # SPLIT THE TWO GAINS. Without this a √dim win is indistinguishable from a cancellation win.
    print(f"\n  WHERE THE GAIN COMES FROM — √dim vs the commutator, separated:")
    for _b, lam, dim, _t, _o, _nb, m in rows[:1] + rows[len(rows) // 2:len(rows) // 2 + 1] + rows[-1:]:
        naive = m["c"] * sum(mp.sqrt(m["frob_rho"]) * mp.sqrt(m["frob_sig"][a + 1])
                             for a in range(ngen - 1))
        gain_comm = naive / (m["c"] * sum(mp.sqrt(m["frob_comm"][a]) * mp.sqrt(m["frob_sig"][a + 1])
                                          for a in range(ngen - 1)))
        print(f"    {str(lam):<20} dim {dim:>4}  √dim = {mp.nstr(mp.sqrt(dim),5):>7}   "
              f"commutator gain (‖ρ‖ vs ‖[ρ,σ]‖) = {mp.nstr(gain_comm,5)}×")

    # DECAY — a tighter bound that stops decaying is useless for this bean, and is called out.
    env = {}
    for b, _l, dim, _t, _o, nb, _m in rows:
        env[b] = max(env.get(b, mp.mpf(0)), nb / dim)
    bs = sorted(env)
    mono = all(env[bs[i + 1]] < env[bs[i]] for i in range(len(bs) - 1))
    print(f"\n  does (NEW)/dim still DECAY with b?  {'YES ✓' if mono else 'NO — see below'}")
    print("      " + " > ".join(f"b={b}:{mp.nstr(env[b],6)}" for b in bs))
    if not mono:
        print("  ⇒ TIGHTER BUT NOT DECAYING is a FAILURE for this bean, not progress: the whole")
        print("    point of the bound is that it falls with b. Report it as such.")
    if skipped:
        print(f"\n  SKIPPED {len(skipped)} shape(s) over --max-dim (NOT evidence — just not run): "
              + ", ".join(f"{l}({d})" for l, d in skipped[:6])
              + (" …" if len(skipped) > 6 else ""))


if __name__ == "__main__":
    main()
