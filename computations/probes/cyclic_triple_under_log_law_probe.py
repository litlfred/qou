#!/usr/bin/env python3
"""
Probe — the cyclic-triple word class re-read under the binding law that #6611
leaves standing.

`cyclic_triple_bond_cross_term_probe.py` (2026-09-04, same day) measured the
one cross-term-bearing non-monotone class on the production 2H–4He words and
converted it to MeV with `B = Q_beta·(tr_free − tr_atom)`. Hours later #6611
refuted that linear law at every scale (p5–p95 spread 1592× over 2548 AME
nuclides) and derived its replacement, already in the repo as
`binding_log_free_energy.py`:

    B = E_0 · log( tr_M(free) / tr_M(atom) ),   E_0 = m_e / (q0 (q0 − 1))  (derived, no fit)

The earlier probe's §4.3 deferred exactly this question ("under a log law the
same reorder would read as 2–4 nats per bond"). This probe answers it with the
same closed forms — every trace here is the product-of-run-traces form that the
earlier probe validated byte-for-byte against the production kernel — so 4He is
included at no cost.

What the log law changes structurally: a monotone word's log-trace is a SUM of
run log-traces, so a cyclic triple at bond k shifts B by

    ΔB_k = E_0 · ln( f_prod,k / f_cyc,k )

where f_prod,k = tr(L1L2L3L4)·tr(B) is the production block and
f_cyc,k = tr(L1L2L3L4)·tr(B²) + b(L1L2L3)·(z²−hz−1) the cyclic block — a
per-bond number that depends only on the bond's species pair and the adjacent
nucleon, NOT on A. The class is therefore EXTENSIVE under the log law (checked:
equal keys give equal shifts across nuclei to 50 dps). The question is then
purely the magnitude and sign against the log-law residuals.

Nothing wired, nothing fitted. mpmath 50 dps; no float64.
"""
from __future__ import annotations

import os
import sys

import mpmath as mp

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
import _path_bridge  # noqa: E402, F401

import cyclic_triple_bond_cross_term_probe as ct  # noqa: E402  (same directory)
from binding_log_free_energy import M_E_MEV  # noqa: E402
from mass_at_3A_proper import atom_braid_word_3A  # noqa: E402
from tr_m_atom_via_transfer import tr_m_atom_zn  # noqa: E402
from codata_constants import ame_binding_mev  # noqa: E402

mp.mp.dps = 50
Q, H, Z_D, DEFECT, TOL = ct.Q, ct.H, ct.Z_D, ct.DEFECT, ct.TOL
M_E = mp.mpf(str(M_E_MEV))
import sys as _s0, pathlib as _p0; _s0.path.insert(0, str(next(p for p in _p0.Path(__file__).resolve().parents if p.name == "computations") / "qbeta")); import qbeta_e0 as _qbeta_e0  # noqa: E401,E402,E702 (#8590)
E0 = _qbeta_e0.order_zero_scaled(M_E, Q)  # order-zero E_0, routed (owner ruling 2026-11-20, #8590)


def species(Z: int, N: int):
    """nucleon k's species in the production chain order (Z protons then N neutrons)."""
    return ["p"] * Z + ["n"] * N


def block_factors(word, i):
    """(f_prod, f_hopf, f_cyc) for the bond letter at index i — the per-bond block traces
    of the left cyclic-triple variant, from the closed forms of the earlier probe."""
    runs = ct.runs_of(word)
    g_run = word[i - 1][2]
    Ls_run = [L for g, Ls in runs if g == g_run for L in Ls]
    B = ct.letter(word[i][0], word[i][1])
    tr_run = ct.aff_tr(ct.aff_prod(Ls_run))
    f_prod = tr_run * ct.aff_tr(B)
    f_hopf = tr_run * ct.aff_tr(ct.aff_mul(B, B))
    f_cyc = f_hopf + ct.aff_prod(Ls_run[:-1])[1] * DEFECT
    return f_prod, f_hopf, f_cyc


def main() -> int:
    checks: list[tuple[str, bool]] = []
    print(f"  q0 = {mp.nstr(Q, 20)}   E_0 = m_e/(q0(q0−1)) = {mp.nstr(E0, 12)} MeV   "
          f"z²−hz−1 = {mp.nstr(DEFECT, 12)}")
    print("  law (#6611): B = E_0 · ln(tr_free / tr_atom)\n")
    shifts_by_key: dict[tuple, list] = {}
    rows = []
    for name, Z, N in ct.NUCLEI:
        A = Z + N
        W = atom_braid_word_3A(Z, N)
        W_free = atom_braid_word_3A(Z, N, include_inter=False)
        tr_atom = ct.tr_monotone_closed(W)
        tr_free = ct.tr_monotone_closed(W_free)
        ta, tf, _, _ = tr_m_atom_zn(Z, N)
        checks.append((f"{name}: closed-form traces = production tr_m_atom_zn (atom, free)",
                       abs(tr_atom - ta) < TOL and abs(tr_free - tf) < TOL))
        B_log = E0 * mp.log(tr_free / tr_atom)
        B_ame = ame_binding_mev(Z, A)
        resid = B_ame - B_log
        sp = species(Z, N)
        per_bond = []
        total_cyc = mp.mpf(0)
        total_hopf = mp.mpf(0)
        for k, i in enumerate(ct.bond_positions(W, A)):
            f_prod, f_hopf, f_cyc = block_factors(W, i)
            checks.append((f"{name} bond {k}: cyclic block < production block (extra binding)",
                           f_cyc < f_prod))
            dB_hopf = E0 * mp.log(f_prod / f_hopf)      # doubling the bond alone
            dB_cyc = E0 * mp.log(f_prod / f_cyc)        # cyclic triple vs production
            total_cyc += dB_cyc
            total_hopf += dB_hopf
            key = (sp[k], sp[k + 1])
            shifts_by_key.setdefault(key, []).append((name, k, dB_cyc))
            per_bond.append((k, key, f_prod, f_cyc, dB_hopf, dB_cyc))
        rows.append((name, A, B_log, B_ame, resid, total_hopf, total_cyc))
        print(f"  ── {name}   tr_atom = {mp.nstr(tr_atom, 12)}   tr_free = {mp.nstr(tr_free, 12)}")
        print(f"     B_log = {mp.nstr(B_log, 8)} MeV   B_AME = {mp.nstr(B_ame, 8)}   "
              f"residual (AME − log) = {mp.nstr(resid, 8)} MeV")
        for k, key, f_prod, f_cyc, dB_hopf, dB_cyc in per_bond:
            print(f"     bond {k} {key[0]}–{key[1]}: block prod = {mp.nstr(f_prod, 10)}   "
                  f"cyclic = {mp.nstr(f_cyc, 10)}   ΔB(double bond) = {mp.nstr(dB_hopf, 8)}   "
                  f"ΔB(cyclic triple) = {mp.nstr(dB_cyc, 8)} MeV  ({mp.nstr(mp.log(f_prod / f_cyc), 6)} nats)")
        print(f"     all bonds cyclic: ΣΔB = {mp.nstr(total_cyc, 8)} MeV   vs residual {mp.nstr(resid, 8)}"
              f"   → B_cyc = {mp.nstr(B_log + total_cyc, 8)} MeV  ({mp.nstr((B_log + total_cyc) / B_ame, 6)} × AME)\n")

    # extensivity: the same (species_k, species_{k+1}) key gives the same per-bond shift in every nucleus
    for key, lst in shifts_by_key.items():
        vals = [v for _, _, v in lst]
        same = all(abs(v - vals[0]) < TOL for v in vals)
        where = ", ".join(f"{n}:b{k}" for n, k, _ in lst)
        checks.append((f"extensive under the log law: bond key {key[0]}–{key[1]} gives one shift "
                       f"({mp.nstr(vals[0], 8)} MeV) across [{where}]", same))

    # magnitude verdict, stated as checks so it is machine-readable
    for name, A, B_log, B_ame, resid, total_hopf, total_cyc in rows:
        checks.append((f"{name}: |ΣΔB(cyclic)| exceeds |residual| (class over-shoots under the log law)",
                       abs(total_cyc) > abs(resid)))
    checks.append(("2H: log-law production already over-binds (residual < 0), and the cyclic triple adds binding",
                   rows[0][4] < 0 and rows[0][6] > 0))

    ok = 0
    print()
    for label, passed in checks:
        print(f"  [{'PASS' if passed else 'FAIL'}] {label}")
        ok += bool(passed)
    print(f"\n  {ok}/{len(checks)} checks passed")
    return 0 if ok == len(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
