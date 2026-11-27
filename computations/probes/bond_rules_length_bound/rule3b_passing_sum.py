#!/usr/bin/env python3
"""rule3b_passing_sum.py — rule (3b): weighted sum over the bond words that PASS reading 3 one by one.

Bean `qou-brng` (brief C2, front E). Companion of `bond_rules_length_bound_probe.py` (rule 3a sums every
bond word and applies reading 3 to the summed element). Here reading 3 filters each word, as in the
ceiling probe, so the sum is known only up to the measured length L (A = 2: L = 6, 5334 words,
408 passing; A = 3: L = 4). The longer passing words are unknown; their contribution is bounded:

  r = (N_T + N') / (Z_T + Z'),  |r - r_T| <= (|N'| + |r_T| Z') / Z_T,
  Z' <= Σ_{L>L0} |t|^L c_L,     |N'| <= Σ_{L>L0} |t|^L c_L R_L,

with c_L the number of bond words of length L (inclusion-exclusion) and R_L >= |tr(x K_w)| / tr(x) for
every word of length L: |tr Y| <= ||Y||_2 (normalised quantum trace, positive weight), ||x K_w|| <=
||x|| ||K_w||, and ||K_w|| <= μ_k^{floor(L/k)} μ_{L mod k}, μ_k = max over length-k vertex words
(computed exactly in the Schur-Weyl rep for k <= KMAX). The bound is geometric iff
|t| (n-2) μ_k^{1/k} < 1.

Per-word ratios are read from the committed ceiling witnesses; nothing is recomputed there. Weights t
are corpus quantities (h, qh, h/q), none derived as the bond weight. mpmath, no float arithmetic.
AME not read. Scorecard only.

-- Ref: [leitner2026] bean qou-brng; QOU.MassTheory.BondLengthSumTail.norm_tail_le
"""
from __future__ import annotations

import itertools
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
A = int(sys.argv[1]) if len(sys.argv) > 1 else 2
KMAX = int(sys.argv[2]) if len(sys.argv) > 2 else (4 if A == 2 else 1)
sys.argv = [sys.argv[0], str(A)]
import importlib.util  # noqa: E402
spec = importlib.util.spec_from_file_location("brl", HERE / "bond_rules_length_bound_probe.py")
brl = importlib.util.module_from_spec(spec)
spec.loader.exec_module(brl)
mp, bc = brl.mp, brl.bc
Q, H, ZERO, ONE = brl.Q, brl.H, brl.ZERO, brl.ONE
N, NV = brl.N, brl.NV


def main() -> int:
    wname = "binding-ceiling-q0" if A == 2 else f"binding-ceiling-q0-A{A}"
    wit = json.loads((HERE.parent / "binding_ceiling_q0" / f"{wname}.witness.json").read_text())
    L_meas = int(wit["parameters"]["L"])
    passing = wit["data"]["passing"]
    E0 = mp.mpf(wit["parameters"]["E0_tower_MeV"])
    x_word = [(s + 3 * a, i) for a in range(A) for (s, i) in bc.V(0) * 3]
    X = brl.op_blocks(x_word)
    trx = brl.trace_blocks(X)
    xnorm = max(brl.opnorm2(X[k]) for k in brl.STATES)
    Vb = {s: brl.op_blocks(bc.V(s)) for s in range(NV)}
    mu = {0: ONE}
    for k in range(1, KMAX + 1):
        best = ZERO
        for w in itertools.product(range(NV), repeat=k):
            for blk in brl.STATES:
                M = mp.eye(len(brl.STATES[blk]))
                for s in w:
                    M = Vb[s][blk] * M
                best = max(best, brl.opnorm2(M))
        mu[k] = best
        brl.log(f"mu_{k} = {mp.nstr(best, 15)}  (mu_k^(1/k) = {mp.nstr(best ** (ONE / k), 15)})")
    kbest = min(range(1, KMAX + 1), key=lambda k: mu[k] ** (ONE / k))
    beta = mu[kbest] ** (ONE / kbest)

    def R_L(L):
        return xnorm * mu[kbest] ** (L // kbest) * mu[L % kbest] / trx

    subsets = [J for r in range(A) for J in itertools.combinations(range(A - 1), r)]

    def count(L):
        return sum((-1) ** len(J) * (NV - 2 * len(J)) ** L for J in subsets)

    out = {}
    for name, t in {"h": H, "q*h": Q * H, "h/q": H / Q}.items():
        NT = mp.fsum(t ** p["length"] * mp.mpf(p["ratio"]) for p in passing)
        ZT = mp.fsum(t ** p["length"] for p in passing)
        rT = NT / ZT
        by_L = {}
        for L0 in range(1, L_meas + 1):
            ps = [p for p in passing if p["length"] <= L0]
            if ps:
                r0 = mp.fsum(t ** p["length"] * mp.mpf(p["ratio"]) for p in ps) / mp.fsum(t ** p["length"] for p in ps)
                by_L[str(L0)] = {"n_words": len(ps), "ratio": mp.nstr(r0, 15),
                                 "B_MeV_tower": mp.nstr(-E0 * mp.log(r0), 10) if r0 > 0 else None}
        geo = abs(t) * NV * beta
        row = {"t": mp.nstr(t, 20), "ratio_truncated": mp.nstr(rT, 20),
               "minus_ln_r": mp.nstr(-mp.log(rT), 15), "B_MeV_tower": mp.nstr(-E0 * mp.log(rT), 12),
               "geometric_factor": mp.nstr(geo, 15), "bound_available": geo < 1,
               "truncated_by_L": by_L}
        if geo < 1:
            # tails summed exactly as geometric series in closed form, per J and per residue
            Lmax_explicit = L_meas + 4000
            epsZ = mp.fsum(abs(t) ** L * count(L) for L in range(L_meas + 1, Lmax_explicit))
            epsN = mp.fsum(abs(t) ** L * count(L) * R_L(L) for L in range(L_meas + 1, Lmax_explicit))
            # remainder beyond Lmax_explicit: count(L) <= NV^L, R_L <= xnorm*beta^L*C/trx
            C = max(mu[j] / beta ** j for j in range(kbest))
            rem = xnorm * C / trx * geo ** Lmax_explicit / (1 - geo) + (abs(t) * NV) ** Lmax_explicit / (1 - abs(t) * NV)
            dr = (epsN + abs(rT) * epsZ + rem * (1 + abs(rT))) / ZT
            lo, hi = rT - dr, rT + dr
            row.update({"ratio_error_bound": mp.nstr(dr, 10),
                        "minus_ln_r_interval": [mp.nstr(-mp.log(hi), 12), mp.nstr(-mp.log(lo), 12) if lo > 0 else "unbounded"],
                        "B_MeV_interval": [mp.nstr(-E0 * mp.log(hi), 10), mp.nstr(-E0 * mp.log(lo), 10) if lo > 0 else "unbounded"]})
        out[name] = row
        brl.log(f"rule 3b t={name}: {row}")
    wb = (bc.WitnessBuilder(f"bond-rules-3b-passing-sum-A{A}", engine="mpmath")
          .set_description(
              "PROBE (bean qou-brng, brief C2 front E): rule (3b), weighted average of per-word trace ratios over the "
              "bond words that pass reading 3 individually, truncated at the measured length, with a proved "
              "norm/count bound on the unmeasured longer words where it is geometric. Per-word ratios from the "
              "committed ceiling witness. Weights are corpus quantities, none derived. Scorecard only.")
          .set_audit_only("docs/audits/2026-11-27-bond-rules-and-length-cutoff.md")
          .add_parameter("A", A).add_parameter("L_measured", L_meas).add_parameter("KMAX", KMAX)
          .add_data("mu", {str(k): mp.nstr(v, 20) for k, v in mu.items()})
          .add_data("beta_per_vertex_norm_growth", mp.nstr(beta, 20))
          .add_data("x_norm", mp.nstr(xnorm, 20))
          .add_data("rule3b", out))
    wb.add_assertion("bound_geometric_for_some_weight", computed=any(r["bound_available"] for r in out.values()),
                     expected=any(r["bound_available"] for r in out.values()), tolerance=0,
                     source="recorded, not required: A >= 3 has none")
    wb.save({"q0Anchor": "proton", "q0Value": mp.nstr(Q, 50),
             "q0AnchorReason": "q0 enters through cf.Q (committed y-lambda-at-q0 witness, proton pin)"})
    return 0


if __name__ == "__main__":
    sys.exit(main())
