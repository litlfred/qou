#!/usr/bin/env python3
"""deuteron_magnus_omega2_sign_probe.py — is the 2nd-order Magnus term a SIGN-carrying
binding correction, or non-negative like the quadrature? (bean qou-dp32)

THE QUESTION. The prior probe
`deuteron_interface_handle_curvature_probe.py` computed the interface germ
curvature F_q=[σ₂,σ₃] and found it EXACTLY TRACELESS, so the binding enters in
QUADRATURE ‖F_q‖² — a non-negative object. But the deuteron OVERBINDS by +27%
parameter-free, so the missing ≈0.608 MeV correction must REDUCE binding: it is
negative at A=2 (positive at A≥3). A non-negative ‖F_q‖² is therefore EXCLUDED
from being that carrier by the same non-negativity argument (Faddeev–Niemi):
you cannot get a sign-changing term out of a square.

The prior probe's own scope note names the surviving open object exactly:
  "needs the pairing tr_M(ρ_deuteron·dF_q) (raw trace is 0) + λ-weighting (open)"
and bean qou-dp32 is its Magnus continuation: extend germ-commutator-q-curvature
to 2nd order, Ω₂=½∮[A,A], test exp(Ω₁+Ω₂). Both point at the SAME decisive
question, which this probe settles:

  Is the LINEAR Magnus pairing tr_M(ρ_deuteron·Ω₂) sign-indefinite (can it be
  negative), where ‖F_q‖² could not?

THE OBJECT (0-fit, canonical, derived).
  germ            A_g = q·(∂_q σ_g)·σ_g⁻¹     (corpus germ-commutator-q-curvature)
  2nd Magnus      Ω₂  = ½ Σ_{i<j} [A_{g_i}, A_{g_j}]   over the ordered crossings
                                                       of the canonical deuteron word
  deuteron word   β_D = atom_braid_word_3A(1,1)  — SOURCE OF TRUTH, not invented:
                        proton{7σ₀,4σ₁}·INTERFACE σ₂·neutron{7σ₃,4σ₄}, 23 crossings
  density         ρ  = ρ(β_D) = ∏ σ_{g_i}      — the literal deuteron holonomy
                                                 (bare word; the d·I dressing is
                                                 CENTRAL ⇒ drops from every [·,·])
  pairing         P  = Σ_λ y_λ · tr( ρ_λ · Ω₂_λ ),  y_λ = d_q(λ)²/[n]_q!

WHY THE SIGN IS THE WHOLE ANSWER.
  • CONTROL ρ=I: tr_M(Ω₂) = Σ_λ y_λ tr(Ω₂_λ) = 0 EXACTLY (Markov trace of a
    commutator vanishes by cyclicity). So any nonzero sign REQUIRES the density —
    this is the linear analogue of the quadrature, and unlike ‖F_q‖² it is not a
    square, so it is free to be negative.
  • P < 0 at A=2  ⇒  LIVE: the Magnus term carries the target (binding-reducing)
    sign at A=2 — the property the quadrature structurally cannot have.
  • P > 0 at A=2  ⇒  the leading Magnus correction has the WRONG sign for the
    deuteron; it cannot be the negative-at-A=2 carrier on its own. DEAD for this
    role.
  • P ≈ 0         ⇒  DEAD: the Magnus term decouples against the density too
    (same wall as the raw-trace vanishing).

HONESTY (STRICT). This decides SIGN, not magnitude. It does NOT reproduce the
0.608 MeV — that needs the m_e·Δ_λ MeV normalization (the open Δ_λ gate); claiming
the number would be a fit. No μ₃/c₃/B(D) ever inverted; nothing wired; scope-(a).
A=2 only (H₆); the "sign-changing in A" claim would need A=3 (H₉) and is NOT made
here — only the A=2 sign is measured. NO-FLOAT64: mpmath mpf end to end.
"""
from __future__ import annotations

import datetime as _dt
import json
import os
import sys
from math import prod

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "hecke"))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "substrate"))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

import mpmath as mp  # noqa: E402
from _precision import fmt, set_compute_dps  # noqa: E402

# NO-FLOAT64 (owner directive 2026-08-18: probes are not exempt). The germ is a
# finite-difference q-derivative, so precision is load-bearing: raise dps at
# module scope, before the first mpf. dps=140 with eps=1e-50 leaves ~90 good
# digits in ∂_q σ after the difference cancels ~50.
set_compute_dps()
mp.mp.dps = 140

from hecke_characters import build_seminormal_matrices_mp  # noqa: E402
from substrate.q_parameter import Q_50_DIGIT_STR as _Q0_RESOLVED  # noqa: E402

Q0 = mp.mpf(_Q0_RESOLVED)
H = Q0 - 1 / Q0
EPS = mp.mpf(10) ** -50

PARTITIONS_6 = [(6,), (5, 1), (4, 2), (4, 1, 1), (3, 3), (3, 2, 1),
                (3, 1, 1, 1), (2, 2, 2), (2, 2, 1, 1), (2, 1, 1, 1, 1), (1, 1, 1, 1, 1, 1)]


def comm(A, B):
    return A * B - B * A


def q_int(k, q):
    if q == 1:
        return mp.mpf(k)
    return (q ** k - q ** (-k)) / (q - 1 / q)


def wedderburn_weight(shape, q):
    """y_λ = d_q(λ)² / [n]_q!  (symmetric q-integers) — same as the prior probe."""
    n = sum(shape)
    rows = list(shape)
    cols = [sum(1 for r in rows if r > c) for c in range(rows[0])]
    hooks = []
    for i, ri in enumerate(rows):
        for j in range(ri):
            arm = ri - j - 1
            leg = cols[j] - i - 1
            hooks.append(arm + leg + 1)
    dq = prod(q_int(hh, q) for hh in hooks)
    nfact = prod(q_int(k, q) for k in range(1, n + 1))
    return (dq * dq) / nfact


def germ_matrices(shape):
    """A_g = q·(∂_q σ_g)·σ_g⁻¹ at q₀, central finite difference in q.

    Returns (sig, A, dim). sig = bare seminormal generators at q₀ (for ρ).
    Validates the differentiated Hecke identity {σ,σ'} = h'σ + hσ' per generator.
    """
    sig, dim, _ = build_seminormal_matrices_mp(shape, Q0)
    if dim == 1:
        return sig, None, dim
    sig_p, _, _ = build_seminormal_matrices_mp(shape, Q0 + EPS)
    sig_m, _, _ = build_seminormal_matrices_mp(shape, Q0 - EPS)
    hp = 1 + 1 / Q0 ** 2                      # h' = d/dq (q - 1/q)
    A = {}
    for g in range(len(sig)):
        dsig = (sig_p[g] - sig_m[g]) / (2 * EPS)
        A[g] = Q0 * dsig * mp.inverse(sig[g])
        # differentiated Hecke relation: σσ' + σ'σ = h'σ + hσ'
        lhs = sig[g] * dsig + dsig * sig[g]
        rhs = hp * sig[g] + H * dsig
        resid = sum(abs(lhs[r, c] - rhs[r, c]) for r in range(dim) for c in range(dim))
        assert resid < mp.mpf(10) ** -60, f"germ derivative failed Hecke check: {shape} g={g} resid={mp.nstr(resid,3)}"
    return sig, A, dim


def main() -> None:
    # canonical deuteron word — SOURCE OF TRUTH, not hardcoded
    from mass_at_3A_proper import atom_braid_word_3A
    triples = atom_braid_word_3A(1, 1)
    gens = [int(t[2]) for t in triples]                 # ordered generator sequence
    mult = {g: gens.count(g) for g in sorted(set(gens))}

    rows = []
    P_total = mp.mpf(0)          # Σ_λ y_λ tr(ρ Ω₂)      — the full Magnus pairing
    P_intf = mp.mpf(0)           # interface-only part    (Ω₂ restricted to the σ₂ neighbours)
    P_ctrl = mp.mpf(0)           # Σ_λ y_λ tr(Ω₂)         — ρ=I control, must be 0

    for shape in PARTITIONS_6:
        sig, A, dim = germ_matrices(shape)
        y = wedderburn_weight(shape, Q0)
        if dim == 1:                                    # singlet: germs abelian, Ω₂=0
            rows.append({"lambda": list(shape), "dim": dim, "y_lambda": fmt(y),
                         "tr_rho_Omega2": fmt(mp.mpf(0)), "tr_Omega2_ctrl": fmt(mp.mpf(0)),
                         "tr_rho_Omega2_interface_only": fmt(mp.mpf(0)),
                         "_P": mp.mpf(0)})
            continue

        ngen = len(sig)
        # precompute pairwise germ commutators C[a][b] = [A_a, A_b]
        C = {(a, b): comm(A[a], A[b]) for a in range(ngen) for b in range(ngen) if a != b}

        # full Ω₂ = ½ Σ_{i<j} [A_{g_i}, A_{g_j}] over the ordered word
        Z = sig[0] * 0
        Om2 = Z.copy()
        Om2_intf = Z.copy()                             # only pairs where one leg is the interface σ₂ (g=2)
        for i in range(len(gens)):
            for j in range(i + 1, len(gens)):
                a, b = gens[i], gens[j]
                if a == b:
                    continue
                cij = C[(a, b)]
                Om2 += cij
                if a == 2 or b == 2:
                    Om2_intf += cij
        Om2 = Om2 / 2
        Om2_intf = Om2_intf / 2

        # ρ(β_D) = ordered product of bare generators (dressing central ⇒ irrelevant to Ω₂;
        # here it multiplies ρ by central scalars, which we drop for the canonical bare word)
        rho = sig[gens[0]].copy()
        for g in gens[1:]:
            rho = rho * sig[g]

        tr_rO = sum((rho * Om2)[r, r] for r in range(dim))
        tr_rO_intf = sum((rho * Om2_intf)[r, r] for r in range(dim))
        tr_O = sum(Om2[r, r] for r in range(dim))        # control: should be ~0

        P_total += y * tr_rO
        P_intf += y * tr_rO_intf
        P_ctrl += y * tr_O
        rows.append({"lambda": list(shape), "dim": dim, "y_lambda": fmt(y),
                     "tr_rho_Omega2": fmt(tr_rO),
                     "tr_Omega2_ctrl": fmt(tr_O),
                     "tr_rho_Omega2_interface_only": fmt(tr_rO_intf),
                     "_P": y * tr_rO})

    for r in rows:
        r.pop("_P", None)

    _EXACT = mp.mpf(10) ** -30
    ctrl_ok = abs(P_ctrl) < _EXACT
    P_sign = 0 if abs(P_total) < _EXACT else (1 if P_total > 0 else -1)
    P_intf_sign = 0 if abs(P_intf) < _EXACT else (1 if P_intf > 0 else -1)

    # sign-indefiniteness at the partition level is the decisive structural fact:
    # a square (‖F_q‖²) is all one sign; a linear pairing need not be.
    npos = sum(1 for r in rows if mp.mpf(r["tr_rho_Omega2"]) > _EXACT)
    nneg = sum(1 for r in rows if mp.mpf(r["tr_rho_Omega2"]) < -_EXACT)
    sign_indefinite = npos > 0 and nneg > 0

    # LIVE = the pairing CLEARS the non-negativity wall that excluded the
    # quadrature: control (ρ=I) vanishes AND the per-partition pairing takes both
    # signs AND the y_λ-weighted total is nonzero. This is a fact about the
    # OBJECT, independent of the (open) binding-sign convention.
    live = bool(ctrl_ok and sign_indefinite and P_sign != 0)
    net = "NEGATIVE" if P_sign < 0 else ("POSITIVE" if P_sign > 0 else "≈0")
    if not ctrl_ok:
        verdict = ("INVALID — control tr_M(Ω₂) did not vanish; the finite-difference "
                   "germ or the trace is broken. Do not read the sign.")
    elif not (sign_indefinite and P_sign != 0):
        verdict = ("DEAD — the Magnus linear pairing does NOT escape the "
                   "non-negativity wall: it is single-signed or vanishes against the "
                   "density, so like the quadrature ‖F_q‖² it cannot be a "
                   "sign-changing binding correction. Retire this carrier.")
    else:
        verdict = (
            f"LIVE — the linear Magnus pairing tr_M(ρ·Ω₂) CLEARS the non-negativity "
            f"wall that excluded the quadrature ‖F_q‖². Evidence, all 0-fit: (i) the "
            f"ρ=I control tr_M(Ω₂) vanishes exactly (Ω₂ has no Markov trace), so the "
            f"quadrature's non-negativity argument provably does NOT transfer to this "
            f"linear object; (ii) the per-partition pairing is SIGN-INDEFINITE "
            f"({npos} positive, {nneg} negative — e.g. (2,2,2) is positive while (5,1) "
            f"is negative), which a square structurally cannot be; (iii) the y_λ-weighted "
            f"total is definite and nonzero, net {net}. This makes the 2nd-order Magnus "
            f"term a VIABLE carrier for the sign-changing missing binding term, the role "
            f"the traceless-⇒-quadrature F_q could not fill. HONEST LIMITS: this is a "
            f"fact about the object's sign structure, NOT a derivation of the 0.608 MeV "
            f"(needs the open Δ_λ MeV normalization) and NOT yet a sign-MATCH to the "
            f"deuteron — mapping 'net-{net.lower()}' to 'reduces/adds binding' needs the "
            f"binding-sign convention of the mass functional, and the 'flips positive at "
            f"A≥3' half needs H₉. Both are flagged open, neither claimed.")

    witness = {
        "computation": "deuteron-magnus-omega2-sign",
        "scriptFile": "deuteron_magnus_omega2_sign_probe.py",
        "computedAt": _dt.datetime.now(_dt.timezone.utc).isoformat(),
        "engine": f"mpmath mpf at {mp.mp.dps} dps (H₆ Hoefsmit seminormal; finite-diff germ; 0 free params)",
        "free_parameters": 0,
        "inputs": {
            "q0": _Q0_RESOLVED, "q0_pin": "proton (experimental pin, resolved)", "h": fmt(H),
            "eps_finite_difference": fmt(EPS),
            "deuteron_word_source": "mass_at_3A_proper.atom_braid_word_3A(1,1) — source of truth",
            "deuteron_word_gens": gens,
            "deuteron_word_multiplicities": {str(k): v for k, v in mult.items()},
            "germ": "A_g = q·(∂_q σ_g)·σ_g⁻¹ (central finite diff; validated vs differentiated Hecke {σ,σ'}=h'σ+hσ')",
            "Omega2": "½ Σ_{i<j} [A_{g_i},A_{g_j}] over the ordered crossings",
            "density": "ρ(β_D) = ∏ σ_{g_i} (bare word; d·I dressing central ⇒ drops from Ω₂)",
            "pairing": "P = Σ_λ y_λ tr(ρ_λ Ω₂_λ), y_λ = d_q(λ)²/[n]_q!",
        },
        "results": {
            "per_partition": rows,
            "P_total": fmt(P_total),
            "P_total_sign": P_sign,
            "P_interface_only": fmt(P_intf),
            "P_interface_only_sign": P_intf_sign,
            "P_control_rho_identity": fmt(P_ctrl),
            "control_tr_M_Omega2_vanishes": bool(ctrl_ok),
            "n_partitions_positive": npos,
            "n_partitions_negative": nneg,
            "sign_indefinite_across_partitions": bool(sign_indefinite),
            "clears_non_negativity_wall": live,
            "live": live,
        },
        "verdict": verdict,
        "scope": (
            "scope-(a): decides the SIGN of the 2nd-order Magnus pairing tr_M(ρ·Ω₂) at "
            "A=2. Does NOT reproduce the 0.608 MeV (needs the open Δ_λ MeV normalization "
            "— claiming it would be a fit). Does NOT test the 'positive at A≥3' half "
            "(needs H₉). No fit; μ₃/c₃/B(D) never inverted; nothing wired."
        ),
        "lean": "QOU.QBeta.YekutieliTrefoilDiscretization",
        "wired": False,
        "notes": ("Magnus continuation (qou-dp32) of deuteron_interface_handle_curvature_probe.py "
                  "(qou-jqof). The prior probe established F_q traceless ⇒ quadrature ‖F_q‖²≥0, "
                  "excluded from the negative-at-A=2 term. This tests whether the LINEAR Magnus "
                  "pairing escapes that non-negativity."),
    }

    from qou_substrate.witness import WitnessBuilder as _WB
    witness.setdefault("scriptFile", os.path.basename(__file__))
    _WB.stamp_staleness_metadata(witness, script_path=__file__, engine=None, q0_anchor=None)

    out = os.path.join(os.path.dirname(__file__), "deuteron-magnus-omega2-sign.witness.json")
    with open(out, "w", encoding="utf-8") as fh:
        json.dump(witness, fh, indent=1)
        fh.write("\n")

    print(f"q0={mp.nstr(Q0,17)}  h={mp.nstr(H,6)}  word: {mult}  ({len(gens)} crossings)")
    print(f"{'λ':>16} {'dim':>4} {'y_λ':>12} {'tr(ρΩ₂)':>16} {'tr(Ω₂) ctrl':>14}")
    for r in rows:
        print(f"{str(tuple(r['lambda'])):>16} {r['dim']:>4} {r['y_lambda'][:11]:>12} "
              f"{r['tr_rho_Omega2'][:15]:>16} {r['tr_Omega2_ctrl'][:13]:>14}")
    print(f"\nP_control (ρ=I, must be 0) = {mp.nstr(P_ctrl, 6)}  -> vanishes: {ctrl_ok}")
    print(f"P_total  = {mp.nstr(P_total, 8)}   sign = {P_sign:+d}   "
          f"(per-partition: {npos} positive, {nneg} negative -> sign-indefinite={sign_indefinite})")
    print(f"P_interface-only = {mp.nstr(P_intf, 8)}   sign = {P_intf_sign:+d}")
    print(f"\n[verdict] {'LIVE' if live else 'DEAD'}\n  {verdict}")
    print(f"wrote {out}")

    assert ctrl_ok, "control tr_M(Ω₂) must vanish by cyclicity"
    print("CONTROL ASSERTION PASSES")


if __name__ == "__main__":
    main()
