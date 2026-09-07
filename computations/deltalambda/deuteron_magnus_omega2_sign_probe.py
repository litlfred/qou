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
# Option A (bean qou-q2q7): the production Wenzl/Markov weight, carried
# alongside the Plancherel measure this probe aggregates with. See
# docs/audits/2026-09-07-magnus-omega2-weight-family-analysis.md.
from y_lambda_wenzl_bridge import y_lambda_wenzl_bridge_numeric  # noqa: E402

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
    """**quantum Plancherel** measure `w_planch(λ) = d_q(λ)² / [n]_q!`
    (symmetric q-integers).

    NOT the Wenzl y_λ (bean qou-za3q). AGENTS.md is explicit that the three
    partition-weight families y_λ / w_λ / w̃_λ are DISTINCT at q ≠ 1 and must
    never be conflated; this docstring used to call this one `y_λ`, which is
    the conflation it forbids, and which makes a corpus scan keying on the
    name `y_lambda` unable to tell this apart from the production weight.

    The two are not a rescaling of each other. At H₃, measured:

        λ            Wenzl y_λ (production)   d_q²/[n]_q! (here)
        (3,)             0.50540423              0.16338323
        (2,1)            0.24729789              0.66067377
        (1,1,1)          0                       0.16338323

    and at higher n the divergence is structural: the Wenzl row cap (level
    r = 2, bean qou-fq0f) annihilates every shape with ≥3 rows, which is where
    the Plancherel measure puts most of its mass — 70 of the 77 partitions of
    12 carry Wenzl weight exactly zero.

    The name is fixed here; whether the Plancherel measure is the RIGHT pairing
    for a Magnus Ω₂ sign question is a separate matter and is not settled by
    this rename. What IS settled (see `sign_robust_to_weight_family` in the
    witness) is that the probe's headline conclusion — the sign of P_total —
    does not depend on the choice.
    """
    n = sum(shape)
    rows = list(shape)
    cols = [sum(1 for r in rows if r > c) for c in range(rows[0])]
    hooks = []
    for i, ri in enumerate(rows):
        for j in range(ri):
            arm = ri - j - 1
            leg = cols[j] - i - 1
            hooks.append(arm + leg + 1)
    # HOOK-LENGTH FORMULA: d_q(λ) = [n]_q! / ∏_x [h(x)]_q.
    #
    # This previously read `dq = prod(q_int(hh, q) for hh in hooks)` — the
    # DENOMINATOR of that formula, not d_q — and then returned dq²/[n]_q!.
    # The result was the EXACT RECIPROCAL of the documented weight:
    # computed H²/[n]_q! where d_q²/[n]_q! = [n]_q!/H². Verified against the
    # committed witnesses to a relative 1e-40, and probe × correct = 1.0
    # identically on every partition checked.
    hook_prod = prod(q_int(hh, q) for hh in hooks)
    nfact = prod(q_int(k, q) for k in range(1, n + 1))
    dq = nfact / hook_prod
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

    # Ω₂ PAIR TABLES — depend on the word only, so built once rather than per
    # partition. Ω₂ = ½ Σ_{i<j, g_i≠g_j} [A_{g_i}, A_{g_j}]; folding the pair
    # multiplicities and using antisymmetry [A_a,A_b] = −[A_b,A_a] builds each
    # needed commutator ONCE, where the previous code built every a≠b pair in
    # range(len(sig)) for every shape — including pairs the word never uses.
    # `_net_intf` is the same fold restricted to pairs with a leg on the
    # interface generator σ₂. Verified exact on the triton probe: identical to
    # 1e-69 at 50 dps, 3.35x faster.
    _net: dict[tuple[int, int], int] = {}
    _net_intf: dict[tuple[int, int], int] = {}
    for _i in range(len(gens)):
        for _j in range(_i + 1, len(gens)):
            _a, _b = gens[_i], gens[_j]
            if _a == _b:
                continue
            _key = (_a, _b) if _a < _b else (_b, _a)
            _d = 1 if _a < _b else -1
            _net[_key] = _net.get(_key, 0) + _d
            if _a == 2 or _b == 2:
                _net_intf[_key] = _net_intf.get(_key, 0) + _d
    _net = {k: v for k, v in _net.items() if v}
    _net_intf = {k: v for k, v in _net_intf.items() if v}

    rows = []
    P_total = mp.mpf(0)          # Σ_λ w_planch tr(ρ Ω₂)  — the Plancherel arm
    P_wenzl = mp.mpf(0)          # Σ_λ y_λ^Wenzl tr(ρ Ω₂) — the HEADLINE (Markov)
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

        # Each needed commutator built exactly once, weighted by its net
        # multiplicity from the pair tables above.
        Z = sig[0] * 0
        Om2 = Z.copy()
        Om2_intf = Z.copy()          # pairs with a leg on the interface σ₂
        for (a, b), n in _net.items():
            cij = comm(A[a], A[b])
            Om2 += n * cij
            m = _net_intf.get((a, b))
            if m:
                Om2_intf += m * cij
        Om2 = Om2 / 2
        Om2_intf = Om2_intf / 2

        # ρ(β_D) = ordered product of bare generators (dressing central ⇒ irrelevant to Ω₂;
        # here it multiplies ρ by central scalars, which we drop for the canonical bare word)
        rho = sig[gens[0]].copy()
        for g in gens[1:]:
            rho = rho * sig[g]

        # tr(ρ·M) without forming ρ·M: Σ_{r,s} ρ[r,s]·M[s,r]. O(d²), not O(d³).
        tr_rO = sum(rho[r, s] * Om2[s, r] for r in range(dim) for s in range(dim))
        tr_rO_intf = sum(rho[r, s] * Om2_intf[s, r]
                         for r in range(dim) for s in range(dim))
        tr_O = sum(Om2[r, r] for r in range(dim))        # control: should be ~0

        P_total += y * tr_rO
        P_wenzl += y_lambda_wenzl_bridge_numeric(shape, Q0, dps=mp.mp.dps) * tr_rO
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
            # Declares WHICH partition-weight family the `y_lambda` column
            # above actually holds (bean qou-za3q). The column name is left
            # alone deliberately — several sibling probes read `r["y_lambda"]`
            # from this witness, so renaming the field would break them; an
            # explicit declaration removes the ambiguity without that.
            "weight_family": "quantum_plancherel_dq2_over_n_factorial",
            "weight_family_note": (
                "NOT the Wenzl y_lambda used by the production Markov trace. "
                "AGENTS.md forbids conflating y_lambda / w_lambda / w~_lambda, "
                "which are distinct at q != 1. Re-weighting this witness's own "
                "per-partition tr(rho.Omega2) with the Wenzl bridge weight "
                "leaves the sign of P_total unchanged — measured in "
                "magnus_omega2_weight_family_robustness_probe.py."
            ),
            # HEADLINE (Option A, bean qou-q2q7): the production Wenzl/Markov
            # weight. `P_total` above keeps its existing name and Plancherel
            # meaning deliberately — `he4_magnus_mpfr_probe.py` and the sparse
            # probe both do a NUMERICAL dense-vs-sparse check against the
            # committed `P_total`, so silently re-meaning it would break a real
            # cross-check. Declaring which arm is authoritative is the same fix
            # this arc used for the `y_lambda` column and for `scriptFile`.
            "headline_pairing": "P_total_wenzl",
            "P_total_wenzl": fmt(P_wenzl),
            "P_total_wenzl_sign": (0 if abs(P_wenzl) < _EXACT
                                   else (1 if P_wenzl > 0 else -1)),
            "P_total_wenzl_note": (
                "Sum over lambda of y_lambda^Wenzl * tr(rho.Omega2), the "
                "production Markov weight (row cap at level r=2 zeroes every "
                "shape with >=3 rows). tr(1)=1 at every n, so values ARE "
                "comparable across A -- which the Plancherel arm is not "
                "(tr(1) = 11.1 / 184.2 / 6751.5 at n = 6 / 9 / 12). See "
                "docs/audits/2026-09-07-magnus-omega2-weight-family-analysis.md."
            ),
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
