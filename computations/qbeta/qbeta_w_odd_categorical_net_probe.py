#!/usr/bin/env python3
"""qbeta_w_odd_categorical_net_probe.py — The W-odd tranche and the h/4 ratio.

This probe verifies that the bar-odd part of the Q_beta categorical net
(neutron - proton) exactly reproduces the KC20 irreducible odd-channel cubic
with a ratio of h/4, where h = q - q⁻¹.

Specifically:
  Δ(net)_odd = (h / 4) · C(q² + q⁻²)
where C(y) = y³ - 4y² + 3y - 2.

It also verifies the sector split:
  Δ(Hopf)_odd = (h / 4) · C_Hopf(q² + q⁻²)
  Δ(unknot)_odd = (h / 4) · C_unknot(q² + q⁻²)
giving KC20's sector split for free.
"""
from __future__ import annotations

import sys
from fractions import Fraction as F
from pathlib import Path
import json

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))
sys.path.insert(0, str(HERE))

try:
    import _path_bridge
    from witness_base import WitnessBuilder
    _HAVE_WB = True
except Exception:
    _HAVE_WB = False

def _git_head_sha() -> str:
    import subprocess
    try:
        return subprocess.run(
            ["git", "rev-parse", "HEAD"], cwd=str(HERE),
            capture_output=True, text=True, check=True,
        ).stdout.strip()
    except Exception:
        return ""

class Lau(dict):
    def _c(self, o): return o if isinstance(o, Lau) else Lau({0: F(o)})
    def __add__(self, o):
        o = self._c(o); r = Lau(self)
        for k, v in o.items(): r[k] = r.get(k, 0) + v
        return Lau({k: v for k, v in r.items() if v != 0})
    __radd__ = __add__
    def __neg__(self): return Lau({k: -v for k, v in self.items()})
    def __sub__(self, o): return self + (-self._c(o))
    def __rsub__(self, o): return (-self) + self._c(o)
    def __mul__(self, o):
        o = self._c(o); r = Lau()
        for a, x in self.items():
            for b, y in o.items(): r[a + b] = r.get(a + b, 0) + x * y
        return Lau({k: v for k, v in r.items() if v != 0})
    __rmul__ = __mul__
    def __pow__(self, n):
        if n < 0:
            (p, c), = self.items()
            return Lau({p * n: F(1) / c ** (-n)})
        r = Lau({0: F(1)})
        for _ in range(n): r = r * self
        return r
    def __truediv__(self, o): 
        if isinstance(o, Lau):
            (p, c), = o.items()
            return Lau({k - p: v / c for k, v in self.items()})
        return Lau({k: v / F(o) for k, v in self.items()})
    def __rtruediv__(self, o):
        (p, c), = self.items()
        return Lau({-p: F(o) / c})

Q = Lau({1: F(1)})

def bar_odd(p: Lau) -> Lau:
    """(p(q) − p(1/q))/2 — the bar-odd part under q ↦ q⁻¹."""
    return (p - Lau({-k: v for k, v in p.items()})) / 2

class _PlainWitness:
    def __init__(self, name, engine="python-exact"):
        self._d = {"computation": name, "engine": engine,
                   "scriptFile": Path(__file__).name,
                   "commitSha": _git_head_sha(),
                   "data": {}, "assertions": [], "audit_only": None,
                   "description": ""}
    def set_description(self, s): self._d["description"] = s
    def add_data(self, k, v): self._d["data"][k] = v
    def add_parameter(self, k, v): self._d["data"].setdefault("parameters", {})[k] = v
    def add_assertion(self, **kw): self._d["assertions"].append(kw)
    def set_audit_only(self, p): self._d["audit_only"] = p
    def save(self):
        out = HERE / f"{self._d['computation']}.witness.json"
        self._d["allPassed"] = all(a.get("computed") == a.get("expected")
                                   for a in self._d["assertions"])
        out.write_text(json.dumps(self._d, indent=2, ensure_ascii=False),
                       encoding="utf-8")
        return out

def _find_witness(name: str) -> Path:
    for cand in (HERE.parent / name, HERE / name):
        if cand.exists():
            return cand
    raise FileNotFoundError(name)

def main() -> int:
    wit = json.loads(
        _find_witness("free-neutron-decay.witness.json").read_text(encoding="utf-8")
    )

    _EVAL_GLOBALS = {"__builtins__": {}, "q": Q}

    def coeff(side: str, ws: str) -> Lau:
        for t in wit[side]["nf_terms"]:
            if t["word_str"] == ws:
                return eval(t["coefficient_symbolic"], _EVAL_GLOBALS)  # noqa: S307
        return Lau()

    basis = [t["word_str"] for t in wit["neutron"]["nf_terms"]]
    net = Lau()
    for ws in basis:
        net = net + (coeff("neutron", ws) - coeff("proton", ws))

    sectors = {
        "unknot": ["𝟏"],
        "virtual": ["σ_0", "σ_1"],
        "Hopf": ["σ_0·σ_1", "σ_1·σ_0"],
        "trefoil": ["σ_0·σ_1·σ_0"],
    }
    
    net_Hopf = Lau()
    for ws in sectors["Hopf"]:
        net_Hopf = net_Hopf + (coeff("neutron", ws) - coeff("proton", ws))
        
    net_unknot = Lau()
    for ws in sectors["unknot"]:
        net_unknot = net_unknot + (coeff("neutron", ws) - coeff("proton", ws))

    # W-odd calculation components
    h = Q - Lau({-1: F(1)})
    y = Q**2 + Lau({-2: F(1)})
    
    C_total = y**3 - 4*y**2 + 3*y - 2
    C_Hopf = y**3 - 6*y**2 + 10*y - 6
    C_unknot = 2*y**2 - 7*y + 4

    delta_net_odd = bar_odd(net)
    expected_total = (h / 4) * C_total
    
    delta_Hopf_odd = bar_odd(net_Hopf)
    expected_Hopf = (h / 4) * C_Hopf
    
    delta_unknot_odd = bar_odd(net_unknot)
    expected_unknot = (h / 4) * C_unknot
    
    match_total = (delta_net_odd == expected_total)
    match_Hopf = (delta_Hopf_odd == expected_Hopf)
    match_unknot = (delta_unknot_odd == expected_unknot)

    _WB = WitnessBuilder if _HAVE_WB else _PlainWitness
    b = _WB("qbeta-w-odd-categorical-net", engine="python-exact")
    b.set_description(
        "Verifies the W-odd tranche of the H3 GS categorical net. "
        "The bar-odd projection of the net (neutron - proton) exactly matches "
        "(h/4) * C(y), reproducing KC20's irreducible odd-channel cubic where "
        "h = q - q^-1 and y = q^2 + q^-2. Also verifies that the sector split "
        "C = C_Hopf + C_unknot naturally extends to the bar-odd projections."
    )
    
    b.add_data("match_total", match_total)
    b.add_data("match_Hopf", match_Hopf)
    b.add_data("match_unknot", match_unknot)
    
    b.add_assertion(name="net_odd_is_h_over_4_times_C", computed=0.0 if match_total else 1.0,
                    expected=0.0, tolerance=0.0, unit="bool (0 = holds)",
                    source="exact Q-Laurent arithmetic")
    b.add_assertion(name="Hopf_odd_is_h_over_4_times_C_Hopf", computed=0.0 if match_Hopf else 1.0,
                    expected=0.0, tolerance=0.0, unit="bool (0 = holds)",
                    source="exact Q-Laurent arithmetic")
    b.add_assertion(name="unknot_odd_is_h_over_4_times_C_unknot", computed=0.0 if match_unknot else 1.0,
                    expected=0.0, tolerance=0.0, unit="bool (0 = holds)",
                    source="exact Q-Laurent arithmetic")
                    
    out = b.save()
    print(f"Witness: {out}")
    print(f"  match_total={match_total}")
    print(f"  match_Hopf={match_Hopf}")
    print(f"  match_unknot={match_unknot}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
