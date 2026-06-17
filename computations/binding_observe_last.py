#!/usr/bin/env python3
# polynomial_q_not_applicable: numerical mpmath consumer (observe-last binding)
"""binding_observe_last.py — observe-EARLY vs observe-LAST binding; is the
Jensen gap the q₀^(10A−5) residual?

Tests the §6b reframe (docs/audits/2026-06-17-singlet-channel-bsym-exploration.md):
production collapses the per-λ q-Reeb phase θ_λ into the scalar tr_M at step 5
(observe-EARLY), BEFORE the archimedean τ at step 9.  Because Kashaev makes τ
exponential, log(Σ_λ y_λ χ_λ) ≠ Σ_λ y_λ log(…) — a Jensen gap that grows with
A.  Claim: that gap is the documented residual Δ_λ(K)=B_AME/B_pred ≈ q₀^(10A−5)
(residual audit 2026-06-09).

  observe-EARLY (production, step-5 collapse):
     tr_X = Σ_λ y_λ χ_λ^X ;  B_pred = E₀·(tr_free − tr_atom)   [residual-audit baseline]
  observe-LAST (step-9 collapse; per-block q-Reeb phase first, sum last):
     θ_λ^X = arccos(χ_λ^X/d_λ)  (|·|≤1, rotation)  or  arccosh(|χ_λ^X/d_λ|) (growth)
     B_late = E₀·Σ_λ y_λ·(θ_λ^free − θ_λ^atom)      [additive over blocks, §6b]

Decisive metrics per atom:
  e_pred = log_{q0}(B_AME/B_pred)   (known: ≈ 10A−5 — preflight on the residual law)
  e_late = log_{q0}(B_AME/B_late)   (≈ 0  ⇒ observe-last RECOVERS AME ⇒ 10A−5 derived)
  g_late = log_{q0}(B_late/B_pred)  (≈ 10A−5 ⇒ the gap IS the residual)

NO FLOAT (owner ruling 2026-06-09): all mpmath at the 50-dps floor.
Exploratory; no fit; no production rewire.
Run:  python3 -u computations/binding_observe_last.py 2>&1 | tee /tmp/ol.log
"""
from __future__ import annotations

import _path_bridge  # noqa: F401, E402
import sys
import json
import math
from pathlib import Path

import mpmath as mp  # noqa: E402

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

from _precision import set_compute_dps  # noqa: E402
set_compute_dps()

from wedderburn_jones_markov import y_lambda_at  # noqa: E402
from q_parameter import Q as Q0  # noqa: E402
from codata_constants import M_E_MEV  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

ATOMS = [("2H", 1, 1, "atom-chi-rust-d.witness.json"),
         ("3H", 1, 2, "atom-chi-rust-t.witness.json"),
         ("3He", 2, 1, "atom-chi-rust-3he.witness.json"),
         ("4He", 2, 2, "atom-chi-rust-4he.witness.json")]


def dim_sn(lam):
    """f^λ = dim(S^λ) via the hook-length formula."""
    n = sum(lam)
    num = math.factorial(n)
    den = 1
    for i in range(len(lam)):
        for j in range(lam[i]):
            arm = lam[i] - j - 1
            leg = sum(1 for r in range(i + 1, len(lam)) if lam[r] > j)
            den *= arm + leg + 1
    return num // den


def load_chi(fname, cfg):
    d = json.loads((HERE / fname).read_text())
    blk = d["data"][cfg]
    return {tuple(e["partition"]): mp.mpf(str(e["chi_lambda"]))
            for e in blk["by_partition"]}


def theta(chi, d):
    """Per-block q-Reeb phase: arccos on the rotation channel (|r|≤1),
    arccosh on the growth channel (|r|>1).  The archimedean observation
    of one Wedderburn block."""
    r = chi / d
    return mp.acos(r) if abs(r) <= 1 else mp.acosh(abs(r))


def main() -> int:
    q0 = mp.mpf(str(Q0))
    from binding_canonical import _Q_BETA_N     # CAL-3 β-decay scale (NOT E_0)
    alpha = mp.mpf(str(_Q_BETA_N))              # Q_β(n) ≈ 0.78233 MeV
    lnq = mp.log(q0)
    print(f"\n  OBSERVE-EARLY vs OBSERVE-LAST   q₀={float(q0):.6f}  "
          f"Q_β={float(alpha):.5f} MeV  (canonical binding scale)\n")

    ame = json.loads((HERE / "data" / "ame2020.json").read_text())
    ae = ame.get("entries", ame)
    arows = ae.values() if isinstance(ae, dict) else ae
    AME = {(r["Z"], r["A"]): mp.mpf(str(r["binding_energy_total_keV"])) / 1000
           for r in arows if r.get("binding_energy_total_keV")}

    w = (WitnessBuilder("binding-observe-last", engine="mpmath")
         .set_content_block("rem:observe-last-jensen-gap")
         .set_description(
             "observe-EARLY (step-5 scalar collapse, B_pred=E₀·(tr_free−"
             "tr_atom)) vs observe-LAST (per-block q-Reeb phase θ_λ first, "
             "B_late=E₀·Σ_λ y_λ(θ_λ^free−θ_λ^atom)); tests whether the Jensen "
             "gap log(Σ)≠Σ(log) reproduces the residual Δ_λ≈q₀^(10A−5) "
             "(§6b reframe). Per-λ χ from atom-chi-rust witnesses; y_λ from "
             "wedderburn_jones_markov. NO FLOAT, 50 dps. Exploratory.")
         .add_data("q_0", str(q0)).add_parameter("compute_dps", str(mp.mp.dps)))

    print("  iso  A  B_pred   e_pred(≈10A−5)  B_late_signed  e_late  g_late  "
          "B_late_growth  e_lateG")
    rows = []
    maxpref = mp.mpf(0)
    REF_BPRED = {"2H": "0.4656", "3H": "0.6290", "3He": "0.6581", "4He": "0.7135"}
    for name, Z, N, fname in ATOMS:
        A = Z + N
        n = 3 * A
        cf = load_chi(fname, "free")
        ca = load_chi(fname, "atom")
        y = y_lambda_at(n, q0)
        parts = list(cf.keys())
        dim = {lam: mp.mpf(dim_sn(list(lam))) for lam in parts}

        # observe-EARLY: scalar trace then difference (residual-audit B_pred)
        tr_free = mp.fsum(y[lam] * cf[lam] for lam in parts)
        tr_atom = mp.fsum(y[lam] * ca[lam] for lam in parts)
        B_pred = alpha * (abs(tr_free) - abs(tr_atom))   # production (residual-audit)
        # preflight: B_pred must match the residual-audit table
        pref = abs(B_pred - mp.mpf(REF_BPRED[name]))
        maxpref = max(maxpref, pref)

        # observe-LAST: per-block q-Reeb phase first, weighted sum last
        dth = {lam: theta(cf[lam], dim[lam]) - theta(ca[lam], dim[lam])
               for lam in parts}
        B_late = alpha * mp.fsum(y[lam] * dth[lam] for lam in parts)
        # growth-only variant (the extensive channel per the reeb probe)
        grow = [lam for lam in parts if abs(cf[lam] / dim[lam]) > 1
                or abs(ca[lam] / dim[lam]) > 1]
        B_lateG = alpha * mp.fsum(y[lam] * dth[lam] for lam in grow)

        bame = AME.get((Z, A))
        e_pred = mp.log(bame / B_pred) / lnq if B_pred > 0 else mp.nan
        e_late = (mp.log(bame / B_late) / lnq if B_late > 0 else mp.nan)
        g_late = (mp.log(B_late / B_pred) / lnq if (B_late > 0 and B_pred > 0)
                  else mp.nan)
        e_lateG = (mp.log(bame / B_lateG) / lnq if B_lateG > 0 else mp.nan)

        print(f"  {name:4s} {A} {float(B_pred):7.4f}  {float(e_pred):8.2f} "
              f"(={10*A-5:>2d})  {float(B_late):11.4f}  {float(e_late):6.2f} "
              f"{float(g_late):6.2f}  {float(B_lateG):11.4f}  {float(e_lateG):6.2f}")
        rows.append({
            "atom": name, "Z": Z, "N": N, "A": A,
            "B_pred": str(B_pred), "B_AME": str(bame),
            "law_10A_5": 10 * A - 5,
            "e_pred_residual_exponent": str(e_pred),
            "B_late_signed": str(B_late), "e_late": str(e_late),
            "g_late_over_pred": str(g_late),
            "B_late_growth_only": str(B_lateG), "e_late_growth": str(e_lateG),
            "preflight_B_pred_resid": str(pref),
            "n_blocks": len(parts), "n_growth_blocks": len(grow)})
    w.add_data("atoms", rows)

    pref_ok = maxpref < mp.mpf("1e-3")
    print(f"\n  PREFLIGHT (B_pred ≡ residual-audit table): max|Δ|="
          f"{float(maxpref):.2e} → {'PASS' if pref_ok else 'CHECK'}")
    w.add_assertion("B_pred_matches_residual_audit_table",
                    computed=float(maxpref), expected=0.0, tolerance=1e-3,
                    source="E₀·(|tr_free|−|tr_atom|) vs 2026-06-09 residual audit")
    # is e_pred ≈ 10A−5 (preflight on the residual law itself)?
    print("  READ: e_pred≈10A−5 confirms the residual law. If e_late≈0 (or "
          "g_late≈10A−5) for some observe-last form, observe-last DERIVES the "
          "residual; if e_late stays far from 0, the Jensen gap is NOT the "
          "residual (reframe refuted at this collapse form).")
    w.add_data("verdict_hint",
               "compare e_late / e_lateG to 0 and g_late to 10A−5 per atom")
    print(f"\n  witness: {w.save()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
