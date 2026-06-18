"""Channel-level audit of the brane-tower per-generator argument |V̂_i^full|.

Context
-------
PR #2467 pinned the physical brane-tower variable as ``z_i = |V̂_i^full|``
(the additive Wedderburn traced volume per generator) and showed the Φ_q
production wire is blocked. It took |V̂_i^full| as given. This probe answers
the next-level question — *why the FULL (regular-representation) trace and not
the genuine Jones–Markov trace?* — by decomposing the per-generator volume
into its three H_3 irrep channels and recording two structural facts that the
physical-z pin glossed:

  1. The genuine localized Jones–Markov trace ``Vol_q^({i})`` equals the
     ``std`` channel ``z·a_i + b_i`` (`def:algebraic-quantum-volume`), and for
     the proton σ₀ it is ``1.146 > q₀`` — so the *Jones–Markov* per-generator
     argument is exactly the one that DIVERGES in the dilog tower.

  2. The bounded ``full`` argument is the trace on the **regular
     representation** (Wedderburn–Artin weights ``w_λ = d_λ²/|S_3|``), which is
     categorically forced by the mass being the trace of a left-multiplication
     endomorphism ``L_{α_ϱ}`` (`def:hecke-mass-element`). It is NOT the
     Jones–Markov trace: ``∏ V̂_i^std = tr_M`` exactly, but ``∏ V̂_i^full`` is
     ~10% off — the descended term `prop:mass-endomorphism-tower` labels "the
     base-level Markov trace" is computed in the regular-rep convention, a
     trace-convention conflation worth reconciling.

It also records a weight-convention discrepancy: `atom-mass-full-hecke.md`
states the *classical* weights ``d_λ²/|S_3|`` while the production code
(`terms_2_3_atom_per_gen_mpfr_50dps.py`) uses the *q-deformed*
``(dim_q λ)²/[3]_q!``.

DISCIPLINE (CLAUDE.md production-vs-exploratory): this is a documentation /
consistency audit, not a production rewire. It changes no mass table. The
headline m_p/m_n/m_e dashboards use the Borromean vol-density form, NOT this
tower; the binding-B and Hecke-path chains are the consumers affected by the
channel choice. Cross-checks assert the *structural facts* (std regresses,
full bounded, full ≠ Jones–Markov) so a correct run is allPassed=true.

Self-contained (mpmath only) — replicates the proton/neutron channel
recurrence from `terms_2_3_atom_per_gen_mpfr_50dps.atom_per_generator_volumes_mpfr`.
"""
from __future__ import annotations

import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path

import mpmath as mp

mp.mp.dps = 50

# q₀ (proton-pinned, 50 dps) — same literal as zhabiro_physical_z_pin.py.
Q0 = mp.mpf("1.1099785955541805752815940796095093779932822799587")
QI = 1 / Q0
H = Q0 - QI
ZM = 1 / (mp.sqrt(Q0) + mp.sqrt(QI))  # Markov parameter z = 1/(q^½+q^-½)


def nucleon_chains(quarks: tuple[str, str, str]) -> tuple[list, list]:
    """Per-generator (c, d) crossing chains for one nucleon.

    Mirrors terms_2_3_atom_per_gen_mpfr_50dps._nucleon_gen_chains_mpfr.
    """
    g0 = [(mp.mpf(1), mp.mpf(0))] * 3          # B₃ confinement, gen 0
    g1 = [(mp.mpf(1), -H)] * 3                 # B₃ confinement, gen 1
    for i, j, gen in [(0, 1, 0), (0, 2, 0), (1, 2, 1)]:
        a, b = quarks[i], quarks[j]
        if a == b == "u":
            cd = (mp.mpf(1), mp.mpf(0))
        elif a == b == "d":
            cd = (mp.mpf(1), -H)
        else:
            cd = (mp.mpf(1), -H / 2)
        (g0 if gen == 0 else g1).append(cd)
    g0 += [(mp.mpf(1), mp.mpf(0))] * 2         # gluon self-coupling
    return g0, g1


def channels(chain: list) -> dict[str, mp.mpf]:
    """std (2×2 transfer trace), sym (trivial), alt (sign), per the Hecke
    eigenvalues (σ−q)(σ+q⁻¹)=0."""
    a, b = mp.mpf(0), mp.mpf(1)
    sp, ap = mp.mpf(1), mp.mpf(1)
    for c, d in chain:
        a, b = a * c * H + a * d + b * c, a * c + b * d
        sp *= c * Q0 + d         # trivial rep eigenvalue +q
        ap *= -c * QI + d        # sign rep eigenvalue −q⁻¹
    return {"std": ZM * a + b, "sym": sp, "alt": ap}


def q_int(n: int) -> mp.mpf:
    return (Q0**n - QI**n) / (Q0 - QI)


def weights_q_deformed() -> tuple[mp.mpf, mp.mpf, mp.mpf]:
    nf3 = q_int(1) * q_int(2) * q_int(3)
    ws, wd, wa = mp.mpf(1) / nf3, q_int(2) ** 2 / nf3, mp.mpf(1) / nf3
    t = ws + wd + wa
    return ws / t, wd / t, wa / t


def weights_classical() -> tuple[mp.mpf, mp.mpf, mp.mpf]:
    # d_sym=1, d_std=2, d_alt=1; |S_3| = 6
    return mp.mpf(1) / 6, mp.mpf(4) / 6, mp.mpf(1) / 6


def full_of(ch: dict, w: tuple) -> mp.mpf:
    ws, wd, wa = w
    return ws * ch["sym"] + wd * ch["std"] + wa * ch["alt"]


def neg_li2q_neg(z: mp.mpf, terms: int = 100000) -> mp.mpf:
    """Production tower term −Li₂^q(−z) = Σ (−1)^{n+1} z^n/(n·[n]_q). +inf if |z|≥q₀."""
    if abs(z) >= Q0:
        return mp.inf
    # Maintain q^n, q^-n iteratively (O(terms) multiplications) instead of
    # calling q_int(n) — which re-does Q0**n / QI**n each step, O(terms)
    # arbitrary-precision exponentiations (Gemini review, PR #2481).
    total, zn, sign = mp.mpf(0), mp.mpf(1), 1
    q0_n, qi_n, denom_factor = mp.mpf(1), mp.mpf(1), Q0 - QI
    for n in range(1, terms + 1):
        zn *= z
        q0_n *= Q0
        qi_n *= QI
        term = (sign * zn * denom_factor) / (n * (q0_n - qi_n))  # 1/[n]_q
        total += term
        sign = -sign
        if abs(term) < mp.mpf(10) ** (-mp.mp.dps - 5):
            break
    return total


def main() -> None:
    self_path = Path(__file__).resolve()
    script_hash = hashlib.sha256(self_path.read_bytes()).hexdigest()[:12]
    wq = weights_q_deformed()
    wc = weights_classical()

    print(f"q₀ = {mp.nstr(Q0, 18)}   z_markov = {mp.nstr(ZM, 12)}")
    print(f"weights q-deformed (sym,std,alt) = "
          f"({mp.nstr(wq[0],8)}, {mp.nstr(wq[1],8)}, {mp.nstr(wq[2],8)})")
    print(f"weights classical  (sym,std,alt) = "
          f"({mp.nstr(wc[0],8)}, {mp.nstr(wc[1],8)}, {mp.nstr(wc[2],8)})")
    print()

    out: dict[str, dict] = {}
    for nuc, quarks in [("proton", ("u", "u", "d")), ("neutron", ("u", "d", "d"))]:
        g0, g1 = nucleon_chains(quarks)
        per_gen = []
        for gi, chain in enumerate((g0, g1)):
            ch = channels(chain)
            full_q = full_of(ch, wq)
            full_c = full_of(ch, wc)
            per_gen.append({
                "gen": gi,
                "std": ch["std"], "sym": ch["sym"], "alt": ch["alt"],
                "full_qdef": full_q, "full_classical": full_c,
            })
        prod_std = per_gen[0]["std"] * per_gen[1]["std"]
        prod_full = per_gen[0]["full_qdef"] * per_gen[1]["full_qdef"]
        # T2 single-generator tower under each per-generator argument
        t2_full = sum(neg_li2q_neg(abs(g["full_qdef"])) for g in per_gen)
        t2_std = [neg_li2q_neg(abs(g["std"])) for g in per_gen]
        print(f"{nuc}:")
        for g in per_gen:
            print(f"  gen{g['gen']}: std={mp.nstr(g['std'],8):>12} "
                  f"sym={mp.nstr(g['sym'],8):>12} alt={mp.nstr(g['alt'],8):>12} "
                  f"full={mp.nstr(g['full_qdef'],8):>12}")
        print(f"  ∏std (=Jones–Markov tr_M) = {mp.nstr(abs(prod_std),10)}   "
              f"∏full (regular-rep) = {mp.nstr(abs(prod_full),10)}   "
              f"ratio = {mp.nstr(abs(prod_full)/abs(prod_std),8)}")
        print(f"  T2 with full = {mp.nstr(t2_full,8)}   "
              f"T2 with std gen0 = {('+inf' if mp.isinf(t2_std[0]) else mp.nstr(t2_std[0],8))}")
        print()
        out[nuc] = {
            "per_gen": [{k: mp.nstr(v, 30) if isinstance(v, mp.mpf) else v
                         for k, v in g.items()} for g in per_gen],
            "prod_std_jones_markov": mp.nstr(abs(prod_std), 30),
            "prod_full_regular_rep": mp.nstr(abs(prod_full), 30),
            "prod_full_over_std_ratio": mp.nstr(abs(prod_full) / abs(prod_std), 18),
            "t2_full_finite": mp.nstr(t2_full, 18),
            "t2_std_gen0": "inf" if mp.isinf(t2_std[0]) else mp.nstr(t2_std[0], 18),
        }

    p = out["proton"]
    p0 = p["per_gen"][0]
    cross = {
        # std channel g0 = the value I recompute = the witnessed std value
        "proton_std_g0_matches_witness_1_1461": bool(
            abs(mp.mpf(p0["std"]) - mp.mpf("1.1461015210575879")) < mp.mpf("1e-9")
        ),
        # the genuine Jones–Markov per-gen arg (std) is PAST the dilog radius
        "jones_markov_std_g0_exceeds_q0": bool(mp.mpf(p0["std"]) > Q0),
        # the regular-rep full arg is bounded < 1
        "regular_rep_full_g0_below_one": bool(mp.mpf(p0["full_qdef"]) < 1),
        # ∏full (regular-rep) ≠ ∏std (Jones–Markov tr_M): the ~10% conflation
        "prod_full_differs_from_jones_markov_trM": bool(
            abs(mp.mpf(p["prod_full_over_std_ratio"]) - 1) > mp.mpf("0.05")
        ),
        # weight conventions differ (classical vs q-deformed)
        "weight_conventions_differ": bool(
            abs(weights_q_deformed()[1] - weights_classical()[1]) > mp.mpf("1e-6")
        ),
        # T2 is finite with full, divergent with std
        "t2_finite_with_full_divergent_with_std": bool(
            p["t2_std_gen0"] == "inf" and mp.mpf(p["t2_full_finite"]) < 5
        ),
    }
    print("cross_checks:", json.dumps(cross, indent=2))

    witness = {
        "engine": "mpmath",
        "engineVersion": f"mpmath {mp.__version__}",
        "computedAt": datetime.now(timezone.utc).isoformat(),
        "computation": "brane-tower-full-channel-trace-audit",
        "scriptFile": self_path.name,
        "scriptHash": script_hash,
        "contentBlock": "prop:mass-endomorphism-tower",
        "description": (
            "Channel-level audit of the brane-tower per-generator argument. "
            "Decomposes |V̂_i| into std/sym/alt H_3 channels and records: (1) the "
            "genuine localized Jones–Markov trace Vol_q^({i}) = std channel = "
            "1.146 > q₀ for proton σ₀ (the divergent one); (2) the bounded |V̂_i^full| "
            "is the REGULAR-representation trace (Wedderburn–Artin w_λ=d_λ²/|S_3|), "
            "forced by the mass being a left-mult endomorphism trace "
            "(def:hecke-mass-element); (3) ∏std = Jones–Markov tr_M exactly while "
            "∏full is ~10% off — the descended term labeled 'base-level Markov "
            "trace' is computed in the regular-rep convention; (4) a weight-convention "
            "discrepancy (classical d_λ²/|S_3| in atom-mass-full-hecke.md vs q-deformed "
            "(dim_q)²/[3]_q! in the production code). Documentation/consistency audit "
            "only — no mass table is rewired."
        ),
        "parameters": {"q_0_50dps": mp.nstr(Q0, 50),
                       "weights_q_deformed": [mp.nstr(w, 30) for w in wq],
                       "weights_classical": [mp.nstr(w, 30) for w in wc]},
        "data": {"nucleons": out},
        "cross_checks": cross,
        "allPassed": all(cross.values()),
        "provenance": [
            "terms-2-3-atom-per-gen-mpfr-50dps.witness.json",
            "zhabiro-physical-z-pin.witness.json (PR #2467)",
            "content/quantum-observable-universe/mass-theory/hecke-mass-element.md",
            "content/quantum-observable-universe/observations/atom-mass-full-hecke.md",
        ],
    }
    out_path = self_path.parent.parent / "brane-tower-full-channel-trace-audit.witness.json"
    out_path.write_text(json.dumps(witness, indent=2) + "\n")
    print(f"\nwrote {out_path}")


if __name__ == "__main__":
    main()
