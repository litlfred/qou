#!/usr/bin/env python3
# polynomial_q_not_applicable: numerical evaluation at q = q_0 only.
"""Does the DOMINANT SUMMAND's own log-weight carry a connected b_3?

The live remainder of bean `qou-brng` after PR #7181. `QOU/Mass/
MultiplicityNotExtensive.lean` proved that the multiplicity channel of the
partition sum

    tr_M(beta_A) = sum_{lambda |- 3A} y_lambda . chi^lambda(beta_A)

is O(sqrt A) and cannot be the extensive binding term. The bean's own scoping
sentence says the only place an extensive term can then live is the dominant
summand's OWN log-weight

    L(A) = log |y_{lambda*} chi^{lambda*}(beta_A)|,   lambda* = argmax |y chi|

and that no probe had tested it. This probe tests it.

*** WHY IT IS UNDECIDED A PRIORI ***

`QOU/Mass/MarkovBondRuleForcesPairwise.lean` forces b_3 = 0 for any binding
read off `tr_M` by a product-to-sum map: the bond rule
`tr(x (sigma_g + d)) = (z + d) tr x` is a statement about the WHOLE trace.
It says nothing about a single Wedderburn block's character chi^lambda, and
the argmax over lambda is not a linear functional of the trace. So the
connected three-body cumulant of L(A) is genuinely open: it could be zero
(the block inherits the bond rule), positive (AME's sign), or negative.

*** WHAT IS COMPUTED, and in what order ***

For every typed cluster (Z, N) with Z + N <= 4 -- p, n, pp, pn, nn, ppp, ppn,
pnn, nnn, ppnn -- and for 6Li as a growth check:

  1. the live atom word `atom_braid_word_3A(Z, N)` (post-2026-09-05
     alternating-core intra word, bean `qou-hu1f`; `include_inter=True`) and
     its free word (`include_inter=False`), on n = 3(Z+N) strands;
  2. all chi^lambda via `chi_general_word.chi_all_lambda_any` (the window
     transfer for the non-monotone live word, Rust kernel fallback -- what
     `tr_m_atom_via_transfer` dispatches to) and the Jones-Markov weights
     `wedderburn_jones_markov.y_lambda_at(n, q0)` -- convention D,
     z = q^3/(q^2+1), proton pin `Q_50_DIGIT_STR`;
  3. the dominant summand AS THE TRACE DEFINES IT: lambda* = argmax_lambda
     |y_lambda chi^lambda|. No choice is made; the argmax of the binding sum
     |y chi Delta| is recorded alongside but not used;
  4. L_atom = log|a_{lambda*}(atom)|, L_free = log|a_{lambda*}(free)|, each
     with its own argmax, and the binding-like difference
     dL = L_free - L_atom -- the exact analogue of the production
     `mass_binding_dashboard` law `B_sym = E_0 ln(tr_free / tr_atom)` with the
     trace replaced by its largest term.

Then the typed Ursell (cluster-cumulant) inversion of three quantities:

  (i)   dL                 -- the candidate binding carrier (b_1 = 0 exactly:
                              an A = 1 word has no interface, asserted);
  (ii)  L_free alone       -- a CONTROL. The free word has no bonds, so any
                              nonzero b_2, b_3 here is an artefact of taking the
                              argmax of a partition sum, not an interaction;
  (iii) log(tr_free/tr_atom), the full trace -- the CONTROL the bond rule
                              predicts: b_3 = b_4 = 0 to the bond-rule
                              precision, on the LIVE word.

Typed inversion (b_1 per nucleon type, b_2 per pair type, b_3 per triple
type, b_4 for ppnn):

    b_2(pn)   = X(1,1) - b_1(p) - b_1(n)
    b_3(ppn)  = X(2,1) - 2 b_1(p) - b_1(n) - b_2(pp) - 2 b_2(pn)
    b_4(ppnn) = X(2,2) - 2b_1(p) - 2b_1(n) - b_2(pp) - b_2(nn) - 4 b_2(pn)
                       - 2 b_3(ppn) - 2 b_3(pnn)

and the corpus UNIFORM convention, which is how the AME targets quoted in
`qou-brng` are defined (`docs/audits/2026-08-30-ursell-alternating-sign-and-
the-b3-obstruction.md`, `2026-08-29-gap2-he4-milnor-indeterminacy-
exclusion.md`): e_2 := B(2H) for every pair, so b_3^unif(A=3) = B(3) - 3 e_2
and b_4^unif = B(4He) - 6 e_2 - 2 b_3^unif(3H) - 2 b_3^unif(3He).
AME2020: b_3^unif(3H) = +1.8081, b_3^unif(3He) = +1.0443 MeV.

*** SCALE ***

Energies are E_0 x (log quantity) with E_0 = m_e / (q_0 (q_0 - 1)), taken
from `mass_binding_dashboard._constants()` -- the constant the production
dashboard multiplies `ln(tr_free/tr_atom)` by. No new scale is introduced. The
sibling #7181 probe carries E_0/(1 - hbar^2) (a 0.99 % difference); the
scale-free ratios b_3/b_2, which are what decide the sign and the shape, do
not depend on either. Per #7174 / `qou-v8ct` a uniform factor is undecidable
at fixed law, so the E_0-carrying rows are labelled and the headline is the
scale-free row.

*** WHAT IS NOT DONE ***

Nothing is wired. No route is selected by residual. AME enters only as a
comparison target. If a positive b_3 appears with the wrong magnitude it is
REPORTED, not fitted -- wiring it would re-open the Delta_lambda-magnitude
family through the back door.

Precision: mpmath at 60 dps; q_0 from `Q_50_DIGIT_STR` (proton pin, AGENTS.md
2026-08-07 directive); AME as `Decimal` from the vendored table with
`parse_float=str`; display through `mp.nstr`. No float arithmetic.

Assertions guard only structure and precision (cache provenance, b_1 = 0 for
dL, dominance margin, inversion round-trip); the sign result is a FINDING and
is never asserted.
"""

from __future__ import annotations

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
from two_row_vs_higher_row_binding_split import (  # noqa: E402
    hook_length_dim, n_of_lambda)

DPS = 60
mp.mp.dps = DPS

M_E, Q0, E0 = _constants()          # all mpf; E0 = m_e / (q0 (q0 - 1))
assert mp.nstr(Q0, 40) == mp.nstr(mp.mpf(Q_50_DIGIT_STR), 40)
Z_D = Q0 ** 3 / (Q0 ** 2 + 1)       # convention D Markov parameter

_AME_PATH = ROOT / "qou-mass" / "src" / "qou_mass" / "data" / "ame2020.json"

#: Typed clusters. Chosen before any number was computed: every (Z, N) with
#: 1 <= Z + N <= 4, plus 6Li as the growth check.
CLUSTERS: list[tuple[int, int, str]] = [
    (1, 0, "p"), (0, 1, "n"),
    (2, 0, "pp"), (1, 1, "pn=2H"), (0, 2, "nn"),
    (3, 0, "ppp"), (2, 1, "ppn=3He"), (1, 2, "pnn=3H"), (0, 3, "nnn"),
    (2, 2, "ppnn=4He"),
    (3, 3, "6Li"),
]
#: Committed per-partition caches (post-ruling, computedAt 2026-09-06) that
#: the live recompute is checked against -- provenance of the word.
CACHES = {
    (1, 1): "chi-deuteron-h6-at-q0-50dps.witness.json",
    (1, 2): "chi-tritium-h9-at-q0-50dps.witness.json",
    (2, 1): "chi-helium-3-h9-at-q0-50dps.witness.json",
    (2, 2): "chi-helium-4-h12-at-q0-50dps.witness.json",
}


def _head_sha() -> str:
    try:
        return subprocess.run(["git", "rev-parse", "HEAD"], cwd=ROOT,
                              capture_output=True, text=True,
                              check=True).stdout.strip()
    except Exception:
        return "unknown"


def ame_binding_mev(Z: int, A: int) -> mp.mpf:
    """B (MeV) from the vendored AME2020 table: `binding_energy_per_A_keV`
    (the column AME quotes) x A / 1000, exactly in Decimal, then mpf from
    the decimal string."""
    raw = json.loads(_AME_PATH.read_text(), parse_float=str)
    for e in raw["entries"]:
        if int(e["Z"]) == Z and int(e["A"]) == A:
            return mp.mpf(str(Decimal(e["binding_energy_per_A_keV"]) * A
                              / Decimal(1000)))
    raise KeyError(f"Z={Z} A={A} not in the vendored AME2020 table")


def _terms(word, n: int, y: dict) -> dict:
    chi = chi_all_lambda_any(word, n)
    return {lam: y[lam] * chi.get(lam, mp.mpf(0)) for lam in y}, chi


def _dominant(terms: dict):
    """(lambda*, a_lambda*, share, runner-up ratio) -- argmax |a_lambda|.
    Ties are impossible at 60 dps in practice; asserted below."""
    ordered = sorted(terms.items(), key=lambda kv: abs(kv[1]), reverse=True)
    (lam, a), (lam2, a2) = ordered[0], ordered[1]
    total_abs = mp.fsum(abs(v) for v in terms.values())
    return lam, a, abs(a) / total_abs, abs(a2) / abs(a), lam2


def cluster(Z: int, N: int) -> dict:
    n = 3 * (Z + N)
    y = {tuple(k): mp.mpf(str(v)) for k, v in y_lambda_at(n, Q_MP).items()}
    t0 = time.monotonic()
    w_atom = atom_braid_word_3A(Z, N, include_inter=True)
    w_free = atom_braid_word_3A(Z, N, include_inter=False)
    ta, chi_a = _terms(w_atom, n, y)
    tf, chi_f = _terms(w_free, n, y)
    wall = time.monotonic() - t0
    tr_a = mp.fsum(ta.values())
    tr_f = mp.fsum(tf.values())
    la, aa, sha, rua, la2 = _dominant(ta)
    lf, af, shf, ruf, lf2 = _dominant(tf)
    # SECONDARY: the dominant summand of the BINDING sum |y chi Delta|,
    # Delta = (-1)^{n(lambda)} f^lambda (proved value). This is the block
    # `QOU/BraidKnot/BindingConcentration.lean` lists ((5,1), (6,3), (9,3));
    # it is two-row, so its character is NOT letter-multiplicative and the
    # one-row argument below does not cover it. Analysed with the same
    # machinery, labelled secondary; not selected by any result.
    def _delta(lam):
        return mp.mpf((-1) ** n_of_lambda(list(lam)) * hook_length_dim(list(lam)))
    tda = {lam: ta[lam] * _delta(lam) for lam in ta}
    tdf = {lam: tf[lam] * _delta(lam) for lam in tf}
    lb, ab, shb, rub, lb2 = _dominant(tda)
    lbf, abf, shbf, rubf, _ = _dominant(tdf)
    return {
        "Z": Z, "N": N, "A": Z + N, "n_strands": n, "n_partitions": len(y),
        "word_len_atom": len(w_atom), "word_len_free": len(w_free),
        "words_identical": w_atom == w_free,
        "tr_atom": tr_a, "tr_free": tr_f,
        "dom_atom": la, "a_dom_atom": aa, "share_atom": sha,
        "runner_up_ratio_atom": rua, "runner_up_atom": la2,
        "dom_free": lf, "a_dom_free": af, "share_free": shf,
        "runner_up_ratio_free": ruf,
        "dom_binding_sum_atom": lb, "a_dom_binding_atom": ab,
        "share_binding_atom": shb, "runner_up_ratio_binding_atom": rub,
        "dom_binding_sum_free": lbf, "a_dom_binding_free": abf,
        "LB_atom": mp.log(abs(ab)), "LB_free": mp.log(abs(abf)),
        "dLB_sameblock": mp.log(abs(tdf.get(lb, mp.mpf(0)))) - mp.log(abs(tda[lb])),
        "L_atom": mp.log(abs(aa)), "L_free": mp.log(abs(af)),
        "L_tr_atom": mp.log(abs(tr_a)), "L_tr_free": mp.log(abs(tr_f)),
        "wall_s": wall,
        # same-block difference: the free word's weight evaluated at the ATOM's
        # own argmax (y_lambda* cancels) -- separates the interface effect
        # inside one block from the free-side argmax switch
        "dL_sameblock": mp.log(abs(chi_f.get(la, mp.mpf(0)))) - mp.log(abs(chi_a[la])),
        "log_y_dom_atom": mp.log(abs(y[la])),
        "log_y_onerow": mp.log(abs(y[(n,)])),
        # one-row block: chi^{(n)} is a ring homomorphism sigma_g -> q, so the
        # character of a word of letters c*sigma_g + d*1 is the product of
        # (c q + d) over the letters
        "onerow_product_atom": mp.fprod(mp.mpf(str(c)) * Q0 + mp.mpf(str(d)) for (c, d, g) in w_atom),
        "onerow_chi_atom": chi_a[(n,)],
        "onerow_product_free": mp.fprod(mp.mpf(str(c)) * Q0 + mp.mpf(str(d)) for (c, d, g) in w_free),
        "onerow_chi_free": chi_f[(n,)],
        "_chi_atom": chi_a, "_y": y,
    }


def ursell_typed(X: dict) -> dict:
    """Typed cluster-cumulant inversion of X[(Z,N)] up to (2,2)."""
    b1p, b1n = X[(1, 0)], X[(0, 1)]
    b2pp = X[(2, 0)] - 2 * b1p
    b2pn = X[(1, 1)] - b1p - b1n
    b2nn = X[(0, 2)] - 2 * b1n
    b3ppp = X[(3, 0)] - 3 * b1p - 3 * b2pp
    b3nnn = X[(0, 3)] - 3 * b1n - 3 * b2nn
    b3ppn = X[(2, 1)] - 2 * b1p - b1n - b2pp - 2 * b2pn
    b3pnn = X[(1, 2)] - b1p - 2 * b1n - b2nn - 2 * b2pn
    b4 = (X[(2, 2)] - 2 * b1p - 2 * b1n - b2pp - b2nn - 4 * b2pn
          - 2 * b3ppn - 2 * b3pnn)
    return {"b1_p": b1p, "b1_n": b1n, "b2_pp": b2pp, "b2_pn": b2pn,
            "b2_nn": b2nn, "b3_ppp": b3ppp, "b3_ppn": b3ppn,
            "b3_pnn": b3pnn, "b3_nnn": b3nnn, "b4_ppnn": b4}


def ursell_uniform(B: dict) -> dict:
    """Corpus uniform-e_2 convention (AME targets of qou-brng are in it):
    e_2 := B(2H) for every pair."""
    e2 = B[(1, 1)]
    b3_3h = B[(1, 2)] - 3 * e2
    b3_3he = B[(2, 1)] - 3 * e2
    b4 = B[(2, 2)] - 6 * e2 - 2 * b3_3h - 2 * b3_3he
    return {"e2": e2, "b3_3H": b3_3h, "b3_3He": b3_3he, "b4_4He": b4}


def _s(x, d: int = 12) -> str:
    return mp.nstr(x, d)


def main() -> int:
    t0 = time.monotonic()
    assertions: dict[str, bool] = {}
    ok = True

    def chk(name: str, cond: bool) -> None:
        nonlocal ok
        assertions[name] = bool(cond)
        ok &= bool(cond)
        print(f"  [{'PASS' if cond else 'FAIL'}] {name}")

    print(f"q0 (proton pin) = {_s(Q0, 30)}   z_D = {_s(Z_D, 20)}")
    print(f"E0 = m_e/(q0(q0-1)) = {_s(E0, 25)} MeV  "
          f"[mass_binding_dashboard._constants]")

    rows = {}
    for Z, N, label in CLUSTERS:
        r = cluster(Z, N)
        rows[(Z, N)] = r
        print(f"\n{label:9} n={r['n_strands']:2} p(n)={r['n_partitions']:3} "
              f"wall {r['wall_s']:.2f}s")
        print(f"  tr_atom {_s(r['tr_atom'], 20)}  tr_free {_s(r['tr_free'], 20)}")
        print(f"  dom atom {list(r['dom_atom'])} a={_s(r['a_dom_atom'], 15)} "
              f"share={_s(r['share_atom'], 6)} runner-up/dom={_s(r['runner_up_ratio_atom'], 6)} "
              f"({list(r['runner_up_atom'])})")
        print(f"  dom free {list(r['dom_free'])} a={_s(r['a_dom_free'], 15)} "
              f"share={_s(r['share_free'], 6)} runner-up/dom={_s(r['runner_up_ratio_free'], 6)}")
        print(f"  argmax|y chi Delta| atom {list(r['dom_binding_sum_atom'])}")
        print(f"  L_atom {_s(r['L_atom'], 15)}  L_free {_s(r['L_free'], 15)}  "
              f"dL {_s(r['L_free'] - r['L_atom'], 15)}   "
              f"log(tr_f/tr_a) {_s(r['L_tr_free'] - r['L_tr_atom'], 15)}")

    # ---- provenance: live recompute == committed post-ruling caches ----
    print("\n== cache provenance (live alternating-core word vs committed caches)")
    worst = mp.mpf(0)
    for zn, fname in CACHES.items():
        w = json.loads((HERE / fname).read_text())
        chk(f"cache_{fname}_postdates_ruling",
            w["computedAt"] >= "2026-09-05" and w["q0Anchor"] == "proton")
        r = rows[zn]
        for rec in w["by_partition"]:
            part = rec["partition"]
            lam = tuple(json.loads(part) if isinstance(part, str) else part)
            d = max(abs(mp.mpf(rec["chi_lambda"]) - r["_chi_atom"][lam]),
                    abs(mp.mpf(rec["y_lambda"]) - r["_y"][lam]))
            worst = max(worst, d)
    print(f"  max |cache - live| over chi, y_lambda, four nuclei: {_s(worst, 5)}")
    chk("live_word_reproduces_committed_caches_1e-40", worst < mp.mpf("1e-40"))

    # ---- structure ----
    chk("A1_words_have_no_interface_atom_eq_free",
        rows[(1, 0)]["words_identical"] and rows[(0, 1)]["words_identical"])
    chk("dominant_summand_unique_margin_ge_1e-3",
        all(1 - r["runner_up_ratio_atom"] > mp.mpf("1e-3") for r in rows.values()))
    dom_two_row = {k: len(r["dom_atom"]) <= 2 for k, r in rows.items()}
    print(f"  dominant lambda* two-row? {dom_two_row}")
    onerow_dom = {k: r["dom_atom"] == (r["n_strands"],) for k, r in rows.items()}
    print(f"  dominant lambda* is the ONE-ROW block [n]? {onerow_dom}")
    onerow_err = max(max(abs(r["onerow_product_atom"] - r["onerow_chi_atom"]),
                         abs(r["onerow_product_free"] - r["onerow_chi_free"]))
                     for r in rows.values())
    print(f"  one-row character == product over letters of (c q + d): max err {_s(onerow_err, 5)}")
    chk("onerow_character_is_letter_product_1e-45", onerow_err < mp.mpf("1e-45"))
    chk("dominant_atom_block_is_onerow_for_A_le_4",
        all(onerow_dom[k] for k in rows if sum(k) <= 4))

    # ---- the three inversions ----
    dL = {k: r["L_free"] - r["L_atom"] for k, r in rows.items()}
    Lf = {k: r["L_free"] for k, r in rows.items()}
    Ltr = {k: r["L_tr_free"] - r["L_tr_atom"] for k, r in rows.items()}
    dLs = {k: r["dL_sameblock"] for k, r in rows.items()}
    switch = {k: dL[k] - dLs[k] for k in dL}      # free-side argmax surplus
    gy = {k: r["log_y_onerow"] for k, r in rows.items()}
    inv_dL = ursell_typed(dL)
    inv_Lf = ursell_typed(Lf)
    inv_tr = ursell_typed(Ltr)
    inv_dLs = ursell_typed(dLs)
    inv_sw = ursell_typed(switch)
    inv_gy = ursell_typed(gy)
    # The atom word is a CHAIN p..p n..n with A-1 interfaces: (Z-1) pp, one pn
    # (if both present), (N-1) nn. A complete-graph Ursell inversion of an
    # edge-additive quantity therefore returns b_3 = -b_2(missing edge) etc.
    # The invariant to test is chain-edge additivity, not b_3 = 0.
    def chain_residual(X: dict) -> mp.mpf:
        worst = mp.mpf(0)
        for (Z, N), v in X.items():
            if Z + N < 2 or Z + N > 4:
                continue
            pred = ((Z - 1) * X[(2, 0)] if Z >= 1 else 0) \
                + (X[(1, 1)] if Z >= 1 and N >= 1 else 0) \
                + ((N - 1) * X[(0, 2)] if N >= 1 else 0)
            worst = max(worst, abs(v - pred))
        return worst
    res_tr = chain_residual(Ltr)
    res_dLs = chain_residual(dLs)
    res_dL = chain_residual(dL)
    print(f"  chain-edge additivity residual: full trace {_s(res_tr, 5)} | "
          f"dominant same-block {_s(res_dLs, 5)} | dominant dL (own argmax) {_s(res_dL, 5)}")
    chk("bond_rule_on_live_word_full_trace_chain_additive_1e-30", res_tr < mp.mpf("1e-30"))
    chk("dominant_sameblock_dL_chain_additive_1e-45", res_dLs < mp.mpf("1e-45"))
    chk("switch_is_nonneg_to_rounding", all(v > mp.mpf("-1e-45") for v in switch.values()))
    same_block_b3 = res_dLs
    chk("dL_b1_is_zero_exactly",
        inv_dL["b1_p"] == 0 and inv_dL["b1_n"] == 0)
    # round-trip: rebuild X(2,2) from the cumulants
    rt = (2 * inv_dL["b1_p"] + 2 * inv_dL["b1_n"] + inv_dL["b2_pp"]
          + inv_dL["b2_nn"] + 4 * inv_dL["b2_pn"] + 2 * inv_dL["b3_ppn"]
          + 2 * inv_dL["b3_pnn"] + inv_dL["b4_ppnn"])
    chk("ursell_roundtrip_4He_1e-50", abs(rt - dL[(2, 2)]) < mp.mpf("1e-50"))

    print("\n== (iii) CONTROL: full trace log(tr_free/tr_atom), typed cumulants (log units)")
    for k, v in inv_tr.items():
        print(f"  {k:8} {_s(v, 20)}")
    bond_rule_b3 = max(abs(inv_tr[k]) for k in ("b3_ppp", "b3_ppn", "b3_pnn", "b3_nnn"))
    print(f"  max |b3| full trace = {_s(bond_rule_b3, 5)}  (MarkovBondRuleForcesPairwise predicts 0)")
    # log(z_D) is L_pp of the bond rule: b2_pp should be -log(z_D) = ln(1/z)
    print(f"  b2_pp vs ln(1/z_D): {_s(inv_tr['b2_pp'], 20)} vs {_s(-mp.log(Z_D), 20)}")

    print("\n== (ii) CONTROL: free word's dominant log-weight L_free alone (no bonds), typed cumulants")
    for k, v in inv_Lf.items():
        print(f"  {k:8} {_s(v, 20)}")

    print("\n== (i) THE TEST: dL = L_free - L_atom of the dominant summand, typed cumulants (log units)")
    for k, v in inv_dL.items():
        print(f"  {k:8} {_s(v, 20)}   = {_s(E0 * v, 12)} MeV  [E0-scaled]")

    print("\n== DECOMPOSITION dL = dL_sameblock + switch  (log units)")
    print("   dL_sameblock: free vs atom weight in the atom's OWN block (y cancels);")
    print("   switch: log|a(free, argmax_free)| - log|a(free, argmax_atom)| >= 0, a function of the FREE word only")
    for k, v in inv_dLs.items():
        print(f"  sameblock {k:8} {_s(v, 20)}   switch {_s(inv_sw[k], 20)}   log y_(3A) {_s(inv_gy[k], 20)}")
    print(f"  (complete-graph cumulants of a chain-additive quantity: b3 = -b2(missing edge); see chain residuals above)")

    # ---- SECONDARY: binding-sum dominant |y chi Delta| ----
    dLB = {k: r["LB_free"] - r["LB_atom"] for k, r in rows.items()}
    dLBs = {k: r["dLB_sameblock"] for k, r in rows.items()}
    inv_dLB = ursell_typed(dLB)
    inv_dLBs = ursell_typed(dLBs)
    res_dLB = chain_residual(dLB)
    res_dLBs = chain_residual(dLBs)
    print("\n== SECONDARY: dominant summand of the BINDING sum |y chi Delta| (BindingConcentration's block)")
    for (Z, N, label) in CLUSTERS:
        r = rows[(Z, N)]
        print(f"  {label:9} argmax atom {list(r['dom_binding_sum_atom'])} share {_s(r['share_binding_atom'], 5)} "
              f"runner-up/dom {_s(r['runner_up_ratio_binding_atom'], 5)} | free {list(r['dom_binding_sum_free'])} "
              f"| dLB {_s(dLB[(Z, N)], 12)}  dLB_sameblock {_s(dLBs[(Z, N)], 12)}")
    print(f"  chain-edge additivity residual: dLB {_s(res_dLB, 5)} | dLB same-block {_s(res_dLBs, 5)}  "
          f"(NOT expected to vanish: two-row block, not letter-multiplicative)")
    print("  typed cumulants (log units | MeV):")
    for k, v in inv_dLB.items():
        print(f"    {k:8} {_s(v, 16)} | {_s(E0 * v, 10)} MeV    same-block {_s(inv_dLBs[k], 16)}")
    BdomB = {k: E0 * dLB[k] for k in dLB}
    domB_u = ursell_uniform(BdomB)
    print(f"  uniform-e2 (MeV): e2 {_s(domB_u['e2'], 8)}  b3_3H {_s(domB_u['b3_3H'], 8)}  "
          f"b3_3He {_s(domB_u['b3_3He'], 8)}  b4_4He {_s(domB_u['b4_4He'], 8)}   "
          f"[AME e2 2.2246 b3 +1.8081 / +1.0443]")

    # scale-free ratios
    print("\n== scale-free ratios b3/b2(pn) (E0 cancels)")
    ratios = {k: inv_dL[k] / inv_dL["b2_pn"] for k in ("b3_ppn", "b3_pnn")}
    for k, v in ratios.items():
        print(f"  {k}/b2_pn = {_s(v, 12)}")

    # ---- against AME, corpus uniform convention ----
    B_ame = {(1, 1): ame_binding_mev(1, 2), (1, 2): ame_binding_mev(1, 3),
             (2, 1): ame_binding_mev(2, 3), (2, 2): ame_binding_mev(2, 4),
             (3, 3): ame_binding_mev(3, 6)}
    ame_u = ursell_uniform(B_ame)
    Bdom = {k: E0 * dL[k] for k in dL}
    dom_u = ursell_uniform(Bdom)
    Btr = {k: E0 * Ltr[k] for k in Ltr}
    tr_u = ursell_uniform(Btr)
    print("\n== uniform-e2 convention (the one qou-brng's AME targets are in), MeV")
    print(f"  {'':10} {'AME2020':>14} {'dominant summand':>18} {'full trace':>14}")
    for k in ("e2", "b3_3H", "b3_3He", "b4_4He"):
        print(f"  {k:10} {_s(ame_u[k], 10):>14} {_s(dom_u[k], 10):>18} {_s(tr_u[k], 10):>14}")
    print(f"  scale-free b3/e2:  AME 3H {_s(ame_u['b3_3H']/ame_u['e2'], 8)}  3He {_s(ame_u['b3_3He']/ame_u['e2'], 8)}"
          f"   | dominant 3H {_s(dom_u['b3_3H']/dom_u['e2'], 8)}  3He {_s(dom_u['b3_3He']/dom_u['e2'], 8)}")
    print("\n== per-A growth of dL (dominant) and log(tr_f/tr_a) (full), vs AME B/A (MeV)")
    for zn in ((1, 1), (1, 2), (2, 1), (2, 2), (3, 3)):
        A = sum(zn)
        print(f"  A={A} ({zn}): dL/A {_s(dL[zn]/A, 10)}  E0.dL {_s(Bdom[zn], 10)} MeV  "
              f"E0.logtr {_s(Btr[zn], 10)} MeV  AME B {_s(B_ame[zn], 10)}  "
              f"AME/E0dL {_s(B_ame[zn]/Bdom[zn], 8) if Bdom[zn] != 0 else 'n/a'}")

    def ser(d: dict) -> dict:
        return {k: (_s(v, 40) if isinstance(v, mp.mpf) else v) for k, v in d.items()}

    cluster_rows = []
    for (Z, N, label) in CLUSTERS:
        r = rows[(Z, N)]
        cluster_rows.append({
            "label": label, "Z": Z, "N": N, "A": Z + N,
            "n_strands": r["n_strands"], "n_partitions": r["n_partitions"],
            "word_len_atom": r["word_len_atom"],
            "dominant_atom": list(r["dom_atom"]),
            "dominant_free": list(r["dom_free"]),
            "argmax_binding_sum_atom": list(r["dom_binding_sum_atom"]),
            "argmax_binding_sum_free": list(r["dom_binding_sum_free"]),
            "a_dominant_atom": _s(r["a_dom_atom"], 40),
            "a_dominant_free": _s(r["a_dom_free"], 40),
            "share_of_sum_abs_atom": _s(r["share_atom"], 20),
            "runner_up_over_dominant_atom": _s(r["runner_up_ratio_atom"], 20),
            "runner_up_atom": list(r["runner_up_atom"]),
            "tr_atom": _s(r["tr_atom"], 40), "tr_free": _s(r["tr_free"], 40),
            "L_atom": _s(r["L_atom"], 40), "L_free": _s(r["L_free"], 40),
            "dL_dominant": _s(dL[(Z, N)], 40),
            "log_tr_ratio_full": _s(Ltr[(Z, N)], 40),
            # per-cluster wall time deliberately NOT serialised: `wall_s` is not
            # in qou_substrate's `_EPHEMERAL_META_FIELDS`, so the raw-float64
            # ratchet would read it as a payload float. `provenance.elapsed_s`
            # (declared ephemeral 2026-09-05, bean qou-m549) carries the total.
        })

    witness = {
        "computation": "brng-dominant-summand-ursell",
        "description": (
            "Ursell (typed cluster-cumulant) inversion of the DOMINANT "
            "SUMMAND's own log-weight L(A) = log|y_lambda* chi^lambda*(beta_A)| "
            "of the partition sum, lambda* = argmax|y chi| as the trace defines "
            "it, on the live post-2026-09-05 alternating-core atom word, proton "
            "pin, convention D, for every typed cluster with A <= 4 and 6Li as a "
            "growth check. Tests the live remainder of bean qou-brng after "
            "PR #7181 (multiplicity channel excluded): whether one Wedderburn "
            "block's log-weight carries a connected b_3, which the tr_M bond "
            "rule (MarkovBondRuleForcesPairwise) does not decide. Two controls: "
            "the free word's L alone (no bonds) and the full-trace log ratio "
            "(bond rule predicts b_3 = 0). AME2020 enters only as a target. "
            "Nothing wired, nothing fitted, no route selected by residual."
        ),
        "assertions": assertions,
        "allPassed": bool(ok),
        "parameters": {
            "q0": _s(Q0, 50), "q0_pin": "proton", "convention": "D",
            "z_D": _s(Z_D, 40), "dps": DPS,
            "m_e_MeV": _s(M_E, 20),
            "E0_MeV": _s(E0, 30),
            "E0_source": "mass_binding_dashboard._constants(): m_e/(q0(q0-1)); "
                         "the production B_sym = E0 ln(tr_free/tr_atom) scale. "
                         "No new scale introduced; the #7181 probe's E0/(1-hbar^2) "
                         "differs by 0.99 % and the scale-free rows do not see it.",
            "word": "mass_at_3A_proper.atom_braid_word_3A(Z, N) default "
                    "intra_order='borromean' (alternating core, qou-hu1f ruling "
                    "2026-09-05), include_inter True/False",
            "chi_kernel": "chi_general_word.chi_all_lambda_any (window transfer for the "
                          "non-monotone live word; Rust kernel fallback)",
            "y_lambda": "wedderburn_jones_markov.y_lambda_at(n, Q_MP)",
            "ame_source": "AME2020 vendored table, binding_energy_per_A_keV x A",
            "dominant_definition": "argmax_lambda |y_lambda chi^lambda| (the trace's); "
                                   "argmax of |y chi Delta| recorded separately",
            "lean": ["QOU/Mass/MultiplicityNotExtensive.lean",
                     "QOU/Mass/MarkovBondRuleForcesPairwise.lean",
                     "QOU/BraidKnot/BindingConcentration.lean"],
        },
        "data": {
            "clusters": cluster_rows,
            "cache_provenance_max_abs_diff": _s(worst, 10),
            "dominant_is_two_row": {f"{k[0]},{k[1]}": v for k, v in dom_two_row.items()},
            "ursell_typed_log_units": {
                "dL_dominant": ser(inv_dL),
                "L_free_dominant_control": ser(inv_Lf),
                "log_tr_ratio_full_control": ser(inv_tr),
            },
            "decomposition_log_units": {
                "dL_sameblock": ser(inv_dLs),
                "free_side_argmax_switch": ser(inv_sw),
                "log_y_onerow_of_3A": ser(inv_gy),
                "per_cluster": {f"{k[0]},{k[1]}": {
                    "dL": _s(dL[k], 30), "dL_sameblock": _s(dLs[k], 30),
                    "switch": _s(switch[k], 30), "log_y_onerow": _s(gy[k], 30)}
                    for k in dL},
                "onerow_character_max_abs_err_vs_letter_product": _s(onerow_err, 10),
            },
            "dominant_atom_is_onerow": {f"{k[0]},{k[1]}": v for k, v in onerow_dom.items()},
            "chain_edge_additivity_residual": {
                "full_trace_log_ratio": _s(res_tr, 10),
                "dominant_sameblock_dL": _s(res_dLs, 10),
                "dominant_dL_own_argmax": _s(res_dL, 10),
                "binding_sum_dominant_dLB": _s(res_dLB, 10),
                "binding_sum_dominant_dLB_sameblock": _s(res_dLBs, 10),
            },
            "secondary_binding_sum_dominant": {
                "definition": "argmax_lambda |y_lambda chi^lambda Delta_lambda|, Delta = (-1)^{n(lambda)} f^lambda",
                "per_cluster": {f"{k[0]},{k[1]}": {
                    "argmax_atom": list(rows[k]["dom_binding_sum_atom"]),
                    "argmax_free": list(rows[k]["dom_binding_sum_free"]),
                    "share_atom": _s(rows[k]["share_binding_atom"], 15),
                    "runner_up_over_dominant_atom": _s(rows[k]["runner_up_ratio_binding_atom"], 15),
                    "dLB": _s(dLB[k], 30), "dLB_sameblock": _s(dLBs[k], 30)} for k in dLB},
                "ursell_typed_log_units": ser(inv_dLB),
                "ursell_typed_sameblock_log_units": ser(inv_dLBs),
                "ursell_typed_MeV_E0_scaled": ser({k: E0 * v for k, v in inv_dLB.items()}),
                "uniform_e2_convention_MeV": ser(domB_u),
            },
            "ursell_typed_dominant_MeV_E0_scaled": ser({k: E0 * v for k, v in inv_dL.items()}),
            "scale_free_b3_over_b2pn_dominant": ser(ratios),
            "uniform_e2_convention_MeV": {
                "AME2020": ser(ame_u),
                "dominant_summand_E0_scaled": ser(dom_u),
                "full_trace_E0_scaled": ser(tr_u),
            },
            "bond_rule_control_max_abs_b3_full_trace": _s(bond_rule_b3, 10),
            "per_A": {f"{k[0]},{k[1]}": {
                "dL_dominant": _s(dL[k], 30), "E0_dL_MeV": _s(Bdom[k], 20),
                "E0_log_tr_ratio_MeV": _s(Btr[k], 20),
                "AME_B_MeV": _s(B_ame[k], 20)} for k in B_ame},
        },
        "provenance": {
            "headSha": _head_sha(),
            "producer": "computations/brng_dominant_summand_ursell_probe.py",
            "bean": "qou-m8f3 (qou-brng live remainder)",
            "elapsed_s": round(time.monotonic() - t0, 3),
        },
    }
    WitnessBuilder.stamp_staleness_metadata(
        witness, script_path=__file__, engine="python",
        q0_anchor="proton",
        q0_anchor_reason=("AGENTS.md 2026-08-07 owner directive: experimental "
                          "pin is the default for all new compute; every chi, "
                          "y_lambda and E0 here is at the proton q0"),
        q0_value=_s(Q0, 30))
    out = HERE / "brng-dominant-summand-ursell.witness.json"
    out.write_text(json.dumps(witness, indent=2, ensure_ascii=False) + "\n")
    print(f"\nassertions {sum(assertions.values())}/{len(assertions)}  "
          f"witness -> {out.relative_to(ROOT)}")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
