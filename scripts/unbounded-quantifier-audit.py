#!/usr/bin/env python3
"""Flag Lean class fields that bound an ARBITRARY quantity by a FIXED constant.

The shape, and why it is a defect
---------------------------------
A class fixes a constant as data, then asserts a bound holding for
*every* value of some universally quantified variable that nothing
constrains:

    Cq : R                                        -- fixed by the instance
    bound : forall (f : N -> R) (f_inf : R) (k : N), k >= 4 ->
              |f k - f_inf| <= Cq / sqrt (k - 3)  -- f_inf ranges over ALL of R

No instance can exist: pick f_inf large enough and the bound fails. The
class is uninhabitable, so `False` follows from it and every
`[C]`-conditional theorem above it is vacuous.

This is the complement of `limit-claim-encoding-audit.py`. That one asks
*is the statement weaker than its prose*; this asks *is the statement
stronger than the truth*. A field can pass one and fail the other --
`HasQPlancherelCLT.bound` did exactly that: flagged there, triaged a
false positive (it carries an explicit quantitative bound rather than an
unlocalised one), and genuinely refutable here.

Named by the q-RH arc on PR #6041 as: *an external theorem asserted for
every inhabitant of a structure that does not carry the theorem's
hypotheses.* Confirmed instances so far: `hasse-weil-bound` (two axioms),
`HasQPlancherelCLT`, `ChiralityFactorClass`.

High-recall by design: a hit is a candidate to read, never a verdict.
Construct the cheapest inhabitant and see whether the field survives it.

Usage:
    python3 scripts/unbounded-quantifier-audit.py [PATH ...]
    python3 scripts/unbounded-quantifier-audit.py --selftest
"""
import re, sys, glob, os

CMP = re.compile(r'[≤<≥>]')

def strip_comments(src):
    out, depth = [], 0
    for line in src.split("\n"):
        res, j = "", 0
        while j < len(line):
            if depth == 0 and line[j:j+2] == "/-": depth += 1; j += 2; continue
            if depth > 0 and line[j:j+2] == "-/": depth -= 1; j += 2; continue
            if depth > 0: j += 1; continue
            if line[j:j+2] == "--": break
            res += line[j]; j += 1
        out.append(res)
    return "\n".join(out)

def classes(src):
    """Yield (class_name, [data_field_names], [(field, statement)])."""
    lines = strip_comments(src).split("\n")
    i = 0
    while i < len(lines):
        m = re.match(r'(?:class|structure)\s+(\S+)', lines[i])
        if not m:
            i += 1; continue
        name, fields, j = m.group(1), [], i + 1
        while j < len(lines):
            if lines[j].strip() and not lines[j][0].isspace():
                break
            fm = re.match(r"^  ([a-zA-Z_][A-Za-z0-9_']*)\s*:(.*)$", lines[j])
            if fm:
                stmt, k = [fm.group(2)], j + 1
                while k < len(lines) and re.match(r'^\s{4,}\S', lines[k]):
                    stmt.append(lines[k]); k += 1
                fields.append((fm.group(1), " ".join(" ".join(stmt).split())))
                j = k; continue
            j += 1
        names = [f for f, _ in fields]
        yield name, names, fields
        i = j

# A binder whose TYPE is a proposition is a proof, not a quantity: nothing
# is "arbitrary" about it, and the hypothesis it carries constrains the
# statement rather than widening it.  `hn : H.n ≥ 2` is the common shape.
PROOF_TYPE_RE = re.compile(r'[≥≤<>=≠∈∉⊆∣]|\bTrue\b|\bFalse\b')

# A binder over a FINITE type ranges over boundedly many values, so a fixed
# constant can bound it.  `i : Fin channels` is the common shape.
#
# `Finset X` is deliberately NOT here, and the omission is load-bearing: a
# `Finset` is a finite set, but the TYPE of finite sets is infinite, so a
# binder over it is arbitrary.  Including it silently skipped the
# Rosso-Jones defect this detector found -- `∀ (partitions_of_r : Finset
# Partition), jonesPoly r s = partitions_of_r.sum …`, refuted by `∅`.
# Pinned as a positive control in --selftest.
FINITE_TYPE_RE = re.compile(r'\bFin\b|\bBool\b|\bUnit\b|\bPUnit\b|\bEmpty\b')

def binders(stmt):
    """Universally bound (name, type) pairs from the leading foralls."""
    out = []
    for grp in re.finditer(r'∀\s*([^,]+),', stmt):
        body = grp.group(1)
        for m in re.finditer(r'\(?\s*([a-zA-Z_][A-Za-z0-9_\']*)\s*([^):]*):([^)]*)\)?', body):
            out.append((m.group(1), m.group(3)))
        for bare in re.findall(r'^\s*([a-zA-Z_][A-Za-z0-9_\']*)\s*$', body):
            out.append((bare, ''))
    return out

def quantity_binders(stmt):
    """Binder names that denote an ARBITRARY QUANTITY.

    Excludes proof binders, binders over finite types, and `_`-prefixed
    names (conventionally unused).  Each exclusion is a measured
    false-positive source, not a guess -- see the module docstring."""
    keep = []
    for name, ty in binders(stmt):
        if name.startswith('_'):
            continue
        if PROOF_TYPE_RE.search(ty or ''):
            continue
        if FINITE_TYPE_RE.search(ty or ''):
            continue
        keep.append(name)
    return keep

def audit(paths):
    hits = []
    for p in paths:
        try: src = open(p).read()
        except Exception: continue
        for cname, data, fields in classes(src):
            for fname, stmt in fields:
                if '∀' not in stmt or not CMP.search(stmt):
                    continue
                parts = CMP.split(stmt)
                if len(parts) < 2:
                    continue
                lhs, rhs = parts[-2], parts[-1]
                # An `∃` after the `∀` can witness the variable, so the
                # claim is satisfiable however large it gets: that is
                # unboundedness, not an unbounded quantity bounded by a
                # constant.  `∀ M, ∃ q, M < enstrophy q` is the shape.
                if '∃' in stmt:
                    continue
                bs = set(quantity_binders(stmt))
                if not bs:
                    continue
                # a class-data constant must appear on the bounding side
                if not any(re.search(rf'\b{re.escape(d)}\b', rhs) for d in data
                           if d != fname):
                    continue
                # antecedents constrain some binders; those are fine
                constrained = set()
                for ante in re.findall(r'([^,→]*)→', stmt):
                    for b in bs:
                        if re.search(rf'\b{re.escape(b)}\b', ante):
                            constrained.add(b)
                free = [b for b in bs
                        if b not in constrained
                        and re.search(rf'\b{re.escape(b)}\b', lhs)
                        and not re.search(rf'\b{re.escape(b)}\b', rhs)]
                if free:
                    hits.append((p, cname, fname, sorted(free), stmt))
    return hits

def selftest():
    import tempfile
    pre_fix = '''namespace T
class HasQPlancherelCLT where
  Cq : ℝ
  Cq_pos : 0 < Cq
  bound : ∀ (f : ℕ → ℝ) (f_inf : ℝ) (k : ℕ), k ≥ 4 →
    |f k - f_inf| ≤ Cq / Real.sqrt (k - 3 : ℝ)
end T
'''
    post_fix = '''namespace T
class HasQPlancherelCLT where
  Cq : ℝ
  Cq_pos : 0 < Cq
  f : ℕ → ℝ
  f_inf : ℝ
  bound : ∀ k : ℕ, k ≥ 4 → |f k - f_inf| ≤ Cq / Real.sqrt (k - 3 : ℝ)
end T
'''
    # Three further shapes that must NOT flag -- each was a measured
    # false positive before the precision rules were added.
    controls = '''namespace T
class MarkovTrace where
  z : R
  tr : C -> R
  markov_stab : ∀ (hn : H.n ≥ 2) (x : C), tr (mul x (T last)) = z * tr x
class CriticalExponent where
  enstrophy : ℝ → ℝ
  enstrophy_diverges : ∀ M : ℝ, ∀ ε : ℝ, 0 < ε →
    ∃ q : ℝ, 1 < q ∧ q - 1 < ε ∧ M < enstrophy q
class LpDualStabilityContext where
  y_star : Fin channels → ℝ
  κ_G : ℝ
  t_norm : ℝ
  dual_price_bound : ∀ i : Fin channels, |y_star i| ≤ κ_G * t_norm
end T
'''

    # The Rosso-Jones shape, which this detector found (#6041).  It must
    # keep flagging: `Finset Partition` is an infinite type of finite sets.
    rosso_jones = '''namespace T
class HeckeRepRingContext where
  jonesPoly : ℕ → ℕ → ℝ
  rjPairing : P → P → ℝ
  fullTwistEig : P → ℝ
  jonesPoly_eq_eval : ∀ (s : ℕ) (partitions_of_r : Finset P),
    jonesPoly r s = partitions_of_r.sum (fun lam => rjPairing lam lam * fullTwistEig lam ^ s)
end T
'''

    def run(text):
        with tempfile.NamedTemporaryFile('w', suffix='.lean', delete=False) as fh:
            fh.write(text); t = fh.name
        got = audit([t]); os.unlink(t); return got
    bad, good, ctrl, rj = (run(pre_fix), run(post_fix), run(controls),
                           run(rosso_jones))
    if not bad:
        print("SELFTEST FAIL: did not flag the known-refutable pre-fix shape")
        return 1
    if good:
        print(f"SELFTEST FAIL: flagged the FIXED shape (false positive): {good}")
        return 1
    if ctrl:
        names = [f'{c}::{f}' for _, c, f, _, _ in ctrl]
        print(f"SELFTEST FAIL: flagged a known false-positive shape: {names}")
        return 1
    if not rj:
        print("SELFTEST FAIL: did not flag the Rosso-Jones shape "
              "(a `Finset` binder is arbitrary -- see FINITE_TYPE_RE)")
        return 1
    print("selftest ok: flags the refutable HasQPlancherelCLT and Rosso-Jones "
          "shapes; does NOT flag a repaired carrier, a proof binder, an "
          "∃-witnessed bound, or a finite index")
    return 0

if __name__ == '__main__':
    if '--selftest' in sys.argv:
        sys.exit(selftest())
    args = [a for a in sys.argv[1:] if not a.startswith('-')]
    if not args:
        args = glob.glob("content/**/*.lean", recursive=True)
    paths = []
    for a in args:
        paths += glob.glob(os.path.join(a, "**", "*.lean"), recursive=True) \
                 if os.path.isdir(a) else [a]
    hits = audit(sorted(set(paths)))
    for p, c, f, free, stmt in hits:
        print(f"\n══ {p}")
        print(f"   {c}::{f}   unconstrained: {', '.join(free)}")
        print(f"   {stmt[:200]}")
    print(f"\n{len(hits)} candidate(s) over {len(set(paths))} file(s) "
          f"-- construct the cheapest inhabitant before calling any of them a defect.")
