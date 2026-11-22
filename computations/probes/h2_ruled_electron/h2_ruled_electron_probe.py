#!/usr/bin/env python3
"""h2_ruled_electron_probe.py — H2 with the ruled electron σ0σ1σ0 and photon-term bond letters.

Issue #8821. Recipe: PREREGISTRATION.md here (committed 8c6466a88 before this file).

Owner rulings used (docs/coordination/owner-rulings.md):
  * electron E = σ0σ1σ0 ∈ B3, closure the Hopf link (2026-11-21); the trefoil backup is not run;
  * photon γ = 1 + φ0σ0 + φ1σ1 + φ01·σ0σ1⁻¹, no virtual photons (2026-11-18/20);
  * two-term Lagrangian trace (2026-11-21).

Bond letters are the junction-absorbed terms of the ruled photon at windows s ∈ {4, 5}:
A = {σ4, σ5, σ6, V4, V5}, V_s = σ_s σ_{s+1}⁻¹; bond K = product of j ∈ {1, 2, 3} letters (155 words).
Each monomial is tested on its own, so no φ is chosen.

Reuses ../h2_gg_atom (and through it ../h2_one_rule) unchanged: mpmath 40 dps, convention D, proton pin,
reading 3 at every level 1..12. Trace ratio reported, never used to select. Nothing fitted or wired.

-- Ref: [manuscript] prop:ilp-covalent-bond; def:photon; issue #8821; PR #8743 (derived lepton insertion)
"""
from __future__ import annotations

import itertools
import json
import sys
from fractions import Fraction
from multiprocessing import Pool
from pathlib import Path

import mpmath as mp
mp.mp.dps = max(mp.mp.dps, 40)

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / "h2_gg_atom"))
import h2_gg_atom_probe as ga  # noqa: E402

base, kct, log, TOL, N = ga.base, ga.kct, ga.log, ga.TOL, ga.N
ONE, ZERO, H, Q, y = ga.ONE, ga.ZERO, base.H, base.Q, ga.y
from qou_substrate.witness import WitnessBuilder  # noqa: E402

ELECTRON = "Tw0_s0s1s0"   # σ0σ1σ0, the ruled electron


def sig(g):
    return [(ONE, ZERO, g)]


def V(s):
    return [(ONE, ZERO, s), (ONE, -H, s + 1)]


LETTERS = {"s4": sig(4), "s5": sig(5), "s6": sig(6), "V4": V(4), "V5": V(5)}
CROSS = {"s4": 1, "s5": 1, "s6": 1, "V4": 2, "V5": 2}


def bond_words():
    out = []
    for j in (1, 2, 3):
        for tup in itertools.product(LETTERS, repeat=j):
            out.append((".".join(tup), j, sum(CROSS[t] for t in tup), sum((LETTERS[t] for t in tup), [])))
    return out


def junction_perm(word):
    """Permutation of strands 4..7 induced by the word (letters σ_g, g in 4..6)."""
    p = list(range(4, 8))
    for _, _, g in word:
        i = g - 4
        p[i], p[i + 1] = p[i + 1], p[i]
    return p


def bonded_rows(m, atom2):
    """All 155 bonds plus the bare word, for nucleon V^m and atom-2 order `atom2`."""
    kct.proton_block = ga.vm(m)
    kct.ELECTRON = ELECTRON
    w1, _ = kct.atom("pe", False)
    w2, _ = kct.atom(atom2, False)
    x = w1 + kct.shift(w2, 6)
    prefix = {}
    for lam in ga.two_row(N):
        dim = kct.cols(list(lam))[1]
        I = [[ONE if i == j else ZERO for j in range(dim)] for i in range(dim)]
        prefix[lam] = kct.right_apply(I, x, list(lam))
    dx = {lam: [prefix[lam][i][i] for i in range(len(prefix[lam]))] for lam in prefix}
    lcx = ga.level_chars(dx, N, 1)
    trx = mp.fsum(y(l) * lcx[(N, l)] for l in ga.two_row(N))
    bare_fails = sorted({k for (k, mu), v in lcx.items() if v < -TOL})
    rows = []
    for name, j, cr, word in bond_words():
        d = base.diag_of(word, N, prefix)
        lc = ga.level_chars(d, N, 1)
        tr = mp.fsum(y(l) * lc[(N, l)] for l in ga.two_row(N))
        fails = sorted({k for (k, mu), v in lc.items() if v < -TOL})
        perm = junction_perm(word)
        rows.append({
            "K": name, "photons_j": j, "j_even": j % 2 == 0, "crossings": cr,
            "junction_perm": perm, "pure": perm == [4, 5, 6, 7],
            "reading3_every_level": not fails, "failing_levels": fails,
            "negative": [f"{k}:{mu}={mp.nstr(v, 8)}" for (k, mu), v in sorted(lc.items()) if v < -TOL][:6],
            "ratio": mp.nstr(tr / trx, 20),
            "chars": {f"{k}:{mu}": mp.nstr(v, 20) for (k, mu), v in sorted(lc.items())},
        })
    return {"m": m, "atom2": atom2, "tr_x": mp.nstr(trx, 30), "bare_every_level": not bare_fails,
            "bare_failing_levels": bare_fails,
            "bare_chars": {f"{k}:{mu}": mp.nstr(v, 20) for (k, mu), v in sorted(lcx.items())}, "rows": rows}


def _job(args):
    m, atom2 = args
    r = bonded_rows(m, atom2)
    npass = sum(1 for row in r["rows"] if row["reading3_every_level"])
    log(f"done V^{m} atom2={atom2}: bare pass={r['bare_every_level']}, {npass}/155 bonds pass")
    return r


# ── two-term insertion (PR #8743 derived form), exact on every basis state ─────────────────────────
def insertion_values(colours):
    """{m: set of values} of Σ_{a<b} Q_aQ_b + (2/3) Σ_ℓ Q_ℓ² and of pairs-only Σ_{a<b} Q_aQ_b."""
    y_off = {"quark": Fraction(1, 6), "lepton": Fraction(-1, 2)}
    full, pairs = {}, {}
    for b in itertools.product((0, 1), repeat=len(colours)):
        t = [Fraction(1, 2) if x == 0 else Fraction(-1, 2) for x in b]
        Qs = [ti + y_off[c] for ti, c in zip(t, colours)]
        tot = sum(Qs)
        pr = (tot * tot - sum(qq * qq for qq in Qs)) / 2
        ins = pr + Fraction(2, 3) * sum(qq * qq for qq, c in zip(Qs, colours) if c == "lepton")
        mm = sum(1 if x == 0 else -1 for x in b)
        full.setdefault(mm, set()).add(ins)
        pairs.setdefault(mm, set()).add(pr)
    return full, pairs


def colours_for(atom2):
    a1 = ["quark"] * 3 + ["lepton"] * 3
    a2 = a1 if atom2 == "pe" else ["lepton"] * 3 + ["quark"] * 3
    return a1 + a2


def main() -> int:
    checks = []

    def check(name, ok, src):
        checks.append((name, bool(ok), src))
        log(f"[{'PASS' if ok else 'FAIL'}] {name} — {src}")

    # E1 + the electron alone, levels 1..3
    E = kct.ELECTRONS[ELECTRON](0)
    lcE = ga.level_chars(base.diag_of(E, 3), 3, 1)
    check("E1_chi3_E_is_q3", abs(lcE[(3, (3,))] - Q ** 3) < TOL, f"chi_(3)(σ0σ1σ0) = {mp.nstr(lcE[(3, (3,))], 15)}")
    e_fails = sorted({k for (k, mu), v in lcE.items() if v < -TOL})
    electron_alone = {"reading3_every_level": not e_fails, "failing_levels": e_fails,
                      "chars": {f"{k}:{mu}": mp.nstr(v, 20) for (k, mu), v in sorted(lcE.items())}}
    log(f"electron alone: every-level={not e_fails} " + ", ".join(f"{k}:{mu}={mp.nstr(v, 10)}" for (k, mu), v in sorted(lcE.items())))

    # E2: the derived insertion is constant on every weight space (both layouts); pairs-only is not
    e2 = {}
    ok2 = True
    for atom2 in ("pe", "ep"):
        full, pairs = insertion_values(colours_for(atom2))
        full_const = all(len(v) == 1 for v in full.values())
        pairs_const = all(len(v) == 1 for v in pairs.values())
        ok2 &= full_const and not pairs_const
        e2[atom2] = {"derived_constant_on_every_W_m": full_const, "pairs_only_constant_on_every_W_m": pairs_const,
                     "derived_value_by_m": {str(k): str(next(iter(v))) for k, v in sorted(full.items())},
                     "pairs_only_distinct_values_by_m": {str(k): len(v) for k, v in sorted(pairs.items())}}
    check("E2_derived_insertion_scalar_on_weight_spaces", ok2,
          "derived (#8743) constant on all W_m, both layouts; pairs-only not constant (the check has teeth)")

    jobs = [(m, a) for m in (3, 6) for a in ("pe", "ep")]
    with Pool(len(jobs)) as pool:
        res = pool.map(_job, jobs)
    results = {f"nucleon=V^{r['m']},atom2={r['atom2']}": r for r in res}

    # E0: V_s^k rows reproduce h2_gg_atom (nucleon V^3, Tw0 electron)
    old = json.loads((HERE.parent / "h2_gg_atom" / "h2-gg-atom.witness.json").read_text())["results"]["V^3"]
    worst, matched = mp.mpf(0), 0
    for atom2 in ("pe", "ep"):
        orows = old[f"electron={ELECTRON},atom2={atom2}"]["rows"]
        mine = {r["K"]: r for r in results[f"nucleon=V^3,atom2={atom2}"]["rows"]}
        for ro in orows:
            if ro["K"] == "none":
                continue
            k = int(ro["K"].split("^")[1])
            rn = mine[".".join([f"V{ro['site']}"] * k)]
            for key, v in ro["chars"].items():
                worst = max(worst, abs(mp.mpf(v) - mp.mpf(rn["chars"][key])))
            matched += 1
    check("E0_V_subfamily_reproduces_h2_gg_atom", worst < mp.mpf("1e-18") and matched == 12,
          f"{matched} rows, max diff {mp.nstr(worst, 5)}")

    summary = {}
    for tag, r in results.items():
        passing = [row for row in r["rows"] if row["reading3_every_level"]]
        summary[tag] = {
            "bare_every_level": r["bare_every_level"],
            "n_pass": len(passing),
            "passing": [row["K"] for row in passing],
            "min_j": min((row["photons_j"] for row in passing), default=None),
            "min_crossings": min((row["crossings"] for row in passing), default=None),
            "all_passing_pure": all(row["pure"] for row in passing),
            "pure_words_failing": [row["K"] for row in r["rows"] if row["pure"] and not row["reading3_every_level"]],
        }
        log(f"{tag}: {summary[tag]}")

    ok_all = all(ok for _, ok, _ in checks)
    wb = WitnessBuilder("h2-ruled-electron", engine="mpmath", output_dir=HERE)
    for name, ok, src in checks:
        wb.add_assertion(name, computed="1" if ok else "0", expected="1", source=src)
    out = wb.save({
        "q0Anchor": "proton",
        "q0AnchorReason": "q0 enters through cf.Q (committed y-lambda-at-q0 witness, proton pin)",
        "description": "PROBE (issue #8821): H2 with the ruled electron σ0σ1σ0 (owner 2026-11-21), nucleon V^m (m=3,6), "
                       "no p-e or junction letter, bond K = product of 1..3 junction-absorbed terms of the ruled photon "
                       "{σ4,σ5,σ6,V4,V5}; reading 3 at every level 1..12, convention D, proton pin. Two-term: derived "
                       "lepton insertion of #8743 checked scalar on every weight space. Pre-registered. Nothing fitted or wired.",
        "weight_family": "markov_y_lambda_convention_D",
        "electron_alone": electron_alone,
        "two_term_insertion": e2,
        "summary": summary,
        "results": results,
    })
    log(f"witness: {out}")
    log(f"{sum(1 for _, ok, _ in checks if ok)}/{len(checks)} checks pass")
    return 0 if ok_all else 1


if __name__ == "__main__":
    sys.exit(main())
