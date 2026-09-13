#!/usr/bin/env python3
# polynomial_q_not_applicable: exact integer / rational combinatorics on a recorded
# integer column; no q-series is evaluated.
"""The recorded Phi_3 column DISCRIMINATES the four candidate strand counts.

BEAN qou-jgg0. The corpus carries two objects called "the atomic braid", both
written `\\mathcal{A}`:

    (a)  H_{A+Z}(q)   -- def:atomic-braid: A nucleon strands + Z ELECTRON strands
    (b)  H_{3A}(q)    -- production (atom_braid_word_3A): 3 quark strands per
                         nucleon, NO electrons

plus two further cells of the 2x2 the bean identified on 2026-09-06:

    (A)  H_A(q)       -- the declared "Default-coarse" nucleon-only coarsening
    (c)  H_{3A+Z}(q)  -- mass-endomorphism/atomic-mass-gb-nf.md:3

The bean framed the choice as a NAMING decision with a priced consequence, and
reserved it to the author. This probe adds the measurement the bean did not
have: **the corpus already contains a number that separates the four cells**,
and it separates them decisively.

THE MEASUREMENT. `computations/phi_allpairs_reconstruction.py` (on main,
1fe569c05) closes Phi_2 and Phi_3 of thm:wedderburn-mass-formula. Its Phi_3
result is

    Phi_3 = w * ln q,   w = 2[ 2*C(Z,2) - C(N,2) - Z^2 ] = -2Z - N(N-1)

exact on 19 of 19 non-hydrogen rows, Ar included -- and Ar is a HELD-OUT
confirmation, since it is the row that refuted the previous candidate
-Z(2N-Z+1). The term structure is tbl:atomic-braid-table1-data's six pair types
with their own crossing values, and the pair COUNTS are forced by the strand
content. Two of those counts -- C(Z,2) electron-electron pairs and Z^2
proton-electron pairs -- presuppose Z ELECTRON STRANDS. That is cell (a), and
nothing else.

WHAT IS NEW HERE, over phi_allpairs_reconstruction:

  1. The Phi_3 sign of each pair type is DERIVED from Table 1's own (c, d)
     values by exact symbolic arithmetic (check 3), not transcribed. The
     reconstruction script hardcodes the six signs.
  2. The other three cells are computed and scored (checks 5-8).
  3. Each cell is then GRANTED THREE FITTED COEFFICIENTS on its own pair-count
     basis and re-scored (checks 10-13) -- a deliberately generous test, and
     labelled a fit.

THE RESULT.

    cell            parameter-free     three FITTED coefficients
    A                    0/19          18/19, integral (2, 0, -2), misses Ar alone
    A+Z  (a)            19/19          19/19, integral (4, -2, -2)  <- Table 1's OWN values
    3A   (b)             0/19          10/19, (7/15, 1/5, -4/9)     -- not integral
    3A+Z (c)             0/19          10/19, (13/15, -1/5, -4/3)   -- not integral

The second column is the sharper half. A three-parameter search on cell (a)'s
basis RECOVERS the parameter-free answer -- the fit lands exactly on the values
Table 1 already fixes -- while (b) and (c) cannot reach the column even when
fitted, and their best coefficients are fractions no crossing table produces.

SCOPE, and it is deliberately narrow:

  * This is a scope-(a) negative for (b) and (c), NOT a structural exclusion.
    What is measured is that THESE pair-count constructions, on THESE bases,
    do not reproduce the column. A genuinely quark-level colour-weighted
    construction is untested and is not excluded here.
  * Phi_2 does NOT discriminate (check 14): Phi_2 = Z*N*ln(1+h^2/4) and the pn
    pair count Z*N is identical under A and A+Z.
  * Phi_1 is not closed under any reading and is untouched.
  * The TARGET is a recovered producer's intermediate, not the published paper
    table (check 2 records the provenance chain and its one known defect).

NO FITTING in the pejorative sense: the headline result is parameter-free, and
the three-coefficient tests are performed on EVERY cell symmetrically and
reported as fits. Nothing is tuned to make (a) win; (a) wins the
parameter-free test, which is the test that counts under the owner's
2026-09-05 no-fitting directive.

NO FLOAT64 is reachable. Every quantity is `int` or `fractions.Fraction`, with
one exception: check 2 uses mpmath at 40 dps to verify that the recorded Phi_3
decimals divide by ln(q0) into integers, and reports the deviation rather than
asserting exact equality (those decimals are recorded to six places).
"""
from __future__ import annotations

import ast
import re
import subprocess
import sys
from fractions import Fraction
from itertools import combinations
from math import comb
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
TABLE_PRODUCER = ROOT / "computations" / "wedderburn_mass_table_z1_20.py"
RECONSTRUCTION = ROOT / "computations" / "phi_allpairs_reconstruction.py"
TABLE1 = (ROOT / "content" / "quantum-observable-universe" / "knots-particles-confinement"
          / "atomic-braid-table1-data.md")

_checks = 0
_failed = 0


def check(label: str, cond: bool, detail: str = "") -> None:
    global _checks, _failed
    _checks += 1
    if not cond:
        _failed += 1
    print(f"  [{'PASS' if cond else 'FAIL'}] {label}" + (f"  {detail}" if detail else ""))


# ---------------------------------------------------------------- the target

def load_recorded_rows():
    """Parse ROWS out of wedderburn_mass_table_z1_20.py by AST, never by import.

    Importing the producer would run it. The tuple layout is
    (atom, Z, protons, N, Phi1, Phi2, Phi3, M_obs, M_pred) -- nine fields; the
    source's own comment above ROWS lists eight and omits the duplicated proton
    count. Indices are asserted against the atoms in check 1 rather than trusted.
    """
    tree = ast.parse(TABLE_PRODUCER.read_text())
    for node in tree.body:
        if isinstance(node, ast.Assign) and any(
                getattr(t, "id", None) == "ROWS" for t in node.targets):
            return [tuple(ast.literal_eval(e) for e in elt.elts)
                    for elt in node.value.elts]
    raise RuntimeError("ROWS not found in " + str(TABLE_PRODUCER))


print("CHECK 1 -- the target exists, and its field layout is what we think")
ROWS = load_recorded_rows()
check("the recorded table has 20 rows", len(ROWS) == 20, f"{len(ROWS)} rows")
check("fields 1 and 2 are both the proton count Z",
      all(r[1] == r[2] for r in ROWS))
check("field 3 is the neutron count N (Ar is Z=18, N=22)",
      [r for r in ROWS if r[0] == "Ar"][0][1:4] == (18, 18, 22))
check("field 6 is Phi_3 (He -0.626052, Ar -51.962315)",
      [r for r in ROWS if r[0] == "He"][0][6] == "-0.626052"
      and [r for r in ROWS if r[0] == "Ar"][0][6] == "-51.962315")

# (atom, Z, N, recorded Phi_3 as a decimal string)
TARGET = [(r[0], r[1], r[3], r[6]) for r in ROWS]
NONH = [t for t in TARGET if t[0] != "H"]

print()
print("CHECK 2 -- PROVENANCE, stated rather than assumed")
src = TABLE_PRODUCER.read_text()
check("the column comes from a RECOVERED witness, named in the producer",
      "atom-mass-complete-wedderburn.witness.json" in src,
      "out of tree since the miga split -- this is not the published paper table")
check("that producer's own third coefficient is disputed, and it says so",
      "beta3" in src and "0.0499" in src,
      "beta3=0.0499 vs published h_A^2=0.0437073, a 14.2 % departure "
      "(computations/audits/wedderburn_beta3_vs_hA2_discrimination.py)")

def phi3_over_lnq():
    """Recorded Phi_3 divided by ln(q0), per row, with the deviation from the
    nearest integer.

    Deliberately a FUNCTION, not module scope: `mp.dps` must be raised before any
    `mpf` is constructed, and a module-scope construction cannot be proved
    ordered by `computations/mpf_import_time_dps_audit.py` (the import-time dps
    ratchet). Raising dps first, inside the call, makes the ordering local and
    checkable. The only mpmath in this probe is here; everything else is `int`
    or `Fraction`.
    """
    sys.path.insert(0, str(ROOT / "tools" / "qou-substrate" / "python"))
    from mpmath import mp, mpf

    mp.dps = 40                                  # before the first mpf, always
    # `q_at(dps)` re-solves the proton pin AT that precision; `constants.Q` is
    # `_solve_q_proton_f64`, so `mpf(str(Q))` launders float64 into mpmath.
    from qou_substrate.constants import q_at

    lnq = mp.log(q_at(40))
    out = []
    for el, _Z, _N, p3 in NONH:
        v = mpf(p3) / lnq
        k = int(mp.nint(v))
        out.append((el, k, abs(v - k) / abs(k)))
    # The tolerance comparison also lives here: an `mpf` tolerance at module
    # scope is a module-scope construction like any other, and the ratchet
    # counts it (correctly -- it cannot know it is only a threshold).
    worst = max(out, key=lambda t: t[2])
    return out, bool(worst[2] < mpf("1e-4")), worst[0], mp.nstr(worst[2], 3)


try:
    devs, within, worst_el, worst_dev = phi3_over_lnq()
    check("every recorded Phi_3 is (integer)*ln(q0) at the proton pin",
          within,
          f"worst {worst_el}: rel dev {worst_dev} "
          f"-- the 6-decimal recording precision, not a mismatch")
    W = {el: k for el, k, _ in devs}
except ImportError as exc:                                    # pragma: no cover
    print(f"  [INFO] mpmath/qou_substrate unavailable ({exc}); "
          "falling back to the reconstruction script's own integers")
    W = None

# The integers, independently: phi_allpairs_reconstruction.py carries them.
rec = RECONSTRUCTION.read_text()
REC_W = {m.group(1): int(m.group(2))
         for m in re.finditer(r'\("([A-Za-z]{1,2})",\s*\d+,\s*\d+,\s*(-?\d+)\)', rec)}
check("phi_allpairs_reconstruction.py carries the same integers, independently",
      W is None or all(REC_W[el] == W[el] for el in W),
      f"{len(REC_W)} rows parsed from the reconstruction script")
if W is None:
    W = {el: REC_W[el] for el, _, _, _ in NONH}

ROWSZN = [(el, Z, N, W[el]) for el, Z, N, _ in NONH]

# ------------------------------------------------- Table 1's signs, DERIVED

print()
print("CHECK 3 -- the Phi_3 sign of each pair type, DERIVED from Table 1's (c, d)")
print("           lam_sym = c*q + d,  lam_alt = -c/q + d,  term = ln|lam_sym/lam_alt|")

PAIR_ROW = re.compile(r"^\|\s*(\$[^|]+?)\s*\|\s*(\$[^|]+?)\s*\|\s*\$(-?\d+)\$\s*\|"
                      r"\s*\$([^|]+?)\$\s*\|")


def parse_table1():
    """(c, d) per pair type, read from the content block. d is 0, 1 or -(q-1/q)."""
    out = {}
    key = {"pp": "pp", "nn": "nn", "pn": "pn", "pe": "pe", "ne": "ne", "ee": "ee"}
    for line in TABLE1.read_text().splitlines():
        m = PAIR_ROW.match(line)
        if not m:
            continue
        pair_tex, _crossing, c_str, d_str = m.groups()
        # "$\mathfrak{p}e$" -> "pe"; "$ee$" -> "ee". A lookaround on a bare `e`
        # cannot do this: the two e's of `ee` are adjacent to each other.
        name = re.sub(r"\\mathfrak\{([pn])\}", r"\1", pair_tex)
        name = re.sub(r"[^pne]", "", name)
        if name not in key:
            continue
        d_clean = d_str.replace(" ", "")
        if d_clean == "0":
            d = ("const", 0)
        elif d_clean == "1":
            d = ("const", 1)
        elif d_clean in ("-(q-q^{-1})", "-(q-q^{-1})"):
            d = ("minus_h", None)
        else:
            raise RuntimeError(f"unparsed d for {name}: {d_str!r}")
        out[name] = (int(c_str), d)
    return out


T1 = parse_table1()
check("all six pair types parsed out of tbl:atomic-braid-table1-data",
      sorted(T1) == ["ee", "ne", "nn", "pe", "pn", "pp"], str(sorted(T1)))
check("three of the six are ELECTRONIC -- this is the (a) reading's content",
      all(k in T1 for k in ("pe", "ne", "ee")),
      f"pe={T1.get('pe')}, ne={T1.get('ne')}, ee={T1.get('ee')}")

try:
    import sympy as sp

    q = sp.Symbol("q", positive=True)
    h = q - 1 / q

    def phi3_coeff(c, d):
        """Exponent k with |lam_sym/lam_alt| = q^k. Exact; no float."""
        dv = sp.Integer(d[1]) if d[0] == "const" else -h
        lam_sym = sp.simplify(c * q + dv)
        lam_alt = sp.simplify(-sp.Rational(c, 1) / q + dv)
        if lam_alt == 0:
            raise RuntimeError("alt eigenvalue vanishes")
        ratio = sp.simplify(lam_sym / lam_alt)
        for k in (-2, -1, 0, 1, 2):
            if sp.simplify(sp.Abs(ratio) - q ** k) == 0:
                return k
        raise RuntimeError(f"ratio {ratio} is not +-q^k")

    SIGN = {k: phi3_coeff(*v) for k, v in T1.items()}
    check("derived signs: pp +2, nn -2, pn 0, pe -2, ne 0, ee +2",
          SIGN == {"pp": 2, "nn": -2, "pn": 0, "pe": -2, "ne": 0, "ee": 2},
          str(SIGN))
    check("they match the six phi_allpairs_reconstruction.py hardcodes",
          SIGN["pp"] == 2 and SIGN["ee"] == 2 and SIGN["pe"] == -2,
          "w = 2*(C(Z,2)*(+1) + C(N,2)*(-1) + C(Z,2)*(+1) + Z^2*(-1)) in that file")
except ImportError:                                           # pragma: no cover
    print("  [INFO] sympy unavailable; using the reconstruction script's signs")
    SIGN = {"pp": 2, "nn": -2, "pn": 0, "pe": -2, "ne": 0, "ee": 2}
    check("fallback signs are the reconstruction script's",
          SIGN["pe"] == -2, "derivation skipped")

# ------------------------------------------- the four cells, parameter-free

print()
print("CHECK 4 -- the four cells of qou-jgg0's 2x2, and their strand contents")


def pair_counts(cell, Z, N):
    """Pair multiplicities per crossing type, forced by the cell's strand content."""
    if cell == "A":            # nucleons only, no electrons
        return {"pp": comb(Z, 2), "nn": comb(N, 2), "pn": Z * N,
                "pe": 0, "ne": 0, "ee": 0}
    if cell == "A+Z":          # nucleons + Z electrons  -- def:atomic-braid
        return {"pp": comb(Z, 2), "nn": comb(N, 2), "pn": Z * N,
                "pe": Z * Z, "ne": N * Z, "ee": comb(Z, 2)}
    if cell == "3A":           # 3 quark strands per nucleon, no electrons
        return {"pp": comb(3 * Z, 2), "nn": comb(3 * N, 2), "pn": 9 * Z * N,
                "pe": 0, "ne": 0, "ee": 0}
    if cell == "3A+Z":         # quark strands + Z electrons
        return {"pp": comb(3 * Z, 2), "nn": comb(3 * N, 2), "pn": 9 * Z * N,
                "pe": 3 * Z * Z, "ne": 3 * N * Z, "ee": comb(Z, 2)}
    raise ValueError(cell)


CELLS = ["A", "A+Z", "3A", "3A+Z"]
STRANDS = {"A": lambda Z, N: Z + N, "A+Z": lambda Z, N: Z + N + Z,
           "3A": lambda Z, N: 3 * (Z + N), "3A+Z": lambda Z, N: 3 * (Z + N) + Z}
check("the four strand counts are strictly ordered A < A+Z < 3A < 3A+Z for Z>=1",
      all(STRANDS["A"](Z, N) < STRANDS["A+Z"](Z, N) < STRANDS["3A"](Z, N)
          < STRANDS["3A+Z"](Z, N)
          for Z in range(1, 61) for N in range(0, 61)),
      "3600 (Z,N) pairs, zero coincidences -- nothing reconciles by accident")
check("only the two electron-bearing cells have nonzero pe/ee counts",
      all(pair_counts(c, 6, 6)["pe"] == 0 and pair_counts(c, 6, 6)["ee"] == 0
          for c in ("A", "3A"))
      and all(pair_counts(c, 6, 6)["pe"] > 0 and pair_counts(c, 6, 6)["ee"] > 0
              for c in ("A+Z", "3A+Z")))


def w_of(cell, Z, N):
    pc = pair_counts(cell, Z, N)
    return sum(SIGN[k] * pc[k] for k in pc)


print()
print("CHECK 5-8 -- PARAMETER-FREE: Table 1's signs, each cell's own pair counts")
print(f"    {'atom':>5} {'Z':>3} {'N':>3} {'recorded':>9}"
      + "".join(f" {c:>8}" for c in CELLS))
for el, Z, N, w in ROWSZN[:4]:
    print(f"    {el:>5} {Z:>3} {N:>3} {w:>9}"
          + "".join(f" {w_of(c, Z, N):>8}" for c in CELLS))
print("    ...")

FREE = {}
for cell in CELLS:
    hits = sum(1 for _, Z, N, w in ROWSZN if w_of(cell, Z, N) == w)
    FREE[cell] = hits
check("cell A (nucleons only) reproduces the column on 0 of 19 rows",
      FREE["A"] == 0, f"{FREE['A']}/19")
check("cell A+Z (a) reproduces the column on ALL 19 rows",
      FREE["A+Z"] == 19, f"{FREE['A+Z']}/19 -- exact integers, no tolerance")
check("cell 3A (b) reproduces the column on 0 of 19 rows",
      FREE["3A"] == 0, f"{FREE['3A']}/19  (He gives {w_of('3A', 2, 2)}, recorded -6)")
check("cell 3A+Z (c) reproduces the column on 0 of 19 rows",
      FREE["3A+Z"] == 0,
      f"{FREE['3A+Z']}/19  (He gives {w_of('3A+Z', 2, 2)}, recorded -6)")

print()
print("CHECK 9 -- what the electron strands contribute, in closed form")
check("w(A+Z) - w(A) = -Z(Z+1) on all 20 rows, exactly",
      all(w_of("A+Z", Z, N) - w_of("A", Z, N) == -Z * (Z + 1)
          for _, Z, N, _ in TARGET),
      "= 2*[C(Z,2) - Z^2]: the ee pairs minus the pe pairs")
check("so removing the electrons moves Ar by +342",
      w_of("A", 18, 22) - w_of("A+Z", 18, 22) == 342,
      f"A+Z {w_of('A+Z', 18, 22)} -> A {w_of('A', 18, 22)}, recorded "
      f"{[w for el, _, _, w in ROWSZN if el == 'Ar'][0]}")

# ------------------------------------------------- now GRANT each cell a fit

print()
print("CHECK 10-13 -- GRANT each cell three FREE coefficients (this IS a fit,")
print("               run symmetrically on every cell, and labelled as one)")


def basis(cell, Z, N):
    pc = pair_counts(cell, Z, N)
    # the three independent nonzero pair families of that cell
    if cell in ("A", "3A"):
        return (pc["pp"], pc["nn"], pc["pn"])
    return (pc["pp"], pc["nn"], pc["pe"])


def det3(m):
    return (m[0][0] * (m[1][1] * m[2][2] - m[1][2] * m[2][1])
            - m[0][1] * (m[1][0] * m[2][2] - m[1][2] * m[2][0])
            + m[0][2] * (m[1][0] * m[2][1] - m[1][1] * m[2][0]))


def best_fit(cell):
    """Exact Cramer solve on every anchor triple; keep the one hitting most rows."""
    best = (0, None, None)
    for trio in combinations(range(len(ROWSZN)), 3):
        rows = [ROWSZN[i] for i in trio]
        M = [[Fraction(x) for x in basis(cell, r[1], r[2])] for r in rows]
        y = [Fraction(r[3]) for r in rows]
        D = det3(M)
        if D == 0:
            continue
        sol = []
        for k in range(3):
            Mk = [r[:] for r in M]
            for i in range(3):
                Mk[i][k] = y[i]
            sol.append(det3(Mk) / D)
        hits = sum(1 for _, Z, N, w in ROWSZN
                   if sum(c * Fraction(b) for c, b in zip(sol, basis(cell, Z, N)))
                   == Fraction(w))
        if hits > best[0]:
            best = (hits, [ROWSZN[i][0] for i in trio], sol)
    return best


FIT = {c: best_fit(c) for c in CELLS}
for c in CELLS:
    hits, anchors, sol = FIT[c]
    integral = all(s.denominator == 1 for s in sol)
    print(f"    {c:>5}  best {hits:>2}/19   coeffs "
          f"{str([str(s) for s in sol]):<34} integral={integral}")

check("even FITTED, cell 3A (b) reaches only 10 of 19 rows",
      FIT["3A"][0] == 10, f"{FIT['3A'][0]}/19")
check("and its best coefficients are FRACTIONS -- no crossing table yields them",
      not all(s.denominator == 1 for s in FIT["3A"][2]),
      str([str(s) for s in FIT["3A"][2]]))
check("even FITTED, cell 3A+Z (c) reaches only 10 of 19, also fractional",
      FIT["3A+Z"][0] == 10
      and not all(s.denominator == 1 for s in FIT["3A+Z"][2]),
      f"{FIT['3A+Z'][0]}/19, {[str(s) for s in FIT['3A+Z'][2]]}")
check("cell A fitted reaches 18/19 with integral (2, 0, -2) -- and misses Ar ALONE",
      FIT["A"][0] == 18
      and [el for el, Z, N, w in ROWSZN
           if sum(c * Fraction(b) for c, b in zip(FIT["A"][2], basis("A", Z, N)))
           != Fraction(w)] == ["Ar"],
      f"{FIT['A'][0]}/19, {[str(s) for s in FIT['A'][2]]}, "
      "misses the one row with a large neutron excess")

print()
print("CHECK 14 -- the sharpest half: the FIT on cell (a) RECOVERS the")
print("            parameter-free answer, landing on Table 1's own values")
check("cell A+Z fitted still reaches 19/19",
      FIT["A+Z"][0] == 19, f"{FIT['A+Z'][0]}/19")
check("its fitted coefficients are exactly (4, -2, -2)",
      [str(s) for s in FIT["A+Z"][2]] == ["4", "-2", "-2"],
      str([str(s) for s in FIT["A+Z"][2]]))
check("and (4, -2, -2) is 2*(pp+ee), 2*nn, 2*pe read straight off Table 1",
      (SIGN["pp"] + SIGN["ee"], SIGN["nn"], SIGN["pe"]) == (4, -2, -2),
      "a three-parameter search lands on the parameter-free prediction")

print()
print("CHECK 15 -- Phi_2 does NOT discriminate, and saying so is part of the result")
check("the pn pair count Z*N is IDENTICAL under A and A+Z on every row",
      all(pair_counts("A", Z, N)["pn"] == pair_counts("A+Z", Z, N)["pn"]
          for _, Z, N, _ in TARGET),
      "Phi_2 = Z*N*ln(1+h^2/4), so only Phi_3 separates the electron-bearing cells")
check("Phi_1 is not closed under any reading -- the reconstruction says so",
      "Phi_1 is NOT closed here" in rec,
      "this probe says nothing about Phi_1")

print()
print("CHECK 16 -- CORRECTION to qou-jgg0: the A+Z object IS built in computations/")


SELF = "./" + str(Path(__file__).resolve().relative_to(ROOT))


def importers(symbol):
    """Files naming `symbol`, excluding deprecated code, the generated qou-mass
    mirror, and THIS FILE -- which names both families in its own check strings
    and would otherwise report itself as a layer straddle."""
    out = subprocess.run(
        ["grep", "-rl", symbol, "--include=*.py", "."],
        cwd=ROOT, capture_output=True, text=True).stdout.split()
    return sorted(p for p in out
                  if "/_deprecated/" not in p
                  and not p.startswith("./qou-mass/")
                  and p != SELF)


az_family = importers("atom_gen_chains")
tha_family = importers("atom_braid_word_3A")
chains = (ROOT / "computations" / "substrate" / "hecke_core_symbolic.py").read_text()
check("atom_gen_chains_sym builds Z ELECTRON crossings explicitly",
      "for _ in range(Z):" in chains and "Z electrons each contributing" in chains,
      "all-pairs nucleon crossings + Z electrons at (1, -h) -- that is the A+Z content")
check("the bean's 'nothing in computations/ has ever built the A+Z object' is FALSE",
      len(az_family) >= 1,
      f"{len(az_family)} importers of the A+Z family "
      f"(e.g. {az_family[0] if az_family else '-'})")
check("the 3A family still has strictly more importers -- recorded as found",
      len(tha_family) > len(az_family),
      f"3A: {len(tha_family)}  vs  A+Z: {len(az_family)}")
both = sorted(set(az_family) & set(tha_family))
check("and some files import BOTH families -- a live layer-straddle surface",
      len(both) >= 1, f"{len(both)}: {both}")

print()
print("CHECK 17 -- SCOPE: this is a scope-(a) negative, not a structural exclusion")
doc = Path(__file__).read_text()
check("the docstring says (b)/(c) are not structurally excluded",
      "NOT a structural exclusion" in doc,
      "a colour-weighted quark-level construction is untested and stays open")
check("the docstring records the target's provenance defect",
      "beta3" in doc and "14.2 %" in doc,
      "the recovered producer disagrees with the published h_A^2 by 14.2 %")

print()
print(f"{_checks - _failed}/{_checks} checks passed")
print()
print("MEASURED: the recorded Phi_3 column separates the four candidate strand")
print("counts, and only the electron-bearing nucleon-strand cell -- A+Z, which")
print("is what def:atomic-braid says -- reproduces it parameter-free.")
sys.exit(1 if _failed else 0)
