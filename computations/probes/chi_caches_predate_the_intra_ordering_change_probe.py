"""The committed chi caches were built under the SUPERSEDED intra ordering.

WHAT THIS IS.  `atom_braid_word_3A`'s intra-nucleon ordering changed on
2026-09-05 (bean `qou-hu1f`, owner ruling, commits 7db032fb48 / deb9ff5728):
each nucleon's confinement core is now ALTERNATING (`intra_order="borromean"`,
the default) where it used to be GROUPED.  The six `chi-<atom>-h<n>-at-q0-50dps`
caches were computed 2026-08-10, twenty-six days earlier.

They are produced by `chi_at_q0_via_hoefsmit_mpfr.py`, which calls
`atom_braid_word_3A(Z, N)` at line 96 with NO `intra_order` argument -- so a
fresh run today produces the borromean word, and the committed caches do not.
That is import-cone staleness: the producer's own source can be byte-stable
while the module it CALLS changed, and a file-local `git diff` cannot see it.

WHY IT MATTERS BEYOND ONE FILE.  84 live (non-deprecated) scripts read these
caches, `aK_via_lp_dual_full.py` among them, and through it
`a-K-via-lp-dual-full.witness.json` and everything computed from that.

WHAT `qou-hu1f` ALREADY COVERS, AND WHAT IT DOES NOT.  That bean measured the
ordering change's blast radius carefully and split it: log-ratio routes
(`tr_M(W_atom)/tr_M(W_free)`) are provably immune by connected-sum
multiplicativity, and difference routes such as `binding_canonical` scale by a
computable per-atom factor `R_quark` (3.785x at 2H up to 14.325x at 4He).
**It does not mention the chi caches or `chi_at_q0_via_hoefsmit_mpfr` at all**
-- grepped, zero hits.  So this surface is outside the measured split, and the
per-atom scalar factor does NOT describe it, as check 2 below shows.

THE FOUR THINGS MEASURED HERE

1. The two orderings give materially different words.  35 letters for A = 3,
   24 of them differing, for both atoms.

2. The character change is NOT a per-atom scalar.  |chi_borromean/chi_grouped|
   spans 12.04x (tritium) and 11.29x (helium-3) across the two-row partitions,
   and TWO OF FIVE partitions CHANGE SIGN ([8,1] and [5,4], in both atoms).
   So `R_quark` -- one factor per atom -- cannot describe this surface, and a
   reader who assumes the ordering change is a uniform rescale here is wrong.

3. The committed cache matches exactly one ordering, and this probe says which.
   Measured: GROUPED to ~3e-50 (the arithmetic floor), against ~1.3 RELATIVE
   for borromean.  Not a subtle drift -- a different number.

4. 🛑 IT MOVES A PUBLISHED RESULT.  `argmin(t) == argmin(w)` -- the
   atom-independence of the O3' selection, measured 6/6 and merged in #6841 /
   #6847 -- HOLDS under grouped and FAILS under borromean:

       tritium    grouped    argmin(t) = [5,4] = argmin(w)     agree
       tritium    borromean  argmin(t) = [7,2], argmin(w) = [5,4]   DIFFER

   `o3prime_selection_is_atom_independent_probe.py` states its own falsifier as
   "a single row where argmin(t) != argmin(w) would refute it".  Tritium under
   the live ordering is that row.  The dim-vs-|chi| concordance moves the same
   way, 9/10 and 10/10 under grouped to 6/10 and 6/10 under borromean.

WHAT IS NOT DECIDED HERE, DELIBERATELY.  Whether to regenerate the caches.
That is 84 consumers plus a 22.5-minute helium-4 recompute (`compute_time_sec`
1352.39 in its own witness), it moves numbers across the binding arc, and
`qou-hu1f` reached the same boundary on the same day for the same reason: a
change of this size "needs an owner ruling, not a probe".  This probe
establishes that the fix is NEEDED and measures what it would move.  It does
not make it.

SCOPE OF THE ASSERTIONS.  All four are stable under a regeneration -- 1, 2 and
4 compare the two orderings directly and do not read the cache at all, and 3
asserts only that the cache matches ONE of the two to 1e-40, reporting WHICH as
a witness field rather than asserting it.  So this probe stays green when the
caches are refreshed, and the `cache_matches` field flips from "grouped" to
"borromean" where a reader can see it.
"""
from __future__ import annotations

import json
import math
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))

import _path_bridge  # noqa: F401,E402

from mpmath import mp  # noqa: E402

import chi_at_q0_via_hoefsmit_mpfr as CHI  # noqa: E402
import mass_at_3A_proper as MA  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402
from _precision import set_compute_dps, fmt  # noqa: E402

set_compute_dps()

CHECKS: list[tuple[str, bool]] = []
_ORIG_WORD = MA.atom_braid_word_3A


def check(name: str, ok: bool, detail: str = "") -> None:
    CHECKS.append((name, ok))
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + (f" -- {detail}" if detail else ""),
          flush=True)


def f_lambda(lam: tuple[int, ...]) -> int:
    """#SYT(lambda), exact integer by hook lengths."""
    d = 1
    for i, row in enumerate(lam):
        for j in range(row):
            arm = row - j - 1
            leg = sum(1 for r in range(i + 1, len(lam)) if lam[r] > j)
            d *= arm + leg + 1
    return math.factorial(sum(lam)) // d


def chi_at(atom: str, Z: int, N: int, q: str, order: str) -> dict:
    """Per-partition chi under a FORCED intra ordering, writing nothing.

    `incremental=False` returns without touching disk -- the incremental path
    persists each partition as it goes, which would overwrite the very cache
    this probe is measuring.
    """
    CHI.atom_braid_word_3A = (
        lambda z, n, **kw: _ORIG_WORD(z, n, intra_order=order, **kw))
    try:
        return CHI.build_chi_cache_at_q0(atom, Z, N, q, dps=50,
                                         incremental=False)
    finally:
        CHI.atom_braid_word_3A = _ORIG_WORD


ATOMS = [("tritium", 1, 2, 9), ("helium-3", 2, 1, 9)]


def main() -> int:
    aK = json.loads((HERE.parent / "a-K-via-lp-dual-full.witness.json").read_text())
    q = aK["q0Value"]
    print(f"=== chi caches vs the 2026-09-05 intra-ordering change ===\n"
          f"    q0 = {q[:22]} ({aK['q0Anchor']})", flush=True)

    # 1 -- the words themselves
    word_rows = []
    for atom, Z, N, _n in ATOMS:
        g = _ORIG_WORD(Z, N, intra_order="grouped")
        b = _ORIG_WORD(Z, N, intra_order="borromean")
        diff = sum(1 for x, y in zip(g, b) if x != y)
        word_rows.append({"atom": atom, "letters": len(b), "differing": diff})
        print(f"  {atom:<10} word: {len(b)} letters, {diff} differ between "
              f"grouped and borromean", flush=True)
    check("the two intra orderings give MATERIALLY DIFFERENT words — this is "
          "not a relabelling",
          all(r["differing"] > 0 for r in word_rows),
          ", ".join(f"{r['atom']} {r['differing']}/{r['letters']}"
                    for r in word_rows))

    rows = []
    for atom, Z, N, n in ATOMS:
        g = chi_at(atom, Z, N, q, "grouped")
        b = chi_at(atom, Z, N, q, "borromean")
        cache = json.loads(
            (HERE.parent / f"chi-{atom}-h{n}-at-q0-50dps.witness.json").read_text())
        gm = {tuple(r["partition"]): mp.mpf(r["chi_lambda"]) for r in g["by_partition"]}
        bm = {tuple(r["partition"]): mp.mpf(r["chi_lambda"]) for r in b["by_partition"]}
        wm = {tuple(r["partition"]): mp.mpf(r["y_lambda"]) for r in g["by_partition"]}
        cm = {tuple(r["partition"]): mp.mpf(r["chi_lambda"])
              for r in cache["by_partition"]}
        two = [l for l in gm if len(l) <= 2 and wm[l] != 0]

        rat = {l: bm[l] / gm[l] for l in two if gm[l] != 0}
        flips = [list(l) for l, v in rat.items() if v < 0]
        ar = [abs(v) for v in rat.values()]

        d_g = max(abs(cm[l] - gm[l]) / abs(cm[l]) for l in two if cm[l] != 0)
        d_b = max(abs(cm[l] - bm[l]) / abs(cm[l]) for l in two if cm[l] != 0)

        sel = {}
        for name, chi in (("grouped", gm), ("borromean", bm)):
            t = {l: abs(chi[l]) * wm[l] for l in two}
            srt = sorted(t.values())
            at = min(t, key=t.get)
            aw = min(two, key=lambda l: wm[l])
            dm = [f_lambda(l) for l in two]
            ch = [abs(chi[l]) for l in two]
            C = D = 0
            for i in range(len(two)):
                for j in range(i + 1, len(two)):
                    if dm[i] == dm[j] or ch[i] == ch[j]:
                        continue
                    if (dm[i] > dm[j]) == (ch[i] > ch[j]):
                        C += 1
                    else:
                        D += 1
            sel[name] = {"argmin_t": list(at), "argmin_w": list(aw),
                         "agree": at == aw, "margin": fmt(srt[1] / srt[0]),
                         "dim_chi_concordance": f"{C}/{C + D}"}

        rows.append({
            "atom": atom, "Z": Z, "N": N, "n": n,
            "abs_ratio_min": fmt(min(ar)), "abs_ratio_max": fmt(max(ar)),
            "abs_ratio_spread": fmt(max(ar) / min(ar)),
            "sign_flips": flips, "n_two_row": len(two),
            "cache_vs_grouped": fmt(d_g), "cache_vs_borromean": fmt(d_b),
            "cache_matches": "grouped" if d_g < d_b else "borromean",
            "selection": sel,
        })
        print(f"\n  {atom} (Z={Z},N={N}) — {len(two)} two-row partitions", flush=True)
        print(f"    |chi_borromean/chi_grouped| spans {mp.nstr(min(ar),6)} .. "
              f"{mp.nstr(max(ar),6)} = {mp.nstr(max(ar)/min(ar),6)}x", flush=True)
        print(f"    SIGN CHANGES on {len(flips)}/{len(rat)}: {flips}", flush=True)
        print(f"    committed cache vs grouped   {mp.nstr(d_g,4)}", flush=True)
        print(f"    committed cache vs borromean {mp.nstr(d_b,4)}"
              f"   -> cache is {rows[-1]['cache_matches'].upper()}", flush=True)
        for name in ("grouped", "borromean"):
            s = sel[name]
            print(f"    {name:<10} argmin(t)={str(s['argmin_t']):>8} "
                  f"argmin(w)={str(s['argmin_w']):>8}  agree={s['agree']}  "
                  f"margin={mp.nstr(mp.mpf(s['margin']),6)}x  "
                  f"dim~|chi| {s['dim_chi_concordance']}", flush=True)

    check("the ordering change is NOT a per-atom scalar — |chi| ratios spread "
          "by an order of magnitude AND some characters change SIGN, so "
          "qou-hu1f's per-atom R_quark factor does not describe this surface",
          all(mp.mpf(r["abs_ratio_spread"]) > 2 and r["sign_flips"] for r in rows),
          "; ".join(f"{r['atom']} spread {mp.nstr(mp.mpf(r['abs_ratio_spread']),6)}x, "
                    f"{len(r['sign_flips'])} sign flips {r['sign_flips']}"
                    for r in rows))

    check("the committed cache matches exactly ONE of the two orderings, to "
          "1e-40 — it is not corrupt and not some third thing; WHICH one is "
          "reported in the witness rather than asserted, so this stays green "
          "after a regeneration",
          all(min(mp.mpf(r["cache_vs_grouped"]),
                  mp.mpf(r["cache_vs_borromean"])) < mp.mpf("1e-40")
              for r in rows),
          "; ".join(f"{r['atom']} matches {r['cache_matches']} "
                    f"(other side off by {mp.nstr(max(mp.mpf(r['cache_vs_grouped']), mp.mpf(r['cache_vs_borromean'])),4)} relative)"
                    for r in rows))

    moved = [r for r in rows
             if r["selection"]["grouped"]["agree"]
             != r["selection"]["borromean"]["agree"]]
    check("🛑 the ordering change MOVES A PUBLISHED RESULT — argmin(t) == "
          "argmin(w) (the O3' atom-independence of #6841/#6847, measured 6/6) "
          "holds under grouped and FAILS under borromean on tritium",
          len(moved) > 0,
          "; ".join(f"{r['atom']}: grouped agree="
                    f"{r['selection']['grouped']['agree']} -> borromean agree="
                    f"{r['selection']['borromean']['agree']} "
                    f"(argmin(t) {r['selection']['grouped']['argmin_t']} -> "
                    f"{r['selection']['borromean']['argmin_t']})" for r in moved))

    consumers = 84
    print(f"\n  BLAST RADIUS: {consumers} live (non-deprecated) scripts read these "
          f"caches.\n  NOT regenerated here — that is an owner decision, the same "
          f"boundary\n  qou-hu1f reached on the same day for the same reason.",
          flush=True)

    w = WitnessBuilder("chi-caches-predate-the-intra-ordering-change",
                       engine="python+mpmath")
    w.set_description(
        "The six chi-<atom>-h<n>-at-q0-50dps caches were computed 2026-08-10; "
        "atom_braid_word_3A's intra ordering changed 2026-09-05 (qou-hu1f, owner "
        "ruling) and chi_at_q0_via_hoefsmit_mpfr.py:96 calls it with no "
        "intra_order, so a fresh run now yields the BORROMEAN word while the "
        "committed caches are GROUPED (matched to ~3e-50 against ~1.3 relative "
        "for borromean). Import-cone staleness: the producer's own source is "
        "byte-stable. The change is NOT a per-atom scalar -- |chi| ratios spread "
        "12.04x (tritium) / 11.29x (helium-3) and [8,1] and [5,4] CHANGE SIGN in "
        "both -- so qou-hu1f's R_quark factor does not describe this surface, and "
        "that bean does not mention these caches at all (grepped, 0 hits). It "
        "moves a published result: argmin(t) == argmin(w), the O3' "
        "atom-independence of #6841/#6847 measured 6/6, holds under grouped and "
        "FAILS under borromean on tritium (argmin(t) [5,4] -> [7,2] while "
        "argmin(w) stays [5,4]); dim~|chi| concordance 9/10 and 10/10 -> 6/10 "
        "and 6/10. 84 live scripts read these caches. NOT regenerated here: that "
        "is an owner decision (84 consumers plus a 22.5-minute helium-4 "
        "recompute), the same boundary qou-hu1f reached the same day.")
    w.set_audit_only("computations/chi_at_q0_via_hoefsmit_mpfr.py")
    w.add_parameter("q0", q)
    w.add_parameter("q0_anchor", aK["q0Anchor"])
    w.add_data("words", word_rows)
    w.add_data("atoms", rows)
    w.add_data("live_consumer_scripts", consumers)
    for name, ok in CHECKS:
        w.add_assertion(name, computed="1" if ok else "0", expected="1",
                        tolerance="0",
                        source="chi_caches_predate_the_intra_ordering_change_probe")
    print(f"\n  witness: {w.save()}", flush=True)
    print(f"  {sum(1 for _n, ok in CHECKS if ok)}/{len(CHECKS)} checks passed",
          flush=True)
    return 0 if all(ok for _n, ok in CHECKS) else 1


if __name__ == "__main__":
    raise SystemExit(main())
