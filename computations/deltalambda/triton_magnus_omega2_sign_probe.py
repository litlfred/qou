#!/usr/bin/env python3
"""triton_magnus_omega2_sign_probe.py — does the 2nd-order Magnus pairing FLIP SIGN
from A=2 to A=3?  (Thread-A takeover follow-on; extends deuteron_magnus_omega2_sign_probe.py)

THE QUESTION. The A=2 probe (deuteron_magnus_omega2_sign_probe.py, bean qou-dp32,
merged audit docs/audits/2026-08-29-deuteron-magnus-omega2-clears-non-negativity-wall.md)
established that the linear Magnus pairing P = Σ_λ y_λ tr_M(ρ·Ω₂) at A=2 is:
control tr_M(Ω₂)=0 exactly, per-partition SIGN-INDEFINITE (2 pos / 7 neg), y-weighted
total NET NEGATIVE (P = -12882.86). That cleared the non-negativity wall the quadrature
‖F_q‖² could not — a VIABLE sign-carrier for the deuteron's negative-at-A=2 missing term.

That doc explicitly left ONE half untested:

  "the 'flips positive at A≥3' half needs H₉ ... only the A=2 sign is measured."

This probe supplies exactly that measurement — the SAME construction on the triton
(A=3, ³H = 1p2n, 9 strands, H₉) — and asks:

  Does the y-weighted Magnus pairing P(A=3) have the OPPOSITE sign to P(A=2)<0,
  i.e. is P(A=3) > 0?  A sign FLIP is the signature the merged doc names for a
  binding correction that reduces binding at A=2 but adds it at A≥3.

THE OBJECT (identical construction to A=2, 0-fit, canonical, derived).
  germ            A_g = q·(∂_q σ_g)·σ_g⁻¹     (corpus germ-commutator-q-curvature)
  2nd Magnus      Ω₂  = ½ Σ_{i<j} [A_{g_i}, A_{g_j}]   over the ordered crossings
  triton word     β_T = atom_braid_word_3A(1,2)  — SOURCE OF TRUTH (35 crossings, σ₀..σ₇)
  density         ρ   = ρ(β_T) = ∏ σ_{g_i}      (bare word; central dressing drops from Ω₂)
  pairing         P   = Σ_λ y_λ tr(ρ_λ Ω₂_λ),  y_λ = d_q(λ)²/[n]_q!,  λ ⊢ 9

WHAT A RESULT MEANS.
  • control tr_M(Ω₂) = 0 (must hold, as at A=2 — Markov trace of a commutator).
  • P(A=3) > 0  ⇒  SIGN FLIP relative to A=2's net-negative: the Magnus carrier
    reverses between A=2 and A=3, matching the "reduces binding at A=2, adds at A≥3"
    signature the merged doc names. This is the datum that was missing.
  • P(A=3) < 0  ⇒  NO flip: same sign as A=2. The simple "negative→positive" reading
    of the Magnus carrier does NOT hold; the A-dependence is more complex (or the
    sign convention is not monotone in A).
  • P(A=3) ≈ 0  ⇒  the pairing decouples at A=3.

HONESTY (STRICT). This decides the A=3 SIGN and its relation to the A=2 sign — a
dimensionless structural datum, scope-(a). It does NOT reproduce any MeV (the Δ_λ
magnitude gate is open; a number would be a fit). It does NOT assert a physical
binding-sign convention (that is the qou-v7ro / PR #6077 bridge — NOT re-derived
here, cited). No fit; nothing inverted; nothing wired. NO-FLOAT64: mpmath mpf end
to end, dps=140, eps=1e-50, germ validated against the differentiated Hecke relation.
Cites, does not rebuild: qou-dp32 / the A=2 probe (the carrier + method), the merged
Magnus-wall audit (the untested A≥3 half), qou-v7ro / #6077 (the sign convention).
"""
from __future__ import annotations

import datetime as _dt
import hashlib
import pathlib
import json
import os
import sys
from math import prod

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "hecke"))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "substrate"))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

import mpmath as mp  # noqa: E402
from _precision import fmt, set_compute_dps  # noqa: E402

# NO-FLOAT64 (owner directive 2026-08-18: probes are not exempt). Same precision
# posture as the A=2 probe: the germ is a finite-difference q-derivative, so raise
# dps at module scope before the first mpf. dps=140, eps=1e-50 leaves ~90 good
# digits after the difference cancels ~50.
set_compute_dps()
mp.mp.dps = 140

from hecke_characters import build_seminormal_matrices_mp  # noqa: E402
from substrate.q_parameter import Q_50_DIGIT_STR as _Q0_RESOLVED  # noqa: E402

Q0 = mp.mpf(_Q0_RESOLVED)
H = Q0 - 1 / Q0
EPS = mp.mpf(10) ** -50


def partitions(n, maxpart=None):
    """All integer partitions of n as decreasing-part tuples."""
    if maxpart is None:
        maxpart = n
    if n == 0:
        yield ()
        return
    for k in range(min(n, maxpart), 0, -1):
        for rest in partitions(n - k, k):
            yield (k,) + rest


PARTITIONS_9 = list(partitions(9))   # 30 partitions of 9 -> H_9


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
    """A_g = q·(∂_q σ_g)·σ_g⁻¹ at q₀, central finite difference — same as A=2 probe.
    Validates the differentiated Hecke identity {σ,σ'} = h'σ + hσ' per generator."""
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
        lhs = sig[g] * dsig + dsig * sig[g]
        rhs = hp * sig[g] + H * dsig
        resid = sum(abs(lhs[r, c] - rhs[r, c]) for r in range(dim) for c in range(dim))
        assert resid < mp.mpf(10) ** -60, f"germ derivative failed Hecke check: {shape} g={g} resid={mp.nstr(resid,3)}"
    return sig, A, dim


def main() -> None:
    from mass_at_3A_proper import atom_braid_word_3A
    triples = atom_braid_word_3A(1, 2)                  # triton ³H = 1p2n, A=3
    gens = [int(t[2]) for t in triples]
    mult = {g: gens.count(g) for g in sorted(set(gens))}

    # A=2 baseline (committed witness), for the sign-flip comparison
    a2_path = os.path.join(os.path.dirname(__file__), "deuteron-magnus-omega2-sign.witness.json")
    a2_sign = None
    try:
        with open(a2_path) as fh:
            a2 = json.load(fh)["results"]
        a2_sign = int(a2["P_total_sign"])
    except Exception:
        pass

    rows = []
    P_total = mp.mpf(0)
    P_ctrl = mp.mpf(0)

    # RESUME CACHE (bean qou-omr7). The H_9 sweep is ~90 min single-threaded and
    # this probe had NO checkpoint, so every container restart cost the entire
    # run — three consecutive attempts died before 10 of 30 partitions. The
    # sibling `he4_binding_k_stage2_probe` already carries this pattern and it
    # demonstrably works: a restart there resumed 154/154 + 74/77 for free.
    #
    # STAMPED, not just keyed on the partition. A cache entry records the q it
    # was computed at, and a mismatch DISCARDS rather than silently serving a
    # stale block. That is the qou-5ovu lesson: a gate that answers "is this
    # entry PRESENT?" when the question is "is this entry CURRENT?" is how two
    # witnesses sat at a superseded convention for three weeks.
    _stamp = hashlib.sha256(f"{Q0}|9".encode()).hexdigest()[:12]
    _prog = pathlib.Path(os.path.dirname(__file__)) / ".triton_magnus_omega2_progress.jsonl"
    _done: dict[tuple, dict] = {}
    _dropped = 0
    if _prog.exists():
        for _line in _prog.read_text().splitlines():
            if not _line.strip():
                continue
            try:                       # a torn final line from a hard kill is
                _r = json.loads(_line)  # skipped, never fatal
            except Exception:
                continue
            if _r.get("st") != _stamp:
                _dropped += 1
                continue
            _done[tuple(_r["row"]["lambda"])] = _r["row"]
        if _dropped:
            print(f"  dropped {_dropped} cached partitions computed at a "
                  f"different q", flush=True)
        if _done:
            print(f"  resumed {len(_done)}/{len(PARTITIONS_9)} partitions from "
                  f"{_prog.name}", flush=True)

    def _checkpoint(row):
        with open(_prog, "a") as _pf:
            _pf.write(json.dumps({"st": _stamp, "row": row}) + "\n")

    for shape in PARTITIONS_9:
        _cached = _done.get(tuple(shape))
        if _cached is not None:
            rows.append(_cached)
            P_total += mp.mpf(_cached["y_lambda"]) * mp.mpf(_cached["tr_rho_Omega2"])
            P_ctrl += mp.mpf(_cached["y_lambda"]) * mp.mpf(_cached["tr_Omega2_ctrl"])
            continue
        sig, A, dim = germ_matrices(shape)
        y = wedderburn_weight(shape, Q0)
        if dim == 1:                                    # singlet: germs abelian, Ω₂=0
            _row = {"lambda": list(shape), "dim": dim, "y_lambda": fmt(y),
                    "tr_rho_Omega2": fmt(mp.mpf(0)), "tr_Omega2_ctrl": fmt(mp.mpf(0))}
            rows.append(_row)
            _checkpoint(_row)
            continue

        ngen = len(sig)
        C = {(a, b): comm(A[a], A[b]) for a in range(ngen) for b in range(ngen) if a != b}

        Z = sig[0] * 0
        Om2 = Z.copy()
        for i in range(len(gens)):
            for j in range(i + 1, len(gens)):
                a, b = gens[i], gens[j]
                if a == b:
                    continue
                Om2 += C[(a, b)]
        Om2 = Om2 / 2

        rho = sig[gens[0]].copy()
        for g in gens[1:]:
            rho = rho * sig[g]

        tr_rO = sum((rho * Om2)[r, r] for r in range(dim))
        tr_O = sum(Om2[r, r] for r in range(dim))       # control ~0

        P_total += y * tr_rO
        P_ctrl += y * tr_O
        _row = {"lambda": list(shape), "dim": dim, "y_lambda": fmt(y),
                "tr_rho_Omega2": fmt(tr_rO), "tr_Omega2_ctrl": fmt(tr_O)}
        rows.append(_row)
        _checkpoint(_row)
        print(f"  {str(tuple(shape)):>22} dim={dim:>3}  tr(rho Om2)={mp.nstr(tr_rO,6):>14}  "
              f"[running P={mp.nstr(P_total,6)}]", flush=True)

    _prog.unlink(missing_ok=True)   # completed cleanly -> next run starts fresh

    _EXACT = mp.mpf(10) ** -30
    ctrl_ok = abs(P_ctrl) < _EXACT
    P_sign = 0 if abs(P_total) < _EXACT else (1 if P_total > 0 else -1)
    npos = sum(1 for r in rows if mp.mpf(r["tr_rho_Omega2"]) > _EXACT)
    nneg = sum(1 for r in rows if mp.mpf(r["tr_rho_Omega2"]) < -_EXACT)
    sign_indefinite = npos > 0 and nneg > 0

    flip = None
    if a2_sign is not None and P_sign != 0 and a2_sign != 0:
        flip = (P_sign != a2_sign)

    if not ctrl_ok:
        verdict = ("INVALID — control tr_M(Ω₂) did not vanish at A=3; germ or trace broken. "
                   "Do not read the sign.")
    elif P_sign == 0:
        verdict = ("DECOUPLED — the Magnus pairing vanishes against the triton density; "
                   "no A=3 sign to compare.")
    elif flip is True:
        verdict = (
            f"SIGN FLIP CONFIRMED — P(A=3) is {'POSITIVE' if P_sign>0 else 'NEGATIVE'} while "
            f"P(A=2) was {'NEGATIVE' if a2_sign<0 else 'POSITIVE'}. The y-weighted 2nd-order "
            f"Magnus pairing REVERSES sign between the deuteron (A=2) and the triton (A=3), "
            f"the signature the merged Magnus-wall audit named for a correction that reduces "
            f"binding at A=2 and adds it at A≥3. Control tr_M(Ω₂)=0 holds; per-partition "
            f"sign-indefinite ({npos}+/{nneg}-). HONEST LIMITS: dimensionless SIGN datum only "
            f"(scope-a); NOT a MeV (open Δ_λ gate), NOT a physical binding-sign assertion "
            f"(that is qou-v7ro/#6077, cited not re-derived). The flip is a fact about the "
            f"object across A; mapping it to 'binding' still needs the sign convention.")
    elif flip is False:
        verdict = (
            f"NO FLIP — P(A=3) has the SAME sign as P(A=2) (both "
            f"{'negative' if P_sign<0 else 'positive'}). The simple 'negative at A=2 → "
            f"positive at A≥3' reading of the Magnus carrier does NOT hold at the triton: "
            f"the A-dependence of the pairing sign is not a single flip at A=3. This does not "
            f"retire the carrier (the A=2 sign stands, control=0, sign-indefinite {npos}+/{nneg}-), "
            f"but it constrains any story that assumed monotone sign reversal. scope-(a).")
    else:
        verdict = (f"A=3 sign measured (P {'>' if P_sign>0 else '<'} 0) but the A=2 baseline "
                   f"witness was unreadable, so no flip comparison. scope-(a).")

    witness = {
        "computation": "triton-magnus-omega2-sign",
        "scriptFile": "triton_magnus_omega2_sign_probe.py",
        "computedAt": _dt.datetime.now(_dt.timezone.utc).isoformat(),
        "engine": f"mpmath mpf at {mp.mp.dps} dps (H₉ Hoefsmit seminormal; finite-diff germ; 0 free params)",
        "free_parameters": 0,
        "inputs": {
            "q0": _Q0_RESOLVED, "q0_pin": "proton (experimental pin, resolved)", "h": fmt(H),
            "eps_finite_difference": fmt(EPS),
            "triton_word_source": "mass_at_3A_proper.atom_braid_word_3A(1,2) — source of truth",
            "triton_word_gens": gens,
            "triton_word_multiplicities": {str(k): v for k, v in mult.items()},
            "n_strands": 9, "n_crossings": len(gens),
            "germ": "A_g = q·(∂_q σ_g)·σ_g⁻¹ (central finite diff; validated vs differentiated Hecke)",
            "Omega2": "½ Σ_{i<j} [A_{g_i},A_{g_j}] over the ordered crossings",
            "density": "ρ(β_T) = ∏ σ_{g_i} (bare word; central dressing drops from Ω₂)",
            "pairing": "P = Σ_λ y_λ tr(ρ_λ Ω₂_λ), y_λ = d_q(λ)²/[n]_q!, λ ⊢ 9",
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
            "P_total": fmt(P_total),
            "P_total_sign": P_sign,
            "P_control_rho_identity": fmt(P_ctrl),
            "control_tr_M_Omega2_vanishes": bool(ctrl_ok),
            "n_partitions_positive": npos,
            "n_partitions_negative": nneg,
            "sign_indefinite_across_partitions": bool(sign_indefinite),
            "A2_P_total_sign": a2_sign,
            "sign_flip_vs_A2": flip,
        },
        "verdict": verdict,
        "scope": (
            "scope-(a): decides the A=3 SIGN of tr_M(ρ·Ω₂) and its relation to the A=2 sign. "
            "Dimensionless structural datum. Does NOT reproduce any MeV (open Δ_λ gate — a "
            "number would be a fit). Does NOT assert a physical binding-sign convention "
            "(qou-v7ro / PR #6077, cited not re-derived). No fit; nothing inverted; nothing wired."
        ),
        "wired": False,
        "notes": ("Thread-A takeover follow-on: the A≥3 half the merged deuteron-magnus-omega2 "
                  "audit (2026-08-29) left untested. Same construction as "
                  "deuteron_magnus_omega2_sign_probe.py (qou-dp32) on the triton (H₉). Cites "
                  "qou-v7ro/#6077 for the sign convention; does not re-derive it."),
    }

    from qou_substrate.witness import WitnessBuilder as _WB
    witness.setdefault("scriptFile", os.path.basename(__file__))
    _WB.stamp_staleness_metadata(witness, script_path=__file__, engine=None, q0_anchor=None)

    out = os.path.join(os.path.dirname(__file__), "triton-magnus-omega2-sign.witness.json")
    with open(out, "w", encoding="utf-8") as fh:
        json.dump(witness, fh, indent=1)
        fh.write("\n")

    print(f"\nq0={mp.nstr(Q0,17)}  triton word: {mult}  ({len(gens)} crossings, 9 strands, H_9)")
    print(f"P_control (ρ=I, must be 0) = {mp.nstr(P_ctrl, 6)}  -> vanishes: {ctrl_ok}")
    print(f"P_total(A=3) = {mp.nstr(P_total, 8)}   sign = {P_sign:+d}   "
          f"(per-partition {npos}+ / {nneg}-)")
    print(f"A=2 sign was {a2_sign:+d}   ->   sign_flip = {flip}")
    print(f"\n[verdict] {verdict}")
    print(f"wrote {out}")
    assert ctrl_ok, "control tr_M(Ω₂) must vanish by cyclicity"
    print("CONTROL ASSERTION PASSES")


if __name__ == "__main__":
    main()
