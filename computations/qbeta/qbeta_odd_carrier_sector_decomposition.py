#!/usr/bin/env python3
"""qbeta_odd_carrier_sector_decomposition.py — where the odd-channel cubic field comes from.

Follow-up to the ζ₄-residue refutation (bean 0zr0, 2026-07-04) and its Lean
certificate (`QOU/QBeta/QBetaZeta4ResidueRefutation.lean`, 2026-07-07). The
surviving non-cyclotomic content of the Q_β bar-odd carrier is the irreducible
cubic ``C(y) = y³ − 4y² + 3y − 2`` in the bar-even trace variable
``y = q² + q⁻²`` (S₃, disc −152 = −2³·19). This probe asks *where the degree-3
comes from* by decomposing the bar-odd carrier over the four **knot sectors**
of the H₃ normal-form basis ``{𝟏, σ₀, σ₁, σ₀σ₁, σ₁σ₀, σ₀σ₁σ₀}`` (unknot /
virtual / Hopf / trefoil), reading the neutron/proton amplitudes exactly from
``free-neutron-decay.witness.json``.

**Result (exact ℚ-Laurent arithmetic, no sympy, no floats, no fit):**

- virtual (σ₀,σ₁; 1 crossing) → **0**;  electron word (σ₀σ₁σ₀; 3 crossings; key "trefoil" below) → **0**
  (the odd-crossing sectors are bar-EVEN).
- unknot (𝟏; identity) → a **quadratic** ``C_unknot(y) = 2y² − 7y + 4``
  (disc 17, field ℚ(√17)).
- Hopf (σ₀σ₁+σ₁σ₀; 2 crossings) → the **cubic** ``C_Hopf(y) = y³ − 6y² + 10y − 6``
  (no rational root ⇒ irreducible over ℚ; disc −76 = −2²·19).
- ``C = C_Hopf + C_unknot`` exactly.

So the **degree-3 field of the odd channel is sourced entirely by the Hopf
(double-crossing) sector**; the identity contributes only a quadratic; the
odd-crossing sectors vanish. Not a 3-dim rep (H₃ blocks are 1,2,1), not a
single knot invariant — the 2-crossing isospin amplitude. The discriminant
prime 19 is shared by C_Hopf (−76) and the total C (−152).

Audit-only; no wiring; nothing fitted. The Lean twin certifies the y-level
identities (`cubicC_sector_decomp`, `cubicC_Hopf_rrt_candidates_all_nonzero`).
"""
from __future__ import annotations

import sys
from fractions import Fraction as F
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
sys.path.insert(0, str(Path(__file__).resolve().parent))
import json  # noqa: E402

HERE = Path(__file__).resolve().parent
# This probe is pure exact ℚ-arithmetic (no mpmath / no substrate deps), so it
# uses the canonical WitnessBuilder when the substrate stack is importable
# (CI: emits full provenance) and otherwise falls back to a self-contained
# writer that still emits the required provenance fields (sandbox without
# mpmath) — it must run in any environment.
try:
    import _path_bridge  # noqa: E402, F401 — puts computations/substrate on sys.path
    from witness_base import WitnessBuilder  # noqa: E402
    _HAVE_WB = True
except Exception:  # pragma: no cover - sandbox without mpmath/substrate
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
    """Sparse Laurent polynomial over ℚ: {int power: Fraction}."""

    def _c(self, o):
        return o if isinstance(o, Lau) else Lau({0: F(o)})

    def __add__(self, o):
        o = self._c(o); r = Lau(self)
        for k, v in o.items():
            r[k] = r.get(k, 0) + v
        return Lau({k: v for k, v in r.items() if v != 0})

    __radd__ = __add__

    def __neg__(self):
        return Lau({k: -v for k, v in self.items()})

    def __sub__(self, o):
        return self + (-self._c(o))

    def __rsub__(self, o):
        return (-self) + self._c(o)

    def __mul__(self, o):
        o = self._c(o); r = Lau()
        for a, x in self.items():
            for b, y in o.items():
                r[a + b] = r.get(a + b, 0) + x * y
        return Lau({k: v for k, v in r.items() if v != 0})

    __rmul__ = __mul__

    def __pow__(self, n):
        if n < 0:
            (p, c), = self.items()
            return Lau({p * n: F(1) / c ** (-n)})
        r = Lau({0: F(1)})
        for _ in range(n):
            r = r * self
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


def to_trace_cubic(numer: Lau) -> dict:
    """Given an even palindromic Laurent poly, return its coeffs in y = q²+q⁻²
    (power-sum → Chebyshev reduction). Returns {y-degree: Fraction} or None."""
    if not numer:
        return {0: F(0)}
    # symmetric about 0 after centring: express q^{2k}+q^{-2k} = P_k(y)
    # collect coeff of q^{2k} for k ≥ 0 (palindrome ⇒ symmetric)
    pos = {}
    for k, v in numer.items():
        if v == 0:
            continue
        if k < 0:
            continue
        if k % 2 != 0:
            return None  # not even in q
        pos[k // 2] = v
    # P_0 = 2 handled via the k=0 term (already counted once, not doubled)
    # power-sum basis: p_0 = 2 (but const counted once), p_k = q^{2k}+q^{-2k}
    def psum(k):
        p = [F(2), None]
        # p_1 = y ; recurrence p_k = y p_{k-1} - p_{k-2}
        y = {1: F(1)}  # represent as dict of y-powers
        seq = [{0: F(2)}, {1: F(1)}]
        for _ in range(2, k + 1):
            prev, prev2 = seq[-1], seq[-2]
            nxt = {}
            for d, c in prev.items():
                nxt[d + 1] = nxt.get(d + 1, 0) + c
            for d, c in prev2.items():
                nxt[d] = nxt.get(d, 0) - c
            seq.append({d: c for d, c in nxt.items() if c != 0})
        return seq[k]
    out = {}
    for k, v in pos.items():
        if k == 0:
            out[0] = out.get(0, 0) + v
        else:
            for d, c in psum(k).items():
                out[d] = out.get(d, 0) + v * c
    return {d: c for d, c in out.items() if c != 0}


class _PlainWitness:
    """Minimal self-contained witness writer (no substrate/mpmath deps)."""

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

    # Restricted evaluator for the witness `coefficient_symbolic` strings
    # (Laurent polynomials in `q`). `__builtins__` is emptied so no arbitrary
    # code can run even if the witness content is tampered with; only `q`
    # (a `Lau` monomial) and arithmetic operators are in scope.
    _EVAL_GLOBALS = {"__builtins__": {}, "q": Q}

    def coeff(side: str, ws: str) -> Lau:
        for t in wit[side]["nf_terms"]:
            if t["word_str"] == ws:
                return eval(t["coefficient_symbolic"], _EVAL_GLOBALS)  # noqa: S307
        return Lau()

    basis = [t["word_str"] for t in wit["neutron"]["nf_terms"]]
    net = {ws: coeff("neutron", ws) - coeff("proton", ws) for ws in basis}

    sectors = {
        "unknot": ["𝟏"],
        "virtual": ["σ_0", "σ_1"],
        "Hopf": ["σ_0·σ_1", "σ_1·σ_0"],
        "trefoil": ["σ_0·σ_1·σ_0"],
    }
    q2m1 = Lau({2: F(1), 0: F(-1)})

    # full odd numerator (×4q⁷) and its cofactor over (q²−1) = R₁₂
    total = Lau()
    for ws in basis:
        total = total + net[ws]
    num = bar_odd(total) * Lau({7: F(4)})
    num_expected = {14: 1, 12: -5, 10: 10, 8: -16, 6: 16, 4: -10, 2: 5, 0: -1}
    num_ok = {k: int(v) for k, v in num.items()} == num_expected

    q6 = Lau({6: F(1)})

    def sector_cubic_in_y(elements) -> dict | None:
        """Bar-odd numerator of a sector → cofactor over (q²−1) → C(y).
        The cofactor is q⁶·C(q²+q⁻²); divide by q⁶ to centre before the
        power-sum → y reduction. Returns None if the sector's bar-odd part is 0."""
        s = Lau()
        for ws in elements:
            s = s + net[ws]
        so = bar_odd(s) * Lau({7: F(4)})
        if not so:
            return None
        cof = _pdiv(so, q2m1)
        if cof is None:
            return None
        return to_trace_cubic(cof / q6)

    sector_zero = {}
    for name, wss in sectors.items():
        s = Lau()
        for ws in wss:
            s = s + net[ws]
        sector_zero[name] = (len(bar_odd(s)) == 0)

    # y-level totals
    C_total = to_trace_cubic(_pdiv(num, q2m1) / q6)
    C_unknot = sector_cubic_in_y(sectors["unknot"])
    C_Hopf = sector_cubic_in_y(sectors["Hopf"])
    decomp_ok = _yadd(C_unknot, C_Hopf) == C_total
    hopf_is_cubic = max(C_Hopf) == 3
    unknot_is_quadratic = max(C_unknot) == 2
    hopf_no_rational_root = all(
        _yeval(C_Hopf, r) != 0 for r in (1, -1, 2, -2, 3, -3, 6, -6)
    )

    def disc_cubic(c):  # c: {deg:Fraction}, monic assumed after scaling
        a = c.get(3, F(0)); b = c.get(2, F(0))
        cc = c.get(1, F(0)); d = c.get(0, F(0))
        return int(18 * a * b * cc * d - 4 * b ** 3 * d + b * b * cc * cc
                   - 4 * a * cc ** 3 - 27 * a * a * d * d)

    _WB = WitnessBuilder if _HAVE_WB else _PlainWitness
    b = _WB("qbeta-odd-carrier-sector-decomposition", engine="python-exact")
    b.set_description(
        "Knot-sector decomposition of the Q_beta bar-odd carrier: virtual "
        "(1-crossing) and trefoil (3-crossing) sectors vanish; unknot "
        "(identity) gives a quadratic C_unknot(y)=2y^2-7y+4 (disc 17); Hopf "
        "(2-crossing) gives the cubic C_Hopf(y)=y^3-6y^2+10y-6 (irreducible, "
        "disc -76=-2^2*19). C = C_Hopf + C_unknot. The degree-3 field of the "
        "odd channel is sourced ENTIRELY by the Hopf (double-crossing) sector. "
        "Exact Q-Laurent arithmetic; audit-only; no wiring, no fit.")
    b.add_data("num_matches_audit", num_ok)
    b.add_data("sector_bar_odd_vanishes",
               {k: v for k, v in sector_zero.items()})
    b.add_data("C_total_in_y", {int(k): str(v) for k, v in C_total.items()})
    b.add_data("C_unknot_in_y", {int(k): str(v) for k, v in C_unknot.items()})
    b.add_data("C_Hopf_in_y", {int(k): str(v) for k, v in C_Hopf.items()})
    b.add_data("C_total_disc", disc_cubic(C_total))
    b.add_data("C_Hopf_disc", disc_cubic(C_Hopf))
    b.add_data("shared_discriminant_prime", 19)
    b.add_data("verdict",
               "degree-3 (irreducible cubic field) is contributed by the Hopf "
               "double-crossing sector alone; identity adds a quadratic; "
               "virtual+trefoil vanish. NOT a 3-dim rep (H3 blocks 1,2,1), NOT "
               "a single knot invariant.")
    for nm, cond in (
        ("num_reconstructs_audit_carrier", num_ok),
        ("virtual_sector_bar_odd_zero", sector_zero["virtual"]),
        ("trefoil_sector_bar_odd_zero", sector_zero["trefoil"]),
        ("C_equals_Hopf_plus_unknot", decomp_ok),
        ("Hopf_sector_is_the_cubic", hopf_is_cubic),
        ("unknot_sector_is_quadratic", unknot_is_quadratic),
        ("Hopf_cubic_no_rational_root", hopf_no_rational_root),
    ):
        b.add_assertion(name=nm, computed=0.0 if cond else 1.0,
                        expected=0.0, tolerance=0.0,
                        unit="bool (0 = holds)", source="exact Q-Laurent arithmetic")
    b.set_audit_only(
        "docs/audits/2026-07-07-zeta4-residue-lean-certificate-and-surviving-cubic.md")
    out = b.save()
    print(f"Witness: {out}")
    print(f"  num_ok={num_ok} virtual0={sector_zero['virtual']} "
          f"trefoil0={sector_zero['trefoil']} decomp_ok={decomp_ok} "
          f"Hopf_cubic={hopf_is_cubic} hopf_irred={hopf_no_rational_root}")
    return 0


def _pdiv(numer: Lau, den: Lau):
    """Exact Laurent division numer/den; return quotient Lau or None if not
    divisible. Robust to an arbitrary Laurent denominator (any `min(den)`):
    both operands are shifted by their minimum power before the polynomial
    long-division and the quotient is shifted back."""
    if not numer:
        return Lau()
    if not den:
        return None
    shift_num = min(numer)
    shift_den = min(den)
    deg_num = max(numer) - shift_num
    deg_den = max(den) - shift_den
    if deg_num < deg_den:
        return None
    a = [numer.get(i + shift_num, F(0)) for i in range(deg_num + 1)]
    dl = [den.get(i + shift_den, F(0)) for i in range(deg_den + 1)]
    quo = {}
    for i in range(deg_num - deg_den, -1, -1):
        c = a[i + deg_den] / dl[deg_den]
        quo[i + shift_num - shift_den] = c
        for j in range(deg_den + 1):
            a[i + j] -= c * dl[j]
    if any(x != 0 for x in a):
        return None
    return Lau(quo)


def _yadd(a: dict, b: dict) -> dict:
    r = dict(a)
    for k, v in b.items():
        r[k] = r.get(k, 0) + v
    return {k: v for k, v in r.items() if v != 0}


def _yeval(c: dict, y) -> F:
    return sum(v * F(y) ** k for k, v in c.items())


if __name__ == "__main__":
    raise SystemExit(main())
