#!/usr/bin/env python3
"""gen-hecke-corner-column — emit one column of the Bokut–Shiao corner in Lean.

The `B × B` corner of the completed Hecke rewriting system has two depths,
`a = i − j₁` and `b = i − j₂`.  In the `a > b` regime the chain's shape does not
depend on `a` at all (see `computations/hecke_gs_confluence_range.py`), so one
Lean theorem covers a whole column — fixed `b`, every `a`.  This script emits
that theorem.

Everything is derived from the confluence engine's own trace rather than
transcribed: the part of the descending run that grows with `a` is abstracted to
`E = descWord i_{b+1} j`, and every word comes out as
`(explicit prefix) ++ E ++ (explicit suffix)`.  Generators are named `i₀ … i_{b+1}`
by distance below the top index.

    python3 scripts/gen-hecke-corner-column.py 2   # §4ad, 15 steps
    python3 scripts/gen-hecke-corner-column.py 3   # §4ae, 23 steps

The output is pasted into `content/unital-groebner-bases/lean/UGB/GrobnerShirshov/
HeckeCompletion.lean`.  Checked by re-deriving §4ad, whose seventeen words and
fifteen rules were worked out by hand first and agree exactly.

Two `rfl` conventions are baked in, and Lean's linter checks them: a rewrite
lands on the stated form already when the statement keeps the `… ++ E ++ [x]`
shape (the general-bottom rules), and needs a `rfl` when the statement is a flat
literal list (the fixed-depth rules and the `descWord` splits).

Bean qou-auq3.
"""
from __future__ import annotations
import importlib.util, sys
from pathlib import Path
import sympy as sp

HERE = Path(__file__).resolve().parent.parent / "computations"
sys.path.insert(0, str(HERE)); sys.path.insert(0, str(HERE / "substrate"))
_spec = importlib.util.spec_from_file_location("eng", HERE / "hecke_gs_confluence_n4.py")
eng = importlib.util.module_from_spec(_spec); _spec.loader.exec_module(eng)


def retune(n):
    eng.N = n
    eng.RULES = eng.build_rules()
    eng.LM = {name: lm for name, _, lm in eng.RULES}
    eng.REL = {name: rel for name, rel, _ in eng.RULES}
    eng.LC = {name: eng.REL[name][eng.LM[name]] for name in eng.LM}


# ------------------------------------------------------------------ tracing

def tokenise(w, i, a, b):
    """Relative word -> tokens over 0..b+1 and 'E'.

    `E` stands for `descWord i_{b+1} j`, so a letter `b+1` followed by the
    grown part of the run becomes the single token 'E'.
    """
    r = [i - x for x in w]
    block = list(range(b + 2, a + 1))
    out, k = [], 0
    while k < len(r):
        if r[k] == b + 1 and r[k + 1:k + 1 + len(block)] == block:
            out.append("E"); k += 1 + len(block)
        else:
            assert r[k] <= b + 1, f"stray deep letter {r[k]} in {r}"
            out.append(r[k]); k += 1
    return tuple(out)


def parse_rule(name, i, a, b):
    """Engine rule name -> a structured description in relative indices."""
    k = name[0]
    nums = [int(c) for c in name[1:]]
    if k == "B":
        p, q, m = (i - nums[0], i - nums[1], i - nums[2])
        return ("BSJ", q) if m == a else ("BSF", p, q, m)
    if k == "F":
        return ("F", i - nums[0], i - nums[1])
    raise AssertionError(f"unexpected rule {name} in the a > b regime")


def trace(b):
    """Drive the two-term reduction directly.

    The engine's own driver works on a dict and `clean`s zero coefficients, so
    the final stage — where the two words become equal and cancel — vanishes
    from it. Every rule reachable in the `a > b` regime is monic with exactly
    two words, so a step is just "replace the redex word by the rule's other
    word", and the pair can be carried explicitly to the end.
    """
    a = b + 2
    n, i = a + 4, a + 1
    retune(n)
    j1, j2 = i - a, i - b
    d1, e2 = eng.desc_word(i, j1), eng.desc_word(i - 1, j2)
    n1, n2 = f"B{i-1}{i}{j1}", f"B{i-1}{i}{j2}"
    spoly = eng.clean(eng.combine(
        {w: eng.LC[n2] * c
         for w, c in eng.context_mul((), eng.REL[n1], e2 + (i,)).items()},
        {w: eng.LC[n1] * c
         for w, c in eng.context_mul(d1, eng.REL[n2], ()).items()}, -1))
    assert len(spoly) == 2, f"S-polynomial has {len(spoly)} terms"
    cur = {("V" if c == 1 else "U"): w for w, c in spoly.items()}
    assert set(cur) == {"V", "U"}

    stages, steps = [], []
    while True:
        stages.append({k: tokenise(v, i, a, b) for k, v in cur.items()})
        if cur["V"] == cur["U"]:
            return stages, steps
        target = None
        for slot in sorted(cur, key=lambda s: eng.deglex_key(cur[s])):
            for name in eng.LM:
                pos = eng.infix_positions(cur[slot], eng.LM[name])
                if pos:
                    target = (slot, name, pos[0]); break
            if target:
                break
        assert target is not None, "normal form reached without cancelling"
        slot, name, k = target
        rel = eng.REL[name]
        assert eng.LC[name] == 1 and len(rel) == 2, f"rule {name} is not monic 2-word"
        other, = [x for x, c in rel.items() if x != eng.LM[name]]
        assert rel[other] == -1, f"rule {name} has an unexpected second coefficient"
        word = cur[slot]
        left, right = word[:k], word[k + len(eng.LM[name]):]
        steps.append((parse_rule(name, i, a, b),
                      tokenise(left, i, a, b), tokenise(right, i, a, b), slot))
        cur = dict(cur)
        cur[slot] = left + other + right


# ------------------------------------------------------------------ emitting

def gen(k):
    return f"(⟨i{chr(0x2080 + k)}⟩ : HeckeGen n)"


def var(k):
    return f"i{chr(0x2080 + k)}"


def lst(ts):
    return "[" + ", ".join(gen(t) for t in ts) + "]"


def toks(ts):
    """Token tuple (letters and 'E') as a Lean Monomial expression."""
    if not ts:
        return "[]"
    parts, run = [], []
    for t in ts:
        if t == "E":
            if run:
                parts.append(lst(run)); run = []
            parts.append(EXPR_E)
        else:
            run.append(t)
    if run:
        parts.append(lst(run))
    return " ++ ".join(parts)


def emit(b):
    stages, steps = trace(b)
    global EXPR_E
    EXPR_E = f"descWord {var(b + 1)} j"
    NG = b + 2                                   # named generators i₀ .. i_{b+1}
    IDX = " ".join(var(k) for k in range(NG)) + " j"
    HY = "".join(f"(h{chr(0x2080 + k)} : {var(k)}.val + 1 = {var(k-1)}.val) "
                 for k in range(1, NG)) + f"(hj : j.val ≤ {var(b + 1)}.val)"
    ARGS = " ".join(f"h{chr(0x2080 + k)}" for k in range(1, NG)) + " hj"
    HARGS = " ".join(f"h{chr(0x2080 + k)}" for k in range(1, NG))

    # name every distinct word
    names, order = {}, []
    for st in stages:
        for slot in ("V", "U"):
            if st[slot] not in names:
                names[st[slot]] = f"{slot}{sum(1 for x in order if x[0] == slot)}"
                order.append((slot, st[slot]))
    o = []
    w = o.append

    w(f"namespace BokutShiaoCornerDepth{b}")
    w("")
    w("variable {n : ℕ}")
    w("")
    w("section")
    w("")
    w(f"variable {{{' '.join(var(k) for k in range(NG))} j : Fin n}}")
    w("")

    # pairwise distinctness of the named generators
    pairs = [(p, q) for p in range(NG) for q in range(NG) if p < q]
    w(f"/-- The {NG} generators in play are pairwise distinct. -/")
    w(f"theorem gen_ne {HY.rsplit('(hj', 1)[0].strip()} :")
    body = "\n      ∧ ".join(f"{gen(p)} ≠ {gen(q)}" for p, q in pairs)
    w(f"    {body} := by")
    w("  refine ⟨" + ", ".join("?_" for _ in pairs) + "⟩ <;>")
    w("    · intro hcon")
    w("      have := congrArg HeckeGen.rank hcon")
    w("      simp only [HeckeGen.rank] at this")
    w("      omega")
    w("")

    # descWord down to j, with the explicit head split off.  Each takes only the
    # step hypotheses at or below its own index, so nothing is left unused.
    def dwhy(k):
        return " ".join(
            f"(h{chr(0x2080 + t)} : {var(t)}.val + 1 = {var(t-1)}.val)"
            for t in range(k + 1, b + 2)) + f" (hj : j.val ≤ {var(b + 1)}.val)"

    def dwargs(k):
        return (" ".join(f"h{chr(0x2080 + t)}" for t in range(k + 1, b + 2))
                + " hj").strip()

    for k in range(b, -1, -1):
        w(f"/-- The run from `{var(k)}` with its explicit head split off. -/")
        w(f"theorem dw{k} {dwhy(k)} :")
        w(f"    descWord {var(k)} j = {lst(list(range(k, b + 1)))} ++ {EXPR_E} := by")
        if k == b:
            w(f"  rw [descWord_cons h{chr(0x2080 + b + 1)} hj]")
            w("  rfl")
        else:
            w(f"  rw [descWord_cons h{chr(0x2080 + k + 1)} (by omega), "
              f"dw{k+1} {dwargs(k + 1)}]")
            w("  rfl")
        w("")

    # descWord between two named generators
    lits = set()
    for m in (b, b + 1):
        for k in range(m, -1, -1):
            lits.add((k, m))
    for (k, m) in sorted(lits, key=lambda t: (t[1], -t[0])):
        w(f"theorem dwLit{k}_{m} {HARGS.replace('h', '(h').replace(' ', ' ')} :")
        o.pop()
        hyp = " ".join(f"(h{chr(0x2080 + t)} : {var(t)}.val + 1 = {var(t-1)}.val)"
                       for t in range(k + 1, m + 1))
        w(f"theorem dwLit{k}_{m}" + (f" {hyp}" if hyp else "") + " :")
        w(f"    descWord {var(k)} {var(m)} = {lst(list(range(k, m + 1)))} := by")
        if k == m:
            w(f"  rw [descWord_self]")
        else:
            args = " ".join(f"h{chr(0x2080 + t)}" for t in range(k + 2, m + 1))
            ref = f"dwLit{k+1}_{m}" + (f" {args}" if args else "")
            w(f"  rw [descWord_cons h{chr(0x2080 + k + 1)} (by omega), {ref}]")
        w("")

    # the rules
    used = {}
    for (rule, _, _, _) in steps:
        used[rule] = None
    OC2 = ("BSF", 1, 0, b)                       # the composition's second rule
    used[OC2] = None

    def rule_term(r):
        if r[0] == "BSJ":
            q = r[1]
            return f"(bokutShiaoRelation {var(q + 1)} {var(q)} j)"
        if r[0] == "BSF":
            _, p, q, m = r
            return f"(bokutShiaoRelation {var(p)} {var(q)} {var(m)})"
        _, p, q = r
        return f"(farCommRelation {var(p)} {var(q)})"

    def rule_words(r):
        if r[0] == "BSJ":
            q = r[1]
            L = list(range(q, b + 1)) + ["E"] + [q]
            R = [q + 1, q] + list(range(q + 1, b + 1)) + ["E"]
            return L, R
        if r[0] == "BSF":
            _, p, q, m = r
            return (list(range(q, m + 1)) + [q], [p, q] + list(range(p, m + 1)))
        _, p, q = r
        return ([p, q], [q, p])

    def bsf_args(p, m):
        return " ".join(f"h{chr(0x2080 + t)}" for t in range(p, m + 1))

    def rule_name(r):
        if r[0] == "BSJ":
            return f"bsJ{r[1]}"
        if r[0] == "BSF":
            return f"bsF{r[1]}_{r[2]}_{r[3]}"
        return f"far{r[1]}_{r[2]}"

    for r in used:
        nm, (L, R) = rule_name(r), rule_words(r)
        if r[0] == "F":
            continue                             # far_hrel / farCommRelation_lm serve
        if r[0] == "BSJ":
            q = r[1]
            hyp, args = dwhy(q), dwargs(q)
            rws = [f"dw{q} {dwargs(q)}"] + ([f"dw{q+1} {dwargs(q+1)}"] if q + 1 <= b else [])
            lmh = (f"bokutShiaoRelation_lm h{chr(0x2080 + q + 1)} (by omega)")
            w1, w2 = f"bsWord₁ {var(q)} j", f"bsWord₂ {var(q + 1)} {var(q)} j"
            lmrw = [f"dw{q} {dwargs(q)}"]
        else:
            _, p, q, m = r
            hyp = " ".join(
                f"(h{chr(0x2080 + t)} : {var(t)}.val + 1 = {var(t-1)}.val)"
                for t in range(p, m + 1))
            args = bsf_args(p, m)
            aq = " ".join(f"h{chr(0x2080 + t)}" for t in range(q + 1, m + 1))
            ap = " ".join(f"h{chr(0x2080 + t)}" for t in range(p + 1, m + 1))
            rws = [f"dwLit{q}_{m} {aq}".rstrip(), f"dwLit{p}_{m} {ap}".rstrip()]
            lmh = f"bokutShiaoRelation_lm h{chr(0x2080 + p)} (by omega)"
            w1, w2 = f"bsWord₁ {var(q)} {var(m)}", f"bsWord₂ {var(p)} {var(q)} {var(m)}"
            lmrw = [f"dwLit{q}_{m} {aq}".rstrip()]
        w(f"theorem {nm}_hrel {hyp}")
        w("    (v : Monomial (HeckeGen n)) :")
        w(f"    {rule_term(r)}.relation.coeff v")
        w("      = (AlgElement.ofTerms")
        w(f"          [({toks(L)}, (1 : ℝ)),")
        w(f"           ({toks(R)}, -1)]).coeff v := by")
        w("  show (AlgElement.ofTerms")
        w(f"    [({w1}, (1 : ℝ)), ({w2}, -1)]).coeff v = _")
        w(f"  rw [bsWord₁, {rws[0]}, bsWord₂" + (f", {rws[1]}" if len(rws) > 1 else "")
          + "]")
        w("  rfl")
        w("")
        w(f"theorem {nm}_hlm {hyp} :")
        w(f"    {rule_term(r)}.lm (heckeOrder n)")
        w(f"      = {toks(L)} := by")
        w(f"  rw [{lmh}, bsWord₁, {lmrw[0]}]")
        if r[0] == "BSF":
            w("  rfl")
        w("")

    w("end")
    w("")

    for slot, tks in order:
        w(f"def {names[tks]} ({IDX} : Fin n) : Monomial (HeckeGen n) := {toks(tks)}")
    w("")
    for k, st in enumerate(stages):
        w(f"noncomputable def T{k} ({IDX} : Fin n) : AlgElement (HeckeGen n) ℝ :=")
        w(f"  AlgElement.ofTerms [({names[st['V']]} {IDX}, (1 : ℝ)), "
          f"({names[st['U']]} {IDX}, -1)]")
        w("")

    w("section")
    w("")
    w(f"variable (hp : HeckeParams) {{{' '.join(var(k) for k in range(NG))} j : Fin n}}")
    w("")

    def mem_and_lemmas(r):
        if r[0] == "F":
            p, q = r[1], r[2]
            return ("(farCommRelation_mem hn hp (by omega))",
                    f"(BokutShiaoBraid.far_hrel {var(q)} {var(p)})",
                    f"(farCommRelation_lm {var(p)} {var(q)} (by omega))")
        nm = rule_name(r)
        if r[0] == "BSJ":
            q = r[1]
            return (f"(bokutShiaoRelation_mem hn hp h{chr(0x2080 + q + 1)} (by omega))",
                    f"({nm}_hrel {dwargs(q)})", f"({nm}_hlm {dwargs(q)})")
        _, p, q, m = r
        return (f"(bokutShiaoRelation_mem hn hp h{chr(0x2080 + p)} (by omega))",
                f"({nm}_hrel {bsf_args(p, m)})", f"({nm}_hlm {bsf_args(p, m)})")

    for k, (r, lc, rc, slot) in enumerate(steps, start=1):
        prev, nxt = stages[k - 1], stages[k]
        src, dst = names[prev[slot]], names[nxt[slot]]
        other = names[prev["U" if slot == "V" else "V"]]
        if slot == "V":
            L1, L2 = "[]", f"[({other} {IDX}, -1)]"
            c, hc = "1", "one_ne_zero"
        else:
            L1, L2 = f"[({other} {IDX}, (1 : ℝ))]", "[]"
            c, hc = "(-1)", "(neg_ne_zero.mpr one_ne_zero)"
        mem, hrel, hlm = mem_and_lemmas(r)
        depthless = r[0] != "BSJ"
        hy = HY.replace("(hj :", "(_hj :") if depthless else HY
        w(f"theorem s{k} (hn : 0 < n) {hy} :")
        w("    SingleStepReduction (heckeOrder n) (heckeCompletedRewritingSystem n hn hp)")
        w(f"      (T{k-1} {IDX}) (T{k} {IDX}) := by")
        w(f"  obtain ⟨" + ", ".join(f"g{p}{q}" for p, q in pairs)
          + f"⟩ := gen_ne {HARGS}")
        for p, q in pairs:
            w(f"  have g{q}{p} := g{p}{q}.symm")
        w(f"  exact monicStep hn hp {rule_term(r)} {mem}")
        w(f"    {hrel} {hlm}")
        w("    (by simp [*])")
        w(f"    {L1} {L2}")
        w(f"    ({toks(lc)}) ({toks(rc)}) _ _ {c} {hc}")
        w(f"    (by simp [{src}]) (by simp [{dst}])")
        w(f"    (by simp [{src}, {other}, *])")
        w("")

    w("end")
    w("")
    last = len(stages) - 1
    w(f"theorem T{last}_isZero ({IDX} : Fin n) : (T{last} {IDX}).isZero := by")
    w("  intro m")
    w(f"  simp only [T{last}, {names[stages[-1]['V']]}, {names[stages[-1]['U']]},")
    w("    AlgElement.ofTerms_coeff, List.filter_cons, List.filter_nil,")
    w("    decide_eq_true_eq]")
    w("  split_ifs <;>")
    w("    simp only [List.map_cons, List.map_nil, List.sum_cons, List.sum_nil]")
    w("  ring")
    w("")

    oc2nm = rule_name(OC2)
    right = list(range(1, b + 1)) + [0]
    w("/-- The composition of the rule at the general depth `j` with the rule at")
    w(f"depth `{b}`, overlapping in the trailing `σᵢ`. -/")
    w(f"noncomputable def oc ({IDX} : Fin n) {HY} :")
    w("    OverlapComposition (HeckeGen n) ℝ (heckeOrder n) where")
    w(f"  rule₁ := bokutShiaoRelation {var(1)} {var(0)} j")
    w(f"  rule₂ := bokutShiaoRelation {var(1)} {var(0)} {var(b)}")
    w(f"  left := {toks(tuple(list(range(0, b + 1)) + ['E']))}")
    w(f"  overlap := [{gen(0)}]")
    w(f"  right := {lst(right)}")
    w(f"  lm₁_decomp := by rw [bsJ0_hlm {dwargs(0)}]")
    w(f"  lm₂_decomp := by rw [{oc2nm}_hlm {bsf_args(1, b)}]; rfl")
    w("  overlap_nonempty := by simp")
    w("")
    w("/-- **The S-polynomial.** -/")
    w(f"theorem oc_spoly_coeff {{{IDX} : Fin n}} {HY}")
    w("    (m : Monomial (HeckeGen n)) :")
    w(f"    (oc {IDX} {ARGS}).spoly.coeff m = (T0 {IDX}).coeff m := by")
    w(f"  show (bokutShiaoRelation {var(1)} {var(0)} {var(b)}).lc (heckeOrder n)")
    w(f"      * (AlgElement.contextMul [] (bokutShiaoRelation {var(1)} {var(0)} j).relation")
    w(f"          {lst(right)}).coeff m")
    w(f"    - (bokutShiaoRelation {var(1)} {var(0)} j).lc (heckeOrder n)")
    w(f"      * (AlgElement.contextMul ({toks(tuple(list(range(0, b + 1)) + ['E']))})")
    w(f"          (bokutShiaoRelation {var(1)} {var(0)} {var(b)}).relation []).coeff m")
    w("    = _")
    w(f"  rw [bokutShiaoRelation_lc h{chr(0x2081)} (by omega), "
      f"bokutShiaoRelation_lc h{chr(0x2081)} (by omega),")
    w("    one_mul, one_mul,")
    w(f"    AlgElement.contextMul_coeff_congr [] {lst(right)}")
    w(f"      (bsJ0_hrel {dwargs(0)}) m,")
    w(f"    AlgElement.contextMul_coeff_congr ({toks(tuple(list(range(0, b + 1)) + ['E']))}) []")
    w(f"      ({oc2nm}_hrel {bsf_args(1, b)}) m]")
    w(f"  simp only [T0, {names[stages[0]['V']]}, {names[stages[0]['U']]},")
    w("    AlgElement.contextMul_ofTerms_coeff, List.map_cons,")
    w("    List.map_nil, List.nil_append, List.append_nil, List.cons_append,")
    w("    List.append_assoc, AlgElement.ofTerms_coeff, List.filter_cons,")
    w("    List.filter_nil, decide_eq_true_eq]")
    w("  split_ifs <;>")
    w("    simp only [List.map_cons, List.map_nil, List.sum_cons, List.sum_nil] <;> ring")
    w("")
    w(f"/-- **{len(steps)} steps, to zero, at every depth `j ≤ i − {b + 1}`.** -/")
    w(f"theorem resolves (hp : HeckeParams) {{{IDX} : Fin n}} (hn : 0 < n)")
    w(f"    {HY} :")
    w("    ∃ nf, ReducesToNF (heckeOrder n) (heckeCompletedRewritingSystem n hn hp)")
    w(f"      (oc {IDX} {ARGS}).spoly nf ∧ nf.isZero := by")
    w(f"  refine reducesToZero_congr ⟨T{last} {IDX},")
    w(f"    ⟨(MultiStepReduction.refl (T0 {IDX}))")
    for k in range(1, len(steps) + 1):
        w(f"      |>.step (s{k} hp hn {ARGS})")
    o[-1] = o[-1] + ","
    w(f"      isNormalForm_of_isZero (T{last}_isZero {IDX})⟩, T{last}_isZero {IDX}⟩ ?_")
    w("  intro m")
    w(f"  exact oc_spoly_coeff {ARGS} m")
    w("")
    w(f"end BokutShiaoCornerDepth{b}")
    return "\n".join(o), len(steps), len(order)


if __name__ == "__main__":
    text, nsteps, nwords = emit(int(sys.argv[1]))
    print(text)
    print(f"\n-- {nsteps} steps, {nwords} words", file=sys.stderr)
