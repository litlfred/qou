#!/usr/bin/env python3
"""gamma_gamma_bond_is_pair_independent_probe.py — does the gamma-gamma bond
give a PAIR-DEPENDENT factor, and can it therefore sign-mix b_3?  (qou-ix0x,
Option 1; junction of qou-ales and qou-q8vl)

## The question, and why it decides Option 1

`QOU.MassTheory.B3SignOneRoot.b3corpus_chain` proves, exactly,

    b3corpus f01 1 f12 = -((f01 - 1) * (f12 - 1))

so on the production A = 3 CHAIN, **b_3 > 0 iff EXACTLY ONE of the two bond
factors exceeds 1**.  (A bond above 1 is NECESSARY, NOT SUFFICIENT: flipping
BOTH leaves b_3 byte-identical.  The AGENTS.md extensive-term bullet and the
Ursell audit section 4 both state the weaker form.)

`PnBetweennessBlocksSignMixed` (bean qou-q8vl) reduces the escape to exactly
two hypotheses -- the AVERAGING of the pn letter, and AFFINENESS of the
interface law `mu = z + d` -- and records as open: *"a THIRD bond family that
supplies the sign-mixed pattern by derivation"*.

The owner ruled 2026-09-08 (bean qou-ales) that every canonical braid word is
selected by gamma-gamma pair production plus the confinement SDP.  Step 3
MEASURED the selected bond `G^3 = (sigma_2 sigma_3^-1)^3` unbinding the
diproton -- ratio 1.001058 > 1 -- and `QOU/Mass/GammaGammaEscapesSingleCrossing`
proves why that does not collide with the single-crossing obstruction.  Step 8's
own not-claimed list names *"the dineutron side"*.  So `mu_pp > 1` is derived
and the other two are UNMEASURED.  This probe measures them.

## Why the answer is not obvious in either direction

`Mass.StrandLayoutForcesChain.crossesBlocks_iff` : `block m != block (m+1)`
iff `m % 3 == 2`.  So `sigma_2` crosses between the two nucleon blocks, and
`sigma_3` (3 % 3 = 0) does NOT -- it lives INSIDE nucleon 1's window.  The
gamma-gamma bond `G^3` therefore REACHES INTO a nucleon block, which is exactly
the `hlow`/`hup` hypothesis that `Mass.ProductionChainBondProduct` needs for

    tr_M(W_atom) / tr_M(W_free) = prod_bonds (z + d_b).

Under that theorem the ratio depends only on the bond LETTERS and not at all on
the nucleon blocks -- so a pair-INDEPENDENT bond word would give three EQUAL
bond factors, which can never be sign-mixed.  `G^3` is outside its hypotheses,
so the ratio MAY depend on the blocks.  Whether it does is the measurement.

RESULT, recorded here so the file does not read as though the expectation held:
it DOES depend on them (spread 4.47e-4 vs the template's 1.6e-61), so the
pair-independence this probe was written to expect is REFUTED.  Option 1 closes
for a different reason -- all four ordered pairs exceed 1, so no chain gets
exactly one bond above 1.

## Anti-fit

Nothing here is tuned.  The bond word is fixed by an owner ruling dated three
days before this probe, made for reasons unrelated to `b_3`; the sign condition
is Lean-proved; the nucleon blocks are `build_atom_nf`'s, unmodified.  The
expected outcome (pair-INDEPENDENCE, hence Option 1 closing structurally) is
written into bean qou-ix0x BEFORE this ran, so a negative cannot be re-read as
selection against the target.  All FOUR ordered pair types -- pp, pn, np, nn --
are reported whatever they say, and no bond word is searched over for a closer
number.  `np` is not a fourth datum but the ORDER-REVERSAL control on `pn`; it
was added after the first run showed mu_pn = mu_nn, to test whether that was a
pair rule or a second-nucleon rule.  It is the latter.

PRECISION: mpmath end to end at 60 dps, seeded from `Q_50_DIGIT_STR` (never the
float64 `q_parameter.Q`).  Proton pin, convention D.  Machinery reused verbatim
from `gamma_gamma_h3_psd_selector_probe` (nucleon_block, vertex_pow,
word_image, tr_m6) so the pp column reproduces step 3 as a control.
"""
from __future__ import annotations

import datetime
import json
import os
import subprocess
import sys
import time
from pathlib import Path

_ROOT = Path(__file__).resolve().parents[2]
for _p in ("tools/pyhecke/python", "tools/qou-substrate/python",
           "computations/substrate", "computations/hecke", "computations"):
    sys.path.insert(0, str(_ROOT / _p))

import mpmath as mp  # noqa: E402

from hoefsmit_mpmath import BlockCacheMP, seminormal_matrices_mp  # noqa: E402
from q_parameter import Q_50_DIGIT_STR, Q_MP  # noqa: E402
from pyhecke.wedderburn import partitions_of  # noqa: E402
from y_lambda_su_n import y_lambda_su_n  # noqa: E402

DPS = 60
mp.mp.dps = DPS
TOL = mp.mpf("1e-40")


def _head_sha() -> str:
    """Repo HEAD at emission time, for the provenance audit's REQUIRED_FIELDS.

    Returns "" when git is unavailable rather than fabricating a sha; the audit
    reads blank as missing, which is the honest state off a checkout.
    """
    try:
        return subprocess.run(
            ["git", "-C", str(Path(__file__).resolve().parent), "rev-parse", "HEAD"],
            capture_output=True, text=True, check=True,
        ).stdout.strip()
    except (OSError, subprocess.CalledProcessError):
        return ""


# --- words: verbatim from gamma_gamma_h3_psd_selector_probe --------------
def vertex(i: int, h):
    """sigma_i sigma_{i+1}^-1 as (c, d, gen) triples (sigma^-1 = sigma - h)."""
    return [(mp.mpf(1), mp.mpf(0), i), (mp.mpf(1), -h, i + 1)]


def vertex_pow(i: int, k: int, h):
    w = []
    for _ in range(k):
        w += vertex(i, h)
    return w


def nucleon_block(kind: str, h, offset: int = 0):
    """The 11-letter per-nucleon block of `build_atom_nf` on (offset, offset+1)."""
    one, zero = mp.mpf(1), mp.mpf(0)
    g0, g1 = offset, offset + 1
    w = []
    for _ in range(3):                       # B_3 = (sigma_0 sigma_1^-1)^3
        w.append((one, zero, g0))
        w.append((one, -h, g1))
    if kind == "p":                          # uu@0, ud@0, ud@1
        w += [(one, zero, g0), (one, -h / 2, g0), (one, -h / 2, g1)]
    else:                                    # ud@0, ud@0, dd@1
        w += [(one, -h / 2, g0), (one, -h / 2, g0), (one, -h, g1)]
    w += [(one, zero, g0), (one, zero, g0)]  # gluon sigma_0^2 (qou-1qsw)
    return w


def word_image(sigmas, dim, word):
    M = mp.eye(dim)
    I = mp.eye(dim)
    for c, d, g in word:
        M = M * (c * sigmas[g] + d * I)
    return M


def trace(M, dim):
    return mp.fsum(M[i, i] for i in range(dim))


def main() -> int:
    t0 = time.time()
    anchor = os.environ.get("QOU_Q0_ANCHOR", "").strip().lower()
    if anchor in ("ideal", "muon", "canonical"):
        raise SystemExit("PROTON-pin producer (owner directive 2026-08-07); "
                         "refusing a muon override")

    q = Q_MP
    qi = 1 / q
    h = q - qi
    z_d = q ** 3 / (q ** 2 + 1)
    cache = BlockCacheMP(q, h)

    print(f"gamma-gamma bond: pair-dependent or not?  proton pin, convention D, {DPS} dps")
    print("=" * 78)
    print(f"  q0  = {Q_50_DIGIT_STR[:34]}...   (Q_50_DIGIT_STR)")
    print(f"  h   = {mp.nstr(h, 15)}    z_D = {mp.nstr(z_d, 15)}")

    parts6 = [tuple(p) for p in partitions_of(6)]
    y6 = y_lambda_su_n(6, q, 2)
    y6 = {tuple(k): mp.mpf(v) for k, v in y6.items()}
    reps6 = {lam: seminormal_matrices_mp(lam, cache=cache) for lam in parts6}
    print(f"  H_6: {len(parts6)} blocks; y > 0 on {[lam for lam in parts6 if y6[lam] > TOL]}")

    def tr_m6(word):
        return mp.fsum(
            y6[lam] * trace(word_image(reps6[lam][0], reps6[lam][1], word), reps6[lam][1])
            for lam in parts6)

    bonds = {
        "template_s2": [(mp.mpf(1), mp.mpf(0), 2)],
        "G3": vertex_pow(2, 3, h),
    }
    # "np" is the ORDER-REVERSAL control: same unordered pair as "pn".  If the
    # bond factor is a function of the PAIR it must equal mu_pn; if it is a
    # function of the SECOND nucleon only (sigma_3 reaches into block 1, and
    # only block 1) it must equal mu_pp instead.
    pairs = {"pp": ("p", "p"), "pn": ("p", "n"), "np": ("n", "p"), "nn": ("n", "n")}

    print(f"\n  {'pair':>5}{'bond':>14}{'tr_M(W_free)':>26}{'tr_M(W_atom)':>26}{'mu = atom/free':>22}  >1?")
    mu = {}
    tr_free_by_pair = {}
    for pname, (k0, k1) in pairs.items():
        w_free = nucleon_block(k0, h, 0) + nucleon_block(k1, h, 3)
        tr_free = tr_m6(w_free)
        tr_free_by_pair[pname] = tr_free
        for bname, bw in bonds.items():
            tr_atom = tr_m6(w_free + bw)
            r = tr_atom / tr_free
            mu[(pname, bname)] = r
            print(f"  {pname:>5}{bname:>14}{mp.nstr(tr_free, 20):>26}"
                  f"{mp.nstr(tr_atom, 20):>26}{mp.nstr(r, 18):>22}  {'YES' if r > 1 else 'no'}")

    # --- is the ratio pair-dependent? -----------------------------------
    print(f"\n  pair-dependence of mu (max spread across pp/pn/nn):")
    spread = {}
    for bname in bonds:
        vals = [mu[(p, bname)] for p in pairs]
        spread[bname] = max(vals) - min(vals)
        print(f"    {bname:>12}: spread = {mp.nstr(spread[bname], 12)}"
              f"   ({'PAIR-DEPENDENT' if spread[bname] > TOL else 'pair-INDEPENDENT'})")

    # WHERE does the order-dependence live?  A sibling arc (qou-99qc, #7295) proves
    # the ALTERNATING character is order-blind: a 1-dim rep sends a word to a
    # PRODUCT of scalars, so it sees only the multiset of letter shifts, never the
    # order or which generator each letter sits on.  That looks like it collides
    # with the mu_pn != mu_np measured above.  It does not, and this localises why:
    # tr_M is a y-weighted sum over ALL blocks, and only the >=2-dimensional ones
    # can resolve order.  Measured per block rather than argued.
    print(f"\n  per-block source of the pn/np gap (1-dim blocks are order-BLIND):")
    print(f"  {'block':>10}{'dim':>5}{'y_lambda':>16}{'chi(pn) - chi(np)':>24}")
    onedim_gap = mp.mpf(0)
    multidim_gap = mp.mpf(0)
    w_pn = nucleon_block("p", h, 0) + nucleon_block("n", h, 3) + bonds["G3"]
    w_np = nucleon_block("n", h, 0) + nucleon_block("p", h, 3) + bonds["G3"]
    for lam in parts6:
        sig, dim, _ = reps6[lam]
        g = trace(word_image(sig, dim, w_pn), dim) - trace(word_image(sig, dim, w_np), dim)
        if dim == 1:
            onedim_gap += abs(y6[lam] * g)
        else:
            multidim_gap += abs(y6[lam] * g)
        if abs(g) > TOL or dim == 1:
            print(f"  {str(lam):>10}{dim:>5}{mp.nstr(y6[lam], 8):>16}{mp.nstr(g, 12):>24}")
    print(f"    1-dim blocks total |y.dchi| = {mp.nstr(onedim_gap, 8)}   "
          f">=2-dim total = {mp.nstr(multidim_gap, 8)}")

    # control: the template bond must reproduce z_D (connected-sum multiplicativity)
    dev_template = max(abs(mu[(p, "template_s2")] - z_d) for p in pairs)
    # one-sidedness: is mu a function of the pair, or of the second nucleon alone?
    sym_gap = abs(mu[("pn", "G3")] - mu[("np", "G3")])          # pair-symmetry
    second_gap = max(abs(mu[("np", "G3")] - mu[("pp", "G3")]),   # second-nucleon rule
                     abs(mu[("pn", "G3")] - mu[("nn", "G3")]))
    print(f"  ONE-SIDEDNESS  |mu_pn - mu_np| (pair-symmetric?)      = {mp.nstr(sym_gap, 12)}")
    print(f"  ONE-SIDEDNESS  worst |mu - mu(same 2nd nucleon)|      = {mp.nstr(second_gap, 12)}")
    print(f"  CONTROL  template sigma_2 ratio vs z_D, worst over pairs: {mp.nstr(dev_template, 6)}")
    dev_step3 = abs(mu[("pp", "G3")] - mp.mpf("1.001058"))
    print(f"  CONTROL  mu_pp(G^3) vs step-3's recorded 1.001058: {mp.nstr(dev_step3, 6)}")

    # --- the chain sign condition ---------------------------------------
    # 3He = ppn  -> chain bonds (pp, pn);  3H = pnn -> chain bonds (pn, nn).
    def b3corpus_chain(f01, f12):
        return -((f01 - 1) * (f12 - 1))

    print(f"\n  chain sign test  b3 = -((mu_a - 1)(mu_b - 1))   [B3SignOneRoot.b3corpus_chain]")
    print(f"  {'atom':>6}{'bond':>14}{'mu_a':>20}{'mu_b':>20}{'b3':>22}  sign")
    chain = {}
    for aname, (ea, eb) in (("3He(ppn)", ("pp", "pn")), ("3H(pnn)", ("pn", "nn"))):
        for bname in bonds:
            fa, fb = mu[(ea, bname)], mu[(eb, bname)]
            b3 = b3corpus_chain(fa, fb)
            n_above = sum(1 for f in (fa, fb) if f > 1)
            chain[(aname, bname)] = {"mu_a": fa, "mu_b": fb, "b3": b3, "n_above_one": n_above}
            print(f"  {aname:>6}{bname:>14}{mp.nstr(fa, 16):>20}{mp.nstr(fb, 16):>20}"
                  f"{mp.nstr(b3, 16):>22}  {'POSITIVE' if b3 > 0 else 'negative'}"
                  f"  ({n_above} bond(s) > 1)")

    # --- assertions ------------------------------------------------------
    a = []
    a.append(("the template bond reproduces z_D on EVERY pair (connected-sum "
              "multiplicativity control)", dev_template < mp.mpf("1e-40")))
    a.append(("the template bond is pair-INDEPENDENT, so it can never sign-mix",
              spread["template_s2"] < TOL))
    a.append(("step-3's mu_pp(G^3) is reproduced to its quoted precision",
              dev_step3 < mp.mpf("1e-6")))
    a.append(("mu_pp(G^3) > 1: the gamma-gamma bond DOES unbind the diproton",
              mu[("pp", "G3")] > 1))
    gg_dep = spread["G3"] > TOL
    a.append(("the gamma-gamma bond IS pair-dependent (it reaches into a nucleon "
              "block via sigma_3, so the bond-product theorem does not apply)", gg_dep))
    he_pos = chain[("3He(ppn)", "G3")]["b3"] > 0
    h3_pos = chain[("3H(pnn)", "G3")]["b3"] > 0
    a.append(("REPORTED, not required: whether G^3 makes 3He's b3 positive -- "
              f"it is {'POSITIVE' if he_pos else 'negative'}", True))
    a.append(("REPORTED, not required: whether G^3 makes 3H's b3 positive -- "
              f"it is {'POSITIVE' if h3_pos else 'negative'}", True))
    a.append(("the gamma-gamma bond is NOT symmetric under swapping the two "
              "nucleons: mu_pn != mu_np, so it is not a function of the pair",
              sym_gap > TOL))
    # MEASURED, not derived: the equalities below are what the numbers say.  A
    # candidate mechanism is that G^3's only block-interior generator is sigma_3,
    # which StrandLayoutForcesChain places inside block 1 (3 % 3 = 0 does not
    # cross).  That is NOT proved here -- G^3 also carries sigma_2, which is
    # ADJACENT to block 0's sigma_1 and therefore does not far-commute past it,
    # so no commutation argument closes it.  Stated as an observation.
    a.append(("MEASURED (mechanism not proved): mu is a function of the SECOND "
              "nucleon alone -- mu_np = mu_pp and mu_pn = mu_nn, to 1.6e-61",
              second_gap < TOL))
    a.append(("EVERY pair type exceeds 1 under G^3, so no chain gets exactly one "
              "bond above 1 and b3 < 0 on both atoms",
              all(mu[(p, "G3")] > 1 for p in pairs)))
    a.append(("CROSS-ARC CONSISTENCY (qou-99qc / #7295): the 1-dimensional blocks "
              "contribute NOTHING to the pn/np gap -- a 1-dim rep is a product of "
              "scalars and is order-blind, so their order-blindness and this "
              "probe's order-DEPENDENCE are not in conflict", onedim_gap < TOL))
    a.append(("the whole pn/np gap is carried by the >=2-dimensional blocks",
              multidim_gap > TOL))
    a.append(("the two chains AGREE in sign under G^3 (a single bond family "
              "cannot give one atom a positive b3 and the other a negative one "
              "without that being a finding in itself)", he_pos == h3_pos))

    print("\n  assertions:")
    ok = True
    for name, passed in a:
        ok &= bool(passed)
        print(f"    [{'PASS' if passed else 'FAIL'}] {name}")

    w = {
        "schema": "witness/v1",
        "computedAt": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "engine": "mpmath",
        "scriptFile": Path(__file__).name,
        "commitSha": _head_sha(),
        "q0Anchor": "proton",
        "q0AnchorReason": "seeded from Q_50_DIGIT_STR; convention D (z = q^3/(q^2+1))",
        "description": (
            "Measures whether the gamma-gamma-selected bond G^3 = (sigma_2 sigma_3^-1)^3 "
            "gives a PAIR-DEPENDENT bond factor, and evaluates the Lean-proved chain sign "
            "condition b3 = -((f01-1)(f12-1)) on both A=3 chains. Decides Option 1 of "
            "qou-brng at the qou-ales / qou-q8vl junction: a pair-INDEPENDENT bond word "
            "gives three equal bond factors and can never be sign-mixed. Nothing is tuned; "
            "the bond word is fixed by the owner's 2026-09-08 ruling."
        ),
        "dps": DPS,
        "q0": Q_50_DIGIT_STR,
        "z_D": mp.nstr(z_d, 30),
        "mu": {f"{p}|{b}": mp.nstr(mu[(p, b)], 30) for p in pairs for b in bonds},
        "tr_free_by_pair": {p: mp.nstr(v, 30) for p, v in tr_free_by_pair.items()},
        "pair_spread": {b: mp.nstr(spread[b], 30) for b in bonds},
        "gamma_gamma_pair_dependent": bool(gg_dep),
        "order_dependence_by_block_dim": {
            "one_dim_total_abs_y_dchi": mp.nstr(onedim_gap, 30),
            "multi_dim_total_abs_y_dchi": mp.nstr(multidim_gap, 30),
            "reading": ("the pn/np gap is carried ENTIRELY by the >=2-dim blocks; "
                        "the 1-dim blocks are order-blind, which reconciles this "
                        "probe with qou-99qc/#7295's altChar order-blindness result"),
        },
        "one_sidedness": {
            "pair_symmetry_gap_mu_pn_minus_mu_np": mp.nstr(sym_gap, 30),
            "second_nucleon_rule_worst_gap": mp.nstr(second_gap, 30),
            "reading": ("MEASURED: mu depends only on the SECOND nucleon. The "
                        "mechanism is NOT established -- sigma_3 lies inside block 1, "
                        "but G^3 also carries sigma_2, adjacent to block 0's sigma_1, "
                        "so far-commutation does not explain it."),
        },
        "chain": {f"{a_}|{b_}": {k: (mp.nstr(v, 30) if not isinstance(v, int) else v)
                                 for k, v in d.items()}
                  for (a_, b_), d in chain.items()},
        "controls": {
            "template_vs_z_D_worst": mp.nstr(dev_template, 12),
            "mu_pp_G3_vs_step3_1p001058": mp.nstr(dev_step3, 12),
        },
        "assertions": [{"name": n, "passed": bool(p)} for n, p in a],
        "allPassed": bool(ok),
        "elapsed_seconds_note": "wall time is not recorded; it is not a result",
    }
    out = Path(__file__).with_name("gamma-gamma-bond-is-pair-independent.witness.json")
    out.write_text(json.dumps(w, indent=1) + "\n")
    print(f"\n  witness -> {out.relative_to(Path(__file__).resolve().parents[2])}")
    print(f"  wall {time.time() - t0:.1f}s")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
