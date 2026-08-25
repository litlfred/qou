#!/usr/bin/env python3
"""alpha_EM 2/(3pi) vs Bloch-Wigner dilog — discriminant probe (#3824 vs #3810).

Tests whether the alpha_EM zero-mode correction 2/(3pi)=2g/(4pi(g-1)) at g=4 (and
the loop measure 1/(pi b1)=1/(8pi)) is a Bloch-Wigner DILOGARITHM shadow (#3824)
or the standard 4D gauge-loop factor 1/(4pi) with b1=8 coincidental (#3810).

HONEST FRAMING: 2/(3pi) is already a closed form, so a bare numerical match at
g=4 cannot by itself discriminate the two readings. What IS informative is the
ARITHMETIC SIGNATURE: dilog values carry pi^2 (Rogers) or are O(1) reals (D);
2/(3pi) carries a SINGLE power of pi -> the gauge-loop signature. This probe
records that structural fact + the absence of a clean bare-D identification.

Emits computations/alphaem-dilog-bloch-probe.witness.json.
"""
import json
from mpmath import mp, mpf, pi, polylog, im, arg, log, sqrt, e, mpc, expjpi, fabs
import _path_bridge  # noqa: F401, E402 — flat-namespace bridge
from _precision import set_compute_dps  # noqa: E402
set_compute_dps()

def D(z):
    z = mpc(z)
    if z == 0 or z == 1:
        return mpf(0)
    return im(polylog(2, z)) + arg(1 - z) * log(fabs(z))

t_add = 2/(3*pi)     # 2g/(4pi(g-1)) at g=4
t_loop = 1/(8*pi)    # 1/(pi b1), b1 = 2g = 8

cands = {
  "D(e^{i pi/3}) [4_1]":   D(expjpi(mpf(1)/3)),
  "Vol(4_1)":              2*D(expjpi(mpf(1)/3)),
  "D(i)=Catalan":          D(1j),
  "D(e^{2pi i/5}) [Bring]":D(e**(2j*pi/5)),
  "D(e^{4pi i/5}) [Bring]":D(e**(4j*pi/5)),
  "L_R(1/phi)=pi^2/10":    pi**2/10,
  "L_R(1/phi^2)=pi^2/15":  pi**2/15,
}

# no clean low-complexity rational multiple within 1e-4
def clean_ratio(x):
    for q in range(1, 25):
        for p in range(1, 25):
            if fabs(x - mpf(p)/q) < mpf(10)**-4:
                return f"{p}/{q}"
    return None

results = []
for k, v in cands.items():
    r = t_add / v
    results.append({"class": k, "D_value": float(v),
                    "ratio_2over3pi": float(r), "clean_rational": clean_ratio(r)})

# The single-power-of-pi signature test: D(z)=2pi/3 would be needed for a bare-D
# origin of 2/(3pi)=(2/3)(1/pi).  Nearest natural value:
need = 2*pi/3
vol41 = 2*D(expjpi(mpf(1)/3))
signature = {
  "target_2over3pi": float(t_add),
  "target_1over8pi": float(t_loop),
  "single_pi_power": True,   # 2/(3pi) = (2/3)*(1/pi)
  "gauge_signature": "1/(4pi) single-pi  (favours #3810)",
  "dilog_signature_would_be": "pi^2 (Rogers) or O(1) real (D)  -- NOT single 1/pi",
  "D_needed_for_bareD_origin": float(need),      # 2pi/3 = 2.0944
  "nearest_natural_value_Vol41": float(vol41),   # 2.0299
  "bareD_mismatch_pct": float(100*(need-vol41)/need),
}
verdict = ("scope-(a) NEGATIVE for the simplest dilog identification: no natural "
           "Bring/4_1/golden bare Bloch-Wigner D-value reproduces 2/(3pi) or "
           "1/(8pi) as a clean rational multiple, and 2/(3pi)'s single power of pi "
           "is the gauge-loop 1/(4pi) signature, not the dilog pi^2/O(1) signature. "
           "Leading order favours #3810 (gauge). Any dilog content must be at the "
           "regulator-normalisation or next-order B_n(C) level (NOT evidenced here).")

witness = {
  "schema": "probe/v0",
  "description": "alpha_EM 2/(3pi) vs Bloch-Wigner dilog discriminant probe (#3824 vs #3810)",
  "computation": "computations/alphaem_dilog_bloch_probe.py",
  "targets": {"2/(3pi)": float(t_add), "1/(8pi)": float(t_loop)},
  "candidate_dilog_values": results,
  "arithmetic_signature": signature,
  "verdict": verdict,
  "scope": "scope-(a) negative; discriminates AGAINST simplest dilog reading, FOR #3810 gauge at leading order; anti-laundering: numerical, not a derivation",
}
import os as _os, sys as _sys  # noqa: E402 — P30 rollup (bean cmiy)
_d = _os.path.dirname(_os.path.abspath(__file__))
while _d != _os.path.dirname(_d) and not _os.path.isdir(_os.path.join(_d, "substrate")):
    _d = _os.path.dirname(_d)
_sys.path.insert(0, _os.path.join(_d, "substrate"))
from witness_base import WitnessBuilder  # noqa: E402
WitnessBuilder.stamp_staleness_metadata(witness, script_path=__file__, engine="python")
witness["scriptFile"] = _os.path.basename(__file__)
# Script-relative, not cwd-relative: the old "computations/…" literal wrote to
# computations/computations/… whenever this ran from inside computations/.
_OUT = _os.path.join(_os.path.dirname(_os.path.abspath(__file__)),
                     "alphaem-dilog-bloch-probe.witness.json")
with open(_OUT, "w") as f:
    json.dump(witness, f, indent=2)
print("VERDICT:", verdict)
print("\nsingle-pi signature:", json.dumps(signature, indent=2))
print("\nany clean rational multiple?",
      [r["clean_rational"] for r in results])
