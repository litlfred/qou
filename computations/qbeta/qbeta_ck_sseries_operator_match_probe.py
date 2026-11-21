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

import sys as _s0, pathlib as _p0; _s0.path.insert(0, str(next(p for p in _p0.Path(__file__).resolve().parents if p.name == "computations") / "qbeta")); import qbeta_e0 as _qbeta_e0  # noqa: E401,E402,E702 (#8590) order-zero E_0 routed + labelled, owner ruling 2026-11-20
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import _path_bridge as _pb  # noqa: E402, F401

import json  # noqa: E402
import sympy as sp  # noqa: E402
import mpmath as mp  # noqa: E402
from _precision import fmt  # noqa: E402
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
    E0 = lambda qq: _qbeta_e0.order_zero_scaled(m_e, qq)
    Qb_q0 = abs(dn_mine) * E0(q0)
    print(f"  VALIDATE @ q0:  |Δnet|·E0 = {mp.nstr(Qb_q0,10)} MeV   (Q_β CODATA ≈ 0.78233)")

    # substrate scalars as mpmath fns of q
    def hbar(qq): return (qq - 1) / qq
    def bsub(qq): return mp.sqrt(qq**4 + qq**2 + 1) / (qq**2 + 1)
    def uf(qq): return bsub(qq) * hbar(qq)**2
    def zf(qq): return qq ** 3 / (qq ** 2 + 1)   # convention D
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
    # `fmt`, not `float()` — these are mpf end to end and the float64 downcast
    # is what the raw-float64 ratchet flags. It matters more than usual here:
    # the c_k extraction amplifies input error by ~7e5 (see below), so digits
    # thrown away at the input are not cosmetic.
    wb.add_data("validate_delta_net_at_q0", fmt(dn_mine))
    wb.add_data("validate_Qbeta_at_q0_MeV", fmt(Qb_q0))
    wb.add_data("R_at_q1", fmt(R1))
    wb.add_data("c2_gate_pass", bool(gate_ok))
    # ── Why this gate is red, and why it must STAY red ───────────────────
    #
    # The gate asks whether a scalar s-series in s = q-1 reproduces c_2 = -1.
    # It does not, and that IS the finding rather than a defect: u = b*hbar_q^2
    # is QUADRATIC in t = q-1 near q = 1 (u ~ (sqrt3/2) t^2), so the
    # u-reversion is singular, R(q) is not analytic in u, and the c_k are not
    # scalar-q Taylor coefficients at all. Blocker 2 of
    # docs/audits/2026-06-16-hoefsmit-stage-b-attempt-verdict.md.
    # Relaxing this gate would delete a recorded refutation.
    #
    # ── The extracted quadratic is INPUT-SENSITIVE, and violently so ──────
    #
    # Do NOT read the extracted value as any named c_2 variant. The witness
    # committed on 2026-06-16 carried -8.006410058709255, which matches the
    # registry's c_2^even = -1049/144 - 5*sqrt(3)/12 to fifteen digits, and
    # that coincidence is tempting. It does not survive a re-run.
    #
    # Re-run 2026-08-23 on a byte-identical producer: -7.45876032789888. The
    # cause is import-cone drift, not this file — free-neutron-decay.witness.json
    # was regenerated in 52c68267f2, moving Delta(net) from -0.18829060147138277
    # to -0.1882906200111204. That is a 9.8e-8 RELATIVE change in the input; it
    # moved the extracted quadratic by 6.8%, an amplification of roughly 7e5.
    #
    # Which is itself the audit's blocker 3 measured rather than argued:
    # sigma(c_k) = sigma_R / u^k, so at u ~ 0.0085 the k = 2 rung divides input
    # error by ~1.4e4 and the k = 3 rung by ~1.6e6. An extraction that amplifies
    # its input error by five orders of magnitude cannot identify a constant, and
    # the 15-digit agreement above is what such an extraction's coincidences look
    # like. Record the value; do not name it.
    wb.add_data("extracted_quadratic_is_a_named_c2_variant", False)
    wb.add_data(
        "why_c2_gate_is_red",
        "NOT a defect and NOT a number to be fixed. The scalar u-reversion is "
        "singular (u is quadratic in q-1), so R(q) is not analytic in u and the "
        "c_k are not scalar-q Taylor coefficients. See "
        "docs/audits/2026-06-16-hoefsmit-stage-b-attempt-verdict.md blocker 2. "
        "Making this gate green would delete a recorded refutation.",
    )
    wb.add_data(
        "extracted_quadratic_input_sensitivity",
        "The 2026-06-16 witness carried -8.006410058709255, matching the "
        "registry's c_2^even = -1049/144 - 5*sqrt(3)/12 to 15 digits. The "
        "coincidence did NOT survive: a byte-identical producer now yields "
        "-7.45876032789888, because free-neutron-decay.witness.json was "
        "regenerated in 52c68267f2 (Delta(net) -0.18829060147138277 -> "
        "-0.1882906200111204). A 9.8e-8 relative input change moved the output "
        "6.8% -- ~7e5 amplification, which is the audit's blocker-3 "
        "sigma(c_k) = sigma_R/u^k measured rather than argued. Do not identify "
        "the extracted quadratic with c_2, c_2-tilde or c_2^even.",
    )
    wb.add_assertion(
        "validate_object_at_q0",
        computed=1 if val_ok else 0, expected=1, tolerance=0,
        source="symbolic Δ(net)(q0) matches free-neutron-decay.witness delta_net",
    )
    wb.add_assertion(
        "c2_gate",
        computed=1 if gate_ok else 0, expected=1, tolerance=0,
        source=(
            "Does the operator s-series reproduce c_2 = -1? EXPECTED RED, and "
            "red is the result. The scalar u-reversion is singular, so the c_k "
            "are not scalar-q Taylor coefficients -- "
            "docs/audits/2026-06-16-hoefsmit-stage-b-attempt-verdict.md "
            "blocker 2. Do NOT relax this gate to make the witness green: it "
            "records a refutation, and the extracted quadratic is input-"
            "sensitive at ~7e5 amplification (see the data fields). "
            "('proved c_2 = -1' until 2026-08-23: c_2 = -1 is STRUCTURAL, not "
            "proved -- N2_factor is a bare def with no theorem deriving it, per "
            "the AGENTS.md correction of 2026-08-16.)"
        ),
    )
    wb.save()
    print("\n  Witness: qbeta-ck-sseries-operator-match.witness.json")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
