#!/usr/bin/env python3
"""qbeta_ck_sseries_operator_match_probe.py — Hoefsmit Stage B (path 1):
do EXACT constant c_k exist?  Decisive s=q-1 series-match.

Object (now CORRECT — validated, q=1 finite):
  Q_beta(q) = |Delta(net)(q)| * E_0(q),
  Delta(net)(q) = net_n(q) - net_p(q)  (GB-reduced, SYMBOLIC, summed from
                  free-neutron-decay.witness.json coefficient_symbolic),
  E_0(q) = m_e / (q(q-1)),  Q_A(q) = m_e (2q+1-q^2)(q+1)/(2q^3) [substrate].
  Delta(net) carries a (q-1) zero that cancels the E_0 pole; Q_beta(1) is
  finite and equals Q_A(1)=2 m_e, so R(1)=1.  Validate |Delta|*E_0 at q0
  ~ 0.787 MeV (~Q_beta) before trusting anything.

Ladder:  R(q) = Q_beta(q)/[Q_A(q) cos(alpha_eff(q))] = prod_{k>=2}(1+c_k u^k),
         u = b hbar_q^2,  alpha_eff = (z-1)h/2 - u/2.

Method (NUMERIC mpmath, fast — replaces the timed-out sympy series):
  Taylor R(s) and u(s) around s = q-1 = 0 via mp.taylor (R analytic at
  q=1).  Match log R(s) = sum_k log(1+c_k u(s)^k) order-by-order in s:
  c_2 from s^4, c_3 from s^6, ..., c_k from s^{2k} (triangular).

GATE: c_2 == -1 (proved, PR #1786). FAIL => convention wrong, STOP.
CONSISTENCY: after solving c_2..c_8, the constant-c_k model is EXACT iff
the residual at the next even order ~ 0; a nonzero residual means the c_k
are q-dependent (kernel R(q,xi) needed). auditOnly; no production wiring.
"""
from __future__ import annotations

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import _path_bridge as _pb  # noqa: E402, F401

import json  # noqa: E402
import sympy as sp  # noqa: E402
import mpmath as mp  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

mp.mp.dps = 60
HERE = Path(__file__).resolve().parent


def load_net_symbolic(side):
    q = sp.Symbol("q", positive=True)
    d = json.load(open(_pb.witness_path("free-neutron-decay.witness.json", HERE)))
    terms = d[side]["nf_terms"]
    net = sp.Integer(0)
    for t in terms:
        net += sp.sympify(t["coefficient_symbolic"], locals={"q": q})
    return sp.simplify(net)


def main() -> int:
    q = sp.Symbol("q", positive=True)
    KC = 8

    print("=" * 78)
    print(" Hoefsmit Stage B — exact s-series operator c_k match (c_2 gate)")
    print("=" * 78)

    net_n = load_net_symbolic("neutron")
    net_p = load_net_symbolic("proton")
    dnet = sp.simplify(net_n - net_p)
    print(f"  net_n(q) = {sp.nsimplify(net_n) if net_n.free_symbols=={ } else net_n}")
    print(f"  Δ(net)(q) = {dnet}")

    q0_str = json.load(open(_pb.witness_path("q-pinning-50-digit.witness.json", HERE)))["derived_50_digit"]["q"]
    q0 = mp.mpf(q0_str)

    # Δ(net) has a (q-1) zero (numerator(1)=0) that cancels the E_0 pole.
    # Regularise: dnet_reg = Δ(net)/(q-1) is finite at q=1.
    dnet_reg = sp.cancel(dnet / (q - 1))
    dnet_f = sp.lambdify(q, dnet, "mpmath")
    dnet_reg_f = sp.lambdify(q, dnet_reg, "mpmath")

    # validate against witness numerics at q0
    d_wit = json.load(open(_pb.witness_path("free-neutron-decay.witness.json", HERE)))
    dn_wit = mp.mpf(str(d_wit["transition"]["delta_net"]))
    dn_mine = dnet_f(q0)
    print(f"\n  VALIDATE @ q0:  Δ(net) mine = {mp.nstr(dn_mine,12)}  witness = {mp.nstr(dn_wit,12)}  Δ={mp.nstr(abs(dn_mine-dn_wit),3)}")
    val_ok = abs(dn_mine - dn_wit) < mp.mpf("1e-6")

    # Q_beta(q0) = |Δnet|·E0 ; m_e in MeV
    from codata_constants import M_E_MEV  # noqa
    m_e = mp.mpf(str(M_E_MEV))
    E0 = lambda qq: m_e / (qq * (qq - 1))
    Qb_q0 = abs(dn_mine) * E0(q0)
    print(f"  VALIDATE @ q0:  |Δnet|·E0 = {mp.nstr(Qb_q0,10)} MeV   (Q_β CODATA ≈ 0.78233)")

    # substrate scalars as mpmath fns of q
    def hbar(qq): return (qq - 1) / qq
    def bsub(qq): return mp.sqrt(qq**4 + qq**2 + 1) / (qq**2 + 1)
    def uf(qq): return bsub(qq) * hbar(qq)**2
    def zf(qq): return 1 / (mp.sqrt(qq) + 1/mp.sqrt(qq))
    def hf(qq): return qq - 1/qq
    def alpha_eff(qq): return (zf(qq) - 1)*hf(qq)/2 - uf(qq)/2
    def QA_over_me(qq): return (2*qq + 1 - qq**2)*(qq + 1)/(2*qq**3)

    # sign of Δnet near q0/q=1 (substrate branch): use |Δnet| = -Δnet if <0
    sgn = mp.sign(dn_mine)
    def Qb_over_me(qq):
        # |Δnet|·E0/m_e = sgn·[Δnet/(q-1)]/q  (regularised — no 0/0 at q=1)
        return sgn * dnet_reg_f(qq) / qq
    def R(qq):
        return Qb_over_me(qq) / (QA_over_me(qq) * mp.cos(alpha_eff(qq)))

    # R(1) check (should be 1)
    R1 = mp.limit(R, 1) if hasattr(mp, "limit") else R(1 + mp.mpf("1e-25"))
    print(f"  R(q->1) = {mp.nstr(R1,12)}  (ladder needs R(1)=1)")

    # numeric Taylor of log(R/R1) and u around s=0 (q=1)
    NS = 2*KC + 3
    print(f"\n  numeric mp.taylor of log R(1+s) and u(1+s) to s^{NS} ...")
    logR_s = mp.taylor(lambda s: mp.log(R(1 + s)/R1), 0, NS)
    u_s = mp.taylor(lambda s: uf(1 + s), 0, NS)

    # u(s)^k Taylor coeffs
    def series_pow(coeffs, k, N):
        res = [mp.mpf(1)] + [mp.mpf(0)]*N
        for _ in range(k):
            new = [mp.mpf(0)]*(N+1)
            for i in range(N+1):
                if res[i] == 0: continue
                for j in range(N+1-i):
                    new[i+j] += res[i]*coeffs[j]
            res = new
        return res
    upow = {k: series_pow(u_s, k, NS) for k in range(1, KC+1)}

    # odd-order check (should be ~0 if structure clean)
    odd_mag = max(abs(logR_s[m]) for m in range(3, NS, 2))
    print(f"  max |odd-order [s^odd] log R| = {mp.nstr(odd_mag,3)} (small => clean even structure)")

    # match: log R = sum_k log(1+c_k u^k); solve c_k sequentially at s^{2k}
    # log(1+c_k u^k) = c_k u^k - c_k^2 u^{2k}/2 + ... ; build model incrementally
    c = {}
    model = [mp.mpf(0)]*(NS+1)   # current sum of log(1+c_j u^j) Taylor coeffs
    gate_ok = None
    for k in range(2, KC+1):
        order = 2*k
        # residual at s^{order} from already-fixed c_j (j<k)
        resid = logR_s[order] - model[order]
        # leading contribution of c_k at s^{order} is c_k * upow[k][order]
        lead = upow[k][order]
        ck = resid / lead
        c[k] = ck
        print(f"  c_{k} (s^{order}) = {mp.nstr(ck, 14)}")
        if k == 2:
            gate_ok = abs(ck - (-1)) < mp.mpf("1e-8")
            print(f"    GATE c_2 == -1 ? {'PASS ✓' if gate_ok else 'FAIL ✗  (convention wrong; c_3.. NOT trusted)'}")
            if not gate_ok:
                break
        # add log(1+c_k u^k) Taylor to model
        ck_u = [ck*upow[k][i] for i in range(NS+1)]   # c_k u^k series
        # log(1+x) = sum_{n>=1} (-1)^{n+1} x^n / n
        xpow = [mp.mpf(0)]*(NS+1); xpow[0] = mp.mpf(1)  # x^0
        acc = [mp.mpf(0)]*(NS+1)
        cur = [mp.mpf(1)] + [mp.mpf(0)]*NS
        n = 1
        while n*order <= NS:
            # cur = (c_k u^k)^n
            new = [mp.mpf(0)]*(NS+1)
            for i in range(NS+1):
                if cur[i] == 0: continue
                for j in range(NS+1-i):
                    new[i+j] += cur[i]*ck_u[j]
            cur = new
            sign = mp.mpf((-1)**(n+1))
            for i in range(NS+1):
                acc[i] += sign*cur[i]/n
            n += 1
        for i in range(NS+1):
            model[i] += acc[i]

    consistent = None
    resid_next = None
    if gate_ok:
        nxt = 2*KC + 2
        if nxt <= NS:
            resid_next = logR_s[nxt] - model[nxt]
            consistent = abs(resid_next) < mp.mpf("1e-12")
            print(f"\n  residual at s^{nxt} after c_2..c_{KC} = {mp.nstr(resid_next,4)}")
            print(f"  constant-c_k model EXACT? {'YES (constants exist!)' if consistent else 'NO -> c_k are q-DEPENDENT (kernel needed)'}")

    print()
    print("  c_k summary:", {k: mp.nstr(v, 8) for k, v in c.items()})

    wb = WitnessBuilder("qbeta-ck-sseries-operator-match", engine="python+sympy+mpmath")
    wb.set_description(
        "Hoefsmit Stage B path-1: exact s=q-1 numeric series-match of the "
        "canonical operator ladder R=Q_beta/[Q_A cos(alpha_eff)] vs "
        "prod(1+c_k u^k), Q_beta=|Delta(net)|*E_0 from GB-reduced symbolic "
        "net. c_2=-1 gate; residual test for constant-c_k consistency."
    )
    wb.add_data("delta_net_q_symbolic", str(dnet))
    wb.add_data("validate_delta_net_at_q0", float(dn_mine))
    wb.add_data("validate_Qbeta_at_q0_MeV", float(Qb_q0))
    wb.add_data("R_at_q1", float(R1))
    wb.add_data("c2_gate_pass", bool(gate_ok))
    wb.add_data("c_k", {str(k): float(v) for k, v in c.items()})
    wb.add_data("max_odd_order_logR", float(odd_mag))
    wb.add_data("residual_next_even", None if resid_next is None else float(resid_next))
    wb.add_data("constant_ck_exact", None if consistent is None else bool(consistent))
    wb.add_assertion(
        "validate_object_at_q0",
        computed=1 if val_ok else 0, expected=1, tolerance=0,
        source="symbolic Δ(net)(q0) matches free-neutron-decay.witness delta_net",
    )
    wb.add_assertion(
        "c2_gate",
        computed=1 if gate_ok else 0, expected=1, tolerance=0,
        source="operator s-series match reproduces proved c_2 = -1",
    )
    wb.save()
    print("\n  Witness: qbeta-ck-sseries-operator-match.witness.json")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
