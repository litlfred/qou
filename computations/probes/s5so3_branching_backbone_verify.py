#!/usr/bin/env python3
"""
S5->SO(3) fiber-action keystone — combinatorial backbone verification.

Verifies the *combinatorially checkable* load-bearing claims of the
2026-06-13 functor-resolution audit
(docs/audits/2026-06-13-s5-so3-fiber-action-functor-resolution.md), which
identifies the missing `conj:s5-so3-fiber-action` functor as the symmetric-group
restriction Res^{S5}_{S3} (Borromean 3-strand <-> 5-strand Bring color-tube).

This script checks ONLY the q=1 / classical-character backbone — the part that
is decidable by representation theory.  It does NOT close the open physics
(the q-deformed E_{(3,2)} vs E_{(3,1,1)} projector shift at q_0, the geometric
partition->A5-rotation map, or the 210 ppb muon evaluation), which remain open
per the resolution doc's own section 4.

Claims verified:
  C1  Branching rule S5 -> S3 (iterated removable-box rule, multiplicity from
      S5->S4->S3):
        (3,2)   |_S3 = (3) + 2.(2,1)
        (3,1,1) |_S3 = (3) + 2.(2,1) + (1,1,1)
      difference = (1,1,1)  [the "exact sign-block subtraction"].
  C2  S5 -> A5 (icosahedral) branching, via character inner products with an
      orthogonality self-check on both character tables:
        (3,1,1) |_A5 = T1 + T2     (dim 6 = 3+3)   -> hosts l=1 (electron, T1)
        (3,2)   |_A5 = H           (dim 5)          -> hosts l=2 (muon, H)
        (2,2,1) |_A5 = H           (dim 5)
  C3  Per-block H3(q) characters of the Borromean braid b = (s1^{-1} s2)^3:
        chi^{(3)}(b)     = 1                  (1-dim trivial, sigma_i -> q)
        chi^{(1,1,1)}(b) = 1                  (1-dim sign,    sigma_i -> -q^{-1})
        chi^{(2,1)}(b)   = 2 - 3 h^4 - h^6    (2-dim standard; h = q - q^{-1})
      => the h^4 coefficient lives EXCLUSIVELY in the (2,1) block (both 1-dim
         blocks are the constant 1), corroborating resolution-doc section 2.4.

No archimedean structure, no fit, no LP/SDP (so no primal-dual emission needed).
Self-checking: character-table orthogonality + Hecke/braid relation checks.
"""
import json
import datetime
import hashlib
import sympy as sp


# ---------------------------------------------------------------------------
# C1 — iterated removable-box branching rule  S_n -> S_{n-1}
# ---------------------------------------------------------------------------
def remove_one_box(part):
    """All partitions of n-1 obtained by removing a single removable corner."""
    out = []
    rows = list(part)
    for i in range(len(rows)):
        # row i corner removable iff it is the last row or strictly longer than next
        if i == len(rows) - 1 or rows[i] > rows[i + 1]:
            new = rows[:i] + [rows[i] - 1] + rows[i + 1:]
            new = tuple(x for x in new if x > 0)
            out.append(new)
    return out


def branch_down(multiset):
    """One level of S_n -> S_{n-1} on a multiset {partition: mult}."""
    res = {}
    for part, m in multiset.items():
        for child in remove_one_box(part):
            res[child] = res.get(child, 0) + m
    return res


def restrict_S5_to_S3(part5):
    lvl4 = branch_down({part5: 1})
    lvl3 = branch_down(lvl4)
    return lvl3


def dim_Sn(part):
    """Hook-length formula dimension of the S_n irrep V_part."""
    n = sum(part)
    # build Young diagram hook lengths
    rows = list(part)
    cols = [0] * (rows[0])
    for r in rows:
        for c in range(r):
            cols[c] += 1
    prod = 1
    for i, r in enumerate(rows):
        for j in range(r):
            arm = r - 1 - j
            leg = cols[j] - 1 - i
            prod *= (arm + leg + 1)
    return sp.factorial(n) // prod


# ---------------------------------------------------------------------------
# C2 — S5 -> A5 branching via characters (with orthogonality self-check)
# ---------------------------------------------------------------------------
phi = (1 + sp.sqrt(5)) / 2
phib = (1 - sp.sqrt(5)) / 2

# A5 conjugacy classes: 1A, 2A=(12)(34), 3A=(123), 5A=(12345), 5B=(13524)
A5_class_sizes = [1, 15, 20, 12, 12]
# A5 irreducible characters (rows): triv, T1(3), T2(3), W(4), H(5)
A5_chars = {
    "triv": [1, 1, 1, 1, 1],
    "T1":   [3, -1, 0, phi, phib],
    "T2":   [3, -1, 0, phib, phi],
    "W4":   [4, 0, 1, -1, -1],
    "H":    [5, 1, -1, 0, 0],
}

# S5 character values on the four EVEN classes that A5 classes fuse into:
#   1A -> 1^5,  2A -> 2^2 1,  3A -> 3 1^2,  5A & 5B -> 5  (same S5 class)
# columns: [1^5, 2^2 1, 3 1^2, 5]
S5_even = {
    "(5)":       [1, 1, 1, 1],
    "(4,1)":     [4, 0, 1, -1],
    "(3,2)":     [5, 1, -1, 0],
    "(3,1,1)":   [6, -2, 0, 1],
    "(2,2,1)":   [5, 1, -1, 0],
    "(2,1,1,1)": [4, 0, 1, -1],
    "(1,1,1,1,1)":[1, 1, 1, 1],
}


def S5_on_A5_classes(name):
    """Character of S5 irrep on the 5 A5 classes (5A,5B share the '5' value)."""
    a, b, c, d = S5_even[name]
    return [a, b, c, d, d]


def a5_inner(chi, mu_name):
    """<chi |_A5 , W_mu>_A5 ."""
    mu = A5_chars[mu_name]
    s = sum(sz * cv * mv for sz, cv, mv in zip(A5_class_sizes, chi, mu))
    return sp.nsimplify(sp.simplify(s / 60))


def a5_orthonormal():
    """Self-check: A5 character table rows are orthonormal."""
    names = list(A5_chars)
    for i in names:
        for j in names:
            s = sum(sz * A5_chars[i][k] * A5_chars[j][k]
                    for k, sz in enumerate(A5_class_sizes))
            # .equals(0) is sympy's robust zero-test (handles the golden-ratio
            # sqrt(5) entries that plain `!= 0` leaves structurally non-zero).
            if not sp.simplify(s / 60 - (1 if i == j else 0)).equals(0):
                return False
    return True


# ---------------------------------------------------------------------------
# C3 — per-block H3(q) characters on the Borromean braid b = (s1^{-1} s2)^3
# ---------------------------------------------------------------------------
def borromean_block_chars():
    q = sp.symbols("q", nonzero=True)
    h = q - 1 / q
    # 1-dim blocks: trivial sigma->q ; sign sigma-> -1/q
    triv = (1 / q * q) ** 3            # (s1^{-1} s2) on trivial = q^{-1}*q = 1
    sign = ((-q) * (-1 / q)) ** 3      # sign: s1^{-1}->-q, s2->-1/q ; product 1
    # 2-dim standard (2,1): concrete Hecke rep, eigenvalues {q, -1/q}.
    b = sp.symbols("b")
    s1 = sp.Matrix([[q, 1], [0, -1 / q]])
    s2 = sp.Matrix([[-1 / q, 0], [b, q]])
    # solve braid relation s1 s2 s1 = s2 s1 s2 for the off-diagonal b
    braid = sp.simplify(s1 * s2 * s1 - s2 * s1 * s2)
    sol = sp.solve([sp.numer(sp.together(e)) for e in braid if e != 0], b, dict=True)
    bval = [s[b] for s in sol if s[b] != 0][0]
    s1 = s1.subs(b, bval)
    s2 = s2.subs(b, bval)
    # relation self-checks
    hecke_ok = (sp.simplify(s1 * s1 - (h * s1 + sp.eye(2))) == sp.zeros(2)
                and sp.simplify(s2 * s2 - (h * s2 + sp.eye(2))) == sp.zeros(2))
    braid_ok = sp.simplify(s1 * s2 * s1 - s2 * s1 * s2) == sp.zeros(2)
    word = (s1.inv() * s2) ** 3
    chi21 = sp.simplify(sp.trace(word))
    chi21_in_h = sp.simplify(sp.expand(chi21) - (2 - 3 * h**4 - h**6))
    return {
        "triv": sp.simplify(triv),
        "sign": sp.simplify(sign),
        "chi21_minus_target": sp.simplify(chi21_in_h),  # expect 0
        "hecke_ok": bool(hecke_ok),
        "braid_ok": bool(braid_ok),
    }


# ---------------------------------------------------------------------------
def main():
    asserts = []

    # ---- C1
    r32 = restrict_S5_to_S3((3, 2))
    r311 = restrict_S5_to_S3((3, 1, 1))
    exp32 = {(3,): 1, (2, 1): 2}
    exp311 = {(3,): 1, (2, 1): 2, (1, 1, 1): 1}
    diff = dict(r311)
    for k, v in r32.items():
        diff[k] = diff.get(k, 0) - v
    diff = {k: v for k, v in diff.items() if v != 0}
    asserts += [
        ("C1_branch_3_2_to_S3", r32 == exp32, exp32, r32),
        ("C1_branch_3_1_1_to_S3", r311 == exp311, exp311, r311),
        ("C1_difference_is_sign_block_1_1_1", diff == {(1, 1, 1): 1}, {"(1,1,1)": 1}, {str(k): v for k, v in diff.items()}),
        ("C1_dim_check_3_2", sum(dim_Sn(p) * m for p, m in r32.items()) == dim_Sn((3, 2)), int(dim_Sn((3, 2))), int(sum(dim_Sn(p) * m for p, m in r32.items()))),
        ("C1_dim_check_3_1_1", sum(dim_Sn(p) * m for p, m in r311.items()) == dim_Sn((3, 1, 1)), int(dim_Sn((3, 1, 1))), int(sum(dim_Sn(p) * m for p, m in r311.items()))),
    ]

    # ---- C2
    ortho = a5_orthonormal()
    m_311_T1 = a5_inner(S5_on_A5_classes("(3,1,1)"), "T1")
    m_311_T2 = a5_inner(S5_on_A5_classes("(3,1,1)"), "T2")
    m_32_H = a5_inner(S5_on_A5_classes("(3,2)"), "H")
    m_221_H = a5_inner(S5_on_A5_classes("(2,2,1)"), "H")
    asserts += [
        ("C2_A5_chartable_orthonormal_selfcheck", ortho is True, True, ortho),
        ("C2_3_1_1_restricts_to_T1_plus_T2", (m_311_T1 == 1 and m_311_T2 == 1), "T1+T2", f"T1x{m_311_T1}+T2x{m_311_T2}"),
        ("C2_3_2_restricts_to_H_electron_l1_hosts_T1", m_32_H == 1, 1, int(m_32_H)),
        ("C2_2_2_1_restricts_to_H", m_221_H == 1, 1, int(m_221_H)),
    ]

    # ---- C3
    c3 = borromean_block_chars()
    asserts += [
        ("C3_hecke_relation_holds_2dim", c3["hecke_ok"], True, c3["hecke_ok"]),
        ("C3_braid_relation_holds_2dim", c3["braid_ok"], True, c3["braid_ok"]),
        ("C3_chi_trivial_borromean_is_1", c3["triv"] == 1, 1, str(c3["triv"])),
        ("C3_chi_sign_borromean_is_1", c3["sign"] == 1, 1, str(c3["sign"])),
        ("C3_chi_2_1_equals_2_minus_3h4_minus_h6", c3["chi21_minus_target"] == 0, 0, str(c3["chi21_minus_target"])),
    ]

    all_passed = all(a[1] for a in asserts)
    for name, ok, exp, got in asserts:
        print(f"[{'PASS' if ok else 'FAIL'}] {name}  expected={exp} got={got}")
    print(f"\nALL PASSED: {all_passed}")

    src = open(__file__).read()
    witness = {
        "computation": "s5so3-branching-backbone-verify",
        "engine": "python+sympy",
        "computedAt": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "description": (
            "Combinatorial backbone of the conj:s5-so3-fiber-action keystone: "
            "verifies the Res^{S5}_{S3} branchings, the (1,1,1) sign-block "
            "difference, the S5->A5 icosahedral branching (l=1->T1 in (3,1,1); "
            "l=2->H in (3,2)/(2,2,1)), and that the Borromean h^4 coefficient "
            "lives exclusively in the H3(q) (2,1) block. q=1/classical backbone "
            "only; the q-deformed projector shift + 210 ppb evaluation stay OPEN "
            "(resolution-doc section 4)."
        ),
        "scriptFile": "s5so3_branching_backbone_verify.py",
        "scriptHash": hashlib.sha256(src.encode()).hexdigest()[:12],
        "assertions": [
            {"name": n, "passed": bool(ok), "expected": str(e), "computed": str(g),
             "tolerance": 0}
            for (n, ok, e, g) in asserts
        ],
        "allPassed": bool(all_passed),
        "openItems": [
            "q-deformed evaluation: the algebraic shift in the H3(q) Markov trace "
            "from the E_{(3,2)} (l=2) vs E_{(3,1,1)} (l=1) projector at q_0 "
            "(needs H5(q); pyhecke_native).",
            "geometric realization: the partition_to_rotation map (partition of 5 "
            "-> A5 rotation on Bring's surface) in S5SO3FiberAction.lean.",
            "does the projector reweighting at q_0 reproduce the 210 ppb muon "
            "tension (GapA4MuonMass)?",
        ],
    }
    with open("computations/probes/s5so3-branching-backbone-verify.witness.json", "w") as f:
        json.dump(witness, f, indent=2)
    print("witness -> computations/probes/s5so3-branching-backbone-verify.witness.json")
    return 0 if all_passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
