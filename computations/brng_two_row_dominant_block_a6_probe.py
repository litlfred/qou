#!/usr/bin/env python3
# polynomial_q_not_applicable: numerical evaluation at q = q_0 only.
"""A >= 6: the trace's dominant block is TWO-ROW -- typed decomposition of its
log-weight over the bond set, on 6Li / 7Li (bean `qou-vn6h`).

The A >= 6 remainder of `qou-brng` after `qou-m8f3` (PR #7200). That probe
proved that for every typed cluster with A <= 4 the dominant summand of

    tr_M(beta_A) = sum_{lambda |- 3A} y_lambda . chi^lambda(beta_A)

is the ONE-ROW block [3A], whose character is a ring homomorphism, so its
log-weight L(A) = log|y_{lambda*} chi^{lambda*}(beta_A)| is EXACTLY chain-edge
additive over the pp / pn / nn interfaces and carries no connected many-body
term (scope (b) at A <= 4, invariant: one-row dominance + letter product). It
STOPPED at 6Li, where the dominant block is the two-row [15,3]: a two-row
character is the trace of a representation of dimension > 1, it is NOT a ring
homomorphism, and a priori it need not be letter-multiplicative. So at A >= 6
the log-weight of the dominant summand could carry a connected term. This probe
measures it.

*** WHAT IS COMPUTED ***

For every typed cluster (Z, N) with 1 <= Z + N <= 7 (35 clusters; A = 7 is
n = 21, p(21) = 792, ~12 s per word on the window transfer):

  1. the live atom word `atom_braid_word_3A(Z, N)` (alternating core, the
     2026-09-05 ruling, bean `qou-hu1f`) and its free word; every chi^lambda
     via `chi_general_word.chi_all_lambda_any`; y_lambda via
     `wedderburn_jones_markov.y_lambda_at(n, q0)`; proton pin `Q_50_DIGIT_STR`,
     convention D, z = q^3/(q^2+1);
  2. the dominant summand AS THE TRACE DEFINES IT, argmax |y chi|, with its
     margin (runner-up / dominant) and its row count. No choice is made;
  3. L_atom, L_free, dL = L_free - L_atom (own argmax each side),
     dL_sameblock (free word in the atom's own block, y cancels) and the
     free-side argmax switch, exactly as in #7200;
  4. FIXED-n CHAIN-EDGE ADDITIVITY, PER BLOCK. At fixed A the A + 1 typed
     words (Z, A - Z) live on the same n = 3A strands and share every block.
     For each lambda |- n the same-block quantity
         X_lambda(Z, N) = log|chi^lambda(atom_{Z,N})| - log|chi^lambda(free_{Z,N})|
     is tested against the chain law
         X = (Z - 1) L_pp + [Z >= 1 and N >= 1] L_pn + (N - 1) L_nn
     with L_pp := X(A,0)/(A-1), L_nn := X(0,A)/(A-1), L_pn := X(A-1,1) -
     (A-2) L_pp, i.e. three constants DETERMINED by three words and the other
     A - 2 words PREDICTED. No parameter is fitted to the residual; the
     residual is the measurement. For the one-row block it is 0 exactly (the
     #7200 letter product); for a two-row block it is the question;
  5. THE TYPED BOND-SET DECOMPOSITION at 6Li and 7Li, inside the dominant
     block. The atom word has A - 1 interface letters, one per chain edge,
     each a single Hecke letter c.sigma_g + d.1 at generator 3k+2. Deleting a
     subset of them gives a word with exactly that interface set S. With
         F_lambda(S) = log|chi^lambda(word with interface set S)|
     the Moebius inversion over subsets,
         c_lambda(S) = sum_{T subset S} (-1)^{|S - T|} F_lambda(T),
     is the connected (Ursell) cumulant of the block's log-weight over the
     typed bond set: c({e}) is the per-edge term, c(S) for |S| >= 2 is the
     connected many-edge term. Letter-multiplicativity of the character over
     the interfaces is EXACTLY c(S) = 0 for all |S| >= 2. All 2^5 = 32 subsets
     at 6Li; at 7Li the 64 subsets are 12 minutes and the pairs already decide
     the question, so 7Li runs singletons, all 15 pairs and the full set.
     Reported for the dominant two-row block, the one-row block (control:
     zero), and the full trace (control: the bond rule, zero);
  6. the typed Ursell inversion (complete-graph, per composition (z, n)) of
     dL, dL_sameblock, the switch, log y_{lambda*} and the full-trace log
     ratio to order 7; the corpus uniform-e_2 convention at A <= 4 (where it
     is defined); and per-cluster totals E_0 . dL against AME2020 for every
     cluster the table lists, with the particle-unbound ones flagged.

*** A = 5 ***

5He and 5Li are unbound to nucleon emission (resonances). They are NOT
skipped: (2,3) and (3,2) -- and the four other A = 5 compositions -- are
sub-clusters of every A >= 6 cumulant and enter the inversion like any other.
Their AME2020 total binding energies (B > 0; the instability is against
4He + n / 4He + p, not against free nucleons) are quoted as targets with the
flag `particle_unbound`, as are 6Be and 7He.

*** SCALE ***

E_0 = m_e / (q_0 (q_0 - 1)) from `mass_binding_dashboard._constants()`, the
constant the production dashboard multiplies ln(tr_free/tr_atom) by. No new
scale. Every sign, ratio and residual below is scale-free.

*** WHAT IS NOT DONE ***

Nothing is wired. No route is selected by residual. AME enters only as a
target. A positive connected term with the wrong magnitude is REPORTED.

Precision: mpmath at 60 dps; AME as Decimal from the vendored table with
parse_float=str; display through mp.nstr; wall times are printed for the
progress log and never serialised. No float arithmetic.
"""

from __future__ import annotations

import itertools
import json
import subprocess
import sys
import time
from decimal import Decimal
from pathlib import Path

import mpmath as mp

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(ROOT / "tools" / "qou-substrate" / "python"))

import _path_bridge  # noqa: E402, F401
from qou_substrate.witness import WitnessBuilder  # noqa: E402
from chi_general_word import chi_all_lambda_any  # noqa: E402
from mass_at_3A_proper import atom_braid_word_3A  # noqa: E402
from wedderburn_jones_markov import y_lambda_at  # noqa: E402
from q_parameter import Q_MP, Q_50_DIGIT_STR  # noqa: E402
from mass_binding_dashboard import _constants  # noqa: E402

DPS = 60
mp.mp.dps = DPS

M_E, Q0, E0 = _constants()          # all mpf; E0 = m_e / (q0 (q0 - 1))
assert mp.nstr(Q0, 40) == mp.nstr(mp.mpf(Q_50_DIGIT_STR), 40)
Z_D = Q0 ** 3 / (Q0 ** 2 + 1)       # convention D Markov parameter

_AME_PATH = ROOT / "qou-mass" / "src" / "qou_mass" / "data" / "ame2020.json"
A_MAX = 7

#: AME2020 comparison set: every (Z, N) with 2 <= A <= 7 the vendored table
#: lists as a real nuclide; flag = particle-unbound (resonance).
AME_SET: dict[tuple[int, int], tuple[str, bool]] = {
    (1, 1): ("2H", False), (1, 2): ("3H", False), (2, 1): ("3He", False),
    (2, 2): ("4He", False),
    (2, 3): ("5He", True), (3, 2): ("5Li", True),
    (2, 4): ("6He", False), (3, 3): ("6Li", False), (4, 2): ("6Be", True),
    (2, 5): ("7He", True), (3, 4): ("7Li", False), (4, 3): ("7Be", False),
}
#: the committed 6Li per-partition cache the live recompute is checked against
CACHE_6LI = "chi-lithium-6-h18-at-q0-50dps-matrix-m.witness.json"


def _head_sha() -> str:
    try:
        return subprocess.run(["git", "rev-parse", "HEAD"], cwd=ROOT,
                              capture_output=True, text=True,
                              check=True).stdout.strip()
    except Exception:
        return "unknown"


def ame_binding_mev(Z: int, A: int) -> mp.mpf:
    raw = json.loads(_AME_PATH.read_text(), parse_float=str)
    for e in raw["entries"]:
        if int(e["Z"]) == Z and int(e["A"]) == A:
            return mp.mpf(str(Decimal(e["binding_energy_per_A_keV"]) * A
                              / Decimal(1000)))
    raise KeyError(f"Z={Z} A={A} not in the vendored AME2020 table")


def _s(x, d: int = 12) -> str:
    return mp.nstr(x, d)


def _lab(Z: int, N: int) -> str:
    return "p" * Z + "n" * N if Z + N <= 4 else f"({Z},{N})"


def _interfaces(word) -> list[int]:
    """Indices of the interface letters (generator == 2 mod 3)."""
    return [i for i, (c, d, g) in enumerate(word) if g % 3 == 2]


def _drop(word, idxs: set[int]):
    return [l for i, l in enumerate(word) if i not in idxs]


def _dominant(terms: dict):
    ordered = sorted(terms.items(), key=lambda kv: abs(kv[1]), reverse=True)
    (lam, a), (lam2, a2) = ordered[0], ordered[1]
    total_abs = mp.fsum(abs(v) for v in terms.values())
    return lam, a, abs(a) / total_abs, abs(a2) / abs(a), lam2


def cluster(Z: int, N: int, y: dict) -> dict:
    n = 3 * (Z + N)
    t0 = time.monotonic()
    w_atom = atom_braid_word_3A(Z, N, include_inter=True)
    w_free = atom_braid_word_3A(Z, N, include_inter=False)
    chi_a = chi_all_lambda_any(w_atom, n)
    chi_f = chi_all_lambda_any(w_free, n)
    ta = {lam: y[lam] * chi_a.get(lam, mp.mpf(0)) for lam in y}
    tf = {lam: y[lam] * chi_f.get(lam, mp.mpf(0)) for lam in y}
    tr_a, tr_f = mp.fsum(ta.values()), mp.fsum(tf.values())
    la, aa, sha, rua, la2 = _dominant(ta)
    lf, af, shf, ruf, lf2 = _dominant(tf)
    n_if = len(_interfaces(w_atom))
    assert n_if == (Z + N - 1 if Z + N >= 1 else 0)
    return {
        "Z": Z, "N": N, "A": Z + N, "n": n, "np": len(y),
        "w_atom": w_atom, "w_free": w_free, "chi_a": chi_a, "chi_f": chi_f,
        "tr_a": tr_a, "tr_f": tr_f,
        "dom_a": la, "a_dom_a": aa, "share_a": sha, "ru_a": rua, "ru_lam_a": la2,
        "dom_f": lf, "a_dom_f": af, "share_f": shf, "ru_f": ruf,
        "L_atom": mp.log(abs(aa)), "L_free": mp.log(abs(af)),
        "L_tr_atom": mp.log(abs(tr_a)), "L_tr_free": mp.log(abs(tr_f)),
        "dL_sameblock": mp.log(abs(chi_f[la])) - mp.log(abs(chi_a[la])),
        "log_y_dom": mp.log(abs(y[la])),
        "onerow_sameblock": mp.log(abs(chi_f[(n,)])) - mp.log(abs(chi_a[(n,)])),
        "wall": time.monotonic() - t0,
    }


def ursell_typed(X: dict, a_max: int) -> dict:
    """Complete-graph typed cluster cumulants b(z, n), one per composition:
    X(Z,N) = sum_{z<=Z, n<=N} C(Z,z) C(N,n) b(z,n). Reproduces the #7200
    formulas at A <= 4 and extends them to any order."""
    b: dict = {}
    for A in range(1, a_max + 1):
        for z in range(0, A + 1):
            nn = A - z
            if (z, nn) not in X:
                continue
            acc = X[(z, nn)]
            for (zz, mm), bv in b.items():
                if zz <= z and mm <= nn and (zz, mm) != (z, nn):
                    acc -= mp.binomial(z, zz) * mp.binomial(nn, mm) * bv
            b[(z, nn)] = acc
    return b


def ursell_uniform(B: dict) -> dict:
    """Corpus uniform-e_2 convention, defined at A <= 4: e_2 := B(2H)."""
    e2 = B[(1, 1)]
    b3_3h = B[(1, 2)] - 3 * e2
    b3_3he = B[(2, 1)] - 3 * e2
    b4 = B[(2, 2)] - 6 * e2 - 2 * b3_3h - 2 * b3_3he
    return {"e2": e2, "b3_3H": b3_3h, "b3_3He": b3_3he, "b4_4He": b4}


def chain_fixed_n(X: dict, A: int) -> dict:
    """Chain-edge additivity at fixed A over the A+1 typed words.
    L_pp, L_nn, L_pn determined by (A,0), (0,A), (A-1,1); every other word
    predicted; returns the constants and the per-word residuals."""
    Lpp = X[(A, 0)] / (A - 1)
    Lnn = X[(0, A)] / (A - 1)
    Lpn = X[(A - 1, 1)] - (A - 2) * Lpp
    res = {}
    for (Z, N), v in X.items():
        pred = (Z - 1) * Lpp * (1 if Z >= 1 else 0) + (Lpn if Z >= 1 and N >= 1 else 0) \
            + (N - 1) * Lnn * (1 if N >= 1 else 0)
        res[(Z, N)] = v - pred
    return {"L_pp": Lpp, "L_pn": Lpn, "L_nn": Lnn, "residuals": res,
            "max_abs_residual": max(abs(v) for v in res.values())}


def subset_cumulants(w_atom, n: int, blocks: list, subsets: list[tuple[int, ...]],
                     y: dict, label: str) -> dict:
    """F(S) = log|chi^lambda(word with interface set S)| for each block, plus
    the full trace, for every S in `subsets`; then the Moebius cumulants on
    every S whose whole down-set is in `subsets`."""
    ifs = _interfaces(w_atom)
    F: dict = {lam: {} for lam in blocks}
    F["trace"] = {}
    for k, S in enumerate(subsets):
        keep = {ifs[i] for i in S}
        w = _drop(w_atom, set(ifs) - keep)
        t0 = time.monotonic()
        chi = chi_all_lambda_any(w, n)
        for lam in blocks:
            F[lam][S] = mp.log(abs(chi[lam]))
        F["trace"][S] = mp.log(abs(mp.fsum(y[lam] * chi.get(lam, mp.mpf(0)) for lam in y)))
        print(f"    {label} subset {k + 1}/{len(subsets)} S={S} "
              f"({time.monotonic() - t0:.1f}s)", flush=True)
    have = set(subsets)
    cum: dict = {}
    for key, Fk in F.items():
        cum[key] = {}
        for S in subsets:
            subs = [tuple(T) for r in range(len(S) + 1)
                    for T in itertools.combinations(S, r)]
            if not all(T in have for T in subs):
                continue
            cum[key][S] = mp.fsum(((-1) ** (len(S) - len(T))) * Fk[T] for T in subs)
    return {"F": F, "cum": cum, "interface_positions": ifs}


def main() -> int:
    t_start = time.monotonic()
    assertions: dict[str, bool] = {}
    ok = True

    def chk(name: str, cond: bool) -> None:
        nonlocal ok
        assertions[name] = bool(cond)
        ok &= bool(cond)
        print(f"  [{'PASS' if cond else 'FAIL'}] {name}", flush=True)

    print(f"q0 (proton pin) = {_s(Q0, 30)}   z_D = {_s(Z_D, 20)}")
    print(f"E0 = m_e/(q0(q0-1)) = {_s(E0, 25)} MeV  [mass_binding_dashboard._constants]")

    # ---- y_lambda per n ----
    Y: dict[int, dict] = {}
    for A in range(1, A_MAX + 1):
        n = 3 * A
        Y[n] = {tuple(k): mp.mpf(str(v)) for k, v in y_lambda_at(n, Q_MP).items()}

    # ---- clusters ----
    rows: dict[tuple[int, int], dict] = {}
    n_clusters = sum(A + 1 for A in range(1, A_MAX + 1))
    done = 0
    for A in range(1, A_MAX + 1):
        for Z in range(A, -1, -1):
            N = A - Z
            r = cluster(Z, N, Y[3 * A])
            rows[(Z, N)] = r
            done += 1
            el = time.monotonic() - t_start
            print(f"[{done:2}/{n_clusters}] {_lab(Z, N):7} A={A} n={r['n']:2} p(n)={r['np']:3} "
                  f"wall {r['wall']:6.1f}s  elapsed {el:6.0f}s  "
                  f"dom atom {list(r['dom_a'])} ru/dom {_s(r['ru_a'], 5)} share {_s(r['share_a'], 4)} "
                  f"| dom free {list(r['dom_f'])} | dL {_s(r['L_free'] - r['L_atom'], 10)} "
                  f"sameblock {_s(r['dL_sameblock'], 10)} logtr {_s(r['L_tr_free'] - r['L_tr_atom'], 10)}",
                  flush=True)

    # ---- provenance: live 6Li == committed cache ----
    print("\n== cache provenance (6Li live alternating-core word vs committed cache)")
    w6 = json.loads((HERE / CACHE_6LI).read_text())
    chk("cache_6Li_is_proton_alternating_core",
        w6.get("q0Anchor") == "proton" and w6.get("braid_word_intra_order") == "borromean")
    worst6 = mp.mpf(0)
    r6 = rows[(3, 3)]
    for rec in w6["by_partition"]:
        part = rec["partition"]
        lam = tuple(json.loads(part) if isinstance(part, str) else part)
        worst6 = max(worst6, abs(mp.mpf(rec["chi_lambda"]) - r6["chi_a"][lam]))
    print(f"  max |cache chi - live chi| over 385 partitions: {_s(worst6, 5)}")
    chk("live_6Li_word_reproduces_committed_cache_1e-40", worst6 < mp.mpf("1e-40"))

    # ---- which block dominates, and its margin ----
    print("\n== dominant summand (trace's argmax), per cluster")
    two_row = {}
    for (Z, N), r in sorted(rows.items(), key=lambda kv: (kv[1]["A"], -kv[0][0])):
        two_row[(Z, N)] = len(r["dom_a"])
        print(f"  {_lab(Z, N):7} atom {str(list(r['dom_a'])):9} rows={len(r['dom_a'])} "
              f"ru/dom {_s(r['ru_a'], 6)} ({list(r['ru_lam_a'])}) share {_s(r['share_a'], 5)} "
              f"| free {str(list(r['dom_f'])):9}")
    chk("dominant_unique_margin_ge_1e-3_all_clusters",
        all(1 - r["ru_a"] > mp.mpf("1e-3") for r in rows.values()))
    chk("dominant_is_onerow_for_A_le_4",
        all(r["dom_a"] == (r["n"],) for r in rows.values() if r["A"] <= 4))
    chk("dominant_is_two_row_for_6Li_and_7Li",
        len(rows[(3, 3)]["dom_a"]) == 2 and len(rows[(3, 4)]["dom_a"]) == 2)
    dom_rows_A56 = {k: len(r["dom_a"]) for k, r in rows.items() if r["A"] >= 5}
    print(f"  rows of the dominant block, A >= 5: {dom_rows_A56}")

    # ---- fixed-n chain-edge additivity, per block ----
    print("\n== fixed-n chain-edge additivity of the same-block log ratio, per block")
    print("   (L_pp, L_nn, L_pn determined by (A,0), (0,A), (A-1,1); the other A-2 words predicted)")
    fixed = {}
    for A in range(3, A_MAX + 1):
        n = 3 * A
        lams = list(Y[n].keys())
        per_block = {}
        for lam in lams:
            X = {k: mp.log(abs(rows[k]["chi_a"][lam])) - mp.log(abs(rows[k]["chi_f"][lam]))
                 for k in rows if rows[k]["A"] == A}
            per_block[lam] = chain_fixed_n(X, A)
        Xtr = {k: rows[k]["L_tr_atom"] - rows[k]["L_tr_free"] for k in rows if rows[k]["A"] == A}
        tr_fix = chain_fixed_n(Xtr, A)
        onerow = per_block[(n,)]
        # dominant blocks appearing at this A
        doms = sorted({rows[k]["dom_a"] for k in rows if rows[k]["A"] == A},
                      key=lambda l: (len(l), l), reverse=True)
        n_additive = sum(1 for v in per_block.values() if v["max_abs_residual"] < mp.mpf("1e-40"))
        worst_lam = max(per_block.items(), key=lambda kv: kv[1]["max_abs_residual"])
        print(f"  A={A} n={n}: blocks chain-additive to 1e-40: {n_additive}/{len(lams)}; "
              f"full trace residual {_s(tr_fix['max_abs_residual'], 4)}; one-row {_s(onerow['max_abs_residual'], 4)}; "
              f"worst block {list(worst_lam[0])} {_s(worst_lam[1]['max_abs_residual'], 6)}")
        for lam in doms:
            v = per_block[lam]
            print(f"    dominant block {str(list(lam)):9} L_pp {_s(v['L_pp'], 12)} L_pn {_s(v['L_pn'], 12)} "
                  f"L_nn {_s(v['L_nn'], 12)} max|res| {_s(v['max_abs_residual'], 8)} "
                  f"res: {[(k, _s(x, 6)) for k, x in v['residuals'].items() if abs(x) > mp.mpf('1e-40')]}")
        fixed[A] = {"per_block": per_block, "trace": tr_fix, "dominant_blocks": doms,
                    "n_additive": n_additive, "n_blocks": len(lams)}
    chk("full_trace_chain_additive_fixed_n_1e-30_all_A",
        all(v["trace"]["max_abs_residual"] < mp.mpf("1e-30") for v in fixed.values()))
    chk("onerow_block_chain_additive_fixed_n_1e-40_all_A",
        all(v["per_block"][(3 * A,)]["max_abs_residual"] < mp.mpf("1e-40") for A, v in fixed.items()))
    r6 = fixed[6]["per_block"][rows[(3, 3)]["dom_a"]]["max_abs_residual"]
    r7 = fixed[7]["per_block"][rows[(3, 4)]["dom_a"]]["max_abs_residual"]
    print(f"  two-row dominant block chain residual: 6Li block {_s(r6, 8)}, 7Li block {_s(r7, 8)}")
    two_row_additive = bool(r6 < mp.mpf("1e-40") and r7 < mp.mpf("1e-40"))
    print(f"  two-row dominant block letter-additive at fixed n? {two_row_additive}  (a FINDING, not asserted)")

    # ---- typed bond-set decomposition inside the dominant block ----
    print("\n== typed bond-set (interface-subset) cumulants of the block log-weight")
    sub = {}
    for (Z, N), nm, subsets in (
        ((3, 3), "6Li", [tuple(c) for r in range(6) for c in itertools.combinations(range(5), r)]),
        ((3, 4), "7Li", [()] + [(i,) for i in range(6)]
                        + [c for c in itertools.combinations(range(6), 2)] + [tuple(range(6))]),
    ):
        r = rows[(Z, N)]
        n = r["n"]
        blocks = [r["dom_a"], (n,)]
        if r["dom_f"] not in blocks:
            blocks.append(r["dom_f"])
        ifs = _interfaces(r["w_atom"])
        types = ["pp"] * (Z - 1) + ["pn"] + ["nn"] * (N - 1)
        print(f"  {nm}: interfaces at word positions {ifs}, types {types}, blocks {[list(b) for b in blocks]}")
        sc = subset_cumulants(r["w_atom"], n, blocks, subsets, Y[n], nm)
        sc["types"] = types
        sub[nm] = sc
        # full-set check: F(all) == log|chi(atom)|
        full = tuple(range(len(ifs)))
        chk(f"{nm}_subset_full_set_equals_atom_word_1e-45",
            abs(sc["F"][r["dom_a"]][full] - mp.log(abs(r["chi_a"][r["dom_a"]]))) < mp.mpf("1e-45")
            and abs(sc["F"][r["dom_a"]][()] - mp.log(abs(r["chi_f"][r["dom_a"]]))) < mp.mpf("1e-45"))
        for key in [r["dom_a"], (n,), "trace"]:
            cum = sc["cum"][key]
            name = "trace" if key == "trace" else str(list(key))
            singles = {S: cum[S] for S in cum if len(S) == 1}
            pairs = {S: cum[S] for S in cum if len(S) == 2}
            higher = {S: cum[S] for S in cum if len(S) >= 3}
            print(f"    block {name:9} per-edge c(e): "
                  + ", ".join(f"{types[S[0]]}@{S[0]}={_s(v, 8)}" for S, v in singles.items()))
            print(f"      pair cumulants c(e,f): max|.| {_s(max(abs(v) for v in pairs.values()), 6)}; "
                  + ", ".join(f"{S}={_s(v, 6)}" for S, v in pairs.items()))
            if higher:
                print(f"      order>=3 cumulants: max|.| {_s(max(abs(v) for v in higher.values()), 6)}; "
                      + ", ".join(f"{S}={_s(v, 5)}" for S, v in higher.items() if abs(v) > mp.mpf('1e-40')))
        chk(f"{nm}_onerow_block_interface_cumulants_vanish_1e-40",
            all(abs(v) < mp.mpf("1e-40") for S, v in sc["cum"][(n,)].items() if len(S) >= 2))
        chk(f"{nm}_full_trace_interface_cumulants_vanish_1e-30",
            all(abs(v) < mp.mpf("1e-30") for S, v in sc["cum"]["trace"].items() if len(S) >= 2))

    # ---- typed Ursell inversion to order 7 ----
    dL = {k: r["L_free"] - r["L_atom"] for k, r in rows.items()}
    dLs = {k: r["dL_sameblock"] for k, r in rows.items()}
    switch = {k: dL[k] - dLs[k] for k in dL}
    gy = {k: r["log_y_dom"] for k, r in rows.items()}
    Ltr = {k: r["L_tr_free"] - r["L_tr_atom"] for k, r in rows.items()}
    inv = {nm: ursell_typed(X, A_MAX) for nm, X in
           (("dL", dL), ("dL_sameblock", dLs), ("switch", switch), ("log_y_dom", gy), ("log_tr_ratio", Ltr))}
    chk("dL_b1_is_zero_exactly", inv["dL"][(1, 0)] == 0 and inv["dL"][(0, 1)] == 0)
    # round trip at (3,4)
    rt = mp.fsum(mp.binomial(3, z) * mp.binomial(4, m) * bv for (z, m), bv in inv["dL"].items()
                 if z <= 3 and m <= 4)
    chk("ursell_roundtrip_7Li_1e-50", abs(rt - dL[(3, 4)]) < mp.mpf("1e-50"))
    chk("switch_is_nonneg_to_rounding", all(v > mp.mpf("-1e-45") for v in switch.values()))
    print("\n== typed Ursell cumulants (log units; MeV = E0 x), complete-graph typed basis")
    print(f"  {'(z,n)':8} {'dL':>16} {'dL_sameblock':>16} {'switch':>16} {'log_y_dom':>16} {'log_tr(ctrl)':>16} {'E0.dL MeV':>12}")
    for A in range(2, A_MAX + 1):
        for z in range(A, -1, -1):
            k = (z, A - z)
            print(f"  {str(k):8} " + " ".join(f"{_s(inv[nm][k], 10):>16}" for nm in inv) + f" {_s(E0 * inv['dL'][k], 8):>12}")
    b3_tr = max(abs(inv["log_tr_ratio"][k]) for k in inv["log_tr_ratio"] if sum(k) >= 3)
    print(f"  full-trace control: max |b_k|, k>=3 = {_s(b3_tr, 5)}  (bond rule: 0);  b2_pp vs ln(1/z_D): "
          f"{_s(inv['log_tr_ratio'][(2, 0)], 20)} vs {_s(-mp.log(Z_D), 20)}")

    # ---- against AME ----
    B_ame = {k: ame_binding_mev(k[0], sum(k)) for k in AME_SET}
    ame_u = ursell_uniform(B_ame)
    Bdom = {k: E0 * dL[k] for k in dL}
    dom_u = ursell_uniform(Bdom)
    Btr = {k: E0 * Ltr[k] for k in Ltr}
    tr_u = ursell_uniform(Btr)
    print("\n== uniform-e2 convention (defined at A <= 4), MeV")
    print(f"  {'':10} {'AME2020':>14} {'dominant summand':>18} {'full trace':>14}")
    for k in ("e2", "b3_3H", "b3_3He", "b4_4He"):
        print(f"  {k:10} {_s(ame_u[k], 10):>14} {_s(dom_u[k], 10):>18} {_s(tr_u[k], 10):>14}")
    print("\n== per-cluster totals vs AME2020 (MeV)")
    print(f"  {'nuclide':8} {'AME B':>12} {'E0.dL(dom)':>12} {'AME/E0dL':>10} {'E0.dL_sameblock':>16} {'E0.switch':>10} {'E0.logtr(full)':>14} {'B/A AME':>8} {'B/A dom':>8}")
    per_A = {}
    for k, (nm, unb) in AME_SET.items():
        A = sum(k)
        ratio = B_ame[k] / Bdom[k] if Bdom[k] != 0 else mp.mpf("inf")
        print(f"  {nm + ('*' if unb else ''):8} {_s(B_ame[k], 9):>12} {_s(Bdom[k], 9):>12} {_s(ratio, 6):>10} "
              f"{_s(E0 * dLs[k], 9):>16} {_s(E0 * switch[k], 8):>10} {_s(Btr[k], 9):>14} "
              f"{_s(B_ame[k] / A, 6):>8} {_s(Bdom[k] / A, 6):>8}")
        per_A[nm] = {"Z": k[0], "N": k[1], "A": A, "particle_unbound": unb,
                     "AME_B_MeV": _s(B_ame[k], 20), "E0_dL_MeV": _s(Bdom[k], 20),
                     "E0_dL_sameblock_MeV": _s(E0 * dLs[k], 20), "E0_switch_MeV": _s(E0 * switch[k], 20),
                     "E0_log_tr_ratio_MeV": _s(Btr[k], 20), "AME_over_E0dL": _s(ratio, 12)}
    print("  (* = unbound to nucleon emission in AME2020; B is the total binding against free nucleons)")

    # ---- growth of the two-row same-block part ----
    print("\n== what the two-row dominant block adds beyond the chain law (its own connected content), 6Li/7Li")
    conn = {}
    for nm, k in (("6Li", (3, 3)), ("7Li", (3, 4))):
        r = rows[k]
        cum = sub[nm]["cum"][r["dom_a"]]
        edge_sum = mp.fsum(v for S, v in cum.items() if len(S) == 1)
        pair_sum = mp.fsum(v for S, v in cum.items() if len(S) == 2)
        high_sum = mp.fsum(v for S, v in cum.items() if len(S) >= 3)
        total = cum[tuple(range(sum(k) - 1))] if tuple(range(sum(k) - 1)) in cum else None
        F = sub[nm]["F"][r["dom_a"]]
        full = tuple(range(sum(k) - 1))
        dF = F[full] - F[()]           # = -dL_sameblock
        conn[nm] = {"edge_sum": edge_sum, "pair_sum": pair_sum, "higher_sum": high_sum, "dF": dF}
        print(f"  {nm} block {list(r['dom_a'])}: log|chi(atom)/chi(free)| = {_s(dF, 12)} "
              f"= edges {_s(edge_sum, 12)} + pairs {_s(pair_sum, 12)}"
              + (f" + order>=3 {_s(high_sum, 12)}" if nm == "6Li" else " + order>=3 (not enumerated at 7Li)")
              + f";  in MeV (E0 x, sign as binding = -dF): edges {_s(-E0 * edge_sum, 8)}, pairs {_s(-E0 * pair_sum, 8)}"
              + (f", higher {_s(-E0 * high_sum, 8)}" if nm == "6Li" else ""))

    # ---- witness ----
    def ser(d: dict) -> dict:
        return {(f"{k[0]},{k[1]}" if isinstance(k, tuple) else k): (_s(v, 40) if isinstance(v, mp.mpf) else v)
                for k, v in d.items()}

    cluster_rows = []
    for (Z, N), r in sorted(rows.items(), key=lambda kv: (kv[1]["A"], -kv[0][0])):
        cluster_rows.append({
            "label": _lab(Z, N), "Z": Z, "N": N, "A": Z + N, "n_strands": r["n"],
            "n_partitions": r["np"], "word_len_atom": len(r["w_atom"]),
            "dominant_atom": list(r["dom_a"]), "dominant_rows": len(r["dom_a"]),
            "runner_up_atom": list(r["ru_lam_a"]),
            "runner_up_over_dominant_atom": _s(r["ru_a"], 20),
            "share_of_sum_abs_atom": _s(r["share_a"], 20),
            "dominant_free": list(r["dom_f"]),
            "a_dominant_atom": _s(r["a_dom_a"], 40), "a_dominant_free": _s(r["a_dom_f"], 40),
            "tr_atom": _s(r["tr_a"], 40), "tr_free": _s(r["tr_f"], 40),
            "L_atom": _s(r["L_atom"], 40), "L_free": _s(r["L_free"], 40),
            "dL_dominant": _s(dL[(Z, N)], 40), "dL_sameblock": _s(dLs[(Z, N)], 40),
            "switch": _s(switch[(Z, N)], 40), "log_y_dominant": _s(gy[(Z, N)], 40),
            "onerow_sameblock_log_ratio": _s(r["onerow_sameblock"], 40),
            "log_tr_ratio_full": _s(Ltr[(Z, N)], 40),
        })

    fixed_ser = {}
    for A, v in fixed.items():
        fixed_ser[str(A)] = {
            "n_blocks": v["n_blocks"], "n_blocks_chain_additive_1e-40": v["n_additive"],
            "full_trace_max_abs_residual": _s(v["trace"]["max_abs_residual"], 10),
            "onerow_max_abs_residual": _s(v["per_block"][(3 * A,)]["max_abs_residual"], 10),
            "dominant_blocks": {str(list(lam)): {
                "L_pp": _s(v["per_block"][lam]["L_pp"], 30), "L_pn": _s(v["per_block"][lam]["L_pn"], 30),
                "L_nn": _s(v["per_block"][lam]["L_nn"], 30),
                "max_abs_residual": _s(v["per_block"][lam]["max_abs_residual"], 15),
                "residuals": ser(v["per_block"][lam]["residuals"])} for lam in v["dominant_blocks"]},
            "worst_block": [list(max(v["per_block"].items(), key=lambda kv: kv[1]["max_abs_residual"])[0]),
                            _s(max(x["max_abs_residual"] for x in v["per_block"].values()), 10)],
        }
    sub_ser = {}
    for nm, sc in sub.items():
        sub_ser[nm] = {
            "interface_word_positions": sc["interface_positions"], "interface_types": sc["types"],
            "blocks": {("trace" if key == "trace" else str(list(key))): {
                "F_by_subset": {str(list(S)): _s(v, 30) for S, v in sc["F"][key].items()},
                "cumulants_by_subset": {str(list(S)): _s(v, 30) for S, v in sc["cum"][key].items()},
                "max_abs_pair_cumulant": _s(max(abs(v) for S, v in sc["cum"][key].items() if len(S) == 2), 12),
                "max_abs_order_ge3_cumulant": (_s(max(abs(v) for S, v in sc["cum"][key].items() if len(S) >= 3), 12)
                                               if any(len(S) >= 3 for S in sc["cum"][key]) else None),
            } for key in sc["cum"]},
        }

    witness = {
        "computation": "brng-two-row-dominant-block-a6",
        "description": (
            "A >= 6 remainder of bean qou-brng after qou-m8f3 (PR #7200): the "
            "trace's dominant summand argmax|y_lambda chi^lambda| is a TWO-ROW "
            "block at 6Li/7Li, whose character is not a ring homomorphism. For "
            "every typed cluster (Z,N) with Z+N <= 7 on the live alternating-core "
            "atom word (proton pin, convention D): the dominant block and its "
            "margin; fixed-n chain-edge additivity of the same-block log ratio "
            "for every block; the typed bond-set (interface-subset) Moebius "
            "cumulants of the dominant block's log-weight at 6Li (all 32 subsets) "
            "and 7Li (singletons, pairs, full); the typed Ursell inversion to "
            "order 7; uniform-e2 at A <= 4 and per-cluster totals vs AME2020. "
            "Controls: the one-row block (letter product, zero cumulants) and "
            "the full trace (bond rule, zero cumulants). Nothing wired, nothing "
            "fitted, no route selected by residual."
        ),
        "assertions": assertions,
        "allPassed": bool(ok),
        "parameters": {
            "q0": _s(Q0, 50), "q0_pin": "proton", "convention": "D",
            "z_D": _s(Z_D, 40), "dps": DPS, "m_e_MeV": _s(M_E, 20), "E0_MeV": _s(E0, 30),
            "E0_source": "mass_binding_dashboard._constants(): m_e/(q0(q0-1)); no new scale",
            "word": "mass_at_3A_proper.atom_braid_word_3A(Z, N) default intra_order='borromean' "
                    "(alternating core, qou-hu1f ruling 2026-09-05); interface subsets by deleting "
                    "interface letters (generator 2 mod 3) from the atom word",
            "chi_kernel": "chi_general_word.chi_all_lambda_any (window transfer)",
            "y_lambda": "wedderburn_jones_markov.y_lambda_at(n, Q_MP)",
            "ame_source": "AME2020 vendored table, binding_energy_per_A_keV x A; A=5 (5He, 5Li), "
                          "6Be and 7He are unbound to nucleon emission and flagged",
            "dominant_definition": "argmax_lambda |y_lambda chi^lambda| (the trace's)",
            "A_max": A_MAX,
            "lean": ["QOU/Mass/MixedSpectrumCharacterNotLetterMultiplicative.lean",
                     "QOU/Mass/OneRowBlockLetterProduct.lean (PR #7200)",
                     "QOU/Mass/MultiplicityNotExtensive.lean",
                     "QOU/BraidKnot/BindingConcentration.lean"],
        },
        "data": {
            "clusters": cluster_rows,
            "cache_provenance_6Li_max_abs_diff": _s(worst6, 10),
            "dominant_rows_A_ge_5": {f"{k[0]},{k[1]}": v for k, v in dom_rows_A56.items()},
            "two_row_dominant_chain_additive_fixed_n": two_row_additive,
            "two_row_dominant_chain_residual": {"6Li": _s(r6, 15), "7Li": _s(r7, 15)},
            "fixed_n_chain_additivity": fixed_ser,
            "interface_subset_cumulants": sub_ser,
            "two_row_connected_content": {nm: ser(v) for nm, v in conn.items()},
            "ursell_typed_log_units": {nm: ser(v) for nm, v in inv.items()},
            "ursell_typed_dL_MeV_E0_scaled": ser({k: E0 * v for k, v in inv["dL"].items()}),
            "uniform_e2_convention_MeV": {"AME2020": ser(ame_u), "dominant_summand_E0_scaled": ser(dom_u),
                                          "full_trace_E0_scaled": ser(tr_u)},
            "per_cluster_vs_AME": per_A,
            "bond_rule_control_max_abs_bk_k_ge_3_full_trace": _s(b3_tr, 10),
        },
        "provenance": {
            "headSha": _head_sha(),
            "producer": "computations/brng_two_row_dominant_block_a6_probe.py",
            "bean": "qou-vn6h (qou-brng A >= 6 remainder after qou-m8f3)",
            "elapsed_s": round(time.monotonic() - t_start, 3),
        },
    }
    WitnessBuilder.stamp_staleness_metadata(
        witness, script_path=__file__, engine="python",
        q0_anchor="proton",
        q0_anchor_reason=("AGENTS.md 2026-08-07 owner directive: experimental "
                          "pin is the default for all new compute; every chi, "
                          "y_lambda and E0 here is at the proton q0"),
        q0_value=_s(Q0, 30))
    out = HERE / "brng-two-row-dominant-block-a6.witness.json"
    out.write_text(json.dumps(witness, indent=2, ensure_ascii=False) + "\n")
    print(f"\nassertions {sum(assertions.values())}/{len(assertions)}  "
          f"witness -> {out.relative_to(ROOT)}  total wall {time.monotonic() - t_start:.0f}s")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
