#!/usr/bin/env python3
# polynomial_q_not_applicable: evaluates at q = q_0, numeric output.
"""Thread 2 — deuteron per-knot VolDensity, RAW (no tuning).

Per the cheat-sheet step-9a wire-up (vol-usage audit 2026-06-02): production
uses the UNIFORM `Vol(𝓑₃)=8·G` for every atom. The paper's per-knot mass is

    m(K) = m_e · [Vol(K)/ℏ_q²] · tr_M(K),

`tr_M(K) = Σ_λ y_λ χ_λ(β_K)/dim λ` over partitions of the knot's OWN strand
count (H₆ for the 6-strand deuteron). This probe computes the deuteron mass with
the §9.3 canonical link assignment **Vol(6₂)** vs the uniform **Vol(𝓑₃)=8G**,
holding the same canonical H₆ trace, and reports BOTH raw against AME — no fit,
no tuning (discipline gate: report the raw discrepancy, never force a match).
"""
from __future__ import annotations

import _path_bridge  # noqa: F401
from codata_constants import M_D_MEV_VALIDATION  # noqa: E402 (codata sweep)
import json
import sys
from pathlib import Path

import mpmath as mp

from _precision import set_compute_dps  # noqa: E402
set_compute_dps()

HERE = Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))

from _li_2_q_util import per_knot_density_per_block  # noqa: E402
from experimental_constants import M_E_MEV  # noqa: E402
from q_parameter import Q_50_DIGIT_STR  # noqa: E402

q0 = mp.mpf(Q_50_DIGIT_STR)
VOL_B3 = 8 * mp.catalan                      # Vol(𝓑₃) = 8·G (Adams 1985), the uniform value
# Vol(6₂), §9.3 deuteron link. The literal here was
#   4.40083298054544839393  -- annotated "SnapPy census" and NOT from it:
# it is wrong at digit 9 (1.06e-7 relative) while printing 21. The true
# value, snappy.Manifold("6_2").volume(bits_prec=500), was already in the
# corpus at probes/gap_a4_T2_per_knot_vol_probe.py, so the two disagreed.
# Vol(6₂) has no closed form, hence a literal; it is checked by
# computations/hyperbolic_volume_literal_audit.py.
VOL_6_2 = mp.mpf("4.40083251612304610144120386564")
M_D_AME = mp.mpf(M_D_MEV_VALIDATION)            # deuteron mass (CODATA/AME), MeV

# canonical H₆ deuteron trace tr_M(β_D) from the chi-deuteron-h6 cache
tr_M_D = None
src = None
try:
    from canonical_tr_m_via_chi_cache import canonical_tr_m
    res = canonical_tr_m("D", 1, 1)
    # locate the scalar trace in the returned dict
    for k in ("tr_M", "trace", "tr_m", "total", "tr_M_canonical", "value"):
        if isinstance(res, dict) and k in res:
            tr_M_D = mp.mpf(str(res[k])); src = f"canonical_tr_m['{k}']"; break
    if tr_M_D is None and isinstance(res, dict):
        print("canonical_tr_m keys:", list(res.keys()))
except Exception as e:  # noqa: BLE001
    print(f"canonical_tr_m unavailable: {type(e).__name__}: {e}")

if tr_M_D is None:
    print("FATAL: could not obtain canonical tr_M(β_D); reporting the Vol-only ratio instead.")
    # Even without the trace, the per-knot vs uniform mass ratio is Vol(6₂)/Vol(𝓑₃):
    print(f"  Vol(6₂)/Vol(𝓑₃) = {float(VOL_6_2/VOL_B3):.6f}  (per-knot mass = this × uniform mass, same trace)")
    sys.exit(1)  # gated: no canonical trace ⇒ non-zero so CI/automation don't read it as success

print(f"tr_M(β_D) [{src}] = {mp.nstr(tr_M_D, 12)}")
geom_perknot = per_knot_density_per_block(VOL_6_2, tr_M_D, q0)   # Vol(6₂)/ℏ² · tr_M
geom_uniform = per_knot_density_per_block(VOL_B3, tr_M_D, q0)    # Vol(8G)/ℏ²  · tr_M  (the bug)
m_perknot = M_E_MEV * geom_perknot
m_uniform = M_E_MEV * geom_uniform
err_pk = (m_perknot - M_D_AME) / M_D_AME
err_un = (m_uniform - M_D_AME) / M_D_AME

print(f"\n m_D (per-knot Vol(6₂)) = {mp.nstr(m_perknot,10)} MeV   err vs AME = {float(err_pk)*100:+.3f}%")
print(f" m_D (uniform Vol(𝓑₃))  = {mp.nstr(m_uniform,10)} MeV   err vs AME = {float(err_un)*100:+.3f}%")
print(f" AME m_D                = {mp.nstr(M_D_AME,10)} MeV")
better = abs(err_pk) < abs(err_un)
print(f"\n per-knot {'IMPROVES' if better else 'does NOT improve'} the deuteron mass "
      f"({abs(float(err_un))*100:.2f}% → {abs(float(err_pk))*100:.2f}%)")

witness = {
    "computation": "vol_density_deuteron_perknot",
    "description": "Thread 2: deuteron per-knot VolDensity (Vol(6₂)) vs uniform (Vol(𝓑₃)=8G), raw vs AME",
    "discipline": "no fit; raw report per the per-block wiring discipline gate; nothing wired to production",
    "q0": str(q0), "tr_M_D": mp.nstr(tr_M_D, 20), "tr_M_source": src,
    "vol_6_2": str(VOL_6_2), "vol_b3_8G": mp.nstr(VOL_B3, 20),
    "m_D_perknot_MeV": mp.nstr(m_perknot, 12), "err_perknot": mp.nstr(err_pk, 15),
    "m_D_uniform_MeV": mp.nstr(m_uniform, 12), "err_uniform": mp.nstr(err_un, 15),
    "m_D_AME_MeV": str(M_D_AME), "per_knot_improves": bool(better),
}
(HERE / "vol-density-deuteron-perknot.witness.json").write_text(json.dumps(witness, indent=2, ensure_ascii=False))
print("witness -> vol-density-deuteron-perknot.witness.json")
